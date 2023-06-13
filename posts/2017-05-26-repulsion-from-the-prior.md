---
layout: post
title: Repulsion from the Prior
geometry: margin=1in
date: "2017-05-26"
---

**the shortest version:** *contrary to recent reports, I do not think it's possible for you to be a Bayesian and consistently exaggerate things.*

![](https://www.dropbox.com/s/sbodcv65vnzxey4/anni_albers_black_mountain_college.jpg?raw=1){: .center-image }

## Short Version

1. If we think of perception as inference, it has implications about the types of biases we would have.
2. Yet many biases and illusions seems to go in the exact *opposite* direction -- sometimes called "anti-Bayesian" biases -- in particular there are ubiquitous *contrast* effects, while Bayesian inference seems to imply *assimilation* effects.
3. Wei and Stocker (2015) say they can rationalize these contrast effects, under the assumption that our sensory mechanisms are tuned to the environment, such that they are relatively more sensitive to more likely signals. They say that this will imply contrast effects (that the bias is inversely proportional to the slope of the prior).
4. Yet their results contradict some simple laws of Bayesian inference -- the law of iterated expectations, and law of total variance -- so there is something odd going on.
5. (If this explanation doesn't work, then why do we get repulsion? I think that Ted Adelson explained the basic reason in the 70s. Will write another post on this.)

## Shortish Version

1. Here's a nice crisp problem: in what cases does inference attract *towards* the prior, and in what cases does it repulse *away* from it?
2. Given an unknown variable $x$ and a signal $s$, let's say that there's "attraction" at a given value of $x$ if the average inferred value of $x$ is closer to the prior than $x$ itself is --

    $$|E[E[x|s]|x]-\mu|<|x-\mu|$$

3. Attraction effects are typically treated as the norm. For example if $x$ is drawn from a normal distribution and if $s$ is equal to $x$ plus normal noise, then you'll always get attraction to the prior. I.e., if $x$ is above the mean, then it'll be, on average, estimated to be closer to the mean than it actually is.
4. However this has sometimes been treated as a puzzle in studies of perception: perception seems like inference, but we also find what look like *repulsion* effects. For example "contrast" effects, in which an object seems less dark when you put it next to another, darker, object. If we assume that the colour of the neighboring objects affects your prior about the target object, then this would imply an *attraction* effect. Yet repulsion effects seems to be the norm across all sorts of judgments (lightness, colour, volume, orientation, size), and similar contrast effects occur in time as well as in space (i.e., something seems less dark if it is preceded by something darker) -- though of course there are exceptions. These types of illusion are sometimes called "anti-Bayesian."
5. A common explanation of these contrast effects is that we 'code for differences' -- i.e. that something about our neural wiring causes us to encode *differences*, rather than *levels*, and this causes us to exaggerate differences, i.e. get contrast effects.
6. But this assumes that we encode the difference and then forget to decode (AKA **coding catastrophe**, AKA the **el Greco fallacy**). If you write down a Bayesian model, which makes its best effort to infer the level from the difference, you typically do *not* find the desired contrast effects (Schwartz, Hsu & Dayan (2007)).
5. Wei and Stocker (2015) announce that they have made a breakthrough -- a fully Bayesian model which generates contrast/repulsion effects generically. They say that the key assumption is that we are more sensitive to differences in areas where signals are more likely to fall -- i.e., sensitivity is proportional to the density of the prior.

6. Formally, let $x\sim f$, and
$$s=F(x)+\varepsilon.$$
 This means that sensitivity is proportional to the density of the prior -- and it implies that $s$ will be roughly uniformly distributed -- so in some sense it's an efficient use of signal capacity. Given this setup, and some simplifications, they find that the bias is proportional to the slope of the prior -- so if the prior is symmetric & single-peaked then for values above the mean, the bias will be positive, and vice versa -- i.e. *repulsion* away from the prior everywhere.
6. In the note below I give a proof that implies that it is impossible to have repulsion effects everywhere -- which seems to contradict the results of Wei & Stocker.
7. I'm not sure what the source of the contradiction is -- it could be either (a) Wei & Stocker's results are true locally, but do not apply at the tails of the distribution, and so things balance out that way; (b) there is a difference in the implicit assumption used when taking conditional expectations (AKA the Borel-Kolmogorov paradox); or (c) I made a mistake.
7. I also mention below a related result, that there cannot be a consistent upward or downward bias (i.e., it cannot be that $E[\hat{x}\|x]>x$ for all $x$). This is relevant for Wei & Stocker's result applied to asymmetric priors -- e.g. if the prior is everywhere decreasing -- where the result seems to imply a consistent upward bias.
<!-- 8. Finally I give an example of an analytic solution for $E[\hat{x}|x]$ (with uniform prior and $x$ and with $x=\ln x$), and show that  this seems to imply the opposite result as derived by Wei and Stocker. -->


![](https://www.dropbox.com/s/hwbeyp8ldrmwysp/rabbit.jpg?raw=1){: .center-image }

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

<!--
## An Additional Note

To figure out what's going on here the sensible thing is to set up a parametric model, and figure out which laws it obeys. I recently did something similar in my [note on Weber's law](http://tecunningham.github.io/2017/02/25/weber-fechner-law/). In the final section I show that, when $s=\ln x+e$, and $x$ is drawn from a uniform distribution, then there is no bias, i.e.: $$E[\hat{x}|x]=x$$
This doesn't fit Wei & Stocker's setup, but it would do if $x$ was drawn from a distribution with $f(x)=\frac{1}{x}$. But then the prior would be downward-sloping everywhere, and this would surely cause posteriors to shift downwards (i.e., lower values of $x$ are relatively more likely), i.e.:$$E[\hat{x}|x]<x$$
Which directly contradicts Wei & Stocker's prediction. (In this case, of course, the above inequality couldn't be true everywhere, it would violate the law of iterated expectations. So it means that if it was a proper prior, then the bias would go in the offsetting direction at either edge.)
-->

## References

- Schwartz, Hsu & Dayan (2007, Nature Review Neuro) “Space and Time in Visual Context”
- Wei & Stocker (2015, Nature Neuroscience) **"A Bayesian observer model constrained by efficient coding can explain ‘anti-Bayesian’ percepts"**
