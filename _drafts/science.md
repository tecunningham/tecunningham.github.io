---
layout: post
title: Episodes in Science
---

- pill and breast cancer -- 1996 analysis with pooled data finds that most associations in prior studies didn't replicate
    + http://www.ncbi.nlm.nih.gov/pubmed/8656904

- genes and behavior, GWAS, Laibson: "most published associations are wrong"
    + editorial about GWAS

- gambles and the utility fn - what a waste of effort

- priming replications

- fat, cholesterol, change of mind

- Feynman on measuring weight of electron, physical constants

- Meta-analyses where an effect disappears:
    + Oxytocin & sociality (Gidi)
    + Ego depletion

- Big systematic replications:
    + 40% of economics studies fail to replicate
    + 60% of psychology studies fail to replicate
    + http://www.sciencemag.org/news/2016/03/about-40-economics-experiments-fail-replication-survey


Use *these* facts to set priors on new research.

- [also: the comments on the failures of research into optical illusions.]


# 2020-08-30 Sunday ---------------- Progress in Machine Learning / Common Task Framework

**David Donoho, "Fifty Years of Data Science"**
  > "the crucial but unappreciated methodology driving predictive modeling’s success is what computational linguist Marc Liberman (Liberman, 2009) has called the Common Task Framework (CTF). An instance of the CTF has these ingredients:
    > (a) A publicly available training dataset involving, for each observation, a list of (possibly many) feature measurements, and a class label for that observation.
    > (b) A set of enrolled competitors whose common task is to infer a class prediction rule from the training data.
    > (c) A scoring referee, to which competitors can submit their prediction rule. The referee runs the prediction rule against a testing dataset which is sequestered behind a Chinese wall. The referee objectively and automatically reports the score (prediction accuracy) achieved by the submitted rule.

**Liberman (2015) "Reproducible Computational Experiments"**
   - http://languagelog.ldc.upenn.edu/myl/LibermanCATS02262015.pdf
   - Tells the history of machine translation. In the 1950s & 60s there were dozens of big research teams, but all pursuing different tracks, and all exaggerating their successes.
   - John Pierce was asked to audit it for DARPA. In 1969 he wrote, regarding the state of work on speech recognition: "Most recognizers [people working on speech recognition] behave, not like scientists, but like mad inventors or untrustworthy engineers. The typical recognizer gets it into his head that he can solve ‘the problem.’ The basis for this is either individual inspiration (the ‘mad inventor’ source of knowledge) or acceptance of untested rules, schemes, or information (the untrustworthy engineer approach). . . . The typical recognizer ... builds or programs an elaborate system that either does very little or flops in an obscure way. A lot of money and time are spent. No simple, clear, sure knowledge is gained. The work has been an experience, not an experiment.”
     > "We are safe in asserting that speech recognition is attractive to money. The attraction is perhaps similar to the attraction of schemes for turning water into gasoline, extracting gold from the sea, curing cancer, or going to the moon. One doesn’t attract thoughtlessly given dollars by means of schemes for cutting the cost of soap by 10%. To sell suckers, one uses deceit and offers glamor.” “It is clear that glamor and any deceit in the field of speech recognition blind the takers of funds as much as they blind the givers of funds. Thus, we may pity workers whom we cannot respect.” 
     - Funding was cut from speech recognition for 20 years. 
     - Mid-1980s DARPA resumed funding, but now on the basis of a common benchmark for evaluation, with public data, and a clear objective. It worked very well, and now we have really impressive speech recognition.
     - Liberman on "common task framework":
       - (a) A publicly available training dataset involving, for each observation, a list of (possibly many) feature measurements, and a class label for that observation.
        - (b) A set of enrolled competitors whose common task is to infer a class prediction rule from the training data.
        - (c) A scoring referee, to which competitors can submit their prediction rule. The referee runs the prediction rule against a testing dataset which is sequestered behind a Chinese wall. The referee objectively and automatically reports the score (prediction accuracy) achieved by the submitted rule.
     - Same basic structure has been used for other fields in machine learning. Donoho says *"The ultimate success of many automatic processes that we now take for granted – Google translate, smartphone touch ID, smartphone voice recognition – derives from the CTF research paradigm, or more specifically its cumulative effect after operating for decades in specific fields. Most importantly for our story: those fields where machine learning has scored successes are essentially those fields where CTF has been applied systematically.*

**Other presentations by Liberman**
   - As far as I can tell he hasn't written any papers on this, it just exists in slide-decks.
   - Mark Liberman, "Why Human Language Technology (almost) works"
     - https://www.centre-cournot.org/img/pdf/pdf-sem/Presentation%20Mark%20Liberman_21-05-2015%20(1.7%20MiB).pdf
   - Liberman, M. 2015 (April). “Reproducible Research and the Common Task Method”
     - https://www.simonsfoundation.org/event/reproducible-research-and-the-common-task-method/


- **Breiman (2001) "Two Cultures": Prediction vs Inference.** (arguing that prediction more important than inference):
   - "Statistics starts with data. Think of the data as being generated by a black box in which a vector of input variables x (independent variables) go in one side, and on the other side the response variables y come out. Inside the black box, nature functions to associate the predictor variables with the response variables ...
   - "There are two goals in analyzing the data:
      1. Prediction. To be able to predict what the responses are going to be to future input variables;
      2. [Inference]. To [infer] how nature is associating the response variables to the input variables.
   - "The statistical community has been committed to the almost exclusive use of [generative] models. This commitment has led to irrelevant theory, questionable conclusions, and has kept statisticians from working on a large range of interesting current problems. [Predictive] modeling, both in theory and practice, has developed rapidly in fields outside statistics. It can be used both on large complex data sets and as a more accurate and informative alternative to data modeling on smaller data sets. If our goal as a field is to use data to solve problems, then we need to move away from exclusive dependence on [generative] models ..."
