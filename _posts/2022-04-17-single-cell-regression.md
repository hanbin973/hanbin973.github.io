---
layout: post
title: Regression in single-cell biology
---

I first intended this content as a research paper but I'm currently not planning any additional single-cell projects so I write this as a blog post.
In many, I mean really many single-cell analysis notes, people suggest regressing out certain variables prior to analysis.
For example, in the cell-cycle vignette in Seurat [manpage](https://satijalab.org/seurat/articles/cell_cycle_vignette.html), they recommend regressing out cell-cycle scores prior to PCA.
I think such practice is not legitimate because it wipes out not only the variation due to cell-cycle but also other biological variations that are correlated to cell-cycle.
I show, in this post, that this is ture _in general_.





