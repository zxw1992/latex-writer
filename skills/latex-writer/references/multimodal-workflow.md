# Multimodal Extraction: Image → LaTeX

When a user provides an image — handwritten notes, a photo of a textbook page, a screenshot of a paper, an annotated diagram — follow this workflow to produce accurate LaTeX.

**The user is trusting you for accuracy. Every misread symbol can silently break a formula.**

---

## Step 1: Survey the Entire Image

Before writing any code, scan the whole image and identify what's present:

- Mathematical formulas (inline, display, numbered, aligned systems)
- Tables (how many columns/rows, are there merged cells, what are the borders)
- Diagrams or figures (geometric shapes, arrows, labels, coordinates)
- Text with special formatting (highlighted, underlined, strikethrough, colored)
- Handwritten annotations or margin notes
- Structural elements (section headers, numbered items)

Mentally map each element to its LaTeX equivalent before writing a single line.

Track content and formatting by source region. Include highlights on display
equations as well as text; record their colors and spans. A highlight command
somewhere in the output does not show that all highlighted regions were preserved.

---

## Step 2: Mathematical Formula Extraction

This is the highest-stakes task — be meticulous.

### Work symbol by symbol

Don't try to recognize an entire expression at once. Scan left to right, top to bottom:

```
x_{i,j}^{(k)}  ← subscript i,j then superscript (k)
\hat{\theta}    ← hat accent over theta
\frac{\partial f}{\partial x}   ← partial derivative fraction
```

### Common lookalike pairs to distinguish carefully

| Looks similar | Correct symbol | LaTeX |
|--------------|----------------|-------|
| n vs η (eta) | Greek letter | `\eta` |
| v vs ν (nu) | Greek letter | `\nu` |
| u vs μ (mu) | Greek letter | `\mu` |
| a vs α (alpha) | Greek letter | `\alpha` |
| p vs ρ (rho) | Greek letter | `\rho` |
| q vs φ (phi) | Greek letter | `\varphi` |
| I vs l vs 1 | Context-dependent | — |
| 0 vs O | Digit vs letter | — |
| · (cdot) vs . | Multiplication | `\cdot` vs `.` |
| × vs x | Cross product | `\times` |
| ÷ vs / | Division | `\div` |
| ≤ vs < | Less-or-equal | `\leq` |
| ≠ vs ≡ | Not-equal vs equiv | `\neq`, `\equiv` |
| ∝ vs ∞ | Proportional vs infinity | `\propto`, `\infty` |
| ⊂ vs ⊆ | Proper vs improper subset | `\subset`, `\subseteq` |

### Fraction structure

```
    a          → \frac{a}{b}
   ───
    b

    ∂f         → \frac{\partial f}{\partial x}
   ────
    ∂x
```

### Summation / integral with limits

```
  n                    → \sum_{i=1}^{n} a_i
  Σ a_i
 i=1

  ∞                    → \int_0^\infty f(x)\,dx
 ∫ f(x) dx
  0
```

### Mark uncertainty honestly

```latex
% If a symbol is ambiguous (bad handwriting, blurry image):
\alpha  % TODO: verify — could be a

% If a sign is unclear:
x + y  % TODO: verify sign — could be x - y
```

Do not silently guess. A marked uncertainty is far more useful than a confident mistake.

---

## Step 3: Table Extraction

### Count structure first

Before any code:
1. Count columns and rows
2. Identify header rows
3. Note merged cells (span multiple columns or rows)
4. Note border style: thick/thin top rule, separator after header, thick bottom rule → booktabs

### Map to LaTeX

```latex
% Standard academic table (booktabs style)
\begin{table}[htbp]
    \centering
    \caption{Extracted table caption}
    \begin{tabular}{alignment}
        \toprule
        Header 1 & Header 2 & ... \\
        \midrule
        data & data & ... \\
        \bottomrule
    \end{tabular}
\end{table}
```

### Column alignment

- Left-aligned text → `l`
- Centered headings → `c`
- Right-aligned numbers → `r`
- Numbers with decimals → `S` (siunitx) or `r` approximation
- Vertical lines in original → only add `|` if the original clearly has them (booktabs style avoids them)

### Merged cells

```latex
% Spanning 3 columns
\multicolumn{3}{c}{Merged header}

% Spanning 2 rows
\multirow{2}{*}{Merged content}

% Partial rule under merged header
\cmidrule(lr){2-4}   % rule spanning columns 2 to 4
```

### Cell content

Reproduce exactly — including superscripts, footnote markers, bold, italic:
```latex
\textbf{bold cell}
\textit{italic cell}
$\pm 0.05$          % ± in a table cell
$^*$                % asterisk superscript as footnote marker
```

---

## Step 4: Diagram and Figure Extraction

### Assess complexity first

**Good candidates for TikZ reproduction:**
- Flowcharts with rectangles, diamonds, arrows
- Simple block diagrams
- Geometric figures with labeled points
- Simple coordinate graphs or number lines
- Neural network layer diagrams (boxes with arrows)

**Too complex for accurate TikZ reproduction:**
- Photographs or realistic illustrations
- Highly detailed scientific schematics (circuit diagrams with many components → suggest `circuitikz` package)
- Organic chemistry structures (→ suggest `chemfig` or `mhchem`)
- Complex CAD-style drawings

For complex cases: state this clearly to the user, reproduce what you can, and suggest alternatives.

### TikZ reconstruction approach

1. Identify the coordinate system — where is the origin, what are the rough dimensions
2. List all nodes (labeled boxes, circles, etc.) and their approximate positions
3. List all edges (arrows, lines) and their types (solid, dashed, labeled)
4. Note colors and styles
5. Build the TikZ code using relative positioning when possible

```tikz
% Use positioning library for cleaner layout
\usetikzlibrary{positioning, arrows.meta, shapes.geometric}
\tikzset{
    node style/.style={...}
}
\node[...] (name) {label};
\draw[->] (A) -- (B);
```

### Annotations (highlighted text, underlines, circles around text)

```latex
% Highlighted text (soul package)
\usepackage{soul}
\hl{highlighted text}

% Colored box
\usepackage{xcolor}
\colorbox{yellow!40}{highlighted}

% Underline
\underline{text}
\uline{text}    % ulem package (\usepackage[normalem]{ulem}), better than \underline

% Strikethrough
\sout{text}     % ulem package (soul's equivalent is \st)

% Circle around inline element
\usepackage{tikz}
\tikz[baseline=(char.base)]{\node[draw, circle, inner sep=1pt](char){x};}
```

---

## Step 5: Handwritten Content

Handwriting introduces ambiguity. Extra care is needed:

1. **Read in context** — a single ambiguous character often becomes clear when you read the whole expression
2. **Use mathematical plausibility as a clue** — it can help interpret `n` versus `η`, but do not silently repair a source formula to make it mathematically correct. Record ambiguous alternatives.
3. **Inconsistent handwriting** — compare repeated variables and definitions, but mark ambiguity rather than assuming two shapes are the same symbol.
4. **Scan for variable definitions** — if the writer defined `let k = ...` earlier, track that variable
5. **Mark all guesses** with `% TODO`

---

## Step 6: Assemble the Final Output

Structure the output for the user:

```latex
% Packages needed (add to your preamble):
% \usepackage{amsmath, amssymb}
% \usepackage{booktabs}
% etc.

% --- Extracted content ---
[LaTeX code here]
```

After the code:
- Briefly explain any notable choices (e.g., why you chose `align` over `equation`)
- List all `% TODO: verify` items in plain language so the user knows what to double-check
- If a diagram was approximated, describe what was simplified

## Step 7: Verify Against the Image

When compilation/rendering tools are available, follow `verification.md` and compare
each source region with the final rendered output. Check symbols, bounds, subscripts,
table spans, diagram edges, and formatting separately. Include the main display
formula and isolated coefficient labels in the highlight check. Use `\colorbox`
or another math-compatible approach for highlighted display formulas; long colored
boxes may need a different layout to stay inside `\linewidth`.

Fix missing or miscolored regions and recheck the affected page. Report any
uncertainties or deliberately normalized formatting. Mark only genuine ambiguities
with `% TODO: verify`; if the source is clear, do not add a marker. Keep each marker
next to the affected code and list the issue in the explanation.

---

## Quick Reference: Image Elements → LaTeX

| Image element | LaTeX approach |
|--------------|----------------|
| Inline formula | `$...$` |
| Displayed formula, no number | `\[ ... \]` |
| Numbered equation | `equation` environment |
| Multiple aligned equations | `align` environment |
| Piecewise function | `cases` environment |
| Simple table, no borders | `tabular` + `booktabs` |
| Table with merged cells | `multirow` + `\multicolumn` |
| Multi-page table | `longtable` |
| Flowchart | TikZ + `shapes.geometric` + `arrows.meta` |
| Block diagram | TikZ + `positioning` |
| Function plot | `pgfplots` |
| Highlighted text | `soul` (`\hl`) or `\colorbox` |
| Circled element | TikZ inline node |
| Underlined | `\underline` or `ulem` `\uline` |
| Strikethrough | `ulem` `\sout` or `soul` `\st` |
| Margin annotation | `todonotes` or footnote |
