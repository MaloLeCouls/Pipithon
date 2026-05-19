"use client";

import { useState } from "react";
import type { RunReport, TestResult } from "../lib/pyodide";

function Row({ t }: { t: TestResult }) {
  const [open, setOpen] = useState(false);
  const passed = t.outcome === "passed";
  return (
    <div className="border-b border-border last:border-0">
      <button
        type="button"
        onClick={() => !passed && setOpen((o) => !o)}
        className="flex w-full items-center gap-2 px-3 py-2 text-left text-sm"
      >
        <span className={passed ? "text-ok" : "text-fail"}>{passed ? "✓" : "✗"}</span>
        <code className="flex-1 truncate font-mono text-xs">{t.name}</code>
        {!passed && <span className="text-muted text-xs">{open ? "▾" : "▸"}</span>}
      </button>
      {open && !passed && (
        <pre className="overflow-x-auto bg-background px-3 py-2 text-xs text-fail/90 whitespace-pre-wrap">
          {t.message}
        </pre>
      )}
    </div>
  );
}

export default function TestResults({ report }: { report: RunReport }) {
  const passed = report.tests.filter((t) => t.outcome === "passed").length;
  const total = report.tests.length;
  return (
    <div>
      <div className={`px-3 py-2 text-sm font-medium ${report.ok ? "text-ok" : "text-fail"}`}>
        {report.ok ? `Tout vert — ${passed}/${total} ✅` : `${passed}/${total} tests passent`}
      </div>
      <div className="rounded-md border border-border bg-surface-2">
        {report.tests.length === 0 ? (
          <pre className="overflow-x-auto px-3 py-2 text-xs text-fail/90 whitespace-pre-wrap">
            {report.stdout || "Aucun test collecté (erreur d'import ?)."}
          </pre>
        ) : (
          report.tests.map((t) => <Row key={t.name} t={t} />)
        )}
      </div>
    </div>
  );
}
