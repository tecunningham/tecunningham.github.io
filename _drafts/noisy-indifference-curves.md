---
title: Moving Indifference Curves, not Moving Alternatives
layout: post
---
Behavioural economists (like me) pass their time by proposing theories which might be able to fit the pattern of choice anomalies mapped out by Tversky & Kahneman in the 1970s. We've been doing this for 4 decades and still going -- no-one's pulled the sword from the stone yet.

Here's a simple point but not often made: these classic choice biases must be due to movement in the *indifference curves*, not due to movement in the *alternatives*.

Put another way: when we see people making inconsistent choices, it's more commonly because their perception of their *preferences* change from case to case, not because their perception of the *alternatives* changes.

Let me state the problem one more time. We have collected a lot of data about peoples choice among gambles, e.g. "would you prefer a 20% chance of \\$5, or a 10% chance of \\$10?" We often observe that peoples' choices are inconsistent. Are these inconsistencies due to (A) peoples' *preferences* changing, or (B) due to having a vague perception of the question (e.g. misreading 10% as 8%).

Here are the reasons why I think it must be due to moving preferences:

1. People rarely choose dominated alternatives.
2. People can do maths problems pretty easily.
3. The motivating examples from perception (for the moving-choice theory) are all wrong.


# Theory

We observe a choice function $c(A)\subseteq A$. Orthodox theory just says we choose the best element from $A$:

$$c(A)=\arg \max_{x\in A} u(x)$$

Here are two basic types of variation which can explain some anomalies:

**(1) Moving indifference curves:** in which my preferences depend on the choice set, $u(x,A)$:

$$c(A)=\arg \max_{x\in A} u(x,A)$$

**(2) Moving alternatives:** Here my preferences are stable, but my perception of the alternatives depends on the choice set, i.e. instead of directly observing $x$ I perceive $\hat{x}(x,A)$ which depends on both $x$ and the choice-set $A$, and so my choice function is: 

$$c(A)=\arg \max_{x\in A} u(\hat{x}(x,A))$$

You could rationalize this theory by saying that when people observe a choice set they observe a noisy signal $s$, and so they form an expectation $\hat{x}=E[x\\|s]$. If the utility function is linear then this all goes through fine, if not linear then you just need a bit more algebra but the basic point holds.

**The theories differ in their predictions about dominated choices.** If you preferences change, you still won't choose something dominated. If your perception of the alternatives changes, then one of the alternatives could slip below another one, and so you accidentally choose the dominated one.


# But People Rarely Make Dominated Choices

More precisely, choice anomalies (like preference-instability and framing effects) are observed for very simple alternatives (e.g., gambles with 1 outcome), but it's only when outcomes become moderately complex that people start making dominated choices (e.g., gambles with 3 outcomes). 

Carbone (1995) say “[w]hat is startling ... are the results of the satisfaction or violation of dominance ... [with a] mean violation rate of just 0.3 percent. In contrast the average inconsistency rate of the repeated pairs was 12 percent.” Similar findings are described in Loomes (1998) and Hey (2001).

People do sometimes directly choose a stochastically dominated gamble, but most example in the literature involve choices among gambles with at least four different outcomes (Tversky et al. (1986)). Caplin et al. (2013) find mistakes when subjects have to count a large number of dots. In experiments documenting “bracketing”, subjects make dominated choices only when they have to combine pairs of gambles (Tversky 1981, Rabin 2009).


# Domains where Moving Alternatives Makes More Sense

Papers which propose a moving-alternatives are justified by .



# Theories which propose moving alternatives

* Woodford's 
* Rangel's multi-attribute
* Gabaix's
