# Formal derivations

## Assumptions

**Assumption A1 (Tasks and time endowment).**
There are (n\in\mathbb{N}) tasks. A time allocation is a vector (t=(t_1,\dots,t_n)\in\mathbb{R}^n_+) satisfying
[
\sum_{i=1}^n t_i \le 1.
]

**Assumption A2 (Task productivities).**
A productivity vector is (A=(A_1,\dots,A_n)\in\mathbb{R}^n_{++}). Effective task outputs are
[
z_i \equiv A_i t_i,\qquad i=1,\dots,n.
]

**Assumption A3 (Output aggregator).**
The function (y:\mathbb{R}^n_+\to\mathbb{R}*+) is continuous and weakly increasing in each coordinate. Moreover, (y) is concave and (for duality and index-number identities) **linearly homogeneous**:
[
y(\lambda z)=\lambda y(z)\quad\text{for all }\lambda\ge 0,\ z\in\mathbb{R}^n*+.
]

**Assumption A4 (Differentiability for share formulas).**
When required, (y) is differentiable on (\mathbb{R}^n_{++}), and the associated unit-expenditure index (defined below) is differentiable on (\mathbb{R}^n_{++}).

---

## Definitions

**Definition D1 (Primal productivity level).**
Define the maximal output attainable under productivity (A) by
[
V(A);\equiv;\max_{t\in\mathbb{R}^n_+}; y(A_1 t_1,\dots,A_n t_n)\quad\text{s.t.}\quad \sum_{i=1}^n t_i\le 1.
]

**Definition D2 (Time prices).**
Define the vector of time prices (p=(p_1,\dots,p_n)\in\mathbb{R}^n_{++}) by
[
p_i \equiv \frac{1}{A_i}.
]

**Definition D3 (Time-price (consumption-form) problem).**
Define the equivalent problem
[
\widetilde V(p);\equiv;\max_{z\in\mathbb{R}^n_+}; y(z)\quad\text{s.t.}\quad \sum_{i=1}^n p_i z_i \le 1.
]

**Definition D4 (Expenditure function and unit-expenditure index).**
For (u\ge 0), define
[
e(p,u);\equiv;\min_{z\in\mathbb{R}^n_+}; p\cdot z \quad\text{s.t.}\quad y(z)\ge u.
]
Define the unit-expenditure index
[
P(p);\equiv;e(p,1).
]

**Definition D5 (Hicksian (compensated) demand and shares).**
Let (h(p,u)) denote any minimizer in the definition of (e(p,u)). Define Hicksian shares at ((p,u)) by
[
s_i^H(p,u);\equiv;\frac{p_i,h_i(p,u)}{e(p,u)}.
]
When (u=1), write (s_i^H(p)\equiv s_i^H(p,1)).

---

## Equivalence and duality

### Proposition 1 (Equivalence of the time-allocation and time-price formulations)

For every (A\in\mathbb{R}^n_{++}) and (p=1/A),
[
V(A) ;=; \widetilde V(p).
]

**Proof (structured).**

1. Fix (A\in\mathbb{R}^n_{++}) and define (p_i=1/A_i) for all (i).
2. For any feasible (t) in Definition D1, define (z_i\equiv A_i t_i). Then (z\in\mathbb{R}^n_+) and
[
\sum_{i=1}^n p_i z_i=\sum_{i=1}^n \frac{1}{A_i},(A_i t_i)=\sum_{i=1}^n t_i \le 1,
]
so (z) is feasible for Definition D3. Moreover (y(A\circ t)=y(z)). Hence (V(A)\le \widetilde V(p)).
3. Conversely, for any feasible (z) in Definition D3, define (t_i\equiv p_i z_i=z_i/A_i). Then (t\in\mathbb{R}^n_+) and (\sum_i t_i=\sum_i p_i z_i\le 1), so (t) is feasible for Definition D1. Moreover (A_i t_i = z_i), hence (y(A\circ t)=y(z)). Thus (\widetilde V(p)\le V(A)).
4. By 2 and 3, (V(A)=\widetilde V(p)). (\square)

---

### Proposition 2 (Productivity level as the reciprocal of a unit-expenditure index)

Under Assumption A3, for every (p\in\mathbb{R}^n_{++}),
[
\widetilde V(p) ;=; \frac{1}{P(p)}.
]
Equivalently, for every (A\in\mathbb{R}^n_{++}),
[
V(A);=;\frac{1}{P(1/A)}.
]

**Proof (structured).**

1. Fix (p\in\mathbb{R}^n_{++}). Consider the set ({z\ge 0: p\cdot z\le 1}). By linear homogeneity of (y), for any (\lambda>0),
[
y(\lambda z)=\lambda y(z).
]
2. Let (z^\star) attain (\widetilde V(p)) in Definition D3, and set (u^\star\equiv y(z^\star)=\widetilde V(p)). Then (p\cdot z^\star\le 1).
3. Define (\widehat z \equiv z^\star/u^\star). By linear homogeneity, (y(\widehat z)=1). Hence (\widehat z) is feasible for (P(p)=e(p,1)).
4. Compute its cost:
[
p\cdot \widehat z = p\cdot (z^\star/u^\star) = (p\cdot z^\star)/u^\star \le 1/u^\star.
]
Since (P(p)) is the minimum cost to reach (y(\cdot)\ge 1), 4 implies
[
P(p)\le \frac{1}{u^\star}=\frac{1}{\widetilde V(p)}.
]
Equivalently, (\widetilde V(p)\le 1/P(p)).
5. Conversely, let (z^H) attain (P(p)) with (y(z^H)\ge 1). By monotonicity of (y), one may take (y(z^H)=1). Define (\bar z\equiv z^H/P(p)). Then (p\cdot \bar z = 1) and, by linear homogeneity, (y(\bar z)=1/P(p)). Hence (\bar z) is feasible in Definition D3 and achieves (y(\bar z)=1/P(p)), so (\widetilde V(p)\ge 1/P(p)).
6. Combine 4–5 to conclude (\widetilde V(p)=1/P(p)). Substituting (p=1/A) yields (V(A)=1/P(1/A)). (\square)

---

## Exact productivity indices and revealed-preference bounds

### Proposition 3 (Exact productivity index between two productivity vectors)

Let (A,A'\in\mathbb{R}^n_{++}) and set (p=1/A), (p'=1/A'). Under Assumption A3,
[
\frac{V(A')}{V(A)} ;=; \frac{P(p)}{P(p')}.
]

**Proof (structured).**

1. By Proposition 2, (V(A)=1/P(p)) and (V(A')=1/P(p')).
2. Therefore,
[
\frac{V(A')}{V(A)}=\frac{1/P(p')}{1/P(p)}=\frac{P(p)}{P(p')}.
]
(\square)

---

### Proposition 4 (Laspeyres–Paasche bounds from observing baseline and/or post allocations)

Let (A,A'\in\mathbb{R}^n_{++}) with (p=1/A), (p'=1/A'). Assume A3. Let (t(A)) and (t(A')) denote optimal time shares in Definition D1. Define multipliers
[
m_i\equiv \frac{A_i'}{A_i}\qquad(i=1,\dots,n).
]
Then the exact productivity index satisfies
[
\boxed{\quad
\frac{1}{\sum_{i=1}^n t_i(A),\frac{1}{m_i}}
;\le;
\frac{V(A')}{V(A)}
;\le;
\sum_{i=1}^n t_i(A'),m_i
\quad}
]
where the lower bound uses only the baseline shares (t(A)), and the upper bound uses only the post shares (t(A')).

**Proof (structured).**

1. Let (u=1). Let (h(p,1)) and (h(p',1)) be Hicksian demands for unit output under prices (p) and (p'). Then
[
P(p)=p\cdot h(p,1),\qquad P(p')=p'\cdot h(p',1).
]
2. Since (h(p,1)) is feasible (achieves output (1)), it provides an upper bound on the minimum cost at prices (p'):
[
P(p') ;=; \min{p'\cdot z:\ y(z)\ge 1};\le; p'\cdot h(p,1).
]
Divide by (P(p)=p\cdot h(p,1)) to obtain
[
\frac{P(p')}{P(p)} ;\le; \frac{p'\cdot h(p,1)}{p\cdot h(p,1)}.
]
3. Similarly, since (h(p',1)) is feasible, it provides an upper bound on the minimum cost at prices (p):
[
P(p)=\min{p\cdot z:\ y(z)\ge 1};\le; p\cdot h(p',1).
]
Rearrange to obtain
[
\frac{P(p')}{P(p)} ;\ge; \frac{p'\cdot h(p',1)}{p\cdot h(p',1)}.
]
4. Combine 2–3 and invert to bound the productivity index (\Gamma\equiv V(A')/V(A)=P(p)/P(p')) (Proposition 3):
[
\frac{1}{\frac{p'\cdot h(p,1)}{p\cdot h(p,1)}}
;\le;
\Gamma
;\le;
\frac{1}{\frac{p'\cdot h(p',1)}{p\cdot h(p',1)}}.
]
5. Express the right-hand sides in shares. For unit output, the Hicksian share is
[
s_i^H(p)=\frac{p_i h_i(p,1)}{P(p)},\qquad s_i^H(p')=\frac{p_i' h_i(p',1)}{P(p')}.
]
Thus
[
\frac{p'\cdot h(p,1)}{p\cdot h(p,1)}=\sum_{i=1}^n s_i^H(p),\frac{p_i'}{p_i},
\qquad
\frac{p'\cdot h(p',1)}{p\cdot h(p',1)}=\frac{1}{\sum_{i=1}^n s_i^H(p'),\frac{p_i}{p_i'}}.
]
6. By Proposition 5 below (time shares coincide with Hicksian shares at the optimum under the unit time endowment), (s_i^H(p)=t_i(A)) and (s_i^H(p')=t_i(A')). Moreover (\frac{p_i'}{p_i}=\frac{A_i}{A_i'}=\frac{1}{m_i}) and (\frac{p_i}{p_i'}=m_i). Substitute into 5 and then into 4 to obtain the stated bounds. (\square)

---

## Welfare in time units (EV and CV)

### Proposition 5 (Equivalent and compensating variation measured in time)

Let (A,A'\in\mathbb{R}^n_{++}) with (p=1/A), (p'=1/A'). Define
[
EV \equiv e!\bigl(p,,V(A')\bigr)-1,\qquad
CV \equiv e!\bigl(p',,V(A)\bigr)-1.
]
Under Assumption A3,
[
EV=\frac{P(p)}{P(p')}-1,\qquad CV=\frac{P(p')}{P(p)}-1.
]

**Proof (structured).**

1. Under Assumption A3 (linear homogeneity), the expenditure function is homogeneous of degree (1) in the required output level:
[
e(p,u)=u,e(p,1)=u,P(p).
]
2. By Proposition 2, (V(A')=1/P(p')) and (V(A)=1/P(p)).
3. Compute
[
EV = e(p,V(A'))-1 = V(A'),P(p)-1 = \frac{1}{P(p')},P(p)-1=\frac{P(p)}{P(p')}-1.
]
4. Similarly,
[
CV = e(p',V(A))-1 = V(A),P(p')-1 = \frac{1}{P(p)},P(p')-1=\frac{P(p')}{P(p)}-1.
]
(\square)

---

## Share formulas: differentials, exact integrals, and approximations

### Proposition 6 (Time shares coincide with Hicksian shares)

Assume A3 and let (t(A)) be optimal in Definition D1. Let (p=1/A). Then the Hicksian shares at unit output satisfy
[
s_i^H(p) = t_i(A)\qquad(i=1,\dots,n).
]

**Proof (structured).**

1. Let (z^\star) solve Definition D3 under prices (p), and let (\widetilde V(p)=y(z^\star)). By Proposition 1, there exists an optimal (t(A)) with (z_i^\star=A_i t_i(A)).
2. Under monotonicity of (y), the budget constraint binds at the optimum in Definition D3: (p\cdot z^\star=1). (Otherwise a uniform expansion of (z^\star) would raise (y) without violating the constraint.)
3. Consider the unit-output Hicksian bundle (h(p,1)). By Proposition 2, (\widetilde V(p)=1/P(p)). By linear homogeneity, the scaled bundle (\widehat z \equiv z^\star/\widetilde V(p)=z^\star,P(p)) satisfies (y(\widehat z)=1). It is feasible for (P(p)=e(p,1)) and has cost
[
p\cdot \widehat z = p\cdot (z^\star P(p)) = (p\cdot z^\star)P(p)=1\cdot P(p)=P(p).
]
Hence (\widehat z) attains the minimum in (e(p,1)), so (h(p,1)=\widehat z=z^\star P(p)).
4. Compute Hicksian shares:
[
s_i^H(p)=\frac{p_i h_i(p,1)}{P(p)}=\frac{p_i (z_i^\star P(p))}{P(p)}=p_i z_i^\star.
]
5. Substitute (p_i=1/A_i) and (z_i^\star=A_i t_i(A)) to obtain (p_i z_i^\star=t_i(A)). Therefore (s_i^H(p)=t_i(A)). (\square)

---

### Proposition 7 (Differential share representation)

Assume A3–A4. Then
[
d\ln P(p) = \sum_{i=1}^n s_i^H(p), d\ln p_i.
]
Equivalently, with (p=1/A),
[
d\ln V(A) = \sum_{i=1}^n t_i(A), d\ln A_i.
]

**Proof (structured).**

1. By Shephard’s lemma under Assumption A4, for (u=1),
[
\frac{\partial P(p)}{\partial p_i} = h_i(p,1).
]
2. Compute the differential:
[
dP(p) = \sum_{i=1}^n \frac{\partial P(p)}{\partial p_i},dp_i = \sum_{i=1}^n h_i(p,1),dp_i.
]
3. Divide by (P(p)) and rewrite in log differentials:
[
d\ln P(p) = \frac{dP(p)}{P(p)} = \sum_{i=1}^n \frac{h_i(p,1),p_i}{P(p)}, d\ln p_i
= \sum_{i=1}^n s_i^H(p), d\ln p_i.
]
4. By Proposition 2, (\ln V(A)=-\ln P(1/A)). Hence
[
d\ln V(A) = - d\ln P(p)\quad\text{with }p_i=1/A_i,
]
and (d\ln p_i = - d\ln A_i). Therefore
[
d\ln V(A)=\sum_{i=1}^n s_i^H(p), d\ln A_i.
]
5. Apply Proposition 6 to substitute (s_i^H(p)=t_i(A)). (\square)

---

### Corollary 7.1 (First-order approximation using baseline time shares)

For a small change (A\to A'),
[
\ln\frac{V(A')}{V(A)} ;=; \sum_{i=1}^n t_i(A),\ln!\left(\frac{A_i'}{A_i}\right) ;+; o!\left(|A'-A|\right).
]

*Proof.* Immediate from Proposition 7 by evaluating (t_i(\cdot)) at (A) and applying a first-order expansion. (\square)

---

### Proposition 8 (Exact integral representation for large changes)

Assume A3–A4. Let (p(\tau)) be a differentiable path in (\mathbb{R}^n_{++}) with (p(0)=p) and (p(1)=p'). Then
[
\ln\frac{P(p')}{P(p)} = \int_0^1 \sum_{i=1}^n s_i^H!\bigl(p(\tau)\bigr),\frac{d}{d\tau}\ln p_i(\tau); d\tau.
]
Consequently, for (A(\tau)=1/p(\tau)),
[
\ln\frac{V(A')}{V(A)}
= \int_0^1 \sum_{i=1}^n t_i!\bigl(A(\tau)\bigr),\frac{d}{d\tau}\ln A_i(\tau); d\tau.
]

**Proof (structured).**

1. By Proposition 7, for each (\tau),
[
\frac{d}{d\tau}\ln P\bigl(p(\tau)\bigr)=\sum_{i=1}^n s_i^H!\bigl(p(\tau)\bigr),\frac{d}{d\tau}\ln p_i(\tau).
]
2. Integrate both sides from (\tau=0) to (\tau=1):
[
\ln P(p')-\ln P(p)=\int_0^1 \sum_{i=1}^n s_i^H!\bigl(p(\tau)\bigr),\frac{d}{d\tau}\ln p_i(\tau); d\tau.
]
3. Substitute (V(A)=1/P(1/A)) and (s_i^H(1/A)=t_i(A)) (Propositions 2 and 6), and use (\ln p_i(\tau)=-\ln A_i(\tau)). (\square)

---

### Corollary 8.1 (Single-component change)

Assume only (p_j) varies along the path and all (p_{-j}) are constant. Then
[
\ln\frac{P(p')}{P(p)} = \int_{\ln p_j}^{\ln p_j'} s_j^H!\bigl(p_j\bigr), d(\ln p_j).
]
Equivalently,
[
\ln\frac{V(A')}{V(A)} = \int_{\ln A_j}^{\ln A_j'} t_j!\bigl(A_j\bigr), d(\ln A_j),
]
holding (A_{-j}) fixed.

*Proof.* Specialize Proposition 8 to paths with only one varying coordinate. (\square)

---

### Proposition 9 (Törnqvist/Divisia trapezoid approximation)

Assume A3–A4. For a finite change (p\to p'), define average shares (\bar s_i\equiv \tfrac12(s_i^H(p)+s_i^H(p'))). Then the trapezoid approximation to Proposition 8 yields
[
\ln\frac{P(p')}{P(p)} \approx \sum_{i=1}^n \bar s_i ,\ln!\left(\frac{p_i'}{p_i}\right).
]
Equivalently, defining (\bar t_i\equiv \tfrac12(t_i(A)+t_i(A'))),
[
\ln\frac{V(A')}{V(A)} \approx \sum_{i=1}^n \bar t_i ,\ln!\left(\frac{A_i'}{A_i}\right).
]

**Proof (structured).**

1. By Proposition 8,
[
\ln\frac{P(p')}{P(p)} = \int_0^1 \sum_{i=1}^n s_i^H!\bigl(p(\tau)\bigr),\frac{d}{d\tau}\ln p_i(\tau); d\tau
]
for any differentiable path (p(\tau)) from (p) to (p').
2. Choose the log-linear path (\ln p_i(\tau)=(1-\tau)\ln p_i + \tau \ln p_i'). Then (\frac{d}{d\tau}\ln p_i(\tau)=\ln(p_i'/p_i)) is constant in (\tau).
3. Under this path,
[
\ln\frac{P(p')}{P(p)} = \sum_{i=1}^n \left(\int_0^1 s_i^H!\bigl(p(\tau)\bigr),d\tau\right)\ln!\left(\frac{p_i'}{p_i}\right).
]
4. Approximate (\int_0^1 s_i^H(p(\tau)),d\tau) by the trapezoid rule:
[
\int_0^1 s_i^H!\bigl(p(\tau)\bigr),d\tau \approx \tfrac12\bigl(s_i^H(p)+s_i^H(p')\bigr)=\bar s_i.
]
Substitute into 3.
5. The (V)-form follows from (p_i'/p_i=(A_i/A_i')) and (s_i^H(1/A)=t_i(A)). (\square)

---

## CES specialization and the two-good reduction

### Assumption C1 (CES aggregator)

For parameters (\sigma>0) and weights (\alpha_i>0), define
[
y(z)=\left(\sum_{i=1}^n \alpha_i, z_i^{\frac{\sigma-1}{\sigma}}\right)^{\frac{\sigma}{\sigma-1}}
\quad (\sigma\neq 1),
]
with the (\sigma=1) case defined by continuity (Cobb–Douglas).

---

### Proposition 10 (CES unit-expenditure index and CES Hicksian shares)

Under Assumption C1, the unit-expenditure index is
[
P(p)=\left(\sum_{i=1}^n \alpha_i^{\sigma}, p_i^{,1-\sigma}\right)^{\frac{1}{1-\sigma}},
]
and Hicksian shares at unit output are
[
s_i^H(p)=\frac{\alpha_i^{\sigma}, p_i^{,1-\sigma}}{\sum_{j=1}^n \alpha_j^{\sigma}, p_j^{,1-\sigma}}.
]

**Proof (structured).**

1. Consider the cost-minimization problem defining (P(p)=e(p,1)):
[
\min_{z\ge 0}; p\cdot z \quad\text{s.t.}\quad
\left(\sum_{i=1}^n \alpha_i, z_i^{\frac{\sigma-1}{\sigma}}\right)^{\frac{\sigma}{\sigma-1}}\ge 1.
]
At optimum, the constraint binds.
2. Form the Lagrangian (with multiplier (\lambda>0)):
[
\mathcal{L}(z,\lambda)=\sum_{i=1}^n p_i z_i + \lambda\left(1-\left(\sum_{i=1}^n \alpha_i, z_i^{\frac{\sigma-1}{\sigma}}\right)^{\frac{\sigma}{\sigma-1}}\right).
]
3. First-order conditions (interior case) imply that for all (i),
[
p_i \propto \alpha_i, z_i^{-\frac{1}{\sigma}},
]
hence (z_i \propto (\alpha_i/p_i)^{\sigma}).
4. Substitute (z_i = k, (\alpha_i/p_i)^{\sigma}) into the binding constraint to solve for (k), and then compute (p\cdot z). The resulting minimum cost equals
[
P(p)=\left(\sum_{i=1}^n \alpha_i^{\sigma}, p_i^{,1-\sigma}\right)^{\frac{1}{1-\sigma}}.
]
5. Apply Shephard’s lemma (h_i(p,1)=\partial P(p)/\partial p_i) and normalize shares:
[
s_i^H(p)=\frac{p_i h_i(p,1)}{P(p)}=\frac{\alpha_i^{\sigma}, p_i^{,1-\sigma}}{\sum_{j=1}^n \alpha_j^{\sigma}, p_j^{,1-\sigma}}.
]
(\square)

---

### Proposition 11 (Two-good CES gain from a single productivity multiplier)

Let (n=2). Fix (A_1'=A_1) and let (A_2'=A_2,A_2^{(m)}) where the multiplier (A_2^{(m)}>0) applies only to task 2 (equivalently (p_2'=p_2/A_2^{(m)}) and (p_1'=p_1)). Let the baseline time share on task 2 be (t_2\equiv t_2(A)). Under Assumption C1 with elasticity (\varepsilon\equiv\sigma),
[
\frac{V(A')}{V(A)}=
\left((1-t_2)+t_2,(A_2^{(m)})^{\varepsilon-1}\right)^{\frac{1}{\varepsilon-1}}.
]

**Proof (structured).**

1. By Proposition 3,
[
\frac{V(A')}{V(A)}=\frac{P(p)}{P(p')}.
]
2. By Proposition 10 (two-good case),
[
P(p)=\left(\alpha_1^{\varepsilon}p_1^{1-\varepsilon}+\alpha_2^{\varepsilon}p_2^{1-\varepsilon}\right)^{\frac{1}{1-\varepsilon}},
\quad
P(p')=\left(\alpha_1^{\varepsilon}p_1^{1-\varepsilon}+\alpha_2^{\varepsilon}(p_2/A_2^{(m)})^{1-\varepsilon}\right)^{\frac{1}{1-\varepsilon}}.
]
3. Define the baseline CES share
[
t_2 \equiv s_2^H(p)=\frac{\alpha_2^{\varepsilon}p_2^{1-\varepsilon}}{\alpha_1^{\varepsilon}p_1^{1-\varepsilon}+\alpha_2^{\varepsilon}p_2^{1-\varepsilon}}.
]
By Proposition 6, this equals the baseline optimal time share.
4. Note ((p_2/A_2^{(m)})^{1-\varepsilon}=p_2^{1-\varepsilon}(A_2^{(m)})^{\varepsilon-1}). Hence
[
\alpha_1^{\varepsilon}p_1^{1-\varepsilon}+\alpha_2^{\varepsilon}(p_2/A_2^{(m)})^{1-\varepsilon}
===============================================================================================

\left(\alpha_1^{\varepsilon}p_1^{1-\varepsilon}+\alpha_2^{\varepsilon}p_2^{1-\varepsilon}\right)\left((1-t_2)+t_2(A_2^{(m)})^{\varepsilon-1}\right).
]
5. Substitute 4 into (P(p)/P(p')) and simplify to obtain
[
\frac{V(A')}{V(A)}=
\left((1-t_2)+t_2,(A_2^{(m)})^{\varepsilon-1}\right)^{\frac{1}{\varepsilon-1}}.
]
(\square)

---

### Proposition 12 (CES share response and identification from pre/post shares)

In the setting of Proposition 11, let (t_2'\equiv t_2(A')) denote the post-change time share on task 2. Then
[
t_2'=\frac{t_2,(A_2^{(m)})^{\varepsilon-1}}{(1-t_2)+t_2,(A_2^{(m)})^{\varepsilon-1}},
]
and equivalently,
[
\operatorname{logit}(t_2')-\operatorname{logit}(t_2)=(\varepsilon-1)\ln A_2^{(m)},
\qquad
\operatorname{logit}(x)\equiv \ln!\left(\frac{x}{1-x}\right).
]
Thus, if (t_2,t_2'), and (A_2^{(m)}) are observed,
[
\varepsilon = 1+\frac{\operatorname{logit}(t_2')-\operatorname{logit}(t_2)}{\ln A_2^{(m)}}.
]

**Proof (structured).**

1. By Proposition 10 (CES shares),
[
t_2=s_2^H(p)=\frac{\alpha_2^{\varepsilon}p_2^{1-\varepsilon}}{\alpha_1^{\varepsilon}p_1^{1-\varepsilon}+\alpha_2^{\varepsilon}p_2^{1-\varepsilon}},
\quad
t_2'=s_2^H(p')=\frac{\alpha_2^{\varepsilon}(p_2/A_2^{(m)})^{1-\varepsilon}}{\alpha_1^{\varepsilon}p_1^{1-\varepsilon}+\alpha_2^{\varepsilon}(p_2/A_2^{(m)})^{1-\varepsilon}}.
]
2. Substitute ((p_2/A_2^{(m)})^{1-\varepsilon}=p_2^{1-\varepsilon}(A_2^{(m)})^{\varepsilon-1}) and factor the common denominator term to obtain the stated closed form for (t_2').
3. Compute odds ratios:
[
\frac{t_2}{1-t_2}=\frac{\alpha_2^{\varepsilon}p_2^{1-\varepsilon}}{\alpha_1^{\varepsilon}p_1^{1-\varepsilon}},
\qquad
\frac{t_2'}{1-t_2'}=\frac{\alpha_2^{\varepsilon}(p_2/A_2^{(m)})^{1-\varepsilon}}{\alpha_1^{\varepsilon}p_1^{1-\varepsilon}}
===========================================================================================================================

\frac{\alpha_2^{\varepsilon}p_2^{1-\varepsilon}}{\alpha_1^{\varepsilon}p_1^{1-\varepsilon}},(A_2^{(m)})^{\varepsilon-1}.
]
4. Divide the second equality in 3 by the first and take logs to obtain
[
\operatorname{logit}(t_2')-\operatorname{logit}(t_2)=(\varepsilon-1)\ln A_2^{(m)}.
]
Rearrange to solve for (\varepsilon). (\square)

---

### Corollary 12.1 (Limiting benchmark cases in the two-good CES gain formula)

Under Proposition 11 with (A_2^{(m)}>0) and (t_2\in[0,1]), the CES gain formula satisfies the following limits:

1. **Perfect complements (Leontief/Amdahl limit):** as (\varepsilon\to 0),
   [
   \frac{V(A')}{V(A)} \to \frac{1}{(1-t_2)+t_2/A_2^{(m)}}.
   ]
2. **Cobb–Douglas:** as (\varepsilon\to 1),
   [
   \frac{V(A')}{V(A)} \to (A_2^{(m)})^{t_2}.
   ]
3. **Perfect substitutes:** as (\varepsilon\to\infty) and (A_2^{(m)}>1),
   [
   \frac{V(A')}{V(A)} \to A_2^{(m)}.
   ]

**Proof (structured).**

1. Start from Proposition 11:
[
G(\varepsilon)\equiv \left((1-t_2)+t_2,(A_2^{(m)})^{\varepsilon-1}\right)^{\frac{1}{\varepsilon-1}}.
]
2. For (\varepsilon\to 0), note ((A_2^{(m)})^{\varepsilon-1}\to (A_2^{(m)})^{-1}) and (\frac{1}{\varepsilon-1}\to -1), hence (G(\varepsilon)\to ((1-t_2)+t_2/A_2^{(m)})^{-1}).
3. For (\varepsilon\to 1), set (r=\varepsilon-1\to 0) and write
[
\ln G(\varepsilon)=\frac{1}{r}\ln!\left((1-t_2)+t_2 e^{r\ln A_2^{(m)}}\right).
]
Use the expansion (e^{r\ln A}=1+r\ln A+o(r)) to obtain (\ln G(\varepsilon)\to t_2\ln A_2^{(m)}), hence (G(\varepsilon)\to (A_2^{(m)})^{t_2}).
4. For (\varepsilon\to\infty) with (A_2^{(m)}>1), ((A_2^{(m)})^{\varepsilon-1}) dominates the constant term, so
[
G(\varepsilon)=\left(t_2(A_2^{(m)})^{\varepsilon-1}\left(1+\frac{1-t_2}{t_2(A_2^{(m)})^{\varepsilon-1}}\right)\right)^{\frac{1}{\varepsilon-1}}
\to (A_2^{(m)})\cdot t_2^{\frac{1}{\varepsilon-1}}\to A_2^{(m)}.
]
(\square)

---

## Task activation and non-smooth choice (minimal formal extension)

The continuous model above permits corner solutions (t_i(A)=0) but remains a convex program. A distinct class of “activation” models introduces discrete feasibility constraints (fixed setup time, unit-demand tasks, lumpy projects). The main implication is potential non-differentiability of (V(\cdot)) and discontinuous jumps in optimal task selection.

### Assumption T1 (Activation costs)

Each task (i) has a fixed time cost (f_i\ge 0) incurred if the task is activated. Let (a_i\in{0,1}) indicate activation. Feasible allocations satisfy
[
\sum_{i=1}^n t_i + \sum_{i=1}^n f_i a_i \le 1,\qquad 0\le t_i,\qquad t_i=0\ \text{if}\ a_i=0.
]
Output is (y(A_1 t_1,\dots,A_n t_n)) as before.

### Proposition 13 (Potential non-differentiability under activation)

Under Assumption T1, the value function (V(A)) (defined analogously to Definition D1 with activation variables) need not be differentiable in (A). In particular, there exist (A,A') such that the set of activated tasks differs between optimizers at (A) and (A'), and at such points the differential formula in Proposition 7 may fail to apply.

**Proof (structured).**

1. Under Assumption T1, the feasible set for ((t,a)) is non-convex because (a\in{0,1}^n).
2. For non-convex maximization problems, standard envelope theorems that deliver differentiability of the value function may fail at parameter values where the identity of the maximizer changes discontinuously.
3. Choose any instance where two distinct activation patterns (a\neq \tilde a) are both locally optimal for different productivity vectors (e.g., tasks with positive fixed costs and near-ties in the best attainable (y(\cdot)) across patterns). Then there exists a boundary in (A)-space across which the optimizer switches from (a) to (\tilde a).
4. At such boundaries, (V(A)) is the pointwise maximum of finitely many smooth functions (one per activation pattern), hence is generally only directionally differentiable and may fail to be differentiable.
5. Proposition 7 requires differentiability (Assumption A4), which can fail here. (\square)

---

## Summary of derived objects

* **Exact productivity ratio:** (\displaystyle \frac{V(A')}{V(A)}=\frac{P(1/A)}{P(1/A')}).
* **EV/CV in time units (homogeneous case):** (\displaystyle EV=\frac{P(p)}{P(p')}-1), (\displaystyle CV=\frac{P(p')}{P(p)}-1).
* **Differential identity:** (\displaystyle d\ln V(A)=\sum_i t_i(A),d\ln A_i).
* **Large-change exactness:** integrate compensated (Hicksian) shares along a path.
* **CES closed forms:** unit-expenditure index, shares, two-good gain formula, and elasticity identification from pre/post shares.
* **Bounds from observing baseline or post shares:** (\displaystyle \bigl(\sum_i t_i(A)/m_i\bigr)^{-1}\le V(A')/V(A)\le \sum_i t_i(A'),m_i), where (m_i=A_i'/A_i).
