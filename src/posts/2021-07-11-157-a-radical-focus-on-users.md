---
title: "157 - A radical focus on users"
date: 2021-07-11
description: "Security has for many years been the purview of a rather niche set of people."
permalink: /a-radical-focus-on-users/
---

Security has for many years been the purview of a rather niche set of people.

Not that long ago at all (potentially this week in some organisations), security professionals would be called in purely on an engagement basis.  The system under test would be scoped, contained and the security team would get to play with it, deploying all kinds of tools to see if they can find security flaws.  They would then write that up in a report, highlight any serious risks, and in the majority of cases, a business representative would accept the risks and trust that the mere existence of the report indicated that the system was now “secure”.  In Government we tended to call this system accreditation, and I’ve seen accreditation reports that extend to 2 CD’s, that cover systems in excruciating detail, and for which the business’s only concern is the checkbox of “Did it go through the accreditation process”.

But the way that people consume their IT and digital services has been changing over the past few decades.  The rise of SaaS tools means that business units can buy their own software, without going through a central team.  It means that individual users have access to encrypted messaging products, shared document collaboration tools and easy to setup slack workspaces.

But people are generally terrible at making judgements about security.  The report into security usability shows that individuals users have a fundamentally  faulty model of how their technology works, and that they build mental models around that faulty technology model that represent what they think is secure use.  

The obstacles to the adoption of secure communication tools isn’t how easy the tool is to use, many of the most secure tools are quite easy to use, it’s the network effect, it’s whether the person they want to talk to uses it.
But furthermore, users actively reject some of the more secure systems.  The research showed that most users believed that 3 properties that experts believe indicate good cryptographic hygiene, “documentation, open source code and code audits” were in fact negative because they believed that good security required obscurity about how it worked.

Because of the model I described before, security hasn’t really had to focus on the customer, on the end user.  Security tools are often hostile to the pentester, requiring you to learn and understand its quirks before you can use it.  Secure platforms can put in place significant barriers to adoption, thinking that it makes them more secure (which it might), but not realising that damaging the network effect is the most damaging thing to adoption.

We don’t need to “educate users about security” or even “educate users about technology” so that their mental models are right.  It doesn’t matter is Chris in accounts actually understands what Phishing is, or how APT’s might target them.  What matters is that the software they use is built to be as secure as it needs to be, but that it most importantly works for the user, is easy to use and doesn’t scare them with buttons to “enable content” (looking at you Microsoft Word!)

We also need to consider that many of the people who work in security are also users of some shocking software.  Whether that’s your pen testers or red team using buggy or difficult to use software that’s named after an internet in-joke, or whether it’s your blue team looking at a security operations platform and seeing tens of thousands of logs for every device because the security software just emits far too much noise.

We can learn from agile software delivery and digital transformation, that success comes from a radical focus on the users, on understanding their needs, and on doing the hard work to make their job simple and easy.

## [Obstacles to the Adoption of Secure Communication Tools](https://jbonneau.com/doc/ASBDNS17-IEEESP-secure_messaging_obstacles.pdf)

[https://jbonneau.com/doc/ASBDNS17-IEEESP-secure_messaging_obstacles.pdf](https://jbonneau.com/doc/ASBDNS17-IEEESP-secure_messaging_obstacles.pdf)

> Several popular personal communication tools
> (e.g., WhatsApp, iMessage) have adopted end-to-end encryption,
> and many new tools (e.g., Signal, Telegram) have been launched
> with security as a key selling point. However it remains unclear
> if users understand what protection these tools offer, and if they
> value that protection. In this study, we interviewed 60 participants about their experience with different communication tools
> and their perceptions of the tools’ security properties. We found
> that the adoption of secure communication tools is hindered by
> fragmented user bases and incompatible tools. Furthermore, the
> vast majority of participants did not understand the essential
> concept of end-to-end encryption, limiting their motivation to
> adopt secure tools. We identified a number of incorrect mental
> models that underpinned these beliefs.
> 
> [...]
> 
> Our findings suggest not only a gap between users’ understanding of secure tools and the technical reality, but also a gap
> between users’ communication priorities and what the security
> research community imagines them to be.


An absolutely fascinating study that shows that most users do not think the way that the security community assumes that they think.

Users don't understand even the basics of encryption, have faulty mental models for which tools are secure or usable for certain actions, and confuse services for tools are lot.

The most important things in peoples mind includes whether the person they are communicating with uses the tool, the appropriateness of the tool for the situation (i.e. SMS and voice for formal conversations, IM for informal conversations).  Interestingly, almost all users felt that spoken voice conversations were more secure than written communications, irregardless of the technology involved, so phone calls from mobile phones are perceived more secure than say Whatsapp messages.


## [An Empirical Assessment of Endpoint Detection and Response Systems against Advanced Persistent Threats Attack Vectors | HTML](https://www.mdpi.com/2624-800X/1/3/21/htm)

[https://www.mdpi.com/2624-800X/1/3/21/htm](https://www.mdpi.com/2624-800X/1/3/21/htm)

> First, we illustrate that, despite the advances in static and dynamic analysis, as well as multiple log collection mechanisms that are applied by state-of-the-art EDRs, there are multiple ways that a threat actor may launch a successful attack without raising suspicions. As it will be discussed, while some of the EDRs may log fragments of the attacks, this does not imply that these logs will trigger an alert. Moreover, even if an alert is triggered, one has to consider it from the security operations center (SOC) perspective. Practically, an SOC receives multiple alerts and each one with different severity. These alerts are prioritized and investigated according to this severity. Therefore, low severity alerts may slip below the radar and not be investigated, especially once the amount of alerts in an SOC is high [2]. Furthermore, we discuss how telemetry providers of EDRs can be tampered with, allowing an adversary to hide her attack and trails.


This is a good read.  Many of the leading commercial EDR systems did successfully detect and alert on several of the attacks, meaning that deploying EDR is still going to protect you against “moderately advanced persistent threats”.  But it’s not a panacea against the most advanced adversaries, and so your SOC or threat team will need to be explicitly threat hunting, deploying views that hunt for correlated weak signals in order to find the bad actors amongst the noise.


## [Changing Security Tool Requirements in the New DevSecOps World](https://www.twilio.com/blog/changing-security-tool-requirements-in-the-new-devsecops-world)

[https://www.twilio.com/blog/changing-security-tool-requirements-in-the-new-devsecops-world](https://www.twilio.com/blog/changing-security-tool-requirements-in-the-new-devsecops-world)

> Before DevSecOps, the Security team would run their tools at the end of the development process and triage the results before working with Engineering on fixes. This meant that Engineering didn't have to deal with many results that weren't useful.
> 
> Now that engineers are direct customers of security scanning tools, it's important for the results to be accurate. False positives generate noise that make it more difficult to focus on real problems. If a scanning tool is leaving useless comments on pull requests or showing spurious results in the build system, it can cause fatigue in the Engineering team: they'll simply stop responding to the notifications. It's critical for the tools to report vulnerabilities with over 90% accuracy, even if it means leaving a few undetected. Once your team has identified a false positive, the tool must provide a way to flag it so that it doesn't get reported again.


The slow absorbtion of modern software development practices into security is creating a new model of security, one that mostly takes the term “security engineering” to seperate it from more compliance and advice based “information security”.

Security engineering is focused on helping development teams build their systems to be secure by design, but that means they are providing tools to developers, tools that need to be run speedily, easily and in continuous integration environments.  For many security people, these concepts are somewhat alien, they are used to tools that are run as part of an engagement, by a human who will read and intepret the results and put them into a word document in the end.

This direction of improving security tooling so that it’s focused on repeatable, reliable and regular tests is a good one, but it’s going to divide a security community that often just doesn’t work that way.


## [AWS Free Tier, where's your spending limit? 'I thought I deleted everything but I have been charged $200' • The Register](https://www.theregister.com/2021/05/28/aws_free_tier/)

[https://www.theregister.com/2021/05/28/aws_free_tier/](https://www.theregister.com/2021/05/28/aws_free_tier/)

> AWS does provide mechanisms for preventing cost overruns, primarily via email alerts which users can configure. It is even possible to set up automation so that the billing alert will automatically shut down instances, though this is relatively advanced (given that free tier issues are often encountered by novices).
> 
> There are caveats though: "If you launch more AWS resources than the AWS Free Tier covers in a short period of time, you can exceed the AWS Free Tier limits before AWS can proactively notify you about exceeding the AWS Free Tier usage limits," the docs explain.


This call for easily configurable spending limits on cloud resources is an important one.  There are lots of reasons for individuals as well as companies to want to implement spending limits on an account, whether it be guaranteeing that you haven't accidentally spend thousands, or whether it be to budget effectively.


## [Behind the scenes, AWS Lambda](https://www.bschaatsbergen.com/behind-the-scenes-lambda)

[https://www.bschaatsbergen.com/behind-the-scenes-lambda](https://www.bschaatsbergen.com/behind-the-scenes-lambda)

> Writing code and deploying it to AWS Lambda is as easy as baking a cake (depending on the type of cake). Lambda performs the heavy lifting for you, from provisioning to scaling. But where is the magic happening and how does it actually work under the hood? Lets find out together!
> 
> Lambda is split into a control plane and data plane. Each plane is responsible for a specific set of activities in the service. The Control Plane provides management APIs and manages integrations with all AWS services. Whilst the Data Plane is Lambda's Invoke API that triggers Lambda function invocations, this explanation is still very abstract but things will become clearer over time.


This is a dense but useful deep dive into how AWS Lambda is constructed under the hood.  All derived from public blog posts, open source code and conference talks given by the lambda engineers.

The complexity and depth here should give you some level of confidence in the amount of engineering effort that has gone into lambda, including the security, isolation and customer data segregation models.  That should also give you a basic idea of just how much complexity is needed for you to build and run your own internal platform that aims to compete with Lambda.


## [Amazon Acquires Encrypted Messaging App Wickr](https://www.vice.com/en/article/epnapp/amazon-acquires-encrypted-messaging-app-wickr)

[https://www.vice.com/en/article/epnapp/amazon-acquires-encrypted-messaging-app-wickr](https://www.vice.com/en/article/epnapp/amazon-acquires-encrypted-messaging-app-wickr)

> Amazon has acquired encrypted messaging platform Wickr, according to announcements from Wickr and Amazon on Friday.
> 
> The move signifies a major shift in the ownership of a popular encrypted messaging service. Wickr offers a free version that is used by journalists, criminals, and the general public; Wickr also sells various paid products including a platform geared specifically for military communications and another for enterprises.


This feels like a weird acquisition for AWS.  The AWS product line is simply enourmous, and covers everything from running functions as a service, using AI to identify security alerts, big data analytical platforms and sending emails as a service.

But what’s common about the products is that generally, AWS offers services that are picked up and consumed by the digital or technology operations bits of companies.  Nobody goes to AWS to buy their office productivity suite or shudder, their internal messaging


## [What if Military AI is a Washout? | Jack McDonald](https://jackmcdonald.org/book/2021/06/what-if-military-ai-sucks/)

[https://jackmcdonald.org/book/2021/06/what-if-military-ai-sucks/](https://jackmcdonald.org/book/2021/06/what-if-military-ai-sucks/)

> This, in a nutshell, is my underlying hunch about AI: It will force changes in organisational practices where adopted, and it is likely to be adopted due to competitive pressure (or perceived competitive pressure). Some people are okay with this, some people are definitely not okay with this. I am somewhat agnostic on the issue: if the starting point is a social process designed to kill people, then so long as humans are still at the top of the decision chain, there isn’t that much normative difference between an AI-reliant force and a computer-reliant force, just as there isn’t much normative difference between a mid-WW2 industrial war machine and their predecessors.
> 
> Hunch 2: Military AI will automate some bits of warfare, but probably not most of them.
> 
> In this view artificial intelligence is essentially automation. We take something that would require human cognition and action, instantiate it in a physical system, and then something that used to require a human being no longer requires a human being. “That is not AI” I hear you say, well, in response, consider how many automatic things were once autonomous things. Fire-and-forget missiles have gone from being discussed as autonomous systems to simply being an automatic function of a system. Automated Target Recognition systems are performing equivalent cognitive work (recognising objects from sense data) to human beings. It’s just that they can make sense of many different types of data, and do it faster than we can, enabling forms of action beyond human capabilities.
> 
> As I see it, object recognition is a key domain in which AI will eventually outperform us. At least for big recognisable pieces of kit. Therein lies the asymmetry - big pieces of recognisable military kit will be vulnerable to recognition by autonomous systems, whereas distinguishing human beings as being combatants or civilians is going to be hard, if not impossible to achieve.


A fascinating set of ruminations about the future of AI within the miliary, which is of course big money and popular at the moment.

I agree with most of this analysis, most of the actual impact of AI within the warfighting machines will be the automation and AI as an assistive force rather than autonomous killing machines roaming the streets.  We already have huge amounts of expert decision making run by computers at the pointy end, from Friend-or-Foe systems, to flight control systems, and it makes a lot of sense for computers to assist analysts and decision makers with their ability to analyse lots of data and highlight areas of incongruity to the operators


## [Adventures in Contacting the Russian FSB – Krebs on Security](https://krebsonsecurity.com/2021/06/adventures-in-contacting-the-russian-fsb/)

[https://krebsonsecurity.com/2021/06/adventures-in-contacting-the-russian-fsb/](https://krebsonsecurity.com/2021/06/adventures-in-contacting-the-russian-fsb/)

> Visit the FSB’s website and you might notice its web address starts with http:// instead of https://, meaning the site is not using an encryption certificate. In practical terms, any information shared between the visitor and the website is sent in plain text and will be visible to anyone who has access to that traffic.
> 
> This appears to be the case regardless of which Russian government site you visit. According to Russian search giant Yandex, the laws of the Russian Federation demand that encrypted connections be installed according to the Russian GOST cryptographic algorithm.
> 
> That means those who have a reason to send encrypted communications to a Russian government organization — including ordinary things like making a payment for a government license or fine, or filing legal documents — need to first install CryptoPro, a Windows-only application that loads the GOST encryption libraries on a user’s computer.
> 
> But if you want to talk directly to the FSB over an encrypted connection, you can just install their own client, which bundles the CryptoPro code. Visit the FSB’s site and select the option to “transfer meaningful information to operational units,” and you’ll see a prompt to install a “random number generation” application that is needed before a specific contact form on the FSB’s website will load properly.
> 
> Mind you, I’m not suggesting anyone go do that: Horohorin pointed out that this random number generator was flagged by 20 different antivirus and security products as malicious.


Absolutely fascinating insight into Russian thinking here.  There are international standards for suitable protection of data in transit, but the russian state clearly does not trust that western interests have not compromised them, and so have built their own cryptographic mechanisms.  Given the last few years of exposes, I'm not convinced that it's that paranoid a view to be honest.


