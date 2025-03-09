---
title: "185 - Classifying data properly"
date: 2022-02-20
description: "It's nice to imagine a world with proper classifications and access control systems."
permalink: /classifying-data-properly/
---

It's nice to imagine a world with proper classifications and access control systems.

You can read declassified US reports and see examples where every single paragraph contains a portion marking, an indicator that this portion of the document bears a classification that might be different to the whole document.

In a security fantasists' world, this means that we can automatically apply rules to determine who can see the document, where it can be stored, sent and managed.

But in reality, people are in fact still just people at the end of the day.  Classifying documents is really difficult to do, and so users get it wrong, a lot!

This means that our dreams of appropriately compartmenting information to protect against insiders getting access to all the things that they want to access is something that is beyond the reaches of anyone but intelligence agencies or those with a really important reason to successfully compartment information.

The reason that this is hard is because humans tend to only be good with a limited number of mental buckets.  If, using the [UK Government's system](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/715778/May-2018_Government-Security-Classifications-2.pdf), I asked you to determine if a given piece of information was Official, Secret or Top Secret, you'd probably make a good stab at it.  But in old money, the UK used to have a more complex system that included "not protectively marked", unclassified, protect, restricted, confidential, secret and top secret.  Now you have to understand the difference between restricted and confidential to make a decision.  

Furthermore, classifications nerds like me enjoy the ability to subdivide classifications down into even more buckets. In the US, the [Intelligence Community Markings Manual](https://www.dni.gov/files/documents/FOIA/2016_IC_Markings_System_Register_and_Manual_Redacted_Stamped-DF-2019-00061.pdf) runs to nearly 200 pages, and explains in excruciating detail how the portion marks work, what a trigraph is, and how to read something with SAP and SCI markings.

Now you can imagine you are a desk officer looking at writing a report, and you are trying to decide whether your email to your coworker asking for some extra detail about something sensitive should be marked with //SI-EEE JJJ-G YYYY//NOFORN or //SI-EEE KKK-GYYY//NOFORN

Information theorists love these systems, and they feel like it gives us a sense of control, with millions of classified US Government documents being created and classified every year, they feel like it means that the documents are appropriately controlled, and that nobody except those with a strict need to know can access them.

But as the Snowden leaks showed, underneath all of this joyful academic exercise is real file systems with real documents, and someone needs to manage them all, even if it's a sharepoint administrator who probably shouldn't be able to see everything at once.  

And then, finally, we come to the seniors in the organisation. These people often don't interact with the IT systems themselves, instead documents might be emailed, but more commonly they are often printed and taken out of their little protective bubble and handed over in dossiers.  These should of course be handled appropriately, and for government protected information there are laws in place for the correct handling of such material.  But it's also a system that starts to feel a little bit silly to such people, because it becomes their everyday experience of being given these files, and having to store them and have them around, and they lose their magical potency.

This is the same information handling risk in government as we see in corporate organisations,  We think that we have an effective information control mechanism, but the reality of how people work, and how they interact is that they make thousands of decisions a day about what to disclose to the people around them.  From working out how to talk about new strategies, to mergers and acquisitions, to talking about whether coworkers performance ratings or bonuses are up to scratch.  

It's also the same information handling risk that underlies data protection, and how we take care of personal data that is entrusted to us.  What systems and companies can we hand that data over to in order to store, process and manage it properly?

When we build a theoretical model that no longer matches people's behaviours, it can grow into a huge unseen problem for the organisation, because in our theoretical model, information is being appropriately handled, but real users are working outside our model and doing things that they feel is acceptable, but breaks the security model.

Much like the zero-trust stuff from last week, many of the models that we as security people create, are not rigorously tested against actual user behaviours.  We constantly see security gaps where real people, trying to get a real thing done, go around our security model.  We must remember that usability almost always trumps theoretical security.

## [When the insider threat is the Commander in Chief | CSO Online ](https://www.csoonline.com/article/3650036/when-the-insider-threat-is-the-commander-in-chief.html#jump)

[https://www.csoonline.com/article/3650036/when-the-insider-threat-is-the-commander-in-chief.html#jump](https://www.csoonline.com/article/3650036/when-the-insider-threat-is-the-commander-in-chief.html#jump)

> Classified information is handled on a need-to-know basis within the United States government and requires the information to be handled in a secure manner. The White House Communications Agency (WHCA) is charged with ensuring classified materials within the White House are afforded secure handling at all times. Those entrusted with a national security clearance as also expected to self-report any mishandling of classified information, be it leaving a piece of classified paper not secured or forgetting to lock a safe at close of business. Furthermore, discovery of classified materials outside of an approved secure environment warrants both reporting and investigation. 


Classifications are really really hard.  Pretty much everyone agrees in principle with these very theoretical models, that data must be handled on a need to know basis, but in 2005, [the new york times reported that the US Government classified 125 new documents every single minute, for a total of 15.6 million documents a year](https://www.nytimes.com/2005/07/03/politics/increase-in-the-number-of-documents-classified-by-the-government.html) .  In 2012, the last ISOO report into the cost of the classification system in the US states that it [costs about $9.7bn to maintain the classification system](https://www.archives.gov/files/isoo/reports/2012-cost-report.pdf), and the secure requirements that go around it.

Classifications are really complex, and in reality, if you work with highly classified documents all the time, much of them become a bit meaningless.  If you are the president, you regularly have papers delivered, including a daily brief that is highly classified.  The minutes of many of your phone calls are marked with caveats like ORCON, and almost every piece of paper you look at is considered sensitive in some way shape or form.  Within these boundaries, when, as a quote I cannot find the source for, but a senior US Official described that he would regularly receive internal emails arranging lunch that were marked at Top Secret, this means that real normal users struggle to understand what classifications really mean, and what they can or can’t do with the documents. 


## [A Journey in Organizational Resilience: Insider Threats](https://securityintelligence.com/organizational-resilience-insider-threats/)

[https://securityintelligence.com/organizational-resilience-insider-threats/](https://securityintelligence.com/organizational-resilience-insider-threats/)

> It is hard to find another single threat that can cause so much damage at one time. The insider needs time, determination, patience, reconnaissance, knowledge of inner workings and knowing when to strike. These qualities differ little from nation-state actors and their advanced persistent threats (APTs).
> 
> In essence, the successful insider is the black swan event: the low probability, high impact event. If you think it cannot happen, there are a few government agencies and large enterprises that may think otherwise.
> 
> So, how do we minimize risk from insiders? Well, it is a matter of both carrot and stick. Going too far one way can have the exact opposite intent and create an entirely new breed of insider threats you never planned for in the first place. Therefore, balance your reaction based on awareness, culture, operational needs and, of course, risk tolerance.
> 
> Turning the Insider Into a Partner
> 
> The insider threat that is lazy, clumsy and stupid is not your worry. Yes, they could cause damage along the way, but won’t do a lot of harm. For insiders like this, you will likely turn to technology and automation to detect odd behavior. And the tech will likely do a good job. All of these protective actions fall within your identity and access management, data loss prevention and your user behavior analytic strategies.
> 
> When it comes to insider threats, these solutions are actually the ‘easy’ ones. They require:
> 
> * Leadership support
> * Financial support
> * People support, to both deploy and maintain
> * Patience, for training and configuration
> * Staying up to date with current trends.
> 
> Of course, you understand why the word easy is in quotes. But with real support and some good frameworks and guidance, you can make some major progress protecting against insider threats.
> 
> The ‘hard’ solutions are much less focused on tech. Instead, they focus on culture, emotions, awareness, incentives and even discipline. Therefore, improving your cybersecurity and organizational resilience posture requires turning prospective and even active insider threats into partners. Put another way: give them a reason not to become a threat.


As it says here, Insiders are the Black Swan event for most organisations.  It's hihgly unlikely, but it's the worst possible impact.  

Insider threats are a good example of how risk management often doesn't work well.  Are you considering the likelihood of Fred, the desk analyst in operations deciding to steal paper or leak a single piece of work they are working on, or are you considering Sue, the network admin with the keys the kingdom?  These risks are wildly different to each other, but they all tend to be lumped into the same category.

The coping strategies here are the right ones, and they're all the strategies for keeping your best staff, and motivating everyone and getting the best out of everyone, so it's win-win-win right?


## [BeyondCorp is dead, long live BeyondCorp ](https://mayakaczorowski.com/blogs/beyondcorp-is-dead)

[https://mayakaczorowski.com/blogs/beyondcorp-is-dead](https://mayakaczorowski.com/blogs/beyondcorp-is-dead)

> BeyondCorp is the gold standard of what we should all aim for when designing zero trust architectures—including what the US government is now mandating. **There’s one problem: a fully zero trust architecture is incredibly difficult and incredibly expensive to deploy, and arguably, no one has ever achieved it.
> Even Google’s BeyondCorp isn’t a fully zero trust architecture** Google adopted its zero trust architecture of BeyondCorp gradually, targeting both greenfield and brownfield applications, over the span of several years. Today, still, BeyondCorp isn’t 100% rolled out at Google. It never will be. There will always be a gap of enterprise applications or new tools being introduced which require work to integrate.
> 
> Like any system, there are exceptions—and those exceptions become more and more expensive (and therefore unworthwhile) to address. Citing another of the BeyondCorp papers :
> > Despite all the best efforts to define, roll out, measure, and enforce controls, you may inevitably face the harsh reality that 100% uniform control deployment is a mythical state where unicorns frolic unconcerned about malware and state-sponsored attackers.
> 
> Google has already invested substantial resources, over many many years, in developing BeyondCorp:
> > Fully achieving the goals outlined in this paper (and the more general goals of BeyondCorp) requires significant resources.
> 
> If it’s “significant resources” at Google scale, it must be a massive investment. I would venture to say that if a VP knew the initial cost and time it would actually take, they might not have made that investment. 


This mostly echos my thoughts from last week.  I note that Maya, like me last week, mostly focuses on just how mind numbingly difficult it is to do devices as well as identities.  We’re both avoiding mentioning that the really really difficult bit is the concept of dynamic policies that act on the data from the devices and identities.  

Google’s Identity Aware Proxy from Google Compute is a good starter for this stuff, but any access policy has to understand so much about the context of every single application that a single proxy is really tricky.  Is /view/job.cgi?jobid=192 more sensitive than /view/job.cgi?jobid=1203?  What if job 192 is a new starter ticket for payroll with bank account details, but just 1203 is a new starter ticket for a trello board to be created?

Identifying your users is hard.  Identifying and attesting to the security of devices is really really hard, but writing, debugging and maintaining an access control policy for any decent sized organisation might be impossible. 


## [Top 10 web hacking techniques of 2021 | PortSwigger Research ](https://portswigger.net/research/top-10-web-hacking-techniques-of-2021)

[https://portswigger.net/research/top-10-web-hacking-techniques-of-2021](https://portswigger.net/research/top-10-web-hacking-techniques-of-2021)

> **1 - Dependency Confusion** Some of the best research has an elegant simplicity that makes it seem deceptively obvious in hindsight. In Dependency Confusion , Alex Birsan exposes critical design and configuration flaws affecting major package managers, exploiting package name ambiguity to achieve RCE on numerous major companies and earn well over $100k in bounties. Beyond the crazy impact, it's also exceptionally well-explained, taking the reader through the entire research journey.
> 
> Discussions and mitigations are still underway for this attack, and we're really curious to see where this avenue of research goes next. Is the attack so elegant it can't be improved? Or is this just the humble beginning of a persistent new attack class? 
> 
> What we do know is if you're only going to read one piece of research this year, you should make it Dependency Confusion. Congratulations to Alex on a well deserved win! 


10 lovely sets of attack vectors that should be at the front of red teams toolboxes this year.  The number 1 win, dependency confusion is complex to pull off, especially as an ethical red-team, but something that every blue team should consider how they can defend against 


## [DHS Launches First-Ever Cyber Safety Review Board | Homeland Security ](https://www.dhs.gov/news/2022/02/03/dhs-launches-first-ever-cyber-safety-review-board)

[https://www.dhs.gov/news/2022/02/03/dhs-launches-first-ever-cyber-safety-review-board](https://www.dhs.gov/news/2022/02/03/dhs-launches-first-ever-cyber-safety-review-board)

> The CSRB will review and assess significant cybersecurity events so that government, industry, and the broader security community can better protect our nation’s networks and infrastructure. The CSRB’s first review will focus on the vulnerabilities discovered in late 2021 in the widely used log4j software library. These vulnerabilities, which are being exploited by a growing set of threat actors, present an urgent challenge to network defenders. As one of the most serious vulnerabilities discovered in recent years, its examination will generate many lessons learned for the cybersecurity community. Together, the White House and DHS determined that focusing on this vulnerability and its associated remediation process was the most important first use of the CSRB’s expertise.
> 
> [...]
> 
> The CSRB’s first report, which will be delivered this summer, will include the following:
> * a review and assessment of vulnerabilities associated with the Log4j software library, to include associated threat activity and known impacts, as well as actions taken by both the government and the private sector to mitigate the impact of such vulnerabilities;
> * recommendations for addressing any ongoing vulnerabilities and threat activity; and,
> * recommendations for improving cybersecurity and incident response practices and policy based on lessons learned from the Log4j vulnerability. 


This is a big deal in the US as well.  Some of the smartest security people have long looked at Safety, and the formation of the NTSB as a key enabler in improving aviation safety.  While security is not the same as safety, there’s a lot of similarities in how we can approach this.

It’s really good to see that they want to make the information open and public, something the NTSB thrives on, but we’ll have to watch to see how effective it is. 


## [Charting TA2541's Flight  | Proofpoint US ](https://www.proofpoint.com/us/blog/threat-insight/charting-ta2541s-flight)

[https://www.proofpoint.com/us/blog/threat-insight/charting-ta2541s-flight](https://www.proofpoint.com/us/blog/threat-insight/charting-ta2541s-flight)

> TA2541 is a persistent cybercriminal actor that distributes various remote access trojans (RATs) targeting the aviation, aerospace, transportation, and defense industries, among others. Proofpoint has tracked this threat actor since 2017, and it has used consistent tactics, techniques, and procedures (TTPs) in that time. Entities in the targeted sectors should be aware of the actor's TTPs and use the information provided for hunting and detection.
> 
> TA2541 uses themes related to aviation, transportation, and travel. When Proofpoint first started tracking this actor, the group sent macro-laden Microsoft Word attachments that downloaded the RAT payload. The group pivoted, and now they more frequently send messages with links to cloud services such as Google Drive hosting the payload. Proofpoint assesses TA2541 is a cybercriminal threat actor due to its use of specific commodity malware, broad targeting with high volume messages, and command and control infrastructure.
> 
> While public reporting detailing similar threat activities exists since at least 2019, this is the first time Proofpoint is sharing comprehensive details linking public and private data under one threat activity cluster we call TA2541. 


This one is interesting mostly because Proofpoint doesn’t seem to link this activity to any specific damage or intent.  So what does this group want with it’s activities?  It’s unclear whether this has financial motivations, whether they’re just selling credentials on, or something else 


## [Discussions · cisagov/bad-practices ](https://github.com/cisagov/bad-practices/discussions)

[https://github.com/cisagov/bad-practices/discussions](https://github.com/cisagov/bad-practices/discussions)

> **Welcome to CISA's Bad Practices Catalog Discussions** 


This is a fascinating idea, and I’m unsure if this will go well, or badly.  Knowing the infosec community, this could go horribly wrong.

CISA are trying to document bad practice, such as allowing administrators to administrate critical national infrastructure from admin accounts that they use to browse reddit.
At the time of browsing, “Force users to change their passwords”, is top of the discussion list, but we’ll see whether regressive security policy suggestions like “let users click links in emails” float to the top or not. 


## [My journey down the rabbit hole of every journalist’s favorite app - POLITICO ](https://www.politico.com/news/2022/02/16/my-journey-down-the-rabbit-hole-of-every-journalists-favorite-app-00009216)

[https://www.politico.com/news/2022/02/16/my-journey-down-the-rabbit-hole-of-every-journalists-favorite-app-00009216](https://www.politico.com/news/2022/02/16/my-journey-down-the-rabbit-hole-of-every-journalists-favorite-app-00009216)

> **So when I talked to Aksu in November, I made sure to use Signal, an encrypted phone app, to protect our discussion about psychological trauma afflicting Uyghurs overseas.**  **The next day, I received an odd note from Otter.ai, the automated transcription app that I had used to record the interview. It read: “Hey Phelim, to help us improve your Otter’s experience, what was the purpose of this particular recording with titled ‘Mustafa Aksu’ created at ‘2021-11-08 11:02:41’?”
> 
> [...]
> 
> I contacted Otter to verify if this was indeed a real survey or some clever phishing ruse. An initial confirmation that the survey was legitimate was followed by a denial from the same Otter representative, laced with a warning that I “not respond to that survey and delete it.” My communications with Otter were all restricted to email and were sporadic, often confusing and contradictory.**  **In the three months since that initial exchange (and there was more to come), I’ve gone down the rabbit hole — talking to cybersecurity experts, press freedom advocates and a former government official — to try and understand what vulnerabilities and risks are present in this app that’s become a favorite among journalists for its fast, reliable and cheap automated transcription.** 


I’ve talked about this before, but the security of the most useful SaaS applications is a critical part of modern security, and yet most internal security teams view it as either out of their control, or forbid access to all applications by default.

We need to work out how to make it simple and easy for people to do their jobs, to use the applications that have a great experience, and yet ensure that they can make good choices about the privacy of the data in the app.

For those who haven’t read it all, this mostly turns out to be a bit of red herring, there was no compromise of data, it was just automated surveys by Otter.ai, but it was really hard for Phelim to verify that, and there’s very little confidence that had there been a national security concern from some nation state, whether they would know the data was handed over or not. 


## [Why Hunting For LOLBINs Is One Of The Best Bets | by Nasreddine Bencherchali | Feb, 2022 | Medium](https://nasbench.medium.com/why-hunting-for-lolbins-is-one-of-the-best-bets-e5e58e1619c2)

[https://nasbench.medium.com/why-hunting-for-lolbins-is-one-of-the-best-bets-e5e58e1619c2](https://nasbench.medium.com/why-hunting-for-lolbins-is-one-of-the-best-bets-e5e58e1619c2)

> Now, we might talk about the latest C2 framework and how it’ll offer command line obfuscation, parent/child spoofing, EDR unhooking, Direct Syscal invokes, and some other shenanigans that I’m not even aware of and while there is a thread of truth in those statements and attackers are certainly using these “advanced” techniques. The fact of the matter is attacks happen in a chain and in this chain often time than not LOLBINs are a big part of it.


This is a nice breakdown on why you should still be spending some of your detective capabilities looking for malicious use of LOLBins.

Yes, bad attackers might use really advanced techniques, but look for the fundamentals that are easy for all attackers before you look for the complex that's only used by a minority of attackers


## [Never Use Text Pixelation To Redact Sensitive Information | Bishop Fox](https://bishopfox.com/blog/unredacter-tool-never-pixelation)

[https://bishopfox.com/blog/unredacter-tool-never-pixelation](https://bishopfox.com/blog/unredacter-tool-never-pixelation)

> We write a lot of reports at Bishop Fox (it’s what happens when you hack all the things). This frequently results in needing to redact certain text. We have a long-standing policy that when you redact text, the only way to do it securely is to use black bars. Sometimes, people like to be clever and try some other redaction techniques like blurring, swirling, or pixelation. But this is a mistake.
> 
> Today, we’re focusing on one such technique – pixelation – and will show you why it’s a no-good, bad, insecure, surefire way to get your sensitive data leaked. To show you why, I wrote a tool called Unredacter that takes redacted pixelized text and reverses it back into its unredacted form. There’s plenty of real-world examples of this in the wild to redact sensitive information, but I won’t name names here.


This is a lovely writeup of how to unredact blurred text in redacted reports.


