---
title: "34 - The sky is falling"
date: 2019-01-12
description: "2FA has been broken, and so it's all over.  This was what the news seemed to scream at me this week with the release of the modlishka tool."
permalink: /the-sky-is-falling/
---

2FA has been broken, and so it's all over.  This was what the news seemed to scream at me this week with the release of the modlishka tool.

As I've said repeatedly, many times, the most effective cyber security defense you can employ right now is 2FA.  The reason is that it moves attackers from harvesting credentials and using them later to having to perform an online attack and immediately deploy some feature to let themselves back in.

If we look at the [timeline for the OPM hack](https://www.wired.com/2016/10/inside-cyberattack-shocked-us-government/) the attackers found a credential and then came back during the long 4th of July weekend to seed their backdoor and get it working.  If that credential had required 2FA and the attackers didn't have access to generating it, then that later attack wouldn't have been possible, instead the attackers would have had to rush through with a session hijacking attack, which is noisier, easier to detect and in their rush they would have been more likely to make a mistake.

Security experts have always known that 2FA is not perfect, it's just a lot better than not having it.  However there is still a sense of absolutism, of black and white in cybersecurity matters.  Security policies and procedures are analysed by "security experts" and either declared useless or brilliant, with very little grading in between.

I sometimes complain about next generation firewall products and "advanced threat protection" products.  I do this not because I think these aren't good products (although some do have far better marketing than capabilities), but because in general network security barriers in normal firewalls are "good enough" and the same money would be better spent elsewhere.

## [The War-Torn Web – Foreign Policy](https://foreignpolicy.com/2018/12/19/the-war-torn-web-internet-warring-states-cyber-espionage/)

[https://foreignpolicy.com/2018/12/19/the-war-torn-web-internet-warring-states-cyber-espionage/](https://foreignpolicy.com/2018/12/19/the-war-torn-web-internet-warring-states-cyber-espionage/)

> Despite refusing to sign as sovereigns, the prominence of American companies in pushing for international internet agreements amid its governmental absence highlights one of Macron’s key points: “The internet is a space currently managed by a technical community of private players,” noted one source from the Macron government, quoted by Reuters, “But it’s not governed. So now that half of humanity is online, we need to find new ways to organize the internet.”


This is a long read, but worth it for thinking about the future of the internet.  The piece articulates that we are in a chaotic period where all sorts of nationstates and technology companies are all using the internet, but have very different ideas about how it should be governed and managed.

The internet has generally resisted governance precisely because it isn't just one thing.  The Arpanet was originally governed by ARPA, but adding connections to similar countries around the world and settling onto IP put some power into the hands of the Internet Assigned Numbers Authority (IANA), but once those critical basic addresses were issued, DNS root services and IP blocks, power shifted to places like the W3C for managing the web, the Internet Engineering Task Force (IETF) for defining standards in data transmission and so on.

Even world standards authorities aren't exempt from this, some standards online are managed by people like the ISO, others by BSI standards, the W3C, Unicode consortium and of course the original RFC process still sticks around.

While nation states might like to think that they can govern the internet, it's entirely unclear to me how anybody actually has the authority to make that happen across all of the various organisations without resistance from everyone else.

The next 20 years on the internet is going to be interesting.


## [Deepfakes and the New Disinformation War](https://www.foreignaffairs.com/articles/world/2018-12-11/deepfakes-and-new-disinformation-war)

[https://www.foreignaffairs.com/articles/world/2018-12-11/deepfakes-and-new-disinformation-war](https://www.foreignaffairs.com/articles/world/2018-12-11/deepfakes-and-new-disinformation-war)

> The most frightening applications of deepfake technology, however, may well be in the realms of politics and international affairs. There, deepfakes may be used to create unusually effective lies capable of inciting violence, discrediting leaders and institutions, or even tipping elections.


Interesting read.  Deep fakes is a worrying aspect from a geopolitical perspective as outlined in this article, but I'm also curious about the new Know Your Customer (KYC) rules and identify verification that new challenger banks are using.

For those who don't know, it's common to have to record a short video saying something like "I am Michael Brunton-Spall and I want to open an Monzo account" to verify your identity with someone like Monzo.  Deepfakes could be used to fake these videos to match the faked identity documents that were sent and I'm not sure how easy it would be to detect and avoid.

Finally, my understanding is that DeepFake technology is not realtime yet, that videos take minutes to render and produce, but it soon will be if it isn't already.  What does that mean for trust in videoconferencing facilities?  If I'm calling the security team on my in corporate technolgoy, how can I be sure that the video I see is actually the person I think I'm speaking too.  How attackers might use this is an interesting place to consider. Imagine the president/CEO calling security and authorising people to come into the building, or the CFO video calling to authorise a large payment.

Deepfakes, and our instinctive trust in our own eyes is going to be a running theme for the next 4 or 5 years, and deepfake detection technology is going to be a necessary development I think.


## [drk1wi/Modlishka: Modlishka. Reverse Proxy. Phishing NG.](https://github.com/drk1wi/Modlishka)

[https://github.com/drk1wi/Modlishka](https://github.com/drk1wi/Modlishka)

> ..Modlishka..
> Modlishka is a flexible and powerful reverse proxy, that will take your phishing campaigns to the next level (with minimal effort required from your side).
> 
> Enjoy :-)
> 
> Features
> Some of the most important 'Modlishka' features :
> 
> Support for majority of 2FA authentication schemes (by design).


This is a fascinating tool, and it's got a lot of press this week.

It's a very simple to deploy reverse proxy whcih you can point at a domain and it will strip out the security features and harvest credentials, including bypassing 2FA.

However, it's worth noting that the sky isn't actually falling.  This still requires active online monitoring and use.  If a user has authenticated via Modlishka, you've got their credentials and can take over their session in a normal session hijacking attack, but you'll have to do that before the session times out.  It doesn't look like it tries to keep the session alive (although my golang is not the best), and so the attacker will need to perform the session hijacking live and inline.  

However, for an organised group, this should be fairly easy to do, and this is a valuable tool for the redteam to use.  Just don't declare that 2FA is pointless and turn it off just because this tool exists.


## [A Growing Frontier for Terrorist Groups: Unsuspecting Chat Apps | WIRED](https://www.wired.com/story/terrorist-groups-prey-on-unsuspecting-chat-apps/?wpisrc=nl_cybersecurity202&wpmm=1)

[https://www.wired.com/story/terrorist-groups-prey-on-unsuspecting-chat-apps/?wpisrc=nl_cybersecurity202&wpmm=1](https://www.wired.com/story/terrorist-groups-prey-on-unsuspecting-chat-apps/?wpisrc=nl_cybersecurity202&wpmm=1)

> These activities—seemingly casual discussions, the exchange of links and usernames, and the sharing of propaganda and amateurish artwork—are exactly how recruitment takes place. Messenger apps now serve as outreach centers for ISIS media workers. And though these applications are attracting millions of new users, many seem unprepared to sift out bad actors.


Building a system that includes a "chatroom" functionality?  You need to think of this as an anti-persona, and one you need to worry about.

I'm sure that small crime gangs already use many chat methods, from discord to whatsapp etc, and with small scale they probably won't be noticed as much.

The difference in the activities of ISIS in this case is that this isn't small group discussion and coordination, it's that they want to advertise, they want to be seen by a wider audience.  They ideally want to reach the audience of people who will be interested and potentially able to be turned, without reaching a much larger audience of people who will be affronted or disgusted and report it, and treading that line is difficult for them.

If you are building systems with a social angle, this is yet another user behaviour that you are going to have to look for and work out how to moderate and shutdown effectively enough to prevent the widescale adoption.


## [On Ghost Users and Messaging Backdoors – A Few Thoughts on Cryptographic Engineering](https://blog.cryptographyengineering.com/2018/12/17/on-ghost-users-and-messaging-backdoors/)

[https://blog.cryptographyengineering.com/2018/12/17/on-ghost-users-and-messaging-backdoors/](https://blog.cryptographyengineering.com/2018/12/17/on-ghost-users-and-messaging-backdoors/)

> In its outlines, the idea they propose is extremely simple. The goal is to take advantage of existing the weaknesses in the identity management systems of group chat and calling systems. This would allow law enforcement — with the participation of the service provider — to add a “ghost user” (or in some cases, a “ghost device”) to an existing group chat or calling session. In systems where group membership can be modified by the provider infrastructure, this could mostly be done via changes to the server-side components of the provider’s system.
> 
> I say that it could mostly be done server-side, because there’s a wrinkle. Even if you modify the provider infrastructure to add unauthorized users to a conversation, most existing E2E systems do notify users when a new participant (or device) joins a conversation. Generally speaking, having a stranger wander into your conversation is a great way to notify criminals that the game’s afoot or what have you, so you’ll absolutely want to block this warning.
> 
> While the GCHQ proposal doesn’t go into great detail, it seems to follow that any workable proposal will require providers to suppress those warning messages at the target’s device. This means the proposal will also require changes to the client application as well as the server-side infrastructure.


This is a good write up by Matthew Green of some of the problems that are inherent with the Ghost interception methodology proposed by GCHQ (see Cyberweekly #28).

While I read the original article by GCHQ as proposing that we change the debate from "encryption is bad mkay" to "there might be other ways", everybody, including GCHQ, seems have doubled down on the example given in the original article.

I agree with Matthews analysis here, although I think it gets a little polemic towards the end, but I think he misses the point that inevitably there will be some providers who won't implement the required features and then the provider to consumer trust relationship will become important in the same way that VPN's that guarantee not to log tend to advertise and trade on that guarantee.


## [The State of Web Application Vulnerabilities in 2018 | Imperva](https://www.imperva.com/blog/the-state-of-web-application-vulnerabilities-in-2018/)

[https://www.imperva.com/blog/the-state-of-web-application-vulnerabilities-in-2018/](https://www.imperva.com/blog/the-state-of-web-application-vulnerabilities-in-2018/)

> The first phase in our yearly analysis was to check the amount of vulnerabilities published in 2018 in comparison to previous years. Figure 1 shows the number of vulnerabilities on a monthly basis over the last three years. We can see that the overall number of new vulnerabilities in 2018 (17,142) increased by 21% compared to 2017 (14,082) and by 159% compared to 2016 (6,615). According to our data, more than half of web application vulnerabilities (54%) have a public exploit available to hackers. In addition, more than a third (38%) of web application vulnerabilities don’t have an available solution, such as a software upgrade workaround or software patch


2018 was quite a year for software vulnerabilities, especially in certain areas (PHP gets a bit of a kicking in this article).

However, I'm not sure that this analysis quite hits the mark for me.  While it's interesting reading, it's lacking the context to truly make the numbers meaningful. While there were more vulnerabilities discovered and tracked by CVD than in previous years, we don't know if the CVSS scores were similar.  Equally, it's difficult to tell what that actually means, were more vulnerabilities actually exploited, or as in previous years, were the majority of exploits still focused on the top 10, including several years old vulnerabilities in IE and Flash that make up the majority of successful exploits?

As a general theme for the year however, this suggests to me that we are finding increasing numbers of vulnerabilities, probably through a combination of more eyes, more security researchers looking at our software, and of course the ever increasing amount of software being written.



## [Exclusive: How a Russian firm helped catch an alleged NSA data thief - POLITICO](https://www.politico.com/story/2019/01/09/russia-kaspersky-lab-nsa-cybersecurity-1089131)

[https://www.politico.com/story/2019/01/09/russia-kaspersky-lab-nsa-cybersecurity-1089131](https://www.politico.com/story/2019/01/09/russia-kaspersky-lab-nsa-cybersecurity-1089131)

> role in exposing Martin is a remarkable twist in an increasingly bizarre case that is believed to be the largest breach of classified material in U.S. history.
> 
> It indicates that the government’s own internal monitoring systems and investigators had little to do with catching Martin, who prosecutors say took home an estimated 50 terabytes of data from the NSA and other government offices over a two-decade period, including some of the NSA’s most sophisticated and sensitive hacking tools.
> 
> The revelation also introduces an ironic turn in the negative narrative the U.S. government has woven about the Russian company in recent years.


Yet another reminder that just because someone works for an intelligence agency doesn't actually mean that they are intelligent or know anything about security necessarily.

In this case, if you decide to use a pseudonym to leak national security impacting secrets, a tip is to not use the same username you've used elsewhere, especially if it's connecting to your photo and location.


## [Finland’s grand AI experiment – POLITICO](https://www.politico.eu/article/finland-one-percent-ai-artificial-intelligence-courses-learning-training/)

[https://www.politico.eu/article/finland-one-percent-ai-artificial-intelligence-courses-learning-training/](https://www.politico.eu/article/finland-one-percent-ai-artificial-intelligence-courses-learning-training/)

> Now, Partanen spends her evenings learning the basics of coding and she is thinking about how to apply artificial intelligence to her job, either to help write up medical summaries or perform orthodontics.
> 
> "I can see it [artificial intelligence] is already here, and it serves us — very much actually," she said, adding that following the latest developments in the field has become a hobby.
> 
> She's one of tens of thousands of non-technology experts who are taking part in a grand experiment aimed at repurposing the country's economy toward high-end applications of artificial intelligence. The idea has a simple, Nordic ring to it: Start by teaching 1 percent of the country's population, or about 55,000 people, the basic concepts at the root of artificial technology, and gradually build on the number over the next few years.


Now this is an interesting idea.  The economic pitch on this aside, there is a value in having an educated citizenry when it comes to new technology so that politicians and technology companies cannot get away with hiding behind magic words.

If we had taught 1% of UK citizens about the reality of blockchain, would it be possible for politicians to go on the Today program and suggest that we could solve the Northern Ireland border problem during EUExit with "blockchain"?  I don't think so because with a greater preponderance of people who understand the technology, the ability to detect bluffing and magical thinking is higher, and 1% is probably enough infect a sufficient number of social circles that everyone knows someone to debunk it.

I also wonder if this would affect not just the level of national discourse, but if we could work out what technologies are important, then teaching them to civil servants, policy advisors, think tanks and many other major decision makers who still remain fundamentally technologically incompetent might change the way we make decisions and recommendations as a country.


## [A response to "Who are we at Cyberwar with?" - Son Of Sun Tzu](http://blog.sonofsuntzu.org.uk/post/2019/01/11/Who-are-we-at-Cyberwar-with)

[http://blog.sonofsuntzu.org.uk/post/2019/01/11/Who-are-we-at-Cyberwar-with](http://blog.sonofsuntzu.org.uk/post/2019/01/11/Who-are-we-at-Cyberwar-with)

> I think examining these analogies and references to other areas are useful, both in what they illuminate and when the analogy breaks because it has been stretched too far. Some of what cyber security is conflict, some of the methods cyber security needs are well-established within safety engineering, but simply advocating one approach or the other is too simplistic for our inordinately complex field, and while the appeal to a safety engineering mindset is far more useful than the "OORAH!" of a particularly distorted view of armed conflict, I think some combination of the two is the way forward.
> 
> As to the best analogy for computer security as a whole, I think Wendy Nather summarises the situation well, as she often does, in that crime is a "fine analogy", https://twitter.com/wendynather/status/1076847905208700928. Crime is a vague concept, with a wide scale of events covered, from petty fraud to mass murder - we should appreciate that cyber security is similarly broad, and learn useful lessons from others where we can, but aggressively toss them aside when they do not.


Nick wrote a response to some of my analysis last week and I found myself agreeing with it.  In particular, while I was pushing back against the idea that the field of cybersecurity is warfare, I'm not trying to minimise that there are some advanced adversaries out there who are organised, well trained and and have specific targets in mind.

A friend of mine likened the analogy to physical protection.  Tesco's UK worries about casual theives shoplifting from their stores by using security guards, and they worry about more organised groups attempting to steal the cash by using safes and limited cash floats and so forth.  Technically they should worry about intercontinental balistic missiles that can destroy the store, but in reality, there is little they can do against it, and investing in defenses is not worth it.  In cyber security we have a tendancy thanks to marketing to worry primarily about the top end, about the advanced cyber adversaries before we worry about putting in security guards and safes.  My argument is that we should be doing the basics right before we get too het up about intelligent capable adversaries.  

However, Nick has a point, which is that the gap between basic cyber attack and advanced cyber attack doesn't feel very high at the moment.  Groups like MageCart are able to carry out quite advanced attacks, ones that we might have purported to be nationstate a few years ago, while seemingly being a small set of criminal gangs with limited resources and capability.


