---
title: "81 - What does best practice even mean?"
date: 2019-12-07
description: "It's a short one this week because I'm currently touring Australia speaking at [Yow! Brisbane](https://yowconference.com/brisbane/) conference, and I've therefore been enjoying the sun and heat."
permalink: /what-does-best-practice-even-mean/
---

It's a short one this week because I'm currently touring Australia speaking at [Yow! Brisbane](https://yowconference.com/brisbane/) conference, and I've therefore been enjoying the sun and heat.

The subject of my talks is really about where security is going.  I repeat the theme that the best practices of the previous generation of architectures are not necessarily the best practices of the next generation of architectures.  That instead we have emerging new practices that sometimes disagree with what we call "best practice".

A good example of this is the way that password best practice has changed over time.  Back when we had just one computer, one password, and it required physical access to get to it, our typical passwords worked against our threat model.  But as the context changed, and we had hundreds of passwords, each with complexity requirements, the humble password no longer works for the threat model of today.  But we continue to fight the battles from before using the weapons of the previous generation, creating increasingly difficult complexity requirements and so on.

A modern security team might not follow the best practices of yesteryear.  They might not be separate to engineering, they might report to the CTO for example, because they spend more time building tools and don't want to be considered the auditors.  They might work in code rather than reading architecture diagrams and documents.

When we say best practice we tend to mean agreed best practice which requires a depth of experience to know what practices are good, what works in pretty much all contexts and can be agreed.  But when we are doing new and novel things, the best practice will rarely work for us.  Instead we have to focus on the emerging practice, the practices done just by a few companies, by the newest and most innovative instead.

But we can't try to evolve and do every possible new practice at once, and we can't do that stuff when we struggle with the basics.  We need to pick the places where an emerging practice aligns with the value that we are looking for as an organisation and focus on the ones that give us the best benefits.

## [A con man allegedly built a fake border crossing between Russia and Finland — and got paid to smuggle migrants to the ‘Finnish’ side - The Washington Post](https://www.washingtonpost.com/world/2019/12/05/conman-built-fake-border-crossing-between-russia-finland-got-paid-smuggle-migrants-finnish-side/)

[https://www.washingtonpost.com/world/2019/12/05/conman-built-fake-border-crossing-between-russia-finland-got-paid-smuggle-migrants-finnish-side/](https://www.washingtonpost.com/world/2019/12/05/conman-built-fake-border-crossing-between-russia-finland-got-paid-smuggle-migrants-finnish-side/)

> The unidentified man swindled four migrant workers from South Asia last month, taking more than $40,000 from them in exchange for the promise of safe passage into the European Union, according to Russian news reports. Finnish broadcaster YLE reported that he took them on a roundabout route that, at one point, included walking them around a lake as they carried a boat.
> 
> “The so-called guide decided to simulate an illicit border crossing and make some easy money without actually providing the four with assistance in illegally crossing the Russian border,” Russia’s border security forces said in a statement, according to the state-run Tass news agency. “The fraudster really got into the character for his role, going as far as making and installing fake border posts in a forest.”


If you can’t trust people smugglers who can you trust?


## [Treasury Sanctions Evil Corp, the Russia-Based Cybercriminal Group Behind Dridex Malware | U.S. Department of the Treasury](https://home.treasury.gov/news/press-releases/sm845)

[https://home.treasury.gov/news/press-releases/sm845](https://home.treasury.gov/news/press-releases/sm845)

> Evil Corp operates as a business run by a group of individuals based in Moscow, Russia, who have years of experience and well-developed, trusted relationships with each other.  Maksim Yakubets (Yakubets) serves as Evil Corp’s leader and is responsible for managing and supervising the group’s malicious cyber activities.  For example, as of 2017, Yakubets supervised Evil Corp actors who were attempting to target U.S. companies.  As of 2015, Yakubets maintained control of the Dridex malware and was in direct communication with Andrey Ghinkul prior to the unsealing of his indictment.  As a result, Yakubets is being designated pursuant to E.O. 13694, as amended, for having acted for or on behalf of and for providing material assistance to Evil Corp.  Prior to serving in this leadership role for Evil Corp, Yakubets was also directly associated with Evgeniy Bogachev, a previously designated Russian cybercriminal responsible for the distribution of the Zeus, Jabber Zeus, and GameOver Zeus malware schemes.  In particular, Yakubets was responsible for recruiting and managing a network of individuals responsible for facilitating the movement of money illicitly gained through the efforts spearheaded by Evgeniy Bogachev.  Yakubets is the subject of an indictment and criminal complaint unsealed today by the Department of Justice, while the Department of State announced a $5 million reward for information leading to the capture of Yakubets. 
> 
> In addition to his leadership role within Evil Corp, Yakubets has also provided direct assistance to the Russian government.  As of 2017, Yakubets was working for the Russian FSB, one of Russia’s leading intelligence organizations that was previously sanctioned pursuant to E.O. 13694, as amended, on December 28, 2016.   As of April 2018, Yakubets was in the process of obtaining a license to work with Russian classified information from the FSB.


If you name your company Evil Corp, and yet get government contracts, there is definitely something funny about that government procurement process going on surely!

This is quite the indictment and hopefully will have an impact on the Dridex family of malware, since it's reliably one of the most pernicious pieces of banking malware out there.


## [#745324 Account takeover via leaked session cookie](https://hackerone.com/reports/745324)

[https://hackerone.com/reports/745324](https://hackerone.com/reports/745324)

> HackerOne triages incoming reports for HackerOne’s own bug bounty program. On November 24, 2019, a Security Analyst tried to reproduce a submission to HackerOne’s program, which failed. The Security Analyst replied to the hacker, accidentally including one of their own valid session cookies.
> 
> Why was a cookie included?
> When a Security Analyst fails to reproduce a potentially valid security vulnerability, they go back and forth with the hacker to better understand the report. During this dialogue, Security Analysts may include steps they’ve taken in their response to the report, including HTTP requests that they made to reproduce. In this particular case, parts of a cURL command, copied from a browser console, were not removed before posting it to the report, disclosing the session cookie.


As a reminder, being able to steal a session cookie means you can almost always completely impersonate a user, because session cookies give you a pre-authenticated account.

This is what makes XSS attacks so powerful, because many cookies are accessible to javascript, and if you can get a users browser to execute your javascript, you can make it steal the session cookie.  Do that in a place an insider or admin uses and you've got yourself admin access.


## [The real “challenger” banking business model is data, not money | 15Mb](http://blog.dgwbirch.com/?p=583)

[http://blog.dgwbirch.com/?p=583](http://blog.dgwbirch.com/?p=583)

> What big tech wants is the distribution side of the business, as shown in this old diagram of mine. They have no legacy infrastructure (eg, branches) so their costs are lower, but to my mind more importantly the provision of financial services will keep customers within their ecosystems. If you use the Google checking account and Google pay then Google will have a very accurate picture of your finances. As the article says “Amazon wants payments in-house so users never leave its app”. Indeed.
> 
> The business model here is very clear. What Big Tech wants isn’t your money (the margins on payments are going down) but your data. That’s why when people talk about “challengers” they should really be talking about Microsoft and not Monzo.


A health reminder, with a lovely diagram this time, that your shopping data is valuable. 

Good companies are thinking about ensuring that users can make healthy choices about using their data appropriately.  Most people aren't privacy advocates and are willing to give up some privacy in exchange for things they find valuable.  Services that can use that data and help you save money by switching energy suppliers, or recommend savings that are appropriate to you.  Of course many companies also just want to make as much money as possible out of capturing and selling that data as well.


## [Zero trust architecture design principles - NCSC](https://www.ncsc.gov.uk/blog-post/zero-trust-architecture-design-principles)

[https://www.ncsc.gov.uk/blog-post/zero-trust-architecture-design-principles](https://www.ncsc.gov.uk/blog-post/zero-trust-architecture-design-principles)

> The journey to a zero trust architecture can seem like climbing a mountain at times. Determining which approach you should take, looking for a solution which is safe and efficient. When you set off it can be tough going. I'm hoping these principles will make it easier to understand what is needed when planning your transition to a zero trust architecture. 
> 
> While coming up with the principles, I realised they would be better if developed 'in the open', with input from the developers and security professionals busy designing and building systems using zero trust concepts.
> 
> So, I've [published the ZTA Design Principles on GitHub](https://github.com/ukncsc/zero-trust-architecture/), as an alpha release. I'd like the community to do what it does best, providing feedback and even contributing to the project. We'll then finesse and finalise the principles, ready for a more formal release.


It's really nice to see that NCSC is experimenting with developing stuff like this in the open.  NIST did this back with the release of 800-63, the principles for digital authentication that did away with password complexity, and obviously the web itself has been developed this way through the IETF and W3C for a long time.

I don't think that many of us can even agree on what Zero Trust Architecture actually is, so setting out some principles can help us to understand what it is, what products are a good fit and to identify snake oil vendors who should be avoided.


## [Atlassian scrambles to fix zero-day security hole accidentally disclosed on Twitter • The Register](https://www.theregister.co.uk/AMP/2019/12/05/atlassian_zero_day_bug/?__twitter_impression=true)

[https://www.theregister.co.uk/AMP/2019/12/05/atlassian_zero_day_bug/?__twitter_impression=true](https://www.theregister.co.uk/AMP/2019/12/05/atlassian_zero_day_bug/?__twitter_impression=true)

> The SwiftOnSecurity Twitter account revealed that Atlassian provided a domain that resolved to a local server with a common SSL certificate for its Confluence cloud service, to enable the Atlassian Companion app to edit files in a preferred local application and save the files back to Confluence.
> 
> Confluence connects to its companion app through the browser using the rather unwieldy domain: https://atlassian-domain-for-localhost-connections-only.com.
> 
> The problem with this arrangement is that anyone with sufficient technical knowledge could copy the SSL key and use it to conduct a man-in-the-middle attack that could allow an attacker to redirect app traffic to a malicious site.


This is a rather startling hole here.  The fact that this allows easy man in the middle attacks on what probably contains a bunch of sensitive information is really not good.  It's unclear from the reporting whether this also affects confluence and jira instances that are on premise as well as the cloud instances, but if it does, that means that companies that took the explicit action to keep the data inside the company rather than on shared hosting could also be vulnerable.


## [Severe Auth Bypass and Priv-Esc Vulnerabilities Disclosed in OpenBSD](https://thehackernews.com/2019/12/openbsd-authentication-vulnerability.html)

[https://thehackernews.com/2019/12/openbsd-authentication-vulnerability.html](https://thehackernews.com/2019/12/openbsd-authentication-vulnerability.html)

> The authentication bypass vulnerability resides in the way OpenBSD's authentication framework parses the username supplied by a user while logging in through smtpd, ldapd, radiusd, su, or sshd services.
> Using this flaw, a remote attacker can successfully access vulnerable services with any password just by entering the username as "-schallenge" or "-schallenge: passwd," and it works because a hyphen (-) before username tricks OpenBSD into interpreting the value as a command-line option and not as a username.


OpenBSD has been famous for some time for being the most secure operating system around.  It's famous for backporting security fixes and taking a lot of care over the code that goes into it.  To have such a large hole is shockingly embarrassing for them.

It's worth highlighting that sshd itself is not vulnerable to this exploit due to defence in depth, so people can't just ssh into your servers this way, but they can tell from the failure mode whether your system is vulnerable, and then look for ways in via the other vulnerable services.


## [Playbook: Government as a Platform [pdf]](https://ash.harvard.edu/files/ash/files/293091_hvd_ash_gvmnt_as_platform_v2.pdf)

[https://ash.harvard.edu/files/ash/files/293091_hvd_ash_gvmnt_as_platform_v2.pdf](https://ash.harvard.edu/files/ash/files/293091_hvd_ash_gvmnt_as_platform_v2.pdf)

> Teams like these have brought modern digital ways of working into the heart of government, adopting agile software development, user centered design, and the use of cloud hosting and open-source technology.
> 
> Along with new practices, these organizations have brought new professions into government: product managers, software engineers, user researchers, service designers, data scientists and chief digital officers. These people are the intended audience of this playbook: practitioners looking for approaches to implementing platforms in government
> 
> As such, there is some level of minimum capability that an organization needs before it starts trying to implement many of the examples listed in this playbook. If you are working in an organization that is just starting on its digital transformation journey, then probably the best thing to do is focus on building an effective user centred design capability first.
> 
> Even for more digitally mature organizations, attempting to do everything listed here at once is probably a bad idea. Every organization will have strategic decisions to make about where to start. Please view this as a starting point rather than a detailed journey map.


This is a great read, lots of really important things to pick up such planning for self service covering not just developer self service, but ensuring that commercial and procurement teams can easily understand what's needed and other things.

But one of the most important statements in here is the reminder that you might not want to do any of this, because you need a level of capability to carry this out and if you don't have it, these patterns wont help.

I see this in security strategies all the time, with strategies looking to create cool red teams or purple teams, or provide amazing devsecops consultants and security engineering platforms.  But in an organisation that doesn't gather logs or know it's own estate, while those are good patterns, they are not necessarily the ones to focus on until you've built your core capability.


## [Federal Agencies Need to Address Aging Legacy Systems [pdf]](https://www.gao.gov/assets/680/677454.pdf)

[https://www.gao.gov/assets/680/677454.pdf](https://www.gao.gov/assets/680/677454.pdf)

> Department for the Treasury - Business Master File
> 
> Retains all tax data pertaining to individual business income taxpayers and reflects a continuously updated and current record of each taxpayer’s account. This
> investment is also written in assembly language code and operates on an IBM mainframe.
> 
> The agency has general plans to update this system, but there is no time frame established for this update.
> 
> Department of Defense - Strategic Automated Command and Control System
> 
> Coordinates the operational functions of the United States’ nuclear forces, such as intercontinental ballistic missiles, nuclear bombers, and tanker
> support aircrafts. This system runs on an IBM Series/1 Computer—a 1970s computing system— and uses 8-inch floppy disks.
> 
> The agency plans to update its data storage solutions, port expansion processors, portable terminals, and desktop terminals by the end of fiscal year 2017


A stark reminder that Government sits on some shockingly legacy systems.  Systems that are over 50 years old, still processing and maintaining critical systems like the tax system or intercontinental ballistic missile launches.

Note that this was from 2016, and it was the DoD's Strategic Automated Command and Control System that triggered the false alarm in Hawaii in 2018, because the project to replace the "terminals" (not the entire system, but the 8 inch floppies bit at least) was running 2 years over from the original expectations. 


