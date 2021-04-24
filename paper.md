---
title: 'Blinkr: Computer Vision based Blink Reminder'
tags:
  - Python
  - Computer Vision
  - Blink Reminder
authors:
  - name: Adrit Rao
    orcid: 0000-0003-0872-7098
    affiliation: "1"
affiliations:
 - name: Greene Middle School
   index: 1
date: 24 April 2021
bibliography: paper.bib

# Optional fields if submitting to a AAS journal too, see this blog post:
# https://blog.joss.theoj.org/2018/12/a-new-collaboration-with-aas-publishing
aas-doi: 10.3847/xxxxx <- update this with the DOI from AAS once you know it.
aas-journal: Astrophysical Journal <- The name of the AAS journal.
---

# Summary

Blinkr is a Python-based, simple piece of software that reminds a user to blink. Dlib Computer Vision based facial landmark detection and Eye Aspect Ratio (EAR) calculation with OpenCV allows for the detection of blinks. Blinks are counted over a 60 second time period with a custom average blink threshold with audible reminders to blink more.

# Statement of need

Prolonged exposure to a screen without blinking over a long period of time can have adverse side effects on eye health and well-being. Blinking is crucial for preventing side effects. Through research, it has been proven that blink rates significantly decrease when on the computer. Reminding a user to blink more can help in preventing side effects and teaching yourself to blink more subconsciously. Blinkr aims to solve this in a simple code-base through Computer Vision. Using the Dlib pre-trained facial landmark detection algorithm along with calculation of variance in the EAR enables blinks to be detected and counted. On average, people blink about 15-20 times a minute. Blinkr can remind a user if they are not blinking enough through an audible voice reminder.

# Acknowledgements

We acknowledge the contributions made by Dlib in creating an open-source facial landmark detection algorithm along with the research that has been conducted in calculation of the EAR.

# References
