---
layout: page
title: 👩‍🏫 Staff
description: A listing of all the course staff members.
nav_order: 20
---

# 👩‍🏫 Staff

{% assign staff_vars = site.data[site.data_folder].staff %}

{% for staff in staff_vars %}
<div class="role">
  {% include staffer.html staff=staff %}
</div>
{% endfor %}
