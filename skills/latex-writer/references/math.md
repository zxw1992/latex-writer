# Math Formulas & Symbols Reference

## Math Environments

| Environment | Usage | Notes |
|-------------|-------|-------|
| `$...$` | Inline formula | `$E = mc^2$` |
| `\(...\)` | Inline formula | Preferred over `$...$` in modern LaTeX |
| `\[...\]` | Display (unnumbered) | Centered, own line |
| `equation` | Display (numbered) | Single equation |
| `equation*` | Display (unnumbered) | `\usepackage{amsmath}` |
| `align` | Multiple aligned equations | Use `&` for alignment point |
| `align*` | Aligned, unnumbered | |
| `gather` | Centered multiple lines | No alignment |
| `multline` | Long equation split across lines | |
| `cases` | Piecewise functions | |

```latex
% Aligned equations
\begin{align}
    f(x) &= x^2 + 2x + 1 \\
         &= (x+1)^2
\end{align}

% Piecewise function
f(x) = \begin{cases}
    x^2  & \text{if } x \geq 0 \\
    -x   & \text{if } x < 0
\end{cases}

% Long equation
\begin{multline}
    \int_0^\infty f(x)\,dx = \lim_{n\to\infty} \sum_{k=0}^{n} f(x_k) \Delta x \\
    = \text{(Riemann sum)}
\end{multline}
```

---

## Greek Letters

| Symbol | Command | Symbol | Command |
|--------|---------|--------|---------|
| α | `\alpha` | Α | `A` (use roman A) |
| β | `\beta` | Β | `B` |
| γ | `\gamma` | Γ | `\Gamma` |
| δ | `\delta` | Δ | `\Delta` |
| ε | `\epsilon` / `\varepsilon` | Ε | `E` |
| ζ | `\zeta` | | |
| η | `\eta` | | |
| θ | `\theta` / `\vartheta` | Θ | `\Theta` |
| ι | `\iota` | | |
| κ | `\kappa` / `\varkappa` | | |
| λ | `\lambda` | Λ | `\Lambda` |
| μ | `\mu` | | |
| ν | `\nu` | | |
| ξ | `\xi` | Ξ | `\Xi` |
| π | `\pi` / `\varpi` | Π | `\Pi` |
| ρ | `\rho` / `\varrho` | | |
| σ | `\sigma` / `\varsigma` | Σ | `\Sigma` |
| τ | `\tau` | | |
| υ | `\upsilon` | Υ | `\Upsilon` |
| φ | `\phi` / `\varphi` | Φ | `\Phi` |
| χ | `\chi` | | |
| ψ | `\psi` | Ψ | `\Psi` |
| ω | `\omega` | Ω | `\Omega` |

---

## Superscripts, Subscripts, Accents

```latex
x^2           % x squared
x^{n+1}       % multi-char superscript → use braces
x_i           % subscript i
x_{ij}        % multi-char subscript
x_i^2         % both
{}^n C_r      % superscript before letter

% Accents
\bar{x}       % x̄  — mean
\hat{x}       % x̂  — estimate
\tilde{x}     % x̃  — tilde
\vec{x}       % x⃗  — vector
\dot{x}       % ẋ  — time derivative
\ddot{x}      % ẍ  — second derivative
\overline{AB} % overline spanning multiple
\underline{x} % underline
\widehat{abc} % wide hat
\widetilde{abc}

% Primes
f'            % f prime
f''           % f double prime
f^{\prime}    % same as f'
```

---

## Fractions and Binomials

```latex
\frac{numerator}{denominator}   % standard fraction
\dfrac{a}{b}                    % display-style fraction (larger, for inline use)
\tfrac{a}{b}                    % text-style fraction (smaller, for display use)
\cfrac{a}{b + \cfrac{c}{d}}     % continued fraction

\binom{n}{k}                    % binomial coefficient C(n,k)
\dbinom{n}{k}                   % display-style binomial
```

---

## Operators and Functions

```latex
% Standard functions (use these, not plain text)
\sin, \cos, \tan, \sec, \csc, \cot
\arcsin, \arccos, \arctan
\sinh, \cosh, \tanh
\log, \ln, \lg, \exp
\lim, \inf, \sup, \max, \min
\det, \deg, \dim, \ker, \gcd
\Pr  % probability

% Limits
\lim_{x \to \infty}
\lim_{n \to 0^+}    % one-sided

% Custom operator
\DeclareMathOperator{\argmax}{argmax}
\DeclareMathOperator*{\argmin}{argmin}  % * puts subscript below in display
```

---

## Sums, Products, Integrals

```latex
\sum_{i=1}^{n} a_i             % sum
\prod_{k=0}^{\infty} f(k)      % product
\int_0^1 f(x)\,dx              % integral (\, for spacing before dx)
\iint, \iiint                   % double/triple integral
\oint                           % contour integral
\int_{\mathbb{R}^n}

% Display style forces big operators inline
\displaystyle\sum_{i=1}^n
```

---

## Relations and Arrows

```latex
% Equality and inequality
= \neq \approx \sim \simeq \equiv \cong \propto

% Order
< > \leq \geq \ll \gg \leqslant \geqslant

% Set relations
\in \notin \subset \subseteq \supset \supseteq

% Arrows
\to \leftarrow \leftrightarrow
\Rightarrow \Leftarrow \Leftrightarrow  % logical implication
\rightarrow \longrightarrow
\uparrow \downarrow \updownarrow
\mapsto                                  % x \mapsto f(x)
\xrightarrow{label}                      % labeled arrow
\xleftarrow{label}
```

---

## Brackets and Delimiters

```latex
% Auto-sizing with \left and \right
\left( \frac{a}{b} \right)
\left[ x \right]
\left\{ S \right\}          % curly braces need backslash
\left| x \right|            % absolute value
\left\| x \right\|          % norm
\left\langle v \right\rangle % angle brackets
\left\lfloor x \right\rfloor % floor
\left\lceil x \right\rceil   % ceiling

% Manual sizing: \big, \Big, \bigg, \Bigg
\bigg( \frac{a}{b} \bigg)
```

---

## Matrices

```latex
\usepackage{amsmath}

% Parentheses
\begin{pmatrix} a & b \\ c & d \end{pmatrix}

% Brackets
\begin{bmatrix} a & b \\ c & d \end{bmatrix}

% Vertical bars (determinant)
\begin{vmatrix} a & b \\ c & d \end{vmatrix}

% Double bars
\begin{Vmatrix} a & b \\ c & d \end{Vmatrix}

% No delimiters
\begin{matrix} a & b \\ c & d \end{matrix}

% Large matrix with dots
\begin{pmatrix}
  a_{11} & a_{12} & \cdots & a_{1n} \\
  a_{21} & a_{22} & \cdots & a_{2n} \\
  \vdots & \vdots & \ddots & \vdots \\
  a_{m1} & a_{m2} & \cdots & a_{mn}
\end{pmatrix}
```

---

## Math Fonts

```latex
\mathbf{x}        % bold (vectors/matrices): x
\mathit{x}        % italic (default in math mode)
\mathrm{x}        % roman (upright): useful for units, constants
\mathsf{x}        % sans-serif
\mathtt{x}        % typewriter
\mathcal{A}       % calligraphic: 𝒜 (uppercase only)
\mathbb{R}        % blackboard bold: ℝ (requires amssymb)
\mathfrak{g}      % fraktur: 𝔤 (requires amssymb)
\boldsymbol{\mu}  % bold Greek/symbols (requires amsmath/bm)
```

Common blackboard bold: `\mathbb{R, C, Z, N, Q, F, E}` (reals, complex, integers, naturals, rationals, field, expectation)

---

## Spacing in Math Mode

```latex
\,   % thin space (before dx in integrals)
\:   % medium space
\;   % thick space
\!   % negative thin space
\quad   % 1em space
\qquad  % 2em space
\ (backslash-space) % normal space
```

---

## Numbering and Labels

```latex
\begin{equation}
    E = mc^2 \label{eq:einstein}
\end{equation}

See Equation~\eqref{eq:einstein}.  % produces (1)

% Suppress number for one equation in align
\begin{align}
    a &= b \\
    c &= d \notag   % this line has no number
\end{align}
```

---

## Common Symbols Quick Reference

```latex
\infty       % ∞
\partial     % ∂  (partial derivative)
\nabla       % ∇  (gradient)
\forall      % ∀
\exists      % ∃
\emptyset    % ∅
\varnothing  % ∅ (rounder variant)
\pm          % ±
\mp          % ∓
\times       % ×
\cdot        % ·  (multiplication dot)
\circ        % ∘  (function composition)
\cup \cap    % ∪ ∩
\setminus    % \  (set difference)
\triangle    % △
\angle       % ∠
\perp        % ⊥
\parallel    % ∥
\because     % ∵  (requires amssymb)
\therefore   % ∴  (requires amssymb)
\ldots       % …  (baseline dots)
\cdots       % ⋯  (centered dots)
\vdots       % ⋮  (vertical dots)
\ddots       % ⋱  (diagonal dots)
```
