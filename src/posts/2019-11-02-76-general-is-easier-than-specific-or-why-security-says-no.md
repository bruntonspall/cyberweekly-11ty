---
title: "76 - General is easier than specific, or why security says no"
date: 2019-11-02
description: "Why do we find rules in place that say \"No, you can't access twitter\" even when the person asking is the social media team?"
permalink: /general-is-easier-than-specific-or-why-security-says-no/
---

Why do we find rules in place that say "No, you can't access twitter" even when the person asking is the social media team?

I sometimes make fun of such rules, pointing about the clear absurdity, but in reality, there is a reason for such absurdities to exist.  The reason is that contextual thinking is really hard for people to do, and it's far more likely to cause a mistake.

Case in point, the actual threat model of electronic devices inside secure compartmented information facilities (SCIFs) is quite complicated.  There are concerns about malware getting in and out, about people smuggling data transfer devices, as well as classified TEMPEST and electromagnetic security concerns.  In reality, not every visitor, and not every device presents the same level of risk, and some facilities will allow certain devices in and out providing the risks are appropriately managed.  But it's far too complex to tell every visitor or staff member what all hte rules are, and in some cases, you might not even be allowed to tell some people what the rules are because it would reveal the capabilities that the intelligence agencies possess.  

Instead we set rules that just say "No electronic devices past this point", and then instruct the guards to verify that people have remembered to remove their smart watches, fitbits, phones, laptops and so on.  

I'm sure that some people who spend their lives going in and out of SCIF's would love to claim that they know the rules and should be allowed to determine what the correct devices are (I've certainly taken my Yubikey with me for example), but it's important to remember that even when we are specialists, we don't know everything, and furthermore, others around us who might be less capable will follow our lead.  

I'm reminded of a tweet I saw recently which said:

> [I can't tell you how many 'senior intelligence officers' I've worked with over the years - government, military, contractor - whose LinkedIn resumes look like they're goddamn Jack Ryan but who in reality are complete morons.](https://twitter.com/ZaknafienDC/status/1185310757451370496?s=20)

It's a good to remember that 50% of the membership of elite organisations like intelligence agencies are of course below average.  Our policies around security need to remember that as well.

## [Why Underachievers Dominate Secret Police Organizations: Evidence from Autocratic Argentina – American Journal of Political Science](https://ajps.org/2019/10/08/why-underachievers-dominate-secret-police-organizations-evidence-from-autocratic-argentina/)

[https://ajps.org/2019/10/08/why-underachievers-dominate-secret-police-organizations-evidence-from-autocratic-argentina/](https://ajps.org/2019/10/08/why-underachievers-dominate-secret-police-organizations-evidence-from-autocratic-argentina/)

> We show that those officers who underperformed early on in their careers were indeed more likely to serve in the secret police. Our results also demonstrate why this was the case. Low performers at the academy were less likely to attain advanced training, stuck at middling ranks, and faced a much higher risk of discharge. The resulting career pressure produced the incentive for underachievers to join the secret police. In addition, we find that the Argentine regime willingly exploited these career concerns and placed the most pressured agents in the most repressive unit within the secret police. Finally, we show that secret police service indeed paid off. Agents attained higher ranks and stayed longer in the security apparatus. These career boosting effects were most pronounced for agents with the lowest early career performance.
> 
> Taken together, our study identifies mundane but universal career concerns as the prime motivation to engage in arduous secret police work. This has important implications. Career pressures serve as the lubricant of repressive machines in autocracies. Leaders can exploit these incentives to maximize bureaucratic compliance. Institutionalized, meritocratic bureaucracies therefore do not contradict autocratic longevity. Likewise, governments can accomplish swift autocratic turns without major bureaucratic resistance. Officials facing career pressures are likely to serve as willing executioners, while their well-placed peers remain silent bystanders.


The most interesting tidbit from this to me is not only that underachievers are more incentivised to join or agree to carry out unethical actions, as the only way to progress their careers, but also that this actually does progress their careers, and ended up with people who had a disregard for ethics at more senior positions.  I think there's a lot of worrying implications that can be drawn from this research, because I doubt that it only applies to secret police organisations.


## [FireEye confirms that APT41 group hacked TeamViewer; Attacks might have accessed billions of devices](https://www.securitynewspaper.com/2019/10/14/fireeye-confirms-that-apt14-group-hacked-teamviewer-attackers-would-have-accessed-billions-of-devices/)

[https://www.securitynewspaper.com/2019/10/14/fireeye-confirms-that-apt14-group-hacked-teamviewer-attackers-would-have-accessed-billions-of-devices/](https://www.securitynewspaper.com/2019/10/14/fireeye-confirms-that-apt14-group-hacked-teamviewer-attackers-would-have-accessed-billions-of-devices/)

> According to the reports, attackers could control any computer that has logged into this service for perform arbitrary activities. The report reveals that TeamViewer was hacked in 2016, an incident that led to the theft of financial information from many users in as little as 24 hours.
> 
> Christopher Glyer, a researcher at security firm FireEye, revealed the incident via Twitter, further stating that users’ passwords are being leaked too. According to this firm, the hacking incident is the responsibility of the APT41 group, operating from Asia, specifically from China, and which has been linked to multiple high-profile malicious hacking operations.


(Joel) On the 21st of June (2019) TeamViewer announced it was deployed on over 2 billion devices (doubling from a billion in October 2015). While TeamViewer comes in a few different flavours (always-on or user-controlled) it is generally always installed with elevated permissions inside the operating system even if it is not running 24/7.

It is unknown how many devices allow complete control (command execution, file transfers etc) via TeamViewer (which is generally on by default) and those that require additional login windows before keyboard/video/mouse can be controlled (although irrelevant if TeamViewer is execution remote commands).

I wouldn't say this is cause to uninstall TeamViewer across an estate, but weigh how it is deployed and configured, including credential management and configuration options such as always-on -v- on-demand or what features are enabled in TeamViewer is connected. In general, if you're using TeamViewer for desktop support, TeamViewer should not be always-on and all actions should require end-user consent (if you feel the need to enable file transfers and command execution).


## [MESSAGETAP: Who’s Reading Your Text Messages? | FireEye Inc](https://www.fireeye.com/blog/threat-research/2019/10/messagetap-who-is-reading-your-text-messages.html)

[https://www.fireeye.com/blog/threat-research/2019/10/messagetap-who-is-reading-your-text-messages.html](https://www.fireeye.com/blog/threat-research/2019/10/messagetap-who-is-reading-your-text-messages.html)

> APT41's newest espionage tool, MESSAGETAP, was discovered during a 2019 investigation at a telecommunications network provider within a cluster of Linux servers. Specifically, these Linux servers operated as Short Message Service Center (SMSC) servers. In mobile networks, SMSCs are responsible for routing Short Message Service (SMS) messages to an intended recipient or storing them until the recipient has come online.


APT41 haven't been around that long.  They are connected to the same group who were behind the Winnti attacks on gaming companies and they seem to use the tools for personal gain as well as at opponents of China.  

Targeting SMS servers and looking for keywords, or specific targets of interest indicates a levelling up of this organisation.  Previously much of their work was far more "smash'n'grab" cyber heists, but this is far more below the radar attempts to gather intelligence.  It could be that we've missed some of the operations carried out by this group, or that they have new orders or new leadership that is giving them more espionage related tasks to carry out.

Because this is highly targeted, it's unlikely that most of us need to worry or change anything.  I'll stand by the advice that you probably shouldn't use SMS to exchange any personal or sensitive information anyway.


## [New Chrome 0-day Bug Under Active Attacks – Update Your Browser Now!](https://thehackernews.com/2019/11/chrome-zero-day-update.html?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+TheHackersNews+%28The+Hackers+News+-+Cyber+Security+Blog%29&m=1)

[https://thehackernews.com/2019/11/chrome-zero-day-update.html?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+TheHackersNews+%28The+Hackers+News+-+Cyber+Security+Blog%29&m=1](https://thehackernews.com/2019/11/chrome-zero-day-update.html?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+TheHackersNews+%28The+Hackers+News+-+Cyber+Security+Blog%29&m=1)

> Discovered and reported by Kaspersky researchers Anton Ivanov and Alexey Kulaev, the audio component issue in the Chrome application has been found exploited in the wild, though it remains unclear at the time which specific group of hackers.
> "Google is aware of reports that an exploit for CVE-2019-13720 exists in the wild," Google Chrome security team said in a blog post.
> "Access to bug details and links may be kept restricted until a majority of users are updated with a fix. We will also retain restrictions if the bug exists in a third party library that other projects similarly depend on, but haven’t yet fixed."


There is a Chrome "zero day" out there that is being used by an active group of hackers.  The fact that it is Kaspersky that have reported at least one of these, indicates that it's probably not just a small infection, but likely some reasonably advanced malware being used by an APT of some form.

The implication from this release is that other browser or other uses of the third party library may also be vulnerable, so there might be other vectors for attack out there.


## [The perils of security and how I finally resolved my Amazon fraud : sysadmin](https://www.reddit.com/r/sysadmin/comments/dpbt3t/the_perils_of_security_and_how_i_finally_resolved/)

[https://www.reddit.com/r/sysadmin/comments/dpbt3t/the_perils_of_security_and_how_i_finally_resolved/](https://www.reddit.com/r/sysadmin/comments/dpbt3t/the_perils_of_security_and_how_i_finally_resolved/)

> It wasn't my TV. In fact, I've never owned an Android device, or anything made by Huawei.
> 
> Of course I already suspected this, but the proof was plain to see. Now we're digging deeper. So it appears someone managed to access my account from another smart TV device (we assume) and make purchases through it. But why then, could I not see this device on my account dashboard or anywhere in my account settings for that matter? "Because," he explains, "non-Amazon devices, such as smart TVs, Roku devices, game consoles... do not show up there. In fact, even Amazon customer support cannot see those authorized devices. We have a special tool in this department to use to see all non-Amazon devices attached to your account."
> 
> I was baffled. How many people have rogue devices fraudulently attached to their account without their knowledge, waiting to be exploited? How did they get there in the first place? Old exploit? Unknown backdoor in a smart device app? Who's to say? And if they were added before OTP enhanced security made it's way to that particular platform, they can circumvent all 2FA requirements perpetually until removed and re-added.


Interesting take here.  I love the user experience of ordering an Amazon device, such as my kindle, my firetv stick or my Alexa, and opening up the box to have it say "Hi Michael".  It's already authed to my account, and it already knows who I am.

Additionally, I have a lot of Amazon devices, over 20 at the last count.  If I added or changed my 2FA method, for example, got a new Yubikey, and every single one was immediately disconnected until I went through a song and dance routine to re-auth it.... well, I probably wouldn't be able to convince any of my friends to turn on 2FA for their Amazon accounts.

However, the idea that allowing my smart tv to view videos from my Amazon Prime account, and maybe even buy new videos from that account also allows the same TV's API key to buy gift cards and ship them to other addresses without extra authorisation indicates a lack of contextual awareness around how to ship API keys and how criminals operate.  No criminal is going to find good value in buying films that are linked to your account, but buying tradeable physical items is something that should be restricted to normal web browsers.


## [WhatsApp sues Israeli firm, accusing it of hacking activists' phones | Technology | The Guardian](https://www.theguardian.com/technology/2019/oct/29/whatsapp-sues-israeli-firm-accusing-it-of-hacking-activists-phones?CMP=Share_iOSApp_Other)

[https://www.theguardian.com/technology/2019/oct/29/whatsapp-sues-israeli-firm-accusing-it-of-hacking-activists-phones?CMP=Share_iOSApp_Other](https://www.theguardian.com/technology/2019/oct/29/whatsapp-sues-israeli-firm-accusing-it-of-hacking-activists-phones?CMP=Share_iOSApp_Other)

> WhatsApp said it believed the technology sold by NSO was used to target the mobile phones of more than 1,400 of its users in 20 different countries during a 14-day period from the end of April to the middle of May.
> 
> In this brief period, WhatsApp believes those who were the subject of the cyber-attacks included leading human rights defenders and lawyers, prominent religious figures, well-known journalists and officials in humanitarian organisations.
> 
> A number of women previously targeted by cyber-violence, and individuals who have faced assassination attempts and threats of violence, as well as their relatives, were also the victims of the attacks, the company believes.
> 
> WhatsApp’s lawsuit, filed in a California court on Tuesday, has demanded a permanent injunction blocking NSO from attempting to access WhatsApp computer systems and those of its parent company, Facebook.
> 
> It has also asked the court to rule that NSO violated US federal law and California state law against computer fraud, breached their contracts with WhatsApp and “wrongfully trespassed” on Facebook’s property.


It's good to see the armies of highly paid lawyers at Facebook being put to good use.  I'm slightly dubious about the claim that NSO has wrongfully trespassed, but we'll have to see what the courts think about that.

It will be interesting to see if other communication companies follow suit, and whether this will set a precedent that commercial sales of hacking capabilities, even if to nation states, is not a viable business to be in.


## [In which I am a bit over this digital transformation business.](https://medium.com/@curiouscatherinehowe/in-which-i-am-a-bit-over-this-digital-transformation-business-b49f9bb4500)

[https://medium.com/@curiouscatherinehowe/in-which-i-am-a-bit-over-this-digital-transformation-business-b49f9bb4500](https://medium.com/@curiouscatherinehowe/in-which-i-am-a-bit-over-this-digital-transformation-business-b49f9bb4500)

> Change requires a relentless focus on the purpose and as others have said the ability to radiate positive intent. You need to be resilient and optimistic as you are not going to get it right most of the time. You need to be able to experiment but you also need to be able to design safe experiments — not because its wrong to fail but because only by designing safe experiments can you robustly learn as you have locked down as many elements as possible so that you can know when you are truly exploring something new.


I love this definition of change.  I've seen lots of digital transformation efforts that focus on technology, or focus on changing as if that's a result by itself.  "We should be more digital" is not a goal by itself, doing digital transformation is about changing your organisation, and that means being clear about what you are changing to, giving people a goal and a purpose.


## [Grumpy Old Person Agile - Product for the People](https://productforthepeople.xyz/grumpy-old-person-agile-d2465d875ac1)

[https://productforthepeople.xyz/grumpy-old-person-agile-d2465d875ac1](https://productforthepeople.xyz/grumpy-old-person-agile-d2465d875ac1)

> The right amount of governance at the right time in the right way. Agile is not the wild west. It totally needs a layer of governance. Just it needs to be horses for courses — not some generic approach used elsewhere. Governance brings assurance, assurance brings trust and trust opens doors for more modern ways of working.
> Work in the open (shocking I know!). Openness builds trust. It removes barriers. Sunlight is the best disinfectant. If you take away the mystery of these ways of working it takes away the fear. Change the language. Demonstrate the discipline needed (the idea that agile is the easy option remain prevalent and it couldn’t be further from the truth!)


Agile and Security are my bugbears.  Much like Jukesie, I loath the performative agile that is so common these days.  Teams who play with lego, or spend hours in retrospectives and futurespectives that serve no actual purpose.  Agile is about delivering value early and often, and about reacting to changes.  Agile is about people and relationships more than processes.

But what agile is not about is chaos personified.  It's not a way to "stick it to the man" and reject any form of oversight or governance.  Security teams need to have some ideas about what agile teams are doing, and in any reasonable size organisation, it would be impossible to attend every standup and show and tell, let alone put a person into every team.

Security teams need to provide better self service security, in the form of easy to use tools, guidance and self assessment frameworks that make it easy for teams to do the right thing.  They also need the right forms of light touch governance, so that they have confidence that the agile teams are actually using these tools, and can identify and help teams who have more serious security needs.


## [6 New MSPs and/or Cloud-Based Service Providers Compromised by Ransomware, A Total of 13 for 2019, Reports Armor - Armor](https://www.armor.com/reports/new-msps-compromised-reports-armor/)

[https://www.armor.com/reports/new-msps-compromised-reports-armor/](https://www.armor.com/reports/new-msps-compromised-reports-armor/)

> “This uptick in successful ransomware attacks against MSPs and/or Cloud-Based Service Providers is a harsh reminder that organizations have to ensure that the third-party vendors they do business with are as equally protected against the current and emerging cyber threats, as they are,” said Chris Hinkley, Head of Armor’s Threat Resistance Unit (TRU)research team.  “This is especially true, because as we have seen, a successful ransomware attack against a MSP/Cloud-Based Service Provider can be debilitating to their customers, as well as to their own company, as the attack can quickly shut down key systems which the customers depend on to run their organization.”
> 
> ”And of course, a ransomware attack against an MSP can be fatal, putting a MSP out of business, which appears to be the case with  PM Consultants, the Oregon-based IT consulting and IT support provider to dental practices, who after being hit by  ransomware in early July  subsequently shut their business down later that month, citing that they were doing so in part due to the ‘devastating event‘.”


I'm not convinced that "organizations have to ensure that the third party vendors they do business with are as equally protected against the current and emerging cyber threats, as they are" is a good take here.

In fact, if you run a cloud services organisation that has only 10 clients, you need to be better protected than any of your clients.  Your suppliers should be far and above your own security requirements, because they are more risky than you are.  If when you talk to your suppliers, they seem oblivious or need pointing at good security guidance, then maybe they aren't good enough to trust with your critical business.

I'll also add that Managed Service Providers generally control your computers, your user logins, your servers.  It's business critical.  Websites for schools may not be, but email, telephone support all those other things.  You need to be able to check whether what a supplier does would impact your business if they were unavailable.


## [Why Republicans Storming a SCIF Puts National Security at Risk | WIRED](https://www.wired.com/story/republicans-storm-scif-national-security-nightmare/)

[https://www.wired.com/story/republicans-storm-scif-national-security-nightmare/](https://www.wired.com/story/republicans-storm-scif-national-security-nightmare/)

> You don’t need a vibrant imagination to see how. The SCIF guidelines from ODNI list three categories of “high-risk” devices: multifunction cellular telephones, electronic devices with RF transmitting (e.g., Bluetooth), and photographic, video, and audio recording devices. Smartphones are all three. They can have malware, and malware can take over microphones and cameras. Making matters worse, the very people storming the SCIF are the among the most at risk of compromise from a sophisticated adversary. Who wouldn’t want to hack a congressperson?
> 
> “They’re definitely appealing targets,” says Mieke Eoyang, who worked as a staffer on the House Intelligence Committee and currently heads up the national security program at Third Way, a nonprofit think tank. “Foreign adversaries have been trying to collect on some of these people from the moment they announced. These are high-value intelligence targets, and well-known.”
> 
> It’s hard to overstate the extent to which the GOP members involved in the ruckus either didn’t know or didn't care about the kinds of risks they were inviting. Several of them not only brought their phones into the SCIF, they proudly tweeted that they had done so. Representative Alex Mooney (R-West Virginia) appears to have tried to livestream the affair, but settled for an audio dispatch.


I'm really torn on this story.  While storming a SCIF is a mind numbingly stupid thing to do, the reality is that almost none of the risks that SCIF security protocols are designed to protect against are actually realised by this action.

The real risks here is that many SCIF's are multi-purpose, that there will be people in there with classified or at least sensitive material lying around on their desk, on their screens or having conversations about them.  That information could have been captured in any live streams or photos sent from the area, and I'd expect almost every intelligence nation on the planet to have made copies of all the photos and looked through, just in case there is anything of use.

But even if a staffers phone was infected with malware, it's presence in the SCIF does not automatically allow that malware to jump the airgap onto classified systems, and malware that is designed to extract sensitive data from nearby computers generally requires careful placement and timing to work.


