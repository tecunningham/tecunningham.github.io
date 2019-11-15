---
layout: post
title: Hierarchical Integration of Information
output: pdf_document
geometry: margin=1in
header-includes:
     - \usepackage{xypic}
---


<!--

Note: I moved the specific discussion of sensations to 'hierarchy-sensations'

Note: difficult to get encircled numbers. See following references:

1. https://tex.stackexchange.com/questions/7032/good-way-to-make-textcircled-numbers
2. in mathjax:  https://tex.stackexchange.com/questions/229005/how-do-i-encircle-text-like-make-a-circle-around-it
-->

# Introduction

I will argue that weaknesses in human perception and judgment (illusions, biases, inconsistencies) can be understood as products of the *hierarchical* way in which the brain processes information.

The diagrams below shows the basic idea. The first diagram represents a model of judgment in which all information is integrated optimally: there is some fact about the world, $v$, a set of observations $x_1,\ldots,x_7$ which relate to that fact, and finally the conscious brain, $\xymatrix{*+[o][F-]{c}}$, which has access to all those observations, and forms an inference about $v$ from them. Next I show the hierchical model in which there are various intermediary aggregations of information, drawing on inputs that are not themselves directly accessible to the conscious brain.

$$\begin{matrix}\xymatrix@R-2pc{
& \boxed{x_{1}}\ar[dddr] \\
& \boxed{x_{2}}\ar[ddr] \\
& \boxed{x_{3}}\ar[dr] \\
v\ar[uuur]\ar[uur]\ar[ur]\ar[r]\ar[dr]\ar[ddr]\ar[dddr] & \boxed{x_{4}}\ar[r] & *+[o][F-]{c} \\
& \boxed{x_{5}}\ar[ur]   \\
& \boxed{x_{6}}\ar[uur] \\
& \boxed{x_{7}}\ar[uuur] \\
} & & & &  \xymatrix@R-2pc{
& \boxed{x_{1}}\ar[dr]\\
& \boxed{x_{2}}\ar[r] & \circ \ar[dr]\\
& \boxed{x_{3}}\ar[rr] &  & \circ \ar[dr]\\
v\ar[uuur]\ar[uur]\ar[ur]\ar[r]\ar[dr]\ar[ddr]\ar[dddr] &  \boxed{x_{4}}\ar[rru] &  &  & *+[o][F-]{c}\\
& \boxed{x_{5}}\ar[r] & \circ \ar[urr]\\
& \boxed{x_{6}}\ar[ur]\\
& \boxed{x_{7}}\ar[uuurrr]
} \\
\text{perfect integration} & & & &  \text{hierarchical integration}
\end{matrix}$$

The intermediate nodes can be thought of as automatic unconscious judgments -- e.g. judgments about the distance of an object, the age of a person, or the value of a bottle of wine. The conscious brain only has access to those intermediate judgments, not the raw data, and this fact causes the many inconsistencies we observe in human judgment.

The setup can be modelled formally such that assumptions about the structure of the hierarchy -- about which nodes are connected to which -- generate predictions about what biases will be exhibited. In principle the theory can explain virtually any pattern of biases, but I will argue that quite simple assumptions about the structure of the hierarchy can explain and unify a broad range of observed biases.

A very brief survey of applications of the theory:

**APPLICATIONS IN PERCEPTION**

1. **Sensitivity to presentation.** Peoples' ability to recognize a pattern will be sensitive to the presentation.
1. **Cross-modal influences on judgment of sensation.** When judging a direct sensation (the brightness of a light, pressure from an object) people make mistakes, and are influenced by other sensations, and the direction of the influence is predictable from an assumption that the hierarchy is inferring properties of the world.
2. **Contrast and assimilation effects.** Sometimes we find contrast effects in perception (an object appears lighter when placed next to a darker object, etc.), sometimes assimilation effects - the opposite. In the model above, contrast effects are predicted when there's relatively higher autocorrelation in signal than in noise, and assimilation otherwise.
3. **Reproduction.** People find it easy to recognize patterns but hard to reproduce them -- e.g. to paint a picture, to transcribe a melody. This is consistent with the model above insofar as the recognition is done pre-consciously, and certain biases in reproduction are predictable: that people underestimate the darkness of shadows.


**APPLICATIONS IN JUDGMENT**

1. **Influence of irrelevant cues.** A common pattern is that people are influenced by cues that they know to be irrelevant -- i.e., when told to ignore some fact they will still be moved by it. This occurs when cues are integrated into preconscious judgments.
3. **Hypothetical questions.** People will be unable to accurately answer hypothetical questions about their own judgments: e.g., would you value this bottle of whisky the same, if it had a different price on it?
4. **Joint evaluation.** When two judgments are being made at the same time -- e.g., two items being valued -- then .


<!-- The hierarchical model, illustrated on the right, implies that the conscious brain,  $\xymatrix{*+[o][F-]{c}}$, has access mainly to pre-interpreted information, and limited insight into the raw material - the stimuli and learned regularities - from which our judgments are formed. This structure also implies the existence of certain characteristic biases, which occur when one branch of the hierarchy does not have access to relevant information available to another branch. I will argue that many of the biases we observe in perception, judgment, and decision-making have explanations which fit this model -- i.e., they are side-effects of the pre-processing of information by the brain. Some of the points are not novel, just formalized into my hierarchical framework. I think the most important contribution is to show an isomorphism between the structure of the hierarchy and the nature of the biases, and the consequence that the hierarchy in the brain can be systematically mapped by documenting the biases in judgment.

Some observations to serve as motivation: everyday experience suggests that we have shallow insight into our own judgments. We are often poor judges of our own sensory stimulation - which light is brighter, or which sound was louder - yet we are extremely good at using that information in recognizing objects - suggesting that we are separated from direct sensory stimulation by an intermediary which interprets it for us. Turning to abstract judgments, when we are asked to explain our reasons for making a certain judgment we often struggle, even in cases where we are confident that our judgment is correct: explaining why some object looks far off, why some face looks like your cousin, why some sentence is not grammatical, or why one restaurant seems better than another. The hierarchical model says that we can have confidence in our judgments without much insight because many inferences are performed pre-consciously.

This analysis has simple implications for behaviour. Suppose that the distance of an object is calculated by a pre-conscious process, using a limited set of cues. In some cases there will be additional information that is relevant in calculating distance which is accessible to the conscious brain but which bypasses the pre-conscious process. Then we should expect that extra information to be imperfectly integrated with the previous inputs. Suppose there is some cue used by a pre-conscious process -- the colour of an object -- but the decision-maker is told that this cue is not relevant in the current case; then I predict that the decision-maker's best estimate of distance will still depend on that cue, in spite of their knowledge that it is irrelevant, because the pre-conscious estimate of distance depends on that cue, and the pre-conscious estimate remains an informative proxy for distance. The direction of the bias can, in addition, be predicted, based on the empirical relationship between that cue and distance. For example, if the light received from more distant objects tend to be bluer (which is true), then we would predict a bias such that people over-estimate the distances of objects that they know to be blue (which is also true).

I discuss connections to various related threads of literature below: (1) the debate over top-down vs bottom-up influences in perception; (2) theories of modularity and massive modularity; (3) theories of efficient coding and predictive coding; (4) the debate over the existence of tacit knowledge; (5) the debate over whether perception should be described as Bayesian inference; (6) inattention models of decision-making in economics; (7) the 'heuristics and biases' and 'dual systems' paradigms in judgment and decision-making; and (8) the realism vs anti-realism debate in philosophy.

# Sketch of Applications

## Sensory biases

When people are asked to directly judge some stimulus - e.g. which of two lights is brighter, which shape is larger - they are often influenced by other irrelevant stimuli. For example judgment of brightness may be influenced by size, judgment of timing may be influenced by sound, etc.. The hierarchical model provides an explanation: the conscious brain has access only to pre-processed information, consisting of inferences about the world, the raw stimuli are not directly accessible. When asked to estimate the raw stimuli, the conscious brain must infer them from the reports generated by intermediary processes. In our diagram, suppose that some set of sensory stimuli $x_{1},\ldots,x_{n}$ are used by a pre-conscious node to infer some value $v$, generating $\hat{v}=E[v|x_{1},\ldots,x_{n}]$, and suppose that the conscious brain has access only to the inference, $\hat{v}$ as in this diagram:

$$\xymatrix{
\,                      & \boxed{x_{1}}\ar[dr]\\
\boxed{v}\ar[ur]\ar[dr] &                 & *++[o][F-]{\hat{v}}\ar[r] & *++[o][F-]{c}\\                     & \boxed{x_{2}}\ar[ur]
}$$

When the conscious brain needs to form a judgment of a sensory stimulus, $x_{1}$, then its best guess will be simply $$E[x_{1}|\hat{v}]=E[x_{1}|E[v|x_{1},x_{2}]].$$ This shows how judgment of one stimulus, $x_{1}$, can be influenced by some other stimulus, $x_{2}$ -- for example, judgment of size is influenced by color, motion by sound, etc. I.e., $\frac{d\hat{x_2}}{dx_1}$. These effects are sometimes called "cross-modal" influences on perception. The model predicts certain features regarding these effects:

1.  If we know what feature, $v$, is being inferred by the brain, and we know the direction of the correlations between $v,x_{1}$, and $x_{2}$, then we can predict the direction of the bias ($\frac{d\hat{x}_{1}}{dx_{2}}\propto\frac{d\hat{v}/dx_{1}}{d\hat{v}/dx_{2}}\propto\frac{dx_{1}/dv}{dx_{2}/dv}$). This can account for the intuitive nature of many of the biases: when people hear more beeps then they report seeing more flashes, and vice versa, because some internal process has inferred them to be generated by the same process.

2.  However there are some well-known apparent paradoxes. These can be reconciled with the hierarchical model by changing the assumption about which value, $v$, is being inferred, and the theory will make additional testable predictions. In the *size-weight* illusion people systematically underestimate the weight of large objects, and vice versa; this is consistent with a hierarchical model if our intermediate processes infer the *density* of an object. Then when we are asked about the weight of an object, we back-infer from our beliefs about its density. Similar in the *size-distance* illusion, people overestimate the distance of smaller objects, and vice versa [check].

3.  In many cases the magnitude of a bias is diminished when judgment is measured by physical response rather than by verbal report. For example, when asked about the weight of an object that they can hold, people are biased by its size (larger objects are judged to be lighter), but when asked to lift the object, their grasp seems to correctly anticipate the weight of the object, and not be biased by the object's size.

The most common formal theory account of sensory biases is based on "coding" of stimulus data: as in the hierarchical model, raw stimuli are not directly accessible to the conscious process, instead they are inferred from intermediate representations. The difference is that coding theories assume that the intermediate nodes *compress* the data from the stimuli, while in the hierarchical theory they perform *inferences* about properties of the world. I discuss in detail how to distinguish predictions of the two models.[^1]

## Contrast and Assimilation effects

Probably the most consistent and widespread sensory bias is a *contrast* effect: the apparent intensity of a stimulus is negatively affected by its neighbors - a light seems darker when its neighbors become brighter, a sound seems louder when its neighbors become softer, etc.. The effect arises both from neighbors in time and in space, and affects all sorts of sensory judgments (brightness, colour, contrast, volume, pitch, size, orientation). This effect has been considered something of a puzzle for Bayesian or signal-processing models of perception because, although it is possible to rationalize a spillover effect from neighboring stimuli by assuming that people receive only noisy signals of stimuli, such an assumption predicts an effect in the *opposite* direction: i.e., if a stimulus' neighbor is bright then, under reasonable assumptions, it would seem to imply that the stimulus itself is probably brighter, all else equal.[^2]

Adelson (1993) gives a neat explanation of why contrast effects occur in perception of lightness, and his explanation can be easily formalized in a hierarchical model. The crucial assumptions being that (1) intermediate nodes infer the properties of objects in the world, not properties of the stimuli; and (2) the relationship between stimuli and properties of the world fluctuates with the environment. The fluctuating relationship implies that sensory organs need to be continuously recalibrated, and this recalibration generates a contrast effect. Consider the following diagram of information flow: suppose that two stimuli, $x_{1}$ and $x_{2}$, are functions of two values ($v_{1}$ and $v_{2}$), but with noise ($e_{1}$ and $e_{2}$). We assume that, in the hierarchy, separate nodes infer $v_{1}$ and $v_{2}$ from $x_{1}$ and $x_{2}$, and it will be rational for each inference to take into account both (i.e., $\hat{v}_{1}$ will be a function of both $x_{1}$ and $x_{2}$) as long as there is a correlation either between $v_{1}$ and $v_{2}$, or between $e_{1}$ and $e_{2}$. Finally, if the correlation between $e_{1}$ and $e_{2}$ is higher than that between $v_{1}$ and $v_{2}$, then a higher $x_{2}$ will imply a *lower* $\hat{v}_{1}$, i.e. this model will generate the contrast effect so often observed.[^3]

$$\xymatrix@R-2pc{
\boxed{e_{1}}\ar[dr]\\
\boxed{v_{1}}\ar[r] & \boxed{x_{1}}\ar[ddr]\ar[r] & *++[o][F-]{v_1}\ar[dr]\\                 &                             &                  & *++[o][F-]{c}\\
\boxed{v_{2}}\ar[r] & \boxed{x_{2}}\ar[uur]\ar[r] & *++[o][F-]{v_2}\ar[ur]\\
\boxed{e_{2}}\ar[ur]
}$$

Intuitively this model says contrast effects occur because of noise in the world, requiring our perceptual systems to continuously recalibrate. To infer the lightness of an object we need to take into account the illumination, implying that when an object has a bright neighbor the brightness will cause us to update positively about the illumination, and so update negatively about the lightness of the original stimulus, i.e. a contrast effect. Similarly with perception of size, contrast, volume, pitch, and orientation, each inference requires calibration, and neighboring stimuli will cause adjustments of the calibration, giving rise to contrast effects.

Evidence for this interpretation comes from the prediction that contrast effects will occur only among pairs of stimuli which the brain expects to be affected by a common source of noise. Adelson (1993) showed that lightness contrast effects only occur between objects which appear to be illuminated by the same light source, and I outline evidence that other types of contrast effects have a similar pattern.

Finally the basic model can explain contrast effects in judgments about the world (about $v_{1}$ and $v_{2}$), but not in judgments of sensations ($x_{1}$ and $x_{2}$), although both occur. I show later how a slight enrichment of the model can explain both.

## Biases in judgment about the world

The two previous applications referred just to biases in judgments of direct sensory stimuli -- brightness, pressure, loudness. The same model can also explain why we have biases in judgments about features of the world, such as distance, weight, or colour. Some examples of such biases are (1) judging colder objects to be heavier; (2) judging bluer objects to be more distant; (3) judging objects to be smaller when surrounded by larger objects.

Here the logic is that relevant information is aggregated in different channels.

-   (E.g., fog & distance; e.g. size-weight )

$$\xymatrix{
\boxed{v_{1}}\ar[r]\ar[ddr] & \boxed{x_{1}}\ar[dr]\\
                          &                    & *++[o][F-]{v_1}\ar[r] & *++[o][F-]{c}\\
\boxed{v_{2}}\ar[r]\ar[uur] & \boxed{x_{2}}\ar[ur]
}$$

## Biases in Judgment and Decision-Making

Violations of consistency are ubiquitous in laboratory tests of judgment. For example the answer to a question often depends on how it is phrased. In a hierarchical model these biases can be interpreted as due to inferences that bubble up in separate streams, and so fail to share relevant information.

A basic model is as follows:

$$\xymatrix@R-2pc{
 & \boxed{x_{1}}\ar[rrd]\\
 &  &  & *++[o][F-]{v}\ar[ddr]\\
\boxed{v}\ar[uur]\ar[r]\ar[ddr] & \boxed{x_{2}}\ar[rru]\ar[rrrd]\\
 &  &  &  & *++[o][F-]{c}\\
 & \boxed{x_{3}}\ar[urrr]
}$$

The hierarchical model implies that:

1.  When people are told to ignore some cue they will fail if that cue is processed prior to reaching consciousness.

2.  When people are given two cases to judge simultaneously, they will be able to control for the influence of irrelevant cues.

## Testing for Implicit Knowledge

There has been a long debate over how much of human knowledge is implicit (i.e., inaccessible to conscious thought) and there remains general disagreement over how to define implicit knowledge, and how to test for it. (See XXX for a discussion of the history of the debate).

Within the hierarchical model there is a simple distinction between information that is explicit and implicit: whether information is accessible to consciousness directly, or only through its contribution to an earlier node. The definition implies a test for conscious accessibility: knowledge is implicit if it cannot be *modulated* at will, for example by asking subjects to interpret a set of cues in a different way, or to selectively ignore some cues.

More precisely, here are some suggested tests for implicit knowledge:

1.  In knowledge of grammar.

2.  (\...)
