---
title: "96 - The cloud is more secure"
date: 2020-04-05
description: "I’m bored of the Zoom infosec debacle at the moment, so I thought I’d look more at one of my favourite hobby horses, the adoption and use of the cloud and how to use it securely."
permalink: /the-cloud-is-more-secure/
---

I’m bored of the Zoom infosec debacle at the moment, so I thought I’d look more at one of my favourite hobby horses, the adoption and use of the cloud and how to use it securely.

Cloud computing has been around for a long time, and infosec professionals have spent a long time sneering at it.  If I go to an infosec conference, I guarantee that I’ll see “the cloud is just other peoples computers” stickers on a large percentage of laptops around the place.

I’ve been lucky enough to be at the forefront of the move to cloud, as, I suspect have many of you who are reading.  [Forbes reckonend back in 2018 that about 41% of enterprise workloads will be on public cloud](https://www.forbes.com/sites/louiscolumbus/2018/01/07/83-of-enterprise-workloads-will-be-in-the-cloud-by-2020/#3b7ad92b6261) by 2020, with another 40% in private or hybrid clouds.  That still means that 1/5 workloads have not been shifted to cloud.  The estimates are that something like 95% of companies have some cloud resources now, but that’s been growing fast, wind back just a couple of years and there were still around 1/3rd of companies that weren’t using cloud computing.

The biggest concern that is often quoted is that of security.  It doesn’t matter which business intelligence reports you read, Gartner, Forbes, you name it, they all come back with the same result... Security concerns are the reason that companies haven't adopted cloud as fast as they would would like, and security concerns are cited by leaders.  But where do those leaders get those security concerns?  Probably from their security professionals in their organisations, the ones who have the faulty thinking about the operating model of cloud computing.

The failure here, as always, is the failure of applying a previous generational set of tools and processes to a new generation of capabilities.  The processes that you use to manage a physical data center are optimised over years of being applied to physical infrastructure and are therefore inherintly flawed in attempting to manage cloud workloads.  The cost of creating and destroying equipment is orders of magnitude smaller in cloud environments, which means that processes that assume that resources must be shared and therefore need coordination are wholly inappropriate.  It also means that security properties that we used to worry about, in particular the administration of shared components are no longer the ones that we should be worrying about.

The new security properties, tools and processes that you need to apply to cloud computing are also just as important in their lack of adoption.  Many of the public S3 buckets should have and could have been caught by modern practices, but instead older practices cannot pivot fast enough to catch that kind of problem.  

We need to move beyond “the cloud is other peoples computers” as if that’s the big risk, and move towards standardising the proper use of cloud computing.  The ubiquitous, convenient and on-demand access to computing resources that cloud provides is exactly the thing that has enabled business agility and allowed some of the amazing teams in Government to spin up valuable resources for citizens during the pandemic. When we look back at the government handling of this pandemic, and the services that were created, we’ll see a marked difference in the offerings between the departments that had cloud native development capabilities, and those that just considered cloud to be another data center.

## [Microsoft’s Skype struggles have created a Zoom moment - The Verge](https://www.theverge.com/2020/3/31/21200844/microsoft-skype-zoom-houseparty-coronavirus-pandemic-usage-growth-competition)

[https://www.theverge.com/2020/3/31/21200844/microsoft-skype-zoom-houseparty-coronavirus-pandemic-usage-growth-competition](https://www.theverge.com/2020/3/31/21200844/microsoft-skype-zoom-houseparty-coronavirus-pandemic-usage-growth-competition)

> The company went in a completely different direction with Skype in 2017, with a design that turned the app into something that looked like Snapchat. Unsurprisingly, people weren’t happy with the design and Microsoft was forced to kill off the Snapchat-like features and redesign Skype once again a year later.
> 
> During this time, Microsoft also pushed Skype for Business as the replacement for its Lync (Office Communicator) enterprise instant messaging software. Skype looked like it would power the future of Microsoft’s chat services across consumers and businesses, until Microsoft Teams arrived in 2016. 


This is a good reminder that when you hear people talking about how Zoom isn’t that good, and that they think that people should use your organisations Microsoft solution, or your organisations Google solution, there’s a lot of brand incoherence in these solutions.

Microsoft still supports old products for various reasons, which means that there are at least 3 video calling apps in the Microsoft ecosystem, Skype, Skype for business, and Teams.  Two of those are called Skype but have vastly different user experiences, and lots of people got on board with Skype for calling family back in 2015 or so and were badly burnt by all the changes.  You can tell them that Skype for Business isn’t the same as Skype, but it’s not going to make people willingly use it.

In Google land, things are far clearer, you can use Google Hangouts Meet, Google Duo, Google Hangouts, Google Chat, Google Talk, Google Voice.  I kid somewhat, but it can get awfully confusing.  I’m a google power user, and I tend to use all of their features and functionality and I only found out a few weeks ago that there was such a thing as Google Chat, a slack like competitor (which includes the ability to start a video call with everyone in a room).

It’s no wonder that people are discarding their unusable corporate offerings and flooding to a competitor that does one thing, and does it really really well.  I’ve had all kinds of issues setting up meetings in departments with our corporate tools.  People who didn’t have a corporate account couldn’t join my Skype for business meeting, but they could dial in from phone.  Google hangouts often work but only if the guest has a google account of some form, and getting them in otherwise is hard.
But in the meantime, I’ve not had a single person not be able to join a Zoom meeting easily and simply on the first try, regardless of whether it’s business or social, it really does just work for people regardless of device or process (with the exception of some draconian government departments that just seem to block everything on the network, but those people invariably end up just using their personal device from guest WiFi or a nearby coffee shop to get around that).


## [Hackers breach FSB contractor and leak details about IoT hacking project | ZDNet](https://www.zdnet.com/article/hackers-breach-fsb-contractor-and-leak-details-about-iot-hacking-project/)

[https://www.zdnet.com/article/hackers-breach-fsb-contractor-and-leak-details-about-iot-hacking-project/](https://www.zdnet.com/article/hackers-breach-fsb-contractor-and-leak-details-about-iot-hacking-project/)

> Based on file timestamps, the project appears to have been put together in 2017 and 2018. The documents heavily reference and take inspiration from Mirai, an IoT malware strain that was used to build a massive IoT botnet in late 2016, which was then used to launch devastating DDoS attacks against a wide range of targets, from ISPs to core internet service providers.
> 
> The documents propose building a similar IoT botnet to be made available to the FSB. Per the specs, the Fronton botnet would be able to carry out password dictionary attacks against IoT devices that are still using factory default logins and common username-password combinations. Once a password attack was successful, the device would be enslaved in the botnet.


This feels like a typical “nation states are building capability” type thing.  There’s something quite bold about the intention to build an IoT botnet, and there’s still an internationally legal grey area about whether nation states should have the ability to target and takeover undefended internet of things devices.  I don’t think that they would meet the definition of valid targets in a conflict, but there’s some argument that they might be considered the landscape and terrain of cyber conflict.  There should be no surprise that this is a capability that Russia wants to build, and feels it’s legitimate to have the capability even if it’s never used.

The leaking of the sources and methods that the FSB is using to build cyber capability is more of a worry I suspect.  There’s been a few of these before, and just like we’ve seen with America, increasing outsourcing of the intelligence machinery to contractors means that the security boundary gets harder and harder to protect.  If the FSB can’t protect its contractors or rely on them to be sufficiently secure, how well do you think your contractors are faring in this area?


## [Involving Engineers in Incident Management: QCon London Q&A](https://www.infoq.com/news/2020/03/engineers-incident-management/)

[https://www.infoq.com/news/2020/03/engineers-incident-management/](https://www.infoq.com/news/2020/03/engineers-incident-management/)

> What have you done to enable continuous learning from incidents?
> 
> Parkinson: One thing we did recently was move our incident reports into GitHub issues. Having all our incidents documented in one place has allowed our engineers to explore the full history, with each person able to add their own insights. The extra metadata available through labels and being able to search incidents is a real step up from what we used to do, which was committing notes into a repository.
> 
> The main thing we started in 2019 however was to run incident workshops: paper-based incident simulations using old incidents. This lightweight method of getting people used to handling incidents has also been a great way of getting new eyes on old problems.


There’s an interesting maturity curve with incident response and follow on actions.  We see organisations move from managing incidents into learning from incidents, including covering things such as blame free post mortems in order to maximise learning but organisations often stop there.  Don’t get me wrong, I’ve worked in lots of places where we didn’t even do that, and being able to learn from an outage is critical in getting the changes made to a system to improve resilience and response in the next outage (and thus reduce the impact of future outages).  But the learning is often restricted only to the people who were involved in the incident.  We write up incident responses but do we ever make use of them?  Do we read them?

This move by the FT to actively make incident responses easier to search, easier to read and easier to access is a strong move towards active learning within the organisation which enables everyone to learn from these outages.  The other thing, then is the fact that they go back and reuse the incidents in simulations.  This helps the learning spread around the organisation and encourages everyone to continue to improve their response capability.


## [The NCSC Research Problem Book - NCSC.GOV.UK](https://www.ncsc.gov.uk/blog-post/the-ncsc-research-problem-book)

[https://www.ncsc.gov.uk/blog-post/the-ncsc-research-problem-book](https://www.ncsc.gov.uk/blog-post/the-ncsc-research-problem-book)

> The problems we would like to solve
> 
> Given these provisos, we're publishing our Problem Book, with the aim of shedding a little light on what we're up to.
> 
> We've arranged some of our more significant long term challenges into 7 themes, designed to emphasise the sorts of problems we'd like to solve.
> 
> The themes are outcome (rather than technology) focused, as there is often more than one possible approach to achieving a particular goal. Within each theme, we have active work items, and areas of interest. These latter items, we may not be actively pursuing right now, but would be interested solutions proposed from other sources.
> 
> Our hope is that the Problem Book will help to inform those looking to conduct innovative cyber security research of our interests, be they in academia, industry or government.


This is a really interesting list of the sorts of things that the NCSC is interested in researching and building on in the next few years.  I’ve linked to the blog post announcing it here because it outlines the thinking, but you can also read [the problem book itself](https://www.ncsc.gov.uk/information/the-ncsc-research-problem-book).

The themes of managing critical risk, “transparency”, resilience, usability, incentives and behaviours, separation of concerns and modelling shows that much of the security problems that NCSC sees over the next 5 years are not primarily technical problems.  Many of these are behavioural problems, either in how users use these systems securely, or how we behave as security experts in understanding the systems and how they work.

The only one I have any issue with really is the name of Transparency for the second theme.  It’s described as using data to better make decisions, and the areas of research are more around awareness of your own environment and systems, which I think is not quite the same as transparency.  Personally I’d have called this area Awareness.  Either way, the research opportunities under it are interesting and valuable.


## [GitHub - secdevops-cuse/CyberRange: The Open-Source AWS Cyber Range](https://github.com/secdevops-cuse/CyberRange)

[https://github.com/secdevops-cuse/CyberRange](https://github.com/secdevops-cuse/CyberRange)

> This CyberRange project represents the first open-source Cyber Range blueprint in the world.
> 
> This project provides a bootstrap framework for a complete offensive, defensive, reverse engineering, & security intelligence tooling in a private research lab using the AWS Cloud.
> 
> This project contains vulnerable systems and a toolkit of the most powerful open-source / community edition tools known to Penetration testers.
> 
> It simply provides a researcher with a disposable offensive / defensive AWS-based environment in less than 5 minutes.


This is an amazing tool, I'm still waiting for my account to be activated, as they don't want to distribute all of the AMI's publicly yet, so you need to submit your AWS account ID to try it out.

This will spin up a mix of estates, both a red team estate running Kali, Commando, and SEED, a set of targets or vulnerable machines from various CTF images from VulnHub and other places. 

It also includes a set of defender boxes that should have logs shipped to them, and some reverse engineering and honeypot systems.  This should let your defenders have a chance to see what the red teams attacks look like in typical operations tools.

The aim of the project is to be compatible with the AWS Free Tier limits.  Putting some rough estimates into an AWS Calculator, I think that if you spin up the entire estate of 27 machines for an entire day, you are looking at a bill of around $20-$30 or so, but that's with a lot of assumptions around it.   This isn't really a thing you want to keep running month in and month out, even if you only run it for 8 hours a day, you will spend around $1000 for a months use.  But for training for your team, that's not an unreasonable budget to spend.


## [Latacora - The SOC2 Starting Seven](https://latacora.micro.blog/2020/03/12/the-soc-starting.html)

[https://latacora.micro.blog/2020/03/12/the-soc-starting.html](https://latacora.micro.blog/2020/03/12/the-soc-starting.html)

> First: for us, SOC2 is about sales. You will run into people with other ideas of what SOC2 is about. Example: “SOC2 will help you get your security house in order and build a foundation for security engineering”. No. Go outside, turn around three times, and spit. Compliance is a byproduct of security engineering. Good security engineering has little to do with compliance. And SOC2 is not particularly good. So keep the concepts separate.
> 
> This is not an instruction guide for getting SOC2-certified. Though: that guide would be mercifully short: “find $15,000, talk to your friends who have gotten certified, get referred to the credible auditor that treated your friends the best, and offer them the money, perhaps taped to the boom box playing Peter Gabriel you hold aloft outside their offices”.


This is an absoutely brilliant guide to getting your security house in order.   I totally agree with the quoted section on the value of SOC2, it's not about building good security, it's about measuring compliance with a defined process that you already setup.

However, the 7 things listed here:

1. Single Sign-On
2. PRs, Protected Branches, and CI/CD
3. Centralized Logging
4. Terraform Or Something
5. CloudTrail And AssumeRole
6. MDM
7. VendorSec

These are all the areas that I think a modern digital team should be hitting as soon as possible.  Regardless of whether you are going to be going through SOC, you should be comfortable that you do these things well, and if not, they should be on your security plan.



## [How Attackers Could Use Azure Apps to Sneak into ...](https://www.darkreading.com/cloud/how-attackers-could-use-azure-apps-to-sneak-into-office-365/d/d-id/1337399)

[https://www.darkreading.com/cloud/how-attackers-could-use-azure-apps-to-sneak-into-office-365/d/d-id/1337399](https://www.darkreading.com/cloud/how-attackers-could-use-azure-apps-to-sneak-into-office-365/d/d-id/1337399)

> The Varonis research team encountered this vector while exploring different ways to exploit Azure, explains security researcher Eric Saraga. While they found a few campaigns intended to use Azure applications to compromise accounts, they discovered little coverage of the dangers. They decided to create a proof-of-concept apps to demonstrate how this attack might work. It's worth noting they did not discover a flaw within Azure, but instead detail ways its existing features could be maliciously used. 
> 
> "We decided to do the proof of concept after seeing potential danger — not from any specific trends," he says. "However, if anybody is utilizing what we described here to launch attacks, it will most certainly be an [advanced persistent threat] group or a very sophisticated attacker." As the cloud advances, Saraga anticipates we'll start seeing campaigns designed to use simpler versions of this attack.


This is here for two reasons, one is that it’s often unclear to many security teams just how much access programs and API’s can have their underlying infrastructure.  It’s super easy to grant rights to things, especially for users to give rights to an application without understanding just what it can do.

However, a word of warning.  As Varonis points out, they have never seen this attack in the wild, used by real attackers.  They created this proof of concept specifically to market that this was possible.  You shouldn’t waste time defending against a hypothetical attack until you are confident that you have defended against all of the real attacks that are out there.


## [How to Embezzle Money Using Amazon AMIs · Security in the Cloud](https://blog.iamwritingaboutsecurity.com/posts/how-to-embezzle-money/)

[https://blog.iamwritingaboutsecurity.com/posts/how-to-embezzle-money/](https://blog.iamwritingaboutsecurity.com/posts/how-to-embezzle-money/)

> If a malicious entity, let’s call him Lawrence was to:
> 
> Duplicate the standard Amazon CentOS AMI
> Publish it on the Amazon Marketplace, charging $0.02 per hour for use
> Write a great CloudFormation template that utilises his Amazon CentOS AMI
> Post his Cloudformation template on Stackoverflow as an answer to questions or other locations
> If people then started using it, Lawrence would make $0.02/hour for each of the instances deployed by his CloudFormation templates. That is approximately $14 per month. This could go completely undetected on some bills and even if it was detected, the account owners would have no recourse to get a refund. They chose to use Lawrence’s template (and AMI). There is nothing illegal happening here.
> 
> [...]
> 
> But what about your instances that are already deployed? How do you know that these can be trusted, having already been deployed before the IAM policies existed?
> 
> AWS Config can perform checks to ensure all instances deployed are utilising approved AMIs.


This is a lovely attack vector.  This is written up as a fraud vector, you are paying a tiny bit extra for each instance you use, which will add up over time and may well be unnoticable in many organisations cloud bills.

But of course, the additional threat vector here is that you can put anything you want in that AMI, so you could put in a sneaky backdoor that lets attackers get in, you could put bitcoin mining software, pretty much anything you want.  

Restricting the use of AMI's down to a whitelist of AMI's totally fixes this problem, but may slow down the agility of your teams, so you probably want to decide between a whitelisting approach, or a trust but verify audit approach.  Personally, I'd go for your security team publishing a list of recommended AMI's (and encoding those into tooling), and then auditing the use of other AMI's using AWS Config.


## [Azure Security Benchmark—90 security and compliance best practices for your workloads in Azure](https://www.microsoft.com/security/blog/2020/01/23/azure-security-benchmark-90-security-compliance-best-practices-azure-workloads/)

[https://www.microsoft.com/security/blog/2020/01/23/azure-security-benchmark-90-security-compliance-best-practices-azure-workloads/](https://www.microsoft.com/security/blog/2020/01/23/azure-security-benchmark-90-security-compliance-best-practices-azure-workloads/)

> The Azure security team is pleased to announce that the Azure Security Benchmark v1 (ASB) is now available. ASB is a collection of over 90 security best practices recommendations you can employ to increase the overall security and compliance of all your workloads in Azure.
> 
> The ASB controls are based on industry standards and best practices, such as Center for Internet Security (CIS). In addition, ASB preserves the value provided by industry standard control frameworks that have an on-premises focus and makes them more cloud centric. This enables you to apply standard security control frameworks to your Azure deployments and extend security governance practices to the cloud.
> 
> You can find the full set of controls and the recommendations at the Azure Security Benchmark website. 
> 
> ASB is integrated with Azure Security Center allowing you to track, report, and assess your compliance against the benchmark by using the Security Center compliance dashboard. In addition, the ASB impacts Secure Score in Azure Security Center for your subscriptions.


This is a nice addition to Azure.  AWS already has some of this with AWS Inspector (for CIS hardening) and AWS Config.  Sadly, it looks like Azure's Security Benchmark is a compliance configuration checker (more like AWS Config), rather than an automated security scanning solution.

However, if you are running existing Azure workloads, you should be turning this on and looking at the recommendations in Azure Security Center, although you'll probably need to opt in to paying for Security Center to get the most value out of this.


## [Doberman says…](https://snyk.io/blog/cloud-transforms-it-security-appsec/)

[https://snyk.io/blog/cloud-transforms-it-security-appsec/](https://snyk.io/blog/cloud-transforms-it-security-appsec/)

> What needs to change is how we defend against these infrastructure threats. Today’s solutions and practices are designed for central IT teams, not independent application teams. They are sometimes retrofitted into a shape that separate teams may use, but it’s quite rare that they truly fit that use-case. 
> 
> We need to embrace a new perspective, built on this new reality of “infrastructure as application”. Such rethinking is a big task, and not one I can summarise in a few simple bullets, but here are some examples of changes to consider:
> 
> * Reconsider your security org structure for securing cloud products. Security for IT stacks was designed to partner well with the IT org structure, but security for application stacks should be structured to work with the development organization. I have much more to say about this topic, but that will likely be a post on its own…
> 
> * Understand the application developer’s needs. Take the time to understand their reality, not just their technology, and aim to adapt your practices, tools and expectations to match theirs. The industry best practices are often based on the needs of IT, not dev, so don’t rely on them.
> 
> * Don’t assume your existing pre-cloud solutions are the right ones for cloud apps. While keeping the same tools across your old and new stacks is convenient, it’s unlikely they will serve both realities well. Check what other tools your vendor has to offer — or other vendors around — and choose the right tool for the cloud environment.
> 
> * Invest in flexible, API-driven, self-serve security tools. IT teams are a central function, allowing you to invest more time in custom integration. Dev teams and stacks vary significantly more. Invest in tools that can adapt to different surroundings, while providing similar security controls and governance. 


This is a great list of how you need to rethink security as you move towards cloud.  It’s easy to think that the cloud is just another data center, but it’s actually fundamentally different.  The key thing here for me is acknowledging that your existing tools and processes are not fit for purpose in a cloud environment.  That’s not to say that they are bad tools and processes, it’s to acknowledge that if you keep applying existing tools and processes in an environment unsuited for them, you will hamstring that environment and fail to take advantage of the benefits that it can offer.

Watching traditional infrastructure teams still insist on retaining control, requiring change control processes before giving out a server, and preventing self service is like watching someone upgrade their pushbike into a motorbike and then insist on pushing it everywhere.  They long to go back to the good old days as this new thing is “heavy and unwieldy”.


