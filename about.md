---
layout: page
title: About 
subtitle: curriculum.vitae
---

<span style="float: right; "><a href="{{ '/assets/cv.pdf' | prepend: site.baseurl }}"><strong> CV [PDF] </strong></a> </span>
<br>


<h2> Education </h2>
<ul style="line-height: 110%;">
	{% for institution in site.data.edu %}
		<li>
			{{ institution.department }}, {{ institution.name }}
			{{ institution.degree }} in {{ institution.major }}, {{ institution.term }}
		</li>
	{% endfor %}
</ul>

<h2> Programming and Computer Skills </h2>

<h2> Language </h2> 

