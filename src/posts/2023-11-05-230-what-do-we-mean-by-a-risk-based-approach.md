---
title: "230 - What do we mean by a risk-based approach?"
date: 2023-11-05
description: "We hear the phrase \"Take a risk-based approach\" or \"make a risk-based decision\" a lot in security, and I do believe that we should be risk-based in our security approach, but it's so much easier to say than to actually do."
permalink: /what-do-we-mean-by-a-risk-based-approach/
---

We hear the phrase "Take a risk-based approach" or "make a risk-based decision" a lot in security, and I do believe that we should be risk-based in our security approach, but it's so much easier to say than to actually do.

Humans are awful at gauging risk, and it's rare that when we give advice to take a risk-based decision, that we provide people with the evidence that can support that decision.

Reading reports on mobile spyware, on commodity malware and on the rising capability of threat actors, you'd be forgiven for taking your computer and throwing it in the rubbish bin as the only sane way to engage safely in modern life.  But in reality, there are about 5.3 billion worldwide users of the internet, around 2/3rds of the worlds population.  The number of breached accounts according to HaveIBeenPwned is around 150 million, which means about 0.3% of users have suffered a personal breach of their email address and/or password.  Assuming the growth rates are largely the same (and I've not had a chance to look at the statistics properly), there's somewhere in the region of 0.3% chance of your email and password being breached on a single site in any given year.  

That's actually a pretty high number, a 1/1000 chance of something happening is high enough that you'll know someone it happened to, even if it doesn't happen to you.  Equivalently, there are around 16000 road accidents a year in the UK that injure a pedestrian, although 11,000 were slight injuries and 5,000 severe injuries, but that means that crossing the road, one of the most dangerous things you can do, has a 0.0002% chance of hurting you.  In comparison, flying is astonishingly unlikely to injure you in any form, and is one of the safest ways to travel given the huge numbers of people who travel and the remarkably low incident rate.

But as humans, many of us are afraid of flying, but many of us will walk around our town centers and our roads without hesitation.  That's because most of us don't look at the statistics, but also because we have different feelings of safety based on how in control of our environment we are.  Sitting in a plane with no control over what happens feels far riskier than being on your own two feet, where you believe that you could take action should something happen.

In cybersecurity, we have very few good numbers on the actual risks that we take, and what causes most cybersecurity breaches.  We instead go on our gut feel about what feels secure or what doesn't feel secure.  Saving a username and password into your browser feels less secure than memorising it because you aren't in control of that storage, but if it lets you keep a more complex password then it's probably far more secure (we don't have good numbers on breaches of password managers, so it's hard to be definitive here)

When we look at cybersecurity interventions, one of the things that we should consider is where the risk is lying.  If our system relies on increasing numbers of people not making a mistake, then it's likely less secure and more risky, than if the computer system itself does something for the users.  This is why I'm so hard over on the use of hardware U2F and FIDO tokens (and a reader last week reminded me not to simply say hardware MFA tokens when I mean U2F or FIDO tokens, as there's some other hardware tokens that aren't as good).  Those tokens have computer based identification systems in them to cryptographically ensure the codes aren't being intercepted, and they're single touch use, meaning that none of the risk is on the user "using them improperly".

That use of computing skills, cryptography and attributes of the solution that make them hard to compromise doesn't make them totally secure, or foolproof.  It's quite possible that there will be a supply chain breach, or a service that has improperly coded it's validation or even a manufacturing or protocol flaw found in the future.  But right now, it's one of the most effective ways to reduce the risk of a compromise, while retaining usability.

We desperately need better statistics on breaches, and while it's interesting to read about all of the fascinating high end attacks that we see, we need to keep them in perspective for how we assess, manage and accept risk in the real world

## [Risk Analysis (vs / and / or) Threat Modelling – Security Differently ](https://www.securitydifferently.com/risk-analysis-vs-and-or-threat-modelling/)

[https://www.securitydifferently.com/risk-analysis-vs-and-or-threat-modelling/](https://www.securitydifferently.com/risk-analysis-vs-and-or-threat-modelling/)

> As Adam Shostack originally wrote, the 4 questions of TM are “what are you building ? what can go wrong ? what are we going to do about it ? how good a job have we done”, so it’s grounded in WHAT WE ARE BUILDING now.
> 
> An often found problem with applying RA practices to the scope of Agile delivery practices, is that of ‘scope creep’ in that the ones mandating or facilitating RA will often identify issues which aren’t in the scope of what’s being built. This tends to generate an organisational dynamic between GRC functions (those usually leading RA) which has them being perceived as not adding much value to the Agile delivery process they’re trying to influence, as they keep asking and identifying things which aren’t in the scope of what’s being built but often other systems or concerns which are already existing problems that the Agile teams aren’t tasked with addressing at that point.
> 
> This isn’t to say that RA can’t be useful in an Agile process, but from experience, I’d argue that it’s success will largely depend on the social capital or technical expertise of the facilitator and if we’re trying to build sustainable practices, we shouldn’t be designing them in ways which are reliant on individuals possessing both business and engineering skills, as there aren’t many out there.
> 
> So, in my opinion, we shouldn’t be trying to choose between one or the other. Instead, we should be trying to ensure we’re talking Risk, RA, RM with the stakeholders whose [**timespan of discretion**](https://www.securitydifferently.com/social-practices-and-timespan-of-discretion-in-cyber-security-cef4fdc16663/) spans medium and long term cycles, and ensuring that the OUTPUTS of RA/RM become INPUTs to TM. 


Interesting differences between Risk Analysis and Threat Modelling.  

In my view, Threat Modelling in it’s most formal sense is also difficult to integrate into agile methodologies.  That’s because it assumes that you can analyse the system in whole, which may not help if you are not designing up front, and instead incrementally building features and systems as you go.

It’s possible to use threat modelling principles and processes within an agile team to continually evaluate suggested changes against a threat model, but that’s far rarer to see implemented in practice, especially if you don’t have enough security people to embed someone into the agile product delivery team. 


## [Threat Modelling Cloud Platform Services by Example: Google Cloud Storage – NCC Group Research ](https://research.nccgroup.com/2023/01/31/threat-modelling-cloud-platform-services-by-example-google-cloud-storage/)

[https://research.nccgroup.com/2023/01/31/threat-modelling-cloud-platform-services-by-example-google-cloud-storage/](https://research.nccgroup.com/2023/01/31/threat-modelling-cloud-platform-services-by-example-google-cloud-storage/)

> The security challenges faced by small/medium companies and enterprises when deploying new services into the cloud can often be daunting, so to get a better understanding of these challenges on GCP and help pointing out the necessary and available security controls, we used a threat modelling approach.
> 
> As a first step we chose to threat model GCP’s Google Cloud Storage service. To gain a better understanding of the service, we identified its key features and then drew a high-level diagram of the service. During the construction of the diagram, it was possible to identify the main data assets involved and any base security controls that were enabled by default. From there, it was possible to create a threat model for the Google Cloud Storage service with all the available features, security control recommendations were provided that would mitigate the identified threats.
> 
> The STRIDE model was used to create the threat model, as it provided a well proven methodology and an industry recognised approach. 


A useful deepdive into GCP, but more importantly, a really useful view of modern threat modelling practices.  What’s not apparent in this is that the end artifact is often only half the value of threat modelling.  Much of the value is in sitting down and carrying out the threat modelling itself.  The conversation, the discussion about how things work and the edge cases and weird little corners often get missed from the writeup.  But this knowledge does reside in the heads of those present and involved.  It’s one of the reasons that I always strongly encourage that threat modelling should involve not just security, but technical leads and a business representative if at all possible. 


## [Article: Product Risk Taxonomy : Silicon Valley Product Group ](https://www.svpg.com/product-risk-taxonomies/)

[https://www.svpg.com/product-risk-taxonomies/](https://www.svpg.com/product-risk-taxonomies/)

> The first is the one I was originally taught, and is the one I described in the first edition of INSPIRED (from 2008): _value_ , _usability_ and _feasibility_ . I used this for well over a decade, and I like that it’s just 3 risks, and it’s fairly intuitive for people to grasp.
> 
> However, over time I began to see a recurring and serious problem with this taxonomy. “Value” was supposed to cover both _customer_ value and _business_ value. But I kept encountering the problem where the product team would focus on _customer_ value, but would gloss over _business_ value. In fact, even today you can find far too many product people, even some that are considered thought leaders, that argue that “the only thing you need to focus on is coming up with a product your customers love.” I wish.
> This might be just a coincidence, but I suspect this problem is correlated with the rise in [the anti-pattern of the product owner as product manager](https://www.svpg.com/the-cspo-pathology/) . Before Agile became widespread, at least in my experience, product teams had a better understanding of the importance of solving for the business as well as for the customer.
> 
> To address this, in the second edition of INSPIRED (2018), I separated out those two risks into customer _value_ and business _viability_ .
> 
> I know this may sound minor to people, but for things like this, where you are trying to coach people to keep something important in their minds while they think through a problem, it really is better to have 3 items rather than 4. But I believed at the time, and I still believe this is the case, that it’s worth the extra cognitive load to have the _four_ risk taxonomy: _value, usability, feasibility_ and _viability_ . 


This is a nice explanation around why “value” is such a hard concept to convey effectively.  We often try to prioritise work based on the “value” it will deliver, but in reality spliting that into both the value to the end user, as well as the value to the business can make clear that there are some piece of work that end customers might love, but have incredibly low value (or even negative value) to the business.  Equally, there are some things you do that have high value to the business but low value for the customer.

Balancing between those two things is one of the keys of business strategy and helps us keep producing products and services that our customers love, but help the company turn a profit or deliver on its objectives 


## [0-days exploited by commercial surveillance vendor in Egypt ](https://blog.google/threat-analysis-group/0-days-exploited-by-commercial-surveillance-vendor-in-egypt/)

[https://blog.google/threat-analysis-group/0-days-exploited-by-commercial-surveillance-vendor-in-egypt/](https://blog.google/threat-analysis-group/0-days-exploited-by-commercial-surveillance-vendor-in-egypt/)

> The Intellexa exploit chain was delivered via a “man-in-the-middle” (MITM) attack, where an attacker is in between the target and the website they’re trying to reach. If the target is going to a website using ‘http’, then the attacker can intercept the traffic and send fake data back to the target to force them to a different website. Visiting a website using ‘https’ means that the traffic is encrypted, and it is easily verifiable that the received data came from the intended website using their certificate. That is not the case when using ‘http’.
> 
> In the case of this campaign, if the target went to any ‘http’ site, the attackers injected traffic to silently redirect them to an Intellexa site, c.betly[.]me. If the user was the expected targeted user, the site would then redirect the target to the exploit server, sec-flare[.]com. While there’s a spotlight on “0-click” vulnerabilities (bugs that don’t require user interaction) this MITM delivery also didn’t require the user to open any documents, click a specific link, or answer any phone calls.
> 
> […]
> 
> This campaign is yet another example of the abuses caused by the proliferation of commercial surveillance vendors and their serious risk to the safety of online users. TAG will continue to take action against, and publish research about, the commercial spyware industry, as well as work across the public and private sectors to push this work forward. 


Google’s TAG group found yet another commercial surveillance vendor, using 0-days and a network level injection.  The network level injection could only be deployed if they had the ability to compromise the network between you and the internet, so sat at home on your couch or in your workplace, this is likely very hard to attack you with, but travelling in a hotel, cafe wifi or similar might make it easier for this attack to start.

Alternatively, for a 1-click vulnerability, if they can get you to take an action on your device that means your browser visits a site they control, they can probably deploy this via that as well 


## [Unauthorized Access to Okta's Support Case Management System: Root Cause and Remediation | Okta Security ](https://sec.okta.com/harfiles)

[https://sec.okta.com/harfiles](https://sec.okta.com/harfiles)

> The unauthorized access to Okta’s customer support system leveraged a service account stored in the system itself. This service account was granted permissions to view and update customer support cases. During our investigation into suspicious use of this account, Okta Security identified that an employee had signed-in to their personal Google profile on the Chrome browser of their Okta-managed laptop. The username and password of the service account had been saved into the employee’s personal Google account. The most likely avenue for exposure of this credential is the compromise of the employee’s personal Google account or personal device. 


Service Accounts are normally talking about situations where a computer needs to talk to another computer, sometimes without the user logging in yet.  They are used for things like communicating with authentication servers to say “A user has just tried to log into me with this username and password, are they allowed and what privileges should I give them?”

In this case, when Okta say that this was a service account, but the user has saved the “service account username and password” in their browser, I suspect what they mean is an account like “SupportUser1”.  I can’t think of any other obvious way that the credentials from a service account would be saved in the browser.  These aren’t really service accounts in the strictest sense of the word then, they’re more like generic accounts.  I’ve seen these used in lots of customer service situations where you don’t control the onboarding of individual agents, for example where you use lots of contractors.  The theory goes that you turn up for your shift, and the documentation says to sign in with “SupportAgent12” and a defined username.  That user account and password likely doesn’t change much, but generally that username and password should only be usable from the original computer or network.

For this accounts credentals to be exposed via a personal users password syncing service, and then abused by the attacker from a remote location indicates a number of system level failures.  

This isn’t a failure of the individual to use their personal account (although that’s probably not wise), the fundamental system failures were already there, and this one action just revealed them in this case. 


## [Results of Major Technical Investigations for Storm-0558 Key Acquisition | MSRC Blog | Microsoft Security Response Center ](https://msrc.microsoft.com/blog/2023/09/results-of-major-technical-investigations-for-storm-0558-key-acquisition/)

[https://msrc.microsoft.com/blog/2023/09/results-of-major-technical-investigations-for-storm-0558-key-acquisition/](https://msrc.microsoft.com/blog/2023/09/results-of-major-technical-investigations-for-storm-0558-key-acquisition/)

> Our corporate environment, which also requires secure authentication and secure devices, allows for email, conferencing, web research and other collaboration tools. While these tools are important, they also make users vulnerable to spear phishing, token stealing malware, and other account compromise vectors. For this reason - by policy and as part of our Zero-Trust and “assume breach” mindset - key material should not leave our production environment.
> 
> Our investigation found that a consumer signing system crash in April of 2021 resulted in a snapshot of the crashed process (“crash dump”). The crash dumps, which redact sensitive information, should not include the signing key. In this case, a race condition allowed the key to be present in the crash dump (this issue has been corrected). The key material’s presence in the crash dump was not detected by our systems (this issue has been corrected).
> We found that this crash dump, believed at the time not to contain key material, was subsequently moved from the isolated production network into our debugging environment on the internet connected corporate network. This is consistent with our standard debugging processes. Our credential scanning methods did not detect its presence (this issue has been corrected).
> 
> After April 2021, when the key was leaked to the corporate environment in the crash dump, the Storm-0558 actor was able to successfully compromise a Microsoft engineer’s corporate account. This account had access to the debugging environment containing the crash dump which incorrectly contained the key. Due to log retention policies, we don’t have logs with specific evidence of this exfiltration by this actor, but this was the most probable mechanism by which the actor acquired the key. 


This was a shocking compromise of Micirosofts systems, but what stood out to me here was the number and complexity of defences in place.  When people sometimes say that Defenders have to be lucky everytime, but attackers only have to be lucky once, this is the sort of thing that people are talking about.

In this, it becomes clear that Microsoft has a crash dump system that routinely attempts to redact sensitive information from crash dumps.  That’s an unusual practice outside of the most regulated environments (although given the use of crypto keys, isn’t unheard of here).

They then have a second system taht additionally redacts credentials when moving crash dumps from production and into their corporate environment that also failed in this case.  That’s a good belt and braces approach which would normally be good enough.

The fact that both systems failed meant that crypto key material must have ended up on the corporate network system where it was able to be picked up by an advanced adversary.  To then find that there was a bug in the code signing library that meant that this key, already damaging, had much wider properties than expected was incredibly fortunate for the attacker. 


## [Octo Tempest crosses boundaries to facilitate extortion, encryption, and destruction | Microsoft Security Blog ](https://www.microsoft.com/en-us/security/blog/2023/10/25/octo-tempest-crosses-boundaries-to-facilitate-extortion-encryption-and-destruction/)

[https://www.microsoft.com/en-us/security/blog/2023/10/25/octo-tempest-crosses-boundaries-to-facilitate-extortion-encryption-and-destruction/](https://www.microsoft.com/en-us/security/blog/2023/10/25/octo-tempest-crosses-boundaries-to-facilitate-extortion-encryption-and-destruction/)

> Octo Tempest is a financially motivated collective of native English-speaking threat actors known for launching wide-ranging campaigns that prominently feature [adversary-in-the-middle (AiTM) techniques](https://www.microsoft.com/security/blog/2023/06/08/detecting-and-mitigating-a-multi-stage-aitm-phishing-and-bec-campaign/) , social engineering, and SIM swapping capabilities. Octo Tempest, which overlaps with research associated with 0ktapus, Scattered Spider, and UNC3944, was initially seen in early 2022, targeting mobile telecommunications and business process outsourcing organizations to initiate phone number ports (also known as SIM swaps). Octo Tempest monetized their intrusions in 2022 by selling SIM swaps to other criminals and performing account takeovers of high-net-worth individuals to steal their cryptocurrency.
> 
> Building on their initial success, Octo Tempest harnessed their experience and acquired data to progressively advance their motives, targeting, and techniques, adopting an increasingly aggressive approach. In late 2022 to early 2023, Octo Tempest expanded their targeting to include cable telecommunications, email, and technology organizations. During this period, Octo Tempest started monetizing intrusions by extorting victim organizations for data stolen during their intrusion operations and in some cases even resorting to physical threats.
> 
> In mid-2023, Octo Tempest became an affiliate of ALPHV/BlackCat, a human-operated [ransomware as a service](https://www.microsoft.com/security/blog/2022/05/09/ransomware-as-a-service-understanding-the-cybercrime-gig-economy-and-how-to-protect-yourself/) (RaaS) operation, and initial victims were extorted for data theft (with no ransomware deployment) using ALPHV Collections leak site. This is notable in that, historically, Eastern European ransomware groups refused to do business with native English-speaking criminals. By June 2023, Octo Tempest started deploying ALPHV/BlackCat ransomware payloads (both Windows and Linux versions) to victims and lately has focused their deployments primarily on VMWare ESXi servers.
> 
> […]
> 
> In rare instances, Octo Tempest resorts to fear-mongering tactics, targeting specific individuals through phone calls and texts. These actors use personal information, such as home addresses and family names, along with physical threats to coerce victims into sharing credentials for corporate access. 


Interesting report showing the growth and change of a criminal enterprise, which started with simple offerings, but has moved into different areas over time.  The details in here about the intimidation of staff is worrying, and feels like an incredibly dangerous escalation in the ransomware modus operandi.  

Once they have identified staff, sending threatening messages to attempt to get hold of the the MFA tokens or passwords, which includes doxing the individual and threatending physical violence against themselves or their family feels like it’s beyond the pale.

If you are a major company who might be targeted in this space, you need to ensure that you have agreed protocols for this kind of threat for your core administrative staff.  Should they tell you immediately, and accept having their accounts completely frozen so they have nothing of value that can be handed over, or should they give up credentials?  Whatever the rules are, you need to ensure all your staff know that you take their physical safety and security seriously 


## [Sophisticated StripedFly Spy Platform Masqueraded for Years as Crypto Miner ](https://www.zetter-zeroday.com/p/sophisticated-stripedfly-spy-platform)

[https://www.zetter-zeroday.com/p/sophisticated-stripedfly-spy-platform](https://www.zetter-zeroday.com/p/sophisticated-stripedfly-spy-platform)

> The cryptocurrency miner is just one component of a large and complex platform that the researchers call StripedFly. The platform is designed for use on both Windows and Linux-based systems and has numerous plug-ins that give the attackers broad spying functionality. Such functionality is common in nation-state spying platforms but not in criminal malware, which is what the researchers originally took the cryptocurrency miner to be.
> 
> The spy components include ones for harvesting credentials from infected machines; for siphoning .PDFs, videos, databases and other valuable files; grabbing screenshots; and recording conversations through an infected system’s microphone. The platform also has an updating function that lets the attackers push out new versions of it whenever Windows and Linux operating systems get updated. The malware gets pushed out from encrypted archives stored on GitLab, GitHub, and Bitbucket.
> 
> But there are three additional things that are notable about StripedFly: it uses a remarkable custom-coded TOR client to transmit communication and siphoned data between infected systems and the attackers’ command and control server. It has a ransomware component that has infected a small subset of victims, including ones in Taiwan. And it uses a custom EternalBlue exploit as the initial vector to get the spyware onto victim machines.
> 
> Eternal Blue was an infamous Windows exploit created and used by an NSA hacking group known as the Equation Group — the name Kaspersky [gave the group in 2015](https://www.wired.com/2015/02/kapersky-discovers-equation-group/) when it discovered tools made by the group. Equation Group was responsible for the [Stuxnet](https://www.amazon.com/Countdown-Zero-Day-Stuxnet-Digital/dp/0770436196) tool that sabotaged Iran’s nuclear program between 2007-2010 as well as a host of sophisticated spy tools discovered by Kaspersky.
> 
> StripedFly, Lozhkin says, has some similarities to Equation Group malware and has coding style and practices that resemble an NSA implant known as [STRAITBIZARRE](https://medium.com/@botherder/everything-we-know-of-nsa-and-five-eyes-malware-e8eac172d3b5) that was exposed in the Edward Snowden leaks in 2013. But despite the similarities, the researchers say there is “no direct evidence that they are related” or that StripedFly is an NSA platform.
> Nonetheless, “the amount of effort invested in creating this framework is truly remarkable, and its unveiling was quite astonishing,” says Lozhkin, whose team published information about StripedFly in a private technical report last year, but plans to present their findings publicly for the first time on Thursday at the company’s [Security Analyst Summit](https://thesascon.com/) in Thailand. 


This one is interesting, and I doubt anyone will ever know for sure quite whats going on here.

However, there have been a number of tools leaked over the last decade from nation state APT teams, along with increasing decryptions and reverse engineering of some highly capable malware.

When Russia’s SVR targeted the build systems of SolarWinds, that will have given ideas to a number of other malware authors.  They’ll have looked at the reported behaviours and thought “I wonder if I can code that?”.

The same is true for complex command and control networks, the use of exploits such as EternalBlue which was released in the Shadow Brokers hack and sale, along with enough information from leakers that enables commercial and individuals analysts to start to catchup with modern nation state capabilities.

Is this simply a copy-cat or is it some capability being reused from the original EquationGroup leaks? I doubt we’ll ever know, but for sure, these techniques being available to criminal groups is going to make defenders life much harder 


## [Chris Albon on X ](https://twitter.com/chrisalbon/status/1717714416555397507)

[https://twitter.com/chrisalbon/status/1717714416555397507](https://twitter.com/chrisalbon/status/1717714416555397507)

> The thing nobody talks about with engineering management is this:
> 
> Every 3-4 months every person experiences some sort of personal crisis. A family member dies, they have a bad illness, they get into an argument with another person at work, etc. etc. Sadly, that is just life. Normally after a month or so things settle down and life goes on.
> 
> But when you are managing 6+ people it means there is _always_ a crisis you are helping someone work through. You are always carrying a bit of emotional burden or worry around with you. 


A reminder that CISO’s have one of the highest burnout rates in modern jobs.  Make sure that you aren’t carrying all the burdens of your team as well as the risk of the entire organisation on your shoulders without a support network 


