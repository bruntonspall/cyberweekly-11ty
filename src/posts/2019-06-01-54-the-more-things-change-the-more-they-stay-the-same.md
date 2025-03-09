---
title: "54 - The more things change, the more they stay the same"
date: 2019-06-01
description: "Iran's conducting disinformation campaigns, Baltimore shows that people aren't patching at all, let alone fast enough, the Huawei discussion rages on."
permalink: /the-more-things-change-the-more-they-stay-the-same/
---

Iran's conducting disinformation campaigns, Baltimore shows that people aren't patching at all, let alone fast enough, the Huawei discussion rages on.

This is the new normal, and looking down the behaviors of nation states, at the data breach report a few weeks ago, and at all of the information that's coming out, we can see that behind every sensationalist headline is the same stuff really.

Nation states have been hacking each other, and their adversaries commercial organisations for decades.  I've been watching The Americans, as I missed it originally, and the amount of independent organisations that the russian spies break into and damage in order to carry out their mission (set in the height of the cold war) is astonishing. But we know that this has been happening for a long time, it's not really news that it's happening.  What's different now is the scale at which it happens, but also the assymetry in cyberwarfare.  Organisations like the US have highly advanced cyber offensive capabilities, but across the nation, not just at the Government level, but in the critical industries and businesses, the defensive capability is so low.

What can we do about it?  While I've got some issues with NCSC's anti patterns document, there's a lot of good in there, in attempting to bust some myths of the past, and show that there are good ways to build new systems.  My biggest worry is all of the legacy IT systems out there, built over the last 40 years, that is hard to patch, hard to fix the security vulnerabilities.  There's only 2 real strategies that you can operate on for a cyber defensive strategy. The first is to focus on improving that legacy estate, protecting it, detecting attempts to get in, and reducing the blast radius when it does get compromised.  The second is to focus on the new stuff you are building, and ensure that tomorrows legacy is in a better state than today's.  You can't focus too much on one, as the other will kill you, so you need to balance your attention between them.

## [The National Guard's cyber escape room -- GCN](https://gcn.com/articles/2019/05/24/cyber-escape-room.aspx)

[https://gcn.com/articles/2019/05/24/cyber-escape-room.aspx](https://gcn.com/articles/2019/05/24/cyber-escape-room.aspx)

> The Massachusetts Army National Guard is building a cyber and network security-themed escape room it can take to schools to get students interested in cybersecurity.
> 
> In November 2018, the guard contracted with Integrated Exhibits Inc. for a full-length trailer complete with two themed challenge rooms, each with seven computers – one mimicking a government office and the other designed to feel like a basement. Each room has a conference table with pop-up workstations, a desk, file cabinet, a wall-mounted touch-screen monitor, white boards and two pictures on the wall, each covering a safe with key-code access.  High-resolution cameras provide video feeds of the entire room. The door has five “locks,” which are actually non-functioning keypad replicas that are connected to a remote computer to change from red to green when unlocked.
> 
> The two challenge rooms are separated by a command room that houses the server and networking equipment and allows officials to assign and monitor challenges in both rooms.
> 
> Each room accommodates seven-member teams who solve five cybersecurity puzzles that deliver clues to physical puzzles that, when solved, unlock the five door locks.  Data and images for the challenges transmit to all screens equally and independently, incorporating and interacting with the trailer environment and physical puzzles.


Now this is a lovely and cute idea.  I want to go play!

People learn through play an awful lot, and this is a great way to get people to understand some of the implications of cyber security, by breaking it, in a fun way.


## [Blockchain Settlement Was Slow, Costly in Trial, Weidmann Says - Bloomberg](https://www.bloomberg.com/news/articles/2019-05-29/blockchain-settlement-was-slow-costly-in-trial-weidmann-says?utm_source=twitter&utm_content=business&cmpid=socialflow-twitter-business&utm_medium=social&utm_campaign=socialflow-organic)

[https://www.bloomberg.com/news/articles/2019-05-29/blockchain-settlement-was-slow-costly-in-trial-weidmann-says?utm_source=twitter&utm_content=business&cmpid=socialflow-twitter-business&utm_medium=social&utm_campaign=socialflow-organic](https://www.bloomberg.com/news/articles/2019-05-29/blockchain-settlement-was-slow-costly-in-trial-weidmann-says?utm_source=twitter&utm_content=business&cmpid=socialflow-twitter-business&utm_medium=social&utm_campaign=socialflow-organic)

> The blockchain solutions did not fare better in every way: the process took a bit longer and resulted in relatively high computational costs,” Weidmann said in Frankfurt on Wednesday. “Similar experiences have been made elsewhere in the financial sector. Despite numerous tests of blockchain-based prototypes, a real breakthrough in application is missing so far.”


So essentially, they tried using a blockchain prototype for one of the key problems that everyone says blockchain should be good for, resolving interbank trades.  And the good news is that it resolved all of the regulatory requirements for audit and transparency, so they produced a working system.  But it proved both slower and more expensive than solving this the traditional way, with central databases and messages flying forwards and backwards.

Distributed ledger technology is interesting and good, but based on this... I wouldn't bet the bank on it.


## [We Need to Build Up ‘Digital Trust’ in Tech | WIRED](https://www.wired.com/story/we-need-to-build-up-digital-trust-in-tech/)

[https://www.wired.com/story/we-need-to-build-up-digital-trust-in-tech/](https://www.wired.com/story/we-need-to-build-up-digital-trust-in-tech/)

> Failures of relational trust are both difficult to recognize and difficult to resolve because they stem from a lack of accountability. If no one is accountable for the problem, it’s hard to find someone to blame and even harder to find someone to fix it. This breakdown in relational trust fuels the current “techlash.”
> 
> This brings us back to the San Francisco facial recognition ban. At least part of the reason such technologies are seen as creepy or dangerous is the belief that they will be used to harm rather than help citizens and consumers. The worry is not that such tech isn’t secure; the worry is that the owners of these technologies build them in order to exert control. This legitimate concern comes from the fact that these technologies seem unaccountable and their uses are not transparent or responsible. In other words, there’s no trust here and no mechanisms for establishing it.
> 
> Unless implementors take digital trust seriously, more technologies will be similarly received. This is where so-called “ethics panels”—meant to advise on the ramifications of new technologies, such as AI—are meant to come in. 


Fascinating reading, and this really resonates with me.  I think that a lot of normal people just don't trust the fundamental technology more than they don't trust the specific implementation.  Some of my friends think that Alexa is creepy and dislike the fact that I have them in the house, but that's not a brand thing about Alexa, it's a generic distrust of technology that listens to you.  
It doesn't matter that they know that she's not listening if the lights aren't on, or that they know that Amazon really doesn't want it to listen to random conversations, they just fundamentally distrust this technological invasion in their life.


## [Security architecture anti-patterns - NCSC](https://www.ncsc.gov.uk/whitepaper/security-architecture-anti-patterns#section_6)

[https://www.ncsc.gov.uk/whitepaper/security-architecture-anti-patterns#section_6](https://www.ncsc.gov.uk/whitepaper/security-architecture-anti-patterns#section_6)

> This security paper describes some common patterns we often see in system designs that you should avoid. We'll unpick the thinking behind them, explain why the patterns are bad, and most importantly, propose better alternatives.
> 
> This paper is aimed at network designers, technical architects and security architects with responsibility for designing systems within large organisations. Technical staff within smaller organisations may also find the content useful.


Anti Patterns are a bit weird.  They tend to exist for a couple of reasons, but two of the most common are because the tools or technology don't allow people to achieve the ivory tower "correct pattern", or sometimes because the ivory tower correct pattern doesn't actually work in the real world.

This list of anti-patterns, and generally I like this list, it's a good set of things that we should stop doing, but some of these are different to others.

People put in place back to back firewalls of different manufacturers purely for security reasons, and normally because of a security architect with a misunderstanding of the threat model or how firewalls are made and operated.  But people don't use Privileged Access Workstations to manage their systems because it doesn't work from an operational perspective.  It doesn't meet their needs, and prevents them from doing their job appropriately.

I think Privileged Access Workstations for admin control is a great idea.  But I've never got anyone who uses them to explain to me what they define as admin, especially in a cloud world.  Can you lock down your AWS console to these PAW's?  How about access to the configuration as code that is deployed to production?

Use them to manage your AD servers, and your exchange servers that are on premise, where the correct pattern works, but not using them isn't necessarily an anti pattern by itself.  


## [Intezer - HiddenWasp Malware Stings Targeted Linux Systems](https://www.intezer.com/blog-hiddenwasp-malware-targeting-linux-systems/)

[https://www.intezer.com/blog-hiddenwasp-malware-targeting-linux-systems/](https://www.intezer.com/blog-hiddenwasp-malware-targeting-linux-systems/)

> The malware is still active and has a zero-detection rate in all major anti-virus systems.
> 
> • Unlike common Linux malware, HiddenWasp is not focused on crypto-mining or DDoS activity. It is a trojan purely used for targeted remote control.
> 
> • Evidence shows in high probability that the malware is used in targeted attacks for victims who are already under the attacker’s control, or have gone through a heavy reconnaissance.
> 
> 


This is interesting, because there isn't a huge amount of linux malware out there.  We tend to worry about our corporate servers, our RDP remote control systems, and our administrative laptops, but so far, actual malware of the implant variety for linux servers is far less common, and therefore much less of a threat.

It doesn't surprise me that this is changing, after all, 2019 is the year of linux on the desktop!  In reality, many organisations who are undergoing cloud or digital transformations are moving to linux for their server estates in teh cloud, and so linux based malware is an inevitability.  Looking at this second stage dropper here, most common "basic" defenses should detect this.  Adding users to the /etc/passwd file should be really rare, and I'd hope you would get a notification either from your continuous integration suite, or from your operational monitoring at a few of these changes.


## [NSA Deflects Blame for Baltimore Ransomware Attack - Nextgov](https://www.nextgov.com/cybersecurity/2019/05/nsa-deflects-blame-baltimore-ransomware-attack/157376/)

[https://www.nextgov.com/cybersecurity/2019/05/nsa-deflects-blame-baltimore-ransomware-attack/157376/](https://www.nextgov.com/cybersecurity/2019/05/nsa-deflects-blame-baltimore-ransomware-attack/157376/)

> On May 7, hackers reportedly used an NSA tool called EternalBlue to freeze thousands of the Baltimore government’s computers. The attack shut down email and disrupted numerous government services, and it could ultimately cost the city more than $18 million to recover.
> 
> EternalBlue, which was stolen during a 2017 breach at NSA, exploited a previously disclosed bug in a Microsoft software package. The company issued a patch for the vulnerability more than two years ago, but because Baltimore never updated its software, the city remained susceptible to the attack.


This one's been bubbling for a few weeks, but because the Baltimore Sun website is inaccessible to people based in Europe, I haven't found something worth linking to yet that sums it up.

Remember that EternalBlue was the name of the NSA tool that exploited MS17-010, the flaw in SMBv1 that Microsoft fixed back in March 2017.  This was the same flaw that was present in the wannacry outbreak, that affected computers all around the world back in May 2017.  The fact that the city of Baltimore has still been hit by ransomware with this exploit in it in 2019 is just unacceptable, and no amount of discussion around the equities process can fix the fact that we are now over 2 years since the patch was released.

Baltimore appears to be trying to shift the blame and say that if the NSA had released the knowledge of this flaw to Microsoft earlier, then they would have been able to patch earlier.  We don't know how long the NSA had known about the SMB flaw, but I don't see that this timeline looks any better no matter how soon Microsoft had released the patch.


## [Council Post: What Businesses Can Learn From The DHS-OMB Assessment Of Federal Agencies' Security Readiness](https://www.forbes.com/sites/forbesbusinessdevelopmentcouncil/2019/05/29/what-businesses-can-learn-from-the-dhs-omb-assessment-of-federal-agencies-security-readiness/#73737efc2728)

[https://www.forbes.com/sites/forbesbusinessdevelopmentcouncil/2019/05/29/what-businesses-can-learn-from-the-dhs-omb-assessment-of-federal-agencies-security-readiness/#73737efc2728](https://www.forbes.com/sites/forbesbusinessdevelopmentcouncil/2019/05/29/what-businesses-can-learn-from-the-dhs-omb-assessment-of-federal-agencies-security-readiness/#73737efc2728)

> Agencies Don’t Know What’s Going On In Their Networks
> 
> The DHS and OMB realized that federal agencies lack both visibility and the ability to minimize the impact of an incident. So they will work with agencies to improve their security operation centers (SOCs). There is a multitude of different tools and techniques that you can use to increase visibility. I find that KISS (Keep it Simple, Stupid) is often the best choice. Complex solutions can also be disruptive and expensive to deploy.


This is an interesting view of this report, but this finding is quite frankly nonsense. 

Departments don't know what's going on in their networks not because they lack a SOC, but because they lack the skills, or even the in house documentation of their networks.  Far too many organizations outsourced the management of their networks and therefore lack the visibility of what they look like and how they are changed.

In the face of that lack of awareness, a SOC is just being setup to fail in most of these cases.


## [Top UK Official Derides Huawei Claiming it has ‘Bad Security’ | Threatpost](https://threatpost.com/top-uk-official-derides-huawei-claiming-it-has-bad-security/145152/)

[https://threatpost.com/top-uk-official-derides-huawei-claiming-it-has-bad-security/145152/](https://threatpost.com/top-uk-official-derides-huawei-claiming-it-has-bad-security/145152/)

> Ian Levy, technical director at the agency, took the stage for the “Policy in the 3G Era” opening session at the show here. Addressing a packed room, including top executives from global telco giants and other communications equipment suppliers, he bluntly said that Huawei is a paragon of “bad security.”
> 
> “[We have a market] where the leader in the market, in terms of market volume, has the security we published in the Oversight report in March,” Levy said from the stage. “We need to fix that.”
> 
> He also mentioned that the number of telecom equipment suppliers has dwindled from at least a dozen as recently as 10 years ago to just five today – Ericsson, Nokia, ZTE and Samsung, in addition to Huawei – contributing to what he termed a “broken” market.
> 
> “Now we have three to five scale vendors across the world,” he noted. “How is that OK?”
> 
> Levy, for his part, concluded with the sentiment that “security is fundamentally broken in the telecoms sector,” but noted that it’s not just a Huawei problem – operators too will have to step up to the plate to acquire the skill set they need to build security into what he said promises to be a much more complex network infrastructure than has been seen before, thanks to the virtualization at the core of the technology


Ignoring the clickbait headline, from what's reported here, what Dr Levy was saying is that security is not a differentiator in a market that is held by a small number of companies.  There are few incentives for these organisations to really make an effort on security, because they trade based on the fact that there isn't much competition and every nation needs telephony equipment.

The final comment, about the infrastructure changing is a good point as well.  I don't know a huge amount about telephony equipment, but my vague understanding is that there is a lot of custom hardware, specially designed racks and that security model is changing towards the use of virtual computers running on cheaper commodity hardware.  That sounds very similar to the challenge faced by many organisations as they move to the cloud, moving from hardware, on-premise, where protection was assumed, to a new cloud operating model creates a whole new threat model, and requires an increase in the security thinking around the product.


## [Network of Social Media Accounts Impersonates U.S. Political Candidates, Leverages U.S. and Israeli Media in Support of Iranian Interests](https://www.fireeye.com/blog/threat-research/2019/05/social-media-network-impersonates-us-political-candidates-supports-iranian-interests.html)

[https://www.fireeye.com/blog/threat-research/2019/05/social-media-network-impersonates-us-political-candidates-supports-iranian-interests.html](https://www.fireeye.com/blog/threat-research/2019/05/social-media-network-impersonates-us-political-candidates-supports-iranian-interests.html)

> Recently, we investigated a network of English-language social media accounts that engaged in inauthentic behavior and misrepresentation and that we assess with low confidence was organized in support of Iranian political interests. In addition to utilizing fake American personas that espoused both progressive and conservative political stances, some accounts impersonated real American individuals, including a handful of Republican political candidates that ran for House of Representatives seats in 2018. Personas in this network have also had material published in U.S. and Israeli media outlets, attempted to lobby journalists to cover specific topics, and appear to have orchestrated audio and video interviews with U.S. and UK-based individuals on political issues. While we have not at this time tied these accounts to the broader influence operation we identified last year, they promoted material in line with Iranian political interests in a manner similar to accounts that we have previously assessed to be of Iranian origin. Most of the accounts in the network appear to have been suspended on or around the evening of 9 May, 2019. 


This is a great report, and again evidence that it's not just Russian disinformation that we need to worry about.  It looks like Iran has been on the case for a few years as well, and it looks like conducting this kind of campaign is reasonably cheap and easy, so we should expect a large number of non nation state actors to be doing this playbook as we step into the next round of elections.

What will it look like when [Bothered About Dungeons and Dragons](https://www.bbc.co.uk/news/magazine-26328105) are able to organise and run this kind of disinformation campaign?  The tools, the plays and the mechanisms are all documented here, and they're here to stay.


## [Nation-State Security: Private Sector Necessity | SecurityWeek.Com](https://www.securityweek.com/nation-state-security-private-sector-necessity)

[https://www.securityweek.com/nation-state-security-private-sector-necessity](https://www.securityweek.com/nation-state-security-private-sector-necessity)

> Nation-state attackers who once could be  identified by a combination of targets, motivations, and tactics no longer fit cleanly into a specific box. Attackers with the backing and sophistication of nation-states are now targeting commercial entities for reasons ranging from financial gains to cultivating economic, social, and political disruption.    


As well as the geo-political undestanding of the threat landscape, we also need to remember that some of those actors are targeting commercial entities for personal gain, or professional gain rather than a specific political gain.

Those actors still need access to large botnets of controlled computers, places that are deniable, that won't be discovered and where htey can store their weapons.  It's easier to hack a box and use it as a weapons cache than to buy server space without any money trail, and nation states that employ freelance or associated organisations to hack for them might not even really know about how they manage this operational capability.

While this says that you might be a target of a nation state attacker, it's worth remembering that their intent might not be quite what you think it is.  They may want to compromise your network, but maybe not to get access to the politically sensitive documents.  They may well be more interested in stealing money, or getting access to your HR system.


## [Geopolitical Cyber Threats and Business Operations - Infosecurity Magazine](https://www.infosecurity-magazine.com/next-gen-infosec/geopolitical-threats-business-1-1/)

[https://www.infosecurity-magazine.com/next-gen-infosec/geopolitical-threats-business-1-1/](https://www.infosecurity-magazine.com/next-gen-infosec/geopolitical-threats-business-1-1/)

> This is evident from a recent global threat 2019 report by Carbon Black, where it was noted that modern cyber-attacks are becoming “increasingly fueled by geopolitical tensions” and that global governments in 2018 experienced an increased cyber-attacks stemming from China, Russia and North Korea. 
> 
> Accordingly, cyber-attacks should no longer be perceived as acts with only technical, financial and legal implications, but also with a clear political, social and cultural dimensions that should be seriously considered in any effective cyber preparedness plan.


What are the geo-political implications of hacks?  As we see the politicization of cyber offense, we also need to remember that some of the biggest hacks in the last decade were carried out by disaffected individuals or loosely organised hacking groups that had no political aim.  The Talk-Talk hack, Anonymous targeting Visa and Mastercard.

Do we jump too quickly to the assumption that an attack that originated from eastern europe has a geo-political angle to it, or do we dismiss that idea too fast?  And what about our defenses and the ability to strike back that several loud proponents keep asking for.  If we allow firms to "hack back", what are the geopolitical implications of those actions?


