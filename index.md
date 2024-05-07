---
layout: mainpage
---

<span style="color:grey">Updated on May 7th, 2024</span>
___

## About
![](profile.jpg){: width="55%"}

I study how various stochastic forces in evolutionary processes shape statistical inference.
More generally, I leverage mechanistic theories of biology to improve inference and computation.

I'm currently working on the following topics:
- Graphical algorithms and tree sequences for scalable statistical genetics
- Phylogenetic constraints of molecular languagle models

Contact: <hblee@umich.edu>


## Education

### University of Michigan, Ann Arbor
- Doctor of Philosophy, Department of Statistics (2024.9 -)

### Seoul National University
- Doctor of Medicine, Department of Medicine (2016.3 - 2023.8)
- Bachelor of Mathematics, Department of Mathematical Sciences (2017.3 - 2023.8)

## Professional service
### Peer review
_International Journal of Epidemiology_,
_Nature Communications_

---

## Publications

<ul style='list-style: none; padding: 0px;'>
    <b>*:</b> Equal contribution
	{% for format in site.data.research %}
		<li>
			<h3 class='pub-format'> {{ format.name }} </h3>
			<div class='pubbox-out'>
				<div class='pubbox-in'>
					<ul style='list-style: none; padding: 0px; font-size: 0.8em;'>
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
						{% endif %}
					</ul>
				</div>
			</div>
		</li>
		
	{% endfor %}
</ul>
