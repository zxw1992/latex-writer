#!/usr/bin/env python3
"""Compile reference examples and known failure cases without changing user projects.

Run: python3 evals/run_regressions.py [--output NEW_DIRECTORY]
Requires latexmk, the selected TeX engines/backends, and PyYAML or Ruby/Psych for
frontmatter validation. Missing tools are SKIPPED, never counted as passes.
PDF previews are generated when pdftoppm is available; they require visual review.
This checks fixtures/reference code, not a model's behavior on evals.json prompts.
"""

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import shutil
import subprocess
import tempfile


SKILL = Path(__file__).resolve().parents[1]


def provenance():
    files = [SKILL / "SKILL.md", Path(__file__).resolve(), SKILL / "evals/evals.json"]
    files += sorted((SKILL / "references").glob("*.md"))
    files += sorted(p for p in (SKILL / "evals/files").iterdir() if p.is_file() and not p.name.startswith("."))
    versions = {}
    for tool in ("xelatex", "lualatex", "pdflatex", "latexmk", "bibtex", "biber"):
        if shutil.which(tool):
            result = subprocess.run([tool, "--version"], capture_output=True, text=True, timeout=10)
            versions[tool] = (result.stdout + result.stderr).strip().splitlines()[0]
        else:
            versions[tool] = None
    return {"recorded_at": datetime.now(timezone.utc).isoformat(), "platform": platform.platform(),
            "python": platform.python_version(), "tools": versions,
            "input_sha256": {str(p.relative_to(SKILL)): hashlib.sha256(p.read_bytes()).hexdigest() for p in files}}


def block(filename, heading, index=0):
    """Read the actual example, so reference edits are exercised by compilation."""
    text = (SKILL / "references" / filename).read_text()
    start = text.index(heading) + len(heading)
    level = len(heading) - len(heading.lstrip("#"))
    end = re.search(r"(?m)^#{1," + str(level) + r"} ", text[start:])
    section = text[start : start + end.start()] if end else text[start:]
    return re.findall(r"```latex\n(.*?)```", section, re.S)[index]


def wrap(body, preamble="", options=""):
    options = "[" + options + "]" if options else ""
    return "\\documentclass" + options + "{article}\n" + preamble + "\n\\begin{document}\n" + body + "\n\\end{document}\n"


def read_frontmatter():
    source = (SKILL / "SKILL.md").read_text()
    match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", source, re.S)
    assert match, "Missing frontmatter delimiters"
    try:
        import yaml
    except ImportError:
        if not shutil.which("ruby"):
            raise FileNotFoundError("Install PyYAML or provide Ruby/Psych for YAML validation")
        parsed = subprocess.run(
            ["ruby", "-ryaml", "-rjson", "-e", "puts JSON.generate(YAML.safe_load(STDIN.read))"],
            input=match[1], text=True, capture_output=True, timeout=10,
        )
        assert parsed.returncode == 0, parsed.stderr
        data = json.loads(parsed.stdout)
    else:
        data = yaml.safe_load(match[1])
    assert isinstance(data, dict) and data.get("name") == SKILL.name
    assert isinstance(data.get("description"), str) and 0 < len(data["description"]) <= 1024
    for path in set(re.findall(r"references/[a-z-]+\.md", source)):
        assert (SKILL / path).is_file(), "Missing reference: " + path
    return "Valid YAML; name/description and reference paths checked"


def check_evals():
    data = json.loads((SKILL / "evals/evals.json").read_text())
    ids = [case["id"] for case in data["evals"]]
    assert len(ids) == len(set(ids)), "Duplicate eval IDs"
    for case in data["evals"]:
        assert case["prompt"] and case["expectations"]
        for filename in case["files"]:
            assert (SKILL / filename).is_file(), "Missing eval input: " + filename
    return str(len(ids)) + " behavioral cases have valid inputs; model runs not performed"


def compile_case(out, name, source, engine="pdflatex", bibliography=None, error=None):
    required = [engine] if error else [engine, "latexmk"]
    if bibliography:
        required.append(bibliography)
    missing = [tool for tool in required if not shutil.which(tool)]
    if missing:
        raise FileNotFoundError("Missing tools: " + ", ".join(missing))
    folder = out / name
    folder.mkdir()
    (folder / "main.tex").write_text(source)
    bib = (SKILL / "evals/files/existing-refs.bib").read_bytes()
    for filename in ("refs.bib", "existing-refs.bib"):
        (folder / filename).write_bytes(bib)
    flags = ["-interaction=nonstopmode", "-no-shell-escape"]
    if error:
        command = [engine] + flags + ["main.tex"]
    else:
        mode = {"xelatex": "-xelatex", "lualatex": "-lualatex", "pdflatex": "-pdf"}[engine]
        command = ["latexmk", "-norc", mode, "-halt-on-error", "-file-line-error"] + flags + ["main.tex"]
    run = subprocess.run(command, cwd=folder, capture_output=True, text=True, timeout=60)
    (folder / "console.txt").write_text(run.stdout + run.stderr)
    log = (folder / "main.log").read_text(errors="replace") if (folder / "main.log").exists() else run.stdout
    if error:
        pattern, count = error
        assert run.returncode != 0, "Expected compilation error was not raised"
        assert len(re.findall(pattern, log)) == count, "Unexpected error sequence; see main.log"
        return "Reproduced expected error sequence"
    assert run.returncode == 0 and (folder / "main.pdf").is_file(), "Compilation failed; see console.txt"
    issues = re.findall(r"(?m)^.*(?:Overfull \\[hv]box|Missing character:|LaTeX Warning:.*(?:undefined|multiply defined)|Package .* Warning:.*(?:undefined|Please \(re\)run|Empty bibliography)).*$", log)
    assert not issues, "Final-log issues: " + "; ".join(issues)
    for filename in ("refs.bib", "existing-refs.bib"):
        assert (folder / filename).read_bytes() == bib, "Bibliography input overwritten"
    if bibliography:
        assert (folder / "main.bbl").is_file(), "No generated bibliography"
        assert "knuth1984" in (folder / "main.bbl").read_text(), "Expected citation missing"
    if shutil.which("pdftoppm"):
        render = subprocess.run(["pdftoppm", "-scale-to", "1300", "-png", "main.pdf", "page"], cwd=folder, capture_output=True, timeout=30)
        assert render.returncode == 0, "PDF render failed"
    if name == "chinese_beamer" and shutil.which("pdfinfo"):
        info = subprocess.check_output(["pdfinfo", "main.pdf"], cwd=folder, text=True)
        assert re.search(r"Pages:\s+2\b", info), "Expected two slides"
    return "Compiled; final log and preserved bibliography inputs checked (previews need visual review)"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="New directory for sources, logs, PDFs, and results")
    args = parser.parse_args()
    if args.output:
        out = args.output.resolve()
        out.mkdir(parents=True, exist_ok=False)
    else:
        out = Path(tempfile.mkdtemp(prefix="latex-writer-regressions-"))
    # Keep Lua font caches outside both the skill and the result artifacts.
    cache = tempfile.mkdtemp(prefix="latex-writer-font-cache-")
    os.environ["TEXMFVAR"] = cache
    os.environ["TEXMFCACHE"] = cache
    results = []

    def check(name, callback):
        try:
            detail = callback()
            status = "passed"
        except FileNotFoundError as exc:
            status, detail = "skipped", str(exc)
        except Exception as exc:
            status, detail = "failed", str(exc)
        results.append(dict(name=name, status=status, detail=detail))
        print(status.upper() + " " + name + ": " + detail, flush=True)

    check("skill_frontmatter", read_frontmatter)
    check("behavioral_eval_inputs", check_evals)
    cases = []
    zh = block("zh-setup.md", "## 标准最小 Preamble")
    cases.extend([("chinese_xelatex", zh, "xelatex"), ("chinese_lualatex", zh, "lualatex")])
    cases.append(("existing_article_class", block("zh-setup.md", "## 保留已有文档类"), "xelatex"))
    cases.append(("chinese_beamer", block("zh-setup.md", "## 中文 Beamer 模板"), "xelatex"))
    font = block("zh-setup.md", "## 字体设置")
    cases.append(("optional_system_fonts", font, "xelatex"))
    cases.append(("missing_optional_fonts", font.replace("Songti SC", "MissingFontForRegression123").replace("Heiti SC", "MissingSansForRegression123"), "xelatex"))
    cases.append(("english_article", block("en-setup.md", "## Standard Minimal Preamble"), "pdflatex"))
    figure = block("figures.md", "## Basic Figure").replace("{filename}", "{example-image}")
    cases.append(("single_column_figure_in_two_columns", wrap(figure, r"\usepackage{graphicx}", "twocolumn"), "pdflatex"))
    subfigure = block("figures.md", "## Subfigures").replace("{fig1}", "{example-image}").replace("{fig2}", "{example-image}")
    pre, body = subfigure.split(r"\begin{figure}", 1)
    cases.append(("subfigures_in_two_columns", wrap(r"\begin{figure}" + body, r"\usepackage{graphicx}" + pre, "twocolumn"), "pdflatex"))
    table = block("tables.md", "## Auto-Width Tables — `tabularx`")
    pre, body = table.split(r"\begin{table}", 1)
    cases.append(("table_in_two_columns", wrap(r"\begin{table}" + body, r"\usepackage{booktabs}" + pre, "twocolumn"), "pdflatex"))
    cases.append(("valid_text_linebreak", wrap(r"This is a line \\ And another."), "pdflatex"))
    cases.append(("valid_multiparagraph_footnote", wrap(block("errors.md", "### `Runaway argument` / `! Paragraph ended before \\X was complete`", 2)), "pdflatex"))
    for name, source, engine in cases:
        check(name, lambda n=name, s=source, e=engine: compile_case(out, n, s, e))

    missing = (SKILL / "evals/files/missing-booktabs.tex").read_text()
    check("missing_booktabs_actual_log", lambda: compile_case(out, "missing_booktabs_actual_log", missing, "xelatex", error=(r"(?m)^! Undefined control sequence\.", 3)))
    fixed = missing.replace(r"\begin{document}", "\\usepackage{booktabs}\n\\begin{document}")
    check("missing_booktabs_fixed", lambda: compile_case(out, "missing_booktabs_fixed", fixed, "xelatex"))
    bad_rule = block("errors.md", "### `! Misplaced \\noalign` / `! Misplaced alignment tab character &`", 1)
    check("missing_row_terminator_actual_log", lambda: compile_case(out, "missing_row_terminator_actual_log", wrap(bad_rule, r"\usepackage{booktabs}"), error=(r"(?m)^! Misplaced \\noalign\.", 1)))
    bibpre = block("bibliography.md", "## Chinese Bibliography: GB/T 7714-2015")
    bibdoc = zh.replace(r"\begin{document}", bibpre + "\n\\begin{document}").replace("内容……", r"\nocite{knuth1984}\printbibliography")
    check("chinese_biber", lambda: compile_case(out, "chinese_biber", bibdoc, "xelatex", "biber"))
    ieee = (SKILL / "evals/files/existing-ieee.tex").read_text()
    check("existing_ieee_lualatex_bibtex", lambda: compile_case(out, "existing_ieee_lualatex_bibtex", ieee, "lualatex", "bibtex"))

    report = {"scope": "Reference/fixture regression checks; no model behavioral evaluation", "metadata": provenance(), "results": results}
    (out / "results.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print("Artifacts:", out)
    counts = {status: sum(r["status"] == status for r in results) for status in ("passed", "failed", "skipped")}
    print(json.dumps(counts))
    return 1 if counts["failed"] else (2 if counts["skipped"] else 0)


if __name__ == "__main__":
    raise SystemExit(main())
