---
layout: post
title: Relative Thinking
---

There are a lot of cute thought experiments where the apparent value of something depends on comparisons:

* A \\$5 discount off a \\$20 radio feels more valuable than a \\$5 discount off a \\$500 bed.
* The difference between a 1% chance and a 2% chance seems more important than between a 51% chance and a 52% chance (likewise with 51 and 52 days vs 1 and 2 days).
* Paying \\$10 for 1 liter of ice cream seems more attractive if you see that the price of half-liter is \\$8
* If you're choosing between a low-price and medium-price version of a good, seeing that there's also a high-price version makes the medium-price version seem more attractive.
* If you have to judge the value of 10 of something -- e.g. bidding on 10 bottles of wine in an auction -- they'll seem more valuable if, at the same time, you're also considering a bid on a single bottle of wine; and vice versa if you're also considering a bid on 100 bottles of wine.
* (Writing out this list gives me a slightly nauseous nostalgia, like drinking Bacardi, it releases old unpleasant memories from working on my PhD when I wrote and rewrote lists like this dozens of time.)

Many people have felt that there's a common principle at work, in particular: that the sensitivity to an attribute (price, probability, square feet) depends on the set of quantities that you're considering. But the details of how that comparison effect works vary a lot:

* **Range**: sensitivity is decreasing in the range of values observed (i.e. the difference between the maximum and minimum) -- Volkmann (1951), Mellers & Cooke (1994), Bushong Schwarzstein & Rabin (2016)
* **Negative Range**: sensitivity is *increasing* in the range of values observed -- Koszegi & Szeidl (2003)
* **Proportional Range**: sensitivity is increasing in the *proportional* range of values (range over average) -- Bordalo Gennaioli & Shleifer (2013)
* **Frequency**: sensitivity at any point is proportional to the density of values in that neighborhood (Parducci (1965), Stewart Chater & Brown (2010))
* **Magnitude**: sensitivity is decreasing in the magnitude of the values (e.g. the average) -- Cunningham (2015).
- (plus there are theories with a reference point, e.g. **Loss Aversion** says you're more sensitive *below* a reference point, and **Diminishing Sensitivity** says you're more sensitive in the *neighborhood* of a reference point (both are in Tversky & Kahneman 1991)).


All of these models can be thought about as indifference curves that change slope as you change the elements in the choice set, e.g. adding option C changes the relative value of A and B:
$$
\xymatrix{\, &  &  &  &  & . & \,\, &  & \,\\
\, & A &  &  &  &  & A\\
\, &  &  & B & \ar@{-}[uullll] &  &  &  & B & \ar@{-}[uul]\\
\, &  &  &  &  &  &  &  &  &  C \\
\ar[uuuu]\ar[rrrr] &  &  &  & \ar@{-}[uullll] & \ar[uuuu]\ar[rrrr] &  &  & \ar@{-}[uuuull] & \,
}
$$

---

I'm going to try to make the following points:

1. **None of these laws is hardwired.** It's easy to find examples where relative-value effects go in the opposite direction predicted by each of the above laws. Each of the papers above are only able to give the impression of unifying all the observed effects by selective use of the evidence, selective use of predictions, or inconsistent interpretation of the laws that they propose.

2. However **each of these laws has intuitive appeal because it fits a rational inference in certain situations.** E.g., in some subset of cases the range of values *is* a good informative cue about the value of that attribute. However this is only true in a subset of cases, and when we step outside that subset, the law stops working, and instead behaviour is governed by the inference (and this explains where the counterexamples come from, as in the previous point). Thus each of these laws (range, magnitude, etc.) are given at the wrong level: we cannot predict comparison effects just from the distribution of quantities on each dimension.

3. Despite this, **relative-value effects are *not* entirely rational inferences.** We know that because many of the effects still work even when people are aware that there is no ground for the inference -- e.g. when the choice set is generated randomly. Thus the inferences must be being performed *pre-consciously*.

**A few other points that I'll leave for later:**

1. There are some cute tricks for identifying different types of relative-thinking effects through intransitive choices.
2. The quality of the evidence we have on almost all of these choice-set effects is very low. 
3. Weber's law is not relevant to diminishing sensitivity in choice.


## DIGRESSION: PERCEPTION

Comparison effects have been studied in perception for a long time, and it's a similar story there: at first people proposed that these were hardwired things, mechanical effects, but on further study it turned out that they were context-dependent, in a way that makes them look like sensible inferences.

Here's a classic contrast effect:
![](https://dl.dropboxusercontent.com/u/13046545/imgs/illusion_contrast.gif){: .center-image }
the same shade of grey looks darker when surrounded by white, than when surrounded by black.

For a long time psychology textbooks gave this as an example of a *hardwired* contrast effect -- i.e. this is caused by the basic wiring of neurons in our eyes.

But take a look at this (White's illusion):
![](https://dl.dropboxusercontent.com/u/13046545/imgs/illusion_white.png){: .center-image }

here the same shade of grey looks *lighter* on the left than on the right, despite the surroundings being relatively *lighter* on the left than on the right. This is exactly the opposite of what's predicted by a hardwired contrast efect in perception.

(An even cleaner example would be *ceteris paribus*, i.e. where making some part of the background lighter, all else held equal, makes the foreground appear lighter. The above illustration implies there must exist at least one such case: imagine a third set of grey rectangles which are surrounded only by white. That new case must serve as a *ceteris paribus* case for at least one of the two cases above (probably both).)

The general point is this: **There is not a stable relationship between the perceived-lightness of an object and the lightness of surrounding objects.** There isn't even an all-else-equal relationship. The relationship can run in either direction depending on the context.

But that's not the last word. We don't have to simply memorize a list of contexts where it goes one way (called "contrast effects"), or the other way ("assimilation effects"). Adelson (2001) shows that you can generally predict when you'll observe one effect or the other: roughly, whether or not the surrounding lightness is a positive or negative ecological cue for illumination. I.e., in typical circumstances, is the surrounding lightness positively or negatively associated with illumination? This also explains why contrast effects are observed more often than assimilation effects - because in most contexts the surrounding lightness a positive cue for illumination.

## DIGRESSION 2

I would write out lists of comparison-effect examples over and over while working on my PhD. My train of thought would get detached and I'd end up asking myself questions like: What are you doing sitting in this office, a continent away from your friends and a different continent away from your family? Why do you spend your weekends in this sad building, where people stare at the carpet when they pass each other? What rock did you hit in adolescence that knocked you out of orbit, and sent you here? Are you trying to compensate for something you didn't have? To impress your mother, avenge your father? Do these professors you work with look like the kind of man you want to be? Why, when you talk about your work, do the people you admire glaze over, and the people who bore you become interested? Do you think that giving your life to intellectual things makes you better than other people? Do you look down on people who don't think so clearly? What are you doing on a Friday night at the NBER eating a tuna subway sandwich and reading reddit? If it takes you 5 years to get straight one point about relative thinking -- one corner of one shelf in one cupboard -- then how long is it going to take to tidy up the whole house? When an undergraduate corners you, asking earnest & boring questions, doesn't it remind you of yourself?

![desk](https://dl.dropboxusercontent.com/u/13046545/imgs/nber_desk.jpg){: .center-image }

## ALTERNATIVE HEURISTICS

I'm going to discuss a few perfectly reasonable reasons why we might infer the value of different attributes from the choice set, and each reason will imply one of the above laws *in a subset of cases*. However I also show that the same reason can imply the exact opposite effect outside that subset.

### (1) **MRS shifting towards MRT.** 

A choice set which varies in different attributes has an implicit rate of tradeoff between the attributes -- i.e. the marginal rate of transformation (MRT) -- and it is easy to think of cases when our preferences would adapt to that implicit tradeoff, i.e., where our marginal rate of substitution (MRS) would rotate towards the MRT that is implicit in the choice set.

The MRS shifting towards the MRT could be rationalized in at least two ways. First, suppose you believe the social MRS to be informative about your own MRS, and you believe that the choice set reflects the market price, and finally, you believe that the price reflects the social MRS (as it would in a competitive equilibrium). Second, suppose you believe the person who constructed the choice set to be cooperative (in the sense of Grice (1967)) - i.e., they only include things which they believe to have similar values, then the MRT in the choice set reflects their beliefs about your MRS, which is itself informative. For example: if I'm staying in your spare room and me you and you ask me “would you prefer a poached egg or gruel for breakfast?” then I will infer that your gruel must be pretty good.

If there are just two attributes (i,j) and two alternatives (a,b) then the implicit tradeoff is $MRT_{i,j}=\frac{\|a_{i}-b_{i}\|}{\|a_{j}-b_{j}\|}$. If the MRS rotates to meet this MRT then the sensitivity to attribute $i$ will be decreasing in the range observed along that dimension, exactly as implied by the range-sensitivity theory (V, M&C, BR&S).

**However the MRS-MRT effect implies range sensitivity only for a 2-attribute, 2-alternative case. Outside of that case the intuitions depart.**

A marginal rate of transformation can only be directly identifed from a menu if the number of alternatives is equal to the number of attributes. I.e., to define a plane in $n$ dimensions from a set of points, you'll need exactly $n$ points. If you have fewer then it becomes the statistical problem of fitting a line to a set of points - e.g. by using orthogonal regression. Here is a simple example where the MRT theory and other theories (e.g. range-sensitivity) give qualitatively different answers, and in which the MRS-MRT theory seems more faithful to the intuition. Suppose we have the following three options:

$$
\xymatrix@C=1em@R=1em{
 & \binom{\mbox{100K salary}}{\mbox{199 days off}}\\
 \\
 &  & \binom{\mbox{105K salary}}{\mbox{189 days off}} & \binom{\mbox{110K salary}}{\mbox{189 days off}}\\
\\
\ar[rrrr]\ar[uuuu] & & &  &  & \, \\
}
$$

The intermediate option is dominated by the by the option on the right, and intuitively - to me - the existence of the intermediate option makes the rightmost option more desirable - because the choice set makes 10-days-off seem to be worth between $5K and $10K, meaning the higher salary is cheap, in terms of days-off. This intuition is not captured by range sensitivity, because the third option does not change the range in either dimension. The third option *does* change the implicit MRS, in the sense of the best-fitting line (e.g. orthogonal regression), and the change will be in favor of the rightmost option.

Even in the 3-attribute 3-alternative case, it is no longer true that $MRT_{i,j}$ is equal to the ratio of ranges on dimension i and j.

When one attribute is a good and the other is a bad (e.g. price and quality; salary and hours) it is sometimes reasonable to think that choosing *neither* alternative is an additional implicit element of the choice set, i.e. the point (0,0). In these cases the ratio of the ranges reduces to the ratio of the maximum values ($\frac{\max_{c\in C}c_{i}}{\max_{c\in C}c_{j}}$), which has similar comparative statics to the theory in (C) - which depends on the ratio of average values - than the theory in (BRS) - which depends on the ratio of the ranges.

Another interesting fact: the effects of this MRS-MRT theory will not be detectable when the choice set is binary: suppose your MRS shifts towards the MRT implicit in the choice set, then although your final MRS will be closer to the MRT, it will not *cross* the MRT, i.e. the shift in MRS will not alter which of the two elements you prefer. This implies that the MRS-MRT theory cannot rationalize the existence of cycles in binary choice, and so cannot explain evidence for 'subadditivity' of different dimensions, such as probability, money, or delay (see Read (2001) for citations). For example, if your have a prior belief that $a$ is better than $b$, and then you observe a choice set containing $a$ and $b$, then you may revise upward your valuation of $b$ relative to $b$, but this observation wouldn't cause you to switch preference, i.e. to think that $b$ must be better than $a$. (This is under the assumption that the posterior MRS is *between* the prior MRS and the MRT; this assumption could be violated under some unusual priors, e.g. if you had bimodal beliefs about the value of b).

### (2) MRS shifting towards demand.

There is a second strong intuition for choice sets influencing demand: the combinations offered often tend to reflect the combinations desired, so a relative increase in attribute 1 could be interpreted as a positive signal about the value of attribute 1. Suppose we manipulate the choice set, while keeping the relative price fixed, for example consider these two choice sets, trading off the price and quantity of some good:

$$
\xymatrix@C=.5em@R=.5em{\ar[rrrrr]\ar[ddddd] & & &  &  & \text{apples}\\
 & \binom{\text{1 apple}}{\$1}\\
 &  & \binom{\text{2 apples}}{\$2}\\
 &  & & \binom{\text{3 apples}}{\$3}\\
\\
\\
\$ }
$$

$$
\xymatrix@C=.5em@R=.5em{\ar[rrrrr]\ar[ddddd] & & & &  & \text{apples}\\
 & \,\,\,\,\,\, & \\
 & & \binom{\text{2 apples}}{\$2}\\
 & & & \binom{\text{3 apples}}{\$3}\\
 & & & & \binom{\text{4 apples}}{\$4}\\
\\
\$ }
$$

A natural intuition is that people will tend to switch from $\binom{2}{\$2}$ to $\binom{3}{\$3}$, when going from the first to the second choice set. It is notable that none of the theories discussed gives an unambiguous prediction about the change in MRS between these two choice sets - because both the range and magnitude change by the same amount on each dimension - yet the intuition remains quite clear (I think).

This idea could be easily formalized - suppose people know the supply curve but are uncertain about the demand curve - then when they observe an increase in quantity (and infer that this because other people demand more) - then they infer an increase in value of the good. This is the exactly the intuition given in Kamenica (2008) - when you observe a higher price/quantity combination, you infer that demand is higher, and so you infer that the value of each marginal good must be higher. I think that a similar foundation is used in Drolet, Simonson, Tversky (2000) “Indifference Curves that Travel with the Choice Set”.

We have discussed diagonal shifts along the budget set, meaning that both attributes are varying at once; if only one attribute varied, it's not clear what a consumer would infer from this.Of course we could formalize a model where the consumer is uncertain about both supply and demand; or we could combine this model with the prior one, where the consumer is uncertain about the price.

### (3) Magnitude effects.

Finally it's easy to come up with a rational magnitude effect, such that when we observe a higher quantity q  we infer that the marginal value of each unit is less. Suppose we know the price and consumption-value of a good, when measured in units that are familiar to us, but we do not know the units that are used in the packaging. Then if we observe other people consuming a higher quantity (measured in unfamiliar units), we infer that each unit is worth less: e.g., observing a 10,000 Kronor bank note we infer each Kronor is not worth a lot; observing a 10,000 Watt bulb, we infer each Watt is worth less; observing 200mg of Oxytocin, we infer each milligram is less valuable. These examples rely on just observing quantities, not prices.

## SUMMARY




## MISCELLANEOUS NOTES

* It is useful to make a sharp distinction between “goods” and 'bads”. E.g., a good-bad tradeoff: e.g., quality vs price; salary vs hours worked. A Good-Good tradeoff: e.g., bedrooms vs bathrooms; MPG vs horsepower; salary vs holiday-days.

* Parducci invented, as well as range-frequency theory, windsurfing.

* Bordalo Gennaioli and Shleifer (2013) has a weird feature: the *salience* of an attribute depends on relative levels ($q-\bar{q}$ and $p-\bar{p}$), but the *utility* of an attribute depends on absolute levels ($q$ and $p$). I think this is just a mistake -- the underlying intuition is matched much better if  $U(q,p) = \hat{\theta}_q(q-\bar{q}) + \hat{\theta}_p(p-\bar{q})$ instead of $U(q,p) = \hat{\theta}_q + \hat{\theta}_p p$. This removed a lot of the weird comparative statics of the theory, such as the severe non-monotonicity of the decoy effects. Also for two-alternative two-attribute choices the theory (as stated in the paper) has a utility representation, i.e. many of the predictions of that paper are equivalent to a model with menu-*independent* preferences:

  $$
  U(q,p)=\begin{cases}
  \delta q-p & ,\,q<\delta p\\
  M+\ln q-\ln p & ,\delta p<q<\delta^{-1}p\\
  M+q-\delta p & ,\,q>\delta^{-1}p
  \end{cases}
  $$


* Both of these sentences make sense:
    > The church looked big because I was expecting it to be big

    > The church seemed small because I was expecting it to be big
    
    (more generally: pairs of contradictory sentences which are both true, because of Gricean cooperative interpretation)


## REFERENCES

KS: Koszegi and Szeidl (2011) (KS)

BRS: Bushong Schwarzstein & Rabin (2014)

MC: Mellers & Cooke ()

C: Cunningham (2013)

BGS: Bordalo Gennaioli Shleifer (2012) 

Simonson (2008) "Will I like a Medium Pillow?"
 
> “much of the evidence for preference construction reflects people’s difficulty in evaluating absolute attribute values and tradeoffs and their tendency to gravitate to available relative evaluations ... These illustrations suggest that many forms of preference construction reflect a key underlying principle: decision makers tend to avoid absolute value judgments and gravitate to accessible relative evaluations ... it is noteworthy that the evidence that has been accumulated to make the case for preference construction might be largely driven by a rather simple common principle. This rather simple, yet important absolute-to-relative principle lends itself to seemingly unrelated demonstrations, which have been treated as distinct phenomena and received unique labels.”




## EXAMPLES

* These two choice sets {sea-facing room, suite} and {sea-facing room, suite with complimentary champagne}. The second choice set seems to imply a greater relative value of being sea-facing (and lower relative value of being a suite).

* If a hotel room with a sea view commands a $50 premium, compared to a $100 premium, again you assume that the sea view is more valuable. The same intuition applies for anything with a known upward-sloping supply curve: a higher price signifies greater value.

* suppose you ask me “would you prefer a holiday in Bilbao or San Francisco?” From this I would assume that Bilbao and San Francisco have a similar value.]

* If you observe the price of oranges is $100/each, you infer that oranges must be pretty good.

* If you observe that orange consumption is 10 per capita per day, you also infer that oranges must be pretty good.

* you see options at an ATM in Reyjkavik airport: 10,000Kr, 20,000Kr; larger options imply each Kr is worth less, but also make you want to get more. (Oh, because you also infer that the price of Kronor is lower).

* you're unsure how much you would like oysters, and you notice, at the market, that they have many oysters for sale. This could indicate a high demand for oysters (a positive signal of value).

* Suppose you observe that a certain drug comes in tablets with either 250mg and 500mg forms -- observing higher doses will make you infer lower effectiveness of marginal doses.

* when you see a camera with more megapixels, you might infer that the marginal value of each additional megapixel is smaller, yet also your desired choice (for a fixed price/megapixel) might increase.

