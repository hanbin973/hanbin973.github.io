---
layout: page
title: Research
subtitle: publications.posters.talks
---

<ul style='text-align: center; list-style: none;'>
	{% for format in site.data.research %}
		<li>
			<h2> {{ format.name }} </h2>
		</li>
	{% endfor %}
</ul>


