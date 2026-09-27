# Bibliography Reference

## Two Systems: BibTeX vs biblatex

| | BibTeX | biblatex |
|--|--------|----------|
| Setup | `\bibliographystyle{style}` | `\usepackage[style=...]{biblatex}` |
| Citation | `\cite{key}` | `\cite{key}` (same) |
| Backend | bibtex | biber (recommended) or bibtex |
| Chinese support | Limited | Good (with `biblatex-gb7714-2015`) |
| Flexibility | Lower | Much higher |
| Common use | Legacy papers, IEEE, AMS | Modern projects, theses |

**Recommendation:**
- Existing projects and specific venues: preserve their required backend and style.
- New Chinese documents requiring GB/T 7714-2015: **biblatex + biblatex-gb7714-2015** is an option, unless the template specifies another setup.
- New unconstrained projects: biblatex with Biber is a useful default.

Chinese content alone does not determine the reference standard. Match the
required standard/version. Keep existing `.bib` entries; put illustrative data
in a separate example file, without `filecontents[overwrite]`. Clearly distinguish
sample metadata from verified references; this guide configures formatting and
does not establish that a cited source exists or supports a claim.

---

## BibTeX (Classic)

### Preamble

```latex
% No \usepackage needed for basic bibtex
% At end of document:
\bibliographystyle{plain}   % or: alpha, unsrt, abbrv, ieeetr, apalike
\bibliography{refs}         % refs.bib file (no extension)
```

### Citation Commands

```latex
\cite{key}           % [1] or [Author, Year]
\cite{key1, key2}    % multiple: [1, 2]
\nocite{key}         % include in bibliography but don't cite
\nocite{*}           % include all entries in .bib
```

### Compilation Order (BibTeX)

```
pdflatex main.tex
bibtex main       % (no .tex extension)
pdflatex main.tex
pdflatex main.tex
```

### Common Bibliography Styles

| Style | Format | Used by |
|-------|--------|---------|
| `plain` | Numbered, sorted by author | General |
| `alpha` | [Knu84] style labels | |
| `unsrt` | Numbered, citation order | |
| `abbrv` | Abbreviated first names | |
| `ieeetr` | IEEE numbered | IEEE journals |
| `apalike` | Author-year | Psychology, social sciences |
| `acm` | ACM style | ACM papers |
| `nature` | Nature journal | Nature |

---

## biblatex (Modern, Recommended)

### Preamble

```latex
\usepackage[
    backend=biber,          % recommended over bibtex
    style=authoryear,       % citation style
    sorting=nyt,            % sort by name, year, title
]{biblatex}
\addbibresource{refs.bib}  % .bib file (include extension)
```

### Citation Commands (biblatex)

```latex
\cite{key}           % full citation: (Author, Year) or [1]
\parencite{key}      % parenthetical: (Author, Year)
\textcite{key}       % Author (Year) — inline
\footcite{key}       % footnote citation
\autocite{key}       % adapts to style

\cite[p.~10]{key}                    % with page
\cite[see also][p.~10]{key}          % with prenote and page
\parencite{key1, key2}               % multiple
```

### Print Bibliography

```latex
\printbibliography
% or with title:
\printbibliography[title={References}]
% or by type:
\printbibliography[type=article, title={Journal Articles}]
\printbibliography[type=book, title={Books}]
```

### Compilation Order (biblatex + biber)

```
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```

This example uses pdfLaTeX throughout. For XeLaTeX or LuaLaTeX, replace **all three**
`pdflatex` calls with the selected engine. `biber main` takes the job name without
`.tex`. `latexmk` can orchestrate this sequence; see `verification.md`.

### Common biblatex Styles

| Style | Format |
|-------|--------|
| `numeric` | [1], [2] |
| `numeric-comp` | [1–3] |
| `authoryear` | (Author, Year) |
| `authoryear-comp` | (Author, Year1, Year2) |
| `alphabetic` | [Knu84] |
| `apa` | APA 7th |
| `ieee` | IEEE |
| `nature` | Nature |
| `gb7714-2015` | Chinese national standard |

---

## Chinese Bibliography: GB/T 7714-2015

Use when the project explicitly requires this standard and permits biblatex.

```latex
\usepackage[
    backend=biber,
    style=gb7714-2015,    % or gb7714-2015ay for author-year
]{biblatex}
\addbibresource{refs.bib}
```

Install: `biblatex-gb7714-2015` package (included in TeX Live 2019+).

Citation styles:
- `gb7714-2015` → sequential numbers [1]
- `gb7714-2015ay` → author-year (张三, 2020)

---

## The .bib File

### Common Entry Types

```bibtex
% Journal article
@article{einstein1905,
    author  = {Einstein, Albert},
    title   = {Zur Elektrodynamik bewegter {K}örper},
    journal = {Annalen der Physik},
    year    = {1905},
    volume  = {322},
    number  = {10},
    pages   = {891--921},
    doi     = {10.1002/andp.19053221004},
}

% Book
@book{knuth1984,
    author    = {Knuth, Donald E.},
    title     = {The {\TeX}book},
    publisher = {Addison-Wesley},
    year      = {1984},
    address   = {Reading, MA},
}

% Book chapter
@incollection{author2020,
    author    = {Author, Name},
    title     = {Chapter Title},
    booktitle = {Book Title},
    editor    = {Editor, Name},
    publisher = {Publisher},
    year      = {2020},
    pages     = {10--30},
}

% Conference paper
@inproceedings{vaswani2017,
    author    = {Vaswani, Ashish and others},
    title     = {Attention Is All You Need},
    booktitle = {Advances in Neural Information Processing Systems},
    year      = {2017},
    pages     = {5998--6008},
}

% PhD thesis
@phdthesis{author2021,
    author = {Author, Name},
    title  = {Thesis Title},
    school = {University Name},
    year   = {2021},
    type   = {PhD dissertation},
}

% Website / Online
@online{source2024,
    author  = {Author, Name},
    title   = {Page Title},
    year    = {2024},
    url     = {https://example.com},
    urldate = {2024-01-15},
}

% Technical report
@techreport{report2022,
    author      = {Author, Name},
    title       = {Report Title},
    institution = {Organization},
    year        = {2022},
    number      = {TR-2022-01},
}

% Chinese paper (bilingual fields for GB7714)
@article{zhang2020,
    author       = {张三 and 李四},
    title        = {论文标题},
    journal      = {期刊名称},
    year         = {2020},
    volume       = {10},
    number       = {2},
    pages        = {1--10},
    language     = {chinese},
}
```

### BibTeX Field Tips

- **Author format:** `Last, First and Last2, First2` or `First Last and First2 Last2`
- **Protect capitalization:** `{GPU}`, `{LaTeX}`, `{TikZ}` — prevents bibtex from lowercasing
- **Page ranges:** use `--` (en-dash): `pages = {10--25}`
- **"and others":** for many authors, use the `others` keyword: `Author, A. and others`

---

## Natbib (Common in Physics/Math Journals)

Some journals provide `.cls` files that use natbib. If so:

```latex
\usepackage{natbib}

% Citation commands:
\citet{key}     % Author (year) — textual
\citep{key}     % (Author, year) — parenthetical
\citet*{key}    % All authors textual
\citealp{key}   % Author, year (no parentheses)
\citealt{key}   % Author year (no comma, no parens)

% Bibliography
\bibliographystyle{plainnat}   % or abbrvnat, unsrtnat
\bibliography{refs}
```

---

## Hyperlinked References

With `hyperref` loaded, citations automatically become clickable links. If using biblatex:

```latex
\usepackage[backend=biber, style=authoryear]{biblatex}
\usepackage[colorlinks, citecolor=blue]{hyperref}   % load AFTER biblatex
```

biblatex detects hyperref automatically — just keep hyperref near the end of the preamble (the usual "hyperref loads last" rule).

---

## Troubleshooting

**"Citation undefined"** → Run the full compilation sequence again (latex → biber/bibtex → latex → latex).

**"I couldn't open database file refs.bib"** → Check the filename and that `\addbibresource{refs.bib}` matches exactly.

**Author name formatting wrong** → Use `Last, First` format in BibTeX. For Chinese names in GB7714, use the Chinese characters directly.

**biber not found** → Identify the missing Biber dependency. Do not silently switch
backends: the bibliography's data and style may require Biber. If installation is
unavailable, deliver the source with an explicit unverified-bibliography status.
