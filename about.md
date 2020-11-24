---
layout: page
title: About 
subtitle: curriculum.vitae
---

<span style="float: right; "><a href="{{ '/assets/cv.pdf' | prepend: site.baseurl }}"><strong> CV [PDF] </strong></a> </span>
<br>


<h2> Education </h2>
<ul style="line-height: 200%">
	{% for institution in site.data.edu %}
		<li style="line-height: 150%; text-align: right;">
			{{ institution.department }}, {{ institution.name }} <br>
			<i> {{ institution.degree }} in {{ institution.major }}, {{ institution.term }} </i>
		</li>
	{% endfor %}
</ul>

<h2> Programming and Computer Skills </h2>

<h2> Language </h2> 

