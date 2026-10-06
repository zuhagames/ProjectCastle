# Blázen z Londýna: Tajná Akce

Browser FPS (three.js r160), the whole game lives in `index.html`; assets are embedded in `assets/*.js`,
three.js is bundled in `assets/three/`. `castle_grimhold.html` only redirects to `index.html`.
Published on GitHub Pages from `main` and embedded in Google Sites.

## Branch workflow (owner's rule)

- Do all work on the `dev` branch. Never commit straight to `main`.
- When an update is finished and checked (the game loads to the menu and a mission plays without errors),
  merge `dev` into `main` right away without asking: open a PR `dev` → `main` if none is open (or use the
  open one) and merge it with a merge commit. If `main` moved on, merge `main` into `dev` first and resolve.
- After the merge keep developing on `dev`.

## Checking a change

Serve the repo root (`python -m http.server 8765`) and open `index.html`; `window.__castle` exposes helpers
(`quick(levelIndex)` starts a mission, `step(n)` advances the simulation).
