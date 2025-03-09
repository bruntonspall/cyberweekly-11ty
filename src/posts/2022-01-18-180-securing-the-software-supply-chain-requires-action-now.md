---
title: "180 - Securing the software supply chain requires action now"
date: 2022-01-18
description: "There's a lot of noise around the \"software bill of materials\" concepts at the moment.  This work has been going for years, but really stepped up a gear after both Solarwinds and then log4shell compromises."
permalink: /securing-the-software-supply-chain-requires-action-now/
---

There's a lot of noise around the "software bill of materials" concepts at the moment.  This work has been going for years, but really stepped up a gear after both Solarwinds and then log4shell compromises.

Some people argue that investing into the SBOM toolchain is pointless because you are not going to get 100% coverage for years at best.  There's a huge number of components that need to work effectively together and they all need to be trusted to actually protect us against adversarial supply chain attacks effectively.

You need not just to trust that a binary you got was sent by the original author, but you need to know that it can be repeatedly built from the same source code, that every library involves was also securely built and that attestation needs to be transitively addressable back to the origins.

A lot of code that we have, whether software libraries like log4j or even the compilers that we use have a huge historical baseline of code, and just trusting that the binary was built with that code doesn't tell you that all that code is trustworthy.  There's a huge amount of trust being built into this system that is taking decades worth of software development and then drawing a line under it and saying "beyond this point lies dragons".

But that doesn't necessarily matter for building trust and for improving cybersecurity outcomes.  As I frequently say, perfect is the enemy of good, and in this case, building reasonably accurate software manifests, keeping track of them, and having even reasonable confidence that they are accurate means that software inventories get more accurate, it means that assessing vulnerability impact is easier and it builds a set of processes that right now are emerging good practice, but over time will become best practice.

This isn't about solving the issues raised by these vulnerabilities found deep in the supply chain, this is about making that supply chain more inspectable, more understandable and enabling us to incentivise the right interventions into the right places.

## [Improve supply chain security with GitHub actions, Cosign, Kyverno and other open source tools](https://www.cloudnative.quest/posts/security/2022/01/01/improve-supply-chain-security-with-github-actions-and-open-source-tools/)

[https://www.cloudnative.quest/posts/security/2022/01/01/improve-supply-chain-security-with-github-actions-and-open-source-tools/](https://www.cloudnative.quest/posts/security/2022/01/01/improve-supply-chain-security-with-github-actions-and-open-source-tools/)

> I am using a product called MeiliSearch for my JAM stack website. It is a great searching application. It could be deployed on-premise or using containers. I wanted to use this application for practicing supply chain security. We would secure it from building to deployment.
> 
> Here’s a diagram to summarize the workflow.


How hard is SBOM?  Well, this is a trivial application, in a fairly trivial JAMstack build, and the entire blogpost covers the ability to compile and build it in such a way that one can generate an SBOM for it.

This stuff is complex, but also note that for almost every step there are a multitude of tools that are available to select from.  

SBOM is going to be [driving up the hype curve into a peak of inflated expectations in the next year just before it drops into the trough of disillusionment](https://www.gartner.com/en/documents/3887767) as people realise that it doesn't actually solve all of the problems that it's hyped to do.


## [Lasting change needs personal motivation – niksilver.com](https://niksilver.com/2022/01/04/lasting-change-needs-personal-motivation/)

[https://niksilver.com/2022/01/04/lasting-change-needs-personal-motivation/](https://niksilver.com/2022/01/04/lasting-change-needs-personal-motivation/)

> Most people are used to their approach to day-to-day working. They may not think it’s perfect, but generally they’re used to it and have learned to work with it. Introducing change disrupts that. Perhaps some tasks need to be approached differently, perhaps they need to use different tools, maybe their processes change, or they have to interact with people differently. There will be a learning curve, and while they’re on that learning curve there will be mistakes, slow-downs, confusion and (inevitably) some frustration.
> 
> Furthermore, the person or people who are driving the change can’t be there all day, every day, to help every individual through their new challenges. So what’s going to ensure each individual persists in the face of difficulty? They need some kind of personal motivation to persist, and make the change a success.
> 
> To some extent there is some motivation in “Because my boss said so.” But that’s pretty weak, and generally only works if the change is very minor. With just this motivation alone a more significant change may work for a short time but is unlikely to last.
> 
> Much more effective is a motivation that is meaningful to an individual personally.


This is key about effecting change.  You can simply enforce it from the center or from above, but for it to really take root, you've got to win hearts and minds, and you've got to make the new system/process/thing more attractive than going back to the old thing


## [Binary Transparency](https://binary.transparency.dev/)

[https://binary.transparency.dev/](https://binary.transparency.dev/)

> If the dependency is itself a binary which is packaged and distributed as part of an application, how could a developer be confident that this hasn’t been tampered with?
> 
> 
> The producer of the library uses a Binary Transparency strategy to maintain their own tamper-evident records of code reviews, together with confirmation of build reproducibility by trusted third parties for each release.
> 
> During the build process, the provenance of the library is checked using the hash of the binary, and the build continues successfully only if these quality assurance attestations are discoverable.


This is a good overview of a critical part of a Software Bill Of Materials.

It's not enough to require that your software developer tells you what dependencies are in a piece of software, you also want confidence that they are telling you the truth, that nobody has interfered in the build process, and to be able to check and validate that the assertations still hold true later.


## [SummitRoute/csp_security_mistakes: Cloud service provider security mistakes](https://github.com/SummitRoute/csp_security_mistakes)

[https://github.com/SummitRoute/csp_security_mistakes](https://github.com/SummitRoute/csp_security_mistakes)

> This page lists security mistakes by cloud service providers (AWS, GCP, and Azure). These are public mistakes on the cloud providers' side of the shared responsibility model. This may be CVEs or bug bounties for issues in the services they run, but could also be in client software they provide, guidance they have given, failed audit tests in their SOC 2 Type 2, security incidents they have had, and more.


This is a worthwhile read.  

I note for comparison, that there hasn't ever really been public disclosure of privately owned server farm security mistakes, precisely because they are not a publicly used commodity.  But don't use this to suggest that these are all reasons that cloud is insecure, instead use this to recognise that no company is perfect.

While you need to trust your cloud provider, these are things that happen, and your risk modelling needs to account for it, and ensure that you have plans for how it might affect you.


## ['Drive It Like You Stole It': When Bug Bounties Went Boom, Part Three | Decipher](https://duo.com/decipher/you-got-to-drive-it-like-you-stole-it-when-bug-bounties-went-boom-part-three)

[https://duo.com/decipher/you-got-to-drive-it-like-you-stole-it-when-bug-bounties-went-boom-part-three](https://duo.com/decipher/you-got-to-drive-it-like-you-stole-it-when-bug-bounties-went-boom-part-three)

> At the lecture, I was spotted by Michael Sulmeyer (director for plans and operations for cyber policy in the Defense Department) and he is now serving in a cyber position somewhere in the White House. And he was sitting in on that lecture and he said, "Have you ever been to the Pentagon?" And I was like, "No," and he said, "Well, would you come brief the Pentagon if I invited you?" and I said, "Of course I would."
> 
> And I briefed an audience of various people that Michael pulled together and among them was Lisa Wiswell and she ended up taking over his position when he moved into a different role. So I showed Lisa and Charley Snyder, who also was in a policy role in the Pentagon, around ShmooCon a little bit. And then we talked on and off, beginning at that point for years. So it was conversations over several years where anytime I was in town in DC, I would stop over at the Pentagon for a visit and talk to them more, answer their questions about scope, scale, and preparation. Once she called and said, "Defense Digital Service launched, we want to pursue a bug bounty as one of the first big major public things that we do." I was like, "All right, well, let's just make it so that you don't wreck yourself." So what Lisa's ideas were, and I'm sure that RoRo had some of these as well, but Lisa was the one who basically rallied all of the different branches of our military that have offense capabilities. So she basically was like, "You know what? Katie says that we should test our stuff first. Why don't we do it with all the various cyber commands across the military?" And so there was a lot of bureaucracy hacking that she did.


This series is a fascinating history of bug bounty programs, and highlights some of the most interesting bits of them.

But this stood out to me, and reminded me of a quote sometimes attributed to Jeff Bezos of Amazon, "All overnight success takes about 10 years to achieve".   The success of the Hack the Pentagon program was because of a lot of the right people in the right place at the right time, but it was also because of the constant conversations, talks and preparation that Katie and others did in the years running up to that.

You need to invest your ideas into early conversations and just keep going with small, frustrating and slow conversations until the ground is fertile for an idea to succeed.


## [How GitLab automates engineering management | GitLab](https://about.gitlab.com/blog/2021/11/16/engineering-managers-automate-their-jobs/)

[https://about.gitlab.com/blog/2021/11/16/engineering-managers-automate-their-jobs/](https://about.gitlab.com/blog/2021/11/16/engineering-managers-automate-their-jobs/)

> From automating their 1:1 document creation, to integrating GitLab with Google Sheets, to writing utilities to provide executive summaries, GitLab team members take advantage of the rich API that GitLab provides to organize the mountains of information that they sort through on a regular basis.
> 
> For this blog post, I’m sharing a repo that contains just a few of the many scripts that our team members use. These scripts were originally written by engineering manager Rachel Nienaber. Rachel’s Infrastructure team is tasked with the exciting work of coordinating large scale infrastructure and code improvements. The work involves coordinating and sequencing lots of issues and epics, and ensuring the work gets done at just the right time and in the right order. Because of the breadth and scale of the work, she has created a handful of scripts that parse issues and epics in order to gain better visibility into the work that needs to be done.


This is a good tip for engineering managers.  Just because your work is more likely in spreadsheets, documents and meetings doesn't mean that you can't automate the worst of it.

Using scripts to pull together status updates, to gather information about the work your team is doing both reduces your need to force people to update you in person, and ensures that staff members know that work status is reported in one place.


## [Hashids - generate short unique ids from integers](https://hashids.org/)

[https://hashids.org/](https://hashids.org/)

> That way when one user passes the salt "abc1", our alphabet becomes cUpI6isqCa0brWZnJA8wNTzDHEtLXOYgh5fQm2uRj4deM91oB7FkSGKxvyVP3l
> 
> And when another user passes "abc2", the alphabet becomes tRvkhHx0ZefcF46YuaAqGLDKgM1W5Vp2T8n9s7BSoCjiQOdrEbJmUINywzXP3l
> 
> You can see that the shuffle is pretty good even when salt value is not that much different. This is what makes the base of Hashids work. Now we are able to encode one integer based on the salt value the user provides.


This is a cute idea.  Note that there's several advantages to this system.

Firstly, using hashids as primary public identifiers, you prevent competitors from learning about your growth.  Do they need to know that they are customer 10 or customer 1000?

Secondly, it harkens back to something I wrote well over a decade ago, that [identifiers are not numbers](https://www.brunton-spall.co.uk/post/2011/09/24/identifiers-are-not-numbers/).  This was written because of issues with twitters tweetids, and their storage, but critically, I said to always use an opaque identifier for user-facing identifiers.  This prevents anyone trying to read more into than you intend them to, such as order, specificity or leaking any other information.

Thirdly and finally, it provides some level of obscurity (rather than security) that makes it harder for a user to simply sequence the ID, looking through other resources looking to see if they can access someone else's data.


## [Swiss Army drops WhatsApp for homegrown messaging service - The Verge](https://www.theverge.com/2022/1/7/22871881/swiss-army-whatsapp-messaging-threema-privacy-concerns-us-jurisdiction)

[https://www.theverge.com/2022/1/7/22871881/swiss-army-whatsapp-messaging-threema-privacy-concerns-us-jurisdiction](https://www.theverge.com/2022/1/7/22871881/swiss-army-whatsapp-messaging-threema-privacy-concerns-us-jurisdiction)

> The Swiss army has banned the use of WhatsApp, Signal, Telegram, and other foreign encrypted messaging services by army personnel, according to Associated Press reports, and instructed staff to use the Swiss-made Threema app instead. The announcement was made in a letter sent to top army staff in December, citing privacy concerns based on US authorities’ ability to access data.
> 
> The original letter reportedly told army chiefs that “no other messaging service will be authorized,” although a spokesperson subsequently seemed to tone down the strength of the decree, describing it to the AP as a “recommendation.”
> 
> The primary concern seems to be the ability of authorities in Washington to access data stored by companies that fall under US jurisdiction, as described in the US CLOUD Act.


Interesting to see state based organisations increasingly move away from the big US tech firms due to US government legal reach.

Interesting especially here that they haven't moved to a government made or run application, but simply a sovereign company.  I wonder if they've decided what the implication would be if Threema were to be acquired by a US company in the future.


## [Cloud Security Breaches and Vulnerabilities: 2021 in Review](https://blog.christophetd.fr/cloud-security-breaches-and-vulnerabilities-2021-in-review/)

[https://blog.christophetd.fr/cloud-security-breaches-and-vulnerabilities-2021-in-review/](https://blog.christophetd.fr/cloud-security-breaches-and-vulnerabilities-2021-in-review/)

> Data about cloud security incidents in the wild is scarce, and often lacks details on tactics, techniques and procedures (TTPs) used by attackers. Breached organizations often don’t disclose the specifics publicly. Available data suffers from survivorship bias; we know about attacks that were detected, not advanced compromises that flew under the radar. 
> 
> In this post, we’ll analyze cloud security incidents and vulnerabilities that were publicly disclosed in 2021. We’ll focus on the ones related to the usage of cloud providers, and we won’t cover vulnerabilities of the cloud providers themselves. Scott Piper has done a great job for these with his repository “csp_security_mistakes”.


This is a lovely summary of cloud misconfigurations by customers in 2021.

It obviously only covers ones that were attacked, noticed, and disclosed, so who knows how many more misconfigurations were picked up by internal scanning, or simply left unnoticed.


## [Azure AD & IAM (Part II) - Leveraging Managed Identities For Privilege Escalation - Complete Cloud Security in Minutes | Orca Security](https://orca.security/resources/blog/azure-ad-iam-part-ii-leveraging-managed-identities-for-privilege-escalation/)

[https://orca.security/resources/blog/azure-ad-iam-part-ii-leveraging-managed-identities-for-privilege-escalation/](https://orca.security/resources/blog/azure-ad-iam-part-ii-leveraging-managed-identities-for-privilege-escalation/)

> At the beginning of my research I wanted to see if there was a way for an attacker to execute in the context of managed identity permissions as a low privileged user. 
> 
> As I discovered, the answer is yes, and in this blog I will present the first of two attack vectors I investigated, which is: “Escalating from low-privileged roles to managed identities that have broader permissions.” In particular, I investigated three Azure services: Functions, Logic Apps, and Automation to find roles that allow an attacker to escalate.


A really nice writeup of privilege escalation within Azure Cloud environments.  Sadly there's nothing in here about how to prevent or remediate it.  The most I can suggest is that you need to ensure that machine identities are created with only the permissions they need.  

In most cases, a machine identity should not need to be able to create other resources, simply act on those that exist.


