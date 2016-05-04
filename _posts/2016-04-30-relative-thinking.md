---
layout: post
title: Relative Thinking
---

### **NUTSHELL**
1.  A lot of people have suggested that, when we make decisions, our sensitivity to an attribute depends on the *relative* value of that attribute -- e.g. the value we put on 100 square feet differs depending on whether the 100 is being compared to 50 square feet, or to 200 square feet.

2. The idea seems simple but there have been surprisingly many alternative attempts at formalizing it. The simplest ones are:
    * **Range**: sensitivity is decreasing in the range of values observed (i.e. the difference between max and min) -- Volkmann (1951), Mellers & Cooke (1994), Bushong Schwarzstein & Rabin (2016).
    * **Proportional Range**: sensitivity is decreasing in the *proportional* range of values -- Bordalo Gennaioli & Shleifer (2013)
    * **Negative Range**: sensitivity is *increasing* in the range of values observed -- Koszegi & Szeidl (2003).
    * **Loss Aversion** -- sensitivity is higher *below* some salient reference point -- Tversky & Kahneman (1991).
    * **Diminishing Sensitivity** -- sensitivity is higher *near* some salient reference point -- Tversky & Kahneman (1991).
    * and my own proposal -- **Magnitude** -- that sensitivity is decreasing in the *magnitude* of the values (e.g. the average) -- Cunningham (2015).

3. Despite big formal differences these papers are largely motivated by the *same* set of thought experiments and laboratory findings -- they all talk about Weber's law, contrast illusions, compromise & asymmetric dominance effects, and common-difference effects.
4. A weakness in all of these papers is that they never really explain *why* we would have this particular bias -- why our judgments would be distorted in such a predictable fashion.

I'm going to try to make the following points:

1. There is no common solution to these diverse relative-thinking effects. There are multiple overlapping effects, and each of these papers could only give the impression of unifying all the effects by selective or ad-hoc use of the evidence.
2. Each of these laws can be identified with a rational inference from the situation. However the identification only works in a certain subset of cases, and indeed when we step outside that subset, the law stops working, and instead behaviour is governed by the rational inferece.
3. So are there just a lot of different overlapping effects? No - there is a common pattern: each pattern is *locally* rational, i.e. it's a good pattern of inference in that particular context. We can tell by playing with the thought experiments, to see how they vary.


A couple of other points that I will try to write about later:

1. There are some cute tricks for identifying different types of relative-thinking through intransitive choices.
2. The quality of the evidence we have on almost all of these choice-set effects is very low. 
3. Weber's law is not relevant to diminishing sensitivity in choice.
4. The situation is the same among psychologists studying perception: people have tried explaining the whole variety of different context-dependent effects with a single principle (e.g. lateral inhibition, divisive normalization), but they've only managed to stuff everything in a suitcase by mangling them. Sometimes effects go one way, sometimes they go another way.



## ALTERNATIVE HEURISTICS

There are multiple independent heuristics which we often use in adjusting preferences contingent on the choice set.

**MRS shifting towards MRT.** In multiattribute choice, a choice set can be interpreted as having an implicit rate of tradeoff between the attributes (the marginal rate of transformation (MRT)), and it is easy to think of cases when our preferences would adapt to that implicit tradeoff, i.e., the MRS rotates towards the MRT. This effect would follow from a prior belief that the elements in a choice set tend to have positively correlated values: E.g., if someone offers you a “bachooka”, you'll value it more highly if they say “bachooka or $100?” than if they say “bachooka or banana?”

  * If there are just two attributes (i,j) and two alternatives (a,b) then the implicit tradeoff is $MRT_{i,j}=\frac{\|a_{i}-b_{i}\|}{\|a_{j}-b_{j}\|}$. If the MRS rotates to meet this MRT then the sensitivity to attribute $i$ will be decreasing in the range observed along that dimension, exactly as implied by the range-sensitivity theory (V, M&C, BR&S).

  * **However the MRS-MRT effect implies range sensitivity for a 2-attribute, 2-alternative case. Outside of that case the intuitions depart.**

  * The MRS shifting towards the MRT could be rationalized in at least two ways: (i) suppose you believe the social MRS to be informative about your own MRS, and you believe that the choice set reflects the market price, and finally, you believe that the price reflects the social MRS (as it would in a competitive equilibrium); (ii) suppose you believe the person who constructed the choice set to be cooperative (in the sense of Grice (1967)) - i.e., they only include things which they believe to have similar values, then the MRT in the choice set reflects their beliefs about your MRS, which is itself informative.For example: if I ask “would you prefer a poached egg or gruel for breakfast?” it's likely that I will infer that the gruel must be quite good.


  * However a marginal rate of transformation can only be derived from a menu if the number of alternatives is equal to the number of attributes. I.e., to define a plane in $n$ dimensions from a set of points, you'll need at least $n$ points. If you have fewer then it becomes the well-known problem from statistics of fitting a line (or curve) to a set of points - e.g. by using orthogonal regression. Here is a simple example where the MRT theory and other theories (e.g. range-sensitivity) give qualitatively different answers, and in which the MRS-MRT theory seems more faithful to the intuition. Suppose we have the following three options:
  
    $$
    \left\{ \binom{\mbox{100K salary}}{\mbox{199 days off}},\binom{\mbox{110K salary}}{\mbox{189 days off}},\binom{\mbox{105K salary}}{\mbox{189 days off}}\right\}
    $$

    The third option is dominated by the second option, and intuitively - to me - that makes the 2nd option more desirable - because it makes it seem a better deal. This intuition is not captured by range sensitivity, because the third option does not change the range in either dimension. The third option will change the implicit price (in the sense of the best-fitting line, i.e. orthogonal regression), and the change will be in favor of the second option.

* Even in the 3-attribute 3-alternative case, it is no longer true that $MRT_{i,j}$ is equal to the ratio of ranges on dimension i and j.

* When one attribute is a good and the other is a bad (e.g. price and quality; salary and hours) it is sometimes reasonable to think that choosing *neither* alternative is an additional implicit element of the choice set, i.e. the point (0,0). In these cases the ratio of the ranges reduces to the ratio of the maximum values ($\frac{\max_{c\in C}c_{i}}{\max_{c\in C}c_{j}}$), which has similar comparative statics to the theory in (C) - which depends on the ratio of average values - than the theory in (BRS) - which depends on the ratio of the ranges.

* Another interesting fact: the effects of this MRS-MRT theory will not be detectable when the choice set is binary: suppose your MRS shifts towards the MRT implicit in the choice set, then although your final MRS will be closer to the MRT, it will not *cross* the MRT, i.e. the shift in MRS will not alter which of the two elements you prefer. This implies that the MRS-MRT theory cannot rationalize the existence of cycles in binary choice, and so cannot explain evidence for 'subadditivity' of different dimensions, such as probability, money, or delay (see Read (2001) for citations). For example, if your have a prior belief that $a$ is better than $b$, and then you observe a choice set containing $a$ and $b$, then you may revise upward your valuation of $b$ relative to $b$, but this observation wouldn't cause you to switch preference, i.e. to think that $b$ must be better than $a$. (This is under the assumption that the posterior MRS is *between* the prior MRS and the MRT; this assumption could be violated under some unusual priors, e.g. if you had bimodal beliefs about the value of b).

**MRS shifting towards demand.** There is a second strong intuition for choice sets influencing demand: the combinations offered often tend to reflect the combinations desired, so a relative increase in attribute 1 could be interpreted as a positive signal about the value of attribute 1. Suppose we manipulate the choice set, while keeping the relative price fixed, for example consider these two choice sets, trading off the price and quantity of some good:

$$
\left\{ \binom{1}{\$1},\binom{2}{\$2},\binom{3}{\$3}\right\}
\left\{ \binom{2}{\$2},\binom{3}{\$3},\binom{4}{\$4}\right\}
$$

A natural intuition is that people will tend to switch from $\binom{2}{\$2}$ to $\binom{3}{\$3}$, going from the first to the second choice set. It is notable that none of the theories discussed gives an unambiguous prediction about the change in MRS between these two choice sets - because both the range and magnitude change by the same amount on each dimension - yet the intuition remains quite clear (I think).

This idea could be easily formalized - suppose people know the supply curve but are uncertain about the demand curve - then when they observe an increase in quantity (and infer that this because other people deamnd more) - then they infer an increase in value of the good. This is the exactly the intuition given in Kamenica (2008) - when you observe a higher price/quantity combination, you infer that demand is higher, and so you infer that the value of each marginal good must be higher.I think that a similar foundation is used in Drolet, Simonson, Tversky (2000) “Indifference Curves that Travel with the Choice Set”.

We have discussed diagonal shifts along the budget set, meaning that both attributes are varying at once; if only one attribute varied, it's not clear what a consumer would infer from this.Of course we could formalize a model where the consumer is uncertain about both supply and demand; or we could combine this model with the prior one, where the consumer is uncertain about the price.

**Magnitude effects.** Finally it's easy to come up with a rational magnitude effect, such that when we observe a higher quantity q  we infer that the marginal value of each unit is less. Suppose we know the price and consumption-value of a good, when measured in units that are familiar to us, but we do not know the units that are used in the packaging. Then if we observe other people consuming a higher quantity (measured in unfamiliar units), we infer that each unit is worth less: e.g., observing a 10,000 Kronor bank note we infer each Kronor is not worth a lot; observing a 10,000 Watt bulb, we infer each Watt is worth less; observing 200mg of Oxytocin, we infer each milligram is less valuable. These examples rely on just observing quantities, not prices.



# ADDITIONAL NOTES

It is useful to make a sharp distinction between “goods” and 'bads”, as shown in these diagrams:

$$
\xymatrix{\ar[rrrr]\ar[dddd] &  &  &  & \,\\
 & A\\
 &  & B\\
\\
\,
}
$$

**A Good-Bad tradeoff: e.g., quality vs price; salary vs hours worked.**

$$
\xymatrix{\,\\
 & A\\
 &  & B\\
\\
\ar[rrrr]\ar[uuuu] &  &  &  & \,\\
}
$$

**A Good-Good tradeoff: e.g., bedrooms vs bathrooms; MPG vs horsepower; salary vs holiday-days.**




## Miscelllaneous Notes

* Parducci invented, as well as range-frequency theory, windsurfing.

* Bordalo Gennaioli and Shleifer (2013) should've been $U(q,p) = \hat{\theta}_q(q-\bar{q}) + \hat{\theta}_p(p-\bar{q})$ instead of $U(q,p) = \hat{\theta}_q + \hat{\theta}_p p$. Also for two-alternative two-attribute choices the theory has a utility representation, i.e. most of the predictions of that paper are equivalent to a model with menu-*independent* preferences:

  $$
  U(q,p)=\begin{cases}
  \delta q-p & ,\,q<\delta p\\
  M+\ln q-\ln p & ,\delta p<q<\delta^{-1}p\\
  M+q-\delta p & ,\,q>\delta^{-1}p
  \end{cases}
  $$


## References

KS: Koszegi and Szeidl (2011) (KS)

BRS: Bushong Schwarzstein & Rabin (2014)

MC: Mellers & Cooke ()

C: Cunningham (2013)

BGS: Bordalo Gennaioli Shleifer (2012) 



## Examples

* These two choice sets {sea-facing room, suite} and {sea-facing room, suite with complimentary champagne}. The second choice set seems to imply a greater relative value of being sea-facing (and lower relative value of being a suite).

* If a hotel room with a sea view commands a $50 premium, compared to a $100 premium, again you assume that the sea view is more valuable. The same intuition applies for anything with a known upward-sloping supply curve: a higher price signifies greater value.

* suppose you ask me “would you prefer a holiday in Bilbao or San Francisco?” From this I would assume that Bilbao and San Francisco have a similar value.]

* If you observe the price of oranges is $100/each, you infer that oranges must be pretty good.

** If you observe that orange consumption is 10 per capita per day, you also infer that oranges must be pretty good.

* you see options at an ATM in Reyjkavik airport: 10,000Kr, 20,000Kr; larger options imply each Kr is worth less, but also make you want to get more. (Oh, because you also infer that the price of Kronor is lower).

* you're unsure how much you would like oysters, and you notice, at the market, that they have many oysters for sale. This could indicate a high demand for oysters (a positive signal of value).

* Suppose you observe that a certain drug comes in tablets with either 250mg and 500mg forms -- observing higher doses will make you infer lower effectiveness of marginal doses.

*– when you see a camera with more megapixels, you might infer that the marginal value of each additional megapixel is smaller, yet also your desired choice (for a fixed price/megapixel) might increase.

