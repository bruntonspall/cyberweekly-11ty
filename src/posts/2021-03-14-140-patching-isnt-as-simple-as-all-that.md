---
title: "140 - Patching isn’t as simple as all that"
date: 2021-03-14
description: "I thought that all the kerfuffle over HAFNIUM and Microsoft exchange patching would be mostly over by now, and it turns out I was wrong."
permalink: /patching-isnt-as-simple-as-all-that/
---

I thought that all the kerfuffle over HAFNIUM and Microsoft exchange patching would be mostly over by now, and it turns out I was wrong.

As you’ll see below, Harry contacted me after last week to gently admonish me that patching exchange isn’t quite as simple and easy as I had said.  The forums were filled with people who had applied the patches and it hadn’t quite taken, or where it had removed or conflicted with other customisations on their servers.

It sounds simple when you are a talking head, “patch your servers”, and that really is the right guidance.  But it can sometimes be difficult for organisations to even know which servers they have, what version they are on, and who is actually in charge of patching them.  

Furthermore, the timeline that has come out makes clear that a number of APT groups were exploiting these vulnerabilities well before the announcement came out, so as well as finding all the vulnerable servers and patching the exploit, you also need the capability to search these servers for existing evidence of exploits, reverse shells or other exploits that have been run on them.

In a rare bit of good news however, looking at the numbers released by Microsoft, nearly 80% of the servers worldwide that are running vulnerable versions ahve been patched within the two weeks timeframe.  It wasn’t that long ago that the number 1 exploit every year was a 5 year old flash vulnerability in Internet Explorer that nobody seemed able or willing to patch.  Wannacry style exploits utilising ETERNALBLUE were still doing the rounds months later, so we’ve collectively gotten better at patching over time.

This will continue to rumble on, and of course, there will be more vulnerabilities announced, in more software, and as such, if this was hard work for you and your team, you need to take a break, get some fresh eyes and make an effort to make patching a regular and easy process.

## [Microsoft Exchange & the HAFNIUM Threat Actor](https://blog.joshlemon.com.au/hafnium-exchange-attacks/)

[https://blog.joshlemon.com.au/hafnium-exchange-attacks/](https://blog.joshlemon.com.au/hafnium-exchange-attacks/)

> Do I need to check if my Exchange Server was compromised?
> Yes. Given the first known report of the threat actor abusing the vulnerabilities was in January 2021, and patching wasn't available from Microsoft until the 2nd of March 2021, you need to check if your system was compromised.
> 
> [UPDATED 11/03/21] The team at ESET reported they observed exploitation of the vulnerabilities from the 28th of February 2021 by other threat actors, including, Tick (aka Bronze Butler), LuckyMouse (aka Emissary Panda and APT27), Calypso and the Winnti Group (aka Wicked Panda and APT41). This would have given these threat actors a head start on compromising systems before the patch was released on the 2nd of March 2021.


The timelines on this looks very worrying and suspicious.  Microsoft shares vulnerability information with a select number of security research organisations pretty early on to help ensure that security response can be coordinated.  There’s a good possibility that at least some of these APT’s have managed to get inside access somehow, and that the trade in exploits is still going.

Of course, many of these APT’s may also be running honeypots or other incoming indicators that enabled them to capture and reverse engineer the exploits.

This write up is great by the way.  Lovely succinct and clear.  


## [Repair failed installations of Exchange Cumulative and Security updates - Exchange | Microsoft Docs](https://docs.microsoft.com/en-us/exchange/troubleshoot/client-connectivity/exchange-security-update-issues)

[https://docs.microsoft.com/en-us/exchange/troubleshoot/client-connectivity/exchange-security-update-issues](https://docs.microsoft.com/en-us/exchange/troubleshoot/client-connectivity/exchange-security-update-issues)

> This article describes the methods to verify the installation of Microsoft Exchange Server Cumulative Updates (CUs) and Security Updates (SUs) on your servers, lists known issues that might occur when installing CUs and SUs, and provides resolutions to fix the issues.


Last week I said that patching exchange should be easy.  Harry got in contact to point out that it’s not always as easy as I make it out to be, which is totally fair.  There’s a whole bunch of issues that can arise during patching, and this page lists many of the ways that it can go wrong and how you can fix it (or in some cases avoid the issues)


## [As firms race to patch Microsoft Exchange flaws, security pros brace for ransomware outbreak](https://www.cyberscoop.com/microsoft-exchange-hack-ransomware-patching/)

[https://www.cyberscoop.com/microsoft-exchange-hack-ransomware-patching/](https://www.cyberscoop.com/microsoft-exchange-hack-ransomware-patching/)

> Security analysts also are warning that the flaws could open the pathway for ransomware attacks, meaning that if organizations fail to act now, it could cost them later.
> 
> “Everyone is waiting on the other shoe to drop, which will be ransomware,” said Dmitri Alperovitch, the former chief technology officer of CrowdStrike and executive chairman of Silverado Policy Accelerator. “.... Are we going to have massive exploitations or ransomware campaigns, or are we going to get the majority of companies to patch?”
> 
> To answer that question, some cybersecurity professionals are taking matters into their own hands.
> 
> Over the last several days, Allison Nixon, the chief research officer at cybersecurity consulting firm Unit 221B, rounded up her team to develop a website that would help alert organizations if they’ve been comprised.
> 
> ”One common problem people have in the security research field is that they get this list of victims … as a human being you feel this need to let people know, ‘Some bad thing is happening to you, or there’s something you need to do to avoid a really really bad thing happening to you,’” Nixon said.
> 
> The [Unit 221B website](https://checkmyowa.unit221b.com/) is designed so users can search to see if they are using compromised Exchange servers with Outlook Web Access (OWA) enabled. Users can go to the site, which launched Tuesday, directly from their Exchange server, which will allow Unit 221B to check their IP address against their victim list.


Reinforcement on just how bad this one is going to be.

The [Unit 221B website](https://checkmyowa.unit221b.com/) is a helpful tool to check your organisations vulnerability.  You need to validate your ownership of the server, but otherwise simple and easy way to check whether there is remedial action you need to take.


## [Protecting on-premises Exchange Servers against recent attacks - Microsoft Security](https://www.microsoft.com/security/blog/2021/03/12/protecting-on-premises-exchange-servers-against-recent-attacks/)

[https://www.microsoft.com/security/blog/2021/03/12/protecting-on-premises-exchange-servers-against-recent-attacks/](https://www.microsoft.com/security/blog/2021/03/12/protecting-on-premises-exchange-servers-against-recent-attacks/)

> While this began as a nation-state attack, the vulnerabilities are being exploited by other criminal organizations, including new ransomware attacks, with the potential for other malicious activities.
> This is now what we consider a broad attack, and the severity of these exploits means protecting your systems is critical. While Microsoft has regular methods for providing tools to update software, this extraordinary situation calls for a heightened approach. In addition to our regular software updates, we are also providing specific updates for older and out-of-support software with the intent to make it as easy as possible to quickly protect your business.
> 
> To illustrate the scope of this attack and show the progress made in updating systems, we’ve been working with RiskIQ. Based on telemetry from RiskIQ, we saw a total universe of nearly 400,000 Exchange servers on March 1. By March 9 there were a bit more than 100,000 servers still vulnerable. That number has been dropping steadily, with only about 82,000 left to be updated. We released one additional set of updates on March 11, and with this, we have released updates covering more than 95% of all versions exposed on the Internet


That’s a nearly 80% patch rate in under 2 weeks.  When everyone tells you how bad this is, and how big a deal it’s going to be, it’s worth noting that many people simply have been able to patch within weeks.  

That’s a huge change from a few years ago, where even with some of the worst vulnerabilities, we were not seeing patching applied across estates in that magnitude or velocity.


## [DEARCRY/DOEJOCRYPT: A quick look into this new ransomware](http://blog.reversing.xyz/dearcry.html)

[http://blog.reversing.xyz/dearcry.html](http://blog.reversing.xyz/dearcry.html)

> DEARCRY/DOEJOCRYPT: A quick look into this new ransomware
> 
> DEARCRY is a ransomware that encrypt files using an hardcoded RSA public key. Microsoft is now tracking it with the name DOEJOCRYPT.


Ransomware operators have quickly taken the exchange vulnerabilities from last week and weaponised them.  Microsoft and others are now tracking DEARCRY ransomware droppers coming after exploit through exchange.


## [Jamaica’s Amber Group fixes second JamCOVID security lapse | TechCrunch](https://techcrunch.com/2021/02/22/jamaica-amber-group-jamcovid-security-lapse/?guccounter=1)

[https://techcrunch.com/2021/02/22/jamaica-amber-group-jamcovid-security-lapse/?guccounter=1](https://techcrunch.com/2021/02/22/jamaica-amber-group-jamcovid-security-lapse/?guccounter=1)

> The exposed environmental variables file was found in an open directory on the JamCOVID website. Although the JamCOVID domain appears to be on the Ministry of Health’s website, Amber Group controls and maintains the JamCOVID dashboard, app and website.
> 
> The exposed file contained secret credentials for the Amazon Web Services databases and storage servers for JamCOVID. The file also contained a username and password to the SMS gateway used by JamCOVID to send text messages, and credentials for its email-sending server. (TechCrunch did not test or use any of the passwords or keys as doing so would be unlawful.)
> 
> [...]
> 
> Details of the exposure comes just days after Escala 24×7, a cybersecurity firm based in the Caribbean, claimed that it had found no vulnerabilities in the JamCOVID service following the initial security lapse.
> 
> Escala’s chief executive Alejandro Planas declined to say if his company was aware of the second security lapse prior to its comments last week, saying only that his company was under a non-disclosure agreement and “is not able to provide any additional information.”
> 
> This latest security incident comes less than a week after Amber Group secured a passwordless cloud server hosting immigration records and negative COVID-19 test results for hundreds of thousands of travelers who visited the island over the past year. Travelers visiting the island are required to upload their COVID-19 test results in order to obtain a travel authorization before their flights. Many of the victims whose information was exposed on the server are Americans.


Systems built at speed to attempt to solve complex problems can be difficult to build and secure at scale, but that doesn’t make it ok to make such simple errors on a system that matters as much as this does.  


## [Internet-Scale analysis of AWS Cognito Security [pdf]](https://andresriancho.com/wp-content/uploads/2019/06/whitepaper-internet-scale-analysis-of-aws-cognito-security.pdf)

[https://andresriancho.com/wp-content/uploads/2019/06/whitepaper-internet-scale-analysis-of-aws-cognito-security.pdf](https://andresriancho.com/wp-content/uploads/2019/06/whitepaper-internet-scale-analysis-of-aws-cognito-security.pdf)

> lambda.list_functions(), ​one of the API calls used to enumerate permissions, returns information about all the AWS lambda functions in the AWS account. This information includes the function name and environment variables used to run it.
> Developers commonly use environment variables to store database credentials, API keys, encryption secrets, etc.
> During this research it was possible to identify 1572 lambda functions, which exposed ​at least 78 environment variables


This is a lovely write up of exploiting modern mobile application permissions.  

In short, if you use Amazon Cogito to give your mobile application an AWS key that can access your databases.  But developers often issue keys with more permissions than intended, which reveal far more info than expected.

Of real interest is that the lambda.list_functions returns not just the functions that exist in lambda but also the environment variables.  

There’s lots more examples in the report


## [Security startup Verkada hack exposes 150,000 security cameras in Tesla factories, jails, and more - The Verge](https://www.theverge.com/2021/3/9/22322122/verkada-hack-150000-security-cameras-tesla-factory-cloudflare-jails-hospitals)

[https://www.theverge.com/2021/3/9/22322122/verkada-hack-150000-security-cameras-tesla-factory-cloudflare-jails-hospitals](https://www.theverge.com/2021/3/9/22322122/verkada-hack-150000-security-cameras-tesla-factory-cloudflare-jails-hospitals)

> The hack was apparently relatively simple: the group managed to gain “Super Admin”-level access to Verkada’s system using a username and password they found publicly on the internet. From there, they were able to access the entire company’s network, including root access to the cameras themselves, which, in turn, allowed the group to access the internal networks of some of Verkada’s customers.
> 
> Verkada prides itself on offering internet-connected security cameras, promising a Silicon Valley “software-first approach” to make security “as seamless and modern as the organizations we protect.” The cloud-connected cameras include a slick, web-based interface for companies to monitor their feeds and offer (optional) facial recognition software, too.
> 
> The company has also come under fire in the past for accusations of sexism and discrimination after an incident in 2019 where a sales director used Verkada’s office security cameras to harass female co-workers by secretly photographing and posting pictures of them in a company Slack channel. In response, Verkada’s CEO offered members of the Slack channel a choice between leaving the company or having their stock options cut.


While it’s hard to argue any causation between a horrific attitude in a sales team, and the attention to detail, pride in work and security implementation of a product, but this feels like a correlating factor.  We know that more diverse teams will provide a broader range of experiences that can be bought to product direction, from knowledge of how common harassment is, to wider societal experiences that help you think about possible abuse and misuse in the future.

The security compromise here is laughably bad, and slightly depressing. 


## [Understanding Fake Agile](https://www.forbes.com/sites/stevedenning/2019/05/23/understanding-fake-agile/?sh=644a43ab4bbe)

[https://www.forbes.com/sites/stevedenning/2019/05/23/understanding-fake-agile/?sh=644a43ab4bbe](https://www.forbes.com/sites/stevedenning/2019/05/23/understanding-fake-agile/?sh=644a43ab4bbe)

> The challenge is usually presented as one of “scaling up agile.” The issue here is that if the firm is thinking about " scaling up agile", it is already on the wrong track. The challenge of genuine Agile is how to descale big monolithic, internally-focused systems into tasks that can be run by small self-managing customer-focused teams.
> 
> A particularly worrying variant is the Scaled Agile Framework or SAFe. Essentially this is codified bureaucracy, in which the customer is almost totally absent. It is now pervasive in large firms because it gives the management a mandate to call themselves agile and keep doing what they have always done. Essentially it subordinates the agile teams to the bureaucracy, rather than doing what is necessary to achieve business agility, namely, namely, transform the big monolithic internally-focused systems into arrangements where the budgets, HR, Finance and so on are flexible and externally focused in support the Agile teams in operations. The insignificant role of the customer in the chart above is indicative of the problem.


A lovely overview of Agile from the perspective of the organisation, talking about taking it beyond software development, and the use of "fake-agile".

I like that this also pillories the agile zealots who declare that agile is all about small teams.  If it were that simple, it would be far less common to see failures in agile implementations.  Agile is about understanding your customer (and working out who that actually is), it's about empowered small teams, and it's about the network, ensuring that many small teams can work together.

Agile zealots have told me before that product planning and strategy is "unagile", but that's not true at all.  Knowing what the targets are that your teams need to get to is just as important how your teams get there.  Many agile methodologies focus on the day to day ability to respond to events and context on the ground, but you also need a customer driven, organisationally visible north-star or target for those teams to aim at.


