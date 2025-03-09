---
title: "197 - Are we getting better or not?"
date: 2022-05-29
description: "It's incredibly difficult to legitimately measure our effectiveness at cybersecurity."
permalink: /are-we-getting-better-or-not/
---

It's incredibly difficult to legitimately measure our effectiveness at cybersecurity.

Security is one of those things, where if you spend money and "nothing happens", it's unclear whether your money made the nothing happen, or if nothing happened because nobody targeted you.

If nothing happened this year, should you keep spending the same amount, should you increase your budget, or are your defenses now good enough that you can cut your budget and spend it elsewhere?

Something interesting was noted in this years DBIR from Verizon.  Although for the last year, we've had a number of measurements showing that we're getting better at security, such as reducing time to patch, and better visibility meaning reduced time to notice a breach, one thing that stood out is that attackers have changed tactics, and are more likely to inform targets that they have been breached.

On the positive side, this means that if you haven't been subject to ransomware, then you are unlikely to have suffered a breach, because you'd know about it at least!

But determining the return on our security investment remains hard.  The most useful thing we can do is invest in detective tools that give us visibility in our network and visibility into the attacks that we suffer.  Endpoint Detection and Response tooling that can detect malware on our endpoints, network intrusion detection and detective tools like canaries and security log visibility tools all give us much greater visibility in the attacks that we see, and in whether our defences are working.

Final note, this week is half term in the UK, and an extra long bank holiday next weekend, so I'll be spending all my time with the family and away from work.  It's therefore unlikely that I'll read enough this week to produce a newsletter next weekend, so if you are UK based, enjoy the long weekend and I'll be back in two weeks.

## [2022 Data Breach Investigations Report | Verizon ](https://www.verizon.com/business/resources/reports/dbir/)

[https://www.verizon.com/business/resources/reports/dbir/](https://www.verizon.com/business/resources/reports/dbir/)

> **Know what your business is up against.**
> 
> ** 82%** of breaches involved the Human Element, including Social Attacks, Errors and Misuse. 
> **13%** increase in Ransomware breaches—more than in the last 5 years combined. 
> **62%** of incidents in the System Intrusion pattern involved threat actors compromising partners. 


The Verizon Data Breach Investigations report is always an interesting read, and they always pull out some interesting highlight stats.
In this case, the 2022 report is based on breaches reported from November 2020 to October 2021, meaning that it does include the Solarwinds breach of December 2020, but does not include the Log4J breach of December 2021.

One other interesting tidbit from here is that although, as has been reported elsewhere, average discovery time of breaches has come down from months to days, the disquiting side of that number is that there’s a huge increase in the number of people who discover the breach through “actor notification”.

That tells a story that we used to go months before we found evidence that hackers had been in the network and made off with data, but now they tend to contact us and tell us days after they get in, as part of a ransomware campaign.  That means that maybe we’re not getting as good at detecting these breaches as we’d like to imagine, it’s just a side effect as an industry, of ransomware becoming a profitable and working actor TTP. 


## [npm security update: Attack campaign using stolen OAuth tokens | The GitHub Blog ](https://github.blog/2022-05-26-npm-security-update-oauth-tokens/)

[https://github.blog/2022-05-26-npm-security-update-oauth-tokens/](https://github.blog/2022-05-26-npm-security-update-oauth-tokens/)

> Using their initial foothold of OAuth user tokens for GitHub.com, the actor was able to exfiltrate a set of private npm repositories, some of which included secrets such as AWS access keys.
> 
> Using one of these AWS access keys, the actor was able to gain access to npm’s AWS infrastructure.
> 
> With access to npm’s AWS infrastructure, the actor was able to exfiltrate an older backup of the skimdb.npmjs.com mirror, which included metadata and package manifests for all public and private packages in the npm registry as of April 7, 2021. This exfiltrated data includes READMEs, package version histories, maintainer email addresses, and package install scripts, but does NOT include the actual package artifacts, i.e., the tarballs themselves.


This was a smart actor, who put together a chain of attacks to move increasingly deeply into Github and NPM's infrastructure.  It looks like the attack was noticed and stopped before anything really significant happened, but those databases would enable an advanced actor with data analytical capabilities to start to develop a really advanced understanding of open source dependency chains and the level of maintenance to enable identification of weakpoints in our software supply chain.


## [Space Pirates: analyzing the tools and connections of a new hacker group ](https://www.ptsecurity.com/ww-en/analytics/pt-esc-threat-intelligence/space-pirates-tools-and-connections/)

[https://www.ptsecurity.com/ww-en/analytics/pt-esc-threat-intelligence/space-pirates-tools-and-connections/](https://www.ptsecurity.com/ww-en/analytics/pt-esc-threat-intelligence/space-pirates-tools-and-connections/)

> We assume that Space Pirates has Asian roots, as indicated by the active use of the Chinese language in resources, SFX archives, and paths to PDB files. In addition, the group's toolkit includes the Royal Road RTF (or 8.t) builder (common among hackers of Asian origin) and the PcShare backdoor, and almost all intersections with previously known activity are associated with APT groups in the Asian region.
> The group began its activity no later than 2017. The main targets of the criminals are espionage and theft of confidential information. Among the victims identified during the threat study are government agencies and IT departments, as well as aerospace and power enterprises in Russia, Georgia, and Mongolia. At least five organizations were attacked in Russia, one in Georgia, and the exact number of victims in Mongolia is unknown.
> Some APT group attacks using malware were also targeted at Chinese financial companies, which suggests a monetary motivation. All potential victims were notified by the respective national CERTs. 


Another reminder that just because a group comes from a certain region, or speaks a language, doesn’t necessarily mean that they have motives that align with the host state.  
Criminals can operate out of any jurisdiction, and while they might be culturally sympathetic to the aims of their host state, there is also a home based advantage in targeting their own country.  Criminals will find it easier to construct social lures, understand the motivations of individuals and find appropriate targets within their own country and culture than they do in other countries and other cultures 


## [Unknown APT group has targeted Russia repeatedly since Ukraine invasion | Malwarebytes Labs ](https://blog.malwarebytes.com/malwarebytes-news/2022/05/unknown-apt-group-has-targeted-russia-repeatedly-since-ukraine-invasion/)

[https://blog.malwarebytes.com/malwarebytes-news/2022/05/unknown-apt-group-has-targeted-russia-repeatedly-since-ukraine-invasion/](https://blog.malwarebytes.com/malwarebytes-news/2022/05/unknown-apt-group-has-targeted-russia-repeatedly-since-ukraine-invasion/)

> An unknown Advanced Persistent Threat (APT) group has targeted Russian government entities with at least four separate spear phishing campaigns since late February, 2022.
> The campaigns, discovered by the Malwarebytes Threat Intelligence team , are designed to implant a Remote Access Trojan (RAT) that can be used to surveil the computers it infects, and run commands on them remotely. The malware uses a number of advanced tricks to hide what it does and how it works, but our analysts have been able to reverse engineer the malware, reveal its inner workings, and uncover some clues about its possible origins.
> Attribution is always difficult, and there is no shortage of countries or agencies with an interest in getting covert access to Russian government computers—and the recent invasion of Ukraine has simply increased the stakes. Although our analysis and attribution efforts are ongoing, we have discovered some indicators that suggest the threat actor may be a Chinese group. 


We tend to focus on conflict between the west and “others”, such as Russia and China.  But this is a useful reminder that the world is not as simple as that.  While Russian forces are distracted by events in Ukraine, and focused on their objectives there, it’s a good opportunity for all other states, even erstwhile allies, to target their systems.
This can be both opportunistic, taking advantage of otherwise distracted defenders, but might also be strategic, as senior leaders in Beijing are also almost certainly interested in the political decision making going on at the moment, so that it is not surprised. 


## [Tesla, Microsoft and Ubuntu bugs found during Pwn2Own hacking competition - The Record by Recorded Future ](https://therecord.media/tesla-microsoft-and-ubuntu-bugs-found-during-pwn2own-hacking-competition/)

[https://therecord.media/tesla-microsoft-and-ubuntu-bugs-found-during-pwn2own-hacking-competition/](https://therecord.media/tesla-microsoft-and-ubuntu-bugs-found-during-pwn2own-hacking-competition/)

> Several bugs in Microsoft, Ubuntu and Tesla products were found and exploited during the three-day Pwn2Own hacking conference in Vancouver this week.
> The conference – organized by Trend Micro’s Zero Day Initiative – gives hackers a chance to earn money in exchange for discovering and exploiting vulnerabilities in popular products. 
> By the end of day two on Thursday, the conference had paid out $945,000 in rewards, including $75,000 to hackers with offensive security company Synacktiv for two unique bugs found in the Tesla Model 3 Infotainment System. 


Firms have 90 days before the findings and write ups can be released, so expect some patches and some juicy write ups in the next few months. 


## [Automating cloud governance at scale | by Skyscanner Engineering | Oct, 2021 | Medium](https://medium.com/@SkyscannerEng/automating-cloud-governance-at-scale-895695fe4a1f)

[https://medium.com/@SkyscannerEng/automating-cloud-governance-at-scale-895695fe4a1f](https://medium.com/@SkyscannerEng/automating-cloud-governance-at-scale-895695fe4a1f)

> But where does Security fit in? Our goal in Platform Security and Automation is to detect and remediate issues early in the development pipeline, minimizing the risk of security misconfigurations in production environments that become harder to track and fix over time. For CloudFormation and IaC, this involves checking templates that define the infrastructure we have in AWS, utilizing our open-source tool CFRipper for the job (we introduced this tool in a 2018 blog post and talked about cloud governance challenges in a second blog post in 2020).


Security teams that build tools to do their job are more effective.  CFRipper is a great tool for inspecting and validating your AWS CloudFormation stacks to ensure that they meet your compliance requirements


## [GitHub - gabrie30/ghorg: Quickly clone an entire org/users repositories into one directory - Supports GitHub, GitLab, Bitbucket, and more 🥚](https://github.com/gabrie30/ghorg)

[https://github.com/gabrie30/ghorg](https://github.com/gabrie30/ghorg)

> ghorg allows you to quickly clone all of an orgs, or users repos into a single directory. This can be useful in many situations including
> 
> 1. Searching an orgs/users codebase with ack, silver searcher, grep etc..
> 1. Bash scripting
> 1. Creating backups
> 1. Onboarding new team members (cloning all team repos)
> 1. Performing Audits


This feels like a bit of hack somewhere between a monorepo, and lots of microrepos.

I don't think that a new developer would ever want to get all of an orgs repos, but for auditing, reviewing and backing up, this is super useful


## [Implementing Secure Code in the Cloud | ScaleSec ](https://scalesec.com/blog/implementing-secure-code-in-the-cloud/)

[https://scalesec.com/blog/implementing-secure-code-in-the-cloud/](https://scalesec.com/blog/implementing-secure-code-in-the-cloud/)

> A method of preventing the vulnerable lambda code to begin with is to leverage Static Analysis Security Tools ( SAST ) which can scan for known vulnerable libraries, syntax, and patterns. In the particular case of Python, a tool such as Bandit can be used within the CI/CD pipeline to fail builds that don’t pass specific security policies.  […] Another layer to consider is the use of instrumentation and Runtime Application Self-Protection (RASP) technologies. Instrumentation is very powerful as it can log different metrics, errors, and trace functions during runtime. Developers may already use instrumentation for the purpose of performance testing and monitoring within their solution. 


A nice walkthrough of setting up a SAsT tool in your CI pipeline.  I also like the demonstration of decent runtime analysis tools, although as noted in the article, it catches any anomalous requests, which might include real user requests, and may not catch all security impacting requests. 


## [CISA Adds 34 Known Exploited Vulnerabilities to Catalog | CISA](https://www.cisa.gov/uscert/ncas/current-activity/2022/05/25/cisa-adds-34-known-exploited-vulnerabilities-catalog)

[https://www.cisa.gov/uscert/ncas/current-activity/2022/05/25/cisa-adds-34-known-exploited-vulnerabilities-catalog](https://www.cisa.gov/uscert/ncas/current-activity/2022/05/25/cisa-adds-34-known-exploited-vulnerabilities-catalog)

> CISA has added 34 new vulnerabilities to its Known Exploited Vulnerabilities Catalog, based on evidence of active exploitation. These types of vulnerabilities are a frequent attack vector for malicious cyber actors and pose significant risk to the federal enterprise. 
> 
> Binding Operational Directive (BOD) 22-01: Reducing the Significant Risk of Known Exploited Vulnerabilities established the Known Exploited Vulnerabilities Catalog as a living list of known CVEs that carry significant risk to the federal enterprise. BOD 22-01 requires FCEB agencies to remediate identified vulnerabilities by the due date to protect FCEB networks against active threats.


Some additional vulnerabilities that federal departments must patch across their estate, and there's now a ticking timer to ensure that they have patched by the due date, normally within 30 days.

Worth noting that this includes core OS patches in Windows, in Linux and in Solaris, patches to desktop applications like Firefox, Silverlight and Adobe Reader,  as well as application environments like InfoSphere and JBoss.


## [Pre-hijacked accounts: An Empirical Study of Security Failures in User Account Creation on the Web – arXiv Vanity ](https://www.arxiv-vanity.com/papers/2205.10174/)

[https://www.arxiv-vanity.com/papers/2205.10174/](https://www.arxiv-vanity.com/papers/2205.10174/)

> In an effort to improve user experience, there is currently a trend towards federated identity and authentication. One of the most visible aspects of this is Single Sign-On (SSO) in which the user creates an account with an Identity Provider (IdP), and can then use this to create accounts with any relying party (RP) service that supports SSO and trusts the user’s IdP. There is a strong incentive for services to support SSO because it improves the experience for users by allowing them to reuse the same IdP account across multiple services. Many large companies, including Google, Facebook, and Microsoft, provide IdP services that are widely supported and trusted by websites and other online services. Previous work has also explored the security implications of SSO, showing that IdPs can become single points of failure [22, 7, 17, 41, 6, 40].
> 
> However, one aspect that has not received much attention is the process of account creation, along with its corresponding security assumptions and requirements. This process is further complicated by the move towards SSO because many services now support two different mechanisms through which users can create an account: the classic approach in which the user sets a password directly with the service, and the federated approach where the user already has an account with an IdP and uses this to create an account with the service. Once an account has been created, some services also offer the possibility to link an IdP account, so that the user can either sign in directly to the service or authenticate via the IdP.
> 
> Inspired by that attack, we demonstrate that there exists an entire class of such attacks, which we call account pre-hijacking attacks. The distinguishing feature of these attacks is that the attacker performs some action before the victim creates an account at the target service. The unsuspecting victim might subsequently create/restore their account and start using it. Finally, the attacker completes the attack by gaining access to the victim’s account. In this work, we identify and describe \nNovelAtkTypes types of pre-hijacking attacks1
> 1
> However, we do not claim that this is an exhaustive list of attacks.. In contrast to the attack by Ghasemisharif et al. [17], none of our attacks require the attacker to compromise the victim’s IdP account.
> 
> All of our attacks make some assumptions about the victim’s actions or lack thereof. These include (common) actions, such as creating an account (using the classic or federated route) or recovering the password for an existing account, as well as inactions, such as ignoring emails from services where the user does not have an account, or failing to notice unexpected identifiers after recovering an account. One variant requires a successful CSRF attack. We set out the assumptions for each type of attack in Table 1.


This is a lovely paper on an almost entirely new, and hitherto unknown, class of attacks.

In essence, if someone can go to a popular web service, and setup an account with a username and password, and then convince you to go and sign up for an account using an identify provider like Google or Microsoft, they can rely on the fact that many systems merge the accounts to end up with maintained access to your account.

This sort of attack is both highly targeted, technically complex and requires the user to ignore certain warning signs, but it's one that actions by SaaS vendors can make significantly harder, so if you are working in security and provide accounts and account merging, this paper is worth a read.


