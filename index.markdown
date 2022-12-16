---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults
title: Welcome
layout: default
nav_exclude: false
nav_order: 1
---

{% assign variables = site.data[site.data_folder].variables %}
{% assign course_calendar = site.data[site.data_folder].course_calendar %}

{: .text-grey-dk-200 .lh-0 }
# UCSD Cogs 9 Intro to Data Science

{{ variables.quarter }}
{: .md-badge-purple }

{{ variables.building }}
{: .md-badge-purple }

{{ variables.timings }}
{: .md-badge-purple }


**Instructor** <br/> {{ variables.instructor.name }} - [[{{ variables.instructor.email }}]](mailto:{{ variables.instructor.email }}) 

**Teaching Assistants (TAs)** {% for ta in variables.teaching_assistants %} <br/> {{ ta.name }} - [[{{ ta.email }}]](mailto:{{ ta.email }}) {% endfor %} 

**Instructional Assistants (IAs)** {% for ia in variables.instructional_assistants %} <br/> {{ ia.name }} - [[{{ ia.email }}]](mailto:{{ ia.email }}) {% endfor %} 

{: .fs-3 }

## Welcome

We are all very excited that you decided to join us on this whirlwind tour of data science. All relevant info, e.g. due dates, assignment links, etc. are found on this website.
We look forward to teaching and working with all of you and hope to meet you in office hours.
Cheers,  
Cogs 9 Course Staff
{: .fs-3 }

Should you have any questions or doubts:
  1. First review this website and syllabus
  2. Still having an issue? Use this form [link here (style as button)] to get help

## Complete The Following

1. Sign up for class Discord server here {{ variables.discord_link }}
2. Sign up for class Gradescope
   -  link-{{ variables.gradescope_link }}
   -  **entry code:** {{ variables.gradescope_entry_code }}
   -  You must include your **Student ID** and **UCSD Email**
3. Start Reading 1 (add link here)
4. Make sure you attend section week 2, as final project groups will be formed

{: .info }
NOTE: When signing up for this class in **gradescope** make sure you include your **Student ID** and **UCSD Email**. You may need to update your profile to do this. Both of these are not optional.


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

<table style="table-layout: fixed; text-align: center; width: 100%;">
    <thead>
        <tr class="header">
            <th style="width: 25%;"> Date </th>
            <th style="width: 75%;"> Lecture </th>
        </tr>
    </thead>
    <tbody>
        {% for row in course_calendar %}
        <tr>
            <td> {{ row.date | date: "%a, %b %d" }} </td>
            <td> {% if row.link %} <a href="{{ row.link }}"> {{ row.title }} </a> {% else %} {{ row.title }} {% endif %} </td>
        </tr>
        {% endfor %}
    </tbody>
</table>
