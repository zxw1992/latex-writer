# 中文研究报告示例

原始需求见 [PROMPT.md](PROMPT.md)。最终文件：[PDF](main.pdf)、[LaTeX](main.tex)、[参考文献数据](refs.bib)。

这是 2026-09-19 实际场景展示中的两页研究方案样稿。包含中英文摘要、数学推导、TikZ 流程图、三线表、PGFPlots 曲线、交叉引用和 BibTeX 文献。演示数值不是真实实验结果。

原始制作经历了编译和版面修订：初版流程图被推到独立页面，缩紧标题区域后恢复到研究问题所在页。这个例子展示最终产物，不衡量一次生成成功率，也不能单独证明 skill 对模型质量的提升。

在本目录运行：

```bash
latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex
```

需要 XeLaTeX、latexmk、BibTeX，以及源码所用的 ctex/Fandol、TikZ、PGFPlots 等宏包。README 展示图为本案例最终 PDF 的逐页渲染，不是重新绘制的宣传图。
