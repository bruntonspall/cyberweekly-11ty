---
title: "135 - How to tell truth from fiction"
date: 2021-02-07
description: "Supermicro.  Remember them?  That story from Bloomberg that there was chinese malware in SuperMicro motherboards that could entirely compromise computers from below the operating system for which there was a lot of very strong denials from almost everyone involved."
permalink: /how-to-tell-truth-from-fiction/
---

Supermicro.  Remember them?  That story from Bloomberg that there was chinese malware in SuperMicro motherboards that could entirely compromise computers from below the operating system for which there was a lot of very strong denials from almost everyone involved.

I’ve raised a few times that my distrust of major newspapers is based not only on 7 years of working for one, but because of the so-called [gell-man amnesia effect](https://www.goodreads.com/quotes/65213-briefly-stated-the-gell-mann-amnesia-effect-is-as-follows-you), which is that when we read a major “trustworthy” newspaper article on area of our expertise, we notice all the flaws and lack of detailed expertise, but we trust newspapers on the next page over.

While not entirely accurate, as newspaper journalists on politics and international desks actually often are experts on their area, but within technology and cybersecurity, its certainly the case that big names doesn’t always mean accuracy.  Firstly, you can never be sure who wrote the story.  Some newspapers have some very good tech reporters who understand the technology, but often when a big story breaks, it tends to be given to the big name journalists to cover and write, not the technology desk.

But this creates real problems for us when we consume news.  As I pointed out last week with the link to the [Axios Codebook](https://www.axios.com/newsletters/axios-codebook-b04bf6f5-5c30-45ba-95b9-fbe944b6a668.html), our news reporting also suffers from an availability bias.  We only get to hear about cyber operations that the news sources we follow will raise, so those reporters are focused on certain countries, you wont get to read about attacks carried out by other countries.  And of course, a good nation state, espionage motivated cyber attack should never be known about, so we almost certainly don’t know about some portion of the attacks.  Worse, we probably don’t even know how many of few we know about... do we miss just 10% or do we miss 90%?

This bias means that it can be really difficult when a news story breaks to work out what action we should be taking.  If you believe the news at surface value, the most recent attack was almost entirely SolarWinds related.  But there’s quiet threads you can pick up, as Gizmodo have, that shows that it’s very likely that the same actor has been carrying out a far more complex campaign than is really noticed.  Many of us have already forgotten that this all started with the discovery that FireEye had been targeted.  If that had been more successful, would we have been talking about the compromise of FireEye security devices instead?

The one clear thing that comes from all of this is that there is some critical software that runs our systems, from managing our Active Directory, managing the network, or synchronising emails to the cloud.  These are generally highly privileged and we still struggle to correctly limit such privileged software to ensure that it has permissions to do it’s job, without having permissions to compromise the entire network.  We need to focus more on these backend services and the management, monitoring and enforcement of them.  It’s not cool and interesting security work, but it should be high on our priority lists.

## [What2Log - About](https://what2log.com/about/)

[https://what2log.com/about/](https://what2log.com/about/)

> What2Log was a project that began when we saw a noticeable gap in computer security notation in regards to logs. There had not been a centralized resource of what and how to understand the logs of the major operating systems that are used everyday. What2Log was made to fill that exact gap.


This looks like a super useful tool for learning how to get the logs you want, and ship them somewhere.  Some of this is a little basic, but I can see at a glance how it pulls this info together easily and makes it trivial for non security teams to consume.
Something that looks like this, but with defined profiles would be a great resource that your security team can provide to the organisation 


## [The balkanization of the cloud is bad for everyone | MIT Technology Review](https://www.technologyreview.com/2020/12/17/1014967/balkanization-cloud-computing-bad-everyone/)

[https://www.technologyreview.com/2020/12/17/1014967/balkanization-cloud-computing-bad-everyone/](https://www.technologyreview.com/2020/12/17/1014967/balkanization-cloud-computing-bad-everyone/)

> The trend toward digital sovereignty has unleashed a digital arms race that slows down innovation and offers no meaningful benefit to customers.
> 
> Companies like Amazon and Microsoft may well be able to afford to keep expanding their cloud computing platforms into new countries, but they are the exception. Thousands of smaller companies that provide cloud services on top of these platforms don’t have the financial or technological wherewithal to make their products available in every data center.
> 
> In Europe, for example, the GAIA-X project may only strengthen the large incumbents. And in China, the vast majority of foreign software providers have decided not to make their cloud services available there because the hurdles are too formidable. This does both Chinese customers and foreign technology providers a disservice. It also unwinds all the economic and security advantages of a global cloud.


This balance between protecting the privacy rights of its citizens and enabling the international commerce of its businesses is tricky.

GDPR regulates what any country should be doing with European citizen data, and the rise of other national laws to regulate the their own citizens should be no surprise.  International agreement on this would make some of this easier, but I don't see that happening anytime soon


## [5 things we learned in the first 6 months of New Style ESA going online - DWP Digital](https://dwpdigital.blog.gov.uk/2021/01/29/five-things-we-learned-in-the-first-six-months-of-new-style-esa-going-online/)

[https://dwpdigital.blog.gov.uk/2021/01/29/five-things-we-learned-in-the-first-six-months-of-new-style-esa-going-online/](https://dwpdigital.blog.gov.uk/2021/01/29/five-things-we-learned-in-the-first-six-months-of-new-style-esa-going-online/)

> The combination of remote working and the pace of the challenge created an environment where we almost worked in isolation, just being consumed by all things NS ESA. However, it soon became obvious that we were not alone in the challenges we faced. I reached out to other Product Managers in similar situations, both in terms of service context and GDS journeys, and it’s been really valuable to share experiences and ensure we learn from each other’s successes and also mistakes.


It’s super hard to really articulate the value of collaboration platforms and tools. If your staff are easily able to reach out to others who may have experienced similar things, then knowledge and learning can easily flow around.  This sort of thing is almost immeasurable, but also incredibly valuable.


## [Even overs: The prioritization tool that brings your strategy to life | by Jurriaan Kamer | The Ready | Jan, 2021 | Medium](https://medium.com/the-ready/even-overs-the-prioritization-tool-that-brings-your-strategy-to-life-e4f28f2949ac)

[https://medium.com/the-ready/even-overs-the-prioritization-tool-that-brings-your-strategy-to-life-e4f28f2949ac](https://medium.com/the-ready/even-overs-the-prioritization-tool-that-brings-your-strategy-to-life-e4f28f2949ac)

> A better approach is to make trade-offs explicit, by choosing one thing over another thing. Done well, it will result in focus, clarity, alignment, better decision-making, and competitive edge. We want to share with you a practical method that we often use with our clients: the even over statement.
> 
> What are even over statements?
> 
> An even over statement is a phrase containing two positive things, where the former is prioritized over the latter.
> 
> A good thing even over another good thing
> 
> Even overs can be applied practically anywhere. They can be used in defining a product strategy, company values, team working agreements, or for seeking behavior change. Even overs can help make these things actionable, as they often aren’t.
> 
> It is tempting to phrase even overs as “a good thing even over a bad thing”, for example empathy even over arrogance, but that reduces its usefulness as there is no real trade-off. An even over should be just as valid when reversed. As an exercise, if you were to reverse some of the examples above, can you see how it might affect the resulting outcomes?


This is a lovely approach for prioritising your strategy.  I remember reading a while back about political statements that are “null statements”, for example “I will be tough on crime” is meaningless because it’s almost impossible to argue the opposite.

These even overs feel like the same kind of statement, and I’ve fallen into that trap before, of good thing even over bad thing.  If you can’t argue for the reverse, it’s not a meaningful trade off


## [Building effective security OKRs. This is an abridged version of my… | by Alex Smolen | Medium](https://alsmola.medium.com/building-effective-security-okrs-94f249230a39)

[https://alsmola.medium.com/building-effective-security-okrs-94f249230a39](https://alsmola.medium.com/building-effective-security-okrs-94f249230a39)

> Here’s our team’s process for building OKRs:
> 
> * Assess prior OKRs
> * Do a live group risk assessment
> * Find inspiration through an article or video
> * Do a bottoms-up brainstorming exercise
> * Use post-it notes and voting
> * Set up time to review with other teams
> * Stay tuned in to company wide goals
> * Prioritize objectives based on impact
> * Document objectives, key results, and initiatives
> * Publish OKRs to get feedback and alignment
> * Execute, rinse, and repeat
> 


This is a good read on thoughts before setting security OKR's for your team to measure how well you are performing and setting good measurable objectives for the team.  I've summarised the process in the quote, it's worth a read if you are considering implementing OKR's


## [DRMacIver's Notebook: We are surrounded by ghosts](https://notebook.drmaciver.com/posts/2020-02-16-14:22.html)

[https://notebook.drmaciver.com/posts/2020-02-16-14:22.html](https://notebook.drmaciver.com/posts/2020-02-16-14:22.html)

> It is very often the case that even when knowledge is written down somewhere, it's nearly impossible to find it. This has happened to me in mathematics before: A friend and I once discovered a result that we thought was very interesting (under certain conditions, the best possible continuous approximation to a discontinuous fucntion exists), only to eventually discover that the result was known, it had just been published in an obscure mathematical journal, in the 1970s, in Poland, so virtually nobody knew about it. Fortunately we had never put in much serious effort into trying to publish it before discovering that (honestly we probably should have, but neither of us were professional mathematicians by that point), but it was still annoying.
> 
> 


This concept of Ghost Knowledge is really valuable.  As David Maciver points out, this isn’t just a thing in academic sectors like Mathematics, but is true in almost all knowledge pools.  This is why when you join a new organisation you get told about the “way we do things here”, or why different bits of IT are discovering DevOps or Microservices from scratch over and over again.

This problem is exactly why I started writing CyberWeekly.  I was in conversation with someone who essentially said to me “Did you know about thing X”, and my response had to be “Oh yes, I read about that a few years ago” and everyone involved wondered why I didn’t tell anyone.

But when something is clear to you because you’ve read or been exposed to it, it becomes increasingly tricky to work out how to expose people to that reading.  Cyber Weekly is a way that I can literally create a paper trail of the things I’ve read that seem interesting. 


## [The Next Cyberattack Is Already Under Way | The New Yorker](https://www.newyorker.com/magazine/2021/02/08/the-next-cyberattack-is-already-under-way)

[https://www.newyorker.com/magazine/2021/02/08/the-next-cyberattack-is-already-under-way](https://www.newyorker.com/magazine/2021/02/08/the-next-cyberattack-is-already-under-way)

> Perlroth writes, “It was often hard to see where the NSA’s efforts ended and Facebook’s platform began.” Only the arrival of the iPhone, in 2007, proved a greater boon to government surveillance.
> 
> Cyberattacks made headlines, and then vanished. In 2008, Russia got into a network at the Pentagon; hackers broke into the campaigns of both Barack Obama and John McCain; the next year, North Korea compromised the Web sites of everything from the Treasury Department to the New York Stock Exchange. In 2010, a computer worm called Stuxnet, created by the U.S. and Israel in an operation approved by George W. Bush and continued by Obama, was discovered to have devastated Iran’s nuclear program. Perlroth, who started covering cybersecurity for the Times a year later, is arguing that, if you build a worm like that, it’s eventually going to come back and eat you.
> 
> In 2012, Iranian hackers destroyed the data of thirty thousand computers used by a Saudi oil company. That year, Republicans in the Senate filibustered a law that would have required American companies to meet minimum cybersecurity regulations. Two years later, North Korean hackers attacked Sony. (As Perlroth observes, the press coverage mainly concerned gossip that was found in Sony executives’ e-mails, not North Korea’s ability to hack into American companies.) Russia, in the same period, was “implanting itself into the American grid,” hacking into systems that controlled basic infrastructure, from pipelines to power switches. By 2015, Russians were inside the State Department, the White House, and the Pentagon. The hackers didn’t turn things off; they just sat there, waiting. Beginning in 2014, in anticipation of the 2016 election, they fomented civil unrest through fake Twitter and Facebook accounts, sowing disinformation. They broke into the computers of the Democratic National Committee. As with the Sony attack, the press mostly reported the gossip found in the e-mails of people like John Podesta. All the while, as Perlroth emphasizes, Russian hackers were also invading election and voter-registration systems in every state in the country. Donald Trump’s response, once he was in office, was to deny that the Russians had done anything at all, and to get rid of the White House cybersecurity coördinator.


When you put it that way,  we have had quite a rotten decade in cybersecurity terms.

This is a slightly over-breathless, over egged whirlwind tour of the rise in the use and abuse of zero-day attacks by nation states, and indicates the scope of the quiet silent conflict that carries on in the background of everyday internet activity.


## [Cleaning up after Emotet: the law enforcement file - Malwarebytes Labs | Malwarebytes Labs](https://blog.malwarebytes.com/threat-analysis/2021/01/cleaning-up-after-emotet-the-law-enforcement-file/)

[https://blog.malwarebytes.com/threat-analysis/2021/01/cleaning-up-after-emotet-the-law-enforcement-file/](https://blog.malwarebytes.com/threat-analysis/2021/01/cleaning-up-after-emotet-the-law-enforcement-file/)

> For victims with an existing Emotet infection, the new version will come as an update, replacing the former one. This is how it will be aware of its installation paths and able to clean itself once the deadline has passed.
> 
> Pushing code via a botnet, even with good intentions, has always been a thorny topic mainly because of the legal ramifications such actions imply. The DOJ affidavit makes a note of how the “Foreign law enforcement agents, not FBI agents, replaced the Emotet malware, which is stored on a server located overseas, with the file created by law enforcement”.
> 
> The lengthy delay for the cleanup routine to activate may be explained by the need to give system administrators time for forensics analysis and checking for other infections.


The takedown of Emotet’s command and control structure is quite a move by itself, but then using the malware self-updating mechanism to deploy code that nullifies and uninstalls the malware gets legally tricky really quickly.

The state, through law enforcement, is running code on compromised devices without the owners permission.  Granted the intent here is to secure the device, but if there’s any error in there and it causes further damage or disruption to the compromised devices, whose fault would it be?  Generally, I support this, I think that cleaning up compromised devices is something we should be doing, for the health of the network if nothing else, but calls for “the greater good” are not popular for good reasons.

It doesn’t help that the breakdown makes clear that the law enforcement update includes a coding mistake, one that apparently won’t matter, but suggests just easy it would be to create a very difficult situation for everyone.  


## [The SolarWinds Hack Just Keeps Getting More Wild](https://gizmodo.com/the-solarwinds-hack-just-keeps-getting-wilder-1846193313)

[https://gizmodo.com/the-solarwinds-hack-just-keeps-getting-wilder-1846193313](https://gizmodo.com/the-solarwinds-hack-just-keeps-getting-wilder-1846193313)

> Investigators have sought to understand the extent of the breach, but they are struggling. Case in point: the recent discovery that nearly a third of the victims of the so-called “SolarWinds” scandal were not actually SolarWinds customers and, therefore, had been compromised by other (so far unknown) means.
> 
> The whole debacle was initially discovered in December. If you’ve been asleep since then, here’s the run-down: Investigators discovered that hackers had infiltrated networks throughout the government, Fortune 500 companies, and other entities using trojanized malware that had been affixed to software updates for SolarWinds’ Orion, a popular IT management program.


This gizmodo article does a good job summing you everything we know about the attack so far, some of the odder claims and covers (or links to) an important point.  [Some victims did not use Solarwinds](https://gizmodo.com/30-of-solarwinds-hacking-victims-did-not-actually-use-1846160687).  If you are linking this attacker to a campaign, it would be wrong to label it purely a Solarwinds campaign.  It feels like Solarwinds was one of several prongs of the campaign, which leaves us to wonder what else there is.


## [The Hack Roundup: USDA Denies Data Breach at Payroll Facility  - Nextgov](https://www.nextgov.com/cybersecurity/2021/02/hack-roundup-usda-denies-data-breach-payroll-facility/171842/)

[https://www.nextgov.com/cybersecurity/2021/02/hack-roundup-usda-denies-data-breach-payroll-facility/171842/](https://www.nextgov.com/cybersecurity/2021/02/hack-roundup-usda-denies-data-breach-payroll-facility/171842/)

> [Reuters first reported on Tuesday](https://www.reuters.com/article/us-cyber-solarwinds-china-exclusive/exclusive-suspected-chinese-hackers-used-solarwinds-bug-to-spy-on-u-s-payroll-agency-sources-idUSKBN2A22K8) that the department’s National Finance Center, which runs a payroll system serving over 600,000 federal employees across 160 agencies, was penetrated by suspected Chinese hackers exploiting a flaw in SolarWinds’ software.    
> 
> The intrusion is separate from earlier reports in December associated with a trojanized update SolarWinds distributed to about 18,000 of its customers, according to Reuters. In response to that hacking campaign, which a number of agencies acknowledged they were affected by, the Cybersecurity and Infrastructure Security Agency directed all agencies to remove certain SolarWinds products from their systems. Government officials have since publicly said Russia is likely behind that event, along with the abuse of authentication configurations in Microsoft’s Office 365 cloud service


This is a confusing story.  The Reuters story was one I was slightly dubious of, because of having been bitten by other major non-cyber specialist news organisations getting basic stories wrong recently.  

But the story seemed well backed up, and while I disagree with the headline, it did sound supported that there had been a breach, and that the attackers had made use of a flaw in Solarwinds Orion during the course of the attack.  It was clear that this wasn’t a supply chain attack, or even particularly novel.  But then the USDA deny even that breach, leaving us all a little confused.  


