"use client";

import { useState } from "react";

export default function HintsPanel({ hints }: { hints: string[] }) {
  const [shown, setShown] = useState(0);
  if (hints.length === 0) return null;
  return (
    <div className="rounded-md border border-border bg-surface-2 p-3">
      <div className="mb-2 flex items-center justify-between">
        <span className="text-sm font-medium text-muted">
          Indices ({shown}/{hints.length})
        </span>
        {shown < hints.length && (
          <button
            type="button"
            onClick={() => setShown((s) => s + 1)}
            className="rounded border border-border px-2 py-1 text-xs hover:border-accent"
          >
            Révéler un indice
          </button>
        )}
      </div>
      <ol className="space-y-2">
        {hints.slice(0, shown).map((h, i) => (
          <li key={h} className="text-sm text-foreground/90">
            <span className="mr-2 text-accent">{i + 1}.</span>
            {h}
          </li>
        ))}
      </ol>
      {shown === 0 && (
        <p className="text-xs text-muted">
          Un indice guide ta pensée, il ne donne pas la solution.
        </p>
      )}
    </div>
  );
}
