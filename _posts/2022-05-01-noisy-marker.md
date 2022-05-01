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

Consider the following _structural_ equation.
It means that the explanatory variables has a causal effect on the dependent variable: changing the explanatory variable changes the distribution of the dependent variable.

$$
y = \beta_0 + \beta_1 x_1 + \cdots + \beta_K x_K^m + v
$$

where the superscript $m$ denotes the mismeasured variable that we don't have access to.
The mismeasured value $x_K$ for $x_K^m$ is instead observed.
Also, assume $\mathbb{E}[v \vert x_1 \ldots x_K^m] = 0$ for unconfoundedness and $E[v]=0$ since we included the intercept $\beta_0$.

By noisy measurement, it means that $x_K^m$ is observed as $x_K$ with some errors $e_K$.

$$
x_K = x_K^m + e_K
$$

It's important to clarify whether equation (2) is structural or not.
