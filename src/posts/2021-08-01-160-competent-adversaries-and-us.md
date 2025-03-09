---
title: "160 - Competent adversaries and us"
date: 2021-08-01
description: "I think I've said this before, but we're really not good at visualising or understanding risk."
permalink: /competent-adversaries-and-us/
---

I think I've said this before, but we're really not good at visualising or understanding risk.

One of the biggest issues with security is that you are often talking about predicting events that will occur and taking actions so that they don't occur.  But given that we have a truly terrible internal sense of probability and likelihood, it can be really difficult to justify the expense of security controls.  This is especially true if the effect of the security control is to take the estimated likelihood of a thing happening down from 1/20 to 1/30.

Security media loves a story about how advanced attackers work, and what they can do.  These stories can be really valuable for us, because capabilities tend to flow down stream, meaning that what advanced actors can do today, much less capable actors will be able to do within a number of years.  

But working out how much time, energy and effort should be spent on these things can be difficult.  Take the stolen laptop research as an example.  This is fantastic research into just what is possible with physical possession of a laptop.  But in reality, people get laptops or bags stolen all the time.  The number of people I've known who put their bag down in the pub, and someone stole it while they weren't looking.  If, as an organisation, we lost 50 laptops a year, nearly one a week, then how likely do we think it is that the attacker is going to carry out those attacks that the security researchers demonstrated?  I suspect that the probability is incredibly low, you'd have to lose thousands of laptops to start to worry about it.  So how much should you spend on hardening the devices against physical attack?

We should always bear the competent adversaries in mind, knowing what they are capable of if they decide to target us.  We need to think through who they target and how likely we are to fall into their crosshairs.  But we also need to worry about the general, low level, constant criminal activity that can be scaled and delivered in bulk.  Bad adverts, stolen cookies, phishing emails and account takeover are all the most common threats facing us today.  While honey traps on social media or physical device compromise is interesting, and valuable things to read about, lets not kid ourselves into thinking that every stolen laptop is the sign of a capable actor.

## [From Stolen Laptop to Inside the Company Network — Dolos Group](https://dolosgroup.io/blog/2021/7/9/from-stolen-laptop-to-inside-the-company-network)

[https://dolosgroup.io/blog/2021/7/9/from-stolen-laptop-to-inside-the-company-network](https://dolosgroup.io/blog/2021/7/9/from-stolen-laptop-to-inside-the-company-network)

> What can you do with a stolen laptop? Can you get access to our internal network? That was the question a client wanted answered recently. Spoiler alert: Yes, yes you can. This post will walk you through how we took a “stolen” corporate laptop and chained several exploits together to get inside the client’s corporate network.


Absolutely fascinating post showing just what is possible with physical access to the device, and some time and expertise.


## [Should ransomware payments be banned? | Tarah Wheeler and Ciaran Martin](https://www.brookings.edu/techstream/should-ransomware-payments-be-banned/)

[https://www.brookings.edu/techstream/should-ransomware-payments-be-banned/](https://www.brookings.edu/techstream/should-ransomware-payments-be-banned/)

> If a ban on ransom payments is to be a credible part of a strategy to stop the flow of money to such criminals, then surely an essential precondition is more effective state intervention in the response to attacks, reflecting the gravity of the problem as a national security threat. Whether or not payments are banned, a more activist approach is needed anyway, even if it means legislating for more interventionist levers over privately-owned critical infrastructure. 
> 
> Some may choose to see this as unwarranted state interference in private commerce: the nationalization of cybersecurity risk, if you will. On the contrary, we believe a coordinated country level response would rectify the glaring deficiency in our current reality: the near-total privatization of national security risk.


([Joel](https://twitter.com/joelgsamuel)) Paying ransomware demands does a few things: funds organised crime, confirms ransomware is a viable global attack/funding strategy, confirms the victim organisation did not summarily have a better route and confirms the victim is likely susceptible once recovered. Oh, it may _may_ also buy access to the decryptor, which may or may not be so slow the victims give up using it.

Ransomware is without a doubt a national and international policy area for legislation or regulation, but one cannot simply take away the victims choices without providing some viable alternatives that Tarah and Ciaran discuss - including state aid, even if that looks like insurance or complimentary cyber incident response.

Removing the probability of ransomware payments out of a region (such as saying no company in the UK can legally pay a cyber ransom) won't stop indiscriminate attacks.


## [Scanning your iPhone for Pegasus, NSO Group's malware | Arkadiy Tetelman](https://arkadiyt.com/2021/07/25/scanning-your-iphone-for-nso-group-pegasus-malware/)

[https://arkadiyt.com/2021/07/25/scanning-your-iphone-for-nso-group-pegasus-malware/](https://arkadiyt.com/2021/07/25/scanning-your-iphone-for-nso-group-pegasus-malware/)

> Amnesty International wrote a blog post with their forensic analysis of several compromised phones, as well as an open source tool, Mobile Verification Toolkit, for scanning your mobile device for these indicators. MVT supports both iOS and Android, and in this blog post we’ll install and run the scanner against my iOS device.


([Joel](https://twitter.com/joelgsamuel)) The NSO Group Pegasus coverage itself may be less intense but the offshoot technical analysis keeps giving.

This is a handy "step by step" (a high technical complexity rating, for IT/cyber teams etc, as opposed to the 'average Joe') on analysing an iPhone's backup for indicators of Pegasus compromise, based on what Amnesty have published.

(<Insert a usual caveat about running third-party code/software, particularly on sensitive data, here>)


## [CVE-2021-3122 | How We Caught a Threat Actor Exploiting NCR POS Zero Day - SentinelOne](https://www.sentinelone.com/blog/cve-2021-3122-how-we-caught-a-threat-actor-exploiting-ncr-pos-zero-day/)

[https://www.sentinelone.com/blog/cve-2021-3122-how-we-caught-a-threat-actor-exploiting-ncr-pos-zero-day/](https://www.sentinelone.com/blog/cve-2021-3122-how-we-caught-a-threat-actor-exploiting-ncr-pos-zero-day/)

> Prior to our IR investigation team being brought in, the client’s network appears to have first been compromised in February 2017. BlackPOS, rtPOS, GratefulPOS and PWNPOS were observed on the client’s systems, along with BTCamant ransomware, shortly after the client had installed an MSP provider. While some of the malware infections avoided C2 communications and wrote files out locally to disk, by December 2018 RampagePOS was observed communicating with a C2 at support[.]nesinoder[.]com. This domain was later seen to be associated with Maze ransomware.
> 
> Having secured the client’s network, our next task was to understand what vulnerability the threat actor was leveraging to access the Aloha BOH server. Our investigation found that a flaw exists within the NCR Command Center Agent (cmcAgent.exe). Systems that are configured with an internet-facing Command Center Agent display a banner with the hostname of the server and are discoverable through network scanning and banner grabbing. Simple searches can also be conducted through the use of tools such as shodan.io.
> 
> The cmcAgent’s RUNCommand function allows for a parameter to be supplied in a specially crafted XML request that can be executed remotely if the server is configured to listen on TCP port 8089 for incoming connections. Passing such a command allows the attacker to execute that command as SYSTEM.


Described by the vendor as a "misconfiguration", what this means is that if you connected this service to the internet, then anyone on the internet could run any code they liked on your point of sale network.  The writeup covers how a number of threat actors did exacrtly that and how they were using it to exfiltrate card data from the machines.  

What's interesting is that the threat actor is associated with the ransomware operator Maze, who are generally connected with cybercrime.  This is a good indication that ransomware is a last resort for many of these operators, and that if they can find a better way to monetise your system, they will do that rather than simply ransomware your system.


## [APT trends report Q2 2021 | Securelist](https://securelist.com/apt-trends-report-q2-2021/103517/)

[https://securelist.com/apt-trends-report-q2-2021/103517/](https://securelist.com/apt-trends-report-q2-2021/103517/)

> While the TTPs of some threat actors remain consistent over time, relying heavily on social engineering as a means of gaining a foothold in a target organisation or compromising an individual’s device, others refresh their toolsets and extend the scope of their activities. Our regular quarterly reviews are intended to highlight the key developments of APT groups.
> 
> Here are the main trends that we’ve seen in Q2 2021:
> 
> We have reported several supply-chain attacks in recent months.. While some were major and have attracted worldwide attention, we observed equally successful low-tech attacks, such as BountyGlad, CoughingDown and the attack targeting Codecov.
> APT groups mainly use social engineering to gain an initial foothold in a target network. However, we’ve seen a rise in APT threat actors leveraging exploits to gain that initial foothold – including the zero-days developed by the exploit developer we call “Moses” and those used in the PuzzleMaker, Pulse Secure attacks and the Exchange server vulnerabilities.
> APT threat actors typically refresh and update their toolsets: this includes not only the inclusion of new platforms but also the use of additional languages as seen by WildPressure’s macOS-supported Python malware.
> As illustrated by the campaigns of various threat actors – including BountyGlad, HotCousin, GoldenJackal, Scarcruft, Palwan, Pulse Secure and the threat actor behind the WebDav-O/Mail-O implants – geo-politics continues to drive APT developments.


This is an excellent summary of the quarter and covers a wide variety of potential threat actors to track and pay attention to.


## [I Knew You Were Trouble: TA456 Targets Defense Contractor with Alluring Social Media Persona | Proofpoint US](https://www.proofpoint.com/us/blog/threat-insight/i-knew-you-were-trouble-ta456-targets-defense-contractor-alluring-social-media)

[https://www.proofpoint.com/us/blog/threat-insight/i-knew-you-were-trouble-ta456-targets-defense-contractor-alluring-social-media](https://www.proofpoint.com/us/blog/threat-insight/i-knew-you-were-trouble-ta456-targets-defense-contractor-alluring-social-media)

> Proofpoint researchers have identified a years-long social engineering and targeted malware campaign by the Iranian-state aligned threat actor TA456. Using the social media persona “Marcella Flores,” TA456 built a relationship across corporate and personal communication platforms with an employee of a small subsidiary of an aerospace defense contractor. In early June 2021, the threat actor attempted to capitalize on this relationship by sending the target malware via an ongoing email communication chain. Designed to conduct reconnaissance on the target’s machine, the macro-laden document contained personalized content and demonstrated the importance TA456 placed on the target. Once the malware, which is an updated version of Liderc that Proofpoint has dubbed LEMPO, establishes persistence, it can perform reconnaissance on the infected machine, save the reconnaissance details to the host, exfiltrate sensitive information to an actor-controlled email account via SMTPS, and then cover its tracks by deleting that day’s host artifacts.  
> 
> This campaign exemplifies the persistent nature of certain state aligned threats and the human engagement they are willing to conduct in support of espionage operations. In mid-July, Facebook disrupted a network of similar personas they attributed to Tortoiseshell. LEMPO, the malware, whose delivery Proofpoint disrupted, along with the network of personas, are attributed to TA456.
> 
> [...]
> 
> Open-source research indicates “Marcella” interacted with TA456’s target on social media starting in late 2019. The earliest publicly available Facebook profile photo of “Marcella” was uploaded on May 30, 2018. Proofpoint’s analysis indicates the profile bears strong similarities to fictitious profiles previously used by Iranian APTs to socially engineer targets of intelligence value. The “Marcella” profile appeared to be friends with multiple individuals who publicly identify as defense contractor employees and who are geographically dispersed from “Marcella’s” alleged location in Liverpool, UK. On July 15, 2021, Facebook announced they had disrupted a network of Facebook and Instagram personas, including “Marcella’s,” they attributed to the Iranian-aligned actor.


This is a useful deep dive into the tactics carried out by capable attackers.  Attempting to identify people who publicly identify as defence contractor employees, and then use that built up relationship to spearphish those vulnerable users


## [Detecting LDAP enumeration and Bloodhound‘s Sharphound collector using AD Decoys | by Madhukar Raina | Securonix Tech Blog | Jul, 2021 | Medium](https://medium.com/securonix-tech-blog/detecting-ldap-enumeration-and-bloodhound-s-sharphound-collector-using-active-directory-decoys-dfc840f2f644)

[https://medium.com/securonix-tech-blog/detecting-ldap-enumeration-and-bloodhound-s-sharphound-collector-using-active-directory-decoys-dfc840f2f644](https://medium.com/securonix-tech-blog/detecting-ldap-enumeration-and-bloodhound-s-sharphound-collector-using-active-directory-decoys-dfc840f2f644)

> So while creating detection rules, it’s important to include the object GUID value of the decoy objects in the use cases to alert only for the events and not for other 4662 events in the environment.
> 
> [... example rule...]
> 
> This kind of rule will result in the events when there is a “Read Property” type access attempt on the AD object with GUID “%{afd7a537–221e-42bd-8063–29c751a32734}” which means the decoy account only.
> 
> Conclusion
> Our goal as a defender is to disrupt the adversary activity in the network. And using deception, it is possible to detect the presence of adversaries. More deception content can be added to strengthen the defense strategy like decoy network shares etc.


I'm really interested in the growth of deception practices such as decoy accounts.  They're cheap and generally easy to configure, so they feel like a cheap win.  However to use them well, you need to make sure that you can actively monitor them, that if they fire, someone knows what to do, and you need to ensure that they are monitored effectively so as not to waste everyone's time.


## [Praying Mantis (TG1021): An Advanced Memory-Resident Attack](https://www.sygnia.co/praying-mantis-targeted-apt)

[https://www.sygnia.co/praying-mantis-targeted-apt](https://www.sygnia.co/praying-mantis-targeted-apt)

> The attack Sygnia identified and responded to was carried out by an advanced and persistent threat actor dubbed "Praying Mantis", which operates almost completely in-memory.
> 
> The initial foothold within the network was obtained by leveraging a variety of deserialization exploits targeting Windows IIS servers and vulnerabilities targeting web applications. The activities observed suggest that Praying Mantis is highly familiar with the Windows IIS software and equipped with zero-day exploits.
> 
> Praying Mantis utilizes a completely volatile and custom malware framework tailor-made for IIS servers. The core component loaded on to internet-facing IIS servers, intercepts and handles any HTTP request received by the server. The threat actor also uses an additional stealthy backdoor and several post-exploitations modules to perform network reconnaissance, elevate privileges, and move laterally within networks.
> 
> The nature of the attack and general modus operandi of the activities suggest that Praying Mantis is an experienced stealthy actor highly aware of OPSEC (operations security). The malware used shows a significant effort to avoid detection by actively interfering with logging mechanisms, successfully evading commercial EDRs, as well as silently awaiting incoming connections rather than connecting back to a C2 channel and continuously generating traffic. Furthermore, Praying Mantis actively removed all disk-resident tools after using the – effectively sacrificing persistency for stealth.
> 
> 


This looks like a nasty attack from a competent attacker.  Entering your network through the IIS servers is a good reminder that zero-trust cloud first architectures, which put such servers outside the main network boundary, and treat them as a standalone system would protect you against some of this activity.  Of course, having your web hosting compromised is bad by itself, but at least it doesn't allow the attacker to pivot from your web servers to your central Active Directory and compromise your entire organisation and network.


## [Can you do agile policy work?. And why even bother trying? | by James Plunkett | Jul, 2021 | Medium](https://medium.com/@jamestplunkett/can-you-do-agile-policy-work-319b6445d5e8)

[https://medium.com/@jamestplunkett/can-you-do-agile-policy-work-319b6445d5e8](https://medium.com/@jamestplunkett/can-you-do-agile-policy-work-319b6445d5e8)

> For all these reasons, we’ve been exploring whether agile principles — which we of course apply in our DDaT teams — can add value to our policy work.
> 
> To be specific, we have:
> * Moved away from siloed / discipline-based policy teams to form multi-disciplinary teams around a policy outcome. This meant bringing together disciplines like press, policy research, data analysis, and public affairs, into a single team seeking to achieve a policy goal.
> * Pushed ourselves to be more outcome-centric in our policy work, so that we plan work less on the basis of ‘projects’ or outputs and more on the basis of an outcome we want to achieve.
> * Given our teams lots of autonomy to pursue these outcomes, choosing their tactics as they go. The role of leaders in these debates has been to stress-test and challenge, not to sign-off or instruct. We’ve setup a mechanism we call ‘challenge panels’ for this purpose.
> * Encouraged iteration — we try to test and then refine our arguments and ideas, rather than sticking rigidly to a plan we’ve decided up front.
> * A lot of this has worked really well. It’s made us much more effective, outcomes-focused, and data-driven, and we now collaborate in a much deeper way. As a result, we’ve helped to improve many areas of government policy, particularly during the pandemic, filling gaps in protections, securing additional support for marginalised groups, and standing up for consumers.


A good insight into taking and adapting Agile into policy teams.  What's interesting here is the way they've adapted for the things that don't fit.  Policy development is not the same as software development, and so you can't simple apply good agile methods directly, but by going back to the principles, you can work out how those principles apply to other types of work.


## [Securing cloud workloads for speed and agility | McKinsey](https://www.mckinsey.com/business-functions/mckinsey-digital/our-insights/security-as-code-the-best-and-maybe-only-path-to-securing-cloud-applications-and-systems#)

[https://www.mckinsey.com/business-functions/mckinsey-digital/our-insights/security-as-code-the-best-and-maybe-only-path-to-securing-cloud-applications-and-systems#](https://www.mckinsey.com/business-functions/mckinsey-digital/our-insights/security-as-code-the-best-and-maybe-only-path-to-securing-cloud-applications-and-systems#)

> Implementing SaC requires a substantial policy, architectural, and cultural departure for almost all companies. For this reason, many have found it helpful to use the SaC framework to classify workloads according to sensitivity and criticality and then apply specific controls, based on workload risk and deployment type. Furthermore, it provides a blueprint for a future-state architecture and outlines the key decisions to be made in order to effectively and efficiently instantiate SaC through various automation use cases. Finally, the framework defines how the company’s operating model must change to extract the full benefits of cloud adoption


This from McKinsey says all the same things that many tech oriented CISO's have been saying for years, but now there's a McKinsey report that says it too.

I quite like the adoption framework that they've come up with, it's intuitive and remarkably simple as well, and I've always been a big fan of risk segregated control sets rather than a one-size-fits-all set of policies and controls.


## [The Tyranny of Spreadsheets | Tim Harford](https://timharford.com/2021/07/the-tyranny-of-spreadsheets/)

[https://timharford.com/2021/07/the-tyranny-of-spreadsheets/](https://timharford.com/2021/07/the-tyranny-of-spreadsheets/)

> The original paper spreadsheets were designed to help us not lose our way, and one might naturally imagine the digital spreadsheet is not only faster but more accurate. Is it? One clue comes from a wonderful study conducted by Felienne Hermans, a computer scientist. A few years ago, Hermans realised that there was a bountiful source of spreadsheets she could study. That source was Enron, the bankrupt energy company.
> 
> After Enron collapsed in 2001 amid an epic accounting scandal, regulators extracted a cache of half a million emails from the company’s servers. Those emails are now publicly available and have been studied by researchers trying to understand everything from the evolution of informal written language to the way people use email folders. Hermans was interested in what was attached to some of these emails: spreadsheets.
> 
> She started digging through them, not looking for fraud, but for spreadsheets with obvious errors such as missing or circular references. Looking at nearly 10,000 spreadsheets with calculations in them, she found that a quarter had at least one such error. The errors even seemed to multiply. If a spreadsheet had any mistakes at all, on average it contained more than 750.


Spreadsheets really do rule the world, I've seen spreadsheets controlling trading floors, educational outcomes, procurements, pay awards, you name it.

But we're not actually very good at spreadsheets.  There's often no real training for most people, and the model is alien to many of the people tasked with supporting them.  But even with that I was surprised to find that 1/4 of spreadsheets have errors in them.


