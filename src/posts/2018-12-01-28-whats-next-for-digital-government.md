---
title: "28 - Whats next for digital government?"
date: 2018-12-01
description: "This week had a bunch of interesting themes for me, but two in particular stand out."
permalink: /whats-next-for-digital-government/
---

This week had a bunch of interesting themes for me, but two in particular stand out.

Tom Loosemore and Dafydd Vaughan brilliantly explained the journey that digital government has been on and how far we've come.  It's very easy to dwell on the size of the challenge ahead, but let us also acknowledge just how much better it is than it was, and how much better prepared we are for the next steps.

The next steps are clear for Government, in terms of focusing on understanding how to operate services, not just build them, and how we go about funding that.  I think there are radical changes in funding models, but also in Governance, operational modelling and staffing that needs to happen as well when we think about operations rather than just building stuff.  If the strategy in 2013 was to deliver, the strategy in 2018 is not just to deliver, but to ensure that we aren't delivering new legacy.  To ensure that we are able to continue to improve, maintain and operate the things we build.

This conversation wouldn't have been possible in 2013, because there frankly just wasn't enough technical talent in Government to have the conversation with.  Lots of well meaning, hard working individuals, but not enough to form a profession and have a technical conversation that goes beyond simple management, policy and traditional operations.  The rise of the ability to have technical conversations across government, and the disagreements in models that come with that is a welcome challenge in my mind.

That leads me onto the other thing that really caught my eye this week.  GCHQ has published two separate policy pieces, both of which are strongly technical in their arguments.  The declassification and publication of the Equities system, and changing the discussion on lawful interception are both pieces of work that had they happened 5 or 10 years ago, would probably have been couched in non technical terms and discussed in a political arena.  They both have political ramifications and that conversation should happen, but the ability to also have them released in a technical arena means that engagement can be done by technical people in a way that it couldn't have before.

The increase in this public discourse, and across infosec general does mean more disagreement, more debate and more differing views, but I don't think that's necessarily a bad thing.  Diversity of thought is vitally important for a healthy community (except where people disagree with me of course).  The next steps are for us to work out how to have these discussions without them descending into name calling, missed perspectives and people being offended.  That probably means we need to use twitter less to have these conversations (such as the City of York news this week), and more thoughtful debate in a long form, or face to face.

## [Have I Been Pwned: Check if your email has been compromised in a data breach](https://haveibeenpwned.com/)

[https://haveibeenpwned.com/](https://haveibeenpwned.com/)

> Check if you have an account that has been compromised in a data breach


So, I kind of assume that everyone has heard of HaveIBeenPwned, but one of the reasons for doing this newsletter was after the discovery that I read and see a lot more of this sort of stuff than most other people, and I wanted to share generally.

But a more interesting point has started to come to my attention with HaveIBeenPwned, which is that the signal from this dataset is getting weaker and weaker for a corporate or threat assessment use.  I recently read a threat intelligence brief that included the action of reviewing an organisations github commit history and looking up each address in the HaveIBeenPwned database to determine how many accounts had been included in breaches.

But this signal is extraordinarily weak when used this way, because HaveIBeenPwned cannot tell you whether that account took any remediating action.  If you look up my email address, you'll see that I was breached in the Adobe breach, along with a bunch of the spam databases and other large breaches.  In the adobe case in particular, I was notified and immedietely changed my password.  I also happened to reuse that password on other sites, and so I changed it on those sites as well.

But HaveIBeenPwned cannot know that I took those actions.  And if you use it to assess whether email addresses associated with a github project have ever been breached, you don't actually understand the impact that it is having.

The front website increasingly could just be replaced with the word "Yes" and it would be just as effective a threat signal, and indeed, when we consider public email accounts, we should adopt a "Assume Breached" concept.  What that looks like, I'm not sure, but if you assumed that all of your users email addresses and passwords were known to attackers, how would that change your security posture?  I suspect you'd want to roll out MFA on anything external pretty quick, which is why I still think that's the number one priority for organisations in my mind.

Note that HaveIBeenPwned has an outstanding notification process, letting users and organisations know that an account was in a recent breach, and that is a high value signal, so I'm not dismissing the value generally, just in this threat intelligence use case


## [USPS Site Exposed Data on 60 Million Users — Krebs on Security](https://krebsonsecurity.com/2018/11/usps-site-exposed-data-on-60-million-users/)

[https://krebsonsecurity.com/2018/11/usps-site-exposed-data-on-60-million-users/](https://krebsonsecurity.com/2018/11/usps-site-exposed-data-on-60-million-users/)

> In addition to exposing near real-time data about packages and mail being sent by USPS commercial customers, the flaw let any logged-in usps.com user query the system for account details belonging to any other users, such as email address, username, user ID, account number, street address, phone number, authorized users, mailing campaign data and other information.


This feels like a significant oversight by the USPS, and not the best response in the world.  It's also disappointing that this was raised with the USPS directly, and no answer could be gotten, so the researcher went to Krebs.  It'd be nice if there was a middle step between disclosure and krebs that could be used.


## [Starwood Reservation Database Security Incident](https://answers.kroll.com/)

[https://answers.kroll.com/](https://answers.kroll.com/)

> On September 8, 2018, Marriott received an alert from an internal security tool regarding an attempt to access the Starwood guest reservation database. Marriott quickly engaged leading security experts to help determine what occurred. Marriott learned during the investigation that there had been unauthorized access to the Starwood network since 2014. Marriott recently discovered that an unauthorized party had copied and encrypted information, and took steps towards removing it. On November 19, 2018, Marriott was able to decrypt the information and determined that the contents were from the Starwood guest reservation database.
> 
> Marriott has not finished identifying duplicate information in the database, but believes it contains information on up to approximately 500 million guests who made a reservation at a Starwood property. For approximately 327 million of these guests, the information includes some combination of name, mailing address, phone number, email address, passport number, Starwood Preferred Guest (“SPG”) account information, date of birth, gender, arrival and departure information, reservation date, and communication preferences. For some, the information also includes payment card numbers and payment card expiration dates, but the payment card numbers were encrypted using Advanced Encryption Standard encryption (AES-128). There are two components needed to decrypt the payment card numbers, and at this point, Marriott has not been able to rule out the possibility that both were taken. For the remaining guests, the information was limited to name and sometimes other data such as mailing address, email address, or other information. Marriott reported this incident to law enforcement and continues to support their investigation. We have already begun notifying regulatory authorities.


This is a huge breach.  The loss of 500,000,000 records is quite something to start with, but the length of time that there was unauthorised access to the system was from 2014 through to 2018.  The attackers had access to the system for 4 years!

I'm also curious about the data retention period here, it doesn't feel hugely reasonable that SPG retains records for such a long period of time in an online system, but we'll have to wait to see how the various data protection authorities react


## [ICO fines Uber £385,000 over data protection failings | ICO](https://ico.org.uk/about-the-ico/news-and-events/news-and-blogs/2018/11/ico-fines-uber-385-000-over-data-protection-failings/)

[https://ico.org.uk/about-the-ico/news-and-events/news-and-blogs/2018/11/ico-fines-uber-385-000-over-data-protection-failings/](https://ico.org.uk/about-the-ico/news-and-events/news-and-blogs/2018/11/ico-fines-uber-385-000-over-data-protection-failings/)

> 2.7million UK customers to be accessed and downloaded by attackers from a cloud-based storage system operated by Uber’s US parent company. This included full names, email addresses and phone numbers.
> 
> The records of almost 82,000 drivers based in the UK – which included details of journeys made and how much they were paid – were also taken during the incident in October and November 2016.
> 
> The ICO investigation found ‘credential stuffing’, a process by which compromised username and password pairs are injected into websites until they are matched to an existing account, was used to gain access to Uber’s data storage.
> 
> However, the customers and drivers affected were not told about the incident for more than a year. Instead, Uber paid the attackers responsible $100,000 to destroy the data they had downloaded.
> 
> ICO Director of Investigations Steve Eckersley said:
> 
> “This was not only a serious failure of data security on Uber’s part, but a complete disregard for the customers and drivers whose personal information was stolen. At the time, no steps were taken to inform anyone affected by the breach, or to offer help and support. That left them vulnerable.”


This is quite an interesting judgement, I recommend reading the [Full Judgement](https://ico.org.uk/media/2553890/uber-monetary-penalty-notice-26-november-2018.pdf) which is annoyingly in PDF, not accessible, and I can't even highlight text to quote here.

There are some worrying statements that make me wonder about the ICO's view of what is technically feasible, 
> Uber does not hold a record of all information it stored on the S3 system *at every point in time.*  The commissioner notes that it is poor data protection practice to unable or unwilling to identify whether and what personal data is contained in those buckets 
_[emphasis mine]_ feels a little ridiculous to me.  

The ICO has made a deal out of some of the github credentials not having 2-factor authentication on them, but it's more interesting to me that Uber has a perfectly good system for securely storing S3 credentials, but failed to use it in this case.

When our developers build systems for actiing in a secure way, we also need to ensure that everybody can and does use it when it's appropriate.

Reading between the lines, I think this judgement is primarily about Ubers attempt to reclassify the extortion as a bug bounty post fact, and to not inform the users of the breach rather than the technical details, but it's an interesting breach notification none the less


## [The Woolworths Experiment | Safety Differently](http://www.safetydifferently.com/the-woolworths-experiment/)

[http://www.safetydifferently.com/the-woolworths-experiment/](http://www.safetydifferently.com/the-woolworths-experiment/)

> When given the opportunity, people gladly throw off the yoke of bureaucracy and compliance. 19 out of 20 stores (a full 95%) from the two ownership conditions immediately ceased compliance activities mandated by the monthly safety pack. They all agreed that these things added no value, and didn’t impact safety outcomes. A store manager commented: “I think that removing the administrative tasks has inspired the team to be driven to look at safety in a different light. Instead of a chore, it is now more enjoyable: they look, observe and engage in what really matters, day to day.”


This is an interesting and great experiment to read about.  Essentially, they did a trial on removing beauracy and central control around "health and safety" rules in stores to see what would happen.

I think this experiment worked primarily because humans have a pretty good instinct for safety and the consequences for doing something unsafe are often both visible, self actualising and rapid.  In cybersecurity, much of the consequences for poor behaviour are delayed (because it requires a later event to exploit it), invisible to those they harm, and often they affect other people far more disproportionatly than oneself.  This means that I don't think you could ever take the same approach, but nevertheless, I'm still keen to rip up the ["organisational scar tissue"](https://m.signalvnoise.com/dont-scar-on-the-first-cut-e9afd256afdf) that is most security policies and focus on them being user centred, simple and clear.


## [The Equities Process | GCHQ Site](https://www.gchq.gov.uk/features/equities-process)

[https://www.gchq.gov.uk/features/equities-process](https://www.gchq.gov.uk/features/equities-process)

> The Equities Process provides a mechanism through which decisions about disclosure are taken. Expert analysis, based on objective criteria, is undertaken to decide whether such vulnerabilities should be released to allow them to be mitigated or retained so that they can be used for intelligence purposes in the interests of the UK. The starting position is always that disclosing a vulnerability will be in the national interest.


Opening up the equities process, in a similar way to how the US published their [equities process last year [PDF]](https://www.whitehouse.gov/sites/whitehouse.gov/files/images/External%20-%20Unclassified%20VEP%20Charter%20FINAL.PDF).

I think most sensible people will understand that there are reasons to legitimately retain a vulnerability, and the argument generally is over where to draw the line.  This explanation does a good job of explaining the process, but sadly doesn't give us any insight into what the actual considerations are.  While it says that the default is to release, critics can easily create supposed considerations that would very quickly move almost all vulnerabilities to retain.

Evidence of the amount of pretty hard to exploit, hard to find vulnerabilities disclosed by NCSC to Apple, Microsoft and others shows that this isn't the case, but I think the next step in transparency would be producing some numbers of the amount of vulnerabilities retained and released, and any sense of average length of time before a retained vulnerability is reviewed.


## [Principles for a More Informed Exceptional Access Debate - Lawfare](https://www.lawfareblog.com/principles-more-informed-exceptional-access-debate)

[https://www.lawfareblog.com/principles-more-informed-exceptional-access-debate](https://www.lawfareblog.com/principles-more-informed-exceptional-access-debate)

> 5) Any exceptional access solution should not fundamentally change the trust relationship between a service provider and its users.
> 
> This means not asking the provider to do something fundamentally different to things they already do to run their business.
> 
> A service provider or device manufacturer can already adversely affect the security and privacy of its users today, without building in exceptional access. Any exceptional access solution shouldn’t make that more likely, or easier for an attacker to take advantage of.


This is a great essay and sets out the start of what I think should be an essential public debate.  I find that the debate on encryption and access for law enforcement tends to be far too polarised. So it's nice to see that GCHQ are trying to have a much more reasoned debate, with technical matters given weight rather than a public policy and political debate here.

However, I think the example given defeats the principle that they've specifically highlighted, which is that creating the ability to surpress a notification is exactly a trust defeating mechanism.

There's a far better counter argument along those lines (From the same workshop)[https://www.lawfareblog.com/what-if-responsible-encryption-back-doors-were-possible] which does a better job of explaining why trust reducing features are fundementally not feasible in a global internet economy.

However, I think focusing on the one example here would be a mistake, I think this is a good set of principles for lawful interception and I'd like to be able to take suggestions around various mooted lawful interception schemes, and the various governments that run them and compare them to these principles and see what works and what doesn't


## [Tom Loosemore reminds us just how much digital government is flailing in the UK](https://government.diginomica.com/2018/11/27/tom-loosemore-reminds-us-just-how-much-digital-government-is-flailing-in-the-uk/)

[https://government.diginomica.com/2018/11/27/tom-loosemore-reminds-us-just-how-much-digital-government-is-flailing-in-the-uk/](https://government.diginomica.com/2018/11/27/tom-loosemore-reminds-us-just-how-much-digital-government-is-flailing-in-the-uk/)

> On what digital government is about…
> “It’s as much about a way of working. The notion of working in small teams, multi-disciplinary teams, bringing the technology and design skills back into government, to be able to deliver in the same way that Google, Amazon, AirBnB and the best start-ups deliver…multi-disciplinary, iterative, incremental, constant improvement, feedback loops, embracing open source, communicating openly. “
> 
> “There are no bits of government that can ignore adapting what they do, right down to their policies, to the internet era. We are still in the foothills as a government of adopting internet-era styles of delivery – the humility to start by accepting that you don’t understand what citizens actually need and want. And that you iterate your way humbly towards getting the policy outcome you want, rather than pretending you know the answer upfront.”


This write up has a specific angle, and I don't entirely agree with Derek's take here, but it was one of the best for just capturing Tom Loosemore's words in front of the [Science and Technology Committee on Digital Government](https://www.parliament.uk/business/committees/committees-a-z/commons-select/science-and-technology-committee/inquiries/parliament-2017/digital-government-17-19/).

I strongly recommend watching [Tom and Dafydd](https://parliamentlive.tv/Event/Index/abfe49d3-f24c-4b93-b8e4-840ff9f03794) talk and either downloading it and listening to it or just watching it.  Tom did a brilliant job of being honest and open, and he summarised a lot of the last 7 years of digital transformation in government in a well explained way.  Despite the desire by all and sundry to use Tom's words to backup their perspective on who's fault the slowdown is, Tom didn't really blame individuals, but instead re-emphasised that the system and the internal incentives cause behaviours that are rational to the individuals involved, but overall return the system to it's original stable state.

I'm sure there are people who could do more, and as always, there will be plenty of blame passed around, you just have to [read the written submissions](https://www.parliament.uk/business/committees/committees-a-z/commons-select/science-and-technology-committee/inquiries/parliament-2017/digital-government-17-19/publications/) to see how the lines are already being drawn (and in particular, I think attacking the "lack of testosterone" of the current leadership of GDS for not being "chest beating enough" is horrific in it's implications on what we think leadership is).  But the problem remains, and as Tom has said, the UK Government has made a brilliant start, and was one of the first to do this stuff, but other Governments are now overtaking the UK.

Tom does a better job than I of thinking through what the next steps should be and how we can advance the pace some more, and I think I agree with his top recommendations, so go watch it and see if you agree


