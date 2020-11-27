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
		<ul style="line-height: 200%; list-style: none; padding: 0px;">
			{% for institution in site.data.edu %}
				<li> 
					<span style='font-weight: bold; font-size: 110%;'> {{ institution.name }} </span>
					<span style='text-align: right; font-size: 80%;'> {{ institution.place }} </span>
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
<div class='aboutbox-out'>
	<div class='aboutbox-in'>
		<ul style="line-height: 200%; list-style:none; padding: 0px;">
			{% for lang in site.data.prog %}
				<li>
					<span style='font-weight: bold;'> {{ lang.name }} </span>
				</li>
				{% if lang.libs %}
					<li>
						{% for lib in lang.libs %}
							<code><span style='font-size: 90%;'>{{ lib.name }}</span></code> 
						{% endfor %}
					</li>
				{% endif %}
			{% endfor %}	
		</ul>
	</div>
</div>

<h2> Language </h2> 
<div class='aboutbox-out'>
	<div class='aboutbox-in'>
		<ul style="line-height: 200%; list-style:none; padding: 0px;">
			{% for lang in site.data.lang %}
				<li>
					<span style='font-weight: bold; font-size: 110%;'> {{ lang.name }} </span>
				</li>
			{% endfor %}	
		</ul>
	</div>
</div>

