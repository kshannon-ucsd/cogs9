---
layout: default
title: Staff Information
has_children: false
nav_order: 9
permalink: /staff-info/
---

{% assign variables = site.data[site.data_folder].variables %}
{% assign course_calendar = site.data[site.data_folder].course_calendar %}

# Office Hours

- Zoom Info (links and passwords) <a href="https://docs.google.com/document/d/1I5w536c7VGTX5EWxvLZfmvtUnMBWB--qPsa48C_ekUA/edit?usp=sharing" target="_blank" rel="noopener">view &#x2197;</a> 
- Office Hour signup sheet <a href="https://docs.google.com/spreadsheets/d/1jtsbQL55JvpUGZjcG13DoCZRYn6nAzpSX5dWE48yVAc/edit?usp=sharing" target="_blank" rel="noopener">view &#x2197;</a> 


![Zoom](https://img.shields.io/badge/Zoom-2D8CFF?style=for-the-badge&logo=zoom&logoColor=white)

Office hours are a great place to personally interact. Beyond projects and course material, we are interested in your goals, career endeavors, and what you want to gain from COGS 9. Data Science is a rapidly changing field and there is always a lot to discuss. 

<table style="table-layout: fixed; text-align: center; width: 100%;">
    <thead>
        <tr class="header">
            <th style="width: 25%;"> Staff </th>
            <th style="width: 15%;"> Day </th>
            <th style="width: 35%;"> Time </th>
            <th style="width: 25%;"> Location </th>
        </tr>
    </thead>
    <tbody>
        {% for oh in variables.instructor.office_hours %}
        <tr>
            <td> {{ variables.instructor.name }} </td>
            <td> {{ oh.day }} </td>
            <td> {{ oh.time }} </td>
            <td> {{ oh.location }} </td>
        </tr>
        {% endfor %}
        {% for row in variables.teaching_assistants %}
            {% for oh in row.office_hours %}
            <tr>
                <td> {{ row.name }} </td>
                <td> {{ oh.day }} </td>
                <td> {{ oh.time }} </td>
                <td> {{ oh.location }} </td>
            </tr>
            {% endfor %}
        {% endfor %}
        {% for row in variables.instructional_assistants %}
            {% for oh in row.office_hours %}
            <tr>
                <td> {{ row.name }} </td>
                <td> {{ oh.day }} </td>
                <td> {{ oh.time }} </td>
                <td> {{ oh.location }} </td>
            </tr>
            {% endfor %}
        {% endfor %}
    </tbody>
</table>

If you are unable to join or are having other issues, please reach out after class (I tend to do impromptu office hours after each class if I have time) or in section. Additionally, we are more than happy, to set up additional 1:1 or 1:group meetings when necessary.
