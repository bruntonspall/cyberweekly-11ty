---
title: "243 - What is enterprise security compared to product security?"
date: 2024-03-24
description: "Some weeks I read a blogpost that just perfectly encapsulates a bunch of my own thoughts and things really crystalise together.  This week was one of those for me."
permalink: /what-is-enterprise-security/
---

Some weeks I read a blogpost that just perfectly encapsulates a bunch of my own thoughts and things really crystalise together.  This week was one of those for me.

I've spent a far long time than I care to count building, scaling and deploying systems from within large organisations.  When we do that we think about the security of the product we are building, and sometimes about the security of our process for building the product and services.

But lots of the conversations that we have about security dont necessarily cover the same set of concerns that we have in product development.  Lots of them overlap, so we spent time thinking about how our users authenticate to our systems, whether they have MFA enabled, and how we might attest to their device security.

The blogpost by Michal Zalewski that articulates there's a difference between "enterprise security" and "product security" really hit the nail on the head for me.  A lot of cybersecurity advice doesn't articulate which of these two models it's talking about, and that creates confusion and problems for applying that advice.

I also think that we can divide enterprise security into two distinct areas.  The governance of enterprise security and the implementation of enterprise security.  The things we care about in terms of risk management, setting policies, governing changes and so on are all a different category of concerns from the actual enterprise implementation of our device policies, user account policies and so on.

As we read through about how red teams operate, what the threat is in the world, and how technology is changing, it's worth having a think about what model of security is being talked about and making sure you are taking the right advice in the right place.

## [Product security: barking up the wrong tree ](https://lcamtuf.substack.com/p/product-security-barking-up-the-wrong?utm_medium=referral)

[https://lcamtuf.substack.com/p/product-security-barking-up-the-wrong?utm_medium=referral](https://lcamtuf.substack.com/p/product-security-barking-up-the-wrong?utm_medium=referral)

> Having been in the trenches, I think that the industry’s approach to product security is broadly sensible. We don’t know how to write bug-free code, but where it matters, major vendors make considerable investments to keep the products robust. Thanks to hardened frameworks, code audits, fuzzing, and sandboxing, key software — such as browsers and operating systems — has gotten quite difficult to attack. When bugs slip through the cracks, automated updates rapidly shield most customers from harm. It’s true that the security of smart lightbulbs and toothbrushes isn’t great — but serious attack scenarios are hard to dream up. I also concede that special considerations exist for certain niche industries; these need to have standards of their own.
> 
> In contrast, my view of enterprise security isn’t nearly as optimistic. The purported basics — meaningful asset inventories, privilege reduction, comprehensive access control — are unsolved problems. It doesn’t matter how much you care: there’s no product or policy that lets you address these challenges at scale.
> 
> To illustrate, consider that even the most robust asset inventory scheme can be thwarted by a single employee who, for the sake of expediency, puts a bootleg AWS instance on a corporate credit card and does some prototyping there.
> 
> […]
> 
> The most successful security programs I've seen are not built around the idea of having perfect defenses. They’re built around the assumption that you’re going to get compromised — and that you need to detect it, respond to it, and contain it faster than the attackers can achieve their goals. But even if you build a corporate panopticon, detection still isn’t a walk in the park — and the attackers are adapting by speeding up their tactics too.
> 
> In the end, product security is a red herring; it’s enterprise security that urgently needs a paradigm shift. 


I really like this articulation.  We intermingle product security and enterprise security at our own risk.  As is set out, doing good product security is hard but managable.  However doing good enterprise security feels like one of the “Wicked Problems” that is almost irreducably hard.

What helps here is admitting we have a problem and trying to work out how we can shift our thinking to better set ourselves up for success 


## [Trust but test: Vendor security testing at Canva - Canva Engineering Blog ](https://www.canva.dev/blog/engineering/trust-but-test/)

[https://www.canva.dev/blog/engineering/trust-but-test/](https://www.canva.dev/blog/engineering/trust-but-test/)

> Like all companies, Canva uses vendors to help achieve our goals, and when choosing our vendors, we need to ensure they reach our high-security standards. These vendors can range from the cloud infrastructure Canva runs on to the software libraries we use in our products. It’s all-encompassing, and as the interconnectedness of software increases, the risk of a single point of failure grows, as evidenced by the amount of supply chain breaches over the past few years. We want to create an ecosystem of trusted, _tested_ vendors to ensure Canva remains a secure and hardened product for even our most security-conscious customers.
> 
> […]
> 
> Most vendors we work with leave long-lasting positive interactions, regardless of the security review results, and become a valued part of Canva. Ultimately, however, we still help Canva make an informed business decision about vendor security. We’ve had a small number of cases where a vendor's security posture was not up to Canva's standards, and we decided to walk away from engagements with them. 


This is an interesting model and one I think I quite like, although I imagine that vendors want something repeatable so tehy can do it once rather than once for every customer.

But what’s critical is this bit hidden in the middle.  If you are a vendor of software, then how you react to reports of vulnerabilities is a critical part of your sales process.  Having a bad vulnerability reporting process that dismisses or minimises the security implications will cost you sales, and increasingly so in the current climate.

Investing in a positive and capable security response capability will improve your reputation, and thus increase sales (and hopefully profitability) 


## [Are We Helping? ](https://jackson-t.com/are-we-helping/)

[https://jackson-t.com/are-we-helping/](https://jackson-t.com/are-we-helping/)

> When I [released](https://twitter.com/Jackson_T/status/1204648426329145349) SysWhispers in 2019, I genuinely thought the direct syscalls technique was a critical ingredient for EDR evasion. With hindsight, it is clear to me that my understanding of defensive sensors was immature. Perhaps like others who release offensive security tools, I had no incentive to seek nuance because of: (1) the direct social reward of hundreds of likes, stars, and re-tweets well past [Dunbar’s number](https://en.wikipedia.org/wiki/Dunbar%27s_number) , and (2) the indirect financial reward that undeniably came from the popularity of this tool’s release (i.e. better job prospects). I still haven’t had the opportunity to use it on an engagement so my empirical sense of its efficacy came only from the anecdotal feedback of others.
> 
> What I gather from that experience and from discussions with red team peers is that the conventional wisdom for evading AV/EDR is to: (1) devise a bag of tricks (direct syscalls, unhooking, digital signatures, packers, obfuscators, encryptors, adding strings, AMSI patching, etc.), (2) duct tape together as many of them as you can, and (3) have some anecdotally-driven faith that it will work.
> 
> This is fine if their tactical purpose is to get some quick wins to keep the engagement going. But if their marketed purpose paints the impression that an elite team of ethical hackers will help defenders be resilient against determined adversaries who leave little to chance… Well, allow me to say that it is increasingly hard for me to imagine those actors struggling with evading defensive vendor products _in the manner_ most commercial red teams do.
> 
> […]
> 
> Threat hunters and detection engineers working for customer-obsessed vendors have an easier time justifying their work when responding to customer complaints of undetected red team activity, and a relatively harder time justifying the detection of real world activity that adversaries do not intend to enter customer consciousness. 


This essay sets out the misaligned incentives that our red team/blue team structures creates.  When our blue teams are rewarded not for defending against real adversaries, but performing well against red team testing, and the red teams are rewarded not for simulating real attackers but for demonstrating blue team competence (or lack of it), then we create a nasty feedback system that loses sight of why we are doing any of this 


## [One does not simply implement passkeys – Josh Grossman – Application Security Specialist ](https://joshcgrossman.com/2024/02/08/one-does-not-simply-implement-passkeys/)

[https://joshcgrossman.com/2024/02/08/one-does-not-simply-implement-passkeys/](https://joshcgrossman.com/2024/02/08/one-does-not-simply-implement-passkeys/)

> There is currently a lot of confusing UX around passkeys, even for very basic operations. Different combinations of browsers and devices lead to a variety of different (and sometimes unpredictable) user journeys.
> 
> Creating a passkey on a device (and using it on that device) is relatively slick although the weird UX differences still apply.
> 
> Once you start trying to use an account on multiple devices, the UX really breaks down. Passkeys don’t synchronise where you might expect them to synchronise and the QR code flow that is supposed to work around that appears to be unusable on my device and maybe all OnePlus devices…
> 
> […]
> 
> At pretty much every stage of this experiment, I could have fallen back on to a code being sent to my email address. In some cases, I was forced to fall back on to this. 


I’ve been doing a bit of digging into Passkeys recently as I’ve been asked by a few people “Should I invest in MFA or jump straight to passkeys?” and honestly, I have no idea what the answer is.

This experience report shows up some of the weaknesses of passkeys.  For the key simple flow, returning to the same site on the same device, they seem to work well.  For multi device accounts, especially if you’ve already invested in password managers, then the work flow feels like it can get a lot more confusing very quickly.

There’s also still something at the root of most implementations that has possession of an email address as the core security foundation.  The place I want passkeys most is for access to the email account, and that’s the place that feels one of the hardest to handle device loss or inaccessibility.

I’m not sure that’s strictly worse than either forgetting your password or selecting a known breached password, but it’s definitely not yet at the point where I’d recommend it for enterprise use. 


## [Canary Infra: Bringing Honeypots towards general adoption ](https://tracebit.com/blog/2024/03/canary-infra-bringing-honeypots-into-general-adoption/)

[https://tracebit.com/blog/2024/03/canary-infra-bringing-honeypots-into-general-adoption/](https://tracebit.com/blog/2024/03/canary-infra-bringing-honeypots-into-general-adoption/)

> There are few practices in security that red teamers and penetration testers alike fear more than honeypots. The idea of having to tiptoe around an environment is a jarring prospect for those used to being able to act with relative impunity.
> 
> […]
> 
> But if you speak with security teams you'll find many haven't implemented this approach, why is that? We think the cost/benefit trade off has never quite been there, but we also think that's changing.
> 
> […]
> 
> Historically the word 'honeypots' is associated with a 'late maturity' or even 'never' roadmap item but when the risks and the costs are tiny and the benefits significant it becomes something that could come at the very beginning of a security program, certainly it isn't something that needs to wait until other boxes have been checked. 


I remain an unabashed fan of deception technology such as Honeypots.  I have never quite understood how a defensive technology that is so cheap, so simple and so high signal-to-noise remains unimplemented in so many organisations.

I’ve tried to implement them in a number of locations, and have always run into very odd bureaucratic hurdles that mostly come from misunderstanding what they are, and how they work.

This work should make it far easier for digital teams especially to experiment with canary infrastructure without requiring quite the level of governance and oversight that is needed within corporate infrastructure.  Definitely something I’d prioritise if I had a digital team today. 


## [France Travail data breach impacted 43 Million people - Security Affairs ](https://securityaffairs.com/160556/data-breach/france-travail-data-breach-34m-people.html)

[https://securityaffairs.com/160556/data-breach/france-travail-data-breach-34m-people.html](https://securityaffairs.com/160556/data-breach/france-travail-data-breach-34m-people.html)

> The [investigation](https://www.cybermalveillance.gouv.fr/tous-nos-contenus/actualites/violation-de-donnees-personnelles-france-travail-formulaire-lettre-plainte-202403) conducted by France’s Cybermalveillance cybercrime prevention initiative revealed that threat actors stole the personal information of 43 million people between February 6 and March 5, 2024.
> 
> “The database allegedly extracted illicitly contains the personal identification data of people currently registered, people previously registered over the last 20 years as well as people not registered on the list of job seekers but having a candidate space on [francetravail.fr](http://francetravail.fr/) . It is therefore potentially the personal data of 43 million people which have been infiltrated.” reads the [press release](https://www.francetravail.org/accueil/communiques/2024/france-travail-et-cap-emploi-victimes-dune-cyberattaque.html?type=article) published by France Travail. 


This is one of those terrifying government breaches that you hope never happens.  Citizens generally have no choice but to hand over their personal information to the state, and breaches of major state organs like this sow distrust between the citizen and the state. 


## [2024 Annual Threat Assessment of the U.S. Intelligence Community ](https://www.dni.gov/index.php/newsroom/reports-publications/reports-publications-2024/3787-2024-annual-threat-assessment-of-the-u-s-intelligence-community)

[https://www.dni.gov/index.php/newsroom/reports-publications/reports-publications-2024/3787-2024-annual-threat-assessment-of-the-u-s-intelligence-community](https://www.dni.gov/index.php/newsroom/reports-publications/reports-publications-2024/3787-2024-annual-threat-assessment-of-the-u-s-intelligence-community)

> This report reflects the collective insights of the Intelligence Community, which is committed every day to providing the nuanced, independent, and unvarnished intelligence that policymakers, warfighters, and domestic law enforcement personnel need to protect American lives and America's interests anywhere in the world.
> 
> […]
> 
> New technologies—particularly in the fields of AI and biotechnology—are being developed and are
> proliferating at a rate that makes it challenging for companies and governments to shape norms regarding
> civil liberties, privacy, and ethics. The convergence of these emerging technologies is likely to create
> breakthroughs, which could lead to the rapid development of asymmetric threats—such as advanced
> UAVs—to U.S. interests and probably will help shape U.S. economic prosperity.
> 
> […]
> 
> The emergence of inexpensive and anonymizing online infrastructure combined with the
> growing profitability of ransomware has led to the proliferation, decentralization, and
> specialization of cyber criminal activity. This interconnected system has improved the
> efficiency and sophistication of ransomware attacks while also lowering the technical bar for
> entry for new actors.
> 
> Transnational organized criminals sometimes cease operations temporarily in response to
> high-profile attention, law enforcement action, or disruption of infrastructure, although group
> members also find ways to rebrand, reconstitute, or renew their activities. 


This is always a really interesting read, as it sets out the geopolitical environment as the US sees it, and enables us to better understand some of the motive and intent in certain actors decisions.

The slightly depressing reading on ransomware emphasises just how much the spread of capability has meant that even the US intelligence community sees it as an everpresent threat that will remain with us. 


## [Update on Microsoft Actions Following Attack by Nation State Actor Midnight Blizzard | MSRC Blog | Microsoft Security Response Center ](https://msrc.microsoft.com/blog/2024/03/update-on-microsoft-actions-following-attack-by-nation-state-actor-midnight-blizzard/)

[https://msrc.microsoft.com/blog/2024/03/update-on-microsoft-actions-following-attack-by-nation-state-actor-midnight-blizzard/](https://msrc.microsoft.com/blog/2024/03/update-on-microsoft-actions-following-attack-by-nation-state-actor-midnight-blizzard/)

> In recent weeks, we have seen evidence that Midnight Blizzard is using information initially exfiltrated from our corporate email systems to gain, or attempt to gain, unauthorized access. This has included access to some of the company’s source code repositories and internal systems. To date we have found no evidence that Microsoft-hosted customer-facing systems have been compromised.
> 
> It is apparent that Midnight Blizzard is attempting to use secrets of different types it has found. Some of these secrets were shared between customers and Microsoft in email, and as we discover them in our exfiltrated email, we have been and are reaching out to these customers to assist them in taking mitigating measures. Midnight Blizzard has increased the volume of some aspects of the attack, such as password sprays, by as much as 10-fold in February, compared to the already large volume we saw in January 2024.
> 
> Midnight Blizzard’s ongoing attack is characterized by a sustained, significant commitment of the threat actor’s resources, coordination, and focus. It may be using the information it has obtained to accumulate a picture of areas to attack and enhance its ability to do so. 


This post breach actions are interesting to see.  We often characterise cyber attacks as almost “once and done”, you protect against the adversary, get breached, they steal your data and they move on.

The the sorts of advanced actors like Midnight Blizzard are after information in order to better position themselves to get even more access and information.  That’s one of the reasons that in this attack they searched for emails and information about themselves, they wanted to know what Microsoft knew about their capabilities to determine how to better hide in the future. 


## [How Microsoft Copilot for Security helps defend against human-operated ransomware attacks | Microsoft Security Blog ](https://www.microsoft.com/en-us/security/blog/2024/03/04/defend-against-human-operated-ransomware-attacks-with-microsoft-copilot-for-security/)

[https://www.microsoft.com/en-us/security/blog/2024/03/04/defend-against-human-operated-ransomware-attacks-with-microsoft-copilot-for-security/](https://www.microsoft.com/en-us/security/blog/2024/03/04/defend-against-human-operated-ransomware-attacks-with-microsoft-copilot-for-security/)

> Organizations everywhere are seeing an increase in human-operated [ransomware](https://www.microsoft.com/security/business/security-101/what-is-ransomware) threats, with Microsoft’s own telemetry showing a 200% increase in threats since September 2022.1 When an entire organization is attacked, they need every advantage they can get to protect against skilled, coordinated cyber threats.
> 
> […]
> 
> In the case of this human-operated ransomware incident, [Microsoft Defender for Endpoints](https://www.microsoft.com/security/business/endpoint-security/microsoft-defender-endpoint) had the first alert, detecting possible human operated malicious activity on a device. Many complex and sophisticated attacks like ransomware use scripts and tools like PowerShell and Mimikatz to access and manipulate files, tamper with system recovery settings, and delete file backups. In this incident, attackers also attempted to access Primary Refresh Tokens (PRT) and used Windows Sysinternals tools for evasion. But with line-by-line script examination in Copilot, security analysts could immediately understand what each section of code does, to quickly identify a script as malicious or benign. This Copilot capability directly helps junior security analysts “upskill” their expertise by learning the context behind the code. 


This is a nice use of AI to augment human capabities, in a manner that I generally like.  But there’s a real question about whether we are truly upskilling our analysts this way.

One of the problems in cybersecuirty is the dearth of people who understand the fundementals.  Learning how to interact with a tool can be effective, but doesn’t always give you transferable skills that you can use if you switch tools.  

I like this tool, but I think it’s incredibly important when using tools like this to ensure you have internal lessons learned functions that work to analyze, share and educate about the details behind an attack.  This AI powered tooling might replace the pointy end of analytical capability, but you are still going to need highly competent and capable analysts for some of the more complex work. 


