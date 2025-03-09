---
title: "51 - What does cyberwar actually mean?"
date: 2019-05-11
description: "The IDF tweeted that they had carried out a missile attack on a Hamas cyber offensive operations team, and it made me ponder the militarisation of cyber warfare."
permalink: /what-does-cyberwar-actually-mean/
---

The IDF tweeted that they had carried out a missile attack on a Hamas cyber offensive operations team, and it made me ponder the militarisation of cyber warfare.

A lot of infosec people tweeting about the IDF attack suggested that they were shocked that IDF could respond to a cyber attack with a kinetic reaction.  I don't think that this is terribly surprising, that the location of the cyber offensive team is a valid military target given that they were a military team operating in a militarised environment.

There's a set of thinking about what makes a valid military target that can follow from this.  Do we think that the NSA's Fort Meade would be a legitimate target of war?  Lots of people there wear fatigues on a regular basis and it is a military base after all.  The reason we don't think about it is that cyber attacks are carried out at a distance.  Mostly, we don't worry that Ft Meade, or the Donut, or other intelligence buildings are a target because they are far away, and most of the major military actors don't have missiles, bombers or other technology that can reach such a target unimpeded.

But out in the theatre of war between two states, some intelligence operatives do their jobs, intercepting enemy lines of communication and applying the intelligence product to advise friendly troops appropriately.  We generally don't have an issue with the idea that they would be valid targets during war, so why was this tweet such an issue?

The unanswered question that this lies on us is exactly what level of military intervention is acceptable or appropriate if we do decide that offensive cyber operation teams within military units are valid targets.  Can cyber force only be responded to with cyber force, or will next time we see a major player using cyber force on a major western nation will we see a military intervention as a response?

Additionally, most of us who work in cybersecurity are not part of the armed forces, and would not consider ourselves valid military targets, but this event reminds us that for military thinkers, cyber is just another domain of warfare, and that they are happy with the militarisation of the field.

## [Security baseline (DRAFT) for Windows 10 v1903 and Windows Server v1903](https://blogs.technet.microsoft.com/secguide/2019/04/24/security-baseline-draft-for-windows-10-v1903-and-windows-server-v1903/)

[https://blogs.technet.microsoft.com/secguide/2019/04/24/security-baseline-draft-for-windows-10-v1903-and-windows-server-v1903/](https://blogs.technet.microsoft.com/secguide/2019/04/24/security-baseline-draft-for-windows-10-v1903-and-windows-server-v1903/)

> Recent scientific research calls into question the value of many long-standing password-security practices such as password expiration policies, and points instead to better alternatives such as enforcing banned-password lists (a great example being Azure AD password protection) and multi-factor authentication. While we recommend these alternatives, they cannot be expressed or enforced with our recommended security configuration baselines, which are built on Windows’ built-in Group Policy settings and cannot include customer-specific values.
> 
> This reinforces a larger important point about our baselines: while they are a solid foundation and should be part of your security strategy, they are not a complete security strategy. In this particular case, the small set of ancient password policies enforceable through Windows’ security templates is not and cannot be a complete security strategy for user credential management. Removing a low-value setting from our baseline and not compensating with something else in the baseline does not mean we are lowering security standards. It simply reinforces that security cannot be achieved entirely with baselines.


Baselines aren’t your strategy.  This is important to be said, because people keep trying to make the baselines high enough to replace any local thinking.  This is the same as baseline risk assessments.  If you are using AWS, there’s a simple baseline of security features that you should enable without needing to do a risk assessment.  You can then do a risk assessment on top of that for the specifics of your project if needed, but that baseline ensures that you don’t waste time on simple questions that have a well known basic answer


## [FBI Budget Request for Fiscal Year 2020 — FBI](https://www.fbi.gov/news/testimony/fbi-budget-request-for-fiscal-year-2020-1)

[https://www.fbi.gov/news/testimony/fbi-budget-request-for-fiscal-year-2020-1](https://www.fbi.gov/news/testimony/fbi-budget-request-for-fiscal-year-2020-1)

> The FY 2020 budget request proposes a total of $9.31 billion in direct budget authority to carry out the FBI’s national security, criminal law enforcement, and criminal justice services missions. The request includes a total of $9.26 billion for salaries and expenses, which will support 35,558 positions (13,201 special agents, 3,115 intelligence analysts, and 19,242 professional staff), and $51.9 million for construction.
> 
> As a result of this budget being formulated before the Consolidated Appropriations Act, 2019, was passed, it was built utilizing the prior year enacted level as a starting point. The request does, however, include six program enhancements totaling $144.9 million. These enhancements are proposed to meet critical requirements and close gaps in operational capabilities, including: $70.5 million to enhance cyber investigative capabilities; $18.3 million to mitigate threats from foreign intelligence services; $16.6 million to support the National Vetting Center, $18.2 million to target and disrupt transnational organized crime financial and Darknet networks; $4.2 million to increase the capacity to perform National Instant Criminal Background Check System (NICS) services; and $17.2 million to enhance the FBI’s ability to render safe a weapon of mass destruction.


The FBI spends a *lot* of money.  I'm a bit confused by the term "salaries and expenses" which I assumed covered expenses like travel and hotels, but the implication of the extra program enhancements means that programme funding might be included in that budget as well.

Anyway, $18 million on mitigating threats from foreign intelligence services feels like a lot of money.  I wonder where they are investing it, what threats they are worried about and what that money will buy?  It's almost as much money as they're going to spend to render safe a weapon of mass destruction.


## [Disclosure and Barring Service: progress review - Committee of Public Accounts - House of Commons](https://publications.parliament.uk/pa/cm201719/cmselect/cmpubacc/2006/200606.htm)

[https://publications.parliament.uk/pa/cm201719/cmselect/cmpubacc/2006/200606.htm](https://publications.parliament.uk/pa/cm201719/cmselect/cmpubacc/2006/200606.htm)

> There are also risks that the DBS and its new contractor may not be able to access systems information. TCS designed the architecture supporting the programme and holds the documentation and codes which the new contractor will need to be able to deliver the services it will inherit. The DBS does not have this knowledge as it was not involved in the detail of the design of the system and failed to act as an ‘intelligent customer’ in its oversight and challenge of TCS as the new system was being delivered. The DBS twice characterised TCS as having been “less than co-operative” when asked to share documentation and information.


This smells terrifying.  The home office is essentially saying that they asked TCS to build the system, they haven't done a good enough job, so they're going to ask them to hand it over to another supplier.  But they don't know anything about the design of the system, about the way it works, and TCS are refusing to hand over documentation and information.

This reminds me a lot of the story of [Hertz suing Accenture](https://www.theregister.co.uk/2019/04/23/hertz_accenture_lawsuit/) which commentators agreed was a sign of poor supplier management.  You can't outsource all of the technical decision making to a supplier and just hope that the project works.  You need to insource at least the technical leadership to make a success of this, and simply handing it to a new supplier isn't going to make any of it better.


## [Ex-Intelligence Analyst Charged With Leaking Information to a Reporter - The New York Times](https://www.nytimes.com/2019/05/09/us/politics/daniel-hale-leak-intercept.html)

[https://www.nytimes.com/2019/05/09/us/politics/daniel-hale-leak-intercept.html](https://www.nytimes.com/2019/05/09/us/politics/daniel-hale-leak-intercept.html)

> Mr. Hale met with the reporter multiple times and communicated using encryption. Prosecutors said that Mr. Hale left the Air Force and was then assigned to the National Geospatial-Intelligence Agency, where he worked as a political geography analyst.
> 
> At the agency, prosecutors said, Mr. Hale printed 36 documents from his Top Secret computer. Mr. Hale provided at least 17 of them to the reporter and The Intercept, which published the documents in whole or in part. Eleven of the published documents were marked as Top Secret or Secret, prosecutors said. The documents appear to be used in Intercept reporting about the military’s use of drones.


This is another leak from a classified source to the Intercept.  Lots of commentators online blaming the Intercept for poor OPSEC practices, but the fault here appears to lie with Mr Hale, who clearly used SMS txts to contact the journalist, and did things like googling the journalists name and the intercept from his classified computer before making the decision to leak.


## [2019 DBIR Results & Analysis | Verizon Enterprise Solutions](https://enterprise.verizon.com/en-gb/resources/reports/dbir/2019/results-and-analysis/)

[https://enterprise.verizon.com/en-gb/resources/reports/dbir/2019/results-and-analysis/](https://enterprise.verizon.com/en-gb/resources/reports/dbir/2019/results-and-analysis/)

> A quick glance at the figures below uncovers two prominent hacking variety and vector combinations. The more obvious scenario is using a backdoor or C2 via the backdoor or C2 channel, and the less obvious, but more interesting, use of stolen credentials. Utilizing valid credentials to pop web applications is not exactly avant garde. 
> 
> The reason it becomes noteworthy is that 60% of the time, the compromised web application vector was the front-end to cloud-based email servers.


The Verizon Databreach Survey is out and it's got a lot of fascinating bits, so it's hard to pick out any specific bit for the newsletter.  This stat however was interesting, that 60% of the time that a company is hacked, it's via the use of stolen credentials applied to a cloud based email server.
The defenses for this are reasonably simple: 2FA for all staff for cloud email accounts will make it significantly harder for attackers (there's another note further down that implies strongly that a lot of the stolen credentials are credential stuffing attacks, which are generally not online attacks).

There's more notes in here that I can cover, public sector breaches are 2.5 times more likely to be undiscovered for years, The spike of breaches that result in 0 financial loss, the relevant note that malware is almost never the initial vector for compromise, but that social or hacking is an initial vector instead.  It's a good report, both in PDF and the online version, so go read it.


## [Thread by @colmmacc: I think right around this minute is just about exactly 5 years since the Heartbleed vulnerability in OpenSSL became public.](https://threadreaderapp.com/thread/1114944298246660100.html)

[https://threadreaderapp.com/thread/1114944298246660100.html](https://threadreaderapp.com/thread/1114944298246660100.html)

> I'd previously worked on OpenSSL things, like Apache's mod_ssl, so then the issue went public ... I was one of the first people paged. I was on the 14th floor of our Blackfoot building.
> It was very very quickly evident that Heartbleed wasn't like other vulnerabilities. Normally there's a window between going public and exploits being crafted, but heartbleed was so easy to exploit that it took just minutes of poking around.
> Heartbleed was a memory disclosure vulnerability, which in theory is supposed to be less significant than a remote execution vulnerability, but this was scarier than any bug I'd ever seen. 


A quick reminder, AWS was able to discover the vulnerability and patch their entire ELB fleet within an hour of the bug being discovered.  GOV.UK was able to patch their entire estate within 2 hours.  How fast could you fix your estate if this happened today?  How confident would you be that you covered the entire estate?


## [Israel Defense Forces on Twitter](https://mobile.twitter.com/idf/status/1125066395010699264?s=21)

[https://mobile.twitter.com/idf/status/1125066395010699264?s=21](https://mobile.twitter.com/idf/status/1125066395010699264?s=21)

> CLEARED FOR RELEASE: We thwarted an attempted Hamas cyber offensive against Israeli targets. Following our successful cyber defensive operation, we targeted a building where the Hamas cyber operatives work. 
> 
> HamasCyberHQ.exe has been removed.


As a tweet, this is an interesting position to take.  The claims in this tweet is that the physical response was a retaliation for the attack in the cyber field is the first time that I'm aware of a national power making the claim for responding to cyber attack with kinetic force.


