---
title: "154 - 2021 is the year of ransomware"
date: 2021-06-20
description: "I've been saving a few of these articles for weeks.  I've talked before about the fact that I don't generally do \"news\" here.  I like to have time to read a number of perspectives and let the initial excitement die down so that I can get a good grip of the facts."
permalink: /2021-is-the-year-of-ransomware/
---

I've been saving a few of these articles for weeks.  I've talked before about the fact that I don't generally do "news" here.  I like to have time to read a number of perspectives and let the initial excitement die down so that I can get a good grip of the facts.

There have been so many ransomware incidents in the last few months that have hit the news that almost everybody has heard about the concept now.  The Colonial pipeline attack by darkside, the [ireland health service attacked by Conti](https://www.bbc.co.uk/news/world-europe-57197688) and of course, NotPetya and Wannacry, both strains of ransomware that weren't in fact ransomware.  The increased profits available to ransomware operators mean that they can afford to invest significant technical effort, buy zero-days and employ professional coders to work on their systems.

Furthermore, as Proofpoint says, the criminal enterprise that fuels ransomware is evolving, and that's the thing that worries me the most.  Initial access brokers, hacking teams who compromise a company and then sell on the access are fueling a market.  That market might be used right now to deploy ransomware as the quickest and easiest way to turn that access into money, but let's be clear, this is bad people buying access to run arbitrary code on your systems.  That means that they could deploy stealthy bitcoin mining, they could deploy integrity modifying software that adds records to your business systems, they could use you to send spam.  

Worse, because that initial access broker can sell the access, they might sell it to lots of people, one after another.  The first gets the use they want, and then finally they sell it to someone who will burn it all down in the way that ransomware does.

Biden met with Putin in Switzerland recently, and where in the 80's and 90's the topic of conversation was about nuclear weapons and how the world would deal with these nuclear powers, in 2021, the meeting is about cybersecurity, ransomware and tolerated if not actively supported criminal enterprises.  

But behind it all, the defences remain the same for individual victims:

* Ensure that your devices are patched and deploy good end user device protection tooling that can detect and prevent the initial access ransomware from running.
* Use MFA for administrative accounts as the lowest possible bar, and deploy MFA for as many users as possible.  Use SMS, Phone calls, TOTP or hardware tokens, any of them are sufficient to raise the bar, and don't let perfect be the enemy of good here, just deploy it.
* Take good backups and practice restoring from them.  Make sure that someone who has administrative access cannot delete or modify the backups.

## [Biden says 16 sectors should be off limits to attack - IT Security Guru](https://www.itsecurityguru.org/2021/06/17/biden-says-16-sectors-should-be-off-limits-to-attack/?utm_source=feedly&utm_medium=rss&utm_campaign=biden-says-16-sectors-should-be-off-limits-to-attack)

[https://www.itsecurityguru.org/2021/06/17/biden-says-16-sectors-should-be-off-limits-to-attack/?utm_source=feedly&utm_medium=rss&utm_campaign=biden-says-16-sectors-should-be-off-limits-to-attack](https://www.itsecurityguru.org/2021/06/17/biden-says-16-sectors-should-be-off-limits-to-attack/?utm_source=feedly&utm_medium=rss&utm_campaign=biden-says-16-sectors-should-be-off-limits-to-attack)

> In a speech on Wednesday, the U.S. President, Joe Biden told the Russian President, that 16 sectors of critical infrastructure should be “off-limits” to attacks, specifically cyberattacks. Unfortunately, analysts believe his efforts to be futile. Robert Golladay, the EMEA and APAC director at Illusive claims that “the fact that one of the leaders of the free world stood up to discuss Ransomware on a global stage is significative. We are in the middle of a global digital pandemic, with cyberattacks happening on all shores, in all countries, in all sectors.  And just as it will take a global effort to control the coronavirus pandemic, a multinational effort is necessary to take on the scourge of these ransomware attacks and prosecuting the criminals behind them.”
> 
> The U.S. President was not specific about which areas he believes should be out of bounds, though he was most likely referring to the 16 sectors designated as critical by Homeland Security. These include telecommunications, healthcare, food and energy. In his speech, Biden stated that: “We [the U.S. and Russia] agreed to task experts in both our countries to work on specific understandings about what is off-limits. We’ll find out whether we have a cybersecurity arrangement that begins to bring some order.”


Such positioning by the US is important for setting some global norms.  The key here is the recognition that inaction by states against criminals operating within their jurisdiction, but against other countries territories needs to be handled appropriately.  The question of whether these groups are state sanctioned or supported is an additional slice on top of this, but when a country makes it an easy environment for these organisations to operate, that has an economic impact on other countries around the world.


## [The First Step: Initial Access Leads to Ransomware | Proofpoint US](https://www.proofpoint.com/us/blog/threat-insight/first-step-initial-access-leads-ransomware)

[https://www.proofpoint.com/us/blog/threat-insight/first-step-initial-access-leads-ransomware](https://www.proofpoint.com/us/blog/threat-insight/first-step-initial-access-leads-ransomware)

> Ransomware attacks still use email -- but not in the way you might think. Ransomware operators often buy access from independent cybercriminal groups who infiltrate major targets and then sell access to the ransomware actors for a slice of the ill-gotten gains. Cybercriminal threat groups already distributing banking malware or other trojans may also become part of a ransomware affiliate network. The result is a robust and lucrative criminal ecosystem in which different individuals and organizations increasingly specialize to the tune of greater profits for all—except, of course, the victims.  
> 
> Preventing ransomware via email is straightforward: block the loader, and you block the ransomware.  
> 
> Typically, initial access brokers are understood to be opportunistic threat actors supplying affiliates and other cybercrime threat actors after the fact, for example by advertising access for sale on forums. But for the purposes of this report, we consider initial access brokers to be the groups who obtain initial access via first-stage malware payloads and may or may not work directly with the ransomware threat actors. 
> 
> [...]
> 
> Ransomware threat actors currently carry out “big game hunting,” conducting open-source surveillance to identify high-value organizations, susceptible targets, and companies’ likely willingness to pay a ransom. Working with initial access brokers, ransomware threat actors can leverage existing malware backdoors to enable lateral movement and full domain compromise before successful encryption.  


This is somewhat misleading, but interesting none the less.

This isn't saying that you wont get infected by ransomware because somebody is able to click a link in an email, you probably will still.  What it's saying is that the people who send yuo that email and compromise your system are probably not the same people who deploy the ransomware and demand the money.  

Instead the majority of ransomware groups are buying access from these initial access brokers, marketplaces where they can buy already compromised systems, and then deploy their ransomware into them.

That means that fighting this menace isn't as simple as taking down the ransomware gangs, because as long as the initial access brokers are still able to provide a heavy supply of compromised systems, there will always be new ransomware gangs or worse popping up to take advantage of that market.


## [Conti Ransomware Gang: An Overview](https://unit42.paloaltonetworks.com/conti-ransomware-gang/)

[https://unit42.paloaltonetworks.com/conti-ransomware-gang/](https://unit42.paloaltonetworks.com/conti-ransomware-gang/)

> Most of these actors use the same methods of access found in many ransomware attacks, such as phishing emails and exploiting unprotected internet-facing applications, the lack of multi-factor authentication (MFA), as well as the typical avenues used to preserve and enhance access once it’s achieved, such as through the use of Cobalt Strike or PowerShell.
> 
> These approaches are not particularly clever or sophisticated, but often they are effective. Conti’s methodology often follows the “double extortion” approach that many leading ransomware groups are presently using. When using double extortion, attackers will not only lock up a victim’s files and demand ransom, but they will also steal files and threaten to publish them on a website or otherwise leak them if their initial ransom demand is not met.
> 
> But Conti’s methods do have atypical elements.
> 
> Usually, the more successful ransomware operators put a lot of effort into establishing and maintaining some semblance of “integrity” as a way of facilitating ransom payments from victims. They want to establish stellar reputations for “customer service” and for delivering on what they promise – that if you pay a ransom, your files will be decrypted (and they will not appear on a leak website). Yet in our experience helping clients remediate attacks, Conti has not demonstrated any signs that it cares about its reputation with would-be victims.
> 
> In one recent case, Conti did not return a client’s files who had paid the ransom. This client got only a small fraction of the file restorations that were promised before the Conti ransomware representatives disappeared back into the dark web. In another case, our client needed an inventory of all files accessed, so that they could notify parties whose data was affected. Conti agreed to share that information if a payment was made, then changed their minds, saying, “We do not own that data anymore. It was deleted and there is no chance to restore it.” Like many ransomware gangs, Conti is constantly adapting to changes, including recent heightened scrutiny by law enforcement and policy makers following high-profile disruptive attacks on the Colonial pipeline and healthcare organizations. When Ireland's healthcare system refused to pay any ransom, Conti provided the agency with what it said was a free decryption key. But there was a twist: The group maintained that it would still make good on its "double extortion" threat to publish stolen data on its leak site.


Slightly frustrating that this isn't more in depth, but useful none the less.  

It's clear that Conti recognises that many of its victims don't care about it's reputation for playing fair.  To some degree, I'm not sure why we expect criminals to play fair, but I think this also speaks to the narrowness of the cybersecurity field.  We might know that Conti won't honour the ransoms fully, but do the victims?  If they don't they might be just tempted to pay rather than talk to a cyber security firm who might advise them not to.

It also a possibility that Conti may well be executing it's exit plan.  There's no need to worry about your reputation if you are already hiving money off and planning to kill the group and reinvent yourself later.


## [Department of Justice Seizes $2.3 Million in Cryptocurrency Paid to the Ransomware Extortionists Darkside | OPA | Department of Justice](https://www.justice.gov/opa/pr/department-justice-seizes-23-million-cryptocurrency-paid-ransomware-extortionists-darkside)

[https://www.justice.gov/opa/pr/department-justice-seizes-23-million-cryptocurrency-paid-ransomware-extortionists-darkside](https://www.justice.gov/opa/pr/department-justice-seizes-23-million-cryptocurrency-paid-ransomware-extortionists-darkside)

>  The Department of Justice today announced that it has seized 63.7 bitcoins currently valued at approximately $2.3 million. These funds allegedly represent the proceeds of a May 8, ransom payment to individuals in a group known as DarkSide, which had targeted Colonial Pipeline, resulting in critical infrastructure being taken out of operation. The seizure warrant was authorized earlier today by the Honorable Laurel Beeler, U.S. Magistrate Judge for the Northern District of California.
> 
> “Following the money remains one of the most basic, yet powerful tools we have,” said Deputy Attorney General Lisa O. Monaco for the U.S. Department of Justice. “Ransom payments are the fuel that propels the digital extortion engine, and today’s announcement demonstrates that the United States will use all available tools to make these attacks more costly and less profitable for criminal enterprises. We will continue to target the entire ransomware ecosystem to disrupt and deter these attacks. Today’s announcements also demonstrate the value of early notification to law enforcement; we thank Colonial Pipeline for quickly notifying the FBI when they learned that they were targeted by DarkSide.”


Ransomware is driven by profits, pure and simple, and this move by the US, chasing down the payment and in essence legally stealing it back deprives the ransomware operator of the gains of their work.

This is probably single handedly the best deterrant that can happen, however it doesn't feel like it can scale.  Unless the US can offer this as a service to every small organisation that gets affected, this just marks certain critical potential victims as out of scope.  

That's a great position for the US government in protecting its critical national infrastructure, but all it will more widely  redirect the attackers to the rest of us.  This needs action to also take down the ransomware operators and deny, disrupt and defeat their entire chain of operations to actually be effective


## [Ukrainian police arrest Clop ransomware members, seize server infrastructure - The Record by Recorded Future](https://therecord.media/ukrainian-police-arrest-clop-ransomware-members-seize-server-infrastructure/)

[https://therecord.media/ukrainian-police-arrest-clop-ransomware-members-seize-server-infrastructure/](https://therecord.media/ukrainian-police-arrest-clop-ransomware-members-seize-server-infrastructure/)

> Multiple suspects believed to be linked to the Clop ransomware cartel have been detained in Ukraine this week after a joint operation from law enforcement agencies from Ukraine, South Korea, and the US.
> 
> The arrests, reported today by the Ukraine National Police and the country’s Cyber Police division, come after authorities conducted searches at 21 residences in Kyiv, the country’s capital, and nearby regions.
> 
> Following the operation, authorities reported that they successfully shut down server infrastructure used by the gang members to launch past attacks.
> 
> Computers, smartphones, and server equipment were seized, together with 5 million Ukrainian hryvnias ($185,000), which authorities believe were obtained from ransoming companies across the world.


Another gang gone, but what's interesting here is that the videos and pictures show that the Clop ransomware gang was a professional organisation.  No dingy basements with hackers in hoodies, this is a business, with nice houses, professional looking macs and good pay.


## [The hard truth about ransomware: we aren’t prepared, it’s a battle with new rules, and it hasn’t near reached peak impact. - Kevin Beaumont](https://doublepulsar.com/the-hard-truth-about-ransomware-we-arent-prepared-it-s-a-battle-with-new-rules-and-it-hasn-t-a93ad3030a54)

[https://doublepulsar.com/the-hard-truth-about-ransomware-we-arent-prepared-it-s-a-battle-with-new-rules-and-it-hasn-t-a93ad3030a54](https://doublepulsar.com/the-hard-truth-about-ransomware-we-arent-prepared-it-s-a-battle-with-new-rules-and-it-hasn-t-a93ad3030a54)

> I've talked about ransomware and extortion attacks on organizations for about a decade. I recently spent a year at Microsoft in Threat Intelligence in Redmond, which included tracking ransomware gangs. I’ve been on the front lines of cybersecurity at the coal face — I am again now — for decades, and the reality is: Houston, we have a (big) problem.
> 
> We are rebuilding entire economies around technology, while having some fundamental issues reducing foundations to quicksand.
> 
> What we are seeing currently is a predictable crisis, which hasn’t yet near peaked. I’m not sure people generally understand the situation yet. The turning circle to taking action is large. With this post, I hope to lay out the reality, and some harsh truths people need to hear.
> 
> [...]
> By the way, my way to position this for business people is: ransomware is the risk of your business having a heart attack. If your IT is lifeblood of operations, doing things that can truly lead to ransomware is a risk to your business existing. Recovery is open heart surgery.


(Joel) Kevin covers a lot here and it was quite hard to pick a quote, let alone a focal point to cover succinctly in CyberWeekly.

My take-away isn't actually quite one of Kevin's points but its one that remains an executive motivation that is quite hard to nail down and make land/stick even with ransomware incidents within the same sector:
Organisations and their governance processes primary assess likelihood before impact within risk discussions. If people do not think ransomware gangs will target their organisation, the defenders (IT/cyber folks) have to switch tact and achieve ransomware defences by tacking that on to another risk or request.

A compliance team may want more features in Microsoft 365, or the Data Officer wants everyone to have Power BI Pro. If you can leverage this into Microsoft E5, the IT/cyber teams get the Defender products on the sly. As Kevin says in the full post, you can't leave these things half implemented though.

I usually describe consequences to boards in terms of downtime: "Nobody will be able to work (check emails, access file/documents, organise meetings, use their laptop/smartphone etc) for at least 3-4 weeks. Is that OK?". That tends to hit the spot.


## [Ransomware Actors Evolved Operations in 2020 | CrowdStrike](https://www.crowdstrike.com/blog/ransomware-actors-evolved-operations-in-2020/)

[https://www.crowdstrike.com/blog/ransomware-actors-evolved-operations-in-2020/](https://www.crowdstrike.com/blog/ransomware-actors-evolved-operations-in-2020/)

> Why is ransomware so prevalent? In short, ransomware with data extortion remains a lucrative tactic for eCrime adversaries to monetize their presence in a victim organization’s network. Fueled by increasingly larger ransom demands, eCrime adversaries continue to develop tactics and tools that allow them to slip past legacy antivirus virtually unnoticed. Following a ransomware incident, many organizations may find that they do not have adequate backups, or that their backups became encrypted, and they have few options but to pay the ransom. In addition, some cyber insurance companies, during cost-benefit analysis, may find that paying the ransom is a less costly option than rebuilding systems and incurring credit monitoring and legal fees due to the disclosure of regulated data by an eCrime adversary. 
> 
> CrowdStrike recommends the following practices: 
> * Build a bulletproof backup strategy. When it comes to ransomware, how you’ve configured your backups is critical. Attackers often delete backups before deploying ransomware so you are more inclined to pay. Some steps to consider include purchasing an immutable backup solution, using separate non-domain accounts with multi-factor authentication to administer your backup solution, retaining multiple copies of data on different media with one of them being off-site, keeping at least one copy of your backups offline or on an otherwise air-gapped network, and closely monitoring your backup solution for evidence of data exfiltration, whether it’s on-premises or in the cloud. eCrime adversaries have publicly boasted about utilizing cloud backups for data exfiltration, and CrowdStrike recommends taking steps to prevent threat actors from accessing cloud backup infrastructure in the event of a compromise. This can involve using non-domain accounts for cloud management and multi-factor authentication.
> * Use multi-factor authentication. Organizations can improve their security posture by enabling multi-factor authentication on all public-facing employee services and portals as well as restricting internet-facing protocols such as RDP and Server Message Block. This will inhibit unauthorized access to the organization’s environment.
> * Implement next-generation endpoint protection. Organizations can improve their security posture by utilizing advanced endpoint protection across their environment. The agent should leverage machine learning to identify anomalies and perform heuristic analysis, in addition to conducting antivirus and anti-malware activities in real time. The agent should be capable of detection and prevention, allow for remote network containment of assets pending investigation and/or remediation, and detect unmanaged assets within the corporate environment. 


An interesting report showing some of the changing nature of ransomware groups.  

The bad news?  Expect it to keep growing and getting worse

The good news?  Crowdstrike's advice is the same as mine, although in a different order.  Use 2FA and modern end point protection software, and you'll be resistant to much of the malware out there.  Adding backups that are write only, cannot be deleted, and owned by different accounts means that you'll be able to recover if you do get hit.


## [Most firms face second ransomware attack after paying off first | ZDNet](https://www.zdnet.com/article/most-firms-face-second-ransomware-attack-after-paying-off-first/)

[https://www.zdnet.com/article/most-firms-face-second-ransomware-attack-after-paying-off-first/](https://www.zdnet.com/article/most-firms-face-second-ransomware-attack-after-paying-off-first/)

> Some 80% of organisations that paid ransom demands experienced a second attack, of which 46% believed the subsequent ransomware to be caused by the same hackers. Amongst those that paid to regain access to their systems, 46% said at least some of their data was corrupted, according to a Cybereason survey released Wednesday. Conducted by Censuswide, the study polled 1,263 security professionals in seven markets worldwide...


(Joel) Well... I can't say I'm surprised.

You may or may not be sent a decryptor should you be ransomware'd then choose to pay. The decryptor may be very slow, or perhaps not even work for all of the files/systems (particularly on servers instead of normal laptops). Payment indicates that was your best option. There is no guarantee at all that persistent access isn't left behind, particularly since your best option was to pay so... could you detect persistence?

Whether you use the decryptor and/or restore backups, you're probably returning your system to the same (or comparable) state than when it was hosed... so even without persistence the same attacker or other (now that its obvious you've paid out) could hit you again for less recon than the first time around.

Oh, and paying ransomware is funding organised crime.

1. Have malware-resistant backups and practised up-to-date processes, which particularly includes your IT staff being able to operate out of band from the system that was just compromised.
2. Don't pay ransomware folks
3. See (1)


## [Latvian National Charged for Alleged Role in Transnational Cybercrime Organization | OPA | Department of Justice](https://www.justice.gov/opa/pr/latvian-national-charged-alleged-role-transnational-cybercrime-organization)

[https://www.justice.gov/opa/pr/latvian-national-charged-alleged-role-transnational-cybercrime-organization](https://www.justice.gov/opa/pr/latvian-national-charged-alleged-role-transnational-cybercrime-organization)

> Alla Witte, aka Max, 55, is charged in 19 counts of a 47-count indictment, which accuses her of participating in a criminal organization referred to as the “Trickbot Group,” which deployed the Trickbot malware. The Trickbot Group operated in Russia, Belarus, Ukraine, and Suriname, and primarily targeted victim computers belonging to businesses, entities, and individuals, including those in the Northern District of Ohio and elsewhere in the United States. Targets included hospitals, schools, public utilities, and governments. Witte, who previously resided in Paramaribo, Suriname, was arrested on Feb. 6, in Miami, Florida.
> 
> [...]
> 
> Witte and her co-conspirators allegedly worked together to infect victim computers with the Trickbot malware designed to capture online banking login credentials and harvest other personal information, including credit card numbers, emails, passwords, dates of birth, social security numbers and addresses. Witte and others also allegedly captured login credentials and other stolen personal information to gain access to online bank accounts, execute unauthorized electronic funds transfers and launder the money through U.S. and foreign beneficiary accounts.
> 
> According to the indictment, Witte worked as a malware developer for the Trickbot Group and wrote code related to the control, deployment, and payments of ransomware. The ransomware informed victims that their computer was encrypted, and that they would need to purchase special software through a Bitcoin address controlled by the Trickbot Group to decrypt their files. In addition, Witte allegedly provided code to the Trickbot Group that monitored and tracked authorized users of the malware and developed tools and protocols to store stolen login credentials.


The biggest surprise out of this, apart from the depressing fact that this means that Trickbot group had more female developers than most blueteams out there.

Alla Witta was living in Miami Florida, meaning that the complaints about this being an eastern european gang, while somewhat valid, includes remote working from all over the world.

There's more analysis of this [by Krebs](https://krebsonsecurity.com/2021/06/how-does-one-get-hired-by-a-top-cybercrime-gang/) and [at ZDnet](https://www.zdnet.com/article/after-doj-arrest-of-latvian-trickbot-user-experts-highlight-public-private-efforts/)


## [Case Study: Password Analysis with BloodHound – Posts By SpecterOps Team Members](https://posts.specterops.io/case-study-password-analysis-with-bloodhound-a3d264736c7)

[https://posts.specterops.io/case-study-password-analysis-with-bloodhound-a3d264736c7](https://posts.specterops.io/case-study-password-analysis-with-bloodhound-a3d264736c7)

> BloodHound is a fantastic tool for analyzing Active Directory, but that’s really just the beginning. The BloodHound database is a resource that enables users to execute all sorts of queries — the only limit is your creativity. 
> 
> BloodHound enhances our analysis by keeping track of several useful pieces of information for every account: what level of privilege the user has, what AD security groups it effectively belongs to, and whether the account is even enabled in the first place. If the script detects password reuse, and checks in with BloodHound before logging it, there is an opportunity to make one very smart analysis script.


This is a nice example of using a red team tool for blue team activities.  Just because a tool can be used to snaffle through an AD system looking for admin accounts doesn't just mean it's for offensive use.  Instead you can use it as part of a continual assurance mechanism to detect and alert on when something has gone wrong


## [Revealed: Government ministry hacked by foreign power](https://www.brusselstimes.com/belgium/171473/georges-gilkinet-sncb-train-reservation-system-would-be-impractical-study-finds/)

[https://www.brusselstimes.com/belgium/171473/georges-gilkinet-sncb-train-reservation-system-would-be-impractical-study-finds/](https://www.brusselstimes.com/belgium/171473/georges-gilkinet-sncb-train-reservation-system-would-be-impractical-study-finds/)

> The entire computer system of the federal home affairs ministry was subject to a full, complicated cyber-attack as far back as April 2019, with all fingers pointing to China, according to De Standaard.
> 
> Unlike many other cyber-attacks, this one was clearly aimed at the collection of information rather than money. The ministry is one of the central links in Belgium’s whole system of government, in charge of the population register, election management, police databases, crisis management and so on.


This is pointing at a further target of the HAFNIUM campaign against Exchange servers, although there's not enough information to make a serious judgement about the potential impact.


## [Google Workspace and Google Chat are officially available to everybody - The Verge](https://www.theverge.com/2021/6/14/22532559/google-workspace-chat-officially-available-consumer-gmail-spaces)

[https://www.theverge.com/2021/6/14/22532559/google-workspace-chat-officially-available-consumer-gmail-spaces](https://www.theverge.com/2021/6/14/22532559/google-workspace-chat-officially-available-consumer-gmail-spaces)

> With the switch, Google Chat messaging should be an option for all now, which can include direct messages and chat Rooms. But Google is also introducing a new terminology to go along with the announcement. It is announcing the “evolution of Rooms in Google Chat to Spaces.”
> 
> A Space is essentially the same thing as a chat Room, but Google wants to separate them out into their own top-level form of communication next to Gmail, Chat, and Meet. Google is layering on a few new features like improved message threading, more emoji reactions, user roles, moderation tools, and “discoverable” spaces. In that sense, it seems that Spaces wants to serve both as a Slack competitor and as a competitor for public Discord groups and, well, maybe as an optional replacement for email groups.
> 
> It’s a little confusing — but that’s par for the course for Google’s messaging strategy.


Snarky but accurate.  As a reminder before Google chat there was Google hangouts, Google meet, google messenger, Google chat, Google plus and Google wave.  But sure, let’s take the already confusing Google rooms within Google Chat and add Google Spaces to the equation.


