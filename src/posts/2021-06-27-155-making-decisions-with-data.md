---
title: "155 - Making decisions with data"
date: 2021-06-27
description: "It's easy to say that if you had more data then you'd be able to make better decisions."
permalink: /making-decisions-with-data/
---

It's easy to say that if you had more data then you'd be able to make better decisions.

The reality is that most of us have access to more data at our fingertips than is even imaginable just a decade or so ago, and it's getting easier and easier to bring that data to the decision makers.

What's always been hard and remains hard is working out how to filter, process and understand that data at the right levels of abstraction to make effective and timely decisions.

Data science is a cool term at the moment, and has been for a number of years now.  We see more and more teams pulling togehter disparate datasets and building "dashboards" that can be put in front of senior leaders.  But sometimes that data is out of date, inaccurate, or tells you the wrong thing.

Our data awareness and familiarity needs to extend not just to making prettier graphs, but actually determining what questions we want to ask, and ensuring that the data is appropriately timely, accurate and at the right level to find the answers to those questions.  This is easy to say, but wicked hard to actually do in many organisations.  Collecting data is never high up in a teams priority list and ensuring that it's accurate and timely requires effort, requires management support and requires attention being paid.  If your VP's, SCS or executives are making decisions based on data from the front line, then you need to be sure that the people on the front line know how important that data is.

This is a developer heavy edition this week, as I've been looking again at the code that underlies the CyberWeekly platform, and that leads me to reading about what makes codebases great.  Many of these tips are ones that I wish I'd followed when I started, as they would make life a lot easier 3 years down the line when I start looking at code.  Since it's a single person project, I can't even wonder aloud "Who even wrote this!", because I already know the answer.  3 years ago me, you suck.

## [What I've learned about data recently | Seldo.com](https://seldo.com/posts/what-i-ve-learned-about-data-recently)

[https://seldo.com/posts/what-i-ve-learned-about-data-recently](https://seldo.com/posts/what-i-ve-learned-about-data-recently)

> Learning 1: you want engineers, not scientists
> 
> I learned this one before I was even hired at Netlify. While deciding about my next career step, I interviewed at a bunch of companies who were doing data-related things. Some were very sophisticated in how they handled data, but they were a minority. There was one pattern in particular I saw repeated over and over: a fast growing company would say "wow, we have all this data, we should do something with it". Then they would go out and hire a Data Scientist, ideally with a PhD, as their very first data hire. 
> 
> [...]
> 
> This is a mistake. Firstly, the term "Data Scientist" is over-used to the point of being meaningless. To me, a data scientist is an academic with very advanced degrees. They advance the state of the art in modeling, they solve novel problems in machine learning. They write white papers in journals. This is not what you need. Unless "we solve a new problem in machine learning" is what your company was founded to do, this is not what you need done. What you need is a data engineer.
> 
> The problem you actually have is: "we are generating a ton of data, but we have no idea what's going on". 


This is worth a read in a world where data science is in ascendance.  

This is true in lots of places where I've looked at data science, what they actually want and need is better data engineering.  The issues they have are normally about "how do I collect the data consistently", "how can I get it to where it needs to be" and "can I present this to a non data- audience".  None of these require advanced scientific backgrounds or even strong statistical skills.  What they need is strong engineering skills in how to gather, manage and represent data.

I'll note that I've worked with a number of people over the years with the title "data scientist" or "data journalist", and the best have those skills.  But with the rise in "cool factor" for data science comes the rise in people who do not have the requisite skills to make the role valuable.


## [The UK’s procurement system & judicial review: a cold deadly monster - Dominic Cummings substack](https://dominiccummings.substack.com/p/the-uks-procurement-system-and-judicial)

[https://dominiccummings.substack.com/p/the-uks-procurement-system-and-judicial](https://dominiccummings.substack.com/p/the-uks-procurement-system-and-judicial)

> At meetings in the days before and after I sent this email, the government’s data system for taking key decisions consisted of me dragging a white board into the Cabinet room and listening while people read out hospital numbers from scraps of paper, writing the numbers on the whiteboard, then hitting x2 x2 x2 on my iPhone and scribbling new numbers and saying to the room — so in X days, Y will be dead, in Z days the NHS is overwhelmed.
> 
> A picture from the time: this whiteboard, scribbled by me, was used in the meeting at ~1700 on Sunday 15 March where I tried to formalise the shift to Plan B. This is the day after the ‘Goldblum’ meeting at which the Warner brothers explained to the PM that Plan A (herd immunity by September) would kill hundreds of thousands and we must shift to Plan B (see earlier piece and my testimony to MPs). I spoke to Vallance that afternoon and before the meeting on Sunday 15th. He agreed on the shift. This whiteboard table was the ‘data system’ for the apex of power in UK handling covid in the crucial weeks of March!
> 
> I drew pictures like this every morning because a) there was no proper dashboard at this time, b) it’s hard for people to hold a lot of spoken numbers in their heads, c) many including the PM really struggled to understand the extreme effect of something doubling every 2-3 days (COBR documents from the time wrongly had doubling time of 5-7 days). The idea that 50 cases in London hospitals today meant *the NHS being totally overwhelmed in a few weeks* was hard for many to grasp, partly because confusing graphs showing a theoretical peak in June were in all the COBR slides.


Cummings is a marmite figure for a bunch of reasons, and if you can escape the political point scoring in here, there's something interesting in all of this.

Dominic seems to argue here that his use of a whiteboard was because the data system in Government was completely broken.  And I don't disagree that the people in that system are likely underskilled, under-equiped and under-empowered to do the sorts of things that DC wants from the system.

But I've also seen data systems get massively complex and difficult to use, with constantly changing data and constantly changing engineering underneath.  As a self-proclaimed techno-phile, DC wants a computer system to make this automated, as do many technologists, but we need to acknowledge that sometimes the simple thing forces us to simplify and make things understandable.

In the face of a crisis, whether a national crisis, security response or even a systems outage, one of the most valuable tools you can have is a whiteboard and a person responsible for updating it, ideally in a fixed, known and understandable manner.

This ensures that data coming in is being presented on the basis of "how will it be used", which prevents people from drowning in raw data and unable to assess the information.  But additionally, it ensures that there is a single source of information, that everyone is looking at it, and that everyone knows how it gets updated.

I don't disagree that it would be great if there was a better systemic way of organising and conducting this on a national pandemic level, but even if there we're, what I'd expect to see is that departmental heads or the crises facility probably doing the same thing DC was doing here, getting the numbers, interpreting them, putting them on a whiteboard and then sharing them.


## [Microsoft admits to signing rootkit malware in supply-chain fiasco](https://www.bleepingcomputer.com/news/security/microsoft-admits-to-signing-rootkit-malware-in-supply-chain-fiasco/)

[https://www.bleepingcomputer.com/news/security/microsoft-admits-to-signing-rootkit-malware-in-supply-chain-fiasco/](https://www.bleepingcomputer.com/news/security/microsoft-admits-to-signing-rootkit-malware-in-supply-chain-fiasco/)

> The mishap seems to have resulted from the threat actor following Microsoft's process to submit the malicious Netfilter drivers, and managing to acquire the Microsoft-signed binary in a legitimate manner:
> 
> "Microsoft is investigating a malicious actor distributing malicious drivers within gaming environments."
> 
> "The actor submitted drivers for certification through the Windows Hardware Compatibility Program. The drivers were built by a third party."
> 
> "We have suspended the account and reviewed their submissions for additional signs of malware," said Microsoft yesterday.
> 
> According to Microsoft, the threat actor has mainly targeted the gaming sector specifically in China with these malicious drivers, and there is no indication of enterprise environments having been affected so far.


This is an interesting trust issue.  

Microsoft's HCL process is designed to validate that a hardware supplier is able to build a driver that wont crash on one of the many many windows configurations out there.  It's designed to validate that the code works, that it won't call undocumented API's and so on.  It's not designed as a security check.

But of course, a DLL that is signed by Microsoft feels like there's a badge of authenticity around it which implies that it's not malware or hostile.  This is a repeat of the same pattern of apps being distributed on the Apple or Android app store, and the user trust engendered there within.

You can find indicators and breakdown of the malware itself at the [GData blog post](https://www.gdatasoftware.com/blog/microsoft-signed-a-malicious-netfilter-rootkit)


## [EU to launch rapid response cybersecurity team – POLITICO](https://www.politico.eu/article/eu-joint-cyber-unit-rapid-response-cyberattacks/)

[https://www.politico.eu/article/eu-joint-cyber-unit-rapid-response-cyberattacks/](https://www.politico.eu/article/eu-joint-cyber-unit-rapid-response-cyberattacks/)

> The European Commission will present its plan on Wednesday to set up what it calls the "Joint Cyber Unit," which would allow national capitals hit by cyberattacks to ask for help from other countries and the EU, including through rapid response teams that can swoop in and fight off hackers in real time, according to the draft.
> 
> A spate of cyberattacks have wreaked havoc on the Continent, leading to concerns that Europe cannot defend itself or its trade secrets against adversaries. The EU's plan aims to help countries fight back against increasingly sophisticated and brash attacks by pooling national governments' cybersecurity powers.
> 
> The plan would also set up a platform for cybercrime police, cyber agencies, diplomats, military services and cybersecurity firms to coordinate responses and share resources. And it would prepare regular threat reports, prepare and test crisis response plans and set up information-sharing agreements between authorities and private cybersecurity firms.
> 
> The Commission first promised to set up a Joint Cyber Unit in 2019 to stop the cyberattacks that have compromised EU institutions, agencies, national ministries and departments, and leading European companies and organizations.
> 
> But the plan took many months to finalize because the EU doesn't have competence over national security, and EU countries have been hesitant to give away control over it.


Ignoring the completely foolish idea of "fighting off hackers in real time", I'm in favour of the ability for European institutions to share detective indicators and threat intelligence, as well as a shared response team who can help respond when compromise is detected.


## [D3FEND Matrix | MITRE D3FEND(TM)](https://d3fend.mitre.org)

[https://d3fend.mitre.org](https://d3fend.mitre.org)

> A knowledge graph of cybersecurity countermeasures


(Joel) You may have heard of the [MITRE ATT&CK framework](https://attack.mitre.org) which is a "knowledge base of adversary tactics and techniques based on real-world observations".

D3FEND is "version 0.9 beta", and takes the offensive model (ATT&CK) and the digital artefacts to describe a defensive model. Very useful, and something to keep an eye on and share to your red/blue and security architecture teams.


## [Google Online Security Blog: Introducing SLSA, an End-to-End Framework for Supply Chain Integrity](https://security.googleblog.com/2021/06/introducing-slsa-end-to-end-framework.html)

[https://security.googleblog.com/2021/06/introducing-slsa-end-to-end-framework.html](https://security.googleblog.com/2021/06/introducing-slsa-end-to-end-framework.html)

> In its current state, SLSA is a set of incrementally adoptable security guidelines being established by industry consensus. In its final form, SLSA will differ from a list of best practices in its enforceability: it will support the automatic creation of auditable metadata that can be fed into policy engines to give "SLSA certification" to a particular package or build platform. SLSA is designed to be incremental and actionable, and to provide security benefits at every step. Once an artifact qualifies at the highest level, consumers can have confidence that it has not been tampered with and can be securely traced back to source—something that is difficult, if not impossible, to do with most software today.


These are some good guidelines for improving your supply chain.

Right now, there's no easy way to formally certify many of these, but if you are looking at improving or assessing your supply chain in 2021, then this should work as a good hitlist of where to focus.


## [Sensemaking: Django for Startup Founders: A better software architecture for SaaS startups and consumer apps](https://alexkrupp.typepad.com/sensemaking/2021/06/django-for-startup-founders-a-better-software-architecture-for-saas-startups-and-consumer-apps.html)

[https://alexkrupp.typepad.com/sensemaking/2021/06/django-for-startup-founders-a-better-software-architecture-for-saas-startups-and-consumer-apps.html](https://alexkrupp.typepad.com/sensemaking/2021/06/django-for-startup-founders-a-better-software-architecture-for-saas-startups-and-consumer-apps.html)

> Over the last couple decades we've seen the majority of companies switch to using Agile and other project management methodologies that not only take these shifting contexts into account, but are entirely designed around them. What we haven't seen though, at least not to nearly the same extent, is the same level of thought being put into architecting the software itself. That is, in the same way that Agile is designed around the assumption that both a product team's priorities and its development velocity can — and likely will — change wildly, likewise the design patterns we use when creating software should be chosen to ensure that:
> 
> * The engineering team isn't ever the limiting factor, even during periods of explosive growth.
> * The business can not only keep the lights on, but can continue moving forward even if it's down to its last (junior) developer.
> 
> I wrote this guide to explain how to write software in a way that maximizes the number of chances your startup has to succeed — by making it easy to maintain development velocity regardless of the inevitable-but-unknowable future changes to team size, developer competence and experience, product functionality, etc. The idea is that, given the inherent uncertainty, startups can massively increase their odds of success by putting some basic systems in place to help maximize the number of ideas, features, and hypotheses they can test; in other words, maximizing "lead bullets," to borrow the phrase from this blog post by Ben Horowitz. What follows are a series of patterns and best practices for building REST APIs, designed especially for the needs of SaaS startups and consumer apps.
> 
> It's very important to understand how each technical recommendation will confer real-world benefits to your business, and the best way to do this is by discussing them in the context of the so-called ilities. In software architecture, the ilities are the words we use to describe the characteristics of the codebase itself, unrelated to what that code is actually doing for the end user. Most existing advice on software architecture is written for $10B+ companies, and as such tends to focus on maximizing things like performance, scalability, availability, reliability, etc.
> 
> This has actually created a huge problem. The issue is that, due to having studied CS in college, most engineers working at startups don't have a ton of business training. So what often happens is that these developers decide how to implement features by just copying the first recommendation that comes up in Google or Stack Overflow without first evaluating that advice from a business perspective, and since most of this advice is geared toward either Fortune 500 companies (at one extreme) or hackathon-type hobby projects (at the other), this inevitably leads to huge unseen costs.
> 
> So how should developers and managers be making decisions instead? Basically the way to consistently make good architecture decisions for any given business is knowing which ilities will create value, making sure the team understands why they create value, and then having a system in place to ensure that code is written in a way that aligns with this understanding.
> 
> Because most startups have similar codebases and face similar challenges, it's usually the same set of ilities that will maximize each startup's likelihood of success. So which ilities are the most valuable for startups? In my experience the answer is: predictability, readability, simplicity, and upgradability.


This is an absolutely great guide if you are writing Django apps in Python, but even if you are not, this analysis on needing better written systems that optimise for predictability, readability, simplicity and upgradability is absolutely true.

There are endless articles on HackerNews about how to implement bleeding edge algorithms or optimise for CPU caches that improve the performance of your systems, but very few that focus on the human nature of development teams.

If the average development team is around 8-10 people, and most people change role every 18 months, that means that you will be bringing a new person onto the team about once every 2-3 months, and within a few years, none of the original engineers will be left.  Emphasising to teams that the code they are writing needs to be written not for themselves, but for the next person who comes along, without the context to understand the decisions is how you get from a good team to a great team.


## [Notes on streaming large API responses](https://simonwillison.net/2021/Jun/25/streaming-large-api-responses/)

[https://simonwillison.net/2021/Jun/25/streaming-large-api-responses/](https://simonwillison.net/2021/Jun/25/streaming-large-api-responses/)

> The more time I spend with APIs, especially with regard to my Datasette and Dogsheep projects, the more I realize that my favourite APIs are the ones that let you extract all of your data as quickly and easily as possible.
> 
> There are generally three ways an API might provide this:
> 
> * Click an “export everything” button, then wait for a while for an email to show up with a link to a downloadable zip file. This isn’t really an API, in particular since it’s usually hard if not impossible to automate that initial “click”, but it’s still better than nothing. Google’s Takeout is one notable implementation of this pattern.
> * Provide a JSON API which allows users to paginate through their data. This is a very common pattern, although it can run into difficulties: what happens if new data is added while you are paginating through the original data, for example? Some systems only allow access to the first N pages too, for performance reasons.
> * Providing a single HTTP endpoint you can hit that will return ALL of your data—potentially dozens or hundreds of MBs of it—in one go.
> 
> It’s that last option that I’m interested in talking about today.


This is a good summary of some smart ideas about how to implement streaming API's that come from a large dataset. In particular, picking up problems about resource contention, server restarts and resuming streams.


## [Best Practices Around Production Ready Web Apps with Docker Compose — Nick Janetakis](https://nickjanetakis.com/blog/best-practices-around-production-ready-web-apps-with-docker-compose)

[https://nickjanetakis.com/blog/best-practices-around-production-ready-web-apps-with-docker-compose](https://nickjanetakis.com/blog/best-practices-around-production-ready-web-apps-with-docker-compose)

> On May 27th, 2021 I gave a live demo for DockerCon 21. It was a 29 minute talk where I covered a bunch of Docker Compose and Dockerfile patterns that I’ve been using and tweaking for years while developing and deploying web applications.
> 
> It’s pretty much 1 big live demo where we look at these patterns applied to a multi-service Flask application but I also reference a few other example apps written in different languages using different web frameworks (more on this soon).
> 
> This post is a written form of the video. The talk goes into more detail on some topics, but I’ve occasionally expanded on certain topics here in written form because even the director’s cut version was pressed for time at the time I recorded it.


This is a lovely set of recommendations for arranging and managing your own Docker based projects.  There's some good advice here around trying to build production/development environment parity.

In particular, I am a big fan that your actual code and system should have as few options as possible.  Ensuring that the defaults for everything matches production means that it's a developer decision to override the production behaviours.

Finally, I'll add a shoutout for ensuring that your systems have a "healthcheck" url.  I generally recommend one further, a deep healthcheck and a shallow healthcheck.  The shallow healthcheck should return something valid if just the service is running.  The deep healthcheck should validate all the dependencies and fail if anything critical to the operation of the service is failing.  The reason for this is that if you have hundreds of services then a failure deep in the stack can make every service look down.  This lets you tell which services are down due to dependency failures versus which are directly down.


## [How to Handle Secrets on the Command Line](https://smallstep.com/blog/command-line-secrets/)

[https://smallstep.com/blog/command-line-secrets/](https://smallstep.com/blog/command-line-secrets/)

> This uses jq to populate a JSON template for an API request (datasource.jq) with variables passed in with --arg, and then PUTs to the API with curl. Nice, huh?
> 
> It didn’t take long to discover that this pipeline leaks secrets all over the place:
> 
> The private key credential file is leaked: "$(< $KEY_LOCATION)"
> The bearer token env variable is leaked: -H "Authorization: Bearer $BEARER_TOKEN"
> And the secret piped data from STDIN is leaked: -d "$(< /dev/stdin)"
> All of these values, including the precious contents of the private key file, can be seen via ps when these commands are running. ps finds them via /proc/<pid>/cmdline, which is globally readable for any process ID.
> 
> To make atonement, I’m writing this post. We’ll look at three methods for handling secrets on the command line: Using piped data, credential files, and environment variables. We’ll look at some of the risks of these approaches, and how to use each of them as safely as possible.
> 
> 


Some nice tips for ensuring that you aren't leaking secrets in your live environment, which can be a massive security issue in hosted systems that run lots of containers.  A breach in any one container may well be able to access the process arguments for other containers, and if they can get the secrets, the attacker can move laterally with ease.


## [Uncomplicate Security for developers using Reference Architectures | by Anunay Bhatt | Mar, 2021 | Medium](https://ab-lumos.medium.com/embedding-security-into-sdlc-using-reference-architectures-for-developers-29403c00fb3d)

[https://ab-lumos.medium.com/embedding-security-into-sdlc-using-reference-architectures-for-developers-29403c00fb3d](https://ab-lumos.medium.com/embedding-security-into-sdlc-using-reference-architectures-for-developers-29403c00fb3d)

> Salient features of a successful reference architecture
> 
> These are the 7 jewels that must adorn your reference architecture program otherwise there is a high likelihood that your work might not be adopted by developers.
> 
>  * 1 Targeted to the developers 
>  * 2 Relatable 
>  * 3 Easily adoptable
>  * 4 Offering benefit to developers
>  * 5 Offering holistic and mappable security
>  * 6 Iterative
>  * 7 Measurable 


This is a nice writeup about reference architectures, focusing on how easy they are to adopt, and to use.

The idea of taking a reference architecture, defining it in code and then encouraging adoption by its use as a template is a great way to sneak or slipstream security features into architectures effectively


## [Dino Dai Zovi on Hardening CI Infrastructure - tl;dr sec](https://tldrsec.com/blog/dino-dai-zovi-harden-ci/)

[https://tldrsec.com/blog/dino-dai-zovi-harden-ci/](https://tldrsec.com/blog/dino-dai-zovi-harden-ci/)

> So absolutely before any of the fancy CAS stuff I mentioned, start with enforcing a maximum time-to-live for build nodes and have new nodes created from a known-good immutable image (e.g. latest AMI, etc) and install latest OS updates at boot (default for Amazon Linux AMIs).


I love that tldrsec has cached a copy of this, as referencing twitter threads is a pain.

This thread is worth reading in its entirety, but also, [this single piece of advice from Dino](https://twitter.com/dinodaizovi/status/1373414239969370112?s=20) is worth the price of admittance alone.  Immutable infrastructure that is rebuilt from a known good configuration on a regular basis is one of the best controls you can put in place for bursty traffic.  An attacker who cannot maintain persistence needs to constantly re-attack your infrastructure, which is harder to carry out and easier to detect.


## [Vigilante malware rats out software pirates while blocking ThePirateBay | Sophos](https://news.sophos.com/en-us/2021/06/17/vigilante-antipiracy-malware/)

[https://news.sophos.com/en-us/2021/06/17/vigilante-antipiracy-malware/](https://news.sophos.com/en-us/2021/06/17/vigilante-antipiracy-malware/)

> In one of the strangest cases I’ve seen in a while, one of my Labs colleagues recently told me about a malware campaign whose primary purpose appears to stray from the more common malware motives: Instead of seeking to steal passwords or to extort a computer’s owner for ransom, this malware blocks infected users’ computers from being able to visit a large number of websites dedicated to software piracy by modifying the HOSTS file on the infected system.


(Joel) Well... peculiar!

The malware tries to stop the machine (and therefore user) from visiting a particular torrent index website (something to do with pirates and bays...)

The malware doesn't sound like it is very well made or evasive either, using a number of trivial kill switches (checks on whether it should stop itself from doing a thing) and is trivial to clean up for a technical specialist or anti-malware vendor. It is distributed as fake games on Discord and as torrent files, claiming to be Minecraft etc.

I suspect somewhere there is a competitor to the torrent index site and they wanted to decrease traffic in this rather amusing/creative way.


