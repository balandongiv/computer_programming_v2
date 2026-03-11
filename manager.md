### Objective

Coordinate a set of sub-agents to review multiple LaTeX chapter files and their associated Python files, using `editor_feedback.md` as the authoritative source of editorial critique. The goal is to produce **one actionable Markdown report per chapter** that translates relevant feedback into clear, beginner-focused revision tasks. These reports will be consumed by a separate “implementation agent” responsible for rewriting and adjusting code.

---

### Inputs

- **LaTeX chapter files** (multiple), e.g., `ses<chapter_name>.tex`. Some tex file will have its own associated table, for example, tab4.tex tab5.tex
- **Associated Python files** for each chapter (one or more), e.g., `code/<chapter_name>/*.py` or otherwise mapped
- **`editor_feedback.md`** containing structured editorial critique focused on:
  - beginner usability
  - clarity
  - pedagogy
  - flow / narrative structure

---

### Outputs

- **One Markdown report per chapter**, saved as:
  - `reports/<chapter_name>_revision_report.md` (or an equivalent consistent naming scheme)

- Each report must be:
  - chapter-specific
  - actionable (task lists, concrete rewrite instructions)
  - aligned to beginner usability and teaching clarity
  - explicit about what should change in both LaTeX content and associated Python files (where relevant)

---

### Delegation Plan

1. **Enumerate chapters** to review (based on the project structure provided).
2. **Assign one sub-agent per chapter** (or a balanced chunk if there are many).
3. Provide each sub-agent:
   - the chapter `.tex` file path
   - all associated Python file paths for that chapter
   - `editor_feedback.md`

4. Enforce consistent report format across sub-agents.

---

### Sub-Agent Responsibilities (Per Chapter)

Each sub-agent must:

1. **Read the chapter LaTeX file thoroughly**
   - Identify the chapter’s learning objectives (explicit or implied)
   - Note structure: section order, transitions, examples, definitions, exercises

2. **Review associated Python files**
   - Confirm code matches the chapter narrative
   - Identify areas where code readability, comments, naming, or step-by-step explanation is missing
   - Check that code complexity matches beginner expectations

3. **Map editorial feedback to the chapter**
   - Use `editor_feedback.md` as the checklist
   - For each feedback point, decide:
     - **Relevant** to this chapter → include in report as required actions
     - **Not relevant** → explicitly ignore (do not force-fit)

4. **Write the chapter revision report**
   - Focus on “what to do next,” not generic critique
   - Be specific: what to add, expand, rewrite, remove, reorder
   - Call out missing explanations, unclear terms, abrupt transitions, or assumed knowledge
   - If the feedback suggests adding pedagogy (examples, exercises, diagrams, stepwise walkthroughs), propose exactly where and how

---

### Required Report Structure (Standard Template)

Each chapter report must follow this structure exactly:

1. **Chapter Overview**
   - Chapter file name/path
   - Associated Python file(s)
   - Intended beginner takeaway (1–3 bullets)

2. **Relevant Editorial Feedback (Mapped)**
   - List each relevant feedback item from `editor_feedback.md`
   - Under each item: 1–2 lines explaining _why_ it applies to this chapter

3. **Action Plan (Prioritized)**
   - **P0 (Must fix):** blocking clarity/usability issues
   - **P1 (Should improve):** meaningful pedagogy/flow improvements
   - **P2 (Nice to have):** polish, extra examples, minor refactors

4. **Concrete Rewrite Instructions (LaTeX)**
   - Specify sections/subsections and what to change
   - Include guidance like:
     - “Add a short motivation paragraph before Section X”
     - “Insert a worked example after concept Y”
     - “Define term Z when first introduced”
     - “Add summary + ‘common mistakes’ callout at end”

5. **Concrete Rewrite Instructions (Python)**
   - File-by-file guidance
   - Identify:
     - code sections that need comments or simplification
     - naming cleanup
     - restructuring into smaller steps
     - additional demonstration snippets aligned to the text

6. **Beginner Usability Checklist (Chapter-Specific)**
   - 5–10 bullets verifying:
     - prerequisites stated
     - terms defined
     - examples included
     - progression is incremental
     - code outputs explained
     - no unexplained jumps

7. **Notes for the Implementation Agent**
   - Any dependencies, risks, or ordering constraints
   - If changes in one chapter may affect others, note it here

---

### Quality Rules

- Do **not** rewrite the chapter content; produce **instructions** for rewriting.
- Do **not** introduce speculative changes unrelated to `editor_feedback.md`.
- Avoid vague guidance (“make clearer”); always specify _what_ to clarify and _how_.
- Keep a strict focus on beginner clarity, pedagogy, and flow.
- Ensure the report can be executed without the sub-agent being available for follow-up.

---

### Manager Coordination Duties

- Ensure every chapter produces exactly one report.
- Ensure naming is consistent and paths are correct.
- Quickly scan reports for:
  - missing mapping to `editor_feedback.md`
  - overly generic advice
  - lack of actionable steps
  - failure to mention Python alignment when applicable

- If a report is too vague, return it to the sub-agent with a request to add concrete, location-specific instructions.

---

### Definition of “Relevant”

A feedback item is relevant if it applies to:

- the concepts taught in the chapter
- the chapter’s structure and flow
- the clarity and beginner onboarding within the chapter
- the code examples used in the chapter or referenced by it

If a feedback item does not clearly connect, it must be excluded to keep reports focused.
