---
title: "77 - Progress marches on even if we aren't ready"
date: 2019-11-09
description: "Security is hard, that's more or less the theme of Cyberweekly every week.  While I get as excited about advances and cool new toys as anyone else (ok, maybe a little more so), one of the problems we have in cybersecurity is the growing legacy of poor decisions and poor technology."
permalink: /progress-marches-on-even-if-we-aren-t-ready/
---

Security is hard, that's more or less the theme of Cyberweekly every week.  While I get as excited about advances and cool new toys as anyone else (ok, maybe a little more so), one of the problems we have in cybersecurity is the growing legacy of poor decisions and poor technology.

I've said before that doing the basics is not easy, but is the most important thing you can do.  That's because so many of the more advanced things depend on the basics being done.  Threat Hunting may be cool and all, but if you don't fetch and store logs, there is nothing for your threat hunters to do.  A next generation SOC sounds amazing, but if you don't even know what your enterprise estate looks like, what servers you've got and no ability to make changes, then it's only just so many blinking lights.

We get very overawed by all of the new exciting things and want to apply them, and in many cases we should be using new and up to date tools.  But we need to ensure that we put in the effort to maintain the basic systems.  The [Red Queen Effect](https://fs.blog/2012/10/the-red-queen-effect/) tells us that everyone has to run just to keep up with their competitors.  As that article goes on to state, and many business guru's have made millions selling books like to say: It's about working smarter not harder. 

I mostly disagree, on the basis that this just changes the race into one of trying to be the one working smarter than all of the others.  The paperless office, video conferencing, telekits and remote presence are all "work smarter" ideas that haven't materially affected how businesses actually operate.  When was the last time you heard of a business trumpting that it beat it's rivals because it had better video conference facilities than it's competitors did.  

What makes successful organisations are not the ones who you see on stage talking about the newest and best things, generally it's the ones that just quietly get one and do the thing, even if it's reasonably basic things that they do.  You won't get plaudits and applause for doing the basics well, but you will free up people to get on with the "smart work" that enables the organisation to be better and deliver better services/products to its users.

## [How Steve Jobs scammed Apple for free lunch with $1 salary - Business Insider](https://www.businessinsider.com/how-steve-jobs-scammed-apple-for-free-lunch-with-1-dollar-salary-2017-6?r=US&IR=T)

[https://www.businessinsider.com/how-steve-jobs-scammed-apple-for-free-lunch-with-1-dollar-salary-2017-6?r=US&IR=T](https://www.businessinsider.com/how-steve-jobs-scammed-apple-for-free-lunch-with-1-dollar-salary-2017-6?r=US&IR=T)

> Apple is well-known in Silicon Valley for making its employees pay for coffee and food from its cafeterias, in contrast with companies like Google that provide meals for free.
> But even though the lunches were inexpensive — about $8, according to Forstall — Jobs, the multibillionaire CEO, still found a way to get around paying for them.


(Jake) With rumours of a 16” MacBook Pro swirling (and then dwindling) it’s easy to have Apple on the mind and I remembered this story in a conversation. It’s easy to have a perfectly designed system, that is simple and clearly works for the majority of cases. From the case of fraud with Amazon recently where an account was breached years ago because MFA wasn’t required for existing devices (I mean I don’t want to enter credentials on 15 devices again within a week, especially when some of them mean using arrow keys to navigate a QWERTY keyboard) to the GitHub OAuth bypass with Rails trying to reduce the amount of work required by tens of thousands of devs (many might not even know about the HEAD verb) by reusing existing codepaths, it’s proof again there’s no such thing as a free lunch—unless you’re like Steve Jobs..


## [Raspberry Pi-Powered AI Beats Human Pilot in Dogfight](https://www.newsweek.com/artificial-intelligence-raspberry-pi-pilot-ai-475291)

[https://www.newsweek.com/artificial-intelligence-raspberry-pi-pilot-ai-475291](https://www.newsweek.com/artificial-intelligence-raspberry-pi-pilot-ai-475291)

> The AI, dubbed ALPHA, went up against retired United States Air Force Colonel Gene Lee in a series of simulated battles, beating Lee in every single engagement.
> 
> Lee described ALPHA as "the most aggressive, responsive, dynamic and credible AI I've seen to date."
> 
> 
> ALPHA has gone on to defeat other expert fighter pilots in what is being hailed as a significant breakthrough in unmanned flight.
> 
> Lee, who has battled AI opponents in simulated environments for more than 30 years, noted that after hours-long sessions with ALPHA, he felt "tired, drained and mentally exhausted," whereas the AI was as sharp as the first battle


This is a fascinating read about the level to which "AI" is going to be used in unmanned vehicles and change the nature of warfare in the future.  I'm not going to say that we are there yet, it's probably years away, but this will create even more of an asymmetry between the "haves" and the "have-nots" at the national level.  As soon as a small nation needs to consider sending its young people to war, in planes where they might die, but where the cost to the enemy of losing a plane is just the loss of the plane and the hardware, then it would be very hard for any nation to support that war.

One might say that this is good from a world stage perspective, but while one could argue that America is a peaceful nation (and one can argue it's not), we've seen how quickly a democratic nation can change, and if the leader decided that going to war and winning a great victory was what would help their internal poll numbers, then how powerful does this technological advantage become?  If that war is guaranteed to not have a human cost, then it will be supported in far greater numbers by the populace.

You can read [the original research in pdf](https://www.longdom.org/open-access/genetic-fuzzy-based-artificial-intelligence-for-unmanned-combat-aerialvehicle-control-in-simulated-air-combat-missions-2167-0374-1000144.pdf).


## [Georgia hit by massive cyber-attack | BBC News](https://www.bbc.co.uk/news/technology-50207192)

[https://www.bbc.co.uk/news/technology-50207192](https://www.bbc.co.uk/news/technology-50207192)

> ...cyber-attack has knocked out more than 2,000 websites - as well as the national TV station - in the country of Georgia.
> 
> Court websites containing case materials and personal data have also been attacked.
> 
> Prof Alan Woodward, cyber-security expert at Surrey University. "With the scale and the nature of the targets, it's difficult not to conclude that this was a state-sponsored attack."


(Joel) The scale in terms of attack and consequence is sizeable. Defacing websites is usually disconnected from preventing a news agency being able to broadcast so begs the question around motives and if (and then why) these systems had comparably weak defences or were inter-connected in some way.

While there are certainly situations where state-sponsored actors are generating/procuring and burning [0days](https://en.wikipedia.org/wiki/Zero-day_(computing)) to achieve goals this may be a case of a relatively sophisticated threat actor using commodity tactics and tooling because the defensive cyber security posture was just that lax.

(Michael) Since we wrote this, it seems like [reports](https://www.forbes.com/sites/daveywinder/2019/10/29/georgia-ill-be-back-cyber-attack-terminates-tv-takes-down-15000-websites/#386392037a48) are suggesting that all of the websites were hosted with the same hosting company, moving this from an "only a state actors can commit this level of disruption" to "supply chains are hard", themes that we cover from week to week here it seems.

Remember that for many intermediate level actors, looking like a state level actor can get them a better response, especially if the aim is to get action at the highest levels.  Attribution is hard.


## [4th November's Landings at LHR](https://tinyletter.com/CloudsAtLHR/letters/4th-november-s-landings-at-lhr)

[https://tinyletter.com/CloudsAtLHR/letters/4th-november-s-landings-at-lhr](https://tinyletter.com/CloudsAtLHR/letters/4th-november-s-landings-at-lhr)

> We’re wrapping up several days worth of updates here. Amazon are really pushing the developer assistance front, with CodeStar helping to generate more production-ready apps, EMR notebooks supporting Git integration, and Amplify making it easier to integrate Authentication, Authorisation, and Accounting inside your Amplify applications. Alongside that there’s updates for the AWS for Wordpress plugin, some IoT updates, Chime, and more. There’s 3 decent blog posts at the bottom of this edition, where we look at the AWS for Wordpress plugin allowing you to add a CloudFront distribution, how it’s now much easier to get started with Lambda applications, and again using Amplify for that AAA integration.
> 
> Grab your coffee/tea/cold-drink/snacks and enjoy!


Landings at LHR is a newsletter that wraps up changes in the AWS product landscape with a particular focus on what's available to UK and Dublin areas that many UK businesses use.

I would love to cover more updates on new features in AWS, but there's so many that I could spend all of my time just doing that.  Luckily Jake does it so I don't have to.  A recommended read and [subscription](https://tinyletter.com/CloudsAtLHR)
(Full Disclosure: He also contributed a link this week, although he didn't know I was going to feature this when he did so)


## [Indian nuclear power plant’s network was hacked, officials confirm | Ars Technica](https://arstechnica.com/information-technology/2019/10/indian-nuclear-power-company-confirms-north-korean-malware-attack/)

[https://arstechnica.com/information-technology/2019/10/indian-nuclear-power-company-confirms-north-korean-malware-attack/](https://arstechnica.com/information-technology/2019/10/indian-nuclear-power-company-confirms-north-korean-malware-attack/)

> In a press release today, [Nuclear Power Corporation of India Limited] Associate Director A. K. Nema stated, "Identification of malware in NPCIL system is correct. The matter was conveyed by CERT-In [India's national computer emergency response team] when it was noticed by them on September 4, 2019."
> That matches the date threat analyst Pukhraj Singh said he reported information on the breach to India's National Cyber Security Coordinator.
> 
> "The matter was immediately investigated by [India Department of Atomic Energy] specialists," Nema stated in the release. "The investigation revealed that the infected PC belonged to a user who was connected to the Internet connected network used for administrative purposes. This is isolated from the critical internal network. The networks are being continuously monitored."


I'm nervous about the term "administrative purposes" here.  While in a good facility, the control network is utterly physically isolated, of course in reality people have the need to move things forwards and backwards, and have processes for "Import/Export".  

Finding malware poking around in nuclear plants is something that should be expected these days.  Malware being discovered before it does harm (particularly like this, when it's reconnaissance malware) is a good thing, not a bad thing.


## [Remember the Uber self-driving car that killed a woman crossing the street? The AI had no clue about jaywalkers • The Register](https://www.theregister.co.uk/2019/11/06/uber_self_driving_car_death/)

[https://www.theregister.co.uk/2019/11/06/uber_self_driving_car_death/](https://www.theregister.co.uk/2019/11/06/uber_self_driving_car_death/)

> The March 2018 accident was the first recorded death by a fully autonomous vehicle. On-board video footage showed the victim, 49-year-old Elaine Herzberg, pushing her bike at night across a road in Tempe, Arizona, moments before she was struck by the AI-powered SUV at 39 MPH.
> 
> Now, an investigation by the NTSB into the crash has pinpointed a likely major contributing factor: the code couldn't recognize her as a pedestrian, because she was not at an obvious designated crossing. Rather than correctly anticipating her movements as a person moving across the road, it ended up running right into her.
> 
> “The system design did not include a consideration for jaywalking pedestrians,” the watchdog stated [PDF] in its write-up. “Instead, the system had initially classified her as an 'other' object which are not assigned goals.”
> 
> The computer-vision systems in self-driving cars are trained to identify things, such as other vehicles, trees, sign posts, bicycles, and so on, and make decisions on what to do next using that information. It appears Uber’s software wasn’t able to identify Herzberg since there was no classification label for a person not using a proper crossing point, and it wasn't able to make the right decisions.


This is a terrible tragedy that hopefully we can learn some things from.

The timeline is interesting because of the confluence of different systems that interact to produce the failure.

The classification system keeps changing it's mind about what she is, is she a vehicle of some form, or an "other", it's unsure.
Meanwhile the path prediction system, being prompted that she's a vehicle, notes that she's moving very very slowly for a vehicle and as such predicts that she's either static, or staying in her lane.
At 1.5 seconds, it seems to have decided that it might hit something slow moving and plans to move around it, but because at that point it currently thinks she's a static object, there's no path prediction for where she might move.
At the next update, the classifier picks her up as a bicycle, that it's going to hit something, and then it triggers a 1 second delay before applying the brakes.

This 1 second delay is a thing that makes sense in the 99% of cases that don't result in accidents.  Given how much the classifiers flip-flop, if everytime it thought there was something ahead it might hit and applied the brakes, the car would constantly stop/start and the ride would be both uncomfortable, people wouldn't buy the car and the system would fail.
This system seems to give the system enough time to be really sure that the situation is as it judged.

That should ahve been the end of it, if the car had engaged the emergency braking, it might have prevented a tragedy, but now another interaction happens.  The system sounds an audible alarm to indicate that there's going to be an accident, and the operator grabs the wheel.  The system assumes that if an operator has hands on the wheel, then they are in control, and disengages all of the autopilot systems, stopping the braking plan.  Of course the human cannot react in under a second (although they come close) and they don't hit the brakes until after collision occurs.

The question we should ask ourselves is not "why did this system fail?" but "why does this system work the rest of the time?".  There's lots of interacting systems, and given the number of miles driven, it works in lots of other cases.

It's super easy to write a headline like "Uber car wasn't programmed to see humans" or talk about the Trolley Problem, but in reality, this is a chaotic mesh of different systems all interacting.  You cannot fit an ethical decision module into it, because at no point was the system in a coherant enough state to actively make that decision.


## [Boeing's poor information security posture threatens passenger safety, national security, researcher says](https://www.csoonline.com/article/3451585/boeings-poor-information-security-posture-threatens-passenger-safety-national-security-researcher-s.html)

[https://www.csoonline.com/article/3451585/boeings-poor-information-security-posture-threatens-passenger-safety-national-security-researcher-s.html](https://www.csoonline.com/article/3451585/boeings-poor-information-security-posture-threatens-passenger-safety-national-security-researcher-s.html)

> Boeing test development networks are publicly exposed to the internet, Kubecka said, and at least one of Boeing's email servers is infected with multiple strains of malware. Kubecka believes that the infected email servers are being used to exfiltrate sensitive intellectual property including code used in both civilian passenger aircraft as well as aircraft Boeing sells to the US military.
> 
> [...]
> 
> "At the time there was no way to get in touch with anyone who understood what I was talking about in a secure manner," Kubecka tells CSO. "I couldn't just send this information in plain text [without using encryption], that would be irresponsible."


(Joel) [This. is. fine.](https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fi0.kym-cdn.com%2Fphotos%2Fimages%2Foriginal%2F001%2F230%2F156%2F005.gif&f=1&nofb=1)

[Chris Kubecka](https://twitter.com/SecEvangelism) highlights various cyber security lapses within Boeing that I summarise as being terrifying and unreasonable in 2019.

The lack of DMARC configuration (helps to stop people spoofing your email domain and sending emails as you) through to publicly accessible unencrypted servers/networks is likely a reflection of the size of Boeing's technology estate, the age of thereof and the 'big organisation' inertia but none of this is an excuse given the sensitivity of the underlying systems and data.

Boeing likely has a limited amount of time to take severe corrective measures before it is seen as negligence (which it might already be) that could lead to a flurry of breaches and regulatory enforcement action.

(Michael) I think this security researcher has an invalid threat model for reporting security research.  I keep meaning to write a blog post about this generally, but in this case, they felt prevented from communicating because they felt that if they sent the information over "plain email" that it would be "irresponsible".  But I'm unsure who they think is tapping that email, what they would do with the information if they got it and how likely that actually is?  Given they have 2 actions, send email and don't send email, and by not sending email, they are ensuring that the organisation cannot fix it's problems.

If you want security researchers to talk to you, you need to provide not just contact details, but what you think are secure channels, and what information is acceptable to send in what form. 


## [Morrisons tells top court it's not liable for staffer who nicked payroll data of 100,000 employees - The Register](https://www.theregister.co.uk/2019/11/07/morrisons_supreme_court_payroll_data_appeal/)

[https://www.theregister.co.uk/2019/11/07/morrisons_supreme_court_payroll_data_appeal/](https://www.theregister.co.uk/2019/11/07/morrisons_supreme_court_payroll_data_appeal/)

> At the heart of the case is a deceptively simple question: was former Morrisons auditor Andrew Skelton acting "in the course of his employment" when he copied nearly 100,000 people's payroll data to a USB stick and dumped it on a hidden Tor site? The supermarket, naturally, argues that he wasn't – and therefore shouldn't be held liable for his actions.


(Joel) This is an interesting argument that I interpret as boiling down to "he may have been an employee using his issued credentials but he wasn't doing his actual job/role when he did that so the employer can't be liable".

(Baring in mind: IANAL - I am not a lawyer) this could set some interesting nuanced precedent but how/when a Data Controller (or Processor, as they are directly liable in some cases) may, may not be, liable for the actions of the people they employ and authorise to process data.

The ICO have used independent assessors to assess whether an organisation applied proportional commitment and investment into cyber security and consider whether they did 'reasonable' things or not as a major factor in administrative action. In this case, we may find that Morrison may have had the right technical controls (role-based access etc) but failed to implement sufficient procedural controls that allowed a single individual to achieve the breach.

Outside of the case at hand we’re back to some fundamental cautions: personal data is toxic and we should be extremely allergic to humans touching production databases (particularly making local copies).


## [Former Twitter employees charged with spying for Saudi Arabia by digging into the accounts of kingdom critics - WaPo](https://www.washingtonpost.com/national-security/former-twitter-employees-charged-with-spying-for-saudi-arabia-by-digging-into-the-accounts-of-kingdom-critics/2019/11/06/2e9593da-00a0-11ea-8bab-0fc209e065a8_story.html)

[https://www.washingtonpost.com/national-security/former-twitter-employees-charged-with-spying-for-saudi-arabia-by-digging-into-the-accounts-of-kingdom-critics/2019/11/06/2e9593da-00a0-11ea-8bab-0fc209e065a8_story.html](https://www.washingtonpost.com/national-security/former-twitter-employees-charged-with-spying-for-saudi-arabia-by-digging-into-the-accounts-of-kingdom-critics/2019/11/06/2e9593da-00a0-11ea-8bab-0fc209e065a8_story.html)

> The [US] Justice Department has charged two former Twitter employees with spying for Saudi Arabia in a case that raises concerns about the ability of Silicon Valley to protect the private information of dissidents and other users from repressive governments.
> 
> The charges, unveiled Wednesday in San Francisco, came a day after the arrest of one of the former Twitter employees, Ahmad Abouammo, a U.S. citizen who is alleged to have spied on the accounts of three users — including one whose posts discussed the inner workings of the Saudi leadership — on behalf of the government in Riyadh.


(Joel) Whether its human analysts working on improving speech recognition improvement (who happen to be able to download/share the clips) from home assistance devices or a SharePoint system administrator on classified networks: the insider threat can be a very real one.

Sadly there isn't enough time, money and people (its a triangle, pick 1.5!) for cyber security in most organisations so those present have to pick their battles, so insider actors gets pushed further down the priority list (even where you may or may not use personnel clearances as _a_ risk management tactic) because you're still fighting shared/leaked credentials, rudimentary OWASP Top 10 application-level problems, and rudimentary patching issues to the point where security logging (just logging, not even monitoring) is so far away in the backlog of things you could do it doesn't even matter anymore because the 15 year old Java app doesn't create any observable data for operational purposes anyway (let alone security ones).

That said (OK, ranted) insider threats vary, there is not a one-size-fits-all approach and ultimately you have to trust someone. To quote [@SwiftOnSecurity](https://twitter.com/SwiftOnSecurity) [who tweeted in response to this news](https://twitter.com/SwiftOnSecurity/status/1192219599581982723?s=20) "The technical controls and visibility I implement as a security engineer... is designed to catch me."

Twitter isn't the first (and won't be the last) social media platform with insider issues. [MySpace](https://www.vice.com/en_us/article/j5w4xx/myspace-employees-spied-on-users-with-internal-tool-overlord), [Facebook](https://www.vice.com/en_us/article/bjp9zv/facebook-employees-look-at-user-data) and [Snapchat](https://www.vice.com/en_us/article/xwnva7/snapchat-employees-abused-data-access-spy-on-users-snaplion) have all been there.


## [Amid NSA warning, attacks on Confluence have risen in recent weeks](https://www.cyberscoop.com/nsa-confluence-vulnerability-warning/)

[https://www.cyberscoop.com/nsa-confluence-vulnerability-warning/](https://www.cyberscoop.com/nsa-confluence-vulnerability-warning/)

> The NSA’s warning on the matter, issued Oct. 30, does not share statistics on exactly when the NSA has seen the vulnerability exploited, how recently it’s been exploited, or the frequency and magnitude of attacks.
> 
> But the updated timeline of attacks shows the NSA’s new Cybersecurity Directorate, stood up just one month ago, to be sharing warnings with the public in an unclassified way of threats it is seeing as they are bubbling up — a process which the NSA is working on improving. Just last month the director of the new cybersecurity division said the process of declassifying threat tips and sharing them quickly with the public is a process that needs to be ironed out more to ensure it is giving timely and relevant information to the private sector on nation-state threats.
> 
> [...]
> 
> When reached for comment, NSA press officer Donna Lohr confirmed the “NSA released this advisory based on an uptick in use of this vulnerability,” and emphasized patching the vulnerability.
> 
> “NSA would like the community to understand that there is always sound reasoning behind the timing of our advisories; they should be viewed as a call to act,” Lohr said.


The confluence bug is a big meh to me.  I really don't think you should be running confluence on premise in most cases (which is what is affected), and if for some weird reason you are, then you should be patching, as this bug was announced back in April.

What's interesting here is both the timeline showing that NSA's Cybersecurity directorate is doing it's thing, and the fact that they basicly said "If we tell you that a vulnerability is out there, there's probably a classified reason for that".  Clearly the NSA have seen this being exploited against the sorts of targets that it normally defends, so defense, aerospace, government that kind of place.  That indicates that maybe an efficient and stealthy APT is using this.

Since they've announced, I've seen reports that there is general scanning for this vulnerability going on, so the cats definitely out of the bag.  Anyway, confluence servers are almost certainly not "critical servers" that cannot be patched, you should be patching these.


## [SANS 2019 Threat Hunting Survey: The Differing Needs of New and Experienced Hunters [pdf]](https://threatconnect.com/wp-content/uploads/Survey_ThreatHunting-2019_ThreatConnect.pdf)

[https://threatconnect.com/wp-content/uploads/Survey_ThreatHunting-2019_ThreatConnect.pdf](https://threatconnect.com/wp-content/uploads/Survey_ThreatHunting-2019_ThreatConnect.pdf)

> Threat hunters leverage tools—and a whole lot of experience—to actively sift through network and endpoint data, always looking for suspicious outliers or traces of an ongoing attack. They consume threat intelligence to understand the tactics, techniques and procedures (TTPs) of attackers better. Most importantly, hunters create a hypothesis on how a potential attack might happen and search for data to prove or reject the hypothesis.
> 
> Is there a difference between threat hunting, incident response (IR) and SOC activities? For some, this might be an easy question to answer; however, for a large segment of respondents, these three areas still blur together. That blurred line is understandable, given that they are all interrelated and necessary. 


Threat Hunting is all the rage, and while your legacy system may not produce useful logs, your team wouldn't know if they were compromised by BlueKeep and you don't have the budget or authority to help the digital team doing whatever it is they are doing on some public cloud away from all of the security sensors, you will be asked by your management team to demonstrate your "Threat Hunting Strategy".

This report covers some of what threat hunters do, and makes clear that threat hunters make use of security logs, operational logs and other data to carry out their task.  Hiring some Threat Hunters when you don't yet have security logs is about as useful as just setting fire to your cash.


## [Proofpoint Q3 2019 Threat Report — Emotet’s return, RATs reign supreme, and more | Proofpoint US](https://www.proofpoint.com/us/threat-insight/post/proofpoint-q3-2019-threat-report-emotets-return-rats-reign-supreme-and-more)

[https://www.proofpoint.com/us/threat-insight/post/proofpoint-q3-2019-threat-report-emotets-return-rats-reign-supreme-and-more](https://www.proofpoint.com/us/threat-insight/post/proofpoint-q3-2019-threat-report-emotets-return-rats-reign-supreme-and-more)

> Assume users will click. Social engineering is increasingly the most popular way to launch email attacks and criminals continue to find new ways to exploit the human factor. Leverage a solution that identifies and quarantines both inbound email threats targeting employees and outbound threats targeting customers before they reach the inbox.
> 
> Deploy robust layered defenses. Threats range from high-volume malware to highly-targeted, low volume business email compromise scams that often have no payload at all and are thus difficult to detect. Network and web-based threats may also affect users, while impostor threats require scalable solutions that defend against a variety of identity deception techniques and should, where possible, include full implementation of DMARC.


Another quarter, another set of threats that haven't changed.  Dodgy emails with malicious links, some small number of malware attachments and the deployment of various remote access trojans.

This advice however is good.  I had a rant this week about the fact that we have traditionally said "check that link before you click".  Sadly absolutely nobody does this, I don't do it, you don't do it, even [directors at GCHQ dont do it all the time](https://www.ncsc.gov.uk/blog-post/serious-side-pranking).  By telling people that this is what they should do, when they inevitably click the malware laden link and their machine does something weird, they are psychologically incentivised to not tell anyone, because they are conditioned to feel like they broke the rules, and people's first instinct when they break rules is to hide and hope they aren't caught.

This advice for security teams is exactly correct.  You should assume that 100% of your staff, including your security staff, your domain administrators, your people with access to the most sensitive content, will click the link 100% of the time.  You therefore need technical mechanisms to either prevent dodgy links getting to people, or to catch the outbound result of that link and prevent the user getting to the payload.  (Or you can add some technical system for highlighting links that are unsure, such as verified senders, external sender notifications and so on.)

For end users, we should remind them that people send emails with dodgy links and that if their suspicions are raised, that there are actionable things they can do, for example:

1. Don't click it *if you think it's suspicious*
2. Forward to security who will check it out, or
3. Press a button marked (suspicious) which might do that for you

Encouraging people to do the right thing isn't about telling them not to click, it's assuming they will and giving them the tools and information to be better some of the time.    (And despite all of this, many users will still click the link, so internally, you assume that none of this works and 100% of users will click 100% of links)


