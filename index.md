---
layout: mainpage
---

Here is my [CV](CV_LeeH.pdf); Contact: <hanbin973@snu.ac.kr>

## News 
<p class="message">
  I'm applying for a PhD in 2024. Feel free to contact me if we share any research interests.
</p>

## Bio
I hold a double major in medicine and pure mathematics.
My work lies in the intersection of causal inference and population/statistical genetics.
Recently, I'm working on identification of genetic associataion studies under various population genetic processes.

## Education
### Seoul National University
- Doctor of Medicine, Department of Medicine (2016 - 2023.2)
- Bachelor of Mathematics, Department of Mathematical Sciences (2016 - 2023.8)

---

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
