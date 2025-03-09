---
title: "45 - How secure is our software?"
date: 2019-03-30
description: "While the debate about the geopolitical implications of Huawei software managing western 5G networks continues on, we really should be worrying about how secure is the software that manages... well everything."
permalink: /how-secure-is-our-software/
---

While the debate about the geopolitical implications of Huawei software managing western 5G networks continues on, we really should be worrying about how secure is the software that manages... well everything.

We rely, in this day and age, on software to manage pretty much everything, from firmware updates on our computer, operating systems, wordpress themes, airplanes and self driving cars.  Software is behind a huge amount of these things, and the bad news for us all, is that much of it is badly written, poorly tested and of dubious provenance.

While I still believe that patching early and patching often is the most useful cyber security control that you can apply in almost any circumstance, we have to acknowledge that patching mechanisms aren't necessarily safe, and that we have to get our updates from somewhere.

While those of us who do cybersecurity on a regular basis are arguing about the exact best configuration of PKI, CA assertions and update mechanisms, far more people will be installing wordpress themes into their blogs or other far less trusted code, and it's hard to get individuals to care about this kind of problem, because if it doesn't negatively affect them, then there's little to no cost to running untrusted software.

As software gets more complex, this problem is only going to get harder.  I was in a session at a conference yesterday where the discussion of testing the provenance and security of containers was raised, and while there were some interesting ideas, essentially most people shrugged and simply expressed that you had to trust the major projects of building valid and acceptable containers.  It looks like, even when you have smart people in a room, the general consensus is "Supply chains are hard".  Worse still, I think it's perceived as being "not a fun problem" to solve and so everyone would just rather get on with solving their business problems instead.

## [The Filter Bubble is Actually a Decision Bubble - Baekdal Plus](https://baekdal.com/trends/the-filter-bubble-is-actually-a-decision-bubble/)

[https://baekdal.com/trends/the-filter-bubble-is-actually-a-decision-bubble/](https://baekdal.com/trends/the-filter-bubble-is-actually-a-decision-bubble/)

> To really fix this problem, we need to think about this in a different way. First of all, remember what I said in the beginning of this article. The problem we are faced with today is not a filter bubble, it's a decision bubble.
> 
> So already here, we can see how differently we really need to approach this. You can't fix this by trying to show people more information from more sources. Instead, we need to approach this in terms of why these decisions happen in the first place.
> 
> So, we need to approach this in two ways. There is one approach for people who are already convinced by something that isn't true, and then there is another approach for normal people who haven't been 'converted' yet.
> 
> So let's talk about the people who have already decided to believe something that isn't true.
> 
> What we need to realize is that we cannot fix this by telling them that they are wrong. They already know this and they have just chosen not to believe it. No amount of 'fact-checking' is ever going to change that.
> 
> What we need to do instead is to figure out why they made the decision to think this way in the first place.


Super insightful, the key takeaway here is that there are people who in possession of the same facts as you, will come to different conclusions.  Rarely will providing them with more facts actually change their minds, instead you need to understand what drove them to that conclusion and engage with them on that level.

So whether they are claiming that patching increases your risk, passwords need high entropy and regular changing, or that devops is less secure than "well managed systems", simply throwing facts at the problem probably won't help, and will just frustrate everyone.


## [Former CIA leaders give ‘briefing book’ to 2020 candidates to counteract ‘fake news’ and ‘foreign election interference’ - The Washington Post](https://www.washingtonpost.com/world/national-security/former-cia-leaders-give-briefing-book-to-2020-candidates-to-counteract-fake-news-election-interference/2019/03/27/22e11fcc-50a2-11e9-8d28-f5149e5a2fda_story.html?utm_term=.e73aa74d8138)

[https://www.washingtonpost.com/world/national-security/former-cia-leaders-give-briefing-book-to-2020-candidates-to-counteract-fake-news-election-interference/2019/03/27/22e11fcc-50a2-11e9-8d28-f5149e5a2fda_story.html?utm_term=.e73aa74d8138](https://www.washingtonpost.com/world/national-security/former-cia-leaders-give-briefing-book-to-2020-candidates-to-counteract-fake-news-election-interference/2019/03/27/22e11fcc-50a2-11e9-8d28-f5149e5a2fda_story.html?utm_term=.e73aa74d8138)

> But this unclassified document has the feel of an urgent primer, a way to quickly get the candidates up to speed on issues any president will face and to dispel myths and misperceptions.
> 
> “We are in­cred­ibly divided as a nation . . . and there are debates about what the facts and the truth are on key issues,” Morell said. “When it comes to national security, that’s a dangerous thing.”
> 
> Morell and McLaughlin, who have participated in the classified presentations to nominees in the past, enlisted former intelligence officials to write short articles highlighting the key issues in their areas of expertise. The briefing book covers 10 topics, including cybersecurity, China’s expanding power, U.S.-Russia relations, North Korea’s nuclear weapons ambitions and tensions with Iran. 


My biggest concern with this is that it really does follow the plan of "provide people with more facts" to see if you can educate them.

For many of these politicians or their teams, they won't have considered many of these things, but if the filter bubble article is to be believed, facts may not help at all.

I do however really really want to read a copy of this report now!


## [Exclusive: Told U.S. security at risk, Chinese firm seeks to sell Grindr dating app | Reuters](https://www.reuters.com/article/us-grindr-m-a-exclusive/exclusive-u-s-pushes-chinese-owner-of-grindr-to-divest-the-dating-app-sources-idUSKCN1R809L)

[https://www.reuters.com/article/us-grindr-m-a-exclusive/exclusive-u-s-pushes-chinese-owner-of-grindr-to-divest-the-dating-app-sources-idUSKCN1R809L](https://www.reuters.com/article/us-grindr-m-a-exclusive/exclusive-u-s-pushes-chinese-owner-of-grindr-to-divest-the-dating-app-sources-idUSKCN1R809L)

> The Committee on Foreign Investment in the United States (CFIUS) has informed Kunlun that its ownership of West Hollywood, California-based Grindr constitutes a national security risk, the two sources said.
> 
> CFIUS’ specific concerns and whether any attempt was made to mitigate them could not be learned. The United States has been increasingly scrutinizing app developers over the safety of personal data they handle, especially if some of it involves U.S. military or intelligence personnel.


I believe that military organisations and intelligence organisations are unaware of how much data third party organisations is building on people, and the ways that this data could be applied to track people.  Operational Security is generally poor even among the most sensitive individuals, as the hack of Military Singles by LulzSec back in 2012 showed, with hundreds of thousands of serving military officers sharing a lot of operational information in their private messages and profiles.

The private sector companies have a lot of identifiable data, which is precisely why OSINT tools for finding out more about your targets before you conduct a major attack are so valuable.


## [Operation ShadowHammer | Securelist](https://securelist.com/operation-shadowhammer/89992/)

[https://securelist.com/operation-shadowhammer/89992/](https://securelist.com/operation-shadowhammer/89992/)

> In January 2019, we discovered a sophisticated supply chain attack involving the ASUS Live Update Utility. The attack took place between June and November 2018 and according to our telemetry, it affected a large number of users.
> 
> ASUS Live Update is an utility that is pre-installed on most ASUS computers and is used to automatically update certain components such as BIOS, UEFI, drivers and applications. According to Gartner, ASUS is the world’s 5th-largest PC vendor by 2017 unit sales. This makes it an extremely attractive target for APT groups that might want to take advantage of their userbase.
> 
> Based on our statistics, over 57,000 Kaspersky users have downloaded and installed the backdoored version of ASUS Live Update at some point in time. We are not able to calculate the total count of affected users based only on our data; however, we estimate that the real scale of the problem is much bigger and is possibly affecting over a million users worldwide.
> 
> The goal of the attack was to surgically target an unknown pool of users, which were identified by their network adapters’ MAC addresses. To achieve this, the attackers had hardcoded a list of MAC addresses in the trojanized samples and this list was used to identify the actual intended targets of this massive operation. We were able to extract more than 600 unique MAC addresses from over 200 samples used in this attack. Of course, there might be other samples out there with different MAC addresses in their list.


What does a nation state attack actually look like?  This is a great example of this in action.  Potentially over 1 million infected devices, but targetted intrusion for only 600 of those devices.  That's less than 0.1% of the potential targets.

Targeting the built in OS updater is something that must have taken a fair amount of effort, and of course, should scare us all slightly, because we really don't have much choice but to trust our hardware and operating system suppliers.  

Remember however that this sort of attack is rare, and you shouldn't turn off updates and patches out of worry from this sort of attack.  The benefit of regular patches far outweighs the risk that a nation state will conduct this attack against you.


## [Huawei's Problem Isn't Chinese Backdoors. It's Buggy Software | WIRED](https://www.wired.com/story/huawei-threat-isnt-backdoors-its-bugs/)

[https://www.wired.com/story/huawei-threat-isnt-backdoors-its-bugs/](https://www.wired.com/story/huawei-threat-isnt-backdoors-its-bugs/)

> The findings come amid a concerted Trump administration effort to ban Huawei products around the world (particularly in 5G wireless networks), because of concerns that Huawei devices are controlled by the Chinese government or that Huawei would take orders from Beijing to undermine its security protections if asked.
> 
> Though the geopolitical discourse has gotten heated, the report concluded that the flaws in Huawei's code are related to "basic engineering competence and cyber security hygiene" and could be exploited by anyone. The report does not conclude that the bugs are intentional backdoors created for the Chinese government. Such broad exposure is still problematic—it could be exploited as well by US espionage agencies and the rest of the Five Eyes, but that’s of less concern to the White House.
> 
> "There is no backdoor, because Huawei doesn’t need a backdoor. It has a front door," says James Lewis, a former State Department official and director of the Center for Strategic and International Studies' Technology and Public Policy Program. "The UK government has lots of problems with Chinese hacking. It’s not like there are Swedish hackers breaking in to steal British intellectual property every week. If Huawei was a Swedish company or a Brazilian company or something it wouldn’t be having these troubles. But it's seen as a tool of a very aggressive Chinese government."


I sat and read the HCSEC report, and I agree with Wired's findings here.  The HCSEC Oversight report can be summed up as "we have confidence that HCSEC is capable of assessing Huawei technology.  But that technology is a mess that looks like many large engineering firms development capability.  It's therefore difficult to build any confidence in the assurance that we might build".

The comment here from the Center for Strategic and International Studies is however naive in it's application.  The flag bearing nature of the writer of poor software is kind of irrelevant to the flag bearing nature of potential attackers.  We find holes in software written in every country, and are exploited by many nations and independent groups.  The risk here is that the software has so many holes, that it cannot be considered to be secure against a nation state level attacker.


## [Failed Efforts to Warn Allies Away from Huawei 5G Technology Could Backfire on US](https://www.voanews.com/a/failed-efforts-to-warn-allies-away-from-huawei-5g-technology-could-backfire-on-us/4849182.html)

[https://www.voanews.com/a/failed-efforts-to-warn-allies-away-from-huawei-5g-technology-could-backfire-on-us/4849182.html](https://www.voanews.com/a/failed-efforts-to-warn-allies-away-from-huawei-5g-technology-could-backfire-on-us/4849182.html)

> Some of the United States' staunchest allies have made it plain that they do not see the Huawei threat as Washington does. Germany has announced that it will not ban the Chinese firm from its networks, and regulators in Britain have said that they are satisfied that any threat can be mitigated by inspection and monitoring.
> 
> Last month, an effort to block Huawei from participating in the 5G rollout in France died in the Senate, and Italy has not only embraced Huawei, but has become the first European country to accept funding from Beijing as part of China's "Belt and Road" program of infrastructure investment.
> 
> [...]
> 
> There has also long been suspicion, bordering on certainty in some sectors, that the company cooperates with Chinese intelligence services.
> 
> "I mean they are clearly malicious actors — I don't think there's any doubt about this," said Trae Stephens, a former U.S. intelligence officer, and a founder of Anduril Industries, which sells technology to the U.S. departments of Defense and Homeland Security. "The evidence has been presented over and over and over again. The intelligence community doesn't make spurious accusations that have no backing."


Much of the noise online about Huawei that you see online seems to follow this pattern.  US based, intelligence related people make assertive statements that the evidence has been presented.  But across the world we aren't really seeing those warnings being listened to.  That could be because the US hasn't presented enough evidence, or it could be because many of those nations really don't have much choice in the matter.

This is going to continue to bubble for the rest of the year at least, and possible the next few years.


## [The Boeing 737 Max crash is a warning to drivers, too.](https://slate.com/technology/2019/03/boeing-737-max-crashes-automation-self-driving-cars-surprise.html?wpmm=1&wpisrc=nl_todayworld)

[https://slate.com/technology/2019/03/boeing-737-max-crashes-automation-self-driving-cars-surprise.html?wpmm=1&wpisrc=nl_todayworld](https://slate.com/technology/2019/03/boeing-737-max-crashes-automation-self-driving-cars-surprise.html?wpmm=1&wpisrc=nl_todayworld)

> But automation has not made pilots’ jobs easier, says Steve Casner, a pilot and research psychologist at NASA’s Ames Research Center: “You’d think it would dumb down the role of the pilot. Contrary to expectation, you have to know more than ever.”
> 
> Casner is one of a number of pilots and analysts who see a parallel between the introduction of automation in airplanes more than 30 years ago and its arrival in cars today, as drivers prepare to relinquish the burdens of navigating the blacktop.
> 
> 
> “It’s like 1983 all over again,” Casner told me Monday. Where airlines by and large got it right, he thinks car-makers may be overeager in sticking humans in the car with unfamiliar technologies. “I’m very concerned that even though aviation has shown us how to do it, we’re about to make a big mistake with cars.


This is an interesting concept, that increases in automation actually makes the job harder rather than easier.  This seems to hold true in security, technology or operations just as much, in which often its harder to manage the automated system than it was to do it all by hand before the automation came along.

If you are involved in automating systems, are you being sure to understand how users will interact with your systems and what mental models they will be building of your system? Because diagnosis in a crisis situation is now significantly harder than it was before.


## [Getting it right this time: Why the strategy is not about delivery for NHSX](https://www.computerweekly.com/opinion/Getting-it-right-this-time-Why-the-strategy-is-not-about-delivery-for-NHSX)

[https://www.computerweekly.com/opinion/Getting-it-right-this-time-Why-the-strategy-is-not-about-delivery-for-NHSX](https://www.computerweekly.com/opinion/Getting-it-right-this-time-Why-the-strategy-is-not-about-delivery-for-NHSX)

> In short, it was clear that XYZ Pharma faced a stark choice in the emerging digital economy. Either it continued to deliver drugs as part of someone else’s ecosystem, or consider a platform play. In the case of a platform play, the strategy would never be pure delivery – it would be brokerage of a multi-sided market.


This is an insightful article from Mark Thompson, but this snippet really gets to the heart of the problem of "The strategy is delivery".

To many people interpret that as license to run off and just write code, deliver a product and keep doing so.  And as I've said before, compared to years spent navel gazing, talking about enterprise architecture patterns or writing strategy documents, delivering in this sense is miles better.
But the hardest thing for an organisation is working out what to deliver, and that's where the strategy really belongs.  

I don't think you need strategy business units with hundreds of people, but you do need to be able to work out what to deliver, whether it be a product, a platform, or a powerful data tracking mechanism disguised as an ad network.  To work out what to deliver, you need to understand the business contexts, understand a map of what your competitors are doing, and understand the market, and then work out delivery plays that ensure that you can deliver brilliant services for users that they want.


## [Security alert: pipdig insecure, DDoSing competitors - Jem - UK blogger](https://www.jemjabella.co.uk/2019/security-alert-pipdig-insecure-ddosing-competitors/)

[https://www.jemjabella.co.uk/2019/security-alert-pipdig-insecure-ddosing-competitors/](https://www.jemjabella.co.uk/2019/security-alert-pipdig-insecure-ddosing-competitors/)

> An unnamed client approached me this week complaining that her website, which was running a theme she’d purchased from a WordPress theme provider, was behaving oddly. Amongst other things, it was getting slower for no obvious reason. As speed is an important ranking factor for search engines (not to mention crucial for retaining visitors) I said I’d do some digging. What I discovered absolutely blew me away; I’ve never seen anything like it.
> 
> pipdig, one of the biggest WordPress theme providers to bloggers, is distributing code dressed up as the “pipdig Power Pack” plugin which amongst other things:
> 
> * is using other blogger’s servers to perform a DDoS on a competitor
> * is manipulating blogger’s content to change links to competitor WordPress migration services to point to the pipdig site
> * is harvesting data from blogger’s sites without permission, directly contravening various parts of the GDPR
> * is using the harvested data to, amongst other things, gain access to blogger’s sites by changing admin passwords
> * contains a ‘kill switch’ which drops all database tables
> * deliberately disables other plugins that pipdig has decided are unnecessary, without asking permission
> * hides admin notices and meta boxes from WordPress core and other plugins from the dashboard, which could contain vital information


It's possible that some of these functions were designed with entirely innocent purposes in mind, but the sheer number of them, as well as the attempts to hide the domain names that are targeted makes it look like this is a deliberate malicious attempt to monetise and use the plugin to achieve nefarious aims.

This reinforces the need to worry about our supply chains, just because you are a running wordpress, and it's patched and managed, someone else is writing your plugins and you need to trust them.  We don't have good models for how to measure that trust, or the impact of what it can do, and it's very difficult to actually assure any of this.  But this kind of thing does happen, and it's hard to find when it does.


## [What does it mean to be good at technology? – Public Digital](https://public.digital/2019/03/11/what-does-it-mean-to-be-good-at-technology/)

[https://public.digital/2019/03/11/what-does-it-mean-to-be-good-at-technology/](https://public.digital/2019/03/11/what-does-it-mean-to-be-good-at-technology/)

> When doing that you’ll remember that technology itself is very rarely where the asset or value lies. It’s in what you deliver for your users, the capabilities in the team, and the data you collect.
> 
> 


This series of posts about what a modern internet-era CTO looks like has been a really interesting read and good summation of the frustration I've seen expressed by organisations, that their CTO isn't really technical and doesn't understand any of this technology stuff.  James Stewart's view is that you need to understand technology even more today than you needed to before, because companies need to work out where to invest and spend their money.  

But this final point that the technology is there to achieve an aim, and has no real value by itself is the most important to me, because the failure mode of having a "internet-era" CTO, is that they are more likely to be excited by and invested in the technology itself.


## [RedTeam Pentesting GmbH - Cisco RV320 Unauthenticated Configuration Export](https://www.redteam-pentesting.de/en/advisories/rt-sa-2019-003/-cisco-rv320-unauthenticated-configuration-export)

[https://www.redteam-pentesting.de/en/advisories/rt-sa-2019-003/-cisco-rv320-unauthenticated-configuration-export](https://www.redteam-pentesting.de/en/advisories/rt-sa-2019-003/-cisco-rv320-unauthenticated-configuration-export)

> By issuing an HTTP GET request to this program, it was possible to export a router's configuration without providing any prior authentication. This vulnerability was adressed in firmware version 1.4.2.19 published by Cisco [3].
> 
> RedTeam Pentesting discovered that the CGI program in the patched firmware is still vulnerable. By performing a specially crafted HTTP POST request, attackers are still able to download the router's configuration. The user agent "curl" is blacklisted by the firmware and must be adjusted in the HTTP client. Again, exploitation does not require any authentication.


As I saw pointed out on Twitter, the UK Governments review of Huawei showed serious concerns about their ability to reliably build software repeatedly and their engineeering efforts.  But this shows that western firms like Cisco can also have bad software development practices.  Simply blocking curl user agents from accessing an API is not an acceptable patch and should never have got through the peer review process.


## [Agile Procurement for the Public Sector - A Primer](https://www.linkedin.com/pulse/agile-procurement-public-sector-primer-emilio-franco/)

[https://www.linkedin.com/pulse/agile-procurement-public-sector-primer-emilio-franco/](https://www.linkedin.com/pulse/agile-procurement-public-sector-primer-emilio-franco/)

> Let's face it - Contracts are ineffective approaches to managing relationships. There's just no way to easily and fully define the complexity and ambiguity of the interactions between clients and suppliers. Not only that, but in a complicated and exponential world, the nature of relationships can be unclear in the beginning and difficult to anticipate in advance.
> 
> Given this uncertainty, agile procurement works to set aside the heavy focus that traditional procurement places on requirements and contracts in favor of approaches that work in collaboration to develop a mutual understanding between the buyer and the supplier of what the client's needs are.


This is a lovely overview of how agile principles can be applied to government procurement processes. There’s lots of good bits in there, so much that I wanted to quote the entire thing, but this snippet sums it up for me.  Procurement processes give an illusion of control and stability.  But in reality, they have never really delivered what we’ve claimed that they do, so let’s tive agile procurement a chance and see if it’s better or worse.


## [helping organisations to play](https://stamplondon.co.uk/)

[https://stamplondon.co.uk/](https://stamplondon.co.uk/)

> Priorities Cards are a simple tool to help you explore the challenges that a CIO, CISO or CMO may face. They can be used in helping sales and marketing teams to better position their messaging and strategy. They can be used by C-suite teams to understand the relative priorities in their organisation. They can be used by technology or marketing teams to explore the breadth of what they should and could be doing.


These look like a lovely tool for assessing priorities and facilitating discussions and workshops with senior leaders.  There’s a CISO set of cards, as well as CIO and CTO sets of concerns to play the games with.


