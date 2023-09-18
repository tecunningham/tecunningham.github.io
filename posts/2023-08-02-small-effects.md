---
title: The Paradox of Small Effects
author: Tom Cunningham, [Integrity Institute](https://integrityinstitute.org/)
date: 2023-08-02
execute:
  echo: false
  cache: true # caches chunk output
fig-align: center
bibliography: social-media.bib
reference-location: margin
#citation-location: margin
format:
   html:
      toc: true
      toc-depth: 2
      toc-location: left
      code-fold: true
      html-math-method:
         method: mathjax
         url: "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg-full.js"
         #     ^ this forces SVG instead of CHTML, otherwise xypic renders weird
      include-in-header:
         - text: |
            <script>window.MathJax = {
                     loader: { load: ['[custom]/xypic.js'],
                                 paths: {custom: 'https://cdn.jsdelivr.net/gh/sonoisa/XyJax-v3@3.0.1/build/'}},
                  tex: {packages: {'[+]': ['xypic']},
                     macros: {
                        bm: ["\\boldsymbol{#1}", 1],
                        ut: ["\\underbrace{#1}_{\\text{#2}}", 2],
                        utt: ["\\underbrace{#1}_{\\substack{\\text{#2}\\\\\\text{#3}}}", 3]
                     }}};
            </script>

engine: knitr
editor:
   render-on-save: true
---
<style>
    h1 {  border-bottom: 4px solid black;}
    h2 {  border-bottom: 1px solid gray; padding-bottom: 0px; font-size: 14px; color: black; }
</style>

In summary:

1. **Attitudes are hard to change.** Many fields in social science have adopted a doctrine of "small effects": high quality studies tend to show that peoples' attitudes are not very sensitive to exposure to media, or to their peers' attitudes.
2. **Yet attitudes do change.** We see very wide society-level variation in attitudes, which are hard to explain without peer or media effects.
3. **Resolution of the paradox: each effect is small, but there are a lot of them.**

(see an earlier [Facebook post](https://www.facebook.com/tom.cunningham.374549/posts/pfbid022GaqAxUuKobKyS6soWnQVZYevPxkGxQ6BxAiScmA47eZdU9RAJPpGi1NrXQip6Jyl))

#              (1) Attitudes are Hard to Change

Many fields in social science tend to say that attitudes show little influence from either peer effects or from media exposure:

- @angrist2014perils says studies of peer effects *"have mostly uncovered little in the way of socially significant causal effects."*

- Political scientists talk about "the paradox of minimal effects", @ansolabehere2006paradox says that election campaigns *"seem to be inessential to understanding who wins and who loses."*

- David Stromberg says *"the lesson from the last 50 years of media research is that it is very hard to manipulate voters ... evidence of [supply side bias] effects is weak or non-existent"*

There are many studies which find large effects but they tend to be treated with extreme skepticism by the methodologists: they are overwhelmingly from lab experiments or observational data and so can be very biased.

#              (2) Attitudes do Change

**Attitudes vary a huge amount across time and space:**

- Variation in political and religious attitudes.
- Variation in attitudes towards other races, sexes, sexualities, religions.
- Variation in preferences over food, e.g. for rice vs wheat vs corn.
- Variation in preferences over how many children to have.


**It is hard to explain this variation with individual economic circumstances:** when someone migrates to another country they face different economic circumstances (different prices and income) but they typically maintain their attitudes for decades. 

**It is hard to explain this variation with genetic variation,** because attitudes vary so much over time, while genes move very slowly. 

So it seems like peer and media effects must be substantial proximal determinants of attitudes.

#              (3) Resolution: Each Effect is Small, but There are Many

**How can we resolve small treatment effects with big variation in outcomes?** It makes sense if we've only been testing very small treatments. Each individual effect is small but there are millions of them, so collectively the effects are large.

**Peer effect studies tend to find small effects when looking at random assignment of peers,** e.g. random assignment of roommates, but this may be because time with your roommate constitutes only a very small share of your overall exposure to other people and ideas.^[Kremer and Levy (2008) say *"Most studies do not find effects of these predetermined characteristics on the whole sample of students ... conventional peer effects on academic achievement ... are not estimated to be particularly important."*] Collectively that exposure must be hugely important in your attitudes.

**Media studies tend to find small effects from exposure to social media or to television,** but in most cases the media exposure is only a single-digit percentage-point share of their lifetime exposure to media. So the aggregate effect can be far larger than that measured in any credible experiment or natural experiment (in addition, much of the effect likely propagates through peer effects).

An individual campaign advertisement might have very small effects on voting intention, but an individual campaign advertisement is only a tiny tiny share of your lifetime exposure to political communication. Small individual effects are consistent with peoples' political attitudes being overwhelmingly determined by exposure and persuasion.

**More technically:** we can reconcile small effects with big variations if:

1. Effects have a long half-life, e.g. exposure in childhood can affect your attitudes as an adult.
2. Peer effects are propagated through many weak links, instead of a few strong links: i.e. there are substantial influences from all of society in addition to your family.
3. Persuasion works even with indirect channels, e.g. your political views aren't just affected by campaign ads, but also by the implicit attitudes to politics reflected in all the media you're exposed to
4. Attitudes are sensitive to the *average* rather than the *total* amount of persuasive material you're exposed to, thus marginal effects can be small while total effects are large.

(As a footnote: from my time in social media companies I learned that individual peer effects are tiny, yet we also know that social media demand is *entirely* peer effects, i.e. people only use Facebook because other people use Facebook.)

#           Other Notes

**The paradox of large effects.** @tosh2021piranha discuss an opposite problem: in some fields there are many claims of large effects, but it is not possible to reconcile the aggregate variance in the data with so many large effects. E.g. they discuss a paper claiming to show that exposure to age-related words tends to lower a subject's subsequent walking speed by 13%. If people are exposed to many such primes, and they are uncorrelated, then we should expect huge and implausible variation in peoples' day-to-day walking speed.

   Their problem is somewhat the opposite: they are talking about a literature which has many non-credible effects from lab experiments or observational data. Instead I'm talking about literature which has credible but small effects.

#           References