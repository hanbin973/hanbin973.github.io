---
layout: page
title: Research
subtitle: publications.posters.talks
---

<ul style='text-align: center;'>
	{% for format in site.data.research %}
		<li>
			<h2> {{ format.name }} </h2>
		</li>
	{% endfor %}
</ul>

<!--
<h2 style='text-align: center;'>Publications</h2>
<h2 style='text-align: center;'>Posters</h2>
<h2 style='text-align: center;'>Talks</h2>
<h2 style='text-align: center;'>ETC</h2>
>
