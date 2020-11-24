---
layout: page
title: Research
subtitle: publications.posters.talks
---

<ul style='list-style: none;'>
	{% for format in site.data.research %}
		<li>
			<h2 style='text-align: center;'> {{ format.name }} </h2>
		</li>
	{% endfor %}
</ul>


