"use client";

import Editor from "@monaco-editor/react";

export default function MonacoEditor({
  value,
  onChange,
  readOnly = false,
}: {
  value: string;
  onChange?: (v: string) => void;
  readOnly?: boolean;
}) {
  return (
    <Editor
      height="100%"
      defaultLanguage="python"
      theme="vs-dark"
      value={value}
      onChange={(v) => onChange?.(v ?? "")}
      options={{
        readOnly,
        fontSize: 13,
        fontFamily: "var(--font-geist-mono), monospace",
        minimap: { enabled: false },
        scrollBeyondLastLine: false,
        tabSize: 4,
        automaticLayout: true,
        renderWhitespace: "selection",
        padding: { top: 12 },
      }}
      loading={<div className="p-4 text-muted text-sm">Chargement de l'éditeur…</div>}
    />
  );
}
