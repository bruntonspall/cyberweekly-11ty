---
title: "257 - Focusing on the right things"
date: 2025-03-23
description: I was taken over the last few weeks at how often we focus on the wrong things.  The things that are exciting, interesting and appear in the media are often vastly disproportionate to the actual impact on the business.
---

Welcome to a new CyberWeekly, and for those of you reading on the web, a new website and publishing system.

I wrote the original cyberweekly website in python about five years back,  because I wanted to keep all the links that I was bookmarking somewhere.  I built it on top of Google's App Engine, their document database, and overall it's cost me less than a dollar a month to run.  But the python was incredibly janky, and I kept looking at the code and wanting to add features for reordering the links, for detecting duplicate notes, and I'd noted that I didn't have the right caching policy in place, meaning that increasing crawlers were costing me money.

Talking with a few people, I realised that the my backend editing and link management concerns were far better separated from the website itself, and that what I really could do with was a static site generator.  Having just done something with eleventy for [the Advent Of Code](https://adventofcode.com/), I decided to pull down all of my old editions, convert them into proper markdown, and generate a site around it.  The looks still aren't perfect, but there's now an [RSS feed](https://cyberweekly.net/feed.xml) for those of you who like such things, and all of the original content is stored in plain markdown in github.

Anyway, that's distracted me for a few weeks, and this is the first I've written entirely in markdown from scratch.

I was taken over the last few weeks at how often we focus on the wrong things.  The things that are exciting, interesting and appear in the media are often vastly disproportionate to the actual impact on the business.

We get taken in that we should scan our systems and create thousands of vulnerability reports, that we should fix anything with a specific CVSS rating higher than a threshold, that the biggest threat to our organisations is shady state directed groups who will absail down the side of our buildings to plug in a USB stick to our servers.

In reality, the world is far more mundane, boring and difficult to work in.  Some vulnerabilities might be severe but they may not be remotely accessible, others might be simple but they would have an outsized impact on our business.  We're more at risk from phishing emails sent to tens of thousands of recipients than a team with photos and bios of the entire security team.

Doing something about the mundane requires us to delegate authority into teams who understand the local risk, enabling them to make decisions, to patch or not patch.  It means informing everyone about our strategy, our priorities, and it means sticking to those and avoiding the noise when the press gets excited about the latest 9.8 CVSS vulnerability.

It can also mean focusing on the things that matter, and picking the top 5 to work on, and finishing that work before moving on.  We know that we all have vulnerabilities in the system, but doing very little about all of them is worse than systemically moving through fixing them one at a time.

Teams that empowered, enabled and self-directing are often far more productive, far more capable.  If you have teams like that, then giving them the right strategic direction and getting out of their way is best way to ensure everything gets a little better, inch by inch, day by day.


## [ State of Cloud Remediation 2025 | Tamnoon ](https://tamnoon.io/state-of-cloud-remediation/)

[https://tamnoon.io/state-of-cloud-remediation/](url)

>  Today’s engineers are so far removed from the actual infrastructure, and that infrastructure has grown so complex and virtual, that “getting your hands dirty” to fix a problem is much harder than it once was.
> 
> To solve that problem, we adopted tools that promised to “handle compliance” for our clouds. These tools evolved into CSPMs and later into CNAPPs—platforms expected to pinpoint exactly what needs fixing.
> 
> We invested in this shiny new platform that delivers more alerts, more data, and more… well, everything. Yet, in practice, the CNAPPs proved almost too good at their job––they’ve become so effective at detecting issues that they’re finding more vulnerabilities than most security teams can realistically address, no matter how skilled or well-staffed. Meanwhile, security hasn’t gotten any easier over the years—threat models have evolved, new technologies and use cases demand attention, and breaches continue to happen year after year.
> 
> […]
> 
> If you’re building anything in the cloud, it’s likely that somewhere along the road you will configure something that could be construed as dangerous, or use a few pieces of infrastructure that will inevitably have vulnerabilities found in them.
> 
> Cloud security is not about eliminating all risk—it’s about managing the risk that you have effectively and making informed decisions between business goals and that risk. It turns out that in cloud security, despite state-of-the-art CNAPPs and 10+ years of technological advancements, we remain very much behind where we need to be in securing our cloud environments.
> 
> […] 
> 
> You can clearly see that our exposure time to these misconfigurations is measured in months, not days. Even for critical alerts, the  **average MTTR remains extremely high at 128 days**  ––or over 4 months of exposure. 

 I thought this was interesting because of the amount of burden that we create when we ”shift-left”.

It’s easy to say “stick a scanner on it, and let that create alerts”, but someone has to fix the alerts, they have to take action on the alert.  Fixing those is vastly more complex than finding them.

The best way to remediate a lot of this is not to create insecure environments in the first place, but as set out in here, sometimes you actively want a public exposed storage bucket, or an ingress route with exposed ports.  Making that both a conscious choice, but also documenting that decision can help, but as each cloud scanning tool is different, we don’t have good standardised mechanisms for doing this yet. 

## [ Cybercrime: A Multifaceted National Security Threat | Google Cloud Blog ](https://cloud.google.com/blog/topics/threat-intelligence/cybercrime-multifaceted-national-security-threat)

[https://cloud.google.com/blog/topics/threat-intelligence/cybercrime-multifaceted-national-security-threat](url)

>  Cybercrime makes up a majority of the malicious activity online and occupies the majority of defenders' resources. In 2024, Mandiant Consulting responded to almost four times more intrusions conducted by financially motivated actors than state-backed intrusions. Despite this overwhelming volume, cybercrime receives much less attention from national security practitioners than the threat from state-backed groups. While the threat from state-backed hacking is rightly understood to be severe, it should not be evaluated in isolation from financially motivated intrusions.
> 
> A hospital disrupted by a state-backed group using a wiper and a hospital disrupted by a financially motivated group using ransomware have the same impact on patient care. Likewise, sensitive data stolen from an organization and posted on a data leak site can be exploited by an adversary in the same way data exfiltrated in an espionage operation can be. These examples are particularly salient today, as criminals increasingly target and leak data from hospitals. Healthcare's share of posts on data leak sites has doubled over the past three years, even as the number of data leak sites tracked by Google Threat Intelligence Group has increased by nearly 50% year over year. The impact of these attacks mean that they must be taken seriously as a national security threat, no matter the motivation of the actors behind it. 

 This is a great report, with a lot of detail on crime groups operating on the internet today, and I think, while the report makes a big deal of talking to Governments and National Security Professionals, it’s a good reminder to everyone that while the “Advanced Persistent Threats” or nation state groups often get all the headlines, the threat from crime groups is the biggest one facing most organisations today.

Your cybersecurity strategy should consider the number one threat to be these groups, who almost certainly don’t know or care who you are before they breach you, to be the actor most likely to conduct an operation against you.  That means focusing on your most vulnerable external interfaces, ensuring that you have patching or vulnerability management regimes and concentrating your asset discovery on yourself.  You don’t want those attackers to know your attack surface better than you do. 

## [ Storm-2372 conducts device code phishing campaign | Microsoft Security Blog ](https://www.microsoft.com/en-us/security/blog/2025/02/13/storm-2372-conducts-device-code-phishing-campaign/)

[https://www.microsoft.com/en-us/security/blog/2025/02/13/storm-2372-conducts-device-code-phishing-campaign/](url)

>  Storm-2372’s targets during this time have included government, non-governmental organizations (NGOs), information technology (IT) services and technology, defense, telecommunications, health, higher education, and energy/oil and gas in Europe, North America, Africa, and the Middle East. Microsoft assesses with medium confidence that Storm-2372 aligns with Russian interests, victimology, and tradecraft.
> 
> In device code phishing, threat actors exploit the device code authentication flow to capture authentication tokens, which they then use to access target accounts, and further gain access to data and other services that the compromised account has access to. This technique could enable persistent access as long as the tokens remain valid, making this attack technique attractive to threat actors.
> 
> The phishing attack identified in this blog masquerades as Microsoft Teams meeting invitations delivered through email. When targets click the meeting invitation, they are prompted to authenticate using a threat actor-generated device code. The actor then receives the valid access token from the user interaction, stealing the authenticated session. 

 This is a good reminder that MFA isn’t automatically phishing proof.  If someone can get you to try to authenticate using your MFA, they have a short window to intercept and use that authentication token as you instead.

Phishing proof MFA is harder to deploy, we’re mostly talking hardware based MFA tokens in a lot of cases.  But it normally uses some form of public key cryptography to ensure that it only generates a valid MFA token for the original site, and wont provide the same token to phishing sites.

If you’ve not managed to roll out MFA yet, jumping straight to phishing proof MFA such as passkeys or FIDO tokens may well be a more secure option, even if they’re less mature than TOTP authentication or user prompt authentication. 

## [ Signals of Trouble: Multiple Russia-Aligned Threat Actors Actively Targeting Signal Messenger | Google Cloud Blog ](https://cloud.google.com/blog/topics/threat-intelligence/russia-targeting-signal-messenger)

[https://cloud.google.com/blog/topics/threat-intelligence/russia-targeting-signal-messenger](url)

>  Google Threat Intelligence Group (GTIG) has observed increasing efforts from several Russia state-aligned threat actors to compromise Signal Messenger accounts used by individuals of interest to Russia's intelligence services. While this emerging operational interest has likely been sparked by wartime demands to gain access to sensitive government and military communications in the context of Russia's re-invasion of Ukraine, we anticipate the tactics and methods used to target Signal will grow in prevalence in the near-term and proliferate to additional threat actors and regions outside the Ukrainian theater of war.
> 
> […]
> 
> The most novel and widely used technique underpinning Russian-aligned attempts to compromise Signal accounts is the abuse of the app's legitimate "  [linked devices](https://support.signal.org/hc/en-us/articles/360007320551-Linked-Devices)  " feature that enables Signal to be used on multiple devices concurrently. Because linking an additional device typically requires scanning a quick-response (QR) code, threat actors have resorted to crafting malicious QR codes that, when scanned, will link a victim's account to an actor-controlled Signal instance. 

 This is the same attack vector we saw against Whatsapp recently as well.

This isn’t so much attacking the tool, as causing the user to misconfigure the tool to make use of a legitimate feature.

Users want to link their whatsapp, signal and other instant messenger systems to their desktop, so they can read and respond to messages without needing to get their phone out constantly.  But any ability to use this feature can also be misused by bad actors.

Since the tool sends the messages back out from the legitimate device, this goes around any encryption you have in the app, bypassing all end to end encryption capabilities.  It’s very similar to the old tactic of putting an auto-forwarding rule on your email inbox, meaning that they get a copy of every incoming email.

Keep an eye out, educate staff not to scan codes relating to whatsapp/signal without checking with someone, and maybe show people how to check the list of devices with access so they can check and make sure it’s not happened before. 

## [ Ransomware The True Cost to Business 2024 | Report ](https://www.cybereason.com/ransomware-the-true-cost-to-business-2024)

[https://www.cybereason.com/ransomware-the-true-cost-to-business-2024](url)

>  Key Highlights:
> 
> * 56% didn’t detect a breach for 3-12 months.
> * 84% paid the ransom. But 78% were then breached again, and 63% of these were asked to pay even more the second time. 

 I was re-reading this the other day and I was reminded of this key figure around ransomware actors.  around 4/5ths of organisations that paid a ransom to a ransomware actor were breached again, most of those within the next year, and a third of them by the same actor.

Many say they paid out of an inability to make any other decision, they feared the business impact of not paying.  But it’s clear that the impact of paying is that you are likely to suffer another breach.

Cyberreason don’t seem to have published the statistics for the counterfactuals, so we don’t know how many of the ones who didn’t pay were breached again.  But it’s clear that paying does not lead to better outcomes. 

## [ CISA: More than 300 critical infrastructure orgs attacked by Medusa ransomware | The Record from Recorded Future News ](https://therecord.media/medusa-ransomware-targeting-critical-infrastructure-orgs)

[https://therecord.media/medusa-ransomware-targeting-critical-infrastructure-orgs](url)

>  Medusa — which the FBI said is not the same as the MedusaLocker variant and the Medusa mobile malware variant — initially started as a closed group operated by developers and hackers before expanding to an affiliate model. Ransom negotiations are still controlled by the ransomware gang’s developers but they typically “recruit initial access brokers (IABs) in cybercriminal forums and marketplaces to obtain initial access to potential victims.”
> 
> “Potential payments between $100 USD and $1 million USD are offered to these affiliates with the opportunity to work exclusively for Medusa,” the agencies  [said](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)  .
> 
> The Medusa ransom note orders victims to contact them within 48 hours. If there is no response, the hackers contact them by phone or email. The gang’s leak site advertises stolen data and offers it to anyone for a price. 
> 
> “FBI investigations identified that after paying the ransom, one victim was contacted by a separate Medusa actor who claimed the negotiator had stolen the ransom amount already paid and requested half of the payment be made again to provide the ‘true decryptor’ — potentially indicating a triple extortion scheme,” the advisory said. 

 The  [advisory itself](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)  has a number of indicators of compromise that you can deploy to detect this.

I was more interested in this little tidbit here about the use of Initial Access Brokers, and the affiliates in essence running away with the ransom.  As I’ve said before, one of the hardest things about dealing with criminals is that, well, they’re criminals and often not terribly trustworthy.

This is yet another reminder that paying ransoms not only funds criminal enterprises, but isn’t likely to actually get your data back or give you any comfort that it wont be sold on elsewhere. 

## [ (34) AI Revolution, Meet the Credibility Revolution ](https://geekway.substack.com/p/ai-revolution-meet-the-credibility)

[https://geekway.substack.com/p/ai-revolution-meet-the-credibility](url)

>  So much for that assumption. As a group, the engineers who started using GenAI when it became available were very different from the ones who didn't. To make matters worse, the two groups were different in exactly the area that we care about: productivity. On average, the engineers who reached for the newly available GenAI were doing significantly more PRs and merges than those who didn't before GenAI appeared on the scene.
> 
> Why were these engineers more productive? And why were they more likely to start using GenAI — why did they  _self-select_  into using the snazzy new technology? We don't know yet. These are interesting and important questions, and we want to investigate them. At this point all we know with confidence is that the GenAI-using engineers were more productive both before and after GenAI showed up.
> 
> […]
> 
> But all is not lost, and the situation is not hopeless. We have tools to disentangle selection and treatment effects. One that’s used a lot in modern econometrics is the  _counterfactual_  — A statistical what-if scenario that lets us compare what actually happened to an alternative. I think of counterfactuals as nearby parallel universes where things are only slightly different. 
> 
> In this case, the parallel universe we want to peer into is one where everything is exactly the same as in this one,  _except that our customer never adopts GenAI_  . We're going to gather the identical data in that universe that we did in this one and compare the two datasets. We're especially interested in the performance of the GenAI-adopting engineers in that other universe vs. in this one.
> 
> […]
> 
> Selection effects, self-selection, treatment effects, counterfactuals, and confidence intervals: we've already made a good start on understanding the vocabulary of the “  [credibility revolution](https://www.aeaweb.org/articles?id=10.1257%2Fjep.24.2.3)  ” in economics. This movement, which started in the late 20th century and blossomed in the 21st, is a big deal - big enough to have merited two batches of Nobel Prizes in recent years.  [6](https://geekway.substack.com/p/ai-revolution-meet-the-credibility#footnote-6-158513758)  The credibility revolution is a sea change in our ability to understand causality. It's a big bag of research designs and statistical methods that when judiciously applied lets us make confident statements about what caused what.
> 
> […]
> 
> Over the past year, I've asked lots of executives at lots of companies if they've ever heard of the credibility revolution. The only "yes" I've received wasn't a surprise, since it came from a CEO who I knew had a Ph.D. in economics. My straw poll indicates that the Credibility Revolution hasn't yet made it from economics to the enterprise. Which opens up a huge opportunity.
> 
> Every ROI analysis is an exercise in causal inference. It's an attempt to determine the changes caused by an investment. But today, most companies’ ROI analyses don’t use the tools of the credibility revolution; they instead rely on simple aggregates, averages, and comparisons. 

 I really like this analysis, which uses a far more statistically thorough set of measures to demonstrate that AI has a small uplift in productivity.

But critically, because it accounts for causal relationships, we can also specify a condition on that uplift, one that rings true to the DORA research in DevOps a few years back.   AI produces a small but significant uplift in productivity in teams that are already highly productive.

Quite why teams that are highly productive are more likely to pick up AI tools is also an interesting question.  I’d argue that it’s not causal, it’s not because they are highly productive, but my hypothesis is that one of the environmental factors that causes them to be highly productive is an ability to choose and select their tools along with a freedom to try new things. This ability to to choose and select their tools results in them using a wider variety of tools, which will include AI tools is critical to getting adoption rates up. 

## [ (34) 🔮 The Sunday edition #516: Abundance; DeepSeek’s power; Copyright & AI; Nvidia, BYD ftw; China's AI education ++ ](https://www.exponentialview.co/p/ev-516)

[https://www.exponentialview.co/p/ev-516](url)

>  DeepSeek seems to have managed to create a research environment where the lab can out-innovate more heavily financed competitors. It only has160 employees, compared to over 2,000 at OpenAI and it is  [unburdened](https://www.ft.com/content/fb5c11bb-1d4b-465f-8283-451a19a3d425)  by the strict commercial or investor pressures that typically demand rapid productization. DeepSeek’s billionaire founder, Liang Wenfeng, bought thousands of high-end chips ahead of export restrictions and deliberately limits commercial activities. He’s content with breaking even rather than chasing growth. 
> 
> Meanwhile, OpenAI has pivoted  [towards product](https://www.theatlantic.com/technology/archive/2023/11/sam-altman-open-ai-chatgpt-chaos/676050/)  , as it hunts for a defensible moat and profitable market position. And the pressures are growing… Open-source may be the foundational kernel of building AI services. After all, the very successful Mac operating system is building on the open-source Linux kernel. And if that wasn’t enough, there’s the reality of  [end-to-end reinforcement learning](https://www.exponentialview.co/p/the-age-of-reasoning-models)  blurring  [the boundary between model and the product](https://vintagedata.org/blog/posts/model-is-the-product)  – the model is the product. 

 What an interesting analysis between the difference between the western, typically American, system of venture capitalism that seeks growth at almost all costs, against the Chinese/DeepSeek model of limiting resources and seeking break even and profitability instead.

Deepseek is an outlier here, this isn’t necessarily the typical model that other Chinese firms have gone down, but this battle between, what is in essence, Silicon Valley and Hangzhou, between OpenAI and Deepseek is demonstrating different ways of approaching the same problem, with different markets, different product fits and different constraints.  

It’s a good reminder to the endless questions of “Why don’t we have a silicon valley model in [France/UK/Europe/India]” is often misrepresenting just how much that model is predicated on the cultural norms that surround it 

## [ How to make any AMD Zen CPU always generate 4 from RDRAND • The Register ](https://www.theregister.com/2025/02/04/google_amd_microcode/)

[https://www.theregister.com/2025/02/04/google_amd_microcode/](url)

>  Well, the boffins at Google have discovered a way to craft their own microcode that is accepted by AMD processors and successfully changes the silicon's operation. They say their technique works on all Zen-based AMD chips – all Ryzen and Epyc parts, basically.
> 
> […]
> 
> To back up these claims, the Googlers this week released  [initial details](https://github.com/google/security-research/security/advisories/GHSA-4xq7-4mgh-gp6w)  of their findings, and a proof-of-concept microcode update for Milan-family Epyc server chips and Phoenix-family Ryzen 9 desktop processors. This  [demo microcode](https://github.com/google/security-research/tree/master/pocs/cpus/entrysign)  forces a chip's read random (  [RDRAND](https://www.felixcloutier.com/x86/rdrand)  ) instruction to always output the value 4 rather than an actual random number, likely a reference to  [XKCD](https://xkcd.com/221/)  .
> 
> […]
> 
> Crucially, you need to kernel-level, ring-0 access on a system to load the microcode, so this can only be used once you have sufficient privileges. This makes this technique more useful for those customizing their own systems, or for privileged malware that really wants to deeply compromise an infected computer.
> 
> But consider a scenario where you're running a virtual machine on a remote host that you may not fully trust, so you rely on AMD's secure encrypted virtualization to  [shield your VM from the host](https://www.amd.com/en/developer/sev.html)  ; now the host can use Google's approach to load microcode that undermines or blows away that security. 

 This is  a neatproof of concept, and the call back to XKCD’s comic on random numbers is just a lovely touch.

It’s important to note the limitations here, you need to have fully compromised the ring-0 kernel on the machine to even start this kind of attack, so in modern cloud environments, that means you not only need to escalate privilege within the virtual machine, but you need a VM escape as well, along with privilege escalation in the host.  

But as indicated, the microcode means that you may well be able to remove some of the low level CPU features that provide secure isolation between tenants or workloads on the same machine.

For 99% of us that’s not an issue, and if this sort of attack is in your threat model, you were probably already requesting and using dedicated hardware anyway (hopefully).

Neat and interesting, but well outside most peoples threat model. 

Thanks for reading

Michael