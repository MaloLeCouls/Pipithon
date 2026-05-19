import { notFound } from "next/navigation";
import ExerciseWorkbench from "../../../../../components/ExerciseWorkbench";
import { getAllExercises, getExercise } from "../../../../../lib/exercises";

export function generateStaticParams() {
  return getAllExercises().map((e) => ({
    track: e.track,
    chapter: e.chapterDir,
    exercise: e.dir,
  }));
}

export default async function ExercisePage({
  params,
}: {
  params: Promise<{ track: string; chapter: string; exercise: string }>;
}) {
  const { track, chapter, exercise } = await params;
  const exo = getExercise(track, chapter, exercise);
  if (!exo) notFound();
  return <ExerciseWorkbench exo={exo} />;
}
