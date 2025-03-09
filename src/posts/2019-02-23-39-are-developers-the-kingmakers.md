---
title: "39 - Are developers the kingmakers?"
date: 2019-02-23
description: "Stephen Grady wrote a book around 5 years ago called [The New Kingmakers](https://www.amazon.co.uk/New-Kingmakers-Developers-Conquered-World-ebook/dp/B0097E4MEU/ref=sr_1_1?ie=UTF8&qid=1550301534&sr=8-1&keywords=Developers+are+the+new+kingmakers) in which he argued that people with the ability to write software would fundamentally change the way that business would operate.  This hasn’t come true generally, probably a combination of developers having a myopic view of users (developers love to build for other developers, but struggle to remember that many users don’t care about the same things that they do), and the fact that while technology has advanced, most businessiness don’t take advantage of the power of developers."
permalink: /are-developers-the-kingmakers/
---

Stephen Grady wrote a book around 5 years ago called [The New Kingmakers](https://www.amazon.co.uk/New-Kingmakers-Developers-Conquered-World-ebook/dp/B0097E4MEU/ref=sr_1_1?ie=UTF8&qid=1550301534&sr=8-1&keywords=Developers+are+the+new+kingmakers) in which he argued that people with the ability to write software would fundamentally change the way that business would operate.  This hasn’t come true generally, probably a combination of developers having a myopic view of users (developers love to build for other developers, but struggle to remember that many users don’t care about the same things that they do), and the fact that while technology has advanced, most businessiness don’t take advantage of the power of developers.

Stephens’s main point was that developers have a unique combination of skills, the ability to see and understand how technology works, and their ability to actively make changes to software, to build systems that can take advantage of the world around them.  

I was reminded of this reading the little nugget in the Okta IT survey that showed that organisations that had Developers in them were significantly more likely to use Google’s G-Suite.  I know that most of the developers I talk to prefer G-Suite over Office 365, but I’ve never stopped to wonder why that is, and what that might mean.  I suspect that in many organisations around the world, the developers are also the ones who use the most “shadow IT”, the ones who want to use various SaaS tools and systems.  Is this just because developers are used to using a variety of small tools to do a job, or is there something about the usage of standard corporate tools that turns off developers?

It would be interesting in your organisations to try to understand what tools your developers use, and would prefer to use, and try to understand why that is.

## [Businesses at Work 2019 | Okta](https://www.okta.com/businesses-at-work/2019/)

[https://www.okta.com/businesses-at-work/2019/](https://www.okta.com/businesses-at-work/2019/)

> We also looked at whether companies who invest in the Office 365 suite — the top app in our network — end up committing to a Microsoft-only environment, and the answer was clearly “no.” We found that 76% of Okta’s Office 365 customers have one or more apps that are duplicative of apps offered by Microsoft. Over 28% are chatting on Slack. Nearly 24% are connecting with their colleagues on Zoom. And over 28% of Okta’s Office 365 customers are “double bundling” themselves, subscribing to G Suite as well. Looking at the total number of customers who leverage Okta for workforce identity, we see a smaller proportion of customers using Active Directory, from a high of over 78% in August 2015 to 70% in 2018.
> 
> Also noteworthy, companies investing in developer tools are three times as likely to deploy G Suite as are “non-developers” (companies without any developer tools). Our data shows that 46% of companies with at least one developer tool also have G Suite, vs. only 17% of non-developers.
> 
> Microsoft has long established itself as a workplace necessity, and thus has its fair share of loyal users. Our survey found that 67% of knowledge workers prefer Microsoft Word over Google Docs, while only 15% report the opposite. When it comes to email, 49% prefer Microsoft Outlook over Gmail, while 35% report the opposite.
> 
> But G Suite has the broader greenfield. Nearly half (49%) of our survey respondents have never used Google Docs. We expect that this number may decrease as G Suite’s rapid growth continues, due in part to employee demands. Gmail is the number one app knowledge workers wish their company would adopt.


This is a really interesting snapshot of what digital tools workers use to do their jobs.

As a self-confessed fan of the G-Suite tools, there's another interesting story here for me.  I think that Office 365 is kind of the corporate default, that lots of companies use it, and that people who use it like it.  But people who have used both is far less common, and market penetration of G-Suite means that this preference is being expressed from a small number.

The most interesting statistic to me though is when you have developers in your company, you are more likely to select G-Suite.  I wonder if that's indicative of the type of company you are, or whether it's indicative of the tool selection capability of developers?


## [dxw cyber: the state of the sector](https://stateofthesector.dxwcyber.com/)

[https://stateofthesector.dxwcyber.com/](https://stateofthesector.dxwcyber.com/)

> The state of the sector
> 
> We've assembled the most complete list yet of domains across the public sector, and collected a large dataset about their security.
> 
> These are the headline statistics.


I didn’t cover this when released because that was before I started this newsletter, and was reminded this week thanks to a discussion in a slack channel.  This is an excellent use of network scanning, analytical tooling and statistics to understand the state of the public sector web presence, and how the public sector manages the basics of security online.  I’m hoping that we've been able to make things better this year, and the update to this should show improvements for Government.


## [dtag-dev-sec/tpotce: T-Pot Universal Installer and ISO Creator](https://github.com/dtag-dev-sec/tpotce)

[https://github.com/dtag-dev-sec/tpotce](https://github.com/dtag-dev-sec/tpotce)

> T-Pot is based on the network installer of Ubuntu Server 18.04.x LTS. The honeypot daemons as well as other support components being used have been containerized using docker. This allows us to run multiple honeypot daemons on the same network interface while maintaining a small footprint and constrain each honeypot within its own environment.


A honeypot is a system that looks sweet and interesting but actually logs all of an attackers behaviour elsewhere so that you can see what they are doing.  This is a lovely tool for trying a well configured interesting honeypot, in a number of configurations, and using docker to keep everything separate.  Install something like this on your internal network and see if it ever sends you anything to know if you've been compromised, or install one on the public internet to start gathering information about what common attacks are being tried out there all the time.


## [APT10 Targeted Norwegian MSP and US Companies in Sustained Campaign](https://www.recordedfuture.com/apt10-cyberespionage-campaign/)

[https://www.recordedfuture.com/apt10-cyberespionage-campaign/](https://www.recordedfuture.com/apt10-cyberespionage-campaign/)

> In all three incidents, the attackers gained access to networks through deployments of Citrix and LogMeIn remote-access software using stolen valid user credentials. The attackers then enumerated access and conducted privilege escalation on the victim networks, utilizing DLL sideloading techniques documented in a US-CERT alert on APT10 to deliver malware. During the Visma intrusion, APT10 deployed their Trochilus malware with command and control (C2) communications encrypted using both RC4 and Salsa20 streaming ciphers rather than the typically observed RC4 variant. On the two other victim networks, the attackers deployed a unique version of the UPPERCUT (ANEL) backdoor, known to have only been used by APT10.
> 
> APT10 actors then compressed proprietary data from Visma using WinRAR (deployed by the attackers) and exfiltrated to a Dropbox account using the cURL for Windows command-line tool. The same Dropbox account was also accessed in a similar fashion by the attackers during the apparel company intrusion. Dropbox was also used to store exfiltrated documents from the third victim, a U.S. law firm, with the files again exfiltrated using identical TTPs and uploaded using cURL for Windows.


This is a good insight into an advanced hacking campaign.  Breaking in using stolen credentials (which thinks like HaveIBeenPwned should alert you to), and then escalating privilege on the networks to start deploying known malware.

The biggest protections against this sort of campaign?  Probably a combination of host based antivirus (such as windows defender), patching core systems to protect against privelege escalations, and montioring for unusual activities of privileged processes.

It's worth noting further down it points out that this attack is conducted as part of the Cloud Hopper campaign and was probably done in order to access Visma's clients rather than targeting Visma themselves.


## [Twitter Still Can't Keep Up With Its Flood of Junk Accounts, Study Finds | WIRED](https://www.wired.com/story/twitter-abusive-apps-machine-learning/)

[https://www.wired.com/story/twitter-abusive-apps-machine-learning/](https://www.wired.com/story/twitter-abusive-apps-machine-learning/)

> They write that more than 60 percent of the time, Twitter waited for those apps to send more than 100 tweets before identifying them as abusive; the researchers' own detection method had flagged the vast majority of the malicious apps after just a handful of tweets. For about 40 percent of the apps the pair checked, Twitter seemed to take more than a month longer than the study's method to spot an app's abusive tweeting. That lag time, they estimate, allows abusive apps to cumulatively churn out tens of millions of tweets per month before they're banned.


I don't think that this research really takes into account the impact of false positives.  They say further down that some 6% of apps flagged this way are in fact benign and could be reviewed by Twitter staff, but the impact on end users, many of whom are just starting to use twitter of being proactively banned or rate limited will hurt takeup rate, and that's the key driver for twitter.


## [Designing Security for Billions | Facebook Newsroom](https://newsroom.fb.com/news/2019/01/designing-security-for-billions/)

[https://newsroom.fb.com/news/2019/01/designing-security-for-billions/](https://newsroom.fb.com/news/2019/01/designing-security-for-billions/)

> In the graphic below, you can see how our “defense-in-depth” approach relies on a combination of technology, expert security teams and the wider security community to help protect our platform. In the following article, we’ll dive into each of these five components — secure frameworks, automated testing tools, peer and design reviews, red team exercises and our bug bounty program — in greater depth.


Note here that bug bounties and red teams are just one component of a security program, and that they are quite far back defences.  These are the sorts of tools you can use effectively only once you have a level of maturity and capability in the other areas.


## [Landlords' 'blacklist' of tenant's criminal convictions hacked and leaked online | National | Stuff.co.nz](https://i.stuff.co.nz/timaru-herald/news/national/110395535/Landlords-blacklist-of-tenants-criminal-convictions-hacked-and-leaked-online)

[https://i.stuff.co.nz/timaru-herald/news/national/110395535/Landlords-blacklist-of-tenants-criminal-convictions-hacked-and-leaked-online](https://i.stuff.co.nz/timaru-herald/news/national/110395535/Landlords-blacklist-of-tenants-criminal-convictions-hacked-and-leaked-online)

> Another "victim", who did not want to be named, said his crimes were committed as a youth in the early 1990s and his convictions are wiped out under the Clean Slate Bill.  
> 
> "I believe this is a privacy breach. I have not reoffended since and do not think it is fair this is dragged back up 25 years later."
> 
> Association president Kerry Beveridge said he was was disappointed that the list had been distributed widely.
> 
> "We are investigating how this happened."
> 
> New Zealand Property Investors Federation chief executive Andrew King said the group had taken legal advice and were within the law. "People added to the list are informed when contact details are known and the list should only be available to SCPIA members."
> 


Yeah, no. This is not an appropriate processing of data. 


## [18F: Digital service delivery | Cloud is not a virtue](https://18f.gsa.gov/2019/02/07/the-cloud-is-not-a-virtue/)

[https://18f.gsa.gov/2019/02/07/the-cloud-is-not-a-virtue/](https://18f.gsa.gov/2019/02/07/the-cloud-is-not-a-virtue/)

> So what is important? When it comes to infrastructure, focus on the outcomes rather than the technology. You should optimize your system around two core benefits: agility and reliability which includes security.


A valuable reminder that cloud native services are more secure than non cloud native services, if only for the audit trail capabilities alone, let alone the rest.  But also a reminder that many organisations treat the cloud as if it is another data centre rather than a new model to work with.


## [620 million accounts stolen from 16 hacked websites now for sale on dark web, seller boasts • The Register](https://www.theregister.co.uk/2019/02/11/620_million_hacked_accounts_dark_web/)

[https://www.theregister.co.uk/2019/02/11/620_million_hacked_accounts_dark_web/](https://www.theregister.co.uk/2019/02/11/620_million_hacked_accounts_dark_web/)

> Their aim is to make "life easier" for hackers, by selling fellow miscreants usernames and password hashes to break into other accounts, as well as make some money on the side, and highlight to netizens that they need to take security seriously – such as using two-factor authentication to protect against password theft. The thief also wanted to settle a score with a co-conspirator, by selling a large amount of private data online.
> 
> The hacker previously kept stolen databases private, giving them only to those who would swear to keep the data secret.
> 
> "I don't think I am deeply evil," the miscreant told us. "I need the money. I need the leaks to be disclosed.
> 
> "Security is just an illusion. I started hacking a long time ago. I'm just a tool used by the system. We all know measures are taken to prevent cyber attacks, but with these upcoming dumps, I'll make hacking easier than ever."


This is an interesting interview with an attacker that includes some insight as to their motivations.  We often, in risk asssessment terms, consider a breach of data to be the worst case. But in reality, there is a bunch of follow on motivations that actually matter when a system is breached.  What is the impact if a nation state breaches you and stores the data in a top secret system only accessible by themselves? What is the impact if an individual hacker takes the data and uses it in follow on crimes?  Not all breaches result in public disclosure of the impacted data, and we should remember that.


