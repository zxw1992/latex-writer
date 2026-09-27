---
name: latex-writer
description: >-
  Create, edit, and debug LaTeX documents, formulas, tables, TikZ diagrams, and
  bibliographies in English or Chinese. Use for .tex projects, LaTeX/Overleaf
  typesetting requests, and images the user wants transcribed into LaTeX.
  Preserve existing templates and report compilation and visual checks performed.
---

# LaTeX Writing Assistant

## Reference Files (read as needed)

| Topic | File | When to read |
|-------|------|--------------|
| Chinese document setup | `references/zh-setup.md` | Chinese content, fonts, Chinese Beamer |
| English document setup | `references/en-setup.md` | New English document from scratch |
| Math formulas & symbols | `references/math.md` | Equations, symbols, math environments |
| Tables | `references/tables.md` | tabular, booktabs, multirow, longtable |
| Figures & floats | `references/figures.md` | Images, subfigures, column widths, placement |
| TikZ drawings | `references/tikz.md` | Flowcharts, diagrams, function plots |
| Package recommendations | `references/packages.md` | Package selection and compatibility |
| Bibliography | `references/bibliography.md` | Citations, BibTeX, biblatex, GB/T 7714 |
| Compilation errors | `references/errors.md` | Error messages, debugging |
| Image → LaTeX extraction | `references/multimodal-workflow.md` | Image transcription |
| Build and visual checks | `references/verification.md` | Complete documents, project edits, compilation fixes |

Read only the references needed for the current task.

## 1. Establish the Document Context

**For an existing project, inspect before changing it.** Identify the main `.tex`
file, document class and options, build configuration or engine directive,
bibliography backend, existing packages/macros, and relevant assets. Preserve the
class, engine, citation system, labels, file structure, and institution/venue
formatting unless the requested change requires otherwise. Make the smallest
relevant edit. Do not replace a project with a generic template or overwrite an
existing `.bib` file with sample entries.

**Decide language from the content to be typeset.** A Chinese request for an English
paper still needs an English document. Chinese text, a Chinese venue, or a GB/T
bibliography does not by itself require changing the document class or engine.

For a new document without a required template:

| Content / document | Default |
|--------------------|---------|
| English paper or notes | `article`, pdfLaTeX |
| Chinese paper or notes | `ctexart`, XeLaTeX, portable fonts from `zh-setup.md` |
| Longer Chinese report / book | `ctexrep` / `ctexbook` |
| Chinese slides | Dedicated `ctexbeamer` example in `zh-setup.md` |
| English slides | Dedicated `beamer` example in `en-setup.md` |
| Specific venue / institution | Its supplied class, engine, and bibliography rules |

Keep an existing LuaLaTeX or working pdfLaTeX+CJK configuration. When Chinese
support is missing, consider adding `ctex` with `scheme=plain` or the appropriate
CJK package to the existing class; check compatibility first. Use portable fonts
for unconstrained new documents, and check availability before selecting system
fonts. Explain missing required fonts instead of silently substituting them.

Ask only when missing requirements materially change the result; otherwise use a
reasonable default and state it briefly.

## 2. Route the Task

| User intent | Action |
|-------------|--------|
| Create a document | Choose the required class, read the setup reference, produce a complete document |
| Modify an existing project | Inspect its configuration, edit in place, verify the affected output |
| Typeset one element | Read its reference; provide a snippet with package dependencies |
| Transcribe an image | Read `multimodal-workflow.md`; preserve content and formatting, identify uncertainties |
| Debug compilation | Read `errors.md`; reproduce when possible, fix the earliest causal error, recompile |
| Configure citations | Read `bibliography.md`; keep the required backend and style |
| Choose packages / draw TikZ | Read `packages.md` or `tikz.md` as needed |

## 3. Produce and Verify the Output

Deliver the requested files or snippet with all necessary dependencies. For a
snippet, include missing preamble commands in a comment; reuse definitions already
present in the project. Include assets and bibliography data needed by a complete
document, and clearly label examples and unresolved content.

For full documents, project edits, and compilation fixes, use the available local
toolchain to compile the final version with the project's engine/backend. Follow
`references/verification.md` for logs, references, and rendered-page checks. A
small standalone snippet can receive a lighter check. If tools or dependencies
are unavailable, provide the usable source and explicitly state what was not
verified. Overleaf use does not rule out local verification when compatible tools
are available.

Briefly explain important choices and give the engine/build command when needed.
Report actual verification status: source prepared, compilation passed or failed,
citations checked, and pages visually checked. Do not equate a generated PDF with
correct content or correct layout.

## Transcription Accuracy

Preserve the source's mathematical content; do not silently correct or complete
it from mathematical expectations. Mark ambiguous readings next to the relevant
code with `% TODO: verify` and list the alternatives for the user. Compare all
source regions, including highlights, annotations, and diagram edges, with the
rendered output when possible. Describe any intentional simplifications.
