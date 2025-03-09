---
title: "36 - What will 2019 hold for us?"
date: 2019-01-26
description: "I've held off on making predictions about cybersecurity.  2018 was such a bonkers year, from the SuperMicro allegations, to Russian interference everywhere, from Facebook breaches to Google+ breaches, it felt like it just kept getting crazier and crazier."
permalink: /what-will-2019-hold-for-us/
---

I've held off on making predictions about cybersecurity.  2018 was such a bonkers year, from the SuperMicro allegations, to Russian interference everywhere, from Facebook breaches to Google+ breaches, it felt like it just kept getting crazier and crazier.

But I think there's a few pretty consistent themes from 2018 that will continue through 2019 (and probably beyond, I think they're in the 5 year horizon for being fixed in normal organisations).

Security as an industry has a long way to catch up on technology. The move to cloud infrastructure has been both faster and slower than many of us expected, but the adoption of cloud practices has lagged a long way behind the technology.  Modern cloud native systems don't build large networks, and they don't trust the network to keep their data safe.  Instead we see zero trust networking, systems that are configured to encrypt everything from point to point, and identity as the core security model for systems.  But security teams themselves haven't been able to keep up with the technological changes, and so we see organisations failing to adopt good security practices in the cloud, and trying to fit an older model of security to a totally different domain.

It's this stuff that makes me think that patching in the cloud is likely to get worse before it gets better.  Because the cloud gives such capability to automate and improve the ability to patch the operating system (just roll a new VM with a new image, bring it up blue-green style and see if it works), but to do that you need to have adopted the cloud native way of building systems.

Secondly, the identity of cloud administrators is a core concept that didn't really exist.  Previously, your admins used desktop computers on a privileged network, and the admin password could be "password1" or "admin" because nobody could ever get onto your management network.  But today, cloud portals are much harder to lock down, and admin accounts are far more powerful.  Good cloud services offer ways to escalate your privileges when needed, or assume roles as needed, all in audited ways that make stealing and using an "admin account" much harder.  But many organisations just aren't using that technology.

I think 2019 will be categorised by more breaches, mostly through insufficient configuration, not patching systems and increasingly through the stealing or takeover of cloud credentials.

On that happy note, I hope you are enjoying January so far, and looking forward to payday after a long month.  There's over 250 of you reading this now, which only moderately terrifies me, so do drop me a note to let me know what things you like, any improvements you'd like to see, and of course if you write anything or see anything you think I'd like to read, send it my way.

## [The rise of DevSecOps](https://www.computerweekly.com/feature/The-rise-of-DevSecOps)

[https://www.computerweekly.com/feature/The-rise-of-DevSecOps](https://www.computerweekly.com/feature/The-rise-of-DevSecOps)

> The State of Software Security (SOSS) report, published by application security firm CA Veracode, also identified the security benefits of DevSecOps practices. Flaws were fixed 11.5 times faster in companies with the most active DevSecOps programmes, compared with those that had not implemented DevSecOps.
> 
> Driven by the need to increase innovation and efficiency, digital transformation initiatives are now commonplace in businesses of all sizes. But rapid technological advancement can often come at the expense of security, with some firms considering security an obstacle that slows down progress. DevSecOps can help bridge this gap and make sure security is not sacrificed, through the use of automation tools.
> 
> By making use of tools that enable code scanning to be automated and almost instantaneous, DevSecOps removes most of the time-intensive human work. Instead of staff waiting for security alerts to pop up, DevSecOps solutions can actively monitor programs and analyse results from such code checks.


This is an interesting viewpoint, I think it puts the cart before the horse.  If you are running a security team and you start putting in these automated scanning tools (of which Veracode just happen to sell one of), then you are going to create more work for your development team.

You can't just start raising an order of magnitude more work for your development teams unless they are capable of receiving and acting upon that work, and they can't receive and act on that work unless they can deploy the changes into production.

It's very akin to the issue of bug bounties.  As [Katie Moussouris](https://twitter.com/@k8em0) has said repeatedly and loudly, just creating a bug bounty program won't fix your security bugs, it's not just free pen testing.  Before you can create a bug bounty program, you need to be able to triage the bugs, allocate them to the right teams and have them fixed and deployed quickly.  Otherwise it's just wasting everyones time.

However, it's worth noting from the State of Software Security report, that organisations that are capable of scanning hundreds of times per year rather than once or twice, also correlate with organisations that fix the most flaws.  The stat they quote is that they fix flaws 11.5 times faster than the norm.


## [On Bureaucracy – OneTeamGov – Medium](https://medium.com/oneteamgov/on-bureaucracy-ba91dca5a75)

[https://medium.com/oneteamgov/on-bureaucracy-ba91dca5a75](https://medium.com/oneteamgov/on-bureaucracy-ba91dca5a75)

> The trouble with ‘bureaucracy’ is that it cuts both ways. It makes the people responsible for helping us operate and keeping us to the rules feel disempowered and worthless, whilst simultaneously making the people who are trying to get things done feel frustrated and confused. With these symptoms, it can be hard to figure out which of the above causes is actually in play. But if we’re trying to get stuff done and bust ‘bureaucracy’, it’s important that we diagnose which of these three causes is the root of our problem. If we don’t, we will do the wrong thing and bad things will happen.


This is a good writeup on bureaucracy that tries not to make the mistake of just assuming that anything that gets in the way of a single team delivering must be bad for an organisation.

My view of this has changed over the years, and I think there's a definite addendum to the mantra "The strategy is delivery", which is to remember more speed and less haste.  We sometimes think that bureaucratic systems such as filling forms to request work done is something that slows us down and prevents communication, and often it is.  But it's also important to the organisation to know what work is actually happening and where the blockers to flow actually are, and without any form of paper trail, it's difficult to know who requested what.

Bureaucracy is also absolutely necessary when you start scaling your organisation.  If you have one team delivering a product, then consistency comes from the teams natural communication pathways.  But if you are overseeing even 8 or 10 delivery teams within an organisation, then you'll see that the teams themselves often fail to communicate, and lack consistency.  We shouldn't all be exactly the same cookie cutter team structure and decisions, but consistency in choice helps us deliver at speed because we can start to take advantage of shared platforms, shared practices and economies of scale.

We need to think about the minimum viable bureaucracy, and we need to find some way of taking the 10,000 feet view of the organisation and making it apparent to teams, so they can see why they might need to raise that thing by a ticket, or take a certain type of decision to a more senior decision maker.


## [The Messy Truth About Infiltrating Computer Supply Chains](https://theintercept.com/2019/01/24/computer-supply-chain-attacks/)

[https://theintercept.com/2019/01/24/computer-supply-chain-attacks/](https://theintercept.com/2019/01/24/computer-supply-chain-attacks/)

> But while Bloomberg’s story may well be completely (or partly) wrong, the danger of China compromising hardware supply chains is very real, judging from classified intelligence documents. U.S. spy agencies were warned about the threat in stark terms nearly a decade ago and even assessed that China was adept at corrupting the software bundled closest to a computer’s hardware at the factory, threatening some of the U.S. government’s most sensitive machines, according to documents provided by National Security Agency whistleblower Edward Snowden


While interesting, this author really does misunderstand the application of risk and threat models.  The documents that they are reading and referring to appear mostly to be assessments of possible capability.  Sure we know that some supply chain interdiction happens in various places, but it tends to require massive operational resources, capability and is prone to needing lots of things to go right.  That doesn't mean it happens all the time, as this article tries to outline.

I can only liken it to reading a military strategy book that points out that infantry troops can hide in forests while manoeuvring, and then pointing at Sherwood forest and saying "Look see, we are at risk".  Just because the capability to carry out an attack exists, doesn't mean that a threat actor actually will carry out that attack, or that it's terribly likely.

This article even goes so far as to highlight weaknesses in two major BIOS manufacturers, and then adds at the end statements from the manufacturers saying "Yeah, these are well known, out of date weaknesses, we moved to UEFI precisely for that".  

That should help people worried about these attacks today, but probably does worry defenders of military networks where the systems are decades old and probably haven't been refreshed recently.  And at the end of the day, that's what most of these documents seem to be talking about.  Here are potential dangers that we might want to worry about, because we protect military and classified networks.


## [How Whatsapp Is Fueling Fake News Ahead of India's Elections | Time](http://time.com/5512032/whatsapp-india-election-2019/)

[http://time.com/5512032/whatsapp-india-election-2019/](http://time.com/5512032/whatsapp-india-election-2019/)

> Ahead of national elections in April and May, India’s political parties are pouring money into creating hundreds of thousands of WhatsApp group chats to spread political messages and memes. Prime Minister Narendra Modi’s ruling Bharatiya Janata Party (BJP) has drawn up plans to have three WhatsApp groups for each of India’s 927,533 polling booths, according to reports. With each group containing a maximum of 256 members, that number of group chats could theoretically reach more than 700 million people out of India’s population of 1.3 billion.


This report is somewhat chilling about the type of message to get out, but look at those numbers and that coordination.  Setting up somewhere in the region of 3 million whatsapp groups, adding people's phone numbers based on their likely voting intentions and then spreading your message through it.

I'm somewhat surprised that adding random people to a group in WhatsApp, which shares the phone numbers of the participants with each person added, isn't a breach of data protection laws, or that users actually stay in the group when added.  Clearly indian use of Whatsapp is nothing like my use of Whatsapp.


## [Global DNS Hijacking Campaign: DNS Record Manipulation at Scale « Global DNS Hijacking Campaign: DNS Record Manipulation at Scale | FireEye Inc](https://www.fireeye.com/blog/threat-research/2019/01/global-dns-hijacking-campaign-dns-record-manipulation-at-scale.html)

[https://www.fireeye.com/blog/threat-research/2019/01/global-dns-hijacking-campaign-dns-record-manipulation-at-scale.html](https://www.fireeye.com/blog/threat-research/2019/01/global-dns-hijacking-campaign-dns-record-manipulation-at-scale.html)

> It is difficult to identify a single intrusion vector for each record change, and it is possible that the actor, or actors are using multiple techniques to gain an initial foothold into each of the targets described above. FireEye intelligence customers have received previous reports describing sophisticated phishing attacks used by one actor that also conducts DNS record manipulation. Additionally, while the precise mechanism by which the DNS records were changed is unknown, we believe that at least some records were changed by compromising a victim’s domain registrar account.
> 
> 


This is a bit of a weird report.  It works as a great generic description of how attackers might exploit having access to change your DNS in order to carry out attacks.  

But this feels quite generic rather than actor specific, and the root cause paragraph highlighted really seems to imply that multiple actors are behaving the same way.  That's because this is a fairly obvious attack to conduct.


## [The French doctrine of offensive cyber operations](https://blog.lukaszolejnik.com/the-french-doctrine-of-offensive-cyber-operations/)

[https://blog.lukaszolejnik.com/the-french-doctrine-of-offensive-cyber-operations/](https://blog.lukaszolejnik.com/the-french-doctrine-of-offensive-cyber-operations/)

> In the French doctrine, the aim of cyber operations is to achieve effects against “enemy systems”. The effects could target the availability or confidentiality. Attacks on integrity are apparently not included in the definition, although of course tampering with data, for example destructive activity, may lead to impacting on the (loss of) availability (“produire des effets à l’encontre d’un système adverse pour en altérer la disponibilité ou la confidentialité des données“). Attacks on integrity (data alteration) are actually mentioned later in the doctrine, too. This might give an impression that the definition of cyber operation in the doctrine might not be coherent with how they are actually made or understood. Or that the doctrine wasn’t proofread. How reassuring is it is for you to decide, but let’s move on.
> 
> In the French doctrine, cyberspace is defined by three layers: physical (i.e. targeting network equipment or hardware; routers, satellite links, etc.), logical (protocols, software, applications, etc.), social (this is about information exchanged between endpoints or users, so includes the addresses, e-mails, but also blogs!). Cyber operations manipulate these layers to achieve goals.


This is a great read about the newly announced French governments decision to ramp up offensive cybersecurity, and an understanding of what that actually means.  The doctrine outlines the problem of asymmetry in cyber warfare, that is to say that cyber capabilities may not be equally damaging to both sides, because some states and actors are far more reliant on technology and may well be significantly weaker in defense than they are in offence.

That's an interesting concept, as is the hybrid battlefield, where military and civilian systems coexist, and it's unclear what is a legal target and what would cause collateral damage that is unacceptable.   Luckily, the French have said that they will be engaging with NATO to discuss exactly these issues, and that they hope to be a leader in being public about these decisions and helping to drive global policy, so that's all good then!


## [Deliveroo users are getting defrauded – and it could be fined millions for it](https://www.newstatesman.com/science-tech/security/2019/01/deliveroo-users-are-getting-defrauded-and-it-could-be-fined-millions)

[https://www.newstatesman.com/science-tech/security/2019/01/deliveroo-users-are-getting-defrauded-and-it-could-be-fined-millions](https://www.newstatesman.com/science-tech/security/2019/01/deliveroo-users-are-getting-defrauded-and-it-could-be-fined-millions)

> (Later – a lot later – a Deliveroo spokesman would tell me it was likely I had been the victim of a “credential stuffing” attack, in which hackers obtain lists of usernames and passwords and try them out on other platforms.)
> 
> This problem is not actually new. In 2016, the Telegraph ran an expose of rampant fraud on the food-delivery service, and reported on customers’ shock at Deliveroo’s poor handling of the situation. The same day, a BBC Watchdog programme did a feature on Deliveroo fraud, in which Deliveroo claimed that “instances of fraud on our system are rare”.
> 
> But dating back several years, Deliveroo’s customer service Twitter account, @DeliverooHelp, has responded to claims of fraud nearly every day – often, in recent months, multiple times a day. They may represent only a small percentage of Deliveroo’s wider customer base, but it’s not at all obvious this is “rare”.


If you build a system that takes money and gives people something, then fraudsters will move in to try to monetise it.  

The fascinating thing here is that surely in these cases, Deliveroo has the address of where the food was delivered to, and as such must know who is committing the fraud.  Or in some cases, the Deliveroo driver is committing the fraud themselves, booking deliveries to places that don't exist and not bothering to deliver it.  Or finally, the restaurants could be committing the fraud and making orders that they don't have to pay out for.

The trend for "Intermediarisation" (Companies that are AirBnB of X), where as a company you take money from a consumer and give it to a supplier means that you have to deal with fraudulant behaviour from every user of your system and work out how to track that, and deal with it.  Deliveroo in this case just isn't managing to keep on top of it enough that it hasn't hit a journalist, and that always magnifies the impact.


## [The most effective security strategies to guard sensitive information - Help Net Security](https://www.helpnetsecurity.com/2019/01/25/effective-security-strategies/)

[https://www.helpnetsecurity.com/2019/01/25/effective-security-strategies/](https://www.helpnetsecurity.com/2019/01/25/effective-security-strategies/)

> Multi-factor authentication: Ninety percent of respondents say multi-factor authentication (MFA) is an effective security control to protect identity data in public clouds, yet only 60% say their organizations actually utilize it.
> 
> Single Sign-On and biometric authentication: IT and security professionals also see identity federation (single sign-on) and biometric authentication as two of the top five most effective security controls, but these technologies have relatively low adoption rates among their organizations. For instance, 80% of respondents say that identity federation, role- or attribute-based policies, and biometric authentication are largely effective to protect access to identity data in public clouds. Despite this, adoption rates are low: only 34%, 38% and 22%, respectively.


I would argue that the most effective security strategy for the cloud is to stop with the hybrid cloud ridiculousness, and to actually embrace a cloud first, cloud native approach to using the cloud.

I say this because, as articulated here, the things that work are MFA and Single Sign-On/Biometrics, which are things that more or less come out of the box with G-Suite and cloud native O365 installations, and yet most of the companies that I see doing email today are still trying to use hybrid cloud technologies that tend to disable or make those features hard to use.  If you tie your Corporate GMail or O365 installation to an on-premise Active Directory controller that doesn't support MFA and SSO, then you've just lost a huge chunk of the security benefit of adopting those cloud providers tools to start with.


## [5 Emerging Cyber Threats to Worry About in 2019 – MIT Technology Review – Medium](https://medium.com/mit-technology-review/5-emerging-cyber-threats-to-worry-about-in-2019-4e789c22a9cb)

[https://medium.com/mit-technology-review/5-emerging-cyber-threats-to-worry-about-in-2019-4e789c22a9cb](https://medium.com/mit-technology-review/5-emerging-cyber-threats-to-worry-about-in-2019-4e789c22a9cb)

> Smart contracts are software programs stored on a blockchain that automatically execute some form of digital asset exchange if conditions encoded in them are met. Entrepreneurs are pitching their use for everything from money transfers to intellectual-property protection. But it’s still early in their development, and researchers are finding bugs in some of them. So are hackers, who have exploited flaws to steal millions of dollars’ worth of cryptocurrencies.
> 
> The fundamental issue is that blockchains were designed to be transparent. Keeping data associated with smart contracts private is therefore a challenge. “We need to build privacy-preserving technologies into [smart contract] platforms,” says Dawn Song, a professor at the University of California, Berkeley, and the CEO of Oasis Labs, a startup that’s working on ways to do this using special hardware.


I've talked about 3 of the other 5 threats on this newsletter a few times, but I haven't ever really touched Quantum Computing and it's effect on cryptography (I don't think I know enough to have an opinion), or on Smart Contracts.

I'm curious about the inclusion of smart contracts in this list, because I don't think there's been enough takeup of the technology for it to be a cyber security threat for 2019.  However, I do suspect that many of the early adopters of the technology will get themselves burned by a failure to understand the security implications and most likely, an attempt to retrofit their existing (probably retrofitted) cloud security policies to smart contracts, which of course won't work.

My list of biggest cyberthreats for 2019 remains, as always, patching, patching, cloud administration credentials/access, lack of estate visibility and user hostile security policies.


