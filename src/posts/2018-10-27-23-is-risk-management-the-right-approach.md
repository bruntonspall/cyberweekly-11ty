---
title: "23 - Is risk management the right approach"
date: 2018-10-27
description: "I'm a big believer in risk management.  I think that security does depend on the context, and risk management is supposed to help you understand your context and take appropriate risks."
permalink: /is-risk-management-the-right-approach/
---

I'm a big believer in risk management.  I think that security does depend on the context, and risk management is supposed to help you understand your context and take appropriate risks.

But in reality, I'm not sure it's actually working.  A friend (and subscriber) recently commented to me that they like the concept of risk assessment in theory, but fail to find any evidence of where it has added any value in the real world that we move in.

This is a sad indictment of the current state of risk assessment, especially in Government.  There are lots of nice in theory ideas about risk assessments, but too frequently, the technical implementation is beyond the technical capabilities of the security person doing risk assessment, and the processes are not setup to deliver good actionable results.

The DIB paper on detecting Agile BS in the defence sector is a great summation of some of the critical questions you need to ask of a project to determine whether it is actually doing agile well.  Things like "Are teams empowered to change the requirements based on user feedback?" and "Is the full ecosystem of your project agile? (Agile programming teams followed by linear, bureaucratic deployment is a failure.)".  I wonder if we need something similar for detecting security BS both in risk management programs, and in security operations and engineering as well.

## [DIB: Detecting Agile BS](https://media.defense.gov/2018/Oct/09/2002049591/-1/-1/0/DIB_DETECTING_AGILE_BS_2018.10.05.PDF)

[https://media.defense.gov/2018/Oct/09/2002049591/-1/-1/0/DIB_DETECTING_AGILE_BS_2018.10.05.PDF](https://media.defense.gov/2018/Oct/09/2002049591/-1/-1/0/DIB_DETECTING_AGILE_BS_2018.10.05.PDF)

> Agile is a buzzword of software development, and so all DoD software development projects are, almost by default, now declared to be “agile.” The purpose of this document is to provide guidance to DoD program executives and acquisition professionals on how to detect software projects that are really using agile development versus those that are simply waterfall or spiral development in agile clothing (“agile-scrum-fall”). 


This guide is a great little take on how governance boards and senior executives can tell real agile projects from waterfall projects that have been merely rebranded into agile.

The questions at the end should form part of any assessment process you have for agile projects


## [Is your email account secure? | Action Fraud](https://www.actionfraud.police.uk/blog/is-your-email-account-secure)

[https://www.actionfraud.police.uk/blog/is-your-email-account-secure](https://www.actionfraud.police.uk/blog/is-your-email-account-secure)

> Cyber Aware has released the following tips as part of its #OneReset awareness campaign:
> 
> * Use a strong, separate password for your email.
> 
> * A good way to create a strong and memorable password is to use three random words. Numbers and symbols can be used to make it stronger.
> Use words which are memorable to you, but not easy for other people to guess. Don’t use words such as your child’s name or favourite sports team which are easy for people to guess by looking at your social media accounts or simple substitutions like ‘Pa55word!’.
> 
> * When available you should use two-factor authentication (2FA) on your email account. It gives it extra layer of security, as it means your account can only be accessed on a device that you have already registered.
> 
> * Don’t use public Wi-Fi to transfer sensitive information such as card details


I was with this as good actionable advice right up to the last line.

This last line is typical of security advice.  It doesn't explain why, it isn't at all realistic for the majority of the users reading it, and it offers no constructive alternative.

We need better security advice generally, and should hold groups like ActionFraud to a higher standard for this sort of advice.

The password advice is however much better and good advice for your core email password or password manager password



## [Yahoo must pay $50 million in damages for data breaches - The Verge](https://www.theverge.com/2018/10/24/18019092/yahoo-data-breach-pay-damages-us-israel)

[https://www.theverge.com/2018/10/24/18019092/yahoo-data-breach-pay-damages-us-israel](https://www.theverge.com/2018/10/24/18019092/yahoo-data-breach-pay-damages-us-israel)

> Yahoo has agreed to pay $50 million in damages for 200 million people in the US and Israel who had their personal data breached, according to the Associated Press. The company also has to provide users with credit monitoring services for two years. California federal court still has to approve the settlement before the payments can be granted


This feels unusual to me.  Most breaches tend to result in actions by information commissioners, and we've seen that fines are often not proportionate to the amount of data leaked.  The implication has always been that the fine goes from the company to Governments, rather than to the users whose data was lost.

This will amount to a $125 payout for anyone with a Yahoo account who was in the breach, but as an British national, I will of course not be eligible to apply for the protection or the payout.


## [British Airways warns that a further 185,000 customers were hit by security breach](https://www.computing.co.uk/ctg/news/3065198/british-airways-warns-that-a-further-185-000-customers-were-hit-by-security-breach)

[https://www.computing.co.uk/ctg/news/3065198/british-airways-warns-that-a-further-185-000-customers-were-hit-by-security-breach](https://www.computing.co.uk/ctg/news/3065198/british-airways-warns-that-a-further-185-000-customers-were-hit-by-security-breach)

> Now, British Airways has released an updated statement admitting that a further 185,000 customers could have been affected.
> 
> Its investigation, carried out with specialist cyber forensic investigators and the National Crime Agency, revealed that hackers "may have stolen" payment details, including CVV numbers, of an additional 77,000 customers.
> 
> A further 108,000 also saw their payment details, without CVV, "potentially compromised" during the incident.


The technical details on this are sparse, but it looks externally, like however the MageCart gang got their javascript onto the payment page may have also allowed them to compromise further systems.


## [Coats: ODNI has seen 'no evidence' of supply chain hack detailed in Bloomberg story](https://www.cyberscoop.com/dan-coats-bloomberg-supply-chain-the-big-hack/)

[https://www.cyberscoop.com/dan-coats-bloomberg-supply-chain-the-big-hack/](https://www.cyberscoop.com/dan-coats-bloomberg-supply-chain-the-big-hack/)

> Director of National Intelligence Dan Coats told CyberScoop on Thursday that he’s seen no evidence of Chinese actors tampering with motherboards made by Super Micro Computer, becoming the latest national security official to question a Bloomberg report that stated the company was the victim of a supply chain hack.
> 
> “We’ve seen no evidence of that, but we’re not taking anything for granted,” Coats told CyberScoop. “We haven’t seen anything, but we’re always watching.”


The Bloomberg story seems deader than ever, and yet Bloomberg still hasn't retracted the claim and has offered no further proof to back up the story.

I'm increasingly of the view that this was mistaken journalism, in that they never vetted the entire story with their sources, just verified individual claims and then drew implications from them. Hopefully journalists will be taking notes on how to get their stories vetted in future.   


## [Some notes for journalists about cybersecurity - Security Boulevard](https://securityboulevard.com/2018/10/some-notes-for-journalists-about-cybersecurity/)

[https://securityboulevard.com/2018/10/some-notes-for-journalists-about-cybersecurity/](https://securityboulevard.com/2018/10/some-notes-for-journalists-about-cybersecurity/)

> This is why I trust the high-tech industry press so much more than the mainstream press. Despite priding itself as the “newspaper of record”, on these technical issues the NYTimes is anything but. It’s the techy sites like Ars Technica and sometimes Wired that become the “paper of record” on things cyber. I mention this because David Sanger gets all the credit for Stuxnet reporting when he’s done a horrible job, while numerous techy sites have done the actual work figuring out what went on.


This is a good rundown of my issues with technology journalism as well.  Part of the problem is the lack fo technical training for journalists.  Very few have ever actually worked in tech, and so they kind of understand the technology, but not at a deep level, and this is where mistakes and misreporting happen


## [Should I Be Afraid of Election Hacking? | Time.com](http://time.com/5422261/should-you-be-afraid-of-election-hacking-heres-what-experts-say/)

[http://time.com/5422261/should-you-be-afraid-of-election-hacking-heres-what-experts-say/](http://time.com/5422261/should-you-be-afraid-of-election-hacking-heres-what-experts-say/)

> But it is possible to interpret some of Russia's broad goals. In addition to seeking to promote leaders who may ease economic sanctions and ignore Russia's aggression in Ukraine, Beyer says Moscow's hacking attempts may be part of an effort "to systematically undermine trust in U.S. ... institutions, exploiting our own divisions to create instability."


This was interesting to me.  All of the conversation online about election hacking has seemed to make the assumption that the interference was about selecting a specific leader.

But I suspect that it's far more likely that they just want increased discord and social instability because that makes the country less effective internationally.

As we see the influence operations online start to come into view, I predict that we are going to see influence operations in some of the most divisive debates of the last few years, probably on both sides of each debate.


## [Serious SSH bug lets crooks log in just by asking nicely… – Naked Security](https://nakedsecurity.sophos.com/2018/10/17/serious-ssh-bug-lets-crooks-log-in-just-by-asking-nicely/)

[https://nakedsecurity.sophos.com/2018/10/17/serious-ssh-bug-lets-crooks-log-in-just-by-asking-nicely/](https://nakedsecurity.sophos.com/2018/10/17/serious-ssh-bug-lets-crooks-log-in-just-by-asking-nicely/)

> Here’s the good news.
> 
> By far the most commonly used SSH version out there is an open source product called OpenSSH, created and maintained by the security-conscious folks at OpenBSD.
> 
> OpenSSH is a completely separate implementation to libssh – they don’t include or rely on each other’s code.


This bug has been much overplayed since almost nobody seems to be using libssh, preferring many alternative implementations.

However, it is a doozy of a bug, caused by a mistaken implementation of the state machine on the server side accepting an input that the server should never get in normal usage and using that input to set the state to be fully authenticated.  I think it's a good example of how complex software can get and how these kinds of bugs can slip in.


## [[Public] STRIDE Cue Cards - Google Slides](https://docs.google.com/presentation/d/1JQae3_BkcOr7pUlgwGznogrHXGE3x3cvkSOVsWH50yU/edit#slide=id.g43faa55bbf_0_50)

[https://docs.google.com/presentation/d/1JQae3_BkcOr7pUlgwGznogrHXGE3x3cvkSOVsWH50yU/edit#slide=id.g43faa55bbf_0_50](https://docs.google.com/presentation/d/1JQae3_BkcOr7pUlgwGznogrHXGE3x3cvkSOVsWH50yU/edit#slide=id.g43faa55bbf_0_50)

> 


These cue cards are part of a toolkit that Jim Gumbley of Thoughtworks put together. He calls it "Security Conversations" and it's part of his process for getting normal developers to talk about security instead of getting security specialists in.  
These cue cards help people understand the STRIDE model


## [Threat Modelling and Infrastructure Risk Assessment at Swiftype](https://swiftype.engineering/threat-modelling-and-infrastructure-risk-assessment-at-swiftype-6c1b337c7df1)

[https://swiftype.engineering/threat-modelling-and-infrastructure-risk-assessment-at-swiftype-6c1b337c7df1](https://swiftype.engineering/threat-modelling-and-infrastructure-risk-assessment-at-swiftype-6c1b337c7df1)

> In this modern world of ever evolving technology, new threats to online businesses are always emerging. Protecting a business from information security threats is an enormous challenge and requires a comprehensive defensive strategy. There are no simple, “plug and play” solutions. Instead, it is key to invest in processes that identify and assess risks, and to ensure that your business evolves to staunch and mitigate any and all identified threats. 


This is a good overview of threat modelling in a modern environment.

My only comment would be that this doesn't address how to keep it updated as the system changes


## [Bumpy ride for the Security Manual - InnovationsAus.com](https://www.innovationaus.com/2018/10/Bumpy-ride-for-the-Security-Manual)

[https://www.innovationaus.com/2018/10/Bumpy-ride-for-the-Security-Manual](https://www.innovationaus.com/2018/10/Bumpy-ride-for-the-Security-Manual)

> Moving on from ‘tick the boxes’ cyber compliance to a risk management approach had been fashionable at the UK government’s National Cyber Security Centre and that approach had been picked up by Australia’s cyber czars.
> 
> The US’ National Institute of Standards and Technology (NIST) cyber assessment and authorisation practices also takes a risk management approach and the CSM is understood to have incorporated the NIST risk management framework.
> 
> The draft CSM appeared to be ‘back filling’ the methodology used to give Microsoft its Protected Certification.


This is disappointing news.  The Australian government cyber security has changed quite a lot in the last year, and I hope that it's getting better again soon, but going back to compliance checklists is not the way forward.


