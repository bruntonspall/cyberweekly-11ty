---
title: "67 - How to compare or weigh risks?"
date: 2019-08-31
description: "Some of you will be aware that I have a love/hate relationship with risk management techniques.  On one hand I am a firm believer that many organisations focus on entirely the wrong things, on back to back multi-vendor firewalls and sheep-dip antivirus systems for JSON payloads, when those things don't actually ameliorate the risks that the organisations face, they just make busy work."
permalink: /fraud-is-a-real-risk/
---

Some of you will be aware that I have a love/hate relationship with risk management techniques.  On one hand I am a firm believer that many organisations focus on entirely the wrong things, on back to back multi-vendor firewalls and sheep-dip antivirus systems for JSON payloads, when those things don't actually ameliorate the risks that the organisations face, they just make busy work.

On the other hand, there are a set of fairly basic things that you should do in 99% of contexts, because there are a set of general risks to operating an IT estate that people use.  You shouldn't give domain admin credentials to everyone on the network, you shouldn't just allow anyone to access anything at any time, and you shouldn't connect your supercomputer directly to the internet to mine bitcoin.

The problem I have with risk management techniques is that many, even the ones I like, are overbearingly complicated, slow and heavyweight to apply, and rarely make sense outside of the context that they were done.  Traditional well accepted models used in risk management don't make sense in a lot of cases.  Case in point, I was discussing threat actor classifications with someone junior the other day, and they had outlined a set of actor types including hactivist; organised crime; insiders and foreign intelligence.  So far, so normal, they had correctly identified some of the traditional actor groupings.  But when you actually being to look at it, insiders have a variety of motivations and skills.  No two insiders are going to want to do the same thing, in the same way, and even if you can identify classes of insiders you are worried about (rogue sysadmin, bribed case workers etc), you now have a hugely complex set of potential actor types, and it's still unclear how to relate those to the systems you are trying to protect.

More importantly, I've sat through lots of risk identification sessions, looking at what might attack systems, both in traditional methods, using a variety of experimental methods, as well as my prefered attack tree methodology.  I don't think Business Email Compromise fraud has ever come up in any of those risk sessions, because the sessions were driven by technology, or by security process, and rarely rooted in data on real compromises.

I wish there was a better way, but I've not seen anything that works better than "hire smart people and let them do their thing", and sadly that doesn't scale.  As a pragmatist, I tend to hold views quite loosely.  I encourage people to conduct risk assessment sessions, but I don't hold the results up as perfect, and I'm content also applying a baseline of security measures that I don't feel the need to risk assess or determine a business need for.  I spend time trying to cover at least the worst 80%, and that should put us into a far safer place than we were before.

## [Microsoft font gives away forgery in bankruptcy case – Naked Security](https://nakedsecurity.sophos.com/2019/01/17/telltale-font-scuppers-bankruptcy-trust-claim/)

[https://nakedsecurity.sophos.com/2019/01/17/telltale-font-scuppers-bankruptcy-trust-claim/](https://nakedsecurity.sophos.com/2019/01/17/telltale-font-scuppers-bankruptcy-trust-claim/)

> The McGoeys claimed that the two properties were held in trust for their children, offering as evidence documents that they said were created and signed in 1995 and 2004.
> 
> The courts decided that the trusts claimed by the McGoeys were shams, and one of the most convincing pieces of evidence were the fonts used to create them.
> 
> The bankruptcy trustees called in Thomas W Phinney, an expert in design and typography who spent over a decade working for Adobe. Phinney, who describes himself as the Font Detective, noticed that the Ledge Lodge document supposedly written in 1995 used the Cambria font, while the Humber Station document used Calibri.
> 
> Both of these fonts were part of the ClearType font collection developed for Microsoft in 2002, which didn’t become available to the general public until the company used it in Vista and Office 2007 five years later. That made things a bit awkward for the McGoeys.


Fraud is so much fun to spot.  Rarely do we need multiple vendors of firewalls, or talk about AI and Machine Learning.  

But because it's simple and easy to conduct, it means that the people who do it aren't always as sophisticated in their methods as more "cyber-y" criminals are.


## [About Google's Community Guidelines | Google](https://about.google/community-guidelines/)

[https://about.google/community-guidelines/](https://about.google/community-guidelines/)

> While sharing information and ideas with colleagues helps build community, disrupting the workday to have a raging debate over politics or the latest news story does not. *Our primary responsibility is to do the work we’ve each been hired to do, not to spend working time on debates about non-work topics.*
> 
> Avoid conversations that are disruptive to the workplace or otherwise violate Google’s workplace policies. Managers are expected to address discussions that violate those rules.


It looks like the wired article above has meant that Google has updated it's internal community guidelines.  This new guidance (emphasis mine) is I think perfectly reasonable, but goes against the Google ethos, and will probably upset a lot of people working in the organisation.


## [Three Years of Misery Inside Google, the Happiest Company in Tech | WIRED](https://www.wired.com/story/inside-google-three-years-misery-happiest-company-tech/)

[https://www.wired.com/story/inside-google-three-years-misery-happiest-company-tech/](https://www.wired.com/story/inside-google-three-years-misery-happiest-company-tech/)

> They had built a sublime constellation of data centers around the world to power Google's own products like Gmail, a service that, for vast swaths of users, had normalized the idea of surrendering your data to a company's remote servers. But Google's MO was building products that a billion people would use by default—not closing deals, managing contracts, and customizing infrastructure for other companies.
> 
> Amazon had no such compunctions. In 2006 it began marketing a simple but highly effective cloud computing platform to other firms, ultimately offering clients like NASA and Netflix on-demand access to computing power, including storing and processing data. By the time Google finally offered a comparable service called Google Cloud Platform, in 2012, Amazon was already leagues ahead. In April 2015, Bezos revealed that Amazon Web Services had brought in $4.6 billion in revenue the previous year and was on track to out-earn his retail business soon. Google's earnings call was the same day. The company reported that 90 percent of its revenue was still from online advertising.


There's so much in this article that is interesting, and I struggle to use the word "good" to describe the article as it's very disheartening and sad.

This nugget however I think really shows one of the big reasons that Google Cloud Platform is still so far behind Amazon Web Services.  The core motto and learning that Amazon had built under Bezos was that there would be API's for everything, and it would all be easy to draw lines of control around things and understand the clear lines of demarcation.  Google was never focused in that way, instead it used the engineering brilliance of the site reliability process to power thousands of heterogeneous services, but each was able to be mandated to be built in a "Google" way.  

That means that the sales and marketing teams tended to just put GCP out there and assume that customers could use it in the right way.  Amazon in the meantime was radically focused on the customer, on providing services that customers wanted, and on meeting customers.  I joked back 2013 that Google I/O was far more Google O(utput) than Google I(nput), because it was far more about Google telling the developers how to build things as well as Google does, rather than listening to their customers and developer base.

It's always important to listen to your customers and understand what they need


## [US military carried out secret cyberstrike on Iran to prevent it from interfering with shipping, officials say - U.S. - Stripes](https://www.stripes.com/news/us/us-military-carried-out-secret-cyberstrike-on-iran-to-prevent-it-from-interfering-with-shipping-officials-say-1.596335)

[https://www.stripes.com/news/us/us-military-carried-out-secret-cyberstrike-on-iran-to-prevent-it-from-interfering-with-shipping-officials-say-1.596335](https://www.stripes.com/news/us/us-military-carried-out-secret-cyberstrike-on-iran-to-prevent-it-from-interfering-with-shipping-officials-say-1.596335)

> The cyberstrike was designed to be debilitating — Iran is still trying to restore data — but proportionate and not so provocative as to result in escalation, officials said.
> 
> "When you're in this realm there's always the chance for miscalculation," said one official, adding "there were concerns generally about Iranian responses," perhaps against U.S. or Israeli interests. But the feeling was the strike would not lead to a retaliatory spiral, the official said.
> 
> The cyber operation did not target missile and rocket launch systems, as the Washington Post previously reported, said U.S. officials.


Interesting that the US is now briefing about this.  Of course, in information operations, it can be really hard to tell whether there is any truth to this.  Iran is hardly going to come out and say "Yes, our ship database system went down", and nobody involved is going to  confirm what happened.  

It's interesting that the Pentagon is both clearly briefing about the operation, while formally providing a statement that says they don't discuss cyberspace operations, intelligence, or planning".


## [Group sex app leaks locations, pics and personal details. Identifies users in White House and Supreme Court | Pen Test Partners](https://www.pentestpartners.com/security-blog/group-sex-app-leaks-locations-pictures-and-other-personal-details-identifies-users-in-white-house-and-supreme-court/)

[https://www.pentestpartners.com/security-blog/group-sex-app-leaks-locations-pictures-and-other-personal-details-identifies-users-in-white-house-and-supreme-court/](https://www.pentestpartners.com/security-blog/group-sex-app-leaks-locations-pictures-and-other-personal-details-identifies-users-in-white-house-and-supreme-court/)

> Several dating apps including grindr have had user location disclosure issues before, through what is known as ‘trilateration’. This is where one takes advantage of the ‘distance from me’ feature in an app and fools it. By spoofing your GPS position and looking at the distances from the user, we get an exact position.
> 
> But, 3fun is different. It just ‘leaks’ your position to the mobile app. It’s a whole order of magnitude less secure.
> 
> Here’s the data that is sent to the users mobile app from 3fun systems. It’s made in a GET request like this:
> 
> GET /match_users?from=0&latitude=xxxxxx&longitude=+yyyyyy&match_gender=63&match_max_age=61&match_min_age=30&offset=40&search_distance=100 HTTP/1.1
> 
> BUT, that data is only filtered in the mobile app itself, not on the server. It’s just hidden in the mobile app interface if the privacy flag is set. The filtering is client-side, so the API can still be queried for the position data. FFS!
> 
> Then it got really worrying. Private photos are exposed too, even when privacy settings were in place. The URIs are disclosed in API responses


Ignoring the fact that threesomes and groupsex isn't illegal, and for consenting adults is something that they can do no matter where they work (including staff in the whitehouse or number 10), this is some pretty shocking security.

Generally adult websites have led in terms of cybersecurity, because so many hackers in the 90s wanted to get free access to some of those sorts of sites.  Thats where people tried password guessing, bruteforcing, password stuffing and so on, and as such those operators got good at security (or didn't care because they didn't lose anything if their product was shared for free).

Dating applications haven't been as much of a target, and so we've seen a series of poor security decisions from these tools.  As we see more and more other applications, trying to sell themselves to VC firms as the "Foursquare of catfood" or whatever, we'll see more and more systems holding and revealing personal data through poor security practices.


## [Imperva Security Update](https://www.imperva.com/blog/ceoblog/)

[https://www.imperva.com/blog/ceoblog/](https://www.imperva.com/blog/ceoblog/)

> On August 20, 2019, we learned from a third party of a data exposure that impacts a subset of customers of our Cloud WAF product who had accounts through September 15, 2017.
> 
> Elements of our Incapsula customer database through September 15, 2017 were exposed. These included:
> * email addresses
> * hashed and salted passwords
> 
> And for a subset of the Incapsula customers through September 15, 2017:
> * API keys
> * customer-provided SSL certificates


(Joel) Several thoughts come to mind but I'll pick up on two that actually have very little to do with this breach:

1. Time to detect
I'll spin this as a positive that Imperva had the log data (etc) required to detect events from two years ago. Many organisations would struggle with investigating an incident from last week.

2. Automated certificates are best
[Extended Validation certificates are dead](https://www.troyhunt.com/extended-validation-certificates-are-dead/) so there is no reason Imperva (and companies like it) can't be trusted to generate certificates when they already handle your data.

[Automated certificate renewal](https://ministryofjustice.github.io/security-guidance/guides/automated-certificate-renewal/) is important and in this scenario would in theory shorten the consequence of the private key breach as it would live for shorter period of time and ease the mop up as Imperva could simply automatically request a new certificate without customer intervention.


## [The IKEA Effect: Why We Cherish Things We Build | Psychology Today UK](https://www.psychologytoday.com/gb/blog/make-your-mind/201209/the-ikea-effect-why-we-cherish-things-we-build)

[https://www.psychologytoday.com/gb/blog/make-your-mind/201209/the-ikea-effect-why-we-cherish-things-we-build](https://www.psychologytoday.com/gb/blog/make-your-mind/201209/the-ikea-effect-why-we-cherish-things-we-build)

> The act of building something, putting your own blood and sweat (and if we’re being honest, plenty of frustrated swearing) into a physical object, seems to imbue it with additional value above and beyond its inherent quality, which the researchers dub the “IKEA effect.” For instance, in one study, participants who built a simple IKEA storage box themselves were willing to pay much more for the box than a group of participants who merely inspected a fully built box. Participants in another study who constructed their own origami frogs and cranes valued them roughly five times as much as another group of participants thought they were worth. The increased value is not just about effort, but about completion, as built-then-disassembled and incomplete projects received no such benefit.


(This was supposed to be included last week, but a slip of the finger means it didn't get added.  Useful read anyway)

The ikea effect is strong and valuable for managers to understand.  Did you simply outsource a project or capability somewhere?  Your team and organisation won't value it anywhere nearly as much as if they were involved in creating it.

When combined with Conways Law, that product design will mirror your organisation design, it's worth remembering that unless a team specifically works together, they will view other teams in the same organisation as outsiders, and will therefore value their work less.  

This is why multidisciplinary teams are so important, and why I am strongly against considering technology and "the business" to be seperate things.  The old XP (eXtreme Programming) technique of onsite customer is there to ensure that the customer feels like they were part of building the service or product as well, and therefore value it


## [Project Zero: Implant Teardown](https://googleprojectzero.blogspot.com/2019/08/implant-teardown.html)

[https://googleprojectzero.blogspot.com/2019/08/implant-teardown.html](https://googleprojectzero.blogspot.com/2019/08/implant-teardown.html)

> The implant is primarily focused on stealing files and uploading live location data. The implant requests commands from a command and control server every 60 seconds.
> 
> Before diving into the code let's take a look at some sample data from a test phone running the implant and communicating with a custom command and control server I developed. To be clear, I created this test specifically for the purposes of demonstrating what the implant enabled the attacker to do and the screenshots are from my device.  The device here is an iPhone 8 running iOS 12.
> 
> The implant has access to all the database files (on the victim’s phone) used by popular end-to-end encryption apps like Whatsapp, Telegram and iMessage. 


This is a scary report.  You can read the [top level report](https://googleprojectzero.blogspot.com/2019/08/a-very-deep-dive-into-ios-exploit.html) which explains in more detail that Google found some untargeted waterhole attacks that had likely been going on for around 2 years.

What's critical to understand is that if you browse to this website using Safari or Chrome mobile (or any other iOS browser I believe), the javascript on the page would have executed an exploit and the malware would have been implanted on your phone.

The bit I've quoted here is to remind you that your device is now the weakpoint in most encryption controls.   I've seen lots of time spent worrying about encrypting data in transit, to prevent a network level attacker from overhearing it essentially.  But even with modern end-to-end encryption, the data is absolutely required to be unencrypted on the device, otherwise the user couldn't make use of it.  This makes our devices an increasingly large target.


## [Ukrainian Nuke Plant Workers Tried to Mine Cryptocurrency - Infosecurity Magazine](https://www.infosecurity-magazine.com/news/ukrainian-nuke-plant-workers-mine/)

[https://www.infosecurity-magazine.com/news/ukrainian-nuke-plant-workers-mine/](https://www.infosecurity-magazine.com/news/ukrainian-nuke-plant-workers-mine/)

> Ukrainian security service (SBU) agents have arrested several nuclear power plant employees in the country after they misguidedly tried to use their facility’s IT systems to mine for cryptocurrency.
> 
> Local media reports this week said the incident occurred on July 10 at the plant in Yuzhnoukrainsk in the south of the country.
> 
> The workers are said to have hooked up a supercomputer, which was kept air-gapped at the power plant, to the internet. In so doing, it’s claimed they unwittingly disclosed information on the physical security measures in place at the nuclear facility, which is a state secret.
> 
> The SBU officers seized unauthorized computer equipment which had been used to build a separate LAN designed to mine for cryptocurrency.
> 
> They reportedly took six Radeon RX 470 video cards, extension cords and cabling, various switches, a motherboard, a USB flash drive, a hard drive and even the metal frame on which was mounted the other items.


The security architect almost certainly built a system that was airgapped, and documented it as so.  When everybody built anything else, when thinking about security the "but it's airgapped, so it doesnt matter" will have been uttered.

This is truly terrifying, and why you should still build assuming that your system is compromised.  I'm not entirely convinced that airgap are a good control anyway (I've yet to see an airgapped system that isn't connected to something connected to the internet, even if it's just for time servers or updates), but you definitely shouldn't rely on it.


## [AIG cyber claims statistics report - 2018](https://www.aig.co.uk/insights/claims-intelligence-cyber-report-2019)

[https://www.aig.co.uk/insights/claims-intelligence-cyber-report-2019](https://www.aig.co.uk/insights/claims-intelligence-cyber-report-2019)

> Nearly a quarter of reported incidents in 2018 were due to business email compromise (BEC), up significantly from 11% in 2017. Ransomware, data breach by hackers and data breach due to employee negligence were the other main breach types in 2018.
> 
> BEC has entered the report this year under a new category given the high number of BEC-related claims received by AIG over the past 12 months.


(Jon) This is an interesting report, based on an analysis of over a thousand claims made by customers of AIG against their cyber insurance policies. There are lots of caveats - as ever - to be aware of when inferring things from these claims, and AIG flag a lot of them in their own narrative - namely, it's unlikely to be a representative data sample of wider sectors; that there's no neat distinction between some categories; some claimants may have been able to claim on other policies (e.g. BEC can potentially be claimed as fraud, depending on how you think about it). 

All this said, it is really positive to see a cyber insurer using the data they've got access to to help inform others about the areas of risk they're seeing cause harm to their customers. 

(Michael) It's rare to see "cyber people" talk about business email compromise attacks.  Ransomware, malware and nation states are far more exciting to talk about than an email asking someone in accounts to change the bank account to a different number, or reset their password or similar.  But BEC attacks are highly damaging, and incredibly low technology, which makes them easy to pull off.


