---
title: "59 - How confident are you that your defences work?"
date: 2019-07-06
description: "How confident are you in your defences?  You've got firewalls, WAF's and even a segmented network.  Maybe you have to leave your phone outside before go into your office, have badges that need a pin as a second factor and armed guards who watch everyone coming and going?"
permalink: /how-sure-are-you-that-your-defences-work/
---

How confident are you in your defences?  You've got firewalls, WAF's and even a segmented network.  Maybe you have to leave your phone outside before go into your office, have badges that need a pin as a second factor and armed guards who watch everyone coming and going?

Have you checked that your firewalls don't have a simple allow:allow rule deployed at the top of them in order to fix an IT issue years ago?  Are your WAFs actually still in learning mode? Does your segmented network allow devices to attach to whichever segment they want to?  Maybe you've accidentally walked into your secure office with an electronic device, set your badge pin to the same as your bank pin?  I think I've done or witnessed pretty much all of these things at one time or another.

We spend a lot of time thinking about creating and deploying defences, but very little time thinking about how we audit or confirm that they actually work.  We react to security incidents with assuming that people must have been advanced persistent threats to get around all of our defences, without ever ackonwledging that our chosen defences don't work reliably.

If you are investing in a defensive technology, tool or process, maybe take a few minutes to consider the questions of "How can I confirm this is working", "How will I know if this is bypassed?", "Is there any automated audit or control of this that gives me confidence in it?".

We need better feedback mechanisms on our defensive mechanisms that help us know that these tools work and that they do what we expect them to do.

## [Pro-tip and reminder: if someone asks you for a random number between one and ten, respond with "π". https://t.co/DQgxNYSulv](https://torvaney.github.io/projects/human-rng)

[https://torvaney.github.io/projects/human-rng](https://torvaney.github.io/projects/human-rng)

> Imagine you have to generate a uniform random number from 1 to 10. That is, an integer from 1 to 10 inclusive, with an equal chance (10%) of selecting each one. But, let’s say you have to do this without access to coins, computers, radioactive material, or other such access to traditional (pseudo) random number generators. All you have is a room of people.
> 
> For the sake of argument, let’s say this room has a little over 8500 students in it.
> 
> The easy thing to do is to ask someone “Hey, pick a random number from 1 to 10!”. The person replies “7!”. Great! Now you have a number. However, you start to wonder, is the number uniformly random?
> 
> So you decide to ask a few more people. You continue to ask people and count their responses, rounding non-integers and ignoring answers from people who think that 1 to 10 includes 0. Eventually you start to see that the pattern is not flat at all


You'll have to read the article to see the amazing graph.  But long story short, if you ask people to pick a random number, they will over 25% of the time pick 7, and around 2.5% of the time pick 1 or 10.

People really don't do random very well, so asking humans to be sources of randomness (such as creating random passwords) is never going to work very well.


## [Opinion | What if All Your Slack Chats Were Leaked? - The New York Times](https://www.nytimes.com/2019/07/01/opinion/slack-chat-hackers-encryption.html)

[https://www.nytimes.com/2019/07/01/opinion/slack-chat-hackers-encryption.html](https://www.nytimes.com/2019/07/01/opinion/slack-chat-hackers-encryption.html)

> Slack’s business case for keeping your old messages is to have them ready for you just in case you decide to upgrade to the paid product, which has no limit on the number of messages available for you to search and view. But many users — including those most likely to be in the cross-hairs of a law enforcement request or headline-grabbing nation-state hack — are unlikely to ever make that switch.
> 
> Some might argue that Slack is the wrong tool for high-risk activists, who would benefit from strong encryption
>  and the ability to host on their own servers — features that Slack doesn’t provide. But for many people, especially small and under-resourced organizations, self-hosting is not a viable option, and using strong encryption is prohibitively difficult. Slack is convenient, easy to use without extensive technical expertise and already familiar to most.
> 
> As its website cheerily reminds us, Slack is a “collaboration hub for work, no matter what work you do.” Slack is responsible for protecting the privacy and security of all its users, even the ones whose work brings risks that the company didn’t originally anticipate.


I think this is a pretty poor take.  I understand that people like to use slack, and I find Slack's decision to keep all data forever, regardless of your preferences at the free tier to be questionable.  I hate to see security and privacy features as being "paid for" features that encourage you to upgrade.

However, the argument that high risk activists should be able to take their pick of tools, and select a tool on the basis of convenience and ease of use but then complain that it doesn't have sufficient security features of their level of risk is ridiculous.

If you have a high risk, and you want to use other tools, then you need to ensure that they meet your level of risk, or that you engage in some mitigative activities that reduce the risk to you from those suppliers.  It's not ok to transfer your risk to a supplier without warning or agreement  and then hold the supplier responsible for it.


## [Someone Is Spamming and Breaking a Core Component of PGP’s Ecosystem - VICE](https://www.vice.com/en_us/article/8xzj45/someone-is-spamming-and-breaking-a-core-component-of-pgps-ecosystem)

[https://www.vice.com/en_us/article/8xzj45/someone-is-spamming-and-breaking-a-core-component-of-pgps-ecosystem](https://www.vice.com/en_us/article/8xzj45/someone-is-spamming-and-breaking-a-core-component-of-pgps-ecosystem)

> Last week, contributors to the PGP protocol GnuPG noticed that someone was “poisoning” or “flooding” their certificates. In this case, poisoning refers to an attack where someone spams a certificate with a large number of signatures or certifications. This makes it impossible for the the PGP software that people use to verify its authenticity, which can make the software unusable or break. In practice, according to one of the GnuPG developers targeted by this attack, the hackers could make it impossible for people using Linux to download updates, which are verified via PGP.
> 
> In practice, this means users can’t verify the authenticity of packages, and their PGP-friendly mail software, such as Enigmail, may break down, according to Hansen.
> 
> If you think this is bad, consider this: the SKS software was written in an obscure language by a PhD student for his thesis. And because of that, according to Hansen, “there is literally no one in the keyserver community who feels qualified to do a serious overhaul on the codebase.”


This is quite bad.  Certain types of software updates don't require checking or pulling keys from the key servers, but once a bad key is downloaded onto your system, any update to the key server will cause the software to break.

The final statement really makes it all clear though, GnuPG is still a general tire-fire of usability and software development.  Sadly there are no good replacements yet, and every attempt ends up with the same problems as before.  

See also [Why Johny Can't Encrypt, 2005](https://people.eecs.berkeley.edu/~tygar/papers/Why_Johnny_Cant_Encrypt/OReilly.pdf) and [Why Still, Still Can't Encrypt, 2015](https://www.arxiv-vanity.com/papers/1510.08555/)


## [Eurovision cyber attack: How grim video was prevented from broadcasting globally Israel News](https://amp.9news.com.au/article/c61ffcca-e3d5-49f8-b39a-e680da4b77ae?__twitter_impression=true)

[https://amp.9news.com.au/article/c61ffcca-e3d5-49f8-b39a-e680da4b77ae?__twitter_impression=true](https://amp.9news.com.au/article/c61ffcca-e3d5-49f8-b39a-e680da4b77ae?__twitter_impression=true)

> As millions of people around the world tuned into this year’s Eurovision Song Contest final in Tel Aviv, little did they know they were within one second of witnessing a grim cyber attack.
> Foreign hackers infiltrated the system broadcasting the event globally online and tried to insert a disturbing video into the live feed.
> Yigal Unna, Director General of the Israeli National Cyber Directorate, told Nine News the attack was stopped in the nick of time."It was about as close as you can get without it going to air,” he said.
> He described the video as “an ugly one”. Nine News has learned it was terror footage.
> A specialist cybersecurity team was standing guard at the venue that night - taking extra precautions, after an earlier attempt on the Eurovision semi-final was successful.
> [...]
> He said organisers needed to take cybersecurity risks into account when designing events, and a cyber response team should be physically present at the venue to deal with emergencies.


This is a fascinating report, but not much of a surprise.  Quite what one can describe as "terror footage" is a whole can of worms itself, especially compared to broadcast news coverage of warzones, but it would have been highly jolting for people watching the eurovision song contest.

The advice to have a "cyber response team" physically present at a venue is an interesting one, since for almost any event that doesn't have broadcast equipment, the physical presence is probably not terribly useful.  There are certain things you can do while on premise that aren't possible if you are remote, but if the attack is remote and, as in most organisations cases, attacking remote servers hosted in the cloud, then being at an event location with poor connectivity and lots of noise and confusion might make things worse.


## [What Does It Really Cost to Fix a Software Defect? | TechWell](https://www.techwell.com/techwell-insights/2013/10/what-does-it-really-cost-fix-software-defect)

[https://www.techwell.com/techwell-insights/2013/10/what-does-it-really-cost-fix-software-defect](https://www.techwell.com/techwell-insights/2013/10/what-does-it-really-cost-fix-software-defect)

> according to Laurent Bossavit, author of The Leprechauns of Software Engineering, the “underlying evidence justifying Boehm’s curve…just isn’t up to any reasonable standard of ‘research.’” The few studies Boehm did reference were misrepresented, and one study even found a 2:1 ratio in the other direction from that claimed in Boehm’s curve.
> 
> This suggests that the mantra of rising-cost-of-defects may be more prescriptive than empirical or it may suffer under the “tyranny of always.”


This is old, but this myth still permeates software development and more critically, security architecture and risk management teams.  The myth is that it's more expensive to fix bugs/security issues in production than it is earlier on in the software development lifecycle.

Agile people have long argued that this isn't true if you build in cost of change into your lifecycle, but actually the myth isn't even true in traditional waterfall development either.  Most waterfall development teams are perfectly capable of dealing with bugs, misunderstood requirements and poor analysis with small patch changes without having to restart the entire requirements or analysis phase.

Interestingly, the more process and the more strictly you manage the development processes, the more expensive the changes get.  So the reaction by some teams when faced with outages, to put in place more process and more stricture is likely to increase the cost of bugs found later.

If we optimise for ease of change in our development process, as DevOps and Agile tends to, then the cost of finding bugs in production is not an increased cost of work redone, but an opportunity cost of the backlog that isn't done.


## [Stealing Clouds](https://www.reuters.com/investigates/special-report/china-cyber-cloudhopper/)

[https://www.reuters.com/investigates/special-report/china-cyber-cloudhopper/](https://www.reuters.com/investigates/special-report/china-cyber-cloudhopper/)

> The hacking campaign, known as “Cloud Hopper,” was the subject of a U.S. indictment in December that accused two Chinese nationals of identity theft and fraud. Prosecutors described an elaborate operation that victimized multiple Western companies but stopped short of naming them. A Reuters report at the time identified two: Hewlett Packard Enterprise and IBM.
> 
> Yet the campaign ensnared at least six more major technology firms, touching five of the world’s 10 biggest tech service providers.
> 
>  
> Also compromised by Cloud Hopper, Reuters has found: Fujitsu, Tata Consultancy Services, NTT Data, Dimension Data, Computer Sciences Corporation and DXC Technology. HPE spun-off its services arm in a merger with Computer Sciences Corporation in 2017 to create DXC.
> 
> Waves of hacking victims emanate from those six plus HPE and IBM: their clients. Ericsson, which competes with Chinese firms in the strategically critical mobile telecoms business, is one. Others include travel reservation system Sabre, the American leader in managing plane bookings, and the largest shipbuilder for the U.S. Navy, Huntington Ingalls Industries, which builds America’s nuclear submarines at a Virginia shipyard.


I've always thought it was weird that this was called Cloud Hopper.  Most of these companies are not traditional cloud companies, and I've had people "in-the-know" tell me that this attack was proof that "cloud services are not safe", whereas in fact, this is a big list of the more traditional Managed Service Providers.

It's an otherwise great write up of the attack, and the efforts to which the managed service providers attempted to deal with it, without overly "disturbing their customers" or letting them know that their data might be at risk.


## [The Most Expensive Lesson Of My Life: Details of SIM port hack](https://medium.com/coinmonks/the-most-expensive-lesson-of-my-life-details-of-sim-port-hack-35de11517124)

[https://medium.com/coinmonks/the-most-expensive-lesson-of-my-life-details-of-sim-port-hack-35de11517124](https://medium.com/coinmonks/the-most-expensive-lesson-of-my-life-details-of-sim-port-hack-35de11517124)

> A “SIM port attack”, however, is a malicious port performed by an unauthorized source — the attacker. The attacker ports your SIM card to a phone that they control. The attacker then initiates the password reset flow on your email account. A verification code is sent from your email provider to your phone number — which is intercepted by the attacker, as they now control your SIM card.


This timeline shows just how a SimPorting attack unfolds, minute by minute.  What's interesting to me is his breakdown of his perceived threat model, and how, with hindsight, he should have noticed the indicators that something was wrong.

I think he's being overly harsh on himself, he made perfectly reasonable assumptions about the lack of cell service, and I think that mobile carriers really have a responsibility to give people better information that they may have started being the target of a sim porting attack.

One can imagine that if the mobile carrier required a 2FA style authentication with the existing mobile device before initiating the porting of a number, or even just sent notification to the device informing the user that "a request to port your number has been initiated, contact your provider if this was not you" that it would make life a lot harder for sim port attackers.


## [Exclusive: FBI Investigates Leak Of 1,000 Pages Of ‘Top Secret’ Air Force Intelligence](https://www.forbes.com/sites/thomasbrewster/2019/07/02/exclusive-fbi-investigates-leak-of-1000-pages-of-top-secret-air-force-intelligence/#e69133129739)

[https://www.forbes.com/sites/thomasbrewster/2019/07/02/exclusive-fbi-investigates-leak-of-1000-pages-of-top-secret-air-force-intelligence/#e69133129739](https://www.forbes.com/sites/thomasbrewster/2019/07/02/exclusive-fbi-investigates-leak-of-1000-pages-of-top-secret-air-force-intelligence/#e69133129739)

> The files, many of which were marked ‘TOP SECRET,’ were uncovered by the Fairborn City Police Department on May 25, the FBI wrote in its search warrant application. Officers came upon the files as they were investigating an alleged “marijuana growing facility” believed to have been located at the home of the suspect, Izaak Vincent Kemp, according to the warrant. The police did find marijuana, but the case was escalated to the FBI after the discovery of the classified papers, the warrant revealed.
> 
> The documents should have had especially strong safeguards from leaking as they were marked as being protected by “Special Access Programs.” Such files are deemed so sensitive they require additional security beyond what’s normally provided for classified files and should only be stored in segregated, highly protected environments.
> 
> The Air Force said the contractor was never authorized to remove the classified documents from the NASIC “and would have had to make a concerted effort to bypass security checkpoints” when taking them home, the search warrant read. 


This feels like a blinkered attitude of security officials to say "This would have taken a concerted effort to bypass security checkpoints" rather than "Oh dear, it looks like our security checkpoints don't really work".

Undoubtably, this will be spun that the dope growing computer expert was also a security genius and got past the worlds most efficient security controls.


## [Black Team War Stories: Which company are you a contractor with?](https://www.nccgroup.trust/uk/about-us/newsroom-and-events/blogs/2019/july/black-team-war-stories-which-company-are-you-a-contractor-with/)

[https://www.nccgroup.trust/uk/about-us/newsroom-and-events/blogs/2019/july/black-team-war-stories-which-company-are-you-a-contractor-with/](https://www.nccgroup.trust/uk/about-us/newsroom-and-events/blogs/2019/july/black-team-war-stories-which-company-are-you-a-contractor-with/)

> Other items were also taken onto site to fill the tray for the scanner as much as possible - security through obscurity... This was an absolute success. However, one of the items brought in to fill the tray was a packet of cigarettes which turned out to be a contraband item. This triggered a series of questions about the consultant. As these questions became more detailed the guard was left to make his own assumptions. Better this than the consultant readily offering answers that would likely dig the hole deeper. The idea was that the guard would likely offer the answers he was looking for and the consultant could then just agree. One of these questions was, “Which company are you a contractor with?” The consultant happened to be wearing a fleece by a popular outdoor clothing brand, and before they consultant could respond, the guard read the brand name out loud, to which the consultant happily agreed. The outdoor clothing company then became the assumed contracting company…clothing had nothing to do with this site or the business in general and was certainly not a contracting company. Lesson learned? It is a lot easier to let people answer their own questions no matter how crazy the answer may seem, just get out before they realise.


This is a great story about a Black/Red team engagement.  For those of you who haven't heard of them, Black Team engagements are physical and social penetration tests, where the penetration testing team attempts to get physical access to a building and normally back out again with some goal information.

There's a lot to unpick here, but as a reminder, this was a highly secure building with security above and beyond what most of us would expect to see, and still the team was able to get in and out.


