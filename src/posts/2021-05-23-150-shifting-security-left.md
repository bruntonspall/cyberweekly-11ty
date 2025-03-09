---
title: "150 - Shifting security left"
date: 2021-05-23
description: "Shift security left is one of those mantras that sounds great, but in reality, struggles to deliver on the promise."
permalink: /shifting-security-left/
---

Shift security left is one of those mantras that sounds great, but in reality, struggles to deliver on the promise.

If you speak to some of the luminaries of the original secdevops/devsecops/ruggeddevops movements, they'll explain that development teams working within large companies want to build secure software, but are hampered by security models that simply don't work for them.

I've railed myself at the idea that a security architect will take a look at your architecture as part of the release process, because those gates either become barriers to releasing software, or cumbersome and unwieldy.  Of course, in an organisation that writes all the software using traditional v-model software delivery models, the idea that someone can review your architecture at the end of your design phase isn't such an issue.

But in a modern iterative and dare I say it, agile, software development company, the mantra is release early, release often, and security gates will simply be ignored.  The only way it seems, to those people, to ensure that security is involved is to shift those security activities left in the plan, making them happen earlier.

Of course, to the 99% of security people who have never heard of agile, don't care about it, and think in terms of compliance and audit, this is meaningless.  It's not about rethinking the work that they are doing, it's simply about fixing that age old problem "If people had involved me earlier in the project, we wouldn't be in this mess", which is of course always silently followed by "because I would have said 'NO' much earlier" rather than any pretence that they would have contributed to a better solution.

Shift security left isn't about ensuring that the same security decisions are engaged earlier in the process, it's about working out how security as a fundamental principle can be applied earlier in the life cycle.  That means totally rethinking how security works, it cannot be about compliance and audit if you are engaging before there is something to look at.  It's about bringing experience and expertise to the early discussions.  It's about asking questions about what we want to achieve and working out how we can best achieve that.

## [Executive Order on Improving the Nation's Cybersecurity | The White House](https://www.whitehouse.gov/briefing-room/presidential-actions/2021/05/12/executive-order-on-improving-the-nations-cybersecurity/)

[https://www.whitehouse.gov/briefing-room/presidential-actions/2021/05/12/executive-order-on-improving-the-nations-cybersecurity/](https://www.whitehouse.gov/briefing-room/presidential-actions/2021/05/12/executive-order-on-improving-the-nations-cybersecurity/)

> But cybersecurity requires more than government action.  Protecting our Nation from malicious cyber actors requires the Federal Government to partner with the private sector.  The private sector must adapt to the continuously changing threat environment, ensure its products are built and operate securely, and partner with the Federal Government to foster a more secure cyberspace.  In the end, the trust we place in our digital infrastructure should be proportional to how trustworthy and transparent that infrastructure is, and to the consequences we will incur if that trust is misplaced.
> 
> Incremental improvements will not give us the security we need; instead, the Federal Government needs to make bold changes and significant investments in order to defend the vital institutions that underpin the American way of life.  The Federal Government must bring to bear the full scope of its authorities and resources to protect and secure its computer systems, whether they are cloud-based, on-premises, or hybrid. 


This has picked up some really interesting areas:

1. Standardising contract language to allow suppliers to share information about compromise
2. Modernising government infrastructure (including the development of cloud strategies)
3. Improving supply chain security including a definition of a software bill of materials
4. Establishing a Cyber Safety Review Board, similar to the much lauded National Transportation Safety Board which reviews all aviation safety incidents
5. Standardising the government playbook for vulnerability and incident response (i.e. ensure that everyone can patch)
6. Definitions around logging and EDR to improve detection capability
7. Some vague handwaving around log retention for post-incident investigation (this feels the least well defined)

As a Presidentially signed strategy, this is quite the vision, of course the questions that will follow will depend on whether federal departments have the cash or capability to actually implement any of this!

Of course the critical thing to remember is that in the US, the actual decisions will be taken by agencies and departments who are funded totally differently, which means that unless this executive order comes with both money and power for a central authority, it will likely fail to be delivered.  What's unclear at the moment is just how the rest of the federal government will respond to any of this, and if the federal government can't respond, you can expect a similarly lacklustre response from much of industry as well.


## [Prime targets: Governments shouldn’t go it alone on cybersecurity | WeLiveSecurity](https://www.welivesecurity.com/2021/04/29/prime-targets-governments-shouldnt-go-it-alone-on-cybersecurity/)

[https://www.welivesecurity.com/2021/04/29/prime-targets-governments-shouldnt-go-it-alone-on-cybersecurity/](https://www.welivesecurity.com/2021/04/29/prime-targets-governments-shouldnt-go-it-alone-on-cybersecurity/)

> The question is, where to start? Drawing also on its own experience as a target for threat actors, ESET has learned that getting the basics right really is the best foundation for securing your organization. These days, it should begin with understanding where your key assets are – whether a home working laptop or a cloud server – and ensuring they’re protected and correctly configured at all times. Prompt patching, regular backups, endpoint protection and “zero trust” access for all home workers should also be table stakes. After all, the distributed workforce is your most exposed front in the war on cybercrime.
> 
> Next, follow international standards, such as ISO 27001, to institute best practices for information security management. It’s a good starting point that you can build on to align with key regulatory compliance requirements. Concerned at how to prioritize so many security activities amidst such a fast-moving landscape? Use risk management and measurement as your guide. Other critical steps include “shifting security left” in your software development lifecycle (SDLC) – to accelerate digital transformation without increasing cyber-risk.


I'm torn between this being good advice and this being more of the same advice that hasn't worked so far.

In particular the emphasis in security companies and talking heads about shifting security left feels like a desire to push cognitive load to somewhere else in the organisation.  I'm not a fan of "shift security left", I'm a fan of "give people secure defaults".


## [Annual threat assessment of the US intelligence community [pdf]](https://www.odni.gov/files/ODNI/documents/assessments/ATA-2021-Unclassified-Report.pdf)

[https://www.odni.gov/files/ODNI/documents/assessments/ATA-2021-Unclassified-Report.pdf](https://www.odni.gov/files/ODNI/documents/assessments/ATA-2021-Unclassified-Report.pdf)

> Cyber threats from nation states and their surrogates will remain acute. Foreign states use cyber operations to
> steal information, influence populations, and damage industry, including physical and digital critical
> infrastructure. Although an increasing number of countries and nonstate actors have these capabilities, we
> remain most concerned about Russia, China, Iran, and North Korea. Many skilled foreign cybercriminals
> targeting the United States maintain mutually beneficial relationships with these and other countries that
> offer them safe haven or benefit from their activity.
> 
> States’ increasing use of cyber operations as a tool of national power, including increasing use by militaries around
> the world, raises the prospect of more destructive and disruptive cyber activity. As states attempt more aggressive
> cyber operations, they are more likely to affect civilian populations and to embolden other states that seek
> similar outcomes.
> 
> Authoritarian and illiberal regimes around the world will increasingly exploit digital tools to surveil their citizens,
> control free expression, and censor and manipulate information to maintain control over their populations. Such
> regimes are increasingly conducting cyber intrusions that affect citizens beyond their borders—such as
> hacking journalists and religious minorities or attacking tools that allow free speech online—as part of their
> broader efforts to surveil and influence foreign populations.
> 
> Democracies will continue to debate how to protect privacy and civil liberties as they confront domestic
> security threats and contend with the perception that free speech may be constrained by major technology
> companies. Authoritarian and illiberal regimes, meanwhile, probably will point to democracies’ embrace of
> these tools to justify their own repressive programs at home and malign influence abroad.
> 
> During the last decade, state sponsored hackers have compromised software and IT service supply chains, helping
> them conduct operations—espionage, sabotage, and potentially prepositioning for warfighting.


This is a good annual report that is always worth a read despite the us centricism of the report (which should be no surprise).

Interesting this year is that although cybersecurity gets a mention in many of the existing country sections as you'd expect, it's also listed here under Transnational issues along with COVID and Emerging Technology among others.  That indicates that the "rising tide floats all boats" concept, or a steady drip of cyber capabilities down to second and thirds tier nation states as well as organised crime and other well funded entities is well underway.  

I also enjoyed the nod towards the idea that "some of these things are good when we do them, but bad when bad people do them" which remains a logical conundrum for lawful intercept and other state surveillance capabilities.


## [Jenkins Attack Framework | Accenture](https://www.accenture.com/us-en/blogs/cyber-defense/red-teaming-jenkins-attack-framework)

[https://www.accenture.com/us-en/blogs/cyber-defense/red-teaming-jenkins-attack-framework](https://www.accenture.com/us-en/blogs/cyber-defense/red-teaming-jenkins-attack-framework)

> Today we are releasing the Jenkins Attack Framework (JAF) to the public. JAF is an Accenture, internally developed, red team-oriented tool for interacting with Jenkins build servers. Jenkins[1] is an opensource build CI/CD pipeline tool that is commonly used in industry to manage building and testing code. It is of interest to red teamers because it often stores powerful credentials, company proprietary code, may have backdoor access into production environments, and often provides attackers with lateral movement and pivoting capabilities. This blogpost does not introduce any new vulnerabilities discovered in Jenkins, but rather demonstrates ways in which it can be abused by red team operators.


Sigh, I can't decide if I like this or not.  It's a lovely tool for pullling together a set of powerful attacks and information discovery operations that redteams will find useful.   On the other hand, I strongly suspect that many development teams out there will be vulnerable to all of this stuff, and I bet the attackers will get this before the building or defensive teams do.

This is worth getting your development teams to run against their Jenkins installs before an attacker does.


## [How to Successfully Hand Over Systems | SoundCloud Backstage Blog](https://developers.soundcloud.com/blog/how-to-successfully-hand-over-systems)

[https://developers.soundcloud.com/blog/how-to-successfully-hand-over-systems](https://developers.soundcloud.com/blog/how-to-successfully-hand-over-systems)

> In a product company, changes are inevitable so as to best support the strategy and the vision. Often during such a change, new teams are formed and other ones are restructured. While there are many challenges to be solved during a big change, there’s one in particular that’s often overlooked: system ownership.
> 
> Who will take ownership of the systems that were owned by a team that doesn’t exist anymore or that are better suited to be owned by another team? It’s in everyone’s interest that the ownership be given to a team familiar with the system’s domain, so that they can continue the maintenance and evolution.
> 
> Regardless of when the system handover will happen, how it’s executed is important, since the cost of failure can be high, and that could result in an outage or a significant amount of unplanned work.
> 
> [...]
> 
> I’m posting the complete guideline below not only to document what we did at SoundCloud, but also in hopes of providing a template for other companies to use when faced with a similar scenario.


This is a lovely template for system documentation to enable handovers.  I'd argue that this also works as a great induction document for new starters, as well as collectively, a great way to udnerstand the systems that you have.

Starting with one of these before the system goes into production, and taking time once a month, or whenever there's an outage or incident to update or maintain it means that you'll have nice clear instructions on how to operate and maintain the system


## [Is Complexity the Enemy of Security?](https://www.philvenables.com/post/is-complexity-the-enemy-of-security)

[https://www.philvenables.com/post/is-complexity-the-enemy-of-security](https://www.philvenables.com/post/is-complexity-the-enemy-of-security)

> In reasoning about complexity and security we also have to deal with the fact that security is not something you can design in to complex systems. Rather, security is an emergent property of a complex system. You don’t do security. You do things to get security.  
> 
> 
> Even if we have what we might describe as a simple system then that can still be quite hard to secure. Simple systems can be equally confusing and hard to manage if not designed well.
> 
> [...]
> 
> Complexity is not the enemy of security. Bad design is. So, what are some examples of good design principles.


This is a good argument around natural inherent complexity, along with a set of design principles that can help manage and surface complexity so it can be sorted.


## [Sending webhooks securely](https://www.ameyalokare.com/technology/webhooks/2021/05/03/sending-webhooks-securely.html)

[https://www.ameyalokare.com/technology/webhooks/2021/05/03/sending-webhooks-securely.html](https://www.ameyalokare.com/technology/webhooks/2021/05/03/sending-webhooks-securely.html)

> Webhooks are a popular way to glue web applications together. On the surface, they’re just HTTP requests with a twist – the “customer” in browser apps is usually the client whereas with webhooks, the server (consumer) is the “customer”. This creates some peculiar security implications as we shall see. Turns out it’s quite tricky to implement a secure webhook sender – over the past few months, I’ve found vulnerabilities even in popular apps that send webhooks. This post is aimed at guiding developers to implement secure webhook senders.


Useful guide to some rather nifty attacks that can be carried out on webhook implementations, and thoughts on how to protect against those attacks.


## [Shifting cost optimisation left: Spotify Backstage Cost Insights – James Governor's Monkchips](https://redmonk.com/jgovernor/2021/04/28/shifting-cost-optimisation-left-spotify-backstage-cost-insights/)

[https://redmonk.com/jgovernor/2021/04/28/shifting-cost-optimisation-left-spotify-backstage-cost-insights/](https://redmonk.com/jgovernor/2021/04/28/shifting-cost-optimisation-left-spotify-backstage-cost-insights/)

> Spotify has almost five hundred engineering teams today. It does about twenty thousand deployments a day across thousands of micro services. That’s a huge amount of complexity to manage, and it’s not really amenable to simply pointing at spreadsheets and saying: “we need to fix this”. Instead Spotify hacked the culture. It went back to basics and thought about cost as a problem to be solved with its engineering culture.
> 
> Spotify engineering teams are used to having a lot of autonomy, so the company couldn’t just introduce new cost guardrails as a top down concern. Autonomy is a core value at the firm, so Cost Insights was built with that in mind. Therefore the Cost team tried to foster a culture where optimisation would be fun.


Rereading the backstage information after Quiney's takedown of it above, one thing that is interesting here is the difference between "Build a portal to intermediate between the developer and the tooling", versus "do the hard work to provide analysis functions for users as well".

This system of providing people with direct access, but automating the 80% of common tasks that people do is the ultimate in enabling autonomy within disparate teams.


## [Developer Portals Are an Anti-Pattern - Last Week in AWS](https://www.lastweekinaws.com/blog/developer-portals-are-an-anti-pattern/)

[https://www.lastweekinaws.com/blog/developer-portals-are-an-anti-pattern/](https://www.lastweekinaws.com/blog/developer-portals-are-an-anti-pattern/)

> The first (and most selfish) of them is that it robs a company’s engineers of an opportunity to develop reusable skills. If you become an expert in wrangling the internal developer portal that your employer has built, that’s not likely to serve you well at basically any other company on the planet.
> 
> Admittedly, “it makes it harder for me to quit” isn’t the most compelling reason an engineer can take to their management in order to advocate against such a thing, so let’s explore a few more.
> 
> Second, developer portals inherently lag the underlying service’s capabilities. If AWS, GCP or whomever enhances a service, it’s up to the developer portal’s maintainer to update and reflect the change (assuming they’re reading Last Week in AWS so they can catch it!).
> 
> Otherwise, the portal will rely overmuch on its “plugin-driven” model, which feels like a polite way of saying “pull requests welcome”—which, in turn, is a polite way of telling people to screw off and build it themselves.
> 
> That may be okay if you’re viewing developer portals purely through the lens of IaaS provisioning of containers, VMs, storage, and load balancers. But it begins to look very odd when you’re tying it in to CloudFlare domains, PagerDuty alerting, and higher-level differentiated offerings (like last week’s Nimble Studio release, as an example).
> 
> The third failure mode pops up when you’re viewing developer portals through the lens of just IaaS: They distill down to Kubernetes without the upsides.
> 
> “Wait, Kubernetes has upsides?” sounds like something you’d expect me to rejoin with, and yes, it absolutely does. It’s broadly deployed, you can find a bunch of folks to run it for you, and just because it looks super-strange to the underlying cloud provider as a monolithic application with very odd behavior patterns doesn’t mean it’s completely without merit.


A great argument against internal developer facing portals that attempt to manage developers access to the supplier provided web based control panels.

The summary of this is that you should just ensure that your engineers can access the control panels provided by the tools that they are being asked to use.


## [GitHub - salesforce/DazedAndConfused](https://github.com/salesforce/DazedAndConfused)

[https://github.com/salesforce/DazedAndConfused](https://github.com/salesforce/DazedAndConfused)

> For each repository, a results array will be generated.
> 
> file indicates which manifest file was scanned.
> vulnerable - this package exists internally but does not exist in public repositories and is possibly vulnerable to being taken over
> sus - this package seems like it should be private and exist only internally, but exists in public repositories and could indicate an in progress exploit


On the back of those dependency confusion hacks a few months back, this is a tool that looks your dependency trees and your servers and tries to reason out whether there are any underlying issues that are there, as well as identifying any private packages that look to have leaked out.


