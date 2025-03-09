---
title: "182 - Protecting the things protecting your infrastructure"
date: 2022-01-30
description: "Back in the good old days, we had really simple systems and services.  We had J2EE stacks and servers, and our systems communicated via JNDI lookups which totally couldn't be abused when logging things."
permalink: /protecting-the-things-protecting-your-infrastructure/
---

Back in the good old days, we had really simple systems and services.  We had J2EE stacks and servers, and our systems communicated via JNDI lookups which totally couldn't be abused when logging things.

But the problem with these systems is that they were often treated as singularly large systems that required complex deployment protocols to get the system released.  Back in around 2007, I was involved in an innovative (at the time) project to rebuild the Guardians core web system from a rather hacky (but artisanally lovely) set of services written in a programming language called TCL into a modern Java system.  

Our deployment process was complex, manual and error prone, so we automated it, which also meant automating our infrastructure and developing systems for storing our infrastructure as code in our central code repository and automatically applying it to the infrastructure

This leads to a problem, at least in security terms.  What do we do if someone can get bad code into our code repository?

You see, the downside to keeping all of our infrastructure controlling code in a code repository is that it becomes the place where we define what our protections are.  It becomes the place where firewall rules are encoded, the place where the rules preventing bad code being released are encoded, the place where tests that must be done before the code can be release are defined.

Once that set of definitions of the protections of the system are in a code repository, they become a thing that can be more easily attacked or bypassed.

One of the big changes in the last few years has been the mass adoption of these concepts, mostly for a security benefit, it means that this code can be audited, inspected, and tested, so we have far more confidence that there's not simply a line saying `ANY:ANY #Testing to see if this fixes bug 132, remove after 1 week` rule at the top of that firewall config.

But that means that the infrastructure that protects your system now needs protecting, and as a community we aren't as good at that work.  There's some good articles this week to cover the protection of that CI and build pipeline infrastructure.

Once we have common patterns and common ways to protect stuff, it's far easier to role out at scale.  That's something that's picked up and the foundation of the new Government Cyber Security Strategy as well.  The application of common patterns that are the same no matter what role you play.

Finally, those of you who read the newsletter on the [Cyberweekly website](https://www.cyberweekly.net/) might have noticed that I've given it a fresh lick of paint this week.  As well as this newsletter going out into your inboxes, I put it up on the website, with no ad trackers, no google analytics.  So if you prefer to read that way, I hope I've made it slightly more readable this week.  If you notice any bugs or issues, do let me know.

## [Securing Terraform monorepo CI | Mercari Engineering](https://engineering.mercari.com/en/blog/entry/20220121-securing-terraform-monorepo-ci/)

[https://engineering.mercari.com/en/blog/entry/20220121-securing-terraform-monorepo-ci/](https://engineering.mercari.com/en/blog/entry/20220121-securing-terraform-monorepo-ci/)

> At Mercari, one of the core platform tenets is to manage all cloud infrastructure in declarative configurations. Our main cloud provider is Google Cloud Platform (GCP) and we use HashiCorp Terraform to manage infrastructure as code. The Platform Infra team provides an in-house CI service to manage all terraform workflows securely.
> 
> Terraform requires cloud providers’ credentials for resource provisioning. To keep the system simple, we started storing these credentials as environment variables, but as the terraform usage started increasing, the blast radius of these credentials grew as well.
> 
> In this article, I’m going to explain the security problems we faced in our Terraform environment, and how we improved the situation.


This is an excellent if short article that covers some of the big risks of running CI systems that can manage and deploy your infrastructure code. It doesn't matter whether you are using CircleCI, CloudRun., AzureDevOps or whatever, these patterns are common and the issues that Mercari noted are also common.


## [10 real-world stories of how we’ve compromised CI/CD pipelines – NCC Group Research](https://research.nccgroup.com/2022/01/13/10-real-world-stories-of-how-weve-compromised-ci-cd-pipelines/)

[https://research.nccgroup.com/2022/01/13/10-real-world-stories-of-how-weve-compromised-ci-cd-pipelines/](https://research.nccgroup.com/2022/01/13/10-real-world-stories-of-how-weve-compromised-ci-cd-pipelines/)

> Mainstream appreciation for cyberattacks targeting continuous integration and continuous delivery/continuous deployment (CI/CD) pipelines has been gaining momentum. Attackers and defenders increasingly understand that build pipelines are highly-privileged targets with a substantial attack surface.
> 
> But what are the potential weak points in a CI/CD pipeline? What does this type of attack look like in practice? NCC Group has found many attack paths through different security assessments that could have led to a compromised CI/CD pipeline in enterprises large and small.
> 
> In this post, we will share some of our war stories about what we have observed and been able to demonstrate on CI/CD pipeline security assessments, clearly showing why there is the saying, “they are execution engines.”
> 
> Through showing many different flavors of attack on possible development pipelines, we hope to emphasize the criticality of securing this varied attack surface to better secure the software supply chain.


Your CI/CD pipelines is both a defensive asset and yet another bit of your software stack that can be compromised.

The advantage of the CI/CD pipeline is that it validates and verifies the security rules that should be run when code is being written.  If you've got a security enforcing test in your CI/CD pipeline, then you can massively build confidence that there will be fewer mistakes that make their way to production.

However, the CI/CD pipeline executes code and runs on systems and machines.  Often, compromising a CI/CD machine gives you huge lateral movement opportunities to compromise other systems or turn off those checks and balances, often invisibly.

It's pretty rare for CI/CD pipelines to be included in pentest scopes, and it's also depressingly rare for an organisation to invest in patterns and tooling to make CI/CD pipelines robust, so in the meantime, learn from people who have actually compromised CI/CD pipelines, and see what they did.


## [Government Cyber Security Strategy: 2022 to 2030 (HTML) - GOV.UK](https://www.gov.uk/government/publications/government-cyber-security-strategy-2022-to-2030/government-cyber-security-strategy-2022-to-2030-html)

[https://www.gov.uk/government/publications/government-cyber-security-strategy-2022-to-2030/government-cyber-security-strategy-2022-to-2030-html](https://www.gov.uk/government/publications/government-cyber-security-strategy-2022-to-2030/government-cyber-security-strategy-2022-to-2030-html)

> The first is to build a strong foundation of organisational cyber security resilience; ensuring that government organisations have the right structures, mechanisms, tools and support in place to manage their cyber security risks.
> 
> This will be underpinned by the adoption of the National Cyber Security Centre’s (NCSC) Cyber Assessment Framework (CAF) as the assurance framework for government, with government specific CAF profiles that articulate the outcomes required by government organisations in order to proportionately respond to the varying threats to their most important functions. Objective verification by independent auditors will be a requirement for central government departments, although it will be for lead government departments to adapt and apply such an approach in a way that is most appropriate for the public sector organisations within their scope. As well as improving visibility of cyber security risks, adopting the CAF provides a common framework for government to more effectively understand and manage them.


Last week the UK Government unveiled it's new Government Cyber Strategy.  It would be overly reductive to say that it says "be competent at cyber defences", but the reality is that government struggles even more than industry to actively shore up its defences.

Part of the problem is that unlike a commercial company, which might have a lot of different business units doing slightly different things, there's a reasonable edge to most commercial companies, but very little "edge" to government.  Government is required to do everything from managing diplomatic talks with foreign nations to balancinging the budget.  But it also has to inspect restaurants for food standards, count the number of trees, and manage student loans and thousands of other services and things that we expect government to do.

Cyber security strategies often seem to assume that Government is a special snowflake that is always worried about the most capable adversaries, and that every department should spend a small fortune on cyber security.  What's different about this strategy is the alignment to NCSC's Cyber Assessment Framework, which is the same framework that NCSC produced for commercial organisations.  This makes is clear and simple, organisations in government like the Forestry Commission, the Company Names Tribunal, or the Groceries Code Adjudicator should all be held the same standard that a typical organisation should.

This strategy goes a long way to giving those organisations a goal post to aim for, and a set of commercial auditors that can be used to determine how to get there.  There's no magic sauce, no special recipes, just essential cyber security hardening needed to get the Government up to a good standard.


## [New Chrome security measure aims to curtail an entire class of Web attack | Ars Technica](https://arstechnica.com/information-technology/2022/01/new-chrome-security-measure-aims-to-curtail-an-entire-class-of-web-attack/)

[https://arstechnica.com/information-technology/2022/01/new-chrome-security-measure-aims-to-curtail-an-entire-class-of-web-attack/](https://arstechnica.com/information-technology/2022/01/new-chrome-security-measure-aims-to-curtail-an-entire-class-of-web-attack/)

> Starting in Chrome version 98, the browser will begin relaying requests when public websites want to access endpoints inside the private network of the person visiting the site. For the time being, requests that fail won't prevent the connections from happening. Instead, they'll only be logged. Somewhere around Chrome 101—assuming the results of this trial run don't indicate major parts of the Internet will be broken—it will be mandatory for public sites to have explicit permission before they can access endpoints behind the browser.
> 
> The planned deprecation of this access comes as Google enables a new specification known as private network access, which permits public websites to access internal network resources only after the sites have explicitly requested it and the browser grants the request. PNA communications are sent using the CORS, or Cross-Origin Resource Sharing, protocol. Under the scheme, the public site sends a preflight request in the form of the new header Access-Control-Request-Private-Network: true. For the request to be granted, the browser must respond with the corresponding header Access-Control-Allow-Private-Network: true.


This is a huge security advantage against DNS rebinding attacks and similar.

The principle is that you go to attacker control evil.com out on the internet.  It uses a cross-origin request to something like bad.evil.com, which would be allowed under the normal cross domain rules.  But while evil.com is out on the internet, bad.evil.com has a DNS record that points to an internal IP address, like 192.168.0.1.  

Your browser, right now, will say that this is perfectly ok, and indeed there are a number of reasons that you might legitimately do this, especially if you are a SaaS provider who can provide an internal enterprise appliance for example.

However this attack has been used in the past to pivot attacks inside the corporate network.  Protecting against this is possible, for example [Cross Site Request Forgery prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html) using tokens can be quite common, but not every appliance, system or service you run internally will implement that.

This should fix the problem at the browser level, which will be quite nice, assuming of course that it doesn't fundamentally break anything.


## [Reducing Security Risks in Open Source Software at Scale: Scorecards Launches V4 - Open Source Security Foundation](https://openssf.org/blog/2022/01/19/reducing-security-risks-in-open-source-software-at-scale-scorecards-launches-v4/)

[https://openssf.org/blog/2022/01/19/reducing-security-risks-in-open-source-software-at-scale-scorecards-launches-v4/](https://openssf.org/blog/2022/01/19/reducing-security-risks-in-open-source-software-at-scale-scorecards-launches-v4/)

> Today, two members of the Open Source Security Foundation, Google and GitHub, are partnering to release Scorecards V4, featuring a new GitHub Action, an added security check, and scaled up scans of the open source ecosystem.
> 
> The Scorecards project was launched last year as an automated security tool to help open source users understand the risks of the dependencies they consume. Though the world runs on open source software, many open source projects engage in at least one risky behavior—for example, not enabling branch protection, not pinning dependencies, or not enabling automatic dependency updates. Scorecards makes it simple to evaluate a package before consuming it: a scan run with a single line of code returns individual scores from 0 to 10 rating each individual security practice (“checks”) for the project and an aggregate score for the project’s overall security. Today’s release of a Scorecards GitHub Action makes it easier than ever for developers to stay on top of their security posture.


This is a really nice proactive tool to help open source projects ensure that they have a healthy security posture.  I'm a big fan of scorecards more generally for enabling comparison both between projects within an organisation, but also in time for a given project, so you can see improvement over time.


## [Why the Belarus Railways Hack Marks a First for Ransomware | WIRED](https://www.wired.com/story/belarus-railways-ransomware-hack-cyber-partisans/)

[https://www.wired.com/story/belarus-railways-ransomware-hack-cyber-partisans/](https://www.wired.com/story/belarus-railways-ransomware-hack-cyber-partisans/)

> On Monday, a group of Belarusian politically motivated hackers known as the Belarusian Cyber Partisans announced on Twitter and Telegram that they had breached the computer systems of Belarusian Railways, the country's national train system, as part of a hacktivist effort the attackers call Scorching Heat. The hackers have since posted screenshots that appeared to show their access to the railway’s backend systems and claimed to have encrypted its network with malware, for which they would only provide decryption keys if the Belarus government met a list of demands. They’ve called for the release of 50 political prisoners detained in the midst of the country’s protests against dictator Alexander Lukashenko, as well as a commitment from Belarusian Railways to not transport Russian troops as the Kremlin prepares for a possible invasion of Ukraine on multiple fronts.
> 
> The hackers appear to have successfully made at least some of Belarusian Railways' databases inaccessible on Monday, according to Franak Viačorka, a technical advisor to Belarusian opposition leader Sviatlana Tsikhanouskaya. Viačorka says he confirmed the database outages with Belarusian Railway workers. The railway's online ticketing system was also taken down Monday; on Tuesday it displayed a message that “work is underway to restore the performance of the system” but remained offline. 
> 
> “At the command of the terrorist Lukashenka, #Belarusian Railway allows the occupying troops to enter our land. We encrypted some of BR's servers, databases, and workstations to disrupt its operations,” the Cyber Partisan hackers wrote on Twitter Monday, noting that the hackers were careful not to affect “automation and security systems” that could cause dangerous railway conditions.


While the Russia/Ukraine tensions will be watched for evidence of how states can interact on a cyber domain during military and sub-war thresholds, so we can also see the democratising power of the internet at work.

Despite the constant refrains of the media and cybersecurity firms about the power of Advanced Persistent Threats, the reality remains that most internet connected systems are poorly secured against a suitably incentivised adversary.  This can include "patriotic" independent hackers who are determined to have an impact on their countries political affairs.

Of course, if they are true independant hackers, then there's no powers within the normal diplomatic or military channels to control their actions, and on a world stage that is fraught with tension, a mistaken attribution could ignite a serious conflict.

And yet, within that space, we also have to consider that around the world, many independent hackers might be moonlighting for nation state capabilities, or might even be cover or false flag operations designed to exacerbate the situation.  The fact that almost nobody will know for certain seems likely to usher in a new, even more confusing "fog of war" for military operations in the future.


## [“BrokenSea” - OpenSea Bug Causes NFTs to Sell For < 1% of True Value](https://novuminsights.com/post/brokensea-opensea-bug-causes-nfts-to-sell-for-less-than-1percent-of-true-value/)

[https://novuminsights.com/post/brokensea-opensea-bug-causes-nfts-to-sell-for-less-than-1percent-of-true-value/](https://novuminsights.com/post/brokensea-opensea-bug-causes-nfts-to-sell-for-less-than-1percent-of-true-value/)

> A bug discovered in OpenSea’s NFT marketplace is reportedly causing high-value NFTs to be sold at extremely low prices. The floor price of BAYC (Bored Ape Yacht Club) is around 86 ETH (c.$200,000), but today a BAYC NFT was sold erroneously for 0.77 ETH (c.$1,850). Users of the platform have already taken to Twitter to express outrage:
> 
> 
> 
> Here’s how the bug works:
> When users delist an NFT for sale, they are supposed to pay a ‘gas-fee’ to return the token to the owner's wallet. Recently, users discovered that by transferring their NFT to another ETH address, the NFT would seemingly be delisted without paying gas. However, this only removes the NFT listing from the platform’s front-end (the user-interface of the marketplace). 
> 
> Opportunists were quick to discover that if the NFT in question was ever sent back to the original ETH wallet, it would still be purchasable on Rarible as the delisting gas-fee was never paid on OpenSea. More importantly, the bug causes OpenSea’s contract to scrape the NFT’s original listing price as the current listing price - this is what caused the BAYC NFT mentioned above to be purchased for less than $2,000. 


This is a a fascinating issue, because it's an issue with an inherent property of the "permanent" nature of the block chain and the ever present cost of transaction fees.

Of course, the irony of a selection of cryptoinvestors who normally exclaim the power of decentralised networks, complaining that the centralised marketplace they invest through should fix issues is totally lost on the crypto audience


## [One Source to Rule Them All: Chasing AVADDON Ransomware | Mandiant](https://www.mandiant.com/resources/chasing-avaddon-ransomware)

[https://www.mandiant.com/resources/chasing-avaddon-ransomware](https://www.mandiant.com/resources/chasing-avaddon-ransomware)

> In the last few years, ransomware has become one of the principal sources of income in the cybercrime ecosystem, with increased use of extortion by shaming victims, threatening to release exfiltrated data, and in some cases hitting them with distributed denial-of-service (DDoS) attacks.
> 
> This blog post explores activity, similarities and overlaps between multiple ransomware families related to AVADDON ransomware, serving as a case study to understand how ransomware operators think and continue to turn a profit in a constantly evolving cybercrime ecosystem.
> 
> Various RaaS services have prevailed in compromising critical targets, leading to major impacts on victim networks and to sizable ransom demands. AVADDON is one of these ransomware services.
> 
> The threat actor behind the AVADDON ransomware service started activity in June 2020 and continued operations until June 2021. The service was apparently shut down rapidly—and private encryption keys released—as governments prioritized the fight against ransomware operations with new legislation and increased law enforcement operations.


This is a really impressive peak behind the curtains of a modern RaaS operator.  In that year of operation, they released nearly 3000 encryption keys which can give a sense of scale of the operation (some 10 infections a day).  There's a good breakdown in here about the capabilities they needed to implement in order to run that, and the ransomware itself.


## [MoonBounce: the dark side of UEFI firmware | Securelist](https://securelist.com/moonbounce-the-dark-side-of-uefi-firmware/105468/)

[https://securelist.com/moonbounce-the-dark-side-of-uefi-firmware/105468/](https://securelist.com/moonbounce-the-dark-side-of-uefi-firmware/105468/)

> In the last year, there have been several public accounts on the ongoing trend of UEFI threats. Notable examples include the UEFI bootkit used as part of the FinSpy surveillance toolset that we reported on, the work of our colleagues from ESET on the ESPectre bootkit, and a little-known threat activity that was discovered within government organisations in the Middle East, using a UEFI bootkit of its own (briefly mentioned in our APT trends report Q3 2021 and covered in more detail in a private APT report delivered to customers of our Threat Intelligence Portal).
> 
> The common denominator of those three cases is the fact that the UEFI components targeted for infection reside on the ESP (EFI System Partition), a storage space designated for some UEFI components, typically based in the computer’s hard drive or SSD. The most notable elements of the ESP are the Boot Manager and OS loader, both invoked during the machine’s boot sequence and which also happen to be the subject of tampering in the case of the aforementioned bootkits.
> 
> While all of the above were seen in use by advanced actors, a different class of bootkits raises even higher concern. This one is made up of implants found in the UEFI firmware within the SPI flash, a non-volatile storage external to the hard drive. Such bootkits are not only stealthier (partially because of limited visibility by security products into this hardware component), but also more difficult to mitigate: flashing a clean firmware image in place of a malicious one can prove to be more difficult than formatting a hard drive and reinstalling an OS, which would typically eliminate ESP level threats.
> 
> MoonBounce is notable for being the third publicly revealed case of an implant from the latter class of firmware-based rootkits. Previous cases included LoJax and MosaicRegressor, which we reported on during October 2020. In that sense, MoonBounce marks a particular evolution in this group of threats by presenting a more complicated attack flow in comparison to its predecessors and a higher level of technical competence by its authors, who demonstrate a thorough understanding of the finer details involved in the UEFI boot process.


As this points out, UEFI attacks are increidbly difficult to pull off, require advanced levels of engineering, but if you can do so, it can be very very difficult to detect the compromise and to recover.

At the moment, this seems to be mostly restricted to nation state level APT's, and so outside the threat model of most organisations, but as we know, capabilities tend to flow downstream.  Whether this is worthwhile for criminals and therefore will flow down will depend on whether this enables them to make more money in some way.  The return on investment here to be stealthier and more persistent is far more attractive for espionage cases than financial gain.


## [Earth Lusca Employs Sophisticated Infrastructure, Varied Tools and Techniques](https://www.trendmicro.com/en_in/research/22/a/earth-lusca-sophisticated-infrastructure-varied-tools-and-techni.html)

[https://www.trendmicro.com/en_in/research/22/a/earth-lusca-sophisticated-infrastructure-varied-tools-and-techni.html](https://www.trendmicro.com/en_in/research/22/a/earth-lusca-sophisticated-infrastructure-varied-tools-and-techni.html)

> Earth Lusca’s infrastructure can essentially be grouped into two “clusters.” The first cluster is built using virtual private servers (VPS), rented from a service provider, that are used for the group’s watering hole and spear phishing operations, in addition to acting as a command-and-control (C&C) server for malware.
> 
> The second cluster is made up of compromised servers running old, open-source versions of Oracle GlassFish Server. Interestingly, this second cluster performs a different role in an Earth Lusca attack — it acts as a scanning tool that searches for vulnerabilities in public-facing servers and builds traffic tunnels within the target’s network. Like the first cluster, it also serves as a C&C server, this time for Cobalt Strike.
> 
> It’s possible that the group used portions of its infrastructure (particularly the scanning aspects) for diversion in order to trick security staff into focusing on the wrong parts of the network.


This is an interesting read, in part because of the fact that the group uses multiple TTP's at the same time.  It both scans public systems to see if it can compromise the system through the front door, as well as these watering hole or phishing attacks that attempt to compromise corporate endpoints inside the network.

It's not entirely clear from the report whether these were used in tandam against a target, or whether they were two different campaigns by the same actor.  The technical report does however go into detail of the post-exploitation phases, which are mostly as you'd expect, although there's one note in the technical report worth highlighting:

>Tracking down the source of the operation can prove to be difficult since threat actors usually hide their activities behind proxy servers located in different countries and regions. Occasionally, however, an attacker makes mistakes by forgetting to use their proxies or by misconfiguring them.

Yup, it looks like occasionally the attackers forget to turn on their VPN before connecting to their compromised machines.  Attackers make mistakes too.


