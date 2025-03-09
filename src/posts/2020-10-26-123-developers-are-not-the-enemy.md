---
title: "123 - Developers are not the enemy"
date: 2020-10-26
description: "If you are a developer, you need to assume that your users are not the enemy, that they want to get the job done in the safest way possible.  If you write code for other developers, you need to assume the same thing."
permalink: /developers-are-not-the-enemy/
---

If you are a developer, you need to assume that your users are not the enemy, that they want to get the job done in the safest way possible.  If you write code for other developers, you need to assume the same thing.

We’ve known for years that cryptographic API’s are hard to use and easy to misuse.  Pass the wrong parameters, or call the wrongly named version of a method, and all of the security constraints fall apart.

But it’s not just API design, tools that are there to be used by developers need to ensure that the defaults are secure, that content is public by default, and that developers can get their job done with the appropriate sets of roles and permissions.

## [Dutch Ethical Hacker Logs into Trump’s Twitter Account | De Volkskrant](https://www.volkskrant.nl/nieuws-achtergrond/dutch-ethical-hacker-logs-into-trump-s-twitter-account~badaa815/)

[https://www.volkskrant.nl/nieuws-achtergrond/dutch-ethical-hacker-logs-into-trump-s-twitter-account~badaa815/](https://www.volkskrant.nl/nieuws-achtergrond/dutch-ethical-hacker-logs-into-trump-s-twitter-account~badaa815/)

> Victor Gevers was also one of the three hackers who logged into Trump’s account in 2016. ‘That we would succeed in doing it again so soon, was not planned’, he says about the buildup to the action. The reason for making another attempt to hack Trump’s account was the reporting in the US about Hunter Biden. A hard disk owned by presidential candidate Joe Biden’s son was supposedly stolen or hacked – also because Hunter Biden used an easy to guess password (Hunter02). Gevers is familiar with leaked databases of old passwords and searched these for Hunter Biden’s data. After analysing these old databases, he felt that the information was incorrect. Hunter Biden used other passwords. Gevers: ‘I could tell that it wasn’t his password.’
> 
> On Friday morning, almost absentmindedly, Gevers tries a number of passwords and their variations. On the fifth attempt: bingo! He tries ‘maga2020!’ (short for make America great again) and suddenly finds himself in the Twitter account of the American President. He is flabbergasted. Gevers: ‘I expected to be blocked after four failed attempts. Or at least would be asked to provide additional information.’ None of that


Newsflash.  People use sucky passwords!

In more interesting news, it feels like this article about the [extra protections afforded to Trumps account](https://www.theverge.com/2020/7/16/21327782/trump-twitter-hacked-massive-attack-bitcoin-scam) is really only talking about protections against insiders within twitter.  I suspect that trumps account could not be modified, viewed or dealt with by normal twitter employees.  But it seems shocking that they didn’t focus on ensuring that the account didn’t have MFA at least.

Turn on MFA for all your significant social media accounts!


## [Operation Earth Kitsune: Tracking SLUB’s Current Operations - Security News - Trend Micro USA](https://www.trendmicro.com/vinfo/us/security/news/cyber-attacks/operation-earth-kitsune-tracking-slub-s-current-operations/)

[https://www.trendmicro.com/vinfo/us/security/news/cyber-attacks/operation-earth-kitsune-tracking-slub-s-current-operations/](https://www.trendmicro.com/vinfo/us/security/news/cyber-attacks/operation-earth-kitsune-tracking-slub-s-current-operations/)

> In our latest research paper, we uncovered a recent watering hole campaign that involves a new variant of the malware. The threat, which we dubbed as such due to its abuse of Slack and GitHub in previous versions, has not abused either of the platforms this time; instead, it employed Mattermost, an open-source online chat service that can be easily deployed on-premise.
> 
> We found Operation Earth Kitsune using a total of five C&C servers, seven samples, and four new bugs, aiming to compromise websites to host malware.


This is interesting in the use of Mattermost as a command and control server. 


## [The Goal of Iran’s Fake 'Proud Boys' Emails Was Chaos](https://www.vice.com/en/article/akdzgp/the-goal-of-irans-fake-proud-boys-emails-was-chaos)

[https://www.vice.com/en/article/akdzgp/the-goal-of-irans-fake-proud-boys-emails-was-chaos](https://www.vice.com/en/article/akdzgp/the-goal-of-irans-fake-proud-boys-emails-was-chaos)

> There is still little public evidence Iran did this campaign: Attributing a cyber operation of any kind to a particular government is a meticulous and often complicated endeavour, and the government who points the finger often can't show the evidence right away. In this case, however, experts who have tracked and studied Iranian government hackers, as well as Iran's hacking and disinformation campaigns, have little doubt.
> 
> Motherboard is publishing the video sent to voters in order to show readers what disinformation campaigns look like, as well as to explain why cybersecurity experts believe Iran is behind this, and what evidence in the video can be useful for attribution purposes. We have redacted the personal information of unsuspecting victims.
> 
> Kargar said that the video that accompanied some of the emails was reminiscent of a video ostensibly created by an Iranian domestic group after a series of mysterious explosions in the country, and an attack on a nuclear plant. The group took credit for those explosions, which have been publicly attributed to Israel, although Israeli officials have denied the accusation. According to Kargar, the fake Proud Boys' video echoes that Iranian video because it has a similar goal of spreading disinformation


There’s lots to unpack here, much of which I can’t really do.  But what was interesting to the casual observer here is that the video mostly just shows how someone can use publicly available information to register to vote.  To normal people this feels like hacking, and I can totally see how it could be intimidating.  The fact that these videos work shouldn’t be much of a surprise, but the fact that people are experimenting and learning what works is worrying


## [Chinese State-Sponsored Actors Exploit Publicly Known Vulnerabilities (PDF)](https://media.defense.gov/2020/Oct/20/2002519884/-1/-1/0/CSA_CHINESE_EXPLOIT_VULNERABILITIES_UOO179811.PDF)

[https://media.defense.gov/2020/Oct/20/2002519884/-1/-1/0/CSA_CHINESE_EXPLOIT_VULNERABILITIES_UOO179811.PDF](https://media.defense.gov/2020/Oct/20/2002519884/-1/-1/0/CSA_CHINESE_EXPLOIT_VULNERABILITIES_UOO179811.PDF)

> This advisory provides Common Vulnerabilities and Exposures (CVEs) known to be recently leveraged, or scanned-for, by Chinese state-sponsored cyber actors to enable successful hacking operations against a multitude of victim networks. Most of the vulnerabilities listed below can be exploited to gain initial access to victim networks using products that are directly accessible from the Internet and act as gateways to internal networks. The majority of the products are either for remote access (T1133)1 or for external web services (T1190), and should be prioritized for immediate patching. While some vulnerabilities have specific additional mitigations below, the following mitigations generally apply:
> 
> * Keep systems and products updated and patched as soon as possible after patches are released.2
> * Expect that data stolen or modified (including credentials, accounts, and software) before the device was patched will not be alleviated by patching, making password changes and reviews of accounts a good practice.
> * Disable external management capabilities and set up an out-of-band management network.3
> * Block obsolete or unused protocols at the network edge and disable them in device configurations.4
> * Isolate Internet-facing services in a network Demilitarized Zone (DMZ) to reduce the exposure of the internal network.5
> * Enable robust logging of Internet-facing services and monitor the logs for signs of compromise.6


The US comes out and identifies a set of known and patched exploits that they say that Chinese state sponsored actors are using.  
Note that to defend against this attack by state sponsored actors, you need to regularly patch your infrastructure.


## [Exploit Developer Spotlight: The Story of PlayBit - Check Point Research](https://research.checkpoint.com/2020/graphology-of-an-exploit-playbit/)

[https://research.checkpoint.com/2020/graphology-of-an-exploit-playbit/](https://research.checkpoint.com/2020/graphology-of-an-exploit-playbit/)

> As part of our effort to focus on the exploit developers themselves, we previously shared our methodology and technique of fingerprinting and tracking exploit developers. In our earlier publication, we thoroughly explained our methodology and focused on Volodya, a prominent exploit developer we tracked using the unique fingerprints left in their exploits. Now our focus is on another exploit developer known as PlayBit or luxor2008.


Now this is some amazing threat hunting content.  Identifying an exploit developer through the code they write, finding all of the other exploits they’ve written and developing clear indicators and TTP’s that can be used to track them.


## [Secrets and spies: Behind the doors of the UK's most enigmatic government agency | National Geographic](https://www.nationalgeographic.co.uk/history-and-civilisation/2020/10/secrets-and-spies-behind-the-doors-of-the-uks-most-enigmatic)

[https://www.nationalgeographic.co.uk/history-and-civilisation/2020/10/secrets-and-spies-behind-the-doors-of-the-uks-most-enigmatic](https://www.nationalgeographic.co.uk/history-and-civilisation/2020/10/secrets-and-spies-behind-the-doors-of-the-uks-most-enigmatic)

> Abrutat explains the value of history in educating the public about GCHQ’s role in national security. Occasionally he and his staff offer tours of the museum to schoolchildren and VIPs. He’s also collaborating with an author on an official history of the agency, due to be published in October 2020. 
> 
> “It’s all about selling us as an organisation, and recruiting the next generation of analysts, linguists and cyber ninjas,” he says. 
> 
> But history is also vital in educating today’s new recruits. For that reason Abrutat documents previous GCHQ missions, in the hope that current employees might learn vital lessons from them. 
> 
> “We’re not very good at learning lessons; most organisations aren't,” he says. “But having a corporate record of why we made a [certain] decision in 1977 or 1984 – you can use that to educate future management and leadership; so as not to trip up again.”


How much do we value the organisational history that surrounds us?  Not many organisations have a storied enough history to have their own historians, but everyone needs some mechanisms to retain decisions and experiences, because while [history doesn’t repeat, it does rhyme](https://quoteinvestigator.com/2014/01/12/history-rhymes/)


## [Falsehoods programmers believe about time zones](https://www.zainrizvi.io/blog/falsehoods-programmers-believe-about-time-zones/)

[https://www.zainrizvi.io/blog/falsehoods-programmers-believe-about-time-zones/](https://www.zainrizvi.io/blog/falsehoods-programmers-believe-about-time-zones/)

> I knew trying to manage time is a fool's errand, but that's what datetime libraries are for. I would merely build an extra time zone conversion layer on top.
> 
> Surely that couldn't be complicated
> 
> ...Right?
> 
> I soon discovered just how wrong I was. One after another, I kept learning the falsehood of yet another "fact" that had seemed obviously true. Eventually my original vision became literally impossible to pull off without making serious compromises (more about that in a future blog post).
> 
> Hopefully this list will help you avoid the landmines I stepped on. All the falsehoods below are ones I'd considered true at some point in my adult life.
> 
> Most of them I believed just one month ago.


Time and Dates are hard, Timezones even more so.


## [How I Found An alg=none JWT Vulnerability in the NHS Contact Tracing App | zofrex.com](https://www.zofrex.com/blog/2020/10/20/alg-none-jwt-nhs-contact-tracing-app/)

[https://www.zofrex.com/blog/2020/10/20/alg-none-jwt-nhs-contact-tracing-app/](https://www.zofrex.com/blog/2020/10/20/alg-none-jwt-nhs-contact-tracing-app/)

> The point of a library is to make doing something easier.
> 
> Why does this even need to be said?
> 
> How has this library failed its users so catastrophically?
> 
> This is a case where a competent engineering team (I’ve read enough of their code - they know what they’re doing) sat down, apparently aware of the pitfalls of JWTs, and tried to avoid them. They set the algorithm, they required a key. They knew these things about the underlying thing they were doing – far more than users of a library should need to know in order to use it safely – and yet they still shot themselves in the foot. How do people who don’t know these things stand a chance?
> 
> And if your library isn’t helping users to do the right thing then why does it even exist?
> 
> Why was a JWT with alg=none and kid set not rejected out of hand for being obviously ridiculous?


This reminded me strongly of [this academic article](https://ieeexplore.ieee.org/document/7676144) from Matthew Green and Matthew Smith about the fact that cryptographic API's are often hard to use correctly


## [Abusing pipelines to hijack production](https://flangvik.com/azure/devops/privesc/abuse/2020/10/15/from-pipeline-to-production.html)

[https://flangvik.com/azure/devops/privesc/abuse/2020/10/15/from-pipeline-to-production.html](https://flangvik.com/azure/devops/privesc/abuse/2020/10/15/from-pipeline-to-production.html)

> However, the root cause of this issue is the the bad-practiced and often rushed setup and configuration of pipelines within DevOps. Users having write access to all pipelines, all pipelines having access to all Azure Service Connections, and so forth.
> When creating a new service connection, the potentially dangerous “All Access” permission is even set by default! Be sure to uncheck this!


This configuration is set by default and yet allows all your developers more or less unfettered access to production.
The only thing I’ll add is that this sort of modification within Azure DevOps is well audited, so if anyone is looking at the log events, the attacker should be noticed, and everyone is watching their build server logs right?


