# Figures & Floats Reference

## Packages (select only what the document needs)

```latex
\usepackage{graphicx}          % basic figure inclusion
\usepackage{float}             % force placement with H
\usepackage{subcaption}        % subfigures, when compatible with the document class
\usepackage{wrapfig}           % text wrapping around figures
\usepackage{caption}           % customize caption style
```

Preserve a template's caption handling. Classes such as IEEEtran have specific
subfigure requirements; consult their instructions before loading `caption` or
`subcaption`. For IEEEtran, its manual documents `subfig` with `caption=false`
to retain the class's main captions. Do not change a journal's caption style by
copying this generic preamble.

---

## Basic Figure

```latex
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.8\linewidth]{filename}
    \caption{Figure caption here.}
    \label{fig:example}
\end{figure}
```

- File extensions: `.pdf`, `.png`, `.jpg`, `.eps` — use `.pdf` for vector graphics
- No need to write the extension (LaTeX finds it), but include it for clarity
- `\label` must come **after** `\caption`

Use `\linewidth` for the current container (a column, list, or minipage).
In a two-column document, `\textwidth` spans both columns and is too wide for a
normal single-column `figure`. To deliberately span both columns, use:

```latex
\begin{figure*}[t]
    \centering
    \includegraphics[width=0.8\textwidth]{filename}
    \caption{A figure spanning both columns.}
    \label{fig:wide}
\end{figure*}
```

Check the rendered width and final log; successful compilation can still leave an
image extending into the adjacent column.

---

## `\includegraphics` Options

```latex
\includegraphics[width=0.5\linewidth]{fig}      % relative to the current container width
\includegraphics[width=8cm]{fig}                % absolute size
\includegraphics[height=5cm]{fig}               % fixed height
\includegraphics[scale=0.5]{fig}                % 50% of original size
\includegraphics[width=\linewidth]{fig}         % full current container width

% Rotation
\includegraphics[angle=90, width=0.5\linewidth]{fig}

% Clip to bounding box (left, bottom, right, top in points)
\includegraphics[trim=10 10 10 10, clip]{fig}
```

---

## Subfigures

```latex
\usepackage{subcaption}

\begin{figure}[htbp]
    \centering
    \begin{subfigure}[b]{0.45\linewidth}
        \centering
        \includegraphics[width=\linewidth]{fig1}
        \caption{First subfigure.}
        \label{fig:sub1}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.45\linewidth}
        \centering
        \includegraphics[width=\linewidth]{fig2}
        \caption{Second subfigure.}
        \label{fig:sub2}
    \end{subfigure}
    \caption{Overall caption for the figure.}
    \label{fig:both}
\end{figure}
```

- `\hfill` adds flexible space between subfigures
- Total widths should sum to less than `\linewidth` (account for spacing)
- Reference: `Figure~\ref{fig:sub1}`; the subfigure label already includes its letter.

### Three subfigures in a row

```latex
\begin{figure}[htbp]
    \centering
    \begin{subfigure}[b]{0.3\linewidth}
        \includegraphics[width=\linewidth]{fig1}
        \caption{Left}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.3\linewidth}
        \includegraphics[width=\linewidth]{fig2}
        \caption{Center}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.3\linewidth}
        \includegraphics[width=\linewidth]{fig3}
        \caption{Right}
    \end{subfigure}
    \caption{Three figures side by side.}
\end{figure}
```

---

## Wrapping Text Around a Figure

```latex
\usepackage{wrapfig}

\begin{wrapfigure}{r}{0.4\linewidth}    % r=right, l=left; 0.4\linewidth = figure width
    \centering
    \vspace{-10pt}                       % reduce extra space above
    \includegraphics[width=\linewidth]{fig}
    \caption{Wrapped figure.}
    \label{fig:wrapped}
    \vspace{-10pt}                       % reduce extra space below
\end{wrapfigure}

Text flows around this figure. Make sure there's enough text for the wrap to work...
```

---

## Floating Placement

| Specifier | Meaning |
|-----------|---------|
| `h` | Here (approximately) |
| `t` | Top of page |
| `b` | Bottom of page |
| `p` | Dedicated float page |
| `H` | Force exactly here (`float` package needed) |
| `!` | Override LaTeX's spacing rules |

Default recommendation: `[htbp]`. For stubborn figures: `[!htbp]` or `[H]`.

---

## Caption Customization

```latex
\usepackage{caption}

% Caption style
\captionsetup{
    font=small,           % small font for caption
    labelfont=bf,         % "Figure 1:" in bold
    format=hang,          % hanging indent
    skip=5pt              % space between figure and caption
}

% Different style for tables
\captionsetup[table]{position=above}    % adjusts spacing for a caption placed above
\captionsetup[figure]{position=below}   % adjusts spacing for a caption placed below
```

These options do not move a caption. Place `\caption` before or after the content
in the source to select its actual position.

---

## List of Figures

```latex
\listoffigures    % generates list of all figures
```

---

## Path Configuration

If figures are in a subdirectory:

```latex
\graphicspath{{figures/}{images/}}   % search in these folders
```

---

## Controlling Float Spacing

If too many floats pile up at the end, use these in the preamble:

```latex
\setcounter{topnumber}{2}           % max floats at top of page
\setcounter{bottomnumber}{2}        % max floats at bottom
\setcounter{totalnumber}{4}         % max floats per page
\renewcommand{\topfraction}{0.9}    % max fraction for top floats
\renewcommand{\textfraction}{0.1}   % min fraction for text
```

Or force all pending floats to appear now:

```latex
\clearpage    % flush all floats, start new page
\FloatBarrier % flush floats without page break (requires placeins package)
```

---

## Figure Without Floating (Non-Float)

If you need a figure exactly here with no floating:

```latex
\begin{center}
    \includegraphics[width=0.6\linewidth]{fig}
    \captionof{figure}{Caption here.}   % requires caption package
\end{center}
```

---

## Cross-Referencing

```latex
As shown in Figure~\ref{fig:example}, ...
See Figures~\ref{fig:sub1} and~\ref{fig:sub2}.
```

The `~` is a non-breaking space — keeps "Figure" and the number together.
