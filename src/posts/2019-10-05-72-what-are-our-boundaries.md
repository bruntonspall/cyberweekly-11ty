---
title: "72 - What are our boundaries?"
date: 2019-10-05
description: "People get overexcited by the term Zero-Trust networking.  If you read the [BeyondCorp research papers](https://cloud.google.com/beyondcorp/), or read [the excellent book on Zero-Trust Networks (affiliate link)](https://amzn.to/30PTT4C), they really say that it is about a new paradigm of computing, it is about access brokers and identity aware proxies and policy enforcement on access and all that good stuff."
permalink: /what-are-our-boundaries/
---

People get overexcited by the term Zero-Trust networking.  If you read the [BeyondCorp research papers](https://cloud.google.com/beyondcorp/), or read [the excellent book on Zero-Trust Networks (affiliate link)](https://amzn.to/30PTT4C), they really say that it is about a new paradigm of computing, it is about access brokers and identity aware proxies and policy enforcement on access and all that good stuff.

But in reality, Zero Trust is just a recognition that our IT no longer has borders or edges in the way we have traditionally thought.  That thinking pervades almost everything that we do, and it's incredibly difficult to shake off, so we still talk about "our infrastructure", or "the network" as if that's a thing.

And in a modern Zero Trust network, we can see that these things are meaningless, but most of us are using IT systems that have extended away from the corporate controlled network a long time ago.  As soon as we started holding our data on other peoples computers, we extended the "boundary" of our system as a whole.  And for most organisations, that boundary is very fuzzy indeed.  Whether it be the tool that controls our mobile phones, or where we keep our emails, having that datastore held by someone else means that it is generally outside of our visibility.  But attacks on those external tools give attackers the ability to access our data, sometimes without even coming into our "core network", and sometimes because it provides us the keys to get in there legitimately.

Software providers who hold our data, at the moment, have very poor auditing tools.  I've spent some time recently looking at common internet tools, like Github, Trello, Jira and so forth, to see what logs you can get out of those tools.  And while it's increasingly common to get my own user actions log (which of my users logged in and did certain actions), it's incredibly rare to get any logs that tell me what that suppliers systems administrators did, whether there was a new software deployment and so forth.  We also can't get any information on the security of that software supplier, so it's hard to know if they use encryption internally, or how they authenticate their staff.  Many will provide a statement that tells you that they follow good security practice, but without standards and assessments for this stuff, it's really hard to know what that means.

This is generally being recognised, and while I'm not a fan of certification, there are groups like the Cloud Security Alliance, who are looking at these things, and for certain simple cases (such as hosting, as loath as I am to call that simple), there are certificates that hold some meaning in terms of staff access, audit trails and so on.  But for more complex software, such as office productivity suites, HR tooling and so forth, we just haven't caught up yet.  And that means we have to take the security of these tools on trust for the most part.

## [Zelimkhan Khangoshvili’s Murder in Berlin: The Untold Story of a Chechen Jihadist Turned Secret Agent](https://www.thedailybeast.com/zelimkhan-khangoshvilis-murder-in-berlin-the-untold-story-of-a-chechen-jihadist-turned-secret-agent)

[https://www.thedailybeast.com/zelimkhan-khangoshvilis-murder-in-berlin-the-untold-story-of-a-chechen-jihadist-turned-secret-agent](https://www.thedailybeast.com/zelimkhan-khangoshvilis-murder-in-berlin-the-untold-story-of-a-chechen-jihadist-turned-secret-agent)

> “After that,” Levan said, “Zelimkhan developed a conviction that the Georgian authorities were cooperating with the Russians. He didn’t believe he was safe in Georgia anymore. And he was right.”
> 
> Khangoshvili emigrated, first to Ukraine, then to Poland, before winding up in Germany, where he’d been pursuing asylum right up until his untimely demise. Khangoshvili wasn’t just exposed to enemy action from abroad in his final port of exile; he was held under suspicion by the authorities. 
> 
> Since his murder, leaks by German intelligence, no doubt abetted by years of pro-Kremlin disinformation, have variously painted a portrait of a violent minority extremist who got what was coming to him or of a man on the lam from a messy entanglement with organized crime. Khangoshvili’s six-year stint as the valued asset of a European security service, and an indirect source for an American one, counted for nothing.


Quite a sad story, but overall a good long read on a western agent, his exploits and what happened to him in the end.


## [British spy in IRA and 20 others could be charged with Troubles-era crimes - TheGuardian.com](https://www.theguardian.com/uk-news/2019/oct/02/ira-spy-and-20-others-could-be-prosecuted-for-troubles-era-crimes?CMP=share_btn_tw)

[https://www.theguardian.com/uk-news/2019/oct/02/ira-spy-and-20-others-could-be-prosecuted-for-troubles-era-crimes?CMP=share_btn_tw](https://www.theguardian.com/uk-news/2019/oct/02/ira-spy-and-20-others-could-be-prosecuted-for-troubles-era-crimes?CMP=share_btn_tw)

> Sources close to the inquiry have also revealed that its head, Jon Boutcher, the ex-chief constable of Bedfordshire, has had access to all secret briefing papers given to every prime minister from Margaret Thatcher onwards that related to the running of Stakeknife within the IRA.
> 
> Stakeknife stands accused of overseeing the murder of alleged informers within the IRA while at the same time working as one of Britain’s most important spies within the Irish republican movement.


This will be troubling for those trying to run sources today in terrorist or criminal cells.  It's always been the hard "grey" morality of running a source from an intelligence agency.  You can't pretend to be a terrorist, you have to either participate in their activities or you won't be in.  This creates a real problem, because you don't want to encourage or support criminal activities, but at the same time, getting intelligence from the most critical people is a long game, which requires running agents who are engaged in dubious low level activities in the hope that they'll be promoted and turn into a hugely valuable source.

There are supposed to be lots of checks and balances, for example MI5 has a [revealed the existence of a previously classified policy on the limits of criminality](https://www.ipco.org.uk/docs/20180301%20PM%20direction%202.pdf) allowed by it's officers (and presumably condoned by officers of their agents), but the policy itself is classified (somewhat sensibibly, if criminal groups knew what was allowed and what was not allowed, then they could devise tests to find moles).


## [Vulnerabilities exploited in VPN products used worldwide - NCSC](https://www.ncsc.gov.uk/news/alert-vpn-vulnerabilities)

[https://www.ncsc.gov.uk/news/alert-vpn-vulnerabilities](https://www.ncsc.gov.uk/news/alert-vpn-vulnerabilities)

> The NCSC is investigating the exploitation, by Advanced Persistent Threat (APT) actors, of known vulnerabilities affecting Virtual Private Network (VPN) products from vendors Pulse secure, Palo Alto and Fortinet.
> 
> This activity is ongoing, targeting both UK and international organisations. Affected sectors include government, military, academic, business and healthcare. These vulnerabilities are well documented in open source.


I suspect this might be actors exploiting the [VPN bypasses raised at DefCon](https://i.blackhat.com/USA-19/Wednesday/us-19-Tsai-Infiltrating-Corporate-Intranet-Like-NSA.pdf) which I commented on back in [Cyberweekly #65](https://cyberweekly.net/how-much-privacy-do-we-expect).  All of these exploits are patched, and patching your VPN appliances should be a high priority consideration in your security program.


## [Did the government kill off the Oligopoly or just send it back to the (US) cloud?](https://diginomica.com/did-government-kill-oligopoly-or-just-send-it-back-us-cloud)

[https://diginomica.com/did-government-kill-oligopoly-or-just-send-it-back-us-cloud](https://diginomica.com/did-government-kill-oligopoly-or-just-send-it-back-us-cloud)

> Over the past decade or so the government has been very vocal about introducing new mechanisms to diversify the supplier base and break up the old Oligopoly (1.0) of outsourcers, SIs and consultancy firms. 
> 
> Procurement frameworks such as G-Cloud, stricter ‘red lines’, and ambitious SME spend targets were all introduced a number of years ago and have since been touted by politicians and senior civil servants as a way of supporting UK business and breaking up the stranglehold of larger suppliers in Whitehall. 
> 
> However, the data, and the perception of those working in industry and in government, is that this isn’t being followed through with any significant spend (at least, not in the way that it used to be) in comparison to the money being spent with AWS, as well as Microsoft and GCP. 


I'm torn on this report, because it has a clickbait headline, and makes a pretty fundamental mistake in it's comparison, but I think it's interesting reading regardless.

The main issue here is the conflation of hosting with managed IT services.   The Oligopoly, as Liam Maxwell and Mike Bracken of GDS used to refer to them, is the collection of the big Systems Integrators, companies like CGI, Fujitsu, ATOS, Dell and others who did the majority of IT contracts for Government for so long.

While it's perfectly possible to buy server hosting from the old Oligopoly, very few people did.  Instead they purchased "Systems", that could cover hosting, networking, wifi in buildings, support desks, internet connectivity, application support and all kinds of things.  The reason they are called Systems Integrators is that you buy a single large contract for, what is in essence an IT-department-in-a-box, and htey subcontract all the individual bits and provide you with a single view of the entire IT estate.  Except that they didn't. In many cases, the department didn't know what to buy, didn't know how to buy it, and trusted that the SI would make good choices.  They often also added restrictive language to the contract, ensuring that the IT couldn't be changed, and putting unnecessary demands on the SI teams delivering the kit.  I'm not defending the SI's here, but I don't think even with the best will in the world, they couldn't have delivered under those terms.

The modern cloud suppliers are totally different.  Because they are self-service, API and Web driven dashboards, they don't wrap the services up, they explicitly expose those services, allowing departments to build on top of them.  Within the subset of IT that is "cloud hosting", it might be easy to suggest that AWS, Google Compute and Azure are winning the majority of contracts, but that's still an unwrapped service.  There is a lot of money to be made by Small and Medium Enterprises (SME's) in providing the development, build and operation of services on top of those cloud hosting platforms.


## [State of Ransomware in the U.S.: 2019 Report for Q1 to Q3 | Emsisoft | Security Blog](https://blog.emsisoft.com/en/34193/state-of-ransomware-in-the-u-s-2019-report-for-q1-to-q3/)

[https://blog.emsisoft.com/en/34193/state-of-ransomware-in-the-u-s-2019-report-for-q1-to-q3/](https://blog.emsisoft.com/en/34193/state-of-ransomware-in-the-u-s-2019-report-for-q1-to-q3/)

> In the first nine months of 2019, at least 621 government entities, healthcare service providers and school districts, colleges and universities were affected by ransomware. The attacks have caused massive disruption: municipal and emergency services have been interrupted, medical practices have permanently closed, ER patients have been diverted, property transactions halted, the collection of property taxes and water bills delayed, medical procedures canceled, schools closed and data lost.
> 
> [...]
> 
> Trends
> 
> Attacks via MSPs on the rise: Cybercriminals are increasingly targeting software commonly used by MSPs and other third-party service providers. In such attacks, multiple customers of the MSP or service provider can be simultaneously hit, as was the case in the August incident in which 22 cities and towns in Texas were impacted.
> 
> Ransom demands get bigger: The average ransom demand has continued to increase in 2019. Like other businesses, criminal enterprises seek to maximize their profits and charge as much as they can for their “services.” If one organization is willing to pay to $500,000, the next may be willing to pay $600,000.
> 
> Cyber insurance: Insured entities may be more likely to pay demands which results in ransomware being more profitable than it otherwise would be which serves incentivize further attacks. See ProPublica’s report The Extortion Economy: How Insurance Companies Are Fueling a Rise in Ransomware Attacks.


Ransomware is going to continue to grow.  The attacks via Managed Service Providers (MSP) makes sense, because it's far more profitable to target a MSP, not ransomware them, but use their network to attack all of their clients. 

We have no good way of assessing how good an MSP is at security, of course they will all show their ISO27001 certificates and so on, but you don't know how much separation there is in their systems, and what changes they will make over time.


## [MyPayrollHR CEO Arrested, Admits to $70M Fraud — Krebs on Security](https://krebsonsecurity.com/2019/09/mypayrollhr-ceo-arrested-admits-to-70m-fraud/)

[https://krebsonsecurity.com/2019/09/mypayrollhr-ceo-arrested-admits-to-70m-fraud/](https://krebsonsecurity.com/2019/09/mypayrollhr-ceo-arrested-admits-to-70m-fraud/)

> “While stating that MyPayroll was legitimate, he admitted to creating other companies that had no purpose other than to be used in the fraud; fraudulently representing to banks and financing companies that his fake businesses had certain receivables that they did not have; and obtaining loans and lines of credit by borrowing against these non-existent receivables.”
> 
> “Mann estimated that he fraudulently obtained about $70 million that he has not paid back. He claimed that he committed the fraud in response to business and financial pressures, and that he used almost all of the fraudulently obtained funds to sustain certain businesses, and purchase and start new ones. He also admitted to kiting checks between Bank of America and Pioneer [Savings Bank], as part of the fraudulent scheme.”


I thought I'd covered this a few weeks ago when the story first broke, but I can't find a record of it.  Apologies if that's the case.

I thought this was an interesting story, when the funds were frozen and companies payroll systems clawed back money from staff, everyone smelt a rat, but I don't think we were expecting anything quite like this.

I don't really understand the motive here, Mann claims that he fraudulently took the money in order to fund his other companies, but I thought from this filing that his other companies were all fraudulent?

The interesting question for me, is that as a user of SaaS software, what possible protections would you have against this kind of thing?  I mean, you could assume that you only trust big players, but the monthly payroll that went through MyPayrollHR was $26m, so that's not a tiny company.  I'm sure that you can get insurance against this sort of thing, so that you can manage payroll for your staff without interruption, but I'm not sure what else you could do in this case.


## [Incident report on the breach of the Australian National University's administrative systems [pdf]](http://imagedepot.anu.edu.au/scapa/Website/SCAPA190209_Public_report_web_2.pdf)

[http://imagedepot.anu.edu.au/scapa/Website/SCAPA190209_Public_report_web_2.pdf](http://imagedepot.anu.edu.au/scapa/Website/SCAPA190209_Public_report_web_2.pdf)

> I have made this report public because it contains valuable lessons not just for ANU, but for all Australian organisations who are increasingly likely to be the target of cyber attacks. It is confronting to say this, but we are certainly not alone, and many organisations will already have been hacked, perhaps without their knowledge. I hope this report will help them protect themselves, and their data and their communities.
> 
> As I said in my statement on 4 June 2019, the perpetrators of our data breach were extremely sophisticated. This report details the level of sophistication, the likes of which has shocked even the most experienced Australian security experts.


This is an amazing report, and a great read that I strongly recommend.  It's worth pointing out that this is what a "high sophistication" attack looks like, and there's good tradecraft outlined here, primarily in terms of defining command and control channels, slow network mapping and the use of a variety of tools to bypass typical security protections.  However I'm not convinced that this is the most sophisticated, many of these actions could have been caught by some of the simpler defences being in place.  It's interesting to note that legacy systems that are unmaintained and not centrally managed are corners where the attacker tried to hide.


## [docs/in-toto-spec.md at v0.9 · in-toto/docs](https://github.com/in-toto/docs/blob/v0.9/in-toto-spec.md)

[https://github.com/in-toto/docs/blob/v0.9/in-toto-spec.md](https://github.com/in-toto/docs/blob/v0.9/in-toto-spec.md)

> While we provide auditability properties so third parties can study and assess the steps of the supply chain to ensure that defenders follow best practices regarding software quality, we do not enforce any specific set of rules. For example, it is possible to configure the supply chain layout so that no code review is performed and a package is built on an untrusted server --- which is an incredibly insecure configuration. While this may be visible to users installing the software, in-toto's role is not to judge or block layouts that are insecure.


In-toto, which I found via a [review of the academic paper about it by the excellent The Morning Paper](https://blog.acolyer.org/2019/10/02/in-toto/), is a lovely idea.

The description as "securing the end to end delivery pipeline" which is aimed to solve supply chain security for software is however much overstated.  What it does is give transparency and auditability of the supply chain.  You can look at the in-toto description of the supply chain for software as a service, software packages or other software and use that to make risk based judgements on how secure the tool is.  For example, you can verify that checkins are all signed by developers, or that the build was built by an authorised build server.

There are a lot of trust points in this system though, you are reliant on developers keeping their private keys secure, on servers being configured appropriately and so on.  As is almost always the case, a lot of the security properties are reliant on the cryptographic keys being managed in a secure way, and that's rarely true for many systems.

For audit purposes, it's a nice idea.  It would be interesting to take a significant project, something built on several frameworks, for example a Rails project using a number of ruby libraries or a major Java SpringFramework project and try to work out the number of transitive dependencies and how much confidence you can actually build.


## [NCSC Cyber Threat Trends Report: Analysis of attacks across UK industries | Digital Shadows](https://www.digitalshadows.com/blog-and-research/ncsc-cyber-threat-trends-report-analysis-of-attacks-across-uk-industries/)

[https://www.digitalshadows.com/blog-and-research/ncsc-cyber-threat-trends-report-analysis-of-attacks-across-uk-industries/](https://www.digitalshadows.com/blog-and-research/ncsc-cyber-threat-trends-report-analysis-of-attacks-across-uk-industries/)

> The first thing the NCSC chose to highlight in their report was the observed attacks against Office 365, Microsoft’s cloud services suite. According to Microsoft, there are over 155 million Office 365 business users as of 2018, a massive attack surface for a single service. When you combine that with the fact that passwords get reused all the time—maybe even for Active Directory integration (O365 makes this easy for Windows users for obvious reasons)—it’s no wonder threat actors see it as an appealing target.
> 
> The NCSC rightfully points out that because these services are cloud-based, and therefore accessible via the open Internet, attacks can be carried out at a much higher scale across the globe than previous on-premises infrastructure services allowed. Accessibility, in this case, puts defenders on their heels. The techniques observed being used are common ones as well: The NCSC highlights password spraying and credential stuffing as the main two attacks against Office 365 logins.
> 
> [...]
> 
> Additionally, even though we’re talking about a cloud service that’s not technically a part of your infrastructure, the compromised account for a service like Office 365 can lead to actual network intrusions. The NCSC has observed this scenario with VPN accesses. Users or administrators may set a VPN login to match that of the internal Active Directory, or another service to make it more convenient remembering a new set of credentials. Password reuse is an all too common technique used by attackers to get access to specific services


There is a lot of good stuff in this excellent blog post from Digital Shadows.

The idea that having moved to Office 365 means that you are more likely to be attacked by a wider variety of people, because your authentication service is now on the internet somewhat disuades from the fact that pretty much every business has to be online in some way, shape or form now.  Businesses that haven't gone to a cloud hosted email solution tend to have some form of remote access solution anyway, and many of those are far more poorly protected.

The reason that the most common attacks on Office 365 is password spraying (trying the top 5 most common passwords on thousands of accounts) and credential stuffing (trying to reuse passwords found in other breaches) are so common is because typical brute forcing, which probably works against your remote VPN or ExchangeOnline, don't work against Office 365, and so attackers have changed tactics.

On the VPN credential reuse thing, I'm a bit nervous of saying "[Office 365] is not technically a part of your infrastructure".

Cloud services that conduct authorisation and authentication for your staff, that contain the passwords and accounts, and that send and receive emails and documents on your behalf are very much part of your infrastructure.  The idea that Cloud services such as Office 365 and Google Suite are "outside" is broken thinking from the era of security as boundary control.  Even Microsoft's own security guidance is at pains to remind people that in a cloud enabled world, identity is the core layer of your infrastructure, and that makes most Office 365 installations the heart of your infrastructure.


## [How we breached a corporate network via Citrix XenMobile](https://medium.com/dxwcyber/how-we-breached-a-corporate-network-via-citrix-xenmobile-934a2a0585a1)

[https://medium.com/dxwcyber/how-we-breached-a-corporate-network-via-citrix-xenmobile-934a2a0585a1](https://medium.com/dxwcyber/how-we-breached-a-corporate-network-via-citrix-xenmobile-934a2a0585a1)

> We set up an instance of XenMobile on one of our own virtual machines, and began analysing its behaviour. By running it on our own infrastructure, we could perform tests that would be detected easily if we ran them on the actual target system.
> We found lots of lovely bugs. In fact, we found so many that it was a challenge to find the right ones. But we persevered, and identified several vulnerabilities that could be combined to create a working exploit:
> 
> * We discovered that we could download files containing administrator credentials
> * We discovered that we were able to upload zip files to a specific directory on the webserver, without having to log in
> * We logged in with the administrator credentials from step 1, and found we could unzip these uploaded files to any other directory on the webserver.
> * We uploaded and unzipped files that allowed us to capture the credentials of all user devices connecting to XenMobile


This is a interesting writeup about a red teaming exercise.  Chaining together several bugs to enable complete access to a company using only their remote access solution.

Again, this was about stealing credentials that could then be reused against the core network.  Identity and credentials are probably the most valuable data target for many adversaries, because once you have them, you can impersonate users at will.


