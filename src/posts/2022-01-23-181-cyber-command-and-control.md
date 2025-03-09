---
title: "181 - Cyber Command and Control"
date: 2022-01-23
description: "If we assume for a minute that you aren't perfect, that somehow, an adversary has gotten onto one of your users endpoints.  What happens next?"
permalink: /cyber-command-and-control/
---

If we assume for a minute that you aren't perfect, that somehow, an adversary has gotten onto one of your users endpoints.  What happens next?

The [concept of a "Cyber Kill Chain"](https://www.varonis.com/blog/mitre-attck-framework-complete-guide#mackc) (originally from [Lockheed Martin](https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html)) is that after exploitation the attacker needs to conduct privilege escalation and lateral movement, before grabbing the data (or conducting "action on target" for those people with a military background) and getting it out.  

The purpose of the cyber kill chain is that an attacker has to complete all the steps to achieve their intended outcome.  So even if they can get exploitation of a device, if you can prevent privilege escalation, or lateral movement, then their ability to conduct their campaign is limited.

Because modern technology environments are incredibly complex and constantly changing, it's very rare to deploy malware that is "blind", which is to say, to deploy it without being able to have to human operator react to what it finds.  This is the key to lateral movement, it requires the malware to sense the computing environment and work out how to best find vulnerable services that it can use for privilege escalation.  For example, if you've compromised an end user device, say someone in marketings laptop, then you probably don't have administrative privileges on that device, and unless you can get a network administrator to log in, you can't simply run [mimikatz](https://github.com/ParrotSec/mimikatz) on it.  So you might want to look around and see if any device you can reach from the laptop might have an administrator logged in.  

Right now, this is incredibly hard to automate, and as such, when that malware runs on your network, it needs a mechanism to establish a channel for communicating back to the remote operator, this is the C2 or Command and Control system.  

In these modern days of zero-trust networking, encryption everywhere, it's far less common, or useful, to force users to use a content inspecting proxy to access the internet.  [Modern TLS breaks when inspected in a lot of ways](https://joelgsamuel.medium.com/can-we-stop-intercepting-user-traffic-aka-man-in-the-middle-please-2a00de208d4b), and even if you can achieve full visibility, the sheer amount of communication going out of the modern enterprise makes it incredibly difficult to tell good traffic from bad.

Even in more controlled environments, the users need to do their job, and that often involves access to forums, SaaS tools or other internet hosted tools.  It's very difficult for systems to determine at a glance whether a request for a Discord image is normal operation of Discord, or a command channel.  Likewise for Slack, Google Docs and many other external systems.

So how can we prevent this kind of thing, how can we reduce the ability for malware to use C2 channels.

Firstly, we can do far more inspection on the device than we can on the network.  If the local device is making calls to Discord, but not from the discord.exe process, but from a different process, then that's suspicious.  We can start to tie together whether the user is logged in and running the application to see whether the traffic correlates.  

Secondly, of course, again on the end user devices, we can prevent the user from running unknown applications of dubious origin.  We have to be careful of this, because Karen, a software engineer might have legitimate reasons for running a wide range of applications, but Mark in accounts probably doesn't.   Building out user profiles like this can also help your organisation work out what permissions they should have in other areas, as well as put in likely internet access profiles.

Finally of course, while zero-trust tends to dictate that our end user devices sit "outside our network" and thus can't be easily inspected for outgoing connections, it also means that every server and every system in your network can treat that device and user as an outsider and require strong authentication for requests coming from them.  This pattern makes lateral movement significantly harder for attackers, because a lot of the time they rely on the fact that servers and systems trust programs that are already "on the network".

While there might be a rise in fun and interesting methods of command and control for malware, it also brings opportunities for detection and prevention that didn't exist before.

## [Destructive malware targeting Ukrainian organizations - Microsoft Security Blog](https://www.microsoft.com/security/blog/2022/01/15/destructive-malware-targeting-ukrainian-organizations/)

[https://www.microsoft.com/security/blog/2022/01/15/destructive-malware-targeting-ukrainian-organizations/](https://www.microsoft.com/security/blog/2022/01/15/destructive-malware-targeting-ukrainian-organizations/)

> Microsoft Threat Intelligence Center (MSTIC) has identified evidence of a destructive malware operation targeting multiple organizations in Ukraine. This malware first appeared on victim systems in Ukraine on January 13, 2022. Microsoft is aware of the ongoing geopolitical events in Ukraine and surrounding region and encourages organizations to use the information in this post to proactively protect from any malicious activity.
> 
> While our investigation is continuing, MSTIC has not found any notable associations between this observed activity, tracked as DEV-0586, and other known activity groups. MSTIC assesses that the malware, which is designed to look like ransomware but lacking a ransom recovery mechanism, is intended to be destructive and designed to render targeted devices inoperable rather than to obtain a ransom.
> 
> At present and based on Microsoft visibility, our investigation teams have identified the malware on dozens of impacted systems and that number could grow as our investigation continues. These systems span multiple government, non-profit, and information technology organizations, all based in Ukraine. We do not know the current stage of this attacker’s operational cycle or how many other victim organizations may exist in Ukraine or other geographic locations. However, it is unlikely these impacted systems represent the full scope of impact as other organizations are reporting.
> 
> Given the scale of the observed intrusions, MSTIC is not able to assess intent of the identified destructive actions but does believe these actions represent an elevated risk to any government agency, non-profit or enterprise located or with systems in Ukraine. We strongly encourage all organizations to immediately conduct a thorough investigation and to implement defenses using the information provided in this post. MSTIC will update this blog as we have additional information to share.


We've seen this kind of behaviour from an APT before, in NotPetya, an attack that targeted the Ukraine a few years back.

Dubbed NotPetya because although it looked like a strain of Ransomware called Petya, NotPetya didn't actually store the recovery credentials, meaning that there was no reason to ever pay.  

Although NotPetya was targeting Ukraine organisations, thousands of companies around the world, including famously, Maersk Shipping, were hit because the tax filing software they had to use to do business in the Ukraine was a key distributor for NotPetya.

The targeting for what is being called WhisperGate looks like it is more restricted in what organisations it is targeting, but of course, many global companies have to do business with or operate within the Ukraine.


## [Cisco Talos Intelligence Group - Comprehensive Threat Intelligence: Ukraine Campaign Delivers Defacement and Wipers, in Continued Escalation](https://blog.talosintelligence.com/2022/01/ukraine-campaign-delivers-defacement.html)

[https://blog.talosintelligence.com/2022/01/ukraine-campaign-delivers-defacement.html](https://blog.talosintelligence.com/2022/01/ukraine-campaign-delivers-defacement.html)

> Several cyber attacks against Ukrainian government websites — including website defacements and destructive wiper malware — have made headlines over the past few weeks as military tensions along the Russian/Ukrainian border have escalated. As a longtime intelligence partner and ally, Cisco Talos quickly responded to provide support, working with the State Special Communications Service of Ukraine (SSSCIP), the Cyberpolice Department of the National Police of Ukraine and the National Coordination Center for Cybersecurity (NCCC at the NSDC of Ukraine).
> 
> Based on our analysis of the wiper malware, dubbed WhisperGate, we identified the following key points:
> 
> * While WhisperGate has some strategic similarities to the notorious NotPetya wiper that attacked Ukranian entities in 2017, including masquerading as ransomware and targeting and destroying the master boot record (MBR) instead of encrypting it, it notably has more components designed to inflict additional damage.
> * We assess that attackers used stolen credentials in the campaign and they likely had access to the victim network for months before the attack, a typical characteristic of sophisticated advanced persistent threat (APT) operations.
> * The multi-stage infection chain downloads a payload that wipes the MBR, then downloads a malicious DLL file hosted on a Discord server, which drops and executes another wiper payload that destroys files on the infected machines.
> * We echo the recommendations from the U.S. Cybersecurity and Infrastructure Security Agency (CISA) that organizations with ties to Ukraine should carefully consider how to isolate and monitor those connections to protect themselves from potential collateral damage.
> 
> [...]
> 
> However, defenders around the world should carefully watch the situation in Ukraine, particularly after the global impact of the Ukraine-centric attack that was NotPetya. In that case, an attack that was intended to punish Ukraine had a wide-ranging, global impact. Any organization that had any sort of business connection to Ukraine could be affected. Because of this history, organizations with ties to Ukraine should consider how to isolate and monitor those connections to protect themselves, a recommendation we made in 2017 and continue to stand by today.


Good quality detection such as up to date Microsoft Defender and good end point protection software should detect this malware and prevent it running, but that of course requires that you have this installed, patched and running on all your machines.

One of the interesting nuggets from this attack is that it uses popular chat application Discord for disseminating the third stage, which is the first time I've noticed that in modern malware.  But increasing use of SaaS tools means that it's much harder to simply block all corporate devices from accessing these tools and the files within them


## [State-sponsored hackers abuse Slack API to steal airline data](https://www.bleepingcomputer.com/news/security/state-sponsored-hackers-abuse-slack-api-to-steal-airline-data/)

[https://www.bleepingcomputer.com/news/security/state-sponsored-hackers-abuse-slack-api-to-steal-airline-data/](https://www.bleepingcomputer.com/news/security/state-sponsored-hackers-abuse-slack-api-to-steal-airline-data/)

> A suspected Iranian state-supported threat actor is deploying a newly discovered backdoor named 'Aclip' that abuses the Slack API for covert communications.
> 
> The threat actor's activity started in 2019 and targeted an unnamed Asian airline to steal flight reservation data.
> 
> According to a report by IBM Security X-Force, the threat actor is likely ITG17, aka 'MuddyWater,' a very active hacking group that maintains a targets organizations worldwide.
> 
> Abusing Slack
> Slack is an ideal platform for concealing malicious communications as the data can blend well with regular business traffic due to its widespread deployment in the enterprise.
> 
> This type of abuse is a tactic that other actors have followed in the past, so it's not a new trick. Also, Slack isn't the only legitimate messaging platform to be abused for relaying data and commands covertly.
> 
> In this case, the Slack API is utilized by the Aclip backdoor to send system information, files, and screenshots to the C2, while receiving commands in return.


This is an example of the growing use of SaaS apps as very difficult to detect command and control mechanisms for malware.


## [Merck wins cyber-insurance lawsuit related to NotPetya attack - The Record by Recorded Future](https://therecord.media/merck-wins-cyber-insurance-lawsuit-related-to-notpetya-attack/)

[https://therecord.media/merck-wins-cyber-insurance-lawsuit-related-to-notpetya-attack/](https://therecord.media/merck-wins-cyber-insurance-lawsuit-related-to-notpetya-attack/)

> Merck wins cyber-insurance lawsuit related to NotPetya attack
> A New Jersey court has ruled in favor of Merck in a lawsuit the pharmaceutical company filed against its insurer, Ace American, which declined to cover the losses caused by the NotPetya ransomware attack.
> 
> The NotPetya incident, which took place in June 2017 and impacted thousands of companies all over the world, destroyed data on more than 40,000 Merck computers and took the company months to recover.
> 
> Merck estimated the damage at $1.4 billion, a loss caused by production outage, costs to hire IT experts, and costs of buying new equipment to replace all affected systems.
> 
> At the time, the company had a $1.75 billion “all-risk” insurance policy, which included coverage for software-related data loss events.
> 
> However, Ace American refused to cover the losses, citing that the NotPetya attack was part of Russian hostilities against Ukraine and, as a result, was subject to the standard “Acts of War” exclusion clause that is present in most insurance contracts.
> 
> Merck sued Ace American in November 2019 and argued in court that the attack was not “an official state action,” hence the Acts of War clause should not apply.
> 
> Merck’s lawyers said that the exclusion clause contained language that limited the Acts of War to official government agencies and did not specifically mention cyber-related events; and, as a result, the clause should not apply to their customer.
> 
> In a ruling last month, spotted by Lexology, the New Jersey Superior Court has sided with Merck and its strict interpretation of the Acts of War clause.


This is a good finding for companies and a bad finding for insurers.  The court has found that cyber action isn't simply an act of war, but that the insurance must explicitly list nation state cyber attacks in its exclusions.

Of course, we are going to increasingly see insurers refuse to insure against these attacks, and we should expect to see more cases over the next few years trying to get the insurers to pay out.

[Note: I was confused by the Merck/Maersk titling here, but as you can see [here](https://www.ciab.com/resources/notpetya-a-war-like-exclusion/), both Merck and Maersk were affected by NotPetya, and it was Merck that has just won the lawsuit.]


## [More than 1,200 phishing toolkits capable of intercepting 2FA detected in the wild - The Record by Recorded Future](https://therecord.media/more-than-1200-phishing-toolkits-capable-of-intercepting-2fa-detected-in-the-wild/)

[https://therecord.media/more-than-1200-phishing-toolkits-capable-of-intercepting-2fa-detected-in-the-wild/](https://therecord.media/more-than-1200-phishing-toolkits-capable-of-intercepting-2fa-detected-in-the-wild/)

> In a study published last month, academics from Stony Brook University and security firm Palo Alto Networks said they analyzed 13 versions of these three MitM phishing toolkits and created fingerprints for the web traffic that goes through one of these tools.
> 
> They used their findings to develop a tool called PHOCA that could detect if a phishing site was using a reverse proxy—a clear sign that the attacker was trying to bypass 2FA and collect authentication cookies rather than credentials alone.
> 
> The researchers said they fed PHOCA with URLs reported by the cybersecurity community as phishing sites between March 2020 and March 2021 and found that 1,220 of these sites were using MitM phishing toolkits.
> 
> The number is a significant jump from the roughly 200 phishing sites running reverse proxies that were active in late 2018 and early 2019, according to stats provided at the time to this reporter by late RiskIQ researcher Yonathan Klijnsma.
> 
> This rise shows that these tools, and MitM phishing kits in general, have slowly gained in popularity among the cybercrime ecosystem.


Just as we are starting to get the number of people using MFA or 2FA into double digits and there's increasing evidence that smart criminals work around it.  It wasn't that long ago that Google was reporting less than 10% of users had MFA, and they keep threatening to roll it out by default to all users, but the next step will be working out if that's even good enough.

A competent phishing system will now steal both your password and your MFA token at the same time, enabling them to get into your accounts even if protected with MFA.


## [Google Online Security Blog: Understanding the Impact of Apache Log4j Vulnerability](https://security.googleblog.com/2021/12/understanding-impact-of-apache-log4j.html)

[https://security.googleblog.com/2021/12/understanding-impact-of-apache-log4j.html](https://security.googleblog.com/2021/12/understanding-impact-of-apache-log4j.html)

> As of December 16, 2021, we found that 35,863 of the available Java artifacts from Maven Central depend on the affected log4j code. This means that more than 8% of all packages on Maven Central have at least one version that is impacted by this vulnerability. (These numbers do not encompass all Java packages, such as directly distributed binaries, but Maven Central is a strong proxy for the state of the ecosystem.)
> 
> As far as ecosystem impact goes, 8% is enormous. The average ecosystem impact of advisories affecting Maven Central is 2%, with the median less than 0.1%.
> 
> 
> 
> Direct dependencies account for around 7,000 of the affected artifacts, meaning that any of its versions depend upon an affected version of log4j-core or log4j-api, as described in the CVEs. The majority of affected artifacts come from indirect dependencies (that is, the dependencies of one’s own dependencies), meaning log4j is not explicitly defined as a dependency of the artifact, but gets pulled in as a transitive dependency.
> 
> [...]
> 
> We counted an artifact as fixed if the artifact had at least one version affected and has released a greater stable version (according to semantic versioning) that is unaffected. An artifact affected by log4j is considered fixed if it has updated to 2.16.0 or removed its dependency on log4j altogether.
> At the time of writing, nearly five thousand of the affected artifacts have been fixed. This represents a rapid response and mammoth effort both by the log4j maintainers and the wider community of open source consumers.
> That leaves over 30,000 artifacts affected, many of which are dependent on another artifact to patch (the transitive dependency) and are likely blocked.


Some lovely analysis by Google here showing just how big a problem log4j is in the dependency chain of Java.

It also highlights just how far we have to go to be able to think that this is fixed


## [Edition 14: To WAF or not to WAF - by Sandesh Mysore Anand](https://boringappsec.substack.com/p/edition-14-to-waf-or-not-to-waf)

[https://boringappsec.substack.com/p/edition-14-to-waf-or-not-to-waf](https://boringappsec.substack.com/p/edition-14-to-waf-or-not-to-waf)

> Log4J RCE response
> It’s December 10th 2021. You are prepping for a nice weekend. Maybe some beer or just catching up on lost sleep or maybe there are a couple of good cricket matches you want to watch. But Log4J had other plans for you . All InfoSec professionals know what happened next. In the first few hours/days after the CVE was released, a key problem all teams faced was how to identify all instances of Log4J in their portfolio. It was clear that for large organizations, this process would take weeks (if not months). In the meantime, WAF came to the rescue.
> 
> Is the cost of fixing a defect is prohibitively more expensive than blocking attack traffic for that defect?
> For the first few days after the CVE dropped, the cost of upgrading Log4J was “unknown” for most orgs. Like we discussed before, how do you secure something when you don’t know if and where it exists? WAF rules turned out to be extremely useful this time. Most SRE teams will tell you that within 24 hours of the CVE dropping, most servers were hit with many attacks containing the payload attempting to exploit vulnerable versions of Log4J. While implementing the right WAF rules wasn’t easy, it turned out to be way cheaper than upgrading Log4J everywhere, over a December weekend.
> 
> Is there is tolerance in the orgranization to some legitimate traffic being blocked?
> The WAF community ( open source tools and commercial vendors) quickly came up with rules that could block attack traffic. The nature of the attack also meant the obscure payload needed to make the attack successful would probably not block a lot of legitimate traffic (it was still non-zero). This made the call easy. You rather block a small chunk of obscure traffic for a few days than risk RCE.
> 
> But as Chris mentioned, this only bought us time (which was precious at the time). In the medium to long run, the effectiveness of WAF response fo the Log4J RCE mirrors that of SQL injection. The cost of performing the upgrade is much lower than maintaining a WAF block list with constantly changing attack vectors.


This is a really good analysis of the value of using a WAF to block an attack. Sandesh's point is that WAF's are only good writing the rules is easier than fixing the software, and when your rules are so overly broad as to block legitimate traffic.

As he points out, long term for something like Log4J (and other "injectable attacks"), the cost of fixing the software is probably lower.  But in the short term, when the attack has only just been released and the complexity of attacks is slow, it almost certainly buys you the time needed to fix it.

Of course, one minor caveat to this is that almost all WAF installations that I've seen are implemented between the "dirty internet" and your application.  If you don't use a zero-trust networking architecture (and you probably don't), there's a good possibility that someone inside your network, whether an insider or an otherwise compromised machine can attack your vulnerable systems directly. 


## [Verica - Root Cause Is for Plants, Not Software](https://www.verica.io/blog/root-cause-is-for-plants-not-software/)

[https://www.verica.io/blog/root-cause-is-for-plants-not-software/](https://www.verica.io/blog/root-cause-is-for-plants-not-software/)

> Roughly a quarter of the VOID incident reports (26%) either identify a specific “root cause” or explicitly claim to have conducted a Root Cause Analysis (RCA). We consider these data preliminary, however, given the incomplete nature of the overall dataset. As we continue to add more reports, we’ll track this and see if it changes. 
> 
> We’re specifically looking into RCA because, like MTTR, it is appealing in its decisiveness and apparent simplicity, but it too is misleading.
> 
> An Artificial Stopping Point
> At its core, RCA posits that an incident has a single, specific cause or trigger, without which the incident wouldn’t have happened. Once that trigger is discovered, a solution flows from it, and the organization can take steps to ensure it never happens again. This sequence-of-events mindset (also known as the “Domino model”) has its origins in industrial accident theory and is common in incident reports, both for software and other domains. 
> 
> As safety researcher Sidney Dekker describes in The Field Guide to Understanding ‘Human Error’ when people choose causes for events, “This choosing can be driven more by socio-political and organizational pressures than by mere evidence found in the rubble. Cause is not something you find. Cause is something you construct. How you construct it and from what evidence, depends on where you look, what you look for, who you talk to, what you have seen before, and likely on who you work for.”
> 
>  Let’s approach this first with a software-centric thought experiment from Casey Rosenthal:
> 
> “Consider an example taken from a large-scale outage that was not publicized but resembles many high-profile outages. A configuration change was deployed that brought down a service. The outage was big enough that time-to-detect was almost immediate. The time-to-remediate took a bit longer though, on the order of about 40 minutes. Service was restored by reverting one single line of the configuration file. It’s tempting to say that the one line is the ‘root cause’ of the incident. Consider these possible alternative causes:
> 
> * The configuration wasn’t wrong; rather, the code that interpreted the configuration file wasn’t flexible enough.
> * The person who wrote the offending line wasn’t given enough context by their team, training, and onboarding process about the configuration to know how it would affect the system.
> * The system allowed a configuration change to be deployed globally all at once.
> * The parts of the organization closer to operations did not spend enough time with feature developers to understand how the latter might actually try to use the configuration file.
> * The person’s management chain did not set the appropriate priorities to allow for more testing, exploration, and review before the change was pushed.
> * The peers who signed off on the change were so busy because of external resource constraints that they didn’t have time to properly review the pull request.
> * The company doesn’t make enough money to support increasing the deployment costs high enough to run blue/green deployments whereby new configurations are run in parallel with the old until they are verified to be correct.
> 
> None of these alternatives are fixed as easily as reverting the one line. None of them suggest that they stem from the same ‘root.’ And yet, all of these alternatives are more fundamental to resilience than the one line of a configuration file.”


This is a lovely thought experiment from Casey on how root cause analysis focuses on the causes that we are conditioned to think of.

All systems are in fact socio-technical systems, that are more than just the software written, but depend on the social dynamics of the engineers, the context of the operations, and the management of the organisation behind them.


## [Understanding the Offense’s Systemwide Advantage in Cyberspace - Lawfare](https://www.lawfareblog.com/understanding-offenses-systemwide-advantage-cyberspace)

[https://www.lawfareblog.com/understanding-offenses-systemwide-advantage-cyberspace](https://www.lawfareblog.com/understanding-offenses-systemwide-advantage-cyberspace)

> By 1991, the U.S. National Research Council was trying to tackle how the advantage was “heavily to the attacker,” with the 1991 Computers at Risk report. The report’s recommendations are rooted in systemwide assessments of one-to-multitude attacks, such as “the current concern about virus attacks derives … from the total lack of a countermeasure [in Microsoft and Apple operating systems]” and “had such attacks been anticipated, the means to resist them could have been intrinsic to the systems.”
> 
> The dominance of the Microsoft operating system led to a “software monoculture,” which can “create aggregated risk like nothing else,” according to another major report by expert cybersecurity practitioners. The September 2003 report warned of a different kind of systemwide vulnerability: common-mode failures, like log4j, “a design fault that causes redundant copies of the same software process to fail under identical conditions,” which is as applicable to ransomware now as it was to viruses then:
> 
> The NIMDA and Slammer worms that attacked millions of Windows-based computers were examples of such “cascade failure”—they spread from one to another computer at high rates. Why? Because these worms did not have to guess much about the target computers because nearly all computers have the same vulnerabilities.
> 
> This was not mere opinion. Cascading failures were modeled to be far more likely once even a single exploitable flaw reached 43 percent prevalence in simulations, a threshold well below Microsoft and other systemically important software, then and now. Dan Geer, one of the report’s authors, later wrote that “only monocultures enable Internet-scale failure; all other failures are merely local tragedies.” As with all highly interconnected, tightly coupled systems, such “unacknowledged correlated risk of cyberspace” leads to very unpredictable, extremely high-consequence incidents.


This is a really interesting point.  We think of the internet as billions of different systems, but because much of it runs the same software, it's actually billions of clones of just thousands of systems.

Of course, this means that if you find an attack that works against one system, it's highly likely that it works again and again against other similarly implemented systems.  This is what drives a lot of cybercrime and low capability actor attacks.


## [FBI document shows what data can be obtained from encrypted messaging apps - The Record by Recorded Future](https://therecord.media/fbi-document-shows-what-data-can-be-obtained-from-encrypted-messaging-apps/)

[https://therecord.media/fbi-document-shows-what-data-can-be-obtained-from-encrypted-messaging-apps/](https://therecord.media/fbi-document-shows-what-data-can-be-obtained-from-encrypted-messaging-apps/)

> Dated to January 7, 2021, the document doesn’t include any new information but does a good job at providing an up-to-date summary of what type of information the FBI can currently obtain from each of the listed services.
> 
> As Forbes reporter Thomas Brewster said on Twitter earlier this week, past news reports have already exposed that the FBI has legal levers at its disposal to obtain various types of personal information even from secure messaging providers that often boast about providing increased privacy to their users.
> 
> While the document confirms that the FBI can’t gain access to encrypted messages sent through some services, the other type of information they can glean from providers might still help authorities in other aspects of their investigations.


I suspect that people are going to freak out about this, but this should mostly confirm what most people already should be aware.

If there is a good legal reason to believe that a subscriber is conducting illegal activities, and they are provided with an appropriate legal warrant, then these providers will hand over especially the metadata.

It's worth noting that backups are a real target here.  Systems that want to enable users to migrate from one device to another must store those messages in some accessible form, and iCloud or Google Drive backups are a good way to do that.


