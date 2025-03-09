---
title: "8 - Where are you spending your security budget?"
date: 2018-07-14
description: "What do we spend our time and money set aside for security in companies doing? Lots of CISO's and security managers I talk to exclaim that they need significantly bigger budgets, that they can't do all of the stuff that is asked of them."
permalink: /where-are-you-spending-your-security-budget/
---

What do we spend our time and money set aside for security in companies doing? Lots of CISO's and security managers I talk to exclaim that they need significantly bigger budgets, that they can't do all of the stuff that is asked of them.
But when I look at the typical activities of a security team, a lot of the work is low yield, low effectiveness work. Writing policies that nobody will read, checking contracts for breach clauses despite being confident the contract wont be breached, adding malware protection to servers and desktops that shouldn't be able to have malware on them. What if we just stopped doing some of this stuff and looked at what things we could do that would massively improve security overall? Paid to upgrade and patch servers and desktops, bought everyone working good security software, ran education programs to help people do their jobs more efficiently and safely?

Sadly this isn't possible, but I wonder what we would spend our time and money on if it wasn't all taken up with the stuff that we feel we are required to do?

## [Exclusive: Apple to deploy 1Password to all 123,000 employees, acquisition talks underway – BGR](https://bgr.com/2018/07/10/apple-1password-acquisition-deal/)

[https://bgr.com/2018/07/10/apple-1password-acquisition-deal/](https://bgr.com/2018/07/10/apple-1password-acquisition-deal/)



"According to our source, after many months of planning, Apple plans to deploy 1Password internally to all 123,000 employees. This includes not just employees in Cupertino, but extends all the way to retail, too. Furthermore, the company is said to have carved out a deal that includes family plans, giving up to 5 family members of each employee a free license for 1Password."
Right now this might be the most effecient use of any organisations security budget, deploying password managers to all staff and their family.  This would protect not just the corporate IT solutions, but staff's personal email and social accounts, and raise the base level of cybersecurity across your entire organisation.  This would also create a seachange in the perception of the value of password managers and remembering passwords, and for the cherry on the top, many password managers support biometric authentication and 2-factor authentication as well.


## [Instant Results! Guaranteed!* – John Cutler – Medium](https://medium.com/@johnpcutler/instant-results-guaranteed-fe0cb6b76b10)

[https://medium.com/@johnpcutler/instant-results-guaranteed-fe0cb6b76b10](https://medium.com/@johnpcutler/instant-results-guaranteed-fe0cb6b76b10)



“In most unoptimized systems — systems that haven’t enjoy work in progress limits, and have not been operated as pull systems — you will see rapid improvement. The basics = big wins”. As well as a great introduction into how to implement kanban in an organisation, I think this advice is true for a lot of security areas. We tend to focus on trying to be perfect, on trying to get everything done and we reject ideas or practices that are flawed for 1% of use cases despite the fact that they would make things better for the majority. Implementing the basics in security will net you big wins and build a foundation on which to improve. 


## [The user is not the enemy [PDF] - 1999](http://discovery.ucl.ac.uk/20247/2/CACM%20FINAL.pdf)

[http://discovery.ucl.ac.uk/20247/2/CACM%20FINAL.pdf](http://discovery.ucl.ac.uk/20247/2/CACM%20FINAL.pdf)



"Both these problems are due to a lack of communication between security departments and users: users do not understand security issues, whilst security departments lack an understanding of users’ perceptions, tasks and needs. The result is that security departments typecast users as “inherently insecure”: at best, they are a security risk which needs to be controlled and managed, at worst they are the enemy within. Users, on the other hand, perceive many security mechanisms as laborious and unnecessary - an overhead which gets in the way of their real work."
Someone asked me recently where the evidence and backing about usability and security not being enemies came from and I found myself back at this seminal academic paper from 1999 by Angela Sasse and Anne Adams.  This paper very clearly articulates how security systems that increase user complexity end up creating users behaviours that bypass the same said security.  If you've never read it, it's worth reading


## [Postmortem for Malicious Packages Published on July 12th, 2018 - ESLint - Pluggable JavaScript linter](https://eslint.org/blog/2018/07/postmortem-for-malicious-package-publishes)

[https://eslint.org/blog/2018/07/postmortem-for-malicious-package-publishes](https://eslint.org/blog/2018/07/postmortem-for-malicious-package-publishes)



"The attacker presumably found the maintainer’s reused email and password in a third-party breach and used them to log in to the maintainer’s npm account."
One of the maintainers of a popular javascript library was reusing their password across multiple sites (allegedly), and this enabled an attacker to post an updated version of the plugin that attempted to send the developers .npmrc file to a remote server.  The .npmrc often contains plaintext username and passwords or tokens for publishing to npm, and eslint is used fairly commonly by lots of developers.  Supply chain attacks are a growing thing, and the problem is that almost all competent attackers, from criminal enterprises, nation states or just people mining bitcoin want to carry them out.


## [Hackers exploit Jenkins servers, make $3 million by mining Monero | CSO Online](https://www.csoonline.com/article/3256314/security/hackers-exploit-jenkins-servers-make-3-million-by-mining-monero.html)

[https://www.csoonline.com/article/3256314/security/hackers-exploit-jenkins-servers-make-3-million-by-mining-monero.html](https://www.csoonline.com/article/3256314/security/hackers-exploit-jenkins-servers-make-3-million-by-mining-monero.html)



"The attackers are leveraging CVE-2017-1000353, a flaw disclosed in a Jenkins security advisory issued in April 2017. Besides making the attackers millionaires, the “JenkinsMiner” could impact servers by slowing their performance and issuing denial of service."

This one terrifies me.  The security around our CI estates tends to be quite poor, because it isn't part of the "production estate" for most development teams.  But malware on that machine can abitrarily change any code deployed to any part of your infrastructure.  This is the weak point in any agile organisation with continuous delivery.


## [Teardown Of USB Fan Reveals Journalists’ Lack Of Opsec | Hackaday](https://hackaday.com/2018/07/11/teardown-of-usb-fan-reveals-journalists-lack-of-opsec/)

[https://hackaday.com/2018/07/11/teardown-of-usb-fan-reveals-journalists-lack-of-opsec/](https://hackaday.com/2018/07/11/teardown-of-usb-fan-reveals-journalists-lack-of-opsec/)



"There is a massive, massive gulf of understanding between otherwise competent professionals and the most basic tenets of computer security. So spread the word when you have the chance: Don’t give your passwords to people. Don’t reuse passwords. And don’t plug random USB devices into your computer.".  We still need to work out how we can make this advice, which is reasonable advice, relevant to users of computers.  Because their day to day jobs often involves doing exactly these things.
On another note, the fascinating teardown of the sorts of USB attack that are possible is worth a read.  The rise of USB-C and Thunderbolt ports, and relevant storage means that you might find that new modern I/O devices might be capable of far more today.


## [This fitness app lets anyone find names and addresses for thousands of soldiers and secret agents](https://decorrespondent.nl/8480/this-fitness-app-lets-anyone-find-names-and-addresses-for-thousands-of-soldiers-and-secret-agents/260810880-cc840165)

[https://decorrespondent.nl/8480/this-fitness-app-lets-anyone-find-names-and-addresses-for-thousands-of-soldiers-and-secret-agents/260810880-cc840165](https://decorrespondent.nl/8480/this-fitness-app-lets-anyone-find-names-and-addresses-for-thousands-of-soldiers-and-secret-agents/260810880-cc840165)



"Yet the activity tracking map in Polar’s fitness app  lets us see that many of Tom’s runs start and end near a cluster of homes in a small town in the northern Netherlands. A little Googling gives us his exact address. We also find the names of his wife and children, and photos."
This stuff is really hard.  Jigsaw identification is a common threat for people who are trying to keep their identity secret.  Early court injuctions simply told newspapers they couldn't identify celebrities involved in salacious court cases, but it meant that one might identify the team, whereas another newspaper would name the age.
No commercial organisation can reasonably protect the identity of sensitive individuals, especially if they don't know the sensitivity, and as such the responsibility tends to lie with the individual and any guidance from their organisation.


## [Thomas Cook website spills personal info – and it's fine with that • The Register](https://www.theregister.co.uk/2018/07/10/thomas_cook_privacy_flap/)

[https://www.theregister.co.uk/2018/07/10/thomas_cook_privacy_flap/](https://www.theregister.co.uk/2018/07/10/thomas_cook_privacy_flap/)



“Thomas Cook has used Article 33 of the GDPR to avoid reporting this incident both to the ICO and its customers. This refers to the fact that organisations do not need to report a breach of personal data where the risk to customers is low.”  One of the first, researcher found, breaches post GDPR and the firm has decided not to share. Presumably they have no evidence that anyone has attempted to bulk transfer the data except the researcher. I’m not sure how I feel on this, it’s kind of right assuming we can trust their data 


## [What Matters Most During a Data Breach? How You React](https://securityintelligence.com/what-matters-most-during-a-data-breach-how-you-react/)

[https://securityintelligence.com/what-matters-most-during-a-data-breach-how-you-react/](https://securityintelligence.com/what-matters-most-during-a-data-breach-how-you-react/)



"The Ponemon Institute’s 2017 study on the cost of a data breach showed companies have a one in four chance of experiencing such a breach within a two-year period."  By this math, the chance of a data breach in any given year is around 1/8 or 12.5%. The raw report makes clear that these are "material breaches" of 1,000 records or more.  Slightly more interesting, human error and system glitch was responsible for 53% of breaches, and malicious hackers are only responsible for 47%.


