---
layout: page
title:  "반복검사의 한계"
subtitle: ""
date:	2021-04-14
comments: true
categories: ["Epidemiology"]
---

[지난 글](https://hanbin973.github.io/epidemiology/2021/04/13/multi-rapid-test.html)에서는 반복검사의 민감도가 단순히 민감도의 곱으로 나타나지 않는다는 것을 증명했습니다.
각 검사는 연관되어 있기 때문에 검사 반복수가 증가할수록 새로 얻는 정보량이 계속 줄어듭니다.

$n$번 검사해서 모두 음성이 나올 확률은

$$
\mathbb{P}(n번음성|감염자) = P(1번째음성|감염자)\prod_{i=2}^n P(i번째음성|(i-1)번음성,감염자)
$$

입니다.

검사가 거듭될수록 P(i번째음성|(i-1)번음성,감염자)가 점점 감소하기 때문에 $1-\mathbb{P}(n번음성|감염자)$를 민감도로 삼아도 반복횟수가 증가할수록 민감도가 높아지는 속도가 점점 감소합니다.
그렇다면 얼마나 감소할까요?



