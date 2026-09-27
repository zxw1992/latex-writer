# Public package verification — 2026-09-27

## Scope

The release preserves the original `SKILL.md` and all eleven reference files byte-for-byte. Packaging adds installation documentation, the MIT license, and two unmodified page renders from the historical research-report example. The historical handwritten-image evaluation and its source image are excluded from the public package; eight behavioral cases remain.

## Checks performed

- README relative file links resolve.
- Both showcase PNG files match the original page renders byte-for-byte.
- The research report was rebuilt in an isolated directory with XeLaTeX, BibTeX and latexmk (TeX Live 2025), then rendered and both pages inspected. No visible clipping, missing glyphs or overlapping content was observed.
- The regression runner validated frontmatter via Ruby/Psych, reference paths and the eight public behavioral-case inputs. No model evaluations were run.
- Regression result: **18 passed, 1 failed, 0 skipped**. The failed case was `chinese_biber`: the installed macOS Biber executable failed before bibliography processing with `extracting arm64 binary with lipo failed (wstatus=256)`. A forced retry outside the sandbox reproduced the failure. This is an unresolved local toolchain limitation; the release does not claim a successful current Biber check.
- The standalone skill-creator validator could not start because its Python environment lacks PyYAML; metadata and reference validation above was performed by the regression runner instead.

This record does not establish client discovery, a model success rate, or a skill-versus-no-skill improvement. Installation checks are recorded below after fetching the published files.
