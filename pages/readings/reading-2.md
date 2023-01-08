---
layout: default
title: Reading 2
has_children: false
parent: Readings
nav_order: 2
permalink: /readings/reading-2
---

# Reading 2

- Loukides M, Mason, H & Patil DJ, Data's Day of Reckoning <a href="https://s3.us-west-2.amazonaws.com/ucsd.cogs9/readings/r2a-ethics-data-reckoning.pdf" target="_blank" rel="noopener">download &#x2197;</a>
- Narayanan and Shmatikov, Privacy & Security Myths & Fallacies of "PII" <a href="https://s3.us-west-2.amazonaws.com/ucsd.cogs9/readings/r2b-ethics-privacy-security.pdf" target="_blank" rel="noopener">download &#x2197;</a>

Reading 2 is about ethics, and specifically, the ethical issues that arise when working with large amounts of data. In class, we talk more about the topic and theory of ethics, with some practical examples. These readings go into much more detail about practical applications for ethics in data science, how you may want to tackle such challenges, and why they exist. Patil's article has a lot of good practical tips to think about when writing your ethics section in Assignment 1 and the final. Narayanan's paper provides a close look into the issues surrounding personal data and the dangers inherent when working with and storing such data.

## Additional Resources

### Security

Here are two excellent sources for security-related information, research, and news. 
- Bruce Schneier's <a href="https://www.schneier.com/" target="_blank" rel="noopener">site &#x2197;</a> He is a fellow/lecturer at Harvard and on the board of the EFF.
- Brian Krebs' blog <a href="https://krebsonsecurity.com/" target="_blank" rel="noopener">KrebOnSecurity &#x2197;</a> is a resource for current news and investigatory material on security issues. He worked for the Washington Post as a reporter for over 15 years.

### Deon Checklist Tool

Deon <a href="https://deon.drivendata.org/" target="_blank" rel="noopener">view &#x2197;</a> is a command line tool that allows you to easily add an ethics checklist to your data science projects. You can look at this checklist for an example during the ethics portion of assignment 1 and your final group project.

### HIPAA Data

For anyone interested, Health Insurance Portability and Accountability Act (HIPAA) data cover the following 18 data identifiers:

- Name
- Address (all geographic subdivisions smaller than a state, including street address, city county, and zip code)
- All elements (except years) of dates related to an individual (including birthdate, admission date, discharge date, date of death, and exact age if over 89)
- Telephone numbers
- Fax number
- Email address
- Social Security Number
- Medical record number
- Health plan beneficiary number
- Account number
- Certificate or license number
- Vehicle identifiers and serial numbers, including license plate numbers
- Device identifiers and serial numbers
- Web URL
- Internet Protocol (IP) Address
- Finger or voice print
- Photographic image - Photographic images are not limited to images of the face.
- Any other characteristic that could uniquely identify the individual
{: .fs-2 }

The HIPAA privacy rule sets forth policies to protect all individually identifiable health information that is held or transmitted. These are the 18 HIPAA Identifiers that are considered personally identifiable information. This information can be used to identify, contact, or locate a single person or can be used with other sources to identify a single individual. When personally identifiable information is used in conjunction with one’s physical or mental health or condition, health care, or one’s payment for that health care, it becomes Protected Health Information (PHI).

If a communication contains any of these identifiers, or parts of the identifier, such as initials, the data is to be considered "identified".   To be considered "de-identified", ALL of the 18 HIPAA Identifiers must be removed from the data set.  This includes all dates, such as surgery dates, all voice recordings, and all photographic images.
