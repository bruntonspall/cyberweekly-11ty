---
title: "239 - How do we learn technical skills?"
date: 2024-02-11
description: "My background is long and deeply nerdy."
permalink: /how-do-we-learn-technical-skills/
---

My background is long and deeply nerdy.

When I was a teenager, all I wanted to do was make computer games.  A close friend and I spent hours on the internet reading tutorials on how to program video graphic with snippets of assembly code embedded in Pascal.  We wrote incredibly simple games, like a version of breakout, maze games and simplistic clones of other popular games.  I taught myself C programming, despite not understanding all the details, but online tutorials gave me a good enough base to work from.   After university I got my first job, writing software of slot machines, poker tables, blackjack tables and various other gambling systems.  This required a good in depth understanding of networking, as well as my self-taught C skills.

Over the next 15 years, I wrote software, built systems, secured systems and moved into cybersecurity.

That background in technology gives me a strong insight into how the underlying networks work, how the computers work and ensure that when looking at cybersecurity, I can do so with a deep technical background.  But that education is freely available for a lot of people these days.  There are some fabulous examples of technical education online that can give you a really good and thorough understanding of things like networking, CRTD's or the maths behind distributed systems.

## [Beej's Guide to Networking Concepts ](https://beej.us/guide/bgnet0/)

[https://beej.us/guide/bgnet0/](https://beej.us/guide/bgnet0/)

> **Beej's Guide to Networking Concepts** 
> 
> This is barely a book. It's stuff that I put together for class and used to have in Canvas, and then slammed together into a volume. I'll improve it over time, but it's kind of just dumped here for now. Forgive me. 


Beej’s original guide to networking in C is how I learned a lot about how networks work, how to write networking code and it’s really helped my career over time.

So to discover that he has written an updated guide that’s deliberately covering the higher level concepts and now is using Python as a language makes me so happy.  Obviously, I’ve not had time to read the entire thing, but the bits I’ve read look good already.

via [lobste.rs](https://lobste.rs/s/ehewh7/beej_s_guide_networking_concepts) 


## [An Interactive Intro to CRDTs | jakelazaroff.com ](https://jakelazaroff.com/words/an-interactive-intro-to-crdts/)

[https://jakelazaroff.com/words/an-interactive-intro-to-crdts/](https://jakelazaroff.com/words/an-interactive-intro-to-crdts/)

> Have you heard about CRDTs and wondered what they are? Maybe you’ve looked into them a bit, but ran into a wall of academic papers and math jargon? That was me before I started my [Recurse Center](https://www.recurse.com/) batch. But I’ve spent the past month or so doing research and writing code, and it turns out that you can build a lot with just a few simple things!
> 
> In this two-part series, we’ll learn what a CRDT is. Then we’ll write a primitive CRDT, compose it into more complex data structures, and finally use what we’ve learned to build a collaborative pixel art editor. All of this assumes no prior knowledge about CRDTs, and only a rudimentary knowledge of TypeScript. 


I love a good interactive tutorial that shows how things work.  CRDT’s is one of those things that I know about, but didn’t really understand, and this does a great job of explaining how they work 


## [The separation of work and play - by Rob Picard ](https://essays.observa.com/p/work-and-play)

[https://essays.observa.com/p/work-and-play](https://essays.observa.com/p/work-and-play)

> **Personal GitHub in work organizations** 
> 
> When a new employee joins an organization that uses GitHub, it is common for them to have their personal GitHub account added to the organization’s account. It is less common for them to create a new GitHub account dedicated to that particular company. GitHub recommends that people have one account used for both personal and work contexts [2](https://essays.observa.com/p/work-and-play#footnote-2-141279734) . 
> 
> **Bad passwords and SMS MFA** 
> 
> Any account that requires a password is liable to have an insecure password. Password reuse is common, and old passwords are often leaked in major data breaches [3](https://essays.observa.com/p/work-and-play#footnote-3-141279734) .
> 
> […]
> 
> You can also authenticate to GitHub with SSH keys. Each user has the ability to create as many SSH keys as they’d like. It’s common practice to create one per device.
> 
> The upshot here is that personal GitHub accounts have many SSH keys, including on old servers and devices that are long forgotten. It can even include servers and devices from previous employers. When this account is granted access to your organization, those keys all have access now too, with no second factor.
> 
> Requiring employees to create separate accounts for work ensures that you're starting from a clean slate and you won't have this long tail of SSH keys being granted access to your organization. 


Some really good points in here generally, but this argument around github accounts makes a lot of sense.  

Developers love to keep their github account, as it helps show their contributions over their career.  

The article points out that there are some controls that can reduce this, but that most of the controls are locked behind Githubs enterprise plan 


## [secengjeff/awskillswitch: Lambda function that streamlines containment of an AWS account compromise ](https://github.com/secengjeff/awskillswitch)

[https://github.com/secengjeff/awskillswitch](https://github.com/secengjeff/awskillswitch)

> AWS Kill Switch is a Lambda function (and proof of concept client) that an organization can implement in a dedicated "Security" account to give their security engineers the ability to quickly deploy restrictions during a security incident, including:
> 
> * Apply a service control policy (SCP) to freeze the state of a targeted account
> * Detach all policies and delete inline policies from a targeted IAM role
> * Revoke all sessions on a targeted IAM role or `ALL` customer managed IAM roles in a targeted account
> * Delete a targeted IAM role (which also revokes all sessions) 


What a lovely tool and idea.  When you have an incident, lets make it a small one rather than a big one, and rapid response in reducing the blast radius is the key to that. 


## [The balance has shifted away from SPAs ](https://nolanlawson.com/2022/05/21/the-balance-has-shifted-away-from-spas/)

[https://nolanlawson.com/2022/05/21/the-balance-has-shifted-away-from-spas/](https://nolanlawson.com/2022/05/21/the-balance-has-shifted-away-from-spas/)

> There’s a feeling in the air. A zeitgeist. SPAs are no longer the cool kids they once were 10 years ago.
> Hip new frameworks like Astro , Qwik , and Elder.js are touting their MPA capabilities with “0kB JavaScript by default.” Blog posts are making the rounds listing all the challenges with SPAs: history, focus management, scroll restoration, Cmd/Ctrl-click, memory leaks, etc. Gleeful potshots are being taken against SPAs.
> I think what’s less discussed, though, is how the context has changed in recent years to give MPAs more of an upper hand against SPAs. 


As some who has been doing web development for around 20 years now, the rise of the Single Page Application was. Softly mystifying.  It’s nice to see the web dev community start to see the benefits of a more traditional architecture with Multi Page Applications (otherwise known as Server Side Rendering ). 


## [Google's Gemini Advanced: Tasting Notes and Implications ](https://www.oneusefulthing.org/p/google-gemini-advanced-tasting-notes)

[https://www.oneusefulthing.org/p/google-gemini-advanced-tasting-notes](https://www.oneusefulthing.org/p/google-gemini-advanced-tasting-notes)

> At the same time, Gemini Advanced [does not obviously blow away GPT-4](https://www.microsoft.com/en-us/research/blog/steering-at-the-frontier-extending-the-power-of-prompting/) [1](https://www.oneusefulthing.org/p/google-gemini-advanced-tasting-notes#footnote-1-140794140) in the benchmarks. It is really good (more rigorous testing will be needed to figure out how good), but I would concur with the tests that suggest it is roughly equivalent, though it has its own strengths and weaknesses. GPT-4 is much more sophisticated about using code and accomplishes a number of hard verbal tasks better - it writes a better sestina and passes the Apple Test. Gemini is better at explanations and does a great job integrating images and search. Both are weird and inconsistent and hallucinate more than you would like.
> 
> […]
> 
> No one has a great definition for sentience, which is okay because LLMs are in no way sentient; they are software systems designed to create human-like language. But there is a weirdness to GPT-4 that isn’t sentience, but also isn’t like talking to a program. A weirdness only comes out after you spend enough hours playing with the AI and getting unnerved, or delighted, or both, by its unexpected abilities and seeming intelligence. There was a famous, controversial paper put out by Microsoft Research soon after the release of GPT-4, called “ [Sparks of Artificial General Intelligence](https://arxiv.org/abs/2303.12712) ” that tried to put this argument into scientific terms, but ended up just calling it “sparks” of artificial general intelligence. It is the illusion of a person on the other end of the line, even though there is nobody there. GPT-4 is full of ghosts.
> 
> Gemini is also full of ghosts.
> 
> Seriously, if you use the system for a while, I can almost guarantee at least one moment when you stand up from your desk, walk around the room, and wonder what is going on. […]
> 
> This means something important, I think, which is that the “sparks” of GPT-4 are not an isolated phenomenon, but rather may represent an emergent property of GPT-4 class models. When an AI model is large enough, you can get ghosts. 


Interesting notes on Google’s Gemini LLM model, the latest release of the AI LLM previously known as Bard.  

Mostly it seems to suggest that theres a class of emergent properties that we can likely expect all models that are trained this large to demonstrate, and that’s useful for us to start understanding the differences between different models and making better choices about how we use and engage with AI models 


## [“Wherever you get your podcasts” is a radical statement - Anil Dash ](https://www.anildash.com/2024/02/06/wherever-you-get-podcasts/)

[https://www.anildash.com/2024/02/06/wherever-you-get-podcasts/](https://www.anildash.com/2024/02/06/wherever-you-get-podcasts/)

> And of course, the winner-takes-all world of media being consumed by tech means that the economics of individual podcast production are often brutal now, sometimes simply _because_ creators can't rely on outsourcing advertising sales to one of the big platforms. An open system isn't a panacea for all that's broken in the media ecosystem.
> 
> But what we can take away from hearing "wherever you find podcasts" at the end of every episode we listen to is that, sometimes without us knowing, radical systems can survive and even thrive in the modern world of tech and media. They can inspire new creators to make similar systems that are unowned, uncentralized, and a little bit uncontrollable. And in this era where we're seeing [the renaissance of the open web](https://www.anildash.com/2024/01/03/human-web-renaissance/) , they point the way toward a future where we can use the same tone to say "wherever you find news" or "wherever you find your friends online", and know that it means that there's a way that our lives online could be fully in our own control. 


Lovely essay from Anil Dash on the rise of open and federated protocols and how they can work.

This one hit home to me, as I’ve just switched podcast client to one that syncs to my car, and it was really simple and easy to find and add my favourite podcasts into a new client, go find the episode I last listened to and it was pretty seamless to transition client. 


## [The Dangers of Default: Cybersecurity in the Age of Intent-Based Configuration | Tripwire ](https://www.tripwire.com/state-of-security/dangers-default-cybersecurity-age-intent-based-configuration)

[https://www.tripwire.com/state-of-security/dangers-default-cybersecurity-age-intent-based-configuration](https://www.tripwire.com/state-of-security/dangers-default-cybersecurity-age-intent-based-configuration)

> When you deploy software, set up a new router, create a new account, or do many other tasks, you are inevitably given a username and password. These are defined as "default" settings. More recently, they have countered the default credentials, which are the same across all routers, by creating new usernames and passwords using an algorithm configuring the routers en masse during the production phase. However, this is still the default because the ability for that algorithm or the process to be compromised means it will inevitably affect your infrastructure and organisation.
> 
> The Cybersecurity & Infrastructure Security Agency ( [CISA](https://www.cisa.gov/news-events/alerts/2013/06/24/risks-default-passwords-internet) ) provides context and guidance on why and how to go about ensuring that you do not run afoul on the default factory configuration vulnerabilities.
> 
> As an example, a recent attack against some Programmable Logic Controllers (PLCs) demonstrates why default configurations are so dangerous. The [attack](https://www.bleepingcomputer.com/news/security/hackers-breach-us-water-facility-via-exposed-unitronics-plcs/) itself allowed the exploitation of vulnerable PLCs, which are used in the OT space in industries such as food manufacturing, chemical production, and water processing plants. The exploitation of the default password and network ports on the PLCs – and their exposure to the internet – created the perfect opportunity for compromise. These PLCs and related controllers are often exposed to outside internet connectivity due to the remote nature of their intended functionalities. Something as trivial as defacing the controllers' user interface rendered the PLCs inoperative. With this type of access, deeper device and network-level access were made available, with potentially more profound cyber-physical effects on processes and equipment.
> 
> To expand this idea, the default configuration is just as bad as a default password. 


Post that articulates much of the same thing I’ve been saying for some time.  Our defaults need to be secure out of the box, because far too many people either wont change them, or wont understand the security implications when they do change them. 


## [Ivanti Patches High-Severity Vulnerability in VPN Appliances - SecurityWeek ](https://www.securityweek.com/ivanti-patches-high-severity-vulnerability-in-vpn-appliances/)

[https://www.securityweek.com/ivanti-patches-high-severity-vulnerability-in-vpn-appliances/](https://www.securityweek.com/ivanti-patches-high-severity-vulnerability-in-vpn-appliances/)

> Ivanti on Thursday announced patches for a high-severity vulnerability impacting enterprise VPN and network access products.
> 
> Tracked as CVE-2024-22024 (CVSS score of 8.3) and described as an XML external entity (XXE) issue, the security defect was identified in the SAML component of Ivanti Connect Secure, Policy Secure, and ZTA gateway appliances.
> 
> According to Ivanti, the successful exploitation of the bug could allow an unauthenticated attacker to access certain restricted resources. 


Note that this is a different Ivanti bug and patch to CVE-2024-22024 from last week.  You should patch this one as well, as even though they say that there’s no evidence of it being exploited, given the number of eyes on Ivanti products over the last few weeks, I’d expect researchers to reverse engineer and develop exploits for this fast 


## [Fortinet Warns of Zero Day in FortiOS | Decipher ](https://duo.com/decipher/fortinet-warns-of-zero-day-in-fortios)

[https://duo.com/decipher/fortinet-warns-of-zero-day-in-fortios](https://duo.com/decipher/fortinet-warns-of-zero-day-in-fortios)

> The vulnerability (CVE-2024-21762) is an out-of-bounds write in the sslvpnd component of the software, and it affects FortiOS 6.0, 6.2, 6.4, 7.0, 7.2, and 7.4. Fortinet released an advisory warning of the vulnerability on Thursday and urged customers to upgrade to the latest versions as soon as possible.
> 
> “A out-of-bounds write vulnerability in FortiOS may allow a remote unauthenticated attacker to execute arbitrary code or command via specially crafted HTTP requests,” the [advisory](https://www.fortiguard.com/psirt/FG-IR-24-015) says.
> 
> Fortinet did not provide any details on the ongoing exploitation or specify which actors may be exploiting the vulnerability. 


As you’ve just finished patching your Ivanti VPN’s, now is the time to ensure that your Fortinet VPN’s are patched as well.

And as a reminder, your VPN appliances should be at the very top of your patching lists, and you should ensure that you have the capability to find, manage and patch all of them easily, quickly and efficiently. 


