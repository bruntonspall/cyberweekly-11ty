---
title: "10 - That’s edition 8 in octal"
date: 2018-07-28
description: "So this week we reach two milestones at more or less the same time.  This is the 10th newsletter, that's 10 weeks in a row compiling and sending this out, as well as reaching 100 subscribers this week, so huge thanks to everyone who subscribes, who is passing it onto friends, and the several hints this week for things to add."
permalink: /thats-edition-8-in-octal/
---

So this week we reach two milestones at more or less the same time.  This is the 10th newsletter, that's 10 weeks in a row compiling and sending this out, as well as reaching 100 subscribers this week, so huge thanks to everyone who subscribes, who is passing it onto friends, and the several hints this week for things to add.

There are increasing numbers of companies and people talking about the sort of holistic security that I've been talking about for years.  The Duo Security team inparticular (full disclosure, Rich Smith one of my coauthors is employed there) are on fire at the moment, constantly releasing great blog posts about how to do security in this new world, but I'm seeing more and more of it.  So this weeks release is mostly happy good news :)  I'm sure the cynical news stories will return next week.


## [Technical Intuition – Alix – Medium](https://medium.com/@alixtrot/technical-intuition-instincts-in-a-digital-world-a6bfda669a91)

[https://medium.com/@alixtrot/technical-intuition-instincts-in-a-digital-world-a6bfda669a91](https://medium.com/@alixtrot/technical-intuition-instincts-in-a-digital-world-a6bfda669a91)



"I didn’t want our organisational partners to learn to code, I wanted them to learn how to talk to developers. I didn’t want them to outsource complexity, I wanted them to learn what skills they need in-house, which they could contract out, and how that might change over time"


## [To Trust or Zero Trust? | Duo Security](https://duo.com/blog/to-trust-or-zero-trust)

[https://duo.com/blog/to-trust-or-zero-trust](https://duo.com/blog/to-trust-or-zero-trust)



"The important thing about trust is that it’s neither binary nor permanent. You don’t trust someone to do anything at all; you trust them to do a particular set of actions, on a particular system, perhaps on behalf of a particular entity (such as a third party accessing a client record as a member of one brokerage firm). And you don’t trust them forever; you trust them for as long as certain risk-related conditions are true. You might stop trusting them in cases where enough time has passed that their password might have been compromised, or when their endpoint becomes vulnerable to a certain exploit by virtue of its software becoming outdated.

This is the reason why network perimeter-based security is less than optimal: organizations tend to trust a user forever, to do anything, as long as they come from the right IP address and give the right password. We have known for a long time that open-ended trust is a bad idea, but given the available technology, it’s been a tough problem to address — until now."

This by Wendy Nather, is a great explanation of the problem of trust, including the explanation about different usages of the word trust, and why it's key to why the old model of bastion hosts and castle networks doesn't really work.  


## [The worst truism in information security - The Blagoblag](https://alexgaynor.net/2018/jul/20/worst-truism-in-infosec/)

[https://alexgaynor.net/2018/jul/20/worst-truism-in-infosec/](https://alexgaynor.net/2018/jul/20/worst-truism-in-infosec/)



"Just this week, a colleague invoked this, with the quip that those of us who've chosen defense must be pretty dumb, given the challenge of that task, and the possibility of an easier career in offense."
There is so much good in here, but I wanted to call out this attitude.  If you think the job of being an ethical hacker/red team in your organisation is to win, to just break stuff, then you are part of the problem.  The only reason you exist is to help the organisation, the business, and just breaking stuff and walking away is not helping.

If your red team has this attitude, then you should get rid of them and get a new red team.  A red teams job is about 10% breaking your stuff, and 90% sitting and working with the team to build a better defence.


## [You used to build a wall to keep them out, but now hackers are destroying you from the inside | WIRED UK](https://www.wired.co.uk/article/darktrace-insider-threats-hackers-security)

[https://www.wired.co.uk/article/darktrace-insider-threats-hackers-security](https://www.wired.co.uk/article/darktrace-insider-threats-hackers-security)



"Organisations are also vulnerable at many more points. The internet of things is rapidly expanding what security experts call “the attack surface”. Intruders can now enter an organisation through a vending machine, a smart thermostat or a TV, not to mention one of the many connected devices that employees carry or wear every day. The gatekeepers, outwitted and overrun, have responded like authoritarian leaders attempting to clamp down on crime, introducing increasingly draconian security policies. But when employees subsequently find it harder to work, innovate and experiment, the business suffers."

As it says.  I'd argue that it's not even the Internet of Things, it's people trying to work around the VPN, people using their iphones as hotspots, and people forwarding emails via their personal accounts that bypasses all of the "gatekeepers".  But everything else here, I think I agree with.


## [NIST Special Publication 800-63B](https://pages.nist.gov/800-63-3/sp800-63b.html#sec5)

[https://pages.nist.gov/800-63-3/sp800-63b.html#sec5](https://pages.nist.gov/800-63-3/sp800-63b.html#sec5)



"Verifiers SHOULD NOT impose other composition rules (e.g., requiring mixtures of different character types or prohibiting consecutively repeated characters) for memorized secrets. Verifiers SHOULD NOT require memorized secrets to be changed arbitrarily (e.g., periodically). However, verifiers SHALL force a change if there is evidence of compromise of the authenticator."

I was asked something this week which reminded me of this NIST standard.  If you are working with someone who insists that your passwords have complexity rules, maximum lengths or regular rotation, note that this is now strongly discouraged by a US Government standard.


## [Google - Site Reliability Engineering](https://landing.google.com/sre/book.html)

[https://landing.google.com/sre/book.html](https://landing.google.com/sre/book.html)



"The Site Reliability Workbook is the hands-on companion to the bestselling Site Reliability Engineering book and uses concrete examples to show how to put SRE principles and practices to work. This book contains practical examples from Google’s experiences and case studies from Google’s Cloud Platform customers. Evernote, The Home Depot, The New York Times, and other companies outline hard-won experiences of what worked for them and what didn’t."
This is a valuable addition to the SRE book, which I think is a great model for security teams as well as for any organisation moving from a small (<150 people) to medium/large (>300 people).


## [Twitter](https://threadreaderapp.com/thread/1021479347486699522.html)

[https://threadreaderapp.com/thread/1021479347486699522.html](https://threadreaderapp.com/thread/1021479347486699522.html)



"GDPR recognises that data collection in exchange for “better” advertising is essentially a transaction, but one which was being conducted without any freely-given informed consent"

This thread from Mo is a great description of the intent of GDPR, but also how it has been interpreted and implemented by news organisations in particular.
Showing users a list of hundreds of possible companies that might set cookies is definitely a breach of the intent of the law, and we'll see how the public and the ICO actually responds over time.


## [Google: Security Keys Neutralized Employee Phishing — Krebs on Security](https://krebsonsecurity.com/2018/07/google-security-keys-neutralized-employee-phishing/)

[https://krebsonsecurity.com/2018/07/google-security-keys-neutralized-employee-phishing/](https://krebsonsecurity.com/2018/07/google-security-keys-neutralized-employee-phishing/)



““Users might be asked to authenticate using their security key for many different apps/reasons. It all depends on the sensitivity of the app and the risk of the user at that point in time.”  “. This if true is an amazing protection against the most common attack mechanism for organisations. Before you go implement it at your org, note that they worked on the usability. You don’t get asked every time, you get asked for the key if there’s some reason for it. That matters in making this a success. 


## [Singapore Hack Is a Speed Bump for $9 Trillion Industry - Bloomberg](https://www.bloomberg.com/view/articles/2018-07-23/singapore-hack-is-a-speed-bump-for-9-trillion-industry)

[https://www.bloomberg.com/view/articles/2018-07-23/singapore-hack-is-a-speed-bump-for-9-trillion-industry](https://www.bloomberg.com/view/articles/2018-07-23/singapore-hack-is-a-speed-bump-for-9-trillion-industry)



"Lee himself signed up for the country’s digitization project, saying that doing so would improve the quality of care across medical professions, though he posted on Facebook that he was aware of the downsides.

Of course, I also knew that the database would be attacked, and there was a risk that one day despite our best efforts it might be compromised. Unfortunately that has now happened.

His calm response, rather than outrage, is appropriate among those trying to build the future of health care, though it’s scant consolation to people whose records were accessed. "


