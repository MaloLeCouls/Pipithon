#!/usr/bin/env node
/**
 * Génère `web/lib/_pymistral-bundle.ts` à partir du paquet Python
 * `exercises/_pymistral/pymistral/`.
 *
 * Pourquoi : `lib/pyodide.ts` tourne dans le navigateur, il ne peut pas lire
 * le FS au runtime. On embarque donc le contenu du framework dans un module
 * TS statique, que Pyodide écrit dans sa FS WASM au démarrage.
 *
 * Lancé via `pnpm prebuild` et `pnpm predev`. Manuel : `node scripts/build-pymistral.mjs`.
 */
import { readFileSync, readdirSync, writeFileSync, statSync, mkdirSync } from "node:fs";
import { dirname, join, relative } from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const REPO = join(__dirname, "..", "..");
const PKG = join(REPO, "exercises", "_pymistral", "pymistral");
const OUT = join(REPO, "web", "lib", "_pymistral-bundle.ts");

function walk(root) {
  const out = [];
  for (const entry of readdirSync(root, { withFileTypes: true })) {
    const p = join(root, entry.name);
    if (entry.isDirectory()) {
      out.push(...walk(p));
    } else if (entry.name.endsWith(".py")) {
      out.push(p);
    }
  }
  return out;
}

const files = walk(PKG)
  .map((abs) => ({
    rel: relative(PKG, abs).replace(/\\/g, "/"),
    src: readFileSync(abs, "utf8"),
  }))
  .sort((a, b) => a.rel.localeCompare(b.rel));

const stamp = new Date().toISOString();
const body = files
  .map((f) => {
    // Échappement pour template literal JS : \, ` et ${
    const esc = f.src.replace(/\\/g, "\\\\").replace(/`/g, "\\`").replace(/\$\{/g, "\\${");
    return `  ${JSON.stringify(f.rel)}: \`${esc}\`,`;
  })
  .join("\n");

const out = `// AUTO-GÉNÉRÉ par scripts/build-pymistral.mjs — NE PAS ÉDITER À LA MAIN.
// Source : exercises/_pymistral/pymistral/  (généré le ${stamp})
// Embarqué côté client pour que Pyodide importe \`pymistral\` sans réseau.

export const PYMISTRAL_BUNDLE: Record<string, string> = {
${body}
};
`;

mkdirSync(dirname(OUT), { recursive: true });
writeFileSync(OUT, out, "utf8");
const lines = out.split("\n").length;
console.log(`[pymistral-bundle] ${files.length} files -> ${OUT} (${lines} lines)`);
