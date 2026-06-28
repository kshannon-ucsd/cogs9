---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults
title: 🏠 Home
layout: home
nav_exclude: false
nav_order: 1
---

{% assign course_vars = site.data[site.data_folder].course %}
{% assign staff_vars = site.data[site.data_folder].staff %}
{% assign calendar = site.data[site.data_folder].calendar %}
{% assign staff = staff_vars[0] %} <!-- Cannot change this to instructor = because it will break the staffer.html include. If this needs to be instructor, then include.staff needs to be used as the variable in staffer.html  -->

# Introduction to Data Science - Summer 2026

<span title="https://jarv.is/" class="wave">👋</span> Welcome to Cogs 9 where we understand data and how it shapes our world.
{: .fs-6 .fw-300 .mb-2 }

{{ course_vars.quarter }}
{: .md-badge-purple }

{{ course_vars.building }}
{: .md-badge-purple }

{{ course_vars.timings }}
{: .md-badge-purple }

{% include staffer.html staff=staff nobio='true' %}

{: .important }
This is a remote asynchronous class. Therefore, lectures have been **pre-recorded**. Also, all quizzes and HW assignments are open and you can work on them at your own pace, just be mindful of the due dates for each. There is no final exam in this class, just a final group project.


{: .highlight }
**Joining the class late?** Summer moves fast. Read the [Joining Late]({{ '/joining-late' | relative_url }}) page right away for the few steps to get set up (Piazza, Gradescope, a project group) and stay eligible for full credit.

### Office Hours
{: .home-h }

Live help on Zoom. Bring questions about lectures, assignments, or the project.

{% for oh in course_vars.office_hours %}- **{{ oh.name }}** (instructor): {{ oh.day }} {{ oh.time }}, [Zoom link]({{ oh.zoom_link }})
{% endfor %}{% for d in course_vars.discussion_sections %}- **{{ d.ta }}** (TA): during the Project Studio sessions below
{% endfor %}

### Project Studio
{: .home-h }

Project Studio is live working time for your group project on Zoom. There are three sessions every week; drop into whichever fits your schedule (you do not need to attend all three). Staff are there to answer questions and help your team make progress.

| Session | When | Zoom |
|:--|:--|:--|
| Tuesday (afternoon) | Tue 2:30-3:30pm | TBD |
| Thursday (afternoon) | Thu 2:30-3:30pm | TBD |
| Tuesday (evening) | Tue 9:00-10:00pm | [Zoom link](https://ucsd.zoom.us/j/4288626123?pwd=TWpyQW5nZkpUTWJvU0YzejQyY25Sdz09) |

See the [Project Studio]({{ '/final-group-project/group-work-primer' | relative_url }}) page for the weekly project plan and group sign-up.

<!-- **{{ course_vars.announcement.text }}** -->

### Course Calendar
{: .home-h }

Lectures, readings, and due dates, laid out week by week.

{% for week in calendar %}
  {% include week.html week=week %}
{% endfor %}
