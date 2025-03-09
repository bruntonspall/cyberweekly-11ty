---
title: "115 - Working from home forever?"
date: 2020-08-16
description: "What's the future going to look like?"
permalink: /working-from-home-forever/
---

What's the future going to look like?

I've been thinking about this a lot recently, and nothing is a bigger focus right now than working out how many of our societal shifts from COVID are going to stick around.

Will people continue to wash their hands and wear face coverings once the pandemic has a vaccine?  Doubtful.

Will people continue to work from home or at least not want to commute back to the office?  Much harder to predict.

Various surveys have been done, and it seems likely that lots of office workers and their bosses see this kind fo work continuing.  But there's also a huge number of social shifts that also need to happen to support a change in work ethos across the country.  From what shops are open and when, to the effect it will have on house prices, the ramifications of a work from home generational shift is massive.

But looking at the competing hypothesis, there must be a large number of people who are working from a 1 room bedsit, sat on teh end of their bed, from shared houses with barely enough room to swing a cat, and from family homes where multiple generations are fighting over access to the computer, to broadband and to rooms to themselves to carry out their endless video conferences.

It's not so clear cut that all organisations will go 100% remote, but if not that, what?

I think there's a far greater chance of organisations moving from a hub model, with big offices in expensive cities, to a far more distributed model.  Staff who work 2,3 or 4 days a week from a local WeWork or Regus shared office.  A place where they can sit comfortably and have social conversations.  These will bloom up all over the country, at a variety of costs, and organisations are going to have to think long and carefully about what the implications are.

Afterall, you trust people in your office, even a shared office.  Every single time I've been to a WeWork for work, someone has asked me to "watch their laptop" while they go get a coffee or nip to the toilet.  They don't know me, they don't know that I'm fundamentally a good person.  How do we have a conversation about sensitive financial information, or one-on-ones with our bosses while working in these environments?

Luckily, there are tech companies who have been working remote for some time.  The rise of Zero Trust computing is driven by some of this, the fact that you no longer have a corporate network requires new thinking.  The ways that we work are going to change, and we are going to need to predict those changes, and ensure that our staff can work safely and securely.

## [Research Casts Doubt on Value of Threat Intel Feeds](https://www.darkreading.com/threat-intelligence/research-casts-doubt-on-value-of-threat-intel-feeds/d/d-id/1338676)

[https://www.darkreading.com/threat-intelligence/research-casts-doubt-on-value-of-threat-intel-feeds/d/d-id/1338676](https://www.darkreading.com/threat-intelligence/research-casts-doubt-on-value-of-threat-intel-feeds/d/d-id/1338676)

> Unfortunately for potential customers, the uneven coverage means every threat intelligence provider's data set will be different, and there is little guarantee — or probability — that the threats will match what the customer will see. Without more information, the services are hard to evaluate, Bouwman said.
> 
> "This is what we refer to as a market with asymmetric information," he said. "The sellers know what they are selling, but the buyers don't know what they are buying."
> 
> The researchers compared the two commercial feeds with four open threat intelligence (OTI) feeds from Alienvault, Blocklist.de, CINScore, and EmergingThreats. While a few of the OTI feeds had significant overlap with other OTI sources, the commercial vendors had less than 1% overlap with any open threat intelligence feed. 
> 
> Even in tracking the same advanced persistent threat (APT) groups, threat intelligence vendors did not seem to collect the same data. Focusing on 22 threat groups that both vendors claimed to be tracking, the researchers found, at most, a 4% overlap in threat indicators, Bouwman said.


The problem with Threat Intelligence is that it's a [Lemon's Market](https://en.wikipedia.org/wiki/The_Market_for_Lemons).  You don't know whether the thing you bought is of value, precisely because it's supposed to tell you about something that is unknown.  While I don't think most threat intelligence organisations are attempting to defraud their customers, it's very difficult for independent observers to work out how useful that intelligence is.

Of course, the bigger thing in most organisations I've known is that the organisation cannot actually make use of the intelligence.  Knowing about potential adversaries and their TTP's is only of value if you've got the data from your logs to compare it against, and if you can use it to hunt down threats.  Most organisations simply aren't that advanced at their security operations capability.


## [RedCurl APT Group Hacks Global Companies for ...](https://www.darkreading.com/attacks-breaches/redcurl-apt-group-hacks-global-companies-for-corporate-espionage/d/d-id/1338664?_mc=rss_x_drr_edt_aud_dr_x_x-rss-simple)

[https://www.darkreading.com/attacks-breaches/redcurl-apt-group-hacks-global-companies-for-corporate-espionage/d/d-id/1338664?_mc=rss_x_drr_edt_aud_dr_x_x-rss-simple](https://www.darkreading.com/attacks-breaches/redcurl-apt-group-hacks-global-companies-for-corporate-espionage/d/d-id/1338664?_mc=rss_x_drr_edt_aud_dr_x_x-rss-simple)

> Mirkasymov notes the use of cloud services helps RedCurl fly under victims' radar. They don't pursue lateral movement or use active Trojans or RDP connections. They simply send a link and wait for victims to click. RedCurl.Dropper establishes connections with cloud storage services such as Cloudme, koofr.net, pcloud.com, and others.
> 
> "That's why it's not easy to detect their activity," he says. "They're really slow and silent."
> 
> Corporate Espionage: A New Threat to Watch
> RedCurl's activity varies depending on its target. Spear-phishing attacks are sent to different levels depending on the business: In an attack on a German company, they went to high-level staff; in others against firms in Russia and Canada, midlevel employees were targeted.
> 
> Similarly, the data stolen varied from business to business. RedCurl has taken contracts, financial documents, employee personal records, and records of legal action and facility construction. Mirkasymov notes RedCurl has taken investigation cases from law and consulting firms, and employee profiles containing polygraph test results from retailers. 


This is a nasty group. Often APT's are releatively noisy in your environment.  They'll attack, they'll compromise your systems and they'll either exfiltrate everything they can get their hands on, sell access to another noisy customer, or deploy ransomware/malware as a means of covering their tracks or making value out of the compromise. 

Slow and silent adversaries are some of the scariest, because they are far harder to detect, and far harder to predict.


## [NIST Special Publication 800-207 Zero Trust Architecture [pdf]](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf)

[https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf)

> ZT is not a single architecture but a set of guiding principles for workflow, system design and operations that can be used to improve the security posture of any classification or sensitivity level [FIPS199]. Transitioning to ZTA is a journey concerning how an organization evaluates risk in its mission and cannot simply be accomplished with a wholesale replacement of technology. That said, many organizations already have elements of a ZTA in their enterprise infrastructure today. Organizations should seek to incrementally implement zero trust principles, process changes, and technology solutions that protect their data assets and business functions by use case. Most enterprise infrastructures will operate in a hybrid zero trust/perimeter-based mode while continuing to invest in IT modernization initiatives and improve organization business processes.


NIST is recognising Zero Trust architectures as a fundamentally good thing.  This is a reasonable overview of Zero-Trust, although it’s not always the most readable summary!

I like that there’s a mention of the difficulties faced with adopting zero-trust, and the fact that most organisations are going to need to run a hybrid architecture for the foreseeable future.  The only thing that I think is missing is just how poorly most external cloud services actually support Zero-Trust models.  Once one of your users has authenticated to Trello, there’s very few controls you have, no ability to kill their session and no ability to provide granular permissions.  All of which belies the fundamental advantages of Zero Trust.


## [US Cyber Command is using unclassified networks to fight election interference](https://www.c4isrnet.com/cyber/2020/08/10/us-cyber-command-is-using-unclassified-networks-to-fight-election-interference/)

[https://www.c4isrnet.com/cyber/2020/08/10/us-cyber-command-is-using-unclassified-networks-to-fight-election-interference/](https://www.c4isrnet.com/cyber/2020/08/10/us-cyber-command-is-using-unclassified-networks-to-fight-election-interference/)

> “From a CYBERCOM standpoint, one of the big changes for us is we historically had been focused working inside [sensitive compartmented information facilities] SCIFs. One of the things we’ve done in support of 2020 is we have organizations now that live outside SCIFs,” Brig. Gen. William Hartman, the head of of U.S. Cyber Command’s Cyber National Mission Force, said during an Aug. 7 virtual panel hosted by DEFCON.
> 
> Hartman said forces are now working on unclassified networks, Slack channels and other platforms to communicate with the FBI, the Department of Homeland Security and private industry.
> 
> “We have really tried to adapt some of our behavior so we’re able to, in real time, collaborate with our partners across government on a little different timescale than a traditional military one because I know most of you are probably not up at 5:30 in the morning,” he said.


This is good news.  Too many government "cyber people" live their lives within the SCIF environments.  The world of slack, whatsapp and generally modern work place messaging has meanwhile passed them by, and they often struggle to see the value of open source intelligence and actions.

Moving themselves outside the SCIF is a clear indicator that they see the value of being out of the classified loop in order to collaborate with normal cyber security people as important.


## [Fortnite Creator Sues Apple and Google After Ban From App Stores - The New York Times](https://www.nytimes.com/2020/08/13/technology/apple-fortnite-ban.html)

[https://www.nytimes.com/2020/08/13/technology/apple-fortnite-ban.html](https://www.nytimes.com/2020/08/13/technology/apple-fortnite-ban.html)

> The fight began on Thursday morning with a clear provocation. Epic Games, the maker of Fortnite, started encouraging Fortnite’s mobile-app users to pay it directly, rather than through Apple or Google. The companies require that they handle all such app payments, so they can collect a 30 percent commission, a policy that has been at the center of antitrust complaints against the companies.
> 
> Hours later, Apple responded, removing the Fortnite app from its App Store.
> 
> “Epic enabled a feature in its app which was not reviewed or approved by Apple, and they did so with the express intent of violating the App Store guidelines,” Apple said in a statement. “We will make every effort to work with Epic to resolve these violations so they can return Fortnite to the App Store.”
> 
> Within an hour, Epic opened a multifront war against Apple that appeared months in the making.
> 
> First, it sued Apple in federal court, accusing the company of violating antitrust laws by forcing developers to use its payment systems.
> 
> Then Epic rolled out a sophisticated public-relations campaign that depicted Apple, one of the industry’s most image-conscious companies, as the stodgy old guard trying to stifle the upstart. To do so, it used Apple’s own imagery against it, mimicking Apple’s iconic “1984” ad from its own fight against IBM 36 years ago. This time, Fortnite characters were defying Apple’s totalitarian regime. Within hours, #FreeFortnite was the top trend on Twitter. [MBS: [Video here, worth a watch if only for amusement value](https://vimeo.com/447590857)]
> 
> Later on Thursday, Google also removed the Fortnite app from its official Android app store, the Google Play Store, saying the app violated Google’s policies. Epic replied with a similar lawsuit.


This is bigger than it appears.  Epic is a multi-billion dollar company and they object to paying 30% of their fees to the appstore for their In-App-Purchases (which one could easily describe as predatory given their popular marketing to the people least able to afford them).  Apple's polciies on what payments are allowed and what aren't is confusing at best, and leaves them on dodgy ground.

But that aside, the appstore is curated against the worst of the malware, the dodgy apps and so forth.  Open Source appstores are far far worse than both the Apple store and the Google Play store, where at least the companies attempt to screen the applications for the worst activity.

Epic will likely encourage their users to sideload the apps, selecting that option that says "install untrusted applications" and making millions of phones far more vulnerable to malware and drive by app installation.


## [Corporate America Worries WeChat Ban Could Be Bad for Business - WSJ](https://www.wsj.com/articles/corporate-america-worries-wechat-ban-could-be-bad-for-business-11597311003?mod=djemalertNEWS)

[https://www.wsj.com/articles/corporate-america-worries-wechat-ban-could-be-bad-for-business-11597311003?mod=djemalertNEWS](https://www.wsj.com/articles/corporate-america-worries-wechat-ban-could-be-bad-for-business-11597311003?mod=djemalertNEWS)

> “For those who don’t live in China, they don’t understand how vast the implications are if American companies aren’t allowed to use it,” said Craig Allen, president of the U.S.-China Business Council. “They are going to be held at a severe disadvantage to every competitor,” he added.
> 
> Other participants in the call Tuesday included Procter & Gamble Co., Intel Corp., MetLife Inc., Goldman Sachs Group Inc., Morgan Stanley, United Parcel Service Inc., Merck & Co. Inc. and Cargill Inc., according to the people.
> 
> [...]
> 
> Organizers started the call by introducing participating executives from the companies, which included those who deal with international relations and trade.
> 
> A number of participants raised concern that the order’s language suggests it could be applied to U.S. businesses all over the world, including in China, where WeChat TCEHY -0.69% is a dominant commercial platform.
> 
> Some participants also raised concerns about lack of clarity over whether the order applies to Tencent and its other platforms, pointing to the potential problems the National Basketball Association faces in its marketing deals with Tencent, which streams NBA games in China.


The implications for a WeChat ban are huge, because the order cuts out any dealings with TenCent.  Within hours, the Whitehouse was having to clarify whether it included companies TenCent had investment in, such as EpicGames and Fortnite (it didn't).  But this shows that US businesses are worried.  An increasingly isolationist US, seeking to focus on what's good for US consumers (such as preventing Chinese companies gathering their private data rather than the normal US companies) has forgotten that globalisation means that the largest customer markets for US companies are abroad.   China, with it's 1.4bn citizens is a huge target market, and all of those people use TenCent apps like WeChat to buy products and services.


## [Russian GRU 85th GTsSS Deploys Previously Undisclosed Drovorub Malware [pdf]](https://media.defense.gov/2020/Aug/13/2002476465/-1/-1/0/CSA_DROVORUB_RUSSIAN_GRU_MALWARE_AUG_2020.PDF)

[https://media.defense.gov/2020/Aug/13/2002476465/-1/-1/0/CSA_DROVORUB_RUSSIAN_GRU_MALWARE_AUG_2020.PDF](https://media.defense.gov/2020/Aug/13/2002476465/-1/-1/0/CSA_DROVORUB_RUSSIAN_GRU_MALWARE_AUG_2020.PDF)

> Drovorub is a Linux malware toolset consisting of an implant coupled with a kernel module rootkit, a file transfer and port forwarding tool, and a Command and Control (C2) server. When deployed on a victim machine, the Drovorub implant (client) provides the capability for direct communications with actor- controlled C2 infrastructure (T1071.0011); file download and upload capabilities (T1041); execution of arbitrary commands as "root" (T1059.004); and port forwarding of network traffic to other hosts on the network (T1090). The kernel module rootkit uses a variety of means to hide itself and the implant on infected devices (T1014), and persists through reboot of an infected machine unless UEFI secure boot is enabled in “Full” or “Thorough” mode.


Yup, that’s Linux targeting malware.  

There’s no details here on how it gets onto the system, you can assume it’s dropped once the attacker has breached your system and escalated their privileges.  This is the implant that lets them continue their control of the server once compromised.  

There’s enough technical detail here for you to build some network indicators as well as some yara and snort rules you can deploy.

The main thing is that’s this is quite complex, quite advanced malware.  There’s a lot of potentially blown Russian equities through the release of this report, and of course a healthy reminder that Linux isn’t “more secure” than your Windows estate.  There are APT’s capabilities that target Linux as well.


## [The age of the office is over – the future lies in Britain's commuter towns | Simon Jenkins | Opinion | The Guardian](https://www.theguardian.com/commentisfree/2020/aug/13/office-future-britain-commuter-towns-home-working)

[https://www.theguardian.com/commentisfree/2020/aug/13/office-future-britain-commuter-towns-home-working](https://www.theguardian.com/commentisfree/2020/aug/13/office-future-britain-commuter-towns-home-working)

> Across Britain there must be many people wondering if they really want to fight their way to a city office block when their home can be their office. Morgan Stanley reports a mere 18% of European office workers wanting to return to an office five days a week. Fulltime home working is estimated to raise productivity by more than 16 days over a full year.
> 
> The media is awash in studies declaring that offices are good for us after all. They promote social diversity and informal contacts, offering relief from relationship claustrophobia in “getting out of the house”. Management ideology has long identified “the company” with its headquarters, its physical presence and hierarchy. The New Scientist reports the boss of Microsoft worrying that unmonitored home working will eat into the “social capital” built up in an office environment. Zoom cannot replace the gossip of “those two minutes before and after” a meeting. We know that from TV’s The Office.
> 
> None the less, office workers seem certain to vote with their feet. As a Birmingham lawyer told the Guardian, “There is absolutely no reason for us to be in this office every day – I can do my job perfectly well from anywhere.” He spoke for millions. Hence the three-quarters of American CFOs now accepting that they must introduce remote working.


While I wont declare the age of the office over, I think the future is hybrid working.  Some staff will want to work from an office like environment (although I expect more satellite hubs like WeWork or Regus), Some staff will want to be 100% from home, but mostly we'll switch to a world where there's no guarantee that anyone will be in the office.


## [CEO Panel Survey 2020 - UK findings - PwC UK](https://www.pwc.co.uk/ceo-survey/ceo-panel-survey.html#key-findings)

[https://www.pwc.co.uk/ceo-survey/ceo-panel-survey.html#key-findings](https://www.pwc.co.uk/ceo-survey/ceo-panel-survey.html#key-findings)

> The onset of the COVID-19 pandemic prompted organisations to change their operations almost overnight, fast-tracking digital collaboration and new systems and services as millions of people were forced to work remotely.
> 
> Many of the changes adopted through necessity now look set to stick, with UK CEOs particularly committed to embedding them in their organisations, compared to their global peers.
> 
> The vast majority of UK CEOs believe COVID-19 has accelerated an enduring shift towards remote collaboration, increased automation and fewer people in workplaces.
> 
> * 86% of UK CEOs believe the shift towards remote collaboration will endure (compared to 78% globally)
> * 77% believe there will be an enduring shift towards increased automation (76% globally)
> * 68% believe the shift towards lower-density workplaces, with fewer people working together in person, will endure (61% globally)


All those "just for COVID" thigns you did, that risk acceptance for poorly configured VPN's and opening up ports to allow people to work from home. That stuff is going to stick around.

If you haven't already carried out a retrospective to understand not just the actions you took at risk during COVID, but also all of the ways the business went around you in order to operate at speed, then you are going to struggle in the coming months.  The clear action here is to understand the new state of your organisation, prioritise and work out how to make some of those emergency changes permanent.


