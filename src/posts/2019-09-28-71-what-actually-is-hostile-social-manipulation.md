---
title: "71 - What actually is hostile social manipulation?"
date: 2019-09-28
description: "As we come into some turbulent years for democracies in the west, I think we are going to hear a lot more about hostile social manipulation in various forms.  Of course we are already used to cries of “fake news” from certain sides anyways, but it’s hard to know what is meant when people talk about it."
permalink: /what-actually-is-hostile-social-manipulation/
---

As we come into some turbulent years for democracies in the west, I think we are going to hear a lot more about hostile social manipulation in various forms.  Of course we are already used to cries of “fake news” from certain sides anyways, but it’s hard to know what is meant when people talk about it.

[Betteridges law](https://en.m.wikipedia.org/wiki/Betteridge%27s_law_of_headlines) states that any newspaper headline that ends with a question mark can be answered “No”, for example “Is this the face of Britains youth?”, “Does this map provide the key to peace?” and so on.  The key here is that we are talking about click bait headlines that are essentially untrue, but designed to hook you in and make you read further.  This gets worse online, culminating in the late 2000’s with the Buzzfeed famous “Listicles” such as “23 ways to get rich” or “13 things rich people do, you won’t believe number 5”.

Additionally, we’ve got biased newspapers and online publications, who take facts and twist them to their own ends.  As [Ad Fontes Media’s chart of biases](https://www.adfontesmedia.com/) shows, media outlets have biases, and those on the far right and the far left have a tendancy to be less truthful, and build stories that twist the facts to cover the narrative that they care about.  This has always happened, but the internet has made it easier for niche extreme views to get more traction and more readers than ever before.  Additionally, it’s difficult for most people to know the biases and be able to tell the biases apart, and so they treat all news as truthful or false.

But none of that counts as hostile social manipulation, that requires nation state level interference normally, and an endgoal in mind.  As I’ve said before, the end goal of different nations is different and as such we aren’t going to be able to take the activities of Russia’s Internet Research Agency and apply them to how Catalan rebels operation, or the Chinese media disinformation campaigns are operating.  Any attempt to claim that we can detect that level of interference and re-apply it is bound to fail.

There are similarities, but the actual tactics and strategy changes from country to country and from campaign to campaign.  We need to be careful that we are not fighting the last war, when our adversaries have moved on to new ways and means.

## [Serverless: 15% slower and 8x more expensive](https://einaregilsson.com/serverless-15-percent-slower-and-eight-times-more-expensive/)

[https://einaregilsson.com/serverless-15-percent-slower-and-eight-times-more-expensive/](https://einaregilsson.com/serverless-15-percent-slower-and-eight-times-more-expensive/)

> I consistently found that the serverless setup was 15% slower. (Also, if you think it's slow altogether, I am running this from Iceland, so there's some latency involved). This was disappointing, but it was still fast enough and I just figured that there was some overhead in running API Gateway in front of our API, it does provide a lot of things, even if we don't use them. So, disappointing but not a dealbreaker!
> 
> Pricing
> To be honest I hadn't thought at all about the pricing beforehand. I just figured "Pay for what you use" sounded like it would be cheaper than paying for instances that are on 24/7. So I let the new serverless setup run for a couple of days and then started checking my bills. Whoops! The Lambda+API Gateway bill was already over a hundred dollars! I first started messing with the Lambda setup, giving the lambda functions less memory to decrease the bill, but when I really looked at what was happening it was obvious that it was API Gateway that was the main problem.


This is an interesting read of someone who has tried to port a perfectly normal application to serverless.  I think the (top response on Hacker News)[https://news.ycombinator.com/item?id=21046547] says exactly what my thoughts were:

> PSA: porting an existing application one-to-one to serverless almost never goes as expected.

Serverless is a totally different way of thinking, and attempting to port your old microservices/REST architecture to it probably won't give you the same results that you are expecting.  Actually understanding serverless is important to get the best out of it.  

But, that's not to criticise, the only way to learn stuff like this is to get it wrong first, and somebody who tried and documented their learning helps us all.


## [Getting RSA 256 Bits Wrong - Phill Hallam-Baker - Medium](https://medium.com/@hallam/getting-rsa-256-bits-wrong-4a9339f2f178)

[https://medium.com/@hallam/getting-rsa-256-bits-wrong-4a9339f2f178](https://medium.com/@hallam/getting-rsa-256-bits-wrong-4a9339f2f178)

> The Crown Sterling attack was laughed at because the attack they demonstrated was against a system roughly thirty million billion times easier than the real thing. And that number isn’t an exaggeration, its the value of 2⁵⁵.


I've been mostly avoiding the (Crown Sterling debacle)[https://www.schneier.com/blog/archives/2019/09/the_doghouse_cr_1.html] because some vendor selling snakeoil at Blackhat with their "TIME AI" was just not worth the effort to read and understand.  And more importantly, because I know enough about cryptography to know exactly how little I know.  While sensible people I trust had called it snakeoil, I can't tell an NP problem from an NP complete problem, so this might be the genius breakthrough that we've all been waiting for.

But I know enough about RSA to know that RSA key lengths in bits is not the same as the number in the title, and that this video was a terrible bit of marketing.  

What I'm curious about is, are they genuinely clueless or are they malicious?


## [UPSynergy: Chinese-American Spy vs. Spy Story - Check Point Research](https://research.checkpoint.com/UPSynergy/)

[https://research.checkpoint.com/UPSynergy/](https://research.checkpoint.com/UPSynergy/)

> * The group’s exploitation tool named Bemstour makes use of a variant of a single Equation group exploit. Our research shows that the particular equivalent to this exploit is EternalRomance. APT3 developed their own implementation, possibly based on their analysis and understanding of EternalRomance’s leveraged vulnerability.
> * The group attempted to develop the exploit in a way that allowed it to target more Windows versions, similar to what was done in a parallel Equation group exploit named EternalSynergy. This required looking for an additional 0-day that provided them with a kernel information leak. All of this activity suggests that the group was not exposed to an actual NSA exploitation tool, as they would then not need to create another 0-day exploit. We decided to name APT3’s bundle of exploits UPSynergy, since, much like in the case of Equation group, it combines 2 different exploits to expand the support to newer operating systems.
> * The underlying SMB packets used throughout the tool execution were crafted manually by the developers, rather than generated using a third party library. As a lot of these packets were assigned with hardcoded and seemingly arbitrary data, as well as the existence of other unique hardcoded SMB artifacts, we can assume that the developers were trying to recreate the exploit based on previously recorded traffic.


This is an interesting breakdown.  It basicly looks like China was aware that the NSA was targeting *something* using some of their more advanced tools, or there was enough forensic data left after an exploit that they were able to get raw packet captures of the EternalBlue exploit happening.  This indicates that they were able to see that stuff, and reverse engineer a similar exploit chain, adding in their own engineering efforts.

The danger of "cyberweapons" is that people can analyse the bullets and produce their own.  In this case it was an advanced actor, but actually, fairly low capability actors could do the same thing and generate more advanced weapons than you'd give them credit for.


## [BotSlayer tool can detect coordinated disinformation campaigns in real time - Help Net Security](https://www.helpnetsecurity.com/2019/09/17/detect-coordinated-disinformation-campaigns/)

[https://www.helpnetsecurity.com/2019/09/17/detect-coordinated-disinformation-campaigns/](https://www.helpnetsecurity.com/2019/09/17/detect-coordinated-disinformation-campaigns/)

> BotSlayer, which combines technology from Hoaxy and Botometer, was created in part based on feedback from political and news organizations asking to make the observatory’s tools faster, more powerful and more user-friendly. These organizations include The Associated Press, The New York Times and CNN.
> 
> The system uses an “anomaly detection algorithm” to quickly report trending activity whose sudden surge is likely driven by bots, Menczer said.
> 
> For example, BotSlayer could be used during a presidential debate to not only instantly detect when a candidate’s username or related hashtags are trending, but also automatically assign a “bot score” to indicate whether the surge appears related to bot activity.


This is a neat tool for looking for coordinated action from bot like accounts. 
The open source version uses some very simple heuristics, like age of account, but it can be hooked up to any analytical engine. 

For people looking at combating disinformation, they could do worse than starting here. 


## [AT&T redirected pen-test payloads to the FBI's Tips portal | ZDNet](https://www.zdnet.com/article/at-t-redirected-pen-test-payloads-to-the-fbis-tips-portal/)

[https://www.zdnet.com/article/at-t-redirected-pen-test-payloads-to-the-fbis-tips-portal/](https://www.zdnet.com/article/at-t-redirected-pen-test-payloads-to-the-fbis-tips-portal/)

> Security researchers like Nux carry out these penetration tests because companies like AT&T have bug bounty programs through which they invite this type of traffic being aimed at their applications.
> 
> The FBI does not have a bug bounty program, nor does it invite such pen-tests.
> 
> By redirecting the penetration test to the FBI's Tips portal, AT&T had effectively put researchers in a position where they'd be launching uninvited penetration tests at a US government's website.


I’m not convinced that I entirely disapprove of this as a defensive mechanism.  

If you are a professional pen tester you should be using tools or systems that prevent you going out of scope.  A 302 redirect to a web system that is out of scope should not result in the tool continuing to attack  the new target host.

However if you are a script kiddy, or other attacker, following the redirect to another host is a perfectly legitimate attack, and therefore sending them to an FBI server as a honeypot isn’t a terrible idea.  

It would be better to send traffic to a honeypot server that is expecting it, so you can gather information, but I think the issue here is the blurry line between professional pen testing tools (which should all support scope) and exploitative hacker tools and the lack of professionalism in security researchers.


## [North Carolina police take down Lyft with Austin passenger inside | KXAN.com](https://www.kxan.com/news/man-wanted-in-drive-by-picks-up-lyft-customer-right-before-police-takedown/amp/?__twitter_impression=true)

[https://www.kxan.com/news/man-wanted-in-drive-by-picks-up-lyft-customer-right-before-police-takedown/amp/?__twitter_impression=true](https://www.kxan.com/news/man-wanted-in-drive-by-picks-up-lyft-customer-right-before-police-takedown/amp/?__twitter_impression=true)

> What I’ve learned from Lyft and law enforcement in the ensuing days is that there is no coordinated cooperation over potentially dangerous vehicles. Lyft performs driver background checks but that’s where it stops unless police notify them. That’s according to a Lyft safety employee who spoke to me the day after the shooting.
> 
> Police say there is no database and currently no standardized process for law enforcement to make ridehailing companies aware when a BOLO has been issued for a vehicle. That information is for law enforcement, not for ridehailing companies, they told me.
> 
> And there’s no standardized way for police to tell whether a car they are pursuing is currently in the process of completing a ridehailing trip with a rider like me on board. There’s no database of vehicle license plates or drivers. And unlike taxis, there’s no obvious signage on the cars unless drivers choose to add it. My driver did not.


This is a surprising lack of integration from Lyft and other ride hailing companies to the police.  Why can’t the police who issue a BOLO, send it to taxi companies, ride sharing and autonomous vehicle operators and see if it has been seen or operated by anyone.  Ride sharing companies even insist that the drivers phones provide constant GPS updates, so the police could literally track such a vehicle.

There are a lot of privacy implications for sure, what if they put in the wrong registration number?  What if it’s used by someone to track down their ex?  But the existing police systems are supposed to have checks and audit controls for this sort of thing.


## [The American Brain — Wait But Why](https://waitbutwhy.com/2019/09/american-brain.html)

[https://waitbutwhy.com/2019/09/american-brain.html](https://waitbutwhy.com/2019/09/american-brain.html)

> we’re a species that isn’t great at truth. We’re built to believe convenient delusions, not to be accurate. Given this fact about us, the MPI isn’t just a way for a large group of people to work together to find truth, it’s the only way for them to do it. As author Jonathan Rauch points out, when someone like Einstein declares his theory of general relativity, there literally is no way to tell if he’s a genius or a madman until the “global network of checkers,” as Rauch puts it, attacks the theory from all angles, looking for holes, and continually fails.


This is a long read, and by long, I mean, to read the entire series is probably going to take you a few hours.  But it’s worth it when we start thinking about disinformation.  The authors general thesis is that human life forms operate at a level of groups and nations in similar ways to human bodies are made of cells.  And that while individual humans defeat one another with physical violence, groups and nations defeat each other with both military might, but also now with ideas.

There’s a lot of interesting ideas in here that gives us a good construct with which to understand or analyse how media manipulation can affect the presentation of acceptable ideas in society, and how it can change the perceived consensus on issues.


## [Hostile Social Manipulation: Present Realities and Emerging Trends | RAND](https://www.rand.org/pubs/research_reports/RR2713.html)

[https://www.rand.org/pubs/research_reports/RR2713.html](https://www.rand.org/pubs/research_reports/RR2713.html)

> Today's practitioners of what this report's authors term hostile social manipulation employ targeted social media campaigns, sophisticated forgeries, cyberbullying and harassment of individuals, distribution of rumors and conspiracy theories, and other tools and approaches to cause damage to the target state. These emerging tools and techniques represent a potentially significant threat to U.S. and allied national interests. This report represents an effort to better define and understand the challenge by focusing on the activities of the two leading authors of such techniques — Russia and China. The authors conduct a detailed assessment of available evidence of Russian and Chinese social manipulation efforts, the doctrines and strategies behind such efforts, and evidence of their potential effectiveness.


This is a 300 page report and not everybody needs to read it all (I haven’t managed to read through all of the detail yet), but the introduction and definitions section is worth reading for anybody worrying about or thinking about disinformation.  I really like that they categorise propaganda as being essentially truthful media manipulation that might use falsehoods occasionally, whereas disinformation is essentially false media manipulation that might use truths occasionally. 

They come to a definition of hostile social manipulation that I think works effectively, 
> Hostile social manipulation is the purposeful, systematic genera- tion and dissemination of information to produce harmful social, political, and economic outcomes in a target area by affecting beliefs, attitudes, and behavior.

There are a number of tables and interesting definitions in here, such as how disinformation applies in different media types, and an understanding of the goals of social manipulation campaigns.


