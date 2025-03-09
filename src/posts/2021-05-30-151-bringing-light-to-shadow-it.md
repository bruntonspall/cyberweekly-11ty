---
title: "151 - Bringing light to shadow IT"
date: 2021-05-30
description: "Generally speaking, users don't break security protocols on purpose."
permalink: /bringing-light-to-shadow-it/
---

Generally speaking, users don't break security protocols on purpose.

They don't squeeze through the access door without badging in because they want to make your life harder.  They don't click on links in emails to find out if the malware works, and they don't copy your data to outside systems just for laughs.

Users have a job to do, and they're normally trying to get it done as best as they can.

In many cases, users do not have the context, education and training to make security decisions.  They haven't spent every weekend reading the latest blogs about new badUSB attacks or the rising threat of ransomware.  Instead they concentrate on doing their jobs. 

Sometimes they learn about new technologies, tools and systems that might make their life easier.  In my experience, if security and IT are approachable, friendly and supportive, then they'll drop in a ticket or email just saying "Hey I heard about AirTable/Trello/Cheg/Quizlett, and wondered if we could use it". 

But since, even if you are personally lovely, most people's experience of IT or Security desks is pretty shoddy, they are far more likely to give the site a once over.  They might check whether it's got a green padlock, because that says that it's secure, and then they'll start using it.  This is especially true if it does something that helps them do their job more effectively, easily and quickly.  

People are generally pretty lazy as a collective.  If it's more work to get a third party tool than to use the thing they've been provided, then they tend not to do it.  So if you provide people with the tools they need for their job, then this kind of problem doesn't happen.

But it's not as simple as that.  Because how someone actually does their job is often different to how IT or managers think that the job is done.  If you don't observe people doing the job, you might find yourself saying "But we provide Sharepoint, and with just <insert ridiculously complex process here> they could do that without the external tool".  People value user experience, they like tools that are easy to use, and that have joy in their use.

You might argue that Teams is on paper, a better tool than Slack for team based real time communications.  And if you are doing an MBA style analysis of the features and capabilities of the tools, you might be right.  But yet most of the people I deal with absolutely loathe their work Teams experience, and find Slack joyful to use.  Slack represents the ultimate shadow IT, it's free to setup, easy to use, and absolutely joyful to use.

So if you want to challenge that shadow IT, then you need to provide corporate tools that are easier and more joyful to use than Slack.  Or just buy slack for them perhaps.

## [US Soldiers Expose Nuclear Weapons Secrets Via Flashcard Apps - bellingcat](https://www.bellingcat.com/news/2021/05/28/us-soldiers-expose-nuclear-weapons-secrets-via-flashcard-apps/)

[https://www.bellingcat.com/news/2021/05/28/us-soldiers-expose-nuclear-weapons-secrets-via-flashcard-apps/](https://www.bellingcat.com/news/2021/05/28/us-soldiers-expose-nuclear-weapons-secrets-via-flashcard-apps/)

> At first glance, many appear uninteresting. Virtually all the sets share the same generic textbook knowledge that soldiers learn to pass career development courses. These include definitions of terms, acronyms, forms to turn in, laws, procedures and radio protocols.
> 
> But in many cases, servicemen or women have added their own need-to-knows and highly specific security details.
> 
> For example, an individual at one base noted down over a 100 things to know related to their specific function. These included the location of modems that connect vaults to the monitoring facility, the procedures for duress signals for each area on base, the sight pictures of cameras aimed at the vault as well as the components and workings of their console. Details around the composition of passwords, usernames and whether they can include spaces were also detailed in the cards.
> 
> [...]
> 
> Yet perhaps of just as much concern is the open posting of precise information around security and base protocols. 
> 
> Some flashcards detailed the number of security cameras and their positions at various bases, information on sensors and radar systems, the unique identifiers of restricted area badges (RAB) for Incirlik, Volkel, and Aviano as well as secret duress words and the type of equipment carried by response forces protecting bases.
> 
> [...]
> 
> A spokesperson for the US Air Force confirmed that they were aware of service members using flashcard apps to study “a wide variety of subjects”. However, they continued, there was no recommendation for service members to do so and they would not discuss past or current security protocols. They also said they were not aware of any Department of Defense or Department of the Air Force assessment on the use of online study aids but were “investigating the suitability of information shared via study flashcards.”


Oh my.  This is really not good.  There are all kinds of controls around information like the location of cameras, duress words, and sign and countersign that are there to protect the security of such weapons and they really shouldn't be on the open internet.

But here's the quesiton I want to ask.  What drove the soldiers to do this kind of thing?  

What if instead of yelling about "didn't follow process" and "broke security regulations" (which this all did), we instead asked "Were these people given the tools to do their job?".

If users need flashcards to memorise important information like this kind of thing, then maybe find that out and provide them with flashcards that meet your security protocols.

But I expect instead that the follow up to this will be investigation and punishment of people who broke policies while trying to do their job.


## [New sophisticated email-based attack from NOBELIUM - Microsoft Security](https://www.microsoft.com/security/blog/2021/05/27/new-sophisticated-email-based-attack-from-nobelium/)

[https://www.microsoft.com/security/blog/2021/05/27/new-sophisticated-email-based-attack-from-nobelium/](https://www.microsoft.com/security/blog/2021/05/27/new-sophisticated-email-based-attack-from-nobelium/)

> Microsoft Threat Intelligence Center (MSTIC) has uncovered a wide-scale malicious email campaign operated by NOBELIUM, the threat actor behind the attacks against SolarWinds, the SUNBURST backdoor, TEARDROP malware, GoldMax malware, and other related components. The campaign, initially observed and tracked by Microsoft since January 2021, evolved over a series of waves demonstrating significant experimentation. On May 25, 2021, the campaign escalated as NOBELIUM leveraged the legitimate mass-mailing service, Constant Contact, to masquerade as a US-based development organization and distribute malicious URLs to a wide variety of organizations and industry verticals.
> 
> Microsoft is issuing this alert and new security research regarding this sophisticated email-based campaign that NOBELIUM has been operating to help the industry understand and protect from this latest activity. Below, we have outlined attacker motives, malicious behavior, and best practices to protect against this attack.
> 
> [...]
> 
> The phishing message and delivery method was not the only evolving factor in the campaign. In one of the more targeted waves, no ISO payload was delivered, but additional profiling of the target device was performed by an actor-controlled web server after a user clicked the link. If the device targeted was an Apple iOS device, the user was redirected to another server under NOBELIUM control, where the since-patched zero-day exploit for CVE-2021-1879 was served.


This has caused a lot of waves, but is mostly just a spearphishing campaign.  You should check your systems if you think you would be a target.

The most interesting thing in here was the use of an iOS 0-day in the attack. If you were using an iPhone or iPad, then clicking the link, from a legitimate sender, about something you expected to get an email about, then your device was compromised and that was it, game over.

There's no defence that any reasonably individual can have at the user level for that.  Everything about this email would make it one where people would click the link.  

Hopefully, all the targets are of course, using Microsoft Defender or similar products, and the computers will have nullified the link before the user could click on it.


## [Check Your Pulse: Suspected APT Actors Leverage Authentication Bypass Techniques and Pulse Secure Zero-Day | FireEye Inc](https://www.fireeye.com/blog/threat-research/2021/04/suspected-apt-actors-leverage-bypass-techniques-pulse-secure-zero-day.html)

[https://www.fireeye.com/blog/threat-research/2021/04/suspected-apt-actors-leverage-bypass-techniques-pulse-secure-zero-day.html](https://www.fireeye.com/blog/threat-research/2021/04/suspected-apt-actors-leverage-bypass-techniques-pulse-secure-zero-day.html)

> Mandiant is currently tracking 12 malware families associated with the exploitation of Pulse Secure VPN devices. These families are related to the circumvention of authentication and backdoor access to these devices, but they are not necessarily related to each other and have been observed in separate investigations. It is likely that multiple actors are responsible for the creation and deployment of these various code families.
> 
> The focus of this report is on the activities of UNC2630 against U.S. Defense Industrial base (DIB) networks, but detailed malware analysis and detection methods for all samples observed at U.S. and European victim organizations are provided in the technical annex to assist network defenders in identifying a large range of malicious activity on affected appliances. Analysis is ongoing to determine the extent of the activity.
> 
> Mandiant continues to collaborate with the Ivanti and Pulse Secure teams, Microsoft Threat Intelligence Center (MSTIC), and relevant government and law enforcement agencies to investigate the threat, as well as develop recommendations and mitigations for affected Pulse Secure VPN appliance owners.
> 
> As part of their investigation, Ivanti has released mitigations for a vulnerability exploited in relation to this campaign as well as the Pulse Connect Secure Integrity Tool to assist with determining if systems have been impacted.


This is about the exploitation of Pulse Secure appliances using either pre-harvested credentials from another source, or using existing vulnerabilities. 

What's different here is the tools being used after access is given to the VPN appliance to enable further exploitation and to hide the evidence of any further activity.

Patch your devices, and if you think there was any chance that your devices were previously compromised, run the detection tools to validate that they are clean. 


## [(How To) Attribute and think about Cybercrime Activity in 2021](https://www.linkedin.com/pulse/how-attribute-think-cybercrime-activity-2021-cian-lynch/)

[https://www.linkedin.com/pulse/how-attribute-think-cybercrime-activity-2021-cian-lynch/](https://www.linkedin.com/pulse/how-attribute-think-cybercrime-activity-2021-cian-lynch/)

>  To understand how to attribute cybercrime activity properly you MUST understand how the cybercrime ecosystem works. I frequently see posts about some ransomware incident that anthropomorphizes the malware and say things along the lines of "the ransomware targeted this sector or that sector", or "the ransomware uses this or that technique to gain access to the target environment". What needs to be understood is that in major ransomware incidents today you are not typically dealing with an autonomous infection, nor one single actor but an entire cybercrime industry involving at least two or three distinct groups of actors who fulfil different roles in the attack.


This is a good run through of the way that major cybercrime and ransomware organisations work at the moment.  Well worth a read


## [Why You Should Stop Using Other People’s iPhone Cables](https://www.forbes.com/sites/zakdoffman/2021/05/29/apple-iphone-and-ipad-users-warned-not-to-borrow-other-peoples-cables/?sh=240e62a12940)

[https://www.forbes.com/sites/zakdoffman/2021/05/29/apple-iphone-and-ipad-users-warned-not-to-borrow-other-peoples-cables/?sh=240e62a12940](https://www.forbes.com/sites/zakdoffman/2021/05/29/apple-iphone-and-ipad-users-warned-not-to-borrow-other-peoples-cables/?sh=240e62a12940)

> O.MG cables are a very different twist on the theme. It doesn’t matter what you plug the cable into—because the cable itself is the attack device. An independent WiFi access point, payload storage, geofencing capacity, the capacity to log keystrokes or inject its own—it can be instructed on the fly.
> 
> [...]
> 
> In reality, the cables you need to worry about are not the ones sold online. “This isn’t the kind of threat the average person is going to encounter,” Grover says. It won’t end up planted in retail stores, “although it’s totally possible, but it doesn’t make any sense as there are easier pathways to go after somebody.” What this is, though, is tangible evidence as to what can be done and how easily it can be done.
> 
> If you travel for work, if you’re in government service or a high-value industry, if you’re a celebrity or a government targeted lawyer or journalist, this publicity should send a clear message: Don’t use cables if you don’t know where they come from.


I was going to complain about this one, but in fact this is more of a "Title belies the content".

Most people are not going to be the target of BadUSB attacks.  The effort required to get a cable to you, program it to work on your hardware, and then get valuable stuff off of you is really quite high.  As Zak says at the end, if you are a high value target, then you should think about this as a warning.  If you are not, then this is likely out of your threat model, at least for now.


## ['Did weak wi-fi password lead the police to our door?' - BBC News](https://www.bbc.co.uk/news/technology-57156799)

[https://www.bbc.co.uk/news/technology-57156799](https://www.bbc.co.uk/news/technology-57156799)

> After a year of lockdowns, home schooling and a bout of Covid, Kate and Matthew (not their real names) were hoping for better times as 2021 dawned.
> 
> Instead, one January morning, there came a knock on the door from the police who were investigating a very serious crime, involving images of child abuse being posted online.
> 
> The couple insisted they had nothing to do with it.
> 
> But the next few months were "utter hell" as they attempted to clear their names.
> 
> And it was only when the case was dropped in March, with no further action, that they realised the most likely explanation for the false accusation was their wi-fi router - and its factory-set password.


This is a nasty example of the sort of random threat that will affect only a tiny proportion of us, but when it does strike, is very difficult to defend against.

In this case, although as always, not enough details are given to draw out a proper understanding, but it seems that an attacker got access to their Wifi network.  Whether they saw the password on the back of the router somehow, or whether they were able to remotely crack it from a nearby location, they got access.  They then piggybacked off of that wifi to commit crimes in a deniable way, leaving all the evidence pointing back at the poor family.

I note here as well, that there's a requirement to tell various agencies about an investigation into the production of child abuse images, but there doesn't seem to be a mechanism to report that the investigation is closed with the target found innocent.  It feels like this is a gross oversight that should be fixed in the investigatory process.

Not a lot anyone can do about this other than patch their home router, change the default passwords and so on.  Hopefully [stronger regulation](https://www.gov.uk/government/publications/regulating-consumer-smart-product-cyber-security-government-response/government-response-to-the-call-for-views-on-consumer-connected-product-cyber-security-legislation#key-policy-positions---role-of-economic-actors) which [bans default passwords and default insecure configurations for such devices](https://www.gov.uk/government/publications/etsi-industry-standard-based-on-the-code-of-practice) will help ensure that people aren't as easily targeted. 


## [Sharing learnings about our image cropping algorithm](https://blog.twitter.com/engineering/en_us/topics/insights/2021/sharing-learnings-about-our-image-cropping-algorithm.html)

[https://blog.twitter.com/engineering/en_us/topics/insights/2021/sharing-learnings-about-our-image-cropping-algorithm.html](https://blog.twitter.com/engineering/en_us/topics/insights/2021/sharing-learnings-about-our-image-cropping-algorithm.html)

> We considered the tradeoffs between the speed and consistency of automated cropping with the potential risks we saw in this research. One of our conclusions is that not everything on Twitter is a good candidate for an algorithm, and in this case, how to crop an image is a decision best made by people. 
> 
> In March, we began testing a new way to display standard aspect ratio photos in full on iOS and Android — meaning without the saliency algorithm crop. The goal of this was to give people more control over how their images appear while also improving the experience of people seeing the images in their timeline. After getting positive feedback on this experience, we launched this feature to everyone. This update also includes a true preview of the image in the Tweet composer field, so Tweet authors know how their Tweets will look before they publish. This release reduces our dependency on ML for a function that we agree is best performed by people using our products.


Twitter have done some research to discover what feels intuitively true to many people, that not everything is a good candidate for an algorithm.

Snarkiness aside, this is good news.  They've proven that their algorithms have inbuilt bias, or reflect the existing biases of their control sets, and have decided to disable the algorithms in this case.

The question remains, how easy is this to turn into a set of sensible questions you can ask about your product of feature... is this a good place to use an algorithm?

The problem comes because this was and remains a clear and obvious way to see the bias causation, because how images are cropped is visibly noticeable.  But what if the other algorithms that run, whether it be detecting fraudulent tweets, or determining who to follow are also biased, but it's less detectable?  These are not easy questions to answer or grapple with, but as more and more algorithms make decisions and recommendations for us, the more these are going to be important.


## [Exclusive: Meet The Murky Russian Network Behind An Anti-Pfizer Disinformation Drive In Europe](https://www.rferl.org/a/russia-pfizer-covid-disinformation-serebryanskaya-murky-vaccine-influencers/31277170.html)

[https://www.rferl.org/a/russia-pfizer-covid-disinformation-serebryanskaya-murky-vaccine-influencers/31277170.html](https://www.rferl.org/a/russia-pfizer-covid-disinformation-serebryanskaya-murky-vaccine-influencers/31277170.html)

> A French investigative news site called Fact & Furious, along with other outlets including The Wall Street Journal, the Associated Press, and The Guardian, reported that French bloggers had received e-mails from a person claiming to work for a marketing firm called Fazze.
> 
> The e-mails reportedly offered to pay the bloggers to produce videos on YouTube, Instagram, and other platforms criticizing the Pfizer/BioNTech vaccine in particular.
> 
> Leo Grasset, a French science blogger whose YouTube account has 1.2 million subscribers, reported he had been contacted, and [posted screenshots](https://twitter.com/dirtybiology/status/1396719090321010688?s=20) of some of the e-mails to his Twitter account.


This is a fascinating insight into a fully commercialised propaganda or disinformation system. 
When we think of disinformation, we tend to think of shadowy agencies creating false personas and fake journalists to carry their narrative.  But attempting to reach out to influencers and bloggers through the existing marketing channels that they are used to using makes it far harder to spot, and far harder to detect.

Who knows if the next time your favourite blogger or twitch streamer says something about local politics whether that's their real view, or something their being paid to say. 


## [Cisco Talos Intelligence Group - Comprehensive Threat Intelligence: Elizabethan England has nothing on modern-day Russia](https://blog.talosintelligence.com/2021/05/privateer-groups.html)

[https://blog.talosintelligence.com/2021/05/privateer-groups.html](https://blog.talosintelligence.com/2021/05/privateer-groups.html)

> The term "APT" has a broad meaning that's being used in more loose terms nowadays. This term often includes the state-sponsored groups. However, we believe state-sponsored should be referred as state-related and be split into three distinct categories: ones working on behalf of specific state organizations, ones closely related to state actors, but with no clear organization affiliation and with no apparent financial motivation, and, finally, ones that are not directly related to state organizations but benefit from state protection, directly or indirectly.
> 
> The first tier includes actors like the Lazarus Group (aka APT38), a state-sponsored actor carrying out attacks for direct gains for a nation-state. The second tier includes groups like Gamaredon and PROMETHIUM. These groups don't seem to be directly linked to state organizations but are believed to work for states. These don't share the same level of sophistication as prime APTs but are not primarily financially motivated.
> 
> Finally, we have groups like the DarkSide syndicate that we are referring to as "privateers." Privateers benefit from a certain level of state protection or acceptance without any real links to the states. These privateer groups are becoming increasingly prevalent and will likely significantly change the threat landscape in the years to come.
> 


This is a good debate to be having.  I'm not sure I like the privateer term, because it will likely be used to create parallels that don't actually match up with real life, but I do think that splitting up the state based attackers into the directly state funded, the state adjacent and the state-tolerated is a useful way to talk about the intent of groups as much as their capability.


## [GitHub - olafhartong/sysmon-modular: A repository of sysmon configuration modules](https://github.com/olafhartong/sysmon-modular?goal=0_f50a9c9026-6ef5eda5d5-1355048436&mc_cid=6ef5eda5d5&mc_eid=5363907636)

[https://github.com/olafhartong/sysmon-modular?goal=0_f50a9c9026-6ef5eda5d5-1355048436&mc_cid=6ef5eda5d5&mc_eid=5363907636](https://github.com/olafhartong/sysmon-modular?goal=0_f50a9c9026-6ef5eda5d5-1355048436&mc_cid=6ef5eda5d5&mc_eid=5363907636)

> This is a Microsoft Sysinternals Sysmon download here configuration repository, set up modular for easier maintenance and generation of specific configs.
> 
> The sysmonconfig.xml within the repo is automatically generated after a successful merge by the PowerShell script and a successful load by Sysmon in an Azure Pipeline run.
> 
> […]
> 
> I strive to map all configurations to the ATT&CK framework whenever Sysmon is able to detect it. A current ATT&CK navigator export of all linked configurations is found [here](https://github.com/olafhartong/sysmon-modular/blob/master/attack_matrix/Sysmon-modular.json)


This is a cute tool, and should make a great base for setting up and using your own sysmon configuration.

You should do that incidentally, you may not want all the modules here, and you can add the modules that are specific for your estate.  You could even use this to pull together different configurations for different classes of device.


