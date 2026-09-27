# TikZ Drawing Reference

## Required Packages

```latex
\usepackage{tikz}
\usetikzlibrary{shapes.geometric, arrows.meta, positioning, calc, fit, backgrounds}
% Load more libraries as needed (see below)

\usepackage{pgfplots}   % function plots and data plots
\pgfplotsset{compat=1.18}
```

## Library Reference

| Library | Purpose |
|---------|---------|
| `arrows.meta` | Modern arrow tips |
| `shapes.geometric` | Diamond, ellipse, cylinder, etc. |
| `positioning` | `above of=`, `right=2cm of` |
| `calc` | Coordinate arithmetic `($(A)+(B)$)` |
| `fit` | Bounding box around nodes |
| `backgrounds` | Draw behind other elements |
| `matrix` | Matrix-of-nodes layout |
| `decorations.pathreplacing` | Braces, waves |
| `patterns` | Fill patterns (hatch, dots, etc.) |
| `shadows` | Drop shadows |

---

## Basic Shapes

```latex
\begin{tikzpicture}

% Lines and paths
\draw (0,0) -- (2,0) -- (2,1) -- cycle;   % triangle
\draw[->] (0,0) -- (3,0);                  % arrow
\draw[<->] (0,1) -- (3,1);                 % double arrow
\draw[dashed] (0,2) -- (3,2);             % dashed
\draw[thick, blue] (0,3) -- (3,3);        % styled

% Shapes
\draw (1,1) circle (0.5cm);               % circle
\draw (0,0) rectangle (2,1);             % rectangle
\draw (1,0) ellipse (1.5cm and 0.8cm);   % ellipse

% Filled shapes
\fill[blue!30] (0,0) rectangle (2,1);
\filldraw[fill=yellow, draw=orange] (1,1) circle (0.5);

% Curved paths
\draw (0,0) to[bend left=30] (2,1);
\draw (0,0) .. controls (1,2) and (2,2) .. (3,0);  % Bezier

\end{tikzpicture}
```

---

## Nodes (Labeled Boxes)

```latex
\begin{tikzpicture}

% Basic node
\node at (0,0) {Text};
\node[draw, rectangle] at (2,0) {Box};
\node[draw, circle] at (4,0) {Circle};

% Styled node
\node[draw, rounded corners, fill=blue!15, minimum width=2cm, minimum height=0.8cm]
    at (0,-2) {Styled};

% Named nodes for later referencing
\node[draw] (A) at (0,0) {A};
\node[draw] (B) at (3,0) {B};
\draw[->] (A) -- (B);              % connect by name
\draw[->] (A.east) -- (B.west);   % connect at anchor points

\end{tikzpicture}
```

**Common node anchors:** `north, south, east, west, north east, north west, south east, south west, center`

---

## Flowcharts

```latex
\usepackage{tikz}
\usetikzlibrary{shapes.geometric, arrows.meta, positioning}

% Define styles
\tikzset{
    startstop/.style = {rectangle, rounded corners, draw, fill=red!20,
                        minimum width=3cm, minimum height=0.8cm, text centered},
    process/.style   = {rectangle, draw, fill=blue!15,
                        minimum width=3cm, minimum height=0.8cm, text centered},
    decision/.style  = {diamond, draw, fill=yellow!20, aspect=2,
                        minimum width=3cm, text centered},
    arrow/.style     = {->, >=Stealth, thick},
}

\begin{tikzpicture}[node distance=1.5cm]

\node[startstop] (start) {Start};
\node[process, below=of start] (proc1) {Process Step};
\node[decision, below=of proc1] (dec1) {Condition?};
\node[process, below left=1.5cm and 1cm of dec1] (proc2) {Branch A};
\node[process, below right=1.5cm and 1cm of dec1] (proc3) {Branch B};
\node[startstop, below=3cm of dec1] (stop) {End};

\draw[arrow] (start) -- (proc1);
\draw[arrow] (proc1) -- (dec1);
\draw[arrow] (dec1) -- node[left] {Yes} (proc2);
\draw[arrow] (dec1) -- node[right] {No} (proc3);
\draw[arrow] (proc2) |- (stop);
\draw[arrow] (proc3) |- (stop);

\end{tikzpicture}
```

---

## Block Diagrams

```latex
\usetikzlibrary{positioning, arrows.meta}

\tikzset{
    block/.style = {rectangle, draw, fill=gray!10, text centered,
                    minimum height=1cm, minimum width=2.5cm},
    arrow/.style = {->, >=Stealth},
}

\begin{tikzpicture}[node distance=1.5cm, auto]

\node[block] (input)  {Input};
\node[block, right=of input]  (proc)  {Process};
\node[block, right=of proc]   (output) {Output};

\draw[arrow] (input) -- (proc);
\draw[arrow] (proc)  -- (output);

% Feedback loop
\draw[arrow] (output.south) -- ++(0,-0.8) -| (input.south);

\end{tikzpicture}
```

---

## Annotated Diagrams with Braces

```latex
\usetikzlibrary{decorations.pathreplacing}

\begin{tikzpicture}
\draw[thick] (0,0) -- (4,0);

% Brace above
\draw[decorate, decoration={brace, amplitude=5pt}]
    (0,0.1) -- (4,0.1) node[midway, above=5pt] {Total length};

% Brace below
\draw[decorate, decoration={brace, mirror, amplitude=5pt}]
    (0,-0.1) -- (2,-0.1) node[midway, below=5pt] {Half};

\end{tikzpicture}
```

---

## Function Plots (pgfplots)

```latex
\usepackage{pgfplots}
\pgfplotsset{compat=1.18}

% Simple function plot
\begin{tikzpicture}
\begin{axis}[
    xlabel={$x$}, ylabel={$y$},
    title={$y = \sin(x)$},
    grid=major,
    width=8cm, height=6cm,
    xmin=-3.14, xmax=3.14,
]
\addplot[blue, thick, smooth, domain=-3.14:3.14, samples=100]
    {sin(deg(x))};
\addplot[red, thick, smooth, domain=-3.14:3.14, samples=100]
    {cos(deg(x))};
\legend{$\sin(x)$, $\cos(x)$}
\end{axis}
\end{tikzpicture}

% Bar chart
\begin{tikzpicture}
\begin{axis}[
    ybar,
    xlabel={Category},
    ylabel={Value},
    symbolic x coords={A, B, C, D},
    xtick=data,
    bar width=0.4cm,
    ymin=0,
]
\addplot coordinates {(A,3) (B,7) (C,5) (D,9)};
\end{axis}
\end{tikzpicture}

% Scatter plot
\begin{tikzpicture}
\begin{axis}[xlabel={$x$}, ylabel={$y$}]
\addplot[only marks, mark=o] coordinates {
    (1,2) (2,3.5) (3,2.8) (4,5) (5,4.2)
};
\end{axis}
\end{tikzpicture}
```

---

## Coordinate Systems

```latex
% Cartesian (default)
(x, y)         % absolute
+(dx, dy)      % relative to previous
++(dx, dy)     % relative, and updates current point

% Polar
(angle:radius) % e.g., (45:2) = 2 units at 45°

% Named node reference
(A)            % center of node A
(A.east)       % east anchor of node A
($(A)!0.5!(B)$) % midpoint of A and B (calc library)
```

---

## Styles and Options Reference

```latex
% Colors
red, blue, green, cyan, magenta, yellow, black, white, gray, orange, violet
blue!50          % 50% blue mixed with white
blue!50!red      % 50% blue + 50% red
black!20         % 20% black = light gray

% Line styles
solid, dashed, dotted, densely dashed, loosely dotted

% Line width
thin, semithick, thick, very thick, ultra thick
line width=1.5pt

% Arrow tips (arrows.meta library)
->, <-, <->, -|, |-
>=Stealth, >=Latex, >=Triangle

% Fill and draw
\fill[blue] ...         % fill only
\draw[red] ...          % stroke only
\filldraw[fill=blue!20, draw=blue] ...  % both
```

---

## Practical Tips

**Positioning:** Use `positioning` library + `right=2cm of NodeName` instead of absolute coordinates when building connected diagrams.

**Reuse styles:** Define `\tikzset{...}` once at the top to avoid repeating options.

**Complex diagrams:** If a diagram is too complex for TikZ to reproduce accurately (e.g., detailed scientific schematics with many custom elements), use TikZ for the structural layout and mention what can't be faithfully reproduced.

**Standalone TikZ picture** (for testing):
```latex
\documentclass[tikz]{standalone}
\begin{document}
\begin{tikzpicture}
% your drawing
\end{tikzpicture}
\end{document}
```
