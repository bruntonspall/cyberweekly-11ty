---
title: "103 - The steady growth of AI"
date: 2020-05-24
description: "Will AI prove to be the downfall of humanity?  Probably not.  But it's clear that proponents of AI and it's use in multiple systems are firm believers that AI is providing a generational jump similar to the dawn of computing and the information age."
permalink: /the-steady-growth-of-ai/
---

Will AI prove to be the downfall of humanity?  Probably not.  But it's clear that proponents of AI and it's use in multiple systems are firm believers that AI is providing a generational jump similar to the dawn of computing and the information age.

Of course, the information age is more than just the growth of silicon valley, microchips and games consoles.  It's about the growth of access to information.  Not that long ago, even the worlds best governments didn't have access to sources as reliable and effective as wikipedia, let alone the steady speed of updating that happened.  It's within a generational gap that we've gone from communications taking weeks to cross oceans, to taking milliseconds to cross the planet.  The change that the information revolution bought to us was access to vast amounts of information at lightning speed.

But the disinformation and misinformation is a festering boil on the side of that.  While everyone now has access to the [CIA World Factbook](https://www.cia.gov/library/publications/the-world-factbook/), [lies can now spread round the world before the truth has got its boots on](https://freakonomics.com/2011/04/07/quotes-uncovered-how-lies-travel/).  AI is not a revolution in information distribution, it is a now much needed revolution in our ability to discern and sift through that information to find the things we are looking for.

AI helps us make decisions, or in some cases takes the decisions away from us, allowing the computer to make thousands of decisions a second, all while more and more information is flowing into the system.

Like all revolutions, there are those who don't believe, there are those who believe fervently without regard for the dangers, and there are those who are simply skeptical.  

It doesn't help that technologists tend to fall into two camps, the "AI is simply advanced statistics" (a quote I find about as useful as "the cloud is other peoples computers", both technically correct and utterly useless), or "If we say it does AI, we'll sell 10x as many".  We can barely even agree a definition of AI, it's such a broad school, that people arguing at one another about the proper use of it, or the ethical ramifications don't have a common agreed upon vocabulary with which to define their arguments, let alone review and understand each others perspectives.

Automated decision making is not only coming, but is already here, and is spreading into wider and wider sections of our lives.  We need a better discourse amongst ourselves to decide what the make of it, what ethical frameworks could and should exist and how to effectively use these tools and techniques for good.

## [Amazon Brushes Off European Challenge to Its Cloud Business - Bloomberg](https://www.bloomberg.com/news/articles/2019-10-29/france-joins-german-cloud-effort-to-challenge-amazon-and-alibaba)

[https://www.bloomberg.com/news/articles/2019-10-29/france-joins-german-cloud-effort-to-challenge-amazon-and-alibaba](https://www.bloomberg.com/news/articles/2019-10-29/france-joins-german-cloud-effort-to-challenge-amazon-and-alibaba)

> Franco-German plan for a European cloud that would allow the continent's businesses to keep their data from being stored in the U.S. or China.
> 
> After the European Union's two leading nations unveiled plans for an EU-focused cloud, a spokesperson for Amazon's AWS cloud business said such a project will lack the scale to compete with the industry's dominant players.


(Joel) There are situations where it is entirely reasonable to require complete control or influence over data sovereignty and that technically storing data in an European data-centre belonging to a US company (putting that data in theory within scope of the US CLOUD Act and so on) does not provide enough assurance - just these situations are relatively rare.

AWS is right in this instance in terms of comparability of scale: this European project will not have the R&D investment to develop (at any similar pace) the plethora of XaaS products that AWS, Alibaba, Azure and Google Cloud have managed to generate. This isn't to say that those functions will be needed but where they do not exist (or intend to exist, because a modern pipeline of products/features is important) they cannot be leveraged.

It will be interesting to see how this actually plays out. I've developed platforms like this before (I did data-centres and hosting back in the day so VMWare will always have a place in my heart) this venture _could_ work out pretty well.

My prediction is that the project will look a lot like VMWare IaaS with potentially CloudFoundry PaaS and a whole bunch of tin (because under every cloud is tin) that should be manageable through modern means such as Terraform. It will lack a certain 2019 public cloud polish but assuming the inter-charging price point is reasonable and it is run as a good managed service, it could do quite well within the bounds of what it is (a private cloud).

I would hope that not all workloads default here and that the European Union countries weigh up AWS, GCP, Azure (etc) just like they have always done but there is a hybrid or private service available when reasonably required.


## [An IRS employee stole identities and went on a 2-year spending spree](https://qz.com/1723855/an-irs-employee-stole-identities-went-on-spending-spree/)

[https://qz.com/1723855/an-irs-employee-stole-identities-went-on-spending-spree/](https://qz.com/1723855/an-irs-employee-stole-identities-went-on-spending-spree/)

> The complaint accuses the 35-year-old federal worker of racking up almost $70,000 in charges over the course of two years, illegally using “the true names, addresses, dates of birth, and Social Security numbers” of at least three people.
> [...]
> “It’s pretty easy to do something like this if you have such unfettered access to other people’s [personal data],” Cedric Leighton, a 26-year US Air Force intelligence officer and an expert on insider threats, told Quartz. “But it’s also easy for [the inspector general] and other law enforcement agencies to catch a rogue insider like this.”


(Joel) Inside actors (malicious or otherwise cajoled) can be a very real set of risks that needs managing... however... basic information security hygiene underpins 'all of the above' and while 'basic' can be often harder to tackle but remains infinitely more important to get right.

Would the Inspector General's Office have caught this insider sooner had role-based access been a little tighter? Audit information been readily captured and analysed? If viewing unrelated citizen case/profile data had been impossible or flagged? You could say we should wait for more analysis to determine whether these factors had any role to play... my challenge to your organisation is does it have these 'always true' controls in place?


## [Europe publishes 5G risk assessment; America scrawls ‘Huawei’ on the side of a nuke and goes for a ride • The Register](https://www.theregister.co.uk/2019/10/10/europe_5g_risk_assessmen/)

[https://www.theregister.co.uk/2019/10/10/europe_5g_risk_assessmen/](https://www.theregister.co.uk/2019/10/10/europe_5g_risk_assessmen/)

> These are the changes that make people so excited about the possibilities of 5G but at the same time, the report notes, “these new features will bring numerous new security challenges. In particular, they will give additional prominence to the complexity of the telecoms supply chain in the security analysis, with various existing or new players, such as integrators, service providers or software vendors, becoming even more involved in the configuration and management of key parts of the network.”
> 
> The report notes: “Some sensitive functions currently performed in the physically and logically separated core are likely to be moved closer to the edge of the network, requiring relevant security controls to be moved too, in order to encompass critical parts of the whole network, including the radio access part.
> 
> If not managed properly, these new features are expected to increase the overall attack surface and the number of potential entry points for attackers, as well as increase chances of malicious impersonation of network parts and functions.”


(Joel) 5G is apparently poised to change our lives... and the technology combined with such intricate assimilation allegedly presents national security risks.

Whether we're talking telecom structures and foreign technology vendors or developing a digital service to overhaul how money is sent to prisoner's it all boils down to risk management and choosing between price, security and functionality.

While I have no doubt the security debate around 5G is important to many people... I am simply waiting for the day my fridge can autonomously send milk to my Nespresso machine and then [Spot](https://edition.cnn.com/2019/09/25/app-tech-section/robot-dog-sale-intl-hnk-scli/index.html) can bring it to me (the finished coffee, not the Nespresso machine or fridge).


## [2020 Global Threat Report | CrowdStrike](https://www.crowdstrike.com/resources/reports/2020-crowdstrike-global-threat-report/)

[https://www.crowdstrike.com/resources/reports/2020-crowdstrike-global-threat-report/](https://www.crowdstrike.com/resources/reports/2020-crowdstrike-global-threat-report/)

> * Big game hunting (BGH) escalated, and ransom demands soared into the millions, causing unparalleled disruption.
> * Cybercriminals are weaponizing sensitive data to increase pressure on ransomware victims.
> * The eCrime ecosystem continues to evolve, mature and develop increasing specialization.
> * Outside of BGH, an increase was observed in eCrime campaigns targeting financial institutions around the world.
> * The trend toward malware-free tactics accelerated, with malware-free attacks surpassing the volume of malware attacks.
> * State-sponsored targeted intrusions continued to gather intelligence and promote division within communities, and possible collaboration with sophisticated eCrime adversaries was observed.
> 
> [...]
> 
> Still, MaaS developers may prefer to stay out of the limelight, as suggested by VENOM SPIDER’s judicious cherry-picking of customers. Pleasing a few selected operators carries less risk than hands-on-keyboard activity within a victim’s network, as well as arguably aiding in protecting the developer’s operational security. 


This is an interesting report covering, primarily the rise in  cybercrime rather than espionage and nation state attackers.  When you read about ransomware and other compromises, there's a good possibility that what you are looking at is the end effects of the cybercrime groups rather than nation states.

The term big game hunting to define ransomware and the increasing amounts of ransoms being asked for and paid shows a clear trend around increasing over the next few years.  Ryuk took around $12.5m as a single large demand in 2019, with demands in the 5-9m making some of the top 10, all by the same few strains of ransomware.

There's a great chart on [page 30](https://go.crowdstrike.com/rs/281-OBQ-266/images/Report2020CrowdStrikeGlobalThreatReport.pdf#page=30) that shows how interconnected many of the cybercrime groups are.  They trade features and more importantly, tend to use the same couple of pieces of malware family to manage the infection and load their desired ransomware strains.

But while this is an efficient income stream for some malware as a service operators, there's definitely evidence that their are tiers of malware developers and operators, and that the higher tiers are going out of their way to pick their operators carefully.


## [Nintendo Switch Issue Shows Quirk in Password UI [Updated] - VICE](https://www.vice.com/en_us/article/889a33/nintendo-switch-eshop-guess-password)

[https://www.vice.com/en_us/article/889a33/nintendo-switch-eshop-guess-password](https://www.vice.com/en_us/article/889a33/nintendo-switch-eshop-guess-password)

> Correction: Researcher Runa Sandvik said they found that an 'OK' dialogue box in a login user interface on the Nintendo Switch lit up when a user entered only part of their password, and that this is unusual behaviour. However, the dialogue box actually changes when a user enters a series of characters that meet Nintendo's minimum requirements for a password. Those are the password being 8 characters in length, and containing at least two of the following: lowercase or uppercase letters, numbers, and punctuation. The password also cannot have the same character more than twice in a row. Motherboard verified Sandvik's interpretation is not correct by typing in a random series of digits that aren't a real password but which do meet those requirements; the 'OK' box lit up. This points to a quirk in the Switch's UI, but not necessarily a security vulnerability. The original article follows below. Motherboard regrets the error.
> 
> [...]
> 
> Typically, websites and services will 'hash' a user's password, and store that rather than the plaintext password itself. A hash is essentially a one-way, cryptographic fingerprint of a piece of data. A user will type their password into the login box, the system will hash that input, and then compare it to the hash the website has on file to see if they match. If they do, the system logs the user in.
> 
> But, that would not necessarily work if Nintendo is able to tell a user that they've successfully entered the first eight characters of their password. Is Nintendo creating a hash of the first eight characters as well as another hash of the full password? Is Nintendo storing the first eight characters in plaintext?


This was a fun one.  We like to laugh at security failures, and a system that gives away the password would have been something to laugh at.  But I wasn't convinced that this was real.  The Switch Online Login has you enter the password, the idea that it would send the first 8 characters to the server for validation, and that the server would say yes if only the first 8 characters matched seemed odd to me.  
I thought about how I could implement this, hashes of the 8 character prefix being the most sensible, but the more I thought about it, the more I couldn't reason out a why.

So I got out my switch and tested it.  And sure enough, if I tried 'aaaaaaaa' nothing lit up, but if I tried the first 8 characters of my password, the ok button lit up. This seemed valid, but still made no sense. so I tried various other things and discovered that it lit up providing it was a valid password according to the rules.  Sent a tweet to Motherboard, along with some other people and they issued the correction.

If it sounds too weird to be true, maybe it actually is too weird to be true


## [Nation State Actors on the Darknet — DarkOwl | Dark Web Search Engine](https://www.darkowl.com/blog-content/nation-state-actors-on-the-darknet)

[https://www.darkowl.com/blog-content/nation-state-actors-on-the-darknet](https://www.darkowl.com/blog-content/nation-state-actors-on-the-darknet)

> The leaked source code for these NSA and CIA cyber tools are readily available and discussed in dark web communities. Dark Web enthusiasts on YouTube have posted downloadable videos walking their viewers through the specifics of these advanced exploits. While the US, China, and Russia continue to develop new even more sophisticated cyber weapons, other Nation-States with an emerging cyber capability can now - as a result of these leaks - have the resources and the knowledge to attack other nation’s network infrastructure and conceal the origin of the attack, further complicating the global nation station cyber environment. 
> 
> The availability of such tools brings into question much of the cybersecurity’s reporting around Nation-State attack attribution. For example, in early October of this year, Microsoft reported that they had witnessed ‘significant’ activity throughout the summer against current and former US government officials, journalists covering global politics and prominent Iranians living outside of Iran. The group Microsoft is calling “Phosophorous” made more than 2700 attempts to identify consumer accounts that could prove potential entry attack vectors. The group, believed to be from Iran, indiscriminately attacked both personal and work email addresses and attacks also included attempts at infiltrating President Trump’s reelection campaign. 
> 
> Recently, NSA revealed that Russian hackers from the infamous “Turla group” co-opted Iranian tools and conducted numerous attacks across industries in dozens of countries in recent months. Leveraging Iranian developed malware, Nautilus and Neuron, in combination with one of its own toolkits, called Snake, Turla obtained access to targets by scouring their networks for backdoors that had been inserted by Iranian hackers. Again, further confusion to attack attribution.  


One of the murkiest parts of attribution, especially when dealing with nation states, is that their level of capability isn't just limited to advances in technical research to discover otherwise unknown exploits.  It's that their strength is in the supporting structures around carrying out operations, from deniable infrastructure purchased through cutout organisations, research and target evaluation in advance of the operation, and "digital camouflage", the ability to operate as if they are in fact another group.

We saw this in the reported behaviour around Turla, but also in certain ransomware attacks such the NotPetya ransomware which it turned out [never generated a key to decrypt your files](https://securelist.com/expetrpetyanotpetya-is-a-wiper-not-ransomware/78902/).  While it looked like eCrime conducting ransomware, it was in fact nothing but a destructive cyberattack.

We'll see a lot more of this over the next few years, but, if the camouflage is any good, naturally we won't know that we've seen it.


## [Where AI and ethics meet | Cosmos](https://cosmosmagazine.com/society/where-ai-and-ethics-meet)

[https://cosmosmagazine.com/society/where-ai-and-ethics-meet](https://cosmosmagazine.com/society/where-ai-and-ethics-meet)

> Finally, the author points to “the relative lack of legal and professional accountability mechanisms” within AI research. Where medicine has numerous layers of legal and professional protections to uphold professional standards, such things are largely absent in AI development. Mittelstadt draws on research showing that codes of ethics do not themselves result in ethical behaviour, without those codes being “embedded in organisational culture and actively enforced”.
> 
> “This is a problem,” he writes. “Serious, long-term commitment to self-regulatory frameworks cannot be taken for granted.”
> 
> All of this together leads Mittelstadt to conclude: “We must therefore hesitate to celebrate consensus around high-level principles that hide deep political and normative disagreement.”
> 
> Instead he argues that AI research needs to develop “binding and highly visible accountability structures” at the organisational level, as well as encouraging actual ethical practice in the field to inform higher level principles, rather than relying solely on top-down principlism. Similarly, he advocates a focus on organisational ethics rather than professional ethics, while simultaneously calling for the professionalisation of AI development, partly through the licensing of developers of high-risk AI.


There have been calls within software engineering for a code of ethics for a long time, but they are getting stronger and more convincing as time goes on.  From [Uber's God Mode](https://bgr.com/2016/12/13/uber-privacy-and-security/) to [Volkswagon's "defeat device"](https://www.bbc.co.uk/news/business-34324772), software developers can deliberately write software that doesn't meet the ethical standards of society around us.

But this conversation is hard enough in plain software engineering.  Whose ethics should we consider?  Is it acceptable to bypass regulations applied by dictatorships such as internet boundary controls, but not those applied by environmental protection agencies?  Which civilisations view of ethical behaviour is the right one, and given that software engineering is probably the best example of a global job, where it's possible to write the code anywhere in the world, how much does the national identity of the developers matter?

This gets even harder when we talk, as we always do, loosely about AI.  What meets the bounds for AI?  Does it have to have a feedback mechanism that learns, or is sufficiently advanced statistics good enough to be called AI?  Does the creation get ethically judged differently from the training of the AI?

These are questions that we have to wrestle with, while an industry both advances in AI development, but also while silicon valley marketing continues to confuse the situation by telling you that everything comes with an AI these days.


## [Password Hunting with Machine Learning in Active Directory - Hunnic Cyber - Blog, Press & Careers](https://blog.hunniccyber.com/password-hunting-with-ml-in-active-directory/)

[https://blog.hunniccyber.com/password-hunting-with-ml-in-active-directory/](https://blog.hunniccyber.com/password-hunting-with-ml-in-active-directory/)

> In Adversary Simulation engagements, or indeed any form of internal penetration test, file shares can be a vast resource of information.
> 
> Often developers and system administrators leave passwords unattended and finding these can be a key to the success of the engagement.
> 
> As far as the tools we have used, most have been centered around "grepping" lines below and above the word password, looking through files with select file extensions and then relying on the human operator for validation.
> 
> We decided to experiement with Machine Learning, in particular Clustering and Classification, to see if we could use these methods to find passwords (and validate them against Active Directory) in accessible file shares.


This is a cute application of simple AI in the form of pattern recognition.  There are thousands of files and documents on shared file drives.  Can you look through them all looking for things that look like passwords without having to use grep or manually look through them?

While, for a simple attacker, this is probably not worth the effort, for an organisation that consistently and constantly attacks a variety of targets, such as a pen test company, there are returns on the speed and efficiency of finding passwords that might make this useful.  As it is only a proof of concept, I doubt this will take off, but it's good to know how red teams are using new technologies.


## [Allies and Artificial Intelligence: Obstacles to Operations and Decision-Making - Texas National Security Review](https://tnsr.org/2020/03/allies-and-artificial-intelligence-obstacles-to-operations-and-decision-making/)

[https://tnsr.org/2020/03/allies-and-artificial-intelligence-obstacles-to-operations-and-decision-making/](https://tnsr.org/2020/03/allies-and-artificial-intelligence-obstacles-to-operations-and-decision-making/)

> Allied decision-makers will also face uncertainty when confronting a rival’s use of AI-enabled technologies. Leaders will be forced to wrestle with whether to respond to actions carried out by AI-enabled systems — like autonomous aircraft or ships — in the same way as actions carried out by traditionally manned assets. Existing doctrine and law are generally silent on these issues, providing no guidance on the appropriate response. States have drafted domestic policies to govern their own use of autonomous weapon systems, but these regulations and international law make no distinction between how states should react to a rival’s AI-enabled military actions versus “traditional” military actions.103 Yet, decision-makers may believe that a rival’s use of AI technologies demands different responses than those involving manned platforms.104 What happens if a rival claims that an attack carried out by an AI-enabled system was the result of a flawed algorithm? Should air defense forces respond differently to an adversary’s autonomous drones that penetrate friendly airspace than to a manned aircraft that does the same? Decision-makers may find themselves with little time to consider these complicated issues, particularly as AI technology accelerates the speed of a rival’s military operations.


While RAND has a paper talking about how AI is most likely to provide benefit to decision making, logistics and manpower, the University of Texas looks at how that can cause problems, either directly or through knock on effects.  The issue this raises is about the acceleration of the OODA loop, the ability to Observe, Orient, Decide and then Act.

AI can help our systems analyse incoming information far more quickly, ensuring that we can observe and orient faster than the enemy, but that means that the pressure to make rapid decisions is ever more present in the minds of military, strategic and diplomatic circles.  

Additionally, if both sides in a conflict have AI systems that speed up the process, we can see escalation scenarios in which it is far more difficult for human diplomacy to provide the time needed for de-escalation.


## [Military Applications of Artificial Intelligence: Ethical Concerns in an Uncertain World | RAND](https://www.rand.org/pubs/research_reports/RR3139-1.html)

[https://www.rand.org/pubs/research_reports/RR3139-1.html](https://www.rand.org/pubs/research_reports/RR3139-1.html)

> But thoughtful people have expressed serious reservations about the legal and ethical implications of using AI in war or even to enhance security in peacetime. Anxieties about the prospects of “killer robots” run amok and facial recognition systems mistakenly labeling innocent citizens as criminals or terrorists are but a few of the concerns that are fueling national and international debate about these systems.
> 
> These issues raise serious questions about the ethical implications of military applications of AI and the extent to which U.S. leaders should regulate their development or restrain their employment. But equally serious questions revolve around whether potential adversaries would be willing to impose comparable guidelines and restraints and, if not, whether the United States’ self-restraint might put it at a disadvantage in future conflicts.
> 
> [...]
> 
> After comparing military AI development efforts in the United States, China, and Russia, the authors examine those states' policy positions regarding proposals to ban or regulate the development and employment of autonomous weapons, a military application of AI that arms control advocates find particularly troubling. 
> 
> Finding that potential adversaries are increasingly integrating AI into a range of military applications in pursuit of warfighting advantages, they recommend that the U.S. Air Force organize, train, and equip to prevail in a world in which military systems empowered by AI are prominent in all domains. Although efforts to ban autonomous weapons are unlikely to succeed, there is growing recognition among states that risks associated with military AI will require human operators to maintain positive control in its employment. 


This paper, which is very long, makes a good argument that the development and application of AI techniques with military uses is essentially inevitable.  World politics mean that perceptions of "winner takes all", and the fact that different ethical frameworks have different areas of concern mean that even if the west were to support the ban of the most controversial of AI applications, namely that of Lethal Autonomous Vehicles, other states would continue to research in the area, and build all of the supporting knowledge needed.

There's good news as well though.  The effective application of AI technology to the pointy end of military applications is probably decades away.  Nightmares of [ED-209](https://www.youtube.com/watch?v=ZFvqDaFpXeM) are far less likely than the use of AI in improving decision making, speeding up military analysis, and enhancing logistical capabilities of military forces deploying around the world.


