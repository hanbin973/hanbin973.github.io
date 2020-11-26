---
layout: page
title: Research
subtitle: publications.posters.talks
---

<ul style='list-style: none; padding: 0px;'>
	{% for format in site.data.research %}
		<li>
			<h2 class='pub-format'> {{ format.name }} </h2>
			<ul style='list-style: none; padding: 0px;'>
				{% for paper in format.papers %}
					<li>
						{{ paper.author }} {{ paper.name }} <i>{{ paper.journal }}</i> {{ paper.year }}
					</li>
				{% endfor %}
			</ul>
		</li>
	{% endfor %}
</ul>


