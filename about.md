---
layout: page
title: About 
subtitle: curriculum.vitae
---

<span style="float: right; "><a href="{{ '/assets/cv.pdf' | prepend: site.baseurl }}"><strong> CV [PDF] </strong></a> </span>
<br>

<h2> Education </h2>
<div class='aboutbox-out'>
	<div class='aboutbox-in'>
		<ul style="line-height: 200%; list-style: none; padding: none;">
			{% for institution in site.data.edu %}
				<li> 
					<span style='font-weight: bold;'> {{ institution.name }} </span>
					<span style='text-align: right;'> {{ institution.place }} </span>
				</li>
				{% for department in institution.departments %}
					<li style="line-height: 150%; text-align: right;">
						{{ department.name }} <br>
						<i> {{ department.degree }} in {{ department.major }}, {{ department.term }} </i>
					</li>
				{% endfor %}
			{% endfor %}
		</ul>
	</div>
</div>

<h2> Programming and Computer Skills </h2>

<h2> Language </h2> 

