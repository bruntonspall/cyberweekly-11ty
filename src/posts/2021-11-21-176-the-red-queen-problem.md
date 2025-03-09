---
title: "176 - The Red Queen Problem"
date: 2021-11-21
description: "> \"Well, in our country,\" said Alice, still panting a little, \"you'd generally get to somewhere else—if you run very fast for a long time, as we've been doing.\""
permalink: /the-red-queen-problem/
---

> "Well, in our country," said Alice, still panting a little, "you'd generally get to somewhere else—if you run very fast for a long time, as we've been doing."
> 
> "A slow sort of country!" said the Queen. "Now, here, you see, it takes all the running you can do, to keep in the same place. If you want to get somewhere else, you must run at least twice as fast as that!"

The Red Queen problem is defined as needing to run just to keep up with the competition.  In economic theory, it's about growing companies needing to continue growing at the same rate as their competitors simply to maintain an equal market share.  In evolutionary theory, it's about evolving features as fast as your predators and competitors to retain a share of the ecological system around you.

In security (and digital technology generally), it's about ensuring that we are improving our defences and our technology as fast as our adversaries are improving their ability to attack it.  If we fail to progress, what happens is that instead of simply standing still, we start to lag behind the adversaries faster and faster.

When faced with a red queen problem, one has two choices generally.  The first is to attempt to evolve and improve faster than the competition.  That is to say, developing against the competition just a bit faster than the other organisations around you and the adversaries, meaning that you start to break away from the pack.  

The second choice is to change the nature of the race in some manner, to seek an improvement that won't just make you 10% faster, but will see you find a 10x gain on your adversaries.  One could stretch the analogy to a breaking point, and suggest that this is like learning to zig when everyone else is zagging.

Keeping an eye on how adversaries are evolving is an important part of situational awareness in this case.  We need to know how well we are doing, and how well our competitors are doing to know what the race is actually like.  This week we've got some great views on how our adversaries think, how they are evolving and sadly the return of Emotet, a criminal capability that was firmly taken down and uninstalled over a year ago by law enforcement.

Within that, we need to remember that the vast majority of breaches don't use exciting new adversarial techniques, but continue to use the same techniques that have been shown to work time and time again.  These continue to catch the slow and the unwary.  We need to outpace those techniques just simply to keep up in 2021.

On an editorial note, I'm planning on taking a break for most of December.  Now I know I did that last year, and then had to [write the longest edition I've ever written](https://www.cyberweekly.net/solarwinds-special) but this time, I'm hoping for a quiet December!  I'm planning to do two more editions for next week and the first week of December, and then I'll take a break until January.  I'd like to do something special for the Christmas holidays though, so email or tweet me your blog posts, your predictions or just your favourite story of the year, and I'll try to pull together a contributors edition.  Let me know if you want to be named and linked, or you'd prefer to be anonymous (or pseudonymous).

## [Vulnerability Intelligence: Do You Know Where Your Flaws Are?](https://resources.digitalshadows.com/whitepapers-and-reports/vulnerability-intelligence-do-you-know-where-your-flaws-are)

[https://resources.digitalshadows.com/whitepapers-and-reports/vulnerability-intelligence-do-you-know-where-your-flaws-are](https://resources.digitalshadows.com/whitepapers-and-reports/vulnerability-intelligence-do-you-know-where-your-flaws-are)

> Managing vulnerabilities is a daunting task in an increasingly nightmarish world. With new vulnerabilities discovered every day, security teams
> are pushed into patching without adequate planning, or missing bugs that continue to represent a significant risk. We’re still not doing enough to
> fight what’s really the most basic of problems for any security team.
> 
> Digital Shadows’ Photon Research Team has researched the patching challenges faced by security professionals across almost every
> organization. Down the rabbit hole of cybercriminal forums, we came to understand how threat actors are continually exploiting security teams’
> weaknesses. The traditional, sometimes chaotic approach to vulnerability patching is not sustainable anymore.
> 
> Here are the top discoveries from our research:
> 
> * Threat actors are working tirelessly to exploit neglected
> vulnerabilities for their attacks.
> * Proof of concept (PoC) code exposed by security
> researchers has been exploited by opportunistic threat
> actors. Monitoring for relevant Indicators of Compromise
> (IOCs) can help preemptively mitigate risks to your
> organization.
> * Zero-day vulnerabilities, unaffectionately known as
> zero-days, are the most expensive flaws advertised on
> cybercriminal forums―unsurprisingly. Digital Shadows
> has observed cybercriminals discussing zero-days
> prices and reaching up to USD 10,000,000 during this
> investigation. If these prices once were a prerogative
> of exclusively state-sponsored threat actors; now
> cybercriminals have amassed sufficient fortunes to
> compete with them.
> * Older (and overlooked) vulnerabilities remain highly
> valuable to cybercriminals. They provide a cheap and
> efficient entry point into target environments. Low-skilled
> threat actors can easily exploit these flaws, carrying
> out attacks by relying on premade tools and methods
> provided by their more experienced counterparts.
> * Both expert and novice cybercriminals often cooperate
> and share knowledge to enhance their exploitation skills
> and carry out disruptive attacks.
> * Information overload, absence of vision of internal
> assets, and problems effectively communicating risks and
> liabilities to executives are only some of the obstacles
> that hinder an effective patch management process.
> * A risk-based approach is an effective defense to
> vulnerability management; it considers risk and likelihood
> of an exploit when dealing with the enormous amount
> of flaws out there. Vulnerability intelligence helps by
> favoring a proactive security posture and support in
> triaging, understanding, and mitigating flaws.


An excellent report from Digital Shadows here.

We need to ensure that when vulnerabilities are disclosed, that our security team is able to act on them, to put indicators of compromise into the system and make sure that they aren't taken by surprise.  Although the Digital Shadows threat research team are highlighting that the purchase of 0-days is moving from just nation state level and into organised crime (a scary trend), the reality of the most damaging compromises table is that most were not 0-days when they started being mass-exploited.  There are few reasons for organisations to still be vulnerable to 2019 Fortinet vulnerabilities or even the Exchange ProxyLogon vulnerability in 2021.


## [How ransomware impacts organizations.](https://thecyberwire.com/podcasts/cyberwire-x/22/transcript)

[https://thecyberwire.com/podcasts/cyberwire-x/22/transcript](https://thecyberwire.com/podcasts/cyberwire-x/22/transcript)

> what goes on after you have been hit by a ransomware attack? What is the impact to an organization? Can you walk us through a little bit of that?
> 
> Don Welch: Sure. So, the first part of your question, what goes on is sheer panic travels throughout everyone who has been told of the problems that we've got. And so, there's a lot of running around with their hair on fire. Hopefully not. I think many organizations now have a process and they, hopefully, practice it with tabletops to understand what is the decision making process. So, the first thing is understanding that you are attacked by ransomware and taking whatever important steps there are to contain it so that it doesn't spread throughout the organization.
> 
> Don Welch: A lot of ransomware attacks are more focused and are designed to spread, so that's common. You want to avoid that as much as possible, and contain the damage. And then, in parallel, you're working on the technical recovery. So, making sure we've got those backups, we know what's going on, we work through our disaster recovery plan on how we are going to recover these systems and so forth. Making sure we understand how far back in time the intrusion goes, to make sure that we don't just restore the ransomware along with our data. But, at the executive level, there should be a process going on about how you communicate this throughout your organization to your stakeholders.


What actually happens inside the organisation when it's hit by ransomware?  This is a good episode of the CyberWire with some useful insights.  You need to be practicing this, running a tabletop workshop to be able to ask questions about what would or wouldn't work in your response plan, and making sure that everyone knows what the process is, where to get to it, and what their role is.


## [Emotet botnet comeback orchestrated by Conti ransomware gang](https://www.bleepingcomputer.com/news/security/emotet-botnet-comeback-orchestrated-by-conti-ransomware-gang/)

[https://www.bleepingcomputer.com/news/security/emotet-botnet-comeback-orchestrated-by-conti-ransomware-gang/](https://www.bleepingcomputer.com/news/security/emotet-botnet-comeback-orchestrated-by-conti-ransomware-gang/)

> The botnet operators provided initial access at an industrial scale, so many malware operations depended on Emotet for their attacks, especially those in the so-called Emotet-TrickBot-Ryuk triad.
> 
> Ryuk is the predecessor of Conti ransomware. The switch occurred last year when Conti activity started to increase and Ryuk detections dwindled down. The operators of both ransomware strains have a long history of attacks hitting organizations in the healthcare and education sector.
> 
> AdvIntel researchers say that once Emotet disappeared from the scene, top-tier cybercriminal groups, like Conti (loaded by TrickBot and BazarLoader) and DoppelPaymer (loaded by Dridex) were left without a viable option for high-quality initial access.
> 
> “This discrepancy between supply and demand makes Emotet’s resurgence important. As this botnet returns, it can majorly impact the entire security environment by matching the ransomware groups’ fundamental gap” - AdvIntel
> 
> The researchers believe that one reason that contributed to multiple ransomware-as-a-service (RaaS) operations shutting down this year (Babuk, DarkSide, BlackMatter, REvil, Avaddon) was that affiliates used low-level access sellers and brokers (RDP, vulnerable VPN, poor quality spam).
> 
> With competitors leaving the ransomware business, the “traditional groups” such as Conti (previously Ryuk) and EvilCorp climbed up the ladder once again, attracting “the talented malware specialists who are massively leaving disbanded RaaSes.”


The return of Emotet has been much hyped this week.  Emotet was a frequent initial access for various groups, you could be infected by Emotet and then that access would be sold on to others.  Back in that day that was primarily for direct financial gain by installing banking trojans that intercepted your connection to your online banking and attempted to transfer money out of your bank.  Of course today, it's far more interesting to see what onward access you might have, whether a VPN back to work, credentials into work portals or SSH keys on your device.

The question will be whether organisations have gotten a better grip on initial defences that will prevent Emotet growing to the levels it was before.  


## [Conti ransomware gang suffers security breach - The Record by Recorded Future](https://therecord.media/conti-ransomware-gang-suffers-security-breach/)

[https://therecord.media/conti-ransomware-gang-suffers-security-breach/](https://therecord.media/conti-ransomware-gang-suffers-security-breach/)

> MalwareHunterTeam, who has been tracking ransomware gangs since the mid-2010s, described the sudden downtime as uncharacteristic for a ransomware group that generally had a more stable and professionally run infrastructure.
> 
> However, the Conti payment portal did eventually come back online Friday night, more than 24h after it was first taken down.
> 
> “Looks like Europeans have also decided to abandon their manners and go full-gansta simply trying to break our systems,” the Conti gang said in an insult-filled statement posted on their blog, effectively confirming Prodaft’s findings and their own security breach, in a message that was also meant to reassure its affiliates that their infrastructure was safe again.


The fights between criminal ransomware operators and security researchers continues unabated. 


## [Insider IP Theft Is Surging — and Most Can't Stop It](https://www.darkreading.com/vulnerabilities-threats/insider-ip-theft-is-surging-and-most-can-t-stop-it)

[https://www.darkreading.com/vulnerabilities-threats/insider-ip-theft-is-surging-and-most-can-t-stop-it](https://www.darkreading.com/vulnerabilities-threats/insider-ip-theft-is-surging-and-most-can-t-stop-it)

> Departing employees have always been a data security risk. Simply put: When people leave jobs, they take data and files with them. They take things that can help them land or succeed in their next gig — things such as source code, customer lists, and other trade secrets. A 2020 survey showed that more than two-thirds of workers say they've taken data to a new job more than once.
> 
> But the departing employee risk has exploded amid the so-called "Great Resignation" that Microsoft says has 41% of the global workforce (and 54% of Gen Z) ready to leave their jobs in the next year.
> 
> Taking IP Has Never Been Easier
> The other part of the problem is that data has never been more portable — so taking it has never been easier. Employees can easily store hundreds of gigabytes on their mobile devices, send company documents to their personal Gmail account, or quickly transfer data to personal cloud storage services like Dropbox. It's little surprise that a recent report noted that corporate litigation involving trade secret theft has shot up 400% over the last decade. And the widespread shift to remote and decentralized work — the "Great Disruption" — has dramatically amplified the data portability challenge. As workers increasingly connect remotely and conduct their everyday work and collaboration through cloud apps, a 2021 study found that employees are now 85% more likely to lose or leak data than they were pre-pandemic.


This is a good summary of a new problem that will be facing organisations in the next year or two.  I don't however agree with the "this is easy to solve", since it starts with (paraphrased)"If you can just monitor all your data flows".  Nobody can monitor all of their data flows, it's impossible to achieve.

What we can do is start thinking seriously about insider threats, and asking ourselves not just how we prevent them stealing data, but also how we detect, deter, reduce and recover from data loss incidents.


## [Triple Threat: North Korea-Aligned TA406 Scams, Spies, and Steals | Proofpoint US](https://www.proofpoint.com/us/blog/threat-insight/triple-threat-north-korea-aligned-ta406-scams-spies-and-steals)

[https://www.proofpoint.com/us/blog/threat-insight/triple-threat-north-korea-aligned-ta406-scams-spies-and-steals](https://www.proofpoint.com/us/blog/threat-insight/triple-threat-north-korea-aligned-ta406-scams-spies-and-steals)

> In this report, we describe in detail many of the campaigns and behaviors associated with an actor operating on behalf of the North Korean government: TA406. (See Figure 1.) We begin by explaining how TA406 is associated with Kimsuky, a threat actor name broadly tracked by the threat intelligence community. We then elaborate on how Proofpoint tracks the activity of Kimsuky as three separate threat actors—TA406, TA408 and TA427. Also, we detail the differences between these actors, based on Proofpoint’s visibility. 
> 
> This report also examines campaign timing and targeting by TA406, and it provides a look into how TA406 conducts phishing campaigns, including the tools and services used.
> 
> TA406 employs both malware and credential harvesting in espionage and information-gathering campaigns. This report details several examples of each, including different types of credential collection and two implants used by TA406 that haven’t been discussed before in open-source reporting. And finally, like all other North Korean state-sponsored actors that Proofpoint tracks, we provide evidence that TA406 conducts financially motivated campaigns, including the targeting of cryptocurrency and sextortion.
> 
> 


This is a useful report not because of the actor or actions that it covers (State based actor does phishing, yawn), but because it's a good breakdown of how what can be labelled a "single actor" like Kimsuky, can actually be what appears to be multiple discreet sets of activity.

This strikes to the heart of the problem of attribution.  It's really hard to work out if these are the same individuals, different teams within the same organisation, or even 3 totally different teams.  There are shared tools, but with local team changes in both how they are used, hosted and delivered.  It's also possible, although unlikely in this case, that one of these actors could be a totally unrelated actor who has stolen the tools of the main actor and is impersonating them.

There's a lot in this report about the attack infrastructure that is used by these actors, but the majority of it goes under the same standard ATT&CK TTP's, phishing emails, credential harvesting, and attachments with malware.


## [Beyond Supply Chain Attacks and Ransomware](https://cisomag.eccouncil.org/beyond-supply-chain-attacks-and-ransomware-2022-will-bring-more-complex-challenges-and-new-types-of-attacks/)

[https://cisomag.eccouncil.org/beyond-supply-chain-attacks-and-ransomware-2022-will-bring-more-complex-challenges-and-new-types-of-attacks/](https://cisomag.eccouncil.org/beyond-supply-chain-attacks-and-ransomware-2022-will-bring-more-complex-challenges-and-new-types-of-attacks/)

> Although it may sound surprising, most of the cyberattacks we have seen during the past year were not highly technically sophisticated; this is true for both simple cybercriminals and state-level actors. Time and again, we saw them using publicly-available tools to take advantage of known vulnerabilities; as this not only saves them time and money but allows them the cover of deniability. In addition, as much as we do see growing usage of the much-feared zero-day attacks, these are still mainly limited to high-level state actors and superpowers.


It must be coming to Christmas as the "year in review" and "predictions for 2022" articles have started popping up.

This one I mostly agree with, if a bit simplistic.  Attackers have long been able to use open source attack tools, they've just gotten better and easier to use this year, and ransomware affiliate models has meant that the attackers have something to do once they are in.


## [The bad old days – Javvad Malik](https://javvadmalik.com/2021/11/12/the-bad-old-days/)

[https://javvadmalik.com/2021/11/12/the-bad-old-days/](https://javvadmalik.com/2021/11/12/the-bad-old-days/)

> I mean take for example passwords – they were a funny thing even back then. We had a policy that dictated how passwords should be. The length, the strength, the expiry and rotation.
> 
> Users would have to reset the password every 90 days – some organisations still enforce that rule today. The problem is they’re like the analogy of 5 monkeys in the cage within which there is one banana. Any time a monkey goes for the banana all of the monkeys get hosed down with cold water. All the monkeys soon realised that it was a bad idea to go for the banana’s. When one monkey was removed and a new ‘dry’ monkey was introduced – if it went for the banana, all the other monkeys would beat it up because they didn’t want to get hosed down. One by one the moneys were replaced until you had all monkeys in the cage that had never been subjected to being hosed down. Yet when a new monkey went for a banana they’d all beat him up. Because that’s the way things have always been.
> 
> Looking at how security is done today, they resemble those monkeys in the cage. You ask them why they follow something and they say it’s because of policy – or because thats how it’s always been done. No-one ever says it’s because they’re blind monkeys.
> 
> Many companies still force their employees to reset their passwords every 90 days – you ask them why is that and they say it’s the policy – but they’re not too sure as to why. Some of them will try to quote something like a standard. We used to quote the orange book – yeah that’s right the DoD’s Trusted Computer System Evaluation Criteria (TCSEC)


This whole post is one long rant from a "long in the tooth infosec professional", but it's entertaining and a valuable documentation of some of our history.

This part around passwords in particular really stuck with me.  Lots of people will make up reasons for why password rotation exists, but the reality is that we have no hard data that it reduces or prevents system compromise, and lots of hard data that it massively reduces the entropy of users passwords.


## [Building a social cyber community of interest - lessons from the field - by Ollie - Desk of a cyber CTO](https://cybercto.substack.com/p/building-a-social-cyber-community)

[https://cybercto.substack.com/p/building-a-social-cyber-community](https://cybercto.substack.com/p/building-a-social-cyber-community)

> So in the winter of 2018 (January) I took the plunge and started to build on Reddit /r/blueteamsec . Its name was unoriginal and named after the /r/netsec/ (one of the original security home on Reddit) and /r/redteamsec/ (founded the summer before for Red Teams). Funnily enough someone latterly created /r/purpleteamsec/ in February 2020.
> 
> In the early years (the first two) there was very few of us, but we grow. I built the community using a very simple set of steps:
> 
> * Clear rules - no high-level abstract news or marketing
> * Strong moderation to keep signal/noise levels right.
> * Finding useful content and using it as an overflow brain for useful things.
> * Cross-posting to more popular ones in a form of internal Reddit advertisement to grow the user base.
> 
> Over time I refined the model and the community to create a high quality space and incentivise participation :
> 
> * Blocked cross-posting into subreddit to keep us as a golden root source of information.
> * Added post flair to categorize the content across different cyber defence tradecraft elements - discovery, defence, vulnerability, exploitation etc.
> * Added user flair to recognize those community builders.
> * Awarding extensively using internet points on Reddit (gold, silver etc.) to contributors of great content as a thank you.
> 
> This started to have an effect, but as mentioned the first couple of years were meagre.
> 


I'd missed this when Oli first published it.  The thinking behind the [reddit community blueteamsec](https://reddit.com/r/blueteamsec) matches very closely with my thinking and purpose in general.

We as a community are better when we work together, but for some reason, most people are content to be part of a communtiy that exists, but struggle to create or initiate community events.

BlueTeamSec and the work that Oli does was a major inspiration for CyberWeekly, and so it's nice to see how cyclical this all is.  I took his ideas and extended them, and then he takes my ideas and extend them, and all for the greater benefit of the communities around us.


## [GitHub - chughes757/SecureSoftwareSupplyChain](https://github.com/chughes757/SecureSoftwareSupplyChain)

[https://github.com/chughes757/SecureSoftwareSupplyChain](https://github.com/chughes757/SecureSoftwareSupplyChain)

> Securing the software supply chain has increasingly become a topic of interest and concern for many IT and Cybersecurity leaders across both the public and private sector. Due to seveal high profile cybersecurity breaches facilitated through software supply chain compromise, organizations are increasingly realizing both the fragility and complexity of the software supply chain. This repository is a collection of resources aggregated to help aid practitioners and leaders both understand the scope of the problem and some of the best practices and solutions to mitigate the risk associated with an insecure software supply chain.


A nice collection of further reading resources for those of us who are thinking more about securing the software supply chain


