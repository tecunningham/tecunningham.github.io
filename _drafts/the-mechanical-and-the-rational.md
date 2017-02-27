---
layout: post
title: The Mechnical & The Rational <br> (the failure of hard-wired rules in psychology)
---

# Nutshell

1. In retrospect a lot of behaviour that was studied in the lab, which we thought was telling us about the wiring of animals, actually was telling us about the world outside the animal, because it turned out that the animals' response is the *optimal* response to the typical circumstances it faces in the world.

2. The biggest case of this is **reinforcement learning**. Psychologists spent decades trying to map out the function between stimulus and response. They started with a simple function but kept adding qualifications and special cases (context-dependence, blocking, intermittent reinforcement, extinction, matching). It gradually became clear that the complications were not at random, but rather made sense from the animal's point of view: they are the product of rational Bayesian inference, based on the regularities in the animal's typical environment. So the complex rules that we had been mapping out were not telling us about the animal's wiring, they were telling us about the world that the animal lives in. Animals tend to repeat actions that are rewarded (i.e. obey the laws of reinforcement learning) only when they have reason to believe that rewards are positively correlated across time. When they are in a situation where they don't expect that correlation, then they no longer obey the rules of reinforcement learning -- i.e. it is not a hard-wired behaviour. Mitchell et al. (2009):

    > "we reconsider (and reject) one of the oldest and most deeply entrenched dual-system theories in the behavioral sciences, namely the traditional view of associative learning as an unconscious, automatic process that is divorced from higher-order cognition."

3. There's a very similar case in perception, where psychologists have been trying to learn the function from sensation to perception. A famous observation was of **lateral inhibition**: a stimulus seems less bright when the neighbouring stimulus gets brighter. In the 1950s this was thought to be due to wiring of neurons in the eye, but gradually it became clear that it only occurs in certain circumstances, and in other cases it reverses. And then people realized that the cases in which it works are exactly the cases where it would be a reasonable influence in a typical environment. Adelson (1993, *Science*):
 
    > “All of the phenomena discussed above lead to the same conclusion: Brightness judgments cannot be simply explained with low-level mechanisms. Geometrical changes that should be inconsequential for low-level mechanisms can cause dramatic changes in the brightness report. It is as if the visual system automatically estimates the reflectances of surfaces in the world, and the resulting lightness percepts inevitably sway the judgment of brightness.”

4. A similar thing has happened in the study of **control laws**, principles which map stimulus to response, for example Lee's (1976) tau-dot model of braking (you brake when $\dot{\tau}$ is above some threshold, where $\tau=\frac{\theta}{\dot{\theta}}$, and $\theta$ is the angle of an approaching object). Many people spent a lot of time proposing control laws for different domains, and testing control laws against each other, but the field (I believe) has now mostly given up the hope of finding simple laws that gives a good representation of behaviour. Weber and Fajen (2014) say 

    > “numerous studies have demonstrated that observers often rely on non-invariants and that the particular optical variables upon which they rely to guide action can change—as a consequence of practice, as a function of the range of conditions that are encountered, and as a function of the dynamics of the controlled system.” 

5. There are some similar episodes in the study of **economic decision-making**. In the 1950s economists had established various laws about how a person's expenditure related to their income. Milton Friedman, in 1957, showed that many properties and puzzles of the expenditure function could be understood as byproducts of a person rationally planning to spread their income over time. In the same spirit Lucas (1976) argued that, in three different cases, where a statistical regularity in decisions was observed, you could explain *why* they occur if you model people as rational decision-makers (additionally, once you model them that way, the policy implications are quite different).

6. I'm not trying to argue that all behaviour is rational, and every piece of the brain shares information with every other piece. However looking at the history of psychology it seems clear that we have a tendency to jump to conclusions: we try to fit simple laws to observed behaviour, and then we are surprised when it turns out that those laws turn out not to be hard-wired, and are only local manifestations of some deeper principle, which often is a principle that is well adapted to the typical environment that the organism faces.

7. I think the same is true for a lot of **behavioural biases.** Economists sometimes treat "loss aversion", "probability weighting", etc., as if these are hard-wired rules, and scratch their heads when an experiment finds behaviour going in the opposite direction. But almost certainly these regularities are just local manifestations of some deeper - as yet unknown - principles. (I have a note that makes this point about relative thinking effects - [Relative Thinking](/2016/04/30/relative-thinking/)).

7. The rest of this note is just examples from the history of reinforcement learning. Probably not as interesting for the overall point.

![Krazy Kat](https://dl.dropboxusercontent.com/u/13046545/herriman-03.jpg)

# Reinforcement Learning

For a long time I'd been confused about the status of reinforcement learning theory -- the theory that behavior is largely driven by whether they were rewarded by doing the act previously (also sometimes called 'behaviorism'). This theory was massively popular in the first half of the 20th century, but these days psychologists seem to treat it as defunct, an ex-theory. Yet it's still being used: people who train animals still talk a lot about conditioning, neuroscientists are crazy about reinforcement learning, and so are people who work in artificial intelligence.

From having read a lot of this stuff my basic understanding is now this: The generalizations about how animals and humans learn are valid only in specific domains, they are *not* deep and fundamental laws of behaviour, as had been once believed. The reason the theory is often a good model of decision-making is because it's a good model of the *environment* in which decision-makers typically work. I.e., the theory doesn't tell us much about how the brain works, it tells us mostly about the environment which the brain was designed for.

<!--
* Formally, suppose we have stimulus s, action a, and reward r.

   We might find that, at every point, probability of each action is just the relative reward in previous training:

   $$P(a|s)= \sum{r_i1\{s_i=s\}1\{a_i=a\}} / \sum{r_i1\{s_i=s\}}$$

   $$a(s) = \arg \max_{a\in A} E[u(a,\theta)|s]$$
-->

# Classic Examples of Reinforcement Learning

In 1905 Thorndike proposed a basic principle of animal learning: "Of several responses ... those which are accompanied or closely followed by satisfaction ... will be more likely to recur." The same basic idea was later described as "instrumental conditioning," "operant conditioning", or "reinforcement learning." The term 'behaviorism' referred to a school of psychology, popular in the middle of the 20th century, based on this principle or variants.

Rats and pigeons in boxes will pretty quickly learn to tap a button, when tapping the button is followed by receiving a food pellet. They can also learn much more complex functions through reinforcement, like learning to tap on the left button when they see a square, and on the right button when they see a circle. (B F Skinner trained pigeons to tap on pictures of military targets, & he planned to put the pigeons in the nose of missiles, looking out a little window, guiding the missile through their taps.)

In the 1950s there were some classic studies in which human behaviour was manipulated through conditioning. In Greenspoon (1955) a subject would be asked to say aloud a sequence of words, whichever came to mind, and the experimenter would give subtle positive cues when he heard certain types of word - for example plural nouns. Gradually subjects would start saying plural nouns more often, without being aware of this. The lesson drawn from studies like this was that many of our everyday decisions, which we think of as conscious and deliberate, are actually just imprints of previous patterns of reinforcement.

I believe that lots of animal training still uses principles of conditioning: you give the animal a small reward whenever it does something you want it to, and you gradually build up more complicated behaviours. They also use other concepts from conditioning like secondary reinforcers and intermittent reinforcement.

In 1992 IBM built a backgammon-playing neural net that used a kind of reinforcement learning: each action (a move) was reinforced depending on whether the outcome was better or worse than expected. The ultimate reinforcement was from winning the game, and expectations propagated back from that, to learn the value of positions in the middle of the game. The program was a great success -- it was trained against itself, and quickly became good enough to beat most human players.

In the 1990s there was great excitement when some neuroscientists discovered that levels of dopamine in the mid-brain responded to rewards in a way consistent with a reinforcement-learning model. In particular, dopamine didn't correlate with the level of reward, but correlated with the level of *unexpected* reward: i.e., if you receive a reward in a situation where you wouldn't normally. This is the kind of calculation which an algorithm would do if it was implementing reinforcement learning: it would update weights when a rewards is different from the expected level of reward.


# Additional Laws

 There are some interesting additional laws that were discovered about conditioning.

**blocking.** The order in which associations are learned is important. Suppose a pigeon learns to press a lever whenever she hears a beep. Subsequently, the beep is always accompanied by a flash. When the flash appears by itself, the pigeon won't have learned to peck. But if the beep and flash were paired right from the beginning, then both the beep or flash would, by themselves, be sufficient for the pigeon to peck. So learning one association can "block" another association from being learned. ("Reverse blocking" is sometimes, but not always, also observed: the pigeon learns to associate A and B with a reward, but then when she finds that B predicts the reward by itself, she subsequently ignores A.).

**intermittent reinforcement.** Intermittent reinforcement is often found to create more robust associations than unvarying reinforcement. When reinforcement for an act is no longer given, then the animal will remain performing the act for a longer time if, during the original training period, their acts were only intermittently reinforced.

**matching.** If you give a pigeon two different levers, each of which will release a pellet with a fixed probability, then the bird will learn to peck preferentially on the lever with the higher probability. However it will still occasionally peck on the lever with the lower probability, roughly in proportion to the difference in probabilities. This seems to be a violation of rationality because if the pigeon had learned the probabilities, and was maximizing expected value, then it should peck just at the high-value lever.

**Also:** secondary reinforcement; overtraining & extinction; superstition.

At the height of the enthusiasm for conditioning many people thought these laws gave insight into all aspects of human behaviour - mental illness, adolescent delinquency, sexual behaviour, language.


# Difficult Cases

In the first few decades of reinforcement learning many confirmations of the basic theory were published but, as often happens in academic disciplines, the published evidence became less coherent as time went on. Many of the laws of reinforcement learning turn out to apply only in a subset of situations, and in other situations the effects seem to reverse.

**reverse reinforcement.** An old finding, regarding rats running mazes, is that when the rat finds a piece of cheese down one passage, then they were *less* likely to go down that passage the next time they were in the maze. According to reinforcement learning they should be more likely to go down that passage.

**context specificity.** The speed of learning associations between stimuli and responses is very different depending on the stimulus and the response. Some associations can be learned firmly with just a single experience, for example a rat refusing to eat red pellets after getting nauseous after eating a red pellet. Others associations take far longer, e.g. a rat learning to associate a sound with getting nauseous.

**awareness.** In humans, despite many attempts, very few cases have been found in which reinforcement can affect behaviour without people being consciously aware of it. Some of the classic findings have been reconsidered: in the study which manipulated peoples' choice of words, it was found that the effect only occurred among subjects who were consciously aware of the association. Additionally, many learned responses can be turned on or off by simply telling the person. Colgan (1970) told subjects, after they learned an association, that the association is no longer valid ("from now on the bell will not signal an electric shock") and he found that, although this didn't entirely extinguish the flinching, it did cause it to markedly decrease.


# Putting it Back Together

As I said, the laws of reinforcement learning turn out to apply only in a subset of situations.

One interpretation is that there exist laws of learning, but they are very complex. However the agreements and deviations from reinforcement-learning are not at random: in many cases they can be understood: the theory works in contexts where past associations are a good guide to future associations; and it fails in contexts where that's not true.

Consider the rat who is *less* likely to run down a passage, when they were previously rewarded for running down that passage. This makes sense if the rat remembers that he just ate the food down that passage, and so wants to look elsewhere. In this situation the rat expects the future payoff of an action to be *negatively* correlated with the past payoff.

The basic law of reinforcement learning can be recast in terms of beliefs: if you expect the future payoff of an action to be positively correlated with its past payoff, then it is rational to perform whichever act was rewarded in a similar situation in the past.

The other laws of reinforcement can also be recast in terms of beliefs. And the situations in which those laws are violated are often exactly the situations where such beliefs would not apply.

**intermittent reinforcement.** Suppose an act was only occasionally reinforced. This means that on previous occasions when rewards stopped they resumed again later. So it's not surprising that, having experienced rewards stop and resume once before, when they stop again you expect them to resume again.

**blocking.** Blocking can be explained by a learning model, given a prior that *either* A or B is predictive of the reward, but not both. (See “Explaining away in Weight Space” by Dayan and Kakade, and good summary at http://www.cs.cmu.edu/~ggordon/conditioning-slides.pdf ). 

Sometimes we observe that forward blocking occurs but not backward blocking. This can be explained by a mechnical prediction model (a Kalman filter), where you update weights only when unexpected things happen. So, you learn that A & B are both associated with reward, then you are exposed to cases with just A and reward. Can this model be rationalized? It's not clear to me. (AKA, what priors would justify a Kalman filter, given that it depends on the order of presentation?)

Mitchell (2009) also notes that there is *less* blocking when you introduce cognitive load, implying that it's not an automatic or mechanical effect. “... showed blocking of skin conductance CRs only when blocking was a valid inference.”

**transfer learning.** There are some examples where organisms can transfer patterns they have learned across quite different stimuli, e.g. learning patterns of complementarity/substitutability (Mitchell (2009) p190). This would require an elaborate reinforcement learning model to rationalize.

**context specificity.** De Houwer, Vandorpe and Beckers (2005) say (in "Why have associative models fared so well?")

> The two types of models can be differentiated ... by manipulating variables that influence the likelihood that people will reason in a certain manner but that should have no impact on the operation of the associative model. We have seen that such variables (e.g., instructions, secondary tasks, ceiling effects, nature of the cues and outcomes) do indeed have a huge effect. Given these results, it is justified to entertain the belief that participants are using controlled processes such as reasoning and to look for new ways to model and understand these processes. 



# Misc Notes 


**Q: If you're so down on it, then why is reinforcement learning useful to dog trainers and to computer programmers?**

<!--
**Barto & Sutton chapter on the history of reinforcement learning.**
  1. multi arm bandit - exploration exploitation - selection rather than just being given information, supervised or unsupervised - active not passive - track avg payoff , update if diff from expectations
  2. associative - depends on cues
  3. temporal difference - secondary reinforcer - track difference - - mdp and bellman dynamic optimization makes policy fn relatively simple
  4. when you win game, reinforce all sequence of actions, or instead just-prior state.
-->

**economic applications of association-based decision-making.** Gilboa & Schmeidler: case-based decision-making; Camerer: experience-weighted attraction learning. The NYU guy has a paper. Erev & Roth (1998) say that reinforcement learning does a good job predicting behaviour in some games, better than equilibrium play. I wouldn't defend completely rational behaviour, but on the other hand I wouldn't expect RL behaviour to be *stable*: probably behaviour approximates RL in some contexts, and does the opposite in others. It's not obvious that the RL model is a very good level of abstraction to describe behaviour at. Charness & Levin (2005) run an experiment where reinforcement & Bayesian updating give different predictions:  you choose between urns, one more sensitive to state, one less sensitive. If you draw from the less-sensitive urn, and you receive a positive outcome, then you update about the state, and the Bayesian prediction is that you should switch urns, while reinforcement learning says you'll stay with the same urn. They find that people largely stay with the same urn.

**the gambler’s fallacy goes in the opposite direction to reinforcement learning.** The gambler's fallacy: winning at time t makes you *decrease* the expectation of winning at t+1, i.e. the opposite prediction of a simple reinforcement model. A heuristic rationalization: caveman Ug is shaking trees to get coconuts out. If there’s no coconut at time t, then there's an increased probability of a coconut at t+1.



