---
title: "130 - Solarwinds Special"
date: 2020-12-20
description: "I was going to have a nice relaxing holiday and take a few weeks off from writing a newsletter and news roundup!"
permalink: /solarwinds-special/
---

I was going to have a nice relaxing holiday and take a few weeks off from writing a newsletter and news roundup!

Last week I talked a bit about the FireEye breach, and was saying that the loss of the red team tools was not as big a deal as was being made out.  I had not realised (like many of us), how big a deal the attack mechanism would be.

## So what’s the big deal?

Let's start with the basics shall we.  Solarwinds Orion is a network management tool.  You can install it on your network in order to see what is happening on the network, which devices are there, and use it to manage those devices, to patch them and maintain them.  It was discovered that someone had managed to install a backdoor into the software that could enable them to get into the networks of people running the software. [Fireeye call them UNC2452](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html), where UNC means "Uncategorised" meaning that FireEye are not confident that they can associate the activity with any known existing group.  

The change in the Solarwinds Orion software was introduced back in March 2020, which means that anyone who has patched since then will have installed the infected version.  Because this software is often installed to manage networks, it often has a lot of privileges, meaning that it's a really valuable target for such a compromise.

The impact of simply installing the backdoored software isn't necessarily that great.  The backdoor waits a few weeks to. avoid detection and then beacons out to a command and control servers hosted at a subdomain of avsvmcloud[.]com.  This would install a second piece of malware, codenamed SUNBURST, which would check your system out, beacon back and wait for instructions.  If the attacker decided you were interesting, then the malware would carry out further compromise, at which point the details get a little fuzzy as the attack seems to have different mechanisms for different targets, making correlating the known data hard.  For the vast majority of people infected, this SUNBURST infection is as far as it got.  Microsoft reports that around 17,000 people are known to have installed the known bad software, and that they are reaching out to around 40 who are known to have been infected further.  Those numbers will likely grow over time, that's just what we know so far.

However, because these were highly capable actors, those who have been infected further are in for quite a time trying to uncover what the actor did with their access.  Those infected further should definitely be calling in experts in cyber remediation to help them coordinate the incident and ensure that any infection is removed.

This attack is a big deal for a number of reasons.  Firstly, this is a highly competent attacker who has struck at a critical chink in modern organisations infrastructure, their supply chain.  Secondly, the duration of infection, over 9 months, makes any detection and remediation really hard.  You need to retain all of your logs for nearly 300 days in order to still have them to hand, and the malware is very sneaky, so you'd need to keep and manage a lot of detail in order to investigate fully.  It's highly likely that some organisations will never truly know whether or not they were compromised, or that they've been able to work out what the attacker did inside their networks.  That will be a chilling thought for some partners and affected users.

## Supply chain attacks

Supply chain attacks are particularly nasty for organisations to defend against.  We have to have a complex supply chain, the sheer amount of companies involved in simply providing you with hardware, let alone the firmware, operating system, common utilities, network management and all the other basics that are needed to run a company in modern times.  It's almost impossible to avoid a complex, long and mostly opaque supply chain even in greenfield IT systems, and within a large organisation with decades of IT, your supply chain may well be unknown even within the organisation, let alone the list of suppliers and people that you consume software for.

[Relevant XKCD](https://xkcd.com/2347/)

I'm sure that over the next month, you'll hear from all kinds of vendors, consultants and snake oil salespeople that their software can validate the supply chain, can detect the undetectable and would have prevented this attack.  But the sad reality is that this attack was almost undefendable against.  Strong geopolitical norms, agreement, policing and punishments would be needed to prevent supply chain attacks of this efficacy and magnitude, and none of those things will be achieved by a startup with "dark" or "cyber" in their name.

## What can we do about these kinds of attacks?

So what can we do about these kinds of attacks?  What is it that we can do to defend ourselves and protect ourselves?  Is it even more compliance spreadsheets and questionnaires that we send to our suppliers?  Probably not, it's accepting that this is a risk that we must take in the modern world, and working out how we can limit the impact when it happens.  It means acknowledging that it is for governments, standards bodies and suppliers themselves to attempt to address the likelihood portion of this risk.

What are the effective mechanisms for reducing the impact of the risk?  Well for starters, there was a lot of evasion techniques in the software.  If it thought that it would be detected, it would not run, it simply sat inert.  Deploying highly capable detection tools means that some malware wont run for fear of being detected, and it also means that the malware that does run is more likely to be detected.

Secondly, we need to rethink our architectures for internet access.  Myself and Joel who sometimes contributes here have [talked in the past about terrible implementations of corporate man-in-the-middle internet proxies](https://medium.com/@joelgsamuel/can-we-stop-intercepting-user-traffic-aka-man-in-the-middle-please-2a00de208d4b), and the privacy and security impact that they have on your corporate IT.  But we're talking about the use of those proxies in your end user devices, of intercepting your staffs access to emails, doctors surgery websites, online shopping and banking.  Your data centers have far less reason to reach out to the internet willy-nilly.  Even within a cloud environment, the servers and services in that environment should ideally be put through a whitelisting proxy that only allows communication to known good endpoints.  

That's a much harder recommendation than it sounds however, as lots of software reaches out to wide, unreliably defined networks and domain names.  Much software does not come with any documentation on how it's updates work, what domains it should talk to, and often changes from patch to patch.  This adds to a workload for an IT team, to manage that white list, to handle systems that don't work because they don't have the internet access.  That cost will have to be borne by IT teams in order to manage a suitable protection.  It's worth noting that if you had such a whitelist in place, the malware wouldn't have executed.  
Of course, in this case, it's highly likely that your IT team would have inspected the payload and content, determined it was a valid payload and whitelisted it.  Suppliers are going to need to start providing better lists of the domains and addresses that they use, and ensuring that they stick to it as well.  That change is going to take time, but will make attackers lives significantly harder.

The third thing is being able to determine what was done.  There's a few important detective capabilities that you'll need, but some of the key ones are DNS lookups and authentication logs.  I'm sure there are others that would be useful, but at its core, some of the strongest indicators come from the lookup of C2 systems, and the lateral movement of attackers through your network. 

From the NSA bulletin, we know that this particularly advanced actor is stealing core authentication keys, and using that to mint their own tokens for accessing systems.  It describes these keys as forgeries, which is accurate.  As a friend pointed out, if you stole a complete passport printing system, and all the details needed, those would still be forged passports, but they would be indistinguishable to real passports.  The key here is not being able to detect that user authentications are invalid because they are a poor copy of a real authentication attempt, but being able to detect that the authentication attempt did not correlate with all of the other processes that would occur.  This is like not trying to detect whether a passport was manufactured poorly, but one that was issued weirdly or used weirdly.

In an interview, FireEye suggested that one mechanism that helped them notice the breach was that a user enrolled a new MFA token, which triggered an automated alert to the security team and to the user, who confirmed that they hadn't attempted to enroll a new token.  This kind of contextual monitoring is hard to do, and may give you false positives, but is likely to pay dividends if you ever get targeted by an advanced actor, or even a low level actor using a tool you've not seen, because trying to get access to user credentials is one of the most valuable and common lateral steps that an attacker will take.


## So what should you do about Solarwinds?

Firstly, this is a big deal in high tech, NGO and government circles.  But only 40 out of 17,000 potential targets (so far) is still quite small.  Even if that number grows by an order of magnitude, it's likely that unless you think you would be targeted by a nation state group intent on espionage that you were a bystander in this case.  

However, you should definitely follow the advice of someone like the NCSC, and check whether you use the software and look for indicators of compromise.  It's coming up to Christmas time, so you need to acknowledge that people have had a rough 2020 and prepare yourself for a marathon rather than a sprint in incident response. 

Concentrate on your corporate IT and your critical business assets.  Find out if they are actively exposed, running the version or have ever run the version and start looking for the indicators of compromise.  Even the minimum should give you some confidence about what is and isn't at risk, and enable you to prioritise efforts in the best places.  There has been good publication already of the major indicators of compromise, but this is a changing situation, so there will be more released over time.  Ensure that you have the logs that will be relevant, and if you think you’ve been seriously compromised, then you should get a professional cyber incident response company in to help you.

Secondly, you should reach out to your major critical suppliers. In particular, if you outsource the management of your servers or network to a supplier, you want to know whether their systems are vulnerable, as we have [evidence of high capability actors pivoting through managed service providers in the past](https://www.pwc.co.uk/issues/cyber-security-services/insights/operation-cloud-hopper.html). You aren’t asking whether that MSP runs Solarwinds for you on your network, but get a statement from them about whether they run it on their network that manages their systems, and what incident response they are doing.

## [A moment of reckoning: the need for a strong and global cybersecurity response - Microsoft On the Issues](https://blogs.microsoft.com/on-the-issues/2020/12/17/cyberattacks-cybersecurity-solarwinds-fireeye/)

[https://blogs.microsoft.com/on-the-issues/2020/12/17/cyberattacks-cybersecurity-solarwinds-fireeye/](https://blogs.microsoft.com/on-the-issues/2020/12/17/cyberattacks-cybersecurity-solarwinds-fireeye/)

> As Microsoft cybersecurity experts assist in the response, we have reached the same conclusion. The attack unfortunately represents a broad and successful espionage-based assault on both the confidential information of the U.S. Government and the tech tools used by firms to protect them. The attack is ongoing and is being actively investigated and addressed by cybersecurity teams in the public and private sectors, including Microsoft. As our teams act as first responders to these attacks, these ongoing investigations reveal an attack that is remarkable for its scope, sophistication and impact.
> 
> There are broader ramifications as well, which are even more disconcerting. First, while governments have spied on each other for centuries, the recent attackers used a technique that has put at risk the technology supply chain for the broader economy. As SolarWinds has reported, the attackers installed their malware into an upgrade of the company’s Orion product that may have been installed by more than 17,000 customers.
> 
> [...]
> 
> First, we need to take a major step forward in the sharing and analysis of threat intelligence. In a new year that will mark the 20th anniversary of 9/11, we should remember one of the lessons from the tragic day that the 9/11 Commission called “a shock but not a surprise.” A recurring theme of the commission’s findings was the inability across government agencies to build collective knowledge by connecting data points together. The commission therefore focused its first recommendation on “unifying strategic intelligence” and moving from the “need to know” to the “need to share.”
> 
> If there is an initial question for the incoming Biden-Harris Administration and America’s allies, it is this: Is the sharing of cybersecurity threat intelligence today better or worse than it was for terrorist threats before 9/11?


Microsoft calls this out as an attack, and positions it within the global infrastructure and technology supply chain.  This poisoning of the well is something that they feel is damaging to global norms, it suggests a level of acceptable collateral damage that puts them directly at risk given how much Microsoft's software is used around the world.

More relevant here is that Microsoft calls on the community to be better at sharing information.  This of course creates the kind of press feeding frenzy that we've seen over the past few days.  But as a community, when we share information, it enables us to work out what the issues are, and how we can respond effectively.  In this area, the updates put out by the NSA, by CISA as well as by FireEye and Microsoft themselves have been excellent.  They've been calm, collected and provided as much factual information as possible.  Of course that hasn't stopped some (looking at you Rueters and Washington Post amongst others) for making generalised sweeping statements.


## [Prevasio: Sunburst Backdoor, Part II: DGA & The List of Victims](https://blog.prevasio.com/2020/12/sunburst-backdoor-part-ii-dga-list-of.html)

[https://blog.prevasio.com/2020/12/sunburst-backdoor-part-ii-dga-list-of.html](https://blog.prevasio.com/2020/12/sunburst-backdoor-part-ii-dga-list-of.html)

> To see the decoder in action, let's select 2 lists:
> 
> List #1
> 
> Bambenek Consulting has provided a list of observed hostnames for the DGA domain.
> 
> List #2
> 
> The second list has surfaced in a Paste bin paste, allegedly sourced from Zetalytics / Zonecruncher.
> 
> NOTE: This list is fairly 'noisy', as it has non-decodable domain names.
> 
> By feeding both lists to our decoder, we can now obtain a list of decoded domains, that could have been generated by the victims of the Sunburst backdoor.
> 
> DISCLAIMER: It is not clear if the provided lists contain valid domain names that indeed belong to the victims. It is quite possible that the encoded domain names were produced by third-party tools, sandboxes, or by researchers that investigated and analysed the backdoor.


This is a good bit of deductive work.  If you aren't in this list it doesn't mean you shouldn't worry, and as the disclaimer says, just because you or a partner of yours is in the list isn't necessarily a smoking gun either.

More importantly, if you do see C2 comms out to one of the specialised domains, you can use this code to work out where those queries came from


## [Nuclear weapons agency breached amid massive cyber onslaught - POLITICO](https://www.politico.com/news/2020/12/17/nuclear-agency-hacked-officials-inform-congress-447855)

[https://www.politico.com/news/2020/12/17/nuclear-agency-hacked-officials-inform-congress-447855](https://www.politico.com/news/2020/12/17/nuclear-agency-hacked-officials-inform-congress-447855)

> Federal investigators have been combing through networks in recent days to determine what hackers had been able to access and/or steal, and officials at DOE still don’t know whether the attackers were able to access anything, the people said, noting that the investigation is ongoing and they may not know the full extent of the damage “for weeks.”
> 
> 
> Shaylyn Hynes, a DOE spokesperson, said that an ongoing investigation into the hack has found that the perpetrators did not get into critical defense systems.
> 
> "At this point, the investigation has found that the malware has been isolated to business networks only, and has not impacted the mission essential national security functions of the department, including the National Nuclear Security Administration,"


Access to business networks is bad enough for many of these systems.   People need to coordinate life, work and all kinds of systems on those business networks, and access to that would give an attacker a great insight into how the organisation works, what processes are in use, which are followed and not followed and a lot of insight into the people and personalities.

More importantly, despite the breathless desire of everyone to posit opinion, state what needs to happen next or know what's going on, the reality is that it's going to take weeks and potentially months to know the impact of this breach.  We're not just talking live incidents, some of these people may have been breached 9 months ago, and the attacker moved on, or deliberately further compromised the system to enable alternative command and control.  We may well never know how far the breaches go, how many companies are affected or what the attackers actually got.


## [Dark Halo Leverages SolarWinds Compromise to Breach Organizations | Volexity](https://www.volexity.com/blog/2020/12/14/dark-halo-leverages-solarwinds-compromise-to-breach-organizations/)

[https://www.volexity.com/blog/2020/12/14/dark-halo-leverages-solarwinds-compromise-to-breach-organizations/](https://www.volexity.com/blog/2020/12/14/dark-halo-leverages-solarwinds-compromise-to-breach-organizations/)

> Volexity has subsequently been able to tie these attacks to multiple incidents it worked in late 2019 and 2020 at a US-based think tank. Volexity tracks this threat actor under the name Dark Halo.
> 
> At one particular think tank, Volexity worked three separate incidents involving Dark Halo. In the initial incident, Volexity found multiple tools, backdoors, and malware implants that had allowed the attacker to remain undetected for several years. After being extricated from the network, Dark Halo then returned a second time, exploiting a vulnerability in the organization’s Microsoft Exchange Control Panel. Near the end of this incident, Volexity observed the threat actor using a novel technique to bypass Duo multi-factor authentication (MFA) to access the mailbox of a user via the organization’s Outlook Web App (OWA) service. Finally, in a third incident, Dark Halo breached the organization by way of its SolarWinds Orion software in June and July 2020.


Volexity seems to be tying this back to another actor and some other TTP's.  One of the TTP's in common is similar to the SAML signing key attack.  By stealing the private key that signs the duo cookie, they are able to forge it, and avoid needing to use Duo MFA when accessing OWA.

Again correlation of logs is what you need to detect this.  Being able to look at OWA access and authentication logs combined with Duo logs, if you see a user log in to OWA without a corresponding Duo challenge, then there's a possibility that the Duo authentication has been bypassed in some manner.


## [Detecting abuse of authentication mechanisms - NSA Cybersecurity advisory [pdf]](https://media.defense.gov/2020/Dec/17/2002554125/-1/-1/0/AUTHENTICATION_MECHANISMS_CSA_U_OO_198854_20.PDF)

[https://media.defense.gov/2020/Dec/17/2002554125/-1/-1/0/AUTHENTICATION_MECHANISMS_CSA_U_OO_198854_20.PDF](https://media.defense.gov/2020/Dec/17/2002554125/-1/-1/0/AUTHENTICATION_MECHANISMS_CSA_U_OO_198854_20.PDF)

> In the first TTP, the actors compromise on-premises components of a federated SSO infrastructure and steal the
> credential or private key that is used to sign Security Assertion Markup Language (SAML) tokens (TA00061
> , T1552,
> T1552.004). Using the private keys, the actors then forge trusted authentication tokens to access cloud resources. A
> recent NSA Cybersecurity Advisory warned of actors exploiting a vulnerability in VMware Access®2 and VMware Identity
> Manager®3
> that allowed them to perform this TTP and abuse federated SSO infrastructure [1]. While that example of this
> TTP may have previously been attributed to nation-state actors, a wealth of actors could be leveraging this TTP for their
> objectives. This SAML forgery technique has been known and used by cyber actors since at least 2017 [2].
> In a variation of the first TTP, if the malicious cyber actors are unable to obtain an on-premises signing key, they would
> attempt to gain sufficient administrative privileges within the cloud tenant to add a malicious certificate trust relationship for
> forging SAML tokens.
> In the second TTP, the actors leverage a compromised global administrator account to assign credentials to cloud
> application service principals (identities for cloud applications that allow the applications to be invoked to access other
> cloud resources). The actors then invoke the application’s credentials for automated access to cloud resources (often
> email in particular) that would otherwise be difficult for the actors to access or would more easily be noticed as suspicious
> (T1114, T1114.002).
> 
> Examine logs for suspicious tokens that do not match the baseline for SAML tokens that are typical for the tenant, and
> audit SAML token use to detect anomalies, for example:
> 
>  * Tokens with an unusually long lifetime;
>  * Tokens with unusual claims that do not match organizational policy;
>  * Tokens that claim to have been authenticated using a method that is not used by the organization (e.g., MFA
> when the organization does not use MFA, or MFA by a provider that does not usually perform MFA);
>  * Tokens presented without corresponding log entries, such as tokens with MFA claims where there is no
> corresponding MFA system transaction, or tokens consumed at the resource with no corresponding federation
> server transaction.
>  * Tokens that include a claim that it is for inside the corporate network when it is not;
>  * Tokens that are used to access cloud resources that do not have records of being created by the on-premises
> identity provider in its logs


What do you do if you think you've been compromised, what's next?  It's not as simple as a normal compromise, this is a highly capable actor.  This advisory makes clear that they attempt to get hold of the SAML signing keys that enable them to forge authentication tokens that enable them to have access to systems and user data in a manner that looks real.

Detecting this kind of activity is hard, really hard, but you can do it if you can start correlating the normal activity of systems that use SAML tokens with the user behaviours that drive the generation and use of those tokens.  Seeing unusual, anomalous behaviour of tokens or users might be an indication that the account or system has been compromised. 


## [Analyzing Solorigate, the compromised DLL file that started a sophisticated cyberattack, and how Microsoft Defender helps protect customers - Microsoft Security](https://www.microsoft.com/security/blog/2020/12/18/analyzing-solorigate-the-compromised-dll-file-that-started-a-sophisticated-cyberattack-and-how-microsoft-defender-helps-protect/)

[https://www.microsoft.com/security/blog/2020/12/18/analyzing-solorigate-the-compromised-dll-file-that-started-a-sophisticated-cyberattack-and-how-microsoft-defender-helps-protect/](https://www.microsoft.com/security/blog/2020/12/18/analyzing-solorigate-the-compromised-dll-file-that-started-a-sophisticated-cyberattack-and-how-microsoft-defender-helps-protect/)

> In many of their actions, the attackers took steps to maintain a low profile. For example, the inserted malicious code is lightweight and only has the task of running a malware-added method in a parallel thread such that the DLL’s normal operations are not altered or interrupted. This method is part of a class, which the attackers named OrionImprovementBusinessLayer to blend in with the rest of the code. The class contains all the backdoor capabilities, comprising 13 subclasses and 16 methods, with strings obfuscated to further hide malicious code.
> 
> Once loaded, the backdoor goes through an extensive list of checks to make sure it’s running in an actual enterprise network and not on an analyst’s machines. It then contacts a command-and-control (C2) server using a subdomain generated partly from information gathered from the affected device, which means a unique subdomain for each affected domain. This is another way the attackers try to evade detection.
> 
> With a lengthy list of functions and capabilities, this backdoor allows hands-on-keyboard attackers to perform a wide range of actions. As we’ve seen in past human-operated attacks, once operating inside a network, adversaries can perform reconnaissance on the network, elevate privileges, and move laterally. Attackers progressively move across the network until they can achieve their goal, whether that’s cyberespionage or financial gain.


What can the attackers do with a successful infection.  Even with just the stage one infection, they can perform certain forms of reconnaissance.  They presumably do this to find out whether it's worth deploying a more capable second stage to the infected system.  It's also worth noting that the stage 1 does a lot of avoidance.  They really didn't want it to fire in any form of analytical environment, where someone might notice the odd traffic and behaviour.


## [Advanced Persistent Threat Compromise of Government Agencies, Critical Infrastructure, and Private Sector Organizations | CISA](https://us-cert.cisa.gov/ncas/alerts/aa20-352a)

[https://us-cert.cisa.gov/ncas/alerts/aa20-352a](https://us-cert.cisa.gov/ncas/alerts/aa20-352a)

> SolarWinds Orion is an enterprise network management software suite that includes performance and application monitoring and network configuration management along with several different types of analyzing tools. SolarWinds Orion is used to monitor and manage on-premise and hosted infrastructures. To provide SolarWinds Orion with the necessary visibility into this diverse set of technologies, it is common for network administrators to configure SolarWinds Orion with pervasive privileges, making it a valuable target for adversary activity.
> 
> The threat actor has been observed leveraging a software supply chain compromise of SolarWinds Orion products[2] (see Appendix A). The adversary added a malicious version of the binary solarwinds.orion.core.businesslayer.dll into the SolarWinds software lifecycle, which was then signed by the legitimate SolarWinds code signing certificate. This binary, once installed, calls out to a victim-specific avsvmcloud[.]com domain using a protocol designed to mimic legitimate SolarWinds protocol traffic. After the initial check-in, the adversary can use the Domain Name System (DNS) response to selectively send back new domains or IP addresses for interactive command and control (C2) traffic. Consequently, entities that observe traffic from their SolarWinds Orion devices to avsvmcloud[.]com should not immediately conclude that the adversary leveraged the SolarWinds Orion backdoor. Instead, additional investigation is needed into whether the SolarWinds Orion device engaged in further unexplained communications. If additional Canonical Name record (CNAME) resolutions associated with the avsvmcloud[.]com domain are observed, possible additional adversary action leveraging the back door has occurred.
> 
> Based on coordinated actions by multiple private sector partners, as of December 15, 2020, avsvmcloud[.]com resolves to 20.140.0[.]1, which is an IP address on the Microsoft blocklist. This negates any future use of the implants and would have caused communications with this domain to cease. In the case of infections where the attacker has already moved C2 past the initial beacon, infection will likely continue notwithstanding this action.


Based on impact assessments.  If you have the vulnerable version, and have not been further compromised, you are probably safe right now.  As well as fixed versions available, Microsoft has taken down the command and control server, meaning that new infections are highly unlikely.

For detection purposes, DNS resolution of the avsvmcloud domain anytime in the last 9 months is highly suspicious and should make you assume that you were compromised in the past, and you should look for further indicators to see just how compromised.  Large numbers of people will have had that traffic, but not been selected by the attacker, and therefore have no further evidence of compromise, but finding that out is your most important next step


## [Responding to Solarigate](https://www.cadosecurity.com/post/responding-to-solarigate)

[https://www.cadosecurity.com/post/responding-to-solarigate](https://www.cadosecurity.com/post/responding-to-solarigate)

> Reviewing the backdoored Orion installers, they match what appears to be SolarWind's normal build process. It is likely the attackers have compromised both the SolarWind source code, and their build process to deliver backdoored updates through their normal release process.
> 
> The first backdoored installers identified so far date back to October 2019, though SolarWinds themselves have only referred to backdoored installers starting in May 2020.


You might have seen news reports claiming that the FTP server had weak credentials and that the attackers were able to insert their backdoored versions there.  But it seems far more likely that the attackers had access to the source control repository for Solarwinds, and were able to inject the source code directly.  This means that to all intents and purposes, this was official software, built by Solarwinds, through the normal solarwinds process.  As a customer it would have been impossible to detect that this software was backdoored through normal means.


## [SolarWinds Post-Compromise Hunting with Azure Sentinel - Microsoft Tech Community](https://techcommunity.microsoft.com/t5/azure-sentinel/solarwinds-post-compromise-hunting-with-azure-sentinel/ba-p/1995095)

[https://techcommunity.microsoft.com/t5/azure-sentinel/solarwinds-post-compromise-hunting-with-azure-sentinel/ba-p/1995095](https://techcommunity.microsoft.com/t5/azure-sentinel/solarwinds-post-compromise-hunting-with-azure-sentinel/ba-p/1995095)

> To hunt for similar TTPs used in this attack, a good place to start is to build an inventory of the machines that have SolarWinds Orion components. Organizations might already have a software inventory management system to indicate hosts where the SolarWinds application is installed. Alternatively, Azure Sentinel could be leveraged to run a simple query to gather similar details. Azure Sentinel collects data from multiple different logs that could be used to gather this information. For example, through the recently released Microsoft 365 Defender connector, security teams can now easily ingest Microsoft 365 raw data into Azure Sentinel. Using the ingested data, a simple query like below can be written that will pull the hosts with SolarWinds process running in last 30 days based on Process execution either via host on boarded to Sentinel or on boarded via Microsoft Defender for Endpoints (MDE). The query also leverages the Sysmon logs that a lot of customers are collecting from their environment to surface the machines that have SolarWinds running on them. Similar queries that leverage M365 raw data could also be run from the M365's Advanced hunting portal.


Centralising the log data into something like Azure Sentinel, or other SIEM tools should allow you to hunt through your network looking for evidence of the product and the network based indicators of compromise.  If you are unlucky enough to have been targeted with the second stages, you'll also want these kinds of detective capabilities to look for network intrusion and lateral movement to further compromise the system.


## [Dealing with the SolarWinds Orion compromise - NCSC.GOV.UK](https://www.ncsc.gov.uk/guidance/dealing-with-the-solarwinds-orion-compromise)

[https://www.ncsc.gov.uk/guidance/dealing-with-the-solarwinds-orion-compromise](https://www.ncsc.gov.uk/guidance/dealing-with-the-solarwinds-orion-compromise)

> Find out if you have an affected system
> Identify if you have a product from the SolarWinds Orion suite versions 2019.4 to 2020.2.1 HF1 inclusive. SolarWinds Orion suite consists of several products - for exact product versions see the SolarWinds advisory.
> If you are able to, check any internet web proxy, DNS proxy, or firewall logs for connections to the legitimate Solarwinds update site of downloads.solarwinds.com. This may help in identifying possible Orion Suite products. (Note, this will likely identify any SolarWinds products, not just the Orion Suite).
> If you find any Orion Suite products on your network, then check for a file named SolarWinds.Orion.Core.BusinessLayer.dll, and generate a SHA-256 hash of the file. You can use the Powershell command Get-FileHash to do this. Upload this hash to VirusTotal and check if it is detected as malicious. If it is detected then you have a copy of SolarWinds that has maliciously added functionality. This DLL is referred to as SUNBURST by FireEye.
> Check any internet web proxy, DNS proxy or firewall logs for connections to any sub-domain of avsvmcloud[.]com (which is used for command and control by the initial backdoor).


This by the NCSC is a good flow chart of what you should do.  Simple pragmatic detection advice here, check outbound DNS and Proxy logs for evidence of the compromise, and check the hash of the file to see if it's known malicious. 


## [Highly Evasive Attacker Leverages SolarWinds Supply Chain to Compromise Multiple Global Victims With SUNBURST Backdoor | FireEye Inc](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)

[https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)

> FireEye has uncovered a widespread campaign, that we are tracking as UNC2452. The actors behind this campaign gained access to numerous public and private organizations around the world. They gained access to victims via trojanized updates to SolarWind’s Orion IT monitoring and management software. This campaign may have begun as early as Spring 2020 and is currently ongoing. Post compromise activity following this supply chain compromise has included lateral movement and data theft. The campaign is the work of a highly skilled actor and the operation was conducted with significant operational security.
> 
> SUNBURST Backdoor
> SolarWinds.Orion.Core.BusinessLayer.dll is a SolarWinds digitally-signed component of the Orion software framework that contains a backdoor that communicates via HTTP to third party servers. We are tracking the trojanized version of this SolarWinds Orion plug-in as SUNBURST.
> 
> After an initial dormant period of up to two weeks, it retrieves and executes commands, called “Jobs”, that include the ability to transfer files, execute files, profile the system, reboot the machine, and disable system services. The malware masquerades its network traffic as the Orion Improvement Program (OIP) protocol and stores reconnaissance results within legitimate plugin configuration files allowing it to blend in with legitimate SolarWinds activity. The backdoor uses multiple obfuscated blocklists to identify forensic and anti-virus tools running as processes, services, and drivers.
> 
> [...]
> 
> TEARDROP and BEACON Malware Used
> 
> Multiple SUNBURST samples have been recovered, delivering different payloads. In at least one instance the attackers deployed a previously unseen memory-only dropper we’ve dubbed TEARDROP to deploy Cobalt Strike BEACON.


This is the report that kicked it all off.  After the FireEye incident last week, we all knew that this was a capable actor, but FireEye's note here that they had a trojanized version of Solarwinds Orion is what caused everyone to start looking.  The key thing here is that this software makes calls back to the C2 infrastructure, but not straightaway, instead it waits up to 2 weeks.  If you applied an update and immedietely it started beaconing, you'd be far more likely to notice.  But we install and change software constantly, by 2 weeks later it's much harder to start to correlate the new network traffic with the software that changed a few weeks back.  

Of course, it helps that the software also obfuscates the command and control traffic, so to any analyst, it does look like legitimate traffic.  It would be very difficult to detect that this was unusual behaviour, or that this traffic should be blocked.


## [Hackers last year conducted a 'dry run' of SolarWinds breach](https://news.yahoo.com/hackers-last-year-conducted-a-dry-run-of-solar-winds-breach-215232815.html?guccounter=1)

[https://news.yahoo.com/hackers-last-year-conducted-a-dry-run-of-solar-winds-breach-215232815.html?guccounter=1](https://news.yahoo.com/hackers-last-year-conducted-a-dry-run-of-solar-winds-breach-215232815.html?guccounter=1)

> The hackers distributed malicious files from the SolarWinds network in October 2019, five months before previously reported files were sent to victims through the company’s software update servers. The October files, distributed to customers on Oct. 10, did not have a backdoor embedded in them, however, in the way that subsequent malicious files that victims downloaded in the spring of 2020 did, and these files went undetected until this month.
> 
> “We’re thinking they wanted to test whether or not it was going to work and whether it would be detected. So it was more or less a dry run,” a source familiar with the investigation told Yahoo News. “They took their time. They decided to not go out with an actual backdoor right away. That signifies that they’re a little bit more disciplined and deliberate.”
> 
> The October files were discovered in the systems of several victims, but investigators have so far found no signs that the hackers engaged in any additional malicious activity on those systems after the files landed on them.


Let's start with the background.  This is a highly competent attacker.  They had access, and could have used it.  But instead they used their access to modify the files, and they stopped and waiting.  Presumably they watched to see if anyone noticed, to see where the files turned up, and to make sure that they could make the changes without being noticed.


