---
title: "161 - How to make a difference"
date: 2021-08-08
description: "It's really easy to criticise, in fact I do it on a weekly basis, but it's much harder to create."
permalink: /how-to-make-a-difference/
---

It's really easy to criticise, in fact I do it on a weekly basis, but it's much harder to create.

Reading the Committee on homeland security and governmental affairs report, I was struck that the report catalogs a thoroughly predictable set of failures in federal IT, and provides a number of recommendations that don't actually feel like they would solve the failures.  It's not that the recommendations are bad, but that it's really hard to constructively provide solutions.  It's far easier to throw your hands up and say things are terrible.

This feels like it hits home a little too closely for comfort for me.  I've spent the last decade or so in the role of technical architect, digital transformer (which sounds like I'm a robot), and security consultant mostly coming into predictably bad systems and organisations, and pointing out where things went wrong.  But actively fixing those things takes a lot more work, and often it's easy to argue that the organisation or context would need to be different before you can actually fix the thing.  

Joel and I have been discussing this at length a lot over the last few months, and trying to work out why giving workable advice is so hard.  In my experience, it's the context that makes it so hard.  We want to say simple things like "use three random words for passwords" and are met with a whole set of "well actually, in this particular situation, that doesn't work".  Advice cannot ever truly be separated from the context, otherwise the advice just reverts back to "it depends".

We decided that one way to try to improve this was to take a common problem that Joel and I know a fair amount about, the protection of data on your smartphone.  We've read the detailed reports into Pegasus, we've both been involved in delivering mobile device management, BOYD programmes and enterprise IT systems, so we think we know what the right answers are.  But we knew that writing it would be hard, how do we say "Using a VPN is easy, but picking one is hard, and if you are just a normal joe, it's probably not protecting you?".  We decided that we would write our guidance based on a number of incremental profiles, facing the typical challenges faced by users.  We separated out casual users from investigative journalists and people who travel from work, and then gave more contextual advice for each user.

We've tried to articulate the principles and reasons behind our advice, so that readers can take it, and modify it, adapt it and use it locally understanding why we make some recommendations or others.

The way that we can make a difference is to do the hard work to not just point out the problems, but to provide solutions, or at least attempts at solutions.  We might be wrong about sections of our advice, but by putting that advice out there, get it out in the open, we can make things better.


## [How to keep your smartphone safe from spying | by Joel Samuel | Aug, 2021 | Medium](https://joelgsamuel.medium.com/how-to-keep-your-smartphone-safe-from-spying-d7d50fbed817)

[https://joelgsamuel.medium.com/how-to-keep-your-smartphone-safe-from-spying-d7d50fbed817](https://joelgsamuel.medium.com/how-to-keep-your-smartphone-safe-from-spying-d7d50fbed817)

> This post discusses four personas, the technical threats to them and their information via their smartphone, and some theory on how to defend against an increasingly capable and focused threat actors.
> 
> If you find yourself matching one of these personas, following the recommendations below may serve you well if you feel that is proportionate to your individual threat profile.
> 
> If you provide IT or cybersecurity services to other people who may fit these personas, double check that what you offer and how you offer it is proportionate to the threats you’re helping to protect them from. Hopefully you have all of our recommendations covered!
> 
> This is definitely not an exhaustive guide and is developed based on article(s) linked and our combined years working in technology and cyber security.


This is a post from Joel and I that seeks to break down some user personas, and how they use their smart phone, and make some positive suggestions for the things they might want to do to protect themselves


## [Federal Cybersecurity: America's data is _still_ at risk | Committee on Homeland Security and Governmental Affairs - United States Senate](https://drive.google.com/file/d/1K0WXtI7F_MTyK2pvEVPkcZGoDDhAxoa4/view?usp=sharing)

[https://drive.google.com/file/d/1K0WXtI7F_MTyK2pvEVPkcZGoDDhAxoa4/view?usp=sharing](https://drive.google.com/file/d/1K0WXtI7F_MTyK2pvEVPkcZGoDDhAxoa4/view?usp=sharing)

> In 2021, the Committee
> sought to determine if the eight agencies made any advancements in their cybersecurity posture
> over the past two years. Just as before, the Committee reviewed the annual audit findings by the
> eight agencies’ inspectors general for fiscal year 2020. While several of the agencies made
> minimal improvements in one or more areas, inspectors general found essentially the same
> failures as the prior 10 years. Only DHS had an effective cybersecurity program for 2020; every
> other agency failed to implement an effective cybersecurity program.
> 
> [...]
> 
> Two components at the Department of Health and Human Services (HHS) had not fully
> implemented DHS’s flagship cybersecurity programs—a cyber-intrusion detection
> system known as “EINSTEIN” that identifies known threats to the network and has been
> required by law for five years,
> 
> [...]
> 
> DHS’s flagship cybersecurity program for Federal agencies—the National Cybersecurity Protection System (NCPS), operationally known as EINSTEIN— suffers from significant limitations in detecting and preventing intrusions.
> 
> [...]
> 
> NCPS comes with a significant cost. As of 2020, the projected lifecycle cost of NCPS was roughly $6.4 billion. For FY 2021 alone, Congress appropriated $371 million for NCPS.


([Joel](https://twitter.com/joelgsamuel)) There is a lot of dire reading in this report. The US has spent billions across a number of years for the 8 federal organisations (so not even 'all of the US Government') and barely a dent has been made. The document scope includes some classified systems used to process national security data, which raises my eyebrows even further (and they were already quite raised).

My main thoughts are:

* centralised security services only make sense if they are (i) exist at the right time; (ii) are any good; and (ii) organisations are required to use them or the service so good they want to
* account management for departing staff is universally terrible (the report identifies thousands of idle accounts)--this is an obvious automation opportunity
* the report repeatedly talks about poor capabilities (my words) to protect personal information--the US Government has not learnt enough lessons from the [Office of Personnel Management (OPM) data breach](https://en.wikipedia.org/wiki/Office_of_Personnel_Management_data_breach)
* assuming adequately scoped and accurately, the fact the US managed to audit and publish this report is impressive. knowing is still a large percentage of the battle. (If the report is based on self-assertions or survey results, the situation is undoubtedly much much worse in real life because my experience with such health check type self-reports, they are absolutely made up)

[Gizmodo has covered this story](https://gizmodo.com/billions-of-dollars-later-the-u-s-government-remains-1847415536), if you don't feel like reading a 47 page PDF.

(Michael) This is both a shocking report, but also something that I suspect we all would have guessed or known if we had been asked.  Money has been poured into cybersecurity across the federal government, but with very little to show for it.  I'm also fascinated that the Department for Health is criticised for not implementing EINSTEIN while the report also criticises EINSTEIN for not actually being effective.

Of course, this is the job of the Inspectors General, to investigate and determine whether the money is being spent effectively, but I note that the report doesn't really make any useful recommendations.  I note that the recommendations themselves, (develop risk based budgeting, create coordinated accountability, expand shared services like EINSTEIN, update EINSTEIN, create risk based metrics), would not really result in fixing most of the issues raised in the report around shadow IT and lack of visibility into federal IT itself.


## [Responsible Cyber Offense | Lawfare - Perri Adams, Dave Aitel, George Perkovich, JD Work](https://www.lawfareblog.com/responsible-cyber-offense)

[https://www.lawfareblog.com/responsible-cyber-offense](https://www.lawfareblog.com/responsible-cyber-offense)

> The SolarWinds hack initially grabbed headlines because of the sheer number of networks affected, but this belied the fact that the Russian operators had intentionally disabled almost all their backdoors without ever using them—they were carefully targeting a smaller number of networks. The Exchange perpetrators, conversely, had indiscriminately installed backdoors on any vulnerable server they could find on the internet—an order of magnitude more compromises than the Russians achieved—and had left these backdoors wide open with easily guessed, hard-coded passwords. Whereas the former hack was a carefully executed espionage campaign, not unlike those carried out by the U.S., the latter resulted in tens of thousands of networks left to the mercy of a thriving ransomware industry. 
> 
> [...]
> 
> Responsible Offensive Behavior
> 
> The technical operational norms we suggest should address irresponsible actions that cause adverse effects, such as collateral damage. Consideration should also be given to verifiability. One aspect of reckless cyber activity is that it is often noisy, but even more subtly reckless behavior can be identified through proper technical analysis. The ability to document irresponsible behavior lends credibility to norms against it. 
> 
> * Test Tools Before Use
> * Avoid Indiscriminate Targeting
> * Prohibit Targets Throughout the Operational Life Cycle
> * Constrain Automation
> * Prevent Criminal and Third-Party Access to Backdoors
> * Responsible Operational Design, Engineering and Oversight


([Joel](https://twitter.com/joelgsamuel)) The authors cover some good background, including points I have made previously in CyberWeekly that other nation states will not constrain themselves if they don't predict any material response from the US, etc.

I don't agree with all of the points raised but this a healthy public debate of offensive cyber capabilities. Testing tools too broadly can lead to detection or otherwise loss of secrecy (including within an organisation). Prohibiting particular target types could potentially describe to adversaries repercussions they can predict they will not ever endure.

(Michael) This piece picks up a critical point, although the Solarwinds created and used a potential back door in thousands of systems, it appears that this was only used, fairly judiciously, in a small number of cases.  Most companies that discovered the stage 1 implant found that it was the only indicator.  That doesn't belie the huge amount of effort required by those companies to verify and validate that fact, to patch the system and deal with the impact of getting the back door in the first place.


## [Ransomware Gangs and the Name Game Distraction – Krebs on Security](https://krebsonsecurity.com/2021/08/ransomware-gangs-and-the-name-game-distraction/)

[https://krebsonsecurity.com/2021/08/ransomware-gangs-and-the-name-game-distraction/](https://krebsonsecurity.com/2021/08/ransomware-gangs-and-the-name-game-distraction/)

> On June 1, Babuk changed the name of its leaks site to payload[dot]bin, and began leaking victim data. Since then, multiple security experts have spotted what they believe is another version of WastedLocker dressed up as payload.bin-branded ransomware.
> 
> “Looks like EvilCorp is trying to pass off as Babuk this time,” wrote Fabian Wosar, chief technology officer at security firm Emsisoft. “As Babuk releases their PayloadBin leak portal, EvilCorp rebrands WastedLocker once again as PayloadBin in an attempt to trick victims into violating OFAC regulations.”
> 
> Experts are quick to point out that many cybercriminals involved in ransomware activity are affiliates of more than one distinct ransomware-as-a-service operation. In addition, it is common for a large number of affiliates to migrate to competing ransomware groups when their existing sponsor suddenly gets shut down.


A good reminder that when we label cybercrime group something like “REvil”, we’re  actually talking about the combination of the tactics, techniques and procedures (TTP’s).  If a crime group has two different bits of ransomware that it deploys depending on the victim, we might track that as if it’s two different groups.

More relevantly, most crime groups don’t write their own software, they buy it, either as a service, or sometimes with contract programmers, who might go on to sell it to another group later.  

This makes tracking them significantly harder than it might appear


## [Escaping from a truly air gapped network via Apple AWDL | by Mikko Kenttälä | SensorFu | Aug, 2021 | Medium](https://medium.com/sensorfu/escaping-from-a-truly-air-gapped-network-via-apple-awdl-6cf6f9ea3499)

[https://medium.com/sensorfu/escaping-from-a-truly-air-gapped-network-via-apple-awdl-6cf6f9ea3499](https://medium.com/sensorfu/escaping-from-a-truly-air-gapped-network-via-apple-awdl-6cf6f9ea3499)

> Bouncing works like this: Bouncer does not allow communication between Alice and Bob. Alice sends a message to Charlie which is allowed via Bouncer saying (spoofing) that the sender of the message is Bob. When Charlie receives the message he replies to Bob that he is not allowed to communicate with Charlie and includes the original message in that reply. This way Bob receives a message from Alice even though Bouncer tried to deny it.
> 
> Fundamental idea is to cause confusion to target network stack which is used for bouncing and make it do things which are not expected. Confusion can be caused with source IP spoofing combined with ICMP error message and the knowledge of the bounce target IP addresses on all the interfaces.
> 
> Leaker sends the secrets bundled into a package which include spoofed source (src) IPv6 address. Package will be sent to the iPhone with the Mobile cellular IPv6 address which means the package will be handled with different rules in the network stack. Because there is no one listening in Mobile interface UDP port 1337, iPhone will send ICMPv6 error message including secrets towards spoofed source address via Mobile interface (with route) and Receiver will receive the secrets.


Lovely write up of a (now patched) bug in apples local discovery network that allows someone to leak secrets from an airgapped network. 


## [The logic behind three random words - NCSC.GOV.UK](https://www.ncsc.gov.uk/blog-post/the-logic-behind-three-random-words)

[https://www.ncsc.gov.uk/blog-post/the-logic-behind-three-random-words](https://www.ncsc.gov.uk/blog-post/the-logic-behind-three-random-words)

> To make it harder for attackers, we need to increase the diversity of password use. This means reducing the number of passwords that are discoverable by cheap and efficient search algorithms, forcing an attacker to run multiple search algorithms (or use inefficient algorithms) to recover a useful number of passwords.
> 
> Currently, complexity requirements are actively working against password diversity (for all the reasons mentioned above). This has led to convergence in strategies and a reduction in password diversity. To increase diversity, we need to encourage people to use other password construction strategies (such as 'three random words'), that use length rather than character sets to achieve the desired strength. This effectively encourages the adoption of passwords that are currently unused, increasing password diversity in the ecosystem.


This is a good defence of three random words. 
You always get a smart ass who looks at suggestions like this and start talking about [entropy and wordlists](https://news.ycombinator.com/item?id=28097341).

This is almost certainly the same kind of person who looks at the stats in every password dump, sees that the number 1 password is “123456” or “password1!” and declares that “people are stupid”.

While there might be more entropy in the total pool of totally random characters from multiple classes, the reality is that people cannot use and remember words that use that entropy pool.  Encouraging three random words creates a wider pool of passwords and makes them more usable.

But also, encourage your staff to use a password manager, buy them a personal account, and get them MFA devices like Yubikeys.  Three random words is good, but password manager plus MFA is better.


## [Amazon's been hit by the largest GPDR fine to date, but EU data protection authorities get the loudest 'wake-up' call](https://diginomica.com/amazons-been-hit-largest-gpdr-fine-date-eu-data-protection-authorities-get-loudest-wake-call)

[https://diginomica.com/amazons-been-hit-largest-gpdr-fine-date-eu-data-protection-authorities-get-loudest-wake-call](https://diginomica.com/amazons-been-hit-largest-gpdr-fine-date-eu-data-protection-authorities-get-loudest-wake-call)

> Amazon, of course, has every intention of appealing as it further confirmed in prepared media statements:
> 
> `Maintaining the security of our customers’ information and their trust are top priorities. There has been no data breach, and no customer data has been exposed to any third party. These facts are undisputed. We strongly disagree with the CNPD’s ruling, and we intend to appeal. The decision relating to how we show customers relevant advertising relies on subjective and untested interpretations of European privacy law, and the proposed fine is entirely out of proportion with even that interpretation.`
> 
> Wake-up call for data authorities?
> What appears to have happened is that this is the outcome of a complaint made by French privacy group La Quadrature du Net back in 2018. The group, which acts in the interests of Europeans to counter misuses of data by Big Tech, filed a collective complaint  - here - on behalf of 10,000 others.
> 
> The group was more open about the backdrop to date in its own blog posting late last week:
> 
> `The decision, revealed by Bloomberg, suffers from no ambiguity: the targeted ad system that Amazon forces onto us is not based on free consent, which is a violation of the GDPR. As such, the corporation is fined to the tune of €746 million. Amazon’s reaction to this historic sanction is to complain to Bloomberg, pretending to not understanding what is at stake: “There has been no data breach, and no customer data has been exposed to any third party”. Rightly so: it is the system of targeted advertising itself, and not merely occasional security breaches, that our legal action attacked. This historic fine hits straight to the heart of Big Tech’s predatory system, and should be celebrated as such.`


The court case that will come out of this will be a landmark case, assuming that it actually results in a judgement.  Whether we, as digital natives, are able to consent or not to advertising systems run by large tech giants is a fundamental question to the operation of the internet in todays modern age.  Like it or not, the advertising models helps fund the vast majority of the sites we use on a regular basis, and those advertisers want better tracking to understand their customer and provide better ads.

I'll add that seeing adverts that are tailored to you is generally better for you, if you don't care about certain types of product, then seeing adverts for them creates noise and distraction.  On the other hand, it's difficult to determine why an advertiser thinks you are interested in the things that you are, and people are not simple 2 dimensional purchasing machines.  The constant tracking of your journey around the web is generally a bad thing.

Sadly, I suspect that none of this will actually come to court, because rather than risk a negative judgement, it's far more likely that Amazon will settle the case unless they are absolutely sure that they'll get a judgement that backs them up.  


## [Ethical hackers collaborate with Defence to strengthen cyber security | GOV.UK](https://www.gov.uk/government/news/ethical-hackers-collaborate-with-defence-to-strengthen-cyber-security)

[https://www.gov.uk/government/news/ethical-hackers-collaborate-with-defence-to-strengthen-cyber-security](https://www.gov.uk/government/news/ethical-hackers-collaborate-with-defence-to-strengthen-cyber-security)

> Bug Bounty programmes provide safe environments for experts to identify areas where security can be improved. The identification of real vulnerabilities by ethical hackers is rewarded and Defence cyber teams are working with the ethical hacking community whose expertise has been extremely valuable in finding and remediating vulnerabilities - ensuring better security across Defence’s networks and 750,000 devices.


([Joel](https://twitter.com/joelgsamuel)) Great move by the MOD. I wrote the [UK Ministry of Justice's Vulnerability Disclosure Policy](https://mojdigital.blog.gov.uk/vulnerability-disclosure-policy/) many moons ago and at the time it wasn't possible to compensate reporters in pounds sterling.

Paying ethical hackers (outside of formal assurance exercises such as an elective [NCSC CHECK](https://www.ncsc.gov.uk/information/check-penetration-testing) penetration test) is a difficult concept for the public purse and public organisations. They are largely required to explicitly decide to do a finite thing, and pay for that thing, and extract value from said decision and move on. An ongoing open framework which could trigger a number of monetary rewards at any time can be a confusing concept. Now that MOD has been successful in a workable bounty model using public funds, I hope other UK departments can follow suit.


## [🕸️Inside the Ransomware Economy🕸️](https://twitter.com/FabiusMercurius/status/1413601716918910978)

[https://twitter.com/FabiusMercurius/status/1413601716918910978](https://twitter.com/FabiusMercurius/status/1413601716918910978)

> Inside the Ransomware Economy
> 
> Ryuk is the biggest Saas unicorn u've never heard of.
> $150M ARR.
> 3 yrs old.
> 
> Maybe it’s taboo to learn business strategy from a cybergang. But the ransomware industry-- from supply chain operations to market microstructures-- is truly genius.
> 


This is a lovely thread looking at a Ransomware operator from the perspective of the startup investment world. 

How good is RYUK at acquisition, retention and revenue (from the startup metrics for pirates)?  How much would we value them if we were investing?

The answer is that RYUK appears to be a storming startup, worth investing in, but they would likely easily be acquired, out-innovated or shut down by law enforcement making it a risky place to invest your money.


