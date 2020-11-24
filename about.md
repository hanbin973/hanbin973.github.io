---
layout: page
title: About 
subtitle: curriculum.vitae
---

<span style="float: right; "><a href="{{ '/assets/cv.pdf' | prepend: site.baseurl }}"><strong> CV [PDF] </strong></a> </span>
<br>

<h2> Education </h2>
<ul style="line-height: 200%; list-style: none;">
	{% for institution in site.data.edu %}
		<li> 
			<b> {{ institution.name }} </b> <br> 
			{{ institution.place }}
		</li>
		{% for department in institution.departments %}
			<li style="line-height: 150%; text-align: right;">
				{{ department.name }} <br>
				<i> {{ department.degree }} in {{ department.major }}, {{ department.term }} </i>
			</li>
		{% endfor %}
	{% endfor %}
</ul>

<h2> Programming and Computer Skills </h2>

<h2> Language </h2> 

