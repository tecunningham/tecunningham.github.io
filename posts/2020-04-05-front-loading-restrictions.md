---
layout: post
title: Optimal Coronavirus Policy Should be Front-Loaded
---

**Q: How should you sequence policies over time?** E.g. suppose you want to manage the epidemic until a vaccine arrives and you have policies (lockdowns, distancing, masks) each of which is associated with a certain effect on the growth-rate of cases, but each also has some fixed social cost per day. How should you apply the policies over time?

**A: The severity of the policies should be gradually *decreasing*,** i.e. they should gradually become less severe, as you approach the availability of a vaccine. There should not be zig-zagging between policies in this setup.

Any justification for zig-zagging must come from some additional consideration like (a) non-separabilities in the costs, e.g. psychological/economic need for occasional respite, (b) uncertainty about the end-date, (c) uncertainty about the effect of the policies, such that there is informational-value from varying policies, or (d) desire to maintain a steady flow of cases, in order to reach herd immunity (the "mitigation" strategy).

## Corollary: you should never *expect* policy to get stricter

You should never find yourself in the situation where you expect policy to get stricter in the future. If you anticipate that a stricter policy will be appropriate next week then that strict policy is appropriate *this* week!

Countries in early stages of the epidemic should be doing as much or more as countries in later stages.

## Intuition

Suppose that there's some tradeoff across policiers between the growth-rate and the social cost.

Then given any fixed time-path of policies: e.g., (A,A,B,C), if it is not monotonically decreasing in severity from high-cost to low-cost, then you can do strictly better by rearranging the path of policies to be monotonically decreasing. The social cost will be identical, because the set of policies will be the same, but the number of cases will be lower at every point in time, since at any given point the cumulative growth rates, up to that point, will be lower. Thus the final cumulative number of cases will be lower.

## Additional Reason to Front-Load: Extinction

All of this is treating the number of cases as a continuous variable which means you can never completely extinguish the disease. However if that's a possibility that's within sight (e.g. as in NZ), then that's a significantly *stronger* case for starting with very severe policies, to try to kill the disease entirely, and then you can go back to the garden of Eden.

## Prior Discussion

There's been some discussion of zig-zagging by the Imperial group ([paper]([URL](https://www.imperial.ac.uk/media/imperial-college/medicine/sph/ide/gida-fellowships/Imperial-College-COVID19-NPI-modelling-16-03-2020.pdf))) and by Timothy Gowers ([twitter & post](https://twitter.com/wtgowers/status/1243973167879794691)) 

Gowers says the optimal policy is very short zig-zags (changing policy every other day), however I think this is misleading. It comes from fixing the lower-threshold and optimizing the upper-threshold. If instead you fixed the upper-threshold and optimized the lower-threshold, then the optimal cycle-length will be long.

If you choose both the upper and lower threshold (both T and S) then he notes that they'll both be arbitarily low. However this ignores the cost of *getting* to zero given current cases. 

Instead a well-defined problem is to choose an optimal time-path of policy given some start-point and end-point. In that case it'll be a path of gradually decreasing strictness (without zig-zags).

You can see the intuition in the diagram below: the total infections is approximately the area under the zig-zag (not quite: because the y-axis is ln(cases), but this won't matter for the argument). Thus you can reduce the area under the line by lowering the upper threshold. However if you instead take the *upper* threshold as fixed, then it's optimal to choose a lower threshold that is as low as possible, i.e. you want *long* cycles, not short cycles.

![abc](https://www.dropbox.com/s/jj93tz0k0kuau49/zigzag.png?raw=1)
