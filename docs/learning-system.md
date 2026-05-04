# Learning System — Hybrid Google Doc + GitHub

This is a two-half system. Each half has a job, and they cross-link.

## The Google Doc ("Python Learning Roadmap")

The journal. It holds:

- Handoff prompts (so I can resume with any AI tutor without re-explaining context)
- Learner profile (background, goals, constraints, ADHD flags)
- Diagnostic Q&A and quiz logs
- Teaching method notes (what explanations actually work for me)
- Key terms tables

The Doc is the living brain — it changes shape as I learn.

## This repo

The code. It holds:

- Chapter exercises and projects (under `chapters/`)
- Reusable utilities (under `snippets/`)
- Dated session logs (under `session-logs/`)

The repo is the receipt — it shows what I actually built.

## How they link

- The Doc references this repo by commit SHA and file path when describing what was learned.
- Session log entries here link back to Doc sections by tab name or heading.

## Rule

Nothing sensitive goes in the public repo. Full diagnostic transcripts, personal reflections, and any private notes stay in the Doc.

## Pomodoro Pacing

Sessions follow a 25/5/25/10 rhythm: 25-min sprint, 5-min pulse (stand, water, no phone), 25-min sprint, 10-min real break. Repeat to chapter complete. Targets: 2 objectives per session today; full chapter in 2 weeks; multi-chapter sessions in 3 months.

## The 3-Sentence Drill

After every concept Claude teaches, I articulate it in exactly 3 sentences: (1) what it IS, (2) when to USE it, (3) when it BREAKS or its limit. Over 3 sentences = restart. Builds surgical-explanation muscle.

## Five Mini-Projects per Chapter

Each chapter has 5 objectives. Each objective gets a small portfolio-grade project living in `chapters/chXX-*/projects/<project-name>/` with its own README. By chapter end: 5 commits, 5 working tools.

## Python Environment

This project uses a Python 3.12 virtual environment located at `C:\Users\Cportable\venvs\python-mastery\`. The venv lives outside this repo intentionally — venvs should never be committed.

Why a venv: isolates project dependencies, avoids polluting system Python, makes the project reproducible. PEP 668 also requires it for externally-managed Pythons like the uv-managed one we used here.

Why Python 3.12 (not 3.14): 3.12 is the current stable target for the Python data-science ecosystem. 3.14 is too new and many wheels do not exist yet.

Jupyter kernel display name: `Python 3.12 (mastery)`

Activate the venv in Git Bash:
`source /c/Users/Cportable/venvs/python-mastery/Scripts/activate`

Deactivate:
`deactivate`

Install a package once activated:
`pip install <package>`

Known machine quirk: this Windows install has a missing `CSIDL_COMMON_APPDATA` registry value, which silently breaks Python 3.13 and system-Python 3.14's pip in different ways. The venv sidesteps this entirely. Non-blocking; can be repaired later by adding the registry key under `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders\Common AppData` pointing to `C:\ProgramData`.
