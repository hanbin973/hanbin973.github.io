---
layout: page
title:  "Complex survey (2)"
subtitle: "국민건강영양조사"
date:	2021-04-04
comments: true
categories: ["Statistics"]
---

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

본격적인 얘기에 앞서 이 공식이 국민건강영양조사 원시자료 이용지침서에 등장하는 분산추정공식과 일치함을 보이도록 하겠습니다.






