---
title: "22 - A new methodology needs a new set of practices"
date: 2018-10-20
description: "I've been thinking a lot about serverless recently.  I know that I'm years behind the cutting edge here, but I'm bullish that serverless is going to take off soon.  I'm hearing more and more that greenfield development should be starting with serverless architectures."
permalink: /a-new-methodology-needs-a-new-set-of-practices/
---

I've been thinking a lot about serverless recently.  I know that I'm years behind the cutting edge here, but I'm bullish that serverless is going to take off soon.  I'm hearing more and more that greenfield development should be starting with serverless architectures.

I'm not 100% sure I can actually define what serverless means though.  Many conversations over the last few weeks with colleagues has pursuaded me that my opinion of "You must use Function-as-a-Service at the core" is probably a good minimum bar for serverless systems, but that the ecosystem includes databases, queues, storage systems that are part of the serverless ecosystem.  Can we describe Amazon RDS as a "serverless database"?  I don't think so, but I think Google BigTable or Amazon Dynamo probably are.

As developer communities start to work out how to define serverless, and to work out what good practices actually look like in this world, I see a security community that has only just started to accept that the cloud is not just "other peoples computers". That it requires a new approach to security, and that the risks have changed significantly to different places in the system.  Serverless architectures are going to create a new world of problems for security specialists as the patterns that worked before really struggle to "cross the rubicon", and if we don't provide good security practice, we'll be left behind.

Finally, I'm shocked and surprised to discover that we passed 200 subscribers this week.  Hello to everyone new, I hope you find this newsletter interesting and useful.  Do please feel free to email me, reply to this, or tweet me to let me know your thoughts, and do pass it onto anyone you think might find it interesting.

## [Serverless Best Practices – Paul Johnston – Medium](https://medium.com/@PaulDJohnston/serverless-best-practices-b3c97d551535)

[https://medium.com/@PaulDJohnston/serverless-best-practices-b3c97d551535](https://medium.com/@PaulDJohnston/serverless-best-practices-b3c97d551535)

> Going back to the functions not calling other functions, it’s important to point out that this is how you chain functions together. A queue acts as a circuit breaker in the chaining scenario, so that if a function fails, you can easily drain down a queue that has got backed up due to a failure, or push messages that fail to a dead letter queue.
> 
> Basically, learn how distributed systems work.
> 
> With client applications with a serverless back end, the best approach is to look into CQRS. Separating out the point of retrieving data from the point of inputting data is key to this kind of pattern.


I'm not a serverless expert, but this guide feels like a good starter for 10 for development teams.  Noting that Serverless or function oriented programming is not the same as your traditional applications is an important step.

Back when PaaS's were brand new, I was part of a team that tried creating what became known as microservices on a PaaS platform.  One team was used to Java/Spring/Hibernate stack and were writing deployable java apps using that stack, my team were experimenting with Python and a precursor library to Flask.  One of the things we discovered was that on a PaaS, the java app on code start had a 45 second startup time, which happened intermittently anytime the application hadn't been called for more than 5 minutes.  The python app had a near 0 start up time, and was far more scalable and successful.

Bringing the best practices of the previous methodology to the new world can have weird side effects, and the worst thing you can do is try to double down on it.  My java PaaS team ended up writing a cronjob that pinged the server once a minute to keep it alive rather than abandon their way of working and did not have a fun time with running their app as a result.


## [The First "Serverless Architectures Security Top 10" Guide Released](https://www.puresec.io/blog/serverless-top-10-released)

[https://www.puresec.io/blog/serverless-top-10-released](https://www.puresec.io/blog/serverless-top-10-released)

> The comfort and elegance of serverless architectures is not without its drawbacks - serverless architectures introduce a new set of issues that must be taken into consideration when securing such applications


I've been thinking more and more about serverless recently, what it means, and how it all works.  It's not surprise to me that the traditional security models that applied to on premise software development don't work for serverless, I'd argue that they barely work for cloud-native applications anyway, and serverless is a step of abstraction too far away.

We need new security practices, designed against the same principles that work for serverless, and if we work fast, we might get those practices embedded into serverless frameworks before the majority of development teams start adopting them.


## [Innovation Isn’t a Top Priority, According to a Survey of 5,000+ Board Members](https://hbr.org/2018/09/innovation-should-be-a-top-priority-for-boards-so-why-isnt-it)

[https://hbr.org/2018/09/innovation-should-be-a-top-priority-for-boards-so-why-isnt-it](https://hbr.org/2018/09/innovation-should-be-a-top-priority-for-boards-so-why-isnt-it)

> Again, we found differences among industries. Just over one-fifth (22%) of boards operating in the IT and telecom industry sought tech expertise when filling their most recent board seat, higher than in any other industry. We also observed that boards of larger companies were more likely to seek new directors with technological expertise.


This report conflates innovation with technology, assuming that only “technology people” can deliver innovation. 
It also assumes that innovation by itself is a good thing, and that organisations that don’t focus strategically at the board level on innovation are struggling. 

I’m not convinced that innovation needs to be a board level concern. “How are we doing on innovation” is like asking “How are we doing on digital?”.  Innovation is something that the organisation should be doing as part of its normal strategy and just expected of the organisation. 

Also worth noting is that less than 24% of the boards thought that they had a handle on 'cybersecurity', the lowest result of any of the activities asked about.  That should be concerning to us.


## [How I Let Disney Track My Every Move](https://gizmodo.com/how-i-let-disney-track-my-every-move-1792875386)

[https://gizmodo.com/how-i-let-disney-track-my-every-move-1792875386](https://gizmodo.com/how-i-let-disney-track-my-every-move-1792875386)

> “The MagicBand was originally built with privacy in mind,” senior vice president Jim MacPhee told me about the device designed to track your every move, after I explained my Splash Mountain surprise. “There’s not connection to you as an individual.”
> 
> I have a hard time with this PR-friendly answer. “Built with privacy in mind” almost sounds like a the punchline of a post-Snowden era joke. Operating in a connected world where everything can be hacked, vague claims of privacy are hardly reassuring without some substantive details.
> 
> Disney’s executives couldn’t give me a source that could speak to the more technical aspects of the MagicBand. Or give me more information about how exactly they’re protecting park goers’ privacy. Or what tech Disney uses to anonymize its visitors’ personal information over the airwaves.
> 
> I still don’t know exactly how and where Disney World tracked me and the millions of other guests who visit the park every year. I do know that MagicBands can be hacked, however.


As I'm planning my first ever trip to Disney World, this article came across my desk for non-security reasons, but is an interesting insight into the security and privacy impacts of a totally different form of technology.

I can see how Disney want to track locations of guests in the parks, at the very least for crowd management, but it also wouldn't surprise me to discover that wait time tracking is enabled with this technology, as well as potentially lost children and so forth.

However, build with privacy in mind is a very unreassuring answer.  I can have privacy in mind while building something that purposefully or accidentally strips someones privacy, and correlation has been shown to be quite powerful in de-anonymising what is often considered safely anonymised data, especially in a system that takes photos of you everywhere you go.


## [Troy Hunt: The Effectiveness of Publicly Shaming Bad Security](https://www.troyhunt.com/the-effectiveness-of-publicly-shaming-bad-security/)

[https://www.troyhunt.com/the-effectiveness-of-publicly-shaming-bad-security/](https://www.troyhunt.com/the-effectiveness-of-publicly-shaming-bad-security/)

> And then, after the crowd died down, a bloke came up and handed me his card - "Betfair Security". Ah shit. But the hesitation quickly passed as he proceeded to thank me for the coverage. You see, they knew this process sucked - any reasonable person with half an idea about security did - but the internal security team alone telling management this was not cool wasn't enough to drive change. Negative media coverage, however, is something management actually listens to. 


I like this from Troy about the effectiveness of public shaming.  I'm always nervous of a bandwagon of vigilantes on twitter yelling about stupid insecure practices or misstatements from press officers, I'm not convinced that it can be helpful.

What's interesting to note here is that the mobs effect on the poor hapless PR person isn't necessarily helpful, but it raises attention for genuine journalists who start asking questions via the press channels, and that gets back to the management team far quicker.  I think if you see one of these examples, tagging in known tech journalists might be far more effective a strategy than just outright shaming.


## [Someone took over the Australian Prime Minister’s domain name and is boasting about it on Facebook – infosec – gaming – music | satiex.net](https://satiex.net/2018/10/18/someone-took-over-the-pms-domain-name-and-is-boasting-about-it-on-facebook/)

[https://satiex.net/2018/10/18/someone-took-over-the-pms-domain-name-and-is-boasting-about-it-on-facebook/](https://satiex.net/2018/10/18/someone-took-over-the-pms-domain-name-and-is-boasting-about-it-on-facebook/)

> Well, now that he controls the domain name, he can set up a catchall mailbox and wait for emails addressed to the PM to come in. He could then enumerate which email addresses were signed up for which services, and then initiate password resets


Losing control of an old domain can be bad, very bad.

One of the great myths of the internet is that one to one connection between an email address and a person.  There are a number of reasons that an email address can expire and be picked up by a different person, from Yahoo recycling accounts that have expired, to domain names expiring, and companies changing names and so forth.

Sadly, we've built an entire security model around sending password reset emails to confirm ownership of an email account, and I still think that's one of the most secure identity mechanisms that we have. If an attack has your email account, then they can pretty much impersonate you anyway. 
What we might need is email providers to work out how to make email addresses immutable, or something in your system to notice domainname ownership change.  

For now, it's a tiny tiny proportion of the threat model that it's probably not worth thinking about for most of us, but can produce entertaining stories like this one.


## [The Cybersecurity 202: Kanye West is going to make password security great again - The Washington Post](https://www.washingtonpost.com/news/powerpost/paloma/the-cybersecurity-202/2018/10/12/the-cybersecurity-202-kanye-west-is-going-to-make-password-security-great-again/5bbf83471b326b7c8a8d1946/?noredirect=on&utm_term=.dbcf65a9ddcf)

[https://www.washingtonpost.com/news/powerpost/paloma/the-cybersecurity-202/2018/10/12/the-cybersecurity-202-kanye-west-is-going-to-make-password-security-great-again/5bbf83471b326b7c8a8d1946/?noredirect=on&utm_term=.dbcf65a9ddcf](https://www.washingtonpost.com/news/powerpost/paloma/the-cybersecurity-202/2018/10/12/the-cybersecurity-202-kanye-west-is-going-to-make-password-security-great-again/5bbf83471b326b7c8a8d1946/?noredirect=on&utm_term=.dbcf65a9ddcf)

> Cranor added that she doesn’t blame users for not trying harder. “The notion that people could actually follow all the password rules we’re given is ludicrous,” she told me. Instead, she said, the companies that supply the devices and services should shoulder more of the burden.
> 
> Security researcher Matt Tait raised a similar point following West’s slip-up. “Lots of folks will laugh at this,” he tweeted, “but I think it's a useful illustration of how security ‘features’ fail when security decisions get offloaded to users who see them as annoying obstacles.”
> 
> Some security pros came to West's defense and said 000000 is actually not as bad a choice as it might seem. After all, it's better than having no passcode. 


This was an entertaining story last week, and it took me a while before I could find an article that didn't make me roll my eyes at the watching infosec community.  This article was it.

While we might want to point and laugh at '000000' as a passcode, there are plenty of reasons that West might have that passcode, from deliberately setting it because he knew he'd be watched, to being required to hand it over when being searched going into the building, to just not needing a better one because he has a bodyguard with him all the time.

But it's far more fun to pour scorn on users for bad security practices than it is to suggest better practices.  Nobody has been able to tell me what makes a good 6 digit pin code for an iPhone.  Why is 000000 (one of the 1,000,000 possible combinations) worse than '142536' or '654321'?  Do we think attackers all start at 0 and work their way up?

The clear sell here was to ask why TouchId or FaceId wasn't enabled, because I think almost everyone can agree that regardless of it's cryptographic security, from a usability perspective for normal people, biometric id as the single factor is a million times more usable than a PIN code we have to remember.


## [Privileged Access Workstations | Microsoft Docs](https://docs.microsoft.com/en-us/windows-server/identity/securing-privileged-access/privileged-access-workstations)

[https://docs.microsoft.com/en-us/windows-server/identity/securing-privileged-access/privileged-access-workstations](https://docs.microsoft.com/en-us/windows-server/identity/securing-privileged-access/privileged-access-workstations)

> This PAW guidance is intended to help you implement this capability for protecting high value accounts such as high-privileged IT administrators and high sensitivity business accounts. The guidance helps you:
> 
> Restrict exposure of credentials to only trusted hosts
> 
> Provide a high-security workstation to administrators so they can easily perform administrative tasks.
> 
> Restricting the sensitive accounts to using only hardened PAWs is a straightforward protection for these accounts that is both highly usable for administrators and very difficult for an adversary to defeat.


At StackTech4 this week there was a discussion about developer shadow IT, which is to say, within many corporate environments the standard IT offer doesn't meet developer needs, and they end up doing unofficial unmanaged builds and going "off-network" in order to do their job.
However, one of my big concerns is that when developers do this, they take the machines on which they administer their systems as well, and now you have highly sensitive administrative actions being done away from a managed device.

This guidance is a good writeup of one way of managing administrative workstations that are specifically there for high value tasks such as managing your corporate AD.  The simultaneous use options are also worth looking at, the Hyper-V user workstation within the PAW is a model that I've looked at before.

My only disappointment with this guidance is that the instructions at the end are all still written for users who don't do infrastructure as code, and this model won't work if your administrative tasks are done using automated tooling such as terraform or the like.  I'd love to see any written up patterns of how people are managing this.


## [Joint report on publicly available hacking tools - NCSC Site](https://www.ncsc.gov.uk/joint-report)

[https://www.ncsc.gov.uk/joint-report](https://www.ncsc.gov.uk/joint-report)

> In it we highlight the use of five publicly-available tools, observed in recent cyber incidents around the world. To aid the work of network defenders and systems administrators, we also provide advice on limiting the effectiveness of these tools and detecting their use on a network.


This report, while nothing that we don't already know, is a good summary of the sorts of tools that attackers use in real compromises, day in and day out.

There's lots of good advice for the sorts of things to look for, but the consistent theme that I see in here is that all of these tools end up requiring command and control traffic that originates from the tool and goes back to the command server, either with outbound connections, often disguised, or with incoming HTTP POST commands.

Your IDS system should definitely be warning you if there are outgoing connections on a well known port that do not follow the expected protocol (i.e RDP traffic on port 53), or if you get incoming POST commands on a URL that has never had POSTdata before.


## [A Trove of Facebook Data Is a Spammer's Dream and Your Nightmare | WIRED](https://www.wired.com/story/facebook-hack-data-spammers/)

[https://www.wired.com/story/facebook-hack-data-spammers/](https://www.wired.com/story/facebook-hack-data-spammers/)

> The possibility that scammers were behind the theft, though, highlights the ways in which centralized data repositories like email accounts and social media profiles are potential gold mines for—and frequent targets of—phishers, spammers, and shady marketers.


This facebook story gives and gives.  But this is interesting to me because in cybersecurity, I've noticed an escalation in attribution.  People want to blame "advanced persistent threats" and nation states for all kinds of attacks, and we feel self-important if we can say that we think we'll be the target of such attackers.  But most attacks online are carried out by small groups with a financial motive.  Hacking your javascript to mine monero or steal credit card numbers, or indeed, spammers seeking to have bigger and better databases to sell.


