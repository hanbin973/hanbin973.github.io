---
layout: page
title: About 
subtitle: curriculum.vitae
---

<span style="float: right; "><a href="{{ '/assets/cv.pdf' | prepend: site.baseurl }}"><strong> CV [PDF] </strong></a> </span>
<br>


<h2> Education </h2>
{% for institution in site.data.edu %}
	<ul style="line-height: 0px;">
		<li>
			{{ institution.department }}, {{ institution.name }}
			{{ institution.degree }} in {{ institution.major }}, {{ institution.term }}
		</li>
	</ul>
{% endfor %}

<h2> Programming and Computer Skills </h2>

<h2> Language </h2> 

