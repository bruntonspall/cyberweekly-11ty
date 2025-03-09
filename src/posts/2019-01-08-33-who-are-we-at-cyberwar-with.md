---
title: "33 - Who are we at Cyberwar with?"
date: 2019-01-08
description: "Over the Christmas period, the [twitter argument started by Perry Metzger](https://twitter.com/perrymetzger/status/1075928695058120705?s=20) has made me think and ruminate a lot on Cyber Warfare and adversarial thinking."
permalink: /who-are-we-at-cyberwar-with/
---

Over the Christmas period, the [twitter argument started by Perry Metzger](https://twitter.com/perrymetzger/status/1075928695058120705?s=20) has made me think and ruminate a lot on Cyber Warfare and adversarial thinking.

I’ve spent the last few years doing a lot of work with Attack Tree’s, considering how an adversary might attack our systems and then comparing our defences and seeing how effectively they prevent the attacks in question (hint: More firewalls is not the answer).

But the Ponemon 2018 Cost of a data breach study was pretty clear that over half of data breaches are caused by accident, misconfiguration or error.  Now we can’t easily detect insider malicious behaviour from that, but general studies imply that actively malicious insider behaviour is pretty rare generally.  

This means that if these numbers are accurate, then we aren’t at war with advanced “cyber-adversaries” whatever that means, but that we are at war with ourselves, with the software that we build, and with the processes that encourage error, misconfiguration and accident.

I’ve spent a lot of time looking at the safety processes and principles, and the way that people work in safety critical systems, and they have the same problem, assuming that users are tired, over worked and stressed and liable to make mistakes, not follow process, or misconfigure things.  I think for me, 2019 will be about focusing on what we can learn from safety engineering, from healthy retrospective behaviours, and how we can build systems that are resistant to misconfiguration or accident.

We still have a long way to go in security as well, but given that there’s an average time of 196 days to detect a breach (and around 5 years for the Marriott breach), and somewhere around 40 days to patch many vulnerabilities (but with a massive error bar on that data), I still think that the best security strategy is to focus on identifying your assets, ensuring they are regularly and easily patched, and then focusing on blocking incoming phishing emails.  Almost all of the more advanced cyber security products and things are of massively reducing value after that compared to dealing with the other half of data breaches

## [2018 in cybersecurity: Regrets, we have a few](https://www.engadget.com/2018/12/21/2018-year-in-review-cybersecurity-privacy-fail/)

[https://www.engadget.com/2018/12/21/2018-year-in-review-cybersecurity-privacy-fail/](https://www.engadget.com/2018/12/21/2018-year-in-review-cybersecurity-privacy-fail/)

> There were cops unlocking iPhones with corpses. Australia mandated backdoors. Apple came out swinging against accusations they were infiltrated by Chinese spy chips. Japan's Cybersecurity minister said he's never used a computer. The head of DC's top cyber think tank turned out to be a con man. A Russian spy claiming to be a cybersecurity aficionado faked her way into the GOP and NRA.


Yes, I’m still reading all of the “2018 in review” articles.  I enjoyed this mostly because Violet Blue has an amazing way with words, and this summarised some of the more interesting stories of 2018.  It really was quite a year when you think about it.


## [Richard Gold on Twitter: "My ten predictions for cyber security in 2019 which are all positive improvements and, hopefully, things to look forward to!"](https://twitter.com/drshellface/status/1072803919020154880?s=19)

[https://twitter.com/drshellface/status/1072803919020154880?s=19](https://twitter.com/drshellface/status/1072803919020154880?s=19)

> 3/9: for those without big security budgets, like home users, even Windows Defender is getting pretty good these days, expect this to keep on improving in 2019. My personal preference is to complement it with @botherder’s hardentools
> 
> [...]
> 
> 5/9: the leaky pipeline and general appalling situation of a lack of women in cyber security is at last being looked at by organisations like 
> @NCSC
>  with their CyberFirst Girls competition 2019. So much more work required in this space though!


This is a good positive spin for 2019.  I agree with all of these, and think they’ll be areas in which we’ll improve in 2019.  I’m especially keen to see the NCSC’s efforts to improve the diversity of the cyber security demographics, as diversity of thinking is so critical to good security programs.


## [Perry E. Metzger @perrymetzger On Twitter ](https://threader.app/thread/1075928695058120705)

[https://threader.app/thread/1075928695058120705](https://threader.app/thread/1075928695058120705)

> I finally realized one of the things that bugs me about most security "certifications" out there. Computer security is warfare. No, really, it's war. There's an opponent who doesn't care about you, doesn't play by the rules, and wants to screw you as fully as possible. 1/
> 
> ...
> 
> And it's just not possible for everyone to be above average. In fact, these days, a shocking fraction of "security professionals" I interview can't even program, can't tell you what a buffer overflow is or how SQL injection works or what XSS is. Like, at all. 4/
> 
> I had a guy tell me, while I was interviewing, "gee, I knew this for my CISSP, but I've forgotten." Well, no, this isn't about signaling the way college was, you needed to learn that stuff _and remember it permanently_. You can't just learn for the exam. Only most people do. 5/
> 
> ...
> 
> Now what do I learn when I see that someone has a CISSP? That at one point, for a brief period, they managed to get a passing score on a standardized test. Not that they know the material _now_. Not that they have the stuff in their blood. 10/


This was before Christmas but it caused quite a discussion on twitter and a lot of back and forth about this.

I agree with Perry about the value of standardised tests.  They don’t, and cannot, show capability or competence.  I got my CISSP and I don’t think it shows a terribly high bar, because exams are always about learning for the exam.  It shows that someone can pass an exam, not that they know this stuff in the slightest (and in fact, knowing the subject areas well is a disadvantage for CISSP because the reality is far more complex than the CISSP exam expects, and you have to learn what the “CISSP” answer is, because “it depends” isn’t on the multiple choice selection).

But I disagree here with Perry that security professionals must know how to program.  Even his focus on a buffer overflow vulnerability, which is more of an issue only in certain older languages, shows that the knowledge is specific and not always correct in the field. 

Information security, Cyber security, Privacy and Law are all areas within computer security, and not all of them require people to be genius programmers.  There is a value to learning how software is built, to learning how this stuff works, but it’s also equally important that security professionals know about psychology, social signals, economics and incentives as the hard computer science stuff.  By focusing on whether your CISO can program, you are focussed entirely on the wrong thing. 


## [Databases suited from our workload (slideshare)](https://www.slideshare.net/AmazonWebServices/building-with-aws-databases-match-your-workload-to-the-right-database-dat301-aws-reinvent-2018/30)

[https://www.slideshare.net/AmazonWebServices/building-with-aws-databases-match-your-workload-to-the-right-database-dat301-aws-reinvent-2018/30](https://www.slideshare.net/AmazonWebServices/building-with-aws-databases-match-your-workload-to-the-right-database-dat301-aws-reinvent-2018/30)

> The iron triangle of purpose (the PIE theorem)


This is a great model for thinking about databases. As well as considering CAP, Considtency, Availability and Partition tolerance you can consider PIE, Pattern flexibility, Infinite scale and Efficiency.

That is to say that databases can support any two of random unstructured queries, large workloads and fast enough response times to be used online.

The entire presentation goes into a lot of detail about Amazons offerings, but this model is a good one for comparing products in the SQL/NoSQL/Graph/Hadoop space.


## [Attack of the Drones – Information Terror, Hot Takes & Hybrid Warfare](http://bit.ly/2T8nMtA)

[http://bit.ly/2T8nMtA](http://bit.ly/2T8nMtA)

> The drones had Britain’s second most economically important transportation hub in a humiliating force choke.  Police dogs2, birds of prey, net launching ‘bazookas’3 and military counter-UAV systems, have all been discussed to deliver control of the air space over Gatwick.  As we face the national crisis of Brexit and at a period of festive emotion, there is apparent ‘presence of the abnormal’.  Regardless of who did this, it feels like we’re being experimented on.
> 
> [...]
> 
> On the basis of 50 sightings over a 24 hour period, it’s possible that a stand-off foe is using multiple air-frames, possibly 2 per hour, in order to achieve air superiority and information effect.  This translates into an outlay of around £60,000 per 24 hour period of airspace denial.  Conversely, Gatwick loses £1.1M per day if closed.  According to Yahoo Finance, a 2014 report from the UK Airport Commission found that the value of a flight delay for a leisure traveler was about £6.60 per hour. The value to a business traveler ranged from about £47 to £49 per hour.  Over 100,000 travelers were affected by this shutdown.  A conservative estimate of loss for the 3 day attack therefore runs close to £10M.  That’s quite a ROI for attackers, present and future.


This is an interesting read on the current state of information warfare, and an analysis of the informational chaos that happened during the drone incident at Gatwick.

I don’t think that it takes into account the issues of incompetence, mistake and information hiding however.  When we assume that reports are either entirely accurate, or falsified by an enemy, we ignore our own fallibility.  It’s entirely possible that people mistakenly saw things they thought were drones, that police officers overreacted and didn’t report their overreaction and so on.  It doesn’t have to be conspiracies, powerful geopolitical enemies and information warfare operations when it could instead simply be overreaction, confusion and mass reporting rushing to get the story out as fast as possible.


## [Come Get Your Free NSA Reverse Engineering Tool!](https://www.rsaconference.com/events/us19/agenda/sessions/16608-Come-Get-Your-Free-NSA-Reverse-Engineering-Tool)

[https://www.rsaconference.com/events/us19/agenda/sessions/16608-Come-Get-Your-Free-NSA-Reverse-Engineering-Tool](https://www.rsaconference.com/events/us19/agenda/sessions/16608-Come-Get-Your-Free-NSA-Reverse-Engineering-Tool)

> NSA has developed a software reverse engineering framework known as GHIDRA, which will be demonstrated for the first time at RSAC 2019. 
> 
> The GHIDRA platform includes all the features expected in high-end commercial tools, with new and expanded functionality NSA uniquely developed, and will be released for free public use at RSA


This is nice to see.  The NSA 5 or 10 years ago would never have presented at a major conference, and has open sourced very little work over the years.  GCHQ has released a number of open source tools, Stroom, Gaffer and the absolutely brillliant CyberChef, and the creation of the NCSC is a clear step towards being far more public about their capabilities.  I think this is a sign that the NSA are following suit and that 2019 and 2020 will be the years in which a lot of the intelligence agencies will come out of the shadows and start to have a public face.


## [Dirty dealing in the $175 billion Amazon Marketplace - The Verge](https://www.theverge.com/2018/12/19/18140799/amazon-marketplace-scams-seller-court-appeal-reinstatement)

[https://www.theverge.com/2018/12/19/18140799/amazon-marketplace-scams-seller-court-appeal-reinstatement](https://www.theverge.com/2018/12/19/18140799/amazon-marketplace-scams-seller-court-appeal-reinstatement)

> When you buy something on Amazon, the odds are, you aren’t buying it from Amazon at all. Plansky is one of 6 million sellers on Amazon Marketplace, the company’s third-party platform. They are largely hidden from customers, but behind any item for sale, there could be dozens of sellers, all competing for your click. This year, Marketplace sales were almost double those of Amazon retail itself, according to Marketplace Pulse, making the seller platform alone the largest e-commerce business in the US.


Amazon Marketplace is huge and pays out a lot of money.  That means that it is obviously a huge vehicle for fraudsters and criminals, but it looks like Amazon do a reasonable job of trying to prevent that behaviour.  But it’s also a competitive marketplace for sellers from around the globe, with different moral and ethical frameworks, and it looks like Amazon struggles to see how to police a community in such a way.  Counter fraud tools being abused to report your competitors is an obvious attack in such a system and it looks like Amazon isn’t geared up to handle that very well.


