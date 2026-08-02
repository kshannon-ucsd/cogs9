---
layout: default
title: Assignment 2 Demo (p-hacking)
has_children: false
parent: 📝 Assignments
nav_order: 4
permalink: /assignment/assignment-2-phacking-demo
---

<h2>Interactive p-hacking Demo</h2>

Use the interactive tool below to explore how choosing different variables can produce a "statistically significant" result (p &lt; 0.05). This is the hands-on companion to Assignment 2.

- Back to <a href="{{ '/assignment/assignment-2' | relative_url }}">Assignment 2</a>
- Open the demo full screen <a href="{{ '/assets/phacking/index.html' | relative_url }}" target="_blank" rel="noopener">view &#x2197;</a>

<div style="position: relative; width: 100%; height: 80vh; border: 1px solid #ccc; border-radius: 6px; overflow: hidden; margin-top: 1rem;">
  <iframe
    src="{{ '/assets/phacking/index.html' | relative_url }}"
    title="Hack Your Way to Scientific Glory - p-hacking demo"
    loading="lazy"
    style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;">
  </iframe>
</div>

<p style="margin-top: 1rem; font-size: 0.9em; color: #555;">
Credit: This demo is a self-hosted copy of "Hack Your Way to Scientific Glory" by
<a href="https://www.andrewheiss.com/" target="_blank" rel="noopener">Andrew Heiss</a>,
a recreation of the original FiveThirtyEight p-hacking interactive.
Source code: <a href="https://github.com/andrewheiss/hack-your-way" target="_blank" rel="noopener">github.com/andrewheiss/hack-your-way</a>.
</p>
