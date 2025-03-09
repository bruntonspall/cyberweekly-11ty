---
title: "143 - A good process badly fitted is a bad process"
date: 2021-04-04
description: "The solarwinds hack has demonstrated just how vulnerable our software supply chain is."
permalink: /a-good-process-badly-fitted-is-a-bad-process/
---

The solarwinds hack has demonstrated just how vulnerable our software supply chain is.

The excellent series from the Atlantic Council, the latest report of which is below, and the first outlined the [history of supply chain attacks](https://www.atlanticcouncil.org/in-depth-research-reports/report/breaking-trust-shades-of-crisis-across-an-insecure-software-supply-chain/), both really articulate that our supply chain is huge, is complex and that we place enormous amounts of trust in those organisations.

Our tools for building and developing that trust is mostly around the certification of the supplier as a "good and proper organisation", for example ISO27001 certification tells you that an auditor has gone in and verified that the organisation has an information security management system, that they have polices and processes for classifying their information, limiting it's distribution and thinking about the information security of the organisation.

However, many of these types of certification often tell you that the organisation has a process, and how rigidly it follows it.  That's a very Taylorist approach to workforce management.  Taylor is considered the father of scientific management, that is applying the principles of science to the management of work.  He did his work understanding how manufacturing factories worked in the early 1900's and built his principles of management around the idea that the worker was a cog in a large machine, and that it should an efficient repeatable process that it takes part in.  Peter Drucker in the 1960's and 70's took the Taylorist approach to manufacturing and applied it to modern "knowledge working".

In this model of thinking, which is still remarkably prevalent today, the process is the king of everything an organisation does, and any flaws, any issues that are discovered are indications either of a flawed process which requires adjustment, or more commonly, people not adhering to the process correctly.

However, my criticism of compliance regimes such as ISO27001 is that it tends to tell you whether you have a good process, rather than tell you if you have the right process, or if you actually apply it for good ends.  Many of the organisations that have been compromised over the last 20 years have had rigid and strong processes in place, and many times in the retrospectives you read afterwards, there is an effort to add a gate or check to the process to prevent this kind of thing from happening again.

But the world in 2020 isn't as simple as a production process that can be tightly managed and controlled.  Increasingly our environments are [Volatile, Uncertain, Complex and Ambiguous](https://hbr.org/2014/01/what-vuca-really-means-for-you), which means that our processes are hard to define up front, and difficult to determine what the right processes are.

If we want to build trust in our supply chains, we are going to have to assume that those suppliers are themselves working within an everchanging and complex environment, and we are going to have to change from a model where we ["Sense the inputs, categorise the solution and respond appropriately using best practice" to a model where we "probe the environment, sense what our probes tell us, and respond to the changes"](https://hbr.org/2007/11/a-leaders-framework-for-decision-making).

## [Broken trust: Lessons from Sunburst - Atlantic Council](https://www.atlanticcouncil.org/in-depth-research-reports/report/broken-trust-lessons-from-sunburst/#enhanceadaptability)

[https://www.atlanticcouncil.org/in-depth-research-reports/report/broken-trust-lessons-from-sunburst/#enhanceadaptability](https://www.atlanticcouncil.org/in-depth-research-reports/report/broken-trust-lessons-from-sunburst/#enhanceadaptability)

> There is a well-recognized spectrum of state support and coordination with non-state groups.184 Actors with less sophistication are still able to utilize the weaknesses of the software supply chain to hit a disproportionate number of targets—and from there can choose to exploit only those that are valuable and manageable. The 2017 Kingslayer case has been attributed to a Chinese group responsible for previous intrusions against services and manufacturing firms, targets that included sensitive intellectual property aligned with past Chinese-state espionage targets, but the group has not been positively linked to government agencies. Tortoiseshell, a non-state hacking group with no known state affiliation, was linked to an exploitation of eleven Saudi IT companies as a part of a larger software supply-chain intrusion in 2019.185 This group’s ability to leverage both custom and off-the-shelf malware to successfully execute a software supply-chain incursion against eleven companies without access to the resources of a state actor illustrates the lowering threshold of action for these types of incidents, providing prospective financial benefits and access for future operations. While seventeen of the intrusions against software updates profiled in the Breaking Trust dataset are attributed to states, the other nineteen remain unknown or positively linked to criminal groups.
> 
> [...]
> 
> Recommendation 12
> The federal CISO and CISA should immediately allow agencies and departments to satisfy any guidance or directive regarding the security and integrity of their IT systems with a feature or data stream directly from any of their authorized cloud services. CISA should immediately permit satisfaction of a BoD or related guidance be demonstrated by an agency or department switching on an appropriate data stream from their cloud services and pointing it to CISA for real-time monitoring. The federal CISO should seek to develop new guidance and cybersecurity governance documentation that maps to widely used cloud service products, features, and tools to prevent the need for agencies or departments to determine their own manner of implementation. 


This is a long report, but well worth reading.  It not only clarifies that software supply chain attacks by no means start and end with Solarwinds, but that the US Government response should not be to create yet another compliance regime for software companies to be required to demonstrate adherance to.

The complex interwoven mix of compliance regimes means that it's increasingly difficult for companies to work with Governments, but also means that government buyers find it harder to work out which compliance regimes they are looking for.  Many government buyers don't understand the technology that they are buying, so they really do just use these many and varied compliance regimes as a checkbox exercise.  As a contractor, I was required by one government contract to demonstrate that I had a VPN in my infrastructure to protect my work devices when not in the office.  As a sole employee with only cloud services, I had to fight a procurement team to understand what they wanted me to demonstrate, because simply having a VPN was not really demonstrating anything.  In the end, I simply bought NordVPN, which checked the box, but almost certainly didn't help.  


## [You Can't Trust Amazon When It Feels Threatened - Last Week in AWS](https://www.lastweekinaws.com/blog/you-cant-trust-amazon-when-it-feels-threatened/)

[https://www.lastweekinaws.com/blog/you-cant-trust-amazon-when-it-feels-threatened/](https://www.lastweekinaws.com/blog/you-cant-trust-amazon-when-it-feels-threatened/)

> But with this [tweet](https://twitter.com/amazonnews/status/1374911222361956359?s=20), that entire sentiment changes from “they haven’t lied” to “they haven’t lied about something germane to cloud in a way in which I’ve caught them doing so” because we’ve just seen them lie to the world when they’re facing something that they perceive to be an existential threat to one of their lines of business (i.e., unionization).
> 
> This teaches us that—when it’s a big enough deal—Amazon will lie to us. And coming from the company that runs the production infrastructure for our companies, stores our data, and has been granted an outsized position of trust based upon having earned it over 15 years, this is a nightmare.
> 
> Look—personally, I don’t care that much if the company that sells me my underpants lies about something that impacts their ability to maintain their margins on selling me those underpants. I don’t like it, and I feel annoyed and betrayed as a customer (and as a human being) that they did it. But it’s not something that I’m going to lose sleep over.
> 
> But when the same company goes on the record to “set the record straight” about the Pentagon’s JEDI contract? Suddenly that denial and statement has to be viewed in the context of “if it’s important enough, they will lie to us about it” and weighed accordingly.
> 
> This isn’t just a subtle shade of nuance; it changes everything. When Bloomberg published its ridiculous Big Hack story a few years back and AWS denied it, my immediate comment was that if AWS is denying it, it flat out didn’t happen—because they don’t lie.
> 
> After last week, I wouldn’t make that claim at all; I’d wait for more data.
> 
> When AWS says that they don’t use customer data or metadata to help inform their retail business, I have to now weigh that in the context of “they might be doing that and lying to us about it.”


This could end up being a landmark moment.  I know that there are retail companies who do not use AWS because they worry that Amazon are their competitor and they refuse to financially support a competitor, as well as concerns around the access to their data that it might give Amazon.

AWS's primary asset is the trust of it's users.  It's trusted to build, operate and manage systems that contain vast amounts of data, and that trust is the most important asset that it has.  Being tarred with the brush from Amazon's logistics firm, the breach of trust in that tweet, and the constant anti-unionisation activities will degrade that trust.


## [php.internals: Changes to Git commit workflow](https://news-web.php.net/php.internals/113838)

[https://news-web.php.net/php.internals/113838](https://news-web.php.net/php.internals/113838)

> Yesterday (2021-03-28) two malicious commits were pushed to the php-src
> repo [1] from the names of Rasmus Lerdorf and myself. We don't yet know how
> exactly this happened, but everything points towards a compromise of the
> git.php.net server (rather than a compromise of an individual git account).
> 
> While investigation is still underway, we have decided that maintaining our
> own git infrastructure is an unnecessary security risk, and that we will
> discontinue the git.php.net server. Instead, the repositories on GitHub,
> which were previously only mirrors, will become canonical. This means that
> changes should be pushed directly to GitHub rather than to git.php.net.


Compromise a source control repository and forge commits from existing users.

Git of course has no internal signing tools, so any user who can commit to a repository can change their metadata to display any name and any email address.  The way that Git works makes it very difficult to actually enforce any identification in this way, because it's designed around distributed teams who share patches by email for the linux kernel development flow.

Interesting to note that in this case, the core PHP team have decided to outsource the security and maintenance of their source control server to Github.  They trust that a 3rd party will do a better job of maintaining it than they will.  This is almost certainly true, but is against a lot of security instincts, that running something yourself is more secure.


## [Securing our approach to domain fronting within Azure - Microsoft Security](https://www.microsoft.com/security/blog/2021/03/26/securing-our-approach-to-domain-fronting-within-azure/)

[https://www.microsoft.com/security/blog/2021/03/26/securing-our-approach-to-domain-fronting-within-azure/](https://www.microsoft.com/security/blog/2021/03/26/securing-our-approach-to-domain-fronting-within-azure/)

> Domain fronting is a networking technique that enables a backend domain to utilize the security credentials of a fronting domain. For example, if you have two domains under the same content delivery network (CDN), domain #1 may have certain restrictions placed on it (regional access limitations, etc.) that domain #2 does not. By taking the valid domain #2 and placing it into the SNI header, and then using domain #1 in the HTTP header, it’s possible to circumvent those restrictions. To the outside observer, all subsequent traffic appears to be headed to the fronting domain, with no ability to discern the intended destination for particular user requests within that traffic. It is possible that the fronting domain and the backend domain do not belong to the same owner.
> 
> As a company that is committed to delivering technology for good, supporting certain use cases that support free and open communication are an important consideration when weighing the potential impacts of a technique like domain fronting. However, we know that domain fronting is also abused by bad actors and threat actors engaging in illegal activities, and we’ve become aware that in some cases bad actors configure their Azure services to enable this.


This is a good change.  While there are some niche good reasons to allow domain fronting, the vast majority is either in providing infrastructure services such as a CDN or whitelabel SaaS products.

There is no reason to generally allow any random Azure resource to domain front any other resource without some agreement being put in place.  Blocking domain fronting generally is almost certainly the right thing to do here.


## [Buffer overruns, license violations, and bad code: FreeBSD 13’s close call | Ars Technica](https://arstechnica.com/gadgets/2021/03/buffer-overruns-license-violations-and-bad-code-freebsd-13s-close-call/)

[https://arstechnica.com/gadgets/2021/03/buffer-overruns-license-violations-and-bad-code-freebsd-13s-close-call/](https://arstechnica.com/gadgets/2021/03/buffer-overruns-license-violations-and-bad-code-freebsd-13s-close-call/)

> Despite not having any kernel developers on-staff, Ars was able to verify at least some of Donenfeld's claims directly, quickly, and without external assistance. For instance, finding a validation function which simply returned true—and printf statements buried deep in cryptographic loops—required nothing more complicated than grep.


This is a fascinating story. But I’m going to point out here that when I worked in the Guardian, I’d say that only about 50% of the developers knew what grep was, and only 2 journalists that I knew of would have known what it was or how to use it.

Now sure. We should hold many of the actors in this story to a higher standard. If a company is sponsoring work, and willing to make statements about the quality, then they need to have some confidence in their ability to know that. 


## [The Day I Trolled The Entire Internet: An Accidental Research Project on CVE-2020-1350 | ZeroSec - Adventures In Information Security](https://blog.zsec.uk/cve-2020-1350-research/)

[https://blog.zsec.uk/cve-2020-1350-research/](https://blog.zsec.uk/cve-2020-1350-research/)

> Microsoft has a critical flaw in DNS server which resulted in a CVSS 10, CVE-2020-1350 is a real vulnerability that was published:
> https://nvd.nist.gov/vuln/detail/CVE-2020-1350 It's a brand new vulnerability therefore people would be interested in a proof of concept.
> A security company publishes the info - no public exploit available at the point of publishing this blog,  a quick kudos to the team over at Checkpoint Research who found the original vulnerability and published a great write up which can be found here.
> I created a fake exploit on GitHub minutes after the original blog post was published - playing a prank on hackers and other security companies picking up and publishing in threat intelligence feeds. The code was initially just a bash script then I added a binary loaded with canary tokens to track who was running the script. If anyone is interested Thinkst has a great blog around how canary tokens work that can be found here.
> Lots of people ran the code or helped spread the existence of the fake exploit, folks ran the "proof of concept" code without reading it first and got trolled. If I had been malicious I could have done something much worse than rick-rolling.


Do not download and run proof of concept code from random security engineers without reading it, checking it and seeing what it does.


## [Assessing the state of breached data search services](https://www.curatedintel.org/2021/03/assessing-state-of-breached-data-search.html)

[https://www.curatedintel.org/2021/03/assessing-state-of-breached-data-search.html](https://www.curatedintel.org/2021/03/assessing-state-of-breached-data-search.html)

> Some services index recycled credential compilation lists containing billions of records worth of excessive overlap (i.e. AntiPublic, Pemiblanc, ExploitIn, Collection #1, db8151dd, Cit0day, et al.); it is acceptable to index such records, if a transparency condition is met, to provide the security practitioner contextual awareness.
> In contrast, looking at indexed data sources, a different story is told. There are significant coverage discrepancies between indexed account records and indexed data sources. For a security practitioner, this means that a service without competitive credential exposure coverage will have many blind spots.
> 
> [...]
> 
> Looking at the data, it becomes easy to understand why security practitioners turn to grey zone breached data search services to protect organizations. An argument can be made that the threat intelligence industry failed to provide a means of doing so that is both competitive and affordable.
> 
> 
> The cybersecurity industry turned to WeLeakInfo when the threat intelligence industry failed them. This claim is alleged with leaked transaction records from 141 companies offering security services.


This is a good analysis of the data from multiple data breach sites that sell the info, demonstrating that threat intelligence sites who provide only anonymised data, or from only a small number of public breaches simply don't provide enough information to allow defenders to protect their systems.

Of course, the ethical, moral and legal quandary is how to allow security firms to do that without promoting and financing illegal activity, especially given the slightly grey nature of many security firms and their employees private activities.  I don't agree with the authors conclusion that "security vetted organisations" is the solution, but I don't have a better solution


## [Secure access to 100 AWS accounts | Segment Blog](https://segment.com/blog/secure-access-to-100-aws-accounts/)

[https://segment.com/blog/secure-access-to-100-aws-accounts/](https://segment.com/blog/secure-access-to-100-aws-accounts/)

> Segment began in a single AWS account and last year finished our move to a dev, stage, prod, and “ops” accounts. For the past few months we’ve been growing at about one new AWS account every week or two, and plan to continue this expansion in to per-team and per-system accounts. Having many “micro-accounts” provides superior security isolation between systems, and reliability benefits by limiting the blast radius of AWS rate-limits.
> 
> 
> When Segment had only a few accounts, employees would log in to the AWS “ops” account using their email, password, and 2FA token. Employees would then connect to the ops-admin role in the dev, stage, and prod accounts using the AssumeRole api.
> 
> 
> Segment now has a few dozen AWS accounts and plans to continue adding more! In order to organize this expansion we needed a mechanism to control our accounts, which accounts employees have access to, and each employee’s permissions in each account. 
> 
> We also hate using AWS API keys when we don’t absolutely have to so we moved to a system where no employees have any AWS keys. Instead, employees only access AWS through our identity provider. Today we have zero employees with AWS keys and there is no future need for employees to have a personal AWS key.


A nice writeup of one way to scale up your AWS account usage, and really subdivide accounts into compartments that ensure that a compromised developer account has a limited blast radius.


## [Update on campaign targeting security researchers](https://blog.google/threat-analysis-group/update-campaign-targeting-security-researchers/)

[https://blog.google/threat-analysis-group/update-campaign-targeting-security-researchers/](https://blog.google/threat-analysis-group/update-campaign-targeting-security-researchers/)

> In January, the Threat Analysis Group documented a hacking campaign, which we were able to attribute to a North Korean government-backed entity, targeting security researchers. On March 17th, the same actors behind those attacks set up a new website with associated social media profiles for a fake company called “SecuriElite.”
> 
> The new website claims the company is an offensive security company located in Turkey that offers pentests, software security assessments and exploits. Like previous websites we’ve seen set up by this actor, this website has a link to their PGP public key at the bottom of the page. In January, targeted researchers reported that the PGP key hosted on the attacker’s blog acted as the lure to visit the site where a browser exploit was waiting to be triggered.


Linking partly for awareness, but also for the entertaining note that the group commonly associated with the cryptonym Lazarus has created a persona (and it might be a real person who knows), called Sebastian Lazarescue


