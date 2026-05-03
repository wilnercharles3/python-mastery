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
