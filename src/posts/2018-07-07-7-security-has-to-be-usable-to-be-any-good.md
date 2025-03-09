---
title: "7 - Security has to be usable to be any good"
date: 2018-07-07
description: "This week there has been a swathe of articles covering usable security in various forms. I'm loving seeing more and more organisations come up with ways to balance usability and security. We're never going to get this perfect, but we have to try."
permalink: /security-has-to-be-usable-to-be-any-good/
---

This week there has been a swathe of articles covering usable security in various forms. I'm loving seeing more and more organisations come up with ways to balance usability and security. We're never going to get this perfect, but we have to try.

One response to the DNC advice on twitter was a user saying "Yeah, but this wouldn't work against the advanced threats that are targeting the DNC", while forgetting that when the DNC was attacked by an "advanced threat" in 2016, it was precisely a phishing email targetting a users personal email, which didn't have 2-factor, that was the root of the attack. These sorts of usable security tips actually do make us secure against even the most capable adversaries. Let's see if we cut out a swathe of low hanging fruit and maybe we'll all be better off.

## [DNC pushes employees, campaigns to embrace email security habits ahead of midterms](https://www.cyberscoop.com/democratic-national-committee-dnc-phishing-emails-staffers-test/)

[https://www.cyberscoop.com/democratic-national-committee-dnc-phishing-emails-staffers-test/](https://www.cyberscoop.com/democratic-national-committee-dnc-phishing-emails-staffers-test/)



“The overall goal is improve the baseline security practices of a wide group of users that includes in-house staffers, candidates and volunteers spread across the country.  “Nearly 80 percent of our users are now either not clicking or at least asking questions about it beforehand,” Krikorian explained. “Being realistic we’ll probably never get to 100 percent compliance but we’re working on it … it’s important that people flag something, anything that seems suspicious … A lot of that happens through Signal to Bob [Lord] or to our help desk, so that we’re informed.””  Note that this is conducting internal phishing campaigns not to blame staff, identify who has clicked links, but to get an understanding of how effective your advice has been. The checklist is a wonderful piece of actionable security advice as well. 


## [Monzo – Engineering Principles at Monzo](https://monzo.com/blog/2018/06/29/engineering-principles/)

[https://monzo.com/blog/2018/06/29/engineering-principles/](https://monzo.com/blog/2018/06/29/engineering-principles/)



“We now have a team of over 70 engineers working on this, with more joining every week. As we continue to grow, it’s crucial that we create a shared understanding of what “good” looks like so that existing engineers know how to make decisions and prioritise work and new engineers know what we expect and how we work.”  I think this article is brilliant for its advice, but I wanted to highlight it for this comment. From my experiences at GDS and the Guardian as well as helping other government departments build out digital teams, one thing is clear. Scaling people is really hard. The Dunbar number means that all of those assumptions and things that “everyone knows” probably aren’t obvious to everyone and when you scale passed around 25 people you need to put real effort into documenting and communicating those cultural assumptions and practices if you want them to succeed. 


## [Use the tools that you need to do good work - Canadian Digital Service](https://digital.canada.ca/2018/06/27/tools-to-do-good-work/)

[https://digital.canada.ca/2018/06/27/tools-to-do-good-work/](https://digital.canada.ca/2018/06/27/tools-to-do-good-work/)



“We’ve chosen to optimize for where our developers spend most of their time.”. This is the crux of one of the issues that security people often don’t understand. Users want good solutions that are close to them. When security offers solutions that are “more secure” but further away from the users, it falls back into the old false dichotomy of user experience is a trade off against security. 


## [NSA ‘Systematically Moving’ All Its Data to The Cloud - Nextgov](https://www.nextgov.com/emerging-tech/2018/06/nsa-systematically-moving-all-its-data-cloud/149179/)

[https://www.nextgov.com/emerging-tech/2018/06/nsa-systematically-moving-all-its-data-cloud/149179/](https://www.nextgov.com/emerging-tech/2018/06/nsa-systematically-moving-all-its-data-cloud/149179/)



"The National Security Agency has moved most of the mission data it collects, analyzes and stores into a classified cloud computing environment known as the Intelligence Community GovCloud."

Next time someone tells you that "the cloud" isn't secure, you can remind them that the NSA has managed to move a lot of it's mission analytics into a intelligence community GovCloud.  Now this isn't the same as the public cloud, it will have dedicated hardware, dedicated sysadmins and of course is segregated.  But even inside the Intelligence Community, agencies and staff don't trust each other very much, so this is still a pretty big deal.


## [Why you should not use Google Cloud. – Punch a Server](https://medium.com/@serverpunch/why-you-should-not-use-google-cloud-75ea2aec00de)

[https://medium.com/@serverpunch/why-you-should-not-use-google-cloud-75ea2aec00de](https://medium.com/@serverpunch/why-you-should-not-use-google-cloud-75ea2aec00de)



“. I receive a barrage of emails from Google saying there is some ‘potential suspicious activity’ and all my systems have been turned off. ” 
Of all the cyber security concerns with cloud, this is the one that scares me the most. The company determining there is a problem with your billing could result in the loss of the account, which is everything! Making sure that you have good terms, aren’t just paying on the CFO’s credit card and that you understand the risk is critical in using the cloud effectively. 


## [Psychology’s trolley problem might have a problem.](https://slate.com/technology/2018/06/psychologys-trolley-problem-might-have-a-problem.html?via=gdpr-consent&via=gdpr-consent)

[https://slate.com/technology/2018/06/psychologys-trolley-problem-might-have-a-problem.html?via=gdpr-consent&via=gdpr-consent](https://slate.com/technology/2018/06/psychologys-trolley-problem-might-have-a-problem.html?via=gdpr-consent&via=gdpr-consent)



"If people’s answers to a trolley-type dilemma don’t match up exactly with their behaviors in a real-life (or realistic) version of the same, does that mean trolleyology itself has been derailed?"

The trolly dilemma is a favourite armchair psychologists thought experiment because it is easy to understand and feels simplistic to reason about.  But if this data is accurate, how people philosophise that they would act and how they do act is significantly different.  The same is true when we think about security policies.  We need to measure how people actually act in these situations, rather than build policies around supposed human behaviour


## [When spies hack journalists - NYTimes](https://www.nytimes.com/2018/05/12/sunday-review/when-spies-hack-journalism.html)

[https://www.nytimes.com/2018/05/12/sunday-review/when-spies-hack-journalism.html](https://www.nytimes.com/2018/05/12/sunday-review/when-spies-hack-journalism.html)



“For reporters, withholding valuable information from the public is anathema. But in a world in which foreign intelligence services hack, leak and fabricate, journalists will have to use extreme caution and extra transparency.”  This is a really interesting take on the ethics in journalism. Getting access to sources and material is obviously useful to journalists, but if the journalist suspects that the person leaking has a political motive to influence the public conversation, who gets to decide what’s right? Especially as politics in various countries around the world gets more polarised, expect more of this


## [IOTA Signatures, Private Keys and Address Reuse? - Lekkertech](http://blog.lekkertech.net/blog/2018/03/07/iota-signatures/)

[http://blog.lekkertech.net/blog/2018/03/07/iota-signatures/](http://blog.lekkertech.net/blog/2018/03/07/iota-signatures/)



“So after generating one piece of the private key, the whole internal state of the sponge only contains information that is also in the first piece of the private key. A Key Derivation Function that behaves like this is critically broken.”  A timely reminder that crypto is hard. Really hard. And crypto currencies are being implemented by people who don’t understand the properties of the safe crypto components they are using. Someone once told me that crypto is unusual because it doesn’t commute. That is to say, applying function f to data d followed by function g doesn’t necessarily give you all the security properties of f and g combined, in fact it’s possible or likely that the output of g might break the security properties of f. Hash functions and encryption often exhibit these properties and very few people understand the mathematics and the implementation to carry this stuff out safely


## [Tory MP says UK needs a chief blockchain officer | City A.M.](http://www.cityam.com/288641/tory-mp-says-uk-needs-chief-blockchain-officer)

[http://www.cityam.com/288641/tory-mp-says-uk-needs-chief-blockchain-officer](http://www.cityam.com/288641/tory-mp-says-uk-needs-chief-blockchain-officer)



“Hughes makes a series of recommendations in his report 'Unlocking Blockchain' issued today including the appointment of a public-facing chief blockchain officer to coordinate the UK’s strategy on applying blockchain technology to public services and data.”  This worries me immensely. This is seeking to force a solution on government departments without a clear idea of what problem it solves. Very tail wagging the dog


