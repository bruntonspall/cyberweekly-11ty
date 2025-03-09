---
title: "196 - Knowing when you are compromised, and doing something about it"
date: 2022-05-22
description: "“Just log more” is the advice that we see most often from cybersecurity defenders and cyber talking heads (which reminds me of [Max Headroom](https://en.m.wikipedia.org/wiki/Max_Headroom)). "
permalink: /knowing-when-you-are-compromised-and-doing-something-about-it/
---

“Just log more” is the advice that we see most often from cybersecurity defenders and cyber talking heads (which reminds me of [Max Headroom](https://en.m.wikipedia.org/wiki/Max_Headroom)). 

But defenders are often sifting through mountains of log entries, and given the increasingly distributed nature of our systems, they might be getting logs from systems they neither control, not have any awareness of.  It’s incredibly difficult to tell between someone forgetting their password and taking a few tries and an attacker trying to brute force an account,  it’s even harder to tell the difference between an attacker and when IT have made a change to move a device and it’s constantly retrying to join the network.

That’s one of the reasons that I’m keen on interesting new detective techniques.  When we move applications and systems to the cloud, the new cloud native functionality means that defenders can have far more visibility of the system.  If the migration to the cloud is done well, with centrally visible infrastructure as code, centralised account provisioning, then defenders can look at indicators of compromise and compare them to the infrastructure as code.

Secondly, we should be really keen on indicators that are high signal and low noise.  Certain activities are almost always done only by attackers, or very rarely happen at all.  Traditional logging audit advice tells you to log every user logging into to every server, and that information *is* useful for going back through your logs when you know an attacker was in your system.  But for detecting attacker events, something that every single member of staff does every day is so much noise that you won’t see an attacker.  

This is where things like Canaries and deception technology can be useful.  Fake infrastructure like honeypots can look like tempting targets for attackers.  When they get their initial access onto your network, whether that’s through connecting to your VPN, compromising your end user devices, or whatever, they are going to scan the network and look for a central server that is unpatched, unmonitored and easy to pivot through the network on.   If those honeypots or canaries are never in real use by real people, then almost everything that touches them should be a real attacker (or a pen test, or someone running a scanner on your network).

But finally, you need to not just detect adversaries on your network, but you need to actually be able to do something about it.  That means working out where the attacks are coming from, and how the attacker got in.  Your systems that trigger alerts and watch for attackers need to be able to disambiguate exactly what thing went wrong and where.  The article on canaries gets to the point of this.  Deploying one canary is all well and good, but deploying a hundred requires you to work out exactly which canary has fired, on which system and from what device.

Managing that means that rolling out something like Canaries means you can’t just roll them out, you are going to need to build and deploy some form of Canary-as-a-service, meaning that application teams can easily self-service their detection needs, and that your defending team gets the data they need to marry these things up.  Bonus points if you can embed all of this into your container base images, so that they just work, out of the box, for each team without needing any intervention on their part.

Double tailscale blog posts this week, one that is somewhat fun about using TailScale for authentication with Minecraft, and one more serious about using the same pattern  with an Nginx reverse proxy.  Both enable your access control system to ditch passwords and rely instead on trusted device identity, which is a really neat trick.

## [Zero Maintenance AWS Canary Tokens That Scale | by William Bengtson | May, 2022 | Medium ](https://medium.com/@williambengtson/zero-maintenance-aws-canary-tokens-that-scale-b470c6f60da)

[https://medium.com/@williambengtson/zero-maintenance-aws-canary-tokens-that-scale-b470c6f60da](https://medium.com/@williambengtson/zero-maintenance-aws-canary-tokens-that-scale-b470c6f60da)

> When looking into implementing a honeytoken strategy in AWS, you might start with creating an AWS honeytoken from Thinkst Canary , a great tool for manually minting and tracking honeytokens for a variety of providers. After retrieving this unique honeytoken, you might choose to put it onto an EC2 instance to detect potential intrusion/compromise. This is a great start and gives you a proof-of-concept as to how honeytokens can be an asset to your company. The problem that you may then face is how to expand coverage and scale an AWS honeytoken strategy.
> 
> There are many approaches to scaling and deploying honeytokens. A common one would be to create a unique honeytoken per application and embed each token on the servers/containers (compute resources) belonging to the corresponding application. This can work really well depending on the number of applications deployed and the number of compute resources per application, but pinpointing which resource was compromised becomes difficult when there are many servers for a given application. This post describes an approach for scaling honeytokens in AWS while maintaining server level attribution no matter the cluster size or number of applications. The approach described requires little to no overhead or maintenance and can take advantage of existing monitoring and alerting pipelines. The overhead of managing the honeytoken infrastructure and deployment should not require a dedicated team. 
> 
> **AWS keys as a honeytoken** 
> 
> When it comes to detecting compromise in AWS, AWS keys are naturally very effective as honeytokens. Adversaries know that these keys are their best chance at privilege escalation — a result of traditionally poor practices around AWS IAM implementation. These poor practices manifest in many ways — the most common are over-privileged permissions attached to the particular key and storing the keys in “unsafe” places (plaintext in source code, a developer machine, slack, etc). Adversaries know that keys on a host are typically stored in a set number of places for scripts or the AWS SDKs to utilize which makes hunting for them on a server trivial. 


I’m a huge fan of honeytokens and other deceptive defences.  The main reason is that these are incredibly high signal notifications.  If someone gets into one your computers, they almost certainly will search for AWS tokens so that they can use them to attack the wider infrastructure.  But these tokens will absolutely never be used.  One being used is a 100% chance indicator that someone bad has managed to find your token.  But actually using them is easy for a single token, but rolling out hundreds of these tokens across your estate is far more complex to track and use.  This post gives you a good guid on how to implement that. 


## [The Cloudflare Bug Bounty program and Cloudflare Pages ](https://blog.cloudflare.com/pages-bug-bounty/)

[https://blog.cloudflare.com/pages-bug-bounty/](https://blog.cloudflare.com/pages-bug-bounty/)

> The Pages team had to solve a pretty difficult problem for Cloudflare Builds (our CI/CD build pipeline): how can we run untrusted code safely in a multi-tenant environment? Like all complex engineering problems, getting this right has been an iterative process. In all cases, we were able to quickly and definitively address bugs reported by security researchers. However, as we continued to work through reports by the researchers, it became clear that our initial build architecture decisions provided too large an attack surface. The Pages team pivoted entirely and re-architected our platform in order to use gVisor and further isolate builds.
> 
> When determining impact, it is not enough to find no evidence that a bug was exploited, _we must conclusively prove that it was not exploited_ . For almost all the bugs reported, we found definitive signals in audit logs and were able to correlate that data exclusively against activity by trusted security researchers.
> 
> However, for one bug, _while we found no evidence that the bug was exploited beyond the work of security researchers_ , we were not able meaningfully prove that it was not. In the spirit of full transparency, we notified all Pages users that may have been impacted.
> 
> Now that all the issues have been remedied, and individual customers have been notified, we’d like to share more information about the issues. 


This, and the associated write up over at [the AssetNote blogpost](https://blog.assetnote.io/2022/05/06/cloudflare-pages-pt1/)makes for a great read into how to protect a multi tenant system and the many ways you can get that wrong. 


## [Weak security controls and practices routinely exploited for initial access ](https://media.defense.gov/2022/May/17/2002998718/-1/-1/0/CSA_WEAK_SECURITY_CONTROLS_PRACTICES_EXPLOITED_FOR_INITIAL_ACCESS.PDF)

[https://media.defense.gov/2022/May/17/2002998718/-1/-1/0/CSA_WEAK_SECURITY_CONTROLS_PRACTICES_EXPLOITED_FOR_INITIAL_ACCESS.PDF](https://media.defense.gov/2022/May/17/2002998718/-1/-1/0/CSA_WEAK_SECURITY_CONTROLS_PRACTICES_EXPLOITED_FOR_INITIAL_ACCESS.PDF)

> Cyber actors routinely exploit poor security configurations (either misconfigured or left unsecured), weak controls, and other poor cyber hygiene practices to gain initial access or as part of other tactics to compromise a victims’ system. This joint Cybersecurity Advisory identifies commonly exploited controls and practices and includes best practices to mitigate the issues.
> 
> Best Practices to Protect Your Systems
> 
> * Control access.
> * Harden credentials.
> * Establish centralized log management.
> * Use antivirus.
> * Employ detection tools.
> * Operate services exposed on internet-accessible hosts with secure configurations.
> * Keep software updated. 


This is a good list of things you can do, mostly fairly easily, to improve your resistance to cyber attacks.  Increasingly good stuff coming out of CISA these days 


## [Image sizes miss the point ](https://blog.chainguard.dev/image-sizes-miss-the-point/)

[https://blog.chainguard.dev/image-sizes-miss-the-point/](https://blog.chainguard.dev/image-sizes-miss-the-point/)

> As illustrated above, images are built out of components which are layered on top of each other. While increased image complexity typically does involve increased image size, the important metric is the number of underlying components. The goal is always to reduce the number of components that are put into an image during the authoring process, which means that image size reduction tools often miss the point – scanners generally still have to deal with the same package set – while introducing their own technical and legal risks (a popular image optimization tool deletes license text from the images it optimizes making those images not legally redistributable!). 


Totally agree with this.  While it’s true that simpler images are probably smaller, it’s not about reducing size, but reducing attack surface that really matters.
Although our friends over in operations who have to store all the images and pay for the bandwidth of endlessly shipping them around your cluster will also appreciate smaller images! 


## [Cyber Threats 2021: A Year in Retrospect - PwC ](https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/cyber-year-in-retrospect.html)

[https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/cyber-year-in-retrospect.html](https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/cyber-year-in-retrospect.html)

> Digital quartermasters, or groups that supply malicious tools like malware to other groups, have been traditionally associated with providing technology to military units. But in 2021, we also saw more “commercial quartermasters,” or companies selling offensive security capabilities such as spyware, 0-day exploits, and related capabilities to more customers based in numerous countries. 


This growth in initial access brokers and other Quartermasters, from zero day resellers, to purveyors of bullet proof hosting is a good indication of the growth of a financially effective offensive cyber industry.  One that will enable crime as well as grey zone activities such as corporate espionage, information leaking and of course nation state operations from lower capability states.

As a side note, I’ve never heard anyone call them Quartermasters before, but as a term I like it, not least because it’s the origin of the code name for James Bond famous gadget supplier, Q, who was Bond’s Quartermaster in the books.


## [Malicious PyPI package opens backdoors on Windows, Linux, and Macs ](https://www.bleepingcomputer.com/news/security/malicious-pypi-package-opens-backdoors-on-windows-linux-and-macs/)

[https://www.bleepingcomputer.com/news/security/malicious-pypi-package-opens-backdoors-on-windows-linux-and-macs/](https://www.bleepingcomputer.com/news/security/malicious-pypi-package-opens-backdoors-on-windows-linux-and-macs/)

> On May 17, 2022, threat actors uploaded a malicious package named 'pymafka' onto PyPI. The name is very similar to PyKafka, a widely used Apache Kafka client that counts over four million downloads on the PyPI registry.
> The typo-squatted package only reached a download count of 325 before it got removed. However, it could still cause significant damage to those affected as it allows initial access to the internal network of the developer.
> Sonatype discovered pymafka and reported it to PyPI, who removed it yesterday. Nevertheless, developers who downloaded it will have to replace it immediately and check their systems for Cobalt Strike beacons and Linux backdoors. 


This is why security researchers shouldn’t actually carry out supply chain attacks, because it makes them hard to disambiguate from real attacks like this. 


## [Mozilla patches Wednesday’s Pwn2Own double-exploit… on Friday! – Naked Security ](https://nakedsecurity.sophos.com/2022/05/21/mozilla-patches-wednesdays-pwn2own-double-exploit-on-friday/)

[https://nakedsecurity.sophos.com/2022/05/21/mozilla-patches-wednesdays-pwn2own-double-exploit-on-friday/](https://nakedsecurity.sophos.com/2022/05/21/mozilla-patches-wednesdays-pwn2own-double-exploit-on-friday/)

> Fast-forward to Wednesday, and Paul’s session started with 30’00” on the clock, counting downwards (a hard upper bound of 30 minutes is imposed for each entrant).
> After a brief pause, the adjudicator reached out and clicked a button to initiate the hacking attempt by visiting a URL that was ready to unleash Paul’s double-exploit remotely. (The server was remote in network terms; physically it was on the same table as the client under attack.)
> Loosely speaking, Paul planned to break into Firefox, earning $50,000’s worth of bug bounty for _remote code execution_ , and then to break back out of it, earning another $50,000 for a _full sandbox escape_ .
> About seven elapsed seconds later, with a fist pump of acknowledgment from the adjudicator (Pwn2Own is exciting for everyone, not just the hackers), and with an unsurprisingly happy smile from Manfred Paul, now $100,000 better off, the clock was stopped, having just flipped over to show 29’52”. 


It must be fascinating to watch your exploit run, months of work, making the exploit reliable and repeatable, and then 7 seconds on tenseness while you hope nothing changed to affect your exploit. 


## [2022-unit42-ransomware-threat-report-final.pdf ](https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/reports/2022-unit42-ransomware-threat-report-final.pdf)

[https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/reports/2022-unit42-ransomware-threat-report-final.pdf](https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/reports/2022-unit42-ransomware-threat-report-final.pdf)

> Ransomware-as-a-Service Is Quickly
> Lowering the Technical Bar
> 
> Ransomware has proven to be an effective
> mechanism for cybercriminals to hit it big,
> in terms of both payouts and notoriety. This
> has led to an evolution of the ransomware
> scene with “entrepreneurial” threat actors
> looking to capitalize on a growing number
> of cybercriminals who want in. These
> entrepreneurs have started offering RaaS. This
> is a business for criminals, by criminals, with
> agreements that set the terms for providing
> actual ransomware to affiliates, often in
> exchange for monthly fees or a percentage of
> ransoms paid. RaaS makes carrying out attacks
> that much easier, lowering the barrier to entry
> and expanding the reach of ransomware. We
> are actively tracking at least 56 active RaaS
> groups, some of whom have been operating
> since 2020. Due to the success of these groups,
> we expect activity of this type to continue
> to grow.
> 
> Attackers Are Making Increasing Use
> of Zero-Days
> 
> Ransomware attacks often leverage a wide
> variety of vulnerabilities as an initial vector of
> compromise. In 2021, we observed at least 42
> vulnerabilities across different technologies
> being used by ransomware operators.
> 
> [...]
> 
> As long as vulnerabilities are available (unpatched), attackers will take advantage of them to
> further their objectives. It’s important to keep in mind that attackers may also take advantage of
> vulnerabilities in third-party software or attack supply chain elements, which can introduce risks
> for many organizations down the line. We saw this with REvil in the Kaseya attacks.
> Organizations may have previously grown used to taking time between the disclosure of a
> vulnerability and patching it, but while it’s still necessary to perform due diligence on a patch,
> attackers’ ability to scan the internet in search of vulnerable systems means it’s more important
> than ever to shorten the time it takes to patch. Organizations need to ramp up patch management
> and orchestration to try to close these known holes as soon as possible. 


Unit42 are still forecasting a growth in the Ransomware market.  Personally I think the combination of previous Russian government activity against REvil and now the sanctions on Russian economic interests is going to make for a much more difficult environment for ransomware operators to operate in, so I’m not so sure that it’s going to grow.

However, Unit42’s prediction that Ransomware-as-a-service is lowering the technical bar for ransomware operators, generally lifting the capability and helping sustain that market is completely correct.  Unless there’s some form of market disruption in this area, that will continue to grow and we’ll see many more small outfits using TTP’s and capabilities that they wouldn’t otherwise have access to. 


## [Tailscale Authentication for NGINX · Tailscale](https://tailscale.com/blog/tailscale-auth-nginx/)

[https://tailscale.com/blog/tailscale-auth-nginx/](https://tailscale.com/blog/tailscale-auth-nginx/)

> Previously on the Tailscale blog, I walked through how authentication works with Tailscale for Grafana and even for Minecraft. Today we’re going to take that basic concept and show how to extend it to services that you have proxied behind NGINX.
> The Grafana/Minecraft authentication proxy trick works because we set up a whole new node on your tailnet to proxy traffic directly to Grafana or Minecraft. This does work, but there’s a nonzero setup cost every time you add a new service to the mix. If you have an existing NGINX configuration for all your internal services, it may be easier to just use NGINX to proxy access to everything.
> I have created nginx-auth to implement the NGINX HTTP subrequest authentication protocol. You can use this to authenticate every request to your internal services and then decorate requests to them with the right HTTP headers.


Tailscale, for those who’ve missed it, is a trivially easy to deploy VPN that doesn’t route traffic by default.  It’s really easy to roll out on mobiles and end points to give them access to corporate resources, without requiring you to back haul all of that Netflix traffic.  In an interesting reversal of the zero trust principles, because Tailscale itself is highly authenticated (at a device level), this shows how you can use that to bind services to users who are “only on the Tailscale network”.  The only gotcha I’d say here is that what you are getting from TailScale is device identity rather than user identity, but that might be good enough, especially for single user devices like phones that have a hard binding to their user. 


## [Tailscale Authentication For Minecraft · Tailscale ](https://tailscale.com/blog/tailscale-auth-minecraft/)

[https://tailscale.com/blog/tailscale-auth-minecraft/](https://tailscale.com/blog/tailscale-auth-minecraft/)

> You can do many things with computers. Some of them are more productive than others. My recent blog post shows how to authenticate to any service, such as Grafana. Some people took the idea of using Tailscale for authenticating to any service as a neat fact. Others took this as a challenge to come up with even more creative applications of Tailscale for authentication. This is the story of one of the latter cases. This is how you can make your Minecraft server join your tailnet and authenticate to it with Tailscale.
> One big question you may be asking is, “why on earth would you want to do this?” I would like to counter this with another question: “why not?” As a great man has said, “science isn’t about ‘why?’ it’s about ‘why not?’” We take this philosophy seriously at Tailscale.
> Putting your Minecraft server into your tailnet with Tailscale for authentication gives you these advantages:
> You can lock down your Minecraft server to just your tailnet so only people you know can access it.
> You can use ACLs to lock down access even further (if you want to allow everyone but the known griefer to connect).
> You can attribute Minecraft users to Tailscale users to allow you to keep a better log of who is using the server.
> You do not have to modify your Minecraft server with Forge, Bukkit, Paper or Spigot mods, this allows you to use a fully vanilla setup with very little extra configuration.
> You can use Node Sharing to add your friends, compatriots in blood, and squadmates to your Minecraft server without having to expose it to the scary internet. You can also expose it to your hopefully less scary friends that are on your tailnet already.
> Your Minecraft server will show up on your tailnet like any other machine.


Very cute


