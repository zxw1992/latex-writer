# Build and Visual Verification

## Before compiling

- Identify the main file and the existing engine/backend from project instructions,
  `.latexmkrc`, editor directives, or a successful build log. Preserve those choices.
- Check required tools, packages, fonts, images, and `.bib` files. For Chinese font
  failures, read `zh-setup.md`; changing the engine alone does not install fonts.
- For a new document, compile in its output directory. For debugging downloaded
  examples or code containing `filecontents`, use a temporary project copy with
  its dependencies. An output-directory flag alone does not prevent source code
  from writing files. Never use `filecontents[overwrite]` for the user's bibliography.

## Compile the selected engine

With `latexmk`, choose the matching command; replace `main.tex` with the actual
entrypoint. These commands run the needed passes and bibliography backend.

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex
latexmk -xelatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
latexmk -lualatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
```

Use only the selected command. If `latexmk` is missing, use the available engine
directly: one initial pass, the configured BibTeX/Biber step when applicable, then
further passes until references settle. Keep the same engine across passes.
Tectonic is an alternative only for projects compatible with its engine and
available bundles; it is not a replacement for a required LuaLaTeX build.

For snippets, wrap the code with the relevant class and dependencies in a temporary
document. Use two-column mode when checking a snippet intended for one column of
a two-column paper. Do not silently enable shell escape to make a build pass;
identify whether the requested workflow actually needs an external command.

## Check the final logs

Read the final `.log` and, when used, `.blg` files after the build has converged.

- Fatal errors or a failed exit status: compilation has not passed, even if an old
  or partial PDF exists.
- Missing characters/fonts: inspect font coverage; a successful exit code can
  still hide missing text.
- Undefined citations/references, duplicate labels, empty required bibliography,
  or requests to rerun: resolve before calling references verified.
- Overfull boxes: locate the affected content and inspect it. Fix substantial
  overflow; document any deliberate exception rather than suppressing warnings.
- Underfull boxes: inspect consequential spacing; these are not automatically failures.

Debug the earliest causal error and rebuild. If the same failure repeats without
new evidence, explain the unresolved dependency or request the missing project
context instead of repeatedly changing unrelated packages.

## Inspect the rendered output

For complete documents with rendering tools available, render the final PDF and
inspect pages affected by the changes, including representative text, tables,
figures, citations, and slides. For short documents, inspect every page. Look for
clipping, overlap, wrong column widths, missing glyphs, tiny labels, misplaced
captions, and unexpected blank pages. Recheck after layout changes.

For image transcription, compare every source region with the corresponding
output, including main equations, limits/subscripts, highlights, and annotations.
A text extractor cannot validate these visual properties. If rendering is
unavailable, report that visual verification was not performed.

## Delivery status

Use brief factual statements: which engine built the final source, whether
citations resolved, which pages were inspected, and any remaining uncertainty.
If compilation was unavailable or failed, say so and provide the source plus the
exact dependency/error needed to complete verification. Do not claim compliance
with a journal or institution unless its supplied requirements were checked.
