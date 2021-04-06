---
layout: page
title:  "Complex survey (2)"
subtitle: "KNHANES의 평균 및 분산 추정"
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

## 분산 추정 (1)
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
\pi_{ci|c} &= \frac{m_c}{M_c} \\
\pi_{ci,cj|c} &= \frac{m_c(m_c-1)}{M_c(M_c-1)} \quad (i \neq j)
\end{align}
$$

이를 분산 식에 대입할 것인데 한 번에 다 넣고 계산하면 복잡하니 $\pi$가 들어간 식부터 정리합니다. 

$$
\frac{1}{\pi_{cd}} \frac{\pi_{cd} - \pi_c \pi_d}{\pi_c \pi_d} =
\begin{cases}
\frac{1-n_c/C}{n_c^2/C^2} & (c=d) \\
- \frac{1-n_c/C}{n_c^2/C^2} \frac{1}{n_c-1}
\end{cases}
$$

$$
\frac{1}{\pi_{ci,dj|c,d}} =
\begin{cases}
	\frac{1}{\pi_{ci|c} \pi_{dj|d}} = \frac{M_cM_d}{m_cm_d} & (c \neq d) \\
	\frac{1}{\pi_{ci|c}} = \frac{M_c}{m_c} & (c=d, i=j) \\
	\frac{1}{\pi_{ci,cj|c}} = \frac{M_c(M_c-1)}{m_c(m_c-1)} & (c=d, i \neq j)
\end{cases}
$$

$$
\frac{1}{\pi_{ci,cj|c}}
\frac{\pi_{ci,cj|c} - \pi_{ci|c}\pi_{cj|c}}{\pi_{ci} \pi_{cj}} =
\begin{cases}
	\frac{1}{\pi_{ci|c}} \frac{\pi_{ci|c} - \pi_{ci|c}^2}{\pi_{ci|c}^2 \pi_c^2} 
	= \frac{C^2}{n_c^2} \frac{1-m_c/M_c}{m_c^2/M_c^2} & (i=j) \\
	- \frac{C^2}{n_c^2} \frac{1-m_c/M_c}{m_c^2/M_c^2}\frac{1}{m_c-1} & (i \neq j)
\end{cases}
$$

참고로 다음 공식을 기억하세요.
비슷한 꼴의 변형을 자주 사용할 예정입니다.

$$
\begin{align}
\sum_{i} y_{ci}^2 - \frac{1}{m_c-1} \sum_{i \neq j} y_{ci} y_{cj} &=
\frac{m_c}{m_c-1} \sum_{i} y_{ci}^2 - \frac{1}{m_c-1} \sum_{i,j} y_{ci} y_{cj} \\
&= \frac{1}{m_c-1} \sum_i \sum_j (y_{ci}^2 - y_{ci}y_{cj}) \\
&= \frac{1}{m_c-1} \sum_i y_{ci} [\sum_j (y_{ci} - y_{cj})] \\
&= \frac{1}{m_c-1} \sum_i y_{ci} \cdot m_c \cdot (y_{ci} - \bar{y}_c) \\
&= \frac{m_c}{m_c-1} \sum_i [(y_{ci} - \bar{y}_c)^2 + \bar{y}_c(y_{ci}-\bar{y}_c)] \\
&= \frac{m_c}{m_c-1} \sum_i (y_{ci} - \bar{y}_c)^2
\end{align}
$$

분산추정량의 두번째 항을 정리하면

$$ 
\begin{align}
&\frac{C^2}{n_c^2} \frac{1-m_c/M_c}{m_c^2/M_c^2} \sum_{c \in A_1}
[\sum_{i \in B_c} y_{ci}^2 - \frac{1}{m_c-1}\sum_{i \neq j \in B_c} y_{ci}y_{cj} ] \\
=& \frac{C^2}{n_c^2} \frac{1-m_c/M_c}{m_c^2/M_c^2} \sum_{c \in A_1}
\frac{m_c}{m_c-1}
\sum_{i \in B_c} (y_{ci}-\bar{y}_c)^2 \\
=& \frac{C^2}{n_c^2} \frac{1-m_c/M_c}{m_c^2/M_c^2} \frac{m_c}{m_c-1}
\sum_{c \in A_1}
\sum_{i \in B_c} (y_{ci}-\bar{y}_c)^2
\end{align}
$$

이 됩니다 ($\bar{y}_c$는 집락의 표본평균입니다). 
정리된 꼴은 표본분산공식과 비슷한 꼴을 가진 친숙한 느낌을 줍니다.
다음은 분산추정공식의 첫항을 계산할 차례인데 이 부분 또한 두번째항과 비슷한 꼴임을 알 수 있습니다.

$$
\frac{1}{\pi_{cd}} \frac{\pi_{cd} - \pi_c \pi_d}{\pi_c \pi_d}
$$

과 

$$
\frac{1}{\pi_{ci,cj|c}}
\frac{\pi_{ci,cj|c} - \pi_{ci|c}\pi_{cj|c}}{\pi_{ci} \pi_{cj}}
$$ 

이 상당히 닮았습니다.
문제는 자명하게 독립된 첨자를 가진 항 둘로 나뉘는 $y_{ci} y_{dj} = y_{ci} \cdot y_{dj}$와 다르게 

$$
\sum_{i \in B_c} \sum_{j \in B_d} \frac{1}{\pi_{ci,dj|c,d}} y_{ci}y_{dj}
$$
는 $c$와 $d$의 첨자로만 구성된 두 개의 항으로 깔끔하게 나뉘지 않습니다.
그래서 두 개로 나뉘도록 하기 위해 식을 조금 변형하겠습니다.

$$
\begin{align}
\sum_{i \in B_c} \sum_{j \in B_d} \frac{1}{\pi_{ci,dj|c,d}} y_{ci}y_{dj}
&= \sum_{i \in B_c} \sum_{j \in B_d} \frac{1}{\pi_{ci|c} \pi_{dj|d}} y_{ci}y_{dj} \\
&+ \sum_{i \in B_c} \sum_{j \in B_d} [\frac{1}{\pi_{ci,dj|c,d}} - \frac{1}{\pi_{ci|c} \pi_{dj|d}}] y_{ci}y_{dj} \\

&= (\sum_{i \in B_c} \frac{1}{\pi_{ci|c}} y_{ci}) (\sum_{j \in B_d}  \frac{1}{\pi_{dj|d}} y_{dj}) \\
&+ \sum_{i \in B_c} \sum_{j \in B_d} [\frac{1}{\pi_{ci,dj|c,d}} - \frac{1}{\pi_{ci|c} \pi_{dj|d}}] y_{ci}y_{dj} 
\end{align}
$$ 

앞쪽은 의도한 대로 분리가 됐고 뒷항도 $c=d$인 경우만 제외하면 괄호 안의 값이 0이 되어 사라집니다.
이 식을 원래 식에 대입하여 정리하면 분산추정식의 첫 항은 두 개의 부분으로 분리됩니다.

$$
\begin{align}
&\sum_{c \in A_1} \sum_{d \in A_1} \frac{1}{\pi_{cd}}  \frac{\pi_{cd} - \pi_c  \pi_d}{\pi_c \pi_d}
\sum_{i \in B_c} \sum_{j \in B_d} \frac{1}{\pi_{ci,dj|c,d}} y_{ci}y_{dj} \\

=&
\sum_{c \in A_1} \sum_{d \in A_1} \frac{1}{\pi_{cd}} \frac{\pi_{cd} - \pi_c  \pi_d}{\pi_c \pi_d}
(\sum_{i \in B_c} \frac{1}{\pi_{ci|c}} y_{ci}) (\sum_{j \in B_d}  \frac{1}{\pi_{dj|d}} y_{dj}) \\
+& \sum_{c \in A_1} \frac{1}{\pi_c} \frac{\pi_c - \pi_c^2}{\pi_c^2} \sum_{i \in B_c} \sum_{j \in B_c} [\frac{1}{\pi_{ci,cj|c}} - \frac{1}{\pi_{ci|c} \pi_{cj|c}}] y_{ci}y_{cj}
\end{align}
$$

앞 부분을 둘째 항에서 했던 것처럼 정리하면

$$
\begin{align}
&\sum_{c \in A_1} \sum_{d \in A_1} \frac{1}{\pi_{cd}} \frac{\pi_{cd} - \pi_c  \pi_d}{\pi_c \pi_d}
(\sum_{i \in B_c} \frac{1}{\pi_{ci|c}} y_{ci}) (\sum_{j \in B_d}  \frac{1}{\pi_{dj|d}} y_{dj}) \\

=& \sum_{c \in A_1}\frac{1-n_c/C}{n_c^2/C^2}
[ 
(\sum_{i \in B_c} \frac{1}{\pi_{ci|c}} y_{ci})^2
-\frac{1}{n_c-1} \sum_{c \neq d \in A_1} (\sum_{i \in B_c} \frac{1}{\pi_{ci|c}} y_{ci}) (\sum_{j \in B_d}  \frac{1}{\pi_{dj|d}} y_{dj})] \\

=& \frac{n_c}{n_c-1}
\sum_{c \in A_1} \frac{1-n_c/C}{n_c^2/C^2} \sum_{c \in A_1} [
(\sum_{i \in B_c} \frac{1}{\pi_{ci|c}} y_{ci})
	- \frac{1}{n_c}{\sum_{d \in A_1}(\sum_{i \in B_d} \frac{1}{\pi_{di|d}} y_{di})}
		]^2

\end{align}  
$$

가 됩니다.
이 식 역시 다소 친숙한 형태를 갖는데 분산추정량의 둘째항을 정리했을 때 표본분산의 형태를 가졌던 것처럼 이 경우에는 각 집락의 총량에 대한 표본분산의 형태를 가집니다.
남은 뒤쪽을 정리하는 건 훨씬 쉽습니다.
$\pi$에 대한 공식들을 대입하면

$$
\begin{align}
&\sum_{c \in A_1} 
\frac{1}{\pi_c} \frac{\pi_c - \pi_c^2}{\pi_c^2}
\sum_{i \in B_c} \sum_{j \in B_c} [\frac{1}{\pi_{ci,cj|c}} - \frac{1}{\pi_{ci|c} \pi_{cj|c}}] y_{ci}y_{cj} \\

=&
\frac{M_c}{m_c}
\frac{M_c-m_c}{m_c} 
\frac{1-m_c/M_c}{n_c^2/C^2}
\sum_{c \in A_1}   [ \frac{1}{m_c-1} \sum_{i \neq j \in B_c} y_{ci}y_{cj} - \sum_{i \in B_c} y_{ci}^2] \\

=&
-\frac{M_c}{m_c}
\frac{M_c-m_c}{m_c} 
\frac{1-m_c/M_c}{n_c^2/C^2}
\frac{m_c}{m_c-1}
\sum_{c \in A_1} \sum_{i \in B_c}(y_{ci}- \bar{y}_c)^2
\end{align}
$$

마찬가지로 친숙한 형태가 됩니다.
이 식을 유심히 관찰하면 분산추정량의 두번째 부분과 거의 차이가 없다는 것입니다.
게다가 바로 위의 식이 부호가 음수이기 때문에 둘을 더하면 사라지지 않을까 하는 기대가 듭니다.

$$
\begin{align}
&\frac{C^2}{n_c^2} \frac{1-m_c/M_c}{m_c^2/M_c^2} \frac{m_c}{m_c-1}
\sum_{c \in A_1}
\sum_{i \in B_c} (y_{ci}-\bar{y}_c)^2 \\

=&
\frac{M_c}{m_c}
\frac{M_c}{m_c}
\frac{1-m_c/M_c}{n_c^2/C^2}
\frac{m_c}{m_c-1}
\sum_{c \in A_1} \sum_{i \in B_c}(y_{ci}- \bar{y}_c)^2
\end{align}
$$

$m_c << M_C$, 즉, 각 집락의 추출율이 작으면 두 항은 근사적으로 크기는 같고 부호가 반대가 되어 사라집니다.
놀랍게도 다음 단락에서 보겠지만 이는 집락에서 표본을 추출하는 방식과 무관하게 항상 성립합니다.

지금까지의 결과를 바탕으로 이번 단락의 결과를 요약하면 $m_c << M_C$ 일 때 각 단계가 단순표본설계인 2단계 집락표본설계의 분산추정량은 다음과 같습니다.

$$
\frac{1-n_c/C}{n_c^2/C^2} \frac{n_c}{n_c-1}
\sum_{c \in A_1} [
(\sum_{i \in B_c} \frac{1}{\pi_{ci|c}} y_{ci})
	- \frac{1}{n_c}{\sum_{d \in A_1}(\sum_{i \in B_d} \frac{1}{\pi_{di|d}} y_{di})}
		]^2
$$

## 분산 추정 (2)

앞 단락의 계산은 앞으로 반복적으로 할 식 변형에 익숙해지는 과정이었습니다.
이 단락에서는 앞선 단락에서 한 계산을 더 일반적인 경우에 대해서 할 것입니다.
기호의 차이일 뿐 똑같기 때문에 편하게 볼 수 있을 거라 생각합니다.

이번에도 마지막에는 

$$
\frac{1-n_c/C}{n_c^2/C^2} \frac{n_c}{n_c-1}
\sum_{c \in A_1} [
(\sum_{i \in B_c} \frac{1}{\pi_{ci|c}} y_{ci})
	- \frac{1}{n_c}{\sum_{d \in A_1}(\sum_{i \in B_d} \frac{1}{\pi_{di|d}} y_{di})}
		]^2
$$

만 남습니다.
여기에 약간의 변형만 가하면 원시자료 이용지침서에 있는 분산공식과 거의 똑같은 결과를 얻습니다.
$\pi_c = \frac{n_c}{C}$이므로 $\frac{1-n_c/C}{n_c^2/C^2}$에 있는 $n_c^2/C^2$을 시그마 안으로 옮겨서 분모에 있는 $\pi_{ci|c}$ 및 $\pi_{di|d}$에 붙여주면 $\pi_{ci} = \pi_{ci|c} \pi_c$로부터 다음을 얻습니다.

$$
\begin{align}
&(1-\frac{n_c}{C})
\frac{n_c}{n_c-1}
\sum_{c \in A_1} [
(\sum_{i \in B_c} \frac{1}{\pi_{ci}} y_{ci})
	- \frac{1}{n_c}{\sum_{d \in A_1}(\sum_{i \in B_d} \frac{1}{\pi_{di}} y_{di})}
		]^2 \\
=&
(1-\frac{n_c}{C})
\frac{n_c}{n_c-1}
\sum_{c \in A_1} [
(\sum_{i \in B_c} w_{ci} y_{ci})
	- \frac{1}{n_c}{\sum_{d \in A_1}(\sum_{i \in B_d} w_{di} y_{di})}
		]^2
\end{align}
$$

원시자료 이용지침서의 공식에는 $y_{ci}$ 대신 $y_{ci} - \hat{\overline{Y}}$가 들어있는데 똑같은 식입니다.
왜냐하면 $\sum_{c \in A_1}$안에 있는 앞 항과 뒷 항에서 똑같은 양만큼 $\hat{\overline{Y}}$가 빠졌기 때문에 전개해보면 사라지는 값이기 때문입니다. 
즉, 항등식입니다.

이제 결론을 봤으니 다시 본론으로 돌아갑시다. 
국민건강영양조사의 경우 1단계 집락 추출은 단순표본 추출입니다.
따라서 1단계에 대한 계산은 위에서 그대로 가져오면 되고 분산공식의 첫 항을 쪼갰을 때 나오는 음수 항과 분산공식의 둘째 항이 마찬가지로 사라지는지만 확인하면 됩니다.
즉, 

$$
\begin{align}
&\sum_{c \in A_1} \frac{1}{\pi_c} \frac{\pi_c - \pi_c^2}{\pi_c^2} \sum_{i \in B_c} \sum_{j \in B_c} [\frac{1}{\pi_{ci,cj|c}} - \frac{1}{\pi_{ci|c} \pi_{cj|c}}] y_{ci}y_{cj} \\

=&
\sum_{c \in A_1} \sum_{i \in B_c} \sum_{j \in B_c} 
\frac{1 - \pi_c}{\pi_c^2} 
\frac{1}{\pi_{ci,cj|c}}
\frac{\pi_{ci|c} \pi_{cj|c} - \pi_{ci,cj|c}}{\pi_{ci|c} \pi_{cj|c}} 
y_{ci}y_{cj} \\

=&
\sum_{c \in A_1} \sum_{i \in B_c} \sum_{j \in B_c} 
(1 - \pi_c)
\frac{1}{\pi_{ci,cj|c}}
\frac{\pi_{ci|c} \pi_{cj|c} - \pi_{ci,cj|c}}{\pi_{ci} \pi_{cj}} 
y_{ci}y_{cj}

\end{align}
$$


과

$$
\sum_{c \in A_1} \sum_{i \in B_c} \sum_{j \in B_c}
\frac{1}{\pi_{ci,cj|c}}
\frac{\pi_{ci,cj|c} - \pi_{ci|c}\pi_{cj|c}}{\pi_{ci} \pi_{cj}} y_{ci}y_{cj}
$$

를 비교하면 됩니다.











