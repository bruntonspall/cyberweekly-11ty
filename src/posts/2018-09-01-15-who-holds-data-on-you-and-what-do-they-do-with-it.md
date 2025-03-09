---
title: "15 - Who holds data on you, and what do they do with it?"
date: 2018-09-01
description: "This newsletter comes to you from a chilly field in the wilds of the UK, where hackers and makers of all forms have gathered to share news, tips and techniques.  The amount of future tech on show that is bodged together with tape, glue and exposed wires is quite fun and always eye opening."
permalink: /who-holds-data-on-you-and-what-do-they-do-with-it/
---

This newsletter comes to you from a chilly field in the wilds of the UK, where hackers and makers of all forms have gathered to share news, tips and techniques.  The amount of future tech on show that is bodged together with tape, glue and exposed wires is quite fun and always eye opening.

There is an interesting set of stories this week about how data mining happens, and how advertising works on that data.  Additionally we can think about how governments collect data and how they use it.  We have an article about China's use of data to replace democracy, but western governments have been talking about data driven policy making for years as well, and face the same sets and types of integrity issues with the data.
Meanwhile, we continue to have breaches, vulnerabilities in major applications and all of the things that go together to make us feel like this collected data is not safe.

Finally, even if we could gather the data and trust it, I've got a couple of articles to remind you that engineering efforts are often not perfect, and that we should consider where we spend our time and effort.  These data platforms are being built by the same mix of competence that builds everything else, and the idea that there is a perfect machine which has been built to analyse the data seems ludicrous.

## [Microsoft Zero-Day Exploit Published Before Patch](https://www.databreachtoday.com/microsoft-zero-day-exploit-published-before-patch-a-11434)

[https://www.databreachtoday.com/microsoft-zero-day-exploit-published-before-patch-a-11434](https://www.databreachtoday.com/microsoft-zero-day-exploit-published-before-patch-a-11434)

> SandboxEscaper has also posted proof-of-concept exploit code on GitHub. The vulnerability allows for local privileges to be escalated to system level due to a flaw within the Advanced Local Procedure Call, or ALPC, interface of the Windows task scheduler.
> 
> "The flaw is that the Task Scheduler API function SchRpcSetSecurity fails to check permissions," Beaumont writes in his blog post. "So anybody - even a guest - can call it and set file permissions on anything locally."


This is quite a serious local exploit, but also the details around how it got leaked in advance of the patch are kind of interesting.  People are people and get emotional and don't always behave logically.


## [Don't Do This in Production · Stephen Mann](https://stephenmann.io/post/dont-do-this-in-production/)

[https://stephenmann.io/post/dont-do-this-in-production/](https://stephenmann.io/post/dont-do-this-in-production/)

> “Move fast and break things,” they said. It turns out that’s a pretty bad idea when your business relies on a small number of large customers. Broken products tend to scare them off, which in turn tanks your business. There’s a lot to be said for building things that work, but “move slowly and steadily towards a goal” just doesn’t have the same ring.  In reality, there’s a balance between moving fast and and moving slow. It’s difficult to communicate that balance because every type of product demands a different balance. I suppose that intuition comes from experience, which is a terrible answer for someone trying to learn.


Bimodal IT, or there’s more than one way to do it, is a fad in cloud adoption at the moment, and is being rightly pilloried by cloud native experts.  But bimodal product development, that is having different teams working in different ways is far more sensible.  You can move fast and break stuff in new products, in certain stages of development, but other times you need to be able to move slowly and ensure that the product works for its users.  
As is highlighted by this article, inexperience is the killer in all of this, inexperienced people aren’t able to easily adapt and modify their development methodology, identify the risk areas of their software or make confident large refactoring reliably, because those all take experience.  But experience isn’t just automatically gained over time, it’s gained through learning from failures and not just repeating the mistakes of that past


## [Shipping Software Should Not Be Scary – charity.wtf](https://charity.wtf/2018/08/19/shipping-software-should-not-be-scary/)

[https://charity.wtf/2018/08/19/shipping-software-should-not-be-scary/](https://charity.wtf/2018/08/19/shipping-software-should-not-be-scary/)

> In too many organizations, deploy code is a technical backwater, an accumulation of crufty scripts and glue code, forked gems and interns’ earnest attempts to hack up Capistrano.  It usually gives off a strong whiff of “sloppily evolved from many 2 am patches with no code review”.
> 
> This is insane.  Deploy software is the most important software you have.  Treat it that way: recruit an owner, allocate real time for development and testing, bake in metrics and track them over time.


This is good from Charity, and a good reminder that your supporting software, deployment, monitoring, security etc, should be some of the most important that you have.


## [Just Like Real Life, EVE Online Wars Are Won With Propaganda](https://kotaku.com/just-like-real-life-eve-online-wars-are-won-with-propa-1828497882)

[https://kotaku.com/just-like-real-life-eve-online-wars-are-won-with-propa-1828497882](https://kotaku.com/just-like-real-life-eve-online-wars-are-won-with-propa-1828497882)

> “When the shoe is on the other foot, propaganda serves to soften the impact being felt from losses,” Paramemetic said. It’s not just about ‘spin,’ but more about framing and softening the losses so that they don’t impact that morale.”
> 
> This need to drive engagement outside of the game’s normal reward structure is something that is relatively unique to EVE. In a more traditional MMORPG, massive group content that lasts for hours at a time often comes with tangible rewards for the players participating in it. Players are rewarded with currency or with character progression in the form of loot or experience points. In contrast, massive battles in EVE Online are rarely profitable, and in fact often cost individual players a great deal, since when ships are destroyed, those assets are permanently lost.


I find the operations within Eve Online fascinating mirrors of the real world.  With information operations, such as propaganda, we can see the effects and how much of a difference it makes, all inside a virtual world that doesn't really exist


## [Experts Urge Rapid Patching of ‘Struts’ Bug — Krebs on Security](https://krebsonsecurity.com/2018/08/experts-urge-rapid-patching-of-struts-bug/)

[https://krebsonsecurity.com/2018/08/experts-urge-rapid-patching-of-struts-bug/](https://krebsonsecurity.com/2018/08/experts-urge-rapid-patching-of-struts-bug/)

> On Aug. 22, the Apache Software Foundation released software updates to fix a critical vulnerability in Apache Struts, a Web application platform used by an estimated 65 percent of Fortune 100 companies. Unfortunately, computer code that can be used to exploit the bug has since been posted online, meaning bad guys now have precise instructions on how to break into vulnerable, unpatched servers.


This seems bad.  Struts is popularly used in large organisations, and those are exactly the organisations that struggle to patch early and patch often.


## [Google and Facebook Didn't End Data Privacy - The Atlantic](https://www.theatlantic.com/technology/archive/2018/08/the-age-of-privacy-nihilism-is-here/568198/)

[https://www.theatlantic.com/technology/archive/2018/08/the-age-of-privacy-nihilism-is-here/568198/](https://www.theatlantic.com/technology/archive/2018/08/the-age-of-privacy-nihilism-is-here/568198/)

> Many people still think their smartphones are listening to them in secret—recording their conversations in the background, then uploading them to Facebook or Google surreptitiously. Facebook has been accused of the practice more than others, probably because its services (including Instagram) are so popular and ads are so easy to spot. The company denies doing so every time, and researchers have shown it to be technically infeasible, too. But the idea still persists.
> 
> It persists because it feels true, and also because it is true, by the spirit if not the letter. Facebook and Google might not literally be listening in on our conversations, but they are eavesdropping on our lives. These companies have so much data, on so many people, and they can slice and dice it in so many ways that they might as well be monitoring our conversations. 


This is an excellent analysis of why the data mining for marketing is not a new thing, but why the rise of connected data is just increasing the accuracy and pervasiveness of it.  It also tackles the fact that we are unable to opt out, and so we have to live with it, and we need someway to ensure that people feel like their privacy is respected


## [Who needs democracy when you have data? - MIT Technology Review](https://www.technologyreview.com/s/611815/who-needs-democracy-when-you-have-data/)

[https://www.technologyreview.com/s/611815/who-needs-democracy-when-you-have-data/](https://www.technologyreview.com/s/611815/who-needs-democracy-when-you-have-data/)

> In theory, data-driven governance could help fix these issues—circumventing distortions to allow the central government to gather information directly. That’s been the idea behind, for instance, introducing air-quality monitors that send data back to central authorities rather than relying on local officials who may be in the pocket of polluting industries. But many aspects of good governance are too complicated to allow that kind of direct monitoring and instead rely on data entered by those same local officials.


To counter the point of the pervasive collection of data, is the understanding of how bad data collection is in many cases.  While the theory of the government getting access to large amounts of data to help make decisions about policies might be good, the reality is that data collection is often poor, is often incentivised to be modified by exactly the same people who would fail to report on it via official mechanisms.
This article also highlights the second issue with large scale data collection and policy, in that organisations will over ambitiously attempt to implement their version of policies, regardless of the original intent.  The example in the article was one of a college not admitting a student because their parent was on a government blacklist, which wasn't the intent of the policy or the blacklist, but I'm sure you can imagine plenty of other cases where organisations will interpret the data or lists as they expect rather than intended.  The Law of Unintended Consequences will apply, and as they say, the road to hell is paved with good intentions


## [Meet 'Intrusion Truth,' the Mysterious Group Doxing Chinese Intel Hackers - Motherboard](https://motherboard.vice.com/en_us/article/wjka84/intrusion-truth-group-doxing-hackers-chinese-intelligence)

[https://motherboard.vice.com/en_us/article/wjka84/intrusion-truth-group-doxing-hackers-chinese-intelligence](https://motherboard.vice.com/en_us/article/wjka84/intrusion-truth-group-doxing-hackers-chinese-intelligence)

> “We won’t achieve anything by publicly naming,” Andrei Barysevich, director of advanced collection at threat intelligence firm RecordedFuture, told Motherboard at the annual Black Hat cybersecurity conference earlier this month. Likely the only time the company may publish names is in a direct collaboration with law enforcement, a RecordedFuture spokesperson added. Legal issues are also a concern—accusing someone of being a government hacker, and likely a criminal in some contexts, without robust evidence could open up a company to libel cases.
> 
> ADVERTISEMENT
> “There’s no upside,” Barysevich said. Several other cybersecurity researchers felt the same.
> 
> Intrusion Truth, awarded the protection of anonymity and free from commercial liability, is taking another approach.
> 
> “We are directly challenging this illegal and unfair activity by exposing those responsible, naming the hackers themselves and identifying the agencies that hide behind them. We will be tireless in our approach and already have a large network of analysts working with us,” Intrusion Truth told Motherboard.


This is an interesting story, and an interesting ethical debate.  In particular, one of the comments caught my eye, that government employed hackers are probably doing completely legal jobs within their nation, but that by being exposed they may find it harder to travel or to work abroad.


