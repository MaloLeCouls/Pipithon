"use client";

import Link from "next/link";
import { useCallback, useEffect, useState } from "react";
import type { Exercise } from "../lib/exercises";
import { clearDraft, isCompleted, loadDraft, markCompleted, saveDraft } from "../lib/progress";
import { getPyodide, type LoadPhase, type RunReport, runCode, runTests } from "../lib/pyodide";
import DiffSolution from "./DiffSolution";
import HintsPanel from "./HintsPanel";
import MonacoEditor from "./MonacoEditor";
import TestResults from "./TestResults";

const PHASE_LABEL: Record<LoadPhase, string> = {
  idle: "",
  pyodide: "Chargement de Python (Pyodide)…",
  pytest: "Installation de pytest…",
  ready: "Prêt",
  error: "Erreur de chargement",
};

export default function ExerciseWorkbench({ exo }: { exo: Exercise }) {
  const [code, setCode] = useState(exo.files.starter);
  const [phase, setPhase] = useState<LoadPhase>("idle");
  const [busy, setBusy] = useState(false);
  const [runOut, setRunOut] = useState<string | null>(null);
  const [report, setReport] = useState<RunReport | null>(null);
  const [fails, setFails] = useState(0);
  const [done, setDone] = useState(false);
  const [showSol, setShowSol] = useState(false);

  // Hydratation : brouillon localStorage > starter ; statut complété.
  useEffect(() => {
    const draft = loadDraft(exo.id);
    if (draft != null) setCode(draft);
    setDone(isCompleted(exo.id));
  }, [exo.id]);

  // Préchauffe Pyodide en arrière-plan dès l'ouverture de l'exo.
  useEffect(() => {
    getPyodide(setPhase).catch(() => setPhase("error"));
  }, []);

  const onChange = useCallback(
    (v: string) => {
      setCode(v);
      saveDraft(exo.id, v);
    },
    [exo.id],
  );

  const doRun = async () => {
    setBusy(true);
    setReport(null);
    try {
      setRunOut(await runCode(code));
    } catch (e) {
      setRunOut(String(e));
    } finally {
      setBusy(false);
    }
  };

  const doSubmit = async () => {
    setBusy(true);
    setRunOut(null);
    try {
      const r = await runTests(code, exo.files.tests);
      setReport(r);
      if (r.ok) {
        markCompleted(exo.id);
        setDone(true);
      } else {
        setFails((f) => f + 1);
      }
    } catch (e) {
      setReport({
        ok: false,
        tests: [],
        stdout: String(e),
      });
    } finally {
      setBusy(false);
    }
  };

  const resetStarter = () => {
    setCode(exo.files.starter);
    clearDraft(exo.id);
    setReport(null);
    setRunOut(null);
  };

  const canSeeSolution = done || fails >= 3;
  const ready = phase === "ready";

  return (
    <div className="flex h-screen flex-col">
      {/* Header */}
      <header className="flex items-center gap-3 border-b border-border bg-surface px-4 py-2 text-sm">
        <Link
          href={`/tracks/${exo.track}/${exo.chapterDir}`}
          className="text-muted hover:text-foreground"
        >
          ← {exo.chapterDir}
        </Link>
        <span className="font-medium">{exo.title}</span>
        <Badge>{exo.type}</Badge>
        <Badge>diff {exo.difficulty}/5</Badge>
        <Badge>{exo.theme}</Badge>
        <span className="text-muted">{exo.concepts.join(" · ")}</span>
        {done && <span className="ml-auto text-ok">✓ complété</span>}
        {!done && <span className="ml-auto text-muted">{PHASE_LABEL[phase]}</span>}
      </header>

      <div className="grid flex-1 grid-cols-2 overflow-hidden">
        {/* Panneau gauche : énoncé + indices + (solution) */}
        <section className="overflow-y-auto border-r border-border p-5 space-y-4">
          <div>
            <h1 className="mb-1 text-lg font-semibold">{exo.title}</h1>
            <p className="text-sm text-muted">{exo.short_description}</p>
          </div>
          <pre className="whitespace-pre-wrap rounded-md border border-border bg-surface-2 p-3 font-mono text-xs leading-relaxed">
            {docstring(exo.files.starter)}
          </pre>
          <HintsPanel hints={exo.hints} />

          <div className="rounded-md border border-border bg-surface-2 p-3">
            <div className="flex items-center justify-between">
              <span className="text-sm font-medium text-muted">Solution référence</span>
              <button
                type="button"
                disabled={!canSeeSolution}
                onClick={() => setShowSol((s) => !s)}
                className="rounded border border-border px-2 py-1 text-xs enabled:hover:border-accent disabled:opacity-40"
                title={canSeeSolution ? "" : "Disponible après réussite ou 3 tentatives échouées"}
              >
                {showSol ? "Masquer" : "Voir la solution"}
              </button>
            </div>
            {!canSeeSolution && (
              <p className="mt-2 text-xs text-muted">
                Débloquée quand tu réussis, ou après 3 soumissions échouées (tentatives : {fails}
                /3).
              </p>
            )}
            {showSol && canSeeSolution && (
              <div className="mt-3">
                <DiffSolution user={code} solution={exo.files.solution} />
              </div>
            )}
          </div>
        </section>

        {/* Panneau droit : éditeur + actions + résultats */}
        <section className="flex flex-col overflow-hidden">
          <div className="min-h-0 flex-1">
            <MonacoEditor value={code} onChange={onChange} />
          </div>
          <div className="flex items-center gap-2 border-t border-border bg-surface px-3 py-2">
            <button
              type="button"
              onClick={doRun}
              disabled={busy || !ready}
              className="rounded bg-surface-2 px-3 py-1.5 text-sm enabled:hover:bg-border disabled:opacity-40"
            >
              ▶ Run
            </button>
            <button
              type="button"
              onClick={doSubmit}
              disabled={busy || !ready}
              className="rounded bg-accent px-3 py-1.5 text-sm font-medium text-background enabled:hover:opacity-90 disabled:opacity-40"
            >
              ✓ Submit
            </button>
            <button
              type="button"
              onClick={resetStarter}
              disabled={busy}
              className="ml-auto rounded border border-border px-2 py-1.5 text-xs text-muted hover:text-foreground"
            >
              Reset starter
            </button>
          </div>
          <div className="h-2/5 overflow-y-auto border-t border-border bg-background p-3">
            {busy && <p className="text-sm text-muted">Exécution…</p>}
            {!busy && report && <TestResults report={report} />}
            {!busy && runOut != null && (
              <pre className="overflow-x-auto whitespace-pre-wrap font-mono text-xs text-foreground/90">
                {runOut}
              </pre>
            )}
            {!busy && !report && runOut == null && (
              <p className="text-sm text-muted">
                <strong>Run</strong> exécute ton code (stdout). <strong>Submit</strong> lance
                pytest.
              </p>
            )}
          </div>
        </section>
      </div>
    </div>
  );
}

function Badge({ children }: { children: React.ReactNode }) {
  return (
    <span className="rounded border border-border bg-surface-2 px-1.5 py-0.5 text-xs text-muted">
      {children}
    </span>
  );
}

// Extrait le docstring de module du starter pour l'afficher comme énoncé.
function docstring(src: string): string {
  const m = src.match(/^\s*(?:"""|''')([\s\S]*?)(?:"""|''')/);
  return m ? m[1].trim() : src;
}
