---
title: "218 - Balancing security and usability"
date: 2023-01-08
description: "Happy new year and welcome to 2023."
permalink: /balancing-security-and-usability/
---

Happy new year and welcome to 2023.

Before the break, I had a very busy period at work because I'm currently covering a vacancy of another manager in addition to my existing role. That means that my time to sit and read and digest cybersecurity news had to take a bit of a back seat for a while, and I couldn't give enough attention to write a full newsletter of CyberWeekly. Christmas, however, was a lovely time to recover my energy and catchup on some reading so we're back on, and I'm recruiting a replacement now, so hopefully things will come back to normal in the next month or so.

In the meantime, a number of the articles I read over the christmas period really re-raised the concept that security and usability are at odds with each other.  

For years, security people claimed that security had to inconvenience people, because the most easy and usable way to do something was always the most insecure way.  I think the rise of cloud computing has shown that this isn't true.  When I was working at the Government Digital Service, we were working alongside security colleagues who had precisely the opposite opinion.  When it's not easy to do something securely, people wont bother.  We boiled that down to something around there needing to be great usability and just enough security, but I prefer the mindset that security has to be an enabler of the things that users want to do.  When security gets in the way or creates an adversarial relationship, then the trust that users have breaks down, and all of the shadow-security that users do that actually keep us secure stops working as well.

But there's something about trust and second parties that really is a fundamental security tradeoff.  There's an old saying, the only way to keep a secret is to ensure it's known by only one person.  The moment you trust a second person with some secret thing is the moment that your threat model changes to include a huge amount of obscurity and ineffability.  It's impossible for humans to truly know what is happening in the minds of others.  We can assess them based on their actions, but the reasoning behind those actions may well be different to what we would ascribe to them, and as such trust is required for the relationship to work.

But in this increasingly networked and connected world, we are forced to trust a huge number of third parties, and it's incredibly difficult to quantify, measure or validate that trust.  Password Managers are a really good example of this, but almost all supply chains exemplify this to some degree.  We have to trust that the third party is dealing with us honestly, and that their incentives align with ours.  We assume that a password manager company wants first and foremost to keep our passwords secure, to ensure that nobody else can access them.  But how they do this, how much money and effort they spend and how well they achieve this goal is something that can be difficult to reconcile.

Furthermore, the economics of this relationship are also complex because it's not a simple one for one purchasing relationship.  I don't just pay per password, instead I use a password manager because it's convenient.  But it also adds security through my human factors.  Like most normal people, before I used a password manager, I would reuse passwords for some sites.  The context of that password would depend on how important that site was in my life, but I couldn't possibly hope to remember the tens of thousands of passwords I'd need to have a different password for every authenticated exchange in my life.  Now that I have a password manager, I can have different passwords everywhere, so I'm also buying an improved security practice along with my service that I get.

But what can we do then about deciding which third parties to trust?  This is where it gets complex, because you can come up with your own rules for how you filter down these third parties.  Do you prefer the one that claims to have had no security incidents, or the one that is open and communicates about the ones it has had?  Do you go for the one that is harder to use but uses a technology you like, or do you trust them to make good technology choices?

If 2022 was about realising the extent of the supply chains that affect our life, then 2023 is going to be realising just what an unsolvable problem securing those supply chains is going to be.  There are no good choices that can be made, just a series of tradeoffs, and in many cases, buyers will be completely unable to make rational choices about them.  This is not just true of the direct purchasing relationship, it would be hard but solvable if that were the case, but the fact that supply chains are recursive, that the trust I put in my supplier is also putting trust in how they trust their suppliers and so on down the line makes this impossible to cohere.

I think we'll make progress, we'll be able to identify things that really matter, push those questions down and build empirical evidence gathering of suitability and improve our supply chain selection processes, but the reality of this is that the worms are out of the can and putting them back in is going to be hard.

In the meantime, remember that users are doing their best to do their job in the most efficient, easy and secure manner possible (probably in that order), and that our job is to help them do that.

## [Telling users to ‘avoid clicking bad links’ still isn’t... - NCSC.GOV.UK ](https://www.ncsc.gov.uk/blog-post/telling-users-to-avoid-clicking-bad-links-still-isnt-working)

[https://www.ncsc.gov.uk/blog-post/telling-users-to-avoid-clicking-bad-links-still-isnt-working](https://www.ncsc.gov.uk/blog-post/telling-users-to-avoid-clicking-bad-links-still-isnt-working)

> Let's start with a basic premise: several of the established tenets in security simply don’t work. One example is advising users not to click on bad links. Users frequently _need_ to click on links from unfamiliar domains to do their job, and being able to spot a phish is **not** their job. The NCSC carries out and reviews red team operations, and a common observation is that red teamers (and indeed criminals or hostile states) only need one person to fall for a ruse for an attacker to access a network.
> 
> We're even aware of some cases where people have forwarded suspicious emails from their home accounts to their work accounts, assuming that the security measures in place in their organisations will protect them. And once a link in a phishing email is clicked and an attack launches, the stigma of clicking can prevent people reporting it, which then delays the incident response.
> 
> So, what if we assume that users will sometimes, completely unintentionally, click on bad links and that when they're at work, it's their organisations that are responsible for protecting them?
> 
> […]
> 
> It's time for organisations to move away from using blame and fear around clicking links, even if it's usually unintentional. This means, for example, not running phishing exercises that chastise users for clicking on bad links.
> 
> Imagine a scenario where a user isn't embarrassed to report when they've clicked on a malicious link, so they do so promptly, the security team thanks them for their swift action, and then works quickly to understand the resulting exposure. This is a much more constructive sequence of events, and with the added security benefit that an attack is identified early on.
> 
> We should also make it easy for users to report suspicious emails, such as using [email add-ins](https://www.ncsc.gov.uk/guidance/configuring-o365-outlook-report-phishing-for-sers#sample) widely. 


Just lovely.  Stop telling users not to click on bad links, instead ensure that bad links don’t get to them, and if they do, clicking on them should have little to no effect.

And if something does go wrong, make sure that your security team is seen as friendly, approachable, and the people you want to say “I clicked a link and X happened” to.  Punishing users always leads to adversarial relationships between security and users and that leads to failures to detect and remediate an issue when it does occur. 


## [The quest for a family-friendly password manager ](https://dustri.org/b/the-quest-for-a-family-friendly-password-manager.html)

[https://dustri.org/b/the-quest-for-a-family-friendly-password-manager.html](https://dustri.org/b/the-quest-for-a-family-friendly-password-manager.html)

> With LastPass [making a habit of getting pwned](https://en.wikipedia.org/wiki/LastPass#Security_incidents) and [generally sucking](https://infosec.exchange/@epixoip/109585049354200263) , I started to look for a proper™ cloud-based password manager that I could recommend to friends and family. **Requirements** 1. A non-lame security level, by a entity that won't crash and burn in 3 months, and whose sole interest is keeping their customer's passwords safe: managing passwords can't be a side-hustle.
> 
> 2. Compromised passwords monitoring: I don't trust people to have used proper passwords before, and would like to make sure that they stop doing this.
> 
> 3. Usable in a web browser, as well as on a smartphone: anything more complex than "Or I can just put `azerty1234` in the password field and call it a day" won't do.
> 
> 4. Data should be exportable.
> 
> Being open-source doesn't really matter, since supply-chain attacks are way more likely than source-level backdooring. I don't know much about web browser extension security, so those are off the scope this article. Firefox and Chrome do offer passwords manager, but those won't autofill smartphone apps. Moreover, tying all your passwords to your Google account sounds like a recipe for disaster, given how infamous Google is for closing accounts on a whim without any kind of possible recourse. 


The TL;DR; of this is that in the case of password managers, it really does seem like security and usability have opposite trade offs.

I believe that password managers are a good thing, they reduce the complexity of trying to remember so many passwords. However, they come with a trade off that you are having to trust the password manager supplier to be reasonably competent.

There is a further thing worth remembering that doesn’t come into most people’s models, which is that you are also somewhat hiding in the noise of a password manager.  If someone can breach a password manager, then they have access to the entire customer set, and that lowers the likelihood of impact on yourself, giving you more time to recover and change all the passwords affected.

But the threat model still stands.  If you don’t trust other people to maintain your passwords for you, then you need to manage them yourself, in a book or in a locally sourced piece of software, and you need to sort out syncing for yourself. 


## [What We Do in the /etc/shadow – Cryptography with Passwords - Dhole Moments ](https://soatok.blog/2022/12/29/what-we-do-in-the-etc-shadow-cryptography-with-passwords/)

[https://soatok.blog/2022/12/29/what-we-do-in-the-etc-shadow-cryptography-with-passwords/](https://soatok.blog/2022/12/29/what-we-do-in-the-etc-shadow-cryptography-with-passwords/)

> When I write about cryptography, my goal is always to be clear, concise, and helpful. I want whoever reads my writing to, regardless of their level of expertise, walk away more comfortable with the subject matter.
> 
> At minimum, I want you to be able to intuit when you need to ask an expert for help, and have a slightly better understanding of how to word your questions to get the answer you need. In an ideal world, you’d even be able to spot the same kind of weaknesses I do in cryptography designs and implementations after reading enough of this blog. **I can’t do that with password-based cryptography.** The use-cases and threat models are too varied to make a clear-cut recommendation, and it’s too complicated to parcel out in a way that doesn’t feel reductive or slightly contradictory. This leads to too many caveats or corner cases. **Passwords suck.** If you ask a password cracking expert and describe your use case, you’ll likely get an opinionated and definitive answer. But every time I’ve asked _generally_ about this subject, without a specific use case in mind, I got an opinionated answer followed by a long chain of caveats and alternatives. **TL;DR** Password-Based Cryptography is a mess.
> 
> If you’re not aware of the history of the field and the technical details that went into the various cryptographic algorithms that experts recommend today, it’s very easy to say something wrong that sounds correct to an untrained ear.
> 
> At the end of the day, the biggest risk you face with password-based cryptography is _not using a suitable algorithm in the first place_ , rather than using a less optimal algorithm.
> Experts have good reasons to hate PBDKF2 (slow for defenders, fast for attackers) and SRP (we have better options today, which also come with actual security proofs), but they certainly hate unsalted SHA1 and Triple-DES more.
> 
> My only real contribution to this topic is an effort to make it easier to talk about to non-experts by offering a new term for the superset of all of these password-based algorithms: Password-Based Cryptographic Functions. 


This is a fairly deep and slightly frustrating read at times, but it does a good job of summarising just why it’s so hard to talk about cryptography with passwords.  

Lots of the advice and recommendations that float around the internet as “good practice” are dated, or so dependent on context that they become bad practice in a number of places.

Of course this is all still (mostly) technical advice on how to store passwords in your system, the reality is that users will create weak passwords, will reuse passwords and many of the cryptographic tricks won’t help against modern phishing and password replay tricks either.

The essence of this article is that there’s a lot of ways to do password hashing wrong, and a few contextual ways you can do it with reasonably positive tradeoffs, but always remember that it’s just one part of the security story. 


## [Disk encryption in AWS is close to useless and potentially harmful | Mellow Root ](https://tmp.bearblog.dev/disk-encryption-aws-is-close-to-useless-and-potentially-harmful/)

[https://tmp.bearblog.dev/disk-encryption-aws-is-close-to-useless-and-potentially-harmful/](https://tmp.bearblog.dev/disk-encryption-aws-is-close-to-useless-and-potentially-harmful/)

> Old-school compliance requires your data to be encrypted, which is great in case someone steals your disk. This compliance has followed to the cloud even though you don't even own the disk, instead you check a box in the AWS web interface and now your data is encrypted.
> 
> But what problems does it solve? Are you worried about someone breaking into the AWS data center, stealing the specific disks your data is stored on, and restoring and analyzing the disk data to target your organization? Just [imagine how much effort](https://tmp.bearblog.dev/make-attacking-not-worth-the-effort/) such an attack would take. 


This is one of my bugbears.  There is some value to on-disk encryption for a number of situations; local devices, backups, relocatable disk stores and so on.

But for working disk in cloud instances, chances are that the attacks in 2023 are unfeasible or the encryption key is stored in memory somewhere.

You’ll have difficulty with compliance systems if you don’t check that box, but in reality, I’m not convinced that it’s buying you all that much a lot of the time.

(The trick of course is not throwing the baby out with the bathwater and knowing when those times when it’s really important are) 


## [The Security Design of the AWS Nitro System - The Security Design of the AWS Nitro System ](https://docs.aws.amazon.com/whitepapers/latest/security-design-of-aws-nitro-system/security-design-of-aws-nitro-system.html)

[https://docs.aws.amazon.com/whitepapers/latest/security-design-of-aws-nitro-system/security-design-of-aws-nitro-system.html](https://docs.aws.amazon.com/whitepapers/latest/security-design-of-aws-nitro-system/security-design-of-aws-nitro-system.html)

> This paper provides a high-level introduction to virtualization and the fundamental architectural change introduced by the Nitro System. It discusses each of the three key components of the Nitro System, and provides a demonstration of how these components work together by walking through what happens when a new [Amazon Elastic Block Store](http://aws.amazon.com/ebs/) (Amazon EBS) volume is added to a running EC2 instance. The whitepaper discusses how the Nitro System, by design, eliminates the possibility of administrator access to an EC2 server, the overall passive communications design of the Nitro System, and the Nitro System change management process. Finally, the paper surveys important aspects of the EC2 system design that provide mitigations against potential side-channels issues that can arise in compute environments. 


This is a nice guide to how AWS has built the Nitro system which underpins the latest generation of hypervisor virtual machines in AWS.

Selecting one of the nitro VM’s will give you increased confidence in the security of the hypervisor behind the VM and how Amazon as the supplier can interact with and affect the machines. 


## [Threat-Report-on-the-Surveillance-for-Hire-Industry.pdf ](https://about.fb.com/wp-content/uploads/2022/12/Threat-Report-on-the-Surveillance-for-Hire-Industry.pdf)

[https://about.fb.com/wp-content/uploads/2022/12/Threat-Report-on-the-Surveillance-for-Hire-Industry.pdf](https://about.fb.com/wp-content/uploads/2022/12/Threat-Report-on-the-Surveillance-for-Hire-Industry.pdf)

> Since publishing our first threat report a year ago, we have continued to investigate and
> take actions against spyware vendors around the world, including in China, Russia, Israel,
> the United States and India, who targeted people in about 200 countries and territories.
> 
> Our threat research shows that the global surveillance-for-hire industry continues to
> grow and indiscriminately target people – including journalists, activists, litigants and
> political opposition – to collect intelligence, manipulate and compromise their devices and
> accounts across the internet.
> 
> We disabled their accounts, blocked their infrastructure from our platform, shared our
> findings with security researchers, other platforms and policymakers, issued cease and
> desist letters demanding that they immediately stop violating activity, and also alerted
> people who we believe were targeted to help them strengthen the security of their
> accounts. 


It’s really easy to assume when reading the cybersecurity news, that NSO Group and Candiru are the “big bad wolves” of the cybersecurity industry.  But in reality they are just the most notorious and probably the most advanced.

This report from Meta sets out a number of the other organisations, many of whom are smaller, more targeted, but are also just the high end actors in this space.  You should assume, from a threat modelling perspective, that this sort of organisation exists and that it can be commercially incentivised to look at your users.

In essence, the genie is out of the bottle, and like it or not, but this industry will continue to grow in the years to come. 


## [The Games People Play With Cash Flow - Commoncog ](https://commoncog.com/cash-flow-games/)

[https://commoncog.com/cash-flow-games/](https://commoncog.com/cash-flow-games/)

> A couple of months ago, a friend sent me a blog post titled [_Startups Shouldn’t Raise Money_](https://ensorial.com/2020/dont-raise-money/) , over at a website called [ensorial.com](http://ensorial.com/) . I thought that the post was tightly argued and reasonably put together, with each proposition leading logically and coherently to the next. I also noticed that the author had taken the time to construct their argument from first principles … which meant it was difficult to refute any individual clause in their chain of reasoning.
> 
> But I also thought it was wrong. I told my friend as much.
> 
> “How is it wrong?” he immediately challenged.
> 
> “Well …” I began. And then I stopped. I realised I didn’t have a good argument for _why_ it was wrong. Every axiom and intermediate proposition were ideas that I agreed with. And it wasn’t so simple as the conclusion being flat out mistaken — you _could_ probably run a small, successful internet business using the ideas laid out in the posts’s argument (internet-based businesses tend to be simpler to manage, and there are many niches you can occupy).
> 
> […] **How First Principles Thinking Fails, Part 2** I’ve spent most of this essay on the nuances of cash flow, which is kind of a joke, given that the goal of this piece is to demonstrate how first principles thinking fails. But I wanted to give you a real world example, and the [ensorial.com](http://ensorial.com/) blog post happened to be the one essay that started it all.
> 
> So I guess the joke’s on me.
> 
> I think it’s worth asking at this point: what are the consequences of believing in a ‘less useful’ argument about the world? What happens if you read the [ensorial.com](http://ensorial.com/) ’s argument as fact?
> 
> Well, for starters, it might mean being limited by your beliefs. It might mean chasing business ideas that have no hope of becoming successful, because structurally they call for external capital; it might mean ignoring alternative sources of capital, because they don’t fit into neat buckets like ‘VC’ or ‘angel’ or ‘venture debt’.
> 
> But of course it might not mean any of that. You could just as well bootstrap a tiny, successful internet business selling Wordpress plugins or Shopify themes, believing that ‘startups shouldn’t raise capital’. You would then never need to update your beliefs, because those are perfectly sufficient for a small, independently-run business.
> 
> And that’s fine.
> 
> Ultimately, we hold beliefs that are good enough for our goals. We only re-examine them when we discover that they no longer serve us in the pursuit of our ambitions. If the [ensorial.com](http://ensorial.com/) author achieves success with this belief; more power to them.
> 
> I’ve mentioned in my previous piece that the most pernicious form of failure for first principles thinking occurs when you start from an incomplete set of axioms. I argued that this was a pernicious because you cannot easily detect a mistake from the structure of your argument; you must observe reality to see how well your beliefs maps to practice. 


This is both an interesting essay about the role of financial planning and cashflow in running a business (something many people have never thought about, and can be quite insightful when trying to reason about why a company might do <insert daft thing here>).

But furthermore, this essay really talks about how we build arguments out of axioms of truthy statements, and build on top of those.  Of course, we cannot know all the axioms that we don’t know, and may not even know about, and as such our arguments may not always be relevant.  This is why context matters so much when you set “good practice” or whatever, so that people can directly understand the axioms you’ve built your practice on. 


## [GitHub - cisagov/ScubaGear: Automation to assess the state of your M365 tenant against CISA's baselines ](https://github.com/cisagov/ScubaGear)

[https://github.com/cisagov/ScubaGear](https://github.com/cisagov/ScubaGear)

> **SCuBA M365 Security Baseline Assessment Tool** Developed by CISA, this assessment tool verifies that an M365 tenant’s configuration conforms to the policies described in the SCuBA Minimum Viable Secure Configuration Baseline documents. 


How do you know if your software is configured the way it should be, whether it aligns to policy?

The ideal way, in a devops world, is to have the policy encoded as code and the ability to execute that code to compare the current configuraiton against the desired configuration.

But too few agencies and regulators release that configuration in a way that can be tested like that, so every organisation regulated by them has to do that work over and over again.  There’s lots of good reasons for that, some systems are different for good contextual reasons and there’s lots of underlying technology choices that the regulator doesn’t care about.

But this from CISA is a great example of trying to lift up the baseline of the most common configurations.  If this tool doesn’t work for you, you can go through the issues and work out whether there’s a business and context dependant exception that applies, or whether you need to adjust your config to match. 


## [Product vs. Policy - Silicon Valley Product Group : Silicon Valley Product Group ](https://www.svpg.com/product-vs-policy/)

[https://www.svpg.com/product-vs-policy/](https://www.svpg.com/product-vs-policy/)

> For the vast majority of products out there, policy plays a relatively minor role, and it’s simply referred to as _business rules_ .
> 
> These rules are usually pretty pedestrian.  Things like tax rates – or even whether you collect taxes.  Merchandise return policies.  Do I need to provide a credit card in order to book a table for a party of 10 at a restaurant?  Can I then cancel that reservation without a penalty? Will we share the data we collect?
> 
> But in some products, the policy can be extremely consequential.  
> 
> When handled appropriately by the product organization, the policy is an integral part of the offering, and in providing the desired value to customers:
> 
> * This is why eBay has a [carefully crafted reputation system](https://www.ebay.com/help/policies/feedback-policies/feedback-manipulation-policy?id=4231) at the foundation of its marketplace.
> * Or even controversial capabilities such as Uber’s [surge pricing](https://www.uber.com/us/en/marketplace/pricing/surge-pricing) can actually improve the health of a marketplace.
> * It is also why Apple has a very people and time-intensive process for reviewing apps that have been [submitted to the app store](https://developer.apple.com/app-store/review/guidelines/) .
> 
> But in too many companies, the product organization has not taken policy seriously enough, and the consequences can be seriously damaging, or even tragic:
> 
> * You’ve all seen the role of policy plays in content moderation systems like [Twitter](https://help.twitter.com/en/rules-and-policies/twitter-rules) .
> * Lest we forget what happens when API access policy is not taken seriously, as was the case with the [Facebook API](https://apiacademy.co/2018/06/how-the-facebook-api-led-to-the-cambridge-analytica-fiasco/) and Cambridge Analytica.
> * Or why Hertz filed false police reports against thousands of [their own customers](https://www.washingtonpost.com/business/2022/12/06/hertz-settlement-false-arrests-lawsuit/) .
> * Or why Tesla’s autopilot [has struggled to recognize motorcycles](https://www.rideapart.com/news/608732/why-tesla-autopilot-ignores-bikes/) .
> 
> One of the challenges of policy is that it’s usually necessary at the product organization level, as the product team level is usually too granular.  It generally needs to be addressed at the same level as the product vision and product strategy.  That is, it applies to all the product teams in that business. 


A useful take on the role of policy within technology product development systems.  In this case, Marty is mostly talking about service as a product, rather than products that you take home, but the business rules that you put in place in your products and services, whether those are offered to consumers or are internal services you offer to the rest of the organisation represent the direct encoding of business policy.

Do you let someone request a new device from IT easily?  Do they need a ticket to be signed off by someone more senior?  Can you request any kind of device or is there a drop down?  These are all policy decisions that are masqureading as product decisions.

It’s worth looking at the services you offer and determining whether you are encoding the right policies in those services. 


## [Albanian IT staff charged with negligence over cyberattack | AP News](https://apnews.com/article/iran-europe-middle-east-albania-tirana-39fce9b5fe112a43f8b35a533b6d29e8)

[https://apnews.com/article/iran-europe-middle-east-albania-tirana-39fce9b5fe112a43f8b35a533b6d29e8](https://apnews.com/article/iran-europe-middle-east-albania-tirana-39fce9b5fe112a43f8b35a533b6d29e8)

> TIRANA, Albania (AP) — Albanian prosecutors on Wednesday asked for the house arrest of five public employees they blame for not protecting the country from a cyberattack by alleged Iranian hackers.
> 
> Prosecutors said the five IT officials of the public administration department had failed to check the security of the system and update it with the most recent antivirus software.
> 
> They are accused of “abuse of post,” which can attract a prison sentence of up to seven years.


([Joel](https://twitter.com/joelgsamuel)) Well, thats quite the route to take.

I have seen no evidence of Data Protection (GDPR, et al) fines leading to custodial sentences: the usual issue is someone is fired or moved around, and perhaps someone on the board steps down potentially forfeiting shares/equity. I can't immediately think of a custodial sentence for a 'victim' in a breach either, so this sets a whole new tone.

I don't see this approach being taken by the US DoJ or UK Crown Prosecution Service even if there was a clear criminal basis created ... that said, something about it makes me wonder if it being _possible_ (even if unlikely to be prosecuted) would lead to better ownership and accountability, particularly irrespective of supply chain contracts ("Well, the contract didn't say we had to patch it"). There are an awful lot of MSPs, SIs, IT managers and IT engineers who don't care about security even when told what is expected (and required) of them, and a little stick might be needed to instil some motivation where the carrot and education has not.


