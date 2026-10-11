---
layout: mainpage
---

<span style="color:grey">Updated in May, 2026</span>

___

## About
![](https://lsa.umich.edu/content/michigan-lsa/stats/en/people/phd-students/Lee/jcr:content/profileImage.transform/profile_portrait/image.jpg){: width="25%"}

I'm a PhD student at the Department of Statistics at the University of Michigan, Ann Arbor.
My main areas of interest are population genetics, phylogenetics, and dynamical systems.
I strongly prefer mechanistic explanations over statistical descriptions.
Ordinary and partial differential equations are my best friends.

I'm currently working on the following problems:
- Evolutionary foundation of statistical genetics
- Augmenting phylogenetic models with neural networks
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
<span style="font-size: 0.8em;"><em>International Journal of Epidemiology</em>,
<em>Nature Communications</em>,
<em>Genetics (GSA)</em>,
<em>HGG Advances</em>,
<em>BMC Medical Research Methodology</em>,
<em>NAR Genomics and Bioinformatics</em>,
<em>Bioinformatics Advances</em></span>

---

## Publications

<ul style='list-style: none; padding: 0px;'>
    <div style="font-size: 0.8em;"> <b>*:</b> Equal contribution</div>
	{% for format in site.data.research %}
		<li>
			<h3 class='pub-format'> {{ format.name }} </h3>
			<div class='pubbox-out'>
				<div class='pubbox-in'>
					<ul style='list-style: none; padding: 0 0 0 1.25em; font-size: 0.8em;'>
						{% for paper in format.papers %}
							<li style='margin-bottom: 0.35em;'>
								<b>
								{{ paper.fauthor }}, 
								</b>
								{{ paper.author }} 
								<a href='{{ paper.doi }}'>{{ paper.name }}</a>. 
								<i>{{ paper.journal }}</i>,
								{{ paper.year }}
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
