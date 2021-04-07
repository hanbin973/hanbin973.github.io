---
layout: page
title:  "Complex survey (3)"
subtitle: "Complex survey and OLS"
date:	2021-04-06
comments: true
categories: ["Statistics"]
---

이 블로그의 핵심철학은 모든 통계가 그저 선형모델 (linear model)에 불과하다는 것입니다.
![](https://lindeloev.github.io/tests-as-linear/linear_tests_cheat_sheet.png)
는 [링크](https://lindeloev.github.io/tests-as-linear/)에서 가져온 그림으로 평균의 t-검정, 교차표 검정, ANOVA 등 흔히 사용하는 통계적 검정이 모두 선형회귀분석의 일종에 불과함을 잘 설명하고 있습니다.
이 철학은 통계 소프트웨어를 코딩하는 입장에서 매우 유용합니다.
이 모든 게 같다면 코드를 여러 번 쓸 필요 없이 한 번 써서 무한정 재활용하면 되기 때문입니다.
저는 복합표본설계를 활용한 대규모 데이터를 다루게 되어 R의 `survey`나 SAS의 `proc survey`를 쓰기보다 직접 코드를 짜는 쪽을 택했습니다.
기존 프로그램들이 살인적으로 느리고 병렬처리를 지원하지 않아 어쩔 수 없는 선택이었습니다.
물론 프로그램을 새로 짜는 것은 성가신 일이지만 모든 검정은 그저 똑같은 선형모델에 불과하기 때문에 저는 코드를 한 번만 짜면 됩니다.

통계적 검정을 선형모델로 이해하는 것은 이처럼 개발자의 입장에서 편리할 뿐만 아니라 복잡한 상황에서 검정을 유연하게 확장할 수 있게 해줍니다.
교차표 검정을 단순히 chi-square test로만 기억하고 있으면 교란요인을 배제하지 못한 데이터에 그대로 적용할 수 없습니다.
그러나 교차표 검정이 (선형) 로지스틱 회귀분석의 특수한 경우라는 사실을 알고 있다면 교란요인을 보정하면 되므로 쉽게 문제를 해결할 수 있습니다.
이제 '모든 통계는 그저 선형모델'이라는 철학을 바탕으로 [지난 글](https://hanbin973.github.io/statistics/2021/04/04/complex-survey-2.html)의 결과에서 복합표본설계에서의 선형회귀분석 (OLS)을 어떻게 하는지 끌어내겠습니다.
이 철학만 있다면 모든 결과는 앞선 결과의 재활용이라는 점을 쉽게 알아차릴 수 있을 것입니다.

## 분산 추정 (3)
이전 글에서 1단계 집락추출이 단순표본설계인 2단계 집락표본설계의 총량의 분산추정식이 다음이 됨을 보였습니다. 

$$
(1-\frac{n_c}{C})
\frac{n_c}{n_c-1}
\sum_{c \in A_1} [
	(\sum_{i \in B_c} w_{ci} y_{ci})
	- \frac{1}{n_c}{\sum_{d \in A_1}(\sum_{i \in B_d} w_{di} y_{di})}
			
]^2
$$

특이하게도 국민건강영양조사는 이 식을 다음과 같이 씁니다.

$$
\begin{align}
&(1-\frac{n_c}{C})
\frac{n_c}{n_c-1}
\sum_{c \in A_1} [
	(\sum_{i \in B_c} w_{ci} (y_{ci} - \hat{\overline{Y}}))
	- \frac{1}{n_c}{\sum_{d \in A_1}(\sum_{i \in B_d} w_{di} (y_{di}- \hat{\overline{Y}}))}
			
]^2 \\

=&
(1-\frac{n_c}{C})
\frac{n_c}{n_c-1}
\sum_{c \in A_1} [
	(\sum_{i \in B_c} w_{ci} e_{ci})
	- \frac{1}{n_c}{\sum_{d \in A_1}(\sum_{i \in B_d} w_{di} e_{di})}
			
]^2
\end{align}
$$

$e_{ci} = y_{ci} - \hat{\overline{Y}}$으로 [원시자료 이용지침서](https://knhanes.cdc.go.kr/knhanes/sub03/sub03_02_05.do)에서는 잔차라는 표현을 씁니다.
잔차라뇨?
잔차는 흔히 회귀분석에서 결과변수에서 설명변수의 영향을 빼고 남은 나머지를 가리키는 말입니다.
이 표현이 평균 혹은 총량의 추정이 선형회귀분석의 일종임을 암시하고 있는 것입니다.
상수만 포함하는 다음의 선형모델은 평균의 추정과 정확하게 같은 값을 줍니다 (위에서 소개한 링크나 표를 참고하세요).

$$
\begin{align}
y = \mu + \epsilon, \quad \epsilon \sim \mathcal{N}(0, \sigma^2)
\end{align}
$$

위 모델의 모수인 $\mu$의 Ordinary Least Squre (OLS) 추정량 $\hat{\mu}$은 표본평균과 완전히 같습니다.
나아가 OLS에 가중치를 반영한 Weighted Least Square (WLS)를 쓰면 국건영에서 쓰는 가중치 평균과 완전히 같은 식을 얻습니다.
WLS 추정량이란 다음을 최적화하여 얻은 추정량을 말합니다.

$$
\hat{\mu} = \mathrm{argmin}_{\mu \in \mathbb{R}} \sum_{i=1}^N w_i (y_i - \mu)^2
$$

실제로 같은지 확인해보면

$$
\begin{align}
0=\frac{\partial}{\partial \mu} \sum_{i=1}^N w_i (y_i - \mu)^2
&= \sum_{i=1}^N - 2 w_i (y_i - \mu) \\
&= -2 \cdot [\sum_{i=1}^N w_i y_i - \mu \sum_{i=1}^N w_i ]
\end{align}
$$

로부터 같음을 알 수 있습니다.

$$
\hat{\mu} = \frac{\sum_{i=1}^N w_i y_i}{\sum_{i=1}^N w_i}
$$

## 표본 (sample), 모집단 (population) 그리고 초모집단 (superpopulation)

다소 개념적이면서 철학적인 얘기를 하겠습니다.
이는 우리가 표본설계를 통해 데이터를 수집하는 목적과 닿아있습니다: 우리가 얻은 데이터는 무엇이고 이로부터 무엇을 알 수 있을까요?

우리가 실제로 수집한 데이터는 표본 (sample)입니다. 
표본은 우리가 알고자 하는 모집단 (population)에서 추출된 측정된 데이터의 모임입니다.
표본에 평균이나 분산 등을 취하면 모집단의 성질을 추정(estimate)할 수 있습니다.
예를 들어, 여론조사는 여론조사 표본을 이용해 실제로 존재하는 유권자의 지지도를 알아보려 합니다.
여기서 여론조사 표본은 표본에 해당하고 전체 유권자의 집합은 모집단에 해당합니다.

그렇다면 표본이 모집단에서 온 것처럼 실제로 존재하는 유권자들은 어디서 온 것일까요?
이것은 다소 쌩둥맞은 질문처럼 들립니다.
여론조사는 실제로 존재하는 유권자의 표심을 알고자 하며 이는 한국을 예로 들면 4300만명의 유권자의 표심을 알고자 함입니다.
만약 우리가 관심법을 수련하여 4300만명의 마음 속을 들여다볼 수 있다면 우리의 물음은 여기서 끝납니다.
알고 싶은 것을 모두 알았으니 더 이상 고민을 할 필요가 없습니다.

그래서 이쯤에서 상황을 조금 더 꼬으겠습니다.
이제 단순한 표심을 넘어 월 소득이 유권자의 표심에 미치는 영향을 알고 싶습니다.
좀 더 구체적으로 월 소득이 500만원을 넘을 경우 민주당을 지지할 확률이 얼마인지 알고자 합니다.
이 질문에 대한 답을 얻는 가장 직관적인 방법은 전국의 월소득 500만원 이상인 유권자 중에 일부를 표본으로 뽑아 민주당 지지자의 비율을 구하는 것입니다.
더 정확한 방법은 앞선 경우와 마찬가지로 관심법을 발휘해 전국의 월소득 500만원 이상인 유권자 모두의 표심을 알아내 민주당 지지자의 비율을 계산하는 것입니다.
전자는 표본을 보는 것이고 후자는 모집단을 보는 것입니다.

그런데 여기서 한 단계 더 나아가 며칠이 지나 500만원을 버는 사람이 한 명 더 늘었다고 합시다.
그러면 모집단에서 얻은 월 500만원 이상 소득자의 민주당 지지율도 값이 바뀔 것입니다.
사람이 계속 늘어날 때마다 이 값을 계속 바뀌겠죠. 
그렇다면 이 사람들은 대체 어디서 오는 걸까요?
여기에 대한 답이 바로 초모집단 (superpopulation)입니다.

## 선형회귀분석 (1)

이제부터 벡터 미적분학의 표기법을 사용할 것입니다.
벡터는 볼드체로 표기하겠습니다.
행렬은 알파벳 대문자의 볼드체로 표기하겠습니다.
단, 경우에 따라 규칙을 어길 수도 있습니다.
본격적으로 시작하기에 앞서 OLS 복습을 하고 가겠습니다.
다음의 모델을 생각합시다.

$$ y = \mathbf{x}^{T} \boldsymbol{\beta}+ \epsilon $$

$\mathbf{x},\boldsymbol{\beta} \in \mathbb{R}^p$이고 나머지는 모두 실수 ($\mathbb{R}$)입니다.
관찰된 값 $(y_1, \mathbf{x}_1), \ldots, (y_n, \mathbf{x}_n)$을 위 모델에 맞춰 나열하면

$$
\begin{align}
y_1 &= \mathbf{x}_1^{T} \boldsymbol{\beta}+ \epsilon_1 \\
y_2 &= \mathbf{x}_2^{T} \boldsymbol{\beta}+ \epsilon_2 \\
& \quad \quad \vdots \\
y_n &= \mathbf{x}_n^{T} \boldsymbol{\beta}+ \epsilon_n \\
\end{align}
$$

가 되고 행렬을 이용하면 

$$ \mathbf{y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\epsilon} $$

가 됩니다.
$ \mathbf{y}, \boldsymbol{\epsilon} \in \mathbb{R}^n$, $\mathbf{X} \in \mathbb{R}^{n \times p}$ 입니다.
$ \boldsymbol{\beta} $는 이전과 같은 크기의 벡터입니다.
여기에 더해 $\boldsymbol{\epsilon} \perp \mathbf{X}$, $\mathbb{E}(\boldsymbol{\epsilon}) =0$입니다.
이전 글과 마찬가지로 $A = \{1, \ldots, n\}$은 뽑힌 표본의 집합입니다.

처음보는 분들은 식의 목록에서 하나의 단일한 식으로 넘어갈 때 헷갈릴 거라 생각합니다.
표기법을 좀 더 명확하게 설명하겠습니다.
저는 벡터를 쓸 때 특별한 말이 없을 경우 열벡터를 씁니다. 
즉, 

$$
\begin{align}
\mathbf{x} &= \begin{bmatrix}
x_{1} \\
x_{2} \\
\vdots \\
x_{n}
\end{bmatrix}
\end{align}
$$

입니다.
열벡터 $\mathbf{x}$를 전치하면 행벡터 $\mathbf{x}^{T}$를 얻고 

$$\begin{align}
\mathbf{x}^{T} = \begin{bmatrix} x_1 & x_2 & \cdots & x_n \end{bmatrix}
\end{align}$$

가 됩니다.
행렬을 이용한 단일 표현은 이 표기법을 바탕으로 식의 목록을 열방향 (수직한 방향)으로 쌓은 것입니다.
즉,

$$ \mathbf{y} 
= \begin{bmatrix}
y_{1} \\
y_{2} \\
\vdots \\
y_{n}
\end{bmatrix}

=\begin{bmatrix}
\mathbf{x}^T_{1} \\
\mathbf{x}^T_{2} \\
\vdots \\
\mathbf{x}^T_{n}
\end{bmatrix} 
\boldsymbol{\beta}

+\begin{bmatrix}
\epsilon_{1} \\
\epsilon_{2} \\
\vdots \\
\epsilon_{n}
\end{bmatrix}

=
\mathbf{X}\boldsymbol{\beta} + \boldsymbol{\epsilon} $$

입니다.

OLS 추정이란 관찰된 $\mathbf{y}$와 $\mathbf{X}$에 대해 다음의 최적화 문제의 답을 찾는 것입니다.

$$
\boldsymbol{\hat{\beta}} = \mathrm{argmin}_{\boldsymbol{\beta} \in \mathbb{R}^p} (\mathbf{y} - \mathbf{X}\boldsymbol{\beta})^T(\mathbf{y} - \mathbf{X}\boldsymbol{\beta})
$$

이제부터 벡터와 행렬의 미적분을 할 것인데 벡터의 표기법에 따라 전체적인 표기법이 크게 달리집니다.
오해를 막기 위해 다시 한번 열벡터 표기법을 사용함을 밝히며 미적분 공식은 [별도의 글](https://hanbin973.github.io/math/2021/04/06/vector-calc.html)을 참고하십시오.
위 식의 도함수가 0이 되는 $\boldsymbol{\beta}$를 찾으면 

$$
0= 2 \cdot (\mathbf{y}-\mathbf{X}\boldsymbol{\beta})^T (-\mathbf{X}) = -2 \mathbf{y}^T \mathbf{X} + 2\boldsymbol{\beta}^T \mathbf{X}^T \mathbf{X}
$$

으로부터 

$$ \boldsymbol{\hat{\beta}} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}$$

가 됨을 알 수 있습니다.
이 추정량은 $\mathbb{E}(\boldsymbol{\hat{\beta}}) = \boldsymbol{\beta}$를 만족하는 불편추정량입니다.
이제 $\boldsymbol{\hat{\beta}}$의 분산을 알아볼 차례입니다.
다소 복잡해보이지만 이 값을 계산하기 위해 알아야할 것은 $\mathbf{y}$의 분산 뿐입니다.
왜냐하면 $\mathbf{X}$는 이미 관찰되어 고정됐다고 보고 $\boldsymbol{\hat{\beta}}$을 계산하기 때문입니다.

$$
\begin{align}
\mathrm{Var}(\boldsymbol{\hat{\beta}}|\mathbf{X}) &= [(\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T] \mathrm{Var}(\mathbf{y}|\mathbf{X}) [(\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T]^T\\

&= (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathrm{Var} (\mathbf{y}|\mathbf{X}) \mathbf{X} (\mathbf{X}^T \mathbf{X})^{-1}  \\

&= (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathrm{Var} (\mathbf{X}\boldsymbol{\beta} + \boldsymbol{\epsilon}|\mathbf{X}) \mathbf{X} (\mathbf{X}^T \mathbf{X})^{-1}  \\

&= (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathrm{Var} (\boldsymbol{\epsilon}|\mathbf{X}) \mathbf{X} (\mathbf{X}^T \mathbf{X})^{-1} \\

&= (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathrm{Var} (\boldsymbol{\epsilon}) \mathbf{X} (\mathbf{X}^T \mathbf{X})^{-1} \\

&= (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbb{E} (\boldsymbol{\epsilon}\boldsymbol{\epsilon}^T) \mathbf{X} (\mathbf{X}^T \mathbf{X})^{-1}

\end{align}
$$

그런데 $\mathrm{Var}(\mathbf{y}|\mathbf{X}) = \mathrm{Var}(\boldsymbol{\epsilon}|\mathbf{X})$ 이므로 ($\mathbf{X}\boldsymbol{\beta}$가 조건부 $\mathbf{X}$하에서 상수) 잔차 $\boldsymbol{\epsilon}$의 분산만 알면 다 알게 됩니다.
참고로 위 계산에서 $\mathrm{Var}(\mathbf{AX}) = \mathbf{A}\mathrm{Var}(\mathbf{X})\mathbf{A}^T$를 썼습니다.
우리의 철학을 떠올리면 국건영 원시자료 이용지침서에 잔차를 써둔 부분이 이해가 되기 시작하는 대목입니다.

그럼 첫번째 단락에서 얻은 결과가 이 공식에서 똑같이 나오는지 확인하겠습니다.
$\mathbf{X} = \begin{bmatrix} 1 & 1 & \cdots & 1 \end{bmatrix}^T \in \mathbb{R}^{n \times 1}$, $\boldsymbol{\beta} = \begin{bmatrix} \mu \end{bmatrix} \in \mathbb{R}^{1}$로 두면 위 모델은 상수항만 포함하는 모델로 환원됩니다.
상단의 분산공식에 이 값을 대입하면

$$
\mathbf{X}^T \mathbf{X} = \begin{bmatrix} 1 & 1 & \cdots & 1 \end{bmatrix} \begin{bmatrix} 1 & 1 & \cdots & 1 \end{bmatrix}^T = n
$$

그리고 

$$
\mathbf{X}^T \mathbb{E} (\boldsymbol{\epsilon}\boldsymbol{\epsilon}^T) \mathbf{X} = \mathbb{E}(\sum_{i \in A} \sum_{i \in A} \epsilon_i \epsilon_j)
$$

로부터 

$$
\begin{align}
\mathrm{Var}(\boldsymbol{\hat{\beta}}|\mathbf{X}) &= \mathbb{E} (\frac{1}{n^2} \sum_{i \in A} \sum_{j \in A} \epsilon_i \epsilon_j)\\

&= \mathbb{E}(\frac{1}{n^2} \sum_{i \in U} \sum_{j \in U} I(i \in A)\epsilon_i I(j \in A) \epsilon_j) \\

&= \sum_{i \in U} \sum_{j \in U} \frac{\mathbb{E}(I(i \in A, j \in A))}{n^2} \epsilon_i \epsilon_j \\

&= \sum_{i \in U} \sum_{j \in U} \frac{\pi_{ij}}{n^2} \epsilon_i \epsilon_j \\

&= \sum_{i \neq j \in U} \frac{n-1}{N(N-1)n} \epsilon_i \epsilon_j + \sum_{i=j \in U} \frac{1}{Nn} \epsilon_i \epsilon_j \\

&= \sum_{i,j \in U} \frac{1}{Nn} \frac{n-1}{N-1} \epsilon_i \epsilon_j + \frac{N-n}{N-1} \sum_{i=j \in U} \frac{1}{Nn} \epsilon_i \epsilon_j \\

\end{align} 
$$

가 됨을 알 수 있습니다.













