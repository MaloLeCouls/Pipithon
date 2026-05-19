// Couche données : scanne exercises/ + docs/curriculum/ au build (server-only).
// Source de vérité = le filesystem du repo (cf. INIT_PROMPT.md §1, §4).
import { existsSync, readdirSync, readFileSync } from "node:fs";
import { join } from "node:path";
import matter from "gray-matter";
import yaml from "js-yaml";

// web/ est le cwd en dev et build ; le repo est un cran au-dessus.
const REPO = join(process.cwd(), "..");
const EXOS = join(REPO, "exercises");
const CURRICULUM = join(REPO, "docs", "curriculum");

export type ExerciseType = "creation" | "modification" | "debugging";

export interface ExerciseMeta {
  id: string;
  chapter: number;
  chapter_slug: string;
  type: ExerciseType;
  difficulty: number;
  estimated_minutes: number;
  concepts: string[];
  theme: string;
  title: string;
  short_description: string;
  hints: string[];
  reference_book: string;
  tags: string[];
}

export interface ExerciseFiles {
  starter: string;
  solution: string;
  tests: string;
}

export interface Exercise extends ExerciseMeta {
  track: string;
  chapterDir: string; // ex. ch01-data-model
  dir: string; // ex. 001-furniture-chair-repr
  files: ExerciseFiles;
}

export interface ChapterInfo {
  number: number;
  chapterDir: string;
  slug: string;
  title: string;
  tier: string;
  status: string;
  count: number;
}

export interface TrackInfo {
  slug: string;
  label: string;
  status: "active" | "locked";
  exerciseCount: number;
}

const TRACK_LABELS: Record<string, string> = {
  "python-pure": "Python pur — Fluent Python",
  "math-foundations": "Maths ML",
  algorithms: "Algorithmes",
  "pytorch-basics": "PyTorch",
  "performance-python": "Performance Python",
  "code-reading": "Code reading OSS",
  "testing-discipline": "Discipline de test",
};

function safeReaddir(p: string): string[] {
  try {
    return readdirSync(p, { withFileTypes: true })
      .filter((d) => d.isDirectory())
      .map((d) => d.name)
      .sort();
  } catch {
    return [];
  }
}

function loadChapterFrontmatter(slug: string, n: number) {
  const file = join(CURRICULUM, slug, `chapter-${String(n).padStart(2, "0")}.md`);
  if (!existsSync(file)) return { title: `Chapitre ${n}`, tier: "?", status: "active" };
  const { data } = matter(readFileSync(file, "utf8"));
  return {
    title: (data.title as string) ?? `Chapitre ${n}`,
    tier: (data.tier as string) ?? "?",
    status: (data.status as string) ?? "active",
  };
}

export function getAllExercises(track = "python-pure"): Exercise[] {
  const root = join(EXOS, track);
  const out: Exercise[] = [];
  for (const chapterDir of safeReaddir(root)) {
    for (const type of ["creation", "modification", "debugging"] as const) {
      const typeDir = join(root, chapterDir, type);
      for (const dir of safeReaddir(typeDir)) {
        const base = join(typeDir, dir);
        const metaPath = join(base, "meta.yaml");
        if (!existsSync(metaPath)) continue;
        const meta = yaml.load(readFileSync(metaPath, "utf8")) as ExerciseMeta;
        out.push({
          ...meta,
          track,
          chapterDir,
          dir,
          files: {
            starter: readFileSync(join(base, "starter.py"), "utf8"),
            solution: readFileSync(join(base, "solution.py"), "utf8"),
            tests: readFileSync(join(base, "tests.py"), "utf8"),
          },
        });
      }
    }
  }
  return out.sort((a, b) => a.chapter - b.chapter || a.dir.localeCompare(b.dir));
}

export function listTracks(): TrackInfo[] {
  return Object.entries(TRACK_LABELS).map(([slug, label]) => {
    const count = slug === "python-pure" ? getAllExercises(slug).length : 0;
    return {
      slug,
      label,
      status: count > 0 ? "active" : "locked",
      exerciseCount: count,
    };
  });
}

export function getChapters(track = "python-pure"): ChapterInfo[] {
  const exos = getAllExercises(track);
  const byChapter = new Map<string, Exercise[]>();
  for (const e of exos) {
    const arr = byChapter.get(e.chapterDir) ?? [];
    arr.push(e);
    byChapter.set(e.chapterDir, arr);
  }
  return [...byChapter.entries()]
    .map(([chapterDir, list]) => {
      const n = list[0].chapter;
      const fm = loadChapterFrontmatter(track, n);
      return {
        number: n,
        chapterDir,
        slug: chapterDir,
        title: fm.title,
        tier: fm.tier,
        status: fm.status,
        count: list.length,
      };
    })
    .sort((a, b) => a.number - b.number);
}

export function getExercises(track: string, chapterDir: string): Exercise[] {
  return getAllExercises(track).filter((e) => e.chapterDir === chapterDir);
}

export function getExercise(track: string, chapterDir: string, dir: string): Exercise | undefined {
  return getAllExercises(track).find((e) => e.chapterDir === chapterDir && e.dir === dir);
}
