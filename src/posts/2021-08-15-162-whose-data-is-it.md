---
title: "162 - Whose data is it?"
date: 2021-08-15
description: "It’s easy to think of data as being very similar to physical property, this is my browsing data, that is your personally identifiable information, and data is like toxic waste that needs to be minimally collected and stored."
permalink: /whose-data-is-it/
---

It’s easy to think of data as being very similar to physical property, this is my browsing data, that is your personally identifiable information, and data is like toxic waste that needs to be minimally collected and stored.

But data is ephemeral, contextual, temporal and intangible, which means that it’s really hard to reason about the ownership and management of said data.

If I send you an email, does the fact that it’s your name and my name in the to and from addresses mean that I’m sharing your personal information with someone?  What if I forward that email onto someone?  Why is it different to include an excel spreadsheet of customer data, but fine to put several hundred peoples addresses in the cc field?

When you work for a company, it’s even more complex, because simple things like where you work, the words you type, and what you think and say may arguably belong to both you and to the company at the same time.

You have a reasonable expectation of privacy from your employer (in the UK), which is to say that it’s unreasonable for them to monitor your online banking activity, or anything you do that is personal, unless there is an overriding reason, such as an active investigation.  But the monitoring that Amazon is talking about doing probably doesn’t invade your privacy in a strict legal sense, but whether employees would agree is another matter, and of course, in law there is a requirement for the judiciary to consider what [“The man on the Clapham Omnibus would think”](https://en.m.wikipedia.org/wiki/Man_on_the_Clapham_omnibus) - which is to say that if every reasonable and normal person would think that it’s an invasion of privacy, then it probably is.

This gets even trickier when you start considering the questions about who owns the data on devices that you own.  Naturally, our clapham omnibus man would consider that anything that you saved on your device is probably yours, and the maker of your device has no good reason to simply search it.  But they would also probably consider that CSAM is one of the few legitimate reasons for that device to attempt to scan and identify files on that device.

Of course privacy experts will always say that this is the thin end of the wedge, just because almost every government in the world is united against CSAM, what does it mean if governments want the same principles to apply for searching for leaked classified material, manuals for creating explosives, terrorism manuals, or just insulting pictures of a holy icon or dear leader.

All of these questions come back to the question of just how much privacy we can expect people to have from the state.  Even the most dedicated privacy campaigners will generally agree that law enforcement, with an independent judicial warrant and an appropriate degree of suspicion can breach an individuals privacy, because the protection of the many demands that we identify and manage the rogue elements in society.  That means that the arguments aren’t about “Do you have privacy or not”, but are instead about the degrees to which you have privacy, the reasons and safeguards for it being breached and of course, the underlying question about whose data it even is anyway.

## [Amazon to Monitor Customer Service Workers’ Keyboard and Mouse Strokes | VICE](https://www.vice.com/en/article/dyvejq/amazon-monitor-employees-keyboard-mouse)

[https://www.vice.com/en/article/dyvejq/amazon-monitor-employees-keyboard-mouse](https://www.vice.com/en/article/dyvejq/amazon-monitor-employees-keyboard-mouse)

> Although the document says Amazon has considered deploying a solution that captures all of a worker's keystrokes, the tool the company has seemingly leaned towards buying is not designed to record exactly what workers type or monitor their communications. Instead, the system generates a profile based on the employee's natural keyboard and mouse movements, and then continuously verifies whether it seems the same person is in control of the worker's account to catch hackers or imposters who may then steal data. The move highlights the sorts of tools companies may increasingly deploy as working from home or remotely continues during the ongoing pandemic, and the issues Amazon is already facing with the theft of customer data
> [...]
> The document later points to several use cases, including one where a customer support worker may walk away from their computer without locking it. In this example, their roommates may have expressed interest in seeing what public figures buy from Amazon, and so then look up that information with an internal search tool, the document says.


([Joel](https://twitter.com/joelgsamuel)) My musing is largely around case management solutions and a centralised system holding lots of records that a large number of staff have to access.

A powerful insider control is only granting access based on the existence of a problem ticket requiring it and/or peer reviewed/approved access. By email/chat, I don't see the staff member having a need to access more than a handful of customer records at the same time. That only requires rolling permissions based on open tickets (not open/assigned but open/being worked on) or open chats. By phone, it is a lot harder to correlate back to source request (when I use Amazon.co.uk chat, I'm logged into my Amazon account, if I call, it may not know my phone number and bring up my account) however again, why do they need to access multiple records at the same time?

If the system cannot detect that a single customer service representative has an unusual amount of parallel access, or is accessing lots of records over time (whether very quickly or there is a trend of accessing records outside of their assigned problem tickets) approaching this by monitoring the device being used is already losing.

Maybe I just don't understand how many billions you need before actually making a decent case management system with security built-in, as opposed to security you add around.

(Michael) Fixing this kind of problem requires layered protections.   Not all customer service representatives should be able to access all records.  But baking that level of access control into your customer record system is really hard, because it’s not easy to work out how to describe those access models.  So on top of role based access control, you need good identity and access management, good passwords, MFA devices, travel detection and all those things.  But again, those are hard, because humans will work around them if they get in the way of their work. 

Given Amazon’s reputation for tracking their own staff, trying to implement this was always going to look tricky, but if we give them the benefit of the doubt, attempting to validate and verify that it’s still the same user at the keyboard is just one more layer in that authentication and authorisation process.


## [Leaked Document Says Google Fired Dozens of Employees for Data Misuse | Vice](https://www.vice.com/en/article/g5gk73/google-fired-dozens-for-data-misuse)

[https://www.vice.com/en/article/g5gk73/google-fired-dozens-for-data-misuse](https://www.vice.com/en/article/g5gk73/google-fired-dozens-for-data-misuse)

> The document says that Google terminated 36 employees in 2020 for security related issues. Eighty-six percent of all security-related allegations against employees included mishandling of confidential information, such as the transfer of internal-only information to outside parties.
> 
> 10 percent of all allegations in 2020 concerned misuse of systems, which can include accessing user or employee data in violation of Google's own policies, helping others to access that data, or modifying or deleting user or employee data, according to the document. In 2019, that figure was 13 percent of all security allegations.
> [...]
> Google terminated 26 people in 2019 and 18 in 2018 related to security incidents, the person who provided the document told Motherboard.


([Joel](https://twitter.com/joelgsamuel)) From a general 'personal' use of services such as Google Mail and Apple iCloud, we simply have to rely on these providers 'having it all covered' and behaving themselves. The policies and processes inside these organisations are opaque, and millions of people likely give no thought about whether these organisations have internal monitoring and so on.

From a 'corporate' perspective, organisations may ask Google, Microsoft (etc) for their security promises and review their ISO certifications or SOC reports... but the internal policies, processes and monitoring systems will remain opaque. Organisations invested in Google Workspace or Microsoft 365 are unlikely to move their entire productivity data (emails, contacts, files/documents and so on) based on such reporting either.

One could argue these organisations are in he security/privacy game, so they will lose users/revenue if they have issues on this, but in reality thats not true in any volume they would care about.

I'd argue such reporting does tell me that Google (etc) are invested in monitoring, detection and response for inside actors. None of those systems are ever perfect, and abuse of legitimate access is a big problem.


## [Expanded Protections for Children  | Apple](https://www.apple.com/child-safety/pdf/Expanded_Protections_for_Children_Technology_Summary.pdf)

[https://www.apple.com/child-safety/pdf/Expanded_Protections_for_Children_Technology_Summary.pdf](https://www.apple.com/child-safety/pdf/Expanded_Protections_for_Children_Technology_Summary.pdf)

> Apple plans to introduce a new feature that would scan messages sent to and by child users of iPhones to determine if the images contain nudity, the company announced on Thursday. The move is a major development in the ongoing debate around privacy and the inspection of communications.
> 
> Messages uses on-device machine learning to analyze image attachments and determine if a photo is sexually explicit. The feature is designed so that Apple does not get access to the messages
> [...]
> [the new feature] will enable parents to play a more informed role in helping their children navigate communication online.
> 
> [VICE also covered this for a simpler read.](https://www.vice.com/en/article/v7ejmy/apple-scan-message-content-nudity).[ EFF has a verbose opinion](https://www.eff.org/deeplinks/2021/08/apples-plan-think-different-about-encryption-opens-backdoor-your-private-life). [As does a contentious figure](https://twitter.com/Snowden/status/1423469854347169798).


([Joel](https://twitter.com/joelgsamuel)) First reaction was "are these kinds of materials shared using iMessage, compared to say WhatsApp or Snapchat?". My second reaction was "does this count as spyware for parents/guardians?". My third reaction was "right now, this is a good thing."

Gosh, what a broad and opinionated response to Apple's announcement. The opinions around this are mixed: ranging from concerns over end-to-end encryption, abusive parents/guardians, expansion of the underlying technical features based on legislative/law enforcement requests etc.
I am choosing to take a narrow view based on the here and now: this is a good development.

Apple already scan photos to identify faces, pets etc. This continues to be on-device. Sure, a lot of things COULD happen with technology like this, but this is a re-application of existing technology for a new purpose. I think attempts to protect child users is a good new purpose.

I do not see anything about making this available to non-Apple native applications within iOS/iPadOS. I see that as a next step. This would give little room for WhatsApp, FB Messenger, Signal and Snapchat not to use these hooks if they can be assured the images do not leave the device.
[Google Cloud Platform's Cloud Vision API to detect explicit content](https://cloud.google.com/vision/docs/detecting-safe-search#vision_safe_search_detection-drest) exists today, but that requires sending the image off the device unencrypted back to cloud systems (then to Google) who I suspect have rights to use the images provided for further machine learning. An on-device system doesn't have those caveats.


## [Bluepurple - Week ending August 15th - by Ollie - Cyber Defence News for Blue & Purple Teams](https://bluepurple.substack.com/p/bluepurple-week-ending-august-15th)

[https://bluepurple.substack.com/p/bluepurple-week-ending-august-15th](https://bluepurple.substack.com/p/bluepurple-week-ending-august-15th)

> Firstly welcome to the inaugural substack from the blueteamsec subreddit.
> 
> So why is this happening? In short it is another way to provide value to the community. Some people live on Reddit others float past but cyber is just the most intense team sport. I have personally increasingly valued various substacks being pushed to my inbox including cyberweekly by Michael Brunton-Spall. The thesis for this substack is if we batch up the weekly content from the subreddit then it will find a wider audience via email forwarding which in turn will raise awareness which will result in better overall cyber defence.
> 
> The data says in < 24 hours 201 people clicked the link and 31 or so signed up. So we will see how this goes.


Including this, not just because Ollie says nice thing about me, and CyberWeekly, but because if you haven’t seen it, then [r/blueteamsec](https://reddit.com/r/blueteamsec) is a brilliant resource for cybersecurity news.

Almost everything posted to blueteamsec is high quality, but it doesn’t have any analysis other than some simple flair.  This newsletter, which hopefully will continue, adds some analysis to a number of the links, giving you enough context to know which ones are worth your time to read.


## [Interview: Apple’s head of Privacy details child abuse detection and Messages safety features | TechCrunch](https://techcrunch.com/2021/08/10/interview-apples-head-of-privacy-details-child-abuse-detection-and-messages-safety-features/)

[https://techcrunch.com/2021/08/10/interview-apples-head-of-privacy-details-child-abuse-detection-and-messages-safety-features/](https://techcrunch.com/2021/08/10/interview-apples-head-of-privacy-details-child-abuse-detection-and-messages-safety-features/)

> In recent years, Apple has often leaned into the fact that on-device processing preserves user privacy. And in nearly every previous case I can think of, that’s true. Scanning photos to identify their content and allow me to search them, for instance. I’d rather that be done locally and never sent to a server. However, in this case, it seems like there may actually be a sort of anti-effect in that you’re scanning locally, but for external use cases, rather than scanning for personal use — creating a ‘less trust’ scenario in the minds of some users. Add to this that every other cloud provider scans it on their servers and the question becomes why should this implementation being different from most others engender more trust in the user rather than less?
> 
> I think we’re raising the bar, compared to the industry standard way to do this. Any sort of server-side algorithm that’s processing all users’ photos is putting that data at more risk of disclosure and is, by definition, less transparent in terms of what it’s doing on top of the user’s library. So, by building this into our operating system, we gain the same properties that the integrity of the operating system provides already across so many other features, the one global operating system that’s the same for all users who download it and install it, and so it in one property is much more challenging, even how it would be targeted to an individual user. On the server side that’s actually quite easy — trivial. To be able to have some of the properties and building it into the device and ensuring it’s the same for all users with the features enabled give a strong privacy property. 
> 
> Secondly, you point out how use of on-device technology is privacy preserving, and in this case, that’s a representation that I would make to you, again. That it’s really the alternative to where users’ libraries have to be processed on a server that is less private.
> 
> The things that we can say with this system is that it leaves privacy completely undisturbed for every other user who’s not into this illegal behavior, Apple gains no additional knowledge about any users cloud library. No user’s iCloud Library has to be processed as a result of this feature. Instead what we’re able to do is to create these cryptographic safety vouchers. They have mathematical properties that say, Apple will only be able to decrypt the contents or learn anything about the images and users specifically that collect photos that match illegal, known CSAM hashes, and that’s just not something anyone can say about a cloud processing scanning service, where every single image has to be processed in a clear decrypted form and run by routine to determine who knows what? At that point it’s very easy to determine anything you want [about a user’s images] versus our system only what is determined to be those images that match a set of known CSAM hashes that came directly from NCMEC and and other child safety organizations.


Apple’s case here is actually quite a good one.  You can argue that providers should not ever scan content, and that’s a fair if unrealistic position to take.  Assuming that providers are going to be asked to scan content for banned and forbidden material, then there are only a limited few ways that you can do it. The majority of those require decrypting the content when it’s on servers.

By distributing the NCMEC hashes to devices, and doing inspection and detection on the device, that means that they can retain all of the end to end encryption infrastructure that they already have.  This is also a good reminder that all of those applications and services that describe end to end encryption, from Whatsapp to PGP to ProtonMail, are always subject to compromise of the end user device.  


## [Bear Tracks: Infrastructure Patterns Lead to More Than 30 Active APT29 C2 Servers | RiskIQ](https://www.riskiq.com/blog/external-threat-management/apt29-bear-tracks/)

[https://www.riskiq.com/blog/external-threat-management/apt29-bear-tracks/](https://www.riskiq.com/blog/external-threat-management/apt29-bear-tracks/)

> RiskIQ’s Team Atlas researchers confirmed that the indicators mentioned in the Tweet were associated with APT29 and WellMess. We then found several additional IP addresses and Certificates that closely matched the pattern found on the original IP address mentioned in the Tweet.
> 
> Building on that discovery, RiskIQ’s Team Atlas was then able to leverage RiskIQ’s Internet Intelligence Graph to link the following SSL Certificates and IP addresses to APT29 C2 infrastructure with high confidence. The first IP address we recorded with these new SSL Certificate features was spotted on October 9, 2020. However, we established that they go back nearly a week prior after corroborating our findings with external sources.
> 
> You can explore the full list of these IOCs in RiskIQ's Threat Intelligence Portal here.
> 
> Readers should note that much of this infrastructure is still in active use by APT29, though we do not have enough information to say how it is being used or who the targets are. We also found it noteworthy that many of the newer IP addresses reside in the same Class-C networks as previously disclosed IP addresses.
> 
> RiskIQ’s Team Atlas next examined the banners returned from HTTP requests made to the servers in the table above. In doing so, we identified a pattern that linked both the old and new styles of SSL certificates together. It also led our researchers to discover an entirely separate group of malicious certificates and IP addresses that were initially stood up around the same time.


This is both anice piece of self promotion by RiskIQ, showing how good their products are, as well as a good bit of investigative research.  

One of the harder things around the operation of a major threat actor is the complexity of setting up the backing infrastructure.  Since renting servers, getting new bank accounts, generating certificates and so on is complex, it's really tempting for these actors to reuse the same infrastructure over and over.  

That however gives us clues to help tie together disparate campaigns by threat actors, so we can track their activities more effectively.


## [GitHub - Skyscanner/turbolift: A simple tool to help apply changes across many GitHub repositories simultaneously](https://github.com/Skyscanner/turbolift)

[https://github.com/Skyscanner/turbolift](https://github.com/Skyscanner/turbolift)

> Anyone who has had to manually make changes to many GitHub repositories knows that it's hard to beat the simplicity of just cloning the repositories and updating them locally. You can use any tools necessary to make the change, and there's a degree of immediacy in having local files to inspect, tweak or run validation.
> 
> It's dumb but it works. It doesn't scale well, though. Manually cloning and raising PRs against tens/hundreds of repositories is painful and boring.
> 
> Turbolift essentially automates the boring parts and stays out of the way when it comes to actually making the changes. It automates forking, cloning, committing, and raising PRs en-masse, so that you can focus on the substance of the change.


One of the downsides of microservices is that occasionally, you might want to make architectural changes across all of your services at the same time.  Upgrading a critical library, or making changes to the underlying service fabric are all things that might require lots of synchronised changes. 

This tool, allowing you to coordinate changes across repo's means that you can easily manage raising those changes with the teams who are owners, and create the pull requests as a batch.

Don't be fooled though, this won't, or shouldn't, serialise changes at deploy time.  You are still dependant on your deployment infrastructure to manage independent microservice changes, so you'll still need to ensure that each pull request is forward and backward compatible, and do the coordination of breaking changes between teams.  This just removes some of the grunt work from doing that.


## [Domain Protect - prevent subdomain takeover of cloud resources](https://tech.ovoenergy.com/how-we-prevented-subdomain-takeovers-and-saved-000s/)

[https://tech.ovoenergy.com/how-we-prevented-subdomain-takeovers-and-saved-000s/](https://tech.ovoenergy.com/how-we-prevented-subdomain-takeovers-and-saved-000s/)

> At OVO we have a complex hybrid cloud environment, with multiple autonomous development teams who manage their own cloud accounts. We’re always looking at how we can improve centralised visibility of vulnerabilities in cloud assets to better protect our customers, so a few months ago, we started a private Bug Bounty program. The security researchers found a number of issues, over half of which were subdomain takeovers.
> 
> We wanted to get ahead of the malicious actors and Bug Bounty researchers, find any vulnerable subdomains ourselves and fix them – bearing in mind we have a big advantage:  access to our DNS records.
> 
> We didn’t just want to find the vulnerabilities at a single point in time – we also felt it was important to quickly find new security issues as and when they arose in the future.
> 
> We began by searching for open-source tools, however although we found code used by Bug Bounty researchers, we didn’t find any defensive tools which could run on a continuous basis.
> 
> We decided to develop our own.


This is a lovely tool for monitoring your own infrastructure and looking for dangling domains


## [Attackers use Morse code, other encryption methods in evasive phishing campaign | Microsoft Security Blog](https://www.microsoft.com/security/blog/2021/08/12/attackers-use-morse-code-other-encryption-methods-in-evasive-phishing-campaign/)

[https://www.microsoft.com/security/blog/2021/08/12/attackers-use-morse-code-other-encryption-methods-in-evasive-phishing-campaign/](https://www.microsoft.com/security/blog/2021/08/12/attackers-use-morse-code-other-encryption-methods-in-evasive-phishing-campaign/)

> Cybercriminals attempt to change tactics as fast as security and protection technologies do. During our year-long investigation of a targeted, invoice-themed XLS.HTML phishing campaign, attackers changed obfuscation and encryption mechanisms every 37 days on average, demonstrating high motivation and skill to constantly evade detection and keep the credential theft operation running.
> 
> This phishing campaign exemplifies the modern email threat: sophisticated, evasive, and relentlessly evolving. The HTML attachment is divided into several segments, including the JavaScript files used to steal passwords, which are then encoded using various mechanisms. These attackers moved from using plaintext HTML code to employing multiple encoding techniques, including old and unusual encryption methods like Morse code, to hide these attack segments. Some of these code segments are not even present in the attachment itself. Instead, they reside in various open directories and are called by encoded scripts.


The use of morse code in this instance is not in fact encryption, it’s simply encoding.  The data in this case is a javascript file that will be decoded and executed, and encoding it in morse code is simply to avoid scanning tools from detecting it.  Previously, this might have been a base64 blob, or some other encoded blob, but mail scanning tools are getting better at detecting and decoding various formats to look for suspicious or dangerous javascript.

Cute headline, and a valuable chance to look at a modern and effective phishing campaign and how it’s all put together.


