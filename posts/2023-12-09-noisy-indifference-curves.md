---
title: Noisy Indifference Curves
subtitle: Against Inattention as an Explanation of Textbook Anomalies
author: Tom Cunningham
draft: true
date: 2023-12-09
---

<!-- https://tecunningham.github.io/posts/2023-12-09-noisy-indifference-curves.html -->

**In short: the classical choice anomalies don't seem to be due to inattention, because:**


1. **People have sufficient attention to answer mathematical questions.**
2. **People have sufficient attention to avoid dominated alternatives.**
3. **People consistently make the *same* anomalous choices.**


#           Explaining Anomalies

The theory of rational choice was formalized in the 1940s and 50s, and then between the 1950s and 70s various *anomalies* were discovered -- i.e. scenarios where the theory contradicted our intuitive choices (due to, among others, Allais, Ellsberg, Tversky, & Kahneman).

Motivated by the anomalies people have proposed various theories of choice to try to tie them together -- to give a unified descriptive theory of choice -- but fifty years later it seems we have not made much progress. There is little concensus on deep explanations for the anomalies, no-one has yet pulled the sword from that stone.

Here are three basic approaches to choice anomalies:

1. **Weird indifference curves:** People have unorthodox preferences -- i.e. people have stable preferences, but the preferences are not orthodox, meaning they don't obey the typical rational choice axioms. For example prospect theory, non-exponential discounting, ambiguity aversion.
2. **Noisy choice sets:** People have orthodox preferences, but they don't perceive perfectly the choice that they face -- i.e. "inattention" type theories.
3. **Noisy indifference curves:** People have orthodox preferences, but the preferences change with each new choice set -- sometimes called "relative thinking" or "contingent weighting".


#           Against Inattention for Textbook Anomalies

Each of the three departures from rational choice has a place, but I'll just make a quick point here: the "inattention" theory -- rational or otherwise -- cannot explain the typical textbook anomalies. By textbook anomalies I mean, for example, the Allais paradoxes, the Ellsberg paradoxes, small-scale risk aversion, reflection effects, loss aversion, decoy effects, common-difference effects ("jacket-calculator" problems), that sort of thing.

My argument will be very brief.

Inattention-style theories (e.g. those of Woodford, Caplin, Gabaix, Rangel, Glimcher) say that people violate rational choice because they misperceive the alternatives. For example, which would you choose from the following?

<!-- NOTE: need special HTML &zwnj; otherwise it interprets it as a list marker -->
- (&zwnj;A) a 50% chance of $11
- (&zwnj;B) a 100% chance of $5

A lot of people would choose B over A. This is often regarded as an anomalous choice because it implies a high level of risk aversion. I'll use this as a working example but I think the argument can be adapted to any of the other textbook anomalies.

If you wanted to explain the above choice with an inattention-style theory you would say that people have rational preferences -- i.e., they *really* would prefer option (A) -- but they have an imperfect perception of the outcomes which causes them to choose (B). E.g., they sometimes choose (B) because they sometimes misread "50% chance" as "60% chance," or they don't read the exact amount of money and instead get a vague sense, like "a small amount of money." Given their imperfect perception of the choice-set they make rational choices. Taken as a set their choices exhibit anomalies.

Here are three reasons why I think this is an unlikely explanation of most textbook anomalies:

##       (1) People don't make the same mistakes when doing algebra.

How would you choose in each of the following choice sets?

* (A') a 50% share of $\$11$ (i.e., $\frac{\$11}{2}$)
* (B') a 100% share of $5

I think very few people would choose (B') over (A'). Of course not everyone is good at algebra -- but it is true that people who *are* good at algebra (e.g. economics students and professors) still make anomalous choices over gambles.

##       (2) People don't make dominated choices.

Which of the following would you choose?

- (A'') a 50% chance of $11
- (B'') a 50% chance of $10

If you have noisy perception of outcomes, then you should, at least occasionally, choose (B''). But in fact people very rarely make dominated choices. More precisely, while choice anomalies are observed for very simple alternatives, people only begin making dominated choices when the outcomes become moderately complex (e.g., gambles with 3 outcomes). Carbone (1995) find that people often make inconsistent choices, but rarely choose a dominated option:

   > “[w]hat is startling ... are the results of the satisfaction or violation of dominance ... [with a] mean violation rate of just 0.3 percent. In contrast the average inconsistency rate of the repeated pairs was 12 percent.”

Similar findings are described in Loomes (1998) and Hey (2001).

People do sometimes directly choose a stochastically dominated gamble, but most example in the literature involve choices among gambles with at least four different outcomes, e.g. Tversky et al. (1986). Caplin et al. (2013) find mistakes when subjects have to count a large number of dots. In experiments documenting “bracketing”, subjects make dominated choices only when they have to combine pairs of gambles (Tversky 1981, Rabin 2009).

You could defend the inattention theory by saying that people have a two-stage process: they first detect and remove dominated choices, and only then go to the trouble of doing the algebra. This means positing a separate cognitive process which has much less noise in its perception, and so the theory loses some of its elegance. But even then you still have a problem with near-dominated choices. Which of the following would you choose?

* (A''') a 50% chance of $11
* (B''') a 50.1% chance of $10

Neither alternative dominates the other, so the dominance rule won't apply. An inattention-based theory says that a significant fraction of people will choose (B'''). But I suspect that almost no-one would choose it.

##       (3) The Anomalies are too consistent.

If inattention is the reason that a significant fraction of people choose (B) over (A), you'd expect that there would also be a large fraction of people would make the rational choice -- i.e. would choose (A) over (B) -- because the noise can go in either direction. However in this case I think that the majority of people will make the anomalous choice, and I think the same is true with many other anomalies: in each of the famous anomalies -- Allais, Elssberg, etc., -- we all immediately recognize the intuition that draws us towards the anomalous choice.

This is not a direct contradiction of a theory of inattention. You can be rationally inattentive and have a consistent bias: e.g. for some $x$, $E[x|s]>x$ for all realizations of $s$ with $f(s|x)>0$. However if you have a consistent bias for one value of $x$ then you must have a stochastic bias for other values of $x$, and I'm skeptical whether those other biases will be found in the data.

#           Against Unorthodox Preferences

There are a few reasons to doubt that the classic choice anomalies are due to deeply-held but unorthodox preferences:

1. Allais-style choices violate dynamic consistency.
2. Choices over gambles are highly sensitive to framing effects, e.g. anchoring, preference reversal.
3. The anomalies observed in choice behavior also appear in pure *judgment* problems. E.g. Oprea (2023) "Simplicity Equivalents" finds that the typical anomalies found in choice over gambles also appear when those choices are transposed into choices over deterministic outcomes. Subjects are given a series of choices that look like this:

   - A: 100 boxes containing $7 each
   - B: 10 boxes containing $25 each, and 90 boxes containing $0 each.

   Oprea finds that subjects exhibit choice patterns that are very similar under each of two instructions:

   1. As gambles: "you will be paid the value of one of the boxes from the set you selected, randomly chosen by the computer."
   2. As deterministic: "you will be paid the value of all of the boxes from the set you selected, added up and divided by 100."

#           Conclusion

If it's not inattention and not unorthodox preferences that explains anomalies then what is it? Here's my explanation in a nutshell -- more detail is given in my paper ["Hierarchical Processing "](https://www.dropbox.com/s/guf8u1r1z5qoc6g/paper_heuristics.pdf?dl=1).

1. When we see a choice set we correctly perceive the outcomes (for sufficiently simple choices).
2. However we get strong *instincts* about which alternative to choose, which can be interpreted as noisy signals about our preferences.
3. It turns out that those instincts are menu-dependent, and so they lead to intransitive choices, meaning our our choices cannot be represented as maximizing a consistent utility function.

This is broadly consistent with the tradition of "contingent weighting" menu-dependent theories of choice. I discuss some models of contingent weighting in [relative thinking](https://tecunningham.github.io/posts/2016-04-30-relative-thinking.html), arguing that the nature of contingent weighting is probably quite *context dependent*.


<!-- # Against Unorthodox Preferences

* Whack-a-mole: solve one puzzle, create others.
* Because by-and-large people don't directly violate axioms, only indirectly. -->


<!-- # Conclusion

Why have these subfields survived for so long? Aren't the objections to pretty obvious? I guess they just held their breath — it started with one or two papers trying out a new approach, somehow ignoring or suspending the obvious objections, made it past that intial stage — and now no-one talks about the obvious objections anymore, they only talk about subtle refinements: whether this paper is an inprovement on a prior one, not noticing that both papers are based on a silly premise. And once a subfield gets a couple of publications there are a set of professors who’ll volunteer to referee each others’ papers, professors who will shepherd fresh graduate students into their dead end street. -->