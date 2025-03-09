---
title: "191 - Risk and Reward"
date: 2022-04-03
description: "Humans are funny creatures, we're afraid of flying but drive cars on a daily basis despite one being the safest form of travel and the other being the most dangerous."
permalink: /risk-and-reward/
---

Humans are funny creatures, we're afraid of flying but drive cars on a daily basis despite one being the safest form of travel and the other being the most dangerous.

We have terrible natural senses of probability, risk and reward.  Asking almost any question involving probability and human decision making almost never makes logical or statistical sense, because we are driven by emotions, by cognitive biases and through logic formed of our own perception of the world rather than an objective reality (if such a thing even exists).

We often exhibit anchoring effects, whereby recent risk decisions will affect our view of the next thing that looks similar.  For example, the log4j vulnerability was a horrendous vulnerability in the java ecosystem first found by a Chinese security researcher and leaked online.  It had a massive impact on our supply chains, it required much out of hours work, and many teams didn't take it seriously enough when it first came out.  The Spring4Shell vulnerability in SpringFramework is a nasty vulnerability in the java ecosystem first found by a Chinese security researcher and leaked online.  We had a number of security research firms start to predict how this would also be a supply chain nightmare, but the actual exploitation and impact of the vulnerability is much less than first predicted, despite the fact that both vulnerabilities have "cool names with a 4 in them".

Our predictions around risk will always suffer from a cognitive bias around availability heuristics, because those of us who work in security spend the vast majority of our time dealing with, reading about and sharing stories of incidents, where everything goes wrong.  But we don't tend to talk about near misses, or complete misses.  We don't talk about the times when our EDR software caught the ransomware software before it could execute and the user didn't notice.  We don't talk about the thousands of people who go about their business online, all day every day, without being phished, defrauded or otherwise compromised.  

That means that we tend to overindex on the likelihood that these events will happen, as well as the potential impact of the events, and makes us terribly unpopular at parties.  (You try telling a cybersecurity incident story at a party and see how popular you are!)

I've long been a fan of Ryan McGeehan's [work in risk management](https://magoo.medium.com/lessons-learned-in-risk-measurement-c33b4de0f72e) and the way that he's moved from [Risk Management to Risk Measurement using lessons learned from forecasting](https://magoo.github.io/risk-measurement/) and [Daniel Miessler's](https://danielmiessler.com/newsletter/) article on risk really emphasises not just the forecasting element, but the need to compare that to the value gained by taking the risk.  The concept of trying to put a numerical value onto the benefit gained by using something, and then seeing if the risk outweighs the reward is something that we could do with doing more in risk management.  However, I suspect it would require far more joined up working between the security team and the product teams, and that's something that is time consuming and difficult to arrange.  In the meantime, when you are considering risks, ask yourself just how realistic you are being, and whether you are really reducing value and reward for the right reasons.

## [Everyday Risk Rating ](https://ahead.feedly.com/posts/everyday-risk-rating)

[https://ahead.feedly.com/posts/everyday-risk-rating](https://ahead.feedly.com/posts/everyday-risk-rating)

> One of my favorite pieces of trivia about the security industry is that the word security itself comes from the Latin se (without) and cura (worry). In other words, **security is all about creating a state where people can go about their lives or their businesses “without worry”. ** This is hard to do right now. We live in a moment where we feel surrounded by dangers, and when some of those dangers are more real than others, and the ability to know the difference is essential to maintaining a peaceful state. ** Security people, perhaps especially threat researchers, are especially sensitive to risks in the world. We see problems in everything, and we’re prone to over-index on the amount of real-word danger they pose.
> 
> [...]
> 
> ** This is a horrific collage of images from fatal car crashes. **
> Are cars safe?
> 
> What does safe even mean when collages like this are possible?
> 
> The answer has to come from understanding the two factors above: 1) how useful cars are to you, and 2) the data around fatal car crashes.
> 
> > There were 36,096 fatalities in motor vehicle traffic crashes in 2019. 36,000 fatalities per year. Is that a lot? A little? The odds of dying from a car crash is about 1 in 107 , which isn’t low, but cars are super useful and we accept the associated risks. **The bigger point is not that we’ve accepted the risk. It’s that we could—if we tried—make ourselves afraid to drive by over-exposing ourselves to evidence of fatal wrecks.** So, using that knowledge—should you let your kid walk to school or not? Should you start a public blog?
> 
> When you are confronted with such questions, and you find yourself having an emotional reaction to the risks, take the time to use the methodology above.
> 
> Make the list of things that could go wrong, and think about their chances. Sometimes this will convince you not to do something when you thought it was ok, but in many more cases you’re likely to realize the benefit outweighs the chances and/or impact of the downside. 


I’m not entirely convinced about the maths at play here, but there’s several good take-home messages.
The first is considering likelihood in terms of a specific timeframe (10 years in this case).  I’ve spent too much time poring over risk documents that articulate that some weird niche attack might have a 2/5 likelihood, the same as a fairly common everyday attack to not get frustrated when likelihood is an arbitrary value.  Instead focusing on likelihood within a fixed time period tends to make people make better decisions about likelihood.

The other is the reminder that when we spend all of our time reading articles about how organisations get compromised, we tend to forget all of the times that someone doesn’t get compromised.  The fact is that the vast majority of companies, big and small, are running outdated software pretty much all the time, and only a tiny tiny percentage of them end up compromised.  They run that risk successfully for a number of reasons, sometimes because of lack of awareness, but sometimes because they’ve chosen to emphasise the value of doing something else.

This article is a good reminder that risk is about proportions, but it also the need to determine what the context and payoff of taking that risk is. 


## [New Spring4Shell Zero-Day Vulnerability Confirmed: What it is and how to be prepared ](https://www.contrastsecurity.com/security-influencers/new-spring4shell-vulnerability-confirmed-what-it-is-and-how-to-be-prepared)

[https://www.contrastsecurity.com/security-influencers/new-spring4shell-vulnerability-confirmed-what-it-is-and-how-to-be-prepared](https://www.contrastsecurity.com/security-influencers/new-spring4shell-vulnerability-confirmed-what-it-is-and-how-to-be-prepared)

> As of Wednesday, March 30, the Contrast Security Labs team confirmed the 0-day vulnerability by use of a public poc , Spring4Shell, which could be the source of Remote Code Execution (RCE).
> 
> Spring translates the body and parameters of an HTTP request and turns them into a domain object for developers to use. This makes their lives easier.
> 
> In the process of building an object graph to give to the developer, Spring takes special care not to let attackers control any parts of the Class , ProtectionDomain , and ClassLoader of the instance being created. Unfortunately, changes to the Class object in Java 9 meant the checks Spring performed were no longer enough. 


This is a good write up of the Spring4Shell exploit, which has now been confirmed by Spring, and there’s a patch available.  

The chatter online seems to indicate that most of the exploits that people are seeing is security researchers scanning for vulnerable systems rather than actual attacks, but I’m sure there are some out there.  

This vulnerability will primarily affect you if you expose web services to the internet, or to users you don’t trust.  Also note that there was a second vulnerability released at about the same time that only affect SpringFunctions, which enables a Lambda Function As A Service style interface for Java apps.  Don’t get the two confused or mixed up, as I did when this first broke. 


## [NCSC-NL/spring4shell: Operational information regarding the Spring4Shell vulnerability in the Spring Core Framework ](https://github.com/NCSC-NL/spring4shell)

[https://github.com/NCSC-NL/spring4shell](https://github.com/NCSC-NL/spring4shell)

> **NCSC-NL has published a HIGH/HIGH advisory for the Spring4shell vulnerability. Normally we would update a HIGH/HIGH advisory for vulnerable software packages, however due to the expected number of updates we have created a list of known vulnerable software in the software directory.
> 
> Mitigation measures** Patches are available through Spring.io :
> • Spring Framework versions 5.3.18 and 5.2.20
> • Spring Boot versions 2.5.12 and 2.6.6
> • Tomcat versions 10.0.20, 9.0.62, and 8.5.78 


I don’t think this is a “The sky is falling” vulnerability, and the initial reporting definitely made this out to be far more serious than it is.

Kudos to the NCSC-NL, who have been doing some great stuff on vulnerabilities this year, but they have started listing other software that runs a SpringFramework web frontend of some form.  There’s quite a bit of network gear in there, which surprises me given how heavyweight java, tomcat and Spring is, even for an admin site.

It’s worth being aware that because this is something that affects a web frontend, it’s almost certainly only exploitable if someone can access the web interface, which for many systems means being on the management network, rather than externally facing.  That should lower the impact slightly, but as always, patch early and patch often. 


## [Use of Russian technology products and services following... - NCSC.GOV.UK ](https://www.ncsc.gov.uk/blog-post/use-of-russian-technology-products-services-following-invasion-ukraine)

[https://www.ncsc.gov.uk/blog-post/use-of-russian-technology-products-services-following-invasion-ukraine](https://www.ncsc.gov.uk/blog-post/use-of-russian-technology-products-services-following-invasion-ukraine)

> We can’t provide generic advice on how to evaluate risk, since it will be different for all organisations. Each will have to evaluate the potential damage to their enterprise if Russian-nexus products and services are suborned, but it would be prudent to err on the side of caution.
> • If you are more likely to be a target for the Russian state because of what’s going on, then it would be prudent to consider your reliance on all types of Russian technology products or services (including, but not limited to, cloud-enabled products such as AV).
> • If you use services that are provided out of Russia (including development and support services), then you should think about how you could insulate yourself from compromise or misuse of these services. This is true whether you contract directly with a Russian entity, or it just so happens that the people who work for a non-Russian company are located in Russia.
> You may choose to remove Russian products and services proactively, wait until your contract expires (or your next tech refresh), or do it in response to some geopolitical event. Alternatively, you may choose to live with the risk. **Whatever you choose, remember that cyber security, even in a time of global unrest, remains a balance of different risks** . Rushing to change a product that's deeply embedded in your enterprise could end up causing the very damage you're trying to prevent.
> Regardless of whether you’re a likely target, ongoing global sanctions could mean that Russian technology services (and support for products) may have to be stopped at a moment’s notice. This would bring a new set of risks. Enterprises should consider how such an event would affect their resilience, and consider plans for mitigation. 


This statement from NCSC sums up a whole world of cybersecurity advice.  We can’t provide generic advice because it’s different for all organisations.  But you also need to remember that rushing to remediate a potential risk might actually cause the thing you are trying to avoid. 


## [Conti Leaks: Examining the Panama Papers of Ransomware | Trellix ](https://www.trellix.com/en-gb/about/newsroom/stories/threat-labs/conti-leaks-examining-the-panama-papers-of-ransomware.html)

[https://www.trellix.com/en-gb/about/newsroom/stories/threat-labs/conti-leaks-examining-the-panama-papers-of-ransomware.html](https://www.trellix.com/en-gb/about/newsroom/stories/threat-labs/conti-leaks-examining-the-panama-papers-of-ransomware.html)

> It isn’t often the whole world gets an inside look of the business operations of a top tier cybercriminal group. Very early on in the Russian-Ukrainian Crisis the predominantly Russian based ransomware group Conti made a public statement where they expressed their loyalty to the Russian Administration.
> 
> As a reaction to this statement and the current conflict, a Ukrainian security researcher, operating by the twitter handle @contileaks decided to publish years of Conti’s internal Jabber conversations online. The chats that were dumped span across several years consisted of thousands of messages making this the “ **Panama Papers of Ransomware** ”.
> This wasn’t the first time the Conti gang got hit, last summer a **disgruntled affiliate posted** their attack playbook online, which was full of very useful intelligence for our customers.
> Since it was public, the whole security community jumped to review the chats and within hours the first findings appeared on Twitter. Trellix was also quick to obtain the dataset and realized that this might be one of the largest “crowd-sourced cyber investigations” ever seen. What this means is that as a research team you must devise a flexible dissemination strategy because findings by the crowd will appear online. So, it is constant balance between verification of the published findings by others, investing in your own research goals and adjusting some of these goals based on new information.
> Even though it was very tempting to dive down the rabbit hole immediately we did make sure we attacked the dataset with a certain plan. 


I’ve been waiting for someone to do a deep dive into the ContiLeaks.  I saw them go out, but the effort of translating them and digging through them seemed really high for an amateur, and I figured someone else would do all that hard work for me.  

This breakdown covers not just what they found, which is that Conti is a large enterprise with all the things you’d expect from that, but also talks a bit about how they planned looking through this trove, first emphasising finding live attack infrastructure and neutralising it before starting down the more prosaic background information.  Good work from the Trellix team here. 


## [WhatsApp in government | The Institute for Government ](https://www.instituteforgovernment.org.uk/publications/whatsapp-government)

[https://www.instituteforgovernment.org.uk/publications/whatsapp-government](https://www.instituteforgovernment.org.uk/publications/whatsapp-government)

> The government must address the inconsistent guidance – or in some cases no guidance at all – for how ministers, special advisers and civil servants use WhatsApp.
> 
> Banning WhatsApp in government is not practical – between 13% and 31% of officials in some departments have the app installed on their work phones – and it is an efficient way of communicating. However, the speed and accessibility of WhatsApp means decisions can be made too quickly without the full facts or without sufficient input from key individuals, and the practicalities of using WhatsApp in government have now gone unaddressed for too long,
> 
> This report calls for the prime minister to uphold guidance stating ministers, special advisers and officials should not use personal phones for substantive government business. This would reduce the risk of important information being lost and help prevent the blurring of boundaries between personal and government business that can – and has – raised questions about propriety and ethics.


One of the most interesting parts of this whole can of worms is that while campaigners are calling for Whatsapp to be banned, primarily because of the lack of transparency and tracability that these tools provide, Whatsapp doesn't really provide any feature that any other instant messaging client hasn't had for years.  I'm sure there are people sending each other messages via SMS or via any number of other instant messaging systems.  

Equally, reading the history books, you often find evidence of conversations and phone calls that aren't effectively minuted, or traced.  

This report however strikes a different tone to most of the others that I've read, in that it instead determines that the use of instant messaging is both ubiquitous and inevitable and instead of calling for it to be banned, focuses on recommendations for how it can be effectively managed and traced.

Of course, unless you work in regulated financial industries (which is the most similar to government in terms of regulating your chat messages), you probably don't need as much transparency and auditability as is laid out here.  But there are questions for security leaders in commercial organisations.  How much company business is conducted on personal phones, via Whatsapp, because it's simple and easy?   Do you have effective ways to monitor that, keep records and ensure that information doesn't flow to personal devices, or are you just hoping that it doesn't happen?  Embracing the technology and providing it in a managed and monitored way may well be the best way to ensure that your staff are staying secure.


## [Forcing WhatsApp and iMessage to Work Together Is Doomed to Fail | WIRED UK ](https://www.wired.co.uk/article/dma-interoperability-messaging-imessage-whatsapp)

[https://www.wired.co.uk/article/dma-interoperability-messaging-imessage-whatsapp](https://www.wired.co.uk/article/dma-interoperability-messaging-imessage-whatsapp)

> One of the biggest unanswered questions is how interoperability would ensure you are chatting with the people you think you are. People use different usernames on each platform, and not knowing who someone is could lead to identity issues, explains Alan Duric, cofounder of encrypted messaging app Wire. “If you’re communicating across Wire and WhatsApp, how can the Wire user be certain that the person they are talking to on WhatsApp is authentic?” he says. “How can they be sure the person they're talking to is even using WhatsApp at all?” Duric says this can be combated by verifying each user's identity, which can then help reduce abuse and spam.
> Those in favor of interoperability say the best way to do this would be for all companies to adopt one encryption standard and stick to it. These standards already exist—for instance, the Matrix messaging protocol , the XMPP standard, and the upcoming Messaging Layer Security . “If every player in the field—so the gatekeepers but also the smaller player—all connect to the same standard, it ends up being a big glue between the different services,” says Amandine Le Pape, a cofounder of the Matrix standard. This would avoid companies implementing APIs via a piecemeal process, although this isn’t what the European Union has opted for at the moment. “The DMA is just the first step,” Le Pape says.
> 
> Getting all messaging apps to use one standard would be a significant, time-consuming challenge. “Potentially, you could just have a situation where everyone switches to Matrix,” Kobeissi says. “But Matrix is a fundamentally different security architecture, not just from an end-to-end encryption perspective, but also from a threat modeling perspective.” Each app faces different potential attacks against it—based on its user base and operations—so moving to one model would require companies to reassess how their users could be compromised. 


This is really hard.  As the article points out, interoperability is almost certainly at odds with the privacy and security aims of some of these systems, and is likely to be impossible to resolve.

Firstly there’s the issues of the end to end encryption, which looks almost impossible over an interoperable standard, meaning that someone somewhere is going to need to decrypt and re-encrypt the communication, which will be a weakpoint.  

But this thing on identity is the bigger issue, especially when it comes to handling spam, harassment or abuse results.  The question isn’t just “How do I know that id X is user Y” but how reports of bad behaviour can be shared appropriately, how those operators can then track and act on those messages.  These are hard problems, and as evidenced by existing problems with spam, disinformation and abuse, already not a priority in the easy model of a closed social system for the big operators. 


## [Why Don't You Use ... ](https://www.brendangregg.com/blog/2022-03-19/why-dont-you-use.html)

[https://www.brendangregg.com/blog/2022-03-19/why-dont-you-use.html](https://www.brendangregg.com/blog/2022-03-19/why-dont-you-use.html)

> These are complicated and time consuming to explain properly, and it may not be a good use of engineering time. If you rushed a quick answer instead, you can put the company in a worse position than by saying nothing: that of providing a _weak_ explanation. Those vested in the technology will find it easy to attack your response – and have more time, energy, and interest in doing so – which can make your company look worse.
> I've found one of these reasons is common: Discovering that a product was built without subject matter expertise. I've seen startups that do nothing new and nothing well in a space that's crying for new or better solutions. I usually find out later that the development team has no prior domain experience. It's complicated to explain, even to the developer team, as they lack the background to best understand why they missed the mark.
> A common reason I've seen at smaller companies is when an internal solution is good enough. Adopting new technologies isn't "free": It takes (their limited) engineering time away from other projects, it adds technical debt, and it may add security risk (agents running as root). In this case, the other technology just doesn't have enough features or improved performance to justify a switch. 


There’s a whole bunch in here, and I’ve had many of the same conversations in the past.
Brendan mentions it in passing, but one of the big reasons that comes up quite a lot is that sometimes software isn’t aimed at larger organisations.  You might have the best performing database in the world, but if I can’t justify it to engineering management, work out how to operate it, debug it, and support it, then it’s not much use to me.  
Every tech choice implies a level of commitment in the organisation that I might not be able to afford over something we already use, even if the technology itself is better. 


## [Hardening Signal ](https://media.cert.europa.eu/static/WhitePapers/TLP-WHITE-CERT-EU_Security_Guidance-22-002_v1_0.pdf)

[https://media.cert.europa.eu/static/WhitePapers/TLP-WHITE-CERT-EU_Security_Guidance-22-002_v1_0.pdf](https://media.cert.europa.eu/static/WhitePapers/TLP-WHITE-CERT-EU_Security_Guidance-22-002_v1_0.pdf)

> Signal is a well-known, secure, encrypted instant messaging service developed by the non-profit
> Signal Technology Foundation and Signal Messenger LLC. It uses standard cellular telephone
> numbers as identifiers and all communications between Signal users are secured with end-toend encryption.
> 
> Staff of public and private organisations, including senior management, may be using Signal
> sometimes to quickly coordinate and exchange information on work-related matters. Signal
> groups may also have been set up for business continuity reasons in case corporate instant
> messaging tools become unavailable.
> 
> The following document provides clear and pragmatic recommendations for hardening the configuration of Signal apps.


This is a nice guide to hardening Signal use.  If you own and manage corporate devices, sadly much of this is not scriptable from a Mobile Device Management system, but you may well want to update your phone build and issuance policy to set some of these defaults before you hand the phone over to VIP’s, or ensure that first use walkthroughs include helping the user set some of these settings when they get issued their phone. 

The recommendations you should focus on are:

* Enable Registration Lock
* Make sure your account is only synchronised on devices you trust
* Activate the screen lock
* Enable notification privacy



## [It Was Easy to Hack a Billionaire - YouTube ](https://www.youtube.com/watch?v=7-lDRgxbU1Y)

[https://www.youtube.com/watch?v=7-lDRgxbU1Y](https://www.youtube.com/watch?v=7-lDRgxbU1Y)

> For most Americans, the following rings true: We’re aware there’s risk online, but we don’t know what to do about it. We have no idea how they get in, how to stop them or what they can find once they’ve made it into our digital lives. To raise awareness around the risk Americans face online and encourage people to take proactive steps to protect themselves from cybercrime, Aura decided to chronicle a hack from start-to-finish. And who better to hack than our billionaire investor, Jeffrey Katzenberg. 


This is a great example of using a recent vulnerability (from https://www.ryanpickren.com/safari-uxss ) to hack someone, combined with some OSINT to create a highly targeted attack.  This might be useful for executive training, as well as a reminder that the number 1 defence against almost all of these targeted attacks is patching. 


