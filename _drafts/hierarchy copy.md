---
layout: post
title: Hierarchy
output: pdf_document
header-includes:
    - \usepackage{xypic}
---

<!--
Note: difficult to get encircled numbers. See following references:

1. https://tex.stackexchange.com/questions/7032/good-way-to-make-textcircled-numbers
2. in mathjax:  https://tex.stackexchange.com/questions/229005/how-do-i-encircle-text-like-make-a-circle-around-it
-->

Introduction
============

Human judgment is very powerful in some respects, and weak in others. We can outperform computers in doing many complex inferences - in deciphering images, sound, and text, and in certain types of complex reasoning. However our judgments are also sensitive to irrelevant details - as in optical illusions, and in framing effects.

I will argue that many of these puzzles can be explained by the *hierarchical* processing of information in the brain. When forming a judgment we draw on enormous pools of information - both current sensory inputs and prior experiences. I will assume that this information is aggregated in a hierarchy of layers, with each node summarizing information from earlier layers. The figures below contrast the two types of model, where $x_{1},\ldots,x_{n}$ are raw pieces of information, and $\xymatrix{*+[o][F-]{c}}$ represents the highest-level node, and arrows represent information flow between nodes.

$$\xymatrix@R-2pc{
\boxed{x_{1}}\ar[dddr] &  &  & \boxed{x_{1}}\ar[dr]\\
\boxed{x_{2}}\ar[ddr] &  &  & \boxed{x_{2}}\ar[r] & \circ \ar[dr]\\
\boxed{x_{3}}\ar[dr] &  &  & \boxed{x_{3}}\ar[rr] &  & \circ \ar[dr]\\
\boxed{x_{4}}\ar[r] & *+[o][F-]{c} &  & \boxed{x_{4}}\ar[rru] &  &  & *+[o][F-]{c}\\
\boxed{x_{5}}\ar[ur] &  &  & \boxed{x_{5}}\ar[r] & \circ \ar[urr]\\
\boxed{x_{6}}\ar[uur] &  &  & \boxed{x_{6}}\ar[ur]\\
\boxed{x_{7}}\ar[uuur] &  &  & \boxed{x_{7}}\ar[uuurrr]
}$$


The hierarchical model, illustrated on the right, implies that the conscious brain, $\xymatrix{*+[o][F-]{c}}$, has access mainly to pre-interpreted information, and limited insight into the raw material - the stimuli and learned regularities - from which our judgments are formed. This structure also implies the existence of certain characteristic biases, which occur when one branch of the hierarchy does not have access to relevant information available to another branch. I will argue that many of the biases we observe in perception, judgment, and decision-making have explanations which fit this model - i.e., they are side effects of the pre-processing of information by the brain. Some of the points are not novel, just formalized into my hierarchical framework. I think the most important contribution is to show an isomorphism between the structure of the hierarchy and the nature of the biases, and therefore show that the hierarchy in the brain can be systematically mapped by varying the information given to a person.

As motivation, everyday experience suggests that we have shallow insight into our own judgments. We are often poor judges of our direct sensory stimulation - such as which light is brighter, or which sound was louder - yet we are extremely good at using that information in recognizing objects - suggesting that we are separated from direct sensory stimulation by an intermediary which interprets it for us. Turning to abstract judgments, when we are asked to explain our reasons for making a certain judgment we often struggle, even in cases where we are confident that our judgment is correct: explaining why some object looks far off, why some face looks like your cousin, why some sentence is not grammatical, or why one restaurant seems better than another. The hierarchical model says that we can have confidence without much insight because our inferences are performed pre-consciously.

This analysis has simple implications for behaviour. Suppose that the distance of an object is calculated by a pre-conscious process, using a limited set of cues. In some cases there will be additional information that is relevant in calculating distance which is accessible to the conscious brain but which bypasses the pre-conscious process. Then we expect that extra information to be only imperfectly integrated with the previous inputs. Suppose there is some cue used by a pre-conscious process -- the colour of an object -- but we are also told that this cue is not relevant in the current case; then the decision-maker's best estimate of distance will depend on that cue, even though they know it is irrelevant, because the pre-conscious estimate of distance depends on that cue, and the pre-conscious estimate remains an informative proxy for distance. The direction of the bias can, in addition, be predicted, if we know the relationship between that cue and distance: if more distant objects tend to be blue (as is indeed true), then we would predict a bias such that people over-estimate the distances of objects that they know to be blue (which is also true).

This model is related to many existing literatures, including: (1) the debate over top-down vs bottom-up influences in perception; (2) theories of modularity and massive modularity; (3) theories of efficient coding and predictive coding; (4) the debate over the existence of tacit knowledge; (5) the debate over whether perception should be described as Bayesian inference; (6) inattention models of decision-making in economics; (7) the 'heuristics and biases' and 'dual systems' paradigms in judgment and decision-making; and (8) the realism vs anti-realism debate in philosophy. I discuss connections to each of these literatures below.

Sketch of Applications
======================

Sensory biases
--------------

When people are asked to directly judge some stimulus - e.g. which of two lights is brighter, which shape is larger - they are often influenced by other irrelevant stimuli. For example judgment of brightness may be influenced by size, judgment of timing may be influenced by sound, etc.. The hierarchical model provides a possible explanation: the conscious brain has access only to pre-processed information, consisting of inferences about the world, the raw stimuli are not directly accessible. When asked to estimate the raw stimuli, the conscious brain must infer them from the reports generated by intermediary processes. In our diagram, suppose that some set of sensory stimuli $x_{1},\ldots,x_{n}$ are used by a pre-conscious node to infer some value $v$, generating $\hat{v}=E[v|x_{1},\ldots,x_{n}]$, and suppose that the conscious brain has access only to the inference, $\hat{v}$ as in this diagram:

$$\xymatrix{
\,                      & \boxed{x_{1}}\ar[dr]\\
\boxed{v}\ar[ur]\ar[dr] &                 & *++[o][F-]{\hat{v}}\ar[r] & *++[o][F-]{c}\\
                        & \boxed{x_{2}}\ar[ur]
}$$

When asked about some sensory stimulus, $x_{1}$, the conscious brain will report, $$E[x_{1}|\hat{v}]=E[x_{1}|E[v|x_{1},x_{2}]].$$ This shows how judgment of one stimulus, $x_{1}$, can be influenced by some other stimulus, $x_{2}$ (for example, judgment of size influenced by color, motion by sound, etc.). The model predicts a number of findings:

1.  If we know what feature, $v$, is being inferred, and we know the correlations between $v,x_{1}$ and $x_{2}$, then we can predict the direction of the bias ($\frac{d\hat{x}_{1}}{dx_{2}}\propto\frac{d\hat{v}/dx_{1}}{d\hat{v}/dx_{2}}\propto\frac{dx_{1}/dv}{dx_{2}/dv}$). Some of these effects are very easy to explain: (1) when exposed to a sequence of beeps and flashes, reports of the number of beeps is influenced by the number of flashes, and vice versa.

2.  There are some well-known paradoxes: e.g., size-weight illusion, or the size-distance effect. These biases make predictions about what value, $v$, is being inferred. For example the size-weight illusion implies that our intermediate processes infer the *density* of an object, and when we are asked about the weight of an object, we back-infer from our beliefs about its density.

3.  In many cases biases are diminished when judgments are measured by physical response, rather than by verbal report. For example, when asked about the weight of an object that they can hold, people are biased by its size (larger objects are judged to be lighter), but when asked to lift the object, their grasp seems to correctly anticipate the weight of the object, and not be biased by the object's size.

The most common formal theory account of sensory biases is based on "coding" of stimulus data: as in the hierarchical model, raw stimuli are not directly accessible to the conscious process, instead they are inferred from intermediate representations. The difference is that coding theories assume that the intermediate nodes *compress* the data from the stimuli, while in the hierarchical theory they perform *inferences* about properties of the world. I discuss in detail how to distinguish predictions of the two models.[^1]

Contrast and Assimilation effects
---------------------------------

Probably the most consistent and widespread sensory bias is a *contrast* effect: the apparent intensity of a stimulus is negatively affected by its neighbors - a light seems darker when its neighbors become brighter, a sound seems louder when its neighbors become softer, etc.. The effect comes from neighbors in time as well as space, and affects all sorts of sensory judgments (brightness, colour, contrast, volume, pitch, size, orientation, etc.). This effect has been considered something of a puzzle for Bayesian or signal-processing models of perception because, although, it is possible to rationalize a spillover effect from neighbors by assuming that people receive only noisy signals of stimuli, such an assumption predicts an effect in the *opposite* direction: i.e., if a stimulus' neighbor is bright then, under reasonable assumptions, it would seem to imply that the stimulus itself is probably brighter, all else equal.[^2]

Adelson (1993) gives a neat explanation of contrast effects in lightness perception which can be formalized in a hierarchical model. The crucial assumptions being that (1) intermediate nodes infer the properties of objects in the world, not properties of the stimuli; and (2) the relationship between stimuli and properties of the world fluctuates with the environment. The fluctuating relationship implies that sensory organs need to be continuously recalibrated, generating a contrast effect. Consider the following diagram of information flow: suppose that two stimuli, $x_{1}$ and $x_{2}$, are functions of two values ($v_{1}$ and $v_{2}$), but with noise ($e_{1}$ and $e_{2}$). We assume that, in the hierarchy, separate nodes infer $v_{1}$ and $v_{2}$ from $x_{1}$ and $x_{2}$, and it will be rational for each inference to take into account both (i.e., $\hat{v}_{1}$ will be a function of both $x_{1}$ and $x_{2}$) as long as there is a correlation either between $v_{1}$ and $v_{2}$, or between $e_{1}$ and $e_{2}$. Finally, if the correlation between $e_{1}$ and $e_{2}$ is higher than that between $v_{1}$ and $v_{2}$, then a higher $x_{2}$ will imply a *lower* $\hat{v}_{1}$, i.e. this model will generate the contrast effect so often observed.[^3]

$$\xymatrix@R-2pc{
\boxed{e_{1}}\ar[dr]\\
\boxed{v_{1}}\ar[r] & \boxed{x_{1}}\ar[ddr]\ar[r] & *++[o][F-]{v_1}\ar[dr]\\
                    &                             &                  & *++[o][F-]{c}\\
\boxed{v_{2}}\ar[r] & \boxed{x_{2}}\ar[uur]\ar[r] & *++[o][F-]{v_2}\ar[ur]\\
\boxed{e_{2}}\ar[ur]
}$$

Intuitively this model says contrast effects occur because of noise in the world, requiring our perceptual systems to continuously recalibrate. To infer the lightness of an object we need to take into account the illumination, implying that when an object has a bright neighbor the brightness will cause us to update positively about the illumination, and so update negatively about the lightness of the original stimulus, i.e. a contrast effect. Similarly with perception of size, contrast, volume, pitch, and orientation, each inference requires calibration, and neighboring stimuli will cause adjustments of the calibration, giving rise to contrast effects.

Evidence for this interpretation comes from the prediction that contrast effects will occur only among pairs of stimuli which the brain expects to be affected by a common source of noise. Adelson (1993) showed that lightness contrast effects only occur between objects which appear to be illuminated by the same light source, and I outline evidence that other types of contrast effects have a similar pattern.

Finally the basic model can explain contrast effects in judgments about the world (about $v_{1}$ and $v_{2}$), but not in judgments of sensations ($x_{1}$ and $x_{2}$), although both occur. I show later how a slight enrichment of the model can explain both.

Biases in judgment about the world
----------------------------------

The two previous applications referred just to biases in judgments of sensory stimuli such as brightness, pressure, loudness. The same model can also explain why we have biases in judgments about features of the world, such as distance, weight, or type of an object. Some examples of such biases are (1) judging colder objects to be heavier; (2) judging bluer objects to be more distant; (3) judging objects to be smaller when surrounded by larger objects.

Here the logic is that relevant information is aggregated in different channels.

-   (E.g., fog & distance; e.g. size-weight )

$$\xymatrix{
\boxed{v_{1}}\ar[r]\ar[ddr] & \boxed{x_{1}}\ar[dr]\\
                          &                    & *++[o][F-]{v_1}\ar[r] & *++[o][F-]{c}\\
\boxed{v_{2}}\ar[r]\ar[uur] & \boxed{x_{2}}\ar[ur]
}$$

Biases in judgment and decision-making
--------------------------------------

Violations of consistency are ubiquitous in laboratory tests of judgment. For example the answer to a question often depends on how it is phrased. In a hierarchical model these biases can be interpreted as due to inferences that bubble up in separate streams, and so fail to share relevant information.

A basic model is as follows:

$$\xymatrix@R-2pc{
     \makeatletter
     \xydef@\xymatrixrowsep@{1px}
     \makeatother
 & \boxed{x_{1}}\ar[rrd]\\
 &  &  & *++[o][F-]{v}\ar[ddr]\\
\boxed{v}\ar[uur]\ar[r]\ar[ddr] & \boxed{x_{2}}\ar[rru]\ar[rrrd]\\
 &  &  &  & *++[o][F-]{c}\\
 & \boxed{x_{3}}\ar[urrr]
}$$

The hierarchical model implies that:

1.  When people are told to ignore some cue they will fail if that cue
    is processed prior to reaching consciousness.

2.  When people are given two cases to judge simultaneously, they can
    control for the influence of irrelevant cues.

Testing for Implicit knowledge
------------------------------

There has been a long debate over how much of human knowledge is implicit (i.e., inaccessible to conscious thought) and there remains general disagreement over how to define implicit knowledge, and how to test for it.

Within the hierarchical model there is a simple distinction between information that is explicit and implicit: whether information is accessible to consciousness directly, or only through its contribution to an earlier node. The definition implies a test: knowledge is implicit if it cannot be *modulated* at will, for example by asking subjects to interpret a set of cues in a different way, or to selectively ignore some cues.

More precisely, here are some suggested tests for implicit knowledge:

1.  In knowledge of grammar.

2.  (\...)

Biases in Judgment of Sensation
===============================

[remains to fix: (1) prediction: unsupervised neural net should show assimilation; supervised should show contrast; (2) the "relief" problem: people should have enough information to fix this, unless they're ignorant of strength of spillovers]

There are many cases where people make systematic mistakes about
    their own sensations - what they see, what they hear, what they
    touch. Most well known are optical illusions, e.g. two identical
    lines which people judge to be different (the Muller-Lyer illusion).
    These are not just imperfect inference from sensations, they imply a
    mistake about the sensations themselves, because the two lines cast
    two identical projections upon your retina, yet you perceive them to
    have different lengths, both in the world and on your eye. A common
    feature in these illusions is *comparison* effects, where judgment
    of the strength of some sensation $s$ is affected by the strength of
    another sensation, $s'$ shown alongside or prior to $s'$. These
    effects can be split into assimilation effects, where an increase in
    $s'$ causes an increase in the apparent size of $s$, and contrast
    effects, where an increase in $s'$ causes a decrease in the apparent
    size of $s$. A second class of effects is cross-modal where, for
    example, judgment of a visual stimulus is affected by a sound, or
    vice versa. In general I will define a bias as an effect:
    $$\frac{d\hat{s}}{ds'}\neq0,$$ where $\hat{s}$ is an estimate of
    some sensation $s$, and $s'$ is the intensity of some other
    sensation.

-   The most popular account of this behaviour is that it is a
    side-effect of the bottleneck of perceptual coding: neurons compress
    sensory information, and when it is decompressed systematic
    distortions are introduced. I will state an alternative theory. The
    basic idea is not new, similar things have been said by others,
    especially Ted Adelson, but I state it in a more explicit and formal
    way, and derive a number of predictions which are not otherwise
    obvious.

-   Before stating the theory it is important to introduce a distinction
    between sensations and the values inferred from those sensations.
    Some examples are as follows:

       sensation ($s$)                 values inferred ($v$)
      ------------------ -------------------------------------------------
        size on retina              size and distance of object
         sound heard              syllable spoken and the speaker
       pressure on hand            weight and density of object
       colour on retina          colour of object, colour of light
       motion on retina   motion of object, motion of eye, motion of head

      : [\[tab:SensationValue\]]{#tab:SensationValue
      label="tab:SensationValue"}The distinction between sensation and
      value.

    The contents of the second column is a matter of conjecture - we do
    not know which things are being inferred from a particular
    sensation, and probably multiple things. However it's worth noting
    that judgment of any given value can be rationally influenced by a
    range of sensations: it is in no way irrational for perception of
    the syllable spoken to be influenced by your hearing, your vision,
    or your prior expectations. The biases we are interested in
    explaining regard the cross-contamination of sensations themselves,
    $\frac{d\hat{s}}{ds'}\neq0$.

-   A second preliminary remark is that humans are, in general,
    extremely good at inferring properties of the world from sensations.
    A simple demonstration is the difficulty in writing a computer
    program to do the same thing.

Back-Inference of Sensations and Correlated Noise.
--------------------------------------------------

-   My account of biases is based on two assumptions: (1) back-inference
    and (2) correlated noise.

-   **Back-inference.** I mean by "back-inference" the idea that we do
    not have direct conscious access to our sensations, and that we
    infer them by reversing the inferences made by early perceptual
    modules. The model assumes two stages: the lower perceptual system
    infers values of the world from the sensations it receives;
    subsequently, the higher cognitive centers receive those inferences,
    without information about the original sensations themselves. Thus
    when we are asked about the sensations, we *back-infer* from the
    values which were themselves inferred from the stimuli.
    Schematically, the setup is as follows:
    $$\xymatrix{ &  &  &  &  & \ar@{<-}@/_{1pc}/[ld]\hat{s}_{1}=s_{1}|\hat{v}\\
    v\ar@/^{2pc}/[rr]|(.3){s_{1}}\ar[rr]|(.3){s_{i}}\ar@/_{2pc}/[rr]|(.3){s_{n}} &  & \boxed{1}\ar[rr]^{\hat{v}=v|\mathbf{s}} &  & \boxed{2} & \ar@{<-}[l]\hat{s}_{i}=s_{i}|\hat{v}\\
     & \,\ar@{.}[uu] &  &  &  & \ar@{<-}@/^{1pc}/[lu]\hat{s}_{n}=s_{n}|\hat{v}
    }$$ The first system, $\boxed{1}$, receives sensations
    $\mathbf{s}=s_{1},\ldots,s_{n}$, from which it forms $\hat{v}$, an
    inference about $v$, which it sends to the second system,
    $\boxed{2}$. The second system, when asked to estimate sensations,
    does not have direct access to $s_{1},\ldots,s_{n}$, so it will
    *back-infer* them. Therefore estimates of one sensation can be
    influenced by another sensation. More interestingly, the direction
    of the influence will be predictable if we know the relationship
    between $s$ and $v$:[^4]
    $$\frac{d\hat{s}_{1}}{ds_{2}}\propto\frac{d\hat{v}/ds_{2}}{d\hat{v}/ds_{1}}.$$

-   A simple intuitive example is the McGurk effect, in which subjects
    are presented with two stimuli: (i) video of lips mouthing a
    syllable, and (ii) a sound clip of speech. Often a subject who is
    played exactly the same sound twice will report *hearing* different
    syllables, when the video shows different motion of lips.[^5] This
    follows from back-inference: System 1 first infers the syllable
    spoken (from both vision and sound), and then System 2 back-infers
    the original sensations from the reconstructed syllable. In this
    example the effect is quite intuitive, and the formal model doesn't
    add much. In other cases the analysis is more enlightening.[^6] [^7]

-   The theory's predictions rest entirely on the correlation of $v$ and
    $s$. A simple prediction is that there should exist positive
    comparison effects ("assimilation" effects) between two similar
    stimuli. Suppose that there were two values ($v_{1},v_{2}$), each
    with a corresponding correlated signal ($s_{1},s_{2}$). In most
    cases it seems natural to assume that $v_{1}$ and $v_{2}$ are, if
    anything, positively correlated. Then $s_{2}$ should be positively
    correlated to $v_{1}$, and therefore we would generally expect
    $\frac{d\hat{s}_{1}}{ds_{2}}>0$.

-   However - and this is a common paradox in the study of perception -
    in many cases we find the opposite: i.e. *contrast* effects, with
    $\frac{d\hat{s}_{1}}{ds_{2}}<0$. This fact has come up as a paradox
    in many discussions of perception (though most discussions don't
    make a clear distinction between $s$ and $v$).[^8][^9]

-   **Correlated noise.** The prevalence of contrast effects can be
    accounted for by my second assumption: correlated noise. Suppose
    that $s_{1}$ and $s_{2}$ are each related to $v_{1}$ and $v_{2}$,
    and each has additive noise, $e_{1}$ and $e_{2}$. If $e_{1}$ and
    $e_{2}$ are sufficiently correlated then, although $s_{2}$ is
    positively correlated to $v_{1}$, it will enter negatively into
    $\hat{v}_{1}(s_{1},s_{2})$, because it will now become more
    informative about $e_{1}$ than about $v_{1}$. In the Gaussian model
    below I show the following relationship:
    $$\frac{d\hat{v}(s_{1},s_{2})}{ds_{2}}\propto\mbox{corr}(v_{1},v_{2})-\mbox{corr}(e_{1},e_{2}).$$
    In short: we should expect assimilation effects when the values are
    more correlated than the noise, and contrast effects when the noise
    is more correlated than the values. I will argue that when we
    observe contrast effects, there is good reason to believe that the
    error is correlated.

-   Why would errors be correlated? Because in our sense organs pick up
    a mixture of environmental variables, most of which are irrelevant,
    requiring us to contininuously recalibrate our sensations. I give
    some examples in the following table:

         sensation ($s$)         value ($v$)            noise ($e$)
      --------------------- ---------------------- ---------------------
         light on retina       colour of object        illumination
         size on retina         size of object      distance of object
        pressure on hand       weight of object     sensitivity of hand
       oriention on retina   orientation in world   orientation of head
        motion on retina       motion of object        motion of eye

      : [\[tab:distinction\]]{#tab:distinction
      label="tab:distinction"}The distinction between sensation, value,
      and noise for a variety of sensory contexts.

    Contrast effects will occur whenever noise tends to be more
    correlated, or slower-moving, than value: for example when we have
    priors that nearby objects tend to share the same illumination, or
    the same distance. Another way of putting this is that the
    low-frequency elements of a stimulus tend to be noise, thus the best
    estimate of value will look like a high-frequency filtered version
    of the original stimuli.

-   **Summary of predictions.** My claim is that this theory can give a
    good prediction of the direction of biases across a range of
    psychophysics experiments. In summary:

    1.  When comparing similar stimuli, contrast effects
        ($\frac{d\hat{s}_{1}}{ds_{2}}<0$) will tend to occur when the
        stimuli are shown clearly (i.e., not near the limits of
        perceptability), and when the two stimuli are perceived to
        reside in the same plane. Assimilation occurs in the opposit
        type of situation.

    2.  When judgment is affected by a dissimilar stimulus (e.g., visual
        judgment being affected by auditory cues), contrast effects will
        tend to occur when the additional cue is associated with the
        stimulus, assimilation effects will occur when it is associated
        with the value.

    3.  These biases will tend to be smaller for more automatic
        responses - e.g. grasping responses - insofar as they receive
        signals prior to high-level processing.

Gaussian model of back-inference
--------------------------------

-   A simple and intuitive solution for the entire model exists when the
    signals and values are all Gaussian. Treating $s$ and $v$ as
    vectors, we will be interested in their covariance:
    $$Var\begin{pmatrix}s\\
    v
    \end{pmatrix}=\begin{pmatrix}U & C\\
    C' & V
    \end{pmatrix},$$ and we can then derive the output of the first
    stage, $E[v|s]$, denotes $v|s$: **$$\begin{aligned}
    \hat{v}=v|s & = & C'U^{-1}s,\end{aligned}$$** which means we can
    derive the second stage output, $s|\hat{v}$: $$\begin{aligned}
    cov\begin{pmatrix}s\\
    \hat{v}
    \end{pmatrix} & = & \begin{pmatrix}U & C\\
    C' & C'U^{-1}C
    \end{pmatrix}\\
    s|\hat{v} & = & C(C'U^{-1}C)^{-1}\hat{v}\\
     & = & C(C'U^{-1}C)^{-1}C'U^{-1}s.\end{aligned}$$

-   Suppose we have just two values and two sensations, all are mean
    zero, with covariance: $$Var\begin{pmatrix}s_{1}\\
    s_{2}\\
    v_{1}\\
    v_{2}
    \end{pmatrix}=\begin{pmatrix}\sigma_{s}^{2} & \theta_{s,s}^{2} & \theta_{s,v}^{2} & \phi_{s,v}^{2}\\
     & \sigma_{s}^{2} & \phi_{s,v}^{2} & \theta_{s,v}^{2}\\
     &  & \sigma_{v}^{2} & \theta_{v,v}^{2}\\
     &  &  & \sigma_{v}^{2}
    \end{pmatrix}.$$ We can solve for $\hat{v}$:[^10] $$\begin{aligned}
    \hat{v}=E\left(\begin{array}{c}
    v_{1}\\
    v_{2}
    \end{array}|\begin{array}{c}
    s_{1}\\
    s_{2}
    \end{array}\right) & = & Cov_{v,s}Var_{s}^{-1}\begin{pmatrix}s_{1}\\
    s_{2}
    \end{pmatrix}\\
     & = & \begin{pmatrix}\theta_{s,v}^{2} & \phi_{s,v}^{2}\\
    \phi_{s,v}^{2} & \theta_{s,v}^{2}
    \end{pmatrix}\begin{pmatrix}\sigma_{s}^{2} & \theta_{s,s}^{2}\\
    \theta_{s,s}^{2} & \sigma_{s}^{2}
    \end{pmatrix}^{-1}\begin{pmatrix}s_{1}\\
    s_{2}
    \end{pmatrix}\\
     & = & \begin{pmatrix}\theta_{s,v}^{2} & \phi_{s,v}^{2}\\
    \phi_{s,v}^{2} & \theta_{s,v}^{2}
    \end{pmatrix}\frac{1}{\sigma_{s}^{4}+\theta_{s,s}^{4}}\begin{pmatrix}\sigma_{s}^{2} & -\theta_{s,s}^{2}\\
    -\theta_{s,s}^{2} & \sigma_{s}^{2}
    \end{pmatrix}\begin{pmatrix}s_{1}\\
    s_{2}
    \end{pmatrix}\\
     & = & \frac{1}{\sigma_{s}^{4}+\rho_{s}^{4}}\begin{pmatrix}\theta_{s,v}^{2}\sigma_{s}^{2}-\phi_{s,v}^{2}\theta_{s,s}^{2} & \sigma_{s}^{2}\phi_{s,v}^{2}-\theta_{s,s}^{2}\theta_{s,v}^{2}\\
    \sigma_{s}^{2}\phi_{s,v}^{2}-\theta_{s,s}^{2}\theta_{s,v}^{2} & \theta_{s,v}^{2}\sigma_{s}^{2}-\theta_{s,v}^{2}\theta_{s,s}^{2}
    \end{pmatrix}\begin{pmatrix}s_{1}\\
    s_{2}
    \end{pmatrix}\end{aligned}$$ so
    $$\frac{d\hat{v}_{1}}{ds_{2}}=\frac{\sigma_{s}^{2}\phi_{s,v}^{2}-\theta_{s}^{2}\theta_{s,v}^{2}}{\sigma_{s}^{4}+\theta_{s}^{4}}.$$
    If signals have additive noise, as in $s_{i}=v_{i}+e_{i}$, where
    $e_{1}$ and $e_{2}$ have variance $\sigma_{e}^{2}$ and covariance
    $\theta_{e,e}^{2}$, then: $$\begin{aligned}
    \sigma_{v}^{2} & = & \sigma_{v}^{2}\\
    \sigma_{s}^{2} & = & \sigma_{v}^{2}+\sigma_{e}^{2}\\
    \theta_{s,v}^{2} & = & \sigma_{v}^{2}\\
    \phi_{s,v}^{2} & = & \theta_{v,v}^{2}\\
    \theta_{s,s}^{2} & = & \theta_{v,v}^{2}+\theta_{e,e}^{2}.\end{aligned}$$
    Plugging back in we get: $$\begin{aligned}
    \frac{d\hat{v}_{1}}{ds_{2}} & \propto & (\sigma_{v}^{2}+\sigma_{e}^{2})\rho_{v}^{2}-(\rho_{v}^{2}+\rho_{e}^{2})\sigma_{v}^{2}.\\
     & = & \alpha^{3}\sigma_{v}^{2}\rho_{v}^{2}+\sigma_{e}^{2}\alpha\rho_{v}^{2}-\alpha^{3}\rho_{v}^{2}\sigma_{v}^{2}-\rho_{e}^{2}\alpha\sigma_{v}^{2}\\
     & = & \alpha(\rho_{v}^{2}\sigma_{e}^{2}-\rho_{e}^{2}\sigma_{v}^{2})\\
     & = & \alpha\sigma_{e}^{2}\sigma_{v}^{2}(\rho_{v}-\rho_{e}).\end{aligned}$$
    Meaning that a contrast effect in value
    $\frac{d\hat{v}_{1}}{ds_{2}}<0$ will occur if and only if errors are
    more correlated than values ($\rho_{v}>\rho_{e}$).

-   An important limitation of this 2-element model is that it does
    *not* imply any comparison effects in sensations
    ($\frac{d\hat{s}_{1}}{ds_{2}}<0$), because, in this case, $\hat{v}$
    is invertible, i.e. both $s_{1}$ and $s_{2}$ can be identified from
    observing $v_{1}$ and $v_{2}$. Comparison effects in sensations
    could be derived if we add some additional noise, however they would
    be of a relatively small magnitude.

Applications of the Model
-------------------------

-   **(1) Comparison effects.** When comparing similar stimuli, contrast
    effects ($\frac{d\hat{s}_{1}}{ds_{2}}<0$) will tend to occur when
    the stimuli are shown clearly (i.e., not near the limits of
    perceptability), and when the two stimuli are perceived to reside in
    the same plane. Assimilation ($\frac{d\hat{s}_{1}}{ds_{2}}>0$) will
    occur in the opposite type of situation.

-   These predictions seem to be supported by the literature: the most
    common reported perceptual comparison effect is of a contrast
    effect, and these often occur in good viewing conditions: i.e., with
    high contrast and plenty of time. Figure
    [\[fig:illusions\]](#fig:illusions){reference-type="ref"
    reference="fig:illusions"} illustrates a variety of contrast
    illusions, and Parducci (1995) has a long discussion of other
    similar effects.

      -- --



      -- --

-   Sequential contrast effects are also very common, Series et al.
    (2009) say:

    > "prolonged exposure to a visual stimulus of a particular
    > orientation, contrast, or direction of movement induces a
    > systematic bias in the estimation of the orientation \...,
    > contrast \..., or direction \... of subsequent stimuli."[^11]

    and they refer to, for each case, evidence that the exposure causes
    a *contrast* effect.[^12]

-   There are some reported instances of assimilation effects
    ($\frac{d\hat{s}_{1}}{ds_{2}}>0$), but they tend to be in cases
    where the stimuli are presented only briefly or with low contrast,
    implying that the idiosyncratic noise for each sensation is
    relatively larger, and so the autocorrelation of noise is
    lower.[^13]

-   **(2) Context-dependence of comparison effects.** The theory implies
    that comparison effects should vary with context, in particular that
    contrast effects should be strongest when other cues indicate that a
    pair of stimuli share the same noise.

    This is exactly the argument of Ted Adelson's extensive work on
    lightness illusions: contrast effects occur almost exclusively when
    the neighboring patches appear to lie on the same plane, and
    therefore are appear subject to the same illumination, one example
    is given in Figure
    [\[fig:AdelsonCube\]](#fig:AdelsonCube){reference-type="ref"
    reference="fig:AdelsonCube"}.

    ![[\[fig:AdelsonCube\]]{#fig:AdelsonCube label="fig:AdelsonCube"}The
    two indicated squares appear to have similar colours in (a), but
    dissimilar colours in (b), though in fact both images are
    distortions of exactly the same pattern. The illusion can be
    explained as different interpretations of orientations, and
    therefore illumination. From Adelson
    (2001).](\string"p perception/figures/AdelsonSteps\string".png)

    If our analysis is correct then each of the illusions in Figure
    [\[fig:illusions\]](#fig:illusions){reference-type="ref"
    reference="fig:illusions"} should modulate in the same way from
    Adelson's manipulations.

    Eagleman (2001) discusses sequential contrast effects (or
    adaptation), and says that there is strong evidence of
    context-dependence, which argues against a simple neuronal
    explanation.[^14] In particular, adaptation effects occur mainly for
    stimuli which are similar in other respects.

-   **(3) Independent cue effects (cross-modal effects).** When judgment
    is affected by a dissimilar stimulus, e.g., visual judgment being
    affected by auditory cues, then contrast effects will tend to occur
    when the additional cue is associated with the stimulus,
    assimilation effects will occur when it is associated with the
    value.

    Some examples of classic cross-modal effects are when perception of
    what syllable is being heard is affected by vision - as in the
    McGurk effect discussed above; perception of the path of a moving
    dot, when ambiguous, is affected by an accompanying sound (Shimojo
    (-)); perception of how many times a light flashed are affected by
    how many times an accompanying beep sounded (Shams, Kamitani,
    Shimojo (2000)). A review article is Shams & Kim (2010, Physics of
    Life reviews) "Crossmodal influences on visual perception." Most of
    these effects are quite intuitive, and seem to fit the
    back-inference framework without having to discuss the value-noise
    distinction.

    There exists a famous exception to these congruent cross-modal
    effects: the size-weight illusion, in which the perceived weight of
    an object is negatively influenced by its size. An intuitive example
    is that an empty cardboard box can seem to have almost no weight.
    Brayanov and Smith (2010) call this an "anti-Bayesian" illusion,
    because the size of an object is, in general, positively correlated
    with its weight, so size should have a positive Bayesian effect on
    judgment of weight. The back-inference theory suggests a
    reinterpretation. We observe that
    $\frac{d\hat{\mbox{weight}}}{d\mbox{size}}<0$. This implies that:
    $$\frac{d\hat{\mbox{v}}/d\mbox{weight}}{d\hat{\mbox{v}}/d\mbox{size}}<0,$$
    these derivatives don't make sense if $v$ is the weight of the
    object. However they would follow if $v$ was the *density* of the
    object. In particular - suppose that our perceptual systems
    transmit, to our conscious brains, the density of an object of
    interest (e.g., because density is informative about composition,
    and composition is of value in making decision about the object).
    If, in turn, estimated density is used to estimate weight then, if
    we only have noisy information about size, the size-weight illusion
    will follow: as an object becomes larger, holding constant weight,
    it will (correctly) be judged to be less dense, and in turn it will
    be judged to weigh less.

    Another interesting case is the effect of distance cues on size
    judgment. In a number of illusions (Muller-Lyer, Ponzo) cues which
    make an object look farther away also cause it to appear larger.
    Gregory (1996) says this is a paradox from the Bayesian point of
    view because "\[t\]hese are illusory expansions from represented
    distance; though increased distance is associated with smaller
    retinal images."

    ![[\[fig:ponzo\]]{#fig:ponzo label="fig:ponzo"}A Ponzo
    illusion.](figures/ponzo)

    However this illusion can also be explained in this model:
    $$\frac{d\hat{\mbox{v}}/d\mbox{distance}}{d\hat{\mbox{v}}/d\mbox{size}}<0.$$
    \[need to finish this\].

-   **perceptual learning and contrast effects.** Another common finding
    is that learned associations can bias judgment: when two sensations
    are paired in a training phase, subsequently presenting one of the
    sensations biases judgment of the other. A simple Bayesian account
    with noisy perception would seem to predict that the bias would go
    in the direction of the association, however there are many cases
    with strong effects in the opposite direction: Howells (1944) paired
    red colours with a tone, subsequently playing the tone biased
    judgment of colour *away* from being red (when asked to identify
    white, subjects would choose a slightly green colour). McCollough
    (1965) found that staring at a horizontal red grille makes a
    subsequent horizontal black grille look greenish, and the effect can
    last several days. Mayhew and Anstis (1972) found that staring at a
    disk spinning clockwise under red light makes a subsequent
    stationary disk, under red light, appear to move counter-clockwise;
    this effect, again, can last several days.

-   A brief explanation is this: when we see a red object, we attribute
    the redness to two factors: the colour of the object, and the colour
    of the illumination (likewise, we attribute rotation in part to
    rotation of the object, and in part to rotation of our frame of
    reference). If we think that the paired stimuli are predictive of
    the context (e.g., illumination, frame of reference), then this can
    get the effect using the model from above.

    Haijing et al. (2006) find the opposite effect. They showed subjects
    a cube in 3D, rotating either left or right, and paired the
    direction of rotation with another cue (e.g., lateral motion of the
    cube). Subsequently when shown the cube in 2D, where the direction
    of rotation was ambiguous, the cue caused subjects to perceive
    rotation in the *same* direction as paired in the training task.
    Again the effect was long-lasting. \[explanation\].

-   **(4) Comparison of automatic and cognitive response to baises.**
    The back-inference theory implies that bias in judgment of $s$ will
    be smaller for the early system ($\boxed{1}$), and so automatic
    actions, which might be processed by the earlier system, could
    exhibit less bias. Pylyshyn (1990) and Aglioti DeSouza &
    Goodale (1995) find that illusions tend to affect visual judgment
    more than grasping. Franz (2001), however, finds no difference.

-   **Correlated noise implies that relative judgments will be more
    accurate.** A common observation in psychophysics is that relative
    judgment is much more sensitive than absolute judgment. This will
    obviously be true if errors are positively correlated in relative
    judgment. Take the derivation of the Just-Noticeable Difference
    (JND) above. Suppose that the two observations have noise with
    variance $\sigma_{e}^{2}$ and correlation $\rho_{e}$, then the JND
    will be: $$\begin{aligned}
    JND(v_{1},p)=\delta & = & v_{1}\left[\exp(2(\sigma_{e}^{2}-\rho_{e}\sigma_{e}^{2})\Phi^{-1}(p))-1\right].\end{aligned}$$
    As the correlation increases, the JND will fall, and it will go to
    zero as $\rho_{e}$ goes to 1.

-   **Other literature on back-inference and correlated noise.**

    -   Adelson (1993) says "\[i\]t is as if the visual system
        automatically estimates the reflectances of surfaces in the
        world, and the resulting lightness percepts inevitably sway the
        judgment of brightness."

    -   Schwartz, Hsu and Dayan (2007) discuss Adelson's theory of
        lightness illusions, and briefly consider it as an explanation
        of other contrast effects: "\[suppose\] that the visual system
        does not act as a veridical photometer, reporting the photon
        flux from different patches of visual space, but rather that it
        is interested in extracting two key properties that are
        associated with the patches illumination \... and surface
        reflectance \... The underlying generative model assumes that
        the observed luminance in a patch is multiplicatively generated
        by these properties. Crudely, brightness illusions arise when
        correct Bayesian inference about these properties is at variance
        with the manner in which particular scenes were generated."

    -   Kahneman (2002): "For a perceptual example of attribute
        substitution, consider the question: "What are the sizes of the
        two horses in Figure 7, as they are shown on the page?" The
        images are in fact identical in size, but the figure produces a
        compelling illusion. The target attribute that the observer is
        instructed to report is two-dimensional size, but the responses
        actually map an impression of three-dimensional size onto units
        of length that are appropriate to the required judgment. In the
        terms of the model, three-dimensional size is the heuristic
        attribute. As in other cases of attribute substitution, the
        illusion is caused by differential accessibility. An impression
        of three-dimensional size is the only impression of size that
        comes to mind for nave observers painters and experienced
        photographers are able to do better and it produces a perceptual
        illusion in the judgment of picture size. The cognitive
        illusions that are produced by attribute substitution have the
        same character: an impression of one attribute is mapped onto
        the scale of another, and the judge is normally unaware of the
        substitution."

    -   J T Enright on the moon illusion: "The subconscious impression
        of distance, once it has determined apparent size, must remain
        irretrievably locked in the subconscious \... \[t\]hese seem to
        be unresolvable paradoxes."

-   **Back-inference and reproduction.** Outside of the laboratory it is
    not very common for people to pay attention to the distinction
    between a sensation itself and the object inferred from that
    sensation. However when we paint a picture, exactly this task is
    necessary. If the back-inference theory is correct, it predicts that
    amateur painters will make certain systematic mistakes: i.e., when
    they see $s$, they will painting $\hat{s}$. The mistakes can be of
    two kinds: first, they know the function $\hat{v}(s)$, but because
    it is not invertible they cannot infer the original $s$; second,
    they do not know the function $\hat{v}(s)$, and so use their beliefs
    about it to reconstruct $\hat{s}$. Here are some quick examples:

    -   **shadows.** Amateur painters tend to underestimate the depth of
        shadows, because information about illumination is discarded by
        the perceptual system, as not relevant. They paint the colours
        of each surface as if it they were all under uniform
        illumination.

    -   **distance & tint.** In the world, more distant objects tend to
        be bluer, due to refraction of light by the atmosphere; amateur
        painters tend not to tint colors in this way, because the visual
        system discards the tint. Leonardo da Vinci noticed, and used,
        this relationship: he said "if one is to be five times as
        distant, make it five times bluer."

    -   **distance & contrast.** More distant objects tend to be
        blurrier and of lower contrast. Amateur painters tend not to
        show this colouring. Leonardo again: "To our obtaining a correct
        idea of the magnitude and distance of any object seen from afar,
        it is necessary that we consider how much of distinctness an
        object loses at a distance (from the mere interposition of the
        air) \... \[t\]his calculation, as to distinctness, must be made
        upon the idea that the air is clear, as, if by any accident it
        is otherwise, we shall (knowing the proportion in which clear
        air dims a prospect) be led to conclude this farther off than it
        is \... "

    -   **foreshortening.** Amateur painters tend to underestimate
        foreshortening effects, making near and far objects of a similar
        scale. Of course a mountain and a man couldn't fit in the same
        painting if drawn at the same scale, but a common feature of
        amateur paintings is a *local* constancy of size; for example,
        characters towards the front of a scene and towards the back are
        drawn at the same scale, despite a foreshortening of the
        architecture in which they are standing.

-   **Miscellaneous notes.**

    -   If this analysis is correct it seems to imply that we are making
        a certain type of systematic mistake: when we see a contrast
        illusion, as in Figure
        [\[fig:illusions\]](#fig:illusions){reference-type="ref"
        reference="fig:illusions"}, we seem to have enough information
        to invert $\hat{v}$ to get the original $s$. An alternative
        explanation could be ignorance of the coefficients.

    -   \[Cross-modal effects sometimes taken as evidence *against*
        modularity, e.g. Shams and Kim (2010) say "In contrast with the
        modular view of perception, \... the accumulating evidence,
        especially over the last several years has revealed that visual
        perception can both quantitatively and qualitatively be modified
        by the input from other modalities."; yet evidence from
        cross-modal illusions in fact is difficult to interpret without
        modularity.\]

    -   \[Coren & Miller 1974 find that contrast effects are modulated
        by context: the Ebbinghaus effect is much stronger when context
        is *similar*.\]

    -   **Side-effects.** The theory makes predictions not only about
        $\hat{s}$, but also about $\hat{v}$, and the noise $\hat{e}$. A
        nice example is the Muller-Lyer illusion, in which the apparent
        length of a line is affected by the orientation of arrowheads at
        the end of the line. Gregory (1966) finds that, when a line is
        suspended in space, the orientation of the arrowheads affects
        not just the perceived length, but also the perceived distance,
        such that the line which appears longer also appears to be
        farther away. This effect is consistent with the back-inference
        theory: people infer the object's true size ($\hat{v}$) from a
        set of cues, including the size on the paper and the presence of
        arrowheads; when comparing two lines they infer two different
        true sizes $\hat{v}_{1}$ and $\hat{v}_{2}$, and so judge the
        size on paper to be different.

    -   \[Damian finds an emotion contrast effect: show pictures of
        angry black men, then you become more gentle towards subsequent
        faces of black men.\]

    -   **Moon illusion.** (and size-distance paradox). [^15]

    -   **Back-inference and expectation.** Many studies find an effect
        of expectations on sensory perception.

        This helps to solve an apparent puzzle in perception: do
        expectations influence perception positively or negatively? Both
        findings are common, and indeed there are strong intuitions
        about both cases: each of the following two sentences makes
        intuitive sense:

        > "It looked big to me because I was expecting it to be big."
        >
        > "It looked big to me because I was expecting it to be small."

        According to the back-inference theory, expectations will have a
        positive effect for values ($\frac{d\hat{v}}{d\mu_{v}}>0$), but
        a negative effect for sensations
        ($\frac{d\hat{v}}{d\mu_{s}}<0$).[^16]

Alternative theory: coding
--------------------------

-   Many people have noticed an interesting analogy between perceptual,
    neural, and cognitive evidence: that some kind of *contrast*
    *effects* seem to occur in all three areas contrast-biases in
    perception; inhibition or normalization in neural coding; and
    reference-dependence in decision-making.[^17]

-   A common conjecture has been that the perceptual and cognitive
    effects can both be explained by the neural coding of signals, and
    in turn, that the neural coding is an optimal solution to an
    information transmission problem. The "efficient coding"
    interpretation was first made by Barlow and Attneave in the 1950s,
    in trying to explain activation patterns of neurons; the application
    to observable behaviour in perception and decision-making has been
    made independently by many people since.

-   In this section I review the evidence for the phenomena in
    perception and decision-making, and I give a number of reasons why I
    think that neural coding is *not* the correct explanation for most
    examples of those phenomena. The argument is largely independent of
    whether or not the neural coding is efficient.

-   The particular phenomena which I think are not explained by neural
    coding are the following:

    -   Contrast illusions in perception, as in the simultaneous
        contrast and sequential contrast examples given above.

    -   Common-difference effects in decision-making, for example being
        more sensitive to a \$10-\$20 difference than a \$210-\$220
        difference; being more sensitive to a 1%-2% difference than
        51%-52% difference; and being more sensitive to a 1-2 day
        difference than to a 71-72 day difference.

    -   Loss aversion in decision-making, for example unwillingness to
        take small gambles, and unwillingness to trade an endowment.

    -

-   The main points I will make are the following:

    -   The principal point is this: suppose we break up maps of stimuli
        into high-frequency and low-frequency parts. The biases we
        observe are as if people had discarded the low-frequency part -
        i.e., they are sensitive to local differences, but seem to
        ignore gradual changes. But if we are optimally compressing the
        stimuli, we should expect the exact opposite bias: the
        reconstructed version of the image should be *smooth*, because
        it's much more efficient to discard the high-frequency parts. We
        can justify discarding the low-frequency part if people are,
        instead of choosing a code to minimize a loss function in
        reconstructed sensations, $L=\sum_{i}(s_{i}-\hat{s}_{i})^{2}$,
        we use a loss function to minimize loss in reconstructed
        *values*: $V=\sum_{i}(v_{i}-\hat{v}_{i})^{2}$, where
        $s_{i}=v_{i}+e_{i}$, and error is more correlated than value
        (i.e., $corr(e_{i},e_{j})>corr(v_{i},v_{j})$).

    -   The magnitude of the biases we observe tends to be much larger
        than the magnitude of discriminability. For example, in Figure
        [\[fig:illusions\]](#fig:illusions){reference-type="ref"
        reference="fig:illusions"}, the contrast effects are quite
        strong - they seem an order of magnitude stronger than the
        limits of discrimination, for two stimuli presented side by
        side. Yet perceptual coding theories suggests that the two
        effects should be of similar magnitude.

    -   Neural coding cannot generate *unambiguous* contrast effects,
        contrast effects can only occur for a subset of the signals, and
        in fact, because coding introduces noise into transmission, it
        will tend to produce the opposite effect, i.e. assimilation.

    -   Perceptual contrast biases are sensitive to context in ways that
        are difficult to explain with perceptual coding.

    -   These three criticisms of perceptual coding explanations also
        apply to the decision-making anomalies I discuss above.

    -   Finally I discuss some reasons to believe that the patterns of
        neural coding we observe may themselves not be explained by the
        efficiency argument originally proposed by Attneave and Barlow.
        Horace Barlow made these points himself, in 2001:

        > "\[T\]wo points have become clear since those early days.
        > First, anatomical evidence shows that there are very many more
        > neurons at higher levels in the brain, suggesting that
        > redundancy does not decrease, but actually increases. Second,
        > the obvious forms of compressed, non-redundant, representation
        > would not be at all suitable for the kinds of task that brains
        > have to perform with the information represented."

-   **History: comparison effects in neurons.** In the 1950s and 60s
    neuroscientists measured the response pattern of cells in the
    sensory system, and found patterns that generated what looked like
    contrast effects. In particular, Stephen Kuffler shined spots of
    light into cats' eyes and found retinal ganglion cells which
    responded positively to stimulation at one point in the visual field
    and negatively to stimulation in surrounding points.[^18] This
    pattern of response among neurons has since been documented many
    times, and given various names "lateral inhibition", "mexican hat
    response", "center-surround filter", "normalization", and "contrast
    effects". A similar pattern is a *sequential* contrast effect: i.e.,
    neurons' firing rate tends to be lower when prior inputs were
    higher. The latter has also been called "adaptation" and "fatigue."

-   **Comparison effects and efficient coding.** In the 1950s Horace
    Barlow and Fred Attneave independently proposed that the
    input-output relationship of neurons can be explained as
    implementing an efficient compression of sensory information,
    applying the tools of Shannon's information theory.[^19]
    Dawkins (2000) gives a lucid explanation:

    > "By exploiting redundancy, it is possible to devise codes that
    > convey the same information at a cost of fewer pulses.
    > Temperatures in the world mostly stay the same for long periods at
    > a time. To signal 'It is hot, it is hot, it is still hot \...' by
    > a continuously high rate of machine-gun pulses is wasteful; it is
    > better to say, 'It has suddenly become hot' (now you can assume
    > that it will stay the same until further notice)."
    >
    > "\[T\]o push the idea to an extreme, most of the time the brain
    > does not need to be told anything because what is going on is the
    > norm. The message would be redundant. The brain is protected from
    > redundancy by a hierarchy of filters, each filter tuned to remove
    > expected features of a certain kind \... the set of nervous
    > filters constitutes a kind of summary description of the norm, of
    > the statistical properties of the world in which the animal
    > lives."

    Applied to comparison effects, if there tends to be a positive
    correlation between two sequential stimuli, $s_{t}$ and $s_{t-1}$,
    then in a loose sense it will be efficient to only send the
    *difference* between $s_{t}$ and $s_{t-1}$.

-

-   **Coding and biases.** If neural signals are encoded, what does this
    imply for behavior? If the encoding is perfect, i.e. there is a 1:1
    mapping between stimuli and encoded value, then the original stimuli
    can be perfectly inferred, and there will be no biases observed in
    behavior.[^20] We can therefore ask this question: given some
    stimuli $s$, what is the nature of the bias produced by the encoding
    function $c(s)$? A simple way of expressing this is to ask what is
    the average posterior for a given stimulus, i.e.:
    $$E[E[s|c(s)]|s].$$ Although this is a well-defined question, given
    a prior over $s$ and the coding function $c(s)$, it is not in
    general easy to characterize the solution. A trivial observation is
    that coding cannot generate a monotonic bias (i.e., systematic
    over-estimation or under-estimation). However we can make a number
    of less trivial observations.

-   **Contrast effects as changing the prior.** A common way of defining
    contrast effects, in this setup, is by varying the prior, $f(s)$.
    For example suppose that the subject observes first $s'$ then $s$. A
    higher $s'$ might lead to a higher expected $s$ in the subsequent
    trial, if $s'$ and $s$ are positively correlated. We can then define
    a contrast effect as: $$\frac{dE[E[s|c]|s]}{d\mu_{s}}<0.$$ i.e. high
    signals ($s>\mu_{s}$) are, on average, over-estimated
    ($E[E[s|c]|s]>s$), and low signals are under-estimated.

    -   **Coding cannot generate unambiguous contrast effects.** One
        general observation is that the posterior means must always have
        less variance than the prior, by the law of total variance:
        $$Var[E[s|c]]=Var[s]-E[Var[s|c]].$$ Suppose that the average
        posterior is always pushed away from the mean, i.e. suppose
        $E[E[s|c]|s]\gtrless s$ when $s\gtrless\mu_{s}$. Then the
        distribution of posteriors must have a greater variance than the
        distribution of $s$ itself, violating the law of total
        variance.[^21]

    -   **Gaussian noise generates** ***assimilation*** **not**
        ***contrast*** **effects.** If stimuli ($s$) are Gaussian and
        $c(s)=s+e$, with Gaussian $e$, then the solution is:[^22]
        $$E[E[s|c(s)]s]=\frac{\sigma_{s}^{2}}{\sigma_{s}^{2}+\sigma_{e}^{2}}(s-\mu_{s}),$$
        i.e. there is a bias towards the prior expectation of $s$(i.e.,
        a bias towards $\mu_{s}$).

    -   **Coding** ***can*** **generate over-reaction.** The coding
        example just given, with Gaussian noise, generates
        *under-reaction*, i.e. $\frac{dE[E[s|c(s)]|s]}{ds}<1$. However
        this is not a necessary property of coding, for example suppose
        $c(s)=\begin{cases}
        1 & ,\,s\geq\mu_{s}\\
        0 & ,\,s<\mu_{s}
        \end{cases}$. This will generate a very steep response function
        in the neighborhood of $s=\mu_{s}$. However the function
        $E[E[s|c(s)]|s]$ cannot be steeper than 1 everywhere, for the
        same reason that it cannot generate unambiguous contrast effects
        above.

    -   **Woodford (2017) claim on coding.** Suppose that the prior over
        stimuli and the transformation function are the same thing. This
        implies that the distribution of codes, $c=F(s)$, will be
        uniform. Now add Gaussian noise, and he claims that the average
        mean posterior, given a signal, will be:
        $$E[\hat{s}|s]=E[F^{-1}(F(s)+\tilde{u})]$$ This means that the
        bias will depend on the curvature of $F^{-1}$. Suppose $F$ is
        the standard normal, then $F^{-1}$ is concave then convex. By
        Jensen's inequality: $$\begin{aligned}
        s & >0\iff E[F^{-1}(F(s)+\tilde{u})]>s\\
        s & <0\iff E[F^{-1}(F(s)+\tilde{u})]<s.\end{aligned}$$ But this
        seems to contradict the result above, the law of total variance.

    -   **Wei & Stocker (2015) claim on coding.**[^23] They say that
        they can derive an expression for the bias
        (**$b(s)=E[\hat{s}|s]-s$**) which depends on the slope of the
        prior: when the prior is decreasing, the bias is positive, and
        vice versa.

    -   **Question:** we can decompose the effect into two parts: (1)
        the effect of the prior (pulling you in); (2) the effect of the
        nonlinear transform (pushing you out?).

    -   **Related literature.**

        -   Stocker and Simoncelli (2006) propose that the comparator
            $s'$ does not change the mean $\mu_{s}$, but changes the
            coding so that it becomes more sensitive in the neighborhood
            of $s'$. They argue that this will tend to produce a
            contrast effect.

        -   Schwartz, Hsu & Dayan (2007) discuss the orientation
            contrast illusion (see Figure
            [\[fig:illusions\]](#fig:illusions){reference-type="ref"
            reference="fig:illusions"} above), and find that occurs,
            with similar characteristics, in both sequential or
            simultaneous comparisons. The discuss whether it could be
            generated by some sort of encoding process (whether
            efficient or not).

        -   Series, Stocker & Simoncelli (2009) make a similar point.

        -   Wei & Stocker (2014) give conditions under which there will
            be a contrastive bias. In their setup the signals are
            defined on a circular space, so it is not clear whether the
            argument using the law of total variance applies (I don't
            know how to define variance for variables in a circular
            space).

-   **Barlow on efficient coding.** Barlow (2001) says:

    > *"\[T\]wo points have become clear since those early days. First,
    > anatomical evidence shows that there are very many more neurons at
    > higher levels in the brain, suggesting that redundancy does not
    > decrease, but actually increases. Second, the obvious forms of
    > compressed, non-redundant, representation would not be at all
    > suitable for the kinds of task that brains have to perform with
    > the information represented."*
    >
    > *"I think one has to recognize that the information capacity of
    > the higher representations is likely to be greater than that of
    > the representation in the retina or optic nerve. If this is so,
    > redundancy must increase, not decrease, because information cannot
    > be created."*

-   **Difficulties with the coding explanation of contrast effects.**

    -   **Stochasticity.** sdf

    -   **Modulation by context.**

    -   **Purpose of information.**sdf

-

-   **Loss aversion in decision-making is not similar to contrast in
    perception.** Comparison effects in perception (e.g., contrast
    illusions) are often compared to reference dependence in
    decision-making; the analogy is discussed at length in Kahneman's
    2002 Nobel lecture. However the analogy is in fact not very close.
    If taken literally it implies, regarding decision-making, that a
    quantity $x$ of some good comes to be perceived as less valuable
    when a comparison quantity $x'$ becomes larger.[^24] In contrast,
    the typical evidence for "reference dependence" is that people are
    more sensitive to regions below a reference point $x'$ than above
    it. Classical evidence for loss aversion comes from unwillingness to
    take small gambles, and unwillingness to trade away endowments. In
    fact, with a loss-averse utility function the effect of the
    comparison (or reference point) $x'$ on value is ambiguous. Consider
    the linear loss-averse function (with $\lambda>1$):
    $$u(x|x')=\begin{cases}
    \kappa+\lambda\beta(x-x') & ,\,x\leq x'\\
    \kappa+\beta(x-x') & ,\,x>x'
    \end{cases}$$ If we add the assumption that it goes through the
    origin ($u(0|x')=0,\,\forall x'$) then this predicts the exact
    opposite of perceptual comparison effect, an increase in the
    comparator will, if anything, *increase* the value of $x$
    $\frac{du(x|x')}{dx'}\geq0$.

-   **miscellanous notes.**

    -   **smoothness effects.** (In some cases people don't notice
        changes: acclimatisation, cornsweet effect. A natural Bayesian
        interpretation is that both value and error are correlated, but
        there is a spike at zero in the prior about changes in value,
        i.e. we expect there to be flat surfaces of value, not smoothly
        changing surfaces. This implies (I think) there should be an
        assimilation effect for small changes, and a contrast effect for
        large changes. I ran some experiments but didn't find it.).

    -   **distinguishing the theories.**\
        (coding catastrophe / etc.)\
        \[see file "compression v inference"\]

    -   -   **filters derived from artificial neural nets:**

    -   ![image](figures/ANNfilters)

Biases in Judgments about the World
===================================

-   Mistakes in judgments about the world. E.g.,
    $$\xymatrix{ & \ar@{.}[dddddd]\\
     & \boxed{x_{1}}\ar[dr]\\
    \boxed{v_{1}}\ar[ur]\ar[dr] &  & \tikz[baseline=(char.base)]{
      \node[shape=circle,draw,inner sep=2pt] (char){$\hat{v}$};}\ar[dr]\\
     & \boxed{x_{2}}\ar[ur] &  & \tikz[baseline=(char.base)]{
      \node[shape=circle,draw,inner sep=2pt] (char){$c$};}\\
    \boxed{v_{2}}\ar[ur]\ar[dr]\\
     & \boxed{x_{3}}\ar[uurr]\\
     & \,
    }$$

Hierarchy in Judgment & Decision-Making
=======================================

-   **Nutshell:**\
    (1) how important is modularity in explaining anomalies of
    judgment?\
    (2) not interested in how judgment degrades when you are in a hurry,
    interested in biases in deliberate judgment.\
    (3) sensory judgments show broad integration of information, but
    failure to modulate, implying encapsulation from high-level
    information.\
    (4) judgments of fact show similar biases, implying encapsulation
    from high-level information.

-   I will define modularity in a different way from most other writers.
    Suppose we think of the brain just as a function from some inputs
    $s_{1},\ldots,s_{n}$ to an action $a$, i.e. $a(s_{1},\ldots,s_{n})$.
    I will be interested in *the testable consequences of sequential
    aggregation of information*. Think of two different ways that the
    inputs could be aggregated. First, we could just aggregate all the
    information: $$\xymatrix{ &  &  & \boxed{a(s_{1},\ldots,s_{n})}\\
    *++[o][F]{s_{1}}\ar[urrr] &  & *++[o][F]{s_{2}}\ar[ur] &  & *++[o][F]{s_{3}}\ar[ul] &  & *++[o][F]{s_{4}}\ar[ulll]
    }$$ Second, we might aggregate it in chunks, as follows:
    $$\xymatrix{ &  &  & \boxed{a(x_{1},x_{2})}\\
     & \boxed{x_{1}(s_{1},s_{2})}\ar[urr] &  &  &  & \boxed{x_{2}(s_{3},s_{4})}\ar[ull]\\
    *++[o][F]{s_{1}}\ar[ur] &  & *++[o][F]{s_{2}}\ar[ul] &  & *++[o][F]{s_{3}}\ar[ur] &  & *++[o][F]{s_{4}}\ar[ul]
    }$$ I will argue that many puzzling features of perception and
    decision-making can be explained by the second model, in which
    information is aggregated in chunks.

-   To be precise, here are some inferences which I believe involve an
    important amount of modularity, i.e. which are made using only a
    subset of the total information: (1) judging the distance of a
    car; (2) recognizing a friend's face; (3) interpreting the sound of
    speech into its words; (4) choosing the next move in a chess
    game; (5) choosing which dish on a menu you'll most enjoy; (6)
    judging the mood of a person you are interacting with.[^25]

-   **Differences from existing literature on modularity.** Modularity
    is a longstanding issue in the study of the brain, and argument
    usually focuses on these issues: (1) the degree of top-down and
    cross-modal influence in perceptual judgments; (2) whether
    regularities learned in one context can generalize to another
    context; (3) disruption of responses by changes to the environment,
    such as imposing cognitive load, memory load, willpower depletion,
    or limiting response time; and (4) whether people have conscious
    access to rules that they have learned.

-   **Basic evidence for modularity.**

    1.  **Hierarchical organization of neurons.** When the activation
        patterns of neurons in the brain have been mapped they seem to
        be arranged in a hierarchical structure, with later neurons
        encoding more abstract representations.[^26] However the neurons
        are wired in both directions: there are substantial top-down
        connections, i.e. axons carrying information from 'later' to
        'earlier' areas. The hierarchical organization could, therefore,
        be consistent with perfect integration of all information
        (Gilbert & Li, 2013).

    2.  **Irrelevant influences in judgments.** (Interpretations that
        fail to take into account other information - stereotyped).

    3.  **Lack of introspection & tacit knowledge.** We have limited
        insight into how we judge the distance of an object, the
        grammaticality of sentence, the emotional state of another
        person, or the value of a house. We are notoriously bad at
        explaining the rules we use in each case - entire academic
        disciplines have spent decades trying to formalize what a child
        knows implicitly - and in many cases quite simples rules have
        been discovered.

    4.  **Context sensitivity of judgments.** Many of the automatic
        judgments we make are sensitive to the context. Consider the
        ability to recognize a face, to draw a logical inference, to
        judge the grammaticality of a sentence, or judge the value of a
        chess move. In each case we have very good instincts when the
        information is presented in a familiar format, but when it is
        presented in an unfamiliar way then our ability becomes much
        worse.

-   **Modularity in a nutshell:** A good metaphor would be that the
    brain works like a group of people - each has a different dossier of
    information - and each passes memos up the hierarchy towards the
    leader.

Existing Literature on Modularity
---------------------------------

-   **Summary.** (1) In the 1980s Fodor, Pylyshyn and Marr argued that
    much of perception is modular, in the sense of forming inferences
    without access to external information. (2)

-   **Physiological:** (1) wiring; (2) hierarchy in representations; (3)
    lesions.

    ![Hierarchical Organization in
    Perception](figures/brain_from_YeCunn)

-   **Pylyshyn: cognitively impenetrability of visual perception**. In
    1980 Zenon Pylyshyn, a cognitive scientist, made an empirical case
    for the "cognitive impenetrability" of visual perception, meaning
    that it "a major portion of vision \... does its job without the
    intervention of knowledge, beliefs or expectations, even when using
    that knowledge would prevent it from making errors."[^27] His
    arguments are that (1) visual perception is not influenced by
    contextual information, even when it would improve the
    inferences; (2) in cases where contextual information, or
    expectations, influence perception, these can be explained through
    the channel of selective attention - e.g. if you are expecting to
    see something, you keep looking for it until you see it; and (3)
    many visual illusions remain even when when you are aware that the
    perception is incorrect.[^28]

-   **Fodor: informational encapsulation of input systems.** Jerry
    Fodor's 1983 book, *The Modularity of Mind*, proposed a definition
    of modularity in cognition. He said that the most important
    characteristic is informational encapsulation: a cognitive process
    is encapsulated if it operates with access to only a subset of all
    the information used in the brain.[^29] Fodor argued that perception
    and language-parsing are modular in this sense: they work oblivious
    to contextual information, even when it's relevant, and this
    encapsulation is detectable in the mistakes the systems make. For
    example, many sensory illusions persist even when we *know* they are
    misinterpretations of our stimuli. In language processing,
    misreadings occur which could be corrected by context. Fodor also
    argued that modularity of the mind is limited to perceptual "input
    systems", and these systems feed into a general-purpose cognitive
    system.

-   **Massive modularity.** A stronger type of modularity proposes that
    even high-level functions are recognizably modular: for example,
    that we have specialized systems to simulate other peoples'
    thoughts, to represent numbers, to simulate physics, to detect the
    relatedness of another person, or to trigger disgust or anger. One
    famous example is Cosmides and Tooby's (1992) proposal that people
    have a "cheater detection" module, based on the observation that
    people are much better at solving a logical problem when it is
    described as a problem of detecting cheaters.[^30] Another set of
    examples is from how our attitudes react to a situation based on its
    associations, even if those associations are irrelevant: e.g.,
    people are unwilling to eat fudge when it is shaped like feces
    (Rozin, Millman and Nemeroff, 1986); people are unwilling to walk on
    a glass platform, over a high drop, even though they know it is
    safe.[^31] Steven Pinker (2008, NYT) discusses examples of moral
    reasoning where people are sensitive to associations or symbolic
    considerations, independent of the consequences: a vegetarian who
    won't eat something which contains a drop of animal blood; disgust
    with incest, even when it could not lead to pregnancy; using an
    American flag to clean the bathroom; eating a dog who died from
    natural causes; active vs passive causing of death. The definitions
    used by Fodor and Pylyshyn are less applicable to this type of
    modularity.[^32]

-   **Two systems in judgment and decision-making.** Since the 1990s an
    important paradigm in the literature on judgment and decision-making
    has been based on the existence of two separate systems or cognitive
    processes: one is fast and associative (System 1); the other is slow
    and logical (System 2). This theory was promoted by Sloman, Evans,
    Stanovich, and West. The argument made in Sloman (1996) is based on
    how people solve logic puzzles: he says that, introspectively, we
    can sometimes distinguish between two responses to a question, one
    that "feels" right, and a second that we know to be true, and
    despite our knowledge we often retain the strong intuitive sense of
    the first, implying the existence of a separate "automatic" system
    of judgment.[^33] Subsequent discussion of the 2-system theory has
    mostly been about how to behaviourally distinguish the automatic and
    reflective responses to a situation: by cognitive load, by memory
    load, by observing response time, by imposing time limits. The
    results of this program, behaviourally distinguishing two responses,
    have been mixed, and many have argued that the 2-system model is a
    failure, or is impossible to test (Osman, et al.).

-   **Integration of information in Classical and Instrumental
    conditioning.** (\...)

-   **Tacit knowledge.** (\...)

-   **Subliminal influences.** (\...)

Top-down and cross-modal influences on perception \[should integrate this into sections above\]
-----------------------------------------------------------------------------------------------

-   We will be discussing how perception of one stimulus can be
    influenced by other stimuli. Different types of influence are often
    discussed: "cross-modal influences," "top-down influences," and
    "surround" or "adaptation" effects"[^34] To simplify I will describe
    all of these as "cross-modal influences."

-   My basic argument will be as follows: (1) there exist ubiquitous
    cross-modal effects, i.e. basic sensory processing is sensitive to
    all sorts of information. However (2) many of those effects are
    *coarse* - i.e., information is aggregated without modulating in a
    sophisticated way. For example, there are many findings that visual
    perception is influenced by sound stimuli, yet the same experiments
    show that sound stimuli influence visual perception even when the
    subject knows that it is irrelevant, even when the subject is trying
    to ignore it. The finding of cross-modal influence contradicts Fodor
    and Pylyshyn's postulate that sensory processing is encapsulated.
    However the second fact implies a modified version of encapsulation:
    sensory processing responds to outside influences only in a coarse,
    stylized way.

-   Before going to the evidence it's worth again remarking on the
    distinction between a *sensation* and the *value* being inferred.
    For example, a sound could affect either a subject's report about
    the color of the light that is hitting their eye (the sensation), or
    their report about the color of the object that they are looking at
    (the value). More examples of the distinction are given above in
    Table
    [\[tab:SensationValue\]](#tab:SensationValue){reference-type="ref"
    reference="tab:SensationValue"} above. Cross-modal effects on
    judgment of sensation are always non-normative, but cross-modal
    effects on perception may be either valid or invalid. It is rational
    to take into account all information in making inferences - so there
    are two types of departure from the rational benchmark in
    perception: sensitivity to something irrelevant, or insensitivity to
    something relevant.

-   **Breadth of cross-modal effects.**

    -   \(1) the McGurk and anti-McGurk effects; (2) the Stroop effect; (3)
        confusing motion of beeps and flashes; (4) confusing numerosity of beeps
        and flashes; (5) phoneme restoration; (6) assimilation to what you
        expect - proofreaders' errors; (7) Simon interference - response
        location & stimulus location; (8) cutaneous rabbit - effect of prior
        stimulus; (9) bistable figures & learned associations.

    -   "\[i\]n contrast with the modular view of perception, \... the
        accumulating evidence, especially over the last several years
        has revealed that visual perception can both quantitatively and
        qualitatively be modified by the input from other modalities."
        (Shams and Kim, 2010) \[This is in contrast to prior dogma that
        effects mostly flow *from* vision; also they report that some
        effects are very fast, implying not through top-down
        influences.\]

    -   **Sensitivity of sensation-judgments to external information.**
        It has often been remarked that people have poor ability to
        report their raw sensory judgments: Fodor (1982) says "one
        simply cannot see the world under its retinal projection and one
        has practically no access to the acoustics of utterances in
        languages that one speaks."[^35] The evidence for this consists
        in the well-known catalogue of sensory illusions: cases where it
        appears that one square is brighter than the other, redder than
        the other, bigger than the other, or oriented differently than
        the other, when they are both the same. Similar illusions exist
        for perception of sound, touch, smell or taste.

-   **Failure of cross-modal effects to modulate.**

    -   *however* those same demonstrations often show *illegitimate*
        inference. incorporation of irrelevant prior stimuli. A failure
        to modulate the effects.

        -   integration even when you know that the other stimuli are
            irrelevant (McGurk; beeps & flashes; ) .

        -   Overall story about integration: *coarse* cross-modal
            integrations.

        -   Pylyshyn & Fodor's examples: (i) parse language w/o
            semantics; (ii) .

-   **Top-down influences, and a misleading model of perception.**

    -   Here are some cases which are often described as illustrating
        "top down" influences on perception: (1) ; (2).

-   **Misc Notes**

    -   **Optimality of cross-modal effects.** Shams and Kim (2010) say
        that many cross-modal effects can be interpreted as Bayesian
        optimal. This is a response to prior literature which
        interpreted them as mistakes, miswirings. They base this on a
        model where people are trying to estimate sensations
        ($s_{1},\ldots,s_{n}$), and only get a noisy signal about each,
        so use covariance among the sensations. Experiment: you
        manipulate covariance, and see if people respond to this.
        **However** the earlier cross-modal experiments find
        effect-sizes way above the limits of discrimination, so can't be
        the same noise. Also the direction of the effects is wrong
        (always get assimilation, can't explain contrast).

    -   Question about the world: how much can be done with only local
        information? Findings in computer science that more context is
        needed (semantics needed for edge-detection; semantic needed for
        language parsing - homophones; ).

    -   \[Note that most artificial neural networks are *feed-foward*,
        though they are trained with back-propagation\]

    -   random-dot stereograms: "unambiguously demonstrated that
        stereoscopic depth could be computed in the absence of any
        identifiable objects, in the absence of any perspective, in the
        absence of any cues available to either eye alone." -
        contradicting Marr (?).[^36]

    -   Gilbert & Li (2013) discussion top-down effects (1) attention
        which increases the gain (contrast); (2) object/feature
        attention which increases receptivity to certain features; (3) .

    -   \[argument that we largely see what we expect, and just encode
        differences\]

    -   \[Papers which argue that cross-modal integration is *optimal* :
        ignore the illusion research, and present noisy stimuli; \]

A model of hierarchical integration.
------------------------------------

-   Suppose there are two systems (1 and 2), that they have private
    access to information $\alpha$ and $\beta$, respectively, and that
    they form inferences about $v$ in a sequential fashion:
    $$\xymatrix{
         \makeatletter
         \xydef@\xymatrixrowsep@{12px}
         \makeatother
    \ar[d]^{\alpha} & \, & \,\ar[d]^{\beta}\\
    *++[o][F]{1}\ar[rr]^{E[v|\alpha]} & \, & *++[o][F]{2}\ar[rr]^{E[v|E[v|\alpha],\beta]} &  & \,
    }$$ We are particularly interested in when this sequential
    aggregation of information is different from simultaneous
    aggregation of information, i.e. under what conditions does the
    following hold: $$E[v|E[v|\alpha],\beta]\neq E[v|\alpha,\beta].$$ In
    short, the answer is that there will be a bias whenever there is an
    interaction between $\alpha$ and $\beta$ in calculating
    $E[v|\alpha,\beta]$. For example suppose that $E[v|\alpha,\beta]$
    can be written as $f(g(\alpha)+h(\beta))$, then there will be no
    bias, i.e. $E[v|E[v|\alpha],\beta]=E[v|\alpha,\beta]$.

-   Here $\alpha$ represents the information that is private to the
    first module (System 1), i.e. information that is not accessible to
    the conscious brain, except indirectly, through $E[v|\alpha]$. Thus
    $\alpha$ has two interpretations: (1) as subliminal perception -
    features of the situation that we are not consciously aware of, such
    as quick exposure to words, or (2) as implicit knowledge - knowledge
    about the world that is used only in making pre-conscious
    inferences, and not available to higher-level systems.

-   Above, we made some observations about choice behavior in the
    laboratory: (1) high rate of instability; (2) sensitive to
    irrelevant framing details; (3) inconsistent with choices outside
    the laboratory; (4) biases often consistent with using valid but
    coarse decision rules (heuristics); (5) but people rarely make
    dominated choices. We also noted that these features are not
    particular to judgments of preference, but also apply to judgment of
    fact. Each of these features of choice can be explained by
    modularity in the judgment of value.

-   **Sequential integration of Gaussian signals.** Suppose that there
    is some unobserved vector of interest, $v$, and two vectors of
    signals, $x_{1}$ and $x_{2}$, with a joint normal distribution (we
    assume everything is mean zero for convenience) and the following
    covariance matrix (the lower half of the matrix is omitted):
    $$Cov\begin{pmatrix}x_{1}\\
    x_{2}\\
    v
    \end{pmatrix}=\begin{pmatrix}U_{1} & P & C_{1}\\
     & U_{2} & C_{2}\\
     &  & V
    \end{pmatrix}.$$ Then we can compare sequential and simultaneous
    integration of the two information vectors ($x_{1}$ and $x_{2}$).
    When aggregated simultaneously we have:
    $$v|x_{1},x_{2}=\begin{pmatrix}C_{1}' & C_{2}'\end{pmatrix}\begin{pmatrix}U_{1} & P\\
    P' & U_{2}
    \end{pmatrix}^{-1}\begin{pmatrix}x_{1}\\
    x_{2}
    \end{pmatrix}.$$ When aggregated sequentially we first calculate the
    posteriors over $v$ given $x_{1}$:
    $$\hat{v}_{1}=v|x_{1}=C_{1}'U_{1}^{-1}x_{1}.$$ This posterior is
    itself a Gaussian random variable, so we can now extend the
    covariance matrix, and therefore calculate the posterior given
    sequential aggregation, $v|\hat{v},x_{2}$ (the lower half of this
    covariance matrix is again omitted): **$$\begin{aligned}
    Cov\begin{pmatrix}x_{1}\\
    x_{2}\\
    v\\
    \hat{v}_{1}
    \end{pmatrix} & = & \begin{pmatrix}U_{1} & P & C_{1} & C_{1}\\
     & U_{2} & C_{2} & P'U_{1}^{-1}C_{1}\\
     &  & V & C_{1}'U_{1}^{-1}C_{1}\\
     &  &  & C_{1}'U_{1}^{-1}C_{1}
    \end{pmatrix}\\
    v|\hat{v}_{1},x_{2} & = & \begin{pmatrix}C_{1}'U_{1}^{-1}C_{1} & C_{2}'\end{pmatrix}\begin{pmatrix}C_{1}'U_{1}^{-1}C_{1} & C_{1}'U_{1}^{-1}P\\
    C_{1}'U_{1}^{-1}P & U_{2}
    \end{pmatrix}^{-1}\begin{pmatrix}C_{1}'U_{1}^{-1}x_{1}\\
    x_{2}
    \end{pmatrix}.\end{aligned}$$** Some observations:

    -   **Sequential aggregation is efficient if signals are
        independent.** If $x_{1}$ and $x_{2}$ are independent (i.e.,
        $P=0$), then the covariance of $x_{2}$ and $\hat{v}_{1}$ is
        zero, so we can get the following: $$\begin{aligned}
        v|\hat{v}_{1},x_{2} & = & C_{1}'U_{1}^{-1}C_{1}(C'_{1}U_{1}^{-1}C_{1})^{-1}C_{1}'U_{1}^{-1}x_{1}+C_{2}'U_{2}^{-1}x_{2}\\
         & = & C_{1}'U_{1}^{-1}x_{1}+C_{2}'U_{2}^{-1}x_{2}\\
         & = & v|x_{1},x_{2}.\end{aligned}$$ More generally, the two
        expressions will be equal whenever the conditional correlation
        between $\hat{v}_{1}$ and $x_{2}$ is zero.

    -   **Sequential aggregation is efficient if signals are**
        ***conditionally*** **independent \[unfinished\].** I.e., if
        $x_{1}|v$ is independent of $x_{2}|v$. This holds independently
        of the Gaussian assumption. (I conjecture this is true, but
        haven't proved it; it seems to be true for the Kalman filter).
        ($x_{1}$ and $x_{2}$ are conditionally independent if there is a
        zero in the corner of the inverse covariance matrix
        (conditioning on $v$). If $v$ is a scalar, this comes down to
        the condition $P=\sigma_{v}^{-2}C_{1}C_{2}'$. See scrap
        2015-04-14 for more notes.)

    -   **Numerical example where sequential aggregation fails.**
        Suppose that $x_{1}$, $x_{2}$ and $x_{3}$ are all correlated
        with $v$, but that $x_{2}$ and $x_{3}$ are in addition
        correlated with each other, in particular the covariance is as
        follows: $$Cov\begin{pmatrix}x_{1}\\
        x_{2}\\
        x_{3}\\
        v
        \end{pmatrix}=\begin{pmatrix}1 & 0 & 0 & 1\\
         & 2 & 1 & 1\\
         &  & 2 & 1\\
         &  &  & 2
        \end{pmatrix}.$$ Here $x_{1}$ and $x_{2}$ are independent, both
        correlated with $v$. $$\begin{aligned}
        v|x_{1},x_{2} & = & x_{1}+\frac{1}{2}x_{2}\\
        v|x_{1},x_{2},x_{3} & = & x_{1}+\frac{1}{3}x_{2}+\frac{1}{3}x_{3}\end{aligned}$$
        $$\begin{aligned}
        v|x_{1},x_{2},x_{3} & = & \begin{pmatrix}1 & 1 & 1\end{pmatrix}\begin{pmatrix}1 & 0 & 0\\
        0 & 2 & 1\\
        0 & 1 & 2
        \end{pmatrix}^{-1}\begin{pmatrix}x_{1}\\
        x_{2}\\
        x_{3}
        \end{pmatrix}\\
         & = & \begin{pmatrix}1 & 1 & 1\end{pmatrix}\frac{1}{3}\begin{pmatrix}3 & 0 & 0\\
        0 & 2 & -1\\
        0 & -1 & 2
        \end{pmatrix}\begin{pmatrix}x_{1}\\
        x_{2}\\
        x_{3}
        \end{pmatrix}\\
         & = & \frac{1}{3}\begin{pmatrix}3 & 1 & 1\end{pmatrix}\begin{pmatrix}x_{1}\\
        x_{2}\\
        x_{3}
        \end{pmatrix}\\
        \hat{v}_{1,2}=v|x_{1},x_{2} & = & \begin{pmatrix}1 & 1\end{pmatrix}\begin{pmatrix}1 & 0\\
        0 & 2
        \end{pmatrix}^{-1}\begin{pmatrix}x_{1}\\
        x_{2}
        \end{pmatrix}=\frac{1}{2}\begin{pmatrix}2 & 1\end{pmatrix}\begin{pmatrix}x_{1}\\
        x_{2}
        \end{pmatrix}=x_{1}+\frac{1}{2}x_{2}\\
        Cov\begin{pmatrix}x_{1}\\
        x_{2}\\
        x_{3}\\
        v\\
        \hat{v}
        \end{pmatrix} & = & \begin{pmatrix}1 & 0 & 0 & 1 & 1\\
         & 2 & 1 & 1 & 1\\
         &  & 2 & 1 & \frac{1}{2}\\
         &  &  & 2 & \frac{3}{2}\\
         &  &  &  & \frac{3}{2}
        \end{pmatrix}\\
        v|x_{3},\hat{v}_{1,2} & = & \begin{pmatrix}1 & \frac{3}{2}\end{pmatrix}\begin{pmatrix}2 & \frac{1}{2}\\
        \frac{1}{2} & \frac{3}{2}
        \end{pmatrix}^{-1}\begin{pmatrix}x_{3}\\
        \hat{v}
        \end{pmatrix}=\begin{pmatrix}1 & \frac{3}{2}\end{pmatrix}\frac{1}{3-\frac{1}{4}}\begin{pmatrix}\frac{3}{2} & -\frac{1}{2}\\
        -\frac{1}{2} & 2
        \end{pmatrix}\begin{pmatrix}x_{3}\\
        \hat{v}
        \end{pmatrix}\\
         & = & \frac{11}{12}\begin{pmatrix}\frac{3}{4} & \frac{5}{2}\end{pmatrix}\begin{pmatrix}x_{3}\\
        \hat{v}
        \end{pmatrix}=\frac{11}{16}x_{3}+\frac{55}{24}\hat{v}=\frac{11}{16}x_{3}+\frac{55}{24}x_{1}+\frac{55}{48}x_{2}\neq v|x_{1},x_{2},x_{3}.\end{aligned}$$
        \[need to double-check this, and give intuition for the nature
        of the bias.\]

Implications of hierarchical processing for economic decision-making.
---------------------------------------------------------------------

-   What implications does the hierarchy have outside the lab?

-   **Encapsulation of areas of expertise.** (buying and selling)

-   **Small details important.** If subtle details are important in
    influencing our decisions in the lab this implies that those details
    are important outside the lab. Details such as the order in which
    alternatives are listed, which alternative is the default, whether a
    situation is described as a loss or a gain, and the relative
    quantity of a good. This implies that good economic decision-making
    must rely on *smell*, or a careful evaluation of the subtle details
    of a case.

-   **Potential for persuasion through small details.** It implies that
    firms will wish to give their products features which the consumer
    knows to be irrelevant, but which have positive associations.

-   \[sensitivity to context; \]

-   **Decisions in unfamiliar contexts.** asdf

-   (point about budget constraints)

Implicit Knowledge
------------------

-   **Nutshell:** There is a long literature studying the degree of
    insight people have into their own judgments, however it has always
    been difficult to define implicit knowledge, and many experiments
    which seemed to demonstrate implicit knowledge have been found to be
    either fragile, or to admit an alternative explanation. I propose a
    new definition of implicit knowledge: knowledge is implicit if
    people are unable to combine it with other information. Consider
    Brunswik's lens model of judgment: $$\xymatrix{ & x_{1}\ar[dr]\\
    v\ar[ur]\ar[r]\ar[dr] & x_{2}\ar[r] & \hat{v}(x_{1},x_{2},x_{3})\\
     & x_{3}\ar[ur]
    }$$ A person uses the cues $x_{1},x_{2},x_{3}$ to form a judgment
    about the unobserved value $v$. Suppose that the decision-maker does
    not have insight into the function $\hat{v}(x_{1},x_{2},x_{3})$,
    i.e. they do not know the weights used with respect to each cue.
    Then we should expect predictable mistakes if we ask the
    decision-maker to reinterpret the cues, e.g. if we provide them
    information that (1) the cue $x_{1}$ is random, and so should be
    ignored; (2) the cues $x_{1}$ and $x_{3}$ have been swapped; (3) the
    cue $x_{1}$ has been artificially increased by a certain amount, so
    its weight should be reduced.

-   There is a longer discussion of almost all the material in this
    section in my 2015 paper "Implicit Knowledge Revealed in Choice."

-   **The intuitive case for tacit knowledge.** Here are some
    observations which could give us ground for suspecting that implicit
    knowledge is important.

    1.  **difficulty in explaining our judgments.** There are many
        occasions when we have difficulty in explaining *why* we made a
        certain judgment, though we are confident that is correct, such
        as explaining why we think that a certain photo looks like your
        cousin; why one barn looks father off than another; why an
        ungrammatical sentence is ungrammatical.

    2.  **history of human sciences.** The history of attempts to
        explicitly write down certain parts of our knowledge: linguists
        have worked for centuries on finding the rules which make a
        sentence grammatical;[^37] computer scientists have worked for
        decades on analyzing pictures and sound, and they still -
        mostly - fall short of the ability of a human child.[^38]

    3.  **Moravec's paradox in artificial intelligence.** "easy things
        are hard; hard things are easy."

    4.  **how little we are helped by logic and science.** Some
        observations about everyday life: people who are good at certain
        activities, are often bad at discussing them. A volleyball
        player isn't helped much by studying physics; successful
        businesspeople are often pretty bad at logic puzzles.

-   **Related issues.** There are a number of concepts which are related
    to implicit knowledge, but distinct. I will describe some of these
    in order to leave them aside. First, there is the concept of an
    implicit or unconscious *motivation* or desire; this is a separate
    issue from knowledge. Second, there is subliminal *perception*:
    whether our responses can be influenced by sensations that we are
    not consciously aware of, for example a stimulus which is flashed
    very quickly.[^39] Third, there is the question of the degree to
    which our memory is *coarse*, for example remembering a general
    impression, without remembering specific episodes; this can occur
    without knowledge being implicit.[^40] Fourth, whether the word
    "knowledge" should be used regarding a non-conscious process - this
    debate seems semantic, and I will define below the sense in which I
    use the word.[^41] Fifth, the distinction between knowing some
    proposition, and knowing the propositions which logically are
    implied by it - this issue is related but not central to the
    examples we are interested in.[^42] Sixth, whether people
    systematically underestimate the accuracy of their intuitive
    judgments. This finding, if true, goes beyond implicit knowledge:
    people could have implicit knowledge which is expressed in their
    judgments, but also be aware that those judgments incorporate
    knowledge, and therefore not underestimate the accuracy of those
    judgments.[^43] Seventh, the distinction between knowing *that* and
    knowing *how*, e.g. between knowing that Bastille day is the 14th of
    July, and knowing how to ride a bicycle. In this paper knowledge
    will always be tested with judgments of fact.

-   Most laboratory test of implicit knowledge give subjects practice at
    a task, until their behaviour reveals that they have learned some
    pattern about the task, and then to ask subjects whether they are
    aware of that pattern.[^44] Positive results have been found many
    times, interpreted as proving the existence of implicit knowledge.
    However these results have been repeatedly reinterpreted, for some
    interesting reasons.

-   **Laboratory tests of implicit knowledge.** The most common test for
    implicitness is simply to ask people to explain what affects their
    judgments, and compare the answers with what actually affects their
    judgments. A number of studies have found a systematic difference:
    Greenspoon (1955) found that subjects' verbal behaviour could be
    influenced by reinforcement without awareness. Slovic et al. (1972)
    found that stockbrokers, when asked to weight the importance of cues
    they used in picking stocks, gave weights that were a poor
    approximation to the way they actually use those cues. Reber (1989)
    taught subjects to recognize when nonsense words satisfied a certain
    rule (a Markov transition process among a set of letters), and found
    that they had little insight into the rule that they had learned.
    Bechara, Tranel, Damasio and Damasio (1996) gave subjects experience
    with a task involving choosing cards, and found that, although
    decisions eventually reflected learning about the task, subjects'
    autonomic responses (skin conductance) seemed to respond even more
    quickly.[^45] Evans et. al. (2003) taught subjects to predict an
    outcome on the basis on a set of cues, and found that subjects were
    poor at ranking the importance of the cues they were using.

-   **Criticism of these tests.** However the protocols used in all
    these experiments have important interpretation problems pointed out
    by Shanks and St John (1994) (and reiterated in Newell and Shanks,
    2014). First, the tests for implicit and explicit knowledge often
    test for different kinds of knowledge. For example, subjects may
    perform well in recognizing words in Reber's artificial grammar
    experiments simply because they have remembered the training set,
    and use simple extrapolation, without recognizing a rule which
    connects them. Such knowledge could be said to be "implicit"
    knowledge of the rule, but this would be in a much weaker sense that
    is normally meant by implicit knowledge.[^46] Second, the tests for
    explicit knowledge are often less sensitive than the test for
    implicit knowledge, so comparison of correlations with true value
    could prejudice the conclusion against implicit knowledge. The
    existing state of the literature is summarized in Newell and
    Shanks' (2014) review, and the commentaries published in the same
    issue of that journal.

-   **Alternative identifcation of implicit knowledge.** These
    considerations suggest a different definition and test for implicit
    knowledge. A definition:

    > *A judgment depends on implicit knowledge if the decision-maker
    > cannot combine the judgment with information about changes in the
    > cues.*

-   **Proposed tests for implicit knowledge.**

    -   Test for implicit knowledge in clinical judgment.

    -   Test for implicit knowledge of grammar.

Extra Notes on Implicit Knowledge
---------------------------------

-   Typically evidence has been to get at $\boxed{1}$: either by (a)
    introspection - many quotes; (b) fast or inattentive response. -
    This is independent of whether (2) has access to inputs of (1).

    -   Suggestion: we test just the output of $\boxed{2}$, but we get
        at it indirectly:

        -   \(a) ask people to report the cues themselves can predict direction by
            hypothesis about what $\boxed{1}$ is calculating

        -   \(b) ask people to ignore a cue

        -   \(c) unusual cue.

-   Conclusions about the internal structure

    -   Sensory information *not passed to conscious processing* -
        biases in preditable direction: sensory areas are inferring
        object colour, size, distance, density.

Appendix: Notes on a General Model
==================================

1.  Suppose $\frac{d\hat{x}_{1}}{dx_{2}}>0$, then (1) direct path to
    neither; (2) must have common node; (3) must enter common node with
    same sign.

    -   sensory biases.

2.  Suppose $\frac{d\hat{v}}{dx_{2}}>0$, then correlated.

    -   use it as a proxy.

3.  Suppose $\frac{d\hat{v}}{dx_{2}}>0$, even when $x_{2}$ known to be
    irrelevant (and no direct path to $x_{2}$)

    -   Then

4.  Suppose $\frac{d\hat{v}}{dx_{2}}>0$, even when $x_{2}$ known to be
    irrelevant (and direct path to $x_{2}$).

    -   Then .

Bibliography
============

\bibliographystyle{plainnat}

[^1]: "Predictive coding" models add the assumption that early nodes
    receive information from later nodes, which update expectations*,*
    and so the information sent back up the hierarchy can be interpreted
    as differences from expectations. Another important difference is
    that coding models usually consider a linear process (sensation,
    coding, then decoding), while many of the implications of the
    hierarchical model comes from the assumption that information flows
    in parallel channels, and this gives rise to the characteristic
    biases.

[^2]: See Gregory (2006), Flanagan (2008) and Brayanov & Smith (2010) on
    "anti-Bayesian" illusions.

[^3]: Formally, if all variables are Gaussian, then
    $\frac{d\hat{v}_{1}}{dx_{2}}\propto\mbox{corr}(v_{1},v_{2})-\mbox{corr}(e_{1},e_{2})$,
    i.e. the effect of a neighboring stimulus will be negative if the
    correlation of noise is greater than the correlation of values, and
    positive if the opposite.

[^4]: This is assuming that $\frac{d\hat{s}_{i}(\hat{v})}{d\hat{v}}$ has
    the same sign as $\frac{d\hat{v}(s_{i})}{ds_{i}}$, which will be
    true in the Gaussian model below, and seems to be generally true if
    $\hat{v}(\mathbf{s})$ satisfies the monotone likelihood ratio (MLRP)
    in $\hat{v}$ and $s_{i}$. Note also that the second term will become
    equal to $\propto\frac{Cov(v,s_{2}|s_{-2})}{Cov(v,s_{1}|s_{-1})}$,
    where $Cov(v,s_{2}|s_{-2})$ represents the covariance of $v$ with
    $s_{2}$, conditional on all the other sensations.

[^5]: https://youtu.be/G-lN8vWm3m0?t=36s

[^6]: When estimating a categorical varaible, such as the syllable being
    spoken, instead of treating $v$ and $s$ as real numbers, they could
    be a vector of dummy variables, or a simplex.

[^7]: \[The fundamental difference from efficient coding theories here
    is that the intermediate stage is implementing *inference* instead
    of *compression*. In both models $\hat{s}$ is inferred from a coarse
    signal of $s$, call it $c(s)$. The two theories just differ on what
    determines $c(s)$, whether $c(s)$ is designed to minimize
    $\sum_{i}(v_{i}-\hat{v}_{i})^{2}$ (inference), or to minimize
    $\sum_{i}(s_{i}-\hat{s}_{i})^{2}$ (coding, compression). \]

[^8]: The puzzle is discussed in Gregory (2006) (who calls it
    "anti-Bayesian"), Schwartz, Hsu & Dayan (2007), Series, Stocker &
    Simoncelli (2009), Brayanov & Smith (2010) - who also call it
    "anti-Bayesian".

[^9]: \[Could mention Series-style experiments which get assimilation\]

[^10]: A nice property of the Gaussian distribution is that the whole of
    the posterior can be summarized just by the mean (i.e., the variance
    of the posterior is independent of the data observed), so we just
    work with expectations.

[^11]: See also Stewart (2006) and Webster (2011).

[^12]: Sequential contrast effects are also called "after-effects" or
    "adaptation effects."

[^13]: For example in Chalk, Seitz, Series (2012), they show subjects
    faint dots in motion, and find that prior experience with dots
    biases judgments in an *assimilatory* direction. Petzschner et al.
    (2015) reports assimilation effects in four domains: estimation of
    distance, angle, time, and length. All of the experiments she
    reports are from reproduction tasks, meaning that subjects are shown
    a stimulus, and then must reproduce graphically, or estimate
    numerically, its magnitude. For example in Petzschner et al. (2011)
    subjects use a 3D computer game, and must reproduce, by moving
    through the world, an angle or a distance shown to them previously.
    Again, in these cases the idiosyncratic component of error seems
    high.

[^14]: "it now seems clear that the fatigue of neuronal populations
    falls short as an explanation for after-effects."

[^15]: http://en.wikipedia.org/wiki/Perceived\_visual\_angle\#The\_size.E2.80.93distance\_paradox

[^16]: The Gaussian derivations above assumed that $\mu_{v}=\mu_{s}=0$.
    More generally we can write $\hat{v}=\mu_{v}+C'U^{-1}(s-\mu_{s})$,
    which directly implies the comparative statics in the text.

[^17]: Also some kind of diminishing sensitivity seems to occur at least
    in perceptual judgment (Weber's law), and in decision-making.

[^18]: It's not clear to me who first documented this pattern of lateral
    inhibition: some people say Baumgartner (1960), or Ratliff and
    Hartline (1959), or Hubel and Wiesel.

[^19]: Simoncelli (2003) reviews empirical evidence for efficient coding
    by neurons.

[^20]: There is a long literature which assumes that the brain makes a
    systematic error when decoding the signals, i.e., treating the
    signals as if they were raw data and had not been encoded. This will
    of course generate biases exactly following the encoding function. I
    don't discuss this as a candidate explanation for biases, but it is
    discussed in Series, Stocker & Simoncelli (2009) who call it
    "unaware decoding" and Schwartz, Hsu & Dayan (2007) who call it a
    "coding catastrophe."

[^21]: To see this, suppose that each signal generates a degenerate
    posterior, $V[E[s|c]|s]=0$. Then, if there is an unambiguous
    contrast effect, the variance of the posteriors will be greater than
    the variance of $s$. Things will be even worse if the posteriors are
    non-degenerate.

[^22]: Sims (2003) discusses assumptions under which this would
    represent the optimal signal.

[^23]: http://www.sas.upenn.edu/\~astocker/lab/publications-files/journals/NN2015/Wei\_Stocker2015b.pdf

[^24]: In fact, this direct interpretation does fit some observed
    features in choice, see Cunningham (2012).

[^25]: It's worth noting that humans can also beat computers in making
    inferences about tasks that we could not have evolved to do, such as
    reading handwriting or playing Go.

[^26]: E.g., going through the visual cortex, from the back towards the
    front of the brain, one finds neurons selective for being bright,
    bring relatively bright, being a vertical line, being a circle,
    being a face, and being a cousin's face. More generally there exists
    some correspondence between regions in the brain and types of
    cognition, using evidence from lesions, imaging, and single-neuron
    recording - though note that Elman, Bates, et al. (1996) "Rethinking
    Innateness" argue that double-dissasociations are rarely clean, and
    so evidence for localisation has been exaggerated.

[^27]: See Pylyshyn (1980), [@pylyshyn1984computation] and
    [@pylyshyn1999vision]. David Marr's 1982 book, *Vision*, made a
    similar case: that visual inference seems to proceed in a series of
    stages, first identifying gross features such as edges, then
    constructing a $2\frac{1}{2}$D representation, then a 3D
    representation.

[^28]: Pylyshyn's arguments seem to remain persuasive: Feldman (2013),
    defending Bayesian models of perception, concedes that "there is a
    great deal of evidence (see Pylyshyn, 1999) that perception is
    singularly uninfluenced by certain kinds of knowledge, which at the
    very least suggests that the Bayesian model must be limited in scope
    to an encapsulated perception module walled off from information
    that an all-embracing Bayesian account would deem relevant."

[^29]: He has 9 total criteria: domain specificity, mandatory operation,
    limited access to internal representations, speed, informational
    encapsulation, shallow outputs, fixed neural architecture,
    characteristic breakdowns, and characteristic ontogeny.

[^30]: The original Wason card task is this: Suppose you see four cards,
    one red, one brown, one showing "3", and one showing "8". Which
    cards do you need to turn over to test whether all even-numbered
    cards have brown on their opposite side? Many people give a wrong
    answer. The transposed version is: Suppose you observe four people,
    one drinking gin, one drinking lemonade, one who is 30, and one who
    is 15. Which information would you need to check to see if anybody
    under 21 is drinking alcohol?

[^31]: Gendler (2008) "Alief and Belief" in the *Journal of Philosophy*.
    She also describes a series other experiments by Rozin: "subjects
    are reluctant to drink from a glass of juice in which a completely
    sterilized dead cockroach has been stirred, hesitant to wear a
    laundered shirt that has been previously worn by someone they
    dislike, and loath to eat soup from a brand-new bedpan. They are
    disinclined to put their mouths on a piece of newly purchased
    vomit-shaped rubber (though perfectly willing to do so with sink
    stopper of similar size and material), averse to eating fudge that
    has been formed into the shape of dog feces, and far less accurate
    in throwing darts at pictures of faces of people they like than at
    neutral faces \... \[subjects\] showed a reluctance to consume sugar
    from \[a\] 'cyanide' labeled bottle."

[^32]: In fact it becomes difficult to define - e.g., Barrett & Kurzban
    (2006) argue that modules need be neither innate, automatic, or
    informationally encapsulated.

[^33]: "A reasoning problem satisfies Criterion S if it causes people to
    simultaneously believe two contradictory responses. By 'believe' I
    mean a propensity, a feeling or conviction that a response is
    appropriate even if it is not strong enough to be acted on."

[^34]: For example, perception of a sound could be influenced by (a) a
    prior sound; (b) a visual stimuli; or (c) expectations of what sound
    will be played.

[^35]: Helmholtz says "we are not in the habit of observing our
    sensations accurately, except as they are useful in enabling us to
    recognize external objects. On the contrary, we are wont to
    disregard all those parts of the sensations that are of no
    importance so far as external objects are concerned. Thus in most
    cases some special assistance and training are needed in order to
    observe these latter subjective sensations. \... For instance, the
    phenomena of the blind spot were discovered by Mariotte from
    theoretical considerations."

[^36]: In the 1950s, working at Bell Labs, Bela Julesz was working on
    detecting patterns in the output of random number generators by
    printing the output in a matrix. He discovered that, if two variants
    of the image were shown, one to each eye, with a square offset in
    one of the two, the viewer would perceive the square as floating in
    front of the background.

[^37]: Chomsky (1965) said "Obviously, every speaker of a language has
    mastered and internalized a generative grammar that expresses his
    knowledge of his language. This is not to say that he is aware of
    the rules of the grammar or even that he can become aware of them."

[^38]: This fact is sometimes described as Moravec's paradox: "it is
    comparatively easy to make computers exhibit adult level performance
    on intelligence tests or playing checkers, and difficult or
    impossible to give them the skills of a one-year-old when it comes
    to perception and mobility." The recent progress in machine learning
    is not inconsistent with the importance of implicit knowledge: we
    have found that it is easier to let the computers learn these facts
    themselves than for us to teach them.

[^39]: Newell & Shanks (2014) argue that the evidence for subliminal
    influences is fairly weak.

[^40]: Descartes said that a person's childhood experience may "remain
    imprinted on his brain to the end of his life \... \[without\] \...
    any memory remaining of it afterwards." Leibniz argued that we have
    ideas of which we are not consciously aware, but which do influence
    behavior, and that we have "remaining effects of former impressions
    without remembering them." Ellenberger (1970) says that these are
    referring to "implicit knowledge," but this is a much weaker
    concept.

[^41]: This position, that it is not knowledge if it is not conscious,
    is made by Gilbert Ryle, John Searle, M. R. Bennett and P.M.S.
    Hacker.

[^42]: Daniel Dennett defines "implicit knowledge" in this way, but this
    is obviously something distinct from what we are interested in here
    ("let us have it that for information to be represented implicitly,
    we shall mean that it is implied logically by something that is
    stored explicitly.").

[^43]: This argument has been made by Bechara, Tranel, Damasio and
    Damasio (1996) and Dienes and Seth (2009), for example by asking
    subjects both to guess at the answer, and to state their confidence
    in that guess. Sometimes it has been found that people are more
    accurate than they realize. Newell and Shanks (2014) discuss
    critically evidence for these experiments.

[^44]: Cleeremans (2003) says there are three main paradigms: (1)
    Reber's artificial grammar learning (see below); (2) dynamic system
    control (the "sugar factory") task; (3) sequence learning - where
    subjects learn sequential correlations.

[^45]: They say "healthy participants show a 'stress' reaction to
    hovering over the bad decks after only 10 trials, long before
    conscious sensation that the decks are bad."

[^46]: Quine (1972) also discusses this point.
