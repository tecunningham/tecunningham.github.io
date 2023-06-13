---
title: On Unconscious Influences (Part 1)
layout: post
output: pdf_document
date: 2017-12-08
header-includes:
    - \usepackage[color,matrix,arrow,curve]{xy}
    - \usepackage{color}
    - \usepackage{graphicx}
    - \usepackage{amsmath}
    - \newcommand{\rsucc}[1]{\rotatebox[origin=c]{#1}{$\succ$}}
    - \newcommand{\rsucceq}[1]{\rotatebox[origin=c]{#1}{$\succeq$}}
    - \newcommand{\rsuccsim}[1]{\rotatebox[origin=c]{#1}{$\succsim$}}
---

<!--
things that remain to do:

- [ ] improve discussion of Freud, & examples of his diagnoses
- [ ] replace guide-god example which gets the right predictions / explain how guide-dog examples leads to inconsistent choices
- [ ] discussion of why guide-dog model implies getting hypotheticals  / wrong.
- [ ] add results of experiment demonstrating unconscious knowledge
- [ ] discuss the *introspection* case for unconscious influences.
-->

# Introduction

Over a couple of years I spent a lot of time in offices looking out the window, thinking about decision-making & the unconscious, scribbling little bits & pieces in a notebook.

![NBER](https://www.dropbox.com/s/be1p2urgqwri2hp/nber_snow.png?raw=1)

I ended up writing two papers - "[Hierarchical Aggregation of Information and Decision-Making](https://dl.dropboxusercontent.com/u/13046545/paper_heuristics.pdf)" by myself and "[Implicit Preferences Inferred from Choice](http://bit.ly/paper_implicit)" with Jon de Quidt. The papers are fairly technical, and this post is going to be a layperson's guide to the background, what's known about unconscious knowledge, and a tiny bit about the ideas in those papers.

Here is the argument in a nutshell:

1. There are plenty of reasons to think that unconscious influences are strong -- in other words, that people have limited insight into what factors influence their decisions.
2. The idea of unconscious influences has been in and out of the mainstream of psychology for the last 200 years, but always hounded by arguments over what it means, i.e. over what evidence would be sufficient to show that a decision was influenced by an unconscious factor. The battle has had many reversals: a new types of evidence has been proposed which is thought to reveal unconscious influences, and then later the technique or interpretation is shown to have substantial flaws and the line of inquiry fizzles out. A couple of decades pass and a different approach becomes popular.
3. Two broad classes of evidence are the following: (A) people reveal their unconscious preoccupations in their involuntary responses -- in how their pupils dilate, how quickly they respond to a stimulus, in their word associations, dreams, slips of the tongue; (B) people reveal unconscious influences in discrepancies between how they act and how they explain their behaviour. Both sources of evidence have got tangled in debates about interpretation, and there are substantial camps on either side with not much agreement on what constitutes sufficient evidence for unconscious influences.
4. A third type of evidence is less common but, I think, more powerful: evidence from inconsistencies in decision-making. The idea being that unconscious factors are by their nature *isolated* from conscious factors, i.e. they don't interact with conscious beliefs and desires, and this isolation will cause certain characteristic inconsistencies among decisions.
5. This can be made precise with an analogy: the relationship between the conscious and unconscious brain is like the relationship between a blind man and his guide dog. The blind man makes decisions based, in part, on which direction the guide dog is pulling towards, so the guide dog's beliefs and desires influence the man's decisions, but without the man knowing exactly what those beliefs and desires are, and so he couldn't tell you how much any particular factor contributed to his decision. Testing for unconscious influences in behaviour is just testing the degree to which your brain is being led by a guide dog.
6. The internal-consistency definition of unconscious influences implies two ways of looking for them: (1) testing whether people can accurately answer *hypothetical* questions about decisions they would make if factors changed - i.e. navigating without your guide dog; and (2) testing whether people make consistent judgments when judging two outcomes at a time.
7. First, hypothetical questions. We can ask people, how would your judgment change if this factor changed? Would you still like this painting if the name of the artist was different? Would this drawing look more like your cousin if the nostrils were bigger? Unconscious influences imply that people will not be able to give accurate answers to these hypothetical questions because if the description of the situation is abstract then their unconscious brain won't be able to evaluate it (AKA, they don't know which direction they would go in without knowing what their guide dog will say).
8. The second way of testing for unconscious influences is what my paper with Jon is about: unconscious influences particularly leave their mark in *comparisons*, where you evaluate two outcomes simultaneously or consecutively, or when you choose between two outcomes. When confronted with two outcomes you surface two unconscious judgments and that gives you some insight into what is affecting those judgments, which in turn will affect your conscious decision.
9. Suppose you had an unconscious preference for men over women, but a conscious preference to be indifferent, this will manifest in the following: (A) when you see two CVs which are identical, except that one is a man and one is a woman, then you're indifferent between them; (B) when you see two CVs which differ in some other respect (e.g. one has a PhD, the other has an MBA), then you consistently have a preference for the CV belonging to the man. Your guide dog has a bias towards men, which you're not aware of: the bias will only sway your decision in the second case because, in the second case, when your guide dog pulls you towards the man with a PhD, you cannot figure out how much of that pull is due to his being a man, and how much is due to his PhD.
10. In the end I think that our brains *are* full of guide dogs all pulling in different directions. If we had the stomach for it we could plot out our decisions all on a map -- measure how each factor influences our judgment -- and we would be able to see both the surface influences and the deeper latent influences.


## Contents

1. Motivating examples
2. Some definitions & theory
3. Ways of measuring implicit preferences
4. The proposal

![Littauer](https://www.dropbox.com/s/lt96t4u3qoh7ywp/harvard_office.png?raw=1)


# Motivating Examples


To help with being clear on what I'm talking about here are some examples of unconscious influences. I'll try to return to these at the end.

1. People judging a presidential candidate's actions differently depending on whether it's a man or a woman; judging an ethical lapse differently depending on whether committed by a Democrat or Republican; judging a study differently depending on whether it supports their own theory. In each case not being aware of that influence.

2. The little things that a family does to spite each other: someone says that Thursday doesn't suit them, in part because they know that Thursday suits you best (perhaps consciously, perhaps unconsciously).

3. Freudian conjectures about trauma causing later responses: e.g. Freud thought Anna O's aversion to water was because of a memory of seeing a dog drinking from a glass of water. More generally, Freud's early seduction theory, that psychosomatic illness is caused by repressed memories of childhood sexual abuse.

4. Your preferences changing with the circumstances: saying yes to a friend, a hairdresser, bartender, waiter, or salesperson, because it seemed like a good idea at the time, and later not understanding why you didn't say no.

5. Knowledge used in your judgments, but not consciously accessible: knowledge of grammar implicit in your judgements of whether a sentence sounds right; knowledge of the physical world implicit in your judgements of distance and velocity of the things you see; knowledge of faces implicit in recognizing your cousins.

My examples include both unconscious knowledge and unconscious desires. I'm not going to talk about unconscious *sensations* -- e.g. flashes of advertisement that don't register consciously but might persuade you.

![tel aviv](https://www.dropbox.com/s/bczy68n3k08s6yl/tel_aviv_office.png?raw=1)

#  Ways of Measuring Unconscious Influences

Here are three ways of identifying whether an influence is conscious:

1. **Involuntary responses.** In the dilation of your pupils, in your response times, in slips of the tongue, what you see in Rorsach blots, in your word associations, in your dreams.
2. **Ability to describe the influence.** Ask people what they think influences their decisions, and compare that to what actually influences their decisions.
3. **Integration with other influences.** Finally we can say that a factor is unconscious if its influence seems to be partitioned off from other influences. The most simple example is if a factor continues to influence you even in cases where you have reason to ignore it.

## Involuntary responses

Freud is the most famous theorist of extracting unconscious factors from involuntary responses -- he wrote three books on different methods: one on dreams, one on jokes, one on mistakes (mis-reading, mis-hearing, mis-speaking). An example from the last book: "A woman who is very anxious to get children always reads 'storks' instead of 'stocks'." Most of Freud's examples of unconscious influences are much more complex than this one, and more often the hidden factor influencing behaviour is something unpleasant or shameful.

Another way of measuring unconscious cognition is through measuring arousal. Most famous is the "Iowa card task" from Bechara et al. (1996). They had their subjects choose among playing cards, and receive rewards if they chose certain cards. They found that people gradually learned which types of cards were rewarded, but they also found that the subjects' automatic responses (measured by skin conductance, i.e. sweating) would show an awareness of the pattern more quickly than the subjects' choices would: after a while, when the subject's hand hovered over one of the cards which was rewarded, the subject would sweat a little more, even though the subject wasn't any more likely to choose that card. They said that this showed that unconscious learning was outpacing conscious learning. Antonio Damasio, one of the authors of this study, went on to write *Descartes' Error* which accused Descartes' of starting the great misapprehension that emotions and reason are in competition -- Damasio said that his experiments show how emotions inform reason and improve decision-making. A lot of subsequent papers tried to show that snap decisions, which avoid conscious processing, can produce better outcomes than slow considered decisions.

Even more famous is the "Implicit Association Test" (IAT) (Greenwald, McGhee and Schwartz (1998)). Subjects are told to press a button whenever they see something from either of two different categories of stimuli, e.g. press the button if you see either a black face or a word with a positive association. Their finding, much-replicated, was that people are relatively quicker at tasks (meaning they have shorter response times) when they are asked to identify a set such as "black face or negative word" or "white face or positive word" than to identify a set like "black face or positive word" or "white face or negative word." They find that this occurs even among people who report no conscious negative feelings towards black people, and they interpret this as revealing an unconscious association between black people and negative feelings, and they argue that this association could affect your decision-making without you being aware of it.

Many other measures of automatic responses have been popular at different times: hypnosis and word association (Freud used both of these before moving to talking therapy); Rorsach blots (AKA inkblot tests); thematic apperception test (interpret an ambiguous drawing, still widely used); lie detectors AKA polygraphs (they measure autonomic responses - blood pressure, pulse, respiration, and skin conductivity - as you are asked different questions).

Unfortunately a great deal of this research turns out to be both hard to replicate, and reliant on strong assumptions in order to interpret as surfacing unconscious associations. Newell and Shanks (2014) give strong arguments for both of these points, covering many of the methods I mentioned here.

It is worth mentioning that, although Freud's more elaborate theories died off, his idea that psychosomatic illness is an indirect expression of a psychological stress, especially about something shameful, I believe remains one of the standard theories of modern neurology (O'Sullivan, 2015).

<!-- Freud's complex theories of unconscious structure, and his elaborate ways of interpreting dreams and actions, are not believed by many today. Nevertheless O'Sullivan (2015) says that Freud's basic theories of psychosomatic illness -- as an indirect expression of some psychological stress, especially something shameful -- remain the basic theory of neurologists today. -->

However even if we had solid evidence for unconscious influences on involuntary responses, this still stops short of unconscious influences on decision-making. It's possible that our associations show up in sweating, response time, and dreams, but have little effect on decision-making, and if that's so then unconscious associations are not terribly important for social science. Most of the authors in this literature have assumed that the unconscious factors they identify affect real decisions but have left that extrapolation untested. Blanton et al. (2009) say that there's no persuasive evidence that implicit racial bias, as measured by the IAT, predicts peoples' decision-making, once you control for measures of *explicit* racial bias, i.e. when you just ask people how they feel about black people. (Singal (2016) has a long discussion on this point).


## Ability to Describe the Influence

A second type of evidence is to compare self-reported influences on behaviour with actual influences on behaviour. Here are some examples:

1. In the mid 20th-century behaviourists found that they could shape their subjects choices through conditioning with rewards and punishments, and the subjects seemed to remain ignorant of this shaping. For example if you say *'mm-hmm'* whenever someone uses a plural noun, then after a while that person ends up using plural nouns more often, apparently unaware of the influence (Thorndike and Rock (1934); Greenspoon (1955)).
2. Since the 1970s social psychologists have published all sorts of experiments in which they vary an apparently irrelevant factor and find that this can affect peoples' decision-making. Nisbett and Wilson (1977) summarize a lot of experiments and say "subjects are sometimes (a) unaware of the existence of a stimulus that importantly influenced a response, (b) unaware of the existence of the response, and (c) unaware that the stimulus has affected the response."
3. Another paradigm from the 1970s asks people to make a judgement - e.g. which stock to pick - and also to rate the importance of factors which contributed to their decision. Slovic et al. (1972) find a low correlation (0.34) between the ratings that a stockbrokers put on factors, and the actual influence of these factors on their decisions. There is a small literature with similar findings across a variety of tasks.
4. Finally, since the 1970s a smaller group of psychologists have been running experiments in which people learn a complicated pattern, and then are asked about their insight into it. E.g. in Arthur Reber's "artificial grammar" experiments subjects learn, through trial and error, to discriminate between two categories of words. After some time they become very good at the task, but when asked to explain how they are making decisions they often say they don't know, or they come up with rules that do not match their actual performance.

As in the previous category, a lot of this evidence is very fragile: either hard to replicate, or based on delicate interpretations of what is happening in the experiment. Newell and Shanks (2014) again give a good summary.

An additional problem is that these findings could reflect knowledge being difficult to articulate, without it being unconscious. And this literature is full of reversals which bear this out: when experiments are repeated it has often turned out that the subjects *do* report awareness of the pattern that they have learned if they are asked the question in a different way. Mitchell et al. (2009) say "[i]t is very difficult to provide a satisfactory demonstration of unaware conditioning simply by showing conditioning in the absence of awareness. This is because it is very difficult to be sure that the awareness measure and the conditioning measure are equally sensitive."

<!-- Some more examples of describing influences: the "sugar factory" game; sequence learning; Mitchell on evaluative conditioning (p191); Perruchet's air puffs. -->

<!-- One final note about this method for detecting unconscious influences: you could say that the bulk of late 20th century literary and cultural theory is, broadly speaking, looking for traces of unconscious factors in decision-making: finding signs of the hegemony, the patriarchy, orientalism, colonialism, in the apparently trivial details of texts. -->

![IIES](https://www.dropbox.com/s/d5s41vykojhy4cv/iies.jpg?raw=1)

##                Isolation of Unconscious Influences

Finally there's a third type of evidence which is more strictly behavioural: an unconscious factor is one which is *isolated* from your other conscious beliefs and desires -- i.e. it does not interact with conscious factors -- and that isolation will be reflected in your behaviour. This isolation criterion has been given various names, but I don't think it's ever been explained as clearly as it could be.

<!-- [new dog example] -->
To be precise think of the blind man (the conscious part of the brain) and the guide dog (the unconscious). The guide dog can know something -- e.g. she knows when the crossing light is flashing -- which the man does not know, and her knowledge will influence the man's decisions through her recommendation of when to cross. However the guide dog's knowledge is isolated from the man's knowledge: it only influences his decisions through the narrow channel of pulling on the leash. Suppose you tell the man that the crossing lights are not working properly, and so whatever color they show is entirely at random and uninformative. The man and dog, considered as a system, has two pieces of information: (1) the light is green (i.e. indicating ready to cross); and (2) the color is uninformative. However the two pieces of information are known by different actors, implying that they will not be integrated, because neither the man or dog knows both. This will be reflected in the man's behaviour: he will be influenced by the guide-dog's recommendation, because the dog sees other things in addition to the crossing-light, such as oncoming traffic. And so the man's behaviour will still be influenced by the color of the light, even though he *knows* that the color is irrelevant.

If information is separated in the brain, we ought to see characteristic patterns of that in behavior. I know of just a few cases where the isolation of knowledge has come up clearly in trying to define or measure unconscious influences.

<!-- [Explain that this will produce inconsistencies in decision-making.] -->

Stich (1978) said that certain mental states are "inferentially unintegrated": <!--He was writing about knowledge of grammatical rules: although native speakers of a language agree about whether particular sentences are grammatical or not, for most people it's extraordinarily difficult to write down this knowledge as a set of rules. Linguists spend entire careers trying to improve on grammars of a language that they already know. He says that one of the distinctive features of this type of knowledge is that it's not "inferentially integrated." -->

> "[unconscious beliefs are] largely inferentially isolated from the large body of inferentially integrated beliefs to which a subject has access"

He gives an example: suppose Noam Chomsky has a theory of grammar, and that there exists some grammatical rule which is a counterexample to that theory. If a linguist knows that rule consciously, then the linguist will immediately infer that Chomsky's theory is false. But if the linguist only knows the rule *unconsciously*, then they won't be able to make that inference, because the knowledge is "inferentially unintegrated" -- i.e. the knowledge is isolated from the knowledge regarding Chomsky's theory. [^quine]

[^quine]: Quine says you shouldn't call this type of thing unconscious knowledge -- your linguistic practice may *obey* some rule, but you can't say that you unconsciously *know* that rule, because there are infinitely many different rules that would imply that pattern of behavior. But this skeptical objection is too tough: Quine would deny that a cow can have a belief about where a water trough is, & instead admit only that the cow's behavior is consistent with a particular belief among infinitely many others.

A separate place where this separation has come up is in the work of Zenon Pylyshyn and Jerry Fodor since the 1980s regarding perception being "cognitively impenetrable," or "informationally encapsulated." They mean that perceptual processes often make inferences without taking into account all the information that is available, i.e. by drawing only on a subset of information. Their principal argument was from perceptual illusions: they argue that illusions can typically be understood as rational inferences from a subset of the information available. Helmholtz had a nice example: if you close one eye and press with your finger on the edge of your eyelid then you'll perceive a point of light, but the light will be coming from the *opposite* side of your field of vision from where your finger is. This is because the left side of your retina receives light from the right side of your visual field and vice versa. So when your retina receives some stimulation on the left-hand side your brain makes infers that light is coming from the right-hand side. This is a sensible inference given only the information that your eye has, i.e. just the information from the retina. In this case there is additional information - the fact your finger is pressing on your eyelid - which should give a different interpretation to the stimulation, but your visual cortex is not wired up to incorporate that information, and so it misinterpret the signals it receives.

The Helmholtz-Fodor-Pylyshyn model of encapsulated inference isn't quite the same as the case of the blind man and the guide dog. In their examples the pre-conscious process have a strict *subset* of the information available to the conscious brain. In other words the man isn't blind, it's just a case where the dog leads in a different direction than the man would. Fodor (1983) does have a brief discussion on whether early perceptual processes have access to information not available to the conscious brain, which would imply unconscious influences, in my sense.

Finally the isolation argument has appeared in the literature on human "associative learning," in testing whether or not the associations that we learn through conditioning are conscious. A typical experiment involves ringing a bell and then giving subjects a small electric shock. After a while people learn to flinch when they hear the bell. For a long time psychologists tried to map out the logic of how such associations would form, trying to figure out the rule which governed learning of associations. However in the last few decades an argument has been made that these learned associations are not in fact mechanical - there is no simple rule - instead they are more-or-less optimal responses to the environment based on the entirety of the information available, i.e. they are not *isolated* from other knowledge, though the argument isn't usually put in terms of conscious vs unconscious knowledge. For example Colgan (1970) told subjects, after they learned an association, that the association is no longer valid ("from now on the bell will not signal an electric shock") and he found that, although this didn't entirely extinguish the flinching, it did cause it to markedly decrease. This implies the flinching is not isolated from your conscious knowledge: the association, at least to some degree, interacts with more abstract knowledge. There are many other circumstances where rule-based theories of association-learning have foundered because it turns out that peoples' responses respond to outside considerations. De Houwer, Vandorpe and Beckers (2005) summarize the evidence against associative models (which can be interpreted as models with unconscious knowledge):

> The two types of models can be differentiated ... by manipulating variables that influence the likelihood that people will reason in a certain manner but that should have no impact on the operation of the associative model. We have seen that such variables (e.g., instructions, secondary tasks, ceiling effects, nature of the cues and outcomes) do indeed have a huge effect. Given these results, it is justified to entertain the belief that participants are using controlled processes such as reasoning and to look for new ways to model and understand these processes.

Mitchell says:

> “The results consistently show evidence for skin conductance [effects] only in participants who are aware of the [relationship] ... [a]lthough there are many papers arguing for unaware conditioning, close inspection reveals, in almost all cases, that the measure of conditioning was most likely more sensitive than that of awareness.”

In retrospect a lot of behavior that was studied in the lab, which was thought to be telling us about the wiring of the animals, actually was telling us about the world outside the animal, because it has turned out that the animals' response is the *optimal* response to the typical circumstances it faces in the world. (See my other post [The Repeated Failure of Laws of Behaviour](http://tecunningham.github.io/2017/04/15/the-mechanical-and-the-rational/) , and also Mitchell et al. (2009) section 4.3)

If this line of thought were entirely correct -- if all information was integrated and fed into every decision -- then there would be no unconscious influences in my sense. However I do think that there's plenty of evidence that remains for a lack of integratation between cognitive processes.

In Part 2 of this essay I will give a more formal statement of how decisions can reveal unconscious knowledge (and unconscious motivations), and a survey what I think is the strength of the evidence.

<!-- in a sense this is similar to the previous section: it's about your ability to describe influences. -->

![Caltech](https://www.dropbox.com/s/hvaaahkc9eshz6z/office_caltech.jpg?raw=1)

# Summary So Far

1. Looking at involuntary reactions tells us *something* about your reaction to a situation, but it doesn't tell us whether it has important impact on your decision-making. (And in addition, the evidence for influences on involuntary reactions is pretty weak).
2.  Comparing peoples' decisions to what they say about their decisions is also imperfect evidence for unconscious associations, because people can be inarticulate about their reasons, without being unconscious of them. (And in addition, this evidence is also pretty weak).
3. Finally, internal coherence of decision-making seems a much more solid way of identifying unconscious influences.

# In Part II

Discussion of the type of evidence needed to establish unconscious knowledge.

# References

**Bechara, Tranel, Damasio and Damasio (1996) “Failure to respond autonomically to anticipated future outcomes following damage to prefrontal cortex"**

**Hart Blanton, James Jaccard, Jonathan Klick, Barbara Mellers, Gregory Mitchell, and Philip E Tetlock (2009). “Strong claims and weak evidence: reassessing the predictive validity of the IAT”. Journal of Applied Psychology, 94(3): 567.**

**Greenwald McGhee & Schwartz (1998) “Measuring individual differences in implicit cognition: The Implicit Association Test.”**

**De Houwer, Vandorpe and Beckers (2005) On the role of controlled cognitive processes in human associative learning**
>  "In hindsight, it seems obvious that people can learn about associations by using controlled processes such as reasoning and hypothesis testing. Why then, are associative models still dominant in modern research? One reason is that the associationistic view has a long tradition in psychology (and philosophy). It is thus difficult for many people to leave behind the associationistic view that has guided their thinking and research for many years. Another important reason is that associative models do quite well in accounting for the available empirical data. The well known Rescorla-Wagner model (Rescorla & Wagner, 1972), for instance, is compatible with a huge number of findings while being relatively simple. If our argument is correct that associative models do not provide an accurate account of the processes that underlie associative learning, how is it possible that they are able to account for so much of the data? We agree with Lovibond (2003, p. 105) that "the success of these models is due to them capturing, at least in part, the operating characteristics of the inferential learning system". What this means is that associative models (as well as probabilistic models for that matter) can be seen as (mathematical) formalisations of certain deductive reasoning processes. A system that operates on the basis of associative models does not reason, but acts very much as if it is reasoning. The associative models will thus often predict the same result as a model that is based on the assumption that humans actually generate and test hypothesis or reason in a controlled, conscious manner. The two types of models can be differentiated, however, by manipulating variables that influence the likelihood that people will reason in a certain manner but that should have no impact on the operation of the associative model. We have seen that such variables (e.g., instructions, secondary tasks, ceiling effects, nature of the cues and outcomes) do indeed have a huge effect. Given these results, it is justified to entertain the belief that participants are using controlled processes such as reasoning and to look for new ways to model and understand these processes."

**Newell & Shanks (2014, BBS) “Unconscious Influences on Decision-Making: A Critical Review”**

+ "There is little convincing evidence of unconscious influences on decision making in the areas we review” -- they say many of Nisbett and Wilson's results on lack of introspection have been reinterpreted
+ (1) multiple-cue judgment : classic paradigm is that you compare weights revealed by decisions to self-reported weights. They say that protocol for getting self-reported weights are usually shitty, & better measurements show that people understand their own judgment better
+ (2) decisions are better when you don't deliberate (all the evidence for this is shitty)
+ (3) awareness / Iowa gambling task (your subconscious is attracted to the best deck, but conscious is not): very shitty evidence
+ (4) priming: people often can report what primes were presented, if you try harder- they say that there is strong evidence for top-down influence even in perceptual tasks. [I emailed them suggesting the joint/separate randomization task, they said it sounds nice]
+ They say that dispute over definitions is over: “A surprising outcome of the review is that debates and disagreements about the meaning of the terms consciousness and awareness have (with a few exceptions) played a remarkably minor role in recent research. Whereas issues about how to define and measure awareness were once highly prominent and controversial (e.g., Campion et al. 1983; Reingold & Merikle 1988), it now seems to be generally accepted that awareness should be operationally defined as reportable knowledge, and that such knowledge can only be evaluated by careful and thorough probing.”

**Michael Polanyi (1966) "The Tacit Dimension"**

**Nisbett & Wilson (1977) “Telling More than we can know”**

* A very influential paper (7000 citations) arguing that unconscious influences are rampant: “Subjects are sometimes (a) unaware of the existence of a stimulus that importantly influenced a response, (b) unaware of the existence of the response, and (c) unaware that the stimulus has affected the response.” However a lot of the experimental literature in this field is now under a cloud -- either through being hard to replicate, or being based on arguable interpretations.

**Quine (1972) “Methodological reflections on current linguistic theory”**

* When Quine wrote this, linguists were talking a lot about how people had unconscious knowledge of grammatical rules. Quine said that you can't say that someone knows a rule, from observing that their behaviour conforms to that rule, because there will always be infinitely many different rules which the behaviour satisfies. So this is Quine pouring some cold water on unconscious knowledge. However, in response, I say that we can still define unconscious knowledge underneath behaviour as the inability to accurately answer hypotheticals. So we don't need to specify *which* rule the person is using, but it's clear that they do not have conscious access to any rule which generates their observed behaviour.

**Stich (1976) "Beliefs & Subdoxastic States"**

**Suzanne O'Sullivan (2015) "It's All in Your Head: Stories from the Frontline of Psychosomatic Illness"**

> p191: "For all the shortcomings in the concepts proposed by Freud and Breuer in *Studies*, the twenty-first century has brought no great advances to a better understanding of the mechanism for this disorder. The terms dissociation and conversion are still widely in use ... the general principles of modern dissociation are not very different to those of Victorian times ... in day-to-day practice Janet's and Freud's theories are regularly used, or misused."

**Singal (2016) in New York Magazine** - article on Implicit Association Test.