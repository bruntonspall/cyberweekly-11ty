---
title: "252 - Keeping secrets secret"
date: 2025-01-19
description: "Our technical systems are filled with secrets, from passwords to API keys or even just internal IP addresses if you listen to some slightly tiresome threat modelling aficionado's"
permalink: /keeping-secrets-secret/
---

Our technical systems are filled with secrets, from passwords to API keys or even just internal IP addresses if you listen to some slightly tiresome threat modelling aficionado's

We need ways for different systems and services that we build to be able to confirm to one another that they actually are working on our behalf.  The most common way is for us to generate some kind of secret value, tell both services the value, and they can check whether the other service knows the secret value or not.

The downside to the most common implementation is that, the way they are normally implemented, at least 3 different people know the secret value, Service A, Service B and Developer Z.  Of course, the developer will want their team to know the secret in case they need it, so they'll also store the secret in other places, a team wiki, a shared password vault, or an encrypted file in their team git repository.  

Of course, this can spread, and it only takes one mistake to accidentally share the secret with other people.

Good secret systems make it so that no human knows the secret at all.  Systems that enable the secret to be generated in a vault system, and that is securely shared with the systems when they are built.

But secrets get shared, and this can be a major issue for many systems.  As set out below, I've had the conversation before about just how serious having a secret shared is.  If you put something up on the internet only briefly, how do you know whether anyone looked at it, and whether it had any damaging impact?

It's really nice to see research into the time taken to compromise secrets, and one of the benefits of reading back through things from the last few months, find two separate bits of research at the same time.  Both agree, you have mere seconds to react to secrets being shared in the most popular platform.  That means that if you share secrets anywhere, you should assume that an adversary has gotten hold of it, and kick off your incident response process.

Of course, machine secrets aren't the only secrets.  I linked to some of the issues with passkeys last week, just ahead of the NCSC reporting that says much the same thing.  Passkeys are incredibly positive development, and the user interface issues are settling down fast.  I'm increasingly of the view that the best possible password is one that you cannot know, and passkeys deliver on that promise in spades.

## [What’s the worst place to leave your secrets? – Research into what happens to AWS credentials that are left in public places - Cybenari ](https://cybenari.com/2024/08/whats-the-worst-place-to-leave-your-secrets/)

[https://cybenari.com/2024/08/whats-the-worst-place-to-leave-your-secrets/](https://cybenari.com/2024/08/whats-the-worst-place-to-leave-your-secrets/)

> The following graph shows the number of access attempts made to GitHub and DockerHub per hour since the canary tokens were published. BitBucket and GitLab are not shown here because, surprisingly, there were 0 attempts to access the canary tokens published on those platforms.
> 
> Conversely, access with the canary tokens that were published on GitHub was attempted within seconds of their release.
> 
> For DockerHub, it took 170 hours (~7 Days), until the first access attempt, after which there was an access attempt every few days.
> 
> […]
> 
> The key take home from this research, that I think people in the cyber security industry should take, is that there are some pretty efficient threat actor groups out there that have optimized scraping open source online services for secrets and they will likely grab your token in a manner of minutes to hours depending on the online service. 
> 
> This means that if you have discovered that your organization’s secret has leaked somehow to one of these services you should **_Immediately roll the key and conduct a forensic investigation into any malicious usage of the key._** 


I’ve had people before say things like “We knew it was an issue wtihin minutes of pushing it and reverted.  The chances of someone knowing it is low right?” and honestly, it’s sometimes hard to answer that question.  

This research gives us some reasonable data on that.  While yes, you should rotate any secret that has been pushed into production, regardless of whether you know it has been stolen or not, it’s now far easier to say “Research shows that tokens leaked into major repositories such as github, npm or pypi are stolen and tested within seconds, so yes, I know it’s a pain, but rotate those secrets”.

I wouldn’t rely on any of the low numbers here as meaning you don’t need to rotate tokens, because it might just be luck.  This could also change over the coming weeks or months, as automated bots looking for credentials to sell might see a new place to scan, and start scraping them just as fast. 


## [Clutch - The Day We Unveiled the Secret Rotation Illusion ](https://www.clutch.security/blog/the-day-we-unveiled-the-secret-rotation-illusion)

[https://www.clutch.security/blog/the-day-we-unveiled-the-secret-rotation-illusion](https://www.clutch.security/blog/the-day-we-unveiled-the-secret-rotation-illusion)

> 
> * **Speed of Exploitation:** Secrets leaked on highly scanned platforms were compromised in seconds to minutes, with unauthorized activity peaking around early morning UTC.
> * **Illusion of Rotation:** Even when we rotated secrets hourly and re-leaked them, new keys were exploited just as quickly. This demonstrated that attackers work faster than most rotation schedules.
> * **Blind Spots in Logging:** Many SaaS platforms don’t log critical read operations. For instance, GitHub, Okta, OpenAI, and Twilio lack robust logging for non-privileged actions, meaning a malicious actor could quietly exfiltrate data without a trace. This absence is even more pronounced on platforms like CircleCI, which provides only daily audit logs without IP tracking.
> 
> [….]
> 
> * **Sophisticated Pivoting:** Attackers used these secrets to pivot, often escalating privileges or attempting lateral movement, particularly with AWS credentials. This isn’t a casual attacker stumbling upon exposed keys. It’s an automated, organized effort.
> 
> [….]
> 
> Analyzing the data, the illusion shattered: secret rotation, as practiced today, isn’t the robust security measure it’s believed to be. It’s a Band-Aid on a bullet wound, offering minimal protection against the speed and sophistication of modern cyber threats.
> 
> The reality is clear: the window between exposure and rotation leaves sufficient time for attackers to cause significant damage. Rotating secrets after they’ve been compromised is akin to locking the barn door after the horse has bolted. 


Again we see that you cannot assume that a secret that has been compromised wont be used by an attacker incredibly quickly.  We also see called out just how hard it can be to determine the actual impact of the breach, given how many SaaS tools provide logging capability.

I’m not entirely sure I totally agree with the finding here, because token rotation is the correct response to accidentally leaking a token.  In fact, I’d argue that if at all possible, for every token in your system, you may want an automated “roll token” button somewhere, that someone can click and it automatically rotates token.  This would make response as quick as failure.

Of course, the actual right answer here is that secrets simply shouldn’t exist anywhere you can possibly help it.   Secret Managers, Vaults and cryptographically secure passkeys that can’t be leaked and reused are all far better than manually typing API tokens everywhere.  Sadly, that’s not standardised anywhere, so it’s not as easy as saying “the right answer is” 


## [EMERALDWHALE:  15k Cloud credentials stolen in operation targeting exposed Git config files | Sysdig ](https://sysdig.com/blog/emeraldwhale/)

[https://sysdig.com/blog/emeraldwhale/](https://sysdig.com/blog/emeraldwhale/)

> Starting with long lists of IP address ranges, the toolset used by EMERALDWHALE automatically discovers relevant hosts, extracts credentials, and validates the recovered tokens. It then uses the stolen tokens to clone repositories, both public and private, belonging to any Git-compatible service. The tool scans the downloaded repositories and extracts more credentials. Finally, all of the results are uploaded to the S3 bucket.
> 
> We discovered that EMERALDWHALE was not only looking for misconfigured servers and exposed credentials but also had another technique at its disposal. It also used bulk web scraping, followed by extracting cloud credentials in the collected assets. We found dozens of folders with similar names, each containing downloaded assets from the targeted websites. For example, statically defined cloud credentials were found in Javascript files utilized by the website. 


[Ed: This was from last October, so “recently” is several months old at this point]

Not a lot to add to this other than a really useful reminder that developers are targets for a number of threat actors.  Even if you work on really boring stuff, or you think nobody is interested, your infrastructure might provide really useful covert command and control, so you should assume that people want to get at your secrets and protect them appropriately. 


## [Passkeys: they're not perfect but they're getting better - NCSC.GOV.UK ](https://www.ncsc.gov.uk/blog-post/passkeys-not-perfect-getting-better)

[https://www.ncsc.gov.uk/blog-post/passkeys-not-perfect-getting-better](https://www.ncsc.gov.uk/blog-post/passkeys-not-perfect-getting-better)

> Passkeys:
> 
> * are generated securely and so can’t be guessed
> * can’t be phished
> * are unique for each website you use, so if one website is compromised it doesn’t put your other logins at risk
> 
> Passkeys manage what was previously thought impossible. As well as being far more secure, they’re also quicker, easier and more convenient for users. For example, [Microsoft has seen](https://www.microsoft.com/en-us/security/blog/2024/12/12/convincing-a-billion-users-to-love-passkeys-ux-design-insights-from-microsoft-to-boost-adoption-and-security/) that on average passkey sign-ins to their services take only 8 seconds, compared with 69 seconds to sign in using a traditional password and second factor.
> 
> As a solution that’s designed to be easier for users **and** more secure, you might expect passkeys to be the NCSC’s default recommendation for websites authenticating their customers. But if you check out our guidance: [MFA for your corporate online services](https://www.ncsc.gov.uk/collection/mfa-for-your-corporate-online-services) and [Authentication methods: Choosing the right type](https://www.ncsc.gov.uk/guidance/authentication-methods-choosing-the-right-type) , you’ll see we’re currently still having to recommend options that include a password and something extra to secure it.
> 
> We welcome the year-on-year improvements in passkey technologies but the remaining problems with them means we aren't ready to recommend them for mass adoption across all services yet. The NCSC wants to see an acceleration in progress and collaboration, so that we can confidently recommend this technology as the most secure and usable form of online authentication.
> 
> […] **Account recovery processes** For passkey-protected accounts, potential attackers are now more likely to focus on finding weaknesses in account recovery and reset requests – whether by email, phone or chat – and pivot to phishing for recovery keys. These processes need to be sufficiently hardened by providers to prevent trivial abuse by these attackers and to maintain the security benefits of using passkeys. Users also need to be educated on how to spot and report abuse of these processes before their accounts are compromised. This problem is not unique to passkeys, but as passkeys begin to successfully frustrate attackers on a large scale, it’s likely that attackers will increasingly shift their focus to these methods. 


I’m really pleased to see that my views on passkeys are in line with the NCSC experts.  I’m really keen on passkeys and using them on a daily basis. 

As a security expert and technology expert, I find the issues all manageable so far, but I really worry that most users would struggle with some of the more fundamental issues.

But for personal use, I’m increasingly at the point where I’d encourage my family to enable passkeys for their email access only.  That access is the root of almost all modern security, and with a simple use case, most of the issues below can be dealt with.

Finally, that account recovery process is increasingly going to be targeted by attackers.  It might be worth in the next year doing a bit of a review of your organisations account recovery processes for critical accounts and making sure they are robust and secure. 


## [Millions of Accounts Vulnerable due to Google’s OAuth Flaw ◆ Truffle Security Co. ](https://trufflesecurity.com/blog/millions-at-risk-due-to-google-s-oauth-flaw)

[https://trufflesecurity.com/blog/millions-at-risk-due-to-google-s-oauth-flaw](https://trufflesecurity.com/blog/millions-at-risk-due-to-google-s-oauth-flaw)

> I purchased just one of these defunct domains and discovered that logging into each of the following services granted us access to old employee accounts:
> 
> * ChatGPT
> * Slack
> * Notion
> * Zoom
> * HR systems (containing social security numbers)
> * More…
> 
> The most sensitive accounts included HR systems, which contained tax documents, pay stubs, insurance information, social security numbers, and more.
> 
> Interview platforms also contained sensitive information about candidate feedback, offers, and rejections.
> 
> And of course, chat platforms contained direct messages, and all sorts of sensitive information that an attacker should never get their hands on. 


I was torn on including this one because I think the headline is slightly misleading.   The issue here is that when a startup shuts down, it lets its domain expire, and if you buy that domain, you can reinstatiate key peoples accounts and then get access to SaaS platforms.  This is because, for many platforms, they don’t make use of some features of Google’s OAuth that differentiates [mbs@domain.com](mailto:mbs@domain.com) in one google workspace from another mbs@domain.com in a second google workspace.

But in reality, OAuth has little to do with this, as with many SaaS platforms, possession of the fully validated domain name is probably sufficient to carry out complete password reset anyway.

The bigger question here for me, that isn’t explored in this blog, is why when a company shuts down, and stops paying their HR, Zoom, Slack or Notion bills, a year later when the domain expires, the data can be recovered by someone taking over the domain.

Sadly, for many of us, that final phase of a project,  “shutdown”, simply isn’t a thing we think about.  In a startup you don’t think about how to handle data deletion if we fail.  And for SaaS providers, if their customer stops paying, you might want to encourage them to come back later by retaining their data, becuase you probably can’t tell between “went to a competitor” versus “went bankrupt”.  But offboarding, and safe deletion of data is an important step that we need to think about more. 


## [New Star Blizzard spear-phishing campaign targets WhatsApp accounts | Microsoft Security Blog ](https://www.microsoft.com/en-us/security/blog/2025/01/16/new-star-blizzard-spear-phishing-campaign-targets-whatsapp-accounts/)

[https://www.microsoft.com/en-us/security/blog/2025/01/16/new-star-blizzard-spear-phishing-campaign-targets-whatsapp-accounts/](https://www.microsoft.com/en-us/security/blog/2025/01/16/new-star-blizzard-spear-phishing-campaign-targets-whatsapp-accounts/)

> The initial email sent to targets contains a quick response (QR) code purporting to direct users to join a WhatsApp group on “the latest non-governmental initiatives aimed at supporting Ukraine NGOs.” 
> 
> This code, however, is intentionally broken and will not direct the user towards any valid domain; this is an effort to coax the target recipient into responding.
> 
> When the recipient responds, Star Blizzard sends a second email containing a Safe Links-wrapped _t[.]ly_ shortened link as the alternative link to join the WhatsApp group.
> 
> When this link is followed, the target is redirected to a webpage asking them to scan a QR code to join the group. However, this QR code is actually used by WhatsApp to connect an account to a linked device and/or the WhatsApp Web portal. This means that if the target follows the instructions on this page, the threat actor can gain access to the messages in their WhatsApp account and have the capability to exfiltrate this data using existing browser plugins, which are designed for exporting WhatsApp messages from an account accessed via WhatsApp Web. 


This is a really neat attack vector, because the user is already assuming that something will happen with whatsapp so is unlikely to notice the compromise here.

I thought the error filled QR code was a good way to get the target to engage, which almost certainly raises the likelihood that they’ll fall for it because they are literally requesting teh attack from the attackers.

Of course, enabling WhatsApp Web will get around all of the end to end encryption in use in WhatsApp as well as around all of the ondevice protections that would protect your mobile device against remote attacks, so this works to get data, in the clear, over to attackers simply and easy. 


## [How to Build Smaller Container Images: Docker Multi-Stage Builds ](https://labs.iximiuz.com/tutorials/docker-multi-stage-builds?utm_source=cloudseclist.com&utm_medium=referral&utm_campaign=CloudSecList-issue-263)

[https://labs.iximiuz.com/tutorials/docker-multi-stage-builds?utm_source=cloudseclist.com&utm_medium=referral&utm_campaign=CloudSecList-issue-263](https://labs.iximiuz.com/tutorials/docker-multi-stage-builds?utm_source=cloudseclist.com&utm_medium=referral&utm_campaign=CloudSecList-issue-263)

> Almost any application, regardless of its type (web service, database, CLI, etc.) or language stack (Python, Node.js, Go, etc.), has two types of dependencies: build-time and run-time.
> 
> Typically, the build-time dependencies are much more numerous and noisy (read - have more CVEs in them) than the run-time ones. Therefore, in most cases, you'll only want the production dependencies in your final images.
> 
> However, build-time dependencies end up in production containers more often than not
> 
> […]
> 
> Below are examples of how to use Multi-Stage Builds to produce smaller and more secure container images for different languages and frameworks. 


I’ve been using docker multi-stage builds for some time, indeed even for CyberWeekly itself, which is a python application, along with a node.js build to generate the tailwind CSS. 

I was surprised to discover in conversation recently that this isn’t as well known knowledge as I had thought, and then this came up on my feed, so thought I’d share.

The other useful thing from this multistage build process is that you can use development secrets, such as private repos, CI build API keys during the build phase, and have some confidence that they won’t leak into the production build, since the copy is clear what does and doesn’t get copied across 


## [Holding Cloud Vendors to a Higher Security Bar | Wut.Dev Blog ](https://blog.wut.dev/2024/08/14/vendor-cloud-security.html)

[https://blog.wut.dev/2024/08/14/vendor-cloud-security.html](https://blog.wut.dev/2024/08/14/vendor-cloud-security.html)

> To state the obvious, having access to a customer’s cloud environment, in any form, is a position of tremendous trust and responsibility. A key element of that responsibility is demonstrating a commitment to cloud security best practices and integration practices that will safeguard not only the data the customer has directly shared, but the rest of their environment as well.
> 
> Frankly, I believe the cloud vendor industry needs to be held to a higher bar. A plethora of insecure practices seem to still prevail, despite years of more secure alternatives, and I believe that it’s up to customers to push back.
> 
> To be clear, both parties in the relationship bear responsibility:
> 
> * Customers are responsible for choosing the third-party vendors they integrate with (and reviewing the security of those integrations)
> * Vendors are responsible for adhering to cloud security best practices when integrating with customer’s cloud environments and providing safe configuration options for those customers
> 
> […]
> 
> Nothing makes me more impressed with (and likely to use) a vendor than one that simply says the following:Our application connects to your cloud via a third-party cross-account AWS IAM role. We generate a unique, external ID for use in the trust relationship and the IAM policy attached to the role has the following permissions…
> 
> When I read this, I know that you know (more or less) what you’re doing. 


I really liked this, and there’s an excellent checklist that you could provide to your commercial or contractual teams for good questions to ask up front.  There’s also a nugget in here about letting technical teams get involved a bit too late.  We all know that from a technical perspective, doing supplier due diligence and contract negotiation feels boring, but it’s also one of the most impactful things you can do.  Maybe it’s a good 20% time task for engineers to take on, reviewing, supporting and engaging suppliers on their technical connectivity requirements. 


## [AI-supported spear phishing fools more than 50% of targets | Malwarebytes ](https://www.malwarebytes.com/blog/news/2025/01/ai-supported-spear-phishing-fools-more-than-50-of-targets)

[https://www.malwarebytes.com/blog/news/2025/01/ai-supported-spear-phishing-fools-more-than-50-of-targets](https://www.malwarebytes.com/blog/news/2025/01/ai-supported-spear-phishing-fools-more-than-50-of-targets)

> Thus, the AI-automated attacks performed on
> par with human experts and 350% better than the control
> group. The results are a significant improvement from similar
> studies conducted last year, highlighting the increased deceptive
> capabilities of AI models. Our AI-automated emails were
> sent using a custom-built tool that automates the entire spear
> phishing process, including information gathering and creating
> personalized vulnerability profiles for each target. The AIgathered information was accurate and useful in 88% of cases
> and only produced inaccurate profiles for 4% of the participant 


This is a bit depressing.  I’ll note positively, that it doesn’t say that there is a rise in AI powered phishing.  What it does say is that if you are competent, and use AI to generate the phishing leads, then you are far more likely to fool your targets than writing them by hand.

That might lead to a rise in AI powered phishing, it will almost certainly lead to a rise in headlines about AI powered phishing, but it is still reliant on the human in the loop being able to use the tool well.

Of course, as always, my stance is that you should assume that users will click phishing emails, and your system should either prevent them getting to users in the first place, or prevent the click from actually realising damage.  Any “phishing training” that aims to reduce click rates as a primary purpose is wasted time and effort. 


## [Backdooring Your Backdoors - Another $20 Domain, More Governments ](https://labs.watchtowr.com/more-governments-backdoors-in-your-backdoors/)

[https://labs.watchtowr.com/more-governments-backdoors-in-your-backdoors/](https://labs.watchtowr.com/more-governments-backdoors-in-your-backdoors/)

> Put simply - we have been hijacking backdoors (that were reliant on now abandoned infrastructure and/or expired domains) that _themselves_ existed inside backdoors, and have since been watching the results flood in. This hijacking allowed us to track compromised hosts as they ‘reported in’, and _theoretically_ gave us the power to commandeer and control these compromised hosts.
> 
> Over 4000 unique and live backdoors later (the number continues to grow), we decided this research would never be finished, and it would be interesting to share the results in their current state.Note to the reader: We have intentionally obfuscated compromised hostnames (in most cases hueheuhueh), and our publishing of this research does not put any system at any additional risk.
> 
> Across those 4000 unique and live backdoors, we saw some systems of interest:
> 
> * Multiple compromised governments
> 
>     - Bangladesh
>     - China
>     - Nigeria
> * Compromised universities/higher education entities across Thailand, China, South Korea and more
> * and, of course, much much more (we’ve so far recorded over 300MB of logs to trawl through).
> 
> As always, we’re quick to remind everyone - we’re not the first to track hackers for fun, we no doubt won’t be the last. But, we have enjoyed continuing to exploit what truly appears to be a hugely underrated vulnerability class - **abandoned and expired infrastructure** - to basically give ourselves ‘theoretical’ free access to thousands of systems for the cost of a few (yet again) $20 domain names. 


It’s nice to know that the same flaws that affect defenders, such as letting some of your domains lapse, can also affect attackers.  

Looking at intermediating criminal activity by taking over their C2 domains is normally a law enforcement operation, and so details are rarely made public.  But WatchTowr’s examples here sets out a bit more about how bad actors use C2 systems and what you can do when you take them over. 


