# Chapter 11 — Organizing Files

Moving, copying, renaming, and deleting files programmatically — shutil, os.walk, send2trash, zipfile.

## Two-track study reminder

- **Quizlet** = recognition (concept cards in strict 3-point Senior format: WHAT it is / WHEN used / LIMIT or what breaks it).
- **Notebooks** = production (real-world drills in the 3-cell pattern: setup / attempt with `# TODO` / reference solution).

## Objectives

- [x] shutil.copy / shutil.move (rename = move)
- [x] delete trio: os.unlink (file) / os.rmdir (empty dir) / shutil.rmtree (tree) — all permanent
- [x] send2trash — recoverable delete while developing
- [x] os.walk — (foldername, subfolders, filenames) per folder: one string, two lists
- [x] zipfile — read (.namelist / .extractall) and write ('w' overwrites, 'a' appends, ZIP_DEFLATED)
- [x] chapter project

## Projects

- `projects/selective_copy.py` — chapter project: walk a tree, collect every `.pdf` into one folder. Ran for real against my Downloads: 91 PDFs collected.

## Traps I hit (so future me remembers)

- RENAME is `shutil.move` to a new name, not copy — copy leaves the original AND makes a duplicate.
- os.walk filenames are BARE names — glue with `os.path.join(foldername, filename)` before copying.
- Quotes = frozen literal; no quotes = live variable. Never hardcode paths inside the walk loop.
- makedirs is setup: it runs ONCE, at the top, before the loop — `exist_ok=True` = quiet skip if the folder already exists.
- Two folders in play: FROM (`foldername`, changes every visit) vs TO (the destination, fixed). The join builds the FROM; the TO never goes inside it.
