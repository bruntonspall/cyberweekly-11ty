---
title: "221 - Can you define a good security culture?"
date: 2023-02-05
description: "It's really easy to hand wave and say that we need a better security culture, but it's really hard when you start to drill down on what that actually means."
permalink: /can-you-define-a-good-security-culture/
---

It's really easy to hand wave and say that we need a better security culture, but it's really hard when you start to drill down on what that actually means.

Many people, when they say they want a good security culture either mean sticking up posters reminding people to watch out for hackers in hoodies, or they might mean running "security awareness" workshops for all staff.

But security culture is so much more than just whether Brian in Marketing clicks one of the links in the one bad email he got that day (out of the links in the 200 good emails he had to deal with).  Security culture can be thought about in at least three different ways.

Firstly, there is some responsibility for employees to consider the security of their actions and to make prudent choices.  They should know that it's inappropriate to carry out illegal actions such as downloading pirated software on their work computers, they should know that they don't comment to the press on incidents going on (unless they're the press team I guess), and they should know that they don't just badge anyone into the building regardless of who they are.  The deal with this, certain levels of security awareness training can be effective.  But so to is setting out the expectations that people are going to be held to.  This requires that your security policies be readable and understandable by normal people; that you make an effort to ensure people understand what is their responsibility; and critically making an effort to be sure they know what is not their responsibility.

Secondly, there is the culture within the security department itself.  Do you blame users for their mistakes?  Do you run regular phishing tests on your own employees, trying to catch them out?  Is your security team approachable, friendly and enabling of others?  You can switch up how your security team engages in the wider business engagement.  You can invest in cake and goodies, and make stopping by security a pleasant experience.  You can make sure that people want to come to you to ask questions on how to do something rather than once it's gone wrong.  You can invest in tools like Yubikeys, password managers and other technologies that make peoples life easier.

But thirdly, you can look at the culture of the organisational bureaucracy itself.  How involved are you in defining the processes for buying new services? in checking through the HR induction packs? in defining when and how people get upgraded, new and more secure end user devices like laptops and phones?  If you focus on making the entire organisation more secure-by-default, then you can measure the impact of security on the culture by looking at compliance with the organisations policies and processes.  Instead of security being a burdensome addon to peoples everyday experience, you can ensure that the default way of working is as secure as possible.

Of course, that's just my definition of security culture.  This is something that is reasonably subjective, and different people have very different opinions on just what defines culture.  What is pretty clear is that if you don't bother defining what you mean, then you can't measure it, and if you can't measure it then you'll have no idea whether any of your culture initiatives are having any impact.

## [Security Principles: Addressing underlying causes of risk in complex systems | Federal Trade Commission ](https://www.ftc.gov/policy/advocacy-research/tech-at-ftc/2023/02/security-principles-addressing-underlying-causes-risk-complex-systems)

[https://www.ftc.gov/policy/advocacy-research/tech-at-ftc/2023/02/security-principles-addressing-underlying-causes-risk-complex-systems](https://www.ftc.gov/policy/advocacy-research/tech-at-ftc/2023/02/security-principles-addressing-underlying-causes-risk-complex-systems)

> One of the most important figures in the last decade among practitioners of computer system resiliency was an anesthesiologist. Dr. Richard Cook, a leading scholar of complex systems [[1]](https://www.ftc.gov/policy/advocacy-research/tech-at-ftc/2023/02/security-principles-addressing-underlying-causes-risk-complex-systems#_ftn1) , posed questions like what do the power grid, the emergency room, air traffic control, and a server farm have in common? And, what can we learn about the people who operate these systems, and the things they do to make them work reliably? 
> 
> One of those lessons is that systems must be designed to be operated by real humans. It's remarkably common for organizations to look at an incident and declare the root cause to be "human error." Cook and his colleagues argue that human error is, in fact, only the beginning of the investigation: did the system make it easy for the human to make a mistake? Was the human warned about the risks of what they were doing? Did those warnings have such a high frequency that they fatigued humans into numbness to the messaging?
> 
> Secure systems take these things into account. They don't end their inquiry with blaming individuals—rather they focus on the system, which has always been a goal of the FTC’s data security orders. The FTC strives to craft remedies that effectuate the principles Cook and his colleagues identified about how to safely operate complex systems.
> There are organizations that have adopted these lessons from complex systems and safety engineering, and they are the ones that are doing a better job living up to their responsibilities to protect users' data. But frustratingly, many organizations haven't yet recognized the value of these approaches. 


Absolutely great point here.  Human error is not a root cause of an issue, but is itself a reaction or response to a complex system.

It’s great that some of the technical interventions that the FTC has pushed onto regulated industries are things like MFA or zero-trust.  But it might be better to mandate building for understanding,  ensuring there is a blameless postmortem culture in place, and regular routine testing / incident exercising.   

We know that these actions help ensure that knowledge is shared, that understanding of how systems go wrong is developed, and muscles for how to respond are effectively exercised and grown.

Of course, mandating a culture is significantly harder than mandating technology.  It’s harder to get agreement on, harder to measure, and harder to even define. 


## [Dr Jessica Barker on cybersecurity culture metrics ](https://twitter.com/drjessicabarker/status/1621465359202107394)

[https://twitter.com/drjessicabarker/status/1621465359202107394](https://twitter.com/drjessicabarker/status/1621465359202107394)

> There are two types of cyber security culture metrics - but many organisations only focus on one of them 
> 
> 
> Here's a thread explaining what I mean.
> 
> There are individual metrics (what people are doing) and organisational indicators (the bigger picture of what the org is doing).
> 
> […]
> 
> Whereas some organisational indicators are:
> 
> 
>  Scale of password manager roll-out
> 
>  Time taken to respond to incident reports
> 
>  Percentage of incident report feedback
> 
>  Frequency of awareness-raising comms 
> 
>  Reported perceptions of executive buy-in 


Really interesting thread, reminding us that metrics that depend on focusing on what individuals do are not the best metrics to determine your security culture.  Focusing on how well the entire organisation is doing will give you better results. 


## [A small mistake does not a complex systems failure make – Surfing Complexity ](https://surfingcomplexity.blog/2023/01/15/a-small-mistake-does-not-a-complex-systems-failure-make/)

[https://surfingcomplexity.blog/2023/01/15/a-small-mistake-does-not-a-complex-systems-failure-make/](https://surfingcomplexity.blog/2023/01/15/a-small-mistake-does-not-a-complex-systems-failure-make/)

> _The source of the problem was reportedly a single engineer who made a small mistake with a file transfer._ 
> 
> Here’s what I’d like you to ponder, dear reader. Think about all of the small mistakes that happen every single day, at every workplace, on the face of the planet. If a small mistake was sufficient to take down a complex system, then **_our systems would be crashing all of the time._** And, yet, that clearly isn’t the case. For example, before this event, when was the last time the FAA suffered a catastrophic outage?
> 
> Now, it might be the case that no FAA employees have ever made a small mistake until now. Or, more likely, the FAA system works in such a way that small mistakes are not typically sufficient for taking down the entire system.
> 
> To understand this failure mode, you need to understand how it is that the FAA system is able to stay up and running on a day-to-day basis, despite the system being populated by fallible human beings who are capable of making small mistakes. You need to understand **_how the system actually works_** in order to make sense of how a large-scale failure can happen.
> 
> Now, I’ve never worked in the aviation industry, and consequently I don’t have domain knowledge about the FAA system. But I can tell you one thing: **_a small mistake with a file transfer_** is a hopelessly incomplete explanation for how the FAA system actually failed. 


Repeat after me, human error isn’t a root cause, it’s just a symptom of a wider problem.  Why was this change not safe to make?  Why wasn’t it obvious what had changed?   These are the questions that don’t seek to place the blame on whoever did the change, but look to understand what makes change risky. 


## [The Untold Story of a Crippling Ransomware Attack | WIRED ](https://www.wired.com/story/ransomware-attack-recovery-hackney/)

[https://www.wired.com/story/ransomware-attack-recovery-hackney/](https://www.wired.com/story/ransomware-attack-recovery-hackney/)

> In addition to the impact on Hackney’s residents, the cyberattack has naturally affected the staff at the organization. Hundreds of staff at Hackney Council have had to work through the disruption, trying to help people despite little or no access to databases and case files. “When there’s an incident like this, it can cause a lot of stress and anxiety and upset for the people who are involved,” says Jessica Barker, the co-CEO of cybersecurity company Cygenta, who has followed the Hackney attack. Barker adds that for people involved in the technical recovery, there can be stress and burnout, and for those involved in helping citizens, it may have added extra time to their jobs.
> 
> Hackney’s Children and Families Service—which initially lost its social care management and document management systems—acknowledged the toll the attack had on staff in an annual report. It said “morale in some parts of the service may be lower” because of the pandemic and the ransomware attack. It also said the “legacy of the cyberattack in October 2020 cannot be understated.”
> 
> Miller says he is “proud” of the way staff at Hackney have responded but admits it has been hard on those working there. “People come into public service because we want to do things right, you give residents and citizens the services they need, we want to make life better for them,” he says. “To be in a position where people have had to put huge amounts of effort in, and they’ve known that they’re delivering less than they would normally expect to deliver—I think that’s been really tough for people. They care about what it means for our residents.” 


This is a good read into the impact of one of the most public ransomware attacks in the UK.  Knowing people who were directly affected, as residents, as well as people who worked there, I think that one of things that people rarely talk about with cyber incidents is the effect on the staff.

Firstly, it’s worth remembering that staff systems are often impacted, so your staff may worry that their own data, payroll data, medical history or employment notes might have been exposed.

Secondly, staff have to work with systems that are barely working.  Had a project you were working on for the last few months, it’s probably getting dropped.  Even just doing your job is suddenly, and you are also going to get pressure to help remediate the issue on top of their existing job.

Finally, your staff still want to serve customers who are in a heightened state of anxiety.  They want their services delivered as normal, and they might be worried about impact on themselves.  This is particularly intense for people working in the public sector, when you are already dealing with people who mostly don’t want to talk to you, but need something fixing in their lives.  But even in the private sector, your customers will have worries about knock on impacts on themselves.

Ransomware or cyber incident response isn’t just about bringing up firewalls, restoring from backups and doing “the cyberz”.  It’s about operating the business and taking care of your staff as well. 


## [How Adversaries Can Persist with AWS User Federation ](https://www.crowdstrike.com/blog/how-adversaries-persist-with-aws-user-federation/)

[https://www.crowdstrike.com/blog/how-adversaries-persist-with-aws-user-federation/](https://www.crowdstrike.com/blog/how-adversaries-persist-with-aws-user-federation/)

> In recent incident response [investigations](https://www.crowdstrike.com/blog/analysis-of-intrusion-campaign-targeting-telecom-and-bpo-companies/) , CrowdStrike Services has observed adversaries use the `sts:GetFederationToken` API call to create federated sessions from IAM users. In this scenario, the federated session inherits permissions from the base IAM user. Perhaps surprising to many incident responders, the privileges and access of the federated session are not revoked when the base IAM user’s credentials are deactivated. 
> 
> Many defenders may not realize it, but this is a characteristic of all forms of temporary credentials obtained via the various API calls to AWS STS. The resulting sessions are independent of the long-term credentials of the underlying IAM or root user. The privileges of the federated session are only reduced or revoked when the IAM policies attached to the base IAM user are modified [to reduce or revoke those permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_disable-perms.html) . (Deleting the IAM user will effectively revoke all privileges but CrowdStrike does not recommend doing so, as detailed below.). The federated session remains active until the session token expires.1 
> 
> It is common for incident responders to only deactivate the base IAM user’s credentials. However, this will not be sufficient to contain an attack utilizing this technique. CrowdStrike is posting this blog to raise awareness of the use of this technique by threat actors and how threat actors can expand its use to establish persistence and escalate privileges within AWS environments if the underlying IAM user already had those escalation privileges. 


This is an interesting finding that is probably a useful pattern for incident responders to be aware of.  

As pointed out last week, many user credentials can be exchanged for tickets or authentication tokens.  But it’s worth checking the documentation carefully for just what gets revoked if you revoke the original account credentials.  Many of those sub-tokens will have their own lifetimes, and if you are managing a known compromise, especially of an admin account, this might give them subtokens that can be used to recompromise the system.

Most ticket/token systems are time limited, but in many cases they might be a number of hours and some may well be long lived, so several days or more. 


## [The Defender's Guide to OneNote MalDocs - Opalsec ](https://opalsec.substack.com/p/the-defenders-guide-to-onenote-maldocs)

[https://opalsec.substack.com/p/the-defenders-guide-to-onenote-maldocs](https://opalsec.substack.com/p/the-defenders-guide-to-onenote-maldocs)

> Similar to traditional Excel and Word document lures, OneNote lures have largely masqueraded as an invoice, remittance advice or other document that the target is urged to view.
> 
> Upon opening the document, **instead of asking a user to click “Enable Content”** , the lure prompts them to double-click a fake “Open” button 


As more and more companies adopt Microsoft’s O365 product, more people will use OneNote as a tool.  Sharing a OneNote document with someone else isn’t as common as emailing say a word document or excel sheet, but as pointed out in the article, there are more built in defenses than you find in OneNote.  

Towards the bottom there’s some indicators, such as Yara rules for detecting OneNote files being emailed in or opened, as well as some Signma rules for detecting the weird sorts of follow on actions that you might get from an infected document 


## [Iran responsible for Charlie Hebdo attacks - Microsoft On the Issues ](https://blogs.microsoft.com/on-the-issues/2023/02/03/dtac-charlie-hebdo-hack-iran-neptunium/)

[https://blogs.microsoft.com/on-the-issues/2023/02/03/dtac-charlie-hebdo-hack-iran-neptunium/](https://blogs.microsoft.com/on-the-issues/2023/02/03/dtac-charlie-hebdo-hack-iran-neptunium/)

> Today, Microsoft’s Digital Threat Analysis Center (DTAC) is attributing a recent influence operation targeting the satirical French magazine Charlie Hebdo to an Iranian nation-state actor. Microsoft calls this actor NEPTUNIUM, which has also been identified by the U.S. Department of Justice as [Emennet Pasargad](https://www.ic3.gov/Media/News/2022/220126.pdf) .
> 
> In early January, a previously unheard-of online group calling itself “Holy Souls,” which we can now identify as NEPTUNIUM, [claimed](https://web.archive.org/web/20230109230118/https:/breached.vc/Thread-Personal-information-of-230000-customers-of-charliehebdo-fr) that it had obtained the personal information of more than 200,000 Charlie Hebdo customers after “gain[ing] access to a database.” As proof, Holy Souls [released a sample of the data](https://web.archive.org/web/20230109230316/https:/www.youtube.com/watch?v=GKRnCjbMqEM) , which included a spreadsheet detailing the full names, telephone numbers, and home and email addresses of accounts that had subscribed to, or purchased merchandise from, the publication. This information, obtained by the Iranian actor, could put the magazine’s subscribers at risk of online or physical targeting by extremist organizations. 


When we talk about “Influence Operations”, people think of hack and leak meaning that information is suddenly available for the media sector to make hay from.  Things like leaking classified documents to wikileaks, email archives and so on.

But we don’t often think about the real world impact of such operations.  In this case it’s really easy to read Microsoft’s report and understand how this can create a threat to life as well as a threat to public order.

It’s a sobering reminder of the potential consequences of a data breach.  The personal data that we are entrusted with is something we need to keep carefully. 


## [Security Writer: "We have one client which we ma…" - Infosec Exchange ](https://infosec.exchange/@SecurityWriter/109777576538835360)

[https://infosec.exchange/@SecurityWriter/109777576538835360](https://infosec.exchange/@SecurityWriter/109777576538835360)

> We have one client which we manage an Azure tenant for. They require, and have specified, a zero-tolerance for device non-compliance.
> 
> In roughly two hours, 1647 devices are about to be locked out of access to organisation resources, wiped, and removed from Intune permanently.
> 4 meetings, 124 emails, and two phone calls a day for the last 14 days have warned them of this.
> 
> We’ve been _very_ clear about what is about to happen for the last 13 months. Their internal management have _acknowledged_ what is about to happen. But still, time marches on.
> 
> Death by middle-management. 


Fabulous Mastodon toot-thread.  Bring popcorn 


