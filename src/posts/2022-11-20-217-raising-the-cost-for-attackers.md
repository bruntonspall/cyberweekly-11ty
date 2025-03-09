---
title: "217 - Raising the cost for attackers"
date: 2022-11-20
description: "One of the things that we don't often talk about in security is that we're often not trying to make our systems immune to attacks.  Instead, what we are often trying to do is ensure that our system is too hard for the average attacker to compromise easily."
permalink: /raising-the-cost-for-attackers/
---

One of the things that we don't often talk about in security is that we're often not trying to make our systems immune to attacks.  Instead, what we are often trying to do is ensure that our system is too hard for the average attacker to compromise easily.

This is true in physical security as much as cyber security.  Your front door can probably be kicked in, but doing so would create noise, attract attention, and leave huge amounts of evidence that the attack had happened.  These are all costs that an attacker has to decide if they are going to pay.

In the cybersecurity world, this is also the case, but the plethora of targets is even bigger.  Attackers aren't comparing other people on your street with you, they are looking at more or less the entire worlds online ecosystem.

This means that our defensive activities should be focused on not only on protecting the system, but also on raising the cost of offensive actions by attackers, so that they need to expend more effort, more money and more resources to carry out the attack.

That can mean making it harder for initial compromise to expand their foothold, or whether it means ensuring that they must invest in new, undetectable and deniable tools.  

Red Teams often claim that by sharing and publishing detections for their tooling, that teams are making life harder for red teams without making life difficult for attackers, but I don't agree with that assessment.  Red Teams should be modeling the kinds of activities that real attackers have, and that means that imposing costs on red teams is also imposing costs on real attackers.

So invest in the technologies, tools and processes that impose cost on your attacker, and hope that you are imposing more costs than your neighbours, making you a harder target.

## [Making Cobalt Strike harder for threat actors to abuse | Google Cloud Blog ](https://cloud.google.com/blog/products/identity-security/making-cobalt-strike-harder-for-threat-actors-to-abuse)

[https://cloud.google.com/blog/products/identity-security/making-cobalt-strike-harder-for-threat-actors-to-abuse](https://cloud.google.com/blog/products/identity-security/making-cobalt-strike-harder-for-threat-actors-to-abuse)

> Cobalt Strike, the popular tool used by [red teams](https://www.youtube.com/playlist?list=PLcjpg2ik7YT6H5l9Jx-1ooRYpfvznAInJ) to test the resilience of their cyber defenses, has seen many iterations and improvements over the last decade. First released in 2012, it was originally the commercial spinoff of the open-source [Armitage project](https://www.offensive-security.com/metasploit-unleashed/armitage/) that added a graphical user interface (GUI) to the [Metasploit framework](https://www.metasploit.com/) to help security practitioners detect software vulnerabilities more quickly. 
> 
> It has since matured into a point-and-click system for the deployment of the Swiss Army Knife of remote access tools onto targeted assets. While the intention of Cobalt Strike is to emulate a real cyber threat, malicious actors have latched on to its capabilities, and use it as a robust tool for lateral movement in their victim’s network as part of their second-stage attack payload. 
> 
> Cobalt Strike vendor [Fortra](https://www.fortra.com/) (until recently known as Help Systems) uses a vetting process that attempts to minimize the potential that the software will be provided to actors who will use it for nefarious purposes, but Cobalt Strike has been leaked and cracked over the years. These unauthorized versions of Cobalt Strike are just as powerful as their retail cousins except that they don’t have active licenses, so they can’t be upgraded easily.
> 
> We are releasing to the community a set of [open-source YARA Rules](https://github.com/chronicle/GCTI) and their integration as a [VirusTotal Collection](https://blog.virustotal.com/2021/11/introducing-virustotal-collections.html) to help the community flag and identify Cobalt Strike’s components and its respective versions. Since many threat actors rely on cracked versions of Cobalt Strike to advance their cyberattacks, we hope that by disrupting its use we can help protect organizations, their employees, and their customers around the globe. 


This is good news.  If you read the threat intelligence reports, you’ll see that many APT’s also use Cobalt Strike as part of their toolkits.  Of course, they probably have the capacity and capability to build their own C2 toolkit, but why would they expend that effort if they can use a RedTeam tool instead.  

Sharing these rulesets and making them open imposes a cost on operations of some of the most advanced actors, as well as the lower tier actors. 


## [About multiple administrative approvals in Intune - Microsoft Intune | Microsoft Learn ](https://learn.microsoft.com/en-us/mem/intune/fundamentals/multi-admin-approval)

[https://learn.microsoft.com/en-us/mem/intune/fundamentals/multi-admin-approval](https://learn.microsoft.com/en-us/mem/intune/fundamentals/multi-admin-approval)

> To help protect against a compromised administrative account, use Intune _access policies_ to require that a second administrative account is used to approve a change before the change is applied. This capability is known as multiple administrative approval (MAA).
> 
> With MAA, you configure access policies that protect specific configurations, like Apps or Scripts for devices. Access policies specify what is protected and which group of accounts are permitted to approve changes to those resources.
> 
> When any account in the Tenant is used to make a change to a resource that’s protected by an access policy, Intune won't apply the change until a different account explicitly approves it. Only administrators who are members of an approval group that’s assigned a protected resource in an access protection policy can approve changes. Approvers can also reject change requests. 


This is a nice feature that Microsoft are launching.   Ensuring that certain administrative changes require a second administrator to sign off, can really make an attackers life harder 


## [No AWS operator access - The Security Design of the AWS Nitro System ](https://docs.aws.amazon.com/whitepapers/latest/security-design-of-aws-nitro-system/no-aws-operator-access.html)

[https://docs.aws.amazon.com/whitepapers/latest/security-design-of-aws-nitro-system/no-aws-operator-access.html](https://docs.aws.amazon.com/whitepapers/latest/security-design-of-aws-nitro-system/no-aws-operator-access.html)

> As with most engineering decisions, the choice to design the Nitro System without a mechanism for operator access came with trade-offs. In rare cases subtle issues can arise that, because there are no general access capabilities on our production hardware, AWS operators are unable to debug in-place. In those rare circumstances we must work with customers, at their request, to reproduce those subtle issues on dedicated non-production Nitro debugging hardware. This can be less convenient than if our operators could debug in-place, but we strongly believe that this is the better trade-off for our customers. As a result, we must by necessity hold ourselves to the highest standard for system quality and testing prior to production release. 


This attribute of AWS's Nitro system (and you can read the [rest of the security design](https://docs.aws.amazon.com/whitepapers/latest/security-design-of-aws-nitro-system/security-design-of-aws-nitro-system.html)) really goes out of its way to improve the security of these VM's for users of the system.

This intentional design is the sort of thing that really can only be done at design time, rather than a security feature bolted on later


## [How LNK Files Are Abused by Threat Actors - Intezer ](https://www.intezer.com/blog/malware-analysis/how-threat-actors-abuse-lnk-files/)

[https://www.intezer.com/blog/malware-analysis/how-threat-actors-abuse-lnk-files/](https://www.intezer.com/blog/malware-analysis/how-threat-actors-abuse-lnk-files/)

> [Microsoft’s decision](https://learn.microsoft.com/en-gb/DeployOffice/security/internet-macros-blocked) to block macros by default for files downloaded from the internet in Office applications provoked malware developers to shift to other techniques. Threat actors have identified the potential profit of using LNK files in different stages of attacks as we expect to see an [increased number of attacks](https://www.proofpoint.com/us/blog/threat-insight/how-threat-actors-are-adapting-post-macro-world) using LNK files, such as [Bumblebee](https://www.bleepingcomputer.com/news/security/bumblebee-malware-adds-post-exploitation-tool-for-stealthy-infections/) and [Quantum Ransomware](https://thedfirreport.com/2022/04/25/quantum-ransomware/) .
> 
> In this blog, we will cover the file format to understand better how threat actors use LNK files in the different stages of attacks. By getting familiar with the LNK (Shell Link) file format and its capabilities, we will present open-source tools and methods to inspect and detect malicious LNK files in incident response and threat-hunting processes.
> 
> […] [Emotet](https://www.bleepingcomputer.com/news/security/emotet-malware-infects-users-again-after-fixing-broken-installer/#:~:text=last%20friday%2C%20the%20emotet%20malware%20distributors%20launched%20a%20new%20email%20campaign%20that%20included%20password-protected%20zip%20file%20attachments%20containing%20windows%20lnk%20(shortcut)%20files%20pretending%20to%20be%20word%20documents.) used this technique in a phishing email they sent to the victims, including a password-protected zip file that contained an LNK file disguised as a Word document that executes a VBS script which downloads malware. [Bumblebee](https://www.bleepingcomputer.com/news/security/bumblebee-malware-adds-post-exploitation-tool-for-stealthy-infections/) , a new and advanced loader, uses an LNK file as part of the attack flow. So far, it has two versions, one delivered ISO file and the latter a VHD. In both cases, an LNK file is included. In the first version, the LNK executed the accompanying DLL, which contains the malicious payload. The later version is more advanced, and the LNK file executes an attached PowerShell file that loads the second stage of the loader.
> 
> Some malware developers took it one step further and created a tool for creating malicious LNK files called [Quantum](https://blog.cyble.com/2022/06/22/quantum-software-lnk-file-based-builders-growing-in-popularity/) , and it’s sold on the dark web. It allows other criminals to create malicious files with extra capabilities such as UAC bypass, delayed execution, post-execution hiding, and a variety of double extensions. 


I learned a lot more about LNK files from this resource.  I knew that they provided a shortcut to another executable, but it turns out there’s more to it.

I hadn’t really realised that LNK files can invoke things like UAC bypass or post-execution hiding. 


## [The 5×5—The rise of cyber surveillance and the Access-as-a-Service industry - Atlantic Council ](https://www.atlanticcouncil.org/content-series/the-5x5/the-5x5-the-rise-of-cyber-surveillance-and-the-access-as-a-service-industry/)

[https://www.atlanticcouncil.org/content-series/the-5x5/the-5x5-the-rise-of-cyber-surveillance-and-the-access-as-a-service-industry/](https://www.atlanticcouncil.org/content-series/the-5x5/the-5x5-the-rise-of-cyber-surveillance-and-the-access-as-a-service-industry/)

> **#5 How has the Access-as-a-Service industry evolved over the past two decades and where do you see it going from here?**  
> 
> **Anstis:** “The Access-as-a-Service industry has become increasingly formalized in the past two decades, with growing interest from investors and states in terms of funding the industry, as well as accessing the services and technologies offered. I see the next few years as a critical turning point in the industry’s development. Countless human rights abuses have brought increased awareness that the services and technologies offered by the Access-as-a-Service industry have serious human rights ramifications—as well as national security concerns—that need to be addressed. With ongoing investigations in the European Parliament, the United States, and elsewhere into companies that participate in this industry, I hope that we will see more specific steps aimed at curbing and controlling it.” 
> 
> **DeSombre:** “Like every part of the cybersecurity ecosystem since the early 2000s, the Access-as-a-Service industry has grown, professionalized, and turned towards mobile, embedded, and other non-desktop systems. Your laptop is not the only place with interesting data!” 
> 
> **Gjesvik:** “This is a pretty opaque industry, and there is not a ton of structured encompassing data available that I am aware of, but there are some broad trends. The first is globalization, a quite substantive expansion of tools and technologies available, and a lot more money to be made as well. Going forward, I am probably most interested in the extent to which the industry is controllable by any state actor. Will recent efforts by the United States and the European Union succeed in limiting the worst excesses? Or will it just accelerate the diversification of suppliers?” 
> 
> **Hazelrig:** “So long as there have been criminal hackers, there have been ways for those with the right connections to procure intrusion services. However, about a decade ago, we started to see the emergence of professional firms that sold these services commercially, primarily to governments around the globe. The past couple of years has brought casual proliferation and a booming ‘consumer’ market—shady companies advertise euphemistically-phrased services on mainstream platforms such as LinkedIn, and many online criminal marketplaces have whole sections of specialty products and services from which to choose.” 
> 
> **Willers:** “The origins of the Access-as-a-Service industry can be traced back to a combination of privatization dynamics in the telecommunication sector during the 1990s, the rise of digital communication systems, and the political focus on surveillance in the aftermath of the September 11 terrorist attacks. Since then, the industry has developed at the speed of technology, and there is good reason to doubt that the United States remains in a position to control it. Limiting access to technology is difficult, especially when it is as mobile as spyware technology. This is why I doubt that the United States or any other country alone can control the operations of the market.” 


An interesting analysis and one that resonates for me.  I’m increasingly nervous of the second and third order effects of a rising access-as-a-service (or initial-access-brokers) industry.  

It’s not just the rise of the use of these firms that concerns, but what effect it will have on the economic markets for cyber compromise (some things might get much cheaper, some services and products might be sold for far more), and then the implications for changing attacker behavours.

Where this goes next is incredibly hard to forecast, but I don’t think this ends up well for most of us.  It ends up with a broader set of attackers, using powerful capabilities, but who previously would never have been able to get involved. 


## [Personnel security in the cloud ](https://www.ncsc.gov.uk/blog-post/personnel-security-in-the-cloud)

[https://www.ncsc.gov.uk/blog-post/personnel-security-in-the-cloud](https://www.ncsc.gov.uk/blog-post/personnel-security-in-the-cloud)

> While security screening and limiting who has access to your data are both important aspects of personnel security, they will only get you so far. In a hyperscale cloud provider, this could still be several thousand people, working around the globe. Security screening and limiting alone still leaves a significant risk of malicious or accidental access to data. Instead, you should expect your cloud provider to take a more layered approach.
> 
> A good cloud provider will also apply technical controls to bring additional defence in depth. A well-designed cloud service will allow a support engineer to diagnose and treat the fault without having to access customer data in a large number of cases. For example, all access to customer data and services should be audited and monitored in detail, to discourage inappropriate access and help investigate incidents. You should also be alerted whenever your cloud provider’s personnel access your data, so you can confirm that this was expected. 


Layered approaches not only protect the infrastructure from attackers, but also protect the staff against personal compromise.  If staff know that their work is audited, that their accesses are monitored, and that they cannot access customer data, then they are a much harder target for blackmail as well as for phishing or device compromise as well.


## [Stealing passwords from infosec Mastodon - without bypassing CSP | PortSwigger Research ](https://portswigger.net/research/stealing-passwords-from-infosec-mastodon-without-bypassing-csp)

[https://portswigger.net/research/stealing-passwords-from-infosec-mastodon-without-bypassing-csp](https://portswigger.net/research/stealing-passwords-from-infosec-mastodon-without-bypassing-csp)

> The story of how I could steal credentials on Infosec Mastodon with a HTML injection vulnerability, without needing to bypass CSP.
> 
> Everybody on our Twitter feed seemed to be jumping ship to the infosec.exchange Mastodon server, so I decided to see what the fuss was all about. After figuring out why exactly you had to have loads of @ symbols in your username, I began to have a look at how secure it was. If you've followed me on Twitter you'll know I like to post vectors and test the limits of the app I'm using, and today was no exception. 
> 
> [...]
> 
> We reported this vulnerability to Mastodon, who initially suggested the flaw may be specific to the Glitch fork used by infosec.exchange. However, they then released Mastodon 4.0.1, 3.5.5, and 3.4.10 to mitigate the issue. After discussing this with the Glitch developer, core Mastodon was not vulnerable to this particular attack since they do not allow title attributes. It was still patched to fix replacement of placeholders such as :verified:.


This is relevant for those of you who are migrating to Mastodon and considering running your own server.  That's more software you need to maintain and yet another  potential attack vector in your life.

Have you checked whether your mastodon server that you trust to represent your online identity has patched?


## [SLSA: The Source of the problem by François Proulx | boostsecurity ](https://medium.com/boostsecurity/slsa-dip-source-of-the-problem-a1dac46a976)

[https://medium.com/boostsecurity/slsa-dip-source-of-the-problem-a1dac46a976](https://medium.com/boostsecurity/slsa-dip-source-of-the-problem-a1dac46a976)

> To map out the GitHub Enterprise Cloud’s attack surface, we will use [GitHub’s documentation](https://docs.github.com/en) . We’ve analyzed the attack surface relevant when considering all aspects of securing access to the source code. You will find all the links in the Appendix of this article.
> 
> We regroup all attacks by focusing on three malicious end goals ( [largely inspired by the SLSA threats catalog](https://slsa.dev/spec/v0.1/threats#source-integrity-threats) ):
> 
> * Submit malicious source code
> * Delete source code
> * Push a release tag pointing to vulnerable commit
> 
> There are numerous ways to achieve those end goals. The attack scenarios can range from relatively simple to highly complex. If we consider an insider threat, there are even more scenarios, and their mitigations might be more difficult to implement, especially for employees with administrative access. 


Lovely use of attack trees to understand the sorts of attacks that can be carried out on your source control system, and how SLSA can help mitigate some of those attacks 


## [Iranian Government-Sponsored APT Actors Compromise Federal Network, Deploy Crypto Miner, Credential Harvester | CISA ](https://us-cert.cisa.gov/ncas/alerts/aa22-320a)

[https://us-cert.cisa.gov/ncas/alerts/aa22-320a](https://us-cert.cisa.gov/ncas/alerts/aa22-320a)

> In April 2022, CISA conducted retrospective analysis using EINSTEIN—an FCEB-wide intrusion detection system (IDS) operated and monitored by CISA—and identified suspected APT activity on an FCEB organization’s network. CISA observed bi-directional traffic between the network and a known malicious IP address associated with exploitation of the Log4Shell vulnerability (CVE-2021-44228) in VMware Horizon servers. In coordination with the FCEB organization, CISA initiated threat hunting incident response activities; however, prior to deploying an incident response team, CISA observed additional suspected APT activity.         
> 
> From mid-June through mid-July 2022, CISA conducted an onsite incident response engagement and determined that the organization was compromised as early as February 2022, by likely Iranian government-sponsored APT actors who installed XMRig crypto mining software. The threat actors also moved laterally to the domain controller, compromised credentials, and implanted Ngrok reverse proxies. 


Fascinating, all that effort to simply install XMRig cryptomining?  They may have had other targets and other activities, but if their main purpose was something else, why tip their hand to install a cryptomining system?  What does this tell us about their intent? 


## [Exclusive: Ex-Russian spy flees to the NATO country that captured him, delivering another embarrassing blow to Moscow ](https://news.yahoo.com/exclusive-ex-russian-spy-flees-to-the-nato-country-that-captured-him-delivering-another-embarrassing-blow-to-moscow-010049616.html)

[https://news.yahoo.com/exclusive-ex-russian-spy-flees-to-the-nato-country-that-captured-him-delivering-another-embarrassing-blow-to-moscow-010049616.html](https://news.yahoo.com/exclusive-ex-russian-spy-flees-to-the-nato-country-that-captured-him-delivering-another-embarrassing-blow-to-moscow-010049616.html)

> In early October, the Estonian government granted Yahoo News unprecedented access to Zinchenko. Over the course of four hours he offered up his autobiography, reflective and remorseless, detailing his supporting role in the mostly unseen shadow play between Russian espionage and Western efforts to thwart it. Estonia, once occupied by the Soviets, is now at the forefront of countering Russian intelligence gathering and provocations on NATO soil.
> 
> As Zinchenko told it, his decision to defect was as much motivated by the Kremlin’s brutality at home and abroad as it was by what he saw as Estonia’s humanity toward him, an enemy agent. His cautionary tale is also an indictment of the policies of Russian President Vladimir Putin, a former KGB case officer whose own spy apparatus has been weakened amid his Ukraine war, according to British intelligence.
> 
> Once a highly secretive and effective spy agency, the GRU in the past decade has come under heightened international scrutiny owing to a spate of compromised or failed operations. Foremost among these is the hacking and leaking of Democratic Party emails in advance of the 2016 U.S. presidential election and the botched 2018 assassination attempt on Sergei Skripal, another defector from its ranks, in Salisbury, England. The GRU is now reportedly assuming a firmer grasp on Russia’s faltering but gruesome campaign in Ukraine, where Zinchenko has relatives fighting on the frontlines on behalf of Kyiv against the very masters he once served.
> 
> The war, in fact, is the reason this GRU spy fled Russia.


Absolutely fascinating story, and as Yahoo makes out, a key reminder of how important morale is in your offensive teams.  You really need them to believe in the mission and believe that the costs are worth it


