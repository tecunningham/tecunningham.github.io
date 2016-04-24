---
layout: post
title: A Note on Reinforcement Learning
---

* For a long time I'd been confused about the status of reinforcement learning theory -- the theory that says someone will perform an act more often if they previously received a reward when they did it. It was a massively popular theory in the first half of the 20th century, but these days psychologists seem to treat it as defunct, an ex-theory. Yet it's still being used: people who train animals still talk a lot about conditioning; neuroscientists are crazy about reinforcement learning, and it's used a lot in applied artificial intelligence.

* From having read a lot of this stuff my basic understanding is now this: The generalizations about how animals and humans learn are valid only in specific domains, they aren't deep laws of behaviour. The reason the theory is often a good model of decision-making is because it's a good model of the *environment* in which decision-makers typically work. (I.e., the theory doesn't tell us much about how the brain works, it tells us about the environment which the brain was designed for).


* Formally, suppose we have stimulus s, action a, and reward r.

   We might find that, at every point, probability of each action is just the relative reward in previous training:

   P(a|s)= \sum{r_i*1{s_i=s}*1{a_i=a}} / \sum{r_i*1{s_i=s}}

        $a(s) = \arg \max_{a\inA} E[u(a,\theta)|s] $


![alt text][krazykat]

==============================================================================

### CLASSIC EXAMPLES OF REINFORCEMENT LEARNING

 * In 1905 Thorndike proposed a basic principle of animal learning: "Of several responses ... those which are accompanied or closely followed by satisfaction ... will be more likely to recur." The same basic idea was later described as "instrumental conditioning," "operant conditioning", or "reinforcement learning."

 * Rats and pigeons in boxes will pretty quickly learn to tap a button, when tapping the button is followed by receiving a food pellet. They can also learn much more complex functions: e.g., learning to tap on the left button when they see a square, and on the right button when they see a circle.

 * In the 1950s there were some classic studies in which human behaviour was manipulated through conditioning. For example in Greenspoon (1955) a subject would be asked to say aloud a sequence of words, whichever came to mind, and the experimenter would randomly give subtle positive cues when he heard certain types of word - for example plural nouns. Gradually subjects would start saying plural nouns more often, without being aware of this.

 * Lots of animal training, I believe, still uses principles of conditioning: you give the animal a small reward whenever it does something you want it to, and you can gradually build up more complicated behaviours. They also use other concepts from conditioning like secondary reinforcers and intermittent reinforcement.

 * In 1992 IBM built a backgammon-playing neural net that used a kind of reinforcement learning: each action (a move) was reinforced depending on whether the outcome was better or worse than expected. The ultimate reinforcement was from winning the game, and expectations propagated back from that, to learn the value of positions in the middle of the game. The program was a great success -- it could beat most human players.

 * [dopamine]


### ADDITIONAL LAWS

 * There are some interesting additional laws that were discovered about conditioning.

 * BLOCKING: The order in which associations are learned is important. Suppose a pigeon learns to press a lever whenever she hears a beep. Subsequently, the beep is always accompanied by a flash. When the flash appears by itself, the pigeon won't have learned to peck. But if the beep and flash were paired right from the beginning, then both the beep or flash would, by themselves, be sufficient for the pigeon to peck. So learning one association can "block" another association from being learned.

 * INTERMITTENT REINFORCEMENT: Intermittent reinforcement was found to create stronger associations than unvarying reinforcement. When reinforcement for an act is no longer given, then the animal will remain performing the act for a longer time if, during the original training period, their acts were only intermittently reinforced.

 * MATCHING: If you give a pigeon two different levers, each of which will release a pellet with a fixed probability, then the bird will learn to peck preferentially on the lever with the higher probability. But it will still occasionally peck on the lever with the lower probability, roughly in proportion to the difference in probabilities (if the pigeon was maximizing expected value then it should peck just at the high-value lever).

 * SECONDARY REINFORCEMENT:
 * OVERTRAINING & EXTINCTION:
 * SUPERSTITION:

At the height of the enthusiasm for conditioning many people thought these laws gave insight into all aspects of human behaviour - mental illness, adolescent delinquency, sexual behaviour, language.
[clockwork orange].

==============================================================================
(4) DIFFICULT CASES

 * In the first few decades of reinforcement learning many confirmations of the basic theory were published. But, as seems common in academic enquiry, as time went on the evidence came to seem much messier. Many of the "laws" of reinforcement learning turn out to apply only in a subset of situations, and they reverse in other situations.

 * REVERSE REINFORCEMENT: An old finding, regarding rats running mazes, is that when the rat finds a piece of cheese down one passage, then they were *less* likely to go down that passage the next time they were in the maze. According to reinforcement learning they should be more likely to go down that passage.

 * CONTEXT-SPECIFICITY: The speed of learning associations between stimuli and responses is very different depending on the stimulus and the response. Some associations can be learned firmly with just a single experience, for example a rat refusing to eat red pellets after getting nauseous after eating a red pellet. Others associations take far longer, a rat learning to associate a sound with getting nauseous.

 * AWARENESS: In humans, despite many attempts, very few cases have been found in which reinforcement can affect behaviour without people being consciously aware of it. Some of the classic findings have been reconsidered: in the study which manipulated peoples' choice of words, it was found that the effect only occurred among subjects who were consciously aware of the association. Additionally, many learned responses can be turned on or off by simply telling the person.

 If all reinforcement goes through the conscious brain, then it is much less interesting: people are simply choosing to do things which get them rewards.



==============================================================================
(5) PUTTING IT BACK TOGETHER

 * As I said, the laws of reinforcement learning turn out to apply only in a subset of situations.

 * One interpretation is that learning is irreducibly complex. However the agreements and deviations from reinforcement-learning often fit a predictable pattern: the theory works in contexts where past associations are a good guide to future associations; and it fails in contexts where that's not true.

 * Consider the rat who is *less* likely to run down a passage, when they were previously rewarded for running down that passage. This makes sense if the rat remembers that he just ate the food down that passage, and so wants to look elsewhere. The rat expects the future payoff of an action to be *negatively* correlated with the past payoff.

 * The basic law of reinforcement learning can be recast in terms of beliefs: if you expect the future payoff of an action to be positively correlated with its past payoff, then it is rational to perform whichever act was rewarded in a similar situation in the past.

 * The other laws of reinforcement can also be recast in terms of beliefs. And the situations in which those laws are violated are often exactly the situations where such beliefs would not apply.

 * BLOCKING:

 * INTERMITTENT REINFORCEMENT: If an act was only occasionally reinforced, this means that on previous occassions when rewards stopped they resumed again later. So it's not surprising that, having experienced rewards stop and resume once before, when they stop again you expect them to resume again.

 * CONTEXT SPECIFICITY:

 * MATCHING: "

==============================================================================
(6) TAKEAWAY

* sadf


 (a) Why is it useful to dog trainers? Tell us some big things about the conditions in which dogs evolved: .

 (b) Connection to some other psychological laws: lateral inhibition; case-based decision-making: they work until they don't.

 (c) Retrospect: in the 1950s people didn't give the human brain much credit. Manipulation by reinforcement; Freudian associations; hidden persuaders; brainwashing.











==============================================================================
==============================================================================
==============================================================================
NOTES:
==============================================================================
Some interesting things about Skinner: (1) corporal punishment in California schools; (2) he prototyped a pigeon-guided rocket in WWII: the pigeon would sit in the nose, looking out a window, and would peck to the left or the right, to guide the rocket towards its target; (3) "beyond freedom and dignity"; (4) science is the new art.

==============================================================================
==============================================================================

* Paradigmatic cases
 * pigeons in a skinner box - pecking at buttons
 * TD-backgammon

* Some history:
 1900: Pavlov
 1905: Thorndike's law of effect ""
 1950s: Skinner
 1966: Chomsky's review of a Skinner book shows how the theory has become vacuous
 1970s: falls apart
 1990s: dopamine in the midbrain

==============================================================================
Barto & Sutton:
1- multi arm bandit - exploration exploitation - selection rather than just being given information, supervised or unsupervised - active not passive - track avg payoff , update if diff from expectations
2- associative - depends on cues
3- temporal difference - secondary reinforcer - track difference - - mdp and bellman dynamic optimization makes policy fn relatively simple
 - when you win game, reinforce all sequence of actions, or instead just-prior state.


About law of effect: "Although sometimes controversial (e.g., see Kimble, 1961, 1967; Mazur, 1994) the Law of Effect is widely regarded as an obvious basic principle underlying much behavior (e.g., Hilgard and Bower, 1975; Dennett, 1978; Campbell, 1958; Cziko, 1995)."

Dennett:
 https://dl.tufts.edu/bookreader/tufts:ddennett-1975.00001#page/1/mode/2up

Departures - where it's actually not optimal
 - (Where td learning not optimal: learn a whole sequence of actions in one shot ; backgammon w fewer steps, can learn variation)
 - over learning and extinction: devalue secondary reinforcer - rationalize if you expect time-series structure

 * If you just drop rewards randomly into life, what changes?
 * Category learning as the same thing


[krazykat]: http://comicsalliance.com/files/2015/08/herriman-03.jpg "Krazy Kat"

