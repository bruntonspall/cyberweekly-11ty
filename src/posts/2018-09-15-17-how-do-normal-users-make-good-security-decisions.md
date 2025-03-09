---
title: "17 - How do normal users make good security decisions?"
date: 2018-09-15
description: "Most security products exist in what economists call a Market for Lemons (https://en.wikipedia.org/wiki/The_Market_for_Lemons), which means that purchasers lack the ability to tell a good product from a bad product."
permalink: /how-do-normal-users-make-good-security-decisions/
---

Most security products exist in what economists call a Market for Lemons (https://en.wikipedia.org/wiki/The_Market_for_Lemons), which means that purchasers lack the ability to tell a good product from a bad product.
The market theory suggests that when there is an information assymetry, then there tends to exist an economic incentive for vendors to push bad security solutions on the purchasers.
How would a normal person select a VPN company if they wanted to follow the advice to "Not use public wifi without a VPN".  They'd google for "free VPN" and they'd struggle to determine what good looks like.  Is it a flashy website, a trust mark of some kind, a personal recommendation?  Maybe they'd select a VPN from a known major brand, or maybe they'd just find the cheapest one out there.

As security professionals, we have to ensure that our advice is actionable and usable, whether it be the advice in a pentest report, advice to a friend, or technical guidance on how to implement something in a secure way.
Although the reality for all situations means that much security advice is contextual, when we try to load the context onto the user, it becomes unfair.  So maybe we should say "It depends" a lot less than we do, even though we know that the real answer is complex and does depend, if for that user, there is a simple answer that works 99% of the time, then we should give that.

## [Why big companies squander good ideas](https://www.ft.com/content/3c1ab748-b09b-11e8-8d14-6f049d06439c)

[https://www.ft.com/content/3c1ab748-b09b-11e8-8d14-6f049d06439c](https://www.ft.com/content/3c1ab748-b09b-11e8-8d14-6f049d06439c)

> Despite alienating the army top brass, Fuller was handed a unique opportunity to advance the cause of tanks in the British army: he was offered the command of a new experimental mechanised force in December 1926.  There was just one problem: he would have to step away from his single-minded focus on the tank, also taking command of an infantry brigade and a garrison. In short, Fuller would have to get into the organisational headaches that surround any architectural innovation. He baulked, and wrote to the head of the army demanding that these other duties be carried out by someone else, eventually threatening to resign. The position was awarded to another officer, and Fuller’s career never recovered. His petulance cost him — and the British army — dearly. Architectural innovations can seem too much like hard work, even for those most committed to seeing them succeed.


This sounds so familiar to me around digital disruptors and transformation communities.  While those working in digital disruption are often gifted and brilliant at the thing they care about, their political and integration skills are often lacking. This failure to acknowledge or carry out the hard work of integrating the ideas into the rest of the business, with those who "don't get it", the disruption then fades or is under accepted by the organisation.


## [Digital resources for governments](https://apolitical.co/solution_article/the-digital-government-atlas-the-worlds-best-tools-and-resources/)

[https://apolitical.co/solution_article/the-digital-government-atlas-the-worlds-best-tools-and-resources/](https://apolitical.co/solution_article/the-digital-government-atlas-the-worlds-best-tools-and-resources/)

> With this collection of resources and toolkits, you’ll be able to work out how to launch a digital revolution in your department, and find some of the tools to help you do it


This is a good list of various digital toolkits, github repos, data repositories and general government improvement from around the world.  I notice that not a single resource has been highlighted on modern digital security


## [How an inmate hacker turned a prison upside down - The Verge](https://www.theverge.com/2017/10/10/16447264/prison-hacker-recycled-computer-fraud-ohio-marion-transkiy)

[https://www.theverge.com/2017/10/10/16447264/prison-hacker-recycled-computer-fraud-ohio-marion-transkiy](https://www.theverge.com/2017/10/10/16447264/prison-hacker-recycled-computer-fraud-ohio-marion-transkiy)

> Transkiy was being questioned about an extraordinary form of contraband. Someone had hidden refurbished computers in the ceiling of the prison. They’d somehow obtained a login to the prison’s network, gaining access to the inner workings of the facility, including databases on inmates and the tools for creating passes needed to enter restricted areas. The computers also granted access to the outside world, which someone had used to apply for credit cards using the stolen identity of a prisoner. The scheme extended from the prison, to a community nonprofit, to multiple banks — all done under the noses of an oblivious prison staff.


This is a lovely story showing how one can abuse a system and the ways you can slip through the cracks of a system if you know what you are doing.


## [Mac App Store apps are stealing user data - Malwarebytes Labs | Malwarebytes Labs](https://blog.malwarebytes.com/threat-analysis/2018/09/mac-app-store-apps-are-stealing-user-data/)

[https://blog.malwarebytes.com/threat-analysis/2018/09/mac-app-store-apps-are-stealing-user-data/](https://blog.malwarebytes.com/threat-analysis/2018/09/mac-app-store-apps-are-stealing-user-data/)

> It could be argued that it is useful for antivirus software to collect certain limited browsing history leading up to a malware/webpage detection and blocking. But it is very hard to argue to exfiltrate the entire browsing history of all installed browsers regardless of whether the user has encountered malware or not. In addition, there was nothing in the app to inform the user about this data collection, and there was no way to opt out of this data collection.


A lot of the writeups of this incident seemed to focus on "Stealing data" and "China servers - bad" and jump to conclusions without acknowledging that there are potentially valid reasons for the attempt to get the data, and that modern cloud environments make geographic ownership a potential red herring.  This writeup does acknowledge that, and does a good job of explaining why this app and series of apps goes well beyond the pale in stealing data.


## [Cisco's Talos Intelligence Group Blog: Vulnerability Spotlight: CVE-2018-3952 / CVE-2018-4010 - Multi-provider VPN Client Privilege Escalation Vulnerabilities](https://blog.talosintelligence.com/2018/09/vulnerability-spotlight-Multi-provider-VPN-Client-Privilege-Escalation.html)

[https://blog.talosintelligence.com/2018/09/vulnerability-spotlight-Multi-provider-VPN-Client-Privilege-Escalation.html](https://blog.talosintelligence.com/2018/09/vulnerability-spotlight-Multi-provider-VPN-Client-Privilege-Escalation.html)

> This code checks if the configuration file sent by the user contains a line starting by plugin, script-security, up or down. These are all the methods to execute code or commands through OpenVPN.


This is not how to patch code that reads files!
More importantly, we security people tell people that they should use a VPN all the time, without giving them any tools or capability to determine a good VPN provider from a bad one.  These two VPN providers are big names and good at this stuff, and they had vulnerabilities in their client package, so a user has to be able to assure themselves that the VPN provider won't sniff their traffic, and that the client is correctly configured.  This means "Use a VPN" isn't usable security advice for normal people


## [Facebook will pull its data-collecting VPN app from the App Store over privacy concerns - The Verge](https://www.theverge.com/2018/8/22/17771298/facebook-onavo-protect-apple-app-store-pulled-privacy-concerns)

[https://www.theverge.com/2018/8/22/17771298/facebook-onavo-protect-apple-app-store-pulled-privacy-concerns](https://www.theverge.com/2018/8/22/17771298/facebook-onavo-protect-apple-app-store-pulled-privacy-concerns)

> Onavo Protect also allegedly violated a part of the iOS developer agreement that regulates how app makers make use of data outside the core function of the software. Onavo Protect is a VPN service, and yet Facebook has been using the traffic routed through its private servers for broad analytic purposes.


How do users pick a VPN provider?  Maybe they select one from a known trusted large brand, such as Facebook.  They wouldn't be snooping on the traffic at all surely?  Oh right, nope


## [Serverless Red Team Infrastructure: Part 1, Web Bugs – MDSec](https://www.mdsec.co.uk/2018/09/serverless-red-team-infrastructure-part-1-web-bugs/)

[https://www.mdsec.co.uk/2018/09/serverless-red-team-infrastructure-part-1-web-bugs/](https://www.mdsec.co.uk/2018/09/serverless-red-team-infrastructure-part-1-web-bugs/)

> As red teamers, this provides a highly attractive proposition for certain components of the red team infrastructure as we no longer need to worry about provisioning, building or configuring servers. Indeed, serverless means you can programatically create new services as and when we need them in minutes and if a particular campaign becomes tainted, you can simply rinse and repeat to create new, unattributable infrastructure.


This is a smart use of serverless infrastructure, although I'm less happy about the assertion in here that "customer data is not secure in the cloud".
Building a small serverless app is simple today and takes 5 or 10 minutes.  Instead of reading about it and trying to understand it, why not just try to write something small and simple and run it for a while and get your head around it.


## [The British Airways Breach: How Magecart Claimed 380,000 Victims](https://www.riskiq.com/blog/labs/magecart-british-airways-breach/)

[https://www.riskiq.com/blog/labs/magecart-british-airways-breach/](https://www.riskiq.com/blog/labs/magecart-british-airways-breach/)

> What is interesting to note from the certificate the Magecart actors used is that it was issued on August 15th, which indicates they likely had access to the British Airways site before the reported start date of the attack on August 21st—possibly long before. Without visibility into its Internet-facing web assets, British Airways were not able to detect this compromise before it was too late.


This was a big deal, and I think we'll see a lot of this over the next year.  Whether financially incentivised criminal groups count as an "advanced persistent threat" or not, the ability to write custom javascript and to tamper with dependencies on servers to create credit card stealing vulnerabilities is here and available to criminal groups.
As far as I can see, things like SRI would help here, but so does having standalone infrastructure for your payments pages.  I'm looking forward to seeing if the PCI council issues any useful guidance on this at all.


## [AWS Parameter Store | Dave Hall Consulting](https://davehall.com.au/blog/dave/2018/08/26/aws-parameter-store)

[https://davehall.com.au/blog/dave/2018/08/26/aws-parameter-store](https://davehall.com.au/blog/dave/2018/08/26/aws-parameter-store)

> Amazon's System Manager Parameter Store provides a secure way of storing and managing secrets for your AWS based apps. Unlike Hashicorp Vault, Amazon manages everything for you. If you don't need the more advanced features of Secrets Manager you don't have to pay for them. For most users Parameter Store will be adequate.


This is a nice guide on using AWS Parameter Store in a secure way to store your secrets, which is plenty good enough for small to medium applications that just want to externalise simple secrets outside of their system


