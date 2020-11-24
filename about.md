---
layout: page
title: About 
subtitle: curriculum.vitae
---

<span style="float: right; "><a href="{{ '/assets/cv.pdf' | prepend: site.baseurl }}"><strong> CV [PDF] </strong></a> </span>
<br>

<ul>
	{% for section in site.data.edu %}
		<li>
			<h2> {{ section.name }} </h2>
		</li>
	{% endfor %}
</ul>
