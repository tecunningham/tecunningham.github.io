---
layout: post
title: The Bayesian Interpretation of Experiments
---

<!-- https://fb.workplace.com/groups/109535843016173/permalink/345590889410666/ -->

*(zips up flame-resistant suit)*

# The Bayesian Interpretation of Experiments

**Once you commit the original sin of testing for statistical significance you enter upside-down world where good is bad, bad is good.** 

There are lots of weird implications of significance testing:

* The significance of a test depends on how many other tests you ran that day. 
* It's considered bad practice to check-in on studies before you've finished them.
* It's considered bad practice to test for things that you thought of after the data was collected.
* It's considered bad practice to talk about an effect which has p=0.06, but OK to talk about one which has p=.05. Some people even say you shouldn't use the phrase "almost significant" to describe things which are almost significant.<!-- (some people roll their eyes and say *"oh ... MaRgInAlLy SiGnIfIcAnT."* Don't mock them, even though they're trying to mock you, they're just confused.) -->

These paradoxes confused me for a long time until I started to think of classical inference as bayesian inference operating under a constraint. 


Classical inference can be thought of as Bayesian inference with a hard-coded prior. In some cases the hard-coded prior will be close to your true prior, and it's fine, but in other cases it won't and it'll cause bad inferences. To deal with those pathological cases classical inference has built up a structure of rules to protect against bad inferences. The rules either specify contexts where you shouldn't do any inference at all, or they suggest transforming the problem into one where the hard-coded prior is closer to your true prior. This gives us rules about multiple testing, about data-dependent stopping, and about testing posterior hypotheses.



<!-- Once you put on Bayesian spectacles then everything comes into focus.  -->

---

**TLDR:** (1) all these issues are much easier to think about through Bayesian lens; nevertheless (2) there is an argument for sometimes following the hypothesis-testing rules for psychological/institutional reasons.

---

## Bayesian vs Classial Inference

I'll compare two ways of interpreting experimental estimates. Suppose `posterior` represents the estimate of an effect that you'll use in decision-making, then here are two methods for calculating that:

1. **Classical.** If the experiment is statistically-significantly different from zero then you use the experimental estimate (`posterior=outcome`), otherwise you assume no effect (`posterior=0`). (This technically should be called "Null Hypothesis Significance Testing", and I'm giving a slightly exaggerated version of it).
2. **Bayesian.** You set `posterior` to be a weighted average of `outcome` and of `prior`. The prior represents your best-estimate of the effect before the experiment ran. The position of the posterior depends on the relative tightness of the two distributions: if the confidence intervals from your experiment are relatively tight then the posterior will be closer to the outcome; if instead your priors are relatively tight, meaning you have firm expectations about the experiment's likely effect, then the posterior will be closer to your prior.

Graphically we can show the three distributions:

```
        prior 
         ____
       _/    \_
    _-/        \-_
__-/              \-__-_______________________

                 experiment outcome        
                       ____
                     _/    \_
                  _-/        \-_
________________-/              \-__-_________
              posterior
                 __
                /  \
             _-/    \-_
___________-/          \-_____________________
```

## Classical Inference as Constrained Prior

Suppose our prior was a spike at zero and otherwise uniform:

```
             __
            | |
            | |
____________| |_____________
____________________________
             0              
```

This prior will cause Bayesian inference to behave similarly to classical inferences: when the outcome is small then the posterior will be heavily influenced by the spike, and so will shrink to be very near zero. When the outcome becomes larger then at some point it will escape the gravity of the central spike, and we'll have `posterior~=outcome`.

[chart of posterior vs outcome]

## Applications

This way of thinking about things turns a lot of crooked things about interpreting experiments straight:

1. **Everything is continuous.** In the classical framework there's a sharp distinction between estimates that are significant and not significant. In reality there aren't sharp edges like this: if something is not-quite significant (p=0.06) you should treat it almost the same as if it's significant (p=0.05).

2. **You can discount a statistically-significant outcome if it's unlikely.** Suppose you're running an experiment and you see a statistically-significant effect on an outcome nobody expected it to move. Then it's perfectly reasonable to heavily discount that outcome towards zero: you have relatively strong reasons to expect a zero effect, AKA a *tight* prior around zero, and so your posterior ought to remain close to your prior.

3. **Most experiments over-estimate the true effect.** If you measure a 3% effect in an experiment then when you re-run it, the effect will typically be closer to zero. Likewise if you measure a -3% effect, the true effect will be typically closer to zero. This is because in most settings the mean effect of experiments is around zero. This is especially true for effects that are noisy (when you have wide confidence intervals), and for outcomes that are hard to move (when your prior is narrow).

4. **It's OK to check-in on an experiment.** In the classical framework you should set and forget: it's bad practice to make decisions about collecting more data after already seeing experimental results, because you can use this to almost guarantee a significant result even when there's no true effect. But if you're interpreting experiments in a Bayesian fashion it doesn't matter: each time you increase the sample size the experimental estimate (i) moves closer to the true effect; and (ii) gets tighter confidence intervals, but it won't cause any bias.

5. **You don't need to adjust for multiple comparisons.** You should never adjust for the number of tests you're doing -- you should only adjust for the strength of your priors. The reason that multiple comparison adjustment is popular is because there's an *empirical* association between number-of-comparisons and strength-of-priors: when someone is testing a lot of different treatments or outcomes it's often because they have weak priors that any one of them would work, and those weak priors imply they should be relatively more conservative with the evidence. But number of tests is only a proxy, the true reason for adjustment is the strength of the priors.

6. **It's OK to come up with hypotheses after the experiment has run.** It's not allowed in classical model to run extra tests you hadn't planned, but there's no problem in the Bayesian framework as long as you're rigidly honest about your priors. I.e., if you state the same prior you would've stated before seeing the outcome.


### Where do Priors Come From?

- 

### Why?

Why do we still teach &  use the classical framework?

You can think of the classical setup as a *constrained* version of the Bayesian interpretation in which you effectively use same prior for all experiments.

In the Bayesian interpretation you must supply a prior, and the shape of the prior is essentially a judgment call about what you think of as the nature of the existing evidence. The classical setup removes that judgment call and replaces it with a rigid rule.

**This can have two justifications:**

1. The psychological justification is that people have a weakness for misremembering their expectations, and thinking they predicted what actually happened -- the classical rule constraints you from doing that.
2. The organizational justification is that people will tend to misrepresent to *others* their expectations. People who run experiments face very strong incentives in interpreting their outcomes -- shipping & promotion, publication & tenure -- and so often they can't be trusted to be neutral reporters of what is a reasonable prior. 

Like plastic cutlery, we use significance-testing as a way of protecting you from hurting yourself and others.^[Tukey: "The tool that is so dull that you cannot cut yourself on it is not likely to be sharp enough to be either useful or helpful."]

I personally think this is a reasonable way of trying to soften these psychological and organizational problems -- but I think the way it's taught often confuses people. It's much easier to understand the paradoxes of hypothesis-testing if we remember:

#  *Hypothesis testing is motivated by psychological & organizational constraints, not by statistical considerations.*

You should think of the rules of significance-testing as *etiquette*, not as statistics: i.e. we consider certain practices "bad form" not because they're bad inferences but because they're socially harmful.

## Coming Up

1. **Q: Where do you get priors?** You can get a useful benchmark from empirical distribution of previous experiments that have been run.
2. **Q: How to think about interpreting multiple metric movements?** and how to come up with an optimal composite/guardrail metric, and how it depends on the relative covariance of the metrics at experiment-level and user-level.
3. **Q: how should inferences map to decisions?** (in short: you need to specify some kind of loss function).
