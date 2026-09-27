# English Document Setup Reference

## Standard Minimal Preamble

```latex
\documentclass[a4paper, 12pt]{article}  % For slides, use the dedicated Beamer example below.

% Math
\usepackage{amsmath, amssymb, amsthm}

% Fonts (recommended for modern output)
\usepackage[T1]{fontenc}
\usepackage{lmodern}

% Figures
\usepackage{graphicx}
\usepackage{float}

% Tables
\usepackage{booktabs}
\usepackage{multirow}

% Hyperlinks (load last)
\usepackage[colorlinks, linkcolor=blue, citecolor=blue, urlcolor=blue]{hyperref}

\title{Document Title}
\author{Author Name}
\date{\today}

\begin{document}
\maketitle

Content here.

\end{document}
```

**Compilation:** pdfLaTeX or XeLaTeX (either works for pure English)

Preserve the class and package requirements of an existing venue template.
Beamer and specialized journal classes need their own setups; changing only the
class name in this generic preamble can cause conflicts with packages they load.

---

## Document Classes

### `article` — Papers, notes, short documents

```latex
\documentclass[a4paper, 12pt]{article}
% Sections: \section, \subsection, \subsubsection
% No \chapter
```

### `report` — Theses, long reports

```latex
\documentclass[a4paper, 12pt, oneside]{report}
% Sections: \chapter, \section, \subsection
% Chapters begin on a new page
```

### `book` — Books, textbooks

```latex
\documentclass[a4paper, 12pt, twoside, openright]{book}
% Two-sided layout, chapters on right-hand pages
```

### `beamer` — Presentation slides

```latex
\documentclass{beamer}
\usetheme{Madrid}        % or: Copenhagen, Warsaw, Singapore, ...
\usecolortheme{default}  % or: orchid, beaver, seahorse, ...

\title{Presentation Title}
\author{Author}
\institute{University}
\date{\today}

\begin{document}
\begin{frame}
    \titlepage
\end{frame}

\begin{frame}{Slide Title}
    Content here.
\end{frame}
\end{document}
```

### `amsart` — AMS journal style

```latex
\documentclass{amsart}
% Produces journal-style formatting
% Uses \address, \email, \subjclass, \keywords in preamble
```

---

## Common Class Options

| Option | Effect |
|--------|--------|
| `a4paper` / `letterpaper` | Paper size |
| `12pt` / `11pt` / `10pt` | Base font size |
| `oneside` / `twoside` | Page layout |
| `draft` | Shows overfull boxes as black bars (debugging) |
| `twocolumn` | Two-column layout |
| `fleqn` | Left-align display equations |
| `leqno` | Equation numbers on the left |

---

## Page Geometry

```latex
\usepackage{geometry}
\geometry{
    top=2.5cm, bottom=2.5cm,
    left=3cm, right=3cm
}
```

---

## Line Spacing

```latex
\usepackage{setspace}
\doublespacing       % Double spacing (common requirement for submissions)
\onehalfspacing      % 1.5x spacing
```

---

## Fonts

**Default (Computer Modern):** No extra packages needed.

**Latin Modern (slightly better CM):**
```latex
\usepackage[T1]{fontenc}
\usepackage{lmodern}
```

**Times-like font:**
```latex
\usepackage{mathptmx}  % Times for text and math
```

**Palatino-like:**
```latex
\usepackage{mathpazo}
```

**With XeLaTeX, system fonts work:**
```latex
\usepackage{fontspec}
\setmainfont{Palatino}
```

---

## Theorem Environments

```latex
\usepackage{amsthm}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{definition}
\newtheorem{definition}{Definition}[section]
\newtheorem{example}{Example}[section]
\theoremstyle{remark}
\newtheorem{remark}{Remark}
```

Usage:
```latex
\begin{theorem}[Optional name]
    Let $f$ be a function...
\end{theorem}
\begin{proof}
    We proceed by...
\end{proof}
```

---

## Abstract

```latex
\begin{abstract}
    This paper presents...
\end{abstract}
```

---

## Common Section Commands

| Command | Level | Available in |
|---------|-------|-------------|
| `\part{...}` | -1 | book, report |
| `\chapter{...}` | 0 | book, report |
| `\section{...}` | 1 | all |
| `\subsection{...}` | 2 | all |
| `\subsubsection{...}` | 3 | all |
| `\paragraph{...}` | 4 | all |
| `\subparagraph{...}` | 5 | all |

Use `*` variant (e.g., `\section*{Introduction}`) to suppress numbering.
