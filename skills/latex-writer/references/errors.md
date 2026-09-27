# Common LaTeX Errors & Fixes

## How to Read Error Messages

LaTeX error messages appear in the `.log` file and terminal. Key parts:

```
! Undefined control sequence.
l.42 \foobar
```

- `!` marks an error; nonstop mode may continue and produce an incomplete PDF
- `l.42` means the error occurred at line 42
- The command or text that caused it follows

**Strategy:** Look at the line number, check that line and a few lines before it.

---

## Top Errors and Fixes

### `! Undefined control sequence`

**Meaning:** You used a command LaTeX doesn't recognize.

**Common causes & fixes:**
```latex
% Cause 1: Typo
\frsction{a}{b}    % → \frac{a}{b}

% Cause 2: Missing package
\mathbb{R}         % → add \usepackage{amssymb}
\toprule           % → add \usepackage{booktabs}

% Cause 3: A command from a package/engine setup that is not loaded
\setCJKmainfont{SimSun} % requires suitable CTeX/xeCJK support; check the engine
```

If a defined math command is used outside math mode, the error may instead say
that the command is allowed only in math mode or report `Missing $ inserted`.
Do not diagnose it as a missing package solely from the command name.

---

### `! Missing $ inserted`

**Meaning:** You used a math symbol or command outside math mode.

```latex
% ✗ Wrong
The value is \alpha + 1.
x_1 is the first element.

% ✓ Correct
The value is $\alpha + 1$.
$x_1$ is the first element.
```

**Sneaky cause:** Underscore `_` and caret `^` are special in math mode. In regular text, they must be escaped:
```latex
file\_name      % underscore in text
100\^{}th       % caret in text
```

---

### `! Missing \begin{document}`

**Meaning:** Text or commands appear before `\begin{document}`.

```latex
% ✗ Wrong — content before \begin{document}
\documentclass{article}
Hello world   % ← this causes the error
\begin{document}

% ✓ Correct
\documentclass{article}
\begin{document}
Hello world
\end{document}
```

---

### `! Environment X undefined`

**Meaning:** You used `\begin{X}` but environment X isn't defined.

```latex
% ✗ Cause: typo or missing package
\begin{alinged}  % → should be aligned
\begin{align}    % needs \usepackage{amsmath}
\begin{lstlisting} % needs \usepackage{listings}
```

---

### `! Misplaced \noalign` / `! Misplaced alignment tab character &`

**Meaning:** `&` appears outside an alignment, or a rule such as `\midrule` is
placed where TeX expects cell content, often because the preceding row lacks `\\`.

```latex
% Misplaced alignment tab character & in ordinary text:
Research & Development          % use Research \& Development
```

```latex
% Misplaced \noalign: booktabs is loaded, but the header row is not terminated.
% Requires: \usepackage{booktabs}
\begin{tabular}{cc}
  A & B
  \midrule
  1 & 2 \\
\end{tabular}
```

Fix the header to `A & B \\` before the rule. Ordinary text such as
`This is a line \\ And another.` is a valid forced line break; it does not itself
cause either alignment error. When `booktabs` is entirely missing, `\toprule`,
`\midrule`, and `\bottomrule` are all undefined. A log showing an expanded
`\midrule -> \noalign` means that command has a definition: inspect the actual
preamble, row endings, local package files, and full log before assigning a cause.

---

### `Runaway argument` / `! Paragraph ended before \X was complete`

**Meaning:** A command's argument is never closed — usually a missing `}`.

```latex
% ✗ Wrong — unmatched brace
\textbf{this is bold
text continues...

% ✓ Correct
\textbf{this is bold} text continues...
```

**Also:** A paragraph break inside a command that does not accept paragraphs.
Replacing the blank line with `\par` does not solve that restriction.
```latex
% ✗ \mbox does not accept multiple paragraphs
\mbox{First paragraph.

Second paragraph.}
```

```latex
% ✓ Standard LaTeX footnotes DO allow multiple paragraphs
Text\footnote{First paragraph.

Second paragraph.}
```

---

### `Overfull \hbox (Xpt too wide)`

**Meaning:** Text/content overflows the line width. This is a **warning**, not an error — the document still compiles.

**Fixes:**
```latex
% Option 1: Add \usepackage{microtype} in preamble — often fixes it automatically

% Option 2: Allow hyphenation by adding a hint
hyper\-parameter  % suggest break point

% Option 3: Suppress with sloppy (use sparingly — makes spacing uneven)
\begin{sloppypar}
Long text that won't break nicely...
\end{sloppypar}

% Option 4: Force a line break
Long text that won't fit on one line\linebreak here.

% Option 5: Rewrite the sentence
```

---

### `Underfull \hbox (badness X)`

**Meaning:** LaTeX couldn't distribute words evenly — too much whitespace. Another warning.

Usually harmless. If it's in a bibliography or URLs, add:
```latex
\usepackage{microtype}
\usepackage[hyphens]{url}  % allow URL line breaks
```

---

### `! File 'X.sty' not found`

**Meaning:** A package is not installed.

**Fixes:**
```latex
% Install the package:
% TeX Live:  tlmgr install package-name
% MiKTeX:    Packages auto-install on first compile, or use MiKTeX Console

% Check if you spelled it correctly:
\usepackage{amsmth}   % ✗
\usepackage{amsmath}  % ✓
```

---

### `! LaTeX Error: \begin{X} on input line N ended by \end{Y}`

**Meaning:** Mismatched `\begin{...}` and `\end{...}`.

```latex
% ✗ Wrong
\begin{align}
    a = b
\end{equation}  % wrong environment name

% ✓ Correct
\begin{align}
    a = b
\end{align}
```

---

### `! Too many }'s`

**Meaning:** You have an extra closing brace `}`.

Count braces: every `{` needs a matching `}`. In complex math expressions, use an editor with brace matching.

---

### `Citation 'X' on page N undefined`

**Meaning:** You cited a key that doesn't exist in your `.bib` file, or you haven't run bibtex/biber yet.

**Fixes:**
1. Check the key spelling in your `.bib` file
2. Run the full compilation sequence:
   - With BibTeX: `latex → bibtex → latex → latex`
   - With biber: `xelatex → biber → xelatex → xelatex`

---

### `I can't find file 'X'` (for \input or \include)

```latex
\input{chapter1}   % LaTeX looks for chapter1.tex
% Make sure the file exists and the path is correct
```

---

## Chinese-Specific Errors

### Garbled Chinese / No Chinese output

**Possible causes:** Missing Chinese support, wrong input encoding, unavailable
fonts, missing glyphs, or an engine/configuration mismatch. Read the log and the
existing project configuration. Preserve a working LuaLaTeX or pdfLaTeX+CJK setup.
For a new unconstrained document, use the portable XeLaTeX setup in `zh-setup.md`.

### `Package inputenc Error: Unicode character`

**Cause:** Chinese file compiled with pdfLaTeX + inputenc.

**Fix:** For a new unconstrained Unicode document, use XeLaTeX or LuaLaTeX with
appropriate Chinese support. For an existing pdfLaTeX project, first check its
CJK configuration and template constraints. Switching engines requires checking
other packages too; `inputenc` is normally unnecessary under XeLaTeX/LuaLaTeX.

### Chinese fonts not found

CTeX's automatic font selection can itself choose an unavailable font. If the
error occurs during `\documentclass` or `\usepackage{ctex}`, change the fontset
at that loading point; a later font command cannot repair an earlier fatal error.
Use `fontset=fandol` for an unconstrained XeLaTeX/LuaLaTeX document, or
`fontset=none` plus explicit available fonts when required. Read the complete
examples in `zh-setup.md`. Do not silently replace an institution's required font.

---

## General Debugging Tips

1. **Start with the earliest causal error** — Later errors may cascade. Check the surrounding log for consistency, fix the root cause, then recompile; multiple independent errors are possible.

2. **Check the line number** — Go to the line LaTeX reports and look for the mistake there or a few lines before.

3. **Use `draft` mode** to compile faster while debugging:
   ```latex
   \documentclass[draft]{article}
   ```

4. **Comment out sections** to isolate the problem:
   ```latex
   %\input{problematic-section}
   ```

5. **Check `.log` file** — more detailed than terminal output.

6. **Minimal working example (MWE)** — Strip the document to the minimum that still shows the error. This makes the cause obvious.
