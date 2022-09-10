---
layout: default
title: Reading 2
has_children: false
parent: Readings
nav_order: 2
permalink: /readings/reading-2
---

# Reading 2

Reading 2 is about ethics, and specifically the ethical issues that arise when working with large amounts of data. In class we talk more about the topic and theory of ethics, with some practical examples. These readings go into much more detail about practical applications for ethics in data science, and how you may want to tackle such challenges, and why they exist.

<!-- TODO: add links and s3 downloads for r1 -->

## R2a: Ethics and Data Science -- [download](https://www.example.com)

*Loukides M, Mason, H & Patil DJ, Ethics and Data Science*

Patil's article deals more with the nuts and bolts of applying ethical decision making process into a data science workflow. This article will be of particular use to you on your assignment 1 and final project, because it introduces you to essentially a checklist.

## R2b: Privacy & Security Myths -- [download](https://www.example.com)

*Narayanan and Shmatikov, Privacy & Security Myths & Fallacies of “PII”*

 This paper is a great look into some of the highly specific data that some data scientists might work with in healthcare. Because healthcare data extremely protected and personal, it introduces students to the concepts of PII, PHI and HIPPA. Finally, the article goes over how brittle privacy is from a security standpoint and just how careful analysts need to be working with such highly protected data. Data leaked, even with PII/PHI removed, can still be statistically tied back to unique individuals. This shows the awesome power that statistics and data analysis can yield, given enough data.

## Additional Resources

### Deon Checklist Tool

Deon ([link](https://deon.drivendata.org/)) is a command line tool that allows you to easily add an ethics checklist to your data science projects. You can look at this checklist for an example during the ethics portion of assignment 1 and your final group project.

### HIPPA Data

For anyone interested, Health Insurance Portability and Accountability Act (HIPPA) data covers the following 18 data identifiers:

- Name
- Address (all geographic subdivisions smaller than state, including street address, city county, and zip code)
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

If a communication contains any of these identifiers, or parts of the identifier, such as initials, the data is to be considered “identified”.   To be considered “de-identified”, ALL of the 18 HIPAA Identifiers must be removed from the data set.  This includes all dates, such as surgery dates, all voice recordings, and all photographic images.
