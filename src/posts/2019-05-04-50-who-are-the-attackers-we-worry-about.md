---
title: "50 - Who are the attackers we worry about"
date: 2019-05-04
description: "The old adage says that on the internet, nobody knows you are a dog.  It's always been hard to attribute cyber attacks because of the complexities of internet governance means that country location of servers isn't the same as commercial affiliation of the owner, who might be selling to organisations in yet another country."
permalink: /who-are-the-attackers-we-worry-about/
---

The old adage says that on the internet, nobody knows you are a dog.  It's always been hard to attribute cyber attacks because of the complexities of internet governance means that country location of servers isn't the same as commercial affiliation of the owner, who might be selling to organisations in yet another country.

In general, when we worry about Advanced Persistent Threats in the UK and US, it's the same four countries that get named each time.  The countries that the 5-eyes intelligence countries named and indicted a few months ago, and the ones that have been most publically attributed for a number of damaging campaigns.  But that also paints a big target on those organisations backs.  They're the most studied, and you can get "Techniques, Tools and Procedures" descriptions for various groups operating out of Iran, China, Russia and North Korea, meaning that if you are a small operating team in a much smaller country, it is probably worth while trying to emulate those TTP's as much as possible.  Everyone is happy and willling to believe that attacks came from those organisations anyway and probably won't dig much further.

But small hacking organisations, whether criminal in nature, single issue motivated groups or loose hacker collectives, are all growing in capability, and sad to say, but attacking capability is becoming more accessible to amateurs far faster than defensive capability is being made available to the rest of us.  This means that we are going to see more and more increases in the number and type of attacks that are of growing complexity.

On the positive side, if everyone is being hit by the same high complexity attacks, that makes the use of threat intelligence, information sharing and indicators of compromise far more useful, so the value of those as defensive tools will also grow at the same time.

I think my view was best summed up by [this tweet this week](https://twitter.com/pmelson/status/864866972839837698).  What matters most is not who attacked you or what country flag they were flying, real or false, but whether you were able to detect and stop the attack before it caused damage

## [Plan to secure internet of things with new law - BBC News](https://www.bbc.co.uk/news/technology-48106582)

[https://www.bbc.co.uk/news/technology-48106582](https://www.bbc.co.uk/news/technology-48106582)

> The proposed legislation, launched by Digital Minister Margot James, would also introduce a new labelling system to tell customers how secure an IOT product is.
> 
> Ms James said it was part of the UK's bid to be a "global leader in online safety".
> 
> Retailers would eventually be barred from selling products without the labels although initially the scheme would be voluntary.
> 
> To gain a label and enter the market, IOT devices would have to:
> * come with unique passwords by default
> * state clearly for how long security updates would be made available
> * offer a public point of contact to whom any cyber-security vulnerabilities may be disclosed


There’s a lot of good ideas in this.  I think there’s some danger in assuming that these are the only features that improve the security of an IoT device, but these are some critical beginning steps that will definitely improve the security of your average device.  Whether there is any appetite for the regulation is still to be seen, and of course, you should go and register your opinions in [the consultation](https://www.gov.uk/government/consultations/consultation-on-regulatory-proposals-on-consumer-iot-security)


## [The inception bar: a new phishing method](https://jameshfisher.com/2019/04/27/the-inception-bar-a-new-phishing-method/)

[https://jameshfisher.com/2019/04/27/the-inception-bar-a-new-phishing-method/](https://jameshfisher.com/2019/04/27/the-inception-bar-a-new-phishing-method/)

> Welcome to HSBC, the world’s seventh-largest bank! Of course, the page you’re reading isn’t actually hosted on hsbc.com; it’s hosted on jameshfisher.com. But when you visit this page on Chrome for mobile and scroll a little way, the page is able to display itself as hsbc.com - and worse, the page is able to jail you in this fake browser! In this post I show how the attack works, then suggest some ways Chrome can fix this vulnerability, then finally show you how to get out if you’re still stuck here.


This is a cute attack.  By drawing something that looks like the address bar, in the place where an address bar should be, but is hidden for space, it means that you can give users confidence that your page is some other domain.

What’s interesting about this, is that it’s mostly a security problem combined with a usability problem.  It’s not a typical, security makes something less usable, but more than in order to be usable, to free up screen space, something that users use for security must be hidden or removed, and that is hard to reason about or make decisions about.


## [News & Workshops - Release of draft knowledge areas for public consultation](https://www.cybok.org/news/release-of-draft-knowledge)

[https://www.cybok.org/news/release-of-draft-knowledge](https://www.cybok.org/news/release-of-draft-knowledge)

> We are pleased to announce the release of further knowledge areas Adversarial Behaviours and Secure Software Lifecycle for public review. These knowledge areas will be open for public release for a 4-week period until Wednesday 15 May 2019.


I have some issues with the Cyber Security Body of Knowledge project, primarily that it is a very academic endeavour to attempt to document terms that we use in cyber security that have been well studied academically.  Of course much of the field of cyber security has not been well studied academically, so this has varying results.

The Secure Software Lifecycle document reads exactly like a set of academics that are not involved in professional software development, writing about theoretical mechanisms by which software development can be secured.  It’s dry and generally irrelevant to my experience of software development teams in agile modern development teams.

The adversarial behaviours one however is far more interesting to me, because instead of computer science papers studying programming languages, it’s referencing sociology, psychology, criminology and various other social sciences.  More importantly, it gives a good overview of a variety of attacks, criminal intent behind them and some language that we can use to be consistent about those attackers.


## [Government as a Platform, the hard problems: part 3 – shared components and APIs](https://medium.com/platform-land/government-as-a-platform-the-hard-problems-part-3-shared-components-and-apis-9c87dba83e66)

[https://medium.com/platform-land/government-as-a-platform-the-hard-problems-part-3-shared-components-and-apis-9c87dba83e66](https://medium.com/platform-land/government-as-a-platform-the-hard-problems-part-3-shared-components-and-apis-9c87dba83e66)

> Today, national and local governments operate multiple payment gateways, hosting setups, and other systems. Local governments often operate functionally similar legacy systems to each other, for managing things like planning applications, or health and safety inspections. Each of these systems needs actively maintaining and protecting against security, data protection and other risks.
> 
> Shared components could represent an opportunity of better responding to such threats. However, the dependencies that shared components and APIs create could lead to new risks too.


Generally, Richard Pope’s platform land series of blog posts about is excellent.  Richard is a great thinker and these posts have all been very inspirational and made me think.  However, I think his security thinking here is a little wrong.  One of the biggest issues for platform providers is not whether their platform is secure, it’s the problem of “secure against what” and “how to prove it’s secure”.

Different organisations that take payments have very different threat models.  One organisation might be subject to small payments, and only minor fraudsters and criminals are interested in attacking it.  Certain types of attack are computationally and economically unfeasible for that payments service.  But let’s say you start allowing house purchases to be made, and you can now take payments in the tens or hundreds of thousands of pounds.  As a platform provider, what is your threat model, is it the aggregate of all your consumers, and how does it change as you onboard each new consumer.

Secondly, it’s increasingly hard to give good transitive assurances for the security of any platform play.  Primarily because we lack the language, but also because it’s so easy to make false statements about the security of a system and never be caught out for it.  This means that you need an effective security assurance process that can relied upon in order to build a good platform.  People are either not willing to accept your assurances, or far too willing to accept them.

Anyway, lots of good thoughts from this blogpost and the entire series, well worth watching.


## [Identity proofing and verification of an individual - GOV.UK](https://www.gov.uk/government/publications/identity-proofing-and-verification-of-an-individual/identity-proofing-and-verification-of-an-individual)

[https://www.gov.uk/government/publications/identity-proofing-and-verification-of-an-individual/identity-proofing-and-verification-of-an-individual](https://www.gov.uk/government/publications/identity-proofing-and-verification-of-an-individual/identity-proofing-and-verification-of-an-individual)

> You should read this guidance to help you decide how you or your service will check someone’s identity.
> 
> You can use this guidance to work out which process you could use to check the identity of a customer, employee, or someone acting on behalf of a business.


Good Practice Guide 45 was first written in 2014, and was a guide for trying to understand how you can verify someone’s identity online.  This updated version is significantly easier to read, and given this is a complex topic, it lays it all out very well, and very clearly.

It’s important to remember that authentication of a user is not the same as verifying an online identity against a claimed physical identity, and this guide not only shows you the different sorts of proofs you might need, but also some profiles that you can use based on your identity proofing requirements.


## [Online Harms White Paper - GOV.UK](https://www.gov.uk/government/consultations/online-harms-white-paper)

[https://www.gov.uk/government/consultations/online-harms-white-paper](https://www.gov.uk/government/consultations/online-harms-white-paper)

> The White Paper proposes establishing in law a new duty of care towards users, which will be overseen by an independent regulator. Companies will be held to account for tackling a comprehensive set of online harms, ranging from illegal activity and content to behaviours which are harmful but not necessarily illegal.


What's not entirely clear from this is what we actually consider to be a harm, or rather the framework for answering the question about why this harm and not another.


## [Operation ShadowHammer: A High Profile Supply Chain Attack | Securelist](https://securelist.com/operation-shadowhammer-a-high-profile-supply-chain-attack/90380/)

[https://securelist.com/operation-shadowhammer-a-high-profile-supply-chain-attack/90380/](https://securelist.com/operation-shadowhammer-a-high-profile-supply-chain-attack/90380/)

> The code injection happened through modification of commonly used functions such as CRT (C runtime), which is similar to ASUS case. However, the implementation is very different in the case of the videogame companies. In the ASUS case, the attackers only tampered with a compiled ASUS binary from 2015 and injected additional code. In the other cases, the binaries were recent (from the end of 2018). The malicious code was not inserted as a resource, neither did it overwrite the unused zero-filled space inside the programs. Instead, it seems to have been neatly compiled into the program, and in most cases, it starts at the beginning of the code section as if it had been added even before the legitimate code. Even the data with the encrypted payload is stored inside this code section. This indicates that the attackers either had access to the source code of the victim’s projects or injected malware on the premises of the breached companies at the time of project compilation.
> 
> [...]
> 
> In late 2018, we found a suspicious sample of the link.exe tool uploaded to a public malware scanning service. The tool is part of Microsoft Visual Studio, a popular integrated development environment (IDE) used for creating applications for Microsoft Windows. The same user also uploaded digitally signed compromised executables and some of the backdoors used in the same campaign.
> 
> The attack is comprised of an infected Microsoft Incremental Linker, a malicious DLL module that gets loaded through the compromised linker. The malicious DLL then hooks the file open operation and redirects attempts to open a commonly used C++ runtime library during the process of static linking. The redirect destination is a malicious .lib file, which gets linked with the target software instead of the legitimate library. The code also carefully checks which executable is being linked and applies file redirection only if the name matches the hardcoded target file name.


I had missed this bit about these attacks the first time I read the Shadow Hammer writeups.  I saw some minor reporting on this and was all "third rate video game got hacked, meh".

But actually there was an [interesting article by Graham Cluley](https://www.tripwire.com/state-of-security/featured/operation-shadowhammer-hackers-planted-malware-code-video-games/)  that sent me back to this to double check what I'd read.

This attack didn't just attack the infrastructure, stealing the signing certificates and then producing their own forged updates that contained malware.  They actually infected Visual Studio, the developers tooling that compiles the real updates.  This form of "supply chain attack", attacking development tools themselves has been long theorised.  There's an [excellent paper on this idea by Ken Thompson](https://www.archive.ece.cmu.edu/~ganger/712.fall02/papers/p761-thompson.pdf), one of the creators of Unix in 1984 that talks about how one cannot ever really trust compiler because it can modify the code you wrote, but this appears to be an actual, in real world, form of this attack.


## [Huawei, hacking, and the stench of western hypocrisy | Prospect Magazine](https://www.prospectmagazine.co.uk/magazine/huawei-hacking-and-the-stench-of-western-hypocrisy)

[https://www.prospectmagazine.co.uk/magazine/huawei-hacking-and-the-stench-of-western-hypocrisy](https://www.prospectmagazine.co.uk/magazine/huawei-hacking-and-the-stench-of-western-hypocrisy)

> The other charge against Huawei is that it is not independent of the Chinese state. But the US tech and communications companies are not entirely independent of the US government. The Prism programme, revealed by Snowden, showed how big communications companies handed over private data to the NSA. The companies insisted they legally had to comply.


There’s a whole bunch of various claims of the typical sort in here, but I thought this was an interesting side note in the article.
I’ve covered this previously around the debate around legal interception technologies.  Almost everyone agrees that there are cases where legal interception is necessary, but the biggest problems for everyone is trying to define under what circumstances we think it’s appropriate.
The hardest part of this debate is working out what countries legal systems we determine are sufficiently strong that we’ll recognise their ability to engage in international legal intercept programs.


## [Vodafone Found Hidden Backdoors in Huawei Equipment - Bloomberg](https://www.bloomberg.com/news/articles/2019-04-30/vodafone-found-hidden-backdoors-in-huawei-equipment)

[https://www.bloomberg.com/news/articles/2019-04-30/vodafone-found-hidden-backdoors-in-huawei-equipment](https://www.bloomberg.com/news/articles/2019-04-30/vodafone-found-hidden-backdoors-in-huawei-equipment)

> In a statement to Bloomberg, Vodafone said it found vulnerabilities with the routers in Italy in 2011 and worked with Huawei to resolve the issues that year. There was no evidence of any data being compromised, it said. The carrier also identified vulnerabilities with the Huawei-supplied broadband network gateways in Italy in 2012 and said those were resolved the same year. Vodafone also said it found records that showed vulnerabilities in several Huawei products related to optical service nodes. It didn’t provide specific dates and said the issues were resolved. It said it couldn't find evidence of historical vulnerabilities in routers or broadband network gateways beyond Italy.


This is an interesting story.  We remember that Bloomberg reported the Super Micro story back in October, which was widely regarded as flawed reporting.  Original reports on this story felt like the same form of reporting, that they had found a minor and understandable flaw and combined it with misunderstood or misapplied background information.  Leaving an open telnet port could be a black door, or it could be a perfectly normal debugging tool, it’s difficult to tell.
However, since then, despite strenuous denials from Vodafone, Bloomberg has updated this story with far more details, which might imply some negative behaviour from Huawei.  But it could also be fairly typical and normal big supplier behaviour.  Trying to hide your mistakes and errors, then blaming them on regulations and rules that prevent a change.

For me, I think the initial reporting being so vociferously denied by Vodafone combined with the Super Micro story means that I think this is poor journalism that is fishing for a story and putting together pieces of evidence in a “no smoke without fire” view.  It’s one that reading the story I can sympathise with, but I don’t really believe is evidence of malfeasance rather than incompetence.


## [Slack Warns Investors It's a Target for Nation-State Hacking - Motherboard](https://motherboard.vice.com/en_us/article/pajbj8/slack-warns-investors-its-a-target-for-nation-state-hacking)

[https://motherboard.vice.com/en_us/article/pajbj8/slack-warns-investors-its-a-target-for-nation-state-hacking](https://motherboard.vice.com/en_us/article/pajbj8/slack-warns-investors-its-a-target-for-nation-state-hacking)

> The document says that these threats from organized crime and nation-states actors and affiliates are alongside “threats from traditional computer ‘hackers;’ malicious code (such as malware, viruses, worms, and ransomware), employee theft or misuse, password spraying, phishing, credential stuffing, and denial-of-service attacks.” These threats are impossible to entirely mitigate, according to the document.
> 
> The S-1 filing does not claim that an attack from organized crime, nation-state, or nation-state affiliate actually happened. Rather, it just says that threats from these actors present an active risk to the company


I kind of think that this is going to become fairly normal declarations for anybody playing the platform game.  Naturally any platform is a potential target for nation state hackers, and with more and more states joining the cyber capable nations with “offensive cyber teams”, the more that platforms will be targeted by at least one nation state level actor.

It’s nice to know that people are considering this in their attack model, are being explicit about it, and are open about the fact that they are impossible to entirely mitigate.


## [Going Toe-to-Toe With Ukraine’s Separatist Hackers – Foreign Policy](https://foreignpolicy.com/2019/05/01/going-toe-to-toe-with-ukraines-separatist-hackers-cyber-russia/)

[https://foreignpolicy.com/2019/05/01/going-toe-to-toe-with-ukraines-separatist-hackers-cyber-russia/](https://foreignpolicy.com/2019/05/01/going-toe-to-toe-with-ukraines-separatist-hackers-cyber-russia/)

> The conversation was detailed in a report released last month by the U.S. cybersecurity firm FireEye exposing the hacking operation as part of a campaign being run by operatives working on behalf of the Luhansk People’s Republic, one of the breakaway republics in Eastern Ukraine backed by Moscow, that used both custom-written malware and publicly available spy software to target Ukrainian government ministries for espionage.
> 
> The Luhansk hacker cornered last year failed to hit his target, but the campaign that it was a part of illustrates how cyberespionage operations that were once the domain of well-funded intelligence agencies have now trickled down to even semi-autonomous regions fighting for independence. The proliferation of these weapons allows individual hackers and their confederates to carry out intelligence operations for their pseudo-governments.


How much does it cost to build a "nation state" level offensive cyber program?  I don't think it's that expensive anymore.  The constant leaking of tools, the sharing of doctorinal practice means that the years of preparation are less important than they used to be.  Instead we can be talking employing expensive security consultants in small teams to build out the core teams for an offensive program.

Sure it's still quite hard to reach the capabilities of the top nations, and a small nation wouldn't have the breadth or the depth of the top teams, but it's not beyond the reach of many small countries.  We in the UK still worry about the list of hostile countries, Russia, China, Iran, North Korea, but who else is going to join that list, and what motivations will they have when they do?


