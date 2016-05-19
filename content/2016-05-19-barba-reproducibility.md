Title: How do you choose a reproducibility metric?
Date: 2016-05-19 12:00
Category: Reproducibility
Tags: Reproducibility
Author: Ian Hawke
Summary: Mesnard and Barba produced a brilliant reproducibility paper, showing how hard it can be to get many details correct. In contrast to some previous reproducibility efforts they don't have a single number, or curve, that they want to reproduce in advance. Is this the best approach?

Some papers are effortlessly brilliant. Some show their brilliance by lifting the lid on just how much work it is to do it *right*. Olivier Mesnard and Lorena Barba just [released a preprint](http://arxiv.org/abs/1605.04339) whose title, "*Reproducible and replicable CFD: it's harder than you think*", shows it firmly belongs in the latter camp. Combine that with the [detailed repository](https://github.com/barbagroup/snake-repro) containing all the code needed to do the work, there's enough information to lose a couple of days.

What most interests me is the criteria chosen for successful reproducibility. I've argued before about what is [close enough](http://ianhawke.github.io/blog/close-enough.html) when comparing a numerical simulation to theoretical expectations, and about [the minimum I'd like to be able to reproduce](http://ianhawke.github.io/blog/the-image-is-the-simulation.html). But Mesnard and Barba's paper is far more complex, and is code versus code comparison with experimental backup, not code versus theory. The criteria discussed in the introduction include

> A previous experimental study had already shown that the lift coefficient of a snake cross section in a wind tunnel gets an extra oomph of lift at 35 degrees angle-of-attack. Our simulations showed the same feature in the plot of lift coefficient. Many detailed observations of the wake (visualized from the fluid-flow solution in terms of the vorticity field in space and time) allowed us to give an explanation of the mechanism providing extra lift.

This is a much more complex than comparing a single number. Hence the paper contains statements such as

> Is it acceptable as a replication study? We think yes, but this is a judgement call.

and

> we make a judgement call that this result does indeed pass muster as a replication of our previous study.

How is this judgement call made? Is this art or science? What needs to be reproduced, and how closely?

## Samurai and Ninja

To think further about this, let's look at a totally different study: the detection of gravitational waves from binary black holes. Long before the [GW150914 observation](http://www.ligo.org/science/Publication-GW150914/index.php) there was a lot of concern about the accuracy of numerical simulations of black holes. After a lot of effort, gravitational wave signals were finally being computed from numerical simulations. With no experiment to compare against, and with significant differences in both the form of the equations and the numerical methods used, the possibility that some, if not all, of the simulations were simply wrong was a big worry.

The [Samurai](http://journals.aps.org/prd/abstract/10.1103/PhysRevD.79.084025) ([arXiv link](http://arxiv.org/abs/0901.2437)) and [Ninja](http://iopscience.iop.org/article/10.1088/0264-9381/26/16/165008/meta) ([arXiv link](http://arxiv.org/abs/0901.4399)) papers were the result. In both cases the key question was "Does it make any difference to a *detection* if we use one numerical result rather than another?". There was a clear metric, given by the "best mismatch" between predicted waveforms, after folding in the expected noise from the experiment. In the Ninja paper waveforms predicted by different codes were directly compared; in the Samurai paper the link to the full data analysis pipelines are made, to see what useful information can be pulled out.

The result was simple: for current detectors, *all* the numerical results were effectively indistinguishable. The difficulty of doing the experiment at all constrained the results so that only the grossest, most qualitative features of the simulations stood out from the noise. This reproducibility metric worked, but hid many of the interesting differences between the simulations. However, without any experiment that could show the differences, is there a point in going further?

## Questioning the metric

In the Mesnard and Barba case, they have broadly specified two "metrics":

1. the variation of the lift coefficient with angle-of-attack;
2. features in the wake explaining the lift mechanism.

The simplest numerical metric is the variation of the lift coefficient, and figures 3, 6, and 8 of their paper show how the time averaged lift coefficients compare across simulations and experiment. What is more interesting to me is the way that Mesnard and Barba challenge this metric, by looking at the variation of the instantaneous lift coefficients (figures 4, 7, 9, and 11), discussing the impact of some of the arbitrary choices (such as the time period over which the averaging is done), and the simulation issues that could cause this. This links to the second metric: by exploring the wake features they can explain issues with the simulations, including meshing and boundary condition problems. These are clear from some of the figures, but difficult to quantify.

This shows a clear difference from the Samurai and Ninja papers. The first metric is there to reproduce the experimental result. If the theory is certain and the mechanism clear, there's nothing more to say. But for the Mesnard and Barba reproduction, they wish in addition to test the *explanation* of the results. This means digging deeper into the details of the simulation results, which in turn shows differences in the lift coefficients. Their reproduction is going beyond the numerical matching of an experimental result and into the physical prediction that a detailed numerical simulation can give.

## Lessons

Mesnard and Barba detail their lessons learned, but to me this paper brings home yet another point. Reproducibility has a number of technical aspects which can be extremely hard, as beautifully illustrated by this paper. However, it also has the human, non-technical aspect of choosing *what* needs to be reproduced: what is the metric? Finally, there's the issue of how that metric will change over time, as the depth of the reproduction goes from the general features that an experiment will catch to the qualitative details that "explain" why something happens.
