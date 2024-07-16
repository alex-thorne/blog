---
layout: project
title: '#chuckstuff'
caption: Chuck Norris facts made possible via Terraform, Ansible, and Docker
description: >
  An example take-home evaluation for basic DevOps engineer candidate qualifications.
date: '10-07-2024'
accent_color: '#4fb1ba'
# accent_image:
#   background: '#ffffff'
#   theme_color: '#ffffff'
image: 
  path: /assets/img/projects/chuck-screenshot.jpg
  srcset: 
    1920w: /assets/img/projects/chuck-screenshot.jpg
    960w:  /assets/img/projects/chuck-screenshot.jpg@0,5x.jpg
    480w:  /assets/img/projects/chuck-screenshot.jpg@0,25x.jpg
links:
  - title: GitHub Link 
    url: https://github.com/alex-thorne/take-home-assignment
sitemap: false
---

## #chuckstuff Project

### Some history on this project
Over the last several years I've interviewed hundreds of candidates for DevOps engineering positions in our department. We developed a method of evaluating candidates which included asking them to complete a small assignment so we use it to assess their skills in IaC related concepts as well as base our follow up interview discussion on their project choices. 

This year we reorganized our department, and several of my colleagues and I branched off to form a new section focused on several new greenfield products. Hiring into the new section is a key topic for us at the moment, so I've been reflecting on the hiring experience I had in the former teams over the last 8 years. I've been trying to decide if asking candidates to complete an assignment like this is still a worthwhile approach, or whether we should refactor the process. 

If we do use an assignment like this, it will need to change a bit, not only because AI-powered tools make it easier and easier to spoof a such an assignment, but also to incorporate some of the updated skills we'll need in the new teams. Either to hand it over to the new hiring managers taking my place, or at least to capture its history before it dies, I decided to better document the process. 

I also couldn't stop thinking that, throughout the years I'd asked so many candidates to do this assignment although I'd never actually completed it myself.

### Results
Without further ado, I submit for evaluation #[chuckstuff](https://github.com/alex-thorne/take-home-assignment): my devops engineer application take-home assignment.  

Without a doubt this project could use more work. I chose to pause at the 'minimum viable product' stage rather than continue on with several further enhancements that really should be there. I'd like to come back to it soon, it is after all a nice little project to build on as a playground of sorts. If my colleagues were to rate me as a candidate with this submission I would have had to be lucky to be invited to a follow up interview 😅 At the "MVP" stage, I failed to follow the instructions calling for "reusability" of the solution. For that I might have separated some logical groupings out of the Terraform provisioning, at least the networking setup. Overall the provisioning and Ansible deployment lacks idempotency and error handling.

### Take-away
This project was a great refresher for me. Although I am familiar with all of the concepts and technologies, putting something like this together from scratch is something I haven't done since long before our adoption of several of these tools. Years ago, when I was still doing "real" work and not just management 😉 we weren't yet using Ansible, Terraform, or Docker. We've also only just recently started deploying services to GCP.

I appreciated the experience of building this as a public repository, as it made me be careful to consider how I handled secrets for authentication while still allowing the project to be reusable by others with minimal changes. 

### Project Details
- Date: 11-07-2024
- Technologies used: Ansible, Terraform, Docker, Python, Google Cloud Platform.
