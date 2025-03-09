---
title: "169 - Knowing how it’s used"
date: 2021-10-03
description: "The products and services that we offer to our users and customers is something we can only improve if we actually understand how it is being used."
permalink: /knowing-how-its-used/
---

The products and services that we offer to our users and customers is something we can only improve if we actually understand how it is being used.

In one of my first experiences with watching user research, nearly a decade ago, I watched a set of people try to interact with a website I had worked on.  I had spent time thinking about what order to ask questions, and what input pickers to use, but my users struggled with things that I hadn’t even considered were things.  From scrolling into the footer, to understanding how to click and select things, skills that are as natural to me as breathing proved to be a challange to my users.

This resulted in my team heavily stripping back the user interface, and spending less time worrying about more complex interactions and instead aiming for something as simple as possible.

The same is true of our other technologies and security processes as well.  How do developers find out how to use your API, how to follow your process, or to get and use your advice?  If we don’t make an effort to understand where our users are, how they think about our systems and what they are trying to achieve, then we are always doomed to fail at getting them used.

## [Kids who grew up with search engines could change STEM education forever - The Verge](https://www.theverge.com/22684730/students-file-folder-directory-structure-education-gen-z)

[https://www.theverge.com/22684730/students-file-folder-directory-structure-education-gen-z](https://www.theverge.com/22684730/students-file-folder-directory-structure-education-gen-z)

> Catherine Garland, an astrophysicist, started seeing the problem in 2017. She was teaching an engineering course, and her students were using simulation software to model turbines for jet engines. She’d laid out the assignment clearly, but student after student was calling her over for help. They were all getting the same error message: The program couldn’t find their files.
> 
> Garland thought it would be an easy fix. She asked each student where they’d saved their project. Could they be on the desktop? Perhaps in the shared drive? But over and over, she was met with confusion. “What are you talking about?” multiple students inquired. Not only did they not know where their files were saved — they didn’t understand the question.
> 
> Gradually, Garland came to the same realization that many of her fellow educators have reached in the past four years: the concept of file folders and directories, essential to previous generations’ understanding of computers, is gibberish to many modern students


This is a good reminder that you need to conduct and watch real users using your systems, whether it be computer systems or security processes.  Real people don’t think the way that we do, and you wont learn how they think unless you meet them where they are.


## [Code Patterns for API Authorization: Designing for Security – NCC Group Research](https://research.nccgroup.com/2020/04/21/code-patterns-for-api-authorization-designing-for-security/)

[https://research.nccgroup.com/2020/04/21/code-patterns-for-api-authorization-designing-for-security/](https://research.nccgroup.com/2020/04/21/code-patterns-for-api-authorization-designing-for-security/)

> In the course of around 5 years at NCC Group, I’d estimate that I’ve worked on more than 50 source-code-assisted web application assessments. One major takeaway I’ve had is that the security of large applications is a reflection of the coding patterns used in the internal codebase. If there are dangerous (code) APIs available internally, security issues will show up externally when those APIs are used without safety checks.
> 
> This isn’t a new idea – awareness of unsafe code APIs has been around for many years. Probably one of the earliest examples was the industry push to migrate C code to using safer functions when operating on strings and arrays (e.g. strcpy vs. strcpy_s). More recently, React chose the name dangerouslySetInnerHTML, instead of innerHTML, in order to better warn developers aware of the security issues with that API.
> 
> The same idea applies to the code used in a web application when implementing authorization controls. When designing a new application, it’s important to create APIs which enforce safe data access across the codebase. The APIs determine whether vulnerabilities are introduced that allow attackers to bypass the application’s authorization controls, escalating privileges or attacking other users. Everyone makes mistakes, but safe APIs make it easier to code without causing vulnerabilities, making the application much more secure.


API access control is not a subject that comes up very often, and when it does it's often focused on the API as an end user consumption point.

But internal API's are far less likely to be audited and viewed as "safe" because only internal users can get to them.  But in many cases a simple reflection attack in any application on your estate will give the attacker access to almost all internal API's.

This is some good guidance for patterns for auditing and writing good secure API's in your code base.


## [Russia tells UN it wants vast expansion of cybercrime offenses, plus network backdoors, online censorship | The Register](https://www.theregister.com/2021/08/03/russia_cybercrime_laws/)

[https://www.theregister.com/2021/08/03/russia_cybercrime_laws/](https://www.theregister.com/2021/08/03/russia_cybercrime_laws/)

> The proposal, titled "United Nations Convention on Countering the Use of Information and Communications Technologies for Criminal Purposes," [PDF](https://drive.google.com/file/d/1fmyWKNcmskp8t_Q8Qya0jA999itYvGY-/view?usp=sharing) calls for member states to develop domestic laws to punish a far broader set of offenses than current international rules recognize.
> [...]
> [Via Twitter](https://twitter.com/lukOlejnik/status/1421525550212993027?s=20), Dr Lukasz Olejnik, independent cybersecurity researcher and consultant, noted that the draft convention disallows online communication calling for "subversive or armed activities directed towards the violent overthrow of the regime of another State," and requires service providers to provide "technical assistance," which generally means providing a backdoor for authorities.


([Joel](https://twitter.com/joelgsamuel)) This isn't a new proposal from Russia, and the article references back to some from 2011. The timing of this makes me believe that Russia is responding to pressure from the US but these things also take time to develop.

In some cases you have to read between the lines, but as per Olejnik's thread on Twitter, there are some things in the proposal that are highly likely to be used for State control.

Proposals, agreement and even Member States creating domestic statues are not the hardest parts of the battle. They are all meaningless unless consistently applied through the direction/focus of law enforcement followed up by prosecution and convictions (over a long period of time, as opposed to burst token arrests). Russia's commitment to dealing with cyber-active organised crime within their borders should be measured primarily on domestic judicial activity 'that sticks' when they aren't being pressured by other nations to do so.


## [T-Mobile Confirms It Was Hacked](https://www.vice.com/en/article/y3d4dw/t-mobile-confirms-it-was-hacked)

[https://www.vice.com/en/article/y3d4dw/t-mobile-confirms-it-was-hacked](https://www.vice.com/en/article/y3d4dw/t-mobile-confirms-it-was-hacked)

> We have determined that unauthorized access to some T-Mobile data occurred, however we have not yet determined that there is any personal customer data involved," T-Mobile wrote in its new announcement. "This investigation will take some time but we are working with the highest degree of urgency. Until we have completed this assessment we cannot confirm the reported number of records affected or the validity of statements made by others," the announcement added.
> 
> The seller told Motherboard that 100 million people had their data compromised in the breach. In the forum post, they were offering data on 30 million people for 6 bitcoin, or around $270,000.
> 
> Motherboard has seen samples of the data, and confirmed they contained accurate information on T-Mobile customers. The data includes social security numbers, phone numbers, names, physical addresses, unique IMEI numbers, and driver license information, the seller said.


This was from last month, but the breach seems to have gone quiet since.  This is a lot of personal data, and includes, as always, lots that can result in identity theft or pretext phishing attacks.


## [Symphony Technology Group Announces Bryan Palma Appointment | Business Wire](https://www.businesswire.com/news/home/20210930005086/en/Symphony-Technology-Group-Announces-Bryan-Palma-Appointment)

[https://www.businesswire.com/news/home/20210930005086/en/Symphony-Technology-Group-Announces-Bryan-Palma-Appointment](https://www.businesswire.com/news/home/20210930005086/en/Symphony-Technology-Group-Announces-Bryan-Palma-Appointment)

> The combination of McAfee Enterprise and FireEye Products will immediately create a pure play, cybersecurity market leader with more than 40,000 customers, 5,000 employees, and nearly $2B of revenue. The new company’s integrated security portfolio protects customers across endpoints, infrastructure, applications, and in the cloud. STG anticipates combining the two companies during the fourth quarter of 2021.


That’s quite the buy, and could well have an impact on the cybersecurity market.  Lets wait to see what the change is.


## [A Deeper Look at Phishing Against Bellingcat Staff Investigating Russia](https://www.riskiq.com/blog/labs/bellingcat-phishing/)

[https://www.riskiq.com/blog/labs/bellingcat-phishing/](https://www.riskiq.com/blog/labs/bellingcat-phishing/)

> Highly focused, the phishing campaign targeted only ten individuals, who have been identified by investigative journalist Christo Grozev. These include some researchers who do not work for Bellingcat but do investigate Russia.
> 
> ProtonMail, the email service used in the attack, published a short statement, which included some fascinating details on the attack from their perspective.
> 
> [...]
> 
> The attackers sent emails to a very select pool of targets indicating a possible breach of the integrity of the target’s ProtonMail account. Under the subject line, “Someone exported your encryption keys,” the attackers sent the following message:
> 
> In this article, we’ll explore a different angle to the phishing campaign against Bellingcat by analyzing it from the outside-in perspective of RiskIQ.
> 
> The July emails contained links to mail.protonmail.sh, with links to /password and /keys. These URLs redirected targets towards the final phishing pages on a new host, mailprotonmail.ch. Interestingly, the exact visited URLs wouldn’t matter; the server behind mail.protonmail.sh was instructed to always 301 redirect visitors to mailprotonmail.ch:


A lovely (and old) deep dive into a highly competent phishing campaign


## [On Computer Passwords](https://syfuhs.net/on-computer-passwords)

[https://syfuhs.net/on-computer-passwords](https://syfuhs.net/on-computer-passwords)

> Your computer has an account in Active Directory and that account has a password. This account is what makes Kerberos work. When you want to communicate with this computer you encrypt tickets to the account password.
> 
> When your computer wants to act as itself on the network (instead of, say, you) it uses it's password to authenticate to the domain controller. Things running as SYSTEM or NETWORK SERVICE operate as the computer account on the network.
> 
> That's why you see COMPUTERNAME$ in DC event logs. Because it's literally the computer account authenticating to-and-fro.
> 
> But the thing people get wrong repeatedly is how this account password is managed.


In a spate of “I didn’t know this”, I never knew how computer accounts are managed on windows 


## [New Azure Active Directory password brute-forcing flaw has no fix | arstechnica](https://arstechnica.com/information-technology/2021/09/new-azure-active-directory-password-brute-forcing-flaw-has-no-fix/)

[https://arstechnica.com/information-technology/2021/09/new-azure-active-directory-password-brute-forcing-flaw-has-no-fix/](https://arstechnica.com/information-technology/2021/09/new-azure-active-directory-password-brute-forcing-flaw-has-no-fix/)

> Imagine having unlimited attempts to guess someone's username and password without getting caught. That would make an ideal scenario for a stealthy threat actor—leaving server admins with little to no visibility into the attacker's actions, let alone the possibility of blocking them.
> 
> A newly discovered bug in Microsoft Azure's Active Directory (AD) implementation allows just that: single-factor brute-forcing of a user's AD credentials. And, these attempts aren't logged on to the server.
> [...]
> Microsoft seems to consider this a design choice, rather than a vulnerability. As such, it remains unclear if or when the flaw would be fixed, and organizations could remain vulnerable to stealthy brute-force attacks.


([Joel](https://twitter.com/joelgsamuel)) This is a... poor show by Microsoft.

The "without generating sign-in events in the targeted organization's tenant" is the kicker for me. It goes beyond it being an issue that customers themselves could write detection rules for - its entirely opaque _and_ Microsoft doesn't seem to intend to do anything about it.

Hopefully all accounts will be using multi-factor authentication (!) which will dramatically reduce the probability of impact (by over 95% I suspect) however that isn't an excuse to leave the first factor vulnerable.

I am finding it increasingly difficult to take Microsoft seriously as a security vendor, or technology vendor with a serious investment in security. They have either lost control of product security governance or something worse. It will take some time for me to take them seriously again.


