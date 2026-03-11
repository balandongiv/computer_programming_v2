# Computer Programming sessionly Tutorial Instructions

This repository contains the LaTeX source code for the Computer Programming sessionly Tutorial Instructions.

## Features

### Lecturer Only Content

The document includes a specialized environment for content that should only be visible to lecturers (e.g., solutions, justifications, or internal notes).

**Usage:**

```latex
\begin{lectureronly}
    This content is only visible if \lecturertrue is set in main.tex.
\end{lectureronly}
```

**Configuration:**
In `main.tex`, you can toggle the visibility of this content:

- `\lecturertrue`: Shows justifications/solutions/remarks.
- `\lecturerfalse`: Produces a clean version for students.

## Compilation

To compile the document, use `xelatex`:

```bash
xelatex -interaction=nonstopmode -shell-escape main.tex
```
