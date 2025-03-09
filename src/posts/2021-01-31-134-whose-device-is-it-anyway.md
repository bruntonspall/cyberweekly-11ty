---
title: "134 - Whose device is it anyway?"
date: 2021-01-31
description: "End User Devices are one of the roots of trust in any modern system.  We might worry about attackers getting into our servers or networks, but it doesn’t matter how much encrypted fairy dust we apply to the data, once it reaches the end user device, it has to be decrypted to be shown to the user."
permalink: /whose-device-is-it-anyway/
---

End User Devices are one of the roots of trust in any modern system.  We might worry about attackers getting into our servers or networks, but it doesn’t matter how much encrypted fairy dust we apply to the data, once it reaches the end user device, it has to be decrypted to be shown to the user.

Your whatsapp messages might be fully encrypted end to end, however the whatsapp application itself can always read the words that are in the messages.

Any security around your corporate network has to cover the security of the end user devices, whether that be corporate laptops and desktops or personal mobile phones.

As we saw in the mass migration to working from home as a pandemic response, we also saw a laxening of the security controls around the end user devices.  Organisations didn’t have enough laptops to provide everyone with one, and workforces who normally timeshared desktops would need to log in remotely from home.

The normal controls for this sort of thing might include using proxies to check what the device is accessing, or activity control on the device.  But these are increasingly privacy intruding and much harder to implement or justify if users are using the devices in their personal home and for personal business.

For many of us working from home, Covid has blurred the lines between work and personal time.  We tend to sit in the same seat, in the same room when we work and when we play computer games or browse the web.  This blurring of boundaries will inevitably lead to a relaxation of typical behaviours and provide security risks for the corporates.

But even if we can implement strong controls, such as VPN’s, activity monitoring and device attestation, the move to storing data in SaaS services, and zero-trust principles don’t make this easy to implement.  Even if your core network requires a healthy device and up to date patch status, you can’t require Trello or other tools to implement that as well.  About the only way to do this right now is to implement some form of Identity Aware Proxy in front of these internet based systems, which defeats much of the point of using internet accessible tools.

How we get solve these problems is going to be a big focus in the coming years.  Supply chain compromises show us that we need to both take advantage of these new dynamic and easy to change systems, but we need to be able to understand the security implications and manage the access controls and risk that they provide.


In another note, I want to thank people who wrote back to me with comments about the last few newsletters.  In particular, someone wrote to me to mention that I’d used the term “whitelisting” when [talking about the Sonicwall vulnerability last week](https://www.cyberweekly.net/the-lies-our-brains-tell-us).  I’d explain why try not to use the term anymore, but the [NCSC does a far better job of it](https://www.ncsc.gov.uk/blog-post/terminology-its-not-black-and-white).  I’m learning to change my language where I can, but sometimes I make mistakes, and I’m grateful that people feel able to point that out to me.

## [11-Year-Old Boy Learns Hacking Tips From YouTube, Demands Rs 10 Crore From Father As Ransom](https://www.india.com/viral/shocking-11-year-old-boy-learns-hacking-tips-from-youtube-demands-rs-10-crore-ransom-from-father-4363050/)

[https://www.india.com/viral/shocking-11-year-old-boy-learns-hacking-tips-from-youtube-demands-rs-10-crore-ransom-from-father-4363050/](https://www.india.com/viral/shocking-11-year-old-boy-learns-hacking-tips-from-youtube-demands-rs-10-crore-ransom-from-father-4363050/)

> When the police started their investigations, something really shocking came to the fore. It was found out that the IP address was of the complainant’s house itself, making it abundantly clear that the threat email was sent by someone from his family. With the crucial clue in hand, the police started interrogating the family members during which the complainant’s 11-year-old son confessed to the crime.
> 
> The minor boy, who is a Class 5 student told police that he learnt about cybercrime and how to avoid getting caught, online. He also watched a lot of YouTube videos to master his skill and ended up sending the extortion email to his father.


This is the modern equivalent of the old horror [trope of “The call was coming from inside the house”](https://tvtropes.org/pmwiki/pmwiki.php/Main/TheCallsAreComingFromInsideTheHouse)


## [How to Build Good Software](https://www.csc.gov.sg/articles/how-to-build-good-software)

[https://www.csc.gov.sg/articles/how-to-build-good-software](https://www.csc.gov.sg/articles/how-to-build-good-software)

> In software development, most ideas are bad; this is not anyone’s fault. It is just that the number of possible ideas is so large that any particular idea is probably not going to work, even if it was chosen very carefully and intelligently. To make progress, you need to start with a bunch of bad ideas, discard the worst, and evolve the most promising ones. Apple, a paragon of visionary design, goes through dozens of prototypes before landing on a final product. The final product may be deceptively simple; it is the intricate knowledge of why this particular solution was chosen over its alternatives that allows it to be good.
> 
> This knowledge continues to be important even after the product is built. If a new team takes over the code for an unfamiliar piece of software, the software will soon start to degrade. Operating systems will update, business requirements will change, and security problems will be discovered that need to be fixed. Handling these subtle errors is often harder than building the software in the first place, since it requires intimate knowledge of the system’s architecture and design principles.
> 
> In the short term, an unfamiliar development team can address these problems with stopgap fixes. Over time though, new bugs accumulate due to the makeshift nature of the additional code. User interfaces become confusing due to mismatched design paradigms, and system complexity increases as a whole. Software should be treated not as a static product, but as a living manifestation of the development team’s collective understanding.
> 
> Software should be treated not as a static product, but as a living manifestation of the development team’s collective understanding.
> 
> This is why relying on external vendors for your core software development is difficult. You may get a running system and its code, but the invaluable knowledge of how it is built and what design choices were made leaves your organisation. This is also why handing a system over to new vendors for “maintenance” often causes problems. Even if the system is very well documented, some knowledge is lost every time a new team takes over. Over the years, the system becomes a patchwork of code from many different authors. It becomes harder and harder to keep running; eventually, there is no one left who truly understands how it works.


This report is excellent generally, but this section was pointed out by Cory Doctorow on twitter and is a great summary of one of the problems of multi-disciplinary teams and the fungibility of “engineers”.  It’s often assumed that teams who build things can leave, that you can hand over a prototype and some research and the next team will develop the right product.  Even in traditional waterfall or V-model software development, the assumption that you can encode knowledge into the specifications creates the problems that are so familiar.

People aren’t replaceable, fungible resources even if they have similar skill sets.  Because many of the things we understand are understood implicitly or understood with a hard won context that is difficult to replace.


## [Wandera Cloud Security Report 2021 | Wandera](https://www.wandera.com/cloud-security-report-2021eapvoeasdasdasdcaz/wandera-cloud-security-report-2021/)

[https://www.wandera.com/cloud-security-report-2021eapvoeasdasdasdcaz/wandera-cloud-security-report-2021/](https://www.wandera.com/cloud-security-report-2021eapvoeasdasdasdcaz/wandera-cloud-security-report-2021/)

> Organizations aspire to strong endpoint security, but they run into common dilemmas —such as how to temporarily secure contractor devices while they are accessing sensitive data, or how to respect the privacy of employees on BYOD devices while still enforcing some kind of security. Users are generally opposed to security and management solutions. They do not want to be spied on and they know that these solutions need to conduct monitoring to catch the bad stuff.
> 
> We know that 70% of successful breaches originate on the endpoint. We also know that 83% of organizations say that providing access to third parties (e.g., contractors or supply chain partners) is difficult to extremely difficult, so there are improvements to be made when it comes to securing unmanaged endpoints.
> 
> According to Verizon, 87% of enterprises are seeing mobile threats outpace other threat types. This is likely because mobile devices are difficult to manage and secure, due to their personal nature, and bad actors are aware of this security gap.
> In one study, 92% of FT 500 companies said they were worried that their growing mobile workforce represents a rising risk of security issues. While the majority of organizations have embraced bring your own device (BYOD) policies, the vast majority (94%) said BYOD has increased mobile security risks.
> 
> Remote working is likely to remain a part of standard business practices, even after enough of the population has been vaccinated against COVID-19. So IT teams need to establish practices that fit the needs of a broad array of managed and unmanaged devices and networks. They also need to ensure that remote devices are no longer on the periphery of security operations by bringing the threat data together from all endpoints into the SOC.


This is an excellent report, not only because the report is just plain HMTL that isn’t hidden behind a registration wall (although I wish more strategy companies would do that).  But covers a variety of security issues that are interesting to most of us.  The focus here on the security of endpoints is critical.  As we move towards a world of people moving data out of their core corporate network and into SaaS tools, as well as staff working more remotely means a blurring of devices.  End users will use the same devices for personal use and work use, and it’s going to be harder and harder to prevent that.


## [Campaigns](https://kellysutton.com/2021/01/06/campaigns.html)

[https://kellysutton.com/2021/01/06/campaigns.html](https://kellysutton.com/2021/01/06/campaigns.html)

> As engineering organizations grow, the problems and their solutions become more intricate. What might have taken an afternoon now takes months of coordinated effort. The system (both the technology and the people) are larger, more complex, and more difficult to change than ever before.
> 
> But change is necessary.
> 
> We might be looking to pay off some technical debt or tee up an architectural change to unlock a better customer experience, cost savings, etc. What is a tool we can use to coordinate many groups of people, hold groups accountable, and eventually succeed?
> 
> Enter what I call the Campaign.


This is an interesting articulation of a fairly common project management problem.  Project managers working across a number of suppliers will already be familiar with tracking a project health at a high level, having status meetings and getting the project delivered.  Of course, within agile software development, classical project management tools and skills are reviled, and as such we reinvent the past.  In this case, I think this is a good articulation of how to define the dependencies, identify blockers and prioritise efforts.  I'd just call it a "project" rather than a "campaign".


## [New campaign targeting security researchers](https://blog.google/threat-analysis-group/new-campaign-targeting-security-researchers/amp/)

[https://blog.google/threat-analysis-group/new-campaign-targeting-security-researchers/amp/](https://blog.google/threat-analysis-group/new-campaign-targeting-security-researchers/amp/)

> The actors have been observed targeting specific security researchers by a novel social engineering method. After establishing initial communications, the actors would ask the targeted researcher if they wanted to collaborate on vulnerability research together, and then provide the researcher with a Visual Studio Project. Within the Visual Studio Project would be source code for exploiting the vulnerability, as well as an additional DLL that would be executed through Visual Studio Build Events. The DLL is custom malware that would immediately begin communicating with actor-controlled C2 domains. 
> 
> In addition to targeting users via social engineering, we have also observed several cases where researchers have been compromised after visiting the actors’ blog. In each of these cases, the researchers have followed a link on Twitter to a write-up hosted on blog.br0vvnn[.]io, and shortly thereafter, a malicious service was installed on the researcher’s system and an in-memory backdoor would begin beaconing to an actor-owned command and control server. At the time of these visits, the victim systems were running fully patched and up-to-date Windows 10 and Chrome browser versions.


As security professionals we often note and warn how vulnerable other people are, but forget that we are interesting targets ourselves.  

This approach via social media and a request to collaborate will sound familiar to experts in science, business and academic professions, but the use of collaboration through a compromised project is a programmer specific twist.  The use of unidentified zero-days in either Windows 10 and Chrome is worrying as well.  Drive-by downloads are generally regarded to be expensive and noisy, and not used for common targets due to the value of the exploits.


## [A deeper dive into our May 2019 security incident - Stack Overflow Blog](https://stackoverflow.blog/2021/01/25/a-deeper-dive-into-our-may-2019-security-incident/)

[https://stackoverflow.blog/2021/01/25/a-deeper-dive-into-our-may-2019-security-incident/](https://stackoverflow.blog/2021/01/25/a-deeper-dive-into-our-may-2019-security-incident/)

> There’s a lot to digest here, but we wanted to give a good overview of how an incident like this starts out and use it as an opportunity to inform other companies and sites on how these things unfold. The more that we are prepared for and anticipate events like this, the better protected we all will be against future events of this nature.
> 
> 


This is a really great writeup of a pretty determined attacker.  The fact that StackOverflow were also able detect the attackers browsing of StackOverflow as a knowledge platform to try to educate themselves on the underlying technology helps us see how much research they need to attack a target.


## [SUNSPOT Malware: A Technical Analysis | CrowdStrike](https://www.crowdstrike.com/blog/sunspot-malware-technical-analysis/)

[https://www.crowdstrike.com/blog/sunspot-malware-technical-analysis/](https://www.crowdstrike.com/blog/sunspot-malware-technical-analysis/)

> Key Points
> SUNSPOT is StellarParticle’s malware used to insert the SUNBURST backdoor into software builds of the SolarWinds Orion IT management product.
> SUNSPOT monitors running processes for those involved in compilation of the Orion product and replaces one of the source files to include the SUNBURST backdoor code.
> Several safeguards were added to SUNSPOT to avoid the Orion builds from failing, potentially alerting developers to the adversary’s presence. 
> Analysis of a SolarWinds software build server provided insights into how the process was hijacked by StellarParticle in order to insert SUNBURST into the update packages. The design of SUNSPOT suggests StellarParticle developers invested a lot of effort to ensure the code was properly inserted and remained undetected, and prioritized operational security to avoid revealing their presence in the build environment to SolarWinds developers.


This is really interesting.  I had assumed that the solar winds attackers would simply have added their backdoored code to the software repository of Orion itself, in the assumption that it would be missed in the noise.  But instead they had custom malware that infected the build servers, and modified every build that came out silently.  

This is a choice, it would reduce the possibility of detection by the development teams during code review and wouldn’t leave traces, but feels far more fragile.  There was explicit checks to avoid compilation error, but there’s a good chance that this wouldn’t work if there was build changes, refactoring or other major changes in the build system.


## [Axios Codebook](https://www.axios.com/newsletters/axios-codebook-b04bf6f5-5c30-45ba-95b9-fbe944b6a668.html)

[https://www.axios.com/newsletters/axios-codebook-b04bf6f5-5c30-45ba-95b9-fbe944b6a668.html](https://www.axios.com/newsletters/axios-codebook-b04bf6f5-5c30-45ba-95b9-fbe944b6a668.html)

> American outrage over foreign cyber espionage, like Russia's SolarWinds hack, obscures the uncomfortable reality that the U.S. secretly does just the same thing to other countries.
> 
> * Why it matters: Secrecy is often necessary in cyber spying to protect sources and methods, preserve strategic edges that may stem from purloined information, and prevent diplomatic incidents.
> 
> But when the U.S. is only portrayed as a victim of nation-state cyber activity and not as a perpetrator in its own right, it creates a false impression of the state of play and invites calls for vengeance that could prove misguided or self-defeating.
> 
> * The big picture: The U.S. is stronger in cyberspace than any other country, with world-spanning digital snooping capabilities, buttressed by American technological ingenuity and some of the planet’s most talented hackers and daring overseas operators.
> 
> 


This is a great newsletter generally, but I thought this point was very interesting. There isn’t a lot of coverage of western agencies as APT’s, which means that we don’t see that coverage the same, and will give bias to our perception of the world


## [Google researcher discovers new iOS security system | ZDNet](https://www.zdnet.com/article/google-researcher-discovers-new-ios-security-system/)

[https://www.zdnet.com/article/google-researcher-discovers-new-ios-security-system/](https://www.zdnet.com/article/google-researcher-discovers-new-ios-security-system/)

> While iOS ships with multiple sandbox mechanisms, BlastDoor is a new addition that operates only at the level of the iMessage app.
> 
> Its role is to take incoming messages and unpack and process their content inside a secure and isolated environment, where any malicious code hidden inside a message can't interact or harm the underlying operating system or retrieve with user data.


This is a strong pattern that should be used for processing messages from untrusted third parties.  Parse the message and it’s content inside a sandbox that prevents any parsing errors from breaking out and affecting anything else.

Of course, the final content can still have a negative effect, but it reduces the number of vectors that the attacker can use to attack the system


## [Apple says iOS 14.4 fixes three security bugs ‘actively exploited’ by hackers | TechCrunch](https://techcrunch.com/2021/01/26/apple-says-ios-14-4-fixes-three-security-bugs-under-active-attack/)

[https://techcrunch.com/2021/01/26/apple-says-ios-14-4-fixes-three-security-bugs-under-active-attack/](https://techcrunch.com/2021/01/26/apple-says-ios-14-4-fixes-three-security-bugs-under-active-attack/)

> In 2019, Google security researchers found a number of malicious websites laced with code that quietly hacked into victims’ iPhones. TechCrunch revealed that the attack was part of an operation, likely by the Chinese government, to spy on Uyghur Muslims. In response, Apple disputed some of Google’s findings in an equally rare public statement, for which Apple faced more criticism for underplaying the severity of the attack.
> 
> Last month, internet watchdog Citizen Lab found dozens of journalists had their iPhones hacked with a previously unknown vulnerability to install spyware developed by Israel-based NSO Group.
> 
> In the absence of details, iPhone and iPad users should update to iOS 14.4 as soon as possible.


There was nothing clear that I’d seen to suggest what Apple was responding to, but it feels highly likely that they were responding to the CitizenLabs accusations


