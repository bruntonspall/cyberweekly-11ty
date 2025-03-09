---
title: "109 - Protecting yourself"
date: 2020-07-05
description: "Welcome to July."
permalink: /protecting-yourself/
---

Welcome to July.

For a variety of reasons, I've not been able to produce a full newsletter for most of June.  I've produced lots of snippets for you, but I've heard from several people that the thing they find the most valuable and interesting is the analysis that I add to each link to explain why I copied it and what I think about it.

I'm getting back together and the general intensity of life is reducing down, so I'm going to commit to producing a more normal newsletter each week through July and August as normal, although it might be slightly shorter than normal.  Some of this is about protecting myself, ensuring that I don't burn out, and making sure that I have some time at weekends to switch off and relax without worrying that I've got more to read and write about in addition to my day job.  

But protecting ourselves is about understanding our environment, our actions and taking the actions necessary to prevent the most easily preventable things from affecting us.  And that's what a lot of security programs are about as well.  It's easy to spend money on expensive systems and programmes to deliver AI and block chain and god knows what security.  But actually focusing on the most draining things, the basics that get us over and over again are some of the most valuable interventions that we can make.

We know that many threat actors simply use of the shelf tools.  They don't customise the tools, they don't vary their techniques or actions.  They simply download and fire it at you.  If your endpoint detection software cannot be loaded with the most basic Indicators of Compromise (IoC's) then you are going to find yourself constantly fighting against all adversaries, both basic and advanced.  

Taking the time to ensure that you can load these IoC's, and block that activity means that you can stop worrying about it, stop investigating it, and start focusing your time and energy on the things that matter.

And if you get tired and fed up of dealing with stuff.  Don't be afraid to take a break, take a breather and don't let it rest all on your shoulders.  Confide in your friends, take rest time and make sure you have a support network.

## [Google blew a ten-year lead. - Second Breakfast](https://secondbreakfast.co/google-blew-a-ten-year-lead)

[https://secondbreakfast.co/google-blew-a-ten-year-lead](https://secondbreakfast.co/google-blew-a-ten-year-lead)

> Then something happened at Google. I’m not sure what. But they stopped innovating on cloud software.
> 
> Docs and Sheets haven’t changed in a decade. Google Drive remains impossible to navigate. Sharing is complicated. Sheets freezes up. I can’t easily interact with a Sheets API (I’ve tried!). Docs still shows page breaks by default! WTF!
> 
> Even though I have an iPhone and a MacBook, I’ve been married to Google services. I browse Chrome. I use Gmail. I get directions and lookup restaurants on Maps. I’m a YouTube addict.
> 
> Yet I’ve been ungluing myself from Google so far this year. Not because of Google-is-reading-my-emails-and-tracking-every-keystroke reasons, but because I like other software so much more that it’s worth switching.
> 
> [...]
> 
> My Gmail inbox has become a mailbox stuffed with clothing flyers, SaaS mailers, and Rollbar alerts. I love when people respond to Second Breakfast, but their responses get lost amid a sea of plastic bottles. I started using HEY last week. My new email is billy@hey.com. I love it so far.
> 
> I’ve given up on Google Docs. I can never find the documents Andy shares with me. The formatting is tired and stuck in the you-might-print-this-out paradigm.


As an unashamed Google fan, this resonated with me far more than I expected.  I love Google Suite for document editing.  I love being able to share documents with my coworkers, being able to turn into suggestion mode and see the edits and changes side by side, being able to collaborate in real time.

But I loved that back in 2010 when it was brand new, and I agree that there has been almost no innovation since then.

I'm giving hey a try, and while I'm not blown away, it is at least an attempt at innovating on what people want from an inbox.


## [Disclosure: Another macOS privacy protections bypass](https://lapcatsoftware.com/articles/disclosure2.html)

[https://lapcatsoftware.com/articles/disclosure2.html](https://lapcatsoftware.com/articles/disclosure2.html)

> Let me explain the issue in slightly less technical terms. In this case, only Safari and Finder should be authorized (by Apple) to access the files in ~/Library/Safari, unless you grant special authorization to another app, such as giving "Full Disk Access" to Terminal. My bypass demonstrates that a maliciously crafted app can also access those files, without being given authorization. There are actually two maliciously crafted apps here: a modified version of Safari, which accesses the protected files, and the app that modifies Safari and launches the modified version of Safari. Any app that you download from the web could accomplish this privacy protections bypass. My sample exploit uploads some of your private data (your Top Sites, for example) to a server that I control, because that's an easy thing to do when I can run any JavaScript I want. 


This is not a great look for Apple.  This bug is a zero-day, which is to say that this was released in public before Apple have released a fix.  The author claims that they informed Apple who have simply failed to fix the problem.

The underlying issue is that it's possible for any application to fairly easily modify another application in order to take control of the private files accessible by that target application.  Safari is particularly nasty here, because it can be used as part of a chain of attacks to completely own a machine.  If you can't trust your browser, then it's essentially game over as a defender


## [Russian Criminal Group Finds New Target: Americans Working at Home - The New York Times](https://www.nytimes.com/2020/06/25/us/politics/russia-ransomware-coronavirus-work-home.html)

[https://www.nytimes.com/2020/06/25/us/politics/russia-ransomware-coronavirus-work-home.html](https://www.nytimes.com/2020/06/25/us/politics/russia-ransomware-coronavirus-work-home.html)

> But the attack’s methodology suggests it was intended for the work-at-home era.
> 
> The malware, Mr. Chien said, was deployed on common websites and even one news site. But it did not infect every computer used to go shopping or read about the day’s events. Instead, the code looked for a sign that the computer was part of a major corporate or government network. For example, many firms have their employees use a “virtual private network,” or V.P.N., a protected channel that allows workers sitting in their basements or attics to tunnel into their corporate computer systems as if they were at the office.
> 
> “These attacks do not try to get into the V.P.N.,” Mr. Chien said. “They just use it to identify who the user works for.” Then the systems wait for the worker to go to a public or commercial website, and use that moment to infect their computer. Once the machine is reconnected to the corporate network, the code is deployed, in hopes of gaining access to corporate systems.


I'm not entirely convinced that this is as focused on the work-from-home era, rather the use of corporate VPN's for corporate laptops is pretty common place in todays mobile workforce.  This is however far more about the specific targeting of individual organisations, which is to some degree far nastier and more worrying than a simple targeting of the work-from-home workforce.

Symantic have a (https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/wastedlocker-ransomware-us)[good writeup with the TTP's].


## [Dark Basin: Uncovering a Massive Hack-For-Hire Operation - The Citizen Lab](https://citizenlab.ca/2020/06/dark-basin-uncovering-a-massive-hack-for-hire-operation/)

[https://citizenlab.ca/2020/06/dark-basin-uncovering-a-massive-hack-for-hire-operation/](https://citizenlab.ca/2020/06/dark-basin-uncovering-a-massive-hack-for-hire-operation/)

> In 2017, Citizen Lab was contacted by a journalist who had been targeted with phishing attempts and asked if we could investigate. We linked the phishing attempts to a custom URL shortener, which the operators used to disguise the phishing links.
> 
> We subsequently discovered that this shortener was part of a larger network of custom URL shorteners operated by a single group, which we call Dark Basin. Because the shorteners created URLs with sequential shortcodes, we were able to enumerate them and identify almost 28,000 additional URLs containing e-mail addresses of targets. We used open source intelligence techniques to identify hundreds of targeted individuals and organizations. We later contacted a substantial fraction of them, assembling a global picture of Dark Basin’s targeting.
> 
> Our investigation yielded several clusters of interest that we will describe in this report, including two clusters of advocacy organizations in the United States working on climate change and net neutrality.
> 
> While we initially thought that Dark Basin might be state-sponsored, the range of targets soon made it clear that Dark Basin was likely a hack-for-hire operation. Dark Basin’s targets were often on only one side of a contested legal proceeding, advocacy issue, or business deal.
> 
> [...]
> 
> The malicious links we discovered during our tracking each led to credential phishing sites, i.e., websites designed to look identical to popular online web services such as Google Mail, Yahoo Mail, Facebook, and others. In addition, Dark Basin operators had created phishing websites which copied the look and feel of specific web services used or operated by the target or their organization (Figure 11).


Absolutely stunning research by Citizen Lab here showing the dark unbelly of a hack for fire operation.

In this case, the organisation appears to offer ethical hacking, penetration testing and other security services, which include private investigation and intelligence gathering activities that are likely illegal.  

It's a good reminder that organisations do operate in this shadowy world, often at one length extended, whether for plausible deniability, or because they simply don't know or care how the investigators get their information (or simple naivete even)

Since almost all of this was credential harvesting, 2FA would prevent the majority of these attacks (or at least force the attacker to put a lot more effort into the attacks, which would increase the cost)


## [Domain Squatting: The Phisher-man's Friend | Digital Shadows](https://www.digitalshadows.com/blog-and-research/domain-squatting-the-phisher-mans-friend/)

[https://www.digitalshadows.com/blog-and-research/domain-squatting-the-phisher-mans-friend/](https://www.digitalshadows.com/blog-and-research/domain-squatting-the-phisher-mans-friend/)

> The internal struggle was real: If we use HTTPS for the landing page, we increase the chances of successfully phishing our targets (people are inherently more trusting of a site which uses HTTPS as opposed to one with HTTP), however by generating a certificate we could also potentially setting off red flashing lights and sirens in a Security Operations Centre somewhere.
> 
> So we decided, let’s not encrypt this time.


[This is an old report and comment by me.  It's been sitting at the bottom of a pile for some reason.  It's still very much worth reading]

I think this over-emphasises how capable most security teams are.  I've never seen anyone in a normal security team receiving notifications for certs issued for potential phishing of their own domains or brands.


## [Detecting PoshC2 - Indicators of Compromise — Nettitude Labs](https://labs.nettitude.com/blog/detecting-poshc2-indicators-of-compromise/)

[https://labs.nettitude.com/blog/detecting-poshc2-indicators-of-compromise/](https://labs.nettitude.com/blog/detecting-poshc2-indicators-of-compromise/)

> As a counterpart to the release of PoshC2 version 6.0 we are providing a list of some of its Indicators of Compromise (IoCs), particularly as used out-of-the-box, as well as some other effective methods for detecting it in your environment.
> 
> We also introduce the new PoshC2 Detections GitHub repository at https://github.com/nettitude/PoshC2_IOCs that will be continually updated as development continues, in order to assist blue teams with detecting PoshC2, particularly when used by less sophisticated attackers that do not alter or configure it to change the default IoCs. We encourage the community to contribute to and help update and improve this repository.


This penetration testing tool provides specific indicators of compromise so that you can easily detect it's use in your environment.  This is a great move by a tool provider, because we know a subset of attackers either wont bother or are unable to customise the tools that they use in their attacks.

If you detect and stop those attacks with these IoC's then you'll be in a better place to then focus your attention on the higher capability threat actors.


## [Talos Blog || Cisco Talos Intelligence Group - Comprehensive Threat Intelligence: IndigoDrop spreads via military-themed lures to deliver Cobalt Strike](https://blog.talosintelligence.com/2020/06/indigodrop-maldocs-cobalt-strike.html)

[https://blog.talosintelligence.com/2020/06/indigodrop-maldocs-cobalt-strike.html](https://blog.talosintelligence.com/2020/06/indigodrop-maldocs-cobalt-strike.html)

> This attack demonstrates how the adversary operates a targeted attack that:
> 
> * Uses legitimate-looking lures to trick the target into infecting themselves.
> * Employs a highly modular infection chain (implemented in the IndigoDrop) to instrument the final payload.
> * Uses an existing offensive framework (Cobalt Strike) to establish control and persist in the target's network without having to develop a bespoke remote access trojan (RAT).
> 
> Analysis of recently discovered attack-chain variations provides insights into the evolution of this threat. These evolutions indicate the changes in tactics and techniques of the attackers used to continue attacks while trying to bypass detections. This campaign also shows us that while network-based detection is important, it should be complemented with system behavior analysis and endpoint protections for additional layers of security.


A strong reminder that you should be deploying endpoint protection and monitoring not just network monitoring.

Even if you just get common signatures for out of the box malware (such as Cobalt Strike), you'll catch the lowest level of attacker and probably half of your red teams activities as well.


