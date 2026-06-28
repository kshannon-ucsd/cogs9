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

{: .mb-2 }
Understanding data and how it shapes the world around us
{: .fs-6 .fw-300 }

{: .fs-6 .fw-300 }
<span title="https://jarv.is/" class="wave">👋</span> Welcome to Cogs 9

{{ course_vars.quarter }}
{: .md-badge-purple }

{{ course_vars.building }}
{: .md-badge-purple }

{{ course_vars.timings }}
{: .md-badge-purple }

{% include staffer.html staff=staff nobio='true' %}

{: .important }
This is a remote asynchronous class. Therefore, lectures have been **pre-recorded**. Also, all quizzes and HW assignments are open and you can work on them at your own pace, just be mindful of the due dates for each. There is no final exam in this class, just a final group project.


{: .important }
{% for oh in course_vars.office_hours %}- **{{ oh.name }}** office hours ({{ oh.day }} {{ oh.time }}): {{ oh.location }}{% if oh.zoom_link %}, [zoom link]({{ oh.zoom_link }}){% endif %}
{% endfor %}

### Project Studio

Project Studio is live working time for your group project on Zoom. There are three sessions every week; drop into whichever fits your schedule (you do not need to attend all three). Staff are there to answer questions and help your team make progress.

| Session | When | Zoom |
|:--|:--|:--|
| Tuesday (afternoon) | Tue 2:30-3:30pm | TBD |
| Thursday (afternoon) | Thu 2:30-3:30pm | TBD |
| Tuesday (evening) | Tue 9:00-10:00pm | [Zoom link](https://ucsd.zoom.us/j/4288626123?pwd=TWpyQW5nZkpUTWJvU0YzejQyY25Sdz09) |

See the [Project Studio]({{ '/final-group-project/group-work-primer' | relative_url }}) page for the weekly project plan and group sign-up.

<!-- **{{ course_vars.announcement.text }}** -->

{% for week in calendar %}
  {% include week.html week=week %}
{% endfor %}
