---
layout: post
title: Marker SNP as a noisy measurement
---

_Genome-wide association study_ (GWAS) runs millions of regressions across the genome to identify genomic regions that are responsible for the variatiblity in a trait.
The idea stems from the concept of _linkage disequilibrium_ (LD), a phenomenon where two genomic regions are statistically correlated due to physical linkage.
Technically, the correlation may come from population phenomenons but the post will consider only physical linkage for simplicity.
There are approximately 3 billion base pairs in the human genome (even larger for plant genomes) but the actual number of regressions are usually around several million.
As long as the genotyped markers are located dense enough, they will cover the whole genome through LD.
Even if the true causal variant is not genotyped, it is likely that it's effect will be detected in a regression of a marker nearby.
Although REAL whole genome regressions based on WGS data are released nowadays, this rationale makes genotype array based GWAS a cost-effective method for identifying trait associated loci.

Another implication of this study design is that most markers are not actually causal.
They are merely markers that _tag_ a nearby causal variant.
Therefore, a causal claim based on GWAS does not really make sense in its raw form.
To make things sense, many proposed a framework viewing genotyped markers as a noisy measurement of the casual locus. 
Read [Pritchard and Prezworski](https://pubmed.ncbi.nlm.nih.gov/11410837/) and [Edge et al.](https://pubmed.ncbi.nlm.nih.gov/24481204/).

The consequence of measurement error has been documented in various fields and the work of Edge is based on that of psychometrics. 
[Econometric analysis of cross-section and panel data](https://mitpress.mit.edu/books/econometric-analysis-cross-section-and-panel-data-second-edition) gives a more comprehensive treatment on the general issue which I describe in this post.

## Exogeneous measurement error

Consider the following _structural_ equation.
It means that the explanatory variables has a causal effect on the dependent variable: changing the explanatory variable changes the distribution of the dependent variable.

$$
y = \beta_0 + \beta_1 x_1 + \cdots + \beta_K x_K^m + v
$$

where the superscript $m$ denotes the mismeasured variable that we don't have access to.
The mismeasured value $x_K$ for $x_K^m$ is instead observed.
Also, assume $\mathbb{E}[v \vert x_1, \ldots, x_K^m] = 0$ for unconfoundedness and $E[v]=0$ since we've included the intercept $\beta_0$.

By noisy measurement, it means that $x_K^m$ is observed as $x_K$ with some errors $e_K$ such that $e_K$ is indpendent from all $x_1, \ldots, x_{K-1}$ and $\mathbb{E}[e_K] = 0$.

$$
x_K = x_K^m + e_K
$$

It's important to clarify whether equation (2) is structural or not.
We assume it's structural for a moment and discuss this later.
This can be described in terms of a DAG.

$$
e_K \rightarrow x_K \leftarrow x_K^m \rightarrow y
$$

Subsituting equation (2) to (1) gives

$$
y = \beta_0 + \beta_1 x_1 + \cdots + \beta_K x_K + (v-\beta_K e_K)
$$

Applying _ordinary least square_ (OLS) to equation (4) will not give a consistent estimate of $\beta_K$ since $x_K$ and $v-\beta_K e_K$ are generally correlated due to equation (2) (or diagram (3)).
To see this, use the Frisch-Waugh-Lovell (FWL) theorem.
First define 
	$r_K = x_K - \mathrm{L}(x_K \vert 1, x_1, \ldots, x_{K-1})$ 
where $\mathrm{L}(\cdot \vert \cdot)$ is the linear projection.
Then by FWL, we have

$$
	\mathrm{plim} \hat{\beta}_K^{\mathrm{OLS}}  = \frac{\mathbb{E}[r_Ky_K]}{\mathbb{E}[r_K' r_K]}
$$

From the definition of $r_K$,

$$
	x_K - \mathrm{L}(x_K \vert 1, x_1, \ldots, x_{K-1}) \\
		= x_K^m + e_K - \mathrm{L}(x_K^m + e_K \vert 1, x_1, \ldots, x_{K-1}) \\
		= r_K^m + e_K - \mathrm{L}(e_K \vert 1, x_1, \ldots, x_{K-1}) \\
		= r_K^m + e_K 
$$

where 
	$r_K^m = x_K^m - \mathrm{L}(x_K^m \vert 1, x_1, \ldots, x_{K-1})$
.
The last equality comes from the fact that the measurement error $e_K$ is indpendent from all $x_1, \ldots, x_{K-1}$ and $\mathbb{E}[e_K] = 0$.

Substituting this to the numerator of (5) gives

$$
	\mathbb{E}[r_K y_K]
		= \mathbb{E}[r_K^m y_K]
		= \mathbb{E}[r_K^m r_K^m]\beta_K
$$

and to the denominator gives

$$ 
	\mathbb{E}[r_K r_K] 
		= \mathbb{E} [r_K^m r_K^m + 2 r_K^m e_K + e_K e_K]  \\
		  = \mathbb{E} [r_K^m r_K^m] + \mathbb{E}[e_K e_K] 
$$

Hence, we finally arrive at the following result.

$$
	\mathrm{plim}{\hat{\beta}_K^{\mathrm{OLS}}} = \beta_K \cdot \frac{\mathrm{Var}(r_K^m)}{\mathrm{Var}(r_K^m)+ \mathrm{Var}(e_K)}
$$

which states that the OLS points to a value that is smaller than the true value.

## Application to GWAS

The core assumption that led to equation (9) is that the error $e_K$ is exogeneous respect to the variables appearing in the structural equation (1).
Some mechanistic reasoning on the process of LD makes this assumption doubtful.
This becomes clear when we focus on the DAG (3).
When the genotype at the causal locus is $x_K^m$ and the marker genotype is $x_K$, the latter is not _caused_ by $x_K^m$.
Instead, they become correlated through a evolutionary process (say, $E$) which is depicted in the following DAG.

$$
x_K \leftarrow E \rightarrow x_K^m
$$

This will eventually break the exogeneity of $e_K$.
Hence, the structural interpretation of equation (2) is lost.
Furthermore, as the evolutionary process can potentially result in population structure, thinking $x_1, \ldots, x_{K-1}$ may be correlated to $e_K$ if we think them as covariates (e.g. PC).
Therefore, the mismeasurement model for GWAS effect size will be valid under a restricted set of evolutionary processes although such processes might be pluasible in real human population.
