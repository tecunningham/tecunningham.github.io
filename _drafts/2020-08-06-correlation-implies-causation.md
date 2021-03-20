
# Correlation Implies Causation

<!--

https://fb.workplace.com/groups/135724786501553/permalink/2666189256788414/
https://fb.workplace.com/groups/135724786501553/permalink/2650519411688732/

-->

1. **Correlational evidence is *always* informative about causal effects.** The correlation is the sum of the causal-effect and the confounding-effect. To interpret it you need to filter it through your prior means and uncertainties of each of those.

2. **We use correlations all the time to help estimate causal effects.** The slide-decks that circulate in businesses and governments are full of scatter plots and conditional means, and that's a good thing, it would be madness to make decisions without collecting that data.

3. **Statisticians teach taboos and fetishes:** There's a taboo against consuming raw correlations because they can make you sick. The taboo is there for a reason but the truth (between you & me) is that they are very nutritious when prepared correctly. 
   
There's a fetish for *identification* -- finding circumstances where we can assume the confounding-effect is exactly zero -- but that's way too conservative: there are lots of cases where the confounding-effect is sufficiently contained that we can learn a lot about causation from correlations, without thinking it's exactly zero. We do this every day but unfortunately statisticians are very prudish and so rarely give useful advice on how to do it well. 

4. **Why the taboo?** The taboo is because sometimes people forget entirely about confounding: they get a regression coefficient and say "this is our best estimate of the causal effect". Doing that is positively harmful, and if that's the only thing you're doing with the data you're probably better-off not looking at the data at all.

The right way of interpreting correlations goes something like the following: "the coefficient is above what I expected by 40%, and my uncertainty about the causal & confounding effects are roughly similar, and so I'll revise upward my estimate of the causal effect by 20%." If you're relatively more certain about the causal effect, then you update relatively more on the confounding, and vice versa. 

This sound complicated, but we do it intuitively all the time.

5. **The taboo is holding back science.** There are a lot of scientific fields where it's hard to find good identification, and it feels like those fields have been stuck for decades looking for their keys under lamp-posts (economic development, returns-to-education, nutrition). (Obviously this claim deserves a substantial argument to back it up, & I don't have anything prepared, but this is how I feel).

6. **Some best practices for interpreting causal effects.** (1) show rich scatter plots to get a full picture of correlations; (2) benchmark against other correlations; (3) brainstorm differential diagnoses, with a causal diagram; (4) be explicit about ranges for both the causal and confounding effect you're inferring from the correlational data.
3. **Identification comes from assuming some causal effects are zero, but they rarely are.** We often talk about whether some causal effect "is identified" or "is not identified" as if it's a binary thing. Realistically it's a continuum. Identification happens when we identify a causal effect with a correlation. The simplest case is univariate regression:  \(E[\hat{\beta}]=\frac{cov(y,x)}{var(x)}=\beta+\gamma\). When you assume unconfoundedness, i.e. \(\gamma=0\), then you get identification: \(E[\hat{\beta}]=\beta\). You get identification from trimming the causal tree. 
   .
   A lot of academic social science uses identification based on an assumption that some effect is probably pretty small relative to the effect of interest, such that we can ignore the bias (e.g. instrumental variables, diff-in-diff, matching, etc), and they use 0 as a stand-in for "small". But by searching for places where we have clean identification, we're passing over mountains of good evidence.
4. **Doesn't it depend on your assumptions about the true model?** People talk about different DAGs as if one of them was true and the other ones not ("does X affect Y, or does Y affect X?"). But we know that everything affects everything, and the idea that some causal arrows have coefficients of zero is just a convenient fiction to help us simplify a complex problem into a simpler one, and achieve identification.
5. [EDIT] **Another reason for the fetish for zero-effects: Because it lets you keep things *objective*.** As soon as you allow for some non-zero confounding effect, then your interpretation relies on more inputs -- you have to put in your best-estimates of means and ranges for different variables. This is hard in science: it typically means we have to allow subjective *judgment* to enter the inference process, and that can cause pain -- through people being either insincere, or self-deceiving, or clumsy in reporting their judgments. So if you don't trust other people, or don't trust yourself, maybe you should stick with well-identified regressions.

**Previous installment:** https://fburl.com/t6eql5fd .

**Future installments:** (1) examples of learning from correlations at FB; (2) recommendations of best-practices for learning from correlations.

----

Going to ask a naive question, but I'm genuinely curious to hear how other people think about this type of situation.

# Why don't we infer *some* causality from correlation?

When you observe the correlation between \(x\) and \(y\) you should always update your best-estimate of the causal relationship by **some** amount, right?

More precisely: you should update our beliefs by the ratio of your uncertainties about the causal-effect vs selection-effect. (at least in the Gaussian case, model below).

**We often talk about correlations as if they're completely uninformative.**

Is this because typically the uncertainty about the selection effect is way larger than the uncertainty about the causal effect?

---

Here are cases where correlations ought to be *somewhat* informative about causal relationships:

1. **Correlation of car model and death rate.**
1. **Correlation of Stories adoption and time-spent.**
2. **Correlation of Instagram and Facebook usage.**
2. **Correlation of coefficient-score and propensity to like a post.**
2. **Correlation of coffee consumption and longevity.** 
3. **Correlation of education and wages.** 
4. **Correlation of social-media use and depression.**
5. **Correlation of using a parachutes & surviving a fall from an aircraft.**

Surely knowing these correlations ought to tell you *something*, yet it feels like we pretty rarely discuss this in explicit terms. (Perhaps the problem is that we're really interested in *excess* correlation, i.e. relative to our priors, and priors are always hard to talk about in an inter-subjective way).

--

Suppose we adopted the following practice: before looking up a correlation you write down (i) your expectation of the correlation; (ii) your relative uncertainty about causal vs selection effects. Then that'll tell you exactly how much you should update, once you observe the correlation.

---

### Model

Suppose we want to know the causal relationship between $x$ and $y$ (i.e., the coefficient \(\beta\)), but there is some unobserved factor $z$ which affects both $x$ and $y$:

$$\begin{matrix}  &  &   z      &  \\  & \swarrow_\gamma &  & \searrow_1 & \\   x & & \rightarrow_\beta         &    & y \end{matrix}$$

Suppose we run a regression of $y$ on $x$, everything is Gaussian, and $x$ and $z$ have underlying shocks $e_x,e_z$ with variance $\sigma_x^2,\sigma_z^2$, then we have:

$$\begin{aligned}    x=& e_x + \gamma e_z \\   y=& \beta e_x + \beta\gamma e_z + e_z \\   \hat{\beta}=& \frac{cov(y,x)}{var(x)}\\   =& \frac{\beta \sigma^2_x+\gamma(\beta\gamma+1)\sigma_z^2}{\sigma_x^2+\gamma^2\sigma_z^2} \\   =& \underbrace{\beta}_\text{causal} + \underbrace{\frac{\gamma\sigma_z^2}{\sigma_x^2+\gamma^2\sigma_z^2}}_\text{bias} \end{aligned}$$

Observations:

* Your inference from observing \(\hat{\beta}\) should be in proportion to the ratio of uncertainties over the *causal* effect and the *bias*, i.e. your uncertainty over the distribution of \(\frac{\gamma\sigma_z^2}{\sigma_x^2+\gamma^2\sigma_z^2}\).

* Interestingly bias is non-monotonic in $\gamma$: if $\gamma=0$ then there's no confounding, great. But as $\gamma$ gets large, then $z$ operates mainly through $x$, and so we measure the true causal effect again.
