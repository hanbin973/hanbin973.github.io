---
layout: page
title:  "Complex survey (2)"
subtitle: "Complex survey에서 평균과 OLS"
date:	2021-04-04
comments: true
categories: ["Statistics"]
---

일반적으로 가중치 $w_i$는 뽑힐 확률 $\pi_i$의 역수입니다.
별 다른 말이 없으면 앞으로 $w_i = \frac{1}{\pi_i}$ 입니다.

## 평균 추정 (1)
평균은 총량에서 전체 인구수를 나누면 됩니다.
나머지 표기법은 [이전 글](https://hanbin973.github.io/statistics/2021/04/03/complex-survey-1.html)을 참고하세요.
$N$은 모집단의 총 인구수입니다.

$$
\hat{\overline{Y}} = \frac{1}{N} \hat{T}
$$

문제는 [국민건강영양조사 원시자료 이용지침서](https://knhanes.cdc.go.kr/knhanes/sub03/sub03_02_05.do)의 평균공식은 실제 인구수가 아니라 가중치의 합으로 인구수를 추정하고 있다는 점입니다.

$$
\hat{\overline{Y}} = \frac{\hat{T}}{\sum_{i \in A} w_i}
$$

실제 인구수 대신 실제 인구수의 추정량 ($\hat{N} = \sum_{i \in A} w_i$)을 사용하고 있는 것입니다.
다음 단락에서 테일러 근사 (Taylor approximation)을 소개하고 실제 인구수 대신 그 추정량을 사용해도 됨을 보이겠습니다.

## 테일러 근사
테일러 근사는 학부 미적분학에서 배우는 것 중 가장 널리 쓰이는 내용입니다.
반가운 소식은 최소 이 시리즈에 한해서는 1차 근사보다 더 복잡한 근사를 쓸 일이 아마 없을 거라는 점입니다 (세상의 모든 함수는 선형입니ㄷ).
2차원 다변수 함수 $f:\mathbb{R}^2 \rightarrow \mathbb{R}$의 $(x_0, y_0)$의 1차 테일러 근사는

$$
f(x,y) = f(x_0, y_0) + \frac{\partial f}{\partial x}(x_0,y_0)(x-x_0)
	+ \frac{\partial f}{\partial y}(x_0, y_0)(y-y_0)
$$

입니다.

$(x_0, y_0)$에 모수 $(\mu, \nu)$를 대입하고 $(x,y)$에 그 추정량 $(\hat{\mu}, \hat{\nu})$를 대입하면 

$$
f(\hat{\mu},\hat{\nu}) = f(\mu, \nu) + \frac{\partial f}{\partial x}(\mu,\nu)(\hat{\mu}-\mu)
	+ \frac{\partial f}{\partial y}(\mu, \nu)(\hat{\nu}-\nu)
$$

가 됩니다.

이 식에 기댓값 $\mathbb{E}$나 분산 $\mathrm{Var}$을 걸면 복잡한 함수 $f$의 기댓값과 분산을 얻을 수 있습니다.

## 평균 추정 (2)
테일러 근사를 평균 추정의 경우에 적용하면 $f(x,y) = \frac{x}{y}$, $\mu=T$, $\nu=N$이 됩니다.
$x$와 $y$에 대한 $f$의 편도함수는 각각 $f_x(x,y) = \frac{1}{y}$ 그리고 $f_y(x,y) = -\frac{x}{y^2}$입니다.
기댓값을 계산하면

$$
\mathbb{E}(\frac{\hat{T}}{\hat{N}}) = \frac{T}{N} + \frac{1}{N}\mathbb{E}(\hat{T}-T) - \frac{T}{N^2}(T,N)\mathbb{E}(\hat{N}-N) = \frac{T}{N}
$$

입니다. 
$\hat{T}$와 $\hat{N}$이 각각 $T$와 $N$의 불편추정량이기 때문입니다.
분산은

$$
\mathrm{Var}(\frac{\hat{T}}{\hat{N}}) = \frac{1}{N^2}\mathrm{Var}(\hat{T}) + \frac{T^2}{N^4}\mathrm{Var}(\hat{N})
$$

입니다.

한국의 총 인구수를 생각하면 $\frac{T^2}{N^4}$은 상당히 작은 숫자입니다.
더군더나 조사는 매번 거의 비슷한 숫자의 대상자를 뽑기 때문에 $\mathrm{Var}(\hat{N})$ 역시 매우 작은 숫자입니다.
그래서 두번째 항을 무시하면 $\hat{N}$을 모수인 $N$으로 취급해도 큰 문제가 생기지 않음을 알 수 있습니다.

## 분산 추정
[지난 시간](https://hanbin973.github.io/statistics/2021/04/03/complex-survey-1.html) 계산한 인구 총량의 Horvitz-Thomspon 추정량의 분산의 불편추정량은 다음과 같습니다.

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

앞 단락의 논증을 이용하면 평균의 분산에 대한 추정량은 위 값을 $\hat{N} = \sum_{c \in A_1} \sum_{i \in B_c} \frac{1}{\pi_{ci}}$의 제곱으로 나눠서 얻을 수 있습니다.
우리의 목표인 국건영과는 다르지만 직관을 얻기 위한 계산연습의 일환으로 1단계 및 2단계가 모두 단순표본추출인 경우에 위 식이 어떻게 단순화되는지 살펴봅시다.
이전 글의 표기법을 따라 $C$를 집락의 갯수, $n_c$를 뽑은 집락의 갯수, $M_c$를 집락 $c$의 대상자 수 그리고 $m_c$를 집락 $c$에서 뽑은 표본의 수라고 하겠습니다.

그러면 각 확률은 다음으로 단순화 됩니다.

$$
\begin{align}
\pi_c &= \frac{n_c}{C} \\
\pi_{cd} &= \frac{n_c(n_c-1)}{C(C-1)} \quad (c \neq d) \\
\pi_{ci|c} &= m_c/M_c \\
\pi_{ci,cj|c} &= \frac{m_c(m_c-1)}{M_c(M_c-1)} \quad (i \neq j)
\end{align}
$$

이를 분산 식에 대입하면






