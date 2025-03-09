---
title: "14 - How many breaches will it take?"
date: 2018-08-25
description: "It sometimes feels like the news in cybersecurity is an endless slew of breaches, with security professionals standing to one side saying \"I told you so\".  This attitude of enjoying disasterporn, or Schadenfreude, doesn't make us look very good as a profession, but it is understandable.  We should be trying to understand from breaches, trying to work out what happened and what was involved, and what steps we could take that would prevent it next time."
permalink: /how-many-breaches-will-it-take/
---

It sometimes feels like the news in cybersecurity is an endless slew of breaches, with security professionals standing to one side saying "I told you so".  This attitude of enjoying disasterporn, or Schadenfreude, doesn't make us look very good as a profession, but it is understandable.  We should be trying to understand from breaches, trying to work out what happened and what was involved, and what steps we could take that would prevent it next time.

To do that, tradition says that we need to balance our advice and our security concerns against the usability of the systems, but as Emma W from NCSC says so well this week, that's a false dichotomy.  We need to work out how to make our systems more resilient, and more usable in the most secure manner.  We need to meet users where they are and ensure that they can easily patch, update and authenticate, in a manner that works for them and helps them remain secure.  Security isn't a tradeoff against usability, but it is inextricably linked.

And if we don't do this soon, then we'll see another attack the scale of NotPetya, and we'll see more of them, and as the gloves come off in an international arena, we'll see growing escalation, but more importantly, the vulnerabilities, the weapons that are being used in the shadowy online conflict will fall into the hands of truly bad people who don't care about "collateral damage" and just want profit at any cost.

## [Hackers Stole Personal Data of 2 Million T-Mobile Customers - Motherboard](https://motherboard.vice.com/en_us/article/a3qpk5/t-mobile-hack-data-breach-api-customer-data)

[https://motherboard.vice.com/en_us/article/a3qpk5/t-mobile-hack-data-breach-api-customer-data](https://motherboard.vice.com/en_us/article/a3qpk5/t-mobile-hack-data-breach-api-customer-data)

> After this story was first published, a T-Mobile spokesperson told me that “encrypted passwords” were included in the compromised data. In its original announcement, the company said: “no passwords were compromised.”
> 
> When I asked why the company used that wording, the spokesperson said in a message: “Because they weren’t [compromised]. They were encrypted.”
> 
> The spokesperson declined to specify how those passwords were encrypted, or what hashing algorithm was used. Hours after this story was published, security researcher Nicholas Ceraolo reached out claiming that the data exposed in the breach was more than what T-Mobile disclosed. The researcher shared a sample of allegedly compromised data that included a field called “userpassword” and what looks like a hash, which is a cryptographic representations of a password. (Ceraolo said he was not involved in the hack but obtained the sample from a "mutual friend.")
> 
> According to two different security researchers, with whom Motherboard shared that hash, it may be an encoded string hashed with the notoriously weak algorithm called MD5, which can potentially be cracked with brute-forcing attacks.


This is bad, especially combined with their online assertion via their customer services agent earlier this month that Troy Hunt and others didn’t need to worry about their passwords being stored in the clear in a database because “their security is amazing”.  How can we reach out to companies like this and get them to understand the problem, and what are the steps one needs to take if you currently have a big database full of insecurely stored passwords?


## [The Untold Story of NotPetya, the Most Devastating Cyberattack in History | WIRED](https://www.wired.com/story/notpetya-cyberattack-ukraine-russia-code-crashed-the-world/)

[https://www.wired.com/story/notpetya-cyberattack-ukraine-russia-code-crashed-the-world/](https://www.wired.com/story/notpetya-cyberattack-ukraine-russia-code-crashed-the-world/)

> It’s the story of a nation-state’s weapon of war released in a medium where national borders have no meaning, and where collateral damage travels via a cruel and unexpected logic: Where an attack aimed at Ukraine strikes Maersk, and an attack on Maersk strikes everywhere at once.


This is a fascinating read generally, but this sentence struck me.  The interconnectedness of computers has been seen over and over again, from WannaCry to NotPetya to the early spread of the Morris Worm.  It's increasingly difficult to reliably and ethically determine what a valid computer target should be for any form of cyber warfare, and as the control of the techniques is no where nearly as easily controlled as the one for the mechanistic capability to produce nuclear weapons, the increasing proliferation of these weapons to more and more non-nation-state groups seems likely and deeply worrying.


## [Cyber security – why you’re doing it all wrong](https://www.computerweekly.com/opinion/Cyber-security-why-youre-doing-it-all-wrong)

[https://www.computerweekly.com/opinion/Cyber-security-why-youre-doing-it-all-wrong](https://www.computerweekly.com/opinion/Cyber-security-why-youre-doing-it-all-wrong)

> For too long, security teams have lived the lie that what they have delivered has been effective, but so often they approach it from a viewpoint divorced from the customers they affect. To be fair to most security teams, they are generally blissfully unaware of the inefficiencies of their controls – or ignorant.
> 
> This is admittedly a very sweeping statement, but headline after headline about data breaches tends to argue the point. And let’s not be shy here – these are major corporations with systemic failures when it comes to protecting their crown jewels. Something doesn’t sit right.
> 
> How can this be? Spending on IT security is at an all-time high. The volume of security offerings to cover every possible facet of security is unparalleled.


Everything about this essay is right. Security is often a complete disaster with failure to recognise what is the reality. We need to take a hard look at what we achieve and determine whether any of our security controls that we take all of our time maintaining is actually worth spending that time.


## [The Post AWS's Billing Team Could Have Written But Didn't - Last Week in AWS](https://lastweekinaws.com/blog/the-post-awss-billing-team-could-have-written-but-didnt.html)

[https://lastweekinaws.com/blog/the-post-awss-billing-team-could-have-written-but-didnt.html](https://lastweekinaws.com/blog/the-post-awss-billing-team-could-have-written-but-didnt.html)

> Imagine a mythical organization that has a single AWS account. (For purposes of this exercise, ignore the technical problems of account-wide rate limits, the operational hazards of "oops that was Production," the governance implications of a lack of a discrete audit trail, etc.) Everything's in one place, it gets charged to one bill, one person in Finance pays the bill (presumably, anyway; you'd be amazed how many Disaster Recovery plans overlook "the credit card stops working" as a potential risk factor). All is well.


This is a good explanation of why multiple AWS accounts makes sense from a finance perspective, not just a security perspective.  But these highlighted security issues are also key.  AWS credentials are a goldmine for attackers these days, and whereas we used to worry about network lateral movement, I predict we'll be worrying about cloud account lateral movement soon, if not already


## [Electronic signatures are valid say Government’s legal experts | Law Commission](https://www.lawcom.gov.uk/electronic-signatures-are-valid-say-governments-legal-experts/)

[https://www.lawcom.gov.uk/electronic-signatures-are-valid-say-governments-legal-experts/](https://www.lawcom.gov.uk/electronic-signatures-are-valid-say-governments-legal-experts/)

> Law Commissioner Stephen Lewis said:  “Contract law in the UK is flexible, but some businesses are still unsure if electronic signatures would satisfy legal requirements.  “We can confirm that they do, potentially paving the way for much quicker transactions for businesses and consumers.  “And not only that, there’s scope, with our proposals for webcam witnesses, to do even more to make signing formal documents more convenient, speed up transactions and get business booming.”


This is welcome news.  Should be useful to quote at people


## [Password and Credential Management in 2018 🔒 – Florian Harwöck – Medium](https://medium.com/@harwoeck/password-and-credential-management-in-2018-56f43669d588)

[https://medium.com/@harwoeck/password-and-credential-management-in-2018-56f43669d588](https://medium.com/@harwoeck/password-and-credential-management-in-2018-56f43669d588)

> We will cover the “perfect” (Nothing is absolutely perfect and of course I would be more than happy for any suggestions for improvements in the comments 😉) way to handle password credentials from the moment a user types them into a form on the client-side, till the moment they are stored in the database. Furthermore, we will look into common errors, that happen when developers store other credentials like Tokens/Secrets/etc.


This is a very good outline of "good password management" on the server side.  Explaining both why the relevant hash or encryption algorithms have been selected and the purpose of the protocol itself.


## [Security and usability: you CAN have it all! - NCSC Site](https://www.ncsc.gov.uk/blog-post/security-and-usability-you-can-have-it-all)

[https://www.ncsc.gov.uk/blog-post/security-and-usability-you-can-have-it-all](https://www.ncsc.gov.uk/blog-post/security-and-usability-you-can-have-it-all)

> Get better value from your security measures by making them more usable. Your security policy manual may cover every conceivable scenario, in painstaking detail, but if this makes it so long that people can't find the right advice when they need it (or understand the language) then your policies are only adding a fraction of the value that they could.
>  


This is great from NCSC reminding us that security has to be usable and that’s it’s not a trade off between the two. Some good tips for ways to make better, more usable security decisions as well. I wholeheartedly agree with pretty much everything in here [full disclosure: I reviewed an early copy of this and submitted feedback]


## [MongoDB Server Exposes Babysitting App's Database](https://www.bleepingcomputer.com/news/security/mongodb-server-exposes-babysitting-apps-database/)

[https://www.bleepingcomputer.com/news/security/mongodb-server-exposes-babysitting-apps-database/](https://www.bleepingcomputer.com/news/security/mongodb-server-exposes-babysitting-apps-database/)

> The exposure took place last week and was caused by a MongoDB database left exposed on the Internet with no credentials.


Sigh. This seems pretty poor, and yet doesn’t surprise me at all


## [Everyone screams patch ASAP – but it takes most organizations a month to update their networks • The Register](https://www.theregister.co.uk/2018/08/22/patching_survey/)

[https://www.theregister.co.uk/2018/08/22/patching_survey/](https://www.theregister.co.uk/2018/08/22/patching_survey/)

> But the reality on the ground, according to Kollective's survey, is that two-thirds of enterprises are not able to automate security updates, with 13 per cent confessing that they have given up on trying to create an automated system and instead rely on employees updating their own systems.
> 
> Big hacker opportunity
> If Kollective is right, a terrifying 81 per cent of companies will not be able to apply the Struts patch within the one-day timeframe that Apache has "urgently advised." Just over a half – 52 per cent – say it will take a week.


While interesting results, this again seems to conflate the issues of patching end user devices with the patching of server side systems.  There should not ever be a need for an organisation to rely on end users patching the server side systems (nor should there be fore end user devices for that matter).  The approach you use for one type of software patching is not the same as the other.
And again, services built in the cloud, with good DevOps practices should improve this rate significantly, the only issue with patching in such an environment is testing,and that should enable made easier with good mature DevOps practices.


