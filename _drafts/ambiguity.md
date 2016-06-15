---
layout: post
title: Ambiguity Aversion
---

Suppose you know that 1/3 of the balls in an urn are red, and the other 2/3 are some mixture of black and yellow:

$$(\$100,\text{red}) \succ (\$100,\text{black})$$

$$(\$100,\text{red or yellow}) \prec (\$100,\text{black or yellow})$$

Reduction objection (Raiffa 1961)

$$\binom{\text{heads:}(\$100,\text{red or yellow})}{\text{tails:}(\$100,\text{black})} vs \binom{\text{heads:}(\$100,\text{black or yellow})}{\text{tails:}(\$100,\text{red})}$$

From the typical Ellsberg choices, it seems like you'd prefer the RHS to the LHS. Yet both of the gambles above have identical probability of receiving the $100, conditional on whatever colour ball is chosen (if black: 50%).

Dynamic consistency objection: see http://www.econ.ohio-state.edu/jpeck/ozdenorenpeck.pdf

See discussion here:
https://www.facebook.com/tom.cunningham.374549/posts/10156983299730230?comment_id=10156983852265230&reply_comment_id=10156985759695230&comment_tracking=%7B%22tn%22%3A%22R%22%7D

==

Many writers have made a distinction between two types of uncertainty: risk and ambiguity. A common example is the difference between betting on whether a coin lands heads (a risky choice), or betting on whether a boxer would beat a wrestler in a fight (an ambiguous choice). Usually the distinction is defined as whether you know the probabilities (risk) or not (ambiguity), and a common observation is that people are unwilling to take ambiguous bets, for example intuitively I would be less willing to bet on either the boxer or the wrestler, than on the coin landing heads, even though I ought to be, at worst, indifferent. An enormous amount of theoretical work has tried to model this behaviour formally. It has been applied to real-world economic decision-making, such as investing, where probabilities are unknown.

However the risk-ambiguity distinction is conceptually strange because the orthodox scientific understanding probability is that it is a property of beliefs, not a property of the world. This implies that it is meaningless to say of an event that it has a probability, but you do not know what the probability is. 

In practice theories of ambiguity have other difficulties: theories which match the Ellsberg behaviour often predict bizarre behaviour in other circumstances, such as dynamic inconsistency (Weinstein & Al-Najjar, 2009). Raiffa (1961), in addition, points out that you could just flip a coin to determine whether to bet on the boxer or wrestler, and so convert the ambiguous bet into a bet with exactly the same structure as the coin flip.

An alternative explanation of ambiguity is the following: there are cases where it seems it makes a difference whether you feel something has 80% probability strongly or weakly. The distinction doesn't mean anything in the normal definition of probability, but it could map to your expectation about how much your belief is likely to change in the future as you receive more information. The case of the dice, and the case of the boxer-wrestler, are very different in this respect: my belief about dice is not sensitive to collecting more information (spending 30 minutes examining the dice is not likely to alter my beliefs); however my belief about the boxer-wrestler fight is sensitive to collecting more information - spending 30 minutes thinking, or googling, is likely to change my odds on the wrestler, though I don't know in advance whether they would go up or down.

Then why are we unwilling to take ambiguous bets? Because we are relying on the same instinct that restrains us from betting on three-card monte or on paper-scissors-rock: you worry that, when playing against an expert, whatever decision you make will be wrong. When you have a strong belief about a probability, as in the case with the coin, then you are happy bet on it; when you have a weak belief then you are generall unwilling because typically the other party is better informed than you. Even when they allow you to choose which side of the bet you wish to take (boxer or wrestler).

A prediction of this theory is that we would be willing to bet on events for which we do not know a 'true' probability, but they are informationally insensitive. For example, (???).

This concept is related to the Holmstrom-Tirole theory of liquidity: “informationally insensitive” assets are liquid, i.e. easily traded, because we do not expect that our counterpart in a trade will have more information than ourself, implying we are not concerned about asymmetric information. Holmstrom and Tirole say that the market for mortage backed securities was very liquid exactly because those assets were opaque. The opacity meant that the returns to effort (i.e., the expected variance in posteriors given research effort) was low. The moral hazard problem was therefore less severe, because you expected the other guy didn't put in much effort in sorting good securities from bad securities. When the securities started being downgraded then the returns to effort increase, as the value becomes closer to the kink on the bond payoff curve; thus the lemons problem appears, and the market loses its liquidity.


# Notes


* **Ellsberg on reactions to the paradox:** 1961: “Responses do vary. There are those who do not violate the axioms, or say they won’t, even in these situations (e.g., G. Debreu, R. Schlaifer, P. Samuelson); such subjects tend to apply the axioms rather than their intuition, and when in doubt, to apply some form of the Principle of Insufficient Reason. Some violate the axioms cheerfully, even with gusto (J. Marschak, N. Dalky); others sadly but persistently…. Still others (H. Raiffa) tend, intuitively, to violate the axioms but feel guilty about it and go back into further analysis.”

