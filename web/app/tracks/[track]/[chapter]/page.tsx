import Link from "next/link";
import { notFound } from "next/navigation";
import Progress from "../../../../components/Progress";
import { getAllExercises, getChapters, getExercises } from "../../../../lib/exercises";

export function generateStaticParams() {
  const seen = new Set<string>();
  return getAllExercises()
    .filter((e) => {
      const k = `${e.track}/${e.chapterDir}`;
      if (seen.has(k)) return false;
      seen.add(k);
      return true;
    })
    .map((e) => ({ track: e.track, chapter: e.chapterDir }));
}

const TYPE_COLOR: Record<string, string> = {
  creation: "text-accent",
  modification: "text-ok",
  debugging: "text-fail",
};

export default async function ChapterPage({
  params,
}: {
  params: Promise<{ track: string; chapter: string }>;
}) {
  const { track, chapter } = await params;
  const exos = getExercises(track, chapter);
  if (exos.length === 0) notFound();
  const ch = getChapters(track).find((c) => c.chapterDir === chapter);

  return (
    <main className="mx-auto max-w-3xl px-6 py-12">
      <Link href={`/tracks/${track}`} className="text-sm text-muted hover:text-foreground">
        ← {track}
      </Link>
      <div className="mt-2 flex items-center justify-between">
        <h1 className="text-2xl font-semibold">
          Ch. {ch?.number} — {ch?.title}
        </h1>
        <Progress ids={exos.map((e) => e.id)} />
      </div>

      <ul className="mt-8 space-y-1.5">
        {exos.map((e) => (
          <li key={e.id}>
            <Link href={`/tracks/${track}/${chapter}/${e.dir}`}>
              <div className="flex items-center gap-3 rounded-md border border-border bg-surface px-4 py-2.5 hover:border-accent">
                <span className={`w-24 text-xs font-mono ${TYPE_COLOR[e.type]}`}>{e.type}</span>
                <span className="flex-1 text-sm">{e.title}</span>
                <span className="text-xs text-muted">diff {e.difficulty}/5</span>
                <span className="text-xs text-muted">{e.theme}</span>
              </div>
            </Link>
          </li>
        ))}
      </ul>
    </main>
  );
}
