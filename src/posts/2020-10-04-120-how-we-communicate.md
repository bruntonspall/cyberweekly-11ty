---
title: "120 - How we communicate"
date: 2020-10-04
description: "How we communicate really matters.  If we want to be taken seriously, we have to be sure that everyone hears us communicate clearly and simply."
permalink: /how-we-communicate/
---

How we communicate really matters.  If we want to be taken seriously, we have to be sure that everyone hears us communicate clearly and simply.

Security and digital folks alike have a tendency to have our own language, from scrum to penetration test, and deployment to exploit.  It's ok for us to have language that is clear and concise for talking to each other, but when we talk to people outside our industry, we need to take the time and effort to ensure that we are clear, simple and understandable.

Being clear and concise is a difficult skill, one that requires hard work to determine what is understandable by our audience, what can be misinterpreted and yes, what jargon or technical language we use.  Sometimes that technical language is about specificity, sometimes you need to know that a team is doing XP or Scrum, but much of the time it's clearer to the people we are talking to when we are less specific but more understandable.  That team is writing software in an agile manner, where the work is reprioritised by their customers every two weeks.

Regardless of whether we prefer specific language or whether we like certain publishing formats (like PDF's), it's more important that we are welcome, understood and understandable.

## [How Malicious Tor Relays are Exploiting Users in 2020 (Part I) | by nusenu | Aug, 2020 | Medium](https://medium.com/@nusenu/how-malicious-tor-relays-are-exploiting-users-in-2020-part-i-1097575c0cac)

[https://medium.com/@nusenu/how-malicious-tor-relays-are-exploiting-users-in-2020-part-i-1097575c0cac](https://medium.com/@nusenu/how-malicious-tor-relays-are-exploiting-users-in-2020-part-i-1097575c0cac)

> The full extend of their operations is unknown, but one motivation appears to be plain and simple: profit.
> 
> They perform person-in-the-middle attacks on Tor users by manipulating traffic as it flows through their exit relays. They (selectively) remove HTTP-to-HTTPS redirects to gain full access to plain unencrypted HTTP traffic without causing TLS certificate warnings. It is hard to detect for Tor Browser users that do not specifically look for the “https://” in the URL bar. This is a well known attack called “ssl stripping” that exploits the fact that user rarely type in the full domain starting with “https://”. There are established countermeasures, namely HSTS Preloading and HTTPS Everywhere, but in practice many website operators do not implement them and leave their users vulnerable to this kind of attack. This kind of attack is not specific to Tor Browser. Malicious relays are just used to gain access to user traffic. To make detection harder, the malicious entity did not attack all websites equally. It appears that they are primarily after cryptocurrency related websites — namely multiple bitcoin mixer services. 
> 
> They replaced bitcoin addresses in HTTP traffic to redirect transactions to their wallets instead of the user provided bitcoin address. Bitcoin address rewriting attacks are not new, but the scale of their operations is. It is not possible to determine if they engage in other types of attacks.


Tor relays can see everything you do on the web, and can interfere with all of the traffic.  Using Tor to browse the web is deliberately choosing to allow an person-in-the-middle attack on all of your content. Even worse, given the use of amnesiac browsers like Tails and TorBrowser, there's a good chance that any use of HTTPS you'll be subject to the worst position for being attacked, that of the first connection, during which certificates are exchanged and keys setup.


## [Exploring the Ubiquiti UniFi Cloud Key Gen2 Plus | by Katie Sexton | Tenable TechBlog | Aug, 2020 | Medium](https://medium.com/tenable-techblog/exploring-the-ubiquiti-unifi-cloud-key-gen2-plus-f5b0f7ca688)

[https://medium.com/tenable-techblog/exploring-the-ubiquiti-unifi-cloud-key-gen2-plus-f5b0f7ca688](https://medium.com/tenable-techblog/exploring-the-ubiquiti-unifi-cloud-key-gen2-plus-f5b0f7ca688)

> What could go wrong with arbitrarily testing API endpoints? Well, most of my API testing was performed externally, but I did try running the test scripts from the command line of the Cloud Key itself to test localhost. I learned that the UniFi Management Portal API doesn’t require authentication for requests from localhost, and I also learned that arbitrarily sending requests to all of the available UMP APIs is not a very safe thing to do. In particular, the /ump/device endpoints can power off, reboot, or factory reset the device with a GET request from localhost.
> 
> At least the script hit “power-off” first and not “reset.” Silver linings


There are lots of fans of UniFi networking kit, not least because Security Researcher Troy Hunt wrote about [wiring his house with them back in 2017](https://www.troyhunt.com/wiring-a-home-network-from-the-ground-up-with-ubiquiti/).

It seems like the cloud controllers haven't had as much security attention as they should have had though.  This exploratory post talks about how the Tenable security researcher, Katie, had a bit of a poke at the software, and leaves me far more questions than answers.  Hopefully Ubiquiti pay attention to this and up their game.


## [The Secret SIMs Used By Criminals to Spoof Any Number](https://www.vice.com/en/article/n7w9pw/russian-sims-encrypted)

[https://www.vice.com/en/article/n7w9pw/russian-sims-encrypted](https://www.vice.com/en/article/n7w9pw/russian-sims-encrypted)

> "Scammers use [it] to to call people so it shows [a] bank number or eBay," one alleged vendor, who went by the handle Captain on the messaging app Telegram, told Motherboard. "They get sold worldwide. Spain. Morocco. Europe shit loads," they added.
> 
> "You can actually pick any number that you want," the person who said they phoned me from one of the SIMs said. "I could change it every call and keep running from a different number every time," they added, making blocking a caller difficult.
> 
> Though some of these SIMs are sold clandestinely, through messaging apps and via people in-the-know, public facing companies also sell these cards.


The terrifying underground of clandestine sim cards, allowing the called to spoof their number.  While not really a security feature against a threat model of a serious police investigation, getting the real caller id out of the mobile operators and telecoms companies is going to require quite a lot more investigative effort than most police cases are going to expend.

How often do we tell our users to only accept calls from known numbers, to be aware of who is calling them.  This suggests that calling from a spoofed number is cheaper and easier than many people previously assumed.


## [[Blog] Zerologon: instantly become domain admin by subverting Netlogon cryptography (CVE-2020-1472)](https://www.secura.com/blog/zero-logon)

[https://www.secura.com/blog/zero-logon](https://www.secura.com/blog/zero-logon)

> Last month, Microsoft patched a very interesting vulnerability that would allow an attacker with a foothold on your internal network to essentially become Domain Admin with one click. All that is required is for a connection to the Domain Controller to be possible from the attacker’s viewpoint.
> 
> Secura's security expert Tom Tervoort previously discovered a less severe Netlogon vulnerability last year that allowed workstations to be taken over, but the attacker required a Person-in-the-Middle (PitM) position for that to work. Now, he discovered this second, much more severe (CVSS score: 10.0) vulnerability in the protocol. By forging an authentication token for specific Netlogon functionality, he was able to call a function to set the computer password of the Domain Controller to a known value. After that, the attacker can use this new password to take control over the domain controller and steal credentials of a domain admin.


This is an extremely serious vulnerability.  You might think that you wouldn't have your Domain Controller connected to the internet, yet lots of people do.  But even if you don't, it's incredibly difficult to block this one with firewalls or other rules.  You should patch ASAP as there is proof of concept code available and it's being weaponised and exploited today


## [Dark Web Price Index 2020. Check all 2020 Dark Web Prices](https://www.privacyaffairs.com/dark-web-price-index-2020/)

[https://www.privacyaffairs.com/dark-web-price-index-2020/](https://www.privacyaffairs.com/dark-web-price-index-2020/)

> You might be asking yourself, just how easy is it to obtain someone else’s personal information, documents, account details? 
> 
> We certainly were.
> 
> To see just how prevalent such items of personal data are being listed, and at what price, we sent our researchers on a data-gathering mission into the dark web.


This could be one of the most valuable resources for risk advisors out there.  The number of times I’ve heard people talking about criminals using expensive, or slow exploits in order to steal users twitter accounts or basic card information.  

Is it worth someone dropping $1500 on an exploit that might work 1% of the time?  Well using this data, you can get a good view of the economics of the situation, and work out just how many people would need to be successfully exploited to break even, and thus the likelihood that an attacker will *rationally* attempt that attack.  Of course, not all attackers are rational, but if you are doing attack trees or other analysis, this kind of data is gold dust for working out what the commercial payoff is for the attacker, and thus the likely cost limitations.


## [PDF: Still Unfit for Human Consumption, 20 Years Later](https://www.nngroup.com/articles/pdf-unfit-for-human-consumption/)

[https://www.nngroup.com/articles/pdf-unfit-for-human-consumption/](https://www.nngroup.com/articles/pdf-unfit-for-human-consumption/)

> Jakob Nielsen first wrote about how PDF files should never be read online in 1996 — only three years after PDFs were invented. Over 20 years later, our research continues to prove that PDFs are just as problematic for users. Despite the evidence, they’re still used far too often to present content online.
> 
> PDFs are typically large masses of text and images. The format is intended and optimized for print. It’s inherently inaccessible, unpleasant to read, and cumbersome to navigate online. Neither time nor changes in user behavior have softened our evidence-based stance on this subject. Even 20 years later, PDFs are still unfit for human consumption in the digital space. Do not use PDFs to present digital content that could and should otherwise be a web page.


The evidence is in, again, and users hate your PDF's, they find them slow, difficult to navigate, inaccessible and confusing.

Where possible, use simple, easy to navigate and easy to read web pages instead.


## [State of AI Report 2020](https://www.stateof.ai/)

[https://www.stateof.ai/](https://www.stateof.ai/)

> The State of AI Report analyses the most interesting developments in AI. We aim to trigger an informed conversation about the state of AI and its implication for the future. The Report is produced by AI investors Nathan Benaich and Ian Hogarth.


There's a lot in here, but two things stood out for me in particular.

The first is the rise in MLOps, as AI and Machine Learning really starts to hit, there's a growing need for people with the skills to not just build these models on their laptops, but to actually run them, at scale, in production, and to ensure that there are repeatable, reliable systems for operating AI subsystems.  I predict that this will grow over the year, there's enough special knowledge within ML to need dedicated operations skills.

Secondly is the rise of "Robotic Process Automation", a technology that I have been pretty caustic about in the past.  Enterprises love RPA, it's a way of getting AI into their systems without needing to invest heavily in AI itself.  I dislike some of the ramifications of most of the RPA implementations that I've seen, but what struck me from this is that most companies that are investing in RPA are doing it in their area of core competency.  So they're not using it to automate the irritating side jobs that frustrate their staff, they're using it to automate the very thing that they do as a company.


## [Compensatory conspicuous communication: Low status increases jargon use - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0749597820303666)

[https://www.sciencedirect.com/science/article/abs/pii/S0749597820303666](https://www.sciencedirect.com/science/article/abs/pii/S0749597820303666)

> Jargon is commonly used to efficiently communicate and signal group membership. We propose that jargon use also serves a status compensation function. We first define jargon and distinguish it from slang and technical language. Nine studies, including experiments and archival data analyses, test whether low status increases jargon use. Analyses of 64,000 dissertations found that titles produced by authors from lower-status schools included more jargon than titles from higher-status school authors. Experimental manipulations established that low status causally increases jargon use, even in live conversations. Statistical mediation and experimental-causal-chain analyses demonstrated that the low status → jargon effect is driven by increased concern with audience evaluations over conversational clarity. Additional archival and experimental evidence found that acronyms and legalese serve a similar status-compensation function as other forms of jargon (e.g., complex language). These findings establish a new driver of jargon use and demonstrate that communication, like consumption, can be both compensatory and conspicuous.


This research, and it's worth reading the full paper if you can, reinforces what I've long believed (which always makes me nervous).

People use jargon and abbreviations more if they feel like they need to project more status than they actually have.  In other words, the worst users of tech jargon are the ones who understand the least.  It takes far more confidence in your abilities and your status with those you are speaking to, to chose to speak simply and plainly.  

What would be interesting as follow on research is to determine whether we judge those who use jargon to have a high status, or whether we all intrinsically know that it's a mask, and that we distrust those who use a lot of jargon.


