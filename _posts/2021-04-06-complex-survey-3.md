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
예를 들어, 여론조사는 여론조사 표본을 이용해 실제로 존재하는 유권자의 표심을 알아보려 합니다.
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
그리고 사람이 계속 늘어날 때마다 이 값은 계속 바뀔 것입니다. 
이 사람들은 대체 어디서 오는 걸까요?
여기에 대한 답이 바로 초모집단 (superpopulation)입니다.

초모집단은 현실에 존재하는 모집단의 구성원의 출처라고 여겨지는 무한인구집단 (infinite-population)입니다.
초모집단은 무수히 많은 구성원으로 이뤄져 있으며 이 구성원은 어떤 규칙이나 법칙을 만족합니다.
예를 들어, 월 500만원 이상 유권자들로 이뤄진 초모집단의 구성원은 일정확률 $p$로 민주당을 지지하고 $1-p$의 확률로 민주당을 지지하지 않습니다.
$N$명으로 이뤄진 월 500만원 이상 유권자들로 이뤄진 모집단은 초모집단에서 온 $N$명의 구성원으로 이뤄져 있습니다.

초모집단의 규칙이 변하지 않을 것이라고 믿을만한 그럴듯한 이유가 있다면 (예를 들어, 물리법칙) 우리의 관심사는 현실에 존재하는 모집단을 넘어 그 모집단의 출처인 초모집단의 규칙을 이해하는 것이 됩니다.
이 경우에 현실의 모집단은 초모집단의 근사치고 표본은 모집단의 근사치로 작동합니다.
그래서 표본을 충분히 뽑으면 모집단에 대해 근사적으로 알 수 있고 다시 그 모집단이 충분히 커서 초모집단을 잘 근사한다면 표본에서 얻은 근사치가 초모집단을 적당히 잘 근사한다고 믿을 수 있습니다.

우리가 다루는 통계는 대체로 이 질문에 대한 답을 얻기 위함인 경우가 많습니다.
유권자의 표심은 시시각각 변하기에 고정된 규칙으로 이뤄진 초모집단을 상정하는 것이 부자연스러우나 비만인구에서의 심근경색 발생이나 우울증인구에서의 자살은 상대적으로 훨씬 고정된 규칙을 따를 것으로 기대됩니다.
이러한 구분이 중요한 이유는 우리의 질문이 모집단에 관한 것인지 (전체 유권자의 표심) 초모집단에 관한 것인지 (비만과 심근경색 사이의 생물학적 관계)에 따라 크게 달라지기 때문입니다.
이는 평균이나 분산을 계산함에 있어서도 마찬가지입니다.
모집단의 평균과 초모집단의 평균은 대개의 경우 다를테니까요.
분산 역시 모집단의 분산과 초모집단의 평균은 대체로 다를 것입니다.
따라서 모집단과 초모집단의 모수를 구분하기 위해 이제부터 모집단의 경우 $\mathbb{E}(\ldots|\mathcal{F})$로, 초모집단의 경우 아무런 표기 없이 $\mathbb{E}(\ldots)$로 적겠습니다.
분산도 마찬가지로 $\mathcal{F}$ 유무로 모집단의 분산과 초모집단의 분산을 구분할 것입니다.

## 복합 설계에서의 선형회귀분석 (1)

이제부터 벡터 미적분학의 표기법을 사용할 것입니다.
벡터는 볼드체로 표기하겠습니다.
행렬은 알파벳 대문자의 볼드체로 표기하겠습니다.
단, 경우에 따라 규칙을 어길 수도 있습니다.
통상적인 선형회귀분석을 공부하고 싶다면 [Hansen Econometrics](https://www.ssc.wisc.edu/~bhansen/econometrics/)의 3장을 추천합니다.

초모집단을 정의하겠습니다.
이 초모집단의 확률변수 $y$와 $\mathbf{x}$는 다음의 모델을 따릅니다.

$$ 
\begin{align}
y = \mathbf{x}^{T} \boldsymbol{\beta}+ \epsilon \\
\epsilon \perp \mathbf{x} \\
\mathbb{E}(\epsilon) = 0	
\end{align}
$$

$\mathbf{x},\boldsymbol{\beta} \in \mathbb{R}^p$이고 나머지는 모두 실수 ($\mathbb{R}$)입니다.
초모집단에서 생성된 모집단은 총 $N$명으로 이루어졌습니다.

$$
\begin{align}
y_1 &= \mathbf{x}_1^{T} \boldsymbol{\beta}+ \epsilon_1 \\
y_2 &= \mathbf{x}_2^{T} \boldsymbol{\beta}+ \epsilon_2 \\
& \quad \quad \vdots \\
y_N &= \mathbf{x}_N^{T} \boldsymbol{\beta}+ \epsilon_N \\
\end{align}
$$

이는 행렬을 이용하면 다음과 같이 축약할 수 있습니다.

$$ \mathbf{y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\epsilon} $$

$ \mathbf{y}, \boldsymbol{\epsilon} \in \mathbb{R}^N$, $\mathbf{X} \in \mathbb{R}^{N \times p}$ 입니다.
처음보는 분들은 식의 목록에서 하나의 단일한 식으로 넘어갈 때 헷갈릴 거라 생각합니다.
표기법을 좀 더 명확하게 설명하겠습니다.
저는 벡터를 쓸 때 특별한 말이 없을 경우 열벡터를 씁니다. 
즉, 

$$
\begin{align}
\mathbf{z} &= \begin{bmatrix}
z_{1} \\
z_{2} \\
\vdots \\
z_{n}
\end{bmatrix}
\end{align}
$$

입니다.
열벡터 $\mathbf{z}$를 전치하면 행벡터 $\mathbf{z}^{T}$를 얻고 

$$\begin{align}
\mathbf{z}^{T} = \begin{bmatrix} z_1 & z_2 & \cdots & z_n \end{bmatrix}
\end{align}$$

가 됩니다.
행렬을 이용한 단일 표현은 이 표기법을 바탕으로 식의 목록을 열방향 (수직한 방향)으로 쌓은 것입니다.
즉,

$$ \mathbf{y} 
= \begin{bmatrix}
y_{1} \\
y_{2} \\
\vdots \\
y_{N}
\end{bmatrix}

=\begin{bmatrix}
\mathbf{x}^T_{1} \\
\mathbf{x}^T_{2} \\
\vdots \\
\mathbf{x}^T_{N}
\end{bmatrix} 
\boldsymbol{\beta}

+\begin{bmatrix}
\epsilon_{1} \\
\epsilon_{2} \\
\vdots \\
\epsilon_{N}
\end{bmatrix}

=
\mathbf{X}\boldsymbol{\beta} + \boldsymbol{\epsilon} $$

입니다.

모집단 전체를 알고 있다면 간단하게 OLS 추정을 통해 초모집단의 모수 $\boldsymbol{\beta}$를 추정할 수 있습니다.
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
이 추정량은 $\mathbb{E}(\boldsymbol{\hat{\beta}}|\mathbf{X}) = \boldsymbol{\beta}$를 만족하는 불편추정량입니다.
이 추정량의 분산도 쉽게 계산할 수 있고 $\mathrm{Var}(\boldsymbol{\hat{\beta}}|\mathbf{X}) = (\mathbf{X}^T \mathbf{X})^{-1}\mathbf{X}^T \mathbb{E}(\boldsymbol{\epsilon}\boldsymbol{\epsilon}^T) \mathbf{X} (\mathbf{X}^T \mathbf{X})^{-1}$ 가 됩니다.
증명은 위에서 언급한 Hansen Econometrics 3장을 참고하세요.

## 복합 설계에서의 선형회귀분석 (2) 

모집단의 정보로 초모집단의 모수를 추정하는 방법을 알아봤고 이제는 표본의 정보로 모집단의 정보를 알아볼 차례입니다.
표본추출과정이 초모집단에서 모집단을 추출하는 것처럼 취급할 수 있다면, 예를 들어 무작위복원추출이 가능하다면 위의 추정을 그대로 사용할 수 있겠으나 복합표본설계는 비복원 추출일뿐만 아니라 표본 추출의 확률 또한 표본마다 다르기 때문에 위의 추정을 그대로 사용할 수 없습니다.
그대로 사용했을 때 어떻게 되는지는 이후에 따로 글을 쓰도록 하겠습니다.

표본의 집합 $A = \\{i_1, \ldots, i_n \\}$을 정의하고 그 크기가 $n$ ($<N$)이라고 하겠습니다. 
우리 일은 표본의 정보로 계산할 수 있는 $\mathbb{E}(\boldsymbol{\tilde{\beta}}|\mathcal{F}) =\boldsymbol{\hat{\beta}}$ 을 만족하는 $\boldsymbol{\hat{\beta}}$의 추정량 $\boldsymbol{\tilde{\beta}}$을 얻는 것입니다.
그러면 

$$
\mathbb{E}(\boldsymbol{\tilde{\beta}}|X) =
\mathbb{E}(\mathbb{E}(\boldsymbol{\tilde{\beta}}|\mathcal{F})|X) = 
\mathbb{E}(\boldsymbol{\hat{\beta}}|X) =
\boldsymbol{\beta}
$$

가 되어 표본으로 모수 $\boldsymbol{\beta}$을 추정할 수 있습니다.
분산 역시 총 분산의 법칙을 이용하면 마찬가지로 계산할 수 있습니다.


$$
\begin{align}
\mathrm{Var}(\boldsymbol{\tilde{\beta}}|X) &=

\mathrm{Var}(\mathbb{E}(\boldsymbol{\tilde{\beta}}|\mathcal{F})|X) + 
\mathbb{E}(\mathrm{var}(\boldsymbol{\tilde{\beta}}|\mathcal{F})|X) 
\\

&=\mathrm{Var}(\boldsymbol{\hat{\beta}}|X) + 
\mathbb{E}(\mathrm{Var}(\boldsymbol{\tilde{\beta}}|\mathcal{F})|X)
\end{align}
$$

그런데 위 계산을 실제로 하는 것은 매우 어렵습니다.
[이전 글](https://hanbin973.github.io/statistics/2021/04/04/complex-survey-2.html)만 봐도 고작 평균 하나 추정하는데 테일러 근사가 들어가야했습니다.
이는 총량의 Thompon-Horvitz 추정량이 선형이 아닐 뿐더러 ($Y$의 추정량과 $Y+c$의 추정량이 다릅니다) $x/y$가 $y$에 대한 선형함수가 아니기 때문입니다.
그래서 실제로 $\mathcal{F}$에 대한 평균과 분산을 계산하기 위해서는 근사를 통해 비선형적인 부분을 모두 선형적인 부분으로 바꿔줘야 합니다.
다음 단락에서는 앞서 소개한 테일러 근사를 이용한 선형화를 본격적으로 다루겠습니다.

## 테일러 선형화 (Taylor linearization)

$ \mathbf{F}: \mathbb{R}^{(p+1) \times N} \rightarrow \mathbb{R}^p $를 $\mathbf{z}_i \in \mathbb{R}^p$ ($i = 1, \ldots, p+1$)에 대해 $F(z_1, z_2, \ldots, z_{p+1}) = $로 정의합시다.








