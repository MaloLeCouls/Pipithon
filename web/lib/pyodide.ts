// Exécution Python côté client via Pyodide (CPython WASM). Zéro backend.
// Pyodide + pytest sont chargés une seule fois et réutilisés (cf. INIT §1).
"use client";

import { PYMISTRAL_BUNDLE } from "./_pymistral-bundle";

const PYODIDE_VERSION = "0.29.4";
const CDN = `https://cdn.jsdelivr.net/pyodide/v${PYODIDE_VERSION}/full/`;

// biome-ignore lint/suspicious/noExplicitAny: l'API Pyodide n'est pas typée ici
type Pyodide = any;

let pyodidePromise: Promise<Pyodide> | null = null;

declare global {
  interface Window {
    loadPyodide?: (opts: { indexURL: string }) => Promise<Pyodide>;
  }
}

function injectScript(src: string): Promise<void> {
  return new Promise((resolve, reject) => {
    if (document.querySelector(`script[src="${src}"]`)) return resolve();
    const s = document.createElement("script");
    s.src = src;
    s.onload = () => resolve();
    s.onerror = () => reject(new Error(`Échec chargement ${src}`));
    document.head.appendChild(s);
  });
}

// Écrit le paquet pymistral/ dans la FS Pyodide sous /exo/pymistral/.
// Fait une seule fois à l'init : le framework est statique entre exos.
function writePymistralBundle(py: Pyodide): void {
  py.FS.mkdirTree("/exo/pymistral");
  for (const [rel, src] of Object.entries(PYMISTRAL_BUNDLE)) {
    const path = `/exo/pymistral/${rel}`;
    const dir = path.substring(0, path.lastIndexOf("/"));
    py.FS.mkdirTree(dir);
    py.FS.writeFile(path, src);
  }
}

export type LoadPhase = "idle" | "pyodide" | "pytest" | "ready" | "error";

export function getPyodide(onPhase?: (p: LoadPhase) => void): Promise<Pyodide> {
  if (pyodidePromise) return pyodidePromise;
  pyodidePromise = (async () => {
    onPhase?.("pyodide");
    await injectScript(`${CDN}pyodide.js`);
    if (!window.loadPyodide) throw new Error("loadPyodide indisponible");
    const py = await window.loadPyodide({ indexURL: CDN });
    onPhase?.("pytest");
    await py.loadPackage("micropip");
    const micropip = py.pyimport("micropip");
    await micropip.install("pytest");
    py.FS.mkdirTree("/exo");
    writePymistralBundle(py);
    onPhase?.("ready");
    return py;
  })();
  return pyodidePromise;
}

export interface TestResult {
  name: string;
  outcome: "passed" | "failed" | "error" | "skipped";
  message: string;
}

export interface RunReport {
  ok: boolean;
  tests: TestResult[];
  stdout: string;
}

// Harnais pytest : un plugin collector capture le résultat par test.
const PYTEST_HARNESS = `
import json, sys, io, contextlib

for _m in ("solution_user", "tests"):
    sys.modules.pop(_m, None)
if "/exo" not in sys.path:
    sys.path.insert(0, "/exo")

import pytest

class _Collector:
    def __init__(self):
        self.reports = {}
    def pytest_runtest_logreport(self, report):
        nid = report.nodeid
        if report.when == "call":
            self.reports[nid] = report
        elif report.outcome == "failed" and nid not in self.reports:
            self.reports[nid] = report  # erreur en setup

_c = _Collector()
_buf = io.StringIO()
with contextlib.redirect_stdout(_buf), contextlib.redirect_stderr(_buf):
    _code = pytest.main(
        ["-q", "-p", "no:cacheprovider", "--no-header", "/exo/tests.py"],
        plugins=[_c],
    )

def _short(r):
    if r.outcome == "passed":
        return ""
    txt = r.longreprtext if hasattr(r, "longreprtext") else str(r.longrepr)
    return txt[-1600:]

_tests = [
    {
        "name": nid.split("::")[-1],
        "outcome": r.outcome,
        "message": _short(r),
    }
    for nid, r in _c.reports.items()
]
json.dumps({
    "ok": int(_code) == 0 and len(_tests) > 0,
    "tests": _tests,
    "stdout": _buf.getvalue()[-4000:],
})
`;

export async function runTests(userCode: string, testsCode: string): Promise<RunReport> {
  const py = await getPyodide();
  py.FS.mkdirTree("/exo");
  py.FS.writeFile("/exo/solution_user.py", userCode);
  py.FS.writeFile("/exo/tests.py", testsCode);
  const raw: string = await py.runPythonAsync(PYTEST_HARNESS);
  return JSON.parse(raw) as RunReport;
}

// "Run" : exécute le code utilisateur, renvoie stdout/stderr (pas les tests).
const RUN_HARNESS = `
import sys, io, contextlib, traceback
_buf = io.StringIO()
with contextlib.redirect_stdout(_buf), contextlib.redirect_stderr(_buf):
    try:
        exec(compile(_USER_SRC, "<solution_user>", "exec"), {"__name__": "__main__"})
    except Exception:
        traceback.print_exc()
_buf.getvalue()
`;

export async function runCode(userCode: string): Promise<string> {
  const py = await getPyodide();
  py.globals.set("_USER_SRC", userCode);
  try {
    const out: string = await py.runPythonAsync(RUN_HARNESS);
    return out || "(aucune sortie — ton code ne print rien)";
  } finally {
    py.globals.delete("_USER_SRC");
  }
}
