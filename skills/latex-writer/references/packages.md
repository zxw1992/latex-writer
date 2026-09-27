# Common LaTeX Packages Reference

## Common Packages (load only what is needed)

Check the existing document class and loaded packages first. In a venue template,
do not add `geometry`, heading/caption customizations, or a new bibliography system
unless its requirements allow them.

```latex
\usepackage{amsmath}    % math environments, align, cases, etc.
\usepackage{amssymb}    % extra math symbols: \mathbb, ∴, ∵, etc.
\usepackage{graphicx}   % \includegraphics
\usepackage{hyperref}   % clickable links, PDF bookmarks (load last)
\usepackage{geometry}   % page margins
\usepackage{booktabs}   % professional tables
```

---

## By Category

### Math & Science

| Package | Purpose | Key Commands |
|---------|---------|--------------|
| `amsmath` | Math environments | `align`, `cases`, `\text`, `\tag` |
| `amssymb` | Math symbols | `\mathbb{R}`, `\therefore` |
| `amsthm` | Theorem environments | `\newtheorem`, `proof` |
| `mathtools` | `amsmath` extensions | `\coloneqq`, `\mathclap`, matrix star |
| `bm` | Bold math | `\bm{\mu}` |
| `siunitx` | SI units & numbers | `\SI{9.8}{m/s^2}`, `\num{1.5e-3}` |
| `physics` | Physics notation | `\dd`, `\dv`, `\pdv`, `\ket`, `\bra` |
| `mhchem` | Chemical formulas | `\ce{H2O}`, `\ce{Fe^{2+}}` |
| `pgfplots` | Function plots | See tikz.md |

### Fonts & Typography

| Package | Purpose |
|---------|---------|
| `fontenc` + `lmodern` | Better font encoding (pdfLaTeX) |
| `fontspec` | System fonts (XeLaTeX/LuaLaTeX) |
| `microtype` | Microtypography (better spacing, fewer overfull boxes) |
| `setspace` | Line spacing: `\onehalfspacing`, `\doublespacing` |
| `xcolor` | Colors: `\textcolor{red}{text}`, `\colorbox` |
| `soul` | Highlighting, strikethrough: `\hl{text}`, `\st{text}` |
| `ulem` | Underline variants: `\uline`, `\uwave`, `\sout` |

### Layout & Structure

| Package | Purpose |
|---------|---------|
| `geometry` | Page margins and paper size |
| `fancyhdr` | Custom headers and footers |
| `titlesec` | Customize section heading styles |
| `tocloft` | Customize table of contents |
| `parskip` | Paragraph spacing instead of indent |
| `multicol` | Multi-column layout: `\begin{multicols}{2}` |
| `enumitem` | Customize lists (itemize, enumerate) |
| `float` | Force float placement with `[H]` |
| `placeins` | `\FloatBarrier` to contain floats |

### Tables

| Package | Purpose |
|---------|---------|
| `booktabs` | Professional rules: `\toprule`, `\midrule`, `\bottomrule` |
| `multirow` | Merge rows: `\multirow{2}{*}{text}` |
| `tabularx` | Auto-width columns with `X` type |
| `longtable` | Tables spanning multiple pages |
| `colortbl` | Colored cells/rows |
| `array` | Extended column types |
| `tabularray` | Modern all-in-one table package (replaces many above) |

### Figures & Drawing

| Package | Purpose |
|---------|---------|
| `graphicx` | Include images |
| `subcaption` | Subfigures |
| `wrapfig` | Text wrapping around figures |
| `caption` | Customize captions |
| `tikz` | Drawing (see tikz.md) |
| `pgfplots` | Data and function plots |
| `svg` | Include SVG files |

### Bibliography

| Package | Purpose |
|---------|---------|
| `biblatex` | Modern bibliography management |
| `natbib` | Author-year and numbered (for many journals) |
| `biblatex-gb7714-2015` | Chinese national standard |

### Code Listings

| Package | Purpose |
|---------|---------|
| `listings` | Code listings with syntax highlighting |
| `minted` | Better syntax highlighting (requires Python+Pygments) |
| `verbatim` | Verbatim text blocks |

```latex
% listings example
\usepackage{xcolor}
\usepackage{listings}
\lstset{
    language=Python,
    basicstyle=\ttfamily\small,
    keywordstyle=\bfseries\color{blue},
    commentstyle=\color{gray},
    numbers=left,
    frame=single,
}
\begin{lstlisting}
def hello():
    print("Hello, world!")
\end{lstlisting}
```

### Links & References

| Package | Purpose |
|---------|---------|
| `hyperref` | Clickable links, PDF metadata |
| `cleveref` | Smart cross-references: `\cref{fig:1}` → "Figure 1" |
| `nameref` | Reference by name instead of number |
| `url` | Format URLs: `\url{https://...}` |

```latex
\usepackage{cleveref}
% Instead of: see Figure~\ref{fig:1}
% Write:       see \cref{fig:1}
% Output:      see Figure 1 (automatic "Figure" label)
```

### Miscellaneous

| Package | Purpose |
|---------|---------|
| `todonotes` | Add todo notes in margins |
| `lipsum` | Dummy Latin text for testing |
| `blindtext` | Dummy text |
| `datetime2` | Formatted dates |
| `pdfpages` | Include PDF pages |
| `appendix` | Better appendix control |
| `algorithm2e` | Algorithm pseudocode |
| `algpseudocode` | Algorithm pseudocode (algorithmicx) |

---

## Recommended Preamble Templates

### Minimal math document

```latex
\usepackage{amsmath, amssymb, amsthm}
\usepackage{hyperref}
```

### Standard academic paper (English)

```latex
\usepackage{amsmath, amssymb, amsthm}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{microtype}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{geometry}
\usepackage[backend=biber, style=authoryear]{biblatex}
\usepackage{hyperref}
\usepackage{cleveref}
```

### Chinese academic paper

```latex
\usepackage{amsmath, amssymb, amsthm}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{geometry}
\usepackage[backend=biber, style=gb7714-2015]{biblatex}
\usepackage[colorlinks]{hyperref}
```

---

## Package Conflicts & Load Order

**Rules of thumb:**
1. Load `hyperref` near the end unless the class has already loaded it. In Beamer, use `\hypersetup{...}` for supported settings instead of loading it again with different options.
2. `cleveref` should be loaded **after** `hyperref`
3. `biblatex` detects `hyperref` automatically — load `hyperref` after `biblatex` (consistent with rule 1)
4. `xcolor` should be loaded before packages that use it (`listings`, `tikz`, etc.)
5. New XeLaTeX/LuaLaTeX font setups normally use `fontspec`; pdfLaTeX commonly uses `fontenc`. Do not paste both generic font setups into a template without checking its requirements.

**Known conflicts:**
- `soul` + `hyperref`: mostly OK but some edge cases
- `subcaption` vs `subfigure`: use one, not both; first check class-specific caption requirements (see `figures.md`).
- `float` vs `placeins`: compatible, use together
