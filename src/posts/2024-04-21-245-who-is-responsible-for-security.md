---
title: "245 - Who is responsible for security?"
date: 2024-04-21
description: "I have just come back from a half week at the excellent London QCon conference, one of my first big conferences in about 5 years for  a number of reasons."
permalink: /who-is-responsible-for-security/
---

I have just come back from a half week at the excellent London QCon conference, one of my first big conferences in about 5 years for  a number of reasons.

It was really nice to mix with people, hear talks on the advancing of the art of technology leadership, and hear the cry from security people about how much security is needed by them.

One of the things that came up in conversation with a number of people is a frustration within engineering leadership about who is actually responsible for security in products, in engineering and in operations.  There's a sense from a number of the people I spoke to that as engineering managers and lead developers, they desperately want someone from security to come and help them, but that most of their interactions with security end up frustrating them in a number of ways.

One of the reflections that I had on the back of these conversations is that a lot of people have an odd view of the responsibility of the CISO or security team in a lot of organisations.  As a general rule of thumb, most CISO's don't care whether the engineering team is secure in and of itself.  What they care about is being able to tell the board or COO that the organisation is meeting it's fiducary or regulatory requirements.  Some of those probably entail having a secure software development lifecycle, handling patches, and the sorts of things that engineers care about.  But it's important to realise that the aim here is not to be secure, but to be compliant.  

And if you are a major company, traded on a public stock exchange, or just returning value to your shareholders or owners (or the public in the case of Government), that stuff is really important.  It'll affect the share price far more than questions about whether you are using Python or Rust, or whether your docker images are scanned for vulenrabilities properly.  

Most regulation and compliance certificates require a minimum level of security, which is often a checkbox exercise that shows that you are doing the same low bar as everyone else in a similar industry.

So if we want to do security well, and we want to do it properly, should we be turning to the CISO to lead that effort?  I am increasingly of the view that you need engineering leadership to lead that charge rather than expecting security to do it for you.

Engineering leadership sits at the conflux of competing requirements already, it needs to champion resilience and reliability of the platform and product, as well as the speed to market of new product development, and balance that against the quality of the product to ensure that people don't abandon it and stop paying you.  Engineering leads needs to take on the mantle of security leader here as well, and start asking or demanding the sort of security features that make their products more secure.  That includes pricing in the cost of doing security well into product development roadmaps, into engineering platform requirements and roadmaps and into team and individual development plans.  

Because waiting for a CISO gandalf atop Shadowfax and the Rohirrim of security to come over the hill and save us at dawn is not a plan that's destined for success

## [Cybersecurity Isn't Special | Sensemaking by Shortridge ](https://kellyshortridge.com/blog/posts/cybersecurity-isnt-special/)

[https://kellyshortridge.com/blog/posts/cybersecurity-isnt-special/](https://kellyshortridge.com/blog/posts/cybersecurity-isnt-special/)

> In sum, cybersecurity really isn’t as esoteric and arcane a problem as we believe. Yet, I’m often met with disbelief by cyberppl that things are really that hard for their platform/infra/devops/SRE colleagues. Sometimes it feels like cybersecurity leaders and engineers think that all these teams were automagically bequeathed respect – autonomy, budget, authority – by the business.
> 
> And, in that vein, I’ve heard CISO described as “the hardest job in corporate America” and maybe it is if you’re scrambling to [cover up felonies](https://www.justice.gov/usao-ndca/pr/former-chief-security-officer-uber-sentenced-three-years-probation-covering-data) , but nearly every problem I hear security leaders complain about is mirrored on the infra and platform and SRE side of things [1](https://kellyshortridge.com/blog/posts/cybersecurity-isnt-special/#fn:1) .
> 
> This respect must be earned. These other teams earn it by solving reliability and developer productivity challenges in clever ways. _They_ do the hard work of thinky thinky and buildy buildy rather than foisting cumbersome policies and tools on software engineers in what I call the SSB model (for “sink or swim, bitch”) [2](https://kellyshortridge.com/blog/posts/cybersecurity-isnt-special/#fn:2) . They don’t carve 100 security commandments into Confluence; they build patterns, frameworks, and tooling that _encode_ the right requirements to make the better way the easier, faster way for software engineers.
> 
> If cybersecurity wants to earn similar respect, it can’t keep roadblocking and gatekeeping software. It can’t pretend like security failure is so distinct in importance and impact that it requires completely separate workflows, stacks, reviews, tooling, design, and basically everything else. Attackers accessing our systems without our consent is one type of failure, but not the only kind. Reliability failures are arguably both more frequent and more damaging when they occur; developer productivity failures can mean the difference between successful market differentiation and losing market share.
> 
> […]
> 
> We don’t have to feel so alone in the cybersecurity struggle. This approach gives us opportunities to learn from our platform engineering and SRE colleagues – to develop a collaborative vibe rather than a combative one. These teams want to help us solve security problems; they don’t want to create or implement roadblocks, but we shouldn’t either. We should want sustained resilience – because that means we can sustain our organization’s success.
> 
> tl;dr Paved roads, not roadblocks. 


I couldn’t agree more with this post by Kelly.  

One of the common misconceptions is that the CISO in most organisations is motivated by, or wants to improve security inside the organisation.  This focus on the security of the products is not what gets CISO’s bonuses, recognition or success.

Instead most executive boards want a CISO who can handle Governance, Risk and Compliance.  Can they show the investors that the data they hold on customers is held securely and appropriately managed?   That’s why they end up “foisting cumbersome policies” or “carving security commandsments into Confluence”.

I agree completely with Kelly in her description of the problem, but I’m not sure the solution is to make the CISO care more. 


## [How Boeing broke down: Inside the series of leadership failures that hobbled the airline giant ](https://fortune.com/2024/02/22/boeing-stock-crash-history-737-outlook/)

[https://fortune.com/2024/02/22/boeing-stock-crash-history-737-outlook/](https://fortune.com/2024/02/22/boeing-stock-crash-history-737-outlook/)

> The structural weaknesses in Boeing’s planemaking flow can actually be quite neatly traced to strategic missteps that took root over three decades ago. 
> 
> Surprisingly, the first big mistake occurred under CEO Phil Condit, an engineer steeped in the tradition of caution, safety, and excellence in design. In 2001, Condit persuaded the board to relocate Boeing’s headquarters to Chicago from Seattle, where the C-suites were a short drive to the giant plants in Renton and Everett that generated the lion’s share of revenue. The idea was to establish a “neutral” nerve center in easier traveling distance to Boeing’s other businesses, including its defense and space arm in Arlington, Va. Then in 2022, Boeing relocated again, this time to Arlington.
> 
> Shifting the top brass far from Boeing’s biggest business, and the one that’s suffered the severest problems, was a huge mistake in the opinion of several of Boeing suppliers and clients Fortune spoke to. Says a former top executive at a Boeing customer whom Fortune interviewed on background: “Why take one of the greatest manufacturing companies in the world and create a de-linkage between the leadership and the wrench-turners who make the company go?” this person asks. “That, coupled with all the outsourcing, created a kind of Frankenstein without enough command and control.”
> 
> And Boeing’s current top executives are now extremely dispersed. Though the commercial aircraft chiefs are based in Seattle, CFO Brian West and the treasurer work from suburban Connecticut, and the HR and PR heads from Orlando. It’s not clear how much time Calhoun, who served as chairman before being named CEO, spent in Renton or Everett, prior to the Portland disaster. He’s stated that Boeing’s headquarters “is wherever Brian and I happen to be.”


This was a really interesting read, and while I generally dislike articles that attempt to draw out a "root cause" for strategic missteps (because there's often lots of contributing factors), there is something incredibly powerful about where your leaders sit in regards to the work being done.  

One of the most common missteps that engineering leaders, CTO's and senior security leaders make is moving away from the "shop floor".  There's lots of reasons why your work might draw you away from the detail, and you don't want to be involved in teh day to day for fear of becoming a micromanager or blocker for work going on, but spend too long away from the people doing the job and you'll forgot what it's really like in the hurly burley of the day to day life.  There's no strategy team and report that replicate the feeling of walking the floor, looking at the work and hearing the frustration, celebration and coordination of the work you sponsor.  Having your finger on the pulse and therefore being able to determine which of those strategic choices is going to make a difference can completely change how you approach your executive decisions.

If you are in one of these roles, go and sit with your coworkers, not with special floor walks, but just sit in the vacinity and listen and watch the work they do.  It matters


## [Price of zero-day exploits rises as companies harden products against hackers | TechCrunch ](https://techcrunch.com/2024/04/06/price-of-zero-day-exploits-rises-as-companies-harden-products-against-hackers/)

[https://techcrunch.com/2024/04/06/price-of-zero-day-exploits-rises-as-companies-harden-products-against-hackers/](https://techcrunch.com/2024/04/06/price-of-zero-day-exploits-rises-as-companies-harden-products-against-hackers/)

> Crowdfense is now offering between $5 million and $7 million for zero-days to break into iPhones; up to $5 million for zero-days to break into Android phones; up to $3 million and $3.5 million for Chrome and Safari zero-days, respectively; and $3 million to $5 million for WhatsApp and iMessage zero-days. [In its previous price list](https://web.archive.org/web/20230607131756/https://www.crowdfense.com/bug-bounty-program.html) , published in 2019, the highest payouts that Crowdfense was offering were $3 million for Android and iOS zero-days.
> The increase in prices comes as companies like Apple, Google, and Microsoft are making it harder to hack their devices and apps, which means their users are better protected.
> 
> “It should be harder year over year to exploit whatever software we’re using, whatever devices we’re using,” said Dustin Childs, who is the head of threat awareness at Trend Micro ZDI. Unlike Crowdfense and Zerodium, ZDI pays researchers to acquire zero-days, then reports them to the companies affected with the goal of getting the vulnerabilities fixed.
> 
> “As more zero-day vulnerabilities are discovered by threat intelligence teams like Google’s, and platform protections continue to improve, the time and effort required from attackers increases, resulting in an increase in cost for their findings,” said Shane Huntley, the head of Google’s Threat Analysis Group, which tracks hackers and the use of zero-days. [In a report last month](https://blog.google/technology/safety-security/a-review-of-zero-day-in-the-wild-exploits-in-2023/) , Google said it saw hackers use 97 zero-day vulnerabilities in the wild in 2023. Spyware vendors, which often work with zero-day brokers, were responsible for 75% of zero-days targeting Google products and Android, according to the company. 


This is good news. It’s an indication that the ecosystems around our phones is getting far more secure.

There’s some occasional odd reporting around the price of iPhone and Android phones, with last year news that Android phones were more expensive.  Some digging seemed to indicate that actually a general Android Open Source Project zero-day that would work on any varient of android was incredibly expensive, but specific varients, such as Google’s Pixel version, Samsungs own android varient etc were far more in line with iPhone breaks.  It’s interesting to note that there’s more or less parity in the prices now, which indicates that most of the low hanging fruit has been picked up.

Of course, this only matters if you are running the latest version, so ensure your devices are patched, and that where possible your vendor is providing upstream patches as fast as possible if you are using an Android but not AOSP build 


## [Cyber security breaches survey 2024 - GOV.UK ](https://www.gov.uk/government/statistics/cyber-security-breaches-survey-2024/cyber-security-breaches-survey-2024#chapter-4-prevalence-and-impact-of-breaches-or-attacks)

[https://www.gov.uk/government/statistics/cyber-security-breaches-survey-2024/cyber-security-breaches-survey-2024#chapter-4-prevalence-and-impact-of-breaches-or-attacks](https://www.gov.uk/government/statistics/cyber-security-breaches-survey-2024/cyber-security-breaches-survey-2024#chapter-4-prevalence-and-impact-of-breaches-or-attacks)

> Half of businesses (50%) and around a third of charities (32%) report having experienced any kind of cyber security breach or attack in the last 12 months (Figure 4.1). This accounts for approximately 718,000 businesses and 65,000 registered charities - although these estimates, like all survey results, will be subject to a margin of error (see Appendix A). [[footnote 8]](https://www.gov.uk/government/statistics/cyber-security-breaches-survey-2024/cyber-security-breaches-survey-2024#fn:8) The survey does not have a separate question to ask whether organisations have experienced any type of breach or attack, as this approach would be subject to considerable recall errors. Instead, the above percentages are based on calculating the proportions of businesses and charities that identified one or more of 11 specific types of breaches or attacks (listed in Figure 4.2), as well as an option allowing organisations to state any other type of breach or attack.
> 
> Larger businesses are more likely to identify breaches or attacks than smaller ones. High-income charities (66% of those with incomes of £500,000 or more) are significantly more likely to record any breaches or attacks than the average for all charities.
> 
> [..]
> 
> When considering their most disruptive breach or attack, the vast majority of businesses (92%) and charities (91%) report being able to restore their operations within 24 hours.
> 
> Furthermore, almost eight in ten businesses (79%) and charities (77%) say it took ‘no time at all’ to recover
> 
> […]
> 
> Among the 50% of businesses that identify breaches or attacks, just over one in ten (13%) experienced at least one of the negative outcomes listed in Figure 4.6, such as a loss of money or data. The low proportion stating a negative outcome indicates that a large proportion of attacks are unsuccessful. Similarly, among the 32% of charities identifying breaches or attacks, around one in ten (12%) have negative outcomes. Disruption to websites, and the temporary loss of access to files or networks are the most commonly reported outcomes (4% for both). 


Comparing and contrasting the likelihood of a breach (approximately 50% or once every two years) with the impact is important.  If you can say that you think there is the likelihood of a breach every two years, but that only 1 in 10 breaches are massively damaging, you are saying that the overall risk of an impactful breach is only 1 in every 20 years for most companies.

Fascinating stats for a risk based nerd like me 


## [Verified curl | daniel.haxx.se ](https://daniel.haxx.se/blog/2024/04/10/verified-curl/)

[https://daniel.haxx.se/blog/2024/04/10/verified-curl/](https://daniel.haxx.se/blog/2024/04/10/verified-curl/)

> xz (and its library liblzma) was presumably selected as a target because it is an often used component and by extension via systemd it often used by openssh in several Linux distros. libcurl is probably an even more widely used software component and if infected, could potentially serve as an effective vessel to distribute evil into the world.
> 
> [...]
> *Is the content in git benign?*
> 
> The process above only verifies that tarballs are indeed generated (only) from contents present in git and that they are unaltered from the moment I made them.
> 
> How do you know that the contents in git does not contain any backdoors or other vulnerabilities?
> 
> Without trusting anyone else’s opinions and without just relying on the fact that you can run the test suite, fuzzers and static code analyzers without finding anything, you can review it. Or pay someone else to review it.
> 
> We have had curl audited several times by external organizations, but can you trust claimed random audits?
> 
> *Anonymous contributors*
> 
> We regularly accept contributions from anonymous and pseudonymous contributors in curl – and we always have. Our policy says that if a contribution is good: if it passes review and all tests run green, we have no reason to deny it – in the name of progress and improvement. That is also why we accept even single-letter typo fixes: even a very small fix is a step in the right direction.
> 
> A (to me) surprisingly large amount of contributions are done by people who do not state a full real name. They may chose to be anonymous for various reasons – we do not ask. Maybe they fear retaliation if they would propose something that ends up buggy? Sometimes people want to hide their affiliation/origin so that their contribution is not associated with the organization they work at. Another reason sometimes mentioned is that women do it to avoid revealing themselves as female. etc. As I said: we do not ask so I cannot tell for sure.


This is a nice writeup from Daniel Stenberg who is the core maintainer of libcurl, which as he points out, would be a great potential target for a libxz style attack.

One of the things we have to remember is that open source software is a sociotechnical system.  We cannot put trust into the system using just technical tools, but we need to considere the social aspects and implications as well.  This point in here that some people want to contribute code back, but may not be able to in their own name because of social issues is a good reminder that the social culture on which our software is built ingrains all of the software that we build.


## [GitHub - amlweems/xzbot: notes, honeypot, and exploit demo for the xz backdoor (CVE-2024-3094) ](https://github.com/amlweems/xzbot)

[https://github.com/amlweems/xzbot](https://github.com/amlweems/xzbot)

> The backdoor uses a hardcoded ED448 public key for signature validation and decrypting the payload. If we replace this key with our own, we can trigger the backdoor.
> 
> The attacker's ED448 key is:
> 
> ```
> 0a 31 fd 3b 2f 1f c6 92 92 68 32 52 c8 c1 ac 28
> 34 d1 f2 c9 75 c4 76 5e b1 f6 88 58 88 93 3e 48
> 10 0c b0 6c 3a be 14 ee 89 55 d2 45 00 c7 7f 6e
> 20 d3 2c 60 2b 2c 6d 31 00```
> 
> We will replace this key with our own (generated with seed=0):
> 
> ```
> 5b 3a fe 03 87 8a 49 b2 82 32 d4 f1 a4 42 ae bd
> e1 09 f8 07 ac ef 7d fd 9a 7f 65 b9 62 fe 52 d6
> 54 73 12 ca ce cf f0 43 37 50 8f 9d 25 29 a8 f1
> 66 91 69 b2 1c 32 c4 80 00
> ```


Work on decompiling and understanding the libXZ backdoor attempt continues, and this is a nice honeypot and some notes on the capabilities of the backdoor.  It's interesting, but not surprising that the attackers needed control of a private key to authenticate to the server, becuase it's already in the middle of the openssh server, so that gives security, privacy and doesn't look suspicious to packet monitoring around it.


## [Security advisory for the standard library (CVE-2024-24576) | Rust Blog ](https://blog.rust-lang.org/2024/04/09/cve-2024-24576.html)

[https://blog.rust-lang.org/2024/04/09/cve-2024-24576.html](https://blog.rust-lang.org/2024/04/09/cve-2024-24576.html)

> The Command::arg and Command::args APIs state in their documentation that the arguments will be passed to the spawned process as-is, regardless of the content of the arguments, and will not be evaluated by a shell. This means it should be safe to pass untrusted input as an argument.
> 
> On Windows, the implementation of this is more complex than other platforms, because the Windows API only provides a single string containing all the arguments to the spawned process, and it's up to the spawned process to split them. Most programs use the standard C run-time argv, which in practice results in a mostly consistent way arguments are splitted.
> 
> One exception though is cmd.exe (used among other things to execute batch files), which has its own argument splitting logic. That forces the standard library to implement custom escaping for arguments passed to batch files. Unfortunately it was reported that our escaping logic was not thorough enough, and it was possible to pass malicious arguments that would result in arbitrary shell execution.


This is one hell of a vulnerability to spot, and a bit of a peculiar one.  It's quite possible and even likely that other systems that attempt to make safe arguments passed out to the command line also fail in some of these situations.

Of course, the rust community is significantly concerned with security and correctness, so it's not a surprise that they've found this


## [ED 24-02: Mitigating the Significant Risk from Nation-State Compromise of Microsoft Corporate Email System | CISA ](https://www.cisa.gov/news-events/directives/ed-24-02-mitigating-significant-risk-nation-state-compromise-microsoft-corporate-email-system)

[https://www.cisa.gov/news-events/directives/ed-24-02-mitigating-significant-risk-nation-state-compromise-microsoft-corporate-email-system](https://www.cisa.gov/news-events/directives/ed-24-02-mitigating-significant-risk-nation-state-compromise-microsoft-corporate-email-system)

> Midnight Blizzard’s successful compromise of Microsoft corporate email accounts and the exfiltration of correspondence between agencies and Microsoft presents a grave and unacceptable risk to agencies. This Emergency Directive requires agencies to analyze the content of exfiltrated emails, reset compromised credentials, and take additional steps to ensure authentication tools for privileged Microsoft Azure accounts are secure. CISA has assessed that the below required actions are most appropriate to understand and mitigate the risk posed by Midnight Blizzard’s possession of the exfiltrated correspondence between FCEB agencies and Microsoft.
> 
> Microsoft and CISA have notified all federal agencies whose email correspondence with Microsoft was identified as exfiltrated by Midnight Blizzard. This Directive will refer to that group of agencies as “affected agencies.” 


One of those slightly odd directives from CISA.  If you were affected, you should already know.  It’s existence implies that either some agencies didn’t want to, or couldn’t convince their suppliers to take this breach seriously, and needed a formal directive.

Given that some government suppliers have taken to putting clauses in contracts that requires patching or mitigating action to be prioritised when there’s an emergency directive, this might be the tail wagging the dog, that the directive is only needed to allow everyone to act the way that they should.

Needless to say, what we can learn from this is:
1. If one of your suppliers gets compromised, there’s an interesting amount of data sat in corporate email systems, likely including passwords, credetnials in attachments and system diagrams
2. Stop writting passwords down in email and use a password manager or enterprise authentication management system of some form 


## [Cyberespionage Group Earth Hundun's Continuous Refinement of Waterbear and Deuterbear | Trend Micro (US) ](https://www.trendmicro.com/en_us/research/24/d/earth-hundun-waterbear-deuterbear.html)

[https://www.trendmicro.com/en_us/research/24/d/earth-hundun-waterbear-deuterbear.html](https://www.trendmicro.com/en_us/research/24/d/earth-hundun-waterbear-deuterbear.html)

> We recently observed a surge in cyberattacks targeting a number of organizations in various sectors such as technology, research, and government.  These attacks involve a malware family known as  Waterbear that is linked to the cyberespionage group Earth Hundun (also known as [BlackTech](https://www.trendmicro.com/en_us/research/17/f/following-trail-blacktech-cyber-espionage-campaigns.html) ), a threat actor that focuses on gathering intelligence from technology and government organizations, particularly in the Asia-Pacific region.
> 
> Among the group’s arsenal of weapons, the Waterbear backdoor is one of the most complex, with a wide array of anti-debug, anti-sandbox, and general antivirus-hindering techniques. Moreover, the frequent updates from its developers have led to even more evasion tactics, including enhancements of its loader, downloader, and communication protocol. This report will delve into the latest techniques Earth Hundun has implemented with Waterbear and provide an analysis of its latest iteration, Deuterbear. **[…]** Interestingly, some Waterbear downloaders have been seen using command-and-control (C&C) servers with internal IP addresses (for instance, the downloader with hash _6b9a14d4d9230e038ffd9e1f5fd0d3065ff0a78b52ab338644462864740c2241_ uses the internal IP 192.168.11[.]2 as its C&C server).
> 
> This suggests that the attackers might have in-depth knowledge of their victims’ networks, employing multilayered jump servers to evade detection. Such tactics underscore the sophisticated nature of these attacks, which are designed to stealthily maintain presence and control within compromised environments. 


This was an interesting report if only for this little gem of opsec knowledge.  In some cases, the version of the malware deployed onto your network has been specifically customised for you, including the use of an internal C&C server.  In more secure environment such as in tech or government, the adversary may want to move their malware and remote access tools around an environment that doesn’t have easy internet connectivity.  One way to acheive that is to compromise something in the environment that does have internet connectivity and then make it act as a proxy.  This might be a VPN concentrator, it might be an internal service that has to access the internet.  The key thing is that anything plugged into both networks, if it can be compromised can act as a proxy for command and control mechanisms and should be monitored accordingly 


## [Muddled Libra’s Evolution to the Cloud ](https://unit42.paloaltonetworks.com/muddled-libra-evolution-to-cloud/)

[https://unit42.paloaltonetworks.com/muddled-libra-evolution-to-cloud/](https://unit42.paloaltonetworks.com/muddled-libra-evolution-to-cloud/)

> The [Okta cross-tenant impersonation attacks](https://sec.okta.com/articles/2023/08/cross-tenant-impersonation-prevention-and-detection) that occurred from late July to early August 2023, where Muddled Libra bypassed IAM restrictions, display how the group exploits Okta to access SaaS applications and an organization's various CSP environments. They accessed an organization’s Okta Identity Portal through technology administrator accounts that the group compromised as part of their new tactic of help desk social engineering. Then they modified permissions to increase their scope of access. By modifying permission sets of compromised users, this escalated their privileges to gain further access to SaaS applications and organization's CSP environments.
> 
> […]
> 
> Depending on the type of SaaS application, the data within the application might be more beneficial for use by threat actors in traditional data exfiltration or for learning about a target’s environment configuration. Historically, Muddled Libra looks for data that falls under either of these classifications within any SaaS application they compromise. They also make a large effort to search for other credentials within a SaaS application.
> 
> Sensitive credentials can be exposed in logs, as well as within PMS applications and SaaS applications that scan for sensitive information. Muddled Libra methodically searches for applications that might store this type of valuable information to then use later on in their attacks for privilege escalation and lateral movement.
> 
> Microsoft provides a wide range of services and tools that become key targets during an attack due to their high value to both organizations and threat actors. An example of how Muddled Libra takes advantage of a SaaS application is how the group exploits [Microsoft SharePoint](https://www.microsoft.com/en-us/microsoft-365/sharepoint/collaboration) .
> 
> The SharePoint platform is used by organizations to store files that document network topology, as well as what tools an organization uses and other general information. Muddled Libra targets this platform to gain a better understanding of the network configuration within a company and which tools they can exploit, such as remote access tools.
> 
> As with any file storage tool, other sensitive information (such as passwords) can also get leaked from these documents. Also, within the Microsoft 365 (M365) suite, the group targets email boxes and other email functionality to gain access to sensitive data. 


SaaS tools are great, but they are also increasing targets of these sorts of attackers.  One of the downsides of SaaS tools is that many lack the level of enterprise logging that make it easy to identify who logged in where, what pages or data they looked at, and anything they did with it.

This is an area that is worth using redteam resources on.  Given access to a corporate device and account, what can they find in your SaaS resources that can help act as a second stage of an attack, especially credentials, overly open file shares and org charts and network diagrams.

That’s not to say that you should hide those in secrecy, but that you should be aware of the data in them, and make sure that you understand what sharing means and how to monitor for inappropriate use 


