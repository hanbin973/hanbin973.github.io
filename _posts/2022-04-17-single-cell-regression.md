---
layout: post
title: Regress-out in single-cell biology
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

where $m$ is the size factor, $T$ is some biological effect (cell-type, trajectory etc.) and $X$ be the covariate (this may include the intercept).
Say someone wants to discard $X$ from the data using the _regress-out_ approach.

It's just a standard log-normal _conditional expectation function_ (CEF) that is assumed in most single-cell methods assuming count models.
One might question about over-dispersion in scRNA-seq data. 
Note that because we only assume equation (1), the setting is robust to any type of over/under-dispersion so don't worry.

In general, we don't have any information about $T$ and as in the Seurat vignette, this is inferred after we regress-out $X$.
Therefore, the regression is done based on the following equation.

$$
\log E[Y \vert m, X] = \log m + \beta' X 
$$

Note that I added an apostrophe ' to explicitely state that $\beta$ and $\beta'$ are not the same.
The parameter $\beta$ is 

$$
\beta = \log \frac{E[Y \vert m, T, X=x+1]}{E[Y \vert m, T, X=x]}
$$

and $\beta'$ is 

$$
\beta' = \log \frac{E[Y \vert m, X=x+1]}{E[Y \vert m, X=x]}
$$

The difference between the two quantities can be analytically obtained using the law of iterated expectation.

$$
E[Y \vert m, X] = E[ E[Y \vert m, T, X] \vert m, X] 
\\= E[ \exp(\log m + \beta X + T ) \vert  m, X]
\\= \exp(\log m + \beta X ) \cdot E[ \exp(T) \vert m,X ]
$$

Substituting this to equation (4) gives

$$
\beta' = \log \frac{E[Y \vert m, X=x+1]}{E[Y \vert m, X=x]} \\
		= \log \frac{\exp(\log m + \beta \cdot (x+1)) \cdot E[\exp(T) \vert m,X=x+1]}{\exp(\log m + \beta \cdot x) \cdot E[\exp(T) \vert m,X=x]} \\
		= \beta + \log \frac{E[\exp(T) \vert X=x+1]}{E[\exp(T) \vert X=x]}
$$

Therefore,

$$
\beta' - \beta =  \log \frac{E[\exp(T) \vert X=x+1]}{E[\exp(T) \vert X=x]}
$$

which shows that the regress-out approach estimates $\beta'$ which is not $\beta$, an intended parameter to estimate.
Equation (6) is zero if the covarite $X$ and $T$ is independent. 
This may not be true, for example, in cases when $X$ is the batch covariate and one tries to merge data from two batches with different cell-type compositions.
This means that $T$ is correlated to $X$ so equation (6) should be non-zero.
Unless the covariate is independent of $T$, regress-out approach always estimates the wrong number and substracts it from data.
Hence, I believe with few exceptions, this should not be recommended.













