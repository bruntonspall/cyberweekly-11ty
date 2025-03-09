---
title: "206 - Too excited to write coherently"
date: 2022-08-07
description: "This newsletter is short for a couple of reasons. "
permalink: /too-excited-to-speak/
---

This newsletter is short for a couple of reasons. 

The main one is that I’ve been looking forward to heading to [Defcon](https://defcon.org/html/defcon-30/dc-30-index.html) and [Blackhat](https://www.blackhat.com/us-22/) this weekend for quite a while. It’s going to be my first time ever making it out to these conferences and they are such a mainstay of the infosec world that they’ve built up quite the reputation in my head!  

But looking forward to something is not quite the same as actually planning for it. So when time came to write this newsletter and the introduction I was instead in a panic of packing and prepping and ensuring my team had work to do while I’m away. 

Secondly, that means that I’m writing this from the lounge waiting to get onto the plane and my brain cannot focus on writing something witty or insightful (as I like to think I do the rest of the time)

I’m very excited to be travelling to the worlds premier security conference, to meeting people and to hopefully seeing some amazing security research.  If you are around, do reach out because, as you might have gathered from this intro, I do not have a well planned itinerary, I’m planning to take it the way anyone should their first time at these conferences, just as it comes. 

## [Uncomplicate security for developers with reference architectures ](https://anunay-bhatt.medium.com/embedding-security-into-sdlc-using-reference-architectures-for-developers-29403c00fb3d)

[https://anunay-bhatt.medium.com/embedding-security-into-sdlc-using-reference-architectures-for-developers-29403c00fb3d](https://anunay-bhatt.medium.com/embedding-security-into-sdlc-using-reference-architectures-for-developers-29403c00fb3d)

> **Phase #4 Make it easy for developers to use your reference architecture and track adoption** Use automation to convert your “How to” guides into one-click templates or create “Hello World” templates which are fully integrated with all the security controls proposed in your reference architecture. You can use any of the following to accomplish this starting with the least resource intensive:
> 
> * Use already existing scaffolding tooling in your company. Partner with the scaffolding team engineers and automate your security controls
> * Offer your controls as infrastructure-as-code scripts (IaaC)
> * Create your own scaffolding templates
> 
> Use metrics to track adoption. Some example metrics include — new teams adopting your scaffolded reference architecture templates, increase in documentation views for “How to” guides, increase in Git forks, etc. **_Quick tip →_** Do not recreate the wheel with automation or scaffolding. Use your existing organizational tooling where applicable. 


I’m not always a fan of reference architectures, for a number of reasons, mostly that organisations tend to try to come up with “the one and only reference architecture” rather than a series of them with common patterns.

But if you are going to use reference architectures, this is a good way of doing it, and ensuring that you use the tools and frameworks already in your organisation, but pre-secured is a great way of baking security into the whole structure. 


## [Granted Approvals - an Open Source Permission Management Framework - Common Fate Blog ](https://commonfate.io/blog/granted-approvals-release)

[https://commonfate.io/blog/granted-approvals-release](https://commonfate.io/blog/granted-approvals-release)

> Granted Approvals is a privileged access management framework that you can self-host in your own AWS environment right now, today. We’ve worked hard to make this a tool that streamlines your access pipeline, with a key focus on: **‍**  **Simplifying access:** set up rules defining who can request access to what, and the resource owners who can approve access. **Seamless integration with your services:** install Access Providers to provision fine-grain access to your SaaS services and cloud providers. Current support for AWS SSO, Okta groups, and Azure AD groups. **Fast and vocal approvals:** approve access with just a few clicks, and connect to your team’s communication tools like Slack. **Auditability:** see past and upcoming access requests. No more pulling all-nighters right before your ISO audits. 


This is a nice looking tool, focusing on making the request and grant for role accesses automated and fast where possible. 


## [An incident impacting some accounts and private information on Twitter ](https://privacy.twitter.com/en/blog/2022/an-issue-affecting-some-anonymous-accounts)

[https://privacy.twitter.com/en/blog/2022/an-issue-affecting-some-anonymous-accounts](https://privacy.twitter.com/en/blog/2022/an-issue-affecting-some-anonymous-accounts)

> In January 2022, we received a report through our [bug bounty program](https://help.twitter.com/en/rules-and-policies/reporting-security-vulnerabilities) of a vulnerability in Twitter's systems. As a result of the vulnerability, if someone submitted an email address or phone number to Twitter’s systems, Twitter's systems would tell the person what Twitter account the submitted email addresses or phone number was associated with, if any. This bug resulted from an update to our code in June 2021. When we learned about this, we immediately investigated and fixed it. At that time, we had no evidence to suggest someone had taken advantage of the vulnerability.
> 
> In July 2022, we learned through a press report that someone had potentially leveraged this and was offering to sell the information they had compiled. After reviewing a sample of the available data for sale, we confirmed that a bad actor had taken advantage of the issue before it was addressed. 


I’m not sure I would use the term zero-day for this, but it’s hard to put my finger on why.  I think it’s because it’s not in a supplier provided system or library, but in twitters code itself. 

It feels like the term zero-day should be used for a vulnerability being used before the vendor can tell you. 

Either way, this looks like a nasty breach of personal data. But also likely one that has been floating around for a while. 


## [BlenderBot 3: A 175B parameter, publicly available chatbot that improves its skills and safety over time ](https://ai.facebook.com/blog/blenderbot-3-a-175b-parameter-publicly-available-chatbot-that-improves-its-skills-and-safety-over-time/)

[https://ai.facebook.com/blog/blenderbot-3-a-175b-parameter-publicly-available-chatbot-that-improves-its-skills-and-safety-over-time/](https://ai.facebook.com/blog/blenderbot-3-a-175b-parameter-publicly-available-chatbot-that-improves-its-skills-and-safety-over-time/)

> So far, existing open research in conversational AI — including ours — has focused on human-model conversations with annotators in a controlled environment. But researchers can’t possibly predict or simulate every conversational scenario in research settings alone. The AI field is still far from truly intelligent AI systems that can understand, engage, and chat with us like other humans can. In order to build models that are more adaptable to real-world environments, chatbots need to learn from a diverse, wide-ranging perspective with people “in the wild.” These are currently open problems and require novel research to be conducted by the community. 
> 
> As a step in this direction, we’ve built and [deployed a live demo](https://l.facebook.com/l.php?u=https%3A%2F%2Fblenderbot.ai%2F&h=AT04BD6sc3L1Rhq09TF0bhbuhm5JQl6oBAfjknpNSLrwJQNX-Qq_5j43AkezdxVhqBWolEI1R0qT-LFepdgqa4Iy6_aNFKTIIEY462VpNtWND3uyusMLTrgqLFO_3rx0diP6I9ot8PeDDiLOYW3sR76qfYI) of BlenderBot 3, our state-of-the-art conversational agent that can converse naturally with humans, who can then provide feedback to the model on how to improve its responses. (Demo is only available in the U.S.) We will be sharing [data from these interactions](https://l.facebook.com/l.php?u=https%3A%2F%2Fparl.ai%2Fprojects%2Fbb3%2F%23interaction-data&h=AT2XVGvjeWJ6y-591sR8HO_4iulORUTog7YIfKqS_0ZdbF1GFd3x3xGY91GPX0328MvDgqPWXRbL4fvsNqpUXaETbJ5Y5Twk_7YyyCRe0G80V6p-1SAJ40Gc0XDUdYGv77E8ZqaQCf43154gMQW3HO_6iC8) , and we’ve shared the BlenderBot 3 [model](https://l.facebook.com/l.php?u=https%3A%2F%2Fparl.ai%2Fprojects%2Fbb3%2F%23models&h=AT3JKV-NOt7VYMvI-KmgJZvTFO3kwQ4EEITHRaDLRxLmBhVgKp6EBVevc1-3ylTVGSHDFcMW6ZDvtU7SC3KjmqqUBU10uPO2jWvVM8FTt4YHYsJ-pGF2jCa7O7q8PlPZWuaYa-EHyeZuY98edoYEqWDtrfY) and [model cards](https://l.facebook.com/l.php?u=https%3A%2F%2Fparl.ai%2Fprojects%2Fbb3%2F%23model-cards&h=AT3wzvSQ3BHqmOowBm8TvS_XEJkC5j-xkQLBMFv2Ct5jfwbPYeTusrRvTA3JYw3WdVLU_D2IHfrE5l0bYTdUzFkPg7nexA7G9ddrLqNuQ7GFLdFXoOPQ7DnaD0SFDtSaHNJ4sbhjZ_nk15IOI50oqzTYWpNP0bZnJHPQ-v9L) with the scientific community to help advance research in conversational AI. 


A couple of really big red flags in this announcement.  Many of us remember what happened when Microsoft [released their conversation bot on the internet… it turned into a racist in under 24 hours!](https://www.theverge.com/2016/3/24/11297050/tay-microsoft-chatbot-racist) But there’s two things in this announcement that would worry me.  Firstly they’re releasing the bot out to unguarded internet input and folding that back into that dataset.  And it’s clear that they’re doing that because they’ve decided that EU GDPR law wont allow them to provide that access to people outside of the US.  That’s not a good sign that they can justify how that data will be used and redistributed.

Secondly, the screenshot in this blogpost includes the snippet where the user asks what the bot has been doing, and it says that it has been busy overnight “writing a book”.  Are we morally and ethically okay with conversational bots that deliberately lie when asked questions?  For creating an artificial personality, that might be ok, but for almost all conversational interactions one has with a computer, you definitely do not expect nor want the computer to lie to you in response to questions. 


## [GitHub - matanolabs/matano: The open-source security lake platform for AWS ](https://github.com/matanolabs/matano)

[https://github.com/matanolabs/matano](https://github.com/matanolabs/matano)

> Matano is an open source security lake platform for AWS. It lets you ingest petabytes of security and log data from various sources, store and query them in a data lake, and create Python detections as code for realtime alerting. Matano is _fully serverless_ and designed specifically for AWS and focuses on enabling high scale, low cost, and zero-ops. Matano deploys fully into your AWS account. 


My first reaction to this was “What on earth is a ‘security lake’?”.  But looking into it, especially for organisations with complex organisational boundaries, the ability to ship events into a single coalesced data platform where they can be correlated and analysed is useful, and this looks like a neat tool to achieve that. 


## [911 Proxy Service Implodes After Disclosing Breach – Krebs on Security ](https://krebsonsecurity.com/2022/07/911-proxy-service-implodes-after-disclosing-breach/)

[https://krebsonsecurity.com/2022/07/911-proxy-service-implodes-after-disclosing-breach/](https://krebsonsecurity.com/2022/07/911-proxy-service-implodes-after-disclosing-breach/)

> 911[.]re, a proxy service that since 2015 has sold access to hundreds of thousands of **Microsoft Windows** computers daily, announced this week that it is shutting down in the wake of a data breach that destroyed key components of its business operations. The abrupt closure comes ten days after KrebsOnSecurity published an in-depth look at 911 and its connections to shady pay-per-install affiliate programs that secretly bundled 911’s proxy software with other titles, including “free” utilities and pirated software.
> 
> 911[.]re ~~is~~ was one of the original “residential proxy” networks, which allow someone to rent a residential IP address to use as a relay for his/her Internet communications, providing anonymity and the advantage of being perceived as a residential user surfing the web. 


Ooof, this is a shady business model and everyone knows it.  Bundling your software into free downloads has been done for decades, but using that to turn customers computers into outgoing proxies feels very underhanded.  I’m sure they can claim that users agreed the terms and conditions, but whether they understood the implications is another matter. 


## [Where Have All The Leaders Gone Redux: The Red Rise | Darrell Mann ](http://www.darrellmann.com/where-have-all-the-leaders-gone-redux-the-red-rise/)

[http://www.darrellmann.com/where-have-all-the-leaders-gone-redux-the-red-rise/](http://www.darrellmann.com/where-have-all-the-leaders-gone-redux-the-red-rise/)

> Like forty-plus years of ‘continuous improvement’ thinking, forty-plus years of MBA programmes teaching students how to use spreadsheets, draw Gantt charts, Manage By Objectives… I could go on. What the whole shebang ultimately leads to is c-suites crammed full of Red-World thinkers. People that know how to climb s-curves, but have no idea what to do when they hit the top. Or, in most cases, are aware that there is such a thing as a top.
> 
> Don’t get me wrong, having the skills to successfully navigate an organisation up the s-curve is important. It creates efficiency, economies of scale, and, for a while at least, impressive sounding EBITDA figures. On the down side, when taken too far, it makes the organisation extremely fragile. Such that when the outside world shifts – a pandemic arrives, for example – and the organisation finds itself thrown off their nice stable s-curve, Red World thinking is no longer going to help. What these organisations need is a healthy dose of Green World thinking. Something that Red World unfortunately fails to recognise. And so what tends to happen is a c-suite that doubles-down on the prevailing problems and becomes even more Red. Doubling down on getting people working harder, chopping costs and flogging the Sales team so they ‘try harder’. This is generally called a slippery-slope. And the thing with slippery slopes is they get slippier if we keep doing the wrong things to get off them. 


A reminder that we need different types of thinking to achieve different purposes. 

When I started looking into innovation programmes, one piece of advice was to look at about 90% of your innovation to be incremental, 9% to be evolutionary and 1% to be revolutionary. 

Adjusting those ratios too far in either direction can be bad for the organisation and bad for the people trying to achieve either business aims or innovation. 


## [HashiCorp State of Cloud Strategy Survey ](https://www.hashicorp.com/state-of-the-cloud)

[https://www.hashicorp.com/state-of-the-cloud](https://www.hashicorp.com/state-of-the-cloud)

> When it comes to the success of a cloud strategy, nothing is more important than security, which was cited as important or very important by almost 9 out of 10 respondents. Related regulatory and compliance issues were third on the list, named by more than 4 out of 5 respondents, behind delivering uptime and availability. And security was even more important to tech firms, where two-thirds (67%) rated it “very important” (vs. 59% for other industries). For comparison, in our [2021 Survey, security was named the second most important cloud inhibitor](https://www.hashicorp.com/state-of-the-cloud/2021#cost,-skills-shortages,-workflow-issues-among-top-cloud-challenges) (47%), trailing cost concerns (51%). 


Generally an abosultely fascinating survey, the second annual one now from Hashicorp.  This shows that cloud adoption continues to rise, but that organisations are struggling to do it.  Around 25% of orgs who don’t have a central cloud platform team don’t do so because their use of the cloud is not coordinated or large enough.

But lots of them see security as a critical concern.  Hashicorp generously assume that menas that people think that security is a critical driver of success, rather than a department to convince of the value of the cloud.  But it is important to organisations that they adopt cloud securely and effectively.  The creation of those cloud platform teams is a great opportunity for CISO’s to get involved and bake security in from the start. 


## [How to Run a Zoom All Hands ](https://chase-seibert.github.io/blog/2022/07/22/how-to-run-a-zoom-all-hands.html)

[https://chase-seibert.github.io/blog/2022/07/22/how-to-run-a-zoom-all-hands.html](https://chase-seibert.github.io/blog/2022/07/22/how-to-run-a-zoom-all-hands.html)

> All Hands are a key tool for communicating big points, giving the audience the best chance to hear and internalize those ideas, and creating transparency. The ideal All Hands also generates enthusiasm, though this is easier said than done with Zoom. If you’re a leader of an organization, you should plan on doing an All Hands roughly once a quarter. 


You can kind of ignore the Zoom part of this.  What the author means is “How to run an All Hands that is entirely on video conference.
This includes a number of useful nuggets, that jump up and down from the technical details on running an all hands and the structure of an all hands.

Two things jump out at me, one technical and one management.

Don’t try to reconnect laptops, move things around in a conference room.  Just make everyone join from their laptop direct.  This is true of almost all VTC etiquette, moving devices around and plugging stuff in and out wastes everyones time.

Go back over the mission statement and vision at every single all hands.  You need to constantly remind people what the mission is and make them feel part of it. 


## [GPSJam GPS/GNSS Interference Map ](https://gpsjam.org/)

[https://gpsjam.org/](https://gpsjam.org/)

> 


This is a lovely bit of hackery. Airplane ADB transmitters for things like flight radar also transmit how much their GPS is out by. Someone has started to map that so we can see what locations on the world have got “some GPS interference”.

Of course, said interferences could be for all kinds of reasons, not just state interference, but it’s another really interesting use of openly available data and one that actors doing this probably didn’t expect 


