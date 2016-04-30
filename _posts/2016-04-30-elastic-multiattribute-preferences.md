---
layout: post
title: Elastic Multiattribute Preferences
---

## Observations:

* Nutshell: (1) there exist various anomalies in multiattribute choice: (a) decoy effects; (b) intransitive choices; (c) diminishing sensitivity; (d) change in reference point; (e) changes between joint and separate evaluation.(2) these anomalies are difficult to explain as due to noisy perception because people rarely choose a dominated alternative, & so they are generally described as due to context-sensitive or comparative preferences.(3) however different papers have proposed about half a dozen different models to unify these effects.(4) there are various plausible ecologically valid heuristics: (a) MRT represents value; (b) larger quantity implies less value; ... .

* The attraction of menu-dependent theories: Suppose we observe some choice anomaly, i.e. choices inconsistent with the assumptions we put on the utility curve u(x). There are a few basic approaches about what's happening:

    1. people have unorthodox preferences -- so we change our assumptions about u(x), e.g. by adding a “taste” or “aversion.”

    2. people have orthodox preferences but misperceive the choice set - so we assume people have biased or imperfect perception, i.e. they maximize u(\hat{x}(x))

    3. people have orthodox preferences but their preferences systematically change with the choice set, - so we model people as make decisions using u(x,A).

   An argument against the first is that many biases do not seem like an expression of genuine preferences, because they often appear only in indirect choice (another way of putting it: they can be characterized by intransitivities). An argument against the second is that people, in normal laboratory situations, do seem to perceive the choice set accurately - well enough to avoid making dominated choices. The third implies that we are trying to make orthodox decisions, but we have difficulty holding onto our preferences.

    When studying menu-dependence in general, we will do our identification with transitivity violations.

* The attraction of multiattribute choice. Many choices are between bundles of attributes. This allows more structure on having menu-dependent preferences. Esp., there are some observations that seem to cut across attributes: (i) diminishing sensitivity; (ii) contrast; (iii) reference-dependence; etc..

*  Existing literature: There are a lot of recent models of menu-dependent multiattribute choice.Also called “menu-dependent preferences”, “contingent-weighting” or “contingent valuation”. There are at least a dozen more models which fall into the same class, and the idea that sensitivity is related to the menu is popular in the marketing literature. For example, tradeoffs between price and quality, probability of a prize and size of the prize, hours of work and payment, bathrooms and bedrooms in a house, salary and holiday-days. Each of these models proposes that sensitivity to a dimension depends on the distribution of values along that dimension: in Koszegi and Szeidl (2011) (KS) sensitivity is positively related to the range of values on an attribute (i.e., maximum minus minimum); in Bushong et al. (2014) (BRS) it is negatively related to the range; in Cunningham (2012) (C) it is negatively related to the average; and in Bordalo et al. (2012) (BGS) it is negatively related to the proportional range.

* Notation. Suppose that we have a menu-dependent utility function, $u(x,A)$, where $A$ is the choice set, or more generally the “comparison set.” $x\in\mathbb{R}^{n}$, and $A\subseteq\mathbb{R}^{n}$. We will assume that all attributes have positive value ($\frac{\partial u}{\partial x_{i}}>0$), meaning that an attribute which represents a bad, such as the price of a good, will be represented as a negative number. It is useful to make a sharp distinction between “goods” and 'bads”, as shown in these diagrams:

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

## Different heuristics. 

There are multiple independent heuristics which we often use in adjusting preferences contingent on the choice set.

**MRS shifting towards MRT.** In multiattribute choice, a choice set can be interpreted as having an implicit rate of tradeoff between the attributes (the marginal rate of transformation (MRT)), and a natural assumption is that our preferences adapt to that implicit tradeoff, i.e., the MRS rotates towards the MRT. This effect would follow from a prior belief that the elements in a choice set tend to have positively correlated values: E.g., if someone offers you a “bachooka”, you'll value it more highly if they say “bachooka or $100?” than if they say “bachooka or banana?”

  * The MRS shifting towards the MRT could be rationalized in at least two ways: (i) suppose you believe the social MRS to be informative about your own MRS, and you believe that the choice set reflects the market price, and finally, you believe that the price reflects the social MRS (as it would in a competitive equilibrium); (ii) suppose you believe the person who constructed the choice set to be cooperative (in the sense of Grice (1967)) - i.e., they only include things which they believe to have similar values, then the MRT in the choice set reflects their beliefs about your MRS, which is itself informative.For example: if I ask “would you prefer a poached egg or gruel for breakfast?” it's likely that I will infer that the gruel must be quite good.

  * If there are just two attributes (i,j) and two alternatives (a,b) then the implicit tradeoff is $MRT_{i,j}=\frac{\|a_{i}-b_{i}\|}{\|a_{j}-b_{j}\|}$. If the MRS rotates to meet this MRT then the sensitivity to attribute $i$ will be decreasing in the range observed along that dimension, exactly as implied by the range-sensitivity theory of BR&S.

  * A MRT can only be directly derived from the menu if the number of alternatives is equal to the number of attributes. I.e., a hyperplane in an $n$-dimensional space requires a set of $n$ points. However if this is not true then it becomes the well-known problem from statistics of fitting a line (or curve) to a set of points - e.g. by using orthogonal regression. Here is a simple example where the MRT theory and other theories give qualitatively different answers, and in which the MRS-MRT theory seems more faithful to the intuition. Suppose we have the following three options:
  
  $$
  \left\{ \binom{\mbox{100K salary}}{\mbox{199 days off}},\binom{\mbox{110K salary}}{\mbox{189 days off}},\binom{\mbox{105K salary}}{\mbox{189 days off}}\right\}
  $$

  The third option is dominated by the second option, and intuitively it might make the 2nd option more desirable - because it comes to seem a better deal. This intuition is not captured by the BR&S theory, because the third option does not change the range in either dimension. The third option will change the implicit price (in the sense of the best-fitting line, i.e. orthogonal regression), and the change will be in favor of the second option.

* Even in the 3-attribute 3-alternative case, it is no longer true that $MRT_{i,j}$ is equal to the ratio of ranges on dimension i and j.

* When one attribute is a good and the other is a bad (e.g. price and quality; salary and hours) it is sometimes reasonable to think that choosing neither is an additional implicit element of the choice set, i.e. the point (0,0). In these cases the ratio of the ranges reduces to the ratio of the maximum values ($\frac{\max_{c\in C}c_{i}}{\max_{c\in C}c_{j}}$), which has similar comparative statics to the theory in (C) - which depends on the ratio of average values - than the theory in (BRS) - which depends on the ratio of the ranges.

* The effects of this MRS-MRT theory will not be detectable when the choice set is binary: suppose your MRS shifts towards the MRT implicit in the choice set, then although your final MRS will be closer to the MRT, it will not cross the MRT, i.e. the shift in MRS will not alter which of the two elements you prefer. This implies that the MRS-MRT theory cannot rationalize the existence of cycles in binary choice, and so cannot explain evidence for 'subadditivity' of different dimensions, such as probability, money, or delay (see Read (2001) for citations). E.g. if your prior is that a is better than b, and then you observe a choice set with a and b, then you may revise upward your valuation of b, and downward your valuation of a, but the observation wouldn't cause you to switch preference, thinking that b must be better than a. (This is under the assumption that the posterior MRS is between the prior MRS and the MRT; this assumption could be violated under some unusual priors, e.g. if you had bimodal beliefs about the value of b).

**MRS shifting towards demand.** There is a second strong intuition for choice sets influencing demand: the combinations offered often tend to reflect the combinations desired, so a relative increase in attribute 1 could be interpreted as a positive signal about the value of attribute 1. Suppose we manipulate the choice set, while keeping the relative price fixed, for example consider these two choice sets, trading off the price and quantity of some good:

$$
\left\{ \binom{1}{\$1},\binom{2}{\$2},\binom{3}{\$3}\right\}
\left\{ \binom{2}{\$2},\binom{3}{\$3},\binom{4}{\$4}\right\}
$$

A natural intuition is that people will tend to switch from $\binom{2}{\$2}$ to $\binom{3}{\$3}$, going from the first to the second choice set. It is notable that none of the theories discussed gives an unambiguous prediction about the change in MRS between these two choice sets - because both the range and magnitude change by the same amount on each dimension - yet the intuition remains quite clear (I think).

This idea could be easily formalized - suppose people know the supply curve but are uncertain about the demand curve - then when they observe an increase in quantity (and infer that this because other people deamnd more) - then they infer an increase in value of the good. This is the exactly the intuition given in Kamenica (2008) - when you observe a higher price/quantity combination, you infer that demand is higher, and so you infer that the value of each marginal good must be higher.I think that a similar foundation is used in Drolet, Simonson, Tversky (2000) “Indifference Curves that Travel with the Choice Set”.

We have discussed diagonal shifts along the budget set, meaning that both attributes are varying at once; if only one attribute varied, it's not clear what a consumer would infer from this.Of course we could formalize a model where the consumer is uncertain about both supply and demand; or we could combine this model with the prior one, where the consumer is uncertain about the price.

**Magnitude effects.** Finally it's easy to come up with a rational magnitude effect, such that when we observe a higher quantity q  we infer that the marginal value of each unit is less. Suppose we know the price and consumption-value of a good, when measured in units that are familiar to us, but we do not know the units that are used in the packaging. Then if we observe other people consuming a higher quantity (measured in unfamiliar units), we infer that each unit is worth less: e.g., observing a 10,000 Kronor bank note we infer each Kronor is not worth a lot; observing a 10,000 Watt bulb, we infer each Watt is worth less; observing 200mg of Oxytocin, we infer each milligram is less valuable. These examples rely on just observing quantities, not prices.

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

## Observations about multiattribute choice in the lab:

* infrequency of dominated choice. People rarely choose dominated options. More precisely: if we rank experiments by the complexity of the choice set (e.g., the number of attributes), then people only start choosing dominated options when they become fairly complex, typically with 3 or more attributes, but they show other biases at a much lower level, with just 2 or more attributes.

* low quality evidence on decoy effects. A decoy-effect experiment shows that people choose x from \{x,y\} but y from \{x,y,z\}. Here z
  is the “decoy”, and if people are maximizing a menu-independent utility function then adding a decoy shouldn't affect preference between existing options. There are many examples of these effects in psychology and economics, sometimes classified into particular types: (i) people are more likely to choose an alternative if another alternative is dominated by it (“asymmetric dominance effect”); (ii) people are more likely to choose an alternative if it is (“compromise effect”).Frederick, Lee & Baskin (2015) “The Limits of Attraction”.

## Miscelllaneous Notes

* Some common bias across domains: Simonsohn paper. Other similarities: (1) oversensitive to small differnces; (2) diminishing sensitivity, common-difference effects; (3) compromise & asymmetric dominance effects; (4) sensitivity to reference point; (5) implied answer in the question - Schwartz.

* The existing papers (C, BGS, BRS) all attempt to explain roughly the same facts. So there must be sloppiness in their discussion. Some mix of (a) selectively choosing results which fit their model; and (b) playing with interpretation to get a better fit.

– reference point effects.

– transitivity.

– diminishing sensitivity.

– RT and choice-difficulty (suggests noise in attributes, not noise in indifference-curves)

– judgment of fact and judgment of preference

– variety of general multiattribute theories (Rabin, Koszegi, Shleifer, etc), each has an appealing but distinct intuition


## References



