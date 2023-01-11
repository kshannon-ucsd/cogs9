---
layout: default
title: Contact Us
has_children: false
nav_order: 10
permalink: /contact-us/
---

{% assign variables = site.data[site.data_folder].variables %}

# Contact Us

{: .warning }
Please **do not email staff about waitlist issues**. Please submit your queries to [{{ variables.cogsadvising }}](mailto:{{ variables.cogsadvising }})

<div>
<h3> Who do you want to email? </h3>
{% assign email_no = 1 %}
<table style="table-layout: fixed; text-align: left; width: 100%; vertical-align: top; border-collapse: collapse;">
<colspan>
<col style="width: 33%;">
<col style="width: 34%;">
<col style="width: 33%;">
</colspan>
<thead>
<tr class="header">
<th> Instructional Assistants </th>
<th> Teaching Assistants </th>
<th> Instructor </th>
</tr>
</thead>
<tbody>
<tr>
<td style="vertical-align: top"> {% for ia in variables.instructional_assistants %} <input type="checkbox" id="email{{ email_no }}" name="email{{ email_no }}" value="{{ ia.email }}"> <label for="email{{ email_no }}"> {{ ia.name }} </label> <br/> {% assign email_no = email_no | plus: 1 %} {% endfor %} </td>
<td style="vertical-align: top"> {% for ta in variables.teaching_assistants %} <input type="checkbox" id="email{{ email_no }}" name="email{{ email_no }}" value="{{ ta.email }}"> <label for="email{{ email_no }}"> {{ ta.name }} </label> <br/> {% assign email_no = email_no | plus: 1 %}  {% endfor %}</td>
<td style="vertical-align: top"> <input type="checkbox" id="email{{ email_no }}" name="email{{ email_no }}" value="{{ variables.instructor.email }}"> <label for="email{{ email_no }}"> {{ variables.instructor.name }} </label> </td>
</tr>
</tbody>
</table>
<h3> Select a topic for your email </h3>
<input type="radio" id="personal" name="topic" value="Personal" checked>
<label for="personal">Personal</label> <br/>
<input type="radio" id="syllabus" name="topic" value="Syllabus">
<label for="syllabus">Syllabus</label> <br/>
<input type="radio" id="grading" name="topic" value="Grading">
<label for="grading">Grading</label> <br/>
<input type="radio" id="project" name="topic" value="Project">
<label for="project">Project</label> <br/>
<input type="radio" id="assgquiz" name="topic" value="Assg/Quiz">
<label for="assgquiz">Assignment/Quiz</label> <br/>
<input type="radio" id="other" name="topic" value="Other">
<label for="other">Other</label> 
<h3> Enter your PID and name </h3>
<label for="pid"><h4>PID *</h4></label>
<input type="text" name="pid" value="" required>
<label for="name"><h4>Name *</h4></label>
<input type="text" name="name" value="" required>
<h3> Enter email subject and body </h3>
<label for="subject"><h4>Subject *</h4></label>
<input style="width:100%;" type="text" id="subject" value="" required>
<label for="body"><h4>Body *</h4></label>
<textarea name="body" rows="10" cols="81" value="" required></textarea> <br/> <br/>
<input type="button" value="Submit" onclick="mail(this.parentNode)">
</div>

<script language="javascript">
function mail(form) {
    var inputs = form.getElementsByTagName("input");
    var emails = [];
    var pid = inputs["pid"].value;
    var name = inputs["name"].value;
    var subject = "[COGS9]" + "[";
    for (var i = 0; i < inputs.length; i++) {
        if (inputs[i].type == "checkbox" && inputs[i].checked) {
            emails.push(inputs[i].value);
        }
        if (inputs[i].type == "radio" && inputs[i].checked) {
            subject += inputs[i].value + "] ";
        }
    }
    subject += inputs["subject"].value;
    var body = "PID: " + pid + "\nName: " + name + "\n\n" + form.getElementsByTagName("textarea")[0].value;
    var url = "mailto:" + emails.join(",") + "?subject=" + subject + "&body=" + body;
    window.location.href = encodeURI(url);
}
</script>
