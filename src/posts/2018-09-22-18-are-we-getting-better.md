---
title: "18 - Are we getting better?"
date: 2018-09-22
description: "This week, I'm keynoting at Agile Cambridge 2018 https://agilecambridge.net/2018/ on the topic of \"Does Agile make us less secure\" which has led to spending a lot of the past few weeks wondering whether we are actually getting any better at security."
permalink: /are-we-getting-better/
---

This week, I'm keynoting at Agile Cambridge 2018 https://agilecambridge.net/2018/ on the topic of "Does Agile make us less secure" which has led to spending a lot of the past few weeks wondering whether we are actually getting any better at security.

We see that the technology available to us in security is constantly moving, and if you believe the endless APT reports from various vendors, you would believe that the world is filled with terrifyingly skilled attackers who can get access to your systems with just a simple thought.

But our processes and systems for ensuring security don't actually seem to be getting any better.  Instead I think a lot of cybersecurity is more the emperors new clothes, in that we've convinced ourselves that because we have a shiny expensive new tool, we are fully protected.

We are getting better in small areas, and it's looking at these that gives me hope.  The ATT&CK framework from MITRE is something I was aware of before but took a proper look at this week, and the idea that we can start developing a shared language around threat models and frameworks is quite exciting.

We've also seen the declassification and publication of a secure operating system from France that looks interesting.  Until now there have been very few good products in this area, and it's nice that there are now multiple open source operating systems to choose from.

## [Andrew Greenway: does the civil service reward bluffers? | Civil Service World](https://www.civilserviceworld.com/articles/opinion/andrew-greenway-does-civil-service-reward-bluffers)

[https://www.civilserviceworld.com/articles/opinion/andrew-greenway-does-civil-service-reward-bluffers](https://www.civilserviceworld.com/articles/opinion/andrew-greenway-does-civil-service-reward-bluffers)

> I worry that the depth of policy knowledge may be dissolving in important corners of Whitehall, as experience walks out the door and systems fail to preserve it. And when anyone begins losing their memory, they tend to cling harder to things they can remember — in this case, the rituals and behaviours grooved hard into the institutional psyche


This is true of cybersecurity as well.  As your organisation loses the memory of why certain decisions were taken, people tend to revert to the rituals and behaviours that they've seen be successful.  This slowly calcifies into slow and difficult accreditation or compliance processes where the questions make no sense to the context or system under consideration.


## [The next 50 years of cyber security. – Ryan McGeehan – Medium](https://medium.com/@magoo/next50-ea33c5db5930)

[https://medium.com/@magoo/next50-ea33c5db5930](https://medium.com/@magoo/next50-ea33c5db5930)

> Much like pre-1950 meteorology, the history of computer security has always been about of innovation. We’ve invented and built most of the tooling, infrastructure, skills, and language so that we can perform jobs that mitigate risk. We have a proud industry that proves our concepts, but we’re failing.
> 
> What does it take to start a similar “50 year” effort?
> It will require massive collaboration, activism, regulation, and agreeable forecasting methods to take advantage of it.


This is a good article about how we need cybersecurity to be more measurable.  But I think that there is too much incentive for vendors and organisations to continue to muddy the waters in "cyber", and too little information available to consumers to actually achieve what Ryan outlines for us.


## [Zero Day Initiative — ZDI-CAN-6135: A Remote Code Execution Vulnerability in the Microsoft Windows Jet Database Engine](https://www.zerodayinitiative.com/blog/2018/9/20/zdi-can-6135-a-remote-code-execution-vulnerability-in-the-microsoft-windows-jet-database-engine)

[https://www.zerodayinitiative.com/blog/2018/9/20/zdi-can-6135-a-remote-code-execution-vulnerability-in-the-microsoft-windows-jet-database-engine](https://www.zerodayinitiative.com/blog/2018/9/20/zdi-can-6135-a-remote-code-execution-vulnerability-in-the-microsoft-windows-jet-database-engine)

>  Microsoft continues to work on a patch for this vulnerability, and we hope to see it in the regularly scheduled October patch release. In the absence of a patch, the only salient mitigation strategy is to exercise caution and not open files from untrusted sources


This looks like an interesting vulnerability, but the fact that the advice is "Don't open files on your computer" is a bit sad


## [MITRE ATT&CK](https://attack.mitre.org/wiki/Main_Page)

[https://attack.mitre.org/wiki/Main_Page](https://attack.mitre.org/wiki/Main_Page)

> MITRE’s Adversarial Tactics, Techniques, and Common Knowledge (ATT&CK™) is a curated knowledge base and model for cyber adversary behavior, reflecting the various phases of an adversary’s lifecycle and the platforms they are known to target. ATT&CK is useful for understanding security risk against known adversary behavior, for planning security improvements, and verifying defenses work as expected.


This is a nice bit of work to categorise and define the variety of ways that someone can carry out an attack on your infrastructure.  Very useful if you are doing threat modelling.


## [Multi-Cloud Is a Trap – Brave New Geek](https://bravenewgeek.com/multi-cloud-is-a-trap/)

[https://bravenewgeek.com/multi-cloud-is-a-trap/](https://bravenewgeek.com/multi-cloud-is-a-trap/)

> Generally speaking, the risk posed to businesses by vendor lock-in of non-strategic systems is low. For example, a database stores data. Whether it’s Amazon DynamoDB, Google Cloud Datastore, or Azure Cosmos DB—there might be technical differences like NoSQL, relational, ANSI-compliant SQL, proprietary, and so on—fundamentally, they just put data in and get data out. There may be engineering effort involved in moving between them, but it’s not insurmountable and that cost is often far outweighed by the benefits we get using them


I totally agree with this.  [active-active] Multi-cloud is a terrible idea for almost all organisations.


## [Let's Encrypt at Scale](https://engineering.autotrader.co.uk/2018/09/04/letsencrypt-at-scale.html)

[https://engineering.autotrader.co.uk/2018/09/04/letsencrypt-at-scale.html](https://engineering.autotrader.co.uk/2018/09/04/letsencrypt-at-scale.html)

> Let’s Encrypt uses an automated system that verifies you “own” the domain, checking that you have control of it. Unlike regular certificates which can last for years, Let’s Encrypt makes it their policy to expire them regularly, forcing you to redo the verification process each time. Whilst this solved the problem of expensive manual verification methods, this did mean that we had to have something in place that handled this process elegantly.


This is a nice review of deploying LetsEncrypt for a large number of client websites, including a diversion into what went wrong.


## [How to access private Azure DevOps repos from a Dockerfile! – Jessica Deen](https://jessicadeen.com/tech/how-to-access-private-azure-devops-repos-from-a-dockerfile/)

[https://jessicadeen.com/tech/how-to-access-private-azure-devops-repos-from-a-dockerfile/](https://jessicadeen.com/tech/how-to-access-private-azure-devops-repos-from-a-dockerfile/)

> Now, for your Docker image build you will want to stick to multi-stage builds because of the way layers works. In a single stage build you might export an ARG to capture the private key file and then delete it but the contents of that file will remain in a layer and is therefore insecure. Best practice is multi-stage builds so we’ll demo that here. It’s also smaller and lighter


This is a cute trick.  Putting secrets into a docker build, even if you delete them later might result in the secrets still being around later, but using a multi-stage build discards all of the first stage and only copies the filesystem over with the copy instruction.

Obviously, this is only good for credentials used during the build process, not the deployed containers


## [The CLIP OS Project | CLIP OS](https://clip-os.org/en/)

[https://clip-os.org/en/](https://clip-os.org/en/)

> The CLIP OS project is an open source project maintained by the ANSSI (National Cybersecurity Agency of France) that aims to build a hardened, multi-level operating system, based on the Linux kernel and a lot of free and open source software.


This is an interesting project that reminds me of https://www.qubes-os.org.  Both attempt to define a secure workstation that can browse an untrusted internet while allowing the user to read and edit secure material.  But where QubesOS uses a Xen hypervisor, and specialist UI, CLIP-OS seems to use a shared linux kernal and linux vserver containers for separation.


