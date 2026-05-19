// Progression + brouillons : localStorage (mono-utilisateur, pas de DB, INIT §1).
"use client";

const DONE_KEY = "pipithon:completed";
const DRAFT_PREFIX = "pipithon:draft:";

function readSet(): Set<string> {
  if (typeof window === "undefined") return new Set();
  try {
    return new Set(JSON.parse(localStorage.getItem(DONE_KEY) ?? "[]"));
  } catch {
    return new Set();
  }
}

export function isCompleted(id: string): boolean {
  return readSet().has(id);
}

export function markCompleted(id: string): void {
  const s = readSet();
  s.add(id);
  localStorage.setItem(DONE_KEY, JSON.stringify([...s]));
}

export function completedIds(): Set<string> {
  return readSet();
}

export function loadDraft(id: string): string | null {
  if (typeof window === "undefined") return null;
  return localStorage.getItem(DRAFT_PREFIX + id);
}

export function saveDraft(id: string, code: string): void {
  localStorage.setItem(DRAFT_PREFIX + id, code);
}

export function clearDraft(id: string): void {
  localStorage.removeItem(DRAFT_PREFIX + id);
}
