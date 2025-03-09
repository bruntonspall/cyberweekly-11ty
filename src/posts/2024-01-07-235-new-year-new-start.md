---
title: "235 - New year, new start"
date: 2024-01-07
description: "Welcome to the first newsletter of 2025, and apparently the 235th newsletter that I've written!"
permalink: /new-year-new-start/
---

Welcome to the first newsletter of 2025, and apparently the 235th newsletter that I've written!

I've talked before about the way that I write this newsletter.  I write this more for me than for the readers, as it's a great forcing mechanism to ensure that I'm taking time in my week to read a variety of information, but more critically, to actually sift that and come up with some analysis and views of that information.  When I fail to produce a newsletter in a given week it's often more the lack of the time to consider what I've read than a lack of ability to actually read.

The second thing that it gives me is a great history of how my thinking has progressed over time.  I always tell my teams that I have "strong opinions, weakly held".  I'm always willing and even eager to be told that I'm wrong, because I recognise that I rarely have all the information at the point at which someone asks my opinion.  A better person might be more reserved about their opinions, but that's not my natural instinct.  Instead I tend lean into being willing to accept that I'm wrong, and to change my opinions on things.  (That, incidentally, is one of the other reasons that I don't write this in any official capacity.  This is all pure opinion and conjecture).

The article about lab notes really reminded me of the value of keeping a track of how my views have changed over time.  Going back over 5 years of weekly notes from me can show my thinking on how identity and access controls systems have changed, can show the importance I place on MFA, and how I've changed opinions in that time.

We often present our ideas as if they are fully formed and objectively right in all senses, but in reality, our ideas are always the product of research, discussion, thought (careful or not) and are the end result at a given point in time.  Once presented, we may continue to think, to review new data, and discuss with people, and our view might change, but we often don't track or present the reasoning that went into our ideas, so it's hard to see when and how we change our opinions.  

Like software, that can age badly, as we go back to opinions, policies, or documents that we wrote years ago we find that we may no longer agree with what we wrote.  But without that backing or comment about why we thought it was relevant or interesting, we cannot easily re-evaluate our ideas to determine if we still hold that opinion, or should change our mind.

I'm planning on taking more time this year to experiment, to learn, and to dust off some skills I don't use often enough, and I'll be planning on blogging my way through that (over on my blog not here) in order to make sure I keep a lab notebook, and track my learning journey.

## [Lab Notebooks | Sam Bleckley ](https://sambleckley.com/writing/lab-notebooks.html)

[https://sambleckley.com/writing/lab-notebooks.html](https://sambleckley.com/writing/lab-notebooks.html)

> I said there was a lot of discipline associated with a lab notebook. This is in part for forensics. If plagiarism/data falsification/ethics/ etc concerns arise over some scientist’s research, the lab notebook can be valuable exonerating evidence — but only if the discipline is kept.
> 
> Software engineering doesn’t have quite the same forensic constraints, but the same disciplines have nevertheless been valuable for me. 
> 
> Here are some of the major points:
> 
> * Always in pen. 
> 
> Your goal is not to preserve the outcome of your thoughts — that’s your code. Your goal is to preserve the process of your thoughts. So no erasing, no blacking out. You can put a single line through anything spelled or written incorrectly. 
> 
> * Always during 
> 
> Write down what the problem is, what you’re about to do, and what you expect the result to be. Treat your work as an experiment! This is especially valuable for junior developers who are still in a “try everything until something works” frame of mind. Forcing yourself to hypothesize what’s actually wrong is really valuable; and there’s nothing wrong with expecting a negative result (“I don’t think the problem is X, but it’s easy to prove it, so…”) If during the actual process, you deviate from your written plan, write down the deviation, and why you’re doing so. Don’t wait until after you’re “done” — because “done” might mean six hours from now. 
> 
> * Always forward. 
> 
> If you write something on Monday and realize you were wrong on Tuesday, write the correction in Tuesday’s entry. This is a lab journal — from the French “daily”. If you had a misconception, you want a record of that, as well as a record of why you were wrong. You can (and should) add a small note to the original entry pointing to the page where you correct yourself — but don’t obscure what you originally wrote. 


I really like this idea of tracking your learning.  As Sam sets out at the start, looking back on some of my projects one could almost get the idea that they sprang fully formed, rather than representing a journey.

This is also true of our policies, our guidance and our organiusational decisions.  I really like [ADR’s](https://adr.github.io/) for documenting the why of an architectural decision, but we rarely use something similar for policy decisions.  Why did you decide to mandate 2FA but decide SMS 2FA was sufficient?  There was probably a good reason, but if in a years time someone reviewing the policy cannot understand the decision making process, then it’s hard to know what decisions were compromises which no longer hold true. 


## [John the Toolmaker ](https://two-wrongs.com/john-the-toolmaker)

[https://two-wrongs.com/john-the-toolmaker](https://two-wrongs.com/john-the-toolmaker)

> _If I had six hours to chop down a tree, I would spend the first four sharpening the axe._ 
> 
> Good tools are the things that allow others to experiment more freely, with less friction. They are a good investment because they can last for a long time – far outlive the initial process they were developed for. 


I think this is really powerful. I've spoken before about the power of tools, because no matter what you write down about process and policy, very few people will read them. But our tools encode our policy, our culture and our values in them. So if you control the tools, you control the culture of the organisation 


## [Cold-blooded software ](https://dubroy.com/blog/cold-blooded-software/)

[https://dubroy.com/blog/cold-blooded-software/](https://dubroy.com/blog/cold-blooded-software/)

> I see a similar dichotomy with software projects. Certain technology decisions lead to projects that are warm-blooded: everything is great when there’s constant motion on the project, generating heat. But put warm-blooded software in the freezer, and you’ll pull out a corpse six months later.
> 
> Maybe your CI isn’t working because one of the services you depend on got bought or ran out of money. You add a new dependency and find yourself needing to upgrade your compiler. Another package you depend on is deprecated, and doesn’t work with the latest version of the compiler.
> 
> Some projects are different. You work alone, make some changes when you’re inspired, and then don’t touch it again for another year, or two, or three. You can’t run something like that as a warm-blooded project. There’s not enough activity to keep the temperature up.
> 
> A cold-blooded project is like the baby painted turtle. You can freeze it for a year and then pick it back up right where you left off.
> 
> A cold-blooded project uses [boring technology](https://mcfunley.com/choose-boring-technology) . The build and test scripts don’t depend on external services that might change, break, or disappear entirely. It uses [vendored dependencies](https://go.dev/ref/mod#vendoring) . 


As the author points out, this harkens back to McFunley’s “Choose Boring Technology” post.  Software that is designed to withstand the continual creep of time needs to be based on stable technologies that wont break over that time period.

SImplicity is hard to do during development, but pays dividends.  As the GDS mantra went: “Do the hard work to make things simple” 


## [Manage Your Capacity, Not Your Time - The Engineering Manager ](https://www.theengineeringmanager.com/management-101/manage-your-capacity-not-your-time/)

[https://www.theengineeringmanager.com/management-101/manage-your-capacity-not-your-time/](https://www.theengineeringmanager.com/management-101/manage-your-capacity-not-your-time/)

> The internet is full of opinions about how to manage your time. There are even whole books written on it. However, they miss an important nuance: it’s not the _quantity_ of time that you are able to juggle, assign and manage that matters, it’s the _quality_ of the time that you are able to spend on your tasks.
> 
> Regardless of where you work or how senior you are, you have a finite amount of capacity: there are only so many hours every day in which you are working effectively, and only so many of those hours that you can spend in a state of productivity and flow.
> Everyone typically has the same amount of hours that they dedicate to their work. However, everybody is different in finding how and when they work best. Some people are better finding flow in the morning, whilst others are better in the afternoon. Some people thrive on long blocks of time spent on a single task, whereas others prefer to work in shorter bursts, switching to new tasks often to avoid repetitiveness. 


I don't know how many of you need to hear this, but it's a useful reminder to me today.

Manage your capacity to get work done, rather than just the hours in your day.  Having a diary that looks like a bad game of tetris is unlikely to result in you being able to be your best self at work.

If you haven't made a new years resolution yet, this is a good one to think about, as it unlocks almost everything else that you do at work


## [Introducing Journaling Suggestions for Day One ](https://dayoneapp.com/blog/introducing-journaling-suggestions/)

[https://dayoneapp.com/blog/introducing-journaling-suggestions/](https://dayoneapp.com/blog/introducing-journaling-suggestions/)

> We know you may have concerns about the privacy and security of Journaling Suggestions.
> 
> All Journaling Suggestions are specific to your personal iPhone. Your Journaling Suggestions are _always_ private and all entries created from your Journaling Suggestions are [end-to-end encrypted](https://dayoneapp.com/features/end-to-end-encryption/) by default. **No one except for yourself can ever view or create journal entries from your data.** Apple ensures that Journaling Suggestions are managed with your privacy in mind. Day One and other third-party apps do not have access to your Journaling Suggestions data until you select a specific suggestion and choose to share it outside of Day One. 


This use of “AI” on your end device is going to become a more normal mode for AI companies.  Users are wary of giving away all their data, so precomputing AI models and shipping them to the users device will allow some on device tweaking.  Device manufacturers like Apple are going to support this as much as possible as well.  Users want the custom experience on their device, they just don’t want to give up _all_ their data to get it 


## [The 3 budgets | Swizec Teller ](https://swizec.com/blog/the-3-budgets/)

[https://swizec.com/blog/the-3-budgets/](https://swizec.com/blog/the-3-budgets/)

> Software engineering salaries come from one of 3 budgets. Which budget pays your salary shapes your day-to-day and influences your career trajectory.
> 
> I think this is like a business law of physics. Nobody needs to make a conscious choice for the pattern to emerge.
> 
> The 3 budgets are:
> 
> * sales/marketing
> * research and development
> * maintenance
> 
> This framing can be useful when thinking about [your career vision](https://swizec.com/blog/your-career-needs-a-vision/) and [positioning statement](https://swizec.com/blog/how-one-sentence-guides-your-career/) . I thought of it while reflecting on why some opportunities make my subconscious scream even if they sound good on paper. 


This can be aligned to more than just budgets.  In my view, this is about which bit of your organisations strategy are you aligned with.  You might be there to help the products or services grow, working directly on the consumer facing portions of products.  You might be part of the backend technology strategy, ensuring that the first group of people can get their job done, and stabilizing the structures.  Finally you can be responsible for the long term health of the organisation, ensuring that everything keeps ticking over.

Obviously, there’s a lot of fame, interest and excitement in the first, but organisations overlook the other two at their own risk.  Organisations that over-invest in the first tend to burn out fast, as consumers know when the product doesn’t meet the core needs.  And of course, there are increasing development and maintenance costs that come up as your product or service goes up through growth phases. 


## [Most 16-year-olds don’t have servers in their rooms ](https://varun.ch/server)

[https://varun.ch/server](https://varun.ch/server)

> I wanted more control and reliability so I jumped head-first into the wonderful world of self-hosting.
> 
> My original rationale for choosing to host at home rather than cheap cloud options was purely out of a desire to learn (at my scale, it’s probably more cost effective to pay for The Cloud). I wanted to learn the whole stack, from user-facing frontends, to the backends and databases that support them, to the servers that actually host them. All I needed was a computer (that wasn’t my desktop) online 24/7.


I love this.  I have a homelab at home (more on this in 2024), and I have it for the same reason, the ability to learn, to experiment and to make real some of the things that I talk about on a regular basis.

You can get started simply and easily and it'll keep growing if you care for and feed it.  Something I recommend to everyone


## [A (beta) Canarytoken for Active Directory Credentials – Thinkst Thoughts ](https://blog.thinkst.com/2023/12/a-beta-canarytoken-for-active-directory-credentials.html)

[https://blog.thinkst.com/2023/12/a-beta-canarytoken-for-active-directory-credentials.html](https://blog.thinkst.com/2023/12/a-beta-canarytoken-for-active-directory-credentials.html)

> Attackers on your network love finding stray credentials. They are an easy way to elevate privileges and are often one of the first things attackers look for during post-exploitation.
> 
> There’s no shortage of places where these credentials can be found and surprisingly, there’s very little downside to attackers trying them…
> 
> …unless there’s a way to drop decoy credentials. This isn’t a new idea, but it usually requires heavy tooling and configuration.
> 
> Our newest AD tokens allow you to create fake credentials that can be left in all the familiar places, but without a heavy software component. A single, light-weight script that runs on your Domain Controller lets you know when the fake credentials are used.
> 
> […]
> 
> 
> This is an unusual token for us, because it runs a script on your Domain Controller. We’ve kept the script simple and legible so that you can make sure it’s not doing anything nefarious (and so that the script logic can be easily extended). Our work on this token is inspired by IppSec, who showed an initial concept for an AD token that you can catch in his YouTube video [here](https://youtu.be/BT9pT1tAmX8?si=qoc4lDGRocC3-4ej) . 


I’m a huge fan of Canary Tokens in general, and deception technologies writ large.  This is a marvelous use for such things, although I’ll admit at first that I was nervous about the use of the tokens requiring you to write PowerShell to run on your AD server, but Thinkst have gone above and beyond to make it clear and simple so you can trust what you’ve written. 


## [Microsoft Incident Response lessons on preventing cloud identity compromise | Microsoft Security Blog ](https://www.microsoft.com/en-us/security/blog/2023/12/05/microsoft-incident-response-lessons-on-preventing-cloud-identity-compromise/)

[https://www.microsoft.com/en-us/security/blog/2023/12/05/microsoft-incident-response-lessons-on-preventing-cloud-identity-compromise/](https://www.microsoft.com/en-us/security/blog/2023/12/05/microsoft-incident-response-lessons-on-preventing-cloud-identity-compromise/)

> In the hybrid identity world, most users and groups are synced from on-premises Active Directory to Microsoft Entra ID. This is required to allow users to access cloud resources via the same set of credentials used on premises. However, in engagements seen by Microsoft IR, accounts used to manage Microsoft Entra ID, such as Global Administrators, have also been synced to Microsoft Entra ID from on-premises. Staff then often use the same credentials to manage both environments.|
> 
> If Active Directory is compromised and the credentials for these accounts are found by a threat actor, this allows them to easily pivot into Microsoft Entra ID, expanding the scope of the compromise. Synced service accounts are particularly vulnerable to exploitation. Microsoft IR commonly sees service accounts used to manage both on-premises Active Directory and Microsoft Entra ID targeted by threat actors. These accounts generally hold a high level of privilege in Microsoft Entra ID (often Global Administrator) but aren’t subject to the same controls such as MFA or Microsoft Entra Privileged Identity Management (PIM).
> 
> Microsoft IR has been involved in numerous investigations where on-premises Active Directory compromise led to Microsoft Entra tenant compromise. Threat actors sometimes uncover account credentials in clear text due to poor handling of credentials in an on-premises environment. If the threat actor already has a foothold in the on-premises environment, controls such as MFA are often not enforced as these networks are seen as ‘trusted’. 


Lots of good advice in here, mostly all along the lines of “Your identity system is too complex, and you should probably simplify it”.

When you have different systems from different providers integrating together, you almost always end up with security holes because of the way that the different security models don’t quite match up, and the level of trust that has to exist between the systems.

This is true regardless of whether you are integrating SaaS applications into your organisations information management system, connecting test runners to your CI system or as in this article, connecting together different identity providers.

One of the things to model at the enterprise level is using the STRIDE framework, and ask yourself what impact Spoofing, Tampering and Repudiation can have on your integrations. If someone can compromise one of the services and craft their own tokens, can modify tokens being passed around, or can use a token that should have expired, then what can they do in your system?

That’s a complex question, and in many cases, nobody even knows what the integrations are, let along has threat modelled them, but without an understanding of this complex system, your defences are likely focused in the right place 


## [Security Adoption Resources - Security documentation | Microsoft Learn ](https://learn.microsoft.com/en-us/security/ciso-workshop/adoption)

[https://learn.microsoft.com/en-us/security/ciso-workshop/adoption](https://learn.microsoft.com/en-us/security/ciso-workshop/adoption)

> Navigating the continuously changing threat landscape, technology platforms, and business requirements is often challenging for many organizations.
> 
> The Security Adoption Framework (SAF) provides guidance for organizations through end-to-end security modernization across a 'hybrid of everything' multicloud and multi-platform technical estate.
> 
> Each element of this guidance can be used individually or as part of holistic end-to-end security modernization from a strategic and programmatic level through architectural and technical planning.
> 
> This guidance applies Zero Trust principles to all aspects of end-to-end security modernization. 


This is rather peculiarly “slideware”, in that quite a lot of the actual products here are powerpoint presentations that you can use to run workshops or meetings with your CISO community to ensure you have a pathway to adopting security.

As someone who grew up through the engineering ranks, this sort of thing sometimes rankles a bit, but the last decade or so in management has made me realise just how powerful this kind of thing can be.  Bringing your management and your non-technical staff together to recognise what the work that needs to be done is can help unblock and focus the capability and work of the engineering community 


