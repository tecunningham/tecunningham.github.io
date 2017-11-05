---
title: On Unconscious Influences (Part 2)
layout: post
output: pdf_document
header-includes:
    - \usepackage[color,matrix,arrow,curve]{xy}
    - \usepackage{color}
    - \usepackage{graphicx}
    - \usepackage{amsmath}
    - \newcommand{\rsucc}[1]{\rotatebox[origin=c]{#1}{$\succ$}}
    - \newcommand{\rsucceq}[1]{\rotatebox[origin=c]{#1}{$\succeq$}}
    - \newcommand{\rsuccsim}[1]{\rotatebox[origin=c]{#1}{$\succsim$}}
---


# Guide Dogs in Your Head

My paper, "[Hierarchical Aggregation of Information and Decision-Making](https://dl.dropboxusercontent.com/u/13046545/paper_heuristics.pdf)", essentially spells out the guide-dog model of unconscious influences in technical detail. It has a few implications which can all be explained in terms of the guide-dog metaphor:

1. You can't answer hypothetical questions accurately. In the same way a blind man wouldn't know what he'd do in another situation, without hearing from his guide dog.
2. You make inconsistent comparisons. .


## Difficulty Introspecting

I'm going to say that there are unconscious influences on my decisions if I can't accurately predict how I would act if the circumstances were different. That shows that I'm not conscious of how different factors contribute to my decisions.

This definition includes both cases where (A) I *think* I know what affects my decisions, and I'm wrong; or (B) I know that I don't know what affects my decisions.

We could then put the question a different way, instead of "how important are unconscious factors?" say "how deep does conscious thought go?" I.e., how much do we understand of our own motivations and reasoning?

Why would we assume that it goes all the way down? Animals make a lot of sensible decisions but probably don't have much insight into the interplay of reasons. We certainly have limited conscious insight into our *perceptual* judgments -- I couldn't explain what it is about my cousin that makes me recognize her, or what it is about the trajectory of a ball that makes me think it's going to land in a particular place.

To ask whether you know motivations is a pretty woolly question -- much more precise is whether people can give accurate answers to hypothetical questions: what would you think or do in this situation? This gives a concrete meaning to unconscious influences.

Overall I think that people are *bad* at this. I.e., they .

Here, first, are some shallow hypotheticals, which I think I can give roughly accurate answers to (but I'd still not be surprised if I was wrong):

* Would I still run for the bus if I had 5 minutes, instead of 6?
* Would I buy this chicken if it were $6/pound, instead of $5?
* Would I have chosen to buy fish, if the chicken wasn't available?

But there are also a lot of deeper ones, which I find pretty difficult to answer.

* Would I still run for the bus if I never saw other people running for the bus?
* Would I behave the same way towards colleague X if they were a woman instead of a man?
* What would I think of my parents if I was to meet them now, as strangers?
* What would I think of my work if I came across it as someone else's?
* Would my politics be the same if I went to a PhD program at a different school (where the professors' politics are different)?
* Would I feel the same way about my favorite album if they were selling it in Starbucks?

<!-- a difference between shallow and deep: whether I often observe independent variation in those attributes. -->


## Bundling Factors: Triangles and Figure-Eights

Jon and my paper builds on this basic idea -- that when factors are *bundled*, then the unconscious influence will tend to increase.

Here we need to make a fine distinction: suppose an unconscious factor $x$ has a weight $w$ in your judgment.

Here are a collection of inconsistent choices that a person could make, each of them revealing an unconscious preference for White over Black:


$$
\xymatrix{\binom{\text{\textsc{black}}}{\text{\textsc{PhD}}}\ar@{-}@/^{.3pc}/[r]|{\prec} & \binom{\text{\textsc{black}}}{\text{\textsc{MBA}}}\ar@{-}@/^{.3pc}/[dl]|(.4){\rsucc{45}}\\
\binom{\text{\textsc{white}}}{\text{\textsc{phd}}}\ar@{-}@/^{.3pc}/[u]|{\rsucc{270}}
}
$$

$$
\xymatrix{\binom{\mbox{\textsc{black}}}{\mbox{\textsc{phd}}}\ar@{.}[d]|{\rsucc{270}} & \binom{\mbox{\textsc{black}}}{\mbox{\textsc{mba}}}\ar@{.}[d]|{\rsucc{270}}\\
\binom{\mbox{\textsc{white}}}{\mbox{\textsc{phd}}}\ar@{.}[ur]|(.65){\rsucc{45}} & \binom{\mbox{\textsc{white}}}{\mbox{\textsc{mba}}}\ar@{.}[ul]|(.65){\rsucc{135}}
}
$$

$$
y\left(BP,\begin{bmatrix}BP & BM\\
\\
\end{bmatrix}\right) < y\left(BP,\begin{bmatrix}BP\\
 & WM
\end{bmatrix}\right)
$$

---

(couple of diagrams missing, need to fill these in.)

---

$$
y(\mbox{B},\{\mbox{B}\})<y(\mbox{B},\{\mbox{B},\mbox{W}\}) \\
y(\mbox{W},\{\mbox{W}\})>y(\mbox{W},\{\mbox{B},\mbox{W}\})
$$


#  Mapping out unconscious influences

So how should we go about testing for the existence of, and mapping out, unconscious influences?

Think of your responses to different outcomes as a landscape of hills (positive responses) and valleys (negative responses).


# Returning to the Motivating Examples

* **People judging a presidential candidate's actions differently depending on whether it's a man or a woman; people judging an ethical lapse differently depending on whether committed by a Democrat or Republican; academics judging a study differently depending on whether it supports their own pet theory.**

* **The little things that a family does to unconsciously spite each other: someone says that Thursday doesn't suit them, in part because they know that Thursday suits you best.**

Here the factor influencing you unconsciously is whether your family-member is free on Thursday.

* Judging hypotheticals:
* Judging jointly:


* **All the Freudian literature on repressed desires and childhood traumas manifesting themselves in adult decision-making. Maslow: “A desire for an ice cream cone might actually be an indirect expression of a desire for love."**

Suppose the factor unconsciously influencing you is your father's coldness when you were a child, and this causes you to be especially sensitive to praise by your boss. This is difficult to apply our two methods to, because it's hard to entertain counterfactuals: what would you do if your father were warmer? How would we know the correct answer?

I guess in principle one could do this: (1) ask people whether they believe that, on average, cold fathers cause people to be more sensitive to praise; (2) do the study, and find out whether cold fathers really do have this effect. This would show that, on average, people are not aware of a factor that has an influence on their decisions.

* **Your preferences changing with the circumstances: saying yes to a friend, a hairdresser, bartender, waiter, or salesperson, because it seemed like a good idea at the time, and later wondering why you didn't say no.**

** **Knowledge used in your judgments, but not consciously accessible: knowledge of grammar implicit in your judgements of whether a sentence sounds right; knowledge of physics implicit in your judgements of distance and velocity of the things you see; knowledge of faces implicit in recognizing your friends.**

As an example, take the order of adjectives. The phrase "big red car" sounds better than "red big car." However it's hard to explain why. Let's say that the rule is that X adjectives always precede adjectives of type Y.

Then judging hypotheticals can be run this way: give someone a list of adjectives and an incomplete sentence, e.g. "big ___ car." Then ask them to choose which of the adjectives would form a grammatical sentence. If they can only answer accurately by trying out each adjective, one by one, in the sentence, then their knowledge of grammar is unconscious.



# Conclusion

.

---

# Odds & ends

## When the guide dog has different preferences from you

My model of unconscious influences assumes that the final decision is always made by the blind man, and the dog just gives advice. However it's also interesting to think about when the guide dog can pull so hard that she forces the man to follow her -- i.e. mental factors which have some influence over the decision. There are a lot of papers in economics on multiple-selves models of decision-making which are like this -- the different selves have different preferences. There's a less-interesting and more-interesting version of this idea: if the two selves differ *only* in preferences, then it's not really different from a single self who has multiple competing preferences. It's more interesting if the two selves have access to different sets of information. Then there's a simple implication: if your guide dog has a preference that you don't share, then you'll take care in what information you expose them to -- you won't walk your dog past the butcher's shop. The papers in economics mostly talk about this kind of result, they try to rationalize all sorts of economic puzzles as people managing their guide dogs. (The future-self vs present-self tradeoff can be thought of in guide-dog terms: the guide-dog only sees the present costs and benefits of an action, not the future consequences). All of this fits within the Fodor-Pylyshyn setup where the dog has a subset of all available information. I think very little has been done in thinking about the degree to which the guide-dog has information that the man doesn't have -- i.e. when they differ in both preferences and beliefs. Then it becomes a little like a cheap-talk or persuasion game: the guide dog is giving you advice, and you know that they have a particular bias, yet you cannot completely was that bias out.


## History of Implicit Preferences

The existence of the unconscious is one of the few modern philosophical ideas, i.e. one of the few not already discussed by the ancient Greeks.

In 1817 in *Mansfield Park* Jane Austen wrote about Thomas Bertram perceiving that a rich suitor was showing interest in his niece, and that he could not “refrain (though unconsciously) from giving a more willing assent to invitations on that account’.” Austen had used the word "unsconscious" before that, but only to mean that people were doing something unintentionally, not that they were unaware that some factor was influencing their judgment. In the same year, 1817, Coleridge first used the term "the unconscious" in English (imitating Schiller's use in German).

It's an interesting question why people didn't talk about unconscious influences prior to the 18th century, given that it's been such a popular thing to talk about ever since. They weren't stupid -- Plato, Augustine, & Shakespeare weren't naive about human nature -- if unconscious influences are a big deal, why didn't they talk about them? If it was there all along, why did it take us so long to discover it?

Perhaps this answer is too cute, but you could say that the unconscious is only a problem for people who expect to be able to give a reason for everything they do. Let's say that human motivation is an emulsion -- drops of logic suspended in a liquid instinct. We often make little logical jumps, like preferring two dollars to one dollar. But more often we have to consult our instincts: when we have to choose between a kiss and a dollar, logic doesn't help, and we don't have a schedule of preferences we can consciously consult to decide whether it's a good deal. Only in the 18th century did European intellectuals begin to expect that we should find an entire logical skeleton underneath our decisions and give an explicit reason for every choice, and perhaps our failure in being able to explain ourselves led to the practice of talking about the unconscious as a separate mental process.
