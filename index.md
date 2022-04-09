---
layout: mainpage
title: Hanbin Lee's Homepage
---

## News 
<p class="message">
  I'm applying for a PhD in 2024. Feel free to contact me if we share any research interests.
</p>

## Bio
I'm an undergraduate student at Department of Medicine, Seoul National University College of Medicine.
My research interest primarily lies in the intersection of causal inference and population genetics.
Currently, I work in Prof. [Buhm Han](https://hanlab.snu.ac.kr) laboratory.

At the mean time, I enjoy tennis and search for delicious dishes.

## Education

### Seoul National University
- M.D at Department of Medicine (2016 - )
- B.S. Mathematics at Department of Mathematical Sciences (2016 - )


## Research

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
								{{ paper.year }}
							</li>
						{% endfor %}
						{% if format.name == 'Publications' %}
						*: Equal contribution
						{% endif %}
					</ul>
				</div>
			</div>
		</li>
		
	{% endfor %}
</ul>
