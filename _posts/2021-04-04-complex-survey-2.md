---
layout: page
title:  "Complex survey (2)"
subtitle: "Complex survey에서 평균과 OLS"
date:	2021-04-04
comments: true
categories: ["Statistics"]
---

## 평균 추정 (1)
평균은 총량에서 전체 인구수를 나누면 됩니다.
문제는 [국민건강영양조사 원시자료 이용지침서](https://knhanes.cdc.go.kr/knhanes/sub03/sub03_02_05.do)의 평균공식은 실제 인구수가 아니라 가중치의 합으로 인구수를 추정하고 있다는 점입니다.
실제 인구수 대신 실제 인구수의 추정량을 사용하고 있는 것입니다.
다음 단락에서 테일러 근사 (Taylor approximation)을 소개하고 실제 인구수 대신 그 추정량을 사용해도 됨을 보이겠습니다.

## 테일러 근사
테일러 근사는 학부 미적분학에서 배우는 것 중 가장 널리 쓰이는 내용입니다.
반가운 소식은 최소 이 시리즈에 한해서는 1차 근사보다 더 복잡한 근사를 쓸 일이 아마 없을 거라는 점입니다 (세상의 모든 함수는 선형입니ㄷ).
2차원 다변수 함수 $f:\mathbb{R}^2 \rightarrow \mathbb{R}$의 $(x_0, y_0)$에서의 1차 테일러 근사는

$$
f(x,y) = f(x_0, y_0) + \frac{\partial f}{\partial x}(x_0,y_0)(x-x_0)
	+ \frac{\partial f}{\partial x}(x_0, y_0)(y-y_0)
$$

입니다.

## 분산 추정
[지난 시간](https://hanbin973.github.io/statistics/2021/04/03/complex-survey-1.html) 계산한 Horvitz-Thomspon 추정량의 분산의 불편추정량은 다음과 같습니다.

$$
\begin{align}
\widehat{\mathrm{Var}}(\hat{T}_{2s}) &= \sum_{c \in A_1} \sum_{d \in A_1} \frac{1}{\pi_{cd}}  \frac{\pi_{cd} - \pi_c  \pi_d}{\pi_c \pi_d}
\sum_{i \in B_c} \sum_{j \in B_d} \frac{1}{\pi_{ci,dj|c,d}} y_{ci}y_{dj} \\
&+
\sum_{c \in A_1} \sum_{i \in B_c} \sum_{j \in B_c}
\frac{1}{\pi_{ci,cj|c}}
\frac{\pi_{ci,cj|c} - \pi_{ci|c}\pi_{cj|c}}{\pi_{ci} \pi_{cj}} y_{ci}y_{cj}
\end{align}
$$

본격적인 얘기에 앞서 이 공식이 [국민건강영양조사 원시자료 이용지침서](https://knhanes.cdc.go.kr/knhanes/sub03/sub03_02_05.do)에 등장하는 분산추정공식과 일치함을 보이겠습니다.
결론부터 말하면 원시자료 이용지침서에 있는 공식에는 적지 않은 근사가 들어갔습니다.
위의 공식을 잘 보면 왠지 없앨 수 있게 생긴 부분이 두 개 있습니다.
하나는 첫 줄의

$$
\frac{\pi_{cd}-\pi_c \pi_d}{\pi_c \pi_d}
$$

이고 다른 하나는 둘쨋줄의

$$
\frac{\pi_{ci,cj|c}-\pi_{ci|c} \pi_{cj|c}}{\pi_{ci} \pi_{cj}}
$$

입니다.

각각은 $c \neq d$ 그리고 $i \neq j$인 경우에 근사적으로 0이 될 수도 있습니다.
예를 들어, 둘째 항의 경우 한 집락 안에서 표본을 매우 적게 뽑을 경우 근사적으로 0이 됩니다.
왜냐하면 뽑는 대상의 수가 모집단에 비해 작을 경우 비복원 추출이 근사적으로 복원추출과 같아져 독립이 되기 때문입니다.
첫째 항의 경우에도 뽑는 집락의 갯수에 비해 전체 집락의 수가 크면 근사적으로 0이 될 것입니다.
이를 염두에 두고 원시자료 이용지침서의 공식을 관찰합시다.
표기법은 비교를 용이성을 위해 이 글에 맞게 바꿨습니다.
참고로 국민건강영양조사는 







