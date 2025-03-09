---
title: "165 - Taking time to relax"
date: 2021-09-05
description: "Last weeks issue seems to have hit a chord with people."
permalink: /taking-time-to-relax/
---

Last weeks issue seems to have hit a chord with people.

I had a number of people reach out to say how much the burnout article resonated with them, and how it really touched on how they were feeling at the moment.

It’s echoed with me as well, and I’m very aware of needing to take time to relax.  I had a proper staycation the last few weeks, and spending time at home with my family and taking a break from work has really helped to recharge, and refocus on whats important.

There’s a lot of good reading in here this week, but I don’t have a lot to say about it that isn’t covered in the analysis, so I’m going to enjoy the lovely summer weather in the UK and relax in the garden with a beer.

If you are UK based, I hope you enjoy the weather, and if you are US based, enjoy the long weekend (if you aren’t on call), and make sure to relax and enjoy.

## [Inside Figma: securing internal web apps](https://www.figma.com/blog/inside-figma-securing-internal-web-apps/)

[https://www.figma.com/blog/inside-figma-securing-internal-web-apps/](https://www.figma.com/blog/inside-figma-securing-internal-web-apps/)

> Figma, like most tech companies, relies on a suite of internally developed applications to make things work behind the scenes. From deploying our software to providing support functionality, the web tools we’ve developed are crucial to employee workflows. They also have stringent security requirements to ensure that only authorized employees can access them.
> 
> Attackers and cybercriminals have a history of going after administrative backends as a way to target user data. To protect our users and their data, we set out to build a system that could provide safe access to internal applications.
> 
> Our approach maximizes off-the-shelf components for easy maintenance and security network effects, but ties them together in novel ways to ensure that we have the best security practices in place. From the start, we had a few requirements:
> 
> * Smooth user experience. Employee productivity is one of our top priorities, so our authentication system must be fast, reliable, and easy to access.
> * Zero-trust principles. Signing in from a “trusted network” isn’t a guarantee of trustworthiness. When authenticating clients, our security model must rely on stronger assertions than network address alone.
> * Strong, modern authentication capabilities. We want to leverage the latest and greatest in web security technologies to protect our internal applications. Any engineer working on an internal app should be able to easily utilize defenses like WebAuthn within the system we build.
> * Centralized authorization. The Figma IT and security teams need to be able to effectively assign, monitor, and adjust permissions granted to employees. A system that is too distributed will quickly become difficult to understand or control, and lead to either over-permissioning or user frustration.
> * Minimal toil for the security team. As a small team with a broad surface to secure, our solution for application access shouldn’t require too much ongoing SRE or operational work.


This is a really good write up of a modern “zero-trust” architecture.  If you have internal application development team, then this architecture is pretty robust.

One thing that isn’t called out in these principles, but seems to come through in the architecture is the principle of “ease of use for developers” or “minimal tool for developers” in their language.  This system is easy to setup, and enables development teams to create new applications, new systems without having to request changes to the core identity system.  For a modern workforce that really is the dream.


## [Cloud Security Orienteering - tl;dr sec](https://tldrsec.com/blog/cloud-security-orienteering/)

[https://tldrsec.com/blog/cloud-security-orienteering/](https://tldrsec.com/blog/cloud-security-orienteering/)

> As a security consultant, I had the challenge and opportunity to enter blind into a variety of cloud environments. They were across Azure, GCP, and AWS, some well-architected and others organically sprawling, containing a single account/project and hundreds.
> 
> This gave me a rapid education in how to find the information necessary to familiarize myself with the environment, dig in to identify the risks that matter, and put together remediation plans that address short, medium, and long term goals. In these engagements, clients were paying for a security assessment, but to execute them was an exercise in orienteering.
> 
> Over the course of a career in cloud security, you’ll likely find yourself walking into a new environment and needing to rapidly orient yourself to both mitigate the biggest risks and also develop a roadmap towards a sustainable, secure future. There are a variety of ways the methodology I’ve defined can be applied, including:
> 
> * Consulting engagements
> * A new job
> * A new team
> * A merger or an acquisition
> * A fresh assessment of your current environment.


This is a valuable resource for any consultant from the excellent Rami McCarthy (and [tldrsec](https://tldrsec.com/newsletter/) is a great newsletter you should be reading).  But I think he’s missed a vital use case here.  Cloud Orienteering (a great name that I’m totally going to steal) is something that you should be doing in your own organisations unless you are unusually mature.

Over time our environments and our central understanding of the various cloud implementations will likely drift.  At the speed of change going on at the moment, you might want to conduct an internal orienteering assessment of your cloud environments around once a year.  New teams, new business units and people with just smart ideas will likely have built, deployed and managed systems or services without your awareness.  This methodology is a great way to trying to get a grip on that.


## [So You Inherited an AWS Account. A 30-day security guide for engineers… | by Matt Fuller | The Startup | Medium](https://medium.com/swlh/so-you-inherited-an-aws-account-e5fe6550607d)

[https://medium.com/swlh/so-you-inherited-an-aws-account-e5fe6550607d](https://medium.com/swlh/so-you-inherited-an-aws-account-e5fe6550607d)

> Many engineers have found themselves in the unenviable position of being handed the keys to an AWS environment with absolutely no explanation of its contents, documentation, or training. Whether an employee leaves the company, teams are restructured, or your company acquires another, you will need to quickly audit the account and get up to speed on its operation. Even worse, many of these inherited accounts are running production infrastructure that must be kept running during the transition period. Now that you’re responsible for this account, you will also be responsible for keeping it secure.
> 
> There is a wealth of documentation, training, guides, and other resources available online to learn about security in AWS cloud environments. But many of those resources assume that you are either building an account from scratch, were intimately involved in building the account from its inception, or can take great liberty in applying destructive changes. In our case, the reality is that you’re likely staring at eight years of accumulated infrastructure with absolutely no idea of what’s running or how to make changes without causing a production outage.
> 
> I’ve written this guide to help you filter through the mess, isolate the changes you need to make, and start to tame your environment. While I’ll assume that you have AWS experience, we’ll start with the security basics, along with changes that won’t impact running services, before moving to making tweaks that will require a bit more investigation and preparation. Our goal is to quickly triage the situation, implement the lowest risk but most impactful changes first, and then work our way toward a concrete security policy that can be used longer-term.


This is a good guide for what to do if you just got handed an account.  A good example of this is if some external consultants have been building your system and you are rolling them off.

You might also consider this guide useful if, as part of a red team exercise, you have just gained control of an AWS account as well.


## [Kubernetes Hardening Guidance [pdf]](https://media.defense.gov/2021/Aug/03/2002820425/-1/-1/1/CTR_KUBERNETES%20HARDENING%20GUIDANCE.PDF)

[https://media.defense.gov/2021/Aug/03/2002820425/-1/-1/1/CTR_KUBERNETES%20HARDENING%20GUIDANCE.PDF](https://media.defense.gov/2021/Aug/03/2002820425/-1/-1/1/CTR_KUBERNETES%20HARDENING%20GUIDANCE.PDF)

> This guidance describes the security challenges associated with setting up and securing a Kubernetes cluster. It includes hardening strategies to avoid common misconfigurations and guide system administrators and developers of National Security Systems on how to deploy Kubernetes with example configurations for the recommended hardening measures and mitigations. 


CISA and NSA have released a good set of guidance to help you avoid the most common misconfiguration issues with Kubernetes clusters.

Of course, if you are using a Kubernetes cluster built and run for you by your cloud provider, then some of this advice won’t be needed, but there’s still some good points in here about how to secure your container workloads, and use that cluster effectively and securely that you might still need to think about.


## [AWS Doesn’t Know Who I Am. Here’s Why That’s A Problem. | by Ben Kehoe | Aug, 2021 | Medium](https://ben11kehoe.medium.com/aws-doesnt-know-who-i-am-here-s-why-that-s-a-problem-4aeca591b0a6)

[https://ben11kehoe.medium.com/aws-doesnt-know-who-i-am-here-s-why-that-s-a-problem-4aeca591b0a6](https://ben11kehoe.medium.com/aws-doesnt-know-who-i-am-here-s-why-that-s-a-problem-4aeca591b0a6)

> AWS needs to have a single identity that is tied to Ben Kehoe, the human. When I go to re:Invent, the identity tied to my conference badge should not be specific to my employer nor independent of my employer. I am both an AWS user in my own right, and an AWS user in my job at iRobot.
> What I don’t need is a single set of credentials that gives me access to everything I do across these different identities. When I’m accessing iRobot resources, I should be required to have authenticated with my iRobot credentials with AWS SSO through Okta. When I’m accessing my personal resources, the authentication that gives me access to iRobot resources is irrelevant; I should have to be authenticated through the identity provider I’m using in my personal projects. And I don’t need to be simultaneously authenticated for both of these; authenticating as one can invalidate my authentication as the other. But no matter what, the identity I’m using should carry with it the identifier for Ben Kehoe the human.
> I don’t think this human identity should be involved in authorization; it should not be a principal in IAM, for example, nor should it even be an context key that you could use in an IAM policy. What it should be is an identifier (that can be used in public, I think) that carries with it context that’s tied to the human, to make the human’s user experience better; and it should be the identity that’s used when interacting with AWS outside the bounds of AWS accounts and resources (e.g., events, the forums, AWS IQ).


Identity is really hard.  Our identity is core to who we are, but is very abstract, and has a different meaning in different contexts.  My identity as someone at work is of course linked to the identity of the person who writes this newsletter, because it’s the same human, but when I sit to write this newsletter, I do so within another context.

I’m not disagreeing with Ben here, AWS is particularly poor at tracking who you are, and it does literally feel like they don’t know who I am on a regular basis, but I’m not sure that there is such a thing as a single canonical identity for a person is always the right thing here.  What we might need is some combination of identity and context that can be easily used when we interact with companies like AWS.


## [Leaving Bastion Hosts Behind Part 1: GCP - Netskope](https://www.netskope.com/blog/leaving-bastion-hosts-behind-part-1-gcp)

[https://www.netskope.com/blog/leaving-bastion-hosts-behind-part-1-gcp](https://www.netskope.com/blog/leaving-bastion-hosts-behind-part-1-gcp)

> Historically, it has been a best practice to implement bastion hosts to limit the exposure of the management protocols. However, there are some disadvantages to that approach. Recently, the big three cloud providers, Amazon Web Services (AWS), Google Cloud Platform (GCP), and Azure, have all released services that provide an alternative solution. We’ll be publishing a series of blog posts on these solutions, detailing the alternatives from each provider in its own blog post. The last blog post of the series will cover Netskope Private Access (NPA), which provides a Zero Trust Network Access (ZTNA) solution that is easy to deploy and can secure management access across all three providers.
> 
> In this post, we’ll first review what bastion hosts are, what the difficulties are with them, and then present the general model that all of the alternative solutions follow. Finally, we’ll examine the GCP services, OS Login, and Identity-Aware Proxy (IAP) in more detail to show how they can be used as an alternative to bastion hosts.


This covers some good models that can replace bastion servers.  One of the problems that isn’t covered here with Bastion servers is that because of the cost and complexity of building, running and maintaining them, organisations tend to prefer to reuse them, which means that compromise of either the developers who access them, or the server itself tends to have a large blast radius.


## [Scan for vulnerabilities early to shift security left in CI/CD | Google Cloud Blog](https://cloud.google.com/blog/products/identity-security/scan-for-vulnerabilities-early-to-shift-security-left-in-cicd)

[https://cloud.google.com/blog/products/identity-security/scan-for-vulnerabilities-early-to-shift-security-left-in-cicd](https://cloud.google.com/blog/products/identity-security/scan-for-vulnerabilities-early-to-shift-security-left-in-cicd)

> The process of checking for vulnerabilities earlier in development is called "shifting left". In fact, building security into software development also  speeds up  software delivery and performance. Thanks to shift-left, research from DevOps Research and Assessment (DORA) shows high-performing teams spend 50 percent less time remediating security issues than low-performing teams. 
> 
> To help companies accomplish a leftward shift in their security, Google Cloud recently launched On-Demand Scanning to general availability.  This new feature checks for vulnerabilities both in locally stored container images and images stored within GCP registries. With On-Demand Scanning, vulnerabilities can be surfaced as soon as  an image is built, well before the image is pushed to a registry.


Ignoring the stupid name (scanning for vulnerabilities at build time should be called scanning for vulnerabilities not “shifting left”) this is a welcome announcement.

Google is right, your vulnerability scanning should ideally be done at the point where you build the image, not when it’s deployed, run or sometime after launch (such as at the annual pentest).  This tool will make that easier in organisations that are using the Google cloud platform.


## [A Security Review of Docker Official Images: Which Do You Trust?](https://blog.aquasec.com/docker-official-images)

[https://blog.aquasec.com/docker-official-images](https://blog.aquasec.com/docker-official-images)

> A full list of deprecated official images is provided at the end of this post for reference. In addition to the images that had a formal deprecation notice, we found images with a large number of unpatched vulnerabilities but no formal deprecation information.
> 
> The following official images had more than 50 unpatched vulnerabilities when scanned with Trivy’s ignore-unfixed option:
> 
> nuxeo:latest - 186
> backdrop:latest - 173
> kaazing-gateway:latest - 95
> centos:latest - 86
> Of these, perhaps the most interesting is the CentOS image, which is a commonly used base image.


If even the formal dockerhub official images includes images that have been deprecated for 4 or more years, or contain a centos image with over 80 known vulnerabilities, then it doesn’t bode well for the ecosystem that companies are building on top of these.

This is even more reason to use a thin, up to date base image and roll it yourself as a base image, so you know that all your internal teams are using a patched and managed base image.


## [A decade and a half of instability: The history of Google messaging apps | Ars Technica](https://arstechnica.com/gadgets/2021/08/a-decade-and-a-half-of-instability-the-history-of-google-messaging-apps/)

[https://arstechnica.com/gadgets/2021/08/a-decade-and-a-half-of-instability-the-history-of-google-messaging-apps/](https://arstechnica.com/gadgets/2021/08/a-decade-and-a-half-of-instability-the-history-of-google-messaging-apps/)

> Because no single company has ever failed at something this badly, for this long, with this many different products (and because it has barely been a month since the rollout of Google Chat), the time has come to outline the history of Google messaging. Prepare yourselves, dear readers, for a non-stop rollercoaster of new product launches, neglected established products, unexpected shut-downs, and legions of confused, frustrated, and exiled users.
> 
> Table of Contents
> 
> * Google Talk (2005)—Google's first chat service, built on open protocols
> *  Google Talk ran Android's entire push notification system
> *  The slow death of GTalk
> *  Google Voice (2009)—SMS and Phone calls get a dose of the Internet
> *  Google Wave (2009)—An email killer from the future
> *  Nobody knew what Wave was for or how to use it
> *  Google Buzz (2010)—The non-consensual social network
> *  Slide’s Disco (2011)—An independent app escapes the Googleplex
> *  The Google+ Era (2011)—Google's social panic
> *  Google+ Hangouts video chat—The first Hangouts
> *  Google+ Huddle/Messenger—I guess we should have some kind of DM function
> *  A competitor emerges—iMessage has entered the chat
> *  One more competitor—WhatsApp is now worth $22 billion
> *  Google Docs Editor Chat (2013)—Just like Gmail chat, but not integrated with anything
> *  Google Hangouts (2013)—Google's greatest messaging service
> *  The death of Hangouts, unified Google messaging, and hope
> *  Google Spaces (2016)—A messaging app for Google I/O 2016 attendees
> *  Google Allo (2016)—Google's dead-on-arrival WhatsApp clone
> *  Allo's legacy: The Google Assistant
> *  Google Duo (2016)—A video companion app for... WhatsApp?
> *  Google (Hangouts) Meet (2017)—Not Zoom
> *  YouTube Messages (2017)—Yes, this was really a thing
> *  Google (Hangouts) Chat (2018)—Part 1: Cloning Slack is actually a good idea
> *  Google Maps Messages (2018)—Business messaging, now with the instability of Google
> *  Google & RCS (2019)—So we found this dusty old messaging standard in a closet...
> *  RCS is bad, and anyone who likes it should feel bad
> *  Google Photos Messages (2019)—You get a messaging feature! And YOU! And you!
> *  Google Stadia Messages (2020)—Two great tastes that taste great together
> *  Google Pay Messages (2021)—We actually learned nothing from Google Allo
> *  Google Assistant Messages (2021)—Text and voice chat, for families?
> *  Google Phone Messaging (2021)—Isn't this going a little too far?
> *  Google Chat, Part 2 (2021)—No wait, this is actually a consumer app now!
> *  Is anyone in charge at Google?


Yes, that’s just the table of contents.

This is an amazing long read that essentially shows blunder after blunder.  The issue here feels like one of culture, Google has long argued that it has a culture of allowing technologists to lead the way and make decisions, and that’s resulted in huge successes elsewhere, but messaging has been a pretty consistent failure because it needs to be so ingrained in eveyr other product and every product decision.

> The biggest legacy of Google Meet will probably be that it's not Zoom, a video conferencing app that absolutely exploded during the COVID-19 pandemic and quickly became a household name. As the pandemic raged across the globe, people were locked down at home and needed a way to communicate for work, school, and fun. Suddenly, everyone in the modern world entered the video chat market, and the world needed to pick a service.
> 
> Nine years after the launch of Google+ Hangouts group video chat in 2011, would you believe that Google still wasn't ready for the COVID video chat era? Google was busy re-re-re-re-launching its video chat solution, so it was caught totally flat-footed when COVID hit. Google Meet just barely got off the ground. Meet was locked behind the GSuite paywall until the very end of April, which was about two months into the work-from-home, remote schooling trend in many areas. Meet was also in the middle of a rebrand from "Google Hangouts Meet" to "Google Meet," which was also happening in April 2020, when Zoom was already hockey-sticking up the daily usage charts. That's nine years into the group video chat market, and when the golden ticket hit, Google had no product ready and no brand recognition. Instead, Google was just starting to launch, or really re-launch, a product.

This, in my mind, is the most damning finding from this analysis, to have built and engineered something effectively 9 years before it’s needed, and still not be able to pivot to use it when needed is a cultural issue that might be the first signs of the death of a dinosaur.

It is however worth remembering that many of these decisions may have been “even over” decisions, and if Google had invested in messaging, we might not have Chrome, Android, GMail, Google Suite or Google Cloud in the same way now, as that attention might have been manifested elsewhere.


