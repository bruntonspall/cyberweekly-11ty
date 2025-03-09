---
title: "184 - How much trust in zero-trust do you have?"
date: 2022-02-13
description: "Zero-trust is the new saviour of all of our security woes, but I suspect that the effort and impact of it is wildly underestimated by most people."
permalink: /how-much-trust-in-zero-trust-do-you-have/
---

Zero-trust is the new saviour of all of our security woes, but I suspect that the effort and impact of it is wildly underestimated by most people.

It's not even really clear what it means in most cases.  Take the rather excellent [zero-trust memo from the US Government](https://www.whitehouse.gov/wp-content/uploads/2022/01/M-22-09.pdf) that I linked to last week:

> 1. Federal staff have enterprise-managed accounts, allowing them to access everything they
need to do their job while remaining reliably protected from even targeted, sophisticated
phishing attacks.
> 2. The devices that Federal staff use to do their jobs are consistently tracked and monitored,
and the security posture of those devices is taken into account when granting access to
internal resources.
> 3. Agency systems are isolated from each other, and the network traffic flowing between
and within them is reliably encrypted.
> 4. Enterprise applications are tested internally and externally, and can be made available to
staff securely over the internet.
> 5. Federal security teams and data teams work together to develop data categories and
security rules to automatically detect and ultimately block unauthorized access to
sensitive information.

This all sounds easy right?  Ensure that everyone has access to an enterprise-managed identity account, and that they use securely managed devices.

That's really easy for your core staff, but what are you going to do about those contract developers you bought in?  They might argue that to retain their status as an independent contractor (rather than say a disguised employee), that they need to provide their own tools, their own devices.  They might work for 3 or 4 or 5 organisations, so which of those organisations gets to manage that device?

What if your DevOps team is a managed service from a provider?  Should you ensure they have strong identities in your system, or a strong identity in the managed providers organisation?  We can do federated trust systems now, but how much faith do you have in it?  Most of the federated systems I've seen allow you to verify that an account is live, that it is authenticated properly, but it's very difficult to ask questions of the security related properties.  Did that user authenticate recently?  Today? In the last week?  Have they time travelled or journeyed to a new location?  Did they use an MFA to login?

And of course, that's just the first of those features.

One of the common mantras of zero-trust is that you no longer need to come back to a central corporate VPN as part of the zero-trust strategy.  If your applications and systems are "available over the internet", then there's no need to force device traffic back through a corporate VPN.  

But as we've seen in recent weeks, exposing more and more services over the internet, such as QNAP NAS devices, increases the potential attack surface of the organisation, and if flaws are found in the software, then you have fewer guardrails between the attackers and the system.

The key here for zero-trust is to recognise that at best, it's an unachievable goal, but one that we should aim for.  Moving, in particular, legacy systems that rely on VPN or network access as the only access control to something far more limited is work that you should be doing.  Of course that work is always hard to justify to boards, because the business gains no actual improvement, the system should work exactly the same after the work is done.  If you can hook that legacy uplift into your shiney new "Zero-trust" strategy, you might be able to fund an uplift of some of the shonkiest systems.

Of course none of this is new, indeed the [Jericho Forum, as part of the Open Group](https://www.opengroup.org/forum/security/zerotrust) started work on " de-perimeterisation" back in around 2004, but the first major implementation of the idea at a fully corporate level was Google's Beyond Corp (or at least, the first proper public description of it that I'm aware of).

If you are embarking on this journey, then the [Google Beyond Corp publications](https://cloud.google.com/beyondcorp) are well worth a read. As well as the one below, which in 2014 kicked a lot of this off, I'd recommend the rather well written ["How we migrated"](https://research.google/pubs/pub46134/), for a good dose of reality, as well as a good plan.  Just remember, you are probably not Google, so you don't have the same resources and accesses that they do.

## [BeyondCorp: A New Approach to Enterprise Security – Google Research ](https://research.google/pubs/pub43231/)

[https://research.google/pubs/pub43231/](https://research.google/pubs/pub43231/)

> Virtually every company today uses firewalls to enforce perimeter security. However, this security model is problematic because, when that perimeter is breached, an attacker has relatively easy access to a company’s privileged intranet. As companies adopt mobile and cloud technologies, the perimeter is becoming increasingly difficult to enforce. Google is taking a different approach to network security. We are removing the requirement for a privileged intranet and moving our corporate applications to the Internet. 


If you’ve never read it, this is the seminal paper on Zero Trust.  

It’s worth reading, if only to understand how much work it was for Google, an organisation famous for building everything themselves internally, and thus with access to the source code and engineering capability to modify every part of their corporate system.

It took Google five years to roll out BeyondCorp, and doing so in an incremental way that doesn’t break everything was a critical part of that process. 


## [State of Cloud Security Concerns | CSA](https://cloudsecurityalliance.org/artifacts/state-of-cloud-security-concerns-challenges-and-incidents/)

[https://cloudsecurityalliance.org/artifacts/state-of-cloud-security-concerns-challenges-and-incidents/](https://cloudsecurityalliance.org/artifacts/state-of-cloud-security-concerns-challenges-and-incidents/)

> The use of cloud services has continued to increase over the past decade. Particularly in the wake of the COVID-19 public health crisis, many enterprises’ digital transformations are on an accelerated track to enable employees to work from home. AlgoSec, a leading network security solution provider, commissioned CSA to develop a survey to add to the industry’s knowledge about hybrid-cloud and multi-cloud security. This report of the survey’s findings will help you better understand the current cloud security landscape, including the most pressing concerns, challenges, and incidents.
> 
> Questions We Asked:
> 
>     What is the current state of cloud usage? What do organizations estimate their usage to be in the future?
>     What are the current security concerns regarding cloud adoption and deployment?
>     What security tools are organizations using?
>     What are the causes of cloud-related security incidents?
>     What types of security incidents have organizations had and how disruptive were they?
> 
> Key Takeaways:
> 
>     Organizations are continuing to move to complex cloud environments
>     Cloud providers’ native security controls are not enough for many organizations
>     Organizations look for security tools that can supplement their workforce
>     Network security is the top cloud adoption concern
> 
> Organizations have increasingly turned to cloud providers’ additional security controls and virtual firewalls. The use of cloud providers’ additional security controls jumped from 58% in 2019 to 71% in 2021. Approximately half of the organizations turned to third party providers for virtual editions of firewalls for network security controls. This could indicate that while many organizations are moving to public cloud, many are still utilizing legacy and hybrid environments, and need uniform control across many different environments. Additionally, with the current health crisis and the dramatic increase in remote workers, many organizations are unable to secure their network as they have previously and must turn to additional and alternative security controls


This is an interesting report, but this stood out to me.  I suspect that the use of non-cloud native firewalls and traditional security tools in VM's is more likely from poor compliance audits that expect traditional firewalls than anything else.

When moving to cloud based architectures, traditional approaches are no longer suited.  We need to ensure that we are using cloud native security controls.


## [Helping users stay safe: Blocking internet macros by default in Office - Microsoft Tech Community ](https://techcommunity.microsoft.com/t5/microsoft-365-blog/helping-users-stay-safe-blocking-internet-macros-by-default-in/ba-p/3071805)

[https://techcommunity.microsoft.com/t5/microsoft-365-blog/helping-users-stay-safe-blocking-internet-macros-by-default-in/ba-p/3071805](https://techcommunity.microsoft.com/t5/microsoft-365-blog/helping-users-stay-safe-blocking-internet-macros-by-default-in/ba-p/3071805)

> We’re introducing a default change for five Office apps that run macros: 
> 
> **VBA macros obtained from the internet will now be blocked by default.** 
> 
> For macros in files obtained from the internet, users will no longer be able to enable content with a click of a button. A message bar will appear for users notifying them with a button to learn more. The default is more secure and is expected to keep more users safe including home users and information workers in managed organizations. 


This is really good news.  Macros are still heavily used in phishing emails and other initial accesses.  Making it much harder to run macros in documents downloaded from the internet will make us all safer.

Of course, there are plenty of other vulnerabilities that phishers can exploit, but at least this will mean that this particular one will be far less of an issue for organisations. 


## [Alpha-Omega - Open Source Security Foundation ](https://openssf.org/community/alpha-omega/)

[https://openssf.org/community/alpha-omega/](https://openssf.org/community/alpha-omega/)

> **The Alpha-Omega Project will improve global open source software (OSS) supply chain security by working with project maintainers to systematically look for new, as-yet-undiscovered vulnerabilities in open source code, and get them fixed.** 
> 
> “Alpha” will work with the maintainers of the most critical open source projects to help them identify and fix security vulnerabilities, and improve their security posture.
> 
> “Omega” will identify at least 10,000 widely deployed OSS projects where it can apply automated security analysis, scoring, and remediation guidance to their open source maintainer communities. 


Even more good news.  In this day of the open source supply chain, vulnerabilities will lead to security departments in essence saying no to any use of open source.

We’ve already seen some open source projects being sent information assurance questionnaires, and of course in many cases they make no sense - “Do you use a VPN on your corporate devices” being a good example of a question that makes no sense if you are a full time open source contributor.

Securing the supply chain by improving the quality of open source projects is a good way to lift the security of all the upstream users as well 


## [CVE-2022-0329 and the problems with automated vulnerability management | Tom Forbes](https://tomforb.es/cve-2022-0329-and-the-problems-with-automated-vulnerability-management/)

[https://tomforb.es/cve-2022-0329-and-the-problems-with-automated-vulnerability-management/](https://tomforb.es/cve-2022-0329-and-the-problems-with-automated-vulnerability-management/)

> As far as I can gather the maintainer was pressured into merging something despite completely valid objections and a rather heated discussion, which resulted in the huntr report being closed. Some automated processes kicked in and a CVE was issued, which made its way into the Github advisory database with a rather weak “The maintainer disputes the issue” comment in the description.
> 
> Automated vulnerability systems like Github advisories and Snyk are great steps forward. But as bug bounty programs proliferate so do the number of useless + spammy reports, as anyone who has run such a program will attest. If we build a system where these reports can, accidentally or maliciously, make their way into the Official List Of All Security Issues That You Must Take Action On For Complaince Reasons with no human oversight then we’re in for a bad time


This was a fascinating story.  Was it a vulnerability?  The maintainer argues that it's not a vulnerability, and their argument isn't a bad argument.  The vulnerability finder is arguing that the library is using a known bad function, and that users of their library could wire things up in a bad way, potentially without knowing.

What's clear is that it almost certainly shouldn't have been registered as such a serious vulnerability, and of course all of the automated systems that then triggered off of that can be a further issue.

This problem is going to get worse before it gets better


## [Meta's Adversarial Threat Report | Meta](https://about.fb.com/news/2021/12/metas-adversarial-threat-report/)

[https://about.fb.com/news/2021/12/metas-adversarial-threat-report/](https://about.fb.com/news/2021/12/metas-adversarial-threat-report/)

> The global threats we tackle have significantly evolved since we first started sharing our findings about Coordinated Inauthentic Behavior in 2017. In addition, adversarial networks don’t strive to neatly fit our policies or only violate one at a time. To account for this constantly shifting threat environment, we build our defenses with the expectation that they will not stop, but rather adapt and try new tactics. We add new layers of defense to address potential gaps from multiple angles. Our goal over time is to make these behaviors more costly and difficult to hide, and less effective.
> 
> Today, we’re sharing our first report that brings together multiple network disruptions for distinct violations of our security policies: Coordinated Inauthentic Behavior and two new protocols — Brigading and Mass Reporting. We shared our findings with industry peers, independent researchers, law enforcement and policymakers so we can collectively improve our defenses. We welcome feedback from external experts as we refine our approaches and reporting.


Facebook (or now Meta as they'd prefer to be known) is reporting the takedown of not only disinformation networks (or coordinated inauthentic behaviour as they'd prefer it be known), but also two new tactics from coordinated groups: 

Brigading, which is mass commenting or mass behaviour designed to swing the network but look like lots of authentic accounts.  

Mass reporting, which is brigading to coordinate reporting, where you get lots of your followers to authentically or inauthentically report a user or post incorrectly.

Note that if you run any form of social commenting or community features in your systems or services, this is the sort of behaviours that you will see eventually.


## [30, 60, 90 Day Plan For New Security Leaders ](https://www.lastweekasavciso.com/p/thirty-sixty-ninety-day-plan-security-leadership)

[https://www.lastweekasavciso.com/p/thirty-sixty-ninety-day-plan-security-leadership](https://www.lastweekasavciso.com/p/thirty-sixty-ninety-day-plan-security-leadership)

> * Check for the basics
> 
>    * Logging / Operations
>    * Incident Response Plan
> 
>        * This is super important as an incident can happen at any time. Hopefully not in the first week the person starts, but we don’t always have that luxury. 
> 
>    * Endpoint Security
>    * Onboarding / Offboarding / Security Awareness 


This is a great set of plans if you’ve moved organisation, or just been handed a whole new area to look over.

Even if you just want to refresh what you are doing, this is a good checklist to check your organisation against 


## [The C-Suite guide to simplifying for cyber readiness, today and tomorrow: PwC](https://www.pwc.com/us/en/services/consulting/cybersecurity-privacy-forensics/library/global-digital-trust-insights.html#content-free-1-be77)

[https://www.pwc.com/us/en/services/consulting/cybersecurity-privacy-forensics/library/global-digital-trust-insights.html#content-free-1-be77](https://www.pwc.com/us/en/services/consulting/cybersecurity-privacy-forensics/library/global-digital-trust-insights.html#content-free-1-be77)

> Is the business world now too complex to secure? Leaders are sounding the alarm. Some 75% of respondents to our 2022 Global Digital Trust Insights Survey say that too much avoidable, unnecessary organisational complexity poses “concerning” cyber and privacy risks.
> 
> But because some complexities are necessary, your enterprise shouldn’t streamline and simplify its operations and processes thoughtlessly, but consciously and deliberately.
> 
> This 2022 Global Digital Trust Insights Survey offers the C-suite a guide to simplifying cyber with intention. It focuses on four questions that tend to get short shrift but, if properly considered, can yield significant dividends.
> 
> These questions may surprise and even challenge you because, in a survey about data trust, they aren’t technology-centered. Tech, in itself, is not the answer to simplified security.


2022 is set to be a big year in cyber security.  Firms are realising the climatic risks that they face, and are forecasting a need to spend and manage that risk effectively.

The survey here shows that there's a huge rise in CEO engagement in cybersecurity matters, and about 2/3rds of organisations expect an increased budget next year.


## [Solana DeFi Project Known as Wormhole Hit With Potential $320 Million Hack - Bloomberg](https://www.bloomberg.com/news/articles/2022-02-02/blockchain-bridge-wormhole-hit-with-potential-315-million-hack)

[https://www.bloomberg.com/news/articles/2022-02-02/blockchain-bridge-wormhole-hit-with-potential-315-million-hack](https://www.bloomberg.com/news/articles/2022-02-02/blockchain-bridge-wormhole-hit-with-potential-315-million-hack)

> Wormhole, a communication bridge between Solana and other decentralized-finance blockchain networks, said all funds have been restored and the platform is back up after hackers stole about $320 million in cryptocurrency.
> 
> The online thieves made away with 120,000 wETH, or so-called wrapped Ether, the project’s team said on Twitter Wednesday. On Thursday morning, the team said “all funds have been restored,” without specifying the source of the funding. Earlier, the project pledged to add Ether to ensure the wETH is backed one-for-one. 
> 
> The vulnerability has been patched, Wormhole management said on the project’s Telegram channel on Thursday, reassuring users that funds are safe. It added an official statement and incident report would be issued in due course. 
> 
> The hack is one of the largest thefts from a DeFi protocol, which bill themselves as allowing users to bypass traditional intermediaries to borrow and lend digital assets with the added feature of anonymity. 
> 
> “This demonstrates once again that the security of DeFi services has not reached a level that is appropriate for the huge sums being stored within them,” said Tom Robinson, co-founder of blockchain analysis firm Elliptic. “The transparency of the blockchain is allowing attackers to identify and exploit major bugs.”  


A $10m bug bounty, and around a $320m potential payout is madness for projects that are run via telegram and in essence a very small number of software developers, backed by a VC that is willing to write off an extra $320m in ETH.

Of course, all the values in here are based on the assumption that someone could turn those into cash.  Attempting to turn $320m of ETH into hard currency would likely drive down the value of ETH at the same time, and reduce the total payout.

The [Incident report](https://wormholecrypto.medium.com/wormhole-incident-report-02-02-22-ad9b8f21eec6) is worth a read as well


## [An incomplete history of Forbes.com as a platform for scams, grift, and bad journalism | Nieman Journalism Lab ](https://www.niemanlab.org/2022/02/an-incomplete-history-of-forbes-com-as-a-platform-for-scams-grift-and-bad-journalism/)

[https://www.niemanlab.org/2022/02/an-incomplete-history-of-forbes-com-as-a-platform-for-scams-grift-and-bad-journalism/](https://www.niemanlab.org/2022/02/an-incomplete-history-of-forbes-com-as-a-platform-for-scams-grift-and-bad-journalism/)

> Forbes’ staff of journalists could produce great work, sure. But there were only so many of them, and they cost a lot of money. Why not open the doors to Forbes.com to a swarm of outside “contributors” — barely vetted, unedited, expected to produce at quantity, and only occasionally paid? (Some contributors received a monthly flat fee — a few hundred bucks — if they wrote a minimum number of pieces per month, with money above that possible for exceeding traffic targets. Others received nothing but the glory.)
> 
> As of 2019, almost 3,000 people were “contributors” — or as they told people at parties, “I’m a columnist for Forbes.”
> 
> Let’s think about incentives for a moment. Only a very small number of these contributors can make a living at it — so it’s a side gig for most. The two things that determine your pay are how many articles you write and how many clicks you can harvest — a model that encourages a lot of low-grade clickbait, hot takes, and deceptive headlines. And many of these contributors are writing about the subject of their main job — that’s where their expertise is, after all — which raises all sorts of conflict-of-interest questions. And their work was published completely unedited — unless a piece went viral, in which case a web producer might “check it more carefully.”
> 
> All of that meant that Forbes suddenly became the easiest way for a marketer to get their message onto a brand-name site.
> 
> And since this strategy did build up a ton of new traffic for Forbes — publishing an extra 8,000 pieces a month will do that! — lots of other publications followed suit in various ways.


Wonderful bit of journalism here and a great reminder of how the incentives for the big media companies that we “trust” are misaligned.  

There’s lots and lots of reasons for organisations like Forbes to add these clickbait style contributors, and generally speaking, the vast majority of the internet doesn’t care how truthful or accurate the articles are.  There’s not much money in careful effective and nuanced reporting, and lots of money in creating content farms.

As the article points out, there are however some online publications, such as Medium, that trade on the value chain here without having an established brand to go with it. 

Oh, and in case you missed it, this is all off of the back of the $4.5bn (yes **billion**) indictment and recovery of stolen bitcoins.  There's going to be a really interesting question somewhere in the US State Department about what they actually do with the bitcoin that they have.  It's not like they can just pass it to the US Treasury and use it to fund the Federal Government, so presumably they'll want to liquidate it at some point, but I have no idea what will happen when the US Government puts 94,000 BTC out on the open mark, I suspect it won't be worth $4.5bn for very long for sure!


