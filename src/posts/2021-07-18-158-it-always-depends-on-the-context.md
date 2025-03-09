---
title: "158 - It always depends on the context"
date: 2021-07-18
description: "We can easily be the victim of binary thinking in cybersecurity and digital. "
permalink: /it-always-depends-on-the-context/
---

We can easily be the victim of binary thinking in cybersecurity and digital. 

You must have a CI/CD pipeline, you should always patch immediately, you must airgap your control network from your operational network.

One of the increasing problems with society in the west is the loss of the happy medium, and the agreement with those who disagree with us.  Politics, media and society for the last few daces has steadily sought and amplified the extreme opinions that create controversy, thus creating headlines, opinion pieces, column inches and most importantly, relevance and infamy.  It feels like we're losing the ability to disagree with one another sensibly, and growing to hate any bipartisan movements that seek to work on common problems, where neither side has a stake in the solution.  

The solution to this is to ensure that we reach out to those we disagree with and that we don't present false binaries to those around us.  Is a CISSP any good?  Are any infosec certifications any good?  Actually yes, there are lots of contexts where taking, learning and passing a CISSP is an incredibly valuable thing.  Where the learning provided to someone is engaging, useful, and demonstrates a clear understanding of the foundations.  There are also lots of situations where certifications are misused, where someone assumes that if you passed it, you must have some specific value, or know a certain thing. 

One of my colleagues once wrote an entire blogpost exhorting his infosec colleagues to stop responding to security questions with the answer "it depends".  Within the community I hang out with, it's become an in-joke, that saying "it depends" is a way of trying to get out of doing the hard work of giving an opinionated answer.  

But we also need to acknowledge that there is no "right way" of doing things, and that the answer someone needs will always depend on the context.

However, we need to strike a fine balance.  Within an expert community, discussing certain topics and deciding that it depends on the context is fine.  There are many situations in which patching a critical zero-day that is being exploited is the worst possible option to take.  But we need to accept that we should be responding to people who ask with the context appropriate advice for them.  Advice for an end user about whether or not they should use a password manager of "well... it depends" isn't useful or actionable.  But as the person being asked, you can respond with "this is why I think the right advice in your situation is X.  However, it might depend on the situation, so if I've misunderstood, do talk to me".

Of course, this doesn't make good blog posts, or even weekly newsletters.  We'd much rather have a set of talking heads with strong opinions stating that there's always a right way to do it.

## [Cybersecurity and the Curse of Binary Thinking](https://www.philvenables.com/post/cybersecurity-and-the-curse-of-binary-thinking)

[https://www.philvenables.com/post/cybersecurity-and-the-curse-of-binary-thinking](https://www.philvenables.com/post/cybersecurity-and-the-curse-of-binary-thinking)

> Working in information/cybersecurity and technology risk is a fascinating and challenging career, as I’ve covered here. There is, mostly, a great spirit of sharing and collaboration among security professionals. However, I’ve observed one disturbing and growing trend in the past few years that might be characterized as a curse of binary thinking. By this I mean the assertion that if something isn’t perfect then it must be terrible, or that if you don’t fully agree with something then you must therefore absolutely disagree with it. This lack of dealing with shades of gray or the ability to hold different views on topics at the same time is by no means confined to our discipline. This seems to have infected the public discourse on many topics. Here are some of the examples in our profession:


This is a good summation of some of the bigger binary statements that are constantly made in the security community


## [The Right Way to Ship Software | First Round Review](https://review.firstround.com/the-right-way-to-ship-software)

[https://review.firstround.com/the-right-way-to-ship-software](https://review.firstround.com/the-right-way-to-ship-software)

> You may find this framework particularly helpful if you struggle with multiple technologies or business models. A startup may very well need to support both web AND native mobile apps, or more than one set of customers (say, a two-sided marketplace with different apps for consumers and businesses). In an ideal world, your release process would just vary to match the product under development. But how you ship is not just process, it’s culture and identity. Swapping out a process is easy. Changing culture is hard. And it’s even harder for a small company to embrace different cultures for different teams.
> 
> If you find multiple “shipping cultures” in tension in your company, you’re dealing with one of the fundamentally hard execution challenges of building and shipping software. There are no easy answers when people stake out positions grounded on emotions rather than reason. On the plus side: your team’s emotions are engaged! It can be hard to remember that silver lining when the conflict is raging, but it is good news that your engineers care passionately about your company.
> 
> Take a deep breath and remind them that release processes come and go, but your company’s mission and values are immutable. Your team hopefully can agree that what ultimately matters is to ship the best product for your users, and that what remains is negotiable. With any luck, this framework will help you negotiate it.
> 
> 


This really gets to the heart of when context matters, and why context matters.  The way we write, test and release software is context dependant.

What this doesn't dive into is that problems that occur when someone tries to take a solution from one context and reapply it in another context.  Applying test matrices to CI/CD pipelines is going to cause you trouble because the underlying assumptions that ensure that test matrices are valuable are broken by a rapidly changing deployment pipeline.


## [Morpheus Turns a CPU Into a Rubik’s Cube to Defeat Hackers - IEEE Spectrum](https://spectrum.ieee.org/tech-talk/semiconductors/processors/morpheus-turns-a-cpu-into-a-rubiks-cube-to-defeat-hackers)

[https://spectrum.ieee.org/tech-talk/semiconductors/processors/morpheus-turns-a-cpu-into-a-rubiks-cube-to-defeat-hackers](https://spectrum.ieee.org/tech-talk/semiconductors/processors/morpheus-turns-a-cpu-into-a-rubiks-cube-to-defeat-hackers)

> Attackers need to know all that underlying stuff, because they need to use that knowledge to step around the defenses. It is the telltale sign of an attack that it is dipping into the implementation details of a system.
> 
> Spectrum: So you can detect an attack just by looking at what’s being looked at?
> 
> Todd Austin: Yeah. Let me give you a classic example—the return stack. [When a program “calls” a subroutine into action, it stores the address the program should return to when the subroutine is over in the return stack.] This is a real popular place for attackers to manipulate to do what’s called a buffer overflow or a code injection. There’s only one part of the program that writes and reads from the return address, and that’s the beginning of a function and the end of a function. That’s really the semantics of the return address. But when you see a program attacking the return address to do code injection, for example, you’ll see writes from many different places in the program. So, these sort of unexpected, undefined accesses, normal programs never do. That’s a tell-tale sign that there is an attack going on. Now, some systems might try to detect that. And when they detect that, then they can kill the program. But that’s problematic, too, because things like operating systems and device drivers do some of this stuff, too.
> 
> So what we do instead is to make the underlying implementation of the machine—the undefined semantics—change every few hundred milliseconds. 


This is a really interesting idea, a processor that actively defends against whole classes of attack by recognising what behaviour looks legitimate and what behaviour looks like an attacker


## [r/WallStreetBets Incident Anthology (What Worked Edition): Autoscaler : RedditEng](https://www.reddit.com/r/RedditEng/comments/o4ygp0/rwallstreetbets_incident_anthology_what_worked/)

[https://www.reddit.com/r/RedditEng/comments/o4ygp0/rwallstreetbets_incident_anthology_what_worked/](https://www.reddit.com/r/RedditEng/comments/o4ygp0/rwallstreetbets_incident_anthology_what_worked/)

> Managing and anticipating the traffic patterns for a platform like Reddit is not an easy task, nor is it an exact science. To deal with all this traffic you need servers, lots of them. There’s always a balance that you need to find when adjusting the number of servers behind a given service pool: if the server count is too low you’ll have outages and your users will be unhappy; if you have too many servers you’ll spend too much money, and then you can’t buy tendies.
> 
> We have a good idea of what our peak traffic would look like during a “normal” day. We also know that many fans will be tuning into r/nfl during SuperbOwl Sunday in the hopes that they’ll see Tom Brady blow a 25 point lead and meme about it. But traffic to Reddit is driven by the redditors, and we have no way to control or anticipate what will drive their attention. Maybe there will be some big news, or maybe half of Reddit will become very interested in the stock market all of a sudden. And then… that week happened (you know the one I’m talking about).
> 
> On the week of January 27th, a lot of eyes were suddenly focused on Reddit and r/WallStreetBets, with daily discussion threads stressing our backend, a big influx of new Redditors, and sharp traffic increases at times when we wouldn’t normally expect them. For instance, during a whole week open and close time for the stock market became a very important (and stressful!) time for us.


I love seeing the internals of big scalable internet systems, and reddits engineers have always, rather naturally, used reddit itself to cover incidents, post mortems and other interesting events.

If stonks to the moon means nothing to you, then this post might not either, but reddit has to deal with surprising scalability challenges and are quite open here on the benefit from paying back engineering debt, and the ability to learn and pivot rapidly to changing events.


## [SimuLand: Understand adversary tradecraft and improve detection strategies | Microsoft Security Blog](https://www.microsoft.com/security/blog/2021/05/20/simuland-understand-adversary-tradecraft-and-improve-detection-strategies/)

[https://www.microsoft.com/security/blog/2021/05/20/simuland-understand-adversary-tradecraft-and-improve-detection-strategies/](https://www.microsoft.com/security/blog/2021/05/20/simuland-understand-adversary-tradecraft-and-improve-detection-strategies/)

> SimuLand is an open-source initiative by Microsoft to help security researchers around the world deploy lab environments that reproduce well-known techniques used in real attack scenarios, actively test and verify the effectiveness of related Microsoft 365 Defender, Azure Defender, and Azure Sentinel detections, and extend threat research using telemetry and forensic artifacts generated after each simulation exercise.
> 
> These lab environments will provide use cases from a variety of data sources including telemetry from  Microsoft 365 Defender security products, Azure Defender, and other integrated data sources through Azure Sentinel data connectors.
> 
> The purpose behind SimuLand
> 
> As we build out the SimuLand framework and start populating lab environments, we will be working under the following basic principles:
> 
> * Understand the underlying behavior and functionality of adversary tradecraft.
> * Identify mitigations and attacker paths by documenting preconditions for each attacker action.
> * Expedite the design and deployment of threat research lab environments.
> * Stay up to date with the latest techniques and tools used by real threat actors.
> * Identify, document, and share relevant data sources to model and detect adversary actions.
> * Validate and tune detection capabilities.


This project gives a great insight into how you can simulate advanced threat actors in environments and test that against detection tools and scripts.

It looks like it'll be really useful for BlueTeams who are able to take the outputs of existing public or private red team reports, apply them and then start working out what detection models can be tuned that would help detect and prevent those attacks.


## [Deciduous: A Security Decision Tree Generator | Kelly Shortridge](https://swagitda.com/blog/posts/deciduous-attack-tree-app/)

[https://swagitda.com/blog/posts/deciduous-attack-tree-app/](https://swagitda.com/blog/posts/deciduous-attack-tree-app/)

> Security decision trees are a powerful tool to inform saner security prioritization when designing, building, and operating software systems. But creating them has largely involved highly manual tinkering, which is why it’s understandable that I’m constantly asked, “Is there an app that my team can use to create them?” I’m delighted that I now can say “fuck yes there is!” with the release of Deciduous, a security decision tree generator.
> 
> Inspired by the Security Chaos Engineering e-book and my previous blog post on creating security decision trees with Graphviz, one of my unindicted co-conspirators Ryan Petrich built a web app that handles all the annoying grunt work of building an attack tree. This lets you focus on the thinky thinky and typey typey around likely attacker actions, potential mitigations, and how attackers will respond to those mitigations as Deciduous dynamically generates an organized and styled1 graph for you.


This is a lovely tool for generating decision paths.  

Without any ability to conduct scoring, estimation or other features, it's a little light, but it certainly beats dragging boxes around on powerpoint, which is what I've done before now.


## [China Taking Control of Zero-Day Exploits - Schneier on Security](https://www.schneier.com/blog/archives/2021/07/china-taking-control-of-zero-day-exploits.html)

[https://www.schneier.com/blog/archives/2021/07/china-taking-control-of-zero-day-exploits.html](https://www.schneier.com/blog/archives/2021/07/china-taking-control-of-zero-day-exploits.html)

> China is making sure that all newly discovered zero-day exploits are disclosed to the government.
> 
> Under the new rules, anyone in China who finds a vulnerability must tell the government, which will decide what repairs to make. No information can be given to “overseas organizations or individuals” other than the product’s manufacturer.
> 
> No one may “collect, sell or publish information on network product security vulnerabilities,” say the rules issued by the Cyberspace Administration of China and the police and industry ministries.
> 
> This just blocks the cyber-arms trade. It doesn’t prevent researchers from telling the products’ companies, even if they are outside of China.


This is good analysis from Schneier here.  There's been a lot written about the new rules, but the reality boils down to 3 critical implications:

1. Chinese security researchers will be required to disclose to the Chinese government first, which will decide what to do with them.  Given the implication recently on their use of an iPhone exploit from the Tianfu Cup, that gives their internal government far greater access to research

2. Security researchers will be prevented from selling the exploits on the open market.  This rather neatly prevents other nation states and advanced actors from buying the capabilities and using them.  This will advance Chinese cybersecurity economic impact while allowing them to claim to be reducing the harmful zero-day market

3. Security researchers will still be able to report their findings back to the affected company.


## [Announcing the Google Workspace Provider for HashiCorp Terraform Tech Preview](https://www.hashicorp.com/blog/announcing-the-google-workspace-provider-for-hashicorp-terraform-tech-preview)

[https://www.hashicorp.com/blog/announcing-the-google-workspace-provider-for-hashicorp-terraform-tech-preview](https://www.hashicorp.com/blog/announcing-the-google-workspace-provider-for-hashicorp-terraform-tech-preview)

> The Google Workspace provider for Terraform allows you to manage domains, users, and groups in your Google Workspace. This provider is a technical preview, which means it's a community supported project and will require incremental testing and polishing to mature into a HashiCorp officially supported project.
> 
> This post will include use cases, requirements, configuration, and examples and show how to create your first user, your first group, and add a user to the group.


I am a huge fan of user definitons via code, not only for the situation where you want to maintain a user database in code, but also as an intermediary language.  This power means that you can can keep users, groups and ACL's in any tool, and export the data to terraform code and use this backend to push duplicates to Google Workspace.  That makes keeping data in sync between different systems easy, as well as providing you with something you can run validators on.

Imagine having this all defined in code and being able to run tests against it to guarantee that two-person rules are enforced, that nobody with access to the customer database also has access to the keystore or whatever rules you think should be in place.


## [GitHub - ukncsc/Device-Security-Guidance-Configuration-Packs: This repository contains policy packs which can be used by system management software to configure device platforms (such as Windows 10 and iOS) in accordance with NCSC device security guidance. These configurations are aimed primarily at government and other medium/large organisations.](https://github.com/ukncsc/Device-Security-Guidance-Configuration-Packs#google-workspace)

[https://github.com/ukncsc/Device-Security-Guidance-Configuration-Packs#google-workspace](https://github.com/ukncsc/Device-Security-Guidance-Configuration-Packs#google-workspace)

> These policies contain the NCSC’s recommended settings for the deployment of new devices across your enterprise estate. The NCSC does not mandate the use of these policies, or even require that they are used exactly as provided.
> 
> These setting are offered as guidance, so it is up to you how you implement and use them. In any case, they can provide a starting point for developing a compliance benchmark, or to expedite the configuration of devices to meet our recommendations.
> 
> Guiding principles
> 
> These three principles have guided the settings encapsulated in the policies.
> 
> * Balance Security and Usability: "Security for security's sake" is not the motto for these policies and settings. The aim is to keep a balance between security and usability. While each setting will have an underlying security purpose, it is perfectly reasonable for you to choose differently in your deployment.
> * Counter threats at OFFICIAL: The policies provided in this repository aim to help organisations counter "commodity threats". This means those within the UK Government's OFFICIAL Threat Model. Despite this, they can provide a starting point for considering how to configure devices that you need to protect against higher capability threat actors and the associated risks.
> * Applicable to the UK: This guidance primarily targets UK government organisations, and UK businesses. If you would like installation instructions for device management software not covered in the installation section, please submit a request via Issues, using the required template, including details on how the product is being used in the UK.


These policies are a brilliant start to locking down the end user devices on your network.  With example policies for most major operating systems, you can import these into your "mobile Device Management" tool of choice, and apply those policies across your estate.

Of course, you shouldn't just do that.  As the guidance here says, you should get your security team to read through them, workshop them and divide your userbase into a number of key user types, and then deploy rules to users where it makes the most sense and has the least impact on usability.


## [FFUF.me](http://ffuf.me/about)

[http://ffuf.me/about](http://ffuf.me/about)

> FFUF.Me is a live playground to practice and improve your ffuf usage
> 
> you can run this application in 3 different places:
> 
> https://ffuf.me
> 
> Run your requests against our live infrastructure
> 
> Locally
> 
> Download the source code from https://github.com/adamtlangley/ffufme and run in a docker container.


This is a cute demonstration website that has web pages that are hidden through obscurity.  Using the FFuF tool, you can fuzz a websites address and directories to see what's there.  But using these tools effectively isn't always obvious, so a target range to practice against is quite nice.


