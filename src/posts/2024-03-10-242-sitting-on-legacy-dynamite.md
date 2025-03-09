---
title: "242 - Sitting on legacy dynamite"
date: 2024-03-10
description: "We all use the term \"legacy\" when talking about IT, but it's rare that organisations actually recognise the real risk that it poses."
permalink: /sitting-on-legacy-dynamite/
---

We all use the term "legacy" when talking about IT, but it's rare that organisations actually recognise the real risk that it poses.

We know that it can costs tens or hundreds of millions to recover from a cyber attack, but for some reason, the idea of investing that same money into remediating the legacy IT problem is hard for boards to swallow.

The British Library report is damning in being clear that the real culprit here is the years of IT neglect at play.  It's not that anyone wanted to neglect the systems, it's more that the cost of doing something about it seemed so high that it was easier to outsource the management and push the problems into the next year.

Of course, this strategy works 9 times out of 10, because cyber attacks are somewhat random, so you may not get compromised this year, or even next year, but you are reliant on luck rather than anything else.

As Alyssa Miller points out, we really don't have a healthy conversation about how to deal with the legacy problem, and I think that's why boards don't invest in it.  All suggestions end up being about investing hundreds of millions in rebuilding everything from scratch, or expensive, cumbersome and difficult migrations.  This lack of good options means that we choose to "accept the risk" and keep going forward with the plans that further the mission of the organisation instead, and it's hard to fault most boards for choosing that option given the proposals.

So how do we deal with legacy systems?  I think we have to be clearer about what bits of new fangled approaches like Zero Trust apply to them, and where they can help.  We should be using the excitement of boards in new technologies like AI help to migrate some of the worst managed datastores into new locations that are more secure and better monitored.  We need to recognise that "backward compatibility" is important and provide ways for those other systems to still integrate with the new system, while uplifting the security model  that underlies the system.  Even defining which systems are supposed to access data and how can help identify where access permissions are too granular and risk is being taken.

We need to recognise that big programmes of legacy remediation that do nothing but reduce risk are intrinsically not exciting to boards and senior leaders, and ensure that each step along the way can deliver value to the business.  This also requires us to take off our idealistic blinkers about perfect modern security systems and recognise that incremental improvements that reduce risk and critically reduce further blockers to improvement are worth while, even if they don't result in perfect security.

## [Learning lessons from the cyber-attack - Knowledge Matters blog ](https://blogs.bl.uk/living-knowledge/2024/03/learning-lessons-from-the-cyber-attack.html)

[https://blogs.bl.uk/living-knowledge/2024/03/learning-lessons-from-the-cyber-attack.html](https://blogs.bl.uk/living-knowledge/2024/03/learning-lessons-from-the-cyber-attack.html)

> The paper does not go into detail about costs, as the net financial impact of the attack is still under review, nor have we gone into detail about the organisation behind the attack, Rhysida, as this information is better available from other sources such as the specialist technology press.
> 
> Wherever possible, though, we have tried to err on the side of openness, and not everything here makes comfortable reading for ourselves as an organisation. We have significant lessons to learn about matters such as our historic reliance on a complex legacy infrastructure, which has affected our ability to restore services as quickly as we would have wished, and the varying effectiveness of different security measures across our digital estate.
> 
> […]
> 
> Our major software systems cannot be brought back in their pre-attack form, either because they are no longer supported by the vendor or because they will not function on the new secure infrastructure that is currently being rolled out. This includes our main library services platform, which supports services ranging from cataloguing and ingest of non-print legal deposit (NPLD) material to collection access and inter-library loan. Other systems will require modification or migration to more recent software versions before they can be restored in the new infrastructure.
> Our cloud-based systems, including finance and payroll, have functioned normally throughout the
> incident.
> 
> [… More from the PDF report]
> 
> The increasing use of third-party providers within our network, some of which has been due to capacity and capability constraints within Technology and elsewhere in the Library, was noted by the Library’s Corporate Information Governance Group (CIGG) in late 2022, and the increasing complexity of managing their access was flagged as a risk. A review of security provisions relating to the management of third parties was planned for 2024; and the tightening of access provisions that would be enabled by improvements to underlying computer and storage infrastructure and the migration of storage to the cloud, which is currently being implemented. Unfortunately, the attack occurred before these necessary pre-requisites for this work were completed.
> 
> In common with other on-premise servers, this terminal server was protected by firewalls and virus software, but access was not subject to Multi-Factor Authentication (MFA). MFA was introduced across the Library in 2020 to increase protection of all remote activities relating to cloud applications such as email, Teams and Word, but for reasons of practicality, cost and impact on ongoing Library programmes, it was decided at this time that connectivity to the British Library domain (including machine log-on access and access to on-premise servers) would be out of scope for MFA implementation, pending further renewal of the Library’s infrastructure. The lack of MFA on the domain was identified and raised as a risk at this time, but the possible consequences were perhaps under-appraised. In mitigation of this risk, it was noted that all Library domain services, including this terminal server, were subject to routine security assessments, and additional measures were implemented on the server to mitigate risk including copy/paste prevention and hardening of security settings to recognised Centre for Internet Security (CIS) standards. The Library also undertakes security assessments including penetration tests where appropriate. 


You couldn’t ask for a more transparent and open [report](https://www.bl.uk/home/british-library-cyber-incident-review-8-march-2024.pdf) than this, and boy does it deliver.  We can look at the specific controls that failed in this case, such as the use of outsourced managed service providers who needed remote access to the core of the British Library system while not investing in MFA or other controls that would limit the risk of a compromised account.

But to stop there would be to miss the issue here.  The issue here is potentially decades of underinvestment in IT systems, leaving them with a mess of “legacy systems” that were difficult to manage and made applying those controls significantly more complex and difficult to implement.

This paper really sets out just why legacy IT systems are so catastrophically bad for cyber security, and why “just apply MFA” is not sufficient.  We need a far more strategic recognition of the risks and why investment is so critical to ensure the security of our systems 


## [Alyssa Miller on X ](https://twitter.com/AlyssaM_InfoSec/status/1766497444211184073)

[https://twitter.com/AlyssaM_InfoSec/status/1766497444211184073](https://twitter.com/AlyssaM_InfoSec/status/1766497444211184073)

> There's going to be a lot of people dunking on CISA after this, this tweet ain't one of them. However their response about older systems set for replacement does highlight something I've been saying about CISA's guidance for a while.
> 
> IMHO too much of the guidance has been pie in the sky, aspirational, and idealistic. Just patch your shit, use MFA everywhere, only use PKI or FIDO hard tokens for MFA because everything else is not phishing resistant, etc.
> 
> Now this has gotten better over the last year or two, with at least more specific threat Intel, especially around exploited-in-the-wild vulnerabilities. However this event highlights that even CISA struggles with the same struggles every organization has.
> 
> It's easy to talk about doing the right things universally, but where we still have a gap in guidance across the board (not just from CISA) is how to defend those exception cases that keep us from doing the right things universally. They're always the risk that gets realized.
> 
> We need to accept that there are always going to be systems that require mitigation because they can't just be fixed and they can't just be turned off. So I think we continue to need more conversation around what those mitigations look like. How do we protect such systems?
> 
> And those conversations have to center on actionable steps, again not idealism or the next blinky light product that's going to save the world. What can companies realistically use, that they already have, to mitigate the threats. That's the conversation we need. 


This is very similar to my take, and Alyssa knows her stuff far better than I do.  Our advice and guidance does need to take into account the reality on the ground for most organisations, which is massive amounts of legacy systems over which there is likely little control or even awareness. 


## [CISA forced to take two systems offline last month after Ivanti compromise ](https://therecord.media/cisa-takes-two-systems-offline-following-ivanti-compromise)

[https://therecord.media/cisa-takes-two-systems-offline-following-ivanti-compromise](https://therecord.media/cisa-takes-two-systems-offline-following-ivanti-compromise)

> “The impact was limited to two systems, which we immediately took offline. We continue to upgrade and modernize our systems, and there is no operational impact at this time,” the spokesperson said.
> 
> “This is a reminder that any organization can be affected by a cyber vulnerability and having an incident response plan in place is a necessary component of resilience.”
> 
> CISA declined to answer a range of questions about who was behind the incident, whether data had been accessed or stolen and what systems were taken offline. Ivanti makes software that organizations use to manage IT, including security and system access.
> 
> A source with knowledge of the situation told Recorded Future News that the two systems compromised were the IP Gateway, which houses critical information about the interdependency of U.S. infrastructure, and the Chemical Security Assessment Tool (CSAT), which houses private sector chemical security plans. CISA declined to confirm or deny whether these are the systems that were taken offline.
> 
> CSAT houses some of the country’s most sensitive industrial information, including the Top Screen tool for high-risk chemical facilities, Site Security Plans and the Security Vulnerability Assessments. 


As CISA says, anyone can be affected by this kind of thing, and in the case where you worry or think that a system might be able to be compromised, the ability to act is crucial.

One of the things you should consider in your operational runbooks is a rough determination of impact if the system has to be taken down for minutes, hours, days or weeks.  Knowing what the impacts are and pre-agreeing the thresholds at which they’ll apply enables your first responders to know whether taking a system offline while they conduct tests or patching is acceptable.

There are a surprisingly high number of our IT systems that could probably suffer a few hours or even days of downtime while the patch process was organised and applied, and companies would prefer that over having to handle a breach 


## [TeamCity hit by critical software supply chain bugs ](https://www.csoonline.com/article/1311593/teamcity-hit-by-critical-software-supply-chain-bugs.html)

[https://www.csoonline.com/article/1311593/teamcity-hit-by-critical-software-supply-chain-bugs.html](https://www.csoonline.com/article/1311593/teamcity-hit-by-critical-software-supply-chain-bugs.html)

> JetBrains is advising immediate patching of two new vulnerabilities affecting its TeamCity software, a CI/CD pipeline tool that can allow attackers to gain unauthenticated administrative access.
> 
> Tracked under CVE-2024-27198 and CVE-2024-27199, the critical bugs have already been fixed within TeamCity cloud servers with an on-premises patch available with version 2023.11.4.
> 
> “The vulnerabilities may enable an unauthenticated attacker with HTTP(S) access to a TeamCity server to bypass authentication checks and gain administrative control of that TeamCity server,” JetBrains said in a blog post on the issue. “The vulnerabilities affect all TeamCity On-Premises versions through 2023.11.3.” 


I’ve talked before about how critical your build servers are.  It’s also worth flagging that even if your build servers are internal to your network, constructing a mechanism to make a web based call to a TeamCity server on your internal network is not a particularly difficult attack, everything from dependency confusion attacks, CSRF as well as just phishing links or documents with macro’s can potentially make one of these calls.

You should patch rather than trusting on network isolation for this one 


## [3 mistakes I’ve made at the beginning of an incident (and how not to make them) | FireHydrant ](https://firehydrant.com/blog/3-mistakes-ive-made-at-the-beginning-of-an-incident-and-how-not-to-make-them/)

[https://firehydrant.com/blog/3-mistakes-ive-made-at-the-beginning-of-an-incident-and-how-not-to-make-them/](https://firehydrant.com/blog/3-mistakes-ive-made-at-the-beginning-of-an-incident-and-how-not-to-make-them/)

> The first few minutes of an incident are often the hardest. Tension and adrenaline levels are high, and if you don’t have a [well-documented incident management plan](https://firehydrant.com/blog/incident-management-best-practices-before-the-incident/) in place, mistakes are inevitable.
> 
> It was actually the years I spent managing incidents without the right tools in those high-tension moments that inspired me to build [FireHydrant](https://firehydrant.com/how-it-works/) . I built the tool I wished I’d had when I was trying to move fast at the start of incidents. 
> 
> Let’s look at three mistakes I’ve made during those stressful moments during the beginning of an incident — and discuss how you can avoid making them. 
> 
> Mistake 1: We didn’t have a plan. 


This is a nice set of notes for how to prepare yourself for incident readiness, and make sure that you don't end up burned out when something happens.  Always make sure you have a plan, that everyone knows what it is and how to find it and follow it.


## [Steve T. on LinkedIn: ⚡ For some organisations, their biggest threat is……themselves. 😢 I’m… | 20 comments ](https://www.linkedin.com/posts/steventownsley_for-some-organisations-their-biggest-threat-activity-7167793023513280512-7YtZ?utm_source=share&utm_medium=member_ios)

[https://www.linkedin.com/posts/steventownsley_for-some-organisations-their-biggest-threat-activity-7167793023513280512-7YtZ?utm_source=share&utm_medium=member_ios](https://www.linkedin.com/posts/steventownsley_for-some-organisations-their-biggest-threat-activity-7167793023513280512-7YtZ?utm_source=share&utm_medium=member_ios)

> ⚡ For some organisations, their biggest threat is……themselves.
> 
> 😢 I’m not talking about insiders. I’m talking about the bureaucracy, politics, and structures which organisations cultivate which then makes security difficult.
> 
> […]
> 
> 👀 There's no point worrying about nation states and criminal groups if you can't defeat the enemy within first. 


This is really succinct and well put.  Before you start worrying about the really advanced stuff, you need to ensure that your organisation actually respects and values security 


## [GTPDOOR - A novel backdoor tailored for covert access over the roaming exchange - doubleagent.net ](https://doubleagent.net/telecommunications/backdoor/gtp/2024/02/27/GTPDOOR-COVERT-TELCO-BACKDOOR.html)

[https://doubleagent.net/telecommunications/backdoor/gtp/2024/02/27/GTPDOOR-COVERT-TELCO-BACKDOOR.html](https://doubleagent.net/telecommunications/backdoor/gtp/2024/02/27/GTPDOOR-COVERT-TELCO-BACKDOOR.html)

> GTPDOOR is the name of Linux based malware that is intended to be deployed on systems in telco networks adjacent to the GRX (GRPS eXchange Network) with the novel feature of communicating C2 traffic over [GTP-C (GPRS Tunnelling Protocol](https://en.wikipedia.org/wiki/GPRS_Tunnelling_Protocol) - Control Plane) signalling messages. This allows the C2 traffic to blend in with normal traffic and to reuse already permitted ports that maybe open and exposed to the [GRX network](https://en.wikipedia.org/wiki/GPRS_roaming_exchange) .The following diagram illustrates a forseen use of GTPDOOR. Here the actor already has established persistence on the roaming exchange network and access a compromised host by sending GTP-C Echo Request messages with a malicious payload:
> 
> ! [https://doubleagent.net/assets/images/gtpdoor/1.png](https://doubleagent.net/assets/images/gtpdoor/1.png) In addition to remote code execution capability, GTPDOOR can be beaconed by sending arbitrary TCP packets to a host the implant resides on. Supporting it’s stealth capability, the beacon response message hides particular information in a TCP header flag. 


This is a lovely writeup of the sort of advanced actor capability that most of us don’t have to worry about the majority of the time.   But it’s a good reminder that while we need to use the internet and telecoms providers as a matter of fact, we should threat model and assume that unknown levels of capability are being deployed at them all the time, and therefore we should treat them as a pure “untrusted bearer”.

This is why VPN’s or application level encryption is so important, as they protect against two major concerns.  Firstly the ability of someone who can control the underlying bearer to inspect and copy any packets that flow over the network.  But secondly, all good VPN’s and TLS implementations should allow you to detect and deal with impersonation attacks where your packets are routed to a different endpoint.

I’m generally opposed to the “VPN everything” approach when applied to individuals, as normal consumers ability to determine a good VPN from a not-good VPN is non-existent, but for your companies business purposes, you should definitely be using a VPN or TLS capability that you have trust in. 


## [Change Healthcare extortionists ALPHV get $22M in Bitcoin • The Register ](https://www.theregister.com/2024/03/04/alphv_ransom_payment/)

[https://www.theregister.com/2024/03/04/alphv_ransom_payment/](https://www.theregister.com/2024/03/04/alphv_ransom_payment/)

> Dmitry Smilyanets, an intelligence analyst at infosec outfit Recorded Future, spotted a Bitcoin wallet believed to be linked to ALPHV [received 350 Bitcoins](https://twitter.com/ddd1ms/status/1764639329165406497) , right now worth at least $22 million, in a single transaction on March 1.
> 
> Change's parent UnitedHealth Group declined to answer _The Register_ 's specific questions, including whether it paid off the ransomware gang. "We are focused on the investigation," spokesperson Tyler Mason told _The Register_ on Monday.
> 
> […]
> 
> It also appears ALPHV may have stolen the $22 million from its affiliate crew that attacked the healthcare IT provider in the first place. Gangs like the Russian-speaking ALPHV effectively rent out their ransomware to affiliates, who do the actual job of infecting victims and take a cut of any money paid to the malware's developers.
> 
> In a subsequent report, Recorded Future's Smilyanets shared a [screenshot](https://twitter.com/ddd1ms/status/1764639254016102410) of ALPHV's forum claiming to be written by the affiliate that broke into Change's network, deployed the BlackCat ransomware, and allegedly stole massive amounts of sensitive data.
> 
> According to the affiliate's post, after receiving the payment, ALPHV then suspended their account, "emptied the wallet and took all the money." 


As a reminder here, there is very little honour among theieves.  If you work in this area and get a big payout, then it’s not like you can take the original provider to court for failing to upkeep 


## [ComPromptMized ](https://sites.google.com/view/compromptmized)

[https://sites.google.com/view/compromptmized](https://sites.google.com/view/compromptmized)

> In the past year, numerous companies have incorporated Generative AI (GenAI) capabilities into new and existing applications, forming interconnected Generative AI (GenAI) ecosystems consisting of semi/fully autonomous agents powered by GenAI services. While ongoing research highlighted risks associated with the GenAI layer of agents (e.g., dialog poisoning, privacy leakage, jailbreaking), a critical question emerges: Can attackers develop malware to exploit the GenAI component of an agent and launch cyber-attacks on the entire GenAI ecosystem?This paper introduces Morris II, the first worm designed to target GenAI ecosystems through the use of adversarial self-replicating prompts. The study demonstrates that attackers can insert such prompts into inputs that, when processed by GenAI models, prompt the model to replicate the input as output (replication) and engage in malicious activities (payload). Additionally, these inputs compel the agent to deliver them (propagate) to new agents by exploiting the connectivity within the GenAI ecosystem. We demonstrate the application of Morris II against GenAI-powered email assistants in two use cases (spamming and exfiltrating personal data), under two settings (black-box and white-box accesses), using two types of input data (text and images). 


Absolutely fascinating, but like many academic papers not terribly well explained.

The basic concept is that an attacker talks to a system that both uses AI to generate a reply, and stores the information for later review.  A good example would be an email based contact system, so that when you email the system, it re-reads the previous emails to generate a new response.
If the first email contains a prompt injection attack, that attack is stored and reapplied each time it’s reused.  If that attack includes somehow a copy of itself, then the attack will be copied into each new victim as it’s executed, thus creating a worm like process.

The famous [Samy worm on MySpace](https://en.wikipedia.org/wiki/Samy_(computer_worm)) did something similar, each person who viewed the profile of an infected user would have their own profile, which meant it spread incredibly fast. 


## [Text-to-image AI models can be tricked into generating disturbing images | MIT Technology Review ](https://www.technologyreview.com/2023/11/17/1083593/text-to-image-ai-models-can-be-tricked-into-generating-disturbing-images/)

[https://www.technologyreview.com/2023/11/17/1083593/text-to-image-ai-models-can-be-tricked-into-generating-disturbing-images/](https://www.technologyreview.com/2023/11/17/1083593/text-to-image-ai-models-can-be-tricked-into-generating-disturbing-images/)

> These models convert text-based requests into tokens—breaking words up into strings of words or characters—to process the command the prompt has given them. SneakyPrompt repeatedly tweaks a prompt’s tokens to try to force it to generate banned images, adjusting its approach until it is successful. This technique makes it quicker and easier to generate such images than if somebody had to input each entry manually, and it can generate entries that humans wouldn’t imagine trying.
> 
> SneakyPrompt examines the prompt it has been given, searches for words known to be blocked by the models, and converts them into tokens. It then replaces the tokens from the banned words with tokens from non-banned words that share semantics, or meanings, similar to the model. For example, giving SneakyPrompt the target prompt “a naked man riding a bike” causes it to replace “naked” with the nonsense term “grponypui,” which the team successfully used to generate images of a naked man riding a bike 


As a reminder, the way that AI models work is horribly complex and since prompts are user controlled, it’s incredibly difficult to manage what your users do with the model underneath 


