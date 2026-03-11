### 1) Objective

You are an **Agent Manager** responsible for orchestrating improvements across a **multi-session LaTeX + Python codebase**. The authoritative requirements live in the session revision reports under `TODO/` (Sessions 2–9).

Your deliverable is the **updated repository state** containing:

- Refactored LaTeX chapter/session files
- Refactored Python scripts associated with those sessions
- Updated `TODO/2.md … TODO/9.md` with clear completion markings
- A concise repository-root `CHANGELOG.md` summarizing changes per session

You must enforce final quality gates:

- `main.tex` compiles successfully with **XeLaTeX**
- Each relevant Python script runs successfully in the intended environment (or blockers are explicitly documented in the relevant TODO report)

> **Important context:** You will work **directly in the repository** (terminal + VS Code). There is **no input zip** and **no final output zip**.

---

### 2) Inputs

The repository already contains:

- LaTeX project files, including a `main.tex` entrypoint (or equivalent)
- Multiple chapter/session `.tex` files
- Python `.py` scripts associated with sessions
- Revision reports located under `TODO/`:
  - `TODO/2.md` through `TODO/9.md`
  - Each report includes prioritized action items, concrete rewrite instructions for LaTeX and Python, beginner usability checklist, and implementation notes

---

### 3) Mandatory First Step: Inspect and Understand the Project

Before delegating anything:

1. Identify:
   - `main.tex` (or the main build entrypoint)
   - Where chapters/sessions live (folders, naming patterns, `\include{}` / `\input{}` relationships)
   - Where Python scripts live and how they relate to sessions
   - The full set of session reports in `TODO/`

2. Build a working mapping of:

**Session N → relevant LaTeX files + relevant Python files + `TODO/N.md`**

If mapping is ambiguous, infer associations using:

- File/folder naming conventions
- Inclusion references from `main.tex`
- Explicit file mentions inside `TODO/N.md`

Document this mapping briefly (either in manager notes, a scratch file, or as comments in `CHANGELOG.md` as needed).

---

### 4) Delegation Plan (Per Session / Chapter)

Create **one sub-agent per session** (Sessions **2–9**).

Each sub-agent receives:

- The session’s `TODO/N.md`
- The mapped LaTeX file(s) for that session
- The mapped Python file(s) for that session
- Any shared project constraints discovered during inspection (common macros, shared utilities, style rules, build tooling, etc.)

---

### 5) Sub-Agent Responsibilities (Per Session N)

Each sub-agent must:

1. Treat `TODO/N.md` as the **authoritative requirements** for that session.
2. Implement requested changes in:
   - **LaTeX:** beginner usability, clarity, structure, pedagogy, correctness, consistency
   - **Python:** readability, correctness, beginner-friendliness while keeping scripts runnable

3. Update `TODO/N.md` by marking **every** action item with exactly one of:
   - `✓` if completed
   - `X` if not completed, followed by a short reason explaining the blocker (missing dependency, unclear requirement, conflicting project constraints, file not found, etc.)

4. Preserve the report’s structure and headings; **do not delete tasks**—only mark them and add brief reasons where needed.
5. Return a short session summary to the manager:
   - What changed (high-level)
   - What remains incomplete and why
   - Any risks to compilation/runtime

---

### 6) Manager Coordination Duties

As the manager, you must:

- Dispatch session work using the session→files mapping.
- Track shared-file edits and resolve conflicts:
  - If multiple sessions touch shared LaTeX macros, shared imports, shared Python utilities, shared configuration, reconcile changes coherently.

- Ensure cross-session consistency:
  - Terminology, formatting, explanation style, pedagogy, and conventions should be consistent across chapters.

- Consolidate all modifications into a coherent repo state.

**Strongly recommended workflow (in-repo):**

- Use git branches and commits to keep work reviewable (e.g., commit per session or per logical chunk).
- Avoid committing build artifacts.

---

### 7) Quality Rules (Apply Globally)

#### LaTeX rules

- The project must compile via XeLaTeX using `main.tex` (or the repo’s main entrypoint).
- Do not introduce missing references, broken includes, or package issues.
- Optimize for beginners:
  - Explain new concepts clearly at first introduction
  - Reduce unexplained leaps
  - Ensure examples are complete and properly contextualized
  - Maintain consistent notation and structure across sessions

#### Python rules

- Scripts must run without errors in the intended environment.
- Optimize for beginner readability:
  - Clear naming, straightforward flow, minimal “cleverness”
  - Add brief clarifying comments only where they truly aid learning

- If a script requires external inputs (files/data), document prerequisites clearly and fail gracefully when reasonable.

#### Report marking rules (`TODO/*.md`)

- Every actionable item must be marked `✓` or `X` (with reason).
- Never leave tasks unmarked.
- Do not remove or rewrite the report’s intent—only reflect completion status and blockers.

---

### 8) `CHANGELOG.md` Requirements

Create/update `CHANGELOG.md` at the repo root with:

- One section per session:

  `## Session 2` … `## Session 9`

- Under each session, include **3–8 high-level bullets** describing what changed (not low-level diffs).

- If anything remains incomplete, note it briefly under that session with the reason.

---

### 9) Final Validation (Run Locally Before Declaring “Done”)

Before considering the work complete, the manager must confirm:

#### XeLaTeX compilation

- Compile `main.tex` successfully with XeLaTeX.

If compilation fails:

- Identify the responsible session/file.
- Fix if feasible.
- Otherwise, ensure the relevant `TODO/N.md` tasks are marked `X` with a clear blocker reason.

#### Python runtime

- Ensure each Python script (at least those present and/or referenced by reports) runs successfully.
- If a script cannot run due to missing external requirements, mark the relevant TODO items with `X` and document the blocker clearly.

# Python (run specific scripts as required by TODOs)

python -m compileall .
python path/to/script.py

```

---

### 10) Output / Delivery Requirements (No Zip)



  * Updated `.tex` files
  * Updated `.py` files
  * Updated `TODO/2.md … TODO/9.md` with ✓/X markings
  * `CHANGELOG.md`
* No temporary build artifacts committed (e.g., `.aux`, `.log`, `_build/`, etc.), unless explicitly required by the project.

---

### 11) Completion Standard

Work is complete only when:

* All session reports reflect accurate completion status (`✓` or `X + reason` for every actionable item)
* `main.tex` compiles with XeLaTeX
* Python scripts run successfully (or blockers are explicitly documented and reflected in TODO statuses)
* `CHANGELOG.md` accurately summarizes changes per session


```
