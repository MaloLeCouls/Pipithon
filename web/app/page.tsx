import Link from "next/link";
import { listTracks } from "../lib/exercises";

export default function Home() {
  const tracks = listTracks();
  return (
    <main className="mx-auto max-w-3xl px-6 py-12">
      <h1 className="text-2xl font-semibold">pipithon</h1>
      <p className="mt-1 text-sm text-muted">
        Dojo de Python idiomatique — cap ML Inference Engineer. Drill par répétition, tests pytest
        dans le navigateur (Pyodide).
      </p>

      <h2 className="mt-10 mb-3 text-sm font-medium text-muted uppercase tracking-wide">Tracks</h2>
      <ul className="space-y-2">
        {tracks.map((t) => {
          const inner = (
            <div
              className={`flex items-center justify-between rounded-md border border-border bg-surface px-4 py-3 ${
                t.status === "active" ? "hover:border-accent" : "opacity-45"
              }`}
            >
              <div>
                <div className="font-medium">{t.label}</div>
                <div className="text-xs text-muted">
                  {t.status === "active" ? `${t.exerciseCount} exercices` : "verrouillé"}
                </div>
              </div>
              <span className="text-xs text-muted">{t.status === "active" ? "→" : "🔒"}</span>
            </div>
          );
          return (
            <li key={t.slug}>
              {t.status === "active" ? <Link href={`/tracks/${t.slug}`}>{inner}</Link> : inner}
            </li>
          );
        })}
      </ul>
    </main>
  );
}
