// Bouton global de reset (statuts + brouillons). Affiche le nb d'exos complétés.
"use client";

import { useEffect, useState } from "react";
import { completedIds, resetAll } from "../lib/progress";

export default function ResetAllButton() {
  const [count, setCount] = useState(0);
  useEffect(() => {
    setCount(completedIds().size);
  }, []);

  if (count === 0) return null;

  return (
    <button
      type="button"
      onClick={() => {
        if (!confirm(`Effacer la progression (${count} exos) et tous les brouillons ?`)) return;
        resetAll();
        setCount(0);
      }}
      className="text-xs text-muted hover:text-fail"
      title="Efface localStorage : progression + brouillons"
    >
      Reset progression ({count})
    </button>
  );
}
