# Lesson Generation Style Sync Design

## Goal

Sync the Day 6 lesson-writing style into the reusable generation rules so future `lesson.md` files default to the same teaching approach.

## Scope

Update:

- `skills/learn-plan.lisp`
- `skills/learn-methods.lisp`

## Design

The change is split into two layers:

1. Planning layer in `learn-plan.lisp`
   - Define the default outline-style daily lesson structure used by the Week 3 notes.
   - Add quality rules that prevent lessons from degrading into bare outlines.
   - Require parameter-level points to be expanded into explanation plus examples.

2. Teaching layer in `learn-methods.lisp`
   - Teach the generator how to expand each outline section.
   - Require a connected mini-workflow example when tasks form a sequence.
   - Require explicit explanation when introducing engineering habits such as file splitting.

## Behavior To Preserve

- Keep the study-note rhythm and headings.
- Keep JS / TS bridge sections.
- Keep concise pacing.

## Behavior To Add

- "Keep the outline, but fill each section with explanation."
- "Parameter-level focus must explain meaning, behavior, and minimal example."
- "Task lists should become one connected example when possible."
- "When introducing structure changes, explain why now."
