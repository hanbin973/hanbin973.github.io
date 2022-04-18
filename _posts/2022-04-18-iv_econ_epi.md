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
The _target parameter_ is absent!

In this post, I review the two approaches in instrumental variable.
The first one is the _local average treatment effect_ (LATE) framework famous in econometrics (Imbens and Angrist, [1994](https://www.jstor.org/stable/2951620?seq=1)).
The second ons is the _structural mean model_ (SMM) framework proposed by the Harvard CI group (Robins, [1994](https://www.tandfonline.com/doi/abs/10.1080/03610929408831393)). 

We start from the switching formula.

$$ Y_i = D_i \cdot Y_i(1) + (1-D_i) \cdot Y_i(0) $$

which gives

$$ Y_i = \tau_i \cdot D_i + Y_i(0) $$

after reordering.
$\tau_i$ is the individual treatment effect. 

Learning the importance of heterogeneous TE in IV was a very illuminating experience.
At the same time, the plethora of many assumptions was very confusing.
How does these different assumptions relate to each other?
I don't have a full-blown answer to this question.
However, I think that the two approaches by econometricians and epidemiologists can be classified in terms of the stage in which the assumption is applied.
The former, which is usually referred to _monotonicity_ is a matter of how the instrument $Z$ affects the instrument $D$.
On the other hand, the latter (e.g. _no treatment effect modification_ (NEM) assumption) imposes restriction on the mode of treatment $D$ influencing the outcome $Y$.
The following derivations will make this point clear.

## Monotonicity
The proof is essentially the same as in _Mostly Harmless Econometrics_ (Theorem 4.4.1, p.155).
Apply $E[\cdot \vert Z]$ to equation (2).

$$ E[Y_i \vert Z_i] = E[\tau_i \cdot D_i \vert Z_i] + E[Y_i(0) \vert Z_i] $$

The last term is just a constant $E[Y_i(0)]$ by the exclusion criteria $Y(d) \perp\kern-5pt\perp Z$.

$$ E[Y_i \vert Z_i=1] - E[Y_i \vert Z_i=0] \\
= E[\tau_i \cdot D_i \vert Z_i=1] - E[\tau_i \cdot D_i \vert Z_i=0]
$$

To simplify this equation, we have two choices.
One is to impose some condition on $\tau_i$ and the other is to impose some condition on $D_i$.
Monotonicity does the latter by assuming no defiers.
Let $C_i = D_i(1) - D_i(0)$ be the compliance status.
Then 

$$
E[\tau_i \cdot D_i \vert Z_i] 
\\= E[ E[ \tau_i \cdot D_i \vert Z_i, C_i ] \vert Z_i]
\\= \sum_c E[\tau_i \cdot D_i \vert Z_i, C_i=c] \cdot P(C_i =c \vert Z_i)
$$

By exogeneity of the instrument, $P(C_i \vert Z_i) = P(C_i)$.
For $Z=1$,

$$
= \sum_c E[\tau_i \cdot D_i \vert Z_i=1, C_i=c] \cdot P(C_i =c) \\
= E[\tau_i \cdot 1 \vert Z_i=1, C_i=1] \cdot P(C_i =1) \\
+ E[\tau_i \cdot D_i \vert Z_i=1, C_i=0] \cdot P(C_i=0)
$$

and for $Z=0$,

$$
= E[\tau_i \cdot 0 \vert Z_i=0, C_i=1] \cdot P(C_i =1) \\
+ E[\tau_i \cdot D_i \vert Z_i=0, C_i=0] \cdot P(C_i=0)
$$

Finally, subsituting (6) and (7) into (4) and the exclusion criteria guarantees

$$
E[\tau_i \cdot D_i \vert Z_i=1] - E[\tau_i \cdot D_i \vert Z_i=0] \\
= E[\tau_i \cdot 1 \vert C_i =1] \cdot P(C_i=1)  \\
= E[\tau_i \vert C_i=1] \cdot E[D_i(1) - D_i(0)] \\
= E[\tau_i \vert C_i=1] \cdot (E[D_i \vert Z=1] - E[D_i \vert Z=0]) 
$$

where the last line came from exogeneity.
The proof shows that there is no restriction on $\tau_i$ and only the assumptions involving $D_i$ was used to derive the Wald ratio.

## Structural Mean Model (SMM)

The additive SMM is 

$$
E[Y-Y(0) \vert D, Z] = (\psi_0 + \psi_1 Z) \cdot D
$$

When I saw this for the first time, I was confused.
Most importantly, the interpretation of $\psi_0$ and $\psi_1$ wasn't very transparent to me.
Therefore, I thought it was better to start from equation (2) to make it more sensible.

Applying $E[\cdot \vert D,Z]$ to equation (2) gives

$$
E[Y_i - Y_i(0) \vert D_i,Z_i ] = E[\tau_i \cdot D_i \vert D_i, Z_i]
\\ = E[\tau_i \vert D_i, Z_i] \cdot D_i
\\ = E[\tau_i \vert Z_i] \cdot D_i
$$

So, what was happening in the SMM was the specification of $E[\tau_i \vert Z_i]$ which is

$$
E[\tau_i \vert Z_i] = \psi_0 + \psi_1 Z_i
$$

NEM imposes $\psi_1 = 0$ so that $\psi_0$ eventually becomes the PATE.
Embracing the soul of Wooldridge's idea that I [wrote](https://hanbin973.github.io/2022/04/17/TEH_reg.html), using $Z - \mu_Z$ instead of $Z$ would have given $\psi_0$ the same interpretation without the NEM although the problem of identification would have remained (the number of moment condition is smaller than the number of estimands).

To obtain the Wald ratio, apply the law of iterated expectation on (assuming NEM),

$$
E[Y_i - Y_i(0) \vert Z] = \\
E[ E[Y_i - Y_i(0) \vert D,Z] Z ] \\
= E[ \psi_0 \cdot D \vert Z ] \\
= \psi_0 E[ D \vert Z ]
$$

and substituting it into equation (4) gives the desired result.
Examining the consequence of NEM on equation (11) directly shows that SMM-based approaches acheives identification by restricting the mode of $D \rightarrow Y$.

## Concluding remark
My impression of these result is that monotonicity and SMM-based assumptions are not necessarily stronger/weaker than the other.
The choice ultimately depends on which stage, $Z \rightarrow D$ or $D \rightarrow Y$, will be restricted through imposing additional assumptions.
May be some person can come up with an alternative identification strategy by imposing restrictions on both but each of them being weaker for each stage.





