---
title: "171 - Managing your risk from vendors"
date: 2021-10-17
description: "We’re going to hear a lot about supply chains over the next few years.  This is going to be the next big thing in security, and luckily, lots of smart people are already working on subsets of the problem."
permalink: /managing-your-risk-from-vendors/
---

We’re going to hear a lot about supply chains over the next few years.  This is going to be the next big thing in security, and luckily, lots of smart people are already working on subsets of the problem.

But there’s a few big problems with supply chain security generally that will make adoption and use of those solutions hard.

Firstly, we don’t have a very good definition of the supply chain to work out what it even means to secure it.  A supply chain security problem can be anything from the vendor who sells you your cloud servers, some code written by an open source project, a binary dependency built by someone else’s build system, or the developer tooling that your teams use to build you code, and probably some other definitions I’ve forgotten.

We can’t talk abstractly about simply “securing the supply chain”, unless we talk clearly and cogently about what we are scoping that down to first.

The biggest supply chain risk for many of is relating to our vendors, and our managed service provides.  In particular those who manage and supply our underlying infrastructure, so the operation of our active directory, our security systems and our cloud vendors.  Understanding their approach to security, and how much of a risk they are to you is key to getting a grip on that vendor security part.

However, there’s an elephant in the room in this stuff.  Sure all the new focus, attention and money is going to be invested in supply chain security programmes.  But the first rule of security is that you can only secure what you can see.  For the last few years, we’ve been saying that good asset management, and understanding your estate is the first step in securing your systems.  But many of us are still effectively blind to large portions of our estate.  

Throwing money at supply chains is only valuable once you have mapped that supply chain, and that means investing in doing the hard, boring basics.  That means properly getting a grip of your data, information and It assets so you know which vendors are in use and what data they hold for you.

## [It's Time for Vendor Security 2.0 - Daniel Miessler](https://danielmiessler.com/blog/its-time-for-vendor-security-2-0/)

[https://danielmiessler.com/blog/its-time-for-vendor-security-2-0/](https://danielmiessler.com/blog/its-time-for-vendor-security-2-0/)

> In short, Vendor Security 2.0 is the transition from external security checks to internal risk analysis.
> 
> #### Questionable value
> 
> For those of you who have been playing the security questionnaire game for multiple years, ask yourselves how many Solarwinds-type compromises, or data breaches from popped vendors were:
> 
> * Caught by a security questionnaire process, AND
> * Stopped from doing business with the company because of the security questionnaire
> 
> ???
> 
> Not many, right? They either weren’t caught by the process, or the business ignored the findings because they wanted to use that product or service.
> 
> I have been part of hundreds—possibly even thousands—of vendor security reviews in my 20 years in security, and I can think of very few examples of where the business really wanted to use a particular vendor and security shot it down.


This somewhat tongue in cheek assessment of our vendor security processes hits home for me.  What value are our security assessments, and what possibly could you have done, as a buyer of SolarWind that would have given you any indication of the issue before it happened?

The answer is nothing.  There’s nothing you could have asked in advance that would have told you, in part because Solarwinds was compromised by such an advanced attacker, but even that aside, we simply don’t know how to audit our own capability, so of course we don’t know how to audit a suppliers capability.


## [Securing Netflix Studios At Scale Netflix TechBlog | Netflix TechBlog](https://netflixtechblog.com/the-show-must-go-on-securing-netflix-studios-at-scale-19b801c86479)

[https://netflixtechblog.com/the-show-must-go-on-securing-netflix-studios-at-scale-19b801c86479](https://netflixtechblog.com/the-show-must-go-on-securing-netflix-studios-at-scale-19b801c86479)

> In deciding how to address this, we focused on two observations. The first was that there were too many security things that each software team needed to think about — things like TLS certificates, authentication, security headers, request logging, rate limiting, among many others. There were security checklists for developers, but they were lengthy and mostly manual, neither of which contributed to the goal of accelerating development. Adding to the complexity, many of the checklist items themselves had a variety of different options to fulfill them (“new apps do this, but legacy apps do that”; “Java apps should use this approach, but Ruby apps should try one of these four things”… yes, there were flowcharts inside checklists. Ouch.). For development teams, just working through the flowcharts of requirements and options was a monumental task. Supporting developers through those checklists for edge cases, and then validating that each team’s choices resulted in an architecture with all the desired security properties, was similarly not scalable for our security engineers.
> Our second observation centered on strong authentication as our highest-leverage control. Missing or incomplete authentication in an application was the most critical type of issue we regularly faced, while at the same time, an application that had a bulletproof authentication story was an application we considered to be lower risk. Concepts like Zero Trust, Beyond Corp, and Identity Aware Proxies all seemed to point the same way: there is powerful assurance in making 100% authentication a property of the architecture of the application rather than an implementation detail within an application.


Simplify.  That’s what the rallying cry of blue teams should be.  Make it easier for developers, builders and integrators to do the right thing


## [Can The Real Codeowners Please Stand Up? Code Provenance at Scale](https://www.twilio.com/blog/determine-code-ownership-about-yaml-gordon)

[https://www.twilio.com/blog/determine-code-ownership-about-yaml-gordon](https://www.twilio.com/blog/determine-code-ownership-about-yaml-gordon)

> More times than we’d like to admit, we found ourselves in a situation where we find a bug or vulnerability in a piece of code, do a git blame to see who last touched that code, and find out that person no longer works at Twilio – or is on PTO. Then, the adventure starts: pick the next name in the git blame timeline and go down the rabbit hole to find the right owner to work on a fix.
> 
> That’s a lot of time wasted in a state of emergency, isn’t it? Every Security team out there had to go through this situation at some point.
> 
> Now imagine a galaxy far, far away (spoiler alert: not far at all, actually) where the code ownership information and all your required metadata (e.g., owning team, Jira project, PagerDuty information) for every piece of code lives within that codebase and is machine parsable.
> 
> The Product Security team at Twilio set out to see if they could make that a reality. And thus – the about.yaml and Gordon initiative


A nice example of trying to ensure that you know who is the owner for the code, and how to get hold of them during an incident.


## [How to attack cloud infrastructure via a malicious pull request | Teleport](https://goteleport.com/blog/hack-via-pull-request/)

[https://goteleport.com/blog/hack-via-pull-request/](https://goteleport.com/blog/hack-via-pull-request/)

> In April 2021, I discovered an attack vector that could allow a malicious Pull Request to a Github repository to gain access to our production environment. Open source companies like us, or anyone else who accepts external contributions, are especially vulnerable to this.
> 
> For the eager, the attack works by pivoting from a Kubernetes worker pod to the node itself, and from there exfiltrating credentials from the CI/CD system. Critically, this vulnerability exposed production AWS credentials that could be used to alter release artifacts and access production infrastructure.
> 
> Once discovered, we immediately fixed our CI system to prevent this attack from occurring. Our response team’s analysis found no evidence this vulnerability was exploited or any data was tampered with. Even so, we encourage customers to upgrade to the recently released Teleport 4.4.11, 5.2.4, 6.2.12, or 7.1.1.
> 
> In this post, I will walk through the vulnerability and focus on some key areas where we are improving our CI/CD tools and practices.


As more people move to using CI/CD, especially public and cloud pipelines, we need to remember that we’re opening up a new potential attack vector. This is a good writeup of an attack and how you can defend against it.


## [Google Online Security Blog: Distroless Builds Are Now SLSA 2](https://security.googleblog.com/2021/09/distroless-builds-are-now-slsa-2.html)

[https://security.googleblog.com/2021/09/distroless-builds-are-now-slsa-2.html](https://security.googleblog.com/2021/09/distroless-builds-are-now-slsa-2.html)

> A few months ago we announced that we started signing all distroless images with cosign, which allows users to verify that they have the correct image before starting the build process. Signing our images was our first step towards fully securing the distroless supply chain. Since then, we’ve implemented even more accountability in our supply chain and are excited to announce that distroless builds have achieved SLSA 2. SLSA is a security framework for increasing supply chain security, and Level 2 ensures that the build service is tamper resistant.
> 
> This means that in addition to a signature, each distroless image now has an associated signed provenance. This provenance is an in-toto attestation and includes information around how each image was built, what command was run, and what build system was used. It also includes any special parameters that were passed in, the exact commit the images were built at, and more. This provenance is a useful tool for builds that need to be audited in the future.


This concept of signed builds having a signed key that tells you that the container hasn’t been modified, and that it was built in a specific way is really powerful for supply chain security.

The combination of this, and repeatable builds gives us a powerful fundamental component that can lead towards a software bill of materials, and confidence in the underlying infrastructure.


## [10 Common Security Issues when Migrating from On Premises to Azure - Praetorian](https://www.praetorian.com/blog/migrating-to-azure/)

[https://www.praetorian.com/blog/migrating-to-azure/](https://www.praetorian.com/blog/migrating-to-azure/)

> This article is focused on the security risks involved in a cloud migration and provides a compilation of common security anti-patterns and best practices for architects only familiar with traditional on-premise data centers to follow. The following were based on reviews of multiple client Azure cloud environments of varying sizes and maturity.
> 
> Common Misconfigurations and Anti-Patterns
> 
> Praetorian has observed the following recurring issues in Azure environments. Many of these issues are caused by a paradigm shift in thought from conventional on-premise data centers to cloud deployments.


This is a useful list of misconfigurations and errors that one can make when migrating from on premise to the cloud.  


## [Threat Detection Maturity Framework | by Haider Dost | Snowflake | Sep, 2021 | Medium](https://medium.com/snowflake/threat-detection-maturity-framework-23bbb74db2bc)

[https://medium.com/snowflake/threat-detection-maturity-framework-23bbb74db2bc](https://medium.com/snowflake/threat-detection-maturity-framework-23bbb74db2bc)

> In March when I joined Snowflake as the Manager of Global Threat Detection, I began working on a framework that supported our vision: “Be an exemplary function within Snowflake greatly reducing organizational risk while also producing content worth sharing with the broader security community that positions Snowflake as a leader in the Threat Detection space”. This “framework” started as eight pages of scattershot thoughts of everything that I felt was needed for a successful program, but I still needed a way to measure and convey maturity. This prompted me to build the Threat Detection Maturity Framework, a structured and re-usable model that could be used to present the program to my leadership and used by my peers in the Threat Detection space.


This is a nice bit of thinking around the development of a capability framework.  I think that it’s a little under granular for me, but for setting out a capability gap review, and the a vision of where you want to get to, it should work, and it should be easy to tweak to work for you.


## [IAM Vulnerable - An AWS IAM Privilege Escalation Playground](https://labs.bishopfox.com/tech-blog/iam-vulnerable-an-aws-iam-privilege-escalation-playground)

[https://labs.bishopfox.com/tech-blog/iam-vulnerable-an-aws-iam-privilege-escalation-playground](https://labs.bishopfox.com/tech-blog/iam-vulnerable-an-aws-iam-privilege-escalation-playground)

> Intentionally Vulnerable Infrastructure as Code
> 
> IAM Vulnerable uses the Terraform binary to deploy over 250 IAM resources into your selected AWS account so that, within minutes, you can start learning how to identify and then exploit intentionally vulnerable IAM configurations that allow for privilege escalation. The project initially started out as a Terraform implementation of Gerben’s environment; however, it has evolved to include more vulnerable configurations commonly observed during our cloud penetration tests, like assume-role chains that lead to privilege escalation and other methods that have been discovered after Spencer’s original research in 2018. At the time of release, there are 31 unique privilege escalation test cases


A collection of templates that allow you to deploy deliberately vulnerable IAM configurations, so you can test out exploiting them, and see what the logs look like, how you might audit and detect it, and hopefully learn the patterns to avoid.


## [IoT Hacking and Rickrolling My High School District | WhiteHoodHacker](https://whitehoodhacker.net/posts/2021-10-04-the-big-rick)

[https://whitehoodhacker.net/posts/2021-10-04-the-big-rick](https://whitehoodhacker.net/posts/2021-10-04-the-big-rick)

> This story isn't one of those typical rickrolls where students sneak Rick Astley into presentations, talent shows, or Zoom calls. I did it by hijacking every networked display in every school to broadcast "Never Gonna Give You Up" in perfect synchronization. Whether it was a TV in a hall, a projector in a classroom, or a jumbotron displaying the lunch menu, as long as it was networked, I hacked it!
> 
> In this post, I'll be explaining how I did it and how I evaded detection, as well as the aftermath when I revealed myself and didn't get into trouble.
> 
> 


This was a fun read, and a really nice example of vulnerability disclosure done right, and handled right.


