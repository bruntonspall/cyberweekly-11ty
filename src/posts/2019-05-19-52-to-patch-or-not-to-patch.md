---
title: "52 - To patch or not to patch"
date: 2019-05-19
description: "It has been quite a week of breaches.  From [WhatsApp](https://arstechnica.com/information-technology/2019/05/whatsapp-vulnerability-exploited-to-infect-phones-with-israeli-spyware/), to [vulnerabilities in the linux kernel](https://www.bleepingcomputer.com/news/security/linux-kernel-prior-to-508-vulnerable-to-remote-code-execution/), [hardware](https://9to5mac.com/2019/05/14/intel-zombieload-vulnerability-mac/), [Windows](https://blogs.technet.microsoft.com/msrc/2019/05/14/prevent-a-worm-by-updating-remote-desktop-services-cve-2019-0708/) and [Cisco products](https://thrangrycat.com/) and I'm sure I've forgotten some others already."
permalink: /to-patch-or-not-to-patch/
---

It has been quite a week of breaches.  From [WhatsApp](https://arstechnica.com/information-technology/2019/05/whatsapp-vulnerability-exploited-to-infect-phones-with-israeli-spyware/), to [vulnerabilities in the linux kernel](https://www.bleepingcomputer.com/news/security/linux-kernel-prior-to-508-vulnerable-to-remote-code-execution/), [hardware](https://9to5mac.com/2019/05/14/intel-zombieload-vulnerability-mac/), [Windows](https://blogs.technet.microsoft.com/msrc/2019/05/14/prevent-a-worm-by-updating-remote-desktop-services-cve-2019-0708/) and [Cisco products](https://thrangrycat.com/) and I'm sure I've forgotten some others already.

Of course, us enlightened security professionals like to tell people, "Just patch, it's the single best thing you can do".  And it's true, it is the right advice, but we sometimes say that it is basic advice, as if patching is the easiest thing in the world.

But our contexts differ massively. If you run a set of docker containers in a cloud providers managed Kubernetes cluster, then the way that you patch and the impact of applying a patch is significantly different to if you run an industrial control system.

While it's easy to wave at the two ends of the patch complexity spectrum, it's also harder when we talk about just different forms of Corporate IT.  This week, [a major RDP big was announced and patched by Microsoft](https://blogs.technet.microsoft.com/msrc/2019/05/14/prevent-a-worm-by-updating-remote-desktop-services-cve-2019-0708/).  Everyone, [including the NCSC](https://twitter.com/NCSC/status/1129479583517036544), are telling you to patch your IT.  But what if this patch included something that broke for your users, say, [a faulty update to the HSTS header that breaks many gov.uk domains](https://www.ghacks.net/2019/05/17/latest-windows-10-updates-break-access-to-some-uk-government-websites/)?  Should you patch to prevent what is still just a potential worm, and guarantee breaking your users web browsing experience?

What about patching your sharepoint instances, or your cisco infrastructure?  How easy is it to apply those patches and not accidentally cut off traffic to some important devices?  

In a perfect world, one can decide to roll out patches to the most critical servers without having to roll them out to all servers, or you can direct patches to a core set of users and test that the patch works and applies correctly before rolling it out to more users.  But who should be part of your testing cohort?  Maybe IT should have the update rolled out first, so they get the pain and disruption, but that means that they also always have the newest and shiniest tools, maybe they should be left to last?  Making these decisions requires people, requires the space to think and make these decisions, and that's not easy to find in most organisations.

It's easy for us to say that patching is the basics, but that doesn't mean it's easy, simple or trivial to do.  It does however remain probably the most effective security intervention you can make.

In other news, this is the 52nd edition of CyberWeekly, meaning that I've been writing these newsletters for a year now.  It's been very therapeutic and valuable for me to sit and write on a regular basis, and I hope that you find it at least half as interesting and useful to read.  Here's to another year of newsletters, and hopefully not quite so many breach reports!

## [GCHQ’s real agent “Q”](https://www.newstatesman.com/spotlight/cyber/2019/05/gchq-s-real-agent-q)

[https://www.newstatesman.com/spotlight/cyber/2019/05/gchq-s-real-agent-q](https://www.newstatesman.com/spotlight/cyber/2019/05/gchq-s-real-agent-q)

> But the government has not created new specialised risk management units for Ericsson and Nokia. Alongside the question of whether or not a piece of Huawei kit is, as Levy puts it, “a bag of spanners” is the fact that it was made by a Chinese company. Levy says that GCHQ began looking at Huawei equipment in 2003, under the assumption “that any company in China could be compelled by the Chinese state to do anything they want… to assume anything else would be crazy. They helpfully codified that into law, a couple of years ago.” China’s “geopolitical and legal differences”, he says, mean that from a security point of view, “Huawei is riskier than other vendors”.
> 
> However, it would also be simplistic to think that espionage by the Chinese state would only come via Chinese equipment. Levy points to Juniper Networks, a large American producer of network technology. “Juniper’s source code system was hacked,” says Levy, “probably by the Chinese, and back doors were put into Juniper’s code. Nobody noticed for a year.” No company is above suspicion. “It’s a different set of risks, depending on how you use different vendors.”


This was an interesting interview with Ian Levy, one peppered with the sorts of quotes that are easily attributable to him.  "Bag of spanners" is a great phrase for describing a very shonky bit of kit.

But the serious point in here, that has been forgotten in the Huawei discussions is this second point.  That while there are some additional risks with Huawei's connection with China, actually they suffer from the same risks as all our technology vendors, that their code and their software is complex and hard to audit. That we should assume that malign actors want to gain access to those systems either through finding and exploiting natural vulnerabilities in those systems or by actively attempting to put vulnerabilities into those systems.


## [Git ransom campaign incident report—Atlassian Bitbucket, GitHub, GitLab](https://github.blog/2019-05-14-git-ransom-campaign-incident-report/)

[https://github.blog/2019-05-14-git-ransom-campaign-incident-report/](https://github.blog/2019-05-14-git-ransom-campaign-incident-report/)

> Subsequently, the bad actor performed command line Git pushes to repositories accessible to these accounts at very high rates, indicating automated methods. These pushes overwrote the repository contents with the ransom note above and erased the commit history of the remote repository. Incident responders from each of the three companies began collaborating to protect users, share intelligence, and identify the source of the activity. All three companies notified the affected users and temporarily suspended or reset those accounts in order to prevent further malicious activity.
> 
> During the course of the investigation, we identified a third-party credential dump being hosted by the same hosting provider where the account compromise activity had originated. That credential dump comprised roughly one third of the accounts affected by the ransom campaign. All three companies acted to invalidate the credentials contained in that public dump.
> 
> Further investigation showed that continuous scanning for publicly exposed .git/config and other environment files has been and continues to be conducted by the same IP address that conducted the account compromises, as recently as May 10. 


This is a novel form of attack, by force pushing and destroying all the commits, you essentially hold the code to ransom.  However Git was designed as a decentralised version control, so everyone who has cloned the source should have the entire codebase with it's entire history, which limits the impact somewhat.

The fact that this was being done by reused credentials reinforces the fact that all three of these providers enables you to mandate 2FA for your developers, and developers are technically savvy enough to manage 2FA easily, so there's no downside to doing so.


## [Why we know your password, and what you can do about it](https://medium.com/dxwcyber/why-we-know-your-password-and-what-you-can-do-about-it-4997725b0aa)

[https://medium.com/dxwcyber/why-we-know-your-password-and-what-you-can-do-about-it-4997725b0aa](https://medium.com/dxwcyber/why-we-know-your-password-and-what-you-can-do-about-it-4997725b0aa)

> When dxw cyber carries out attack simulations, we search published data breaches for details of known users to help us identify the passwords they use to log into other places. When we find their passwords, we try them out against their accounts in the system we’re targeting.
> 
> During a recent attack simulation, this simple password lookup — that requires no technical skills at all — gave us access to the entire system at the highest possible level.


Good general advice on passwords, and some good reasoning for why.  I'm sure we all know this by now, but complex password policies often backfire, and ensure that it's actually far easier to guess passwords rather than harder.  

It's sad that even today, pen testing firms really don't have to try very hard to get access to a lot of systems.  A sensible password policy and pushing the use of MFA and password managers is a hugely effective security intervention that you can do today.


## [DevOps Topologies](https://web.devopstopologies.com/#)

[https://web.devopstopologies.com/#](https://web.devopstopologies.com/#)

> So what team structure is right for DevOps to flourish? Clearly, there is no magic conformation or team topology which will suit every organisation. However, it is useful to characterise a small number of different models for team structures, some of which suit certain organisations better than others. By exploring the strengths and weaknesses of these team structures (or ‘topologies’), we can identify the team structure which might work best for DevOps practices in our own organisations, taking into account Conway’s Law.


This is a great writeup of different ways that teams can implement DevOps, along with a large number of ways that the authors have seen organisations claim to implement DevOps, but fail to gain the benefits.

One of the keys to delivering strategy effectively is to be able to talk about it, with a shared language, and to be able to identify different contexts, so that you can identify different plays that work.  This sort of resource is absolutely valuable for anyone thinking about implementing DEvOps, or anyone who has a DevOps team or culture but isn't seeing the benefits as much as they thought.


## [Welcome to the updated Service Standard - Government Digital Service](https://gds.blog.gov.uk/2019/05/09/welcome-to-the-updated-service-standard/)

[https://gds.blog.gov.uk/2019/05/09/welcome-to-the-updated-service-standard/](https://gds.blog.gov.uk/2019/05/09/welcome-to-the-updated-service-standard/)

> We’re really proud of the impact the Digital Service Standard has had. It’s contributed to the growth in digital maturity across government, to the extent that the best government services are now among the simplest, most accessible services around.
> 
> But we think things can get better still – and that the updated standard is the first step on an exciting journey to making that happen.
> 
> [...]
> 
> Some of those extra questions will relate to things that aren’t within a digital service team’s  direct control. For instance, you might be asked about the offline parts of your service when you come in for assessment.
> 
> We’re not asking digital teams to take responsibility for these things: we’re asking digital teams to make sure they’re talking to the right people, and for the organisation as a whole to support those conversations.


This updated service standard is a good iteration of the previous standard.

It's really hard in Government to get the balance between iterating, changing and updating things to stay fresh, and keeping them stable enough that people get to understand them.  The GDS service standard is something that has needed updating for a while, based on all of the feedback and data that GDS gets from it's assessment processes as well as feedback from delivery teams.  But there's a whole culture and niche enterprise in people and consultants who understand the old standard, and so migrating to this new one will be hard for some people.

Having spent a lot of time assessing teams against the standard and involved in conversations about the standard and evolving it, I don't think this change actually changes huge amounts of it.  It sharpens it up in a few places, expands it to covers new areas, but all of those things were things that were often intended by the original authors, so this shouldn't be a surprise to that many people.

I'll be looking forward to more guidance from GDS on how they think you can meet the standard, especially in some of the new areas, such as working with the non digital portions of a service.


## [Top-Tier Russian Hacking Collective Claims Breaches of Three Major Anti-Virus Companies](https://www.advanced-intel.com/blog/top-tier-russian-hacking-collective-claims-breaches-of-three-major-anti-virus-companies)

[https://www.advanced-intel.com/blog/top-tier-russian-hacking-collective-claims-breaches-of-three-major-anti-virus-companies](https://www.advanced-intel.com/blog/top-tier-russian-hacking-collective-claims-breaches-of-three-major-anti-virus-companies)

> In March 2019, Fxmsp stated they could provide exclusive information stolen from three top anti-virus companies located in the United States. They confirmed that they have exclusive source code related to the companies' software development. They are offering to sell it, and network access, for over $300,000 USD.
> 
> [...]
> 
> Most recently, the actor claimed to have developed a credential-stealing botnet capable of infecting high-profile targets in order to exfiltrate sensitive usernames and passwords. Fxmsp has claimed that developing this botnet and improving its capabilities for stealing information from secured systems is their main goal.
> 
> [...]
> 
> According to “ShadowRunTeam,” a high-profile Russian threat actor operating on Telegram, Fxmsp is reportedly a Moscow resident with the first name "Andrey" who started to engage in cybercrime activities in mid-2000 and specialized in social engineering. 
> 
> Our subject matter experts assess with high confidence that Fxmsp is a credible hacking collective that has a history of selling verifiable corporate breaches returning them profit close to $1,000,000 USD. AdvIntel alerted US law enforcement regarding the purported intrusions.


This "security report" is very vague and scary, and some of the detail is suspicious.  Is this a highly capable group that has advanced capabilities or a guy called "Andrey"?  What actually is a "credential stealing botnet" as that phrase makes no sense as far as I can tell.

If this is true, and someone has made off with the source code to some of the largest anti virus engines, then to malware writers this is incredibly valuable, since they can look at what the detection systems are looking for and see if they can write their code to get around it.

Additionally, it's worth remembering that antivirus is almost always running as the system administrator, and so if you can find a vulnerability in the malware detection engine itself, you can compromise machines via the malware scanner itself.

However, as I said, I'm slightly dubious of this report and unless it's confirmed by other sources, wouldn't recommend uninstalling your antivirus just yet!


## [Google warns Bluetooth Titan security keys can be hijacked by nearby hackers | Ars Technica](https://arstechnica.com/information-technology/2019/05/google-warns-bluetooth-titan-security-keys-can-be-hijacked-by-nearby-hackers/)

[https://arstechnica.com/information-technology/2019/05/google-warns-bluetooth-titan-security-keys-can-be-hijacked-by-nearby-hackers/](https://arstechnica.com/information-technology/2019/05/google-warns-bluetooth-titan-security-keys-can-be-hijacked-by-nearby-hackers/)

> While people wait for a replacement, Brand recommended that users use keys in a private place that’s not within 30 feet of a potential attacker. After signing in, users should immediately unpair the security key. An Android update scheduled for next month will automatically unpair Bluetooth security keys so users won’t have to do it manually.
> 
> Brand said that iOS 12.3, which Apple started rolling out on Monday, won’t work with vulnerable security keys. This has the unfortunate result of locking people out of their Google accounts if they sign out. Brand recommended people not sign out of their account. A good safety measure would be to use a backup authenticator app, at least until a new key arrives, or to skip Brand’s advice and simply use an authenticator app as the primary means of two-factor authentication.


Sigh.  This is not a good recommendation for users.  Not using your 2FA devices while within 30 feet of a *potential* attacker, which could be anybody!

These bluetooth enabled titan keys have been widely derided by the other makers of 2FA devices on the basis that Bluetooth is such a poor protocol from a security perspective.  I'd advise either getting the NFC, USB versions from Google, or one of the major competitors.


## [Introducing GitHub Package Registry - The GitHub Blog](https://github.blog/2019-05-10-introducing-github-package-registry/)

[https://github.blog/2019-05-10-introducing-github-package-registry/](https://github.blog/2019-05-10-introducing-github-package-registry/)

> GitHub Package Registry is fully integrated with GitHub, so you can use the same search, browsing, and management tools to find and publish packages as you do for your repositories. You can also use the same user and team permissions to manage code and packages together. GitHub Package Registry provides fast, reliable downloads backed by GitHub’s global CDN. And it supports familiar package management tools: JavaScript (npm), Java (Maven), Ruby (RubyGems), .NET (NuGet), and Docker images, with more to come.


In what shouldn't really be a surprise to many, Github is moving into the packaging game.  It's already the repository of choice for many open source projects, and is built into some package management tools.  This could be interesting to watch, as the data and information that Github and Microsoft get from this is enormous.  Whether they'll work on solving the supply chain attestation problem, or at least improving it will be another matter as well.  I'd like to see better assurances that the software packages that are up there came from the original authors and haven't been changed by outsiders. 


## [Sharepoint vulnerability exploited in the wild | AT&T Alien Labs](https://www.alienvault.com/blogs/labs-research/sharepoint-vulnerability-exploited-in-the-wild)

[https://www.alienvault.com/blogs/labs-research/sharepoint-vulnerability-exploited-in-the-wild](https://www.alienvault.com/blogs/labs-research/sharepoint-vulnerability-exploited-in-the-wild)

> AT&T Alien Labs has seen a number of reports of active exploitation of a vulnerability in Microsoft Sharepoint (CVE-2019-0604).
> 
> One report by the Saudi Cyber Security Centre appears to be primarily targeted at organisations within the kingdom.
> 
> An earlier report by the Canadian Cyber Security Centre identified similar deployment of the tiny China Chopper web-shell to gain an initial foothold.


Sharepoint instances that are open to the web are vulnerable to a [slightly complicated file parsing bug](https://www.thezdi.com/blog/2019/3/13/cve-2019-0604-details-of-a-microsoft-sharepoint-rce-vulnerability).  This was patched by Microsoft back in February/March, but of course many people haven't patched, and several people have noticed this being weaponised.

Looking at the bug, this isn't very easy to weaponise, and neither is it that easy to exploit, so the fact that it is being exploited is interesting.


## [Software update crashes police ankle monitors in the Netherlands | ZDNet](https://www.zdnet.com/article/software-update-crashes-police-ankle-monitors-in-the-netherlands/)

[https://www.zdnet.com/article/software-update-crashes-police-ankle-monitors-in-the-netherlands/](https://www.zdnet.com/article/software-update-crashes-police-ankle-monitors-in-the-netherlands/)

> The faulty update effectively stopped traffic from ankle monitors from reaching the Department of Justice's DV&O control rooms, preventing officials from knowing the locations of suspects in house arrests or released on bail.
> 
> The issue was fixed later in the day, on Thursday; however, the Dutch Ministry of Justice and Security had to step in and preemptively arrest and jail some of its most high-risk suspects.
> 
> Dutch police also stepped up to help during the downtime, either by performing house visits or by calling suspects and asking them to check in at police stations or with officers.


There's always a risk when patching that it will go wrong, and when the thing you are patching is tracking convicted criminals to goefence them and prevent them visiting their victims, or leaving certain zones, then having a failing patch is a really serious issue.

the language of the press release, that the ankle monitors traffic was no longer reaching the control rooms, implies to me that this might not have been a firmware update of the ankle monitors, but actually a network, firewall or management backplane update on the traffic receiving side.   If that's the case, then not being able to fix it for 24 hours is quite a serious issue.


## [RIDL and Fallout: MDS attacks](https://mdsattacks.com/)

[https://mdsattacks.com/](https://mdsattacks.com/)

> Dont attackers need local execution first?
> 
> Yes, similar to existing attacks, attackers can only mount our attacks in practical settings once they have the ability to execute (unprivileged) code on the victim machine. We could convince ourselves this is still an obstacle, but we should first be prepared to disable JavaScript (and similar) in the browser, abandon cloud computing, etc.


There was a slew of new CPU based side channel attacks released, and after the mass hyping and running around with hair on fire of SPECTRE and MELTDOWN, I was pleased that these passed mostly uncommented on (although that might just be because of the news all week).

Many of these attacks are very theoretical, and hard to weaponise in changing target environments.  It's one thing to use these attacks to fetch information from a process that you know is running at the same time, fetching data you know the look of, it's entirely another thing to actually use that to compromise a target machine that is run arbitrary code and unknown data formats.

The ridiculousness of the quoted statement above about abandoning cloud computing I think really summarises my view on these attacks.  


## [Buckeye: Espionage Outfit Used Equation Group Tools Prior to Shadow Brokers Leak | Symantec Blogs](https://www.symantec.com/blogs/threat-intelligence/buckeye-windows-zero-day-exploit)

[https://www.symantec.com/blogs/threat-intelligence/buckeye-windows-zero-day-exploit](https://www.symantec.com/blogs/threat-intelligence/buckeye-windows-zero-day-exploit)

> The 2017 leak of Equation Group tools by a mysterious group calling itself the Shadow Brokers was one of the most significant cyber security stories in recent years. Equation is regarded as one of the most technically adept espionage groups and the release of a trove of its tools had a major impact, with many attackers rushing to deploy the malware and exploits disclosed. One of these tools, the EternalBlue exploit, was used to devastating effect in the May 2017 WannaCry ransomware outbreak.
> 
> However, Symantec has now found evidence that the Buckeye cyber espionage group (aka APT3, Gothic Panda) began using Equation Group tools in attacks at least a year prior to the Shadow Brokers leak.


One of the things to remember about the scary APT's and their actual behaviour in the real world is that if they are sitting on these piles of "zero day" attacks, they are going to be reluctant to use them.  Whenever you conduct a cyber attack, there is a high likelihood that the victim will eventually notice, and that they'll conduct forensics to work out how you got in and what you did.

The most advanced attackers, such as Equation Group, tend to clean up after themselves, leaving no trace of the tools, or as little as possible.  But if you attack a target that is under surveillance, then the opponent is quite likely to catch the exploit in action.

Inside advanced intelligence agencies, compartmentalisation ensures that often the attacks that they have available to them, they don't tell their own defending teams in unclassified environments about those vulnerabilities, because that would tip off that there are known issues (and often, there may be no good defence since they haven't told the supplier).  Therefore catching an attack in progress and understanding how it works and building your own tooling to exploit it is highly likely to work effectively.

This looks like a classic case of an enemy catching a vulnerability and promptly throwing it back.  Given that APT3, Buckeye, is the group named in the 2017 indictment of 3 chinese operatives working for a "purported internet security firm", this is a good view into the cut and thrust of international cyber espionage at work.


## [WhatsApp vulnerability exploited to infect phones with Israeli spyware | Ars Technica](https://arstechnica.com/information-technology/2019/05/whatsapp-vulnerability-exploited-to-infect-phones-with-israeli-spyware/)

[https://arstechnica.com/information-technology/2019/05/whatsapp-vulnerability-exploited-to-infect-phones-with-israeli-spyware/](https://arstechnica.com/information-technology/2019/05/whatsapp-vulnerability-exploited-to-infect-phones-with-israeli-spyware/)

> A representative of WhatsApp, which is used by 1.5 billion people, told Ars that company researchers discovered the vulnerability earlier this month while they were making security improvements. CVE-2019-3568, as the vulnerability has been indexed, is a buffer overflow vulnerability in the WhatsApp VOIP stack that allows remote code execution when specially crafted series of SRTCP packets are sent to a target phone number, according to this advisory.
> 
> According to the Financial Times, exploits worked by calling either a vulnerable iPhone or Android device using the WhatsApp calling function. Targets need not have answered a call, and the calls often disappeared from logs, the publication said. The WhatsApp representative said the vulnerability was fixed in updates released on Friday.


This WhatsApp vulnerability made the news in a big way, it was even featured on Radio4's Today program in the morning, meaning I woke up to people saying odd things about cybersecurity!  Not a great way to start the day.

The fact that NSO group continues to attempt to find highly targetable vulnerabilities is no real surprise.  Their commercial mechanism for profit is to find vulnerabilities, package them up and sell them to Governments and Law Enforcement for use.

The security community rounded on WhatsApp for their patch notes failing to mention the security update, but instead focusing on the ability to see stickers in full size.  However I think that users are far more likely to install the update if they are getting shiny stickers, and we've seen Apple doing the same thing, packaging new emoji's with security updates because they know it gets a higher and faster install rate for their users.

Finally, despite the reporting in the mainstream media (Radio 4 I'm looking at you), it's worth remembering that this was just a first stage exploit.  Whoever was using it is then able to execute code, as the WhatsApp process on your phone.  That might enable stealing your whatsapp history, but to establish a permanent compromise of the phone, and to access information in other applications, they would have to have a second stage that included a privilege escalation on the phone itself.  That's also hard and expensive, so this complete compromise was likely only going to be used by high end actors on the most promising of targets.


