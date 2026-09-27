# Tables Reference

## Required Packages

```latex
\usepackage{booktabs}   % professional tables (\toprule, \midrule, \bottomrule)
\usepackage{multirow}   % merge rows
\usepackage{array}      % extended column types
\usepackage{tabularx}   % auto-width columns
\usepackage{longtable}  % multi-page tables
\usepackage{colortbl}   % colored cells/rows
\usepackage{siunitx}    % align numbers by decimal point (S column type)
```

---

## Professional Table Template (booktabs)

```latex
\begin{table}[htbp]
    \centering
    \caption{Table caption goes here}
    \label{tab:example}
    \begin{tabular}{llr}
        \toprule
        Column A & Column B & Column C \\
        \midrule
        data     & data     & 1.23 \\
        data     & data     & 4.56 \\
        \bottomrule
    \end{tabular}
\end{table}
```

Rule: `\toprule` (top), `\midrule` (header separator), `\bottomrule` (bottom). **Never use `\hline` in booktabs-style tables.**

---

## Column Alignment Specifiers

| Specifier | Meaning |
|-----------|---------|
| `l` | Left-aligned |
| `c` | Center-aligned |
| `r` | Right-aligned |
| `p{width}` | Fixed-width, top-aligned (wraps) |
| `m{width}` | Fixed-width, vertically centered |
| `b{width}` | Fixed-width, bottom-aligned |
| `X` | Auto-fill width (`tabularx` only) |
| `S` | Align by decimal point (`siunitx`) |
| `\|` | Vertical line (avoid in booktabs style) |
| `@{...}` | Custom inter-column separator |
| `>{...}` | Pre-column code (e.g., `>{\bfseries}l`) |

---

## Merging Cells

### Merge Columns — `\multicolumn`

```latex
\multicolumn{num_cols}{alignment}{content}

% Example: header spanning 3 columns
\begin{tabular}{cccc}
    \toprule
    ID & \multicolumn{3}{c}{Scores} \\
    \cmidrule(lr){2-4}
    & Math & Physics & Chemistry \\
    \midrule
    001 & 90 & 85 & 92 \\
    \bottomrule
\end{tabular}
```

### Merge Rows — `\multirow`

```latex
\usepackage{multirow}

\begin{tabular}{ccc}
    \toprule
    Group & Student & Score \\
    \midrule
    \multirow{2}{*}{A} & Alice & 90 \\
                       & Bob   & 85 \\
    \midrule
    \multirow{2}{*}{B} & Carol & 88 \\
                       & Dave  & 92 \\
    \bottomrule
\end{tabular}
```

### Merge Both

```latex
\multicolumn{2}{c}{\multirow{2}{*}{content}}
```

---

## Partial Horizontal Rules — `\cmidrule`

```latex
\cmidrule{2-4}         % rule from column 2 to 4
\cmidrule(lr){2-4}     % trimmed on both sides (cleaner)
\cmidrule(l){2-4}      % trimmed left only
\cmidrule(r){2-4}      % trimmed right only
```

---

## Auto-Width Tables — `tabularx`

```latex
\usepackage{tabularx}

\begin{table}[htbp]
    \centering
    \caption{Auto-width table}
    \begin{tabularx}{\linewidth}{lXr}   % X fills the current column/container
        \toprule
        Name & Description & Value \\
        \midrule
        Item & This is a long description that will wrap automatically & 100 \\
        \bottomrule
    \end{tabularx}
\end{table}
```

---

## Multi-Page Tables — `longtable`

Use in one-column document flow, outside a `table` float. `longtable` does not
work directly in ordinary two-column mode; follow the template's approach for
wide or multi-page tables instead of changing the whole document layout silently.

```latex
\usepackage{longtable}
\usepackage{booktabs}

\begin{longtable}{lcr}
    \caption{Long table spanning multiple pages} \label{tab:long} \\
    \toprule
    Column A & Column B & Column C \\
    \midrule
    \endfirsthead    % end of first-page header

    \multicolumn{3}{l}{\textit{(continued from previous page)}} \\
    \toprule
    Column A & Column B & Column C \\
    \midrule
    \endhead         % end of repeated header

    \midrule
    \multicolumn{3}{r}{\textit{(continued on next page)}} \\
    \endfoot         % end of repeated footer

    \bottomrule
    \endlastfoot     % end of last-page footer

    % --- Data rows ---
    data & data & data \\
    data & data & data \\
    % ... more rows
\end{longtable}
```

---

## Colored Rows and Cells — `colortbl`

```latex
\usepackage{colortbl}
\usepackage{xcolor}

% Color entire row (put before row)
\rowcolor{gray!20}

% Color a single cell
\cellcolor{blue!15} content

% Alternating row colors (with xcolor option table)
\usepackage[table]{xcolor}
\rowcolors{2}{gray!10}{white}   % starting from row 2: alternating gray/white
```

---

## Decimal Alignment — `siunitx`

```latex
\usepackage{siunitx}

\begin{tabular}{lS[table-format=3.3]}
    \toprule
    Method & {Score} \\        % header in {} for S column
    \midrule
    Model A & 12.345 \\
    Model B &  9.87 \\
    Model C & 100.0 \\
    \bottomrule
\end{tabular}
```

---

## Floating Placement

| Specifier | Meaning |
|-----------|---------|
| `h` | Here (where it appears in text) |
| `t` | Top of page |
| `b` | Bottom of page |
| `p` | Separate float page |
| `H` | Force here (requires `float` package) |
| `!` | Override LaTeX's aesthetic restrictions |

Use `[htbp]` as default. Add `!` if LaTeX keeps ignoring your placement: `[h!]`.

---

## Common Patterns

### Notes below a table

```latex
\begin{table}[htbp]
    \centering
    \caption{Results}
    \begin{tabular}{lcc}
        \toprule
        Method & Accuracy & F1 \\
        \midrule
        Ours\textsuperscript{*} & \textbf{95.3} & \textbf{94.1} \\
        Baseline & 91.2 & 90.5 \\
        \bottomrule
    \end{tabular}
    \vspace{1ex}
    {\small \textsuperscript{*} Statistically significant ($p < 0.01$).}
\end{table}
```

### Bold best result

```latex
\textbf{95.3}   % bold the best value in a comparison table
```

### Cross-referencing a table

```latex
See Table~\ref{tab:example} for results.
```
