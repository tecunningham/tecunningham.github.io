---
layout: post
title: The Time we Wasted on Ambiguity Aversion
---

TO DO
* Add example of event which we do not know a 'true' probability but which we believe to be informationally insensitive. -- say, .

# Argument

1. There are some predictions of the theory of expected utility which violate our intuitions.
2. People have proposed modifications of expected utility to accommodate the intuitions.
3. But every attempt has backfired: fixing one counter-intuitive prediction each time causes the theory to produce other *more* counter-intuitive predictions.
4. I think the deep conclusion is that our intuitions in the original cases are wrong, and the theory is right, and probably it's a shame that we spent so much time stubbornly trying to defend those intuitions.
5. Can reword this a little more carefully. We are putting together the intuitions, like a jigsaw puzzle, trying to see how they all fit together. But a fuller view of the situation tells us that there *is* no way to arrange them so they all fit together.
6. Still it's interesting to know why we have these intuitions.
7. In the case of ambiguity I think we can give a good answer: it's about whether the event is *information-sensitive*, i.e. is it something which we *could* easily learn more about, or it inscrutable, such that we couldn't learn much more about probabilities even if we tried. People tend to have a strong disinclination - for good reason - to make bets or exchanges when the other person knows more about the value of the good than ourselves. The typical examples of ambiguity-aversion conflate the information-sensitivity of an outcome and whether it has a known probability.

# Violations of Intuition

Here are a couple of intuitions which violate expected utility:

* Suppose I know there are 30 black balls in an jar, and another 60 which are either blue or gold. I would be much happier betting on getting a black ball, than betting on a blue ball, or betting on a gold ball.

* I would be much happier to bet on the outcome of a coin flip than to bet on the outcome of a fight between a boxer and a wrestler, even if, in the latter case, I can choose whether to bet on the boxer or the wrestler.

Both intuitions violate expected utility which says that I should be at least as happy with the latter types of bet, the ones without stated probabilities, because I can take the choice of two, one of which must have a higher probability of coming out true. Yet most people share this intuition that the second type of bet sounds less attractive.

And many modern textbooks on decision-making say that highlights the deep conceptual distinction between *risk* and *ambiguity*. With *risk* you know the probability of an outcome -- as in the coin flip, the black ball; with *ambiguity*, you don't -- as with the blue and gold balls, and the boxer-v-wrestler fight.

However the distinction between risk and ambiguity is conceptually strange because the "probability" of an event, under the orthodox definition of probability, is a property of your beliefs about that event, not a property of the event. And so it's strange to say that you don't know the probability of an event, as if there was such a thing as a probability which you could know. The probability of it being a full moon tonight, to me, is around 1/30. But to an astronomer who knows the moon's phases they either believe the probability to be 0%, or believe it to be 100%. There is no probability of that event independent of an observer.

Nevertheless a lot of otherwise smart and sincere people have spent chunks of their lives trying to modify expected utility in a way that can justify the intuitions above, commonly treating people as if they were ignorant about the "true" probability of an event, and then say that ignorance about probabilities influences their decisions.

However the theories proposed produce far worse violations of intuition than the violations that they were intended to solve.

* Raiffa (1961) points out that you can convert the ambiguous bet into a risky bet: e.g. you could say "I'll bet on the boxer if I flip heads, and on the wrestler if I flip tails." This strategy should give you an exactly 50% chance of winning. So if you can convert the bet with ambiguity, at worst, a bet which is equivalent to the bet with risk, then why would you prefer the bet with risk to the bet with ambiguity? (Unless those original intuitions were wrong, were mistakes.)
* Weinstein & Al-Najjar (2009) show that following your intuitions will lead to dynamic inconsistency. Suppose you have a jar with 30 black balls, plus 60 balls which are either blue or gold. Many people say they would prefer to bet on "a random ball with be either blue or gold" than to bet on "a random ball will be blue or black". Now suppose a ball is drawn, and you are told that it is *not* blue -- i.e., it's either black or gold. The bet becomes effectively a bet between the ball being black or it being gold, and most people have the intuition that they'd prefer to bet on it being black. But suppose you learn that the ball is drawn and it *is* blue, then you'd be indifferent between the bets because you'll win either way. So this is a paradox: if you learn the ball is blue, you're indifferent between them, if it's not blue, then you strictly prefer to switch -- so why didn't you switch in the first place, before you learned whether the ball was blue?
* Gelman (2013) shows that combining an uncertain and an ambiguous outcome produces paradoxical results. Suppose you think that the chance of a coin landing heads is 50% and that the chance of the boxer winning is ambiguous. Now suppose you learn that *either* the coin landed heads and the boxer won *or* the coin landed tails and the wrestler won. You ought to have the exactly same posterior belief about both the boxer winning and the coin landing heads (it would be odd if you didn't, since you know that one implies the other). But any statement of your posteriors seems to violate the spirit of a model of ambiguity: if you now believe that the boxer won with 50% probability this seems odd for the ambiguity to collapse to risk, because you didn't learn anything material to the fight. If you believe that the probability of the coin landing heads is now ambiguous then this is even odder -- uncertainty has suddenly ballooned into ambiguity, without you learning anything material about the coin.

# Why are we Nervous about Ambiguous Bets?

It seems that our original intuition was wrong: we *should* be willing to bet on things which don't have stated probabilities. So why do we have such strong intuitions against doing it?

Here's my suggestion: we have a strong disinclination to bet on things which are *informationally-sensitive*, and the typical examples of ambiguous bets are, besides being ambiguous, informationally sensitive.

Define informational sensitivity of a bet as the expected return to effort, measured in the expected change in beliefs. E.g., if I spend an hour investigating this topic, how much do I expect my posteriors to change? If I spend an hour examining a coin I'm unlikely to change my estimated probability of it landing heads when you throw it. If I spend an hour looking up information about boxing and wrestling, or talking to people, I'm quite likely to change my beliefs about who would win in a fight. I believe that this is the reason why we have different intuitions about the two cases.

So then why would we be unwilling to take ambiguous bets? Because we are relying on the same instinct that restrains us from betting on horses: you worry that, when playing against an expert, whatever decision you make will be wrong. When you have a strong belief about a probability, as in the case with the coin, then you are happy bet on it; but when you have a weak belief then you are generally unwilling because typically the other party is better informed than you.

So far so good, but you could say that this doesn't explain why you're wary of an informationally sensitive bet even when you are free to choose which side to take (either the boxer or the wrestler). Well the explanation says that you have an *intuition* against informationally sensitive bets, and intuitions tend to be leaky -- they fire even in cases where they are not strictly appropriate.

However there is an additional argument: in some cases, even when people have a choice of which side of a bet to take, they typically choose the wrong one, as in three-card monte or on paper-scissors-rock. In these cases it is *rational* - in a sense - to not want to take any of the bets on offer - because you have a belief - with evidence for that belief - that whichever arm you choose it's likely to be the wrong one, by the fact that you chose it.

A prediction of this theory is that we would be willing to bet on events for which we do not know a 'true' probability but which we still believe to be informationally insensitive. For example, **XXX***.

This concept is related to the Holmstrom-Tirole theory of liquidity: “informationally insensitive” assets are liquid, i.e. easily traded, because we do not expect that our counterparty in a trade will have more information than ourself, implying we are not concerned about asymmetric information. Holmstrom and Tirole say that the market for mortage backed securities was very liquid exactly because those assets were opaque. The opacity meant that the returns to effort (i.e., the expected change in posteriors given effort in researching their value) was low. The moral hazard problem was therefore less severe, because you expected the other guy didn't know much more than you about sorting good securities from bad securities. When the securities started being downgraded then the returns to effort increase as the value becomes closer to the kink on the bond payoff curve; thus the lemons problem appears, and the market suddenly lost its liquidity.


# Notes


* **Ellsberg on reactions to the paradox, 1961:** “Responses do vary. There are those who do not violate the axioms, or say they won’t, even in these situations (e.g., G. Debreu, R. Schlaifer, P. Samuelson); such subjects tend to apply the axioms rather than their intuition, and when in doubt, to apply some form of the Principle of Insufficient Reason. Some violate the axioms cheerfully, even with gusto (J. Marschak, N. Dalky); others sadly but persistently…. Still others (H. Raiffa) tend, intuitively, to violate the axioms but feel guilty about it and go back into further analysis.”

* **Gilboa's example.** There's a paper somewhere by Itzhak Gilboa, about ambiguity aversion, that describes a thought experiment which is meant to motivate ambiguity aversion. Something like this: you're looking for the lecture theatre and you see two doors, each with a sign in a foreign language. What probabilities do you assign to each being the lecture theatre? When I read it I could see that the example is bad: the intuition it evokes doesn't support ambiguity-aversion, and in fact there's another, better, explanation of what's going on. Seeing that Gilboa's motivating example for ambiguity is no good gives me confidence that ambiguity aversion, as a theory, is a not addressing a real need.
  &nbsp;
  But then I think of the motivating examples I have given in my own papers, and remember that they are often technically not quite right, I gloss over some detail. I had hoped that my readers are either too slow to spot the flaw, or too quick to be bothered by it because they see that the theory's good despite it being hard to give a really crisp example.

* **A nice example: phases of the moon.** Citlali asked me "but Daddy *why* is the moon in the sky in the daytime?" I said "I don't know, it's random." It's something which probably has unconditional probability of 50%, and yet, conditional on the recent history of the moon, we can predicted almost perfectly. In general the movements of heavenly bodies is changing, and often hard to predict, but there is a perfect way of predicting them.

* See also some argument on FB here:
https://www.facebook.com/tom.cunningham.374549/posts/10156983299730230?comment_id=10156983852265230&reply_comment_id=10156985759695230&comment_tracking=%7B%22tn%22%3A%22R%22%7D
