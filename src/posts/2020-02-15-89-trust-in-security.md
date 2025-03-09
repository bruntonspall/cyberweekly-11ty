---
title: "89 - Trust in security"
date: 2020-02-15
description: "A short one this week I’m afraid. Prepping for half term and a heavy workload this week have conspired against me. So most of the stories are from the backlog from before Christmas. "
permalink: /trust-in-security/
---

A short one this week I’m afraid. Prepping for half term and a heavy workload this week have conspired against me. So most of the stories are from the backlog from before Christmas. 

The Crypto AG story however is a fascinating insight into the behaviours of the US intelligence apparatus and the goals of the US abroad and in its intelligence operations. 

The problem of such stories is that while some of us are working really hard to create good cyber security standards, to giving advice that protects the majority of people, as long as this sort of story comes out, people often won’t trust government backed security advice. 

If you believe that the CIA is willing to backdoor cryptographic machinery, then why would you believe the US government CISA team who are telling you how to configure VPN’s effectively are giving the right advice?

This sort of activity unfortunately is viewed as necessary by government officials, and I half agree, intelligence intercept material helps the western governments to make decisions about international crises on a regular basis. The cost of that however is the lack of trust in security people to actually give good coherent advice. 

Personally, I know that the advice around securing your endpoints, configuring VPNs and managing your networks from the UK’s NCSC is good advice and driven by a desire to make the UK economy and organisations stronger and more resistant to attacks from our adversaries, both state backed and independent. But it’s hard when stories like this get out because nobody can ever say with seriousness that there is no possibility that some small subset of an intelligence agency doesn’t have some special backdoor somewhere.

## [Top Secret documents show Cyber Command's growing pains in its mission against ISIS](https://www.cyberscoop.com/cyber-command-pentagon-counter-isis-glowing-symphony-foia/)

[https://www.cyberscoop.com/cyber-command-pentagon-counter-isis-glowing-symphony-foia/](https://www.cyberscoop.com/cyber-command-pentagon-counter-isis-glowing-symphony-foia/)

> The documents reveal broader issues Cyber Command has had with other portions of the U.S. government, slowing down the processes by which the command could carry out its orders.
> 
> “Interagency policies and processes are not established to meet the demand for speed, scale, and scope required for effective cyberspace operations,” the documents say.
> 
> Beyond working with coalition partners, the Department of Justice, FBI, CIA, NSA, and other members of the U.S. government were involved in coordinating Glowing Symphony, according to the documents.
> 
> One briefing said the process for vetting the operation’s targets was too “lengthy and difficult.” One briefer bluntly noted that the deconfliction processes — which allows other government agencies or councils check to make sure Cyber Command’s campaigns didn’t negate other government operations — “were too immature to execute.”


This is an interesting point when it comes to offensive cyber operations.  If these operations are highly classified and compartmentalised, then it's really hard to organise any level of coordination between them.

If you have a sensitive intelligence operation, collecting data from a router in a target location, and a totally different team in offensive cyber looking to target the same server, then you need to have a clearance process that goes in and out of all those compartments.

That gets even harder when you have multinational cooperation, because your goals of gathering intelligence without detection are going to be at odds with others goals in shutting down your target groups.


## [OHCHR | The Special Rapporteur’s 2019 report to the United Nations Human Rights Council](https://www.ohchr.org/EN/Issues/FreedomOpinion/Pages/SR2019ReporttoHRC.aspx)

[https://www.ohchr.org/EN/Issues/FreedomOpinion/Pages/SR2019ReporttoHRC.aspx](https://www.ohchr.org/EN/Issues/FreedomOpinion/Pages/SR2019ReporttoHRC.aspx)

> The private surveillance industry has thrived with low levels of transparency and public scrutiny and weak controls on transfers of technology. More often than not, governments offer limited information on the use of surveillance products and regulations of private surveillance companies. These challenges contribute to the lack of accountability for the human rights interferences suffered by direct targets of surveillance, as well as for victims of human rights violations facilitated by the use of surveillance technologies. In the face of these challenges, the Special Rapporteur proposes a human rights based legal and policy framework for the regulation and accountability of, as well as transparency within, the private surveillance industry.
> 
> The report’s key recommendations are:
> 
> To establish an immediate moratorium on the global sale and transfer of private surveillance technology until rigorous human rights safeguards are put in place to regulate such practices and guarantee that governments and non-State actors use the tools in legitimate ways.
> States purchasing surveillance technologies should take measures to ensure that their use is in compliance with international human rights law. This includes reinforcing national laws limiting surveillance, creating public mechanisms for approval and oversight of surveillance technologies, and ensuring that victims of abuse have domestic legal tools of redress. 


The UN’s Special Rapporteur has recommended that firms selling “private surveillance technology” be stopped from doing so until such time as the UN has established laws and measures that ensure that states are transparent about their use. 

It’s a lovely idea in theory, but the lack of definition of a private surveillance technology makes it incredibly hard for this to be adopted. 
Additionally, getting UN wide agreement from all countries about what is a transparent oversight would be tricky. Would the UK’s secret warrants signed by the Home Secretary or the US’s FISA courts meet the standards?  Would states that have more corrupt internal bureaucracies insist on transparency that they’d never implement but they know their adversaries would implement?


## [Stopping the Press: New York Times Journalist Targeted by Saudi-linked Pegasus Spyware Operator - The Citizen Lab](https://citizenlab.ca/2020/01/stopping-the-press-new-york-times-journalist-targeted-by-saudi-linked-pegasus-spyware-operator/)

[https://citizenlab.ca/2020/01/stopping-the-press-new-york-times-journalist-targeted-by-saudi-linked-pegasus-spyware-operator/](https://citizenlab.ca/2020/01/stopping-the-press-new-york-times-journalist-targeted-by-saudi-linked-pegasus-spyware-operator/)

> Our investigation included scanning the Internet to find Command & Control (C&C) servers that behaved similarly to the ones communicating with the spyware sent to Mansoor. While the Pegasus servers we found were pulled offline even before we published Million Dollar Dissident, we continued to monitor them in case some of them might come back online. In the weeks after our report, we noticed a small number of Pegasus servers that came back online, but the servers no longer matched our fingerprint. We built a new fingerprint based on this behaviour, and began conducting regular Internet scans to find servers matching this new fingerprint.
> 
> In September 2018, Citizen Lab published Hide and Seek: Tracking NSO Group’s Pegasus Spyware to Operations in 45 Countries, which described the results of this follow-up scanning, conducted between August 2016 and August 2018. In these scans, we detected 1,091 IP addresses and 1,041 domain names matching our new fingerprint. We further grouped these IPs and domains into 36 distinct Pegasus operators using a technique we developed and named Athena. We also devised a new way to conduct DNS Cache Probing, and used this method to find likely infections, by identifying Internet Service Providers (ISPs) where one or more user was repeatedly looking up domain names associated with Pegasus C&C servers.


This is a neat detection method.  Users who have been infected with malware (as Pegasus should be defined), will need to talk to command and control servers (C2).  This communication means that it will look up the domain name of the C2 server, and that lookup, despite internet standards saying to obey certain TTL's, will likely be cached on their ISP's DNS server, to return faster results for other people looking up the domain.  By timing the lookup, they can determine if any given ISP's DNS server has been asked recently about a control domain, and therefore has an infected user.


## [Evernote Gave Dark Web Dealer’s Notes to the DEA - VICE](https://www.vice.com/en_us/article/j5yyxp/evernote-search-warrant-gave-data-to-us-government)

[https://www.vice.com/en_us/article/j5yyxp/evernote-search-warrant-gave-data-to-us-government](https://www.vice.com/en_us/article/j5yyxp/evernote-search-warrant-gave-data-to-us-government)

> The warrant highlights how as users increasingly move aspects of their lives to various pieces of software, from ridesharing to note taking apps, that information is often stored remotely on a company's servers and is available to third parties.
> 
> "One flashdrive provided by Evernote consisting of 18 data folders in Evernote proprietary software," the executed search warrant from July 2018, listing what data Evernote provided, reads.
> 
> Evernote is a note taking app, which allows users to sync images, videos, and texts between their computers and phones via Evernote's servers.


I saw a lot of discussion online about how terrible this makes evernote, but having read the warrant, I'm not convinced that this isn't a perfect example of a warrant being properly and correctly processed.

In this case, the federal investigators had considerable evidence that the suspect was engaged in producing and distributing illegal drugs.  The (application for the warrant)[https://www.documentcloud.org/documents/6567400-Evernote-Search-Warrant-Application.html] to the judge including the details of enough suspicion to conduct surveillance, to correlate envelopes he was posting with others that had been intercepted containing drugs.  They had arrested the subject and discovered that he had accounts on the phone with evernote and therefore wanted the contents of those accounts.

If the police had that evidence and wanted to access a diary held by a third party, that's the sort of warrant that I think most people would like to see raised.  The evidence required to grant this search warrant and the resultant search seems reasonable to me.


## [The False Choice of Penetration Testing Tools – Stranded on Pylos](https://pylos.co/2019/12/24/the-false-choice-of-penetration-testing-tools/)

[https://pylos.co/2019/12/24/the-false-choice-of-penetration-testing-tools/](https://pylos.co/2019/12/24/the-false-choice-of-penetration-testing-tools/)

> Essentially, defenders should look at the public release of offensive capabilities as an opportunity and not a burden, so long as such release is made with defender needs and lifecycles in mind. Instead of only learning of a new attack technique or methodology once it hits the defended network, public release (and in-network testing through red teaming) allows defenders to grasp such methodologies in advance of hostile actor use. In this fashion, networks can evolve to incorporate needed visibility, implement required controls, or close off potential attack vectors before other parties take advantage of them.


I think I said much the same back when I first saw this, but this is a far better written and comprehensive view than my quick analysis. 


## [Opinion | How to Track President Trump - The New York Times](https://www.nytimes.com/interactive/2019/12/20/opinion/location-data-national-security.html)

[https://www.nytimes.com/interactive/2019/12/20/opinion/location-data-national-security.html](https://www.nytimes.com/interactive/2019/12/20/opinion/location-data-national-security.html)

> The threats will only grow as more data is collected and shared. More apps will enter the marketplace using tracking technology. And companies are becoming more sophisticated at collecting location data, adding signals from Wi-Fi networks and Bluetooth beacons. They also often rely on one-time consent or disclosures that don’t explicitly state what’s collected or shared.
> 
> Experts emphasized how location data has joined many other kinds of sensitive information in the espionage toolkit, showing how intelligence agencies must continually adapt to the digital age.
> 
> “We need to learn to operate with fewer secrets,” Ms. Spaulding said.
> 
> Even areas once thought to be secure showed up in the data. Personal phones aren’t generally allowed inside the C.I.A. or the National Security Agency. But while no pings registered inside the C.I.A. headquarters, we found thousands of pings in the parking lots outside, with trails that led to the homes of likely employees.


This New York Times article shows the power of location data held by mobile phone operators.  This is likely just as true around the world as it is in the US, and forms a key part of intelligence strategies in almost every country I imagine.  We know from many accounts that within occupied territories, tracking mobile phones is exactly how the US and NATO tries to keep tabs on terror suspects operating in the middle east, and most Americans would have no problem with this.
 
However, they tend to assume that this technology and data is not available or used within the US or on US citizens. And by inteligence agencies and police agencies, it generally isn't.  The access to this data requires warrants, and those tend to need very specific attributes.  Nobody in law enforcement is likely able to perform the sort of convoy analysis that the NYTimes did here.

It again points at the hypocrisy of western nations, in particular the US, of objecting to state surveillance by other states, objecting to national powers to demand lawful intercept, while gladly using such powers within their own opaque processes. 



## [How the CIA used Crypto AG encryption devices to spy on countries for decades - Washington Post](https://www.washingtonpost.com/graphics/2020/world/national-security/cia-crypto-encryption-machines-espionage/)

[https://www.washingtonpost.com/graphics/2020/world/national-security/cia-crypto-encryption-machines-espionage/](https://www.washingtonpost.com/graphics/2020/world/national-security/cia-crypto-encryption-machines-espionage/)

> But what none of its customers ever knew was that Crypto AG was secretly owned by the CIA in a highly classified partnership with West German intelligence. These spy agencies rigged the company’s devices so they could easily break the codes that countries used to send encrypted messages.
> 
> 
> The decades-long arrangement, among the most closely guarded secrets of the Cold War, is laid bare in a classified, comprehensive CIA history of the operation obtained by The Washington Post and ZDF, a German public broadcaster, in a joint reporting project.
> 
> The account identifies the CIA officers who ran the program and the company executives entrusted to execute it. It traces the origin of the venture as well as the internal conflicts that nearly derailed it. It describes how the United States and its allies exploited other nations’ gullibility for years, taking their money and stealing their secrets.


This is a fascinating read for several reasons. 

Firstly it’s a look into how the CIA actually operates. Secondly it’s a look at how the US views both it’s adversaries and it’s erstwhile international allies. Finally it’s interesting in its timing and provenance. 

Looking at the first two, this is a great story of an intelligence coup. This enabled the US to decrypt supposedly “military grade security” used by nations and military juntas around the world for decades. 

If you read between the lines, it looks like the CIA didn’t actually interfere with the machines too much. There was too much chance of that being discovered. Instead it really had an impact on the training manuals. Telling people to use the devices improperly would ensure that the security was much reduced. 

This also means that the big targets, Russia, China for example, were probably not targets of this. It was aimed at much smaller actors who didn’t build and manage their own equipment and training. 

What’s more interesting to me is that the Washington Post and ZDF have been clearly given unredacted access to the source documents. There must be a reason that they want this to be in the news. While Crypto AG shut down a few years ago, this indicates a trend. The US believes that it is acceptable to interfere with such equipment and sell it oversees, and that it won’t mind if that equipment is used by UN members, European countries or other western allies. Are they sending a signal to China about Huawei or is there some other reason this was briefed?


