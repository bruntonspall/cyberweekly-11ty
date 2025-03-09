---
title: "202 - Where responsibilities lie"
date: 2022-07-10
description: "If you run a major company, and use code written by a hobbyist developer, whose job is it to ensure the code is secure?"
permalink: /where-responsibilities-lie/
---

If you run a major company, and use code written by a hobbyist developer, whose job is it to ensure the code is secure?

What if that code is not used directly by you, but you are using a popular open source framework that is supported by an open source foundation and they use the hobbyist code?

When log4j was happening, Daniel Stenberg, the maintainer of Curl (and libcurl) [received a mandatory survey from a Fortune-500 company](https://daniel.haxx.se/blog/2022/01/24/logj4-security-inquiry-response-required/) saying that as a supplier of theirs, he needed to answer questions about whether log4j affected him.

Of course, this is how large companies do deal with their supply base.  If they bought till software from a company, they write to that company to get them to validate that it's not vulnerable to the latest vulnerability, or better yet, insist in their contract that the company provide security updates and notices within a short deadline of a vulnerability being announced.  This works when you are dealing with vmWare, or Oracle, or Microsoft for your commercial operating system tools, but it starts to fall apart when companies don't realise just how open source software is embedded in their systems.

But further, the push for dependency and supply chain solutions is liable to keep pushing requirements down on the people writing the software.   It's kind of seen as if software supply chain is like a pyramid, at the top there's you with your one till system, and below that a number of suppliers and bits of software that make that up, and below that much wider base of libraries and code that makes a baseline of the software.  But in fact it's much more of an hourglass shape, because there are thousands of companies just like you, who all use the same accounting, or business process packages.  That means that requirements for secure development are flowing down into some of those critical frameworks hundreds or thousands of times over.

If those frameworks simply pass their responsibilities for secure software onto the libraries below them, then it's creating work and noise for software developers, many of whom are simply [not paid well enough, or in some cases at all](https://thenextweb.com/news/log4j-bug-internet-open-source-contributors-analysis).

The vetting concept is a good one, by taking the responsibility for vetting packages sideways, or into the big software foundations, we can drive some standards that developers might want to use.  However it will also create some weird incentives in the system, that those vetters will be incentivised to raise bugs in the dependant systems, but not to fix them.  

There are companies that are doing something like this already, such as [418sec](https://www.418sec.com/) based out of London who have a really impressive supply chain trust system that includes paying bounties to fix vulnerabilities in their clients codebases.  However that of course resulted in the confused release of a [9.8 CVE in Loguru](https://portswigger.net/daily-swig/no-smoke-without-fire-critical-loguru-security-flaw-turns-out-to-be-non-issue) that was almost certainly not a real flaw, but a false positive detected by an automated scanner.

> Offering further insight, Justin Hutchings, director of product management at GitHub, told The Daily Swig: “CVE-2022-0329 was issued by huntr.dev with a severity of 3.8 (low).
>
> “The National Vulnerability Database (NVD) upgraded the severity score to 9.8 (critical) when they published it, and we subsequently republished it to our Advisory Database and started sending alerts.

This mix of different people, with different incentives and differing levels of expertise in the systems, languages and libraries under the microscope is always going to result in some mixups.

Getting this right is going to be hard, and we're going to have to see lots of ways of trying to improve the current estate.  But it should be on your organisations risk register, even if you don't have a good solution yet.

## The Cyberweekly Survey

As I’ve been doing this newsletter for nearly 4 years, I decided that it was time to find out if I’m doing a good job. I can tell from subscriptions that more and more people are subscribing, but I don’t know what’s working well or badly. I’ve put together some simple questions into a Google Form, and if you’ve got 2-5 minutes, I’d really appreciate some feedback. You can find the Form here: [https://docs.google.com/forms/d/e/1FAIpQLSeojV4ILcB7Oz9rPtNMPHCGRFL1ctfaiwpS2ZvsOqbCBDu9rA/viewform?usp=sf_link](https://docs.google.com/forms/d/e/1FAIpQLSeojV4ILcB7Oz9rPtNMPHCGRFL1ctfaiwpS2ZvsOqbCBDu9rA/viewform?usp=sf_link)

## [Congratulations: We Now Have Opinions on Your Open Source Contributions | Armin Ronacher's Thoughts and Writings ](https://lucumr.pocoo.org/2022/7/9/congratulations/)

[https://lucumr.pocoo.org/2022/7/9/congratulations/](https://lucumr.pocoo.org/2022/7/9/congratulations/)

> On Friday I along many others in the Python community "congratulated" me on having created [a critical package](https://pypi.org/security-key-giveaway/) . Once packages are within a certain level of adoption compared to the global downloads, they are considered critical. Currently if you maintain a "critical" package it means that you need to enroll a multi factor authenticator. It appears that the hypothetical consequence of not enrolling into 2FA is not being able to release new versions. My visceral reaction to this email was not positive.
> 
> From the package index' point of view increasing the protection for critical packages makes a lot of sense. Running a package index is expensive and the users of the package index really do want to reduce the chance that a package that they depend on is compromised. In theory that type of protection really should apply to every package. That's not what PyPI did, they decided to draw a line between “critical” and other packages.
> 
> From the index' point of view I really understand this, but as a developer of Open Source software I'm quite conflicted about this. The message to me as a maintainer is quite clear: once a project achieved criticality, then the index wants to exercise a certain amount of control. From the index' perspective it's within the bounds of it's terms of service to put further restrictions on such a project.
> 
> However when I create an Open Source project, I do not chose to create a “critical” package. It becomes that by adoption over time. Right now the consequence of being a critical package is quite mild: you only need to enable 2FA. But a line has been drawn now and I'm not sure why it wouldn't be in the index best interest to put further restrictions in place.
> 
> Instead of putting the burden to the user of packages, we're now piling stuff onto the developer who already puts their own labor and time into it.
> 
> […]
> 
> In the Rust world Mozilla started a project that looks quite promising called [cargo-vet](https://github.com/mozilla/cargo-vet) . It's based on the idea that the users of packages can vet dependencies and most importantly individual versions of them. You can share your vettings with others or at least within your organization. There is an interactive tool that assists you in the vetting process. It will help you audit the source code, the diffs between vetted versions, show you the changelog and more. After you made a decision about the individual version you can commit your attestation and others can use it too. Others typically means same company, but one could imagine that this also turns into independent companies or others to perform these vettings. 


Python has just had it’s “leftpad” moment, where a package was removed from the core Python Packing Index over this, and that potentially has caused dependency breakage all the way down.

I use Armin’s absolutely fantastic python web framework, Flask, to build the website that powers CyberWeekly and have done for years.

His point here is really valid.  As an open source maintainer, he just creates tools that meet his needs.  Sometimes those are useful for others, sometimes not, but when one reaches a level of criticality, the onus appears to drift down to him to enforce security policies and do additional work.  And all of this for software that he writes for his own use, not because he wants it to be critical in someone else’s system.

The proposal here around Rusts package manager, of enabling not just a package, but an open source system of vetting would enable you to offload some of that security work to others.  They can tell everyone whether or not the package is any good, and what policies it meets.  Those independent vettings will of course create work for those developers who deliberately want to create critical packages, but can be easily ignored by hobbyist developers, meaning that leftpad type hobbyist packages shouldn’t enter the dependency tree for major critical packages without people being aware.

Of course, with over 350,000 packages in PyPI, and 1.2 million in NPM, the horse may well and truly have bolted already 


## [This Is the Code the FBI Used to Wiretap the World ](https://www.vice.com/en/article/v7veg8/anom-app-source-code-operation-trojan-shield-an0m)

[https://www.vice.com/en/article/v7veg8/anom-app-source-code-operation-trojan-shield-an0m](https://www.vice.com/en/article/v7veg8/anom-app-source-code-operation-trojan-shield-an0m)

> The app uses XMPP to communicate, a long-established protocol for sending instant messages. On top of that, Anom wrapped messages in a layer of encryption. XMPP works by having each contact use a handle that in some way looks like an email address. For Anom, these included an XMPP account for the customer support channel that Anom users could contact. Another of these was bot.
> 
> Unlike the support channel, bot hid itself from Anom users’ contact lists and operated in the background, according to the code and to photos of active Anom devices obtained by Motherboard. In practice the app scrolled through the user’s list of contacts, and when it came across the bot account, the app filtered that out and removed it from view. 
> 
> That finding is corroborated by law enforcement files Motherboard obtained which say that bot was a hidden or “ghost” contact that made copies of Anom users’ messages.
> 
> Authorities have previously floated the idea of using a ghost contact to penetrate encrypted communications. In a [November 2018 piece published on](https://www.lawfareblog.com/principles-more-informed-exceptional-access-debate) [_Lawfare_](https://www.lawfareblog.com/principles-more-informed-exceptional-access-debate) , Ian Levy and Crispin Robinson, two senior officials from UK intelligence agency GCHQ, wrote that “It’s relatively easy for a service provider to silently add a law enforcement participant to a group chat or call,” and “You end up with everything still being end-to-end encrypted, but there’s an extra ‘end’ on this particular communication.”
> 
> The code also shows that in the section that handles sending messages, the app attached location information to any message that is sent to bot. On top of that, the AndroidManifest.xml file in the app, which shows what permissions an app accesses, includes the permission for “ACCESS_FINE_LOCATION.” This confirms what [Motherboard previously reported](https://www.vice.com/en/article/93b3ay/fbi-backdoor-anom-phones-gps-data) after reviewing thousands of pages of police files in an Anom-related investigation. Many of the intercepted Anom messages in those documents included the precise GPS location of the device at the time the message was sent. 


Motherboard are treading a fine line here.  Exposing how this attack was carried out prevents the FBI from easily doing so again, or at least in theory.

In reality, this attack, the so called Ghost Protocol, is incredibly difficult to detect unless you can decompile the software.  We trust our endpoints, we trust that our iphones don’t modify Whatsapp when it’s running, and we trust that the Whatsapp application doesn’t secretly expose our logs.

If the application had stored or sent the logs out via another mechanism, getting them out of the end to end encrypted stream, then a network analyser might have found the log exfiltration system.  But by adding a secret third party to the encryption system, the messages look exactly like they normally do, and the intercept capability is entirely done on the server end, which is a really smart way of implementing such encryption.

There’s very little you can do to protect against this attack, but it’s also outside of almost all non-criminal threat models, so that’s probably an acceptable risk that society is willing to take. 


## [China lured graduate jobseekers into digital espionage](https://arstechnica.com/information-technology/2022/06/china-lured-graduate-jobseekers-into-digital-espionage/)

[https://arstechnica.com/information-technology/2022/06/china-lured-graduate-jobseekers-into-digital-espionage/](https://arstechnica.com/information-technology/2022/06/china-lured-graduate-jobseekers-into-digital-espionage/)

> The application process included translation tests on sensitive documents obtained from US government agencies and instructions to research individuals at Johns Hopkins University, a key intelligence target.
> 
> Hainan Xiandun is alleged by a 2021 US federal indictment to have been a cover for the Chinese hacking group APT40. Western intelligence agencies have accused APT40 of infiltrating government agencies, companies and universities across the US, Canada, Europe and the Middle East, under the orders of China’s Ministry of State Security (MSS).
> The FBI sought to disrupt the activities of Hainan Xiandun last July by indicting three state security officials in Hainan province—Ding Xiaoyang, Cheng Qingmin and Zhu Yunmin—for their alleged role in establishing the company as a front for state-backed espionage. Another man mentioned in the indictment, Wu Shurong, is believed to be a hacker who helped supervise employees at Hainan Xiandun.
> 
> Western intelligence services also seek out prospective spies from universities, with applicants undergoing rigorous vetting and training before joining the likes of the CIA in the US or the UK’s GCHQ signals intelligence agency.
> 
> But Chinese graduates targeted by Hainan Xiandun appear to have been unwittingly drawn into a life of espionage. Job advertisements from the company were posted on university websites for translators without further explanation of the nature of the work.
> 
> This could have life-long consequences, as individuals identified as having co-operated with the MSS through their work for Hainan Xiandun are likely to face difficulty in living and working in Western countries, a key motivation for many students who study foreign languages. 


Fascinating primarily because it's the lack of transparency that we see as an issue.  Of course it's possible to do this sort of work for western intelligence agencies as well, but they tend to be transparent about who the person is working for and ensuring that they understand the implications on their career and future job opportunities.

The fact that it's not just a cover agency from the perspective of outsiders, but also from insiders, that some of the people working there didn't know who they were working for is quite the thing.  It makes me wonder just how that's possible, if the tests you are given are sensitive documents that you've obtained through espionage, how do you ensure that the workers don't twig to what they are translating?  How do you make sure they handle and manage the documents correctly?  Presumably, by the time people get to working on the most sensitive stuff, they do know what they are doing, it's just that the path to get there wasn't clearly signposted, and so translators might find themselves already in the role and doing the work before they start to discover where they are.


## [ATT&CK® for Containers now available! | by Jen Burns | MITRE-Engenuity | Apr, 2021 | Medium](https://medium.com/mitre-engenuity/att-ck-for-containers-now-available-4c2359654bf1)

[https://medium.com/mitre-engenuity/att-ck-for-containers-now-available-4c2359654bf1](https://medium.com/mitre-engenuity/att-ck-for-containers-now-available-4c2359654bf1)

> We talked about how we created ATT&CK for Containers in a previous blog post, and we recommend checking that out to learn more about our process. As a refresher on scope of ATT&CK for Containers, despite what the ATT&CK Twitter account mentioned on April 1st, it actually covers orchestration-level (e.g. Kubernetes) and container-level (e.g. Docker) adversary behaviors in a single Containers platform in ATT&CK.


This is a useful update to ATT&CK covering not just common infrastructure, but now covering container specific attacks as well as techniques for attacks on the container orchestration platforms.


## [About | cloudvulndb.org ](https://www.cloudvulndb.org/about)

[https://www.cloudvulndb.org/about](https://www.cloudvulndb.org/about)

> Security bugs in cloud services tend to [fall between the cracks](https://www.wiz.io/blog/security-industry-call-to-action-we-need-a-cloud-vulnerability-database/) , as they don’t fit well into the current [shared responsibility model](https://cloudsecurityalliance.org/blog/2020/08/26/shared-responsibility-model-explained/) of cloud security. As a result, remediation often requires a joint effort between both the CSP and their customers.
> 
> There is currently no universal standard for cloud vulnerability enumeration – CSPs rarely issue CVEs for security mistakes discovered in their services, there are no industry conventions for assessing severity, no proper notification channels and no unified tracking mechanism – this leads to a great deal of inefficiency and confusion.
> 
> Our goal in this project is to pave the way for a centralized cloud vulnerability database, by cataloging CSP security mistakes and listing the exact steps CSP customers can take to detect or prevent these issues in their own environments. 


The existing CVE system for enumerating vulnerabilities and weaknesses is predicated around the concept of software in a box, or software as a release.  But cloud providers as a service can have architectural flaws or weaknesses that aren’t well described by a CVE.

This project aims to enumerate those we know about, and allow security researchers to register new vulnerabilities in default configurations, service provision and so on.  

Well worth a look and thinking about how you’d apply this in your own risk scoring mechanism 


## [GitHub - h3xduck/TripleCross: A Linux eBPF rootkit with a backdoor, C2, library injection, execution hijacking, persistence and stealth capabilities. ](https://github.com/h3xduck/TripleCross)

[https://github.com/h3xduck/TripleCross](https://github.com/h3xduck/TripleCross)

> TripleCross is a Linux eBPF rootkit that demonstrates the offensive capabilities of the eBPF technology.
> 
> TripleCross is inspired by previous implant designs in this area, notably the works of Jeff Dileo at DEFCON 27 [1](https://github.com/h3xduck/TripleCross#user-content-fn-1-1d5826d44eaa430d8c5198b61c1d6d6e) , Pat Hogan at DEFCON 29 [2](https://github.com/h3xduck/TripleCross#user-content-fn-2-1d5826d44eaa430d8c5198b61c1d6d6e) , Guillaume Fournier and Sylvain Afchain also at DEFCON 29 [3](https://github.com/h3xduck/TripleCross#user-content-fn-3-1d5826d44eaa430d8c5198b61c1d6d6e) , and Kris Nóva's Boopkit [4](https://github.com/h3xduck/TripleCross#user-content-fn-4-1d5826d44eaa430d8c5198b61c1d6d6e) . We reuse and extend some of the techniques pioneered by these previous explorations of the offensive capabilities of eBPF technology.
> 
> This rootkit was created for my Bachelor's Thesis at UC3M. More details about its design are provided in the [thesis document](https://github.com/h3xduck/TripleCross/blob/master/docs/ebpf_offensive_rootkit_tfg.pdf) . 


This has some amazing diagrams and shows just how powerful malware written to abuse the Berkley Pattern Filter capabilities in the linux kernel.  

Originally written to make it possible to write security modules that can monitor and handle security events happening deep within the kernel without needing to actually write a full kernel module, it provides a set of core capabilities that is incredibly valuable for malware. 


## [How a fake job offer took down the world’s most popular crypto game ](https://www.theblock.co/post/156038/how-a-fake-job-offer-took-down-the-worlds-most-popular-crypto-game)

[https://www.theblock.co/post/156038/how-a-fake-job-offer-took-down-the-worlds-most-popular-crypto-game](https://www.theblock.co/post/156038/how-a-fake-job-offer-took-down-the-worlds-most-popular-crypto-game)

> Ronin, the Ethereum-linked sidechain that underpins play-to-earn game Axie Infinity, [lost $540 million](https://www.theblock.co/post/139761/axie-infinitys-ethereum-sidechain-ronin-hit-by-600-million-exploit) in crypto to an exploit in March. While the US government later [tied the incident](https://www.coindesk.com/policy/2022/04/14/us-officials-tie-north-korean-hacker-group-to-axies-ronin-exploit/) to North Korean hacking group Lazarus, full details of how the exploit was carried out have not been disclosed. 
> 
> The Block can now reveal that a fake job ad was Ronin’s undoing. 
> 
> According to two people with direct knowledge of the matter, who were granted anonymity due to the sensitive nature of the incident, a senior engineer at Axie Infinity was duped into applying for a job at a company that, in reality, did not exist.
> 
> […]
> 
> After what one source described as multiple rounds of interviews, a Sky Mavis engineer was offered a job with an extremely generous compensation package. 
> 
> The fake “offer” was delivered in the form of a PDF document, which the engineer downloaded — allowing spyware to infiltrate Ronin’s systems. From there, hackers were able to attack and take over four out of nine validators on the Ronin network — leaving them just one validator short of total control. 
> In [a post-mortem](https://roninblockchain.substack.com/p/back-to-building-ronin-security-breach) blog post on the hack, published April 27, Sky Mavis said: “Employees are under constant advanced spear-phishing attacks on various social channels and one employee was compromised. This employee no longer works at Sky Mavis. The attacker managed to leverage that access to penetrate Sky Mavis IT infrastructure and gain access to the validator nodes.” 


A great example of how a targeted lure can get someone.  

As always, the key lesson here is not about not allowing users to click links or open PDF’s that are dodgy, it’s almost impossible for even expert users to tell good from bad.  It’s to ensure that your IT systems cannot or should not be compromised by a piece of drive by malware.  That means good endpoint protection software, application allow lists and good blast radius protection so that one compromised device cannot take out the entire network. 


## [Absurd Trolley Problems ](https://neal.fun/absurd-trolley-problems/)

[https://neal.fun/absurd-trolley-problems/](https://neal.fun/absurd-trolley-problems/)

> Oh no! A trolley is heading towards 5 people. You can pull the lever to divert it to the other track, killing 1 person instead. What do you do? 


Just an absolutely lovely bit of fun that also gives you some insight into how many people take which choice.  Wonderfully put together and illustrated 


## [‘Some staff work behind armoured glass’: a cybersecurity expert on The Undeclared War | Television | The Guardian ](https://www.theguardian.com/tv-and-radio/2022/jul/07/some-staff-work-behind-armoured-glass-a-cybersecurity-expert-on-the-undeclared-war)

[https://www.theguardian.com/tv-and-radio/2022/jul/07/some-staff-work-behind-armoured-glass-a-cybersecurity-expert-on-the-undeclared-war](https://www.theguardian.com/tv-and-radio/2022/jul/07/some-staff-work-behind-armoured-glass-a-cybersecurity-expert-on-the-undeclared-war)

> When I heard there was going to be a TV drama about [cybersecurity](https://www.theguardian.com/technology/data-computer-security) , my initial reaction was that it was a brave thing to attempt. Trying to make what we do televisual is notoriously difficult. There is very little to see – just people tapping at keyboards and staring at screens, with most of the action going on inside their heads. So I have been pleasantly surprised by Peter Kosminsky’s Channel 4 series [The Undeclared War](https://www.theguardian.com/tv-and-radio/2022/jul/03/the-undeclared-war-review-peter-kosminsky-aids-the-unheard-tapes-sherwood-only-murders-in-the-building-money-heist-korea-joint-economic-area) (whose [second episode airs tonight](https://www.channel4.com/programmes/the-undeclared-war) ). I binge-watched the entire thing in a weekend.
> 
> The cyber-attack on the UK in episode one was all too credible. I initially thought they were going to be vague and melodramatic – “The internet’s gone down!” – but the script went on to explain how the BT infrastructure, which does run a huge chunk of web traffic in the UK, had been taken offline. They specified how 55% of web access had been lost and it was cleverly timed to be a disruptive attack, rather than a disastrous one with planes falling out of the sky. You can cause a lot of chaos by taking out any of these “Tier 1 networks”. We’ve seen it happen by accident – last October, [Facebook managed to wipe itself](https://www.theguardian.com/technology/2021/oct/05/facebook-outage-what-went-wrong-and-why-did-it-take-so-long-to-fix) by mistake – so it’s perfectly plausible an attacker could do the same.
> 
> […]
> 
> I enjoyed the juxtaposition in the Cobra meeting between what the ministers demanded and what GCHQ advised. Politicians often suffer from “do-something-itis” – they want to be seen to take decisive action. Nobody in our trade would think hacking back is a good idea, because it leads to escalation. The GCHQ representatives – Danny Patrick (Simon Pegg) and David Neal (Alex Jennings) – correctly pointed out that tit-for-tat can go horribly wrong. If you’re not careful, a conflict in cyberspace can escalate into military retaliation. Indeed, [Nato’s Tallinn document](https://cyberlaw.ccdcoe.org/wiki/Scenario_17:_Collective_responses_to_cyber_operations) says that if it comes under a cyber-attack of sufficient magnitude, it reserves the right to respond “kinetically”, meaning missiles and bombs.
> 
> The drama also highlighted the huge problem with retaliation. Cyber-attacks allow plausible deniability, and attribution is incredibly difficult. People presume it was the Russians but nobody knows for certain. If someone launches a missile at you, you’re pretty sure where it came from. With cyber-attacks, it’s hard to tell who wrote the code and where they were. It is also easy to plant false flags in there – make it look North Korean, say, or timestamp files to correspond with Moscow timezones. You need ancillary intelligence because the bits and pieces gleaned from electronic warfare data aren’t enough. 


This review matches my feelings on this series, only a few episodes in.  It’s a fabulous series that really does a good job of trying to represent computer security in a realistic way while still trying to make it dramatic.   I note from the credits that Ollie who pulls together the BluePurple Pulse newsletter and the excellent r/blueteamsec was a consultant on the screenshots and code, which probably adds to the realism

Enjoyable so far and worth a watch if you can 


