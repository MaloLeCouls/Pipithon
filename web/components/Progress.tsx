"use client";

import { useEffect, useState } from "react";
import { completedIds } from "../lib/progress";

export default function Progress({ ids }: { ids: string[] }) {
  const [done, setDone] = useState(0);
  useEffect(() => {
    const set = completedIds();
    setDone(ids.filter((i) => set.has(i)).length);
  }, [ids]);
  const pct = ids.length ? Math.round((done / ids.length) * 100) : 0;
  return (
    <div className="flex items-center gap-2">
      <div className="h-1.5 w-24 overflow-hidden rounded bg-surface-2">
        <div className="h-full bg-ok" style={{ width: `${pct}%` }} />
      </div>
      <span className="text-xs text-muted">
        {done}/{ids.length}
      </span>
    </div>
  );
}
