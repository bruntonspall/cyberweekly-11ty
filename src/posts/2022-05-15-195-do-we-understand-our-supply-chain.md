---
title: "195 - Do we understand our supply chain?"
date: 2022-05-15
description: "[Betteridge's law](https://en.wikipedia.org/wiki/Betteridge%27s_law_of_headlines) should tell you the answer to this!  "
permalink: /do-we-understand-our-supply-chain/
---

[Betteridge's law](https://en.wikipedia.org/wiki/Betteridge%27s_law_of_headlines) should tell you the answer to this!  

Of course the answer here is no.  We almost certainly do not understand our supply chains, and I suspect it's likely that we never will.  

The NIST have put out a stadnard for risk management of supply chains, which is a reasonable set of models to start thinking about supply chains.  But for most organisations, we struggle to articulate the difference in threat between several different scenarios.  For example, would you describe all of these as "supply chain risks"?

1. Your company is reliant on a technology provided by a third party company.  One of your direct competitors has just decided to a significant stake in that company and will now sit on it's board of directors
2. Your company outsources a critical piece of business information processing to a third party company, but that third party company has been hit by ransomware and says they won't pay the ransom so the data will be exposed
3. Your company uses a third party management company to manage a number of internal systems, and that management company has been compromised by attackers
4. Your software is reliant on libraries written by a third party, and that third parties software writing and delivery pipeline has been compromised
5. You use a critical piece of management equipment or software that has privileged access to much of your organisation, but the supplier of that equipment has been compromised

I think that many of you would easily be able to argue that all 5 scenarios belong in the world of "supply chain", but they all present wildly different risks to your business, and they all need to be managed totally differently.

Secondly, supply chains are by nature recursive.  For those of you without a background in computer programming, recursion is where the definition of a function is reliant on executing the function itself.  A good example is [a dictionary entry for recursion might say "see recursion"](https://www.google.com/search?q=recursion).  The most common example is the definition of a factorial, which is simply the number multiplied by itself minus 1, so `5 factorial` is `5 x (4 factorial)`.  In this case, we always declare that `1 factorial` is a special case of `1`, and so we end up with `5 factorial = 5 x (4 factorial) = 5 x (4 x (3 factorial)) = 5 x (4 x (3 x (2 factorial))) = 5 x (4 x (3 x (2 x (1))))`.

This act of essentially doing the same thing everytime you descend is important here.  Because you aren't just worried about a single scenario.  If you have scenario 5, the solarwinds example, then you aren't just worrying about whether you use solarwinds on your network, but you are also worrying about scenario 3, where there's a managed security company operating your systems, and you are now having to worry about whether that managed service company is using Solarwinds on their network.

This is what makes supply chains so difficult to comprehend, because you can end up in chains of dependencies and trying to work out just how big an issue it is for you.  

At a recent event, I was chatting with a supplier who was asking me if we could improve the way we ask commercial questions of our suppliers.   It was said that it's quite common to have a clause in the contract that requires us to be able to inspect their data centers if we need to.  But since they have started using cloud systems, they are unable to fulfil some of the clauses of the contract, because they don't own the data centers that are being used by their SaaS tools.  The question there then starts to be, what level of assurance or accreditation can bubble up.  If they are asking for SOC2 compliance in their suppliers, is that sufficient for us, providing they have a good risk management process (as verified by something like ISO27001)?

It feels like this has got to be part of the solution, but I don't think we're agreed on what we are actually worrying about, and so asking for SOC2 compliance or even ISO27001 compliance for use case 1 is an exercise in futility.

I hope that we'll soon come to an industry agreed definition of supply chain, that enables us to separate out commercial concerns from technical concerns from change and risk management concerns, and be far more easily able to articulate, in contracts if possible, just what levels of assurance we are looking for.

Otherwise, we'll be left worrying about an endless fractal and therefore infinite supply chain, and [pushing that boulder up a hill for eternity](https://en.wikipedia.org/wiki/Sisyphus#Punishment_in_the_underworld) doesn't sound fun to me.

## [How Apple, Google, and Microsoft will kill passwords and phishing in one stroke | Ars Technica ](https://arstechnica.com/information-technology/2022/05/how-apple-google-and-microsoft-will-kill-passwords-and-phishing-in-1-stroke/)

[https://arstechnica.com/information-technology/2022/05/how-apple-google-and-microsoft-will-kill-passwords-and-phishing-in-1-stroke/](https://arstechnica.com/information-technology/2022/05/how-apple-google-and-microsoft-will-kill-passwords-and-phishing-in-1-stroke/)

> The program that Apple, Google, and Microsoft are rolling out will finally organize the current disarray of MFA services in some significant ways. Once it’s fully implemented, I’ll be able to use my iPhone to store a single token that will authenticate me on any of those three companies' services (and, one expects, many more follow-on services). The same credential can also be stored on a device running Android or Windows.
> 
> By presenting a facial scan or fingerprint to the device, I’ll be able to log in without having to type a password, which is faster and much more convenient. Equally important, the credential can be stored online so that it’s available when I replace or lose my current phone, solving another problem that has plagued some MFA users—the risk of being locked out of accounts when phones are lost or stolen. The recovery processes works by using an already authenticated device to download the credential, with no password required. 


We’ve heard this before, but the announcements from all 3 major providers might actually be correct this time.  The FIDO and CTAP standards have been floating around for some time, and I’ve been using a YubiKey as my FIDO key, along with Authy for TOTP codes for a number of years. 

I swear by this, although I’m always nervous of the claim that it will kill phishing.  What it definitely kills is the ability of someone to capture your credentials and then re-use them later.  That also means that scammers can’t capture your credentials and then sell them on.

However, phishing emails that either contain malware, or prompt you to download malware will still compromise your device, and if the user is both present and using the device, then MFA won’t protect you there.

Secondly, the lower tier of MFA capabilities, such as TOTP codes, are vulnerable to Man-in-the-middle attacks, where an attacker can live attack your session and steal both your credentials and a live TOTP code to get into your account or system.

Finally, of course, the problem is going to start that instead of having to know or memorise a few hundred passwords, people are going to have hundreds of MFA tokens in their apps, which will frustrate people and encourage them turning them off.
The use of MFA on your core identity provider, such as Google, Apple or Microsoft, should be sufficient in most threat models for many systems.  There’s very little benefit to putting additional MFA into your application if you are confident the user has MFA enabled on their account.

Of course, this also means that security teams really must ensure that company policies allow you to sign into applications using your secured enterprise IT account.  I’m always astonished how many deliberately disable this feature, which only drives people to far worse security outcomes with enterprise data. 


## [Cybersecurity Supply Chain Risk Management Practices for Systems and Organizations ](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-161r1.pdf)

[https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-161r1.pdf](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-161r1.pdf)

> Cybersecurity risks throughout the supply chain are the results of
> threats that exploit vulnerabilities or exposures within products and services that traverse the
> supply chain or threats that exploit vulnerabilities or exposures within the supply chain itself.
> Examples of cybersecurity risks throughout the supply chain include:
> 1) A widget manufacturer whose design material is stolen in another country, resulting in the
> loss of intellectual property and market share.
> 2) A widget manufacture that experiences a supply disruption for critical manufacturing
> components due to a ransomware attack at a supplier three tiers down in the supply chain.
> 3) A store chain that experiences a massive data breach tied to an HVAC vendor with access to
> the store chain’s data-sharing portal. 


There’s a lot of this, over 300 pages in fact, and much of it is probably overspecific, and doesn’t have a huge amount of value.  A lot of it repeats the NIST risk management guidance, and there’s an awful lot of handwaving around saying that you need to define your risk tolerance for supply chain issues, which if it were that easy, we’d have all done that already!  But this introduction starts to build a great framework for actually thinking about supply chain issues.  Subdividing the wider breadth of possible supply chain vulnerabilities into state based interest in your assets, disruption events and assets with unusual reach means that you can start defining different management strategies for different contexts.

Otherwise, you’ll end up, like many risk management approaches, with a one size fits all system that fails to articulate the risk at either end of the contextual spectrum 


## [npm Supply Chain Attack Targeting Germany-Based Companies ](https://jfrog.com/blog/npm-supply-chain-attack-targets-german-based-companies/)

[https://jfrog.com/blog/npm-supply-chain-attack-targets-german-based-companies/](https://jfrog.com/blog/npm-supply-chain-attack-targets-german-based-companies/)

> The JFrog Security research team constantly monitors the npm and PyPI ecosystems for malicious packages that may lead to widespread software supply chain attacks . Last month, we shared a widespread npm attack that targeted users of Azure npm packages.
> 
> Over the past three weeks, our automated scanners have detected several malicious packages in the npm registry, all using the same payload. Compared with most malware found in the npm repository, this payload seems particularly dangerous: a highly-sophisticated, obfuscated piece of malware that acts as a backdoor and allows the attacker to take total control over the infected machine. Furthermore, this malware seems to be an in-house development, and not based on publicly-available tools.
> 
> We set out to research this malware to understand its targets and capabilities. In this blog post, we share our technical analysis findings, as well as thoughts on the potential attackers. 
> 
> **Update May 11th: Following the publication of this blog post, a penetration testing company called “Code White”** **took responsibility** **for this dependency confusion attack** 
> 
> [...]
> The malware consists of two parts – a dropper and a payload.
> 
> The dropper exfiltrates information about the infected machine to the malware’s “telemetry” server (by default hosted at www.pkgio.com) through HTTPS and DNS. This information contains the victim’s username, hostname, and the content of the files “/etc/hosts” and “/etc/resolv.conf”.
> 
> As mentioned, the payload is dynamic and different versions of the malicious package may be shipped with different payloads. However, in the malicious packages we observed, we always saw the same type of basic Javascript payload (“obfusc.enc.js”).
> 
> The payload is a backdoor, an HTTPS client, which registers itself on startup to a hardcoded C2 server and receives commands from it. The payload does not seem to have any persistence mechanisms built into it (will not persist after reboot).
> 
> Once communications are established with the C2 server, the payload can accept the following commands:
> 
> * download – payload will download a file from the C2 server
> * upload – payload will upload a file to the C2 server, at endpoint “callbackupload”
> * eval – evaluate arbitrary Javascript code
> * exec – execute a local binary
> * delete – terminate the process
> * register – Initial registration of the payload on the C2 server


No.  This is completely unacceptable "ethical hacking".

It's entirely possible to clearly define the takeover that you do on a repository with a meaningless artifact that cannot do anything.  But exfiltrating data from the computers it has infected, including details of the network they can talk to, and dropping a payload that can run arbitrary commands is deliberately creating actual vulnerabilities in real peoples computers.

This may have been "an enthusiastic intern", but it's well past the line of acceptable behaviour in infosec


## [Unauthorized gem takeover for some gems · Advisory · rubygems/rubygems.org · GitHub ](https://github.com/rubygems/rubygems.org/security/advisories/GHSA-hccv-rwq6-vh79)

[https://github.com/rubygems/rubygems.org/security/advisories/GHSA-hccv-rwq6-vh79](https://github.com/rubygems/rubygems.org/security/advisories/GHSA-hccv-rwq6-vh79)

> Due to a bug in the yank action, it was possible for any RubyGems.org user to remove and replace certain gems even if that user was not authorized to do so.
> 
> To be vulnerable, a gem needed:
> 
> * one or more dashes in its name
> * an attacker-controlled gem with the name before the dash
> * creation within 30 days OR no updates for over 100 days
> 
> For example, the gem something-provider could have been taken over by the owner of the gem something. Organizations with many gems were not vulnerable as long as they owned the gem with the name before the dash, for example owning the gem orgname protected all gems with names like orgname-provider.


That's a nasty bug, and yet another in the dependency confusion group.  

We put a lot of trust into package managers and the repositories that they hold, but because they are a community affair, it's incredibly difficult to really build a coherent threat model, and protect against it effectively


## [Srsly Risky Biz: Thursday May 12 - by Tom Uren ](https://srslyriskybiz.substack.com/p/srsly-risky-biz-thursday-may-12?s=r)

[https://srslyriskybiz.substack.com/p/srsly-risky-biz-thursday-may-12?s=r](https://srslyriskybiz.substack.com/p/srsly-risky-biz-thursday-may-12?s=r)

> Clearview's facial recognition technology is objectively pretty good , as determined by NIST's facial recognition technology testing . The company has fallen afoul of various  regulators , however, for voraciously scraping publicly available images for its facial database without consent. 
> Clearview is not the only company that does this, but the ACLU's Nate Wessler , Deputy Director of its Speech, Privacy, and Technology Project, told _Seriously Risky Business_ that Clearview was "especially brazen among American companies" in harvesting faceprints without consent.
> "We hope this settlement will be a strong deterrent to any other company considering replicating Clearview’s original business model, by making clear how untenable such practices are under Illinois’ strong law."
> Clearview also aggressively marketed its product to law enforcement by offering free trial accounts to individual police officers without the knowledge of their employers.
> The unconstrained collection of biometrics and unregulated use by police forces _is_ concerning, but we think privacy advocates sometimes go too far.
> [...]
> In most respects, the three experts we consulted were in agreement.
> They all agreed that there are more risks from facial recognition technology than just Clearview and that overarching federal legislation is desirable. As Lewis puts it, "federal regulation would be the best solution instead of 50 states with different rules".
> Where they differed however, was on the desired end state. Wessler and Schwartz were sceptical about legitimate government uses of facial recognition technology, whereas Lewis argued for a tiered approach, outlined below:
> 1. Strict controls on use by law enforcement agencies should be similar to those used for communications data. These should include oversight and prior approval for programs, transparency in use, rules limiting secondary uses of collected data, and requirements for human review and rights for redress.      
> 2. Rules governing government uses other than law enforcement should be less restrictive. These should also include transparency and oversight, defining acceptable secondary uses, and providing processes for redress.  
> 3. Rules for commercial use should be linked to improved privacy protections. Rules for commercial use in public spaces may need to be more fulsome than rules for on-premise use.
> These tiers make sense to us, and there are certainly reasons to be wary of unrestrained government access to its citizen's data. 


I read Srsly Risky Biz (and you should too) as part of my reading for this newsletter.  It often highlights interesting news stories and has a different view on things to me.

Unusually, I found myself really reading the editorial this week, not just the links included (although they are great too).  There is a very US driven world view around the increasing privacy risks of things like facial recognition that stands in stark contrast to the UK and EU views more generally.

This view essentially boils down to “The government should be strongly restricted in how it invades peoples privacy, but commercial firms can do whatever they want”.

This distrust in government and specifically law enforcement uses of surveillance technology builds a world where the one thing that a citizen can hold to account, the government, is the one organisation that is heavily restricted from using such technologies, even when there are public safety benefits to doing so.  Most European countries and regulators seem to be far more worried about the commercial companies invading peoples private lives for profit than abuse by governments.

Given the increasingly global world of tech, where Spotify is based in Sweden, TikTok is based out of China, and many other examples, there’s a real question about whether we’ll actually get a global consensus on the balance of privacy from states, global corporations and the rights of the individual 


## [UNC3524: Eye Spy on Your Email | Mandiant ](https://www.mandiant.com/resources/unc3524-eye-spy-email)

[https://www.mandiant.com/resources/unc3524-eye-spy-email](https://www.mandiant.com/resources/unc3524-eye-spy-email)

> In this blog post, we introduce UNC3524, a newly discovered suspected espionage threat actor that, to date, heavily targets the emails of employees that focus on corporate development, mergers and acquisitions, and large corporate transactions. On the surface, their targeting of individuals involved in corporate transactions suggests a financial motivation; however, their ability to remain undetected for an order of magnitude longer than the average dwell time of 21 days in 2021, as reported in M-Trends 2022, suggests an espionage mandate. Part of the group’s success at achieving such a long dwell time can be credited to their choice to install backdoors on appliances within victim environments that do not support security tools, such as anti-virus or endpoint protection. The high level of operational security, low malware footprint, adept evasive skills, and a large Internet of Things (IoT) device botnet set this group apart and emphasize the “advanced” in Advanced Persistent Threat. UNC3524 also takes persistence seriously. Each time a victim environment removed their access, the group wasted no time re-compromising the environment with a variety of mechanisms, immediately restarting their data theft campaign. We are sharing the tools, tactics, and procedures used by UNC3524 to help organizations hunt for and protect against their operations.


It's interesting that Mandiant associate a long dwell time with an espionage mandate.  

Typically for financially motivated attackers, they want to get in, get the money and get out as fast as possible.  This is because real "OpSec" is hard, and criminal organisations often don't have the resources to setup everything needed to conduct these campaigns effectively.  The speed of the operation means that being noisy isn't so bad.  This is why I think Mandiant have said that this is an espionage group.

But that's only true for financially motivated hackers who are compromising their direct financial target.  In this case, by attempting to compromise mergers and acquisitions targets, they are in fact after information that helps them make money in other ways and places.  Critically, that means that using the information may well not burn the compromise that they've achieved.  Furthermore, if you've compromised teams involved in Mergers and Acquisitions, chances are that they'll be involved in more M&A activity, for different companies over and over.  That means that maintaining stealthy access will get you more money and more return for your investment.  I see this kind of stealthy approach as totally in line with a financial criminal groups motivations.

Of course, none of that matters if you are the victim.  You don't care about the attackers real motivations, what you care about is their behaviours, and in this case, both espionage mandate attackers and this kind of financial crime group attackers would behave in the same way.


## [Trello From the Other Side: Tracking APT29 Phishing Campaigns | Mandiant ](https://www.mandiant.com/resources/tracking-apt29-phishing-campaigns)

[https://www.mandiant.com/resources/tracking-apt29-phishing-campaigns](https://www.mandiant.com/resources/tracking-apt29-phishing-campaigns)

> Beginning mid-January 2022, Mandiant detected and responded to an APT29 phishing campaign targeting a diplomatic entity. During the investigation, Mandiant identified the deployment and use of the BEATDROP and BOOMMIC downloaders. Shortly following the identification of this campaign, Mandiant discovered APT29 targeting multiple additional diplomatic and government entities through a series of phishing waves.
> 
> The phishing emails sent by APT29 masqueraded as administrative notices related to various embassies and utilized legitimate but co-opted email addresses to send emails and Atlassian's Trello service for command and control (C2). These phishing emails were similar to previous Nobelium phishing campaigns in 2021 as they targeted diplomatic organizations, used ROOTSAW (publicly known as EnvyScout) to deliver additional payloads, and misused Firebase or DropBox for C2. The misuse of legitimate webservices such as Trello, Firebase, or DropBox is likely an attempt to make detection or remediation harder.
> 
> An operational shift was observed in February 2022 when APT29 moved from deploying BEATDROP, which used a third-party cloud service to retrieve BEACON, to a simpler BEACON dropper that relied on co-opted infrastructure. The subsequent sections will highlight the Tactics, Techniques, and Procedures as well as the tooling used by APT29 in their latest phishing campaigns.


This is a nasty attack by a competent and capable adversary.  It's interesting to note again that the use of existing real SaaS services for command and control is something that is incredibly difficult for enterprise IT teams to monitor or notice.

Clear customer segmented SaaS offerings would make some of this easier, as it would mean that Enterprise IT services can enable access to their SaaS tools with enterprise agreements without adding access to any random usage of the SaaS tool.  Sadly, I'm not really aware of any SaaS offering in the market which offers that yet.


## [Building a Data Perimeter on AWS - Building A Data Perimeter on AWS ](https://docs.aws.amazon.com/whitepapers/latest/building-a-data-perimeter-on-aws/building-a-data-perimeter-on-aws.html)

[https://docs.aws.amazon.com/whitepapers/latest/building-a-data-perimeter-on-aws/building-a-data-perimeter-on-aws.html](https://docs.aws.amazon.com/whitepapers/latest/building-a-data-perimeter-on-aws/building-a-data-perimeter-on-aws.html)

> In traditional, on-premises data center environments, a trusted network and strong authentication are the foundation of security. They establish a high-level perimeter to help prevent untrusted entities from coming in and data from going out. This perimeter provides a clear boundary of trust and ownership. When customers think about creating an AWS perimeter as part of their responsibility for security “in the cloud” in the AWS Shared Responsibility Model , they want to achieve the same outcomes. They want to draw a circle around their AWS resources, like Amazon Simple Storage Service (S3) buckets and Amazon Simple Queue Service (SQS) queues, that clearly separates “my AWS” from other customers. 
> The circle that defines an AWS perimeter is typically represented as an AWS _organization_ managed by AWS Organizations. AWS Organizations is an account management service that lets you consolidate multiple AWS accounts into an organization that you create and centrally manage. 
> Each AWS account you own is a logical container for AWS identities, resources, and networks. The AWS organization is a grouping of all of those items into a single entity. Along with on-premises networks and systems that access AWS resources, it is what most customers think of as the perimeter of “my AWS”. 


This is a nice example of showing how “zero-trust” moves the perimeter from the network to a strong identity system.  In this example, “My AWS” instances may well be on the same physical network or sharing hardware with other peoples AWS instances, but with the right identity control policy in place, it doesn’t matter. 


## [Costa Rica declares national emergency after Conti ransomware attacks ](https://www.bleepingcomputer.com/news/security/costa-rica-declares-national-emergency-after-conti-ransomware-attacks/)

[https://www.bleepingcomputer.com/news/security/costa-rica-declares-national-emergency-after-conti-ransomware-attacks/](https://www.bleepingcomputer.com/news/security/costa-rica-declares-national-emergency-after-conti-ransomware-attacks/)

> On Sunday, May 8th, the newly elected Costa Rican President Chaves declared a national emergency citing ongoing Conti ransomware attacks as the reason.
> Conti ransomware had originally claimed the ransomware attack against Costa Rican government entities last month.
> 
> The country's public health agency Costa Rican Social Security Fund (CCSS) had earlier stated that "a perimeter security review is being carried out on the Conti Ransomware, to verify and prevent possible attacks at the CCSS level.
> 
> BleepingComputer observed that as of yesterday Conti's data leak site had been updated to state that the group had leaked 97% of the 672 GB data dump allegedly containing information stolen from government agencies 


I thought that after their training material and chats were leaked, Conti might entirely fold up and it's members start afresh.

It looks like instead, they've chosen to simply change targets, and start targeting organisations that might put them less in the crosshairs.  Given that the US Government has put out a reward for information on their leaders, this seems quite bold.

Sadly the impact here could be significant.  That's a lot of government data that has been leaked, and it's unclear just who will use it and what for, but it will almost certainly come at a cost to the citizens of Costa Rica


## [Jack Rhysider on Twitter: "If you're in IT, I highly encourage you to write a blog. Here are 17 reasons why you should be blogging. 🧵👇" / Twitter ](https://twitter.com/JackRhysider/status/1524416387434762241)

[https://twitter.com/JackRhysider/status/1524416387434762241](https://twitter.com/JackRhysider/status/1524416387434762241)

> 1. Don't think of the blog as some new profound insight that makes you look smart. Instead, just write notes to yourself. If you make the blog useful to you, it'll be useful to others.
> 
> 6. The more you explain technical concepts to people. The better you'll get at understanding technical concepts yourself. Sounds backwards but it's true. Teach to learn.
> 
> So to recap. By blogging you will become a better writer and communicator, learn the concepts better, open new opportunities, have a fantastic notebook for self reference, maybe make money, become appreciated by more people, and show off your IT skills. 


Lovely thread by Jack Rhysider of the DarkNet Diaries.  This resonated strongly with me, but most especially points 1 and 6.  Write for yourself, and you’ll learn through teaching.  That’s what drives this newsletter and all the blogging I’ve ever done that’s been successful. 


