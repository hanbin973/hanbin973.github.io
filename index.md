---
layout: mainpage
---

Contact: <hanbin973@snu.ac.kr>

## News 
<p class="message">
  I'm applying for a PhD in 2024. Feel free to contact me if we share any research interests.
</p>

## Bio
I'm an undergraduate student at Department of Medicine, Seoul National University College of Medicine.
My research interest primarily lies in the intersection of causal inference and population genetics.
Currently, I work in Prof. [Buhm Han](https://hanlab.snu.ac.kr) laboratory.
I'm largely interested in the philosophy of science and epistemology which makes me a strong proponent of the [feminist standpoint theory](https://www.jstor.org/stable/10.7591/j.ctt1hhfnmg).

At the mean time, I enjoy tennis and dining.

## Education

### Seoul National University
- M.D. at Department of Medicine (2016 - *current*)
- B.S. Mathematics at Department of Mathematical Sciences (2016 - *current*)

---

## Reserach interests
My current research goal is to promote identification as a central practice in scientific inquiry.

### The role of casual inference
The biggest contribution of the modern study on causality was establishing the [distinction](https://www.bradyneal.com/slides/2%20-%20Potential%20Outcomes.pdf) between *identification* and *estimation*.
In my opinion, recent biomedical research has focused largely on the latter while missing the essential components of identification.
Instead of focusing on identification, literature tend to accept post-hoc interpretation of estimation outputs without proper justification.
As a result, the meanings of research findings became very unclear and vague.

### Why population genetics?
I believe that population genetics has a potential to overcome the current limitations in biomedical research.
As one of the [first field](https://doi.org/10.1093/genetics/143.4.1499) to adopt graph-based causal reasoning, causality has been a central component of the field.
While most identification research focuses endogeneity issues such as establishing conditional exchangeability, my primary focus is on consistency and covariate distributions.
For example, when questioning the causal role of body-mass index on a health outcome, one must first precisely define [what really means to manipulate BMI](https://doi.org/10.1038/ijo.2008.82) which is a matter of consistency.
Addressing such questions is possible only with the support of proper domain-specific knowledge and theory where population genetics is a very likely candidate.


## Publications

<ul style='list-style: none; padding: 0px;'>
	{% for format in site.data.research %}
		<li>
			<h3 class='pub-format'> {{ format.name }} </h3>
			<div class='pubbox-out'>
				<div class='pubbox-in'>
					<ul style='list-style: none; padding: 0px;'>
						{% for paper in format.papers %}
							<li>
								<b>
								{{ paper.fauthor }}, 
								</b>
								{{ paper.author }} 
								<a href='{{ paper.doi }}'>{{ paper.name }}</a>. 
								<i>{{ paper.journal }}</i>,
								{{ paper.year }}<br>
								<b>
								Description:
								</b>
								{{ paper.description }}
								<br>
								<br>
							</li>
						{% endfor %}
						{% if format.name == 'Journals' %}
						*: Equal contribution
						{% endif %}
					</ul>
				</div>
			</div>
		</li>
		
	{% endfor %}
</ul>
