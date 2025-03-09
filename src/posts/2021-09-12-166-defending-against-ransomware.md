---
title: "166 - Defending against ransomware"
date: 2021-09-12
description: "Ransomware infection is almost certainly the single most impactful cybersecurity incident that your company or organisation could suffer from."
permalink: /defending-against-ransomware/
---

Ransomware infection is almost certainly the single most impactful cybersecurity incident that your company or organisation could suffer from.

If you look at incident breach numbers, then users accidentally sharing information, cloud misconfiguration, and user account compromise are probably the most common incidents, but ransomware infection is both reasonably common and massively impactful on organisations, far more than individual data losses in many cases.

If you were to sit and try to predict for the coming year, how likely do you think it would be that you'd suffer a ransomware infection?  The numbers of reported infections continues to grow, and so the chances of an infection feels quite high.

Yet we more or less know the ways to defend against ransomware, because almost all ransomware has to follow the same chain of attack.  Initial access, local execution, network traversal (or lateral movement), and finally escalation of privilege.  

Sure, some actors have human directed malware and more advanced campaigns, but the reality is that most of this stuff is being carried out not by cyber ninjas, but by fairly lowly script kiddies who press the buttons to see if the thing worked.

If you can estimate how likely it is that you'll be hit by ransomware, you can start to look at your workload this coming quarter and ask yourself, "will this lower the chance of ransomware hitting me?" or "will this lower the impact of ransomware when it does hit me?".  If you aren't carrying out at least one action designed to resist the initial access, or reduce the ability of a single compromise to spread across the network, then you aren't doing enough to protect against ransomware attack.

## [Cobalt Strike, a Defender's Guide](https://thedfirreport.com/2021/08/29/cobalt-strike-a-defenders-guide/)

[https://thedfirreport.com/2021/08/29/cobalt-strike-a-defenders-guide/](https://thedfirreport.com/2021/08/29/cobalt-strike-a-defenders-guide/)

> In our research, we expose adversarial Tactics, Techniques and Procedures (TTPs) as well as the tools they use to execute their mission objectives. In most of our cases, we see the threat actors utilizing Cobalt Strike. Therefore, defenders should know how to detect Cobalt Strike in various stages of its execution. The primary purpose of this post is to expose the most common techniques that we see from the intrusions that we track and provide detections. Having said that, not all of Cobalt Strike’s features will be discussed.
> 
> As you have noticed from our reporting so far, Cobalt Strike is used as a post-exploitation tool with various malware droppers responsible for the initial infection stage. Some of the most common droppers we see are IcedID (a.k.a. BokBot), ZLoader, Qbot (a.k.a. QakBot), Ursnif, Hancitor, Bazar and TrickBot. Cobalt Strike is chosen for the second stage of the attack as it offers enhanced post-exploitation capabilities. Threat actors turn to Cobalt Strike for its ease of use and extensibility.


Cobalt Strike is used by red teams internally, as it's legitimate use, but it's also massively popular for actual attackers.  Learning how it works, what it looks like and how to detect it is important for defenders.


## [Confessions of a ransomware negotiator: Well, somebody's got to talk to the criminals holding data hostage • The Register](https://www.theregister.com/2021/09/03/how_to_be_a_ransomware/)

[https://www.theregister.com/2021/09/03/how_to_be_a_ransomware/](https://www.theregister.com/2021/09/03/how_to_be_a_ransomware/)

> He also told us that in general he doesn't expect to be dealing with the developers of the attack but rather a subset of staff within the criminal organisation that are basically the "Help Desk from Hell".
> 
> The more amateur operations use email to communicate with their "marks," which creates gaps that allow stalling whilst remediation efforts are being carried out. That is part of the balancing act the negotiator needs to maintain: making sure the criminals keep in contact, and are talking towards some sort of solution while the in-house IT professionals and his firm work to try to get things back on track.
> 
> Storm's technical team need time to try to disarm the ransomware and, if possible, resolve the issue without payment, Shah tells us, adding: "Negotiation is not about getting the lowest figure possible, it is mainly about getting information and time. My job is to get them time without the attackers becoming aware of the tactic."
> 
> But be clear when data is leaked, it stays leaked.
> 
> Shah explains: "The attackers will increase the pressure as time goes on. They are focused on getting payment as soon as possible and as such will make attempts to rush matters along.
> 
> [...]
> 
> His experience with these criminals has not left him very impressed, he says.
> 
> Firstly, the former NCA man says, they waste too much time on unrealistic demands and would make more money by asking for a number that can be put down as a cost of business then moving on.
> 
> Speaking about them personally, he adds: "It is important to note also that ransomware attackers are criminals – just like kidnappers. In most cases, they generally have the same incentives of financial gain, and as such a good negotiator will use the same skills in building a relationship and maintaining discussions to seek a resolution.


A reminder that many of the ransomware operators that people have to deal with are not advanced super criminals or nation states, but in fact people in the helpdesk from hell, or simply low scale criminals looking for a payout, using tools they don't really understand themselves.


## [An Analysis of Sidoh: WIZARD SPIDER's Exfiltration Tool | CrowdStrike](https://www.crowdstrike.com/blog/sidoh-wizard-spiders-mysterious-exfiltration-tool/)

[https://www.crowdstrike.com/blog/sidoh-wizard-spiders-mysterious-exfiltration-tool/](https://www.crowdstrike.com/blog/sidoh-wizard-spiders-mysterious-exfiltration-tool/)

> WIZARD SPIDER’s Sidoh has an aura of mystery due to its rarity and the keyword list it uses to determine what data is exfiltrated. As of this blog’s publication, CrowdStrike Intelligence has observed 16 unique SHA256 hashes, with nine of them containing unique build times (date and time of compilation) and with the first build date of June 16, 2019, and the last build date of Jan. 18, 2020. Sidoh searches for specific file types with a fixed set of keywords. If a file matches Sidoh’s criteria, it is exfiltrated via FTP to a hardcoded IP address. 
> 
> The list of keywords suggests the adversary is searching for and targeting data related to government, military and financial sectors. It is unknown if WIZARD SPIDER was using Sidoh to steal files for espionage purposes or if they were stealing files for extortion purposes. Stealing files for espionage purposes is unusual for criminal threat actors. However, GameOver Zeus3 was a previously observed criminal malware family that searched victim systems for files matching keywords related to foreign government officials, military documents, classified information and terrorism. 
> 
> [...]
> 
> WIZARD SPIDER is one of the most sophisticated groups tracked by CrowdStrike. Their threat arsenal ranges from banking trojans to spam bots to ransomware — with all of these tools designed with an end result of getting money from their victims. Some of these tools have been short-lived, but the diversity in tooling used by WIZARD SPIDER demonstrates their desire to use new strategies to monetize their attacks. It is unknown if Sidoh is one such strategy that experimented with monetizing victims by stealing potentially sensitive or proprietary data, or if Sidoh was used by WIZARD SPIDER to steal data from specific victims at the request of a third party.
> 
> There is even the possibility that the original Hermes source code (which Ryuk was derived from) was modified to be Sidoh, and the threat actors added the Ryuk file artifact references as a false flag. But the likely and simplest solution is Sidoh was used in rare instances to automatically steal data from compromised hosts by WIZARD SPIDER. 


The overlap between criminal groups, state sponsored groups and state directed groups appears to be quite blurry.  It is of course unclear whether this is actually the original criminal actors, or whether these infections are simply a state based actor who are using the TTP's of a criminal group.

Regardless of the truth, the blending of these attacker intents doesn't significantlly change the initial access vectors that they use.  Account compromise, malware by email attachment and vulnerable network endpoints are still the main vectors and need to be protected.


## [Emerging Ransomware Groups: AvosLocker, Hive, HelloKitty, LockBit 2.0](https://unit42.paloaltonetworks.com/emerging-ransomware-groups/)

[https://unit42.paloaltonetworks.com/emerging-ransomware-groups/](https://unit42.paloaltonetworks.com/emerging-ransomware-groups/)

> During our operations, we have observed four emerging ransomware groups that are currently affecting organizations and show signs of having the potential to become more prevalent in the future:
> 
> AvosLocker is ransomware as a service (RaaS) that started operations in late June, using a blue beetle logo to identify itself in communications with victims and “press releases” aimed at recruiting new affiliates. AvosLocker was observed promoting its RaaS program and looking for affiliates on dark web discussion forums and other forums. Like many of its competitors, AvosLocker offers technical support to help victims recover after they’ve been attacked with encryption software that the group claims is “fail-proof,” has low detection rates and is capable of handling large files. This ransomware also has an extortion site, which claims to have impacted six organizations in the following countries: the U.S., the U.K., the U.A.E., Belgium, Spain and Lebanon. We have observed initial ransom demands ranging from $50,000 to $75,000.
> Hive Ransomware is double-extortion ransomware that started operations in June. Since then, Hive has impacted 28 organizations that are now listed on the group’s extortion site, including a European airline company and three U.S.-based organizations. Hive uses all tools available in the extortion toolset to create pressure on the victim, including the date of initial compromise, countdown, the date the leak was actually disclosed on their site, and even the option to share the disclosed leak on social media.
> HelloKitty is not a new ransomware group; it can be tracked as early as 2020, mainly targeting Windows systems. However, in July, we observed a Linux variant of HelloKitty targeting VMware’s ESXi hypervisor, which is widely used in cloud and on-premises data centers. We also observed two clusters of activity. Across the observed samples, some threat actors preferred email communications, while others used TOR chats for communication with the victims. The observed variants impacted five organizations in Italy, Australia, Germany, the Netherlands and the U.S. The highest ransom demand observed from this group was $10 million, but at the time of writing, the threat actors have only received three transactions that sum up to about $1.48 million.
> LockBit 2.0 (previously known as ABCD ransomware) is a three-year-old RaaS operator that has been linked to some high-profile attacks lately following the June launch of a slick marketing campaign to recruit new affiliates. It claims to offer the fastest encryption on the ransomware market. LockBit 2.0 has impacted multiple industries – 52 victims are listed on the group’s leak site. Its victims include organizations in the U.S., Mexico, Belgium, Argentina, Malaysia, Australia, Brazil, Switzerland, Germany, Italy, Austria, Romania and the U.K.


Good write up of four new or repurposed ransomware groups emerging at the moment. 


## [LockFile ransomware’s box of tricks: intermittent encryption and evasion – Sophos News](https://news.sophos.com/en-us/2021/08/27/lockfile-ransomwares-box-of-tricks-intermittent-encryption-and-evasion/)

[https://news.sophos.com/en-us/2021/08/27/lockfile-ransomwares-box-of-tricks-intermittent-encryption-and-evasion/](https://news.sophos.com/en-us/2021/08/27/lockfile-ransomwares-box-of-tricks-intermittent-encryption-and-evasion/)

> In this detailed analysis of the LockFile ransomware, we reveal its novel approach to file encryption and how the ransomware tries to bypass behavior and statistics-based ransomware protection.
> 
> This article discusses the following key findings in depth:
> 
> LockFile ransomware encrypts every 16 bytes of a file. We call this “intermittent encryption,” and this is the first time Sophos researchers have seen this approach used. Intermittent encryption helps the ransomware to evade detection by some ransomware protection solutions because an encrypted document looks statistically very similar to the unencrypted original.
> Like WastedLocker and Maze ransomware, LockFile ransomware uses memory mapped input/output (I/O) to encrypt a file. This technique allows the ransomware to transparently encrypt cached documents in memory and causes the operating system to write the encrypted documents, with minimal disk I/O that detection technologies would spot.
> The ransomware doesn’t need to connect to a command-and-control center to communicate, which also helps to keep its activities under the detection radar.
> Additionally, LockFile renames encrypted documents to lower case and adds a .lockfile file extension, and its HTA ransom note looks very similar to that of LockBit 2.0.


Intermittent encryption is a genius idea.  As a user, almost all of ten document is relevant to you, so the ransomware doesn’t need to encrypt it all, just a couple of key sections and the document becomes unreadable.


## [Data Brokers Are Advertising Data on U.S. Military Personnel - Lawfare](https://www.lawfareblog.com/data-brokers-are-advertising-data-us-military-personnel)

[https://www.lawfareblog.com/data-brokers-are-advertising-data-us-military-personnel](https://www.lawfareblog.com/data-brokers-are-advertising-data-us-military-personnel)

> The data brokerage industry advertises data on many individuals and activities, and many vulnerable populations in particular, as documented in the report for Duke’s Sanford Cyber Policy Program. Military personnel are but one segment of the population whose information is currently held by data brokers and advertised as part of their product offerings. Among other problems with the data brokerage industry, the aggressive collection of data on military personnel presents risks to U.S. national security.
> 
> Three of the 10 data brokers surveyed for the report—Acxiom, LexisNexis and Nielsen—openly and explicitly advertise data on current and former U.S. military personnel. By no means are data sets on U.S. military personnel necessarily used for nefarious purposes: Current and former U.S. military personnel are a unique demographic, and as such, many different industries may want to target them with uniquely tailored advertisements for products and services. Some data brokers may also offer economic opportunities to businesses through the use of this information, without actually selling the information to the business client—for example, allowing a client insurance firm to run ads through the data broker’s platform, but without ever handing over the underlying data on particular individuals.
> 
> That said, many data brokers actively sell their data sets to willing buyers. There is little transparency, if any at all, into data brokerage transactions. There is also virtually nothing in U.S. law preventing data brokers from selling information on U.S. individuals to foreign entities. The data advertised by these brokers—spanning everything from financial transaction histories and internet browsing patterns to travel interests and support for political causes and organizations—could be used by foreign entities for a range of activities that damage national security. This could include building profiles on senior U.S. military personnel involved in key decisions relevant to a foreign power, or even building profiles on their family members and close acquaintances—some data brokers openly and explicitly advertise their ability to map network connections between individuals. All of this could theoretically aid information operations, coercion, blackmail, or intelligence gathering.


It’s tough to work out the implications of this.  Of course various good people want to use this form of targeting.  If you are advertising military careers, veterans benefits, post-service college credits or even just products and services that you think are relevant to service personnel, then narrowing your advertising down by “military personnel” is valuable.  

But of course, this dataset can also be used by bad people, whether simply to make information operations easier, or to target phishing attempts easily.

Other than dismantling the global advertising system, I don’t see an easy solution for this. 


## [Cloud Encryption is worthless! Click here to see why... - Chris Farris](https://www.chrisfarris.com/post/cloud-encryption/)

[https://www.chrisfarris.com/post/cloud-encryption/](https://www.chrisfarris.com/post/cloud-encryption/)

> Don’t be focusing on encryption before you first have your IAM and account governance houses in order!
> 
> It doesn’t matter how much encryption you have on your data. If I provide AWS the right AKIA and 40 character random gobbledygook, Amazon will happily decrypt and hand me your data.
> 
> Ok then, besides ninjas, what threats does encryption-at-rest protect against?
> 
> * Cloud Insider Threats - AWS has access to your data. As Rich Mogull wrote: “If you can see your data in a Web browser after entering only your account password, the odds are extremely high that your provider can read it as well.” However, there are segregation of duties at AWS, and the person in the S3 team with access to your bits is not the same person who has access to your KMS key. So the S3 engineer would need to meet and conspire with the KMS engineer at the nearby Starbucks and then decide they want to go after your data. Maybe what you have is so valuable it’s worth the risk to them. Perhaps you should keep that shit on-prem.
> * Bad Code Paths - KMS, even AWS Managed KMS, is tied to your account. Assuming a software bug in the S3 service removed some amount of access controls, KMS access controls might prevent the decryption of the data. As far as anyone knows this has never happened, but it’s not outside the realm of possibility.
> * Poor Cloud Hygiene - If you have an EBS Volume that is encrypted, and you snapshot that volume and accidentally share it to the world, access to the KMS key would be required to hydrate that snapshot into a volume in an adversary’s account. However if you have such crappy cloud hygiene, you’re probably also not encrypting things consistently, so focus on fixing the hygiene and stop having myopic focus on encryption.
> * Encryption-in-Transit in the hypervisor-plane - AWS documentations states that EBS encrypt/decrypt operations happen in the hypervisor of the compute node (not on the node where the volume is stored). As a result, the EBS I/O is encrypted when going across that back-end AWS network.


This warms the cockles of my heart.  One of my biggest bugbears is contextless security advice, and “encrypt your stuff” is contextless security advice.  Sure it’s useful in lots of cases, but there’s some performance, management, financial and complexity trade offs you need to make for that.

This article goes into detail explaining the likely threat models that on-disk encryption protects you against, and makes effort to point out that most of the threats in those categories are probably either not targeting you, or can simply get around the control.

Chris still says (and I agree) that when encrypting something is simply a matter of checking the box, with little downside, you should go ahead and do that.  But if you inherited or found a system where that didn’t happen, then you probably have other concerns you should fix first.


## [Root cause of failure, root cause of success – Surfing Complexity](https://surfingcomplexity.blog/2021/08/13/root-cause-of-failure-root-cause-of-success/)

[https://surfingcomplexity.blog/2021/08/13/root-cause-of-failure-root-cause-of-success/](https://surfingcomplexity.blog/2021/08/13/root-cause-of-failure-root-cause-of-success/)

> Succeeding at a project in an organization is like pushing a boulder up a hill that is too heavy for any single person to lift.
> 
> It doesn’t make sense to ask what the “root cause of success” is for an effort like this, because it’s a collaboration that requires the work of many different people to succeed. It’s not meaningful to single out a particular individual as the reason the boulder made it to the top.
> 
> Now, let’s imagine that the team got the boulder to the top of the hill, and balanced it precariously at the summit, maybe with some supports to keep it from tumbling down again.
> 
> Next, imagine that there’s a nearby baseball field, and some kid whacks a fly ball that strikes one of the supports, and the rock tumbles down.


This is a lovely analogy for why looking for a single root cause for failure is a bad idea.


## [Security Technology Arms Race 2021 Medal Event - Mark Dowd [pdf]](https://conference.hitb.org/hitbsecconf2021sin/materials/KEYNOTE%201%20-%20Security%20Technology%20Arms%20Race%20-%20Mark%20Dowd.pdf)

[https://conference.hitb.org/hitbsecconf2021sin/materials/KEYNOTE%201%20-%20Security%20Technology%20Arms%20Race%20-%20Mark%20Dowd.pdf](https://conference.hitb.org/hitbsecconf2021sin/materials/KEYNOTE%201%20-%20Security%20Technology%20Arms%20Race%20-%20Mark%20Dowd.pdf)

> Summary
> 
> 1) Memory corruption is still the most effective strategy for offense, but it’s advantages are eroding
> 
> 2) Increasingly, offense will replace memory corruption components with other logic flaws
> 
> 3) Defensive profits by improved detection facilities as a result of less powerful offensive toolkits, and moving to the cloud
> 
> The old adage “Defense needs to be right every time, offense only needs to be right once” will possibly be inverted!


Mark gave the keynote at HackInTheBox Singapore recently, and gave his predictions for the coming changes to cybersecurity in the future.

Due to the event, this is mostly focused on the security researcher and device vulnerability community.  His argument that unsafe memory operations are getting increasingly hard to find and exploit, and that this will cause a pivot to cryptographic vulnerabilities seems to hold up.  We’ve seen a number of fairly major vulnerabilities recently, and cryptography is notoriously hard to do right.  Given the aim of most offensive security researchers is to run executable code, expect the first targets to be anything that signs code or code updates.


## [Securing cloud workloads for speed and agility | McKinsey](https://www.mckinsey.com/business-functions/mckinsey-digital/our-insights/security-as-code-the-best-and-maybe-only-path-to-securing-cloud-applications-and-systems)

[https://www.mckinsey.com/business-functions/mckinsey-digital/our-insights/security-as-code-the-best-and-maybe-only-path-to-securing-cloud-applications-and-systems](https://www.mckinsey.com/business-functions/mckinsey-digital/our-insights/security-as-code-the-best-and-maybe-only-path-to-securing-cloud-applications-and-systems)

> But traditional cybersecurity mechanisms were not designed to ensure secure configuration or operate at the tempo required to capture the benefits of agility and speed that business leaders expect. As a result, as companies try to capture cloud value, they must adopt new security architectures and processes to protect their cloud workloads. Then cloud migration can increase not only the delivery of business value but also the security of their systems and applications compared with the old on-premises world.
> 
> “Security as code” (SaC)1  has been the most effective approach to securing cloud workloads with speed and agility. At this point, most cloud leaders agree that infrastructure as code (IaC) allows them to automate the building of systems in the cloud without error-prone manual configuration. SaC takes this one step further by defining cybersecurity policies and standards programmatically, so they can be referenced automatically in the configuration scripts used to provision cloud systems and systems running in the cloud can be compared with security policies to prevent “drift”


Valuable if your security or executive leadership wont believe you when you tell them you need a security as code programme.  Even McKinsey agrees that Security as Code (and relatedly Code as Compliance) are the most robust way to secure modern cloud systems.


