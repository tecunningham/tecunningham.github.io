---
layout: post
title: Weber's Law Doesn't Imply Concave Representations or Concave Judgments
usemathjax: true # not sure if this necessary
date: 2017-02-25
---

![runningman](https://www.dropbox.com/s/24cumup0i7uiksn/runningman.jpg?raw=1)

**Nutshell.**

1. If you spend any time reading about behavioural economics you'll come across "diminishing sensitivity" pretty soon, applied to all sorts of things in decision-making (probability weighting, value-function weighting, relative thinking), and often you'll find a reference to "Weber's law" from psychology.
2. Weber's law says that if you can tell the difference between a 1-pound and a 1.2-pound weight 90% of the time, then you will also be able to tell the difference between a 10-pound and 12-pound weight about 90% of the time (and generally, the ability to discriminate between two sensations is a function of the ratio of the magnitudes).
3. This finding is often interpreted as implying that we have, in some sense, *concave* representations of value. And indeed this behaviour *would* be implied by a model in which we receive a signal which is a concave function of the underlying value, plus additive noise.
4. However Weber's law would also be seen if we have a linear representation of value with multiplicative noise. And there are good reasons to think that perceptual noise is generally closer to multiplicative than additive (but I leave that for another time).
5. Also of interest is, given our assumptions about value and noise, how a person's posteriors look. I.e., what is the average best-guess of the weight of an object, given it's true weight. I also derive those below (you have to make assumptions about a person's priors), and show that, under multiplicative noise & lognormal priors, expected weight is concave function of true weight, while under additive noise & uniform priors, expected weight is a linear function of true weight.
6. In general I think that Weber's law is *not* relevant most of the anomalies we see in decision-making. This note doesn't really tie the knot on that argument, but I think these are useful results going in that direction. (I'm sure these mathematical points must have been made elsewhere but I've never been able to find them.)

# History.

Ernst Weber (1795-1878) tested subjects' ability to discriminate between the strength of sensations - for example two sounds, two shades of light, two intensities of touch - and found that the Just Noticeable Difference (JND) between two sensations tended to be proportional to the average magnitude of the two sensations: e.g., if you can determine which of two lights is brighter with 80% accuracy, then Weber predicts that you will also have 80% accuracy when the brightness of both lights is doubled. Gustav Fechner (1801-1887) showed that, under the assumption that each JND has an equal subjective difference, this implies a logarithmic relationship between objective and subjective magnitude. Later S. S. Stevens (1906-1973) directly asked subjects for cardinal reports of subjective intensity and found a power law relationship (i.e., the logarithmic relation is a special case of this).

# In Decision-Making

In the 19th century a number of economists made a connection between the Weber-Fechner law and the diminishing marginal utility of consumption. However Max Weber -- a different Weber -- Weber the sociologist, wrote an essay in 1908 to explain that they are fundamentally distinct phenomena ("Marginal Utility Theory and  the Fundamental Law of Psychophysics"). Stigler later wrote about Max Weber's essay and agreed that there is little meaningful connection.

More recently the Weber-Fechner law has been cited by a number of economists to explain diminishing sensitivity in other domains (not just in absolute consumption): Thaler (1980), Tversky & Kahneman (1992), Thaler (1999), Gonzalez & Wu (1999) all argue that the curvature of a gain/loss
function, and of probability-weighting function, are somehow connected with the Weber-Fechner law in perception.

However, I show below that the Weber behaviour (the proportional JND being invariant to scale) does not imply either (A) a concave internal representation of magnitude; or (B) a concave bias in judgment of magnitudes.

(It's also worth noting that a *literal* application of Weber's law to decision-making would be the following: that subjects are equally likely to choose \\$7 over \\$8, as they are to choose \\$70 over \\$80. I'm not sure if this has ever been tested, it doesn't seem like an especially interesting fact for economic decision-making.)

# Weber's Law & Linear vs Concave Representations of Value

First I show that Weber's law does not imply that we must have, in some sense, a concave representation of value. I show that the law can be derived from two different setups: one in which we have a linear representation and multiplicative noise; one with a concave representation and additive noise.

Suppose that we can observe subjects' judgments about which of two values ($v_{1}$ and $v_{2}$) is greater. Then we can define a just noticeable difference, $JND(v,p)$, as the difference in values, such that subjects correctly discriminate $v$ and $v+JND(v,p)$ in a proportion $p$ of trials.

## Linear Representation & Multiplicative Noise

Assume people get signals about underlying value with multiplicative noise, $s=v\cdot e$, with $e$ lognormal. For conciseness let $\delta=JND(v_{1},p)$, then $\delta$ can be implicitly defined as:

$$
\begin{aligned}
p   =&  P(E[v_{1}+\delta|s_{2}]>E[v_{1}|s_{1}]) \\
    =&  P((v_{1}+\delta)e_{2}>v_{1}e_{1}) \\
    =&  P(\ln(v_{1}+\delta)+\ln e_{2}>\ln v_{1}+\ln e_{1}) \\
    =&  \Phi\left(\frac{\ln(v_{1}+\delta)-\ln v_{1}}{\sigma_{e}^{2}+\sigma_{e}^{2}}\right)
\end{aligned}
$$

where $\Phi$ is the CDF of a standard normal distribution. Then,

$$
\begin{aligned}
\ln(v_{1}+\delta)-\ln v_{1} =&   2\sigma_{e}^{2}\Phi^{-1}(p) \\
\frac{v_{1}+\delta}{v_{1}}  =&   \exp(2\sigma_{e}^{2}\Phi^{-1}(p))\\
JND(v_{1},p)=\delta         =&   v_{1}\left[\exp(2\sigma_{e}^{2}\Phi^{-1}(p))-1\right]
\end{aligned}
$$

In other words, the just noticeable difference is proportional to the value, $v_{1}$, as found by Weber.

## A Concave Representation & Additive Noise

Suppose that the decision-maker receives a concave signal of value with additive noise, i.e. $s=\ln v+e$, with Gaussian $e$. Then the derivation is very similar:

$$
\begin{aligned}
  p =& P(E[v_{1}|s_{2}]>E[v_{1}|s_{1}]) \\
    =& P(\ln(v_{1}+\delta)+e_{2}>\ln v_{1}+e_{1}).
\end{aligned}
$$

The rest of the derivation is the same: i.e., the JND in the neighborhood of $v_{1}$ will be proportional to $v_{1}$.

# Weber's Law & Bias in Judgment

Weber's law implies that perception is noisy. We can then ask what is the appropriate Bayesian posterior given noise. In particular, what will the relationship be between a value $v$, and the subjective best-estimate of that value given the signal $s(v)$, i.e. $E[E[v\|s]\|v]$.

It has often been assumed that Weber's law will imply or justify a concave bias in estimates of value. However I show that this is not necessarily so.

**Note on expectations:** In a continuous setup, like the below, you can't just write the conditional expectation as an integral without further notes. The conditional expectation is undefined without specifying which *limit* you're taking ([AKA Borel-Kolmogorov paradox](https://en.wikipedia.org/wiki/Borel%E2%80%93Kolmogorov_paradox)). Below I *believe* that the integrals follow from taking limits with respect to the noise. Intuitively, this is like assuming that you observe only that the signal is in some range $(s-\varepsilon,s+\varepsilon)$, and taking limits as $\varepsilon\rightarrow0$.

## Multiplicative Noise => Posteriors are Concave in $v$

Suppose we have lognormal priors for both $v$ and $e$:

$$
\begin{eqnarray*}
\ln v & \sim & N(\mu_{v},\sigma_{v}^{2})\\
\ln e & \sim & N(\mu_{e},\sigma_{e}^{2}),
\end{eqnarray*}
$$

and $s=v\cdot e$, then we will have posteriors like:

$$
\begin{eqnarray*}
f(\ln v|s) & \sim & N(\frac{\sigma_{v}^{2}}{\sigma_{e}^{2}+\sigma_{v}^{2}}\ln s,\left(\sigma_{v}^{-2}+\sigma_{e}^{-2}\right)^{-1})\\
E[v|s] & = & \exp\left(\frac{\sigma_{v}^{2}}{\sigma_{e}^{2}+\sigma_{v}^{2}}\ln s+\frac{1}{2}\left(\sigma_{v}^{-2}+\sigma_{e}^{-2}\right)^{-1}\right)\\
 & = & s^{\frac{\sigma_{v}^{2}}{\sigma_{e}^{2}+\sigma_{v}^{2}}}e^{\frac{1}{2}(\sigma_{v}^{-2}+\sigma_{e}^{-2})^{-1}}
\end{eqnarray*}
$$

This means that the expected $v$ is concave in the signal $s$ (because
the exponent is less than one). Intuitively: a doubling of the value,
which causes a doubling of the stimulus, will cause a *less*
than doubling of the expected value conditional on that stimulus,
because it will cause us to revise upwards our beliefs about both
$v$ and $e$.

Finally, we are also interested in the *average* posterior for
a given $v$. This will also be concave (abbreviating $\alpha=\frac{\sigma_{v}^{2}}{\sigma_{e}^{2}+\sigma_{v}^{2}}$,
and dropping the constant coefficient in $E[v|s]$):

$$
\begin{eqnarray*}
E[E[v|s]|v] & = & \int(v\cdot e)^{\alpha}f(e)de\\
 & = & v^{\alpha}\int e^{\alpha}f(e)de.
\end{eqnarray*}
$$

## Additive Noise => Posteriors are Linear in $v$

Suppose again that the decision-maker receives a logarithmic signal with additive noise: $s=\ln v+u$,  and let $u$ be Gaussian. (I changed notation from $e$ to $u$ because I use a lot of exponential functions in the derivation.) Now assume that, in addition, $v$ is drawn from an improper uniform $(0,\infty)$. Consider the expected value of $v$ given the signal $s$ (I drop the constant term from the Gaussian distribution for conciseness):

$$
\begin{eqnarray*}
E[v|s] & = & \frac{\int_{0}^{\infty}ve^{-\left(s-\ln v\right)^{2}}dv}{\int_{0}^{\infty}e^{-\left(s-\ln v\right)^{2}}dv}.
\end{eqnarray*}
$$

Now exchange variables, so that $v=e^{z}$:

$$
\begin{eqnarray*}
E[v|s] & = & \frac{\int_{-\infty}^{\infty}e^{z}e^{-(s-z)^{2}}e^{z}dz}{\int_{-\infty}^{\infty}e^{-(s-z)^{2}}e^{z}dz}\\
 & = & \frac{\int_{-\infty}^{\infty}e^{-s^{2}+2(1+s)z-z^{2}}dz}{\int_{-\infty}^{\infty}e^{z-(s-z)^{2}}dz}\\
 & = & \frac{\int_{-\infty}^{\infty}e^{-(z-1-s)^{2}}e^{1+2s}dz}{\int_{-\infty}^{\infty}e^{s+\frac{1}{4}}e^{-((s+\frac{1}{2})-z)^{2}}dz}\\
 & = & e^{s}e^{3/4}\frac{\int_{-\infty}^{\infty}e^{-(z-1-s)^{2}}dz}{\int_{-\infty}^{\infty}e^{-((s+\frac{1}{2})-z)^{2}}dz}
\end{eqnarray*}
$$

Note that both of the integrals are independent of $s$ (because the
integration is between $-\infty$ and $\infty$), so there exists
some $\kappa$ such that:

$$
E[x|s]=\text{e}^{s}\kappa.
$$

Finally we are interested in the average posterior for a given $v$ (here I'm again ignoring all constant terms):

$$
\begin{eqnarray*}
E[E[v|s]|v] & = & \int_{-\infty}^{\infty}E[v|s=\ln v+u]\text{e}^{-u^{2}}du\\
 & = & \int_{-\infty}^{\infty}\text{e}^{(\ln v+u)}\kappa\text{e}^{-u^{2}}du\\
 & = & v\int_{-\infty}^{\infty}\kappa\text{e}^{u-u^{2}}du.
\end{eqnarray*}
$$

I.e., despite the logarithmic internal representation, the average posterior is linear in the value.
