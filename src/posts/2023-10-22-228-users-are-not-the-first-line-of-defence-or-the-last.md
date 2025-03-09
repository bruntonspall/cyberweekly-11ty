---
title: "228 - Users are not the first line of defence, or the last"
date: 2023-10-22
description: "Phishing exercises do more damage than they prevent."
permalink: /users-are-not-the-first-line-of-defence-or-the-last/
---

Phishing exercises do more damage than they prevent.

There I said it, in black and white.  Running phishing exercises, especially where you rank or score your employees has negligable effects on actual phishing successes, but definitely has a negative impact on how your employees feel and interact with your systems.

It's easy for the stressed out CISO to decide that recent news of social engineering campaigns and advanced actors, that the cheapest thing they can do that has a visible and measurable impact is to run a test phishing exercise, show the board how vulnerable they are, do some cheap phishing training and then re-run the phishing exercises to show an improvement.

I've covered below some of the most recent campaigns from nation states and advanced attackers, from phishing lures dressed up as job interviews, to the use of zero-days embedded in press announcements, or compromising development servers.  What's clear from the attacks set out is that most of the attacks can be managed through normal good practice.  The use of commercial malware capabilities, the pivoting to scan the AD directory, and the abuse of admin credentials cached on local machines.

We know that many of these can be fixed through the use of good privilege separation, the use of highly controlled privileged devices, and the use of hardware MFA tokens and so on.

But this stuff might be "basic", but it's not easy and it's not simple. 

To tie together these two things, the way that we can improve phishing protection is both through user education, not punishing tests, but actual education about the threats that are out there, and support on the services that are most attacked to ensure that users can easily and clearly tell the difference.

As we chase the complex, exciting, news headline driven improvements that we can make, we need to invest in the core basics to enable a more secure future, that allows users to better defend themselves and their organisation.

## [It might Be Time to Rethink Phishing Awareness ](https://malwaretech.com/2023/09/it-might-be-time-to-rethink-phishing-awareness.html)

[https://malwaretech.com/2023/09/it-might-be-time-to-rethink-phishing-awareness.html](https://malwaretech.com/2023/09/it-might-be-time-to-rethink-phishing-awareness.html)

> Imagine you’ve had a long difficult year at work. You’re struggling with bills, maybe your car needs a big repair. But don’t worry, you’re getting a Christmas bonus! Or, so you thought. Upon clicking the link you’re met with the harsh reality that not only are you not getting that bonus, you’re going to have to add sitting through phishing training to your busy work schedule. Now, I don’t know about you, but I’d be leaning less towards extra security vigilance and more toward ransoming the network myself.
> 
> Jokes aside, playing on employees’ emotions or punishing them for failing at something that isn’t even their job is likely to be extremely counter-productive. Employees who fall victim to genuine phishing attempts will become far less likely to notify the security team out of fear, shame, or resentment. Workers may also attempt to avoid failing phishing tests by undermining other security controls, such as through the use of personal devices that don’t run EDRs or pass through the corporate gateway.
> 
> I’ve often joked that the world’s best hackers aren’t the people who work for ransomware groups, nor the NSA, they’re your employees when your security controls get in the way of their work.
> 
> […]
> 
> Personally, I’d lean toward silent phishing test if testing is a must. Ones where employees are given no indication of the fact that it is a test, was a test, or that they failed. Data gathered can instead be used behind the scenes to inform future security decisions, without undermining employee trust. Even then, I’d still avoid emotionally-manipulative lures at all costs.
> 
> Overall, I think phishing awareness can be highly effective, but far too many organizations are treating it as a carrot and stick exercise. Negative incentives seldom work in any aspect of life, and organizational security is no different. 


Totally agree with this take.  Raising awareness of phishing and what it looks like is valuable, but that can be done through training, through sharing information.  Do that right and your employees can forward or report phishing when it does slip through your nets and you’ll be better off.

Phishing tests that are silent, that simply tell the user “Thanks for the feedback, your participation helps us tweak the systems that protect you” but that don’t attempt to punish users might be useful to gather feedback on your systems.

But don’t involve your users or gamify your phishing simulations to punish the users who do badly.  All it will do is create resentment and lower your chances that employees will think positively of Security and come to them if they think they might have accidentally clicked on a link. 


## [Phishing versus Defence-in-Depth. Why I think simulated phishing… | by Joel Samuel | Medium ](https://joelgsamuel.medium.com/what-i-mean-by-defence-in-depth-cybersecurity-6ac07f89ad89)

[https://joelgsamuel.medium.com/what-i-mean-by-defence-in-depth-cybersecurity-6ac07f89ad89](https://joelgsamuel.medium.com/what-i-mean-by-defence-in-depth-cybersecurity-6ac07f89ad89)

> I have a small sympathy for stretched security teams, who use phishing exercises as something they can do, in lieu of other things they want to do but don’t have the money for (they would love an EDR system but can’t afford one, etc). Its only a small sympathy, because ‘I get it’ but all its doing is bugging users and feeding the cycle: phishing exercises don’t improve security, but security isn’t being improved, so conduct more phishing exercises. [The beatings will continue until morale improves](https://quoteinvestigator.com/2020/07/15/morale/) . **The culture cost** Hacking off end-users is counter-productive to security in the long term. Even if phishing exercises are done well, end-users who ‘fall’ for these exercises won’t feel good about, will loathe any training they are sent on, and may be less likely to engage with security teams in the future. 


Joel’s main point in this article is about the number of technical systems that a phishing email has to go through before a user see’s it, and then the number of technical systems that have to be involved in the actual downloading and execution of malware.

But all of that aside, and Joel makes excellent points in the article, the psychological and cultural impact on your teams is significant and shouldn’t be discounted as a cost of a poorly thought out phishing exercise 


## [Be On Alert; That HR Email Could Be A Phishing Email! - IT Security Guru ](https://www.itsecurityguru.org/2023/10/19/be-on-alert-that-hr-email-could-be-a-phishing-email/)

[https://www.itsecurityguru.org/2023/10/19/be-on-alert-that-hr-email-could-be-a-phishing-email/](https://www.itsecurityguru.org/2023/10/19/be-on-alert-that-hr-email-could-be-a-phishing-email/)

> New research this week has given warning to employees to be on alert to emails seemingly from human resources (HR) as they could be fraudulent. In fact, the findings from KnowBe4’s latest phishing report has highlighted that fraudulent HR emails remain a prevalent tactic employed by cybercriminals.
> 
> Such deceptive emails may encompass subjects like alterations in dress code policies, updates on training sessions, changes in vacation policies, or a wide range of other topics.
> 
> These deceptive tactics prove effective as they often prompt individuals to react impulsively, bypassing logical scrutiny of the email’s legitimacy. Consequently, they possess the potential to disrupt both an employee’s personal life and professional workday, as cautioned by the company. 


The solution to this isn’t to train your staff to not click on fraudulant emails, it’s not to train them what fraudulant emails looks like, it’s not even to have better incoming email filters.

Fraudsters don’t target HR just because it’s a good way to reach individuals (although it is), they  target HR because they know that they never get given good tools, and so most of us receive our HR survey from some inscrutable qualtrics domain, get updates from the HR director from a random mailchimp address, get benefits from some whitelabel company most of us haven’t heard of.

The solution to this is for your security team to actually work with HR, to ensure that they have reliable, safe and consistent ways of communicating with staff, that the survey systems are correctly labelled, and to support them providing services to your staff.

When that happens, you make life a thousand times more difficult for fraudsters, as those phishing emails do actually look different to the real ones 


## [How Cloudflare mitigated yet another Okta compromise ](http://blog.cloudflare.com/how-cloudflare-mitigated-yet-another-okta-compromise/)

[http://blog.cloudflare.com/how-cloudflare-mitigated-yet-another-okta-compromise/](http://blog.cloudflare.com/how-cloudflare-mitigated-yet-another-okta-compromise/)

> This is the second time Cloudflare has been impacted by a breach of Okta’s systems. In [March 2022](https://blog.cloudflare.com/cloudflare-investigation-of-the-january-2022-okta-compromise/) , we blogged about our investigation on how a breach of Okta affected Cloudflare. In that incident, we concluded that there was no access from the threat actor to any of our systems or data – Cloudflare’s use of hard keys for multi-factor authentication stopped this attack.
> 
> The key to mitigating this week’s incident was our team’s early detection and immediate response. In fact, we contacted Okta about the breach of their systems before they had notified us. The attacker used an open session from Okta, with Administrative privileges, and accessed our Okta instance. We were able to use our Cloudflare Zero Trust Access, Gateway, and Data Loss Prevention and our Cloudforce One threat research to validate the scope of the incident and contain it before the attacker could gain access to customer data, customer systems, or our production network. With this confidence, we were able to quickly mitigate the incident before the threat-actors were able to establish persistence.
> 
> […]
> 
> If you are an Okta customer, we recommend that you reach out to them for further information regarding potential impact to your organization. We also advise the following actions:
> 
> * Enable Hardware MFA for all user accounts. Passwords alone do not offer the necessary level of protection against attacks. We strongly recommend the usage of hardware keys, as other methods of MFA can be vulnerable to phishing attacks.
> […]
> * Utilize tools to validate devices connected to your critical systems, such as Cloudflare Access Device Posture Check.
> * Practice defense in depth for your detection and monitoring strategies. 


Using third parties is required in this day and age, and you have no choice but to trust that a compromise of their systems should be caught and maintained with minimal impact on yours.

The solutions here are more use of hardware tokens, along with understanding and tracking what changes third parties make in their systems and yours.

You need to ensure that where you trust third parties, you are clearly able to articulate and extend that trust only as far as necessary.  Anything you can do to ensure that compromise of the supplier doesn’t extend into your systems is worth doing to limit the blast radius of the attack. 


## [October Windows Server updates cause Hyper-V VM boot issues ](https://www.bleepingcomputer.com/news/microsoft/october-windows-server-updates-cause-hyper-v-vm-boot-issues/)

[https://www.bleepingcomputer.com/news/microsoft/october-windows-server-updates-cause-hyper-v-vm-boot-issues/](https://www.bleepingcomputer.com/news/microsoft/october-windows-server-updates-cause-hyper-v-vm-boot-issues/)

> According [to](https://learn.microsoft.com/en-us/answers/questions/1390482/vms-wont-start-since-windows-updates-october-2023)  [complaints](http://learn.microsoft.com/en-us/answers/questions/1390624/virtual-machines-failed-to-start-after-installing)  [from](http://twitter.com/JetzeMellema/status/1713277368968650786)  [Windows](https://answers.microsoft.com/en-us/windowserver/forum/all/hyper-v-guests-fail-to-start-after-october-2023/fa4ef87f-001f-44a2-af05-92de8fa84706)  [admins](https://community.spiceworks.com/topic/2496148-hyper-v-vm-won-t-start-vhdx-incorrect-function) , the issue is triggered after installing [KB5031361](https://support.microsoft.com/en-gb/topic/october-10-2023-kb5031361-os-build-17763-4974-766593db-b47a-4b18-a698-906426860313) and [KB5031364](https://support.microsoft.com/en-us/topic/october-10-2023-kb5031364-os-build-20348-2031-7f1d69e7-c468-4566-887a-1902af791bbc) on Windows Server 2019 and Windows Server 2022 systems.
> 
> A Microsoft spokesperson told BleepingComputer that the company is aware of the issue and is investigating.
> 
> The following errors will be logged to the event viewer when trying to start a VM on an affected Hyper-V system:
> * Failed to start virtual machine TOOLS. Error: 'TOOLS' failed to start.
> * Failed to Power on with Error 'Incorrect function.'
> * Failed to open attachment 'vhdx_path'. Error: 'Incorrect function.'
> 
> Administrators with impacted devices have noted that uninstalling the problematic updates resolves the issue, allowing all virtual machines (VMs) to start up without any problems. 


Remember that when IT says that they need to test patches before just “patch immediately”, they mean it because sometimes patches break critical things.

Make sure that your desire as security to patch everything is held in tension with the complexity of applying patches across large and hetrogeneous estates, and the need to ensure the business keeps running.  There’s lots of reasons that patches can’t always be applied the moment they come out. 


## [Lazarus luring employees with trojanized coding challenges: The case of a Spanish aerospace company ](https://www.welivesecurity.com/en/eset-research/lazarus-luring-employees-trojanized-coding-challenges-case-spanish-aerospace-company/)

[https://www.welivesecurity.com/en/eset-research/lazarus-luring-employees-trojanized-coding-challenges-case-spanish-aerospace-company/](https://www.welivesecurity.com/en/eset-research/lazarus-luring-employees-trojanized-coding-challenges-case-spanish-aerospace-company/)

> At the beginning of Lazarus attacks, the unaware targets are usually convinced to recklessly self-compromise their systems. For this purpose, the attackers employ different strategies; for example, the target is lured to execute an attacker-provided (and trojanized) PDF viewer to see the full content of a job offer. Alternately, the target is encouraged to connect with a trojanized SSL/VPN client, being provided with an IP address and login details. Both scenarios are described in a Microsoft blogpost published in September 2022. The narrative in this case was the scammer’s request to prove the victim’s proficiency in the C++ programming language.
> 
> Two malicious executables, Quiz1.exe and Quiz2.exe, were provided for that purpose and delivered via the Quiz1.iso and Quiz2.iso images hosted on a third-party cloud storage platform. Both executables are very simple command line applications asking for input.
> 
> The first one is a Hello World project, which is a very basic program, often consisting of just a single line of code, that displays the text “Hello, World!” when executed. The second prints a Fibonacci sequence up to the largest element smaller than the number entered as input. A Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, typically starting with 0 and 1; however, in this malicious challenge, the sequence starts with 1 and 2. Figure 2 displays example output from the Fibonacci sequence challenge. After the output is printed, both executables trigger the malicious action of installing additional payloads from the ISO images onto the target’s system. The task for a targeted developer is to understand the logic of the program and rewrite it in the C++ programming language.


Scary set of attacks here.  The social pretext is creates a desire from the user to keep the actions hidden from their employer, and makes it far more likely that the engineer would run the program on their local computer.  I can picture lots of developers falling for this campaign.


## [Government-backed actors exploiting WinRAR vulnerability ](https://blog.google/threat-analysis-group/government-backed-actors-exploiting-winrar-vulnerability/)

[https://blog.google/threat-analysis-group/government-backed-actors-exploiting-winrar-vulnerability/](https://blog.google/threat-analysis-group/government-backed-actors-exploiting-winrar-vulnerability/)

> The payload, found in “Навчальна-програма-Оператори.pdf /Навчальна-програма-Оператори.pdf_.bat” was a packed Rhadamanthys infostealer. Rhadamanthys is a commodity infostealer that is able to collect and exfiltrate browser credentials and session information among other things. It operates on a subscription-based model and can be rented out for as low as $250 for 30 days. Usage of commercially available infostealers, that are typically employed by cybercrime actors, is atypical of FROZENBARENTS. 


Thus vulnerability, a peculiar one that takes advantage of how a few different systems interact, has been seen being used by state based threat actors.  But what I thought was even more interesting, is that the example here was then using a commodity tool after compromise.  

This was a zero-day exploit to execute code on a computer based on user interaction without the user realising that it would be the result, but if you couldn’t defend against that, you still should have had sufficient end user device protections to prevent a commodity infostealer from executing. 

AS commodity tools get better and better, states will use them more often in their campaigns.  Defending against those commodity tools however should be much easier for most of us, so this is broadly speaking a good thing. 


## [Cisco identifies another IOS XE vulnerability, with patches coming this weekend ](https://therecord.media/cisco-ios-xe-vulnerability-patches-coming)

[https://therecord.media/cisco-ios-xe-vulnerability-patches-coming](https://therecord.media/cisco-ios-xe-vulnerability-patches-coming)

> Earlier this week, Cisco released [an advisory](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-iosxe-webui-privesc-j22SaA4z) and a [detailed blog post](https://blog.talosintelligence.com/active-exploitation-of-cisco-ios-xe-software) about CVE-2023-20198 — warning defenders that it carries the highest severity CVSS score possible of 10 and was being exploited by hackers. A patch was not available to address the issue, and Cisco urged customers to make sure that affected devices were not accessible from the internet.
> 
> In a statement to Recorded Future News on Friday, the tech giant said a patch would be available for the issue on Sunday.
> 
> The company also addressed a specific issue raised in the blog that had caused alarm among experts. Cisco initially said that during attacks involving the vulnerability, their incident responders observed hackers also exploiting CVE-2021-1435, which Cisco had patched in 2021.
> 
> Devices fully patched against that bug were seen infected by implants successfully installed “through an as of yet undetermined mechanism.” 


This one has probably caused a bunch of work this weekend for a number of operational teams.  

Yet again, this is a vulnerability in the web based administrative interface, which is something that shouldn’t be exposed to the internet or attackers.  But the act of segregating management interfaces away to a specific management network and set of devices is still not common practice, especially if your systems are run by a managed service provider who need to connect into your IT systems from afar to access them. 


## [TeamCity Flaw Exploited By North Korean Nation-State Actors | Decipher ](https://duo.com/decipher/teamcity-flaw-exploited-by-north-korean-nation-state-actors)

[https://duo.com/decipher/teamcity-flaw-exploited-by-north-korean-nation-state-actors](https://duo.com/decipher/teamcity-flaw-exploited-by-north-korean-nation-state-actors)

> Software development tool company JetBrains [released version 2023.05.4](https://duo.com/decipher/teamcity-users-urged-to-apply-fix-for-critical-flaw) to fix the flaw (CVE-2023-42793) on Sept. 18, and said that on-premises instances of the TeamCity CI/CD server are impacted. On Wednesday, [Microsoft’s threat intelligence group said](https://www.microsoft.com/en-us/security/blog/2023/10/18/multiple-north-korean-threat-actors-exploiting-the-teamcity-cve-2023-42793-vulnerability/) that it has observed two groups targeting the flaw since early October in attacks that deploy backdoors, steal credentials and more.
> 
> “Based on the profile of victim organizations affected by these intrusions, Microsoft assesses that the threat actors may be opportunistically compromising vulnerable servers,” according to Microsoft researchers. “However, both actors have deployed malware and tools and utilized techniques that may enable persistent access to victim environments.” 


The security of our build systems is something that I’ve talked about before.  It’s a huge value target for advanced attackers due to the level of access that it can get, and the level of trust that has to be built in. 


