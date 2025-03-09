---
title: "29 - When is risk management not risk management?"
date: 2018-12-11
description: "A theme I've seen recently is a reluctance by organisations to take certain actions to reduce risk because they either aren't perfect, they don't totally remove the risk, or they contain too many unknowns."
permalink: /when-is-risk-management-not-risk-management/
---

A theme I've seen recently is a reluctance by organisations to take certain actions to reduce risk because they either aren't perfect, they don't totally remove the risk, or they contain too many unknowns.

I've spent a fair amount of time looking at legacy system risk documents and noting just how much existing risk organisations are carrying with existing systems.  But for building a new system, often times the risk management process insists on a perfect implementation of security features and total risk reduction.

We need to remember that risk is acceptable.  Organisations succeed and fail based on their ability to desire to take risks to outperform their competitors.  Government doesn't need to perform in a market, but Government organistations operate in a highly complex and ambiguous environemnt, with the average term of a minister being around 18 months, the desires of the organisation changes on a regular basis.

Risk management should be about taking advised risks, and know what your outstanding risk debt is.  It's about knowing and recording your risks and going ahead anyway.  It's about having a plan to improve that once you know more, once you have a thing that works and real customers and it's worth the effort to fix properly.

Even ISO27001 ISMS systems talk about nonconformant systems and continual improvement, but rarely have I actually seen a mitigation plan put in place that will continuously improve the risk posture of something.  Instead we rely on people making sensible decisions inside programs to do this for us.

That said, we also focus often on the wrong things.  We spend a lot of time concentrating on firewalls and preventing users from having admin privileges, and stopping users from accessing modern tools like slack (Or maybe that's just in Government), but we still can't patch desktop machines within a few hours, know the state our servers should be in, or let our users use memorable complex passphrases instead of P@ssword1.

We can't build a perfect system in advance of every possible risk or concern, and we shouldn't be trying, instead we need to do the simple things that we know work, and then build on top of those foundations.

## [Adobe Flash Zero-Day Leveraged Via Office Docs in Campaign | Threatpost | The first stop for security news](https://threatpost.com/adobe-flash-zero-day-leveraged-via-office-docs-in-campaign/139635/)

[https://threatpost.com/adobe-flash-zero-day-leveraged-via-office-docs-in-campaign/139635/](https://threatpost.com/adobe-flash-zero-day-leveraged-via-office-docs-in-campaign/139635/)

> An Adobe Flash Player zero-day exploit has been spotted in the wild as part of a widespread campaign, researchers said on Wednesday.
> 
> Adobe has just issued a patch for the previously unknown critical flaw.
> 
> The vulnerability, CVE-2018-15982, is a use-after-free flaw enabling arbitrary code execution in Flash. Researchers with Gigamon Applied Threat Research said the zero-day in Flash was being exploited via a Microsoft Office document dubbed “22.docx.”
> 
> Researchers said the document was submitted to VirusTotal from a Ukranian IP address, and purports to be an employment application for a Russian state healthcare clinic, containing seven pages of personal questions that would typically be part of that kind of application.


The timeline here is that the flaw was publicly revealed and a patch released on the 5th December, and within 12 hours was being seen used in real attacks.

The proof of concept was [pushed to github by prsecurity](https://github.com/prsecurity/CVE-2018-15982), and it was [almost immediately detected being bundled into other phishing exploits](https://sysopfb.github.io/malware/2018/12/07/CobaltGroup-abusing-15982.html)

It looks like the flaw might have been known to Hacking Team, and that the discovery came from people looking through the public dump of their tools from a few years ago.

I hope you can patch your desktop estates within 12 hours, because that's table stakes now.


## [NCSC Advisory: The rise of O365 compromise and how to mitigate [PDF]](https://www.ncsc.gov.uk/content/files/protected_files/article_files/O365%20Compromise%20and%20mitigation%20advice.pdf)

[https://www.ncsc.gov.uk/content/files/protected_files/article_files/O365%20Compromise%20and%20mitigation%20advice.pdf](https://www.ncsc.gov.uk/content/files/protected_files/article_files/O365%20Compromise%20and%20mitigation%20advice.pdf)

> The NCSC is aware of several incidents involving the compromise of O365 accounts within the UK, including the use of such methods in targeted supply chain attacks. The ultimate objective of this type of targeting is not clear and the attacks appear not to be limited to any particular sector or attributed to any single threat actor.
> 
> [...]
> 
> The impact of an O365 account compromise can vary in severity depending on an actor’s objectives. Once an actor has obtained credentials for an O365 account, not only can the account access be used to access documents across a user’s O365 surface (SharePoint, OneNote etc.) but it can also be used as a launchpad to carry out further compromises within an organisation.


This mentions supply chain targeting but doesn't go into details.  I'm guessing that this means starting a attack from a compromised member of your supply chain (which is backed up by information I've seen reported on twitter).  The way this currently reads could be read as NCSC warning that Microsoft and Office 365 has been compromised in certain cases, but I suspect that this is highly unlikely and I hope NCSC clarifies that paragraph.

The advice here is to turn on MFA, and there's a note to say that some users might struggle with MFA.  From personal experience, a lot of security people view this as black and white, either turn on a single MFA option that can be used by everyone, or don't do it at all.  In reality you should turn it on for as many people as possible.  If some of your userbase cannot use MFA, for example if they don't have work mobile phones, then exclude them and just get it turned on for everyone else first, and then come back to solve that problem after.  Patchy coverage of MFA is still massively lower risk than no coverage of MFA.


## [Ericsson apologises for O2 network outage | Computing](https://www.computing.co.uk/ctg/news/3067847/ericsson-apologises-for-o2-network-outage)

[https://www.computing.co.uk/ctg/news/3067847/ericsson-apologises-for-o2-network-outage](https://www.computing.co.uk/ctg/news/3067847/ericsson-apologises-for-o2-network-outage)

> Ericsson, which manufactures much of the equipment used in modern cellular networks, says that the fault was due to an expired software certificate in a version of its management software.
> 
> The company said, ‘During December 6, 2018, Ericsson...identified an issue in certain nodes in the core network resulting in network disturbances for a limited number of customers in multiple countries using two specific software versions of the SGSN-MME (Serving GPRS Support Node - Mobility Management Entity).'
> 
> It added, ‘An initial root cause analysis indicates that the main issue was an expired certificate in the software versions installed with these customers. A complete and comprehensive root cause analysis is still in progress. Our focus is now on solving the immediate issues.'


This was quite the outage, but expired certificates is a real issue.

[As parodied on twitter](https://twitter.com/spazef0rze/status/1070732430649294849) in reality, building auto renewing certificate management isn't that hard.  For websites, LetsEncrypt does it, but that uses the ACME protocol which you should be able to implement on your internal certificates if you run your own certificate authority.

But the effort of doing that, while it has massive future savings, is a high initial cost compared to "just renewing this certificate the once" and so we continue with sites having to scramble every year to renew their certificates.


## [Downsides of DevOps](https://www.business2community.com/strategy/downsides-of-devops-02140033)

[https://www.business2community.com/strategy/downsides-of-devops-02140033](https://www.business2community.com/strategy/downsides-of-devops-02140033)

> It is great to have a continuous deployment train that can automatically push new features in production. It is not so great to read customer feedback telling us they are exhausted with learning new features every other month. Who would have thought! We were so happy to push features, automate our deployment process to speed up things that we completely forgot about the customer at the end of the production line.
> 
> I define User fatigue as customers who can’t keep up with new features. Features roll out just to frequently for a user to discover and adapt them to their current ways of working with the software.


Repeat after me, software deployment is not the same as feature deployment.

If you need to do a deploy of your software to turn on or off a feature, then you are missing a vital trick.  You should be deploying software multiple times per day because it enables continous delivery of bug fixes, performance tweaks and software patches that don't fundementally alter the feature set that the customer uses.

If you equate software deployment with feature release, you won't need to deploy frequently (because of precisely the problem of user fatigue) and so you won't be as easily able to deploy that critical security patch when you need to.


## [Inside China's audacious global propaganda campaign | News | The Guardian](https://www.theguardian.com/news/2018/dec/07/china-plan-for-global-media-dominance-propaganda-xi-jinping)

[https://www.theguardian.com/news/2018/dec/07/china-plan-for-global-media-dominance-propaganda-xi-jinping](https://www.theguardian.com/news/2018/dec/07/china-plan-for-global-media-dominance-propaganda-xi-jinping)

> Since 2003, when revisions were made to an official document outlining the political goals of the People’s Liberation Army, so-called “media warfare” has been an explicit part of Beijing’s military strategy. The aim is to influence public opinion overseas in order to nudge foreign governments into making policies favourable towards China’s Communist party.


This is an interesting discussion.  What's the difference between propaganda and state communications?  How does this differ from the Britain is Great campaign by the UK to get international companies and states to buy british products?

I think the real story here is similar to the one I posted a few weeks ago about the militirsation of influence operations on the internet.  The internet is a new military arena for operations, and states and countries are realising that they need to up their game on it.

One of the big differences between the internet and the physical world for information operations is that it's much less common for people to check the source of information online.  Is this website reputable tends to be answered by looking to see if the website looks professional, rather than anything else.  The cost to setup a professional looking news site is minimal, and there is such a long tail of publishers that it's hard to know which are real or not.


## [Widely used open source software contained bitcoin-stealing backdoor | Ars Technica](https://arstechnica.com/information-technology/2018/11/hacker-backdoors-widely-used-open-source-software-to-steal-bitcoin/)

[https://arstechnica.com/information-technology/2018/11/hacker-backdoors-widely-used-open-source-software-to-steal-bitcoin/](https://arstechnica.com/information-technology/2018/11/hacker-backdoors-widely-used-open-source-software-to-steal-bitcoin/)

> According to the Github discussion that exposed the backdoor, the longtime event-stream developer no longer had time to provide updates. So several months ago, he accepted the help of an unknown developer. The new developer took care to keep the backdoor from being discovered. Besides being gradually implemented in stages, it also narrowly targeted only the Copay wallet app. The malicious code was also hard to spot because the flatmap-stream module was encrypted.


This was a devious, and well executed supply chain attack.  
I think we are going to see these divide into two categories:
1. Attacking the supply chain indiscrinimately, just trying to get as much as possible.  These will be noisy, caught quickly, but like Phishing scams, a 0.001% success rate can work if there are millions of targets
2. Attacking the supply chain is a highly targeted way.  These backdoors will remain silent and well hidden until the attacker needs them.


## [The Paradox of Scale – David Carboni – Medium](https://medium.com/@davidcarboni/the-paradox-of-scale-c0c6546c8c61?_referrer=twitter)

[https://medium.com/@davidcarboni/the-paradox-of-scale-c0c6546c8c61?_referrer=twitter](https://medium.com/@davidcarboni/the-paradox-of-scale-c0c6546c8c61?_referrer=twitter)

>  spend plenty of my time in conversations about microservices. API design, infrastructure, operations, architecture. If you’ve been there, you’ll have heard phrases like scheduling, circuit breakers, service discovery, distributed tracing, health checks, cenralised logging, mutual authentication, rolling deployments, traffic splitting, the list goes on.
> 
> When you consider that each of those can easily balloon into a couple of months of work, especially when they come “for free out-of-the-box”, a spot of arithmetic will tell you you could be looking at two years of peripheral work before you even think about the thing you’re actually trying to build.
> 
> Do you have a million users and a billion transactions? And do you have them today? Or are you just starting out with a new product? It’s easy to assume this stuff is critical to running production-quality systems and, you know what, it might be, but more likely it isn’t right now.
> 
> The question is not “whether”, but “when” these things are useful
> Paradoxically, trying to build it all — to emulate our heroes on day one — is more likely to be disastrous.


This is a useful reminder that we need to ask ourselves when to build features that "everyone" has, but also not to judge organisations and products just because they aren't doing everything right. 

It's often more efficient, at first, to do things manually and not worry about solving the problems that you know will come down the road, because those problems aren't there yet.


## [How Anna Delvey Tricked New York’s Party People](https://www.thecut.com/2018/05/how-anna-delvey-tricked-new-york.html?utm_source=tw&utm_medium=s3&utm_campaign=sharebutton-b)

[https://www.thecut.com/2018/05/how-anna-delvey-tricked-new-york.html?utm_source=tw&utm_medium=s3&utm_campaign=sharebutton-b](https://www.thecut.com/2018/05/how-anna-delvey-tricked-new-york.html?utm_source=tw&utm_medium=s3&utm_campaign=sharebutton-b)

> The following January, Anna hired a PR firm to put together a birthday party at one of her favorite restaurants, Sadelle’s in Soho. “It was a lot of very cool, very successful people,” said Huang, who, while aware Anna owed him money for their Venice trip, remained mostly unconcerned about it, at least until the restaurant, having seen Polaroids of Huang and Anna at the party on Instagram, messaged him a few days later. “They were like, ‘Do you have her contact info?’ ” he says now. “ ‘Because she didn’t pay her bill.’ Then I realized, Oh my God, she is not legit.”
> 
> As Anna bounced around the globe, there was some speculation as to where her means to do this came from, though no one seemed to care that much so long as the bills got paid.
> 
> “I thought she had family money,” said Jayma Cardoso, one of the owners of the Surf Lodge in Montauk. Delvey’s father was a diplomat to Russia, one friend was sure. No, another insisted, he was an oil-industry titan. “As far as I knew, her family was the Delvey family that is big in antiques in Germany,” said another acquaintance, a millionaire tech CEO. (It is unclear what family he was referring to.) 


This is a wonderful long read on a scammer living it up and mostly managing to pull it off.  A reminder that everybody is capable of being duped, and that people generally want to believe whats in front of them rather than that they might be being duped


