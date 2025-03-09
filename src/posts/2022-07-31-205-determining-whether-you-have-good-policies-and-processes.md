---
title: "205 - Determining whether you have good policies and processes"
date: 2022-07-31
description: "I’m not a huge fan of certifications."
permalink: /determining-whether-you-have-good-policies-and-processes/
---

I’m not a huge fan of certifications.

However, SOC2 seems to actually provide a lot of things that we care about.

I’ve often joked in the past that ISO27001, since it focuses on the existence of repeatable processes, doesn’t give you confidence that the company is actually any good, just that it’s repeatably and reliably bad at what it does.  That’s a little unfair, but it’s really important to recognise what the scope of your certification covers.

The interesting thing with SOC2 is that it actually does attempt to validate that your company has a good set of processes, that actually make a difference in how secure the company is.

If you improve your internal processes and policies to meet the SOC2 standard, then you’ll defintely be more secure.

But further, as we look more and more into the supply chain for our organisation, knowing that your suppliers are secure in their processes and policies will help reduce the risk they pose to you.  While I’m not sure that SOC2 is necessarily appropriate if you are a tech giant like Google or Microsoft, or a 10 person startup, for almost everyone else, especially those SaaS vendors you want to trust with your organisational data, it’s a damn good start.

But that aside, this bit of the SOC2 blogpost really stood out to me:

> But actually SOC2'ing a company I have a stake put me in a sort of CorpSec state of mind. You read a template incident response or data classification policy. You start thinking about why those policies exist. Then you think about would could go wrong if there was a major misunderstanding about those policies. Long story short, we wrote our own.
>
> This part of the process was drastically simplified by the work Ryan McGeehan has published, for free, on his “Starting Up Security” site. We have, for instance, an Information Security Policy. It’s all in our own words (and ours quotes grugq). But it’s based almost heading-for-heading on Ryan’s startup policy, which is brilliant.
>
> One thing about writing policies inspired by Ryan’s examples is that it liberates you to write things that make sense and read clearly and don’t contain the words “whereas” or “designee”.

I’m a huge fan of Ryan McGeehan’s work, and for some reason I don’t think I’ve linked to his startup policies before.

But Ryan really believes that policies need to make sense and be readable.  His one is filled with humour, but it’s in clear simple language, and it really sets out the risks that employees are taking with your data.  If employees have read this, then they’ve actually understood what the risks are, and what you do about them.

You could do a lot worse than copying Ryan’s security policy for your org

## [SOC2: The Screenshots Will Continue Until Security Improves · Fly ](https://fly.io/blog/soc2-the-screenshots-will-continue-until-security-improves/)

[https://fly.io/blog/soc2-the-screenshots-will-continue-until-security-improves/](https://fly.io/blog/soc2-the-screenshots-will-continue-until-security-improves/)

> SOC2 is an accounting-style, or "real", audit. That means it confirms on-paper claims companies make about their security processes. They’re nothing at all like “security audits” or “penetration tests”, which are heavily adversarial, engineering-driven, and involve giving third parties free rein to find interesting problems.  
> 
> SOC2 is about the security of the company, not the company’s products. A SOC2 audit would tell you something about whether the customer support team could pop a shell on production machines; it wouldn’t tell you anything about whether an attacker could pop a shell with a SQL Injection vulnerability. 
> 
> The guts of a SOC2 audit are a giant spreadsheet questionnaire (the “DRL”) and a battery of screenshots serving as evidence for the answers in the questionnaire 


If you are a CISO, this is probably one of the most important things you will read.  Read it once through, then sit down and read it carefully section by section.  Most importantly, believe Thomas when he says that you can start all the work to be SOC certified without actually doing the audit.  Almost all of the requirements of the SOC2 process will make your company more secure, and many will show you where there are dangerous gaps in your company culture or process. 


## [CSRB | CISA - Review of the December 2021 Log4J Incident ](https://www.cisa.gov/cyber-safety-review-board)

[https://www.cisa.gov/cyber-safety-review-board](https://www.cisa.gov/cyber-safety-review-board)

> Numerous interviewees highlighted the overall unity of effort and communications across the broader cyber community, noting a sense of common struggle against an unprecedented and dangerous new vulnerability. They also observed that the flood of well-intentioned information soon became overwhelming, rather than empowering, for impacted organizations. This was especially true during the initial response, due to the amount of information coming from security researchers on Twitter,139, 140 notifications from ASF, vendor security alerts, press coverage, and notifications from government agencies, such as CISA. In a sea of alerts about potential mitigations and defensive measures, network defenders sought authoritative guidance that they could confidently take to their teams and execute against.141 Appendix D provides more insight into the amount of information that inundated responders.
> 
> The impact of this information overload is apparent in the sequence of multiple releases of Log4j upgrades as researchers discovered additional security flaws (see Section 1.2 – Discovery and Disclosure). Due to continuous releases of upgrades, organizations had to consume new information in real time in order to understand to which version they should upgrade relative to their overall risk posture. Some turned to CVSS scores for insights into their risk exposure. However, CVSS scores do not provide insight into the impact of the vulnerability in the context of an organization’s business assets, exposure, or operations, or the specific intent of attackers exploiting the vulnerability. As impacted organizations attempted to prioritize these risks and determine remediations, they were forced to sort through bulletins, advisories, and guidance from vendors, media, partners, and government sources.
> 
> Organizations also faced information overload from their own security monitoring programs. After disclosure of the vulnerability, organizations reported observing widespread vulnerability scanning, and many were unable to distinguish attackers from bona fide researchers. This meant organizations found it challenging to understand whether or not malicious threat actors were attacking their systems. Some organizations offered resources to help focus responders, for example GreyNoise has a free community portal to help identify known malicious and known benign (including research) scans. 


There’s a lot of interesting bits in this report, the first that the Cyber Security Review Board has produced.  But one of the things that they didn’t really make any strong recommendations about, is the sheer amount of information that was published, and how confusing it all was.

Some major threat intel organisations massively over inflated the risk, and the thousands of researchers scanning for vulnerable systems defintiely added to the noise rather than making life better.

For myself and others in my area, the reddit r/blueteamsec daily threads, like this one: [https://www.reddit.com/r/blueteamsec/comments/rd38z9/log4j_0day_being_exploited/](https://www.reddit.com/r/blueteamsec/comments/rd38z9/log4j_0day_being_exploited/?utm_source=share&utm_medium=ios_app&utm_name=iossmf) were an amazing way of making sense of that noise, and trying to keep the majority of people focused on the important developments. 


## [Discovery of new UEFI rootkit exposes an ugly truth: The attacks are invisible to us | Ars Technica ](https://arstechnica.com/information-technology/2022/07/researchers-unpack-unkillable-uefi-rootkit-that-survives-os-reinstalls/)

[https://arstechnica.com/information-technology/2022/07/researchers-unpack-unkillable-uefi-rootkit-that-survives-os-reinstalls/](https://arstechnica.com/information-technology/2022/07/researchers-unpack-unkillable-uefi-rootkit-that-survives-os-reinstalls/)

> On Monday, researchers from Kaspersky [profiled CosmicStrand](https://securelist.com/cosmicstrand-uefi-firmware-rootkit/106973/) , the security firm’s name for a sophisticated UEFI rootkit that the company detected and obtained through its antivirus software. The find is among only a handful of such UEFI threats known to have been used in the wild. Until recently, researchers assumed that the technical demands required to develop UEFI malware of this caliber put it out of reach of most threat actors. Now, with Kaspersky attributing CosmicStrand to an unknown Chinese-speaking hacking group with possible ties to cryptominer malware, this type of malware may not be so rare after all.
> 
> 
> “The most striking aspect of this report is that this UEFI implant seems to have been used in the wild since the end of 2016—long before UEFI attacks started being publicly described,” Kaspersky researchers wrote. “This discovery begs a final question: If this is what the attackers were using back then, what are they using today?” 
> 
> While researchers from fellow security firm Qihoo360 [reported](https://bbs.360.cn/thread-14959110-1-1.html) on an earlier variant of the rootkit in 2017, Kaspersky and most other Western-based security firms didn’t take notice. Kaspersky’s newer research describes in detail how the rootkit—found in firmware images of some Gigabyte or Asus motherboards—is able to hijack the boot process of infected machines. The technical underpinnings attest to the sophistication of the malware.      
> 
> The CosmicStrand workflow looks like this:
> 
> * The initial infected firmware bootstraps the whole chain.
> * The malware sets up a malicious hook in the boot manager, allowing it to modify Windows’ kernel loader before it is executed.
> * By tampering with the OS loader, the attackers are able to set up another hook in a function of the Windows kernel.
> * When that function is later called during the normal startup procedure of the OS, the malware takes control of the execution flow one last time.
> * It deploys a shellcode in memory and contacts the C2 server to retrieve the actual malicious payload to run on the victim’s machine. 


This is an interesting change in our risk tolerances.  As Ars makes out, it’s always been assumed that UEFI implants are too complex, difficult to control, and low value to be used by anyone but the most advanced attackers.  

In theory, a UEFI implant can bypass all of the OS’s protections, which is really valuable if you want to crack really locked down computers, but since most people deploying crypto miners are monetarily focused, and their targets are low security, it’s felt unlikely that UEFI malware would be used. This report might change that likelihood. 


## [Untangling KNOTWEED: European private-sector offensive actor using 0-day exploits - Microsoft Security Blog ](https://www.microsoft.com/security/blog/2022/07/27/untangling-knotweed-european-private-sector-offensive-actor-using-0-day-exploits/)

[https://www.microsoft.com/security/blog/2022/07/27/untangling-knotweed-european-private-sector-offensive-actor-using-0-day-exploits/](https://www.microsoft.com/security/blog/2022/07/27/untangling-knotweed-european-private-sector-offensive-actor-using-0-day-exploits/)

> PSOAs, which [Microsoft also refers to as cyber mercenaries](https://blogs.microsoft.com/on-the-issues/2022/07/27/private-sector-cyberweapons-psoas-knotweed/) , sell hacking tools or services through a variety of business models. Two common models for this type of actor are access-as-a-service and hack-for-hire. In access-as-a-service, the actor sells full end-to-end hacking tools that can be used by the purchaser in operations, with the PSOA not involved in any targeting or running of the operation. In hack-for-hire, detailed information is provided by the purchaser to the actor, who then runs the targeted operations. Based on observed attacks and news reports, MSTIC believes that KNOTWEED may blend these models: they sell the Subzero malware to third parties but have also been observed using KNOTWEED-associated infrastructure in some attacks, suggesting more direct involvement. 


An advanced actor that is not only selling their tools onto less advanced actors, but also using them themselves.  There’s a question here about why they would choose to impact on their operational security in this way.  Is it sheer greed, wanting to use their own tools on targets of their own choosing?  Is it that they didn’t realise that MSTIC would be able to track their use?  Or is it deliberate cover, allowing the less capable actors to fill the space with noise?

Maybe it’s just the way they decided to run their operation? 


## [How to Safely Lend Someone Else Your Phone | WIRED ](https://www.wired.com/story/how-to-safely-lend-someone-else-your-phone/)

[https://www.wired.com/story/how-to-safely-lend-someone-else-your-phone/](https://www.wired.com/story/how-to-safely-lend-someone-else-your-phone/)

> **FROM THE NEPHEW** who wants to play games for a few minutes, to the friend who wants to see your vacation snaps, to the stranger who needs to make a call, there are going to be people who want to borrow your phone.
> 
> That's quite a privacy and security risk if you think about everything that your phone gives you access to: social media profiles, [banking details](https://www.wired.com/story/simple-online-bank-alternatives-chime-one-bbva/) , instant messenger conversations, photos and videos that you'd rather the world didn't see, and so on.
> 
> However, there are ways to hand over your phone to someone else without having to worry about what they might get up to on it. You just need to make sure that you've taken a few precautions before the exchange takes place. 


These features are not very well known, but both major phone operating systems enable you to do this.  Whether it was intended to “child lock” your device, or whether it was a privacy feature, it’s worth knowing as a privacy feature to use. 


## [GitHub - jorgef/engineeringladders: A framework for Engineering Managers ](https://github.com/jorgef/engineeringladders)

[https://github.com/jorgef/engineeringladders](https://github.com/jorgef/engineeringladders)

> This framework allows software engineering managers to have meaningful conversations with their direct reports around the expectations of each position and how to plan for the next level in their career ladder.
> 
> Although the framework uses roles and levels that are somewhat standard in the US tech industry, every company is different. Please use the information provided as a baseline and feel free adjust it to your needs.
> 
> […]
> 
> The framework has 4 different ladders:
> 
> * [**Developer**](https://github.com/jorgef/engineeringladders/blob/master/Developer.md) : role also known as programmer or software engineer, requires a deep level of technical expertise
> * [**Tech Lead**](https://github.com/jorgef/engineeringladders/blob/master/TechLead.md) : role also known as dev lead, is the owner of the system and requires a unique balance between hands-on development, architecture knowledge and production support
> * [**Technical Program Manager**](https://github.com/jorgef/engineeringladders/blob/master/TechnicalProgramManager.md) : role responsible for coordinating and driving to completion initiatives that span multiple teams
> * [**Engineering Manager**](https://github.com/jorgef/engineeringladders/blob/master/EngineeringManager.md) : role also known as dev manager, is responsible for the consistent delivery, career growth and level of happiness of the team 


This is a nicely put together framework.  It’s way too complicated if you have 3 developers, but if you are looking at teams of hundreds of developers, it’s worth looking at.  It’s also worth a read through if you currently work in a small company and are thinking of moving to a big company, to work out what job role and level best suits you. 


## [Best Practices for AWS Organizations Service Control Policies in a Multi-Account Environment | AWS for Industries ](https://aws.amazon.com/blogs/industries/best-practices-for-aws-organizations-service-control-policies-in-a-multi-account-environment/)

[https://aws.amazon.com/blogs/industries/best-practices-for-aws-organizations-service-control-policies-in-a-multi-account-environment/](https://aws.amazon.com/blogs/industries/best-practices-for-aws-organizations-service-control-policies-in-a-multi-account-environment/)

> The following sections explain the hierarchy of an OU structure for the FSI customer and some of the SCPs that can be considered for OUs in the hierarchy. 
> 
> This is general guidance and by no means an exhaustive list of SCPs. You can start with this guidance and extend the SCPs to cover controls and governance needed for your organization. Also please note, the SDLC OUs would mimic the structure of the production OUs and for simplicity it is not shown in the diagram.
> 
> Before we dive into the OU structure here are few things to note about SCPs:
> 
> * SCPs are invisible to all the roles in the child account, including the root user
> * SCPs are applied to all roles in the child account, including root user
> * SCPs can be attached to the organization root, specific OU or to a specific account. Because you can attach policies to multiple levels in the organization, accounts can [inherit](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_inheritance_auth.html) multiple policies. 
> 
> 
> 
> * As a general best practice, when applying SCPs, the less granular policies are applied higher in the hierarchy and the SCPs become more restrictive as you go to lower level OUs and accounts. As an example, a higher-level policy can permit the use of [Amazon Elastic Compute Cloud](https://aws.amazon.com/ec2/) (Amazon EC2) and a less granular policy applied at lower level can then restrict the instance types that can be used.
> * The effective permission for the user (including administrative user) in the child account is the intersection between the SCP and IAM permissions. 


This is designed for financial services companies, but actualy it’s just a really good writeup of how to setup multi-organisational unit policies for any reasonably complex production infrastructure.

I particularly like the separation of the security OU from the Production OU, and the emphasis on low granularity, low impact policies at the higher level.  If your policies are too restrictive, then developer teams will simply use unsupported external cloud services instead. 


## [Will AI Steal Submarines’ Stealth? ](https://spectrum.ieee.org/nuclear-submarine)

[https://spectrum.ieee.org/nuclear-submarine](https://spectrum.ieee.org/nuclear-submarine)

> Experts disagree on the irreversibility of ocean transparency. Because any technological breakthroughs will not be implemented overnight, “nations should have ample time to develop countermeasures [that] cancel out any improved detection capabilities,” says [Matt Korda](https://www.sipri.org/about/bios/matt-korda) , senior research associate at the Federation of American Scientists, in Washington, D.C. However, Roger Bradbury and eight colleagues at the National Security College of the Australian National University [disagree](https://nsc.crawford.anu.edu.au/publication/16666/transparent-oceans-coming-ssbn-counter-detection-task-may-be-insuperable) , claiming that any technical ability to counter detection technologies will start to decline by 2050.
> 
> Korda also points out that ocean transparency, to the extent that it occurs, “will not affect countries equally. And that raises some interesting questions.” [For example, U.S. nuclear-powered submarines are “the quietest on the planet. They are virtually undetectable](https://thebulletin.org/2019/01/invisible-nuclear-armed-submarines-or-transparent-oceans-are-ballistic-missile-submarines-still-the-best-deterrent-for-the-united-states/) . Even if submarines become more visible in general, this may have zero meaningful effect on U.S. submarines’ survivability.” 


Fascinating insight into how evolving and merging technologies in a variety of areas are interacting in a totally different domain.  Do people working on drone swarming technology realise that it’s could change how submarine detection systems work?

Advancements in technologies are often reusable in domains that we don’t think about at first. 


