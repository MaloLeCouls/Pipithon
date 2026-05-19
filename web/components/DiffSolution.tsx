"use client";

// Diff côte-à-côte minimal (pas de dépendance externe) : on aligne ligne à
// ligne et on surligne ce qui diffère. Suffisant pour comparer sa solution
// à la référence idiomatique.
export default function DiffSolution({ user, solution }: { user: string; solution: string }) {
  const a = user.replace(/\s+$/, "").split("\n");
  const b = solution.replace(/\s+$/, "").split("\n");
  const n = Math.max(a.length, b.length);
  const rows = Array.from({ length: n }, (_, i) => {
    const l = a[i] ?? "";
    const r = b[i] ?? "";
    return { l, r, diff: l.trim() !== r.trim() };
  });
  return (
    <div className="grid grid-cols-2 gap-px overflow-hidden rounded-md border border-border bg-border font-mono text-xs">
      <div className="bg-surface-2 px-3 py-1 text-muted">Ta solution</div>
      <div className="bg-surface-2 px-3 py-1 text-muted">Référence idiomatique</div>
      {rows.map((row, i) => (
        // biome-ignore lint/suspicious/noArrayIndexKey: un diff est positionnel par nature (rendu statique, pas de réordonnancement)
        <Pair key={i} {...row} />
      ))}
    </div>
  );
}

function Pair({ l, r, diff }: { l: string; r: string; diff: boolean }) {
  const cell = "overflow-x-auto whitespace-pre px-3 py-0.5";
  return (
    <>
      <div className={`${cell} bg-surface ${diff ? "text-fail/90" : "text-foreground/70"}`}>
        {l || " "}
      </div>
      <div className={`${cell} bg-surface ${diff ? "text-ok" : "text-foreground/70"}`}>
        {r || " "}
      </div>
    </>
  );
}
