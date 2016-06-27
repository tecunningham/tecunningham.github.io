---
layout: post
title: Signaling
---

# Nutshell
If everyone exerts effort to persuade you of some fact, then you won't be fooled on average, you'll adjust for the effort exerted. 

However Ines and I show that there are circumstances in which effort at persuasion will change the *decisions* you make, even though it doesn't change your average beliefs. What's more it will change your decisions in a way that benefits the persuaders. 

The two main conditions are that (a) you are making a binary decision, and (b) the persuaders know the information which you want to know.

The basic intuition: 

* In equilibrium you will settle on some threshold, where you take the action if and only if you receive a signal above that threshold. 
* The most effort will be exerted by people who are close to the threshold (because it's there where effort has the biggest marginal effect). 
* This will lead to a bunching of signals just above your threshold (and a deficit just below it)
* Consider a different threshold, that which admits exactly half of all signals. At that threshold, because of the bunching, the relatively higher types will be over-represented, meaning that the expected type will be *greater* than a half. And so the threshold at which the expected type is 1/2 will admit *more* than a half of all signals.

# On a Diagram

The key question is, when will more than half of the signals be above average? Suppose you have a prior over $t$ that is uniform between 0 and 1, and you receive a signal $s$, from which you make an inference $E[t\|s]$. Then under what conditions will more than half of the signals have $E[t\|s]>\frac{1}{2}$? 

We make a couple of assumptions: the signal is $s=m+u$, where $m$ is chosen strategically by the sender who pays a cost $c(m-t)$, and $u$ is drawn from a symmetric bounded distribution. This graph shows all the possible combinations of $u$ and $t$, and the red line is the receiver's threshold, i.e. the value $k$ such that $E[t\|s=k]=0$. If you receive a signal above this threshold then you believe $t>\frac{1}{2}$, and so you perform the action that I want you to perform. 

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

The two quantities we are interested in are the area below the curve (A), and the expectation along the curve (E):

$$\begin{align} A &= \int g(u)t(u)du \\
  E &= \frac{\int t(u)|t'(u)|g(u)du}{\int |t'(u)|g(u)du} \end{align}$$

We say that *persuasion* occurs if A<E: this means that the area below the curve is less than the expectation along the curve, so if the expectation along the curve is $\frac{1}{2}$ then more than half of the signals are above average (i.e., more than half have $E[t\|s]>\frac{1}{2}$).

Given this setup we can make a series of observations about equilibrium:

**Observations about the existence of persuasion:**

1. **If $m(t)$ is linear there will be no persuasion.** If $m(t)$ is linear, then $t(u)$ is linear and $t'(u)$ is a constant, and in the expression for $E$ it will cancel out, so $A=E$.
2. **If $m(t)$ is concave there will be persuasion.**  If $m(t)$ is concave then $t(u)$ will be convex, as in the figure above, and then there will be relatively greater weight on higher values of $t$ in the expression for $E$ (this is because $\|t'\|$ will be high when $t$ is high), so $E>A$. 
4. **If $m(t)$ is chosen subject to a cost c(m-t) there will be persuasion.** Suppose $m$ is chosen strategically, where the benefit is the probability of getting over the threshold ($G(m-k)$), and the cost is some convex function $c(m-t)$. Then the first-order condition will be:
    $$\pi g(m-k)=c'(m-t)$$
    and we can rewrite this as:
    $$t=m-r(g(m-k))$$
    where $r(\cdot)=c'^{-1}(\cdot)$ 
    This function is linear-symmetric around $k$.  so satisfies the above condition, *so persuasion occurs*.

**Observations about the receiver's utility:**

1. **The receiver's optimal commitment threshold admits half of all signals.** This is because .


**Observations about the receiver's utility:**

1. **The average benefits of persuasion equal the average costs.** The benefits of persuasion are just equal to A, i.e. admission. The cost will be:

    $$C=\frac{1}{2T}\int c(r(g(u))) du$$
    
    which is the area between the curve and the straight line (...).


## Notes

* **Borel-Kolmogorov paradox.** We have to be careful when defining a conditional expectation along a line, because falling on that line is a measure-zero event, and so the answer is only well-defined as a limit of expectations taken on positive-measure events (called the [Borel-Kolmogorove paradox](https://en.wikipedia.org/wiki/Borel%E2%80%93Kolmogorov_paradox). So what is a sensible limit to take? In the above diagram think of expanding the red line into a ribbon with positive width: but the answer changes whether the ribbon has positive *width* (limit w.r.t $u$) or positive *height* (limits w.r.t. $t$). A natural extension of the model is that you learn that the signal is between $[s-\delta,s+\delta]$, and form an expectation based on the signal falling within that ribbon. This is equivalent to a horizontal ribbon.

---

# IGNORE ALL THE REST -- it's all offcuts



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
