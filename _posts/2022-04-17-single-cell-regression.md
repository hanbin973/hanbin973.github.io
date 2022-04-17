---
layout: post
title: Regres-out in single-cell biology
---

I first intended this content as a research paper but I'm currently not planning any additional single-cell projects so I write this as a blog post.
In many, I mean really many single-cell analysis notes, people suggest regressing out certain variables prior to analysis.
For example, in the cell-cycle vignette in Seurat [manpage](https://satijalab.org/seurat/articles/cell_cycle_vignette.html), they recommend regressing out cell-cycle scores prior to PCA.
I think such practice is not legitimate because it wipes out not only the variation due to cell-cycle but also other biological variations that are correlated to cell-cycle.
I show, in this post, that this is ture _in general_.

As an illustrative example, let's think of the following model that includes Poisson, negative-binomial and many more.

$$
\log E[Y \vert m, T, X] = \log m + T + \beta X 
$$

where $m$ is the size factor, $T$ is some biological effect (cell-type, trajectory etc.) and $X$ be the covariate.
Say someone wants to discard $X$ from the data using the `regress-out` approach.

It's just a standard log-normal _conditional expectation function_ (CEF) that is assumed in most single-cell methods assuming count models.
One might question about over-dispersion in scRNA-seq data. 
Note that because we only assume equation (1), the setting is robust to any type of over/under-dispersion so don't worry.

In general, we don't have any information about $T$ and as in the Seurat vignette, this is inferred after we regress-out $X$.
Therefore, the regression is done based on the following equation.

$$
\log E[Y \vert m, X] = \log m + \beta' X 
$$

Note that I added a ' to explicitely state that \beta and \beta' are not the same.







