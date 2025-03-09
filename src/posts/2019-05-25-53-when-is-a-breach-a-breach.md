---
title: "53 - When is a breach a breach?"
date: 2019-05-25
description: "In risk management, and data protection, we tend to assume the worst.  That if we've exposed the data of millions of users, that someone has actively exploited it and done terrible things with it."
permalink: /when-is-a-breach-a-breach/
---

In risk management, and data protection, we tend to assume the worst.  That if we've exposed the data of millions of users, that someone has actively exploited it and done terrible things with it.

But the reality isn't like that most of the time for most of us.  These huge data breaches that happen all the time show up to have very little impact on real users.  It's incredibly hard to get any reliable statistics about identity fraud caused by data breaches.  It clearly happens, and when the police capture fraudsters, they often find that they had access to large amounts of user data, but it's very hard to draw a specific link.

I don't necessarily mind that we are pessimists about data breaches, that in risk management we prepare for the worst, because if we're prepared for the worst, then if it's not as bad as we thought, then our systems should respond better.

But it does cause us to make weird decisions sometimes.  I've sat in meetings talking about risk, and the ever present advanced persistent threats tend to outweigh doing the simple easy stuff, because the risk management processes look at risk as "Likelihood times Impact".  But the impact is always the worst case, and we don't have a good way to model "likely impact" or "median impact" instead.

Sensible thinking should lead you to the view that the most common breach, with middling to low impact, is password stuffing and account compromise.  We know that solving this is easy, simple and fast with things like 2FA.  But instead we end up discussing the weaknesses of the global telecommunications system and whether the SMS will transit a Huawei switch at any point before reaching the user, or whether a users mobile phone is truly a second factor if they're also browsing on it.  The highly unlikely, but huge impact stuff dominates our thinking and prevents simple pragmatic solutions from being used.

The oft quoted "Perfect is the enemy of good" is a good phrase to remember.  We try so hard to model everything, and to worry about the really hard and difficult stuff, and not enough time just delivering the good stuff we can do now.

## [The Spies Who Came In From the Continent – Foreign Policy](https://foreignpolicy.com/2019/04/27/the-spies-who-came-in-from-the-continent-espionage-britain-brexit/)

[https://foreignpolicy.com/2019/04/27/the-spies-who-came-in-from-the-continent-espionage-britain-brexit/](https://foreignpolicy.com/2019/04/27/the-spies-who-came-in-from-the-continent-espionage-britain-brexit/)

> Brexit will force Britain’s intelligence services to answer uncomfortable questions they have not had to confront since World War II: What can they offer that others cannot? That Brexit is taking place at the same time as the cyber-revolution, however, offers opportunities for Britain to maintain some semblance of its current global power. Investing in digital intelligence offers London the best—and perhaps only—way out of the strategic intelligence quagmire Brexit has placed it in.


This is a fun read on some of the historical achievements of the UK's intelligence services, as well as some questions and suggestions for how the UK can turn it's intelligence apparatus into an advantage in a post-brexit world.


## [Uber, Lyft drivers manipulate fares at Reagan National causing artificial price surges | WJLA](https://wjla.com/news/local/uber-and-lyft-drivers-fares-at-reagan-national)

[https://wjla.com/news/local/uber-and-lyft-drivers-fares-at-reagan-national](https://wjla.com/news/local/uber-and-lyft-drivers-fares-at-reagan-national)

> By turning off their apps at certain times, drivers are able to artificially manipulate the Uber and Lyft apps into higher fares.
> 
> “All the airplanes we know when they land. So five minutes before, we turn all our apps off all of us at the same time. All of us we turn our apps off. They surge, $10, $12, sometimes $19. Then we turn our app on. Everyone will get the surge,” one driver says.


Given any system with people with competing incentives, and they'll find a way to attempt to game the system to give themselves an advantage.  In this case, the taxi drivers are defrauding the fee paying taxi passengers by artificially raising the prices.  I suspect that Uber and Lyft will crack down on this, and then the next action will be how the taxi drivers coordinate to raise fares again.


## [RDP Stands for “Really DO Patch!” – Understanding the Wormable RDP Vulnerability CVE-2019-0708 | McAfee Blogs](https://securingtomorrow.mcafee.com/other-blogs/mcafee-labs/rdp-stands-for-really-do-patch-understanding-the-wormable-rdp-vulnerability-cve-2019-0708/)

[https://securingtomorrow.mcafee.com/other-blogs/mcafee-labs/rdp-stands-for-really-do-patch-understanding-the-wormable-rdp-vulnerability-cve-2019-0708/](https://securingtomorrow.mcafee.com/other-blogs/mcafee-labs/rdp-stands-for-really-do-patch-understanding-the-wormable-rdp-vulnerability-cve-2019-0708/)

> According to the advisory, the issue discovered was serious enough that it led to Remote Code Execution and was wormable, meaning it could spread automatically on unprotected systems. The bulletin referenced well-known network worm “WannaCry” which was heavily exploited just a couple of months after Microsoft released MS17-010 as a patch for the related vulnerability in March 2017. McAfee Advanced Threat Research has been analyzing this latest bug to help prevent a similar scenario and we are urging those with unpatched and affected systems to apply the patch for CVE-2019-0708 as soon as possible. It is extremely likely malicious actors have weaponized this bug and exploitation attempts will likely be observed in the wild in the very near future.


There is now a Metasploit plugin for this exploit as well, so this is going to become something that people try.  You should patch, you should add rules to your IDS/IPS systems to detect this attack and prevent it, and of course you should work out how to minimise the exploitable attack surface, remembering of course that your network perimeter is probably breached and attackers may well already have passwords for network based authentication as well.


## [Garbage In, Garbage Out | Spotlight on the New York Police Department](https://www.flawedfacedata.com/)

[https://www.flawedfacedata.com/](https://www.flawedfacedata.com/)

> with ones that more closely resemble those in mugshots—collected from photos of other people. Presentations and interviews about FIS include the following examples:
> 
> * "Removal of Facial Expression"—such as replacing an open mouth with a closed mouth. In one example provided in a NYPD presentation, detectives conducted "...a Google search for Black Male Model" whose lips were then pasted into the probe image over the suspect’s mouth.
> * "Insertion of Eyes"—the practice of "graphically replacing closed eyes with a set of open eyes in a probe image," generated from a Google search for a pair of open eyes.


This feels like madness.  The people building image recognition software don't intend it to be used like this, and the idea of people trusting the computer match and using it as evidence or a reason to arrest someone later is truly chilling.


## [As Far Right Rises, a Battle Over Security Agencies Grows - The New York Times](https://www.nytimes.com/2019/05/07/world/europe/austria-far-right-freedom-party.html)

[https://www.nytimes.com/2019/05/07/world/europe/austria-far-right-freedom-party.html](https://www.nytimes.com/2019/05/07/world/europe/austria-far-right-freedom-party.html)

> Shortly after the far-right Freedom Party joined the government 17 months ago, taking over the powerful Interior Ministry, the ministry’s top official asked Ms. Geissler and her boss to turn over the names of informants who had infiltrated the far-right scene.
> 
> They refused. Just weeks later, armed police burst into her office and carted away years’ worth of domestic files as well as intelligence from allied nations.
> 
> The consequences continue to reverberate through the country’s politics and beyond, and have made Austria an important test of what happens when the far right moves from the political fringe to the halls of power.


This is quite scary.  The Austrian equivalent of MI5 being asked to hand over files and intelligence it holds is one of the worries that we should have with our own governments within the UK and US.  

More concretely, the rise of populism across Europe means that intelligence agencies are sharing less stuff (see further down the article for examples of Austria being excluded from stuff), and that weakens us all when we cannot coordinate across Europe easily. 


## [NATO Cyber Defence Pledge conference: Foreign Secretary's speech - GOV.UK](https://www.gov.uk/government/speeches/foreign-secretary-speech-at-the-nato-cyber-pledge-conference)

[https://www.gov.uk/government/speeches/foreign-secretary-speech-at-the-nato-cyber-pledge-conference](https://www.gov.uk/government/speeches/foreign-secretary-speech-at-the-nato-cyber-pledge-conference)

> We cannot afford to wait until one of our adversaries succeeds in changing the result of an election. We must be crystal clear that any cyber operations designed to manipulate another country’s electoral system and alter the result would breach international law – and justify a proportionate response.
> 
> Together, we possess options for responding to any attacks that fall below the threshold for Article V. We should be prepared to use them.


I think this is an interesting public statement, that the UK is willing to use offensive cyber attacks as a form of military action, in what is determined as a proprtionate response.

More importantly, I still think this language about "cyber operations design to manipulate another county's electoral system", because it's very unclear whether anybody internationally has actually tried to hack a voting system effectively.  But disinformation campaigns are much harder to claim to cyber operations, so the language ties us into a framework that doesn't represent reality.


## [Burned After Reading: Endless Mayfly’s Ephemeral Disinformation Campaign - The Citizen Lab](https://citizenlab.ca/2019/05/burned-after-reading-endless-mayflys-ephemeral-disinformation-campaign/)

[https://citizenlab.ca/2019/05/burned-after-reading-endless-mayflys-ephemeral-disinformation-campaign/](https://citizenlab.ca/2019/05/burned-after-reading-endless-mayflys-ephemeral-disinformation-campaign/)

> This report employs a multidisciplinary approach to track and understand Endless Mayfly’s multi-platform, multi-narrative disinformation campaign. We use infrastructure analysis and open source intelligence techniques to characterize the scope and nature of Endless Mayfly’s Tactics, Techniques, and Procedures (TTPs). This technical research is paired with discourse analysis to understand the narratives Endless Mayfly deploys and leverages as part of their efforts to influence online conversations and, ultimately, attempt to achieve political outcomes.
> 
> We pay special attention to Endless Mayfly’s extensive use of ephemerality (by intentionally deleting content once it has been amplified) and tactical experimentation when seeding narratives, and reflect on what this means for the future of disinformation online. We discuss how these techniques can frustrate efforts by researchers to understand the objectives of a campaign and reach conclusive attribution.
> 
> [...]
> 
> Typically, after the inauthentic articles were posted to Twitter, amplified by third parties, or covered by mainstream media, Endless Mayfly deleted the content and redirected visitors to the legitimate media outlets that they were impersonating. The redirects were usually removed after some time and the website taken down.
> 
> The Endless Mayfly content, however, would often remain in the caches of social media platforms, leaving a trail of posts that appeared authentic at a cursory glance. Although the links no longer pointed to the article, clicking on the associated links would lead to the genuine news outlet, until the websites were taken down completely. This deceptive technique further amplified the sense of a genuine story. In other cases, Endless Mayfly tweeted screenshots of the spoofed websites and their falsified content, further cementing the impression of a legitimate story.


I've covered Russia and China's form of disinformation or propaganda campaigns, but this shows that Iran has been in on the action as well, running a campaign of disinformation since at least 2016.  

There's something quite slick about deleting the propaganda once it's done it's job, since the people you are trying to influence will only care when they read it, and only if it's recent, so a constantly changing set of news stories that atrophy over time is no great loss, and in fact makes it hard for people to go back and check where they heard something.   The fact that the information is cached in social media platforms (they mean facebook), so that it'll still appear in the news feed with the attacker controlled metadata is just icing on the top.


## [About security alerts for vulnerable dependencies - GitHub Help](https://help.github.com/en/articles/about-security-alerts-for-vulnerable-dependencies)

[https://help.github.com/en/articles/about-security-alerts-for-vulnerable-dependencies](https://help.github.com/en/articles/about-security-alerts-for-vulnerable-dependencies)

> When GitHub discovers or is notified of a new vulnerability, we identify public repositories (and private repositories that have opted in to vulnerability detection) that use the affected version of the dependency, send a security alert to repository maintainers, and generate an automated security fix.
> 
> Each security alert includes a severity level, a link to the affected file in your project, and a link to a pull request containing an automated security fix that resolves the vulnerability. When available, the alert will include further details about the vulnerability.


This has been previously automated by third parties like Snyk and Dependabot, but now Github offers it out of the box with their new dependancy graph tools.


## [Google Online Security Blog: New research: How effective is basic account hygiene at preventing hijacking](https://security.googleblog.com/2019/05/new-research-how-effective-is-basic.html)

[https://security.googleblog.com/2019/05/new-research-how-effective-is-basic.html](https://security.googleblog.com/2019/05/new-research-how-effective-is-basic.html)

> If you’ve signed into your phone or set up a recovery phone number, we can provide a similar level of protection to 2-Step Verification via device-based challenges. We found that an SMS code sent to a recovery phone number helped block 100% of automated bots, 96% of bulk phishing attacks, and 76% of targeted attacks. On-device prompts, a more secure replacement for SMS, helped prevent 100% of automated bots, 99% of bulk phishing attacks and 90% of targeted attacks.


This data is super useful.  I know people argue about the value of 2FA, whether SMS is safe since SS7 is such a shonky protocol and so forth.  But look, SMS based 2FA has 100% success rate against automated bots (that's password spraying I think) and a 96% rate against bulk phishing attacks.  That's the majority of almost every companies attacks they'll see.  Specific targeted attacks are rare, and much harder to protect against, and even then SMS 2FA handles 76% of them.  

Want a clear easy deliverable win?  Block 76% of the most capable attacks on your organisations data in one easy move, and turn on 2FA for your organisations email and SSO systems.   If you are using GSuite, Office 365 for core staff identity (and I think you should be), this is trivially easy to setup, turn on, and just works.


## [Which government department suffers the most data breaches? | PublicTechnology.net](https://www.publictechnology.net/articles/features/which-government-department-suffers-most-data-breaches)

[https://www.publictechnology.net/articles/features/which-government-department-suffers-most-data-breaches](https://www.publictechnology.net/articles/features/which-government-department-suffers-most-data-breaches)

> Examining data from five years’ worth of annual reports (see graph below - click on the image to open it in a new window, where it can be enlarged, magnified, and downloaded) reveals that the Ministry of Justice is responsible for far more incidents than any other government department. In 2017-18 it recorded 3,184 incidents, including 10 serious enough to be reported to the Information Commissioner’s Office. The Ministry of Defence, in second place, recorded just 117, with none reported to the ICO. The Home Office and the Department for Environment, Food and Rural Affairs recorded 66 and 62 respectively, while the Department for Work and Pensions recorded no incidents, despite handling information on most of the population.


I refuse to believe that the DWP had 0 incidents of data breach in the last 5 years.  It's just not possible that an organisation that size cannot have at least 1 case of a mistyped email address or printouts left on the printer.  

This suggests to me that the data provided here is just not valid data, presumably because it's unclear what constitutes a data breach, and how differently different departments treat their data breaches.  It could also be that some departments have poor controls for detecting data breaches, or poor processes for reporting them and recording them.

There's a lot of criticism here for the Ministry of Justice [Full disclosure: I'm currently contracting there] but it's possible to look at this in a good light and suggest that the Ministry has the best process for detecting, recording and responding to breaches.  I suspect it's somewhere in the middle, with aging legacy systems, complex operational concerns combined with good processes for recording and declaring those breaches.


## [First American Financial Corp. Leaked Hundreds of Millions of Title Insurance Records — Krebs on Security](https://krebsonsecurity.com/2019/05/first-american-financial-corp-leaked-hundreds-of-millions-of-title-insurance-records/)

[https://krebsonsecurity.com/2019/05/first-american-financial-corp-leaked-hundreds-of-millions-of-title-insurance-records/](https://krebsonsecurity.com/2019/05/first-american-financial-corp-leaked-hundreds-of-millions-of-title-insurance-records/)

> Earlier this week, KrebsOnSecurity was contacted by a real estate developer in Washington state who said he’d had little luck getting a response from the company about what he found, which was that a portion of its Web site (firstam.com) was leaking tens if not hundreds of millions of records. He said anyone who knew the URL for a valid document at the Web site could view other documents just by modifying a single digit in the link.
> 
> And this would potentially include anyone who’s ever been sent a document link via email by First American.
> 
> KrebsOnSecurity confirmed the real estate developer’s findings, which indicate that First American’s Web site exposed approximately 885 million files, the earliest dating back more than 16 years. No authentication was required to read the documents.


:facepalm:

But is this really a leak of 885 million files?  The possibility that those files were accessed in bulk by data harvesters and scammers exists, but that's not to actually say it happened.  


## [Phisher folk reel in Computacenter security vetting mailbox packed with sensitive staff data • The Register](https://www.theregister.co.uk/2019/05/23/computacenter_staff_security_clearance_application_mailbox_breached/)

[https://www.theregister.co.uk/2019/05/23/computacenter_staff_security_clearance_application_mailbox_breached/](https://www.theregister.co.uk/2019/05/23/computacenter_staff_security_clearance_application_mailbox_breached/)

> The mailbox was used to collate data from individuals when information relating to their security clearance applications was deemed to be missing or incorrect. The information requested could include ID data, contact details, bank details, addresses and employment history.
> 
> The "attacker" gained entry and changed the password for the mailbox, which system audit logs showed prevented further access by Computacenter. The mailbox was then used to send phishing emails.
> 
> "However, these logs cannot tell us precisely what was in the mailbox at the time of the attack or whether the data was exported or just deleted," the mail to staff stated.
> 
> On being made aware of the attack, Computacenter said it initiated the Group Information Assurance compliance methodology, establishing that other systems connected to the security vetting process were unaffected and "secure workaround processes for security clearance have been implemented".


Of all the things to have breached, the employee vetting system is one of the worst.  The OPM hack in the US was probably one of the scariest from an adversarial perspective.

I'm unsure about the wisdom of an organisation requiring that these sorts of files and identity documents be emailed to a shared mailbox in the first place, especially one managed and hosted by a third party.

Luckily it sounds like the attacker just wanted an email account to send phishing emails from and so probably didn't know what they stumbled across


