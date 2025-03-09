---
title: "159 - The rise of commercial spyware"
date: 2021-07-25
description: "(Joel) Hi folks, [Joel](https://twitter.com/joelgsamuel) here."
permalink: /the-rise-of-commercial-spyware/
---

(Joel) Hi folks, [Joel](https://twitter.com/joelgsamuel) here.

If like Michael and I you spend the vast majority of your working time in central government, you will be aware that the Spending Review 2021 (the UK civil service's next 3-year financial settlement) has started to warm up. I thought I would take over this week's CyberWeekly intro (Michael himself chose all the links and did the analysis, so all commentary is from him) to share the load.

The NSO Group's Pegasus coverage is particularly noteworthy. It exposes the level of technical attack depth targeted attacks will go. The technical details provided by Amnesty are really important for blue (defence) teams and researchers. Fortunately, the vast majority of us will not warrant or attract such targeting. For the non-targeted 'average joe' promptly (ideally automatically) updating/patching your devices is the most important thing you can do if you're worried about this type of attack.

Between SolarWinds Orion and Kaseya VSA there has been a significant (valid) focus on supply chain attacks and how those impacts can ripple from upstream supplier, to supplier (such as a managed IT services company) to a customer/client and even their payment terminals grinding their businesses to a halt. Most organisations will still have no clue at all who, or what, their supply chain is formed of.
Even if organisations do all the right things (patching, MFA, monitoring) an event upstream negates all of that. We used to be able to debate the probability of such attacks happening and how they weren't targeting SMEs... the message is now clear: supply chain attacks are broad and can be indiscriminate to attract a larger ransomware payout.

Even if organisations are mature enough to critique their supply chain to sufficient depth (which of course is debatable as it may be client -> managed service provider -> managed service provider -> SolarWinds Orion, etc) MSPs are not motivated to share all of their tools, tactics and operational information with clients, let alone clients of clients. Contracts that share risk (indemnity) are moot, if the organisation who pay pursue such a case in court closes their doors because they are unable to handle the losses stemmed from the upstream attack. Many organisations do not hold enough cash reserves to deal with a sudden and total loss of income/operations, while being responsible for wages etc.

(Michael) What a few weeks it has been!  Joel helpfully contributed an introduction at short notice, for which I’m hugely thankful.  What he neglected to mention is that he had also read up on the Twitter research showing the poor takeup of MFA among its users.  Security people tend to forget that most users either don’t want to use MFA, or hear that it’s insecure from someone, and as such, the take-up is absurdly low.  Again, I’ll bang the drum that MFA is hands down the single most effective security control you can apply, SMS, app based or hardware token, doesn’t matter, it’s miles better than not having it.

## [Forensic Methodology Report: How to catch NSO Group’s Pegasus | Amnesty International](https://www.amnesty.org/en/latest/research/2021/07/forensic-methodology-report-how-to-catch-nso-groups-pegasus/)

[https://www.amnesty.org/en/latest/research/2021/07/forensic-methodology-report-how-to-catch-nso-groups-pegasus/](https://www.amnesty.org/en/latest/research/2021/07/forensic-methodology-report-how-to-catch-nso-groups-pegasus/)

> For a long time, triaging the state of a suspected compromised mobile device has been considered a near-impossible task, particularly within the human rights communities we work in. Through the work of Amnesty International’s Security Lab we have built  important capabilities that may benefit our peers and colleagues supporting activists, journalists, and lawyers who are at risk.
> 
> Therefore, through this report, we are not only sharing the methodology we have built over years of research but also the tools we created to facilitate this work, as well as the Pegasus indicators of compromise we have collected.
> 
> All indicators of compromise are available on our GitHub , including domain names of Pegasus infrastructure, email addresses recovered from iMessage account lookups involved in the attacks, and all process names Amnesty International has identified as associated with Pegasus.
> 
> Amnesty International is also releasing a tool we have created, called Mobile Verification Toolkit (MVT). MVT is a modular tool that simplifies the process of acquiring and analysing data from Android devices, and the analysis of records from iOS backups and filesystem dumps, specifically to identify potential traces of compromise.


Absolutely essential reading.  This story broke last week as I was writing CyberWeekly.  I was reading the first website to go up, but the content didn’t make sense at the time and with a deadline, I didn’t pick it up.

Ignoring the political and ethical ramifications of private and state level access to computer network exploitation tooling like commercial spyware, this release by Amnesty should massively uplift mobile phone forensic capabilities.  Forensically examining an apple device is still really hard and most organisations do not possess even the ability to get started if they think their executives might have been targeted.  The release of this report and the methodology and open source tools will enable far more organisations to uplift their detection capabilities.


## [A case against security nihilism – A Few Thoughts on Cryptographic Engineering](https://blog.cryptographyengineering.com/2021/07/20/a-case-against-security-nihilism/)

[https://blog.cryptographyengineering.com/2021/07/20/a-case-against-security-nihilism/](https://blog.cryptographyengineering.com/2021/07/20/a-case-against-security-nihilism/)

> Critics are correct that fixing these issues won’t stop exploits. The problem that companies like Apple need to solve is not preventing exploits forever, but a much simpler one: they need to screw up the economics of NSO-style mass exploitation.
> 
> Targeted exploits have been around forever. What makes NSO special is not that they have some exploits. Rather: NSO’s genius is that they’ve done something that attackers were never incentivized to do in this past: democratize access to exploit technology. In other words, they’ve done precisely what every “smart” tech business is supposed to do: take something difficult and very expensive, and make it more accessible by applying the magic of scale. NSO is basically the SpaceX of surveillance.
> 
> But this scalability is not inevitable.
> 
> NSO can afford to maintain a 50,000 number target list because the exploits they use hit a particular “sweet spot” where the risk of losing an exploit chain — combined with the cost of developing new ones — is low enough that they can deploy them at scale. That’s why they’re willing to hand out exploitation to every idiot dictator — because right now they think they can keep the business going even if Amnesty International or CitizenLab occasionally catches them targeting some human rights lawyer.


An excellent essay into the economics of the NSO group exploitation case.

NSO Group are just the best and most visible of these commercial spyware companies, but this is an industry problem.  The ability for states and major organisations to build intelligence service level computer network exploitation capabilities without the other investments needed means that the playing field is going to be levelled globally.

The cost of these exploits is still high, buying a target pack of 50 targets is still liable to cost you millions, and there’s no guarantees of getting access with that, that’s just people who they will attempt exploitation on, but they can scale that effectively, and can provide the same zero-day use over and over again.  What they have to build into the cost of those exploits is the detect and patch cycle of the big providers, and the more that Apple, Google and telecoms companies speed up that cycle, the greater the cost to companies like NSO Group, and thus the more selective they’ll be about their target lists.


## [He couldn’t get over his fiancee’s death. So he brought her back as an A.I. chatbot](https://www.sfchronicle.com/projects/2021/jessica-simulation-artificial-intelligence/)

[https://www.sfchronicle.com/projects/2021/jessica-simulation-artificial-intelligence/](https://www.sfchronicle.com/projects/2021/jessica-simulation-artificial-intelligence/)

> Joshua didn’t know much about language models. But because he had already fed Jessica’s real texts into Project December, it wasn’t hard for him to believe, even as a skeptic, that a ribbon of her authentic voice was woven through the chat. He’d handed the A.I. a Jessica-shaped compass: The bot wasn’t actually her, but it was “based on her,” he later said.
> 
> Of course, the simulation was based on Joshua as well. Because of the way Project December is set up, the seed text that gives birth to a bot is not static, but grows along with the chat: Each new word, whether selected by the bot or the human, gets added to the original seed.
> 
> Every time Joshua typed to the bot, then, he was shaping its next response. Still, he couldn’t predict where the chat might go.
> 
> The simulation really did appear to have a mind of its own. It was curious about its physical surroundings. It made gestures with its face and hands, indicated by asterisks. And, most mysterious of all, it seemed perceptive about emotions: The bot knew how to say the right thing, with the right emphasis, at the right moment.
> 
> Word by word, the A.I. was convincing him that a deep conversation was possible. He wondered: By speaking to Jessica as if she were alive again, could he engineer a moment of catharsis that had eluded him for eight years? Could this trick actually heal his grief?
> 
> He decided to try.


*Trigger warning for death and grief* - I don’t normally do trigger warnings but this one will hit you in the feels. I wouldn’t read this yet if that’s going to be a problem. 

I found this profoundly moving in a lot of ways. Dealing with grief is a funny thing because we all cope or fail to cope differently. There are lots of mechanisms to get closure, to feel like you’ve completed any open loops and had a chance to say goodbye properly.  People write letters, go to the graves, pray or even have conversations with their loved ones. 

The use of GPT-3 to imitate the textual style and personality of a dead loved one throws up some ethical questions, but in this case it seems to have worked to help Joshua cope with the loss and move on.  It’s a powerful reminder that it’s hard as creators to understand how our creations will be used and the profound impacts they can have on people’s lives. 

You can see Joshua tweet about this and respond to people who both loved it, hated it, feared it or were curious about it all here: https://twitter.com/joshuabarbeau/status/1418452459744280577?s=21


## [Ars AI headline experiment finale—we came, we saw, we used a lot of compute time | Ars Technica](https://arstechnica.com/information-technology/2021/07/ars-ai-headline-experiment-conclusion-we-came-we-saw-we-used-a-lot-of-compute-time/)

[https://arstechnica.com/information-technology/2021/07/ars-ai-headline-experiment-conclusion-we-came-we-saw-we-used-a-lot-of-compute-time/](https://arstechnica.com/information-technology/2021/07/ars-ai-headline-experiment-conclusion-we-came-we-saw-we-used-a-lot-of-compute-time/)

> Having reviewed the issues that we ran into with this exercise, several things rapidly became obvious. The first is that headlines are too short and do not provide enough context to accurately predict their performance, especially without considerably more data. With only 80 or so characters to work with, we improved our accuracy with the BERT-derived models by using the pair of headlines for context. Efforts to remove stop words and other things that we'd normally purge in natural-language processing tasks reduced the amount of signal available, reducing accuracy further.
> 
> Regardless of what ML benchmarks say, skilled humans will do a better job of choosing the better headline (usually). I could see that there were traits common to the headlines that failed tests, some of which I noted in the first article in this series: passive structure and use of qualifying words (like "may") or other words that commonly fall into what I refer to as "weasel words." Successful headlines were direct, precise, and engaging in ways that a machine would have difficulty catching (e.g. Beth Mole's weaponized puns).
> 
> As one of the Amazon engineers pointed out, the problem with headline choices is that they can be so subjective at times. While the more complex models were able to get some boost in accuracy (at least exceeding that of a coin flip), faster and lighter-weight models fall flat because they're only smart to a point.


It’s quite nice to see a writeup of a place where a technology has mostly failed. This helps break the hypecycle of people making out like technologies are a panacea.

This clearly demonstrates both the limitations of machine learning, that short small sentences are really hard to build models around, so tweets, headlines, chat logs are all far trickier than more complex long form sentences and paragraphs.

The second thing to pick from here is that the tooling, development flows and testing capabilities are still no where nearly capable enough to make it easy for normal people to take advantage easily.

Finally, there’s something around the deployment of trained models that needs more work.  there’s a growing movement of MLOps (or AIOps) that is looking at good practice and behaviours for building and deploying AI models effectively, but a lot of good practice is very nascent at the moment.


## [Kaseya Makes Customers Sign NDAs to Obtain Ransomware Decryptor](https://gizmodo.com/kaseya-is-making-its-customers-sign-non-disclosure-agre-1847356517)

[https://gizmodo.com/kaseya-is-making-its-customers-sign-non-disclosure-agre-1847356517](https://gizmodo.com/kaseya-is-making-its-customers-sign-non-disclosure-agre-1847356517)

> A new CNN report published on Friday revealed the non-disclosure agreements, citing several cybersecurity experts working with victims of the attack. The outlet notes that these agreements are not unusual in the cybersecurity industry, but that they could make it harder to understand how the attack occurred. The revelation is the latest step in Kaseya’s tight-lipped response since it announced it had obtained a “universal decryptor” from a “trusted third party” on Thursday.
> 
> It is still unknown where Kaseya got the decryptor from and whether it paid the mind-blowing $70 million ransom the REvil cybercriminal gang asked for in exchange for providing the universal key for all the roughly 1,500 victims worldwide in early July. To add another twist to the saga, days after claiming credit for the attack, the REvil gang disappeared from the internet.
> 
> The company declined to comment on whether it paid for the key in a statement to Gizmodo on Friday. However, some experts say it’s possible the Russian government could have given Kaseya the key after pressure from the Biden administration. Others claim Kaseya might have paid REvil’s ransom early on, after which the criminals went into hiding.


The Kaseya/REvil saga continues to get weirder and weirder.

Ignoring the weirdness around REvil’s disappearance, a managed service provider insisting that it’s customers sign a non-disclosure agreement before being allowed access to the incident response capabilities feels very negative.  It’s typical for the CIR company to sign a non-disclosure agreement, because nobody wants the information about who was affected spread by the incident responders, but in the relationship between a supplier and their customers, it’s less normal.  I would say that it’s questionable about whether it would be enforceable, if Kaseya was the route in which their customer was attacked and is refusing to hand over a solution to make good without a non-disclosure agreement, then it probably meets the definition for a contract made under duress.


## [State of Kubernetes Security Report 2021 [pdf]](https://www.redhat.com/rhdc/managed-files/cl-state-kubernetes-security-report-ebook-f29117-202106-en_0.pdf)

[https://www.redhat.com/rhdc/managed-files/cl-state-kubernetes-security-report-ebook-f29117-202106-en_0.pdf](https://www.redhat.com/rhdc/managed-files/cl-state-kubernetes-security-report-ebook-f29117-202106-en_0.pdf)

> DevSecOps is no longer just a buzzword—the term encompasses the processes and tooling that allows security to be built into the application development life cycle, rather than as an afterthought. Our survey found good news on this front—the vast majority of respondents say they have some form of DevSecOps initiative underway. Only 26% of respondents continue to operate DevOps separate from Security.
> 
> Even more promising is that 25% of respondents have an advanced DevSecOps initiative, where they’re integrating and automating security throughout the life cycle.


Interesting survey from Redhat (who of course will sell you a managed Kubernetes service) which shows that security concerns are a major part of kubernetes adoption.  One of things that I found interesting is that the respondents generally felt that their DevOps or SRE teams were responsible for the security of their platforms, rather than security teams.


## [New PetitPotam attack forces Windows servers to authenticate with an attacker - The Record by Recorded Future](https://therecord.media/new-petitpotam-attack-forces-windows-hosts-to-share-their-password-hashes/)

[https://therecord.media/new-petitpotam-attack-forces-windows-hosts-to-share-their-password-hashes/](https://therecord.media/new-petitpotam-attack-forces-windows-hosts-to-share-their-password-hashes/)

> The issue, discovered by Gilles Lionel, a Paris-based French security researcher, was nicknamed PetitPotam, and proof-of-concept (PoC) code was published earlier this week on GitHub.
> 
> According to Lionel, the issue takes place when an attacker abuses MS-EFSRPC, a protocol that allows Windows machines to perform operations on encrypted data stored on remote systems.
> 
> The PetitPotam attack PoC code allows an attacker to send SMB requests to a remote system’s MS-EFSRPC interface and force the victim computer to initiate an authentication procedure and share its authentication details.
> 
> Attackers can then collect this data and abuse it as part of a NTLM relay attack to gain access to remote systems on the same internal network.
> 
> A very dangerous issue
> 
> PetitPotam cannot be exploited remotely over the internet and is an attack designed to be used inside large corporate networks, where attackers could use it to force domain controllers to cough up their NTLM password hashes or authentication certificates, which could lead to the complete takeover of a company’s internal network.


This is a pretty serious issue.  Nobody disables NTLM even though it’s an old protocol, and lots of things on windows networks still rely on it, so you’ll have to patch this one when the patch comes out.

Because this is used as a second stage as part of an attack, this is being used to escalate privileges once an attacker has achieved remote execution.  Blue-teams should add the hashes for the POC to their detection tools straight away.


## [Biden official: ‘We don’t know exactly why’ ransomware gang vanished from the web - POLITICO](https://www.politico.com/news/2021/07/20/biden-official-ransomware-gang-revil-500376)

[https://www.politico.com/news/2021/07/20/biden-official-ransomware-gang-revil-500376](https://www.politico.com/news/2021/07/20/biden-official-ransomware-gang-revil-500376)

> When pressed on whether the administration has taken any action against such cyber criminals in Russia, the senior official would not say.
> 
> On REvil specifically, “We have certainly noticed that they’ve stood down their operations. We don’t know exactly why,” the official said. “But we’re still pressing on Russia to take action against the cyber criminals that are operating on its territory. We’re not declaring victory.”
> 
> 
> Asked if the Kremlin took down the group or made the group take down its sites, the official said: “It’s possible, I guess. Again, we don’t know exactly why they’ve stood down.” The official spoke on condition of anonymity per ground rules set by the administration.


It’s always difficult to parse these statements.  The US in particular has a very strong compartmentalisation mechnism for intelligence that means that it’s possible that whoever was speaking simply didn’t know what had happened, especially when it’s a statement being given under anonymity.

What is clear is that REvil has gone to ground, whether that’s because they’ve been taken out by a western cyber operation, by russian law enforcement, by a rival gang or because they’ve decided that ransomware is getting too hot and they’ve cashed out.  What’s good for us is that one of the most prolific and dangerous groups are no longer a threat.  

Of course, the individuals will still be around, may still have access to their funds, and may well disperse into the wider criminal underground, so we might see those skills and capabilities pop up elsewhere in coming months


## [Windows 10 July security updates break printing on some systems](https://www.bleepingcomputer.com/news/microsoft/windows-10-july-security-updates-break-printing-on-some-systems/)

[https://www.bleepingcomputer.com/news/microsoft/windows-10-july-security-updates-break-printing-on-some-systems/](https://www.bleepingcomputer.com/news/microsoft/windows-10-july-security-updates-break-printing-on-some-systems/)

> Redmond addressed Windows 10 printing issues caused by changes introduced in the June 2021 cumulative update preview earlier this month.
> 
> Users also encountered printing issues in March after installing the March 2021 Patch Tuesday updates, reporting that Windows 10 would crash when printing or print jobs would be missing graphics elements, blank pages, or other issues.
> 
> To resolve these issues, Microsoft released two out-of-band emergency updates for Windows 10 one week later: KB5001567 on March 15 to fix blue screen crashes when printing and KB5001649 on March 18 to fix the printing issues.
> 
> One day later, the company released yet another emergency update to fix additional printing issues besides blue screen crashes, including blank pages, document elements missing or printed as block boxes, and alignment or formatting issues.


This is why telling people to just patch isn’t as clear and simple as it’s made out.  You need to ensure that IT have the time and capacity to test the patches and make sure they work.  And if rolling out a security patch would definitely cause an impact then the business may well prefer to run with the risk of compromise rather than apply the patches.

There is workarounds for some systems, [disabling the print spooler on any systems that don’t need it](https://us-cert.cisa.gov/ncas/current-activity/2021/06/30/printnightmare-critical-windows-print-spooler-vulnerability) can reduce the impact.


## [The State of Developer Ecosystem in 2021 Infographic | JetBrains: Developer Tools for Professionals and Teams](https://www.jetbrains.com/lp/devecosystem-2021/)

[https://www.jetbrains.com/lp/devecosystem-2021/](https://www.jetbrains.com/lp/devecosystem-2021/)

> This report presents the combined results of the fifth annual Developer Ecosystem Survey conducted by JetBrains. 31,743 developers from 183 countries or regions helped us map the landscape of the developer community.
> Here you can find the latest trends in the tech industry, as well as interesting facts about tools, technologies, programming languages, and many other facets of the programming world.


This is an interesting report that shows the changing development landscape.  

There’s nothing too surprising in here, a couple of interesting tidbits which caught my eye includes the odd statistic that developers who work with microservices tend to be more senior than those who don’t (cannot work out why that would be), that US based developers are paid significantly more than Brits and Canadians (I wonder if this is just cost of living, a silicon valley effect, or the healthcare/benefits regimes being different), and that developers primarily use Windows as their main development platform with MacOS coming a close but definite second.


## [Account Security (Report July 14, 2021) | Twitter](https://transparency.twitter.com/en/reports/account-security.html#2020-jul-dec)

[https://transparency.twitter.com/en/reports/account-security.html#2020-jul-dec](https://transparency.twitter.com/en/reports/account-security.html#2020-jul-dec)

> "Overall 2FA adoption remains relatively low, which is an unfortunate challenge across the industry. When accounts do not enable 2FA, we are left relying on less robust mechanisms to help keep Twitter accounts secure. We are, however, encouraged to see a significant increase in 2FA usage over the reporting period since it shows that people are increasingly utilizing 2FA to protect their Twitter accounts."
> 
> 2.3% of active Twitter accounts with *at least one 2FA method enabled* on average over the reporting period. Of the 2.3% of active Twitter accounts that have at least one type of 2FA enabled, 79.5% use SMS, 30.9% use an authentication app and 0.5% use a security key.
> 
> A handy TL;DR thread is [https://twitter.com/RachelTobac/status/1417984118810238976](https://twitter.com/RachelTobac/status/1417984118810238976)


(Joel) Not much to unpack here.

My summary takeaway? Twitter (and other services) should be using more nudges to not just hoover up more contact details, but actually nudge people into enabling and using MFA. SMS MFA is still great for the vast majority of people. (It happens to also be a lot better than no MFA at all!)


## [Classified Challenger tank specs leaked online for videogame](https://ukdefencejournal.org.uk/classified-challenger-tank-specs-leaked-online-for-videogame/)

[https://ukdefencejournal.org.uk/classified-challenger-tank-specs-leaked-online-for-videogame/](https://ukdefencejournal.org.uk/classified-challenger-tank-specs-leaked-online-for-videogame/)

> A user identifying as a Challenger 2 commander posted specific excerpts from a Challenger 2 AESP (Army Equipment Support Publication, sort of like a user manual) to show game developers that they “didn’t model it correctly”.
> 
> The user identifies as a make in Tidworth with a history of “Tanks & AFV’s, CR2 Tank Commander, AFV Instr, D&M Instr, Gunnery Instr, Former ATDU”. It should be noted that Tidworth is home to the Royal Tank Regiment who operate Challenger 2 tanks.
> 
> 
>  
> Anyway, it is understood that the excerpts from the document had their ‘UK RESTRICTED’ label crossed out and a stamp of ‘UNCLASSIFIED’ added, as well as having various parts fully blanked. One forum user remarked that “the cover for instance had basically everything except CHALLENGER 2 blacked out”.


So, this is how redaction is done to reduce classification, and I suspect that the person in question felt that they had done a suitable job, however declassification can only be done by the information owner, not by any user who feels that they want to.

It’s also worth noting that within the UK classification system, Restricted is no longer a formal classification, replaced with Official, which is the lowest classification that a document can have. Under the old system, Restricted was only the second lowest classification, which used to run in the order Unclassified, Protect, Restricted, Confidential, Secret and then Top Secret.  That’s not to say that it’s not classified material, but that the material is very low classification and available to large numbers of serving military staff.


