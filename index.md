---
layout: mainpage
---

<span style="color:grey">Updated in May, 2026</span>

___

## About
![](https://lsa.umich.edu/content/michigan-lsa/stats/en/people/phd-students/Lee/jcr:content/profileImage.transform/profile_portrait/image.jpg){: width="25%"}

Any statistical and computational methods operate under the constraints imposed by the data generating process.
As such, I study how evolutionary processes shape statistical inference. 

I'm currently working on the following topics:
- Evolutionary basis of statistical genetics
- Random dynamical systems on manifolds

Contact: <hblee@umich.edu>


## Education

### University of Michigan, Ann Arbor
- Doctor of Philosophy, Department of Statistics (2024.9 -)

### Seoul National University
- Bachelor of Mathematics, Department of Mathematical Sciences (2017.3 - 2023.8)
- Doctor of Medicine, Department of Medicine (2016.3 - 2023.8)

## Professional service
### Peer review
_International Journal of Epidemiology_,
_Nature Communications_,
_Genetics (GSA)_,
_HGG Advances_,
_BMC Medical Research Methodology_,
_NAR Genomics and Bioinformatics_,
_Bioinformatics Advances_

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
