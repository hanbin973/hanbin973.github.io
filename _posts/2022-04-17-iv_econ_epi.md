---
layout: post
title: Instrumental variables in econometrics and epidemiology
excerpt_separator:  <!--more-->
---

_Mendelian randomization_ (MR) became very famous in the recent year.
Even clinical journals that are quite restrictive in using causal languages outside randomized trials also embrace MR studies nowadays.
In the methodological field, may new MR methods have been proposed.
However, I'm very skeptical about them as they impose extremely strict parametric assumptions.
For example, with very few execptions (see Shi [2021](https://pubmed.ncbi.nlm.nih.gov/34847085/) and [2022](https://bmcmedresmethodol.biomedcentral.com/articles/10.1186/s12874-021-01449-w)), they assume strict homogeneity (see Morrison [2020](https://pubmed.ncbi.nlm.nih.gov/32451458/)).
Furthermore, the biggest problem in current literature is that we are not very transparent about which parameter we are estimating. 
The _target paramter_ is absent!

In this post, I review the two approaches in instrumental variable.
The first one is the _local average treatment effect_ (LATE) framework famous in econometrics (Imbens and Angrist, [1994](https://www.jstor.org/stable/2951620?seq=1)).
The second ons is the _structural mean model_ (SMM) framework proposed by the Harvard CI group (Robins, [1994](https://www.tandfonline.com/doi/abs/10.1080/03610929408831393)). 

We start from the switching formula.

$$ Y_i = D_i \cdot Y_i(1) + (1-D_i) \cdot Y_i(0) $$

which gives

$$ Y_i = \tau_i \cdot D_i + Y_i(0) $$

after reordering.
$\tau_i$ is the individual treatment effect. 

In my experience, the distinction between all the IV frameworks comes from the level of heterogeneous treatment effect we allow in the model.
This means it is really how we model the $E[\tau_i \vert D_i, Z_i]$ where $Z_i$ is the instrument. 


