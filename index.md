---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults
title: Home
layout: default
nav_exclude: false
nav_order: 1
---

{% assign variables = site.data[site.data_folder].variables %}
{% assign course_calendar = site.data[site.data_folder].course_calendar %}

{: .text-grey-dk-200 .lh-0 .pt-4 }
# Introduction to Data Science

{: .text-grey-dk-300 .fw-300 .lh-0 }
## COGS 9 - UC San Diego 

{{ variables.quarter }}
{: .md-badge-purple }

{{ variables.building }}
{: .md-badge-purple }

{{ variables.timings }}
{: .md-badge-purple }


**Instructor** <br/> {{ variables.instructor.name }} - [{{ variables.instructor.email }}](mailto:{{ variables.instructor.email }})

**Teaching Assistants (TAs)**
{% for ta in variables.teaching_assistants %} <br/> {{ ta.name }} - [{{ ta.email }}](mailto:{{ ta.email }}) {% endfor %}

**Instructional Assistants (IAs)**
{% for ia in variables.instructional_assistants %} <br/> {{ ia.name }} - [{{ ia.email }}](mailto:{{ ia.email }}) {% endfor %}
<!-- {: .fs-3 } -->

## Welcome <span title="https://jarv.is/" class="wave">👋</span> 

We are all very excited that you decided to join us on this whirlwind tour of data science. All relevant info, e.g. due dates, assignment links, etc. are found on this website.
We look forward to teaching and working with all of you and hope to meet you in office hours.
{: .fs-3 }

## Discussion Section Times

<table style="table-layout: fixed; text-align: center; width: 100%;">
    <thead>
        <tr class="header">
            <th style="width: 10%;"> Section </th>
            <th style="width: 10%;"> Day </th>
            <th style="width: 25%;"> Time </th>
            <th style="width: 15%;"> Location </th>
            <th style="width: 25%;"> Staff </th>
            <th style="width: 15%;"> Materials </th>
        </tr>
    </thead>
    <tbody>
        {% for ds in variables.discussion_sections %}
        <tr>
            <td> {{ ds.section }} </td>
            <td> {{ ds.day }} </td>
            <td> {{ ds.time }} </td>
            <td> {{ ds.location }} </td>
            <td> {{ ds.ta }}, {{ ds.ia }} </td>
            <td> <a href="{{ ds.materials }}"> view </a> </td>
        </tr>
        {% endfor %}
    </tbody>
</table>

## Course Calander

{% assign first_date = course_calendar[0].date | date: '%s' %}
{% assign first_day = course_calendar[0].date | date: '%w' %}
{% assign prev_week_no = 0 %}
<table style="table-layout: fixed; text-align: left; width: 100%;">
    <colspan>
        <col style="width: 25%;">
        <col style="width: 10%; border: none">
        <col style="width: 65%; border: none">
    </colspan>
    <thead>
        <tr class="header">
            <th colspan="3" style="padding-left:8%; font-size-adjust:0.75"> Week 0 </th>
        </tr>
    </thead>
    <tbody>
{% for row in course_calendar %}
    {% assign week_no = row.date | date: '%s' | minus: first_date | divided_by: 60 | divided_by: 60 | divided_by: 24 | plus: first_day | divided_by: 7 %}
    {% if week_no != prev_week_no %}
    </tbody>
</table>
<table style="table-layout: fixed; text-align: left; width: 100%;">
    <colspan>
        <col style="width: 25%;">
        <col style="width: 10%; border: none">
        <col style="width: 65%; border: none">
    </colspan>
    <thead>
        <tr class="header">
            <th colspan="3" style="padding-left:8%; font-size-adjust:0.75"> Week {{ week_no }} </th>
        </tr>
    </thead>
    <tbody>
    {% endif %}
    {% assign prev_week_no = week_no %}
        <tr>
            <td style="text-align: center"> {{ row.date | date: "%a, %b %d" }} </td>
            <td style="text-align: center">
              {% if row.label == "LECT" %} <span class="md-cal-badge md-cal-badge-blue"> {{ row.label }} </span>
              {% elsif row.label == "GLCT" %} <span class="md-cal-badge md-cal-badge-purple"> {{ row.label }} </span>
              {% elsif row.label == "CNCL" %} <span class="md-cal-badge md-cal-badge-red"> {{ row.label }} </span>
              {% elsif row.label == "ASSG" %} <span class="md-cal-badge md-cal-badge-green"> {{ row.label }} </span>
              {% elsif row.label == "EXAM" %} <span class="md-cal-badge md-cal-badge-gray"> {{ row.label }} </span>
              {% elsif row.label == "QUIZ" %} <span class="md-cal-badge md-cal-badge-green"> {{ row.label }} </span>
              {% elsif row.label == "EXTR" %} <span class="md-cal-badge md-cal-badge-yellow"> {{ row.label }} </span>
              {% else %}
                {% if row.label %} <span class="md-cal-badge md-cal-badge-black"> {{ row.label }} </span>
                {% endif %}
              {% endif %}
            </td>
            <td style="padding-left: 4%"> {% if row.link %} <a href="{{ row.link }}"> {{ row.title }} </a> {% else %} {{ row.title }} {% endif %} </td>
        </tr>
{% endfor %}
    </tbody>
</table>







<!-- extra credit

<h2>Mid quarter team eval</h2>
Use this Google form <a href="https://docs.google.com/forms/d/e/1FAIpQLSfYbYuYjYlyrCY50yjVe_ejOBMiIwq_3t0U4NTkVafsiFVwrA/viewform?usp=sf_link" target="_blank" rel="noopener">link &#x2197;</a>

This eval will close after the assignment 2 due date.

<h2>Final quarter team eval</h2>
Use this Google form <a href="https://docs.google.com/forms/d/e/1FAIpQLSeP8N88eSRuFNeZqk8NpcX24No2c9aCmHIMW-PjIkD5zQH_yg/viewform?usp=sf_link" target="_blank" rel="noopener">link &#x2197;</a>

This eval will close on Sunday week 10, before finals week.

<h2> CAPE reviews</h2>

CAPE reviews are a great opportunity to share with instructional staff what you thought about the course. I am always striving to improve and tweak the class so I read all my CAPE reviews and take them seriously. It gives you, the student body, a voice. I consider them important and thus if at least 70% of the class fills out CAPEs by the due date, I will award the whole class 5 points of extra credit.

Access CAPE reviews with this <a href="https://cape.ucsd.edu/" target="_blank" rel="noopener">link &#x2197;</a> -->