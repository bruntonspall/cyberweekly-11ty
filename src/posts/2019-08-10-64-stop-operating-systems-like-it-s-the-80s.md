---
title: "64 - We need to stop operating IT like it's 1999"
date: 2019-08-10
description: "We see this again and again, but the ransomware attacks on enterprise It estates in local government in the US (which are the ones we know the most about) just shows that many small to medium size organisations still haven't got the memo.  "
permalink: /stop-operating-systems-like-it-s-the-80s/
---

We see this again and again, but the ransomware attacks on enterprise It estates in local government in the US (which are the ones we know the most about) just shows that many small to medium size organisations still haven't got the memo.  

It's easy when you work in digital development to roll your eyes and explain how easy puppet or chef is to configure your AWS servers automatically as configuration as code.  Monzo's response to PIN's being found in their logs was excellent, both in terms of response, but also in terms of managed infrastructure, but they have it easy, with a relatively green field digital system.  Enterprise IT is a whole different ball game for many of these smaller organisations, with deployment of thousands of computers, many with different users and different needs, all using a multitude of different services on the network.  There isn't a lot of developer experience in building enterprise IT wide automation and configuration management.  There are some tools do some of this, but many of the people working in enterprise IT aren't developers, they don't understand program code, and they haven't been given the skills to do the job that's now required of them.

This is a security nightmare, because we know that "devops" and agile give us the ability to make changes more rapidly, more safely and more efficiently.  But without that safety and rapidity, rolling out patches and updates to the corporate estate is slow, painful and prone to failure.  That means that we do it less often, and that leaves a gap into which criminal organisations can slide.

The solution is to take devops and agile principles and apply them to our enterprise IT, ensuring that we have code that describes what our infrastructure and devices should look like, and that we can make changes confidently and quickly.  That's far from easy to actually do, but as I've said in the past, we need to do the hard work to make it simple.

## [Thread by @Foone: "So, Kodak is weird. And a particular way they are weird has to do with the International Fixed Calendar, as developed by Moses Cotsworth in […]"](https://threadreaderapp.com/thread/1151546837578313728.html)

[https://threadreaderapp.com/thread/1151546837578313728.html](https://threadreaderapp.com/thread/1151546837578313728.html)

> This was a secret 1-kiloton test. No one was supposed to know, but Kodak did. They filed a complaint with the Atomic Energy Commission and the National Association of Photographic Manufacturers.
> The AEC's reply was basically "Sorry about that, but we can't tell you where the tests are going to be (They're secret!) and we can't stop the wind from blowing"
> And Kodak's reply was: YOUR TESTS ARE GOING TO COST US MILLIONS IN RUINED FILM, AND WE HAVE LOTS OF LAWYERS.
> So the AEC compromised: Executives of Kodak and other film companies would get Q Clearance (an above-top-secret clearance needed for nuclear weapons matters) and be told ahead of time where tests would be and where the fallout might go/did go.
> So during the cold war, Kodak and other film manufacturers had access to highly secret information (the kind the Soviets would (literally) kill for), in order to ensure their film wouldn't be contaminated by fallout from US tests.


I'm quite taken with the International Fixed Calendar, which I discovered through this thread. This newsletter is sent on 27th July according to the International Fixed Calendar, although that's mostly because we've just finished the month of Sol. Love it!.

Anyway, that aside, this little snippet from one of the most amazing twitter threads I've read in a while just made me stare at the screen wondering "why?" and occasionally "How?".  Kodak was inducted into one of the most secret programs in the world.


## [North Korea took $2 billion in cyberattacks to fund weapons program: U.N. report - Reuters](https://www.reuters.com/article/us-northkorea-cyber-un/north-korea-took-2-billion-in-cyberattacks-to-fund-weapons-program-u-n-report-idUSKCN1UV1ZX)

[https://www.reuters.com/article/us-northkorea-cyber-un/north-korea-took-2-billion-in-cyberattacks-to-fund-weapons-program-u-n-report-idUSKCN1UV1ZX](https://www.reuters.com/article/us-northkorea-cyber-un/north-korea-took-2-billion-in-cyberattacks-to-fund-weapons-program-u-n-report-idUSKCN1UV1ZX)

> “Democratic People’s Republic of Korea cyber actors, many operating under the direction of the Reconnaissance General Bureau, raise money for its WMD (weapons of mass destruction) programmes, with total proceeds to date estimated at up to two billion US dollars,” the report said.
> 
> North Korea is formally known as the Democratic People’s Republic of Korea (DPRK). The Reconnaissance General Bureau is a top North Korean military intelligence agency.
> 
> The experts said they are investigating “at least 35 reported instances of DPRK actors attacking financial institutions, cryptocurrency exchanges and mining activity designed to earn foreign currency” in some 17 countries.
> 
> The U.N. experts said North Korea’s attacks against cryptocurrency exchanges allowed it “to generate income in ways that are harder to trace and subject to less government oversight and regulation than the traditional banking sector.”


At this point, it's probably worth noting that DPRK is acting like a very very well funded cyber criminal organisation.  It is interested in profit, seeking to gain money and funnel it into state based programs to avoid the sanctions that prevent it selling it's normal exports.

However, much like many cyber enabled criminal organisations, it's really hard to work out how states are going to react to this. DPRK doesn't exactly have a large online economy or digitally connected populous, so therefore striking back with offensive cyber wont have much effect.  Diplomatic and economic sanctions are what states are trying, but it doesn't seem to be working.  It's unclear what will work to prevent the attacks starting, but one thing is clear, many of the activities can be stopped by the same techniques we use to stop criminal activity, that is to say, being a smaller target that's more highly defended.


## [Black Hat: GDPR privacy law exploited to reveal personal data - BBC News](https://www.bbc.co.uk/news/technology-49252501)

[https://www.bbc.co.uk/news/technology-49252501](https://www.bbc.co.uk/news/technology-49252501)

> Overall, of the 83 firms known to have held data about his partner, Mr Pavur said:
> 
> 24% supplied personal information without verifying the requester's identity
> 16% requested an easily forged type of ID that he did not provide
> 39% asked for a "strong" type of ID
> 5% said they had no data to share, even though the fiancee had an account controlled by them
> 3% misinterpreted the request and said they had deleted all her data
> 13% ignored the request altogether


This should be no surprise to anyone who looked at processes for answering GDPR queries in organisations.  Getting an online proof of identity is already hard enough, and now you've got to confirm that it matches what you already hold, before attempting to respond, all while watching the clock on how long you have to answer the query.

What scares me here, is the 21%, that's around 1/5 companies that either said they had no data, ignored the request or worse, the 3% who just deleted the account in response to a Subject Access Request.  If 1/5 companies are essentially flouting the law, what does that actually mean for the efficacy of the law?

(I'm also fascinated that 3% of the 83 companies is almost exactly 2.5 companies, so did half a company delete the data?)


## [The Security Impact of HTTPS Interception [pdf]](https://jhalderm.com/pub/papers/interception-ndss17.pdf)

[https://jhalderm.com/pub/papers/interception-ndss17.pdf](https://jhalderm.com/pub/papers/interception-ndss17.pdf)

> Security companies are acting negligently. Many of the
> vulnerabilities we find in antivirus products and corporate
> middleboxes— such as failing to validate certificates and
> advertising broken ciphers— are negligent and another data
> point in a worrying trend of security products worsening
> security rather than improving it


A old, but great academic study that included Mozilla, Google, Cloudflare representatives reviewing how much TLS traffic is intercepted by either a corporate proxy or local antivirus.

They find, disappointingly, that lots of "security products" actively make things worse, by downgrading the browsers built in TLS support and adding flaws and vulnerabilities.


## [FTC Imposes $5 Billion Penalty and Sweeping New Privacy Restrictions on Facebook | Federal Trade Commission](https://www.ftc.gov/news-events/press-releases/2019/07/ftc-imposes-5-billion-penalty-sweeping-new-privacy-restrictions)

[https://www.ftc.gov/news-events/press-releases/2019/07/ftc-imposes-5-billion-penalty-sweeping-new-privacy-restrictions](https://www.ftc.gov/news-events/press-releases/2019/07/ftc-imposes-5-billion-penalty-sweeping-new-privacy-restrictions)

> Facebook, Inc. will pay a record-breaking $5 billion penalty, and submit to new restrictions and a modified corporate structure that will hold the company accountable for the decisions it makes about its users’ privacy, to settle Federal Trade Commission charges that the company violated a 2012 FTC order by deceiving users about their ability to control the privacy of their personal information.


That's a lot of money, although against a revenue in the second quarter of the year of $16.89 billion (for an estimated $65 billion a year annual income) it's still affordable for the company.  


## [The State of Container and Kubernetes Security Spring 2019](https://www.stackrox.com/kubernetes-adoption-and-security-trends-and-market-share-for-containers/)

[https://www.stackrox.com/kubernetes-adoption-and-security-trends-and-market-share-for-containers/](https://www.stackrox.com/kubernetes-adoption-and-security-trends-and-market-share-for-containers/)

> Container security still a big concern
> Inadequate investment in security dominates the list of concerns users have about their company’s container strategy. The increase in both this worry and the concern that the strategies are not detailed enough provide clear signals that people are thinking more comprehensively about their use of containers. These findings show maturation in how people are using containers and the importance of containerized apps in their business.


Some 34% of respondents have no container security strategy (That's people who responded non-existent or planning).  There wasn't a response for "It's part of another strategy".

Interestingly, people are most worried about misconfiguration when asked what they are worried about (60% of respondents, compared to 11% worrying about attacks generally, and 29% worrying about container vulnerabilities) however when asked to rate the importance of container security capabilities, over 75% went for vulnerability management, as compared to just 66% asking for configuration management.


## [North Carolina county lost $1.7 million in email scam](https://statescoop.com/north-carolina-cabarrus-county-lost-1-7-million-email-scam/)

[https://statescoop.com/north-carolina-cabarrus-county-lost-1-7-million-email-scam/](https://statescoop.com/north-carolina-cabarrus-county-lost-1-7-million-email-scam/)

> Cabarrus County was ensnared last November when online scammers posed as Branch and Associates, a firm based in Roanoke, Virginia, hired as the general contractor for a new high school. The scammers emailed Cabarrus County Schools with a request to alter details on the electronic funds transfer account the county had set up to pay its contractor, according to a county government report. Unaware of the ruse, county officials followed their standard processes for such a request, including an updated EFT form and bank documentation. The scammers returned the signed forms as requested on Dec. 4, and the county wired a $2.5 million payment a few weeks later to an account at Bank of America.
> 
> The county discovered something was amiss on Jan. 8, when the actual Branch and Associates called about a missing payment for $2.5 million. Cabarrus County school officials notified the county sheriff’s office, which in turn brought in the FBI to investigate. The county also notified its bank, SunTrust, and filed an insurance claim.


This is a great example of a typical BEC fraud.  Invoicing processes are highly vulnerable to fraud changes.

the interesting question for me here, is what bank account did the money go to?

If you are a good fraudster, and were sensible, the destination account was the subject of another fraud, probably one of those nigerian prince scams.  "You'll be wired $2.5 million, you need to send us $2.1 million of it, and you can keep $400,000 of it".


## [How AT&T Insiders Were Bribed to 'Unlock' Millions of Phones | WIRED](https://www.wired.com/story/att-insiders-bribed-unlock-phones/)

[https://www.wired.com/story/att-insiders-bribed-unlock-phones/](https://www.wired.com/story/att-insiders-bribed-unlock-phones/)

> According to the lawsuit, AT&T was tipped off to their activity in September 2013, when IT staff noticed a surge in unlock requests, which “occurred within milliseconds of one another, suggesting the use of an automated or scripted process.” The lawsuit was halted a month after it was filed, when some of the defendants learned they were “targets of a long-running federal criminal investigation” that had already been underway for more than two years.
> 
> LOUISE MATSAKIS COVERS AMAZON, INTERNET LAW, AND ONLINE CULTURE FOR WIRED.
> Federal investigators were after more than a handful of call center workers. They were looking for the operation’s leaders.


Fascinating insight into insider threat.  We don't often see real insider threat activities, either because it's far more rare than security professionals would have you believe, or because it's happening without being detected in many cases.

The length of time this investigation was going on tells you something about how hard it was to actually track down the targets, however it also raises the question of how long they were allowed to run their scam, and potentially affect individual's lives, while trying to chase the ultimate perpetrators.


## [DOD continues to buy products it knows have cybersecurity vulnerabilities](https://www.fedscoop.com/defense-department-known-cyber-vulnerabilities-lenovo-lexmark-gopro/)

[https://www.fedscoop.com/defense-department-known-cyber-vulnerabilities-lenovo-lexmark-gopro/](https://www.fedscoop.com/defense-department-known-cyber-vulnerabilities-lenovo-lexmark-gopro/)

> The equipment was purchased years — or in some cases more than a decade — after the cybersecurity vulnerabilities were known.
> 
> “If the DoD continues to purchase and use [commercial off the shelf] items without identifying, assessing, and mitigating known vulnerabilities associated with [commercial off the shelf] items, missions critical to national security could be compromised,” the report states.
> 
> Threats from China
> Lexmark printers and Lenovo computers are manufactured in China and have connections to state intelligence agencies, according to the report. With growing fears of Chinese counterintelligence and great power competition, the connections to China add to the threats the vulnerabilities pose.


It's very disappointing to see that the focus of the oversight report concentrating on devices of chinese manufacture rather than on the fact that some of these devices haven't been patched in nearly a decade!

[The report itself](https://www.oversight.gov/sites/default/files/oig-reports/DODIG-2019-106.pdf) (interesting but long) goes into far more detail, covering the fact that when people purchase tools on their "Government Procurement Card", these purchases are not tracked anywhere, and as such are not patched, managed, maintained (as well as not being subject to the controls that would advise against purchasing stuff with known vulnerabilities)


## [we weren’t storing some customers’ PINs correctly - Monzo](https://monzo.com/blog/2019/08/05/weve-fixed-an-issue-storing-some-customers-pins)

[https://monzo.com/blog/2019/08/05/weve-fixed-an-issue-storing-some-customers-pins](https://monzo.com/blog/2019/08/05/weve-fixed-an-issue-storing-some-customers-pins)

> And as your bank, we keep a record of your PIN so we can check you’ve entered it correctly. We store them in a particularly secure part of our systems, and tightly control who at Monzo can access them. 
> 
> On Friday 2nd August, we discovered that we’d also been recording some people’s PINs in a different part of our internal systems (in encrypted [log files](https://en.wikipedia.org/wiki/Log_file)). Engineers at Monzo have access to these log files as part of their job.


(Joel) Mistakes happen. While not ideal (when is ever lapse ideal?) Monzo's response and transparency should be somewhat commended.

My main takeaway has little to do with this incident or even Monzo: while it is unclear what the intended log data is (in which the unencrypted/hashed PINs were found) the fact they were encrypted and subject to role-based access control already is good work.

How often are log files rarely considered for documentation let alone review for sensitivity and encryption? Security should not be responsive. If you take the default position of encryption should always be enabled unless there are good reasons why it can't and role-based access controls applied _regardless of content_ we limit the damage of accidental leakages - for example, when your content delivery logs for your website happens to be logging form content when you didn't realise, but you never opted to store them in an encrypted fashion as no one considered them to be sensitive in any way.


## [De-risking custom technology projects: A handbook for state budgeting and oversight - 18F](https://github.com/18F/technology-budgeting/blob/master/handbook.md)

[https://github.com/18F/technology-budgeting/blob/master/handbook.md](https://github.com/18F/technology-budgeting/blob/master/handbook.md)

> Unlike bridges or other capital infrastructure projects, custom software is never "done," so it’s important to plan for it to be modified continuously. That way it can serve today’s agency needs, not yesterday’s.
> 
> For small systems, this may require adding one or fewer FTEs to the agency’s staff of software developers. For large, flagship systems, this may require procuring a team of developers to continually develop and maintain the software.
> 
> Software maintenance is sometimes budgeted for as if it is a different activity than initially building software, but that is a mistake. Maintaining software should mean simply continuing to modify it in response to identified user needs, which change continuously along with laws, regulations, policies, best practices, and technology. This requires the same skill sets, methodology, and tasks as building a system in the first place. A proposal to transition software development into an "operations and maintenance" ("O&M") phase should be seen as a red flag,


There's a lot in this document that I'd love to unpick, but this stood out to me today.  

Security people often view agile as "seat of your pants", which results in poor code, poor design and poor security.  Of course, in traditional software development, being given a system that is poorly coded and full of vulnerabilities is a security nightmare, because that system is going to be a pain to maintain.

Most security issues with existing systems comes not from poor code in the building of the system, but from the lack of ability to modify and maintain the system over time.  A system that undergoes a pentest, fails laughably, but has a team that can fix it around for the next 6 months is hugely better than a system that only has a few low to medium vulnerabilities but doesn't have any maintenance.


## [A tale of two cities: Why ransomware will just get worse | Ars Technica](https://arstechnica.com/information-technology/2019/06/a-tale-of-two-cities-why-ransomware-will-just-get-worse/)

[https://arstechnica.com/information-technology/2019/06/a-tale-of-two-cities-why-ransomware-will-just-get-worse/](https://arstechnica.com/information-technology/2019/06/a-tale-of-two-cities-why-ransomware-will-just-get-worse/)

> Ransomware succeeds, in short, because organizations are still running their IT operations like it's 1999 and because the products they buy are too difficult for underfunded and undermanned organizations to properly configure and maintain. Until there's a significant change in how cities, towns, and companies buy and run IT, there will continue to be Baltimores and Riviera Beaches. And ransomware operators will continue to rake in the rewards of a fundamentally broken way of using technology.


Strong words as to why ransomware works.  So much of the IT operations of these cities is baked into old ways of working, and criminals have worked that out and are taking advantage of it.


