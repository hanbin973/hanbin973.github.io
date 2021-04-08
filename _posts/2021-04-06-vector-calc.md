---
layout: page
title:  "Vector Calculus"
subtitle: "A cheat sheat"
date: 2021-04-06
comments: True
categories: ["Math"]
---

All notations are numerator layouts.
Irregularly updated.

| <span style='font-size: 80%'> Function </span> | <span style='font-size: 80%'> Derivative </span> |
| --------------- | --------------- |
| $$\frac{\partial \mathbf{Ax}}{\partial \mathbf{x}}$$ | $$\mathbf{A}$$ | 
| $$\frac{\partial \mathbf{x}^T\mathbf{A}}{\partial \mathbf{x}}$$ | $$\mathbf{A}^T$$ |
| $$\frac{\partial \mathbf{x}^T \mathbf{A} \mathbf{x}}{\partial \mathbf{x}}$$ | $$2\mathbf{x}^T\mathbf{A}$$ |
| $$|fraC{\partial \mathbf{F}^{-1}}{\partial \mathbf{x}} | - \mathbf{F}^{-1} \frac{\partial \mathbf{F}}{\partial \mathbf{x}} \mathbf{F}^{-1} |
{: style="color:black; font-size: 150%; text-align: center;"}

A small tip for multivariate calculus.
Given a vector-valued function $F: \mathbb{R}^n \rightarrow \mathbb{R}^m$, the derivative $F'$ is a $m \times n$ matrix.
Hence, the shape of the derivative as a matrix ($m \times n$) is ordered in an opposite direction of the dimension of the domain-range of the function ($n \rightarrow m$).



