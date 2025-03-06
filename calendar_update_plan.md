# Calendar Update Plan

## Overview

This document outlines the plan for updating the course calendar for Spring 2025. The changes include:

1. Creating a new YAML file with the course schedule
2. Updating the week.html template to match the new structure

## 1. Calendar YAML File (`_data/sp25/calendar.yml`)

The new YAML file will follow this structure for each week:

```yaml
- week: [week number]
  title: "Week [week number] - [Descriptive title based on lecture topics]<br>
    <small>
      [Reading/Watching placeholder with emoji, alternating each week]
    </small>"
  days:
    - date: "[Tuesday date]"
      in_class: true
      events:
        - label: LEC [lecture number]
          type: lecture
          title: [Lecture title]
          slides: # Placeholder for slides
        - label: [HW/QUIZ/etc. if released]
          type: [hw/quiz/etc.]
          title: <b>[Assignment title] Released (due [date], 11:59 pm)</b>
          
    - date: "[Wednesday date]"
      in_class: true
      events:
        - label: DISC
          type: disc
          title: Discussion Section
          
    - date: "[Thursday date]"
      in_class: true
      events:
        - label: LEC [lecture number]
          type: lecture
          title: [Lecture title]
          slides: # Placeholder for slides
        - label: [HW/QUIZ/etc. if due]
          type: [hw/quiz/etc.]
          title: <b>[Assignment title] Due</b>
```

### Complete YAML Content

```yaml
- week: 1
  title: "Week 1 - Introduction to Data Science & Ethics<br>
    <small>
      📘 Read <a href='#'>Introduction to Data Science (TBD)</a>.<br>
    </small>"
  days:
    - date: "2025-04-01"
      in_class: true
      events:
        - label: LEC 1
          type: lecture
          title: What is DS
          slides: 
        - label: HW
          type: hw
          title: <b>Homework 1 Released (due Apr 10, 11:59 pm)</b>
        - label: QUIZ
          type: quiz
          title: <b>Reading Quiz 1 Released (due Apr 10, 11:59 pm)</b>
          
    - date: "2025-04-02"
      in_class: true
      events:
        - label: DISC
          type: disc
          title: Discussion Section
          
    - date: "2025-04-03"
      in_class: true
      events:
        - label: LEC 2
          type: lecture
          title: Ethics
          slides: 

- week: 2
  title: "Week 2 - Data Science Questions & Reproducibility<br>
    <small>
      🍿 Watch <a href='#'>Data Science in Practice (TBD)</a>.<br>
    </small>"
  days:
    - date: "2025-04-08"
      in_class: true
      events:
        - label: LEC 3
          type: lecture
          title: DS Questions
          slides: 
          
    - date: "2025-04-09"
      in_class: true
      events:
        - label: DISC
          type: disc
          title: Discussion Section
          
    - date: "2025-04-10"
      in_class: true
      events:
        - label: LEC 4
          type: lecture
          title: Reproducibility & Bias
          slides: 
        - label: HW
          type: hw
          title: <b>Homework 1 Due</b>
        - label: QUIZ
          type: quiz
          title: <b>Reading Quiz 1 Due</b>

- week: 3
  title: "Week 3 - Data Fundamentals & Collection<br>
    <small>
      📘 Read <a href='#'>Data Collection Methods (TBD)</a>.<br>
    </small>"
  days:
    - date: "2025-04-15"
      in_class: true
      events:
        - label: LEC 5
          type: lecture
          title: Data (Redo Databases Portion)
          slides: 
        - label: HW
          type: hw
          title: <b>Homework 2 Released (due Apr 24, 11:59 pm)</b>
        - label: QUIZ
          type: quiz
          title: <b>Reading Quiz 3 Released (due Apr 24, 11:59 pm)</b>
          
    - date: "2025-04-16"
      in_class: true
      events:
        - label: DISC
          type: disc
          title: Discussion Section
          
    - date: "2025-04-17"
      in_class: true
      events:
        - label: LEC 6
          type: lecture
          title: Data Collection
          slides: 
        - label: QUIZ
          type: quiz
          title: <b>Reading Quiz 2 Due</b>

- week: 4
  title: "Week 4 - Data Wrangling & Visualization<br>
    <small>
      🍿 Watch <a href='#'>Data Visualization Techniques (TBD)</a>.<br>
    </small>"
  days:
    - date: "2025-04-22"
      in_class: true
      events:
        - label: LEC 7
          type: lecture
          title: Data Wrangling
          slides: 
          code: 
        - label: QUIZ
          type: quiz
          title: <b>Reading Quiz 4 Released (due May 1, 11:59 pm)</b>
          
    - date: "2025-04-23"
      in_class: true
      events:
        - label: DISC
          type: disc
          title: Discussion Section - Form Project Groups (3-4 people/team)
          
    - date: "2025-04-24"
      in_class: true
      events:
        - label: LEC 8
          type: lecture
          title: Data Visualization
          slides: 
        - label: HW
          type: hw
          title: <b>Homework 2 Due</b>
        - label: QUIZ
          type: quiz
          title: <b>Reading Quiz 3 Due</b>

- week: 5
  title: "Week 5 - Exploratory Data Analysis & Communication<br>
    <small>
      📘 Read <a href='#'>Exploratory Data Analysis (TBD)</a>.<br>
    </small>"
  days:
    - date: "2025-04-29"
      in_class: true
      events:
        - label: LEC 9
          type: lecture
          title: EDA
          slides: 
          code: 
        - label: QUIZ
          type: quiz
          title: <b>Reading Quiz 5 Released (due May 22, 11:59 pm)</b>
          
    - date: "2025-04-30"
      in_class: true
      events:
        - label: DISC
          type: disc
          title: Discussion Section - Project Teams
          
    - date: "2025-05-01"
      in_class: true
      events:
        - label: LEC 10
          type: lecture
          title: Communicating
          slides: 
        - label: QUIZ
          type: quiz
          title: <b>Reading Quiz 4 Due</b>
        - label: PROJECT
          type: project
          title: <b>Group Project Topics Due</b>

- week: 6
  title: "Week 6 - Inferential Analysis & Data Literacy<br>
    <small>
      🍿 Watch <a href='#'>Statistical Inference in Data Science (TBD)</a>.<br>
    </small>"
  days:
    - date: "2025-05-06"
      in_class: true
      events:
        - label: LEC 11
          type: lecture
          title: Inferential Analysis
          slides: 
        - label: HW
          type: hw
          title: <b>Homework 3 Released (due May 22, 11:59 pm)</b>
          
    - date: "2025-05-07"
      in_class: true
      events:
        - label: DISC
          type: disc
          title: Discussion Section
          
    - date: "2025-05-08"
      in_class: true
      events:
        - label: LEC 12
          type: lecture
          title: Data Literacy and Calling Bullshit
          slides: 

- week: 7
  title: "Week 7 - Machine Learning Fundamentals & Applications<br>
    <small>
      📘 Read <a href='#'>Introduction to Machine Learning (TBD)</a>.<br>
    </small>"
  days:
    - date: "2025-05-13"
      in_class: true
      events:
        - label: LEC 13
          type: lecture
          title: Machine Learning (Supervised vs. Unsupervised Learning Reinforcement & Deep Learning)
          slides: 
          
    - date: "2025-05-14"
      in_class: true
      events:
        - label: DISC
          type: disc
          title: Discussion Section
          
    - date: "2025-05-15"
      in_class: true
      events:
        - label: LEC 14
          type: lecture
          title: Machine Learning (Demo code)
          slides: 
          code: 
        - label: PROJECT
          type: project
          title: <b>Project P1 Due</b>

- week: 8
  title: "Week 8 - Specialized Data Types & Industry Perspectives<br>
    <small>
      🍿 Watch <a href='#'>Text and Geospatial Data Analysis (TBD)</a>.<br>
    </small>"
  days:
    - date: "2025-05-20"
      in_class: true
      events:
        - label: LEC 15
          type: lecture
          title: Text/Geospatial Data
          slides: 
          demo: 
          
    - date: "2025-05-21"
      in_class: true
      events:
        - label: DISC
          type: disc
          title: Discussion Section
          
    - date: "2025-05-22"
      in_class: true
      events:
        - label: LEC 16
          type: lecture
          title: Data Science Talk
          slides: 
        - label: QUIZ
          type: quiz
          title: <b>Reading Quiz 5 Due</b>
        - label: HW
          type: hw
          title: <b>Homework 3 Due</b>

- week: 9
  title: "Week 9 - Guest Lectures & Industry Insights<br>
    <small>
      📘 Read <a href='#'>Data Science in Industry (TBD)</a>.<br>
    </small>"
  days:
    - date: "2025-05-27"
      in_class: true
      events:
        - label: LEC 17
          type: lecture
          title: Guest Lecture I
          slides: 
          
    - date: "2025-05-28"
      in_class: true
      events:
        - label: DISC
          type: disc
          title: Discussion Section
          
    - date: "2025-05-29"
      in_class: true
      events:
        - label: LEC 18
          type: lecture
          title: Guest Lecture II (Ahmed & Jiesen)
          slides: 

- week: 10
  title: "Week 10 - Modern AI Applications & Future of Data Science<br>
    <small>
      🍿 Watch <a href='#'>The Future of Data Science (TBD)</a>.<br>
    </small>"
  days:
    - date: "2025-06-03"
      in_class: true
      events:
        - label: LEC 19
          type: lecture
          title: LLMs chatgpt etc demos
          slides: 
          demo: 
        - label: PROJECT
          type: project
          title: <b>Project P2/Video Due (7 min video)</b>
          
    - date: "2025-06-04"
      in_class: true
      events:
        - label: DISC
          type: disc
          title: Discussion Section
          
    - date: "2025-06-05"
      in_class: true
      events:
        - label: LEC 20
          type: lecture
          title: Future of DS in 2025 beyond
          slides: 
        - label: PROJECT
          type: project
          title: <b>Project Report Due (~10 pages)</b>
```

## 2. Week HTML Template (`_includes/week.html`)

The week.html template needs to be updated to match the new structure. Here are the changes needed:

### Current Structure (Lines 26-50):

```html
{% case event.type %}
{% when "lecture" %}
<small>
  {% if event.blank %} <br><span style="margin-left: 10ch;"><a href="{{ event.blank }}">blank</a></span>{% endif %}
  {% if event.filled %}<span style="margin-left: 0.5ch;"><a href="{{ event.filled }}">filled</a></span>{% endif %}
  {% if event.code %}<span style="margin-left: 0.5ch;"><a href="{{ event.code }}">code</a></span>{% endif %}
  {% if event.animations %}<span style="margin-left: 0.5ch;"><a href="{{ event.animations }}">animations</a></span>{% endif %}
  {% if event.recording %}<span style="margin-left: 0.5ch;"><a href="{{ event.recording }}">recording</a></span>{% endif %}
  {% if event.faqs %}<span style="margin-left: 0.5ch;"><a href="{{ event.faqs }}">FAQs</a></span>{% endif %}
</small>

{% when "hw" or "hops" or "disc" or "lab" or "demo" or "exam" %}
<small>
  {% if event.guide %}<br><span style="margin-left: 10ch;"><a href="{{ event.guide }}">study guide</a></span>{% endif %}
  {% if event.problems %}<br><span style="margin-left: 10ch;"><a href="{{ event.problems }}">problems</a></span>{% endif %}
  {% if event.template %}<span style="margin-left: 0.5ch;"><a href="{{ event.template }}">template</a></span>{% endif %}
  {% if event.code %}<span style="margin-left: 0.5ch;"><a href="{{ event.code }}">code</a></span>{% endif %}
  {% if event.code_solutions %}<span style="margin-left: 0.5ch;"><a href="{{ event.code_solutions }}">code solutions</a></span>{% endif %}
  {% if event.data %}<span style="margin-left: 0.5ch;"><a href="{{ event.data }}">data</a></span>{% endif %}
  {% if event.walkthrough %}<span style="margin-left: 0.5ch;"></span><a href="{{ event.walkthrough }}">walkthrough</a></span>{% endif %}
  {% if event.solutions %}<span style="margin-left: 0.5ch;"><a href="{{ event.solutions }}">solutions</a></span>{% endif %}
  {% if event.submission %}<span style="margin-left: 0.5ch;"><a href="{{ event.submission }}">submission</a></span>{% endif %}
  {% if event.code_addt %}<span style="margin-left: 0.5ch;"><a href="{{ event.code_addt }}">additional code</a></span>{% endif %}
</small>
{% endcase %}
```

### Updated Structure:

```html
{% case event.type %}
{% when "lecture" %}
<small>
  {% if event.slides %} <br><span style="margin-left: 10ch;"><a href="{{ event.slides }}">slides</a></span>{% endif %}
  {% if event.code %}<span style="margin-left: 0.5ch;"><a href="{{ event.code }}">code</a></span>{% endif %}
  {% if event.demo %}<span style="margin-left: 0.5ch;"><a href="{{ event.demo }}">demo</a></span>{% endif %}
  {% if event.animations %}<span style="margin-left: 0.5ch;"><a href="{{ event.animations }}">animations</a></span>{% endif %}
  {% if event.faqs %}<span style="margin-left: 0.5ch;"><a href="{{ event.faqs }}">FAQs</a></span>{% endif %}
</small>

{% when "hw" or "quiz" or "disc" or "project" or "demo" or "exam" %}
<small>
  {% if event.submission %}<br><span style="margin-left: 10ch;"><a href="{{ event.submission }}">submission</a></span>{% endif %}
  {% if event.code %}<span style="margin-left: 0.5ch;"><a href="{{ event.code }}">code</a></span>{% endif %}
  {% if event.data %}<span style="margin-left: 0.5ch;"><a href="{{ event.data }}">data</a></span>{% endif %}
</small>
{% endcase %}
```

## Implementation Steps

1. Switch to Code mode to implement these changes
2. Update the `_includes/week.html` file with the new structure
3. Create or update the `_data/sp25/calendar.yml` file with the new content
4. Test the changes locally

## Next Steps

After implementing these changes, we should:

1. Review the calendar to ensure all dates and events are correct
2. Add actual URLs for slides, code, and other resources as they become available
3. Update any other files that might reference the calendar structure