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

# {{ site.tagline }}

{: .mb-2 }
{{ site.description }} <span title="https://jarv.is/" class="wave">👋</span>
{: .fs-6 .fw-300 }

{{ course_vars.quarter }}
{: .md-badge-purple }

{{ course_vars.building }}
{: .md-badge-purple }

{{ course_vars.timings }}
{: .md-badge-purple }

{% include staffer.html staff=staff nobio='true' %}

{: .important }
Please note that due to technical issues with podcast, the recordings from SP'25 were deleted and I only have recordings from last year. The slides may be slightly altered in places, but most of the changes are in appearances and memes 😁. The content is still moreover the same.
This is why the pdf slides and videos slides might be slightly different, but do not fret! There are no exams (check out the exam section for more), so the content being the same is largely conducive for your projects!


{: .important }
  - Kyle's OH (PDT): Thursday 5:00pm - 6:00pm [zoom link](https://ucsd.zoom.us/j/4288626123?pwd=TWpyQW5nZkpUTWJvU0YzejQyY25Sdz09)
  - Quirine OH (PDT): Tursday 8:00am - 9:00am [zoom link](https://ucsd.zoom.us/j/95336512099)
  - TA Discussion Session: Tuesday & Thursday 2:30 pm - 3:30pm (PDT) [zoom link](https://ucsd.zoom.us/j/96222015762)

<!-- **{{ course_vars.announcement.text }}** -->

{% for week in calendar %}
  {% include week.html week=week %}
{% endfor %}
