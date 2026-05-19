import Link from "next/link";
import { notFound } from "next/navigation";
import Progress from "../../../components/Progress";
import { getChapters, getExercises, listTracks } from "../../../lib/exercises";

export function generateStaticParams() {
  return listTracks()
    .filter((t) => t.status === "active")
    .map((t) => ({ track: t.slug }));
}

export default async function TrackPage({ params }: { params: Promise<{ track: string }> }) {
  const { track } = await params;
  const chapters = getChapters(track);
  if (chapters.length === 0) notFound();

  return (
    <main className="mx-auto max-w-3xl px-6 py-12">
      <Link href="/" className="text-sm text-muted hover:text-foreground">
        ← tracks
      </Link>
      <h1 className="mt-2 text-2xl font-semibold">{track}</h1>
      <p className="mt-1 text-sm text-muted">{chapters.length} chapitres avec des exercices.</p>

      <ul className="mt-8 space-y-2">
        {chapters.map((c) => {
          const ids = getExercises(track, c.chapterDir).map((e) => e.id);
          return (
            <li key={c.chapterDir}>
              <Link href={`/tracks/${track}/${c.chapterDir}`}>
                <div className="flex items-center justify-between rounded-md border border-border bg-surface px-4 py-3 hover:border-accent">
                  <div>
                    <div className="font-medium">
                      Ch. {c.number} — {c.title}
                    </div>
                    <div className="text-xs text-muted">
                      tier {c.tier} · {c.status} · {c.count} exos
                    </div>
                  </div>
                  <Progress ids={ids} />
                </div>
              </Link>
            </li>
          );
        })}
      </ul>
    </main>
  );
}
