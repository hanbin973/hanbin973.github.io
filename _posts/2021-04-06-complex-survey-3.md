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
WLS란 다음을 최적화하여 얻은 추정량을 말합니다.

$$
\hat{\mu} = \mathrm{argmin}_{\mu \in \mathbb{R}} \sum_{i=1}^N w_i (y_i - \mu)^2
$$

실제로 같은지 확인해보면

$$
\begin{align}
\frac{\partial}{\partial \mu} \sum_{i=1}^N w_i (y_i - \mu)^2
&= \sum_{i=1}^N - 2 w_i (y_i - \mu) \\
&= -2 \cdot [\sum_{i=1}^N w_i y_i + \mu \sum_{i=1}^N w_i ]
\end{align}
$$

로부터 같음을 확인할 수 있습니다.

$$
\hat{\mu} = \frac{\sum_{i=1}^N w_i y_i}{\sum_{i=1}^N w_i}
$$


## 선형회귀분석






