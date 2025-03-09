---
title: "174 - One Team, Two Team; Blue Team, Green Team"
date: 2021-11-07
description: "Within security we often think a lot about the bad guys, the red team, and how they work, how they can compromise our systems."
permalink: /one-team-two-team-blue-team-green-team/
---

Within security we often think a lot about the bad guys, the red team, and how they work, how they can compromise our systems.
We also pay a lot of attention to the blue team, the team of defenders watching the screens, analysing the systems and trying to defend against the red team.

But what we rarely spend enough time thinking about is the green team, the team who actually builds the system that we need to defend.  The growing focus on supply chain means that we're starting to think about some of it more, but to many people, the supply chain can mean focusing on the third party tools that we buy, the platforms that we use and even sometimes the hardware we buy and companies we buy it from.

But someone, somewhere, is writing code that makes our systems work.  These teams are made up of people who want to build systems and solve user needs in some form.  Those teams need IT systems of their own, they do email, they write documents and they can be phished just like every other member of the company.  But they're also far more likely to have privileged access to the system, whether it be API keys that enables ownership of tens of millions of dollars, or access keys to the servers that control your company.

Protecting developers and ensuring that they can build systems effectively is still something that isn't as well understood as other security processes.  Done well, a green team who builds the thing, can be a huge security advantage.  Having the skills in house to build and customise your own systems means that you can log the things you need to log, and you can fix bugs or issues easily. 

But you also need those teams to have the skills and capabilities to protect themselves.  The tools that we use, from package managers like npm, source code review tools like github or gitlab or even the languages that we use can drive a thought process around security that helps or hinders people from doing their job well.

At the end of the day, the red team has one goal in mind, to trick the system into doing the wrong thing.  Once we get our systems to a certain level of maturity, it's far easier to trick the human behind the system than it is to trick the system.  That means we need to invest in those humans, making their jobs easy, and ensuring that they have the data and protections to do their job securely and effectively.

## [Trojan Source: Invisible Vulnerabilities [pdf]](https://www.trojansource.codes/trojan-source.pdf)

[https://www.trojansource.codes/trojan-source.pdf](https://www.trojansource.codes/trojan-source.pdf)

> We present a new type of attack in which source
> code is maliciously encoded so that it appears different to a
> compiler and to the human eye. This attack exploits subtleties in
> text-encoding standards such as Unicode to produce source code
> whose tokens are logically encoded in a different order from the
> one in which they are displayed, leading to vulnerabilities that
> cannot be perceived directly by human code reviewers. ‘Trojan
> Source’ attacks, as we call them, pose an immediate threat both
> to first-party software and of supply-chain compromise across
> the industry. We present working examples of Trojan-Source
> attacks in C, C++, C#, JavaScript, Java, Rust, Go, and Python.
> We propose definitive compiler-level defenses, and describe other
> mitigating controls that can be deployed in editors, repositories,
> and build pipelines while compilers are upgraded to block this
> attack.


This is an interesting attack that isn't clear that it's actually a CVE.  It's been numbered [CVE-2021-42574](https://nvd.nist.gov/vuln/detail/CVE-2021-42574) but it's far more like a class of attacks like buffer overflow or double free.

The attack in essence uses the fact that many text editors and code review systems (such as Github's pull requests) renders the code as text.  That means that unicode characters that are invisible, unrendered or otherwise change the meaning of the text won't be rendered to the humans reviewing the source code, but will be seen by the compiler.  

Similar homoglyph attacks have been possible for some time, for example, the function `LOGIN` and the function `LOGlN` both look the same in certain fonts despite one using an uppercase i, and the other using a lowercase l.  

There's no clear way to solve this kind of vulnerability.  The best way to solve this is for [review systems like Github's pull request system, to flag unusual characters in the code](https://github.blog/changelog/2021-10-31-warning-about-bidirectional-unicode-text/) so that users are aware that the merge request contains something suspicious.  You can see an example of this in the [researchers github repository, in your favourite language of course](https://github.com/nickboucher/trojan-source/blob/main/Python/commenting-out.py)


## [Popular 'coa' NPM library hijacked to steal user passwords](https://www.bleepingcomputer.com/news/security/popular-coa-npm-library-hijacked-to-steal-user-passwords/)

[https://www.bleepingcomputer.com/news/security/popular-coa-npm-library-hijacked-to-steal-user-passwords/](https://www.bleepingcomputer.com/news/security/popular-coa-npm-library-hijacked-to-steal-user-passwords/)

> This incident follows last month's hack of another popular npm library "ua-parser-js" that is used by Facebook, Microsoft, Amazon, Reddit, and other big tech firms.
> 
> The malware contained in hacked 'coa' versions, as analyzed by BleepingComputer, is virtually identical to the code found in the hijacked ua-parser-js versions, potentially establishing a link between the threat actors behind both incidents.
> 
> Although the malicious 'coa' versions have been taken down on npm, as a Sonatype security researcher I was able to retrieve archived copies from Sonatype's automated malware detection system.
> 
> [...]
> 
> When loaded, Danabot will perform the various malicious activity, including:
> 
> * Steal passwords from a variety of web browsers, including Chrome, Firefox, Opera, Internet Explorer, and Safari.
> * Steal passwords from various applications, including VNC, online casino applications, FTP clients, and mail accounts.
> * Steal stored credit cards.
> * Take screenshots of the active screens.
> * Log keystrokes.
> 
> All of this stolen data is then sent back to the threat actors to allow them to breach victims' other accounts.


That's 3 packages in the last month within npmjs that have had code added to them.  The start of this article states "developers around the world were left surprised to notice new releases for npm library 'coa'—a project that hasn't been touched for years, unexpectedly appear on npm." but in reality developers likely won't notice this.  

Node dependencies are often not locked, and in fact there's a security tradeoff each way for dependencies, where you want to get updated dependencies with as little effort as possible in order to get security updates.  

Secondly, don't forget that npm supports transitive dependencies, so your system might not rely on coa, rc or ua-parser-js, but there's a good possibility that you use a library that uses it, and that might introduce the vulnerable version into your build.

npm has a `--ignore-scripts` option, which disables the preinstall and postinstall scripts.  For library dependencies, this is almost always fine, it's only for people installing binaries to their local system who likely need those scripts.  The fact that npm supports and does both is a clear weakness in its security model and makes it almost impossible to properly secure the operation.  Separating concerns into different tools, using the unix philosophy, means that we can separate security concerns as well, and that makes us all safer.


## [Hacker steals $55 million from bZx DeFi platform - The Record by Recorded Future](https://therecord.media/hacker-steals-55-million-from-bzx-defi-platform/)

[https://therecord.media/hacker-steals-55-million-from-bzx-defi-platform/](https://therecord.media/hacker-steals-55-million-from-bzx-defi-platform/)

> “A bZx developer was sent a phishing email to his personal computer with a malicious macro in a Word document that was disguised as a legitimate email attachment,” the company said in a preliminary post mortem of the attack published on Friday night, hours after the hack.
> 
> bZx said the email attachment ran a script on the developer’s computer that compromised the employee’s mnemonic wallet phrase.
> 
> The attacker then proceeded to empty the developer’s personal wallet and then stole two private keys from the employee’s computer that were being used by the bZx platform for its integration with the Polygon and Binance Smart Chain (BSC) blockchains.
> 
> The hacker then used these keys to steal the platform’s Polygon and BSC funds, along with the same funds from a small number of users who approved unlimited spend operations for the two tokens in their accounts.
> 
> While bZx said it’s still investigating the exact amount of stolen funds, blockchain security firm SlowMist put the sum at more than $55 million, based on the malicious transactions it detected.


"Developer laptops don't need to be secure" said almost every developer everywhere.

Quite how the developer can have access to private keys that control some $55m without any second party controls is yet another warning sign around the state of cryptocurrencies.


## [Organising for Digital Delivery | GOV.UK](https://www.gov.uk/government/publications/organising-for-digital-delivery/organising-for-digital-delivery)

[https://www.gov.uk/government/publications/organising-for-digital-delivery/organising-for-digital-delivery](https://www.gov.uk/government/publications/organising-for-digital-delivery/organising-for-digital-delivery)

> A recent analysis by Government Security indicates that almost 50% of current Government IT spend (£2.3BN out of a total central Government spend of £4.7BN in 2019) is dedicated to “keeping the lights on” activity on outdated legacy systems, with an estimated £13-22BN risk over the coming five years
> 
> * Challenge 1: Uncertain quality of technical product delivery.
> * Challenge 2: Unaddressed legacy systems and technical debt.
> * Challenge 3: Relatively weak operational performance monitoring.
> * Challenge 4: Failure to leverage scale.
> * Challenge 5: Missed opportunities in leveraging Government held data sets.
> * Challenge 6: Low technical fluency across senior Civil Service leadership.
> * Challenge 7: Confusion over the role of the central functions.
> 
> *The way forward*
> 
> 1. Build mechanisms to put the citizen at the heart of all design decisions
> 2. Strengthen the accountability of Departments and their Permanent Secretaries
> 3. Hire a Permanent Secretary level head of function
> 4. Re-focus and add teeth to the centre
> 5. Create clear investment swim lanes to address the legacy debt
> 6. Set up a quarterly business review process
> 7. Invest in developing the technical fluency of senior civil service leadership
> 8. Create a Government data application centre of excellence


([Joel](https://twitter.com/joelgsamuel)) Doing nothing costs something when it comes to at least technology. Something gets worse, is hard to maintain, expensive to change or even just missing new features you would want but can't have. You also still have to keep that thing ticking, and those extended extended support contracts with vendors end up being the only choice (just burning the money would have the same outcome).

The UK Government is winding up for a 3-year financial settlement. It will be interesting to see how much of this is taken to heart, not just in nodding and lip service but the delivery of cash in real terms in the right way. Its early in the process, but these investment swim lanes to address legacy debt have yet to become clear.


## [cyber.dhs.gov - Binding Operational Directive 22-01](https://cyber.dhs.gov/bod/22-01/)

[https://cyber.dhs.gov/bod/22-01/](https://cyber.dhs.gov/bod/22-01/)

> This directive establishes a CISA-managed catalog of known exploited vulnerabilities that carry significant risk to the federal enterprise https://cisa.gov/known-exploited-vulnerabilities and establishes requirements for agencies to remediate any such vulnerabilities included in the catalog. CISA will determine vulnerabilities warranting inclusion in the catalog based on reliable evidence that the exploit is being actively used to exploit public or private organizations by a threat actor. This directive enhances but does not replace BOD 19-02, which addresses remediation requirements for critical and high vulnerabilities on internet-facing federal information systems identified through CISA’s vulnerability scanning service.
> 
> Scope
> 
> This directive applies to all software and hardware found on federal information systems managed on agency premises or hosted by third parties on an agency’s behalf. These required actions apply to any federal information system, including an information system used or operated by another entity on behalf of an agency, that collects, processes, stores, transmits, disseminates, or otherwise maintains agency information.


This is a really powerful and useful directive.  In essence, CISA will maintain a list of known exploited vulnerabilities, the ones that they've been warning about for months.

Not only will agencies be required to patch them, but all third parties hosting data or systems on the agencies behalf will be required to put in place vulnerability management practices that will ensure that they can patch vulnerabilities listed here within 2 weeks.

The knock on effect of this is that suppliers to government are going to need to ensure that they have a vulnerability management system that can meet this pace.


## [Commerce Adds NSO Group and Other Foreign Companies to Entity List for Malicious Cyber Activities | U.S. Department of Commerce](https://www.commerce.gov/news/press-releases/2021/11/commerce-adds-nso-group-and-other-foreign-companies-entity-list)

[https://www.commerce.gov/news/press-releases/2021/11/commerce-adds-nso-group-and-other-foreign-companies-entity-list](https://www.commerce.gov/news/press-releases/2021/11/commerce-adds-nso-group-and-other-foreign-companies-entity-list)

> NSO Group and Candiru (Israel) were added to the Entity List based on evidence that these entities developed and supplied spyware to foreign governments that used these tools to maliciously target government officials, journalists, businesspeople, activists, academics, and embassy workers.  These tools have also enabled foreign governments to conduct transnational repression, which is the practice of authoritarian governments targeting dissidents, journalists and activists outside of their sovereign borders to silence dissent.  Such practices threaten the rules-based international order.  
> 
> Positive Technologies (Russia), and Computer Security Initiative Consultancy PTE. LTD. (Singapore) were added to the Entity List based on a determination that they traffic in cyber tools used to gain unauthorized access to information systems, threatening the privacy and security of individuals and organizations worldwide. 


Adding NSO group to this list is going to have some interesting ramifications.  It's not just about whether US companies can buy access to NSO group tools (and I'm sure there are law enforcement orgs who would like to), but it means that third parties are not able to trade with NSO group, which means that US based security firms cannot sell security research to them.

Interestingly, it may also have an impact on whether or not companies like Apple and Google can pay for info on vulnerabilities that NSO have as well.  It'll be interesting to see how this turns out.  Of course, NSO Group is simply the tip of the iceberg within the commercial spyware market, and this means that people will start looking at the next tier of suppliers


## [Gamaredon/Armageddon Group [pdf]](https://ssu.gov.ua/uploads/files/DKIB/Technical%20report%20Armagedon.pdf)

[https://ssu.gov.ua/uploads/files/DKIB/Technical%20report%20Armagedon.pdf](https://ssu.gov.ua/uploads/files/DKIB/Technical%20report%20Armagedon.pdf)

> The Security Service of Ukraine believes that Armageddon
> was formed and has been operating since 2014 (some sources
> on the Internet indicate June 2013). The main purpose of its
> activity is to conduct targeted cyberintelligence operations
> against state bodies of Ukraine, primarily security, defense and
> law enforcement agencies, in order to obtain intelligence
> information.
> The activity and development of the hacker group
> "Armageddon" during 2014-2021 has led to the existence of a
> new real cyber threat. In the period 2017-2021 this group
> implemented the most numerous cyberintelligence actions on
> various vectors of public administration.
> Armageddon does not use complex and sophisticated
> techniques, tactics and procedures, does not try to make an effort
> to stay secret for a long time. Staying off the radar is not a group
> priority.
> However, the group's activities are characterized by
> intrusiveness and audacity.


The Ukraine Security Services (The SSU) claiming that the FSB operate a fairly intrusive APT cyber gang here.  Naturally the targets are all Ukrainian government workers, so low risk for most people, but what I thought was interesting here was the use of phishing emails marked important, and a microsoft office vulnerability from 2017 for initial access.

We cower in terror from "Advanced Persistant Threats", but we're talking here about (alledgedly) one of the most powerful spy agencies in the world using 5 year old vulnerabilities and very basic attacks that even a basic pen testing firm should be able to replicate.

Even the second stage infections, the software that is dropped onto the computer after the initial access has marked similarity to software floating around the cybercrime forums from 2016.

The remediation is to turn on attack surface reduction within the [Microsoft Defender ATP](https://docs.microsoft.com/en-au/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction) which mostly reduce threat without impacting users


## [The ‘Groove’ Ransomware Gang Was a Hoax – Krebs on Security](https://krebsonsecurity.com/2021/11/the-groove-ransomware-gang-was-a-hoax/)

[https://krebsonsecurity.com/2021/11/the-groove-ransomware-gang-was-a-hoax/](https://krebsonsecurity.com/2021/11/the-groove-ransomware-gang-was-a-hoax/)

> In the first week of September, Groove posted on its darknet blog nearly 500,000 login credentials for customers of Fortinet VPN products, usernames and passwords that could be used to remotely connect to vulnerable systems. Fortinet said the credentials were collected from systems that hadn’t yet implemented a patch issued in May 2019.
> 
> Some security experts said the post of the Fortinet VPN usernames and passwords was aimed at drawing new affiliates to Groove. But it seems more likely the credentials were posted to garner the attention of security researchers and journalists.
> 
> Sometime in the last week, Groove’s darknet blog disappeared. In a post on the Russian cybercrime forum XSS, an established cybercrook using the handle “Boriselcin” explained that Groove was little more than a pet project to screw with the media and security industry.
> 
> “For those who don’t understand what’s going on: I set up a fake Groove Gang and named myself a gang,” Boriselcin wrote. 


This kind of thing is one of the reasons that I don't cover as much in the ransomware sector as you might think.  A lot of the reports are more or less breathless exhortations that there are scary advanced actors doing all this "cyber" stuff, and don't add a lot for us as defenders and security leaders.


## [Army Enlistment Waivers in the Age of Legal Marijuana | RAND](https://www.rand.org/blog/rand-review/2021/10/army-enlistment-waivers-in-the-age-of-legal-marijuana.html)

[https://www.rand.org/blog/rand-review/2021/10/army-enlistment-waivers-in-the-age-of-legal-marijuana.html](https://www.rand.org/blog/rand-review/2021/10/army-enlistment-waivers-in-the-age-of-legal-marijuana.html)

> Recruits who make it into the U.S. Army despite low-level histories of marijuana use perform no worse, overall, than other soldiers. That should be welcome news in recruiting offices nationwide. More than half of all new recruits come from states where marijuana is now legal, at least for medicinal use.
> 
> The Army's rules have not changed. Marijuana use is still a disqualifying offense for anyone hoping to join up. But those who have left it in the past can ask for a waiver, just like recruits who have diabetes, chronic insomnia, or bunions on their feet. Researchers at RAND wanted to know, How do those waivered recruits actually perform once they get into uniform?
> 
> They looked at thousands of soldiers who enlisted despite past marijuana use and other disqualifying marks on their records, such as depression or anxiety disorders. They found no evidence that those recruits were riskier across the board than any others. The Army could tighten up its policy on waivers, they concluded—but, for the most part, it works.


This is both interesting research and an interesting finding.  I've been wondering for a while, with increasing decriminilisation of marijuana use, what the impact was on vetting for security clearances for example.  If you want a TS/SCI clearance in the US, then you need to pass drug tests and show now history of drug use (more or less).  But as generations change, so does attitudes around some of these things.

If we can't determine, in a data driven and testable way, whether or not a given action has a negative impact, we can't really understand whether to make rules for it.  This research shows that the waiver system works, and moreso, that there is no appreciable difference in quality of candidates, which might suggest that instead of a waiver to the rules, maybe this needs to simply be "the rules"


## [Reward Offers for Information to Bring DarkSide Ransomware Variant Co-Conspirators to Justice - United States Department of State](https://www.state.gov/reward-offers-for-information-to-bring-darkside-ransomware-variant-co-conspirators-to-justice/)

[https://www.state.gov/reward-offers-for-information-to-bring-darkside-ransomware-variant-co-conspirators-to-justice/](https://www.state.gov/reward-offers-for-information-to-bring-darkside-ransomware-variant-co-conspirators-to-justice/)

> The U.S. Department of State announces a reward offer of up to $10,000,000 for information leading to the identification or location of any individual(s) who hold(s) a key leadership position in the DarkSide ransomware variant transnational organized crime group. In addition, the Department is also offering a reward offer of up to $5,000,000 for information leading to the arrest and/or conviction in any country of any individual conspiring to participate in or attempting to participate in a DarkSide variant ransomware incident.
> 
> The DarkSide ransomware group was responsible for the Colonial Pipeline Company ransomware incident in May 2021, which led to the company’s decision to proactively and temporarily shut down the 5,500-mile pipeline that carries 45 percent of the fuel used on the East Coast of the United States. In offering this reward, the United States demonstrates its commitment to protecting ransomware victims around the world from exploitation by cyber criminals. The United States looks to nations who harbor ransomware criminals that are willing to bring justice for those victim businesses and organizations affected by ransomware.


This is a new approach by the US Department of State.  

There's a question in my mind about whether this bounty is actually about finding out who these people are, because even if they find out, they wont actually be extradited and tried surely?  Maybe its more about making those people feel like targets, making them start to worry about their friends and coworkers, and driving a wedge of suspicion around them.

I suspect it will also put pressure on any local authority that is enabling or actively ignoring the operation of ransomware groups, because even if there's some corruption that enables the continued operation of those groups, the corrupt officials now have even higher financial motives to sell out their existing partners.


## [How to get useful answers to your questions](https://jvns.ca/blog/2021/10/21/how-to-get-useful-answers-to-your-questions/)

[https://jvns.ca/blog/2021/10/21/how-to-get-useful-answers-to-your-questions/](https://jvns.ca/blog/2021/10/21/how-to-get-useful-answers-to-your-questions/)

> My second favourite tactic is to state my understanding of how the system works.
> 
> Here’s an example from the “asking good questions” post of a “state your understanding” email I sent to the rkt-dev mailing list:
> 
> [...]
> 
> This:
> 
> * states my goal (understand rkt’s design choices)
> * states my understanding of how rkt and docker work
> * makes some guesses at the goal so that people can confirm/deny
> 
> This question got a great reply, which among other things pointed out something that I’d totally missed – that the ACI format is a DAG instead of a linked list, which I think means that you could install Debian packages in any order and not have to rebuild everything if you remove an apt-get install in the middle of your Dockerfile.


This is a really good tool to use when you are trying to understand something complex, especially when communicating by email.

We don't take enough time in the modern office to actually compose and structure emails properly.  Most are a couple of lines and dashed off in a hurry.   This is a technique that I'll be trying to adopt more in future.


## [A half-hour to learn Rust](https://fasterthanli.me/articles/a-half-hour-to-learn-rust)

[https://fasterthanli.me/articles/a-half-hour-to-learn-rust](https://fasterthanli.me/articles/a-half-hour-to-learn-rust)

> In order to increase fluency in a programming language, one has to read a lot of it. But how can you read a lot of it if you don't know what it means?
> 
> In this article, instead of focusing on one or two concepts, I'll try to go through as many Rust snippets as I can, and explain what the keywords and symbols they contain mean.


This is a really neat introduction to the programming language that is rapidly gaining momentum in the system programmer community.

Rust is specifically designed to protect against classes of bugs that are common in C and C++, buffer overflows, off by one errors, and so forth.

Out of the box, variables are immutable by default, and it's both incredibly typesafe (in a very similar way to Haskell or Scala, but you know, actually usable), as well as filled with compiler warnings that will refuse to compile unsafe code.

Rust differs from the other language in this space, Go, which is a replacement for low level languages like C, in that where Go is designed for web scale engineers writing high performant low level network and byte programming code, Rust is there to manage the kind of device driver, embedded programming and predictable performance types of code.

Between the two languages, if we see major low level operating systems (such as in firewalls, VPN's and network appliances) as well as major components like web rendering engines and javascript engines built in these languages, we'll almost totally eliminate entire classes of bugs.

Definitely a language worth taking a peek at


## [A retrospective on a decade of innovations | | The Guardian](https://www.theguardian.com/info/2021/oct/29/running-a-post-decade-innovation-retrospective)

[https://www.theguardian.com/info/2021/oct/29/running-a-post-decade-innovation-retrospective](https://www.theguardian.com/info/2021/oct/29/running-a-post-decade-innovation-retrospective)

> I sent a questionnaire to past and present colleagues and asked them to list their top three innovations and to break down how, from their perspective, they came into being. I analysed and clustered the responses and wrote a document that I hope reflects the opinions of the people that generously filled in the questionnaire. That document has in turn been used to input into discussions within the senior leadership teams to shape the next decade.
> 
> Below is an overview of those innovations and the people and factors that helped – and hindered – their coming into existence.
> 
> While I initially did this work for the benefit of the Guardian, I hope that everyone can learn something from our reflections.


I'm particularly proud of my time at the Guardian.  I worked with some of the smartest people I've ever met, and I learned so much from all of those people.  I'm pleased to see that several of the things I worked on, in particular the changing culture, the move from centralised operations to team owned products and operations, and the early adoption of AWS and the cloud were all referenced as innovations.

I wish I could take credit for any of it, but in fact mostly I was just a small cog in a big machine, with a lot of people around me who were smarter than me.  The biggest thing I have looking back is just how powerful it is to have such a good collection of collaborative and insightful people, all aligned on a good common set of goals.


