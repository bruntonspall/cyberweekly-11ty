---
title: "86 - Tackling only what we can"
date: 2020-01-25
description: "We often want to fix everything around us.  We want to fix systems, processes, and entire organisations all at once.  And then we burn out unable to get the fixes we need in place."
permalink: /tackling-only-what-we-can/
---

We often want to fix everything around us.  We want to fix systems, processes, and entire organisations all at once.  And then we burn out unable to get the fixes we need in place.

Most company technology estates are enormous complex beasts and it is impossible to fix everything at once.  

Our strategy for approaching broken things is to start small and demonstrate that we can deliver, and then to grow our solutions to cover more stuff.  This can be true for applying new authentication systems, rolling out 2FA, starting to patch our systems, logging and monitoring, or pretty much anything we look at.

It's super easy to be overwhelmed by size and complexity, and it takes skill (or maybe experience, I don't know how different those two are in this case) to be able to clearly select a slice of something that you can transform, modernise, change without causing havoc everywhere else or feeling like you are wading through molasses.

Instead of trying to patch everything, fix everything, we need to identify places where we can make the most impactful changes.  This means knowing what systems are important to us.  You can worry about patching everything on your estate against the latest vulnerability, or you can focus on just your VPN endpoints, or certain servers etc.  Trying to patch just a portion of the estate will show you how hard or easy it is to patch, give you experience of delivering and prove the value of the work you do.  Once you've done something once, it is much easier to repeat that work in other areas.

## [Steven Murdoch on Twitter](https://twitter.com/sjmurdoch/status/1217157683796680708)

[https://twitter.com/sjmurdoch/status/1217157683796680708](https://twitter.com/sjmurdoch/status/1217157683796680708)

> Today my Head of Department emailed me about something. It sounded urgent, though it's odd he switched to using a Gmail address [thread]


Steven Murdoch got a an email from his boss asking him to nip out to a store to get some giftcards.  If you haven't seen a giftcard scam before, it's an interesting read, and even if you have, it's a good fun read.


## [Exclusive: The inside story of how the U.S. gave up a chance to kill Soleimani in 2007](https://www.yahoo.com/news/its-not-in-our-dna-soleimani-thought-he-was-untouchable-and-for-more-than-a-decade-he-was-100014025.html)

[https://www.yahoo.com/news/its-not-in-our-dna-soleimani-thought-he-was-untouchable-and-for-more-than-a-decade-he-was-100014025.html](https://www.yahoo.com/news/its-not-in-our-dna-soleimani-thought-he-was-untouchable-and-for-more-than-a-decade-he-was-100014025.html)

> But when CIA officers asked Army Lt. Gen. Stanley McChrystal, head of Joint Special Operations Command (JSOC), and other senior U.S. officials, about targeting Soleimani and other Iranian intelligence figures, their requests went nowhere, according to Maguire. “I was told, ‘No, these are Iranians,’” he said. “There was no appetite for it” in the Pentagon. 
> 
> A Bush administration directive shortly after the invasion meant the CIA could not take matters into its own hands, according to the former senior CIA official. “We were limited to straight intel collection,” he said. “No covert action, no influence operations.”
> 
> The CIA’s Iraqi counterparts were equally frustrated at Washington’s reluctance to kill Soleimani. “The Iraqi intel service wanted to kill him and couldn’t understand why we wouldn’t target him,” Maguire said. “They thought he was the most dangerous guy in Iraq.”


Two things here.  The first is the interesting note that the US had been following Soleimani for over a decade, aware of what he was doing, but felt that taking action wasn't a good tradeoff at the time. Also, the wording here is no covert action, no influence operations.  This is not just about drones and assassination, they were explicitly forbidden from directing proxies to the same ends.

The second thing that I note is that Yahoo News has had a lot of stories over the last few months with sources within the US intelligence community.  Yahoo News is not on my normal reading list, I read technology and intelligence focused publications a lot.  I'll be keeping an eye on their national security news in future for sure.


## [Is SMS 2FA Secure?](https://www.issms2fasecure.com/)

[https://www.issms2fasecure.com/](https://www.issms2fasecure.com/)

> An Empirical Study of Wireless Carrier Authentication for SIM Swaps
> 
> * We examined the authentication procedures used by five prepaid wireless carriers when a customer attempts to change their SIM card, or SIM swap.
> * We found that all five carriers use insecure authentication challenges that can easily be subverted by attackers.
> * We reverse-engineered the authentication policies of over 140 websites that offer SMS-based authentication, and rated the vulnerability level of users of each website to a SIM swap attack.
> * We found 17 websites on which user accounts can be compromised based on a SIM swap alone.


This was quite badly reported on, because the paper is a bit more complex than the headline.

SMS based second factors are still significantly more secure than having no second factor at all.  However, we should be aware that SIM Swapping is not beyond the capabilities of even fairly low capability actors.

The key thing to pick up from this research however is that authentication mechanisms within telehone carriers (who primarily deal with normal users, not technically competent users) are broken almost by design.

The research points out that many systems have far far weaker secondary or backup authentication mechanisms.  An attacker can deliberately fail at the strong authentication mechanisms, and fall through to the easier to break authentication mechanisms.

One possible fix for this is to continue to allow weaker authentication mechanisms for users who lose their pin or password, but only allow that to conduct low authority actions, such as having a password reissued to your home address, or querying overbilling or other administrative activities that have low value to attackers.


## [Ghost ships, crop circles, and soft gold: A GPS mystery in Shanghai](https://www.technologyreview.com/s/614689/ghost-ships-crop-circles-and-soft-gold-a-gps-mystery-in-shanghai/amp/)

[https://www.technologyreview.com/s/614689/ghost-ships-crop-circles-and-soft-gold-a-gps-mystery-in-shanghai/amp/](https://www.technologyreview.com/s/614689/ghost-ships-crop-circles-and-soft-gold-a-gps-mystery-in-shanghai/amp/)

> The question now is, are these previous AIS hacks connected to Shanghai’s new GPS circles in some way? An effective spoofing system could be worth millions to sand thieves. By spoofing their own ships, they could glide invisibly into port. Or by spoofing others and creating chaos, smugglers would give themselves a better chance of slipping through unnoticed. It could be that the ability to generate spoofed circles is an escalation in technological know-how by the sand thieves.
> 
> Of course, it could be just a coincidence that the spoofed circles are occurring at a hot spot for AIS cloning. Another possibility is that the Chinese state itself is testing out a new electronic weapon, perhaps for eventual use in disputed regions of the South China Sea.


GPS is one of those interesting technologies that a lot of people and things rely on and very few people actually understand very well.  This older story is a frightening view of what happens when it goes wrong, and how nobody really seems to know what actually causes the problem


## [LastPass Status - LastPass Chrome Extension Issue](https://status.lastpass.com/incidents/8bbt8vpxmbrx)

[https://status.lastpass.com/incidents/8bbt8vpxmbrx](https://status.lastpass.com/incidents/8bbt8vpxmbrx)

> The LastPass extension in the Chrome Web Store was accidentally removed by us and we are working with the Google team to restore it ASAP. Thank you for your understanding and patience in the meantime.


Yup.  LastPass accidentally delisted their chrome extension from the chrome web store.

As a security tool, this was jumped on as a major security flaw, but in reality, this is simply an administrative error.  Admittedly a rather silly one, but it has very little security impact.

Existing users weren't affected, new users couldn't download the chrome extension for 24 hours.

The one lingering question for me is around what the actual provenance checks are within the Google Chrome Webstore for an extension.  How hard would it be to insert your own extension code in place of the LastPass one?


## [Here Is the Technical Report Suggesting Saudi Arabia's Prince Hacked Jeff Bezos' Phone - VICE](https://www.vice.com/en_uk/article/v74v34/here-is-the-technical-report-suggesting-saudi-arabias-prince-hacked-jeff-bezos-phone)

[https://www.vice.com/en_uk/article/v74v34/here-is-the-technical-report-suggesting-saudi-arabias-prince-hacked-jeff-bezos-phone](https://www.vice.com/en_uk/article/v74v34/here-is-the-technical-report-suggesting-saudi-arabias-prince-hacked-jeff-bezos-phone)

> Investigators determined the video or downloader were suspicious only because Bezos’ phone subsequently began transmitting large amounts of data. “[W]ithin hours of the encrypted downloader being received, a massive and unauthorized exfiltration of data from Bezos’ phone began, continuing and escalating for months thereafter,” the report states.


This [twitter thread by Errata Rob is worth reading](https://twitter.com/ErrataRob/status/1220459660131622912?s=20).  Pretty much everything that is in this report is wrong or amateur hour.  From buying your mobile forensics lab on demand (they didn't have one?), resetting all of the settings on the phone before starting forensics, detecting websites like "amazon.com" as potential indicator of compromise on Jeff Bezos' phone (I really want to see the video of someone explaining that to him).

Based on this report, I see pretty much no evidence at all that the headline claims are actually accurate.  This feels more like someone had a hypothesis and was looking for evidence that met their hypothesis.


## [Windows will improve user privacy with DNS over HTTPS - Microsoft Tech Community - 1014229](https://techcommunity.microsoft.com/t5/networking-blog/windows-will-improve-user-privacy-with-dns-over-https/ba-p/1014229)

[https://techcommunity.microsoft.com/t5/networking-blog/windows-will-improve-user-privacy-with-dns-over-https/ba-p/1014229](https://techcommunity.microsoft.com/t5/networking-blog/windows-will-improve-user-privacy-with-dns-over-https/ba-p/1014229)

> Providing encrypted DNS support without breaking existing Windows device admin configuration won't be easy. However, at Microsoft we believe that "we have to treat privacy as a human right. We have to have end-to-end cybersecurity built into technology."
> 
>  
> 
> We also believe Windows adoption of encrypted DNS will help make the overall Internet ecosystem healthier. There is an assumption by many that DNS encryption requires DNS centralization. This is only true if encrypted DNS adoption isn’t universal. To keep the DNS decentralized, it will be important for client operating systems (such as Windows) and Internet service providers alike to widely adopt encrypted DNS.
> 
> Based on these principles, we are making plans to adopt DNS over HTTPS (or DoH) in the Windows DNS client. As a platform, Windows Core Networking seeks to enable users to use whatever protocols they need, so we’re open to having other options such as DNS over TLS (DoT) in the future. For now, we're prioritizing DoH support as the most likely to provide immediate value to everyone. For example, DoH allows us to reuse our existing HTTPS infrastructure.
> 
>  
> 
> For our first milestone, we'll start with a simple change: use DoH for DNS servers Windows is already configured to use. There are now several public DNS servers that support DoH, and if a Windows user or device admin configures one of them today, Windows will just use classic DNS (without encryption) to that server. However, since these servers and their DoH configurations are well known, Windows can automatically upgrade to DoH while using the same server


After all of the hand wringing and complaining that Mozilla was going to enable DNS-over-HTTPS and would break all enterprises, we now have a heads up that Microsoft is looking at building encrypted DNS directly into the operating system in the future.

If you are currently reliant on the ability to sniff DNS because it's plain text as part of your security tooling, then you need to rethink how you monitor DNS queries.  Running an enterprise DNS resolver for your enterprise desktops is something you probably need to roll out.  One benefit of DNS-over-TLS is that you can do authentication as part of your DNS queries, and thus use a zero-trust network style architecture to host your resolver on the public internet.


## [Demos, Prototypes, and MVPs | Jacob Kaplan-Moss](https://jacobian.org/2020/jan/16/demos-prototypes-mvps/)

[https://jacobian.org/2020/jan/16/demos-prototypes-mvps/](https://jacobian.org/2020/jan/16/demos-prototypes-mvps/)

> A prototype is similar to a demo in scope. But the audience and the goal make them fundamentally different. A prototype is used to prove that a product, feature, or approach is viable. They can be very rough, even barely working, as long as they serve their purpose. Demos, the other hand, usually need to look good; they're part of a sales pitch.
> 
> A concrete example: an iPython notebook makes a fine prototype. It's totally sufficient to prove the technical feasibility of some approach. But they make lousy demos. They're visually unappealing, very confusing to non-technical users, and I've never seen a notebook help close a deal.


This is a really good explanation about the difference between a prototype and a demo is from a technical perspective.

Within Government, we've tended to use the word prototype to cover things that are more like demos.  That's because we have a push for user research and getting feedback.  These "prototypes" are far more like how Jacob describes a demo, but less about selling and more about gathering user experience feedback.

This leads to some confusion about what we mean when we talk about doing technical prototypes.  I've seen a few projects where they created lots of prototypes for user research, but had no idea what technology stack they should use when they come to build the thing.  Technical prototypes are valuable for understanding the impact of technical decisions that you'll have to make early.


## [Building new services around older IT – Public Digital](https://public.digital/signals/building-new-services-around-older-it/)

[https://public.digital/signals/building-new-services-around-older-it/](https://public.digital/signals/building-new-services-around-older-it/)

> These are two very different cultures, both technically and operationally. How do you make the old and new work together?
> 
> There are many ways of connecting systems together, from syncing data between old and new, to developing APIs to allow information from one to update the other. That’s the kind of thing that technologists often call an “integration”. But where do you start?
> 
> It’s tempting to try and solve the problem in one go with one solution – particularly if the existing system is difficult or costly to change. But doing this comes with its own set of problems.
> 
> Often, existing systems have grown and become more complex over time. Designing and implementing one single monolithic integration for everything will take a long time, and your new digital service won’t work until it’s all done.
> 
> It’s likely you don’t know everything that your new digital service will need from day one, so you’re going to be making guesses which might not be correct and will necessitate changes later on. The more larger and complex the integration, the longer it’ll take to change later.
> 
> The alternative is to start small and design integrations based on user needs – in exactly the same way as you would develop the new digital service.


Start small and iterate is pretty much my answer for everything.  Some of us love to think and write big and want to solve all of problems at once.  The most important thing you need to do is work out how to start small and yet still deliver value.  Dafydd here really gets to the nub of the solution.  You need to work out how to isolate your part of the solution, deliver value fast and easily, and be able to integrate and grow that solution over time.


