---
title: "247 - Delivering what the users want"
date: 2024-04-28
description: "In Charles Arthur's book on cyber attacks, [Cyber Wars (amazon affiliate link)](https://amzn.to/3y5xxCv), Charles pointed out that the stock price of companies that suffered public breaches often dipped ever so slightly straight after an attack and then rebounded up.  Consumers it seems didn't care whether their service providers were hacked or not, and in one case study, it was shown that only people who were considering leaving that quarter anyway actually left, and new customer signups continued at normal pace, which somewhat counter-intuitively, got rid of some of the more difficult customers, and replaced them with loyal ones!"
permalink: /delivering-what-the-users-want/
---

In Charles Arthur's book on cyber attacks, [Cyber Wars (amazon affiliate link)](https://amzn.to/3y5xxCv), Charles pointed out that the stock price of companies that suffered public breaches often dipped ever so slightly straight after an attack and then rebounded up.  Consumers it seems didn't care whether their service providers were hacked or not, and in one case study, it was shown that only people who were considering leaving that quarter anyway actually left, and new customer signups continued at normal pace, which somewhat counter-intuitively, got rid of some of the more difficult customers, and replaced them with loyal ones!

Users have a remarkably low baseline for caring about security.  Most of the time security is classical economic hygiene factor for purchasers, the complete lack of it will be noted, but it's presence is more or less ignored when comparing products.  Purchasers assume in many cases that all products, services or companies are equally unsafe and rarely does it figure high in surveys on how purchasers make purchasing decisions.  In essence, they cost lack of security into the fundemental decision to buy anyway.

That means that convincing the company board, or indeed anyone truly rational within an organisation to care about security is a bit of a fools errand, because people only really care about security when its absence impacts on them.  The same is true for many other hygiene factors, from quality to documentation, ease of use and accessibility.

As engineers, security practitioners and leaders, we often care about these hygiene factors far more than our users do, and that's right, that's how we ensure that we are investing and building products that actually do work, rather than products that fall apart in the users hands.  But we cannot mistake that the users care significantly about the choices that we make.  We have to remember that the ultimate aim is to deliver what the user wants (or if you prefer, what the user needs while telling them they want what you deliver!).

No user has ever selected their product becuase ofthe brand of Kubernetes platform it runs on, whether the database was a specific vendor, or which cloud provider was selected.  Those things matter to us within the organisation, and in some cases, those decisions might be important to company strategy, in that they are decisions that will impact the speed to market, the quality of product and the ability to maintain the product.  But if we spend too much time sweating the details of every single internal decision, we do so because we forgot that the primary purpose is to produce products that delight, that fill a need and a niche, and that deliver value to the purchaser or user of them.

## [LogLog Games - Leaving Rust Gamedev after 3 years ](https://loglog.games/blog/leaving-rust-gamedev/)

[https://loglog.games/blog/leaving-rust-gamedev/](https://loglog.games/blog/leaving-rust-gamedev/)

> ECS in Rust has this tendency of turning from something that is considered a tool in other language to become almost a religious belief. Something that should be used because it is pure and correct, and because doing that is the right way.
> 
> Programming language communities often have certain tendencies, and having been a serial language hopper over the years I find it interesting to compare these. The closest thing to Rust's view on ECS I can think of is Haskell, except, and I know this is an oversimplification but I'll say it anyway, I do feel that the overall community in Haskell is a lot more mature, and that people in general tend to be more reasonable about the existence of other approaches, and view Haskell as a "fun tool to solve problems where it fits well".
> 
> Rust on the other hand often feels like when you talk to a teenager about their preference about anything. What comes out are often very strong opinions and not a lot of nuance. Programming is a very nuanced activity, where one has to often make suboptimal choices to arrive at a result in a timely manner. The prevalence of perfectionism and obsession with "the correct way" in the Rust ecosystem often makes me feel that the language attracts people who are newer to programming, and are easily impressionable. Again, I understand this doesn't apply to everyone, but I think the overall obsession with ECS is in some sense a product of this.
> 
> […]
> 
> Because of the general vibes in the Rust community it's very common for people to receive very positive reinforcement on what they're building. This is nice in terms of mental health and short term motivation, but having gone through the process of releasing something on Steam publicly more than once, I feel like many people are headed for a bitter realization once people who aren't in their friend group/community see their game. The reason I'm saying this is that I think the community as a whole has adopted this idea of relentless positivity and praise towards everything Rust related, shielding itself completely from the outside world.
> 
> But the real world of gamers is not as nice. Gamers on Steam don't care if something is made in Rust, they don't care if it took 5 years to make, they don't care if the code is opensource. **They care about looking at the game, and within** **_a few seconds_** **being able to tell if this is going to be a waste of time, or something potentially interesting.** […]
> 
>  If you're showcasing your game and the response is anything but "can I please play this?", the game was not interesting to the person who you showed it to. At least not in the sense that truly matters for the purposes of making commercially successful games. 


This is a long blog/rant, and if you aren’t into the Rust programming language and/or game development, much of it won’t be interesting.  But there’s some interesting tidbits in here that I think are more general than just in game development.

This core idea that somehow our technical choices matter to our end users is one of those projections that doing good user research counters.  Until you see real people using your product, in their real workflows, it’s far easier to simply project that your users and customers are simply you, probably without the complex computer skills and dashing good looks, but still, they are copies of you who care about the same things you care about.

Endless conversations on technical mailing lists will argue over whether emacs is better than vi, whether C++ is better than Rust, or whether you should use a relational database versus an document database.  But in the end, it’s incredibly unlikely that your users care in the slightest.  Almost nobody peers under the good of the products they are using, and if they do, they probably have their own, semi-religious beliefs about what good looks like.

Users care about whether your product meets their needs in the most usable possible way.  In the same way that the blog argues that game players don’t care whether you used an ECS system, or used Rust to program the game underneath, they just want a fun playable experience. 


## [Efficient Security Principle (ESP) ](https://danielmiessler.com/p/efficient-security-principle)

[https://danielmiessler.com/p/efficient-security-principle](https://danielmiessler.com/p/efficient-security-principle)

> **The Efficient Security Principle** 
> 
> 1. The security baseline of an offering or system faces continuous downward pressure from customer excitement about, or reliance on, the offering in question.
> 2. The baseline for an offering’s security will be set at the point at which people will not stop using the offering because it’s insecure.
> 3. The better the offering is, the lower the security baseline can be without losing customers.
> 
> […] 
> **If You’re a Technical Security Expert**  
> 
> _Recommendation_ **:** Realize that it’s not about us as technical security experts. Realize that it’s about the bigger system, which is primarily concerned with the functionality they’re getting from an offering, not with its security risks. If people in general know the risk and they’re still taking it, that’s just because they value the offering that much. Don’t take it personally. 
> 
> **If You’re a Security Leader** 
> 
> Even security leaders within large organizations can become disillusioned because they don’t see their programs being taken seriously. Just like the technical implementers, they know how to improve security and they can get quite upset when nobody is listening. 
> 
> _Recommendation_ **:** First, make sure the baseline is actually where people think it is. If there are security gaps that the company—or its users—don’t know about, make those visible to close the gap of knowledge and get additional support. Second, find innovative ways to raise the baseline in a way that doesn’t inconvenience the company or its users. They may not want to spend much extra effort to raise the baseline, but they won’t object if it goes up without effort on their part. 


I like this articulation, that security of a system will mostly face a downward pressure to a baseline that is an acceptable level of security for the customers risk.

I also like that bit at the end, nobody is going to object to the security level going up, they just don’t want to inconvenience the users or their delivery plans.  Finding out ways that you can get security done while also meeting those aims is the key to raising the security baseline above the lowest possible point 


## [GuptiMiner: Hijacking Antivirus Updates for Distributing Backdoors and Casual Mining - Avast Threat Labs ](https://decoded.avast.io/janrubin/guptiminer-hijacking-antivirus-updates-for-distributing-backdoors-and-casual-mining/)

[https://decoded.avast.io/janrubin/guptiminer-hijacking-antivirus-updates-for-distributing-backdoors-and-casual-mining/](https://decoded.avast.io/janrubin/guptiminer-hijacking-antivirus-updates-for-distributing-backdoors-and-casual-mining/)

> We’ve been tracking a curious one here. Firstly, GuptiMiner is a highly sophisticated threat that uses an interesting infection chain along with a couple of techniques that include performing DNS requests to the attacker’s DNS servers, performing sideloading, extracting payloads from innocent-looking images, signing its payloads with a custom trusted root anchor certification authority, among others.
> 
> The main objective of GuptiMiner is to distribute backdoors within big corporate networks. We’ve encountered two different variants of these backdoors: The first is an enhanced build of PuTTY Link, providing SMB scanning of the local network and enabling lateral movement over the network to potentially vulnerable Windows 7 and Windows Server 2008 systems on the network. The second backdoor is multi-modular, accepting commands from the attacker to install more modules as well as focusing on scanning for stored private keys and cryptowallets on the local system.
> 
> Interestingly, GuptiMiner also distributes XMRig on the infected devices, which is a bit unexpected for such a thought-through operation.
> 
> The actors behind GuptiMiner have been capitalizing on an insecurity within an update mechanism of Indian antivirus vendor eScan to distribute the malware by performing a man-in-the-middle attack. We disclosed this security vulnerability to both eScan and the India CERT and received confirmation on 2023-07-31 from eScan that the issue was fixed and successfully resolved.
> 
> GuptiMiner is a long-standing malware, with traces of it dating back to 2018 though it is likely that it is even older. We have also found that GuptiMiner has possible ties to Kimsuky, a notorious North Korean APT group, by observing similarities between Kimsuky keylogger and parts of the GuptiMiner operation. 


One of the problems in attributing campaigns is that you rely on what the system actually does, which may or may not fit the actor you think is behind it.

This attack had a couple of interesting notes to it.

Firstly, the attacker is using some form of Man-in-the-middle attack on the antivirus suite when it downloads updates.  It turns out that eScan didn’t use HTTPS or TLS Cert pinning, so an attacker that can influence the network between the desktop/server and the eScan update service could deploy down malicious code.  MITM’ing isn’t hard, but it’s quite hard to do selectively and effectively without being caught.  This could be that they already have compromised the endpoint, or maybe they’ve compromised the company VPN or a central service, or compromised Wifi etc…

It’s a good reminder that HTTPS everywhere, when combined with either certificate transparency or cert pinning is good for authenticating software updates.

Secondly, there’s some really neat use of a malicious DNS server in this attack.  Normally when your computer needs to lookup a domain, it asks the local resolver, which then goes and asks out on the internet on the root servers.  In this case, the malware is hardcoded to go and ask a malicious DNS server for a specific type of record.  This will look slightly odd in network traffic, but it’s not entirely out of the normal for some services to use trusted or third party DNS servers.  In this case, the actual domain being looked up is irrelevant, because the next stage of the malware is obfuscated within an image returned in the DNS txt record, which is not the sort of thing that most SOC’s would be looking for.

Thirdly, and most oddly, the above feels pretty advanced.  There’s significant effort into the control infrastructure, there’s the use of Man in the middle attacks and there’s some other bits in the detailed writeup.  But then once it’s on the machine, it deploys not just some configurable malware to gain access to the target, but it also deploys a cryptocurrency mining client.  There’s some work to look for crypto-currency wallets, private keys, and also to keep the CPU usage of the crypto-miner below a certain level to avoid notice.  But still, it’s odd that an actor with this level of competence is also deploying crypto-miners onto their targets.

That means from an attribution perspective, this looks like an advanced attack, with capable infrastructure, but doing things that you wouldn’t necessarily expect from such an advanced attacker. 


## [GitHub besieged by millions of malicious repositories in ongoing attack | Ars Technica ](https://arstechnica.com/security/2024/02/github-besieged-by-millions-of-malicious-repositories-in-ongoing-attack/)

[https://arstechnica.com/security/2024/02/github-besieged-by-millions-of-malicious-repositories-in-ongoing-attack/](https://arstechnica.com/security/2024/02/github-besieged-by-millions-of-malicious-repositories-in-ongoing-attack/)

> The technique observed by Apiiro is known as repo confusion.
> 
> “Similar to dependency confusion attacks, malicious actors get their target to download their malicious version instead of the real one,” Wednesday’s post explained. “But dependency confusion attacks take advantage of how package managers work, while repo confusion attacks simply rely on humans to mistakenly pick the malicious version over the real one, sometimes employing social engineering techniques as well.”
> 
> The flow of the campaign is simple:
> 
> 1. Cloning existing repos (for example: TwitterFollowBot, WhatsappBOT, discord-boost-tool, Twitch-Follow-Bot, and hundreds more)
> 2. Infecting them with malware loaders
> 3. Uploading them back to GitHub with identical names
> 4. Automatically forking each thousands of times
> 5. Covertly promoting them across the web via forums, Discord, etc.
> 
> Developers who use any of the malicious repos in the campaign unpack a payload buried under seven layers of obfuscation to receive malicious Python code and, later, an executable file. The code—mainly consisting of a modified version of the open source [BlackCap-Grabber](https://github.com/Inplex-sys/BlackCap-Grabber-NoDualHook?tab=readme-ov-file#-%E3%80%A2-features) —then collects authentication cookies and login credentials from various apps and sends them to a server controlled by the attacker. The researchers said the malicious repo “performs a long series of additional malicious activities.” 


I think I’ve referenced this sort of campaign before.  The worry on this stuff is that it’s so incredibly hard for anyone, even Github to be able to tell when this is happening becuase of an attack, versus a community fork or a change in maintainer.  This is at it’s heart a social problem more than a technical one, and that means we’re going to need better social mechanisms to solve it. 


## [Attacking Supply Chains at the Source – O’Reilly ](https://www.oreilly.com/radar/attacking-supply-chains-at-the-source/)

[https://www.oreilly.com/radar/attacking-supply-chains-at-the-source/](https://www.oreilly.com/radar/attacking-supply-chains-at-the-source/)

> Is that the end of the story? The compromised xz Utils was never distributed widely, and never did any damage. However, many people remain on edge, with good reason. Although the attack was discovered in time, it raises a number of important issues that we can’t sweep under the rug:
> 
> * We’re looking at a social engineering attack that achieves its aims by bullying—something that’s all too common in the Open Source world.
> * Unlike most supply chain attacks, which insert malware covertly by slipping it by a maintainer, this attack succeeded in inserting a corrupt maintainer, corrupting the release itself. You can’t go further upstream than that. And it’s [possible that other packages have been compromised](https://openssf.org/blog/2024/04/15/open-source-security-openssf-and-openjs-foundations-issue-alert-for-social-engineering-takeovers-of-open-source-projects/) in the same way.
> * Many in the security community believe that the quality of the malware and the patience of the actors is a sign that they’re working for a government agency.
> * The attack was discovered by someone who wasn’t a security expert. The security community is understandably disturbed that they missed this. 


This was a good summary of the xz utils scenario from Mike, and I think covers some of the biggest worries that came out of it.  Again, this isn’t a purely technical problem, this was a social engineering attack on the social structures that underpin our software.  Those social structures are rarely documented, modelled or paid attention to.  We can run software that validates which libraries are in any given build of our software, but we cannot determine whether the person who wrote the critical code also wrote the safety checker that should validate and check that code. 


## [IAM Is The Worst ](https://matduggan.com/iam-is-the-worst/)

[https://matduggan.com/iam-is-the-worst/](https://matduggan.com/iam-is-the-worst/)

> Imagine your job was to clean a giant office building. You go from floor to floor, opening doors, collecting trash, getting a vacuum out of the cleaning closet and putting it back. It's a normal job and part of that job is someone gives you a key. The key opens every door everywhere. Everyone understands the key is powerful, but they also understand you need to do your job.
> 
> Then your management hears about someone stealing janitor keys. So they take away your universal key and they say "you need to tell Suzie, our security engineer, which keys you need at which time". But the keys don't just unlock one door, some unlock a lot of doors and some desk drawers, some open the vault (imagine this is the Die Hard building), some don't open any doors but instead turn on the coffee machine. Obviously the keys have titles, but the titles mean nothing. Do you need the "executive_floor/admin" key or the "executive_floor/viewer" key?
> 
> But you are a good employee and understand that security is a part of the job. So you dutifully request the keys you think you need, try to do your job, open a new ticket when the key doesn't open a door you want, try it again, it still doesn't open the door you want so then there's another key. Soon your keyring is massive, just a clanging sound as you walk down the hallway. It mostly works, but a lot of the keys open stuff you don't need, which makes you think maybe this entire thing was pointless.
> 
> The company is growing and we need new janitors, but they don't want to give all the new janitors your key ring. So they roll out a new system which says "now the keys can only open doors that we have written down that this key can open, even if it says "executive_floor/admin". The problem is people move offices all the time, so even if the list of what doors that key opened was true when it was issued, it's not true tomorrow. The Security team and HR share a list, but the list sometimes drifts or maybe someone moves offices without telling the right people.
> 
> Soon nobody is really 100% sure what you can or cannot open, including you. Sure someone can audit it and figure it out, but the risk of removing access means you cannot do your job and the office doesn't get cleaned. So practically speaking the longer someone works as a janitor the more doors they can open until eventually they have the same level of access as your original master key even if that wasn't the intent.
> 
> That's IAM (Identity and access management) in cloud providers today. 


This is a wonderful takedown of Identity and Access Management solutions.  One of teh problems of this space is that you are trading off between access permissions being too fine grained, making it increasingly complex to manage, versus being too granular and creating security holes.  

Humans really struggle with more than a couple of concepts in a category.  My instinct is that this probably related to [Dunbars number](https://en.wikipedia.org/wiki/Dunbar%27s_number) which suggests that we can handle certain groups of fidelity (normally in social groups), so a small group of 5-7, a medium group of 30-50, a large group up to about 150 or so.  When we ask people to think about concepts such as classifications, access control lists or anything where you select from groups, humans generally start to feel overwhelmed and confused above the 5-7 group size.  If there are too many options to select from, then we cannot make rational choices.

On the other hand, computers are far better at handling millions of combinations of metadata.  

This fundementally is the problem that faces zero-trust approaches.  A good access control model should be able to take into account hundreds of access controls, meta data properties and information to make decisions of whether to grant access.  But humans who have to use the system, and critically define the policies will always struggle to map the world into such complex decision matrices and will become overwhelmed quickly 


## [maximzubarev.com/why-ai-is-failing-at-giving-good-advice ](https://maximzubarev.com/why-ai-is-failing-at-giving-good-advice)

[https://maximzubarev.com/why-ai-is-failing-at-giving-good-advice](https://maximzubarev.com/why-ai-is-failing-at-giving-good-advice)

> **TLDR: ChatGPT generates responses based on the highest mathematical probabilities derived from existing texts on the internet. Popular advice (for various reasons) is seldomly good, nor (by definition) uniquely applicable, nor (mostly) founded on actual experience. You are probably better off taking advice from a real person who can empathize and knows what they are talking about.** […]
> 
> At the current state of the internet, there is almost any educational information and advice already out there in some form, freely accessible to everybody, more than anyone could ever take action on in their lifetime. Today, the value of providing information is about more than just delivering it; it's about delivering the right information to the right people the right way. And LLMs fail at the former. 


There’s some slightly misunderstanding about how LLM’s actually work here, in that they are a bit more complex in generating their vectors than just a simple substitution of words for numbers.   The more moden LLM’s have models that are clearly disambiguating concepts based on combinations of words, meaning that they can disambiguate economic cost from financial cost, and normally define how likely words and word combinations are with that concept.

But that aside, this is accurate in the problem that LLM’s are trained mostly of freely available information, and the most popular advice and information is actually generally pretty poor advice.  The issue here is that people fail to give enough context to get good advice, as well as the content pumping strategies of the last few decades that has generated huge swathes of internet content that is incredibly low value to humanity, but designed to capture search terms and sell ads.

I think this is getting better fast, but it will still be a while before large language models are any good at giving helpful useful advice rather than repackaged generic advice 


## [FTC says Amazon executives destroyed potential evidence by using apps like Signal - The Verge ](https://www.theverge.com/2024/4/26/24141801/ftc-amazon-antitrust-signal-ephemeral-messaging-evidence)

[https://www.theverge.com/2024/4/26/24141801/ftc-amazon-antitrust-signal-ephemeral-messaging-evidence](https://www.theverge.com/2024/4/26/24141801/ftc-amazon-antitrust-signal-ephemeral-messaging-evidence)

> Now, [_The Washington Post_](https://www.washingtonpost.com/technology/2024/04/26/amazon-ftc-messages-deleted-bezos/) (which is owned by Amazon founder and former CEO Jeff Bezos) reports that Amazon is just one of several companies recently accused of turning to encrypted messaging apps like Signal that can permanently erase messages automatically.
> 
> You may recall the government making similar arguments [about Sam Bankman-Fried’s use of Signal](https://www.theverge.com/2023/10/26/23934195/sam-bankman-fried-self-testimony-deleted-signal) during his trial for fraud and [how that verdict eventually shook out](https://www.theverge.com/23894366/ftx-sam-bankman-fried-trial-updates-news) . Deleted chats were also a sticking point for [at least one juror](https://www.theverge.com/2023/12/12/23999333/epic-juror-confirms-googles-deleted-chats-were-a-factor-in-the-verdict) in Google’s recent courtroom [loss to Epic Games](https://www.theverge.com/24003500/epic-v-google-loss-apple-win-fortnite-trial-monopoly) and came up in [the DOJ’s antitrust trial against Google](https://www.theverge.com/2023/10/30/23939043/us-v-google-sundar-pichai-testimony) .
> 
> This week’s filing includes screenshots of a Signal chat between two Amazon executives who said, “Are you feeling encrypted?” and proceeded to turn on disappearing messages. 


Another example of how everyday use just isn’t reflected in the way that most people in organisations, especially those with fiducary duties, actually work.

I’ve argued before, that from a purist security perspective, given that your device could be hacked and compromised, self-deleting messages reduces the amount of information that gets leaked during a hack.  That’s a nice feature of them, and if I’ve got executives talking to each other about sensitive company details, as CISO I probably want them to have disappearing messages on.  However from a governance, accountibility and record keeping perspective, that’s the worst thing to do.

The right middle ground is either one that requires users to copy infomraiton to the corporate record when needed, but that requires users to take proactive action.  Alternately, there’s an increasing number of tools out there that can either run on the device to copy messages out, or act as a visible secretry account in group chats, that can take copies of messages, and then store them in the corporate store.  The downside to that of course, is that you need to trust that secretary and corporate store to keep all those messages secure. 


## [Deepfakes in the courtroom: US judicial panel debates new AI evidence rules | Ars Technica ](https://arstechnica.com/information-technology/2024/04/deepfakes-in-the-courtroom-us-judicial-panel-debates-new-ai-evidence-rules/)

[https://arstechnica.com/information-technology/2024/04/deepfakes-in-the-courtroom-us-judicial-panel-debates-new-ai-evidence-rules/](https://arstechnica.com/information-technology/2024/04/deepfakes-in-the-courtroom-us-judicial-panel-debates-new-ai-evidence-rules/)

> During Friday's three-hour hearing, the panel wrestled with the question of whether existing rules, which predate the rise of generative AI, are sufficient to ensure the reliability and authenticity of evidence presented in court.
> 
> Some judges on the panel, such as US Circuit Judge Richard Sullivan and US District Judge Valerie Caproni, reportedly expressed skepticism about the urgency of the issue, noting that there have been few instances so far of judges being asked to exclude AI-generated evidence.
> 
> "I'm not sure that this is the crisis that it's been painted as, and I'm not sure that judges don't have the tools already to deal with this," said Judge Sullivan, as quoted by Reuters.
> 
> Last year, Chief US Supreme Court Justice John Roberts [acknowledged](https://www.reuters.com/legal/us-supreme-courts-roberts-urges-caution-ai-reshapes-legal-field-2023-12-31/) the potential benefits of AI for litigants and judges, while emphasizing the need for the judiciary to consider its proper uses in litigation. US District Judge Patrick Schiltz, the evidence committee's chair, said that determining how the judiciary can best react to AI is one of Roberts' priorities. 


This is going to be one to watch.  I think that there will be a looming crisis over the authenticity of digital evidence and the lack of easy ability to identify and disambiguate altered or generated content from real content, but legal circles move slowly, and it will take some time to build.  This is going to be an example of a rising tide of individual cases rather than an overwhelming rush all of a sudden.

It’ll be interesting to see how the US legal system starts to handle this, as individual cases come through, get appealed and rise up through the legal system 


## [Addis Ababa Ethiopia Metro's Decline Shows China's Step Back From Africa - Bloomberg ](https://www.bloomberg.com/news/articles/2024-04-12/addis-ababa-ethiopia-metro-s-decline-shows-china-s-step-back-from-africa)

[https://www.bloomberg.com/news/articles/2024-04-12/addis-ababa-ethiopia-metro-s-decline-shows-china-s-step-back-from-africa](https://www.bloomberg.com/news/articles/2024-04-12/addis-ababa-ethiopia-metro-s-decline-shows-china-s-step-back-from-africa)

> Almost a decade ago, the light-rail system in Ethiopia’s bustling capital of Addis Ababa was [hailed as a revolutionary solution](https://www.bloomberg.com/news/articles/2015-09-21/modernizing-ethiopia-opens-475-million-china-built-urban-rail) to the city’s transportation woes. Envisioned as a project that would redefine urban transport, the system promised to sweep up to 60,000 passengers per hour along its tracks.
> 
> Today it sits as a daily reminder of the broken promises of [China-funded infrastructure investments that swept Africa in recent years](https://www.bloomberg.com/news/features/2019-07-19/china-s-belt-and-road-leaves-kenya-with-a-railroad-to-nowhere) . Frequent breakdowns, inadequate maintenance funding and operational constraints mean barely one-third of its 41 trains are operational, ferrying 55,000 passengers a day, a fraction of initial projections.
> 
> […]
> 
> Key hurdles include frequent power outages, inadequate local maintenance facilities, limited availability of spare parts, and challenges in accessing foreign currency for importing spare parts from China, says Mitiku Asmare, head of the city’s transport agency.
> 
> The greatest concern is the project’s inability to repay its debt, resorting to local bank loans to stay afloat. And running the system below capacity means revenue is insufficient to cover future payments.
> 
> The project may have prioritized short-term political goals over long-term operational sustainability, says Frangton Chiyemura, a lecturer in Global Development at the UK Open University’s Development Policy and Practice Group who studies China-Africa relations and Chinese-funded projects in Africa.
> 
> The project’s original sin was poor planning, with insufficient arrangements in place to cover needs including maintenance work, spare parts, and the required local skills to sustainably run the project, Chiyemura said. He cited a standard-gauge, China-backed railway in Nigeria as an analogue to the Ethiopian metro, saddling the government with infrastructure and its associated maintenance costs. 


This was a nice reminder that developing a programme to build something, without considering the ongoing operational cost, the ongoing maintenance and the senior leadership will to invest in it is not just a problem facing secuirty or technology leaders, but one that faces governments, corporations and organisations of all shapes and sizes, all the way up to multi-billion dollar infrastructure investment programmes.

Investing in the long term maintenance of infrastructure is a common theme and it’s always worth remembering when you see systems, services and products that speed up build time for you and your teams.  Investing in things that make it easier and cheaper to maintain almost always pays off more in the long run, and anything that gives you speed of deliverability for a higher maintenance cost is something that should only be done as an urgent quick fix, knowing you’ll want to undo it later 


