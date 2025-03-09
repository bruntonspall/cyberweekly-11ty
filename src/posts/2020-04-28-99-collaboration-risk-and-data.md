---
title: "99 - Collaboration, Risk and Data"
date: 2020-04-28
description: "Major General Copinger-Syme’s speech is a rousing affair that outlines 3 areas of opportunity for the UK Military complex that digital disruption is going enable.  These are challenges around collaboration, around risk and around use of data."
permalink: /collaboration-risk-and-data/
---

Major General Copinger-Syme’s speech is a rousing affair that outlines 3 areas of opportunity for the UK Military complex that digital disruption is going enable.  These are challenges around collaboration, around risk and around use of data.

The last few weeks of lockdown in the UK has shown to me just how unprepared most organisations and specifically, most security teams within organisations are in these areas.  When we've needed to collaborate the most, security teams have over-egged the risks that collaboration tools provide, and have lacked the basic access to data to backup their points about said risk.  Security has yet again been at worst a blocker or at best irrelevant for organisations trying to cope with changing and trying circumstances.

I really like these challenges set out by the Major General, they really show the challenges facing most major organisations around the world. The challenge that our staff need increasingly complex and capable ways of interacting and collaborating.  The old silo's of work places just don't cut it anymore, and instead we see small multi-disciplinary teams that have members from different areas of the organisation, and all wanting to collaborate on the same projects.  This often means discovering that our standard issue corporate tools of Word and Excel are just not up to the task, and we need to enable people to take notes, to sketch ideas, to organise their time, and of course to work in a variety of places.

I feel I've spoken endlessly about the problems of risk assessment, and our understanding of risk, so I'm going to skip that area.

But our access to data, and our ability to understand data is generally lacking in many organisations.  Instead of fast moving ability to understand data, the ability to use modern data science tools and multidisciplinary teams, we tend to see vast slow enterprise data products, huge data lakes that are slow to be updated, impossible to get analytics out of, and require the use of enterprise tooling to create dashboards that are mostly almost as bad as the data that gets put into them.

We need to understand our data more by artfully considering the insights we need to glean, and then going back to capture the data that is needed to provide those insights.  Rarely, when faced with a soup of low value data, have we been able to generate useful insights.  Skilled data analysis requires input at all levels, including understanding the data needs of decision makers, both at executive level and at delivery level, as well as understanding what's possible and the privacy and security implications of gathering the data.

Major General Copinger-Syme is right to highlight these areas as ones that we need to address and try to fix in our organisations.  We won't fix these with overarching enterprise architectures or governance structures that change organisations, we'll fix these with small multi-disciplinary teams who have the ability and authority to work across silos to develop appropriate ways of working, and to demonstrate the value of a transformed organisation.

## [Application Security Training For Developers | Kontra](https://application.security/free-application-security-training)

[https://application.security/free-application-security-training](https://application.security/free-application-security-training)

> At KONTRA, we believe every software engineer should have free access to developer security training. KONTRA OWASP Top 10 is our first step in that direction. Inspired by real-world vulnerabilities and case studies, we've created a series of interactive application security training modules to help developers understand, identify and mitigate security vulnerabilities in their applications.


This is a lovely training resource for developers.  I featured their Capital One SSRF module when it first launched, but they now have a variety of examples, mostly taken from real world public exploits, explaining how they worked and how you can spot them.


## [You’ve Got (0-click) Mail! - ZecOps Blog](https://blog.zecops.com/vulnerabilities/unassisted-ios-attacks-via-mobilemail-maild-in-the-wild/#)

[https://blog.zecops.com/vulnerabilities/unassisted-ios-attacks-via-mobilemail-maild-in-the-wild/#](https://blog.zecops.com/vulnerabilities/unassisted-ios-attacks-via-mobilemail-maild-in-the-wild/#)

> Following a routine iOS Digital Forensics and Incident Response (DFIR) investigation, ZecOps found a number of suspicious events that affecting the default Mail application on iOS dating as far back as Jan 2018. ZecOps analyzed these events and discovered an exploitable vulnerability affecting Apple’s iPhones and iPads. ZecOps detected multiple triggers in the wild to this vulnerability on enterprise users, VIPs, and MSSPs, over a prolonged period of time.
> 
> The attack’s scope consists of sending a specially crafted email to a victim’s mailbox enabling it to trigger the vulnerability in the context of iOS MobileMail application on iOS 12 or maild on iOS 13. Based on ZecOps Research and Threat Intelligence, we surmise with high confidence that these vulnerabilities – in particular, the remote heap overflow – are widely exploited in the wild in targeted attacks by an advanced threat operator(s).


There's been a bit of to-ing and fro-ing about this, is it really a vulnerability, is it as bad as ZecOps say it is?  Apple denies that this is actually a live exploit.  Their security team have tried it using the details passed and are unable to actually get "remote code execution" which is of course a critical step in remotely compromising someones iOS device.

The bug that causes crashes and loss of mail data in Apple's Mail product should be fixed any day now, and ZecOps said that they'll publish more details, along with Proof of Concept code when that happens.

This is a good reminder that all of our devices run thousands of pieces of software, and that many will contain bugs and issues that could result in a security flaw.  It's exciting to focus on the coolest newest application, such as Zoom, but the reality is that your todo list, calendar tool or mail client may also have vulnerabilities that can be exploited by malicious actors.


## [Is BGP safe yet? · Cloudflare](https://isbgpsafeyet.com/)

[https://isbgpsafeyet.com/](https://isbgpsafeyet.com/)

> Border Gateway Protocol (BGP) is the postal service of the Internet. It’s responsible for looking at all of the available paths that data could travel and picking the best route.
> 
> Unfortunately, it isn’t secure, and there have been some major Internet disruptions as a result. But fortunately there is a way to make it secure.
> 
> ISPs and other major Internet players (Comcast, Sprint, Verizon, and others) would need to implement a certification system, called RPKI.


This has got a nice, if overly simplistic depiction of BGP hijacking.  Obviously it's being pushed by Cloudflare who were one of the first adopters of RPKI.  But we do need better protections for BGP, since the current system is based on trust that only network operators and internet service providers would broadcast BGP routes, and those would all be trustworthy organisations.  Global scale and politics means that there is less trust in the system than originally envisioned and there are lots of reasons for organisations to either make mistakes or to believe that they have a legitimate reason to announce a route that the rest of the network or owner of the end target doesn't agree is legitimate.

Cloudflare have been pushing for improvements to this system for a while now and RPKI is their posterchild for the last few years.  You can read a lot more about it [at their blog](https://blog.cloudflare.com/rpki/) if you want to know more about how BGP works or RPKI is intended to fix some of the problems


## [Azure Skeleton Key: Exploiting Pass-Through Auth to Steal Credentials](https://www.varonis.com/blog/azure-skeleton-key/)

[https://www.varonis.com/blog/azure-skeleton-key/](https://www.varonis.com/blog/azure-skeleton-key/)

> Should an attacker compromise an organization’s Azure agent server–a component needed to sync Azure AD with on-prem AD–they can create a backdoor that allows them to log in as any synchronized user. We created a proof-of-concept that manipulates the Azure authentication function to 1.) give us a ‘skeleton key’ password that will work for all users, and 2.) dump all real clear-text usernames and passwords into a file.


Microsoft have denied that this is a vulnerability, this is "working as intended" as far as they are concerned, and requires attackers to have already compromised a server on your estate that is running the Azure AD Sync toolset.  Of course, if the attacker can compromise that server, they already have a lot of access to your systems, but this falls into the ATT&CK exploit frameworks "[Credential Access](https://attack.mitre.org/tactics/TA0006/)" set of tactics which are of course, post exploitation.

In simple terms, if an attacker can get onto one of your servers and upgrade their local access on that server to enable them to deploy software that can interfere with the AD sync tools, then they can get other users access passwords, which might be useful for attacking other systems where the users use the same password, and they can additionally authenticate users as admins in any other system that relies on the AD sync.  That enables remote exploitation in a far easier and stealthier way.

Yes, they need to have already broken into your active sync server, but maybe that's not as hard as it should be.  This finding strongly suggests that you run a dedicated server for this, and that you lockdown and monitor that server carefully.


## [Azure AD introduction for red teamers](https://www.synacktiv.com/posts/pentest/azure-ad-introduction-for-red-teamers.html)

[https://www.synacktiv.com/posts/pentest/azure-ad-introduction-for-red-teamers.html](https://www.synacktiv.com/posts/pentest/azure-ad-introduction-for-red-teamers.html)

> Azure Active Directory (Azure AD) is Microsoft’s cloud-based identity and access management service. It is more and more used by customers in order to connect their on-premises Active Directory with online services such as Office365, SharePoint, Teams, etc.
> 
> The aim of this article is to briefly present Azure AD and to explore the different attacking paths this new cloud environment offers to pentesters and red teamers.


A good partner article to the Varonis Azure Skeleton Key, this article explains a lot more about common Active Directory setups and ways that you can explore and recon those setups to work out what's going on.  It has a very similar attack as the Varonis one, as well as some nice info on single sign on attacks and a list of further reading for red teams


## [Thread by @jsrailton: Wow, @WhatsApp just dropped a bunch of hacking group NSO's IPs in their latest filing. Notably, these were servers located in the USA. THREA…](https://threadreaderapp.com/thread/1253502213353361412.html)

[https://threadreaderapp.com/thread/1253502213353361412.html](https://threadreaderapp.com/thread/1253502213353361412.html)

> KEY TAKEAWAY: NSO says "our clients do the hacking, not us". This filing shows NSO purchasing & operating the servers doing the hacking. This makes the company look much more like hacking-as-a-service than software developers... 
> 
> ...moreover, if NSO runs these infection servers then they must have logs of the connections. Sounds like they should be able to know exactly who was targeted, down to the victim device IP and time. So much for denials that they can't see what customers are doing. 
> 
> ...Which makes you wonder: does NSO collect detailed intelligence on their customers? Do its customers realize that NSO has this level of total visibility into what they are doing?


This is quite the damning finding from WhatsApp/Facebook's legal team.  NSO group has long stuck to the PR line that they provide tools only to governments and law enforcement entities.  And while some nations have very differing views on the moral and ethical frameworks that law enforcement has in different jurisdictions, that's a somewhat defensible line (if you squint at it right).  Furthermore they've always claimed that like a weapons manufacturer, they don't actually use the weapons, they simply supply them to legally appropriate organisations

However, WhatsApp/Facebook is saying that this isn't true, that NSO is both unable to provide a list of the organisations it has sold to in order to verify its claim, but also has produced evidence that it operates some of the infrastructure on behalf of the organisations.  As John points out in his twitter thread, I wonder if the organisations that bought these systems were aware of that, and that their target list would therefore be visible to NSO?


## [The Cybersecurity 202: There's finally a Supreme Court battle coming over the nation’s main hacking law - The Washington Post](https://www.washingtonpost.com/news/powerpost/paloma/the-cybersecurity-202/2020/04/24/the-cybersecurity-202-there-s-finally-a-supreme-court-battle-coming-over-the-nation-s-main-hacking-law/5ea1ade6602ff140c1cc5f51/)

[https://www.washingtonpost.com/news/powerpost/paloma/the-cybersecurity-202/2020/04/24/the-cybersecurity-202-there-s-finally-a-supreme-court-battle-coming-over-the-nation-s-main-hacking-law/5ea1ade6602ff140c1cc5f51/](https://www.washingtonpost.com/news/powerpost/paloma/the-cybersecurity-202/2020/04/24/the-cybersecurity-202-there-s-finally-a-supreme-court-battle-coming-over-the-nation-s-main-hacking-law/5ea1ade6602ff140c1cc5f51/)

> That case focuses on a former Georgia police officer, Nathan Van Buren, who was convicted under the law in 2017 after he allegedly sold information from a police database to an acquaintance for $6,000. The information was allegedly focused on helping the acquaintance figure out whether a local stripper was actually an undercover cop. 
> 
> CFAA critics say that takes the anti-hacking law too far because Van Buren didn’t actually hack into anything. He just broke the rules for a database that he was legitimately allowed to use. 
> 
> Courts in New York, California and several other states generally require that a person actually hack into a computer by using stolen information or exploiting a bug in the system to be prosecuted under the law, while courts in states including Georgia and Florida have convicted people in cases such as Van Buren's where there’s no clear hacking. 


The problem with broadly drafted laws, such as the Computer Fraud and Abuse Act (CFAA) is that the decision about whether to enforce lies with the prosecutors.  They are correctly saying that this isn't supposed to be about hacking into computers, but to also cover misuse of a computer to which you have authorised access.

The big problem here is not the police officer looking up confidential information about undercover officers (like what!), it's that we can't easily and effectively describe "misuse" in legal language that doesn't also catch out security researchers who might break the terms of service.

In my mind, reducing the impact of the CFAA to not cover misuse of official systems, but then either writing a new law, or adjusting existing laws around fraud and misuse should make it clearer.  In the case of a police officer, the misuse of their powers and data is a breach of trust that should be prosecuted directly, rather than because they happened to use a computer to carry out the crime.


## [The Extended AWS Security Ramp-Up Guide – NCC Group Research](https://research.nccgroup.com/2020/04/24/the-extended-aws-security-ramp-up-guide/)

[https://research.nccgroup.com/2020/04/24/the-extended-aws-security-ramp-up-guide/](https://research.nccgroup.com/2020/04/24/the-extended-aws-security-ramp-up-guide/)

> Clients, in the run up to or wake of an assessment, are frequently looking to broaden their understanding of AWS security. We’ve found the Ramp-up a useful reference to point people to, as it gives the high-level view of how to learn AWS Security. Its role as an official AWS document lends to the curation, credibility, and overall quality. However, as an AWS resource, it focuses exclusively on AWS’s first-party resources and services. In light of this, we’ve put together the following “Extended” AWS Security Ramp-Up Guide, compiling some of the public resources we’ve found most helpful. Centralizing these resources will serve the same purposes as the original, and it allows us to publicly document them in a place that we can point to in the future. We also hope this will be a reference for the general public, those learning AWS Security, and those responsible for AWS environments.


I tend to think that this is a bit embaressing of AWS that a third party has put this tofgether.  I like AWS as a technical system, and generally the documentation of any given service is excellent.  But the overall documentation of the AWS ecosystem and how things fit together can be frustrating to the extreme.

This is a handy additional guide on top of [The AWS Ramp Up Learning Guide for AWS Cloud Security, Governance and Compliance](https://aws.amazon.com/blogs/security/ramp-up-learning-guide-cloud-security-governance-compliance/)


## [Digital Disruption: Major General Copinger-Syme’s Speech to the UK Strategic Command Inaugural Conference at RUSI](https://wavellroom.com/2020/02/24/digital-disruption-major-general-copinger-symes-speech-to-the-uk-strategic-command-inaugural-conference-at-rusi/)

[https://wavellroom.com/2020/02/24/digital-disruption-major-general-copinger-symes-speech-to-the-uk-strategic-command-inaugural-conference-at-rusi/](https://wavellroom.com/2020/02/24/digital-disruption-major-general-copinger-symes-speech-to-the-uk-strategic-command-inaugural-conference-at-rusi/)

> Second, that our leaders are disoriented and dislocated by the blizzard of information with which they’re currently being hit – our own, our partners’ and our adversaries’ – so that their decisions are confused; or too late to be relevant; or focused on the wrong problems.  As I’ve said at RUSI before – we risk drowning in information; asphyxiated by a lack of understanding.
> 
> Thirdly that our exquisite, few, beautifully engineered – and rather large platforms – are out-paced, out-thought and out-fought by multiple, small, agile and autonomous platforms, whether in the hands of terrorist groups or challenger states.  Particularly if those adversary platforms are defined by the software that animates them rather than the armour and weaponry that weighs us down.
> 
> We don’t have an innovation problem – quite the opposite, a thousand innovative flowers are blooming across Defence, whether in the Services, the DE&S or the DIO, the Ministry itself, or our peerless scientists in dstl.  But we do have an ‘innovation adoption’ problem – we struggle to incorporate those innovations into our core capabilities and focus real investment on them.  The old saying is ‘think big; start small; and be prepared to scale – or fail’.  But we are bad at ‘scaling’ and we are simply awful at ‘failing’ old ideas to make way for new ones.  As Liddell Hart used to say – ‘it’s not so hard getting a new idea into a military mind; but it’s very hard to get an old one out’.  
> 
> We are good at doing things better – but we are bad at imagining our way to doing better things.  So, for me the key opportunities lie in ‘hacking’ our culture – taking us back to our better selves, when we were prepared to think the unthinkable to achieve a generational edge on our competitors.
> 
> I’ll focus on three areas of opportunity, where I think we can hack our culture to get back to where we used to be:
> 
> The first area is collaboration.  Like many large, established organisations, we are fixated by our structural boundaries.  We like to tell people to ‘stay in lane’…  But that’s not the way to win the 21st Century, which is a time of collaboration, cooperation and integration.  And there is little chance of Defence or the Services suffering from too little competition.
> 
> The second area is risk.  The risk aversion is exhausting us; it’s tying up our resources – in particular our people but also our money and critically our time; and it’s turning off our brightest and best.  They want to move at the speed of relevance and in a disruptive age that means taking very significant risks.  In the Digital space this is tricky – with our mantra of ‘Secure First’.  But when you get under the skin that doesn’t mean cutting ourselves off from our partners – rather it means ‘designing in’ features that allow us to take risks knowingly and for the right reasons.
> 
> Last it will really help us in all this if we can breed a culture in which we recognise and value data as the strategic asset that it is. 


I've decided to quote quite a few different bits of this, but you should definitely go and read the entire speech, it's a complete stonker of a speech.  It correctly identifies some of the biggest challenges in digital transformation, especially within the military services, but also generally in any large organisation, and it identifies some of the areas of opportunity where we can make a difference.


