---
layout: post
title: Repulsion from the Prior
geometry: margin=1in
---

**the shortest version:** *contrary to recent reports, I do not think it's possible for you to be a Bayesian and consistently exaggerate things.*

## Basic argument

1. Here's a nice crisp problem: in what cases does inference attract *towards* the prior, and in what cases does it repulse *away* from it?
2. Given an unknown variable $x$ and a signal $s$, let's say that there's "attraction" at a given value of $x$ if the average inferred value of $x$ is closer to the prior than $x$ itself is --

    $$|E[E[x|s]|x]-\mu|<|x-\mu|$$

3. Attraction effects are typically treated as the norm. For example if $x$ is drawn from a normal distribution and if $s$ is equal to $x$ plus normal noise, then you'll always get attraction to the prior. I.e., if $x$ is above the mean, then it'll be, on average, estimated to be closer to the mean than it actually is.
4. However this has sometimes been treated as a puzzle in studies of perception: perception seems like inference, but we also find what look like *repulsion* effects. For example "contrast" effects, in which an object seems less dark when you put it next to another, darker, object. This type of effect seems to be the norm across all sorts of judgements (lightness, colour, volume, orientation, size), and similar contrast effects occur in time as well as in space (i.e., something seems less dark if it is preceded by something darker) -- though of course there are exceptions. These types of illusion are sometimes called "anti-Bayesian."
5. A common explanation of these contrast effects is that we 'code for differences' -- i.e. that something about our neural wiring causes us to encode *differences*, rather than *levels*, and this causes us to exaggerate differences, i.e. get contrast effects. But this assumes that we encode the difference and then forget to decode. If you write down a Bayesian model, which makes its best effort to infer the level from the difference, you typically do *not* find the desired contrast effects.
5. Wei and Stocker (2015) announce that they have made a breakthrough -- a fully Bayesian model which generates contrast effects.
6. In the note below I give a proof that seems to imply that it is impossible to have repulsion effects everywhere -- which seems to contradict the results of Wei & Stocker.
7. I'm not sure what the source of the contradiction is -- it could be either (a) Wei & Stocker's results are true locally, but do not apply at the tails of the distribution, and so things balance out that way; (b) there is a difference in the implicit assumption used when taking conditional expectations (AKA the Borel-Kolmogorov paradox); or (c) I made a mistake.
7. Finally I mention a related result, that there cannot be a consistent upward or downward bias (i.e., it cannot be that $E[\hat{x}\|x]>x$ for all $x$). This is relevant for Wei & Stocker's result applied to asymmetric priors -- e.g. if the prior is everywhere decreasing -- where the result seems to imply a consistent upward bias.


## Summary of proof

1. Suppose that there is repulsion from the prior everywhere, i.e. for all $x$, $\|E[\hat{x}\|x]-\mu\|>\|x-\mu\|$.
2. This implies that $Var[\hat{x}]>Var[x]$.
3. But this contradicts the law of total variance, which says that $Var[E[A\|B]]\leq Var[A]$.

## Detail:

Suppose there are two random variables $x$ and $s$, and let $\hat{x}=E[x\|s]$. Let $x$ be mean-zero, and let's assume repulsion from the prior everywhere, i.e. for all $x$:

$$
E[\hat{x}|x]|>|x|
$$

From this repulsion assumption I think it's clear that there's more variance in $E[\hat{x}\|x]$ than in $x$:

$$Var[E[\hat{x}|x]]>Var[x]$$

Now let's apply the law of total variance:

$$
\begin{aligned}
Var[A]=& E[Var[A|B]]+Var[E[A|B]] \\\\
Var[\hat{x}]=& E[Var[\hat{x}|x]]+Var[E[\hat{x}|x]]
\end{aligned}
$$

Thus implying that:

$$Var[\hat{x}]\equiv Var[E[x|s]]>Var[x]$$

Applying the law of total variance again we get:

$$\begin{aligned}
Var[x]=& E[Var[x|s]]+Var[E[x|s]] \\\\
      >& Var[x]
\end{aligned}$$

A contradiction.

## No consistent upward/downward bias

The law of iterated expectations states that, for any $A$ and $B$:

$$E[E[A|B]]=E[A]$$

This implies that there cannot be a consistent upward or downward bias, i.e. it cannot be true that:

$$E[\hat{x}|x]>x, \forall x$$

## References

* Wei & Stocker (2015, Nature Neuroscience) **"A Bayesian observer model constrained by efficient coding can explain ‘anti-Bayesian’ percepts"**
