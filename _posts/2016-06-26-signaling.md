---
layout: post
title: Signaling
---

# Nutshell
If everyone exerts effort to persuade you of some fact, then you won't be fooled on average, you'll adjust for the effort exerted. However the paper by Ines and I show that there are circumstances in which effort at persuasion will change the *decisions* you make, even though it doesn't change your average beliefs. What's more it will change your decisions in a way that benefits the persuaders. The two main conditions are that (a) you are making a binary decision, and (b) the persuaders know the information which you want to know.

# The Key Condition

The basic mathematical problem is this: suppose $t$ is what I'm trying to persuade you of, and $u$ is random noise. Given that you observe a signal which is a combination of both, $s=f(t,u)$, will the expected value of $t$, given the signal $s$, be greater or less than the fraction of signals below $s$?

Put another way: will more than half of the signals above-average? This graph shows all the possible combinations of $u$ and $t$, and the red line is .

$$
\xymatrix{
1 & &  &  &  & \ar@{-}[llll]\ar@{-}[dddd]  \\
& \ar@[red]@{-}@/_/[ddrrrr] &  &  &  &  \\
\text{type (t)} &  &  &  &  &  \\
\, &  &  &  &  & \color{red}t(u) \\
0 & \ar@{-}[uuuu]\ar@{-}[rrrr] &  & & & \, \\
& &  & \text{noise (u)} & & \,
}
$$

Here the red line represents your *threshold* $k$, defined by $E[t\|m+u>k]=0$ i.e. if you receive a signal above this threshold then you believe $t>\frac{1}{2}$, and so you perform the action that I want you to perform. 

We assume that $t$ is uniform between 0 and 1, and that $u$ is drawn from a symmetric MLRP distribution $g(.)$. The two quantities we are interested in are the area below the curve (A), and the expectation along the curve (E):

$$\begin{align} A &= \int g(u)t(u)du \\
  E &= \frac{\int t(u)|t'(u)|g(u)du}{\int |t'(u)|g(u)du} \end{align}$$

We can make a series of observations: 

1. If $t(u)$ is linear then $t'(u)$ is a constant, and it will cancel out in the fraction, so $A=E$. 
2. If $t(u)$ is convex, as in the figure above, then there will be relatively greater weight on higher values of $t$ in the expression for $E$ (this is because $\|t'\|$ will be high when $t$ is high), so $E>A$. 
3. If $t(u)$ is proportional to $g'$, then .



The interesting question is this: what is the fraction of the times that you believe that $t>\frac{1}{2}$? 



# Slightly More Formally



![asdf](https://dl.dropboxusercontent.com/u/13046545/imgs/thresholds-graph.png){: .center-image }


* Suppose there is a sender and a receiver, and two variables $t$ and $u$
* Only the sender knows $t$, neither knows $u$
* The receiver has to decide whether or not to take some action which has payoff $t$, which is uniformly distributed between $-\frac{1}{2}$ and $\frac{1}{2}$
* The sender gets a fixed benefit if the receiver takes the action, so it's in their interest for the receiver to believe that $t>0$
* The receiver receives a signal $s$ that is correlated with $t$, but the sender can pay to manipulate that signal: in particular $s=m+u$, where the sender has to pay a convex cost $c(m-t)$
* In equilibrium the receiver will take the action whenever the signal they receive $s$ is above some threshold $k$, where that threshold is defined by $E[t\|s=k]=0$.

We can represent the equilibrium in this diagram: 

![asdf](https://dl.dropboxusercontent.com/u/13046545/imgs/thresholds-graph.png){: .center-image }

The red line represents the combinations of $t$ and $u$ which produce a signal exactly at the threshold $k$. 

We are interested in two quantities:

$$
A&=& \int t(u) \\
asdf
$$


# Notes

* Careful about the Borel-Kolmogorov paradox.


---

# One

(A lot of economic theory deals with choosing things that affect others' beliefs)

Signaling says that peoples' decisions will be biased towards producing outcomes that are correlated with favorable facts, i.e. facts that the person would want other people to believe are true. For example:

- As an employee I'd like my boss to think I'm clever, and so I put in some extra hours to come up with clever things to say.

- As a firm I'd like other firms to think that my market is not very profitable, for fear that they would enter my market, and so I will tend to nudge my prices a little lower to give them that impression.

- As a politician I'd like voters to think I'm relatively honest, and so I'll spend a bit more public money (and embezzle a little less) to persuade them of that.

Signaling theory is often used to explain why people exert effort in the absence of explicit incentives: why do we work hard if we're on a fixed salary? why do politicians stay honest if voters oly .

# Two

Of course people won't be fooled on average. If *all* employees stay late an extra hour, just to persuade their boss of their industry, then the relationship between industry and hours-worked has changed, and the boss won't be systematically biased overestimate everyone's ability.

So the net effect of signaling seems to be an excess production of those things that are correlated with facts that people want others to believe. The excess production can be both good and bad things:

- Employees will
- Firms will lower prices (not obviously a good thing in equilibrium, because expected profits decrease, so there'll be less entry)
- Politicians will do things to boost the economy -- good things, like 



---

Suppose there are some *favorable* facts, such that it would be good for you if other people believed they were true. As an employee you'd like people to think that you're capable, as a firm you'd like other firms to think that your market is not very profitable, as a politician you'd like voters to think that you're honest. 

- As an employee I'll work a bit harder than otherwise, because it helps persuade my boss that I'm smart, which helps me get a promotion.


**Ines and my paper**

We show that .



---

**puzzles it'll help solve**  

Let's go apply our theory of human behaviour -- which says that people choose whichever path leads to more expected discounted concavified consumption. 

It's a beautiful theory, but one of the problems we run into is this: why do people keep doing things for which they have no direct incentive? Most people work for a salary, not a piece rate, so why work so hard? Once you're elected, why do politicians put in any effort? Why go to the expense of punishing a crime once it's already committed? 

One answer is that other people will reward you or punish you for certain actions, even though they're not obliged to: e.g. reward you with a promotion or a bonus for working hard.

- As an employee you'll put in long hours at work because it'll make people think you're good at your job, and so make them more likely to hire or promote you.
- As a firm you'll charge lower prices for your good because it'll dissuade other people from entering your market, by making them think it's less profitable.
- As a politician you'll spend more public money (and embezzle less) because it'll persuade people that you're good at governing

Some puzzles that signaling has been used to explain:

* Why do employees work hard when they're on a fixed salary? Because they want to show that they are good at their job.
* Why do politicians work hard when they have no incentive to work?
* Why do monopolists charge below-monopoly prices?

**notes:**

* (implies you should always downplay effort you put in, to make people think you're more capable)
