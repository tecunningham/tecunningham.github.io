---
layout: post
title: The Repeated Failure of Laws of Behaviour
date: 2017-04-15
---

![krazy kat](https://www.dropbox.com/s/g5zrkpncc4mff29/krazy.jpg?raw=1)

# Nutshell

1. In retrospect a lot of behaviour that was studied in the lab, which we thought was telling us about the wiring of animals, actually was telling us about the world outside the animal..

2. It has turned out, over and over again, that an animal's response to a stimulus reflects the animal's *beliefs* about what that stimulus represents in the world. So the "laws" of behaviour that we discovered are actually just describing, at a remove, regularities in the world.

    | "law" of behaviour                                                                                                                | truth about the environment                                                                                                                       |
    |-----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
    | Animals will tend to repeat whichever action is rewarded                                                                          | Actions which have been rewarded in the past tend to be rewarded in the future                                                                    |
    | Objects appear darker to people when neighboring objects are brighter                                                             | Objects *are* darker when neighboring objects are brighter                                                                                        |
    | Blue objects appear more distant to people                                                                                        | Blue objects *are* more distant                                                                                                                   |
    | People brake when the rate of change of the angle of an approaching object ($\frac{\dot{\theta}}{\theta}$) exceeds some threshold | $$\frac{\dot{\theta}}{\theta}$$ determines the time to impact of an approaching object in typical circumstances, and so the optimal time to brake |
    | Consumers' expenditure increases less than proportionally with changes in income                                                  | Changes in income are typically temporary, and so imply a less-than-proportional response to maintain stable long-run expenditure                 |

3. Here's the point expressed formally. Some scientist observes response $r$ and stimulus $s$, and proposes a law of behaviour, a simple function from $s$ to $r$. But for any such law, $r(s)$ there exists at least one rationalization, under which the organism has beliefs about an unobserved variable $x$, and they choose $r$ optimally given what they infer about $x$ from observing $s$, i.e.,

    $$r(s) = \arg \max_{r} \int u(s,r,x) f(x|s)$$

   Given some pattern of behaviour $r(s)$, we can back out the beliefs that would justify that behaviour, $f(x\|s)$, and we've seen -- many times repeated -- that those beliefs turn out to be *accurate* -- as in the cases above, even when the scientist wasn't aware of that truth.

1. You could reply that, sure, it's optimal in the typical situation, but animals keep applying the same behaviours in cases where it's not optimal, and that's why they are laws of behaviour. There are some cases like that, but it seems to me that there are many more cases which go in the other direction: when the situation is changed, the behaviour changes, and it turns out the animal does what's optimal, not what the law implies.


2. The biggest example of the failure of behavioural laws is the theory of **conditioning and associative learning**. Psychologists started with proposing a simple function that governs behaviour -- the more often you are rewarded for doing something, the more often you do it -- but then were forced to add a long list of qualifications and special cases (context-dependence, blocking, intermittent reinforcement, extinction, matching). It gradually became clear that the complications were not arbitrary, but made sense from the animal's point of view: they are sensible strategies based on what an animal should expect in a typical environment. So the complex rules that we had been mapping out were not telling us about the animal's wiring, they were instead telling us about the world that the animal lives in. Animals tend to repeat actions that are rewarded (i.e. obey the laws of reinforcement learning) only when they have reason to believe that rewards will be positively correlated across time. When they are in a situation where they don't expect that correlation, then they no longer obey the rules of reinforcement learning. Mitchell et al. (2009) cite a lot of evidence about human associative learning and say:

    > "we reconsider (and reject) one of the oldest and most deeply entrenched dual-system theories in the behavioral sciences, namely the traditional view of associative learning as an unconscious, automatic process that is divorced from higher-order cognition."

    Their rejection is based on evidence that, when people learn associations, they only follow them insofar as those associations are good guides to achieving their goals.

3. There's a very similar case in **perception**, where psychologists have been trying to learn the function from sensation to perception. A famous observation was of lateral inhibition: a stimulus seems less bright when the neighbouring stimulus gets brighter. In the 1950s this was thought to be due to wiring of neurons in the eye, but gradually it became clear that the effect only occurs in certain cases, and in other cases the opposite effect is observed. And then people realized that the cases in which it works are exactly the cases where it would be a reasonable inference in a typical environment. Adelson (1993, *Science*):

    > “All of the phenomena discussed above lead to the same conclusion: Brightness judgments cannot be simply explained with low-level mechanisms. Geometrical changes that should be inconsequential for low-level mechanisms can cause dramatic changes in the brightness report. It is as if the visual system automatically estimates the reflectances of surfaces in the world[.]"

4. A similar thing has happened in the study of **control laws**, or invariants, simple principles which map stimulus to response. For example Lee's (1976) tau-dot model of braking: you brake when $\dot{\tau}$ is above some threshold, where $\tau=\frac{\theta}{\dot{\theta}}$, and $\theta$ is the angle of an approaching object. Many people spent a lot of time proposing control laws for different domains, and testing control laws against each other, but the field (I believe) has now mostly given up the hope of finding simple laws to model behaviour. Weber and Fajen (2014) say:

    > “numerous studies have demonstrated that observers often rely on non-invariants and that the particular optical variables upon which they rely to guide action can change—as a consequence of practice, as a function of the range of conditions that are encountered, and as a function of the dynamics of the controlled system.”

5. Slightly more of a stretch - there are some similar episodes in the study of **economic decision-making**. In the 1950s economists had established various laws about how expenditure related to a person's income. Milton Friedman, in 1957, showed that many properties and puzzles of the expenditure function could be understood as byproducts of a person rationally planning to spread their income over time. Likewise Lucas (1976) argued that, in three different cases, where a statistical regularity in decisions was observed, you could explain *why* they occur if you model people as making tradeoffs given sensible beliefs about their economic prospects.

6. I'm not trying to argue that all behaviour is rational and that the brain optimally combines all available information. But looking at the track record of psychologists they have systematically underestimated the brain -- they keep proposing simple behavioural rules -- response as a function of stimulus -- which later turn out to be only true insofar as they reflect some deeper organizing principle.

7. I think the same is true for a lot of **behavioural biases.** Economists sometimes treat "loss aversion", "probability weighting", etc., as if they are hard-wired, and scratch their heads when an experiment finds behaviour going in the opposite direction. But almost certainly these regularities are just local manifestations of some deeper - as yet unknown - principles. (An earlier [post](/2016/04/30/relative-thinking/) makes this point about "relative thinking" effects).

8. The rest of this note gives some more detail about how this pattern played out in the history of reinforcement learning.

![Krazy Kat](https://www.dropbox.com/s/u3pqkseoxfqvh1k/herriman-03.jpg?raw=1)

# Reinforcement Learning

For a long time I'd been confused about the status of reinforcement learning theory -- the theory was massively popular in the first half of the 20th century, but these days psychologists seem to treat it as defunct, an ex-theory. And yet it's still being used: people who train animals still talk a lot about conditioning, neuroscientists are crazy about reinforcement learning, as are people who work in artificial intelligence.

From having read a lot of this stuff my basic understanding is now this: The generalizations about how animals and humans learn are valid only in specific contexts, they are *not* deep and fundamental laws of behaviour, as had been once believed. However the theory remains a very useful simple model of decision-making because it's a good model of the *environment* in which decision-makers typically work. I.e., the theory doesn't tell us much about how the brain works, it tells us mostly about the environment which the brain was designed for.

<!--
* Formally, suppose we have stimulus s, action a, and reward r.

   We might find that, at every point, probability of each action is just the relative reward in previous training:

   $$P(a|s)= \sum{r_i1\{s_i=s\}1\{a_i=a\}} / \sum{r_i1\{s_i=s\}}$$

   $$a(s) = \arg \max_{a\in A} E[u(a,\theta)|s]$$
-->

# Classic Examples of Reinforcement Learning

In 1905 Thorndike proposed a basic principle of animal learning: "Of several responses ... those which are accompanied or closely followed by satisfaction ... will be more likely to recur." The same basic idea was later described as "instrumental conditioning," "operant conditioning", or "reinforcement learning." The term 'behaviorism' referred to a school of psychology, popular in the middle of the 20th century, based on this principle or variants.

Rats and pigeons in boxes will pretty quickly learn to tap a button, when tapping the button is followed by receiving a food pellet. They can also learn much more complex functions through reinforcement, like learning to tap on the left button when they see a square, and on the right button when they see a circle. (B F Skinner worked on using pigeons to guide missiles, by training them to tap on pictures of military targets.)

In the 1950s there were some influential studies in which human behaviour was manipulated through conditioning. In Greenspoon (1955) a subject would be asked to say aloud a sequence of words, whichever came to mind, and the experimenter would give subtle positive cues when he heard certain types of word - for example plural nouns. Gradually subjects would start saying plural nouns more often, without being aware of this. The implication drawn was that many of our everyday decisions, which we think of as conscious and deliberate, are actually just imprints of previous patterns of reinforcement.

I believe that lots of animal training still uses principles of conditioning: you give the animal a small reward whenever it does something you want it to, and you gradually build up more complicated behaviours. They also use other concepts from conditioning like secondary reinforcers and intermittent reinforcement.

In 1992 IBM built a backgammon-playing neural net that used a kind of reinforcement learning -- in short the computer would be more likely to make the same move again if it had a good outcome in previous cases. The ultimate reinforcement was from winning the game, and expectations propagated back from that, to learn the value of positions in the middle of the game. The program was a great success -- it was trained against itself, and quickly became good enough to beat most human players.

In the 1990s there was a lot of excitement when some neuroscientists discovered that levels of dopamine in the mid-brain responded to rewards in a way consistent with a reinforcement-learning model. In particular, dopamine didn't correlate with the level of reward, but correlated with the level of *unexpected* reward: i.e., if you receive a reward in a situation where you wouldn't normally. This is the kind of calculation which an algorithm would do if it was implementing reinforcement learning: it would update weights when a rewards is different from the expected level of reward.


# Additional Laws

 There are some interesting additional laws that were discovered about conditioning.

**blocking.** The order in which associations are learned is important. Suppose a pigeon learns to press a lever whenever she hears a beep. Subsequently, the beep is always accompanied by a flash. When the flash appears by itself, the pigeon won't have learned to peck. But if the beep and flash were paired right from the beginning, then both the beep or flash would, by themselves, be sufficient for the pigeon to peck. So learning one association can "block" another association from being learned. ("Reverse blocking" is sometimes, but not always, also observed: the pigeon learns to associate A and B with a reward, but then when she finds that B predicts the reward by itself, she subsequently ignores A.).

**intermittent reinforcement.** Intermittent reinforcement is often found to create more robust associations than unvarying reinforcement. If you give a pigeon a pellet every time she pecks the button, then when you stop giving her pellets she'll stop pecking the button. If you only give her a pellet occasionally, then the behaviour will take much longer to die out.

**matching.** If you give a pigeon two different levers, each of which will release a pellet with a fixed probability, then the bird will learn to peck preferentially on the lever with the higher probability. However it will still occasionally peck on the lever with the lower probability, roughly in proportion to the ratio of probabilities. This seems to be a violation of rationality because if the pigeon had learned the probabilities, and was maximizing expected value, then it should peck constantly at the high-value lever.

(also: secondary reinforcement; overtraining & extinction; superstition.)

At the height of the enthusiasm for conditioning many people thought these laws gave insight into all aspects of human behaviour - mental illness, adolescent delinquency, sexual behaviour, language.


# Difficult Cases

In the first few decades of reinforcement learning many confirmations of the basic theory were published but, as often happens, the published evidence became less coherent as time went on. Many of the laws of reinforcement learning turn out to apply only in a subset of situations, or the parameters varied widely, and in other situations the effects seem to reverse.

**reverse reinforcement.** An old finding, regarding rats running mazes, is that when the rat finds a piece of cheese down one passage, then they were *less* likely to go down that passage the next time they were in the maze. According to reinforcement learning they should be more likely to go down that passage.

**context specificity.** The speed of learning associations between stimuli and responses is very different depending on the stimulus and the response. Some associations can be learned firmly with just a single experience, for example a rat refusing to eat red pellets after getting nauseous after eating a red pellet. Others associations take far longer, e.g. a rat learning to associate a sound with getting nauseous.

**awareness.** In humans, despite many attempts, very few cases have been found in which reinforcement can affect behaviour without people being consciously aware of it. Some of the classic findings have been reconsidered: in the study which manipulated peoples' choice of words, it was found that the effect only occurred among subjects who were consciously aware of the association. Additionally, many learned responses can be turned on or off by simply telling the person. Colgan (1970) told subjects, after they learned an association, that the association is no longer valid ("from now on the bell will not signal an electric shock") and he found that, although this didn't entirely extinguish the flinching, it was much less pronounced after the instruction.


# Putting it Back Together

As I said, the laws of reinforcement learning turn out to apply only in a subset of situations.

One interpretation is that there do exist laws of learning, but that they are more complex. However the agreements and deviations from reinforcement-learning are not at random: in many cases they can be understood: the theory works in just those contexts where past associations tend to be a good guide to future associations; and it fails in contexts where that's not true. E.g., a rat knows that the taste of food is a good predictor of whether it'll make you sick, but doesn't have reason to believe that the sound you hear when you eat food is a very good predictor.

Consider the rat who is less likely to run down a passage when they were previously rewarded for running down that passage. This makes sense if the rat remembers that he just ate the food down that passage, and so wants to look elsewhere. In this situation the rat expects the future payoff of an action to be *negatively* correlated with the past payoff, rather than positively correlated, and so we get the opposite effect than that predictedb by reinforcement learning.

The basic law of reinforcement learning can be recast in terms of beliefs: if you expect the future payoff of an action to be positively correlated with its past payoff, then it is rational to perform whichever act was rewarded in a similar situation in the past.

The other laws of reinforcement can also be recast in terms of beliefs. And the situations in which those laws are violated are often exactly the situations where such beliefs would not apply.

**intermittent reinforcement.** Suppose an act was only occasionally reinforced. This means that on previous occasions when rewards stopped they resumed again later. So it's not surprising that, having experienced rewards stop and resume once before, when they stop again you expect them to resume again.

**matching.** There's an obvious argument that probability matching is rational -- in your usual environment the probability of reward changes over time, so it makes sense to continue monitoring each action, to see if the payoff has changed (see Estes, 1976).

**blocking.** Blocking can be explained by a learning model, given a prior that *either* A or B is predictive of the reward, but not both. (See “Explaining away in Weight Space” by Dayan and Kakade, and good summary at http://www.cs.cmu.edu/~ggordon/conditioning-slides.pdf ).

Sometimes we observe that forward blocking occurs but not backward blocking. This can be explained by a mechnical prediction model (a Kalman filter), where you update weights only when unexpected things happen. So, you learn that A & B are both associated with reward, then you are exposed to cases with just A and reward. Can this model be rationalized? It's not clear to me. (AKA, what priors would justify a Kalman filter, given that it depends on the order of presentation?)

Mitchell (2009) also notes that there is *less* blocking when you introduce cognitive load, implying that it's not an automatic or mechanical effect (subjects “showed blocking of skin conductance CRs only when blocking was a valid inference.”)


**transfer learning.** There are some examples where organisms can transfer patterns they have learned across quite different stimuli, e.g. learning patterns of complementarity/substitutability (Mitchell (2009) p190). This would require an elaborate reinforcement learning model to rationalize, but is simple with a rational model.

**context specificity.** De Houwer, Vandorpe and Beckers (2005) say (in "Why have associative models fared so well?")^[Also Seligman (1970) *On the Generality of Laws of Learning*, "That all events are equally associable and obey common laws is a central assumption of general process learning theory ... A review of data from the traditional learning paradigms shows that the assumption of equivalent associability is false ... it is speculated that the laws of learning themselves may vary with the preparedness of the organism for the associa- tion and that different physiological and cognitive mechanisms may covary with the dimension."]

> The two types of models can be differentiated ... by manipulating variables that influence the likelihood that people will reason in a certain manner but that should have no impact on the operation of the associative model. We have seen that such variables (e.g., instructions, secondary tasks, ceiling effects, nature of the cues and outcomes) do indeed have a huge effect. Given these results, it is justified to entertain the belief that participants are using controlled processes such as reasoning and to look for new ways to model and understand these processes.


# Conclusion

I guess there are two natural followup questions to this argument:

**(1) If you looked in the history of psychology, could you find as many examples of making the opposite mistake?**

In other words, how often have we have over-estimated the rationality of human behaviour. Yeah, maybe you're right. It's not hard to find economists who will insist that, whatever people do, it's in their best interest. I just think that psychologists tend to make the other mistake.

**(2) If you're so down on it, then why is reinforcement learning useful to dog trainers and to computer programmers?**


# Misc Notes

<!--
**Barto & Sutton chapter on the history of reinforcement learning.**
  1. multi arm bandit - exploration exploitation - selection rather than just being given information, supervised or unsupervised - active not passive - track avg payoff , update if diff from expectations
  2. associative - depends on cues
  3. temporal difference - secondary reinforcer - track difference - - mdp and bellman dynamic optimization makes policy fn relatively simple
  4. when you win game, reinforce all sequence of actions, or instead just-prior state.
-->

---

**economic applications of association-based decision-making.** Gilboa & Schmeidler: case-based decision-making; Camerer: experience-weighted attraction learning. The NYU guy has a paper. Erev & Roth (1998) say that reinforcement learning does a good job predicting behaviour in some games, better than equilibrium play. I wouldn't defend completely rational behaviour, but on the other hand I wouldn't expect RL behaviour to be *stable*: probably behaviour approximates RL in some contexts, and does the opposite in others. It's not obvious that the RL model is a very good level of abstraction to describe behaviour at. Charness & Levin (2005) run an experiment where reinforcement & Bayesian updating give different predictions:  you choose between urns, one more sensitive to state, one less sensitive. If you draw from the less-sensitive urn, and you receive a positive outcome, then you update about the state, and the Bayesian prediction is that you should switch urns, while reinforcement learning says you'll stay with the same urn. They find that people largely stay with the same urn.

---

**the gambler’s fallacy goes in the opposite direction to reinforcement learning.** The gambler's fallacy: winning a gamble at time $t$ makes you *decrease* the expectation of winning at $t+1$, i.e. the *opposite* prediction of a simple reinforcement model. However there's a heuristic rationalization similar to the rationalization of rats in a maze: caveman Ug is shaking trees to get coconuts out. If there’s no coconut at time t, then there's an increased probability of a coconut at t+1.

**Poggio and visual perception.** In 1983 Poggio found that he could reinterpret prior findings in perception as implementation of Bayesian inference:

   > “All problems in vision and more general perception were inverse problems, going back from the image to 3-D properties of objects and scenes. They were also, as typical for inverse problems, ill-posed. We used regularization techniques to “solve” specific vision problems such as edge detection and motion computation. In the process, we found that some of the existing algorithms for shape-from-shading, optical flow, and surface interpolation were a form of regularization. Our main contribution was to recognize illposedness as the main characteristic of vision problems and regularization as the set of techniques to be used for solving them.”


**Shephard's theory of generalization.** Shepard (1987) and Tenenbaum and Griffiths (2001) give a persuasive argument that apparent laws governing generalization between stimuli are context-dependent, in a way that is consistent with Bayesian inference.