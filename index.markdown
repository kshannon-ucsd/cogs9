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

# UCSD Cogs 9 - Intro to Data Science

{{ variables.quarter }}
{: .label .label-purple .fs-1 }

{{ variables.building }}
{: .label .label-purple .fs-1 }

{{ variables.timings }}
{: .label .label-purple .fs-1 }

**Instructor** <br/> {{ variables.instructor.name }} - [[{{ variables.instructor.email }}]](mailto:{{ variables.instructor.email }}) 

**Teaching Assistants (TAs)** {% for ta in variables.teaching_assistants %} <br/> {{ ta.name }} - [[{{ ta.email }}]](mailto:{{ ta.email }}) {% endfor %} 

**Instructional Assistants (IAs)** {% for ia in variables.instructional_assistants %} <br/> {{ ia.name }} - [[{{ ia.email }}]](mailto:{{ ia.email }}) {% endfor %} 

{: .fs-3 }

## Welcome to Cogs 9!

We are all very excited that you decided to join us on this whirlwind tour of data science. All the information you need and due dates are located on this website. The syllabus, and links to the assignments/quizzes/exams are located on the left under the side nav panel. We will make every effort to record class lectures, as attendance is not mandatory, but highly encouraged. Discussion section attendance the first/second week is very important because group assignments will occur in section. This class has a large amount of group project work (by design) to reflect the group nature of data science projects in the workplace.  
{: .fs-3 }
If you have any issues or have any questions, please first review the syllabus, as it has all the information pertaining to logistics and structure. If you still have any doubts please see the contact course staff link to determine how best to get a hold of us. I personally want to meet and interact with as many students as possible, but there are limited staff and many students. So we must use communication channels to facilitate a high student to staff ratio.  
{: .fs-3 }
We look forward to teaching and working with all of you and hope to meet you in office hours.
Cheers,  
Cogs 9 Course Staff
{: .fs-3 }

**Class Discord chat server:** {{ variables.discord_link }}  
**Class Gradescope link:** {{ variables.gradescope_link }}  
**Gradescope entry code:** {{ variables.gradescope_entry_code }} 

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
