# 中文文档配置参考

## 标准最小 Preamble

```latex
\documentclass[UTF8, a4paper, 12pt, fontset=fandol]{ctexart}

% 数学
\usepackage{amsmath, amssymb, amsthm}

% 图片
\usepackage{graphicx}
\usepackage{float}

% 表格
\usepackage{booktabs}
\usepackage{multirow}

% 超链接（放在最后）
\usepackage[colorlinks, linkcolor=blue, citecolor=blue, urlcolor=blue]{hyperref}

\title{文章标题}
\author{作者姓名}
\date{\today}

\begin{document}
\maketitle

内容……

\end{document}
```

**编译方式：XeLaTeX 或 LuaLaTeX**；新建普通中文文档默认推荐 XeLaTeX。
此模板使用 TeX 发行版可提供的 Fandol 字体，适合没有指定字体要求的文档。
已有学校或期刊模板应保留其文档类、引擎和字体要求。已有正常工作的
pdfLaTeX+CJK 工程也无需仅因正文含中文而切换引擎。

## 保留已有文档类

先检查模板是否已有中文支持。以下为在普通 `article` 中补充中文支持的完整示例；
用于第三方文档类前，应检查该模板的宏包限制和版式要求。

```latex
\documentclass{article}
\usepackage[UTF8, scheme=plain, fontset=fandol]{ctex}
\begin{document}
\section{An English Heading}
保留原有文档类，并加入中文说明。
\end{document}
```

`scheme=plain` 避免套用完整的中文文档格式方案；它不代表任意模板都自动兼容。

## 中文 Beamer 模板

Beamer 使用 `frame` 环境，并已加载 `hyperref` 和定理支持。使用专门的模板，
不要把 article 的导言区直接复制过来或重复加载带不同选项的 `hyperref`。

```latex
\documentclass[UTF8, fontset=fandol, aspectratio=169]{ctexbeamer}
\usetheme{Madrid}
\hypersetup{colorlinks=false}
\title{中文学术报告}
\author{作者姓名}
\date{\today}
\begin{document}
\begin{frame}
  \titlepage
\end{frame}
\begin{frame}{主要结果}
  \begin{theorem}
    对任意实数 $x$，有 $x^2 \geq 0$。
  \end{theorem}
\end{frame}
\end{document}
```

---

## 文档类选项

```latex
\documentclass[UTF8, a4paper, zihao=-4, fontset=fandol]{ctexart}
```

| 选项 | 说明 |
|------|------|
| `UTF8` | 显式声明 UTF-8 编码；当前常用引擎下通常已是默认值 |
| `a4paper` | A4 纸张 |
| `12pt` | 基础字号 |
| `fontset=fandol` | 使用可移植的 Fandol 字体方案，适用于 XeLaTeX / LuaLaTeX |
| `zihao=-4` | 正文字号为小四（学术论文常用）。与 `10pt`/`11pt`/`12pt` 二选一，不要同时指定 |
| `oneside` / `twoside` | 单面 / 双面排版 |
| `linespread=1.5` | 1.5 倍行距（放在选项里或用 `\linespread{1.5}\selectfont`） |

---

## 各文档类适用场景

| 类名 | 对应 | 适用场景 |
|------|------|---------|
| `ctexart` | article | 期刊论文、技术报告、短文 |
| `ctexrep` | report | 毕业论文、长篇报告 |
| `ctexbook` | book | 书籍、教材 |
| `ctexbeamer` | beamer | 幻灯片、学术报告 |

---

## 字体设置

ctex 会按操作系统选择默认字体，但这不保证所选字体在当前机器上可用。
例如旧版本的 macOS 字体方案可能在加载文档类时就因缺少 `STHeiti` 报错。
这时在导言区后面写 `\setCJKmainfont` 已来不及；应在加载类或宏包时选择
`fontset=fandol`，或使用 `fontset=none` 并完整配置所需字体族。

**无指定字体要求的文档：**优先使用前面的 Fandol 模板。若包或字体未安装，
检查 `ctex` 和 `fandol` 是否可用，并明确提示缺失依赖。

**可选系统字体：**先用 `\IfFontExistsTF` 检查可用性，保留 Fandol 作为回退。
以下为 XeLaTeX 示例；CTeX 也为 LuaLaTeX 提供这些中文字体设置命令。

```latex
\documentclass[UTF8, fontset=fandol]{ctexart}
\IfFontExistsTF{Songti SC}{\setCJKmainfont{Songti SC}}{}
\IfFontExistsTF{Heiti SC}{\setCJKsansfont{Heiti SC}}{}
\begin{document}
字体存在时使用系统字体，否则保持 Fandol。\textsf{无衬线文字。}
\end{document}
```

Windows 可检查 `SimSun` / `SimHei`；Linux 可检查 `Noto Serif CJK SC` /
`Noto Sans CJK SC`。不要仅根据操作系统假设字体存在。

**学校或期刊指定字体：**先检查要求和字体安装情况；缺失时告知用户。
Fandol 可用于说明清楚的临时预览，但不能把替代字体的结果称为满足指定字体要求。

---

## 中文格式命令

```latex
% 字号
\zihao{-4}   % 小四
\zihao{3}    % 三号
\zihao{5}    % 五号

% 字体
\textbf{加粗}      % 粗体
\textit{斜体}      % 斜体（中文斜体效果有限，慎用）
\kaishu{楷书}      % 楷体
\heiti{黑体}       % 黑体
\fangsong{仿宋}    % 仿宋
\songti{宋体}      % 宋体
```

---

## 行距与段落

```latex
\usepackage{setspace}
\onehalfspacing      % 1.5 倍行距
\doublespacing       % 2 倍行距

% 或者直接设置
\linespread{1.6}\selectfont

% 段间距（不建议同时用 \parskip 和 \parindent 调整，ctex 已经处理好了）
\setlength{\parskip}{0.5em}
```

---

## 页边距

```latex
\usepackage{geometry}
\geometry{
    top=2.5cm, bottom=2.5cm,
    left=2.5cm, right=2.5cm
}
```

---

## 定理环境（中文）

```latex
\usepackage{amsthm}
\newtheorem{theorem}{定理}[section]
\newtheorem{lemma}[theorem]{引理}
\theoremstyle{definition}
\newtheorem{definition}{定义}[section]
\theoremstyle{plain}
\newtheorem{corollary}[theorem]{推论}
\theoremstyle{remark}
\newtheorem{remark}{注}
\theoremstyle{definition}
\newtheorem{example}{例}[section]
\renewcommand{\proofname}{证明}
```

使用：
```latex
\begin{theorem}
    设 $f$ 是……
\end{theorem}
\begin{proof}
    证明如下……
\end{proof}
```

---

## 章节标题格式

ctex 提供中文章节格式，默认格式随文档类与方案而异。自定义示例：

```latex
\ctexset{
    section = {
        format = \Large\bfseries,
        name = {第,节},
        number = \chinese{section},
    },
    subsection = {
        format = \large\bfseries,
    }
}
```

---

## 常见问题

**Q：编译报错 "Package inputenc Error"**
A：检查文件编码、实际编译引擎和中文宏包是否匹配；`UTF8` 选项本身不会添加字体或中文支持。

**Q：中文字符不显示/乱码**
A：检查中文支持、字体是否存在、字体是否覆盖缺失字符，以及日志里的 `Missing character`；按已有工程选择引擎。参考 `errors.md`。

**Q：数学公式中的中文（如"其中"）**
A：使用 `\text{其中}` 或 `\mbox{其中}`，不要在数学模式中直接写汉字。
