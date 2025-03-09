---
title: "16 - Blockchain has a history"
date: 2018-09-08
description: "_NOTE: This email was sent out without this introduction, it's preserved here as I wrote it, rather than how I sent it out.  Sorry for everyone who missed this_"
permalink: /blockchain-has-a-history/
---

_NOTE: This email was sent out without this introduction, it's preserved here as I wrote it, rather than how I sent it out.  Sorry for everyone who missed this_

We stand on the shoulders of giants in technology.  We often however like to think that we are the first to be solving problems, that our problems are unique and special.  In my experience they are often much the same as everyone else’s problems, but our context is different, and we are very bad at looking across at other contexts.

Blockchain and distributed ledgers have a long history much prior to the hype of the last few years, but I don’t think anyone realised just how old that history was, so the story about the block chain in the New York Times was a welcome reminder of this.

Equally, I think there’s a lot that modern security can learn from the current practices and experiences happening in startups, DevOps movements and modern user testing arenas.  This week has a good session from chaos engineering, which is teams who actively test the reliability and failover mechanisms of their digital systems by deliberately injecting failures into the system and seeing how they respond.  This is very similar to the way that we conduct penetration tests or in some organisations we have red teams continually testing our systems security.  There’s a lot we can learn from how chaos engineering tries to build failures, but to limit the blast radius, how they help diagnose the issues that occur and how they help fix these issues.

## [The World’s Oldest Blockchain Has Been Hiding in the New York Times Since 1995 - Motherboard](https://motherboard.vice.com/en_us/article/j5nzx4/what-was-the-first-blockchain)

[https://motherboard.vice.com/en_us/article/j5nzx4/what-was-the-first-blockchain](https://motherboard.vice.com/en_us/article/j5nzx4/what-was-the-first-blockchain)

> Surety’s main product is called “AbsoluteProof” that acts as a cryptographically secure seal on digital documents. Its basic mechanism is the same described in Haber and Stornetta’s original paper. Clients use Surety’s AbsoluteProof software to create a hash of a digital document, which is then sent to Surety’s servers where it is timestamped to create a seal. This seal is a cryptographically secure unique identifier that is then returned to the software program to be stored for the customer.
> 
> At the same time, a copy of that seal and every other seal created by Surety’s customers is sent to the AbsoluteProof “universal registry database,” which is a “hash-chain” composed entirely of Surety customer seals. This creates an immutable record of all the Surety seals ever produced, so that it is impossible for the company or any malicious actor to modify a seal. But it leaves out an important part of the blockchain equation: Trustlessness. How can anyone trust that Surety’s internal records are legit?
> 
> Instead of posting customer hashes to a public digital ledger, Surety creates a unique hash value of all the new seals added to the database each week and publishes this hash value in the New York Times. The hash is placed in a small ad in the Times classified section under the heading “Notices & Lost and Found” and has appeared once a week since 1995.


Just lovely, and a good example of where a blockchain (or similar) is the right solution.  I’m increasingly looking to see where the underlying blockchain or ledger technology is a good fit, and this kind of public record held by a company is exactly the sort of thing that works


## [What to make of cryptocurrencies and blockchains - The pot of gold at the end of the rainbow](https://www.economist.com/technology-quarterly/2018/08/30/what-to-make-of-cryptocurrencies-and-blockchains)

[https://www.economist.com/technology-quarterly/2018/08/30/what-to-make-of-cryptocurrencies-and-blockchains](https://www.economist.com/technology-quarterly/2018/08/30/what-to-make-of-cryptocurrencies-and-blockchains)

> This Technology Quarterly will take a more sceptical view. It will point out that, despite a decade of development, bitcoin has failed in its stated objective: to become a usable currency. Security is poor (according to one estimate, around 14% of the supply of big cryptocurrencies has been compromised); its decentralised nature inevitably makes it slow; there is no consumer protection; and the price is so volatile that not many people would want to use it as a means of exchange for goods and services. Other cryptocurrencies suffer from similar problems. Few merchants accept them.


14%?? That’s a huge amount for what is supposedly a “cryptographically secure currency”.  But otherwise this is a good summary of the world of block chain as it stands


## [TSB boss Paul Pester to step down after IT fiasco - BBC News](https://www.bbc.co.uk/news/business-45406322)

[https://www.bbc.co.uk/news/business-45406322](https://www.bbc.co.uk/news/business-45406322)

> The IT debacle cost TSB £176m and 26,000 customers closed their accounts (although 20,000 new accounts were opened offsetting some of the damage). The bank and Mr Pester's reputation took a heavy knock.


That's a lot of money for many people, but I suspect is just the direct costs involved, rather than the losses incurred over the time.  The numbers on how many customers closed or opened accounts are meaningless without anything to compare to.


## [Ba customer data](https://www.grahamcluley.com/british-airways-hacked-customer-data-and-details-of-380000-card-payments-stolen/)

[https://www.grahamcluley.com/british-airways-hacked-customer-data-and-details-of-380000-card-payments-stolen/](https://www.grahamcluley.com/british-airways-hacked-customer-data-and-details-of-380000-card-payments-stolen/)

> British Airways, which once liked to describe itself as “The World’s Favourite Airline”, is about to become a whole lot less popular with hundreds of thousands of its customers.  The airline has announced that hackers have stolen customers’ personal and payment card information from its website


This is a pretty major breach in a post GDPR world, so this is a story to watch unfold and work out whether BA will be found of carrying out sufficient security measures.


## [Hurricane Maria was the most deadly storm in America since 1900 - A chronicle of deaths untold](https://www.economist.com/united-states/2018/08/30/hurricane-maria-was-the-most-deadly-storm-in-america-since-1900)

[https://www.economist.com/united-states/2018/08/30/hurricane-maria-was-the-most-deadly-storm-in-america-since-1900](https://www.economist.com/united-states/2018/08/30/hurricane-maria-was-the-most-deadly-storm-in-america-since-1900)

> It is absurd that the death toll of 64 remained official for so long. Although ascertaining good data on deaths after a natural disaster is difficult—the official death count from hurricane Katrina in 2005 is still disputed—the governor’s office could have done a lot more to communicate the inherent uncertainty in the official count. After New Orleans was hit by Katrina, its mayor simply said the death toll would “shock the nation”.
> 
> By contrast, the low number in Puerto Rico may well have lessened the urgency of relief efforts. A third of Americans said they donated money in the immediate aftermath, which is low by the country’s generous standards.


Gathering data is hard, but the ways that the data is used and published is really important.  In this case, the official death toll only counted people directly killed during the hurricane by its effects, but didn't count people killed by the aftereffects.  The lower official death toll probably hampered aid efforts, by reducing the perceived priority of the disaster and the real impacts


## [North Korean programmer charged in Sony hack, WannaCry attack | PBS NewsHour](https://www.pbs.org/newshour/nation/north-korean-programmer-charged-in-sony-hack-wannacry-attack)

[https://www.pbs.org/newshour/nation/north-korean-programmer-charged-in-sony-hack-wannacry-attack](https://www.pbs.org/newshour/nation/north-korean-programmer-charged-in-sony-hack-wannacry-attack)

> A computer programmer accused of working at the behest of the North Korean government was charged Thursday in connection with several high-profile cyberattacks, including the Sony Pictures Entertainment hack and the WannaCry ransomware virus that affected hundreds of thousands of computers worldwide.


Charged in absentia, which makes me wonder what the prosecution is hoping to achieve.  Without an extradition treaty, this is unlikely to result in any actual ramifications apart from restricting this individuals ability to travel.  But presumably there will be no defence, no trial and no ability to verify whether or not the charges are accurate in a court of law that all involved countries will recognise.


## [user-security-stories/security-acceptance-criteria.md at master · OWASP/user-security-stories · GitHub](https://github.com/OWASP/user-security-stories/blob/master/security-acceptance-criteria.md)

[https://github.com/OWASP/user-security-stories/blob/master/security-acceptance-criteria.md](https://github.com/OWASP/user-security-stories/blob/master/security-acceptance-criteria.md)

> Security Acceptance Criteria
> 
> More often, existing user stories will contain security requirements as acceptance criteria. Examples follow below.


I’m not 100% sold on the user stories for security, I don’t think that a customer cares about CSRF, which is what the stories make it seem.  But these acceptance criteria work quite nicely for the checklist manifesto style process for an agile team.  Agreeing what the checklists are for your team, and then checking everything off before a story is signed off is worth doing.  But make sure that security doesn’t become a bottleneck, each of the acceptance criteria either needs to be doable by the team, or only used rarely, so that your security team can manage the requests on their time.


## [GitHub - aquasecurity/kube-hunter: Hunt for security weaknesses in Kubernetes clusters](https://github.com/aquasecurity/kube-hunter)

[https://github.com/aquasecurity/kube-hunter](https://github.com/aquasecurity/kube-hunter)

> Kube-hunter hunts for security weaknesses in Kubernetes clusters


This is a very neat looking tool for exploring common weaknesses in hosted Kubernetes clusters.  Security teams and hosting teams should be running this kind of tool to confirm that everything is configured well and that the security promises of kubernetes are actually upheld.


## [Netflix, LinkedIn and Gremlin Engineers Talk Chaos Engineering - The New Stack](https://thenewstack.io/netflix-linkedin-and-gremlin-engineers-talk-chaos-engineering/)

[https://thenewstack.io/netflix-linkedin-and-gremlin-engineers-talk-chaos-engineering/](https://thenewstack.io/netflix-linkedin-and-gremlin-engineers-talk-chaos-engineering/)

> That’s what I mean by vulnerability. And we’re actually trying to figure out a way to easily service vulnerabilities to teams. You saw that Monocle screen I put up. I could pull up certain teams’ Monocles and see probably 50 vulnerabilities. But if you hand a team 50 vulnerabilities, they’re probably not going to fix any of them. You know what I mean? So you have to figure out a way to prioritize those … figure out a way to show them, “Hey, this is actually a very important thing that you want to fix because it’s only a matter of time before it could actually become an outage and it could end up on Twitter.”


This is talking about vulnerabilities in terms of reliability and availability rather than traditional security based confidentiality vulnerabilities, but there’s a lot that existing red teams can learn from chaos engineering teams and the movement around there.  This little snippet in particular reminded me that spending effort finding issues is wasted if you don’t already have the process and the money and time to actually deal with the issues.


## [Password managers: Please make sure AutoFill is secure! | Wladimir Palant's notes](https://palant.de/2018/08/29/password-managers-please-make-sure-autofill-is-secure)

[https://palant.de/2018/08/29/password-managers-please-make-sure-autofill-is-secure](https://palant.de/2018/08/29/password-managers-please-make-sure-autofill-is-secure)

> Dear developers of password managers, we communicate quite regularly, typically within the context of security bug bounty programs. Don’t get me wrong, I don’t mind being paid for finding vulnerabilities in your products. But shouldn’t you do your homework before setting up a bug bounty program? Why is it the same basic mistakes that I find in almost all password managers? Why is it that so few password managers get AutoFill functionality right?
> 
> Of course you want AutoFill to be part of your product, because from the user’s point of view it’s the single most important feature of a password manager. Take it away and users will consider your product unusable. But from the security point of view, filling in passwords on the wrong website is almost the worst thing that could happen. So why isn’t this part getting more scrutiny? There is a lot you can do, here are seven recommendations for you.


This is a good list of things to address that password managers, but also anybody developing systems that show in the browser should deal with (extensions for example, but also security related login forms on your website).
It would be nice to get a list of which password managers do this stuff right and well, and therefore can be trusted in future.


