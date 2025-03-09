---
title: "240 - Commoditisation of Capability"
date: 2024-02-25
description: "There's a concept that's been floating around for decades called the [commoditization of process](https://hbr.org/2005/06/the-coming-commoditization-of-processes) or commoditisation of capability."
permalink: /commoditisation-of-capability/
---

There's a concept that's been floating around for decades called the [commoditization of process](https://hbr.org/2005/06/the-coming-commoditization-of-processes) or commoditisation of capability.

I first encountered the concept in the business management book ["The Innovators Dilemma" by Clayton Christiansen](https://en.wikipedia.org/wiki/The_Innovator%27s_Dilemma) back in about 2013 which was first published in 1997.  Clayton was talking about disruptive technologies and what they do to firms, and charted the rise of the minicomputer and how it disrupted the mainframe, along with the later rise of the desktop and how that affected the minicomputer.

In the disruptive technology model, the principle is that established companies don't innovate in novel new ways, because their customers tend to want iteration rather than disruption.  Instead they iterate their products "upstream", to higher value, smaller numbers of customers, leaving a wide long-tail of customers who might have a changing product requirement, which new innovative disruptors can take advantage of.  In this model, the idea is that you don't compete with big players at the thing they are good at, but instead you compete in the areas that they aren't good at and they tend to retreat, leaving you free to capture the market.

There's a second order impact of this as you look at technological markets over time.  Most technology product firms start their journey through the creation of single, individually hand made products that totally match a target customer.  Tesla started the building of its cars with very expensive custom luxury sports cars for example.  Products that are successful move over time to become productised, so that it's easier for consumers to compare products from Company A with products from Company B.  Data center hosting followed this curve in the late 90's, where it became increasingly unimportant just what hardware you bought, and what physical building it was in, because you knew that you relied on fixed power, network access and software to put on the boxes.  Where people competed in this space, it was because their box fit in the 1/2/4u product specification, and provided capabilities that you wanted, so was either lower power, or more dense storage arrays, or better product guarantees and so on.

However, something peculiar happens at a certain point in this area, epitomised by the rise in cloud computing, but replicable into lots of other industries.  The individual products become commoditised.  That is to say, you really do stop caring about the individual product, because it has become essentially a base commodity.  As the user, you might have preferences for Dell Servers or HP servers, but at almost any point at least 1 removed from it, you probably don't care.  As a software engineer building systems in the early 00's, I didn't know whether I had a Dell Server, an HP server or similar.  All I cared about was that it ran a Java Enterprise stack and could run my code, and provided the right levels of abstractions.

This commoditisation is something we've seen in products over hundreds of years, but it's happening in places that we're not as used to, and the last 20 years have changed some really significant services that we care about.  It isn't just products that you buy off of the shelf, but entire processes, like incident response processes.  Why custom create your own processes if you can use a well defined one and it fits and works with other tools effectively?

Threat Intelligence used to be the preserve of just [three letter agencies](https://en.wikipedia.org/wiki/Alphabet_agencies#In_national_security), essentially a capability that only the most advanced nation states could make use of.  In the same way that massive scale of compute was something that was only available to the [FAANG tech giants](https://en.wikipedia.org/wiki/Big_Tech#FAANG).  This commoditisation of cloud makes it easier than ever for tiny tech companies to make use of the same benefits of scale that the big tech companies had, but it's not without it's own drawbacks and implications.

So if commoditisation is a second order effect of this disruptive innovation concept, what's the second order concept of commoditisation?  In my view, the challenge and opportunity that commoditisation brings is the paralysis of too much choice, and the impact of making decisions so much more complex. 

As Jack Lindermood articulates in his article about the tech choices that his organisation has made, there are now a huge number of choices that one can make about which product to select from this commoditised marketplace.  It's much harder to define the parameters for each choice, and of course different companies will make different choices.  Indeed, even within companies, sometimes individual teams will want to make different technology choices, either because they think the choice is better suited, or because [it better builds their CV, their interest or their personal preference](https://mcfunley.com/choose-boring-technology).  We as a community should be doing more of what Jack has done, and articulating which choices we've made, and why we've made them to enable the community to understand the tradeoffs, decisions and the breadth of decision making that happens.  Tech firms need to think about the way they will make and support choice within their organisation, whether that be by defining strict governance that prohibits choice, or it's through the creation of a [paved path model](https://netflixtechblog.com/scaling-appsec-at-netflix-part-2-c9e0f1488bc5).

Commoditisation doesn't happen to every product, in every vertical or consistently in my experience.  But it is a business force that is worth paying attention to, because if you currently have products built or customised for you, knowing when those will slip over into commodity products that you can easily swap out, is a decision worth revisiting on a regular basis.  

As for what it brings in Cybersecurity, I can't predict exactly, but it's something that I think is increasingly affecting our industry and often in unexpected ways.  Of the ones most visible, the commoditisation of threat intelligence is the one that I see impacting us the most.  It's this change in threat intelligence and the capabilities that make it possible that make an ["open source intelligence agency"](https://www.bellingcat.com/) something that is possible.

Final note, I'm going to be speaking at [London QCon in early April](https://qconlondon.com/), on a talk tentatively titled ["Beyond the Breach: Proactive Defense in the Age of Advanced Threats"](https://qconlondon.com/presentation/apr2024/beyond-breach-proactive-defense-age-advanced-threats).  I'll be attending the conference and watching other sessions, so I'll be around in hallways, so do come say hello if you are around.

## [Unmasking I-Soon | The Leak That Revealed China's Cyber Operations - SentinelOne ](https://www.sentinelone.com/labs/unmasking-i-soon-the-leak-that-revealed-chinas-cyber-operations/)

[https://www.sentinelone.com/labs/unmasking-i-soon-the-leak-that-revealed-chinas-cyber-operations/](https://www.sentinelone.com/labs/unmasking-i-soon-the-leak-that-revealed-chinas-cyber-operations/)

> I-Soon (上海安洵), a company that contracts for many PRC agencies–including the Ministry of Public Security, Ministry of State Security, and People’s Liberation Army–was subject to a data leak over the weekend of Feb 16th. It is not known who pilfered the information nor their motives, but this leak provides a first-of-its-kind look at the internal operations of a state-affiliated hacking contractor. The authenticity of the documents is still undecided. While the leak’s contents do confirm public threat intelligence, efforts to corroborate further the documents are on-going.
> 
> […]
> 
> Machine translation enabled the rapid consumption of leaked data. These tools broadened the initial analysis of the information beyond seasoned China experts with specialized language skills and technical knowledge. This has enabled many more analysts to scan the leaked information and quickly extract and socialize findings. As researchers dig into the voluminous information, domain expertise will be required to understand the complex relationships and implicit patterns between the relevant organizations, companies, and individuals. One upshot is that geographically-specialized analysis will continue to provide distinct value, but the barrier to entry is much lower. 


This leak was obviously a big deal in threat intelligence areas, but there was a lot of complexity over actual attribution, and as mentioned below, further corroboration will be needed before anyone can take much away from it.

What I thought was more interesting was that it touched on a topic that I’m really interested in, that of increasing commercial capability.

Years ago, if a major leak was published in a foreign language, then it would have been incredibly difficult for any journalistic outfit other than the largest to get the documents translated and understood.  Google translate is all good and well, people would say, but it can do simple phrases, it doesn’t get idiom, it doesn’t do documents at scale and it doesn’t do technical language.  

Many of those problems have become increasingly commoditised, and it’s now far easier for an up and coming small threat intelligence firm to grab documents like this, translate them using modern LLM powered translation tools and summarise and understand them.  

This makes use of the increasing commoditisation of language and analysis tooling to further commoditise threat intelligence itself.  Again, years ago, only the biggest firms or state organisations could possibly have both the language capability but also the cyber threat expertise to understand what was there.  I think that’s still partially true today, but it’s increasingly easier for small players to develop and deliver incredibly valuable expertise in this space.

Of course, the downside to increasingly commoditised capability is that it becomes much harder to distinguish based on quality, or determine the effectiveness of sourcing.  If there were deliberate errors, falsehoods or misinformation buried in a leak this size, the fact that many small organisations would read it, repeat it, would amplify that “fact” and adjust the discourse.  That’s one of the reasons that these growing threat intelligence firms are still going to have to be careful about the speed and quality of their analytical product. 


## [(Almost) Every infrastructure decision I endorse or regret after 4 years running infrastructure at a startup · Jack's home on the web ](https://cep.dev/posts/every-infrastructure-decision-i-endorse-or-regret-after-4-years-running-infrastructure-at-a-startup/)

[https://cep.dev/posts/every-infrastructure-decision-i-endorse-or-regret-after-4-years-running-infrastructure-at-a-startup/](https://cep.dev/posts/every-infrastructure-decision-i-endorse-or-regret-after-4-years-running-infrastructure-at-a-startup/)

> I’ve led infrastructure at a [**startup**](https://cresta.com/careers/) for the past 4 years that has had to scale quickly. From the beginning I made some core decisions that the company has had to stick to, for better or worse, these past four years. This post will list some of the major decisions made and if I endorse them for your startup, or if I regret them and advise you to pick something else. 


This is an absoutely marvelous list of the sorts of tech decisions, apps and platforms that you need to run a modern digital company that employs software developers.

This list is why I think it’s so important to have a team, reporting to the CTO, who care about internal employee experience.  You can focus it on developer experience if you want, or you can lump it in with infrastructure, but being able to make these decisions about what apps you support, what they give to your staff, and how they enable the business to achieve its goals is how you outmaneuver your competition

via [lobste.rs](https://lobste.rs/s/pgahrv/almost_every_infrastructure_decision_i) where there’s some excellent discussions 


## [Postmortem Template - PagerDuty Incident Response Documentation ](https://response.pagerduty.com/after/post_mortem_template/)

[https://response.pagerduty.com/after/post_mortem_template/](https://response.pagerduty.com/after/post_mortem_template/)

> This page is intended to be reviewed during a postmortem meeting that should be scheduled within 5 business days of any event. Your first step should be to schedule the postmortem meeting in the shared calendar for within 5 business days after the incident. Don't wait until you've filled in the info to schedule the meeting. Make sure the page is completed by the meeting. 


Do you ocnduct post mortems for your operations and security incidents?  You definitely should and probably don’t.
Even if you do, based certainly on my experience consulting with teams, there’s a good chance that you aren’t as effective at them as you’d like to be.

This template also links to some of PagerDuty’s writeups on good process and getting the best out of post-mortems, but the starter for most of us is both doing them, and making sure they are done quickly, consistently and they are lightweight.  This kind of template makes all of those things much easier. 


## [Unleashing the power of cloud with containerisation - NCSC.GOV.UK ](https://www.ncsc.gov.uk/blog-post/unleashing-the-power-of-cloud-with-containerisation)

[https://www.ncsc.gov.uk/blog-post/unleashing-the-power-of-cloud-with-containerisation](https://www.ncsc.gov.uk/blog-post/unleashing-the-power-of-cloud-with-containerisation)

> It’s important to recognise that the security benefits associated with containerisation are opportunities, not guarantees. In other words, if you take an existing application and turn it into a container, you are unlikely to gain any security benefits if you do nothing else. In fact, if you take applications that used to be in separate machines (or virtual machines) and put them all into containers on one machine, you may have worsened your security posture.
> 
> To get the most out of containerisation, you need to invest time and resources to adapt your approach to be ‘container native’.
> 
> As we cover in our [new guidance on using containerisation](https://www.ncsc.gov.uk/collection/using-containerisation) , you need to adapt how you [build container images](https://www.ncsc.gov.uk/collection/using-containerisation/building-container-images) and [run containers](https://www.ncsc.gov.uk/collection/using-containerisation/running-containers) to ensure that you make the most of the security opportunities that containerisation can bring.
> 
> When you use [containerisation in the cloud](https://www.ncsc.gov.uk/collection/using-containerisation/containerisation-in-the-cloud) , you also need to think about how much [responsibility you can share](https://www.ncsc.gov.uk/collection/cloud/understanding-cloud-services/cloud-security-shared-responsibility-model) with your cloud provider so that they can achieve these security outcomes on your behalf. For example, when using serverless compute services that will build your code for you, the service can make it easier for you to test your workloads locally, or to analyse their contents by giving you the ability to export the container image it builds. 


This is a great bit of work by the NCSC technical team to do a bit more of a deep dive into the security properties and models of containers.  The caveat here is a good one to remember, that containers don’t give you much of a security boundary.

Container breakouts are possible, and will be increasingly possible as more security research is directed in that area.  Treating your containers as if they have have the same properties as virtual machines will lead to adversaries having a far easier time of lateral movement than you have modelled for, and could give rise to some attacks that you didn’t threat model against. 


## [Leaky Vessels: Docker and runc Container Breakout Vulnerabilities - January 2024 | Snyk ](https://snyk.io/blog/leaky-vessels-docker-runc-container-breakout-vulnerabilities/)

[https://snyk.io/blog/leaky-vessels-docker-runc-container-breakout-vulnerabilities/](https://snyk.io/blog/leaky-vessels-docker-runc-container-breakout-vulnerabilities/)

> On January 31, 2024, the [**maintainers**](https://github.com/opencontainers/runc) of `runc` , a CLI tool for spawning and running containers on Linux, announced a vulnerability ( [**CVE-2024-21626**](https://security.snyk.io/vuln?search=CVE-2024-21626) ) that allows for an order-of-operations container breakout centered around the `WORKDIR` command. Exploitation of this vulnerability can result in container escape to the underlying host operating system. This could occur by _running_ a malicious image or by _building_ a container image using a malicious Dockerfile or upstream image (i.e. when using `FROM` ). The patched version, `runc` 1.1.12, was released on January 31, 2024, at around 3:00 PM EST, per the maintainers.
> 
> You can read more details about the vulnerability in this [**high-level**](https://snyk.io/blog/cve-2024-21626-runc-process-cwd-container-breakout/) blog, which outlines the `runc` vulnerability itself. In addition, Rory and the Snyk Labs team identified three other container escape vulnerabilities for a total of four vulnerabilities 


This is a reminder that containers provide _some_ separation of concerns on a given estate, but do not necessarily provide a strong security control.  You should assume that if you are sharing a host computer with another untrusted container, that malicious activity could jump from the container to the host and then into your container.  

If those containers are all operating within the same security domain (i.e. they’re all part of the same application), then that may not be an issue, but if you are using containers to separate out different tenants, or to separate highly privileged operations from user facing operations, you should ensure that those containers run on different hosts that are legitimately in different security domains 


## [The Nine Lives of Commando Cat: Analysing a Novel Malware Campaign Targeting Docker - Cado Security | Cloud Forensics & Incident Response ](https://www.cadosecurity.com/the-nine-lives-of-commando-cat-analysing-a-novel-malware-campaign-targeting-docker/)

[https://www.cadosecurity.com/the-nine-lives-of-commando-cat-analysing-a-novel-malware-campaign-targeting-docker/](https://www.cadosecurity.com/the-nine-lives-of-commando-cat-analysing-a-novel-malware-campaign-targeting-docker/)

> Cado researchers have recently encountered a novel malware campaign, dubbed “Commando Cat”, targeting exposed Docker API endpoints. This is the second campaign targeting Docker since the beginning of 2024, the first being the malicious deployment of the [9hits](https://www.cadosecurity.com/containerised-clicks-malicious-use-of-9hits-on-vulnerable-docker-hosts/) traffic exchange application, our report into which was published only a matter of weeks ago. 
> 
> Attacks on Docker are relatively common, particularly in cloud environments. This campaign demonstrates the continued determination attackers have to exploit the service and achieve a variety of objectives. Commando Cat is a cryptojacking campaign leveraging Docker as an initial access vector and (ab)using the service to mount the host’s filesystem, before running a series of interdependent payloads directly on the host. 


This is an interesting breakdown of how an attacker can use an exposed Docker API instance, break out of the container and infect the host with the intent of running cryptocurrency mining software on it. 


## [Your AI Girlfriend Is a Data-Harvesting Horror Show ](https://gizmodo.com/your-ai-girlfriend-is-a-data-harvesting-horror-show-1851253284)

[https://gizmodo.com/your-ai-girlfriend-is-a-data-harvesting-horror-show-1851253284](https://gizmodo.com/your-ai-girlfriend-is-a-data-harvesting-horror-show-1851253284)

> You’ve heard stories about data problems before, but according to Mozilla, AI girlfriends violate your privacy in “disturbing new ways.” For example, CrushOn.AI collects details including information about sexual health, use of medication, and gender-affirming care. 90% of the apps may sell or share user data for targeted ads and other purposes, and more than half won’t let you delete the data they collect. Security was also a problem. Only one app, Genesia AI Friend & Partner, met Mozilla’s minimum security standards.
> 
> One of the more striking findings came when Mozilla counted the trackers in these apps, little bits of code that collect data and share them with other companies for advertising and other purposes. Mozilla found the AI girlfriend apps used an average of 2,663 trackers per minute, though that number was driven up by Romantic AI, which called a whopping 24,354 trackers in just one minute of using the app.
> 
> The privacy mess is even more troubling because the apps actively encourage you to share details that are far more personal than the kind of thing you might enter into a typical app. EVA AI Chat Bot & Soulmate pushes users to “share all your secrets and desires,” and specifically asks for photos and voice recordings. It’s worth noting that EVA was the only chatbot that didn’t get dinged for how it uses that data, though the app did have security issues.


You can read the [original Mozilla reporting](https://foundation.mozilla.org/en/privacynotincluded/articles/happy-valentines-day-romantic-ai-chatbots-dont-have-your-privacy-at-heart/) if you want, but this Gizmodo write up is pretty much on point.

I doubt the fact of these AI chat bots using data to track you and build a advertising model is much of a surprise to anyone, but the scale should be.  Pinging out data to tens of thousands of trackers that are summarised views on your sexual health, gender identify and deep wants and desires should scare not just the users, but anyone who could be the subject of invasive nation state targeting.  Buying this data in aggregate so that you can target malvertising at people is far easier than you'd think, and this sort of thing in someone's personal life can create a vector to target and attack your company.

Awareness is probably the key for this.  Ensure your most critical staff are aware of the privacy implications of such AI chat bots, and that they can make good decisions.


## [Solene'% : OpenBSD workstation hardening ](https://dataswamp.org/~solene/2023-12-31-hardened-openbsd-workstation.html)

[https://dataswamp.org/~solene/2023-12-31-hardened-openbsd-workstation.html](https://dataswamp.org/~solene/2023-12-31-hardened-openbsd-workstation.html)

> I wanted to share a list of hardening you can do on your OpenBSD workstation, and explaining the threat model of each change.
> 
> [...]
> 
> 2.1. The Least privileges §
> In order to prevent a program to escalate privileges, remove yourself from the wheel group, and don't set any doas or sudo permission.
> 
> If you need root privileges, switch to a TTY using the root user.
> 
> 2.2. Multiple-factor authentication §
> In some cases, it may be desirable to have a multiple factor authentication, this mean that in order to log in your system, you would need a TOTP generator (phone app typically, or a password manager such as KeePassXC) in addition to your regular password.
> 
> This would protect against people nearby who may be able to guess your system password.
> 
> I already wrote a guide explaining how to add TOTP to an OpenBSD login.


Some of these are interesting.  You are definitely making user experience harder, but in many cases, this is about making life also difficult for an adversary who has compromised your user account.

The non privileged user one is applicable to other operating systems as well.  On windows, you are probably better with fast user switching between an admin user and a non-privileged user rather than using the User Account Control model.


## [Tyranid's Lair: Sudo On Windows a Quick Rundown ](https://www.tiraniddo.dev/2024/02/sudo-on-windows-quick-rundown.html)

[https://www.tiraniddo.dev/2024/02/sudo-on-windows-quick-rundown.html](https://www.tiraniddo.dev/2024/02/sudo-on-windows-quick-rundown.html)

> What always gets me interested is where there’s an RPC channel involved. The reason a communications channel exists is due to the limitations of UAC, it very intentionally doesn’t allow you to attach elevated console processes to an existing low privileged console (grumble UAC is not a security boundary, but then why did this do this if it wasn’t grumble).
> 
> [...]
> 
> Yup, the DACL for the ALPC port has the Everyone group. It would even allow restricted tokens with the RESTRICTED SID set such as the Chromium GPU processes to access the server. This is pretty poor security engineering and you wonder how this got approved to ship in such a prominent form. 
> 
> 
> The worst case scenario is if an admin uses this command on a shared server, such as a terminal server then any other user on the system could get their administrator access. Oh well, such is life…
> 
> 
> 
> I will give Microsoft props though for writing the code in Rust, at least most of it. Of course it turns out that the likelihood that it would have had any useful memory corruption flaws to be low even if they'd written it in ANSI C. This is a good lesson on why just writing in Rust isn't going to save you if you end up just introducing logical bugs instead.


This is why secure by design principles matter so much.  By definition a command that is designed to escalate the privileges of a user is a security feature and needs to have explicit and careful threat modelling applied to it.

The fact that this can be silently enabled through a simple registry change, and can then be abused to run commands as the administrator means that it will be a tool that can be abused.  It would be worth considering putting in place detection rules for the use of the RPC channel or the command on all server instances that shouldn't have it installed.


## [cohost! - "I broke IKEA." ](https://cohost.org/sirocyl/post/2891449-i-broke-ikea)

[https://cohost.org/sirocyl/post/2891449-i-broke-ikea](https://cohost.org/sirocyl/post/2891449-i-broke-ikea)

> my phone service has a rather clever anti-spam tactic, which works like this:
> 
> I receive a phone call from an unknown number, and it goes through screening when I answer it. It rings until the fifth ring, the voicemail greeting plays out, then I've got 30 seconds to judge if it's a spam robocall or if it's genuine
> 
> * If it's okay, I press 1, and it interrupts the ring/voicemail sequence and I answer the call like usual.
> * If it's spam, I press ### (the # key by itself normally opens my PBX menu, so it doesn't go through) and hang up immediately.
> 
> Pressing ### and hanging up, will shove the call to voicemail, then launch a "DTMF bomb", which is a rapid sequence of over a hundred tones of DTMF keysmash, even including some of the ["ABCD" keys](https://en.wikipedia.org/wiki/Dual-tone_multi-frequency_signaling##,_*,_A,_B,_C,_and_D). This has blown up spammers' cheapass PBXes, especially ones with poor security and too much trust given to the DTMF decoder on the call server.
> 
> So, when IKEA called from a random 1-877 number to confirm my furniture shipment worth $1200 (that's the equivalent of :sixty: blåhaj!), the only thing it said is "To continue in English, please press 1."... and I had no idea who it was, immediately thought it was spam, and did the ### gesture. Oops.


What a great defensive concept for dealing with spam.  In the comments you can see the juryrigged service that Sirocyl uses, which they say they have mostly dropped since moving to Google Voice, as that platform drops most of the spam calls anyway.


