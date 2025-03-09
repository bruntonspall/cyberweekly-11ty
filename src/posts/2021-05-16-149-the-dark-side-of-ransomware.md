---
title: "149 - The dark side of ransomware"
date: 2021-05-16
description: "Sorry, I couldn't resist the pun!"
permalink: /the-dark-side-of-ransomware/
---

Sorry, I couldn't resist the pun!

This last few years has seen the rise and rise of ransomware operators.  It used to be that the operators had to compromise you and demand a ransom, but there have been changes recently, from the rise of Ransomware-as-a-service, enabling central gangs to bring in "affiliates", who simply pay to license the ransomware software on systems that they have compromised, in return for a share of the profits.

What we've also seen is the change in tactics by operators, who are demanding larger and larger ransoms, targeting those with insurance who will pay out, and the increase in double extortion methods, where they sell the data exfiltrated rather than just recovery of the system.

This has been on the increase for years, and many have wondered what we will need to do about it, but the hack of Colonial, who run a major oil pipeline in the US, flooding social media with pictures of people stockpiling fuel in the US, which creates a political incentive for the US Government to really do something about this.

Whether they will use new powers and what the [UK calls "full spectrum cyber"](https://www.gov.uk/government/news/international-policy-review-puts-cyber-at-the-centre-of-the-uks-security), and the [US calls "defending forward"](https://www.fdd.org/analysis/2020/12/15/defending-forward-defending-forward-in-the-cyber-domain/), or whether this has been a political conversation to increase law enforcement activity within the countries that house these criminal groups, and the companies that host their infrastructure, I doubt we'll ever know, but it's clear that some action has been taken.  What remains to be seen is just how far this will go.  Is this an activity to deal with the ransomware operators behind Darkside, or has this roused a set of actions against ransomware as a criminal enterprise in the large?

As defenders, there's not a lot that we can do other the same old findings.  Patch your infrastructure, especially at the network edges such as VPNs, and deploy endpoint detection and response capabilities to prevent malware from being downloaded and executed on endpoints

## [US Gov Issues Emergency Order While Colonial Pipeline Is Down - Zero Day](https://zetter.substack.com/p/biden-declares-state-of-emergency)

[https://zetter.substack.com/p/biden-declares-state-of-emergency](https://zetter.substack.com/p/biden-declares-state-of-emergency)

> Colonial Pipeline has said that only its corporate IT network was infected with the ransomware but that it decided to close down the operational network — and the pipelines that this network controls — out of an abundance of caution.
> 
> The source who works for the midstream oil company told Zero Day that one reason Colonial might still be keeping the pipelines offline — in addition to needing to add security measures to it — is because “something they need for [restarting] the pipeline is ransomed.”
> 
> He thinks this could be the automated ticketing system for billing customers, which is on the corporate IT network that was hit with the ransomware. If that system is locked, Colonial can’t invoice customers automatically, he said.
> 
> Colonial’s operational network controls the flow of oil product from the pipeline to distributors, then passes information to the ticketing system — located on the IT network — about how much each distributor received so the ticketing system can invoice them. If that system is locked and the pipeline is still flowing, Colonial would have to manually collect information about how much fuel is flowing to each customer, then manually process invoices. If Colonial didn’t already have a plan for doing this manually, it may keep the pipelines down until it can determine an efficient way to invoice customers this way or until it can restore the automated ticketing system.


This is important to note.  It's easy when thinking about industrial control systems to assume that if you "airgap" the operational control systems, then you wont be affected by attackers.  

It's true that a well airgapped system will mean that attackers can't get access to the operational systems to trigger failsafes or changes to the industrial process to disrupt your business.

But of course, like any other company, these companies need to have an IT system, from HR records to payroll systems, and of course invoicing and customer support systems.  Even if the operational tools are working, a company cannot work without the IT systems.


## [A Closer Look at the DarkSide Ransomware Gang – Krebs on Security](https://krebsonsecurity.com/2021/05/a-closer-look-at-the-darkside-ransomware-gang/)

[https://krebsonsecurity.com/2021/05/a-closer-look-at-the-darkside-ransomware-gang/](https://krebsonsecurity.com/2021/05/a-closer-look-at-the-darkside-ransomware-gang/)

> DarkSide also started recruiting new affiliates again last month — mainly seeking network penetration testers who can help turn a single compromised computer into a full-on data breach and ransomware incident.
> 
> “We have grown significantly in terms of the client base and in comparison to other projects (judging by the analysis of publicly available information), so we are ready to grow our team and a number of our affiliates in two fields,” DarkSide explained. The advertisement continued:
> 
> “Network penetration testing. We’re looking for one person or a team. We’ll adapt you to the work environment and provide work. High profit cuts, ability to target networks that you can’t handle on your own. New experience and stable income. When you use our product and the ransom is paid, we guarantee fair distribution of the funds. A panel for monitoring results for your target. We only accept networks where you intend to run our payload.”
> 
> DarkSide has shown itself to be fairly ruthless with victim companies that have deep pockets, but they can be reasoned with. Cybersecurity intelligence firm Intel 471 observed a negotiation between the DarkSide crew and a $15 billion U.S. victim company that was hit with a $30 million ransom demand in January 2021, and in this incident the victim’s efforts at negotiating a lower payment ultimately reduce the ransom demand by almost two-thirds.


Advertising for more people who can take a single compromise computer and turn that into full network takeover.  This human guided compromise is often the second stage after an initial operator manages to compromise a single machine.  

This is also fascinating for the engagement and conversation between the attackers and the compromised company, negotiating the payout down from the original $30m or so


## [Darkside ransomware gang says it lost control of its servers & money a day after Biden threat | The Record by Recorded Future](https://therecord.media/darkside-ransomware-gang-says-it-lost-control-of-its-servers-money-a-day-after-biden-threat/)

[https://therecord.media/darkside-ransomware-gang-says-it-lost-control-of-its-servers-money-a-day-after-biden-threat/](https://therecord.media/darkside-ransomware-gang-says-it-lost-control-of-its-servers-money-a-day-after-biden-threat/)

> n two conferences this week, on Monday and Thursday, US President Biden himself came out and said the US would go after the group after one of its attacks crippled a major fuel transport pipeline that impacted half of the US East Coast, leading the US to declare a state of national emergency in order to ensure gasoline was delivered to impacted regions.
> 
> “We have been in direct communication with Moscow about the imperative for responsible countries to take decisive action against these ransomware networks,” President Biden said in a press conference on Thursday.
> 
> “We are also going to pursue a measure to disrupt their ability to operate,” he added


Another good analysis of the effect that this message has had on the Ransomware sector.


## [DarkSide ransomware servers reportedly seized, operation shuts down](https://www.bleepingcomputer.com/news/security/darkside-ransomware-servers-reportedly-seized-operation-shuts-down/)

[https://www.bleepingcomputer.com/news/security/darkside-ransomware-servers-reportedly-seized-operation-shuts-down/](https://www.bleepingcomputer.com/news/security/darkside-ransomware-servers-reportedly-seized-operation-shuts-down/)

> In the post, 'Unkn' shared a message allegedly from DarkSide explaining how the threat actors lost access to their public data leak site, payment servers, and CDN servers due to law enforcement action.
> 
> "Since the first version, we have promised to speak honestly and openly about problems. A few hours ago, we lost access to the public part of our infrastructure, namely : Blog, Payment server, DOS servers," reads the forum post from UNKN.
> 
> "Now these servers are unavailable via SSH, the hosting panels are blocked. Hosting support, apart from information "at the request of law enfocement agencies", does not provide any other information."
> 
> [...]
> 
> However, after the DarkSide's reported takedown, REvil has now begun to impose new restrictions on who can be encrypted.
> 
> REvil's representative, UNKN, states that affiliates are now required first to gain permission to target an organization and that they can no longer target the following entities:
> 
> 1. Work in the social sector (health care, educational institutions) is prohibited;
> 2. It is forbidden to work on the gov-sector (state) of any country;
> 
> Ransomware-as-a-Service (RaaS) operations have historically run as a free-for-all, where affiliates encrypt any victim they want without gaining prior approval.


This is an interesting note, somebody at least has clearly taken some action against Darkside.  There's a number of theories floating around out there.  It could be the US Government or one of its allies, it could be a competing criminal gang whose sensed weakness, or it could be Darkside themselves attempting to get themselves out of the game (or reinvent themselves).

It's pretty clear that the signal has been read by Ransomware-as-a-service operators though that the US Government machine has noticed them and is turning it's eyes to look at them.  Time for them to revert back to petty crime and not "poke their head above the fence".

We'll see what the other big operators do next


## [Cyber attack 'most significant on Irish state' - BBC News](https://www.bbc.co.uk/news/world-europe-57111615)

[https://www.bbc.co.uk/news/world-europe-57111615](https://www.bbc.co.uk/news/world-europe-57111615)

> A cyber attack on Irish health service computer systems is "possibly the most significant cybercrime attack on the Irish state", a minister has said.
> 
> Speaking on broadcaster RTÉ, Ossian Smyth said the attack "goes right to the core of the [health] system".
> 
> However, he also said that it was "not espionage".
> 
> Taoiseach (Irish PM) Micheál Martin said that he had consulted with cyber security experts and that the state would not be paying a ransom.
> 
> He said it would "take some days" to assess its impact.
> 
> "What's important is people cooperate with the HSE," he said, and added that emergency services remain open, and the vaccine programme continues uninterrupted.
> 
> The health service has temporarily shut down its IT system to protect it after the attack.


This is a serious attack on the health system, not just because ransomware is in the news, but because Conti is normally human operated, so somebody knew what they were doing when they directed it.

Furthermore, if, like many ransomware operators, they exfiltrated data before encrypting the devices, then we could be looking at a huge potential leak of health data.  Hopefully this is not the situation, but that's the worst case scenario here.


## [I Have a Lot to Say About Signal’s Cellebrite Hack | Center for Internet and Society](https://cyberlaw.stanford.edu/blog/2021/05/i-have-lot-say-about-signal%E2%80%99s-cellebrite-hack)

[https://cyberlaw.stanford.edu/blog/2021/05/i-have-lot-say-about-signal%E2%80%99s-cellebrite-hack](https://cyberlaw.stanford.edu/blog/2021/05/i-have-lot-say-about-signal%E2%80%99s-cellebrite-hack)

> So is, uh, is Signal going to update its app to make it hack police computers? Recall what Signal said about how “upcoming versions of Signal will be periodically fetching files to place in app storage...”. It’s very cutesy, coy, evasive language and it doesn’t say exactly what the hell they mean by that. They’re winking and smiling and nudging the reader instead of being clear.
> 
> They seem to be implying — or at least they seem to intend for the reader, and more importantly Cellebrite and its customers, to infer — that Signal will add “innocuous” code to their app that might, maybe, alter the data on a Cellebrite machine if the phone gets plugged into it. If they’re saying what they’re hinting they’re saying, Signal basically announced that they plan to update their app to hack law enforcement computers and also tamper with and spoliate evidence in criminal cases. 
> 
> When you put it that way, it becomes clear why they were using such coy language and why I bet they’re bluffing: Those things are illegal. It’s a stunt that could get their own users in trouble (if the user gets blamed for what her phone does to a Cellebrite machine, she will be plunged into a world of pain, irrespective of whether she would ultimately be held culpable for the design of an app she had installed on her phone), and could get them in hot water (because they intentionally designed and put those booby-trapped files on the user’s phone).
> 
> [...]
> 
> So while computer security folks were giggling at Signal’s cute, clever blog post, lawyers like me were sighing. Why? Because of an important life lesson that engineers typically don’t understand: Judges hate cute and clever. 
> 
> In general, if you do something very clever and you show it off in a cute presentation, it won’t go over well with a judge. They have no patience for stunts and showboating. The courtroom is not the stage at DEF CON. And judges do not like mealy-mouthed vague statements that are designed for plausible deniability. 
> 
> Trying to find the edges of the law using technology will not make a judge, or prosecutors for that matter, shrug and throw up their hands and say “Wow, that’s so clever! You sure got us.” They won’t reward your cleverness with reddit coins and upvotes and retweets. They will throw the book at you. (As usual, xkcd said it best, not once, but twice.) 
> 
> The law just does not work the way engineers assume it does. Having that pounded into you by law professors is the easy way to learn how the law really works.


This is a good rebuttal against the Signal blogpost from a few weeks back, arguing why it's mostly a flash in the pan, and why it's still going to cause problems either way


## [GitHub - iacsecurity/tool-compare](https://github.com/iacsecurity/tool-compare)

[https://github.com/iacsecurity/tool-compare](https://github.com/iacsecurity/tool-compare)

> In the world of infrastructure-as-code security there are several tools for users to choose from. The goal of this repository is to help compare the different options so that users can choose the tool that best fits their own needs.


Nice comparison of various infrastructure as code security compliance tools, such as Checkov, Terrascan and Tfsec


## [AI security risk assessment using Counterfit - Microsoft Security](https://www.microsoft.com/security/blog/2021/05/03/ai-security-risk-assessment-using-counterfit/)

[https://www.microsoft.com/security/blog/2021/05/03/ai-security-risk-assessment-using-counterfit/](https://www.microsoft.com/security/blog/2021/05/03/ai-security-risk-assessment-using-counterfit/)

> However, performing security assessments of production AI systems is nontrivial. Microsoft surveyed 28 organizations, spanning Fortune 500 companies, governments, non-profits, and small and medium sized businesses (SMBs), to understand the current processes in place to secure AI systems. We found that 25 out of 28 businesses indicated they don’t have the right tools in place to secure their AI systems and that security professionals are looking for specific guidance in this space.
> 
> This tool was born out of our own need to assess Microsoft’s AI systems for vulnerabilities with the goal of proactively securing AI services, in accordance with Microsoft’s responsible AI principles and Responsible AI Strategy in Engineering (RAISE) initiative. Counterfit started as a corpus of attack scripts written specifically to target individual AI models, and then morphed into a generic automation tool to attack multiple AI systems at scale.
> 
> Today, we routinely use Counterfit as part of our AI red team operations. We have found it helpful to automate techniques in MITRE’s Adversarial ML Threat Matrix and replay them against Microsoft’s own production AI services to proactively scan for AI-specific vulnerabilities. Counterfit is also being piloted in the AI development phase to catch vulnerabilities in AI systems before they hit production.


This is a lovely looking tool from Microsoft for conducting adversarial assessments on AI systems.  But further than that, the links in here are important if you are embedding or building AI systems within your systems.


## [I Mailed an AirTag and Tracked Its Progress; Here's What Happened - The Mac Security Blog](https://www.intego.com/mac-security-blog/i-mailed-an-airtag-and-tracked-its-progress-heres-what-happened/)

[https://www.intego.com/mac-security-blog/i-mailed-an-airtag-and-tracked-its-progress-heres-what-happened/](https://www.intego.com/mac-security-blog/i-mailed-an-airtag-and-tracked-its-progress-heres-what-happened/)

> After the AirTag was delivered, my friend left the envelope on a table in his house. He has an iPhone, so I expected him to be notified of the presence of the AirTag after a while. According to Apple, anyone who is in the presence of an AirTag that has been separated from its owner for three days will get an alert on their iPhone. They are supposed to get an "AirTag Found Moving With You" message. It’s possible that this alert only displays when the person is actually moving with the AirTag, but that seems somewhat limiting; imagine that you leave an AirTag in someone’s bag at their home, but they don’t take the bag with them right away. Should it take another three days for them to get an alert? Apple isn’t clear enough about the way to prevent AirTags from being used by stalkers.
> 
> I therefore expected my friend to get such a message on or after Monday afternoon, three days after I mailed it. By Tuesday, he had still not received any alerts. As I write this article, I just checked in the Find My app, and the AirTag was last seen 13 minutes ago, at his location, but he still has not received any alerts.
> 
> Apple also says that “When moved, any AirTag separated for a period of time from the person who registered it will make a sound to alert those nearby.” Again, this is supposed to be three days, and the sound apparently only plays for 15 seconds, and isn’t very loud, according to this Washington Post article. My friend thinks he might have heard a sound at some point, but he couldn’t be sure, because he had the TV on at the time.


Fascinating insight into AirTag's and how they work.  But what's scary here is just how inefficiently these protect people against malicious use.  Apple's guidance seems to suggest that the tag will do a lot more than simply make a noise once, but whether it does that in practice remains to be seen.


