---
title: "118 - Do you need a threat model?"
date: 2020-09-13
description: "When I see people talking about threat modelling, they can be referring to two totally different kinds of activities."
permalink: /introduction-to-threat-modelling/
---

When I see people talking about threat modelling, they can be referring to two totally different kinds of activities.

Component based threat modelling tends to look at an individual system and how the components interact.  The Microsoft threat modelling tool will allow you to do this, drawing up your system architecture and tracking risks and threats across the system.  Tools like the Escalation of Privilege can help you develop the skills to learn this style of threat modelling.

But I'm also a big fan of Systemic threat modelling, which is looking at the system as a black box, and often at how the attackers might look at your system.  Methods for analysing systems in this way vary and are far less common.  It's hard to find good tools and systems to help people consider how an attacker might actually operate.  We can use things like the Mitre ATT&CK system to build a shared vocabulary, but actual methods for threat modelling are less well described.

A lot of my problem with much cybersecurity advice is that it often lacks a sensible or articulated threat model.  It's unclear what a given security control is actually trying to achieve and who it's protecting against.  The threats, as raised by Microsoft again this week, reminds us that account takeover through poor password hygiene and password stuffing is still the preferred attack of even the most competent adversary.  You can worry about side channel attacks and cache misses and quantum supremacy if you want, but the reality of attackers is that they want the simplest, easiest, safest mechanism to get to their target.

## [The Evolution of Trust](https://ncase.me/trust/)

[https://ncase.me/trust/](https://ncase.me/trust/)

> THE EVOLUTION OF TRUST


This is a lovely interactive game that will teach you about game theory.  I love games as a learning tool, and this is both well put together, deep enough to cover a hefty amount of game theory and yet accessible enough that my 8 year old watching me with it wanted to have a go and picked up the concepts easily enough.


## [15 rules for blogging, and my current streak (Interconnected)](http://interconnected.org/home/2020/09/10/streak)

[http://interconnected.org/home/2020/09/10/streak](http://interconnected.org/home/2020/09/10/streak)

> My current streak: I’ve now been writing new posts for 24 consecutive weeks. Multiple posts a week. How on earth? I just calculated it, and I’ve added the live streak count to the site footer. I wonder how long I can keep it up.
> 
> This blog has been going since February 2000. I’m writing more now, two decades on, than I have for YEARS. That’s not just because of lockdown – it’s because, about six months ago, I set myself some rules. The rules, which are specific to me, are intended to bump me out of certain mental traps that I know will otherwise stop my words. And since these rules have been working for, well, 24 weeks now, I figured I’d write them down.


I wish I blogged more.  Looking back over my personal blog and I see that I've written 3 articles in 2019 and 2020 combined.

But then I remember that I've written this newsletter once a week for the past 2 years, which is close to blogging.  These writing rules are ones that work for me writing the intros here as well, and good tips for blogging more generally.


## [Security by Obscurity is Underrated – Utku Sen - Blog – computer security, programming](https://utkusen.com/blog/security-by-obscurity-is-underrated.html)

[https://utkusen.com/blog/security-by-obscurity-is-underrated.html](https://utkusen.com/blog/security-by-obscurity-is-underrated.html)

> One of the main goal of defensive security is reducing the risk for the target business. According to the OWASP’s methodology, the risk of an issue is calculated with the formula below:
> 
> `Risk = Likelihood * Impact`
> 
> According to this formula, a Remote Code Execution issue poses more risk than a Cross Site Scripting one since the RCE causes more impact. This is easy. But what about the likelihood metric. 
> 
> At the highest level, this is a rough measure of how likely this particular vulnerability is to be uncovered and exploited by an attacker
> 
> So, if we can reduce the likelihood, we can reduce the overall risk. That’s good. It’s actually very similar to a very common idea called “Defense in Depth”. It’s also referred as “Swiss Cheese Model”


There's quite a lot I disagree with in this article.  In the slack channel where this was raised, I said:

> I think that for a good solid security architect, adding obscurity features is like a chef sprinkling some salt over the top of the meal at the end.
> To a great meal, the salt adds and brings out the flavours that are there.
> But no amount of salt can help you if you made bad food, selected bad ingredients or cannot cook.
>
> The problem in “cybersecurity” is that too many people look at others work and blindly copy what they do. So they see you adding salt and say “see, the way to make it secure is to sprinkle salt at the end”.
>
> I support someone who had done all of the basics and much of the advanced stuff doing some obfuscation work on top of what they’ve done. But I worry whenever someone talks about obfuscation because 99 times out of 100, they are doing it in place of doing the right security controls.

But the swiss cheese method, as called out here is the root of some really bad security architecture decisions.  If you've ever been asked to install back to back firewalls from different manufacturers, then you've been subjected to this.  The argument goes that firewalls from different manufacturers will have different flaws (or holes), and therefore the two brands will protect you more.  But the reality is that there's a shocking amount of common supply chain issues among multiple vendors. Secondly, there are lots of things above those firewalls that will be the same, your system administrators, your admin network, your configuration and all the issues that come with it.  The faulty thinking of the "swiss cheese model" just doesn't add up to the reality of technology.


## [Realizing the full potential of AI in the workplace | Deloitte Insights](https://www2.deloitte.com/us/en/insights/focus/technology-and-the-future-of-work/ai-in-the-workplace.html?id=us:2em:3pa:digital-transformation:eng:di:073120)

[https://www2.deloitte.com/us/en/insights/focus/technology-and-the-future-of-work/ai-in-the-workplace.html?id=us:2em:3pa:digital-transformation:eng:di:073120](https://www2.deloitte.com/us/en/insights/focus/technology-and-the-future-of-work/ai-in-the-workplace.html?id=us:2em:3pa:digital-transformation:eng:di:073120)

> The zero-sum conception of jobs as fixed bundles of tasks, many of which will increasingly be performed by machines, limits one’s ability to reimagine jobs in ways that create new forms of value and meaning.6 And framing AI as a kind of technology that imitates human cognition makes it easy to be misled by exaggerated claims about the ability of machines to replace humans.
> 
> We believe that a change in perspective about AI’s role in work is long overdue. Human and machine capabilities are most productively harnessed by designing systems in which humans and machines function collaboratively in ways that complement each other’s strengths and counterbalance each other’s limitations. Following MIT’s Thomas Malone, a pioneer in the study of collective intelligence, we call such hybrid human-machine systems superminds.


This is a good article summing up why AI and ML shouldn't be viewed as simply replacing the humans in a system, but as a symbiotic relationship to assist the humans in doing their job.

The corollary to this is that if you are buying something from a vendor that claims that it has ML inside that will replace your staff, then that claim is missing the value that ML can offer, and probably is not providing enough information out of the system to assist your staff when they need it.


## [Principles for Microservice Design: Think IDEALS, Rather than SOLID](https://www.infoq.com/articles/microservices-design-ideals/)

[https://www.infoq.com/articles/microservices-design-ideals/](https://www.infoq.com/articles/microservices-design-ideals/)

> For object-oriented design we follow the SOLID principles. For microservice design we propose developers follow the “IDEALS”: interface segregation, deployability (is on you), event-driven, availability over consistency, loose-coupling, and single responsibility.
> Interface segregation tells us that different types of clients (e.g., mobile apps, web apps, CLI programs) should be able to interact with services through the contract that best suits their needs. 
> Deployability (is on you) acknowledges that in the microservice era, which is also the DevOps era, there are critical design decisions and technology choices developers need to make regarding packaging, deploying and running microservices. 
> Event-driven suggests that whenever possible we should model our services to be activated by an asynchronous message or event instead of a synchronous call. Availability over consistency reminds us that more often end users value the availability of the system over strong data consistency, and they’re okay with eventual consistency. 
> Loose-coupling remains an important design concern in the case of microservices, with respect to afferent (incoming) and efferent (outgoing) coupling. Single responsibility is the idea that enables modeling microservices that are not too large or too slim because they contain the right amount of cohesive functionality.


This, via [Pat Kua's Level Up newsletter](http://levelup.patkua.com/) is a really great architectural model and set of guiding practices for building good systems made up of microservices.  Architects and Dev team leads should definitely read this, and use the IDEALS model any place where SOLID is being recommended at the moment.


## [How Target Figured Out A Teen Girl Was Pregnant Before Her Father Did](https://www.forbes.com/sites/kashmirhill/2012/02/16/how-target-figured-out-a-teen-girl-was-pregnant-before-her-father-did/#7c3f3a146668)

[https://www.forbes.com/sites/kashmirhill/2012/02/16/how-target-figured-out-a-teen-girl-was-pregnant-before-her-father-did/#7c3f3a146668](https://www.forbes.com/sites/kashmirhill/2012/02/16/how-target-figured-out-a-teen-girl-was-pregnant-before-her-father-did/#7c3f3a146668)

> So Target started sending coupons for baby items to customers according to their pregnancy scores. Duhigg shares an anecdote -- so good that it sounds made up -- that conveys how eerily accurate the targeting is. An angry man went into a Target outside of Minneapolis, demanding to talk to a manager:
> 
> 
> Target knows before it shows.
> “My daughter got this in the mail!” he said. “She’s still in high school, and you’re sending her coupons for baby clothes and cribs? Are you trying to encourage her to get pregnant?”
> 
> The manager didn’t have any idea what the man was talking about. He looked at the mailer. Sure enough, it was addressed to the man’s daughter and contained advertisements for maternity clothing, nursery furniture and pictures of smiling infants. The manager apologized and then called a few days later to apologize again.
> 
> (Nice customer service, Target.)
> 
> On the phone, though, the father was somewhat abashed. “I had a talk with my daughter,” he said. “It turns out there’s been some activities in my house I haven’t been completely aware of. She’s due in August. I owe you an apology.”
> 
> [...]
> 
> “Then we started mixing in all these ads for things we knew pregnant women would never buy, so the baby ads looked random. We’d put an ad for a lawn mower next to diapers. We’d put a coupon for wineglasses next to infant clothes. That way, it looked like all the products were chosen by chance.
> 
> “And we found out that as long as a pregnant woman thinks she hasn’t been spied on, she’ll use the coupons. She just assumes that everyone else on her block got the same mailer for diapers and cribs. As long as we don’t spook her, it works.”


I was reminded of this article via [a tweet from Nick Drage](https://twitter.com/SonOfSunTzu/status/1304379629118074888?s=20) about just how shockingly bad the advertising industry is at advertising to us.

I've just bought some new mattresses, and so my advertising banners all over the web are for more mattresses, something I'm unlikely to buy for another 5 years at least, instead of seeing adverts for say duvets or sheet sets or bedroom decorations.

This story reminds me that advertising companies actively try not to be seen as too good, and therefore creepy.  I'd love to know how this has moved on in the last 8 years since this article was written.  


## [Amazon’s Alexa for Landlords Is a Privacy Nightmare Waiting to Happen](https://www.gizmodo.com.au/2020/09/amazons-alexa-for-landlords-is-a-privacy-nightmare-waiting-to-happen/)

[https://www.gizmodo.com.au/2020/09/amazons-alexa-for-landlords-is-a-privacy-nightmare-waiting-to-happen/](https://www.gizmodo.com.au/2020/09/amazons-alexa-for-landlords-is-a-privacy-nightmare-waiting-to-happen/)

> This is all on top of the fact that the entire smart-speaker-that-comes-with-your-rental phenomenon is still strange to me for a few reasons; Amazon cites a study by the National Apartment Association, which says “84% of renters want an apartment with smart home amenities,” and “61% of whom said they would pay a monthly fee for a voice assistant” as part of its justification for offering its new Alexa for Residential service.
> 
> First of all, who is this 84% of people who would be ok with their landlord having access to the smart speaker in their home? Never mind the possibility that employees at Amazon could be listening to a recording of whenever you pay your rent. Amazon says that property managers will not “have access to any customer data” and “voice recordings are automatically deleted daily.” Residents will also be able to connect their personal Amazon account to the device and control their privacy settings. Still, having a landlord-owned smart speaker — or even a personal smart speaker — in my home is a big hell-fucking-no from me.


There are privacy concerns here to be sure, and I think that there are lot of bad landlords out there, and there are no laws that really apply to digital intrusion into your increasing internet of things enabled house.

But more relevant to me here is just how out of touch tech and privacy journalists and campaigners are with the general population.  84% of renters want some form of home automation.  That is to say that they see the value that such systems bring as being worth the privacy cost that they see with them.  You can argue that people don't understand the privacy implications, and I have some sympathy for that view, but as far as I can tell, most of my normal friends just give a huge shrug if anyone tries to explain.  They understand and really just don't care.


## [New cyberattacks targeting U.S. elections  - Microsoft on the Issues](https://blogs.microsoft.com/on-the-issues/2020/09/10/cyberattacks-us-elections-trump-biden/)

[https://blogs.microsoft.com/on-the-issues/2020/09/10/cyberattacks-us-elections-trump-biden/](https://blogs.microsoft.com/on-the-issues/2020/09/10/cyberattacks-us-elections-trump-biden/)

> In 2016, the group primarily relied on spear phishing to capture people’s credentials. In recent months, it has engaged in brute force attacks and password spray, two tactics that have likely allowed them to automate aspects of their operations. Strontium also disguised these credential harvesting attacks in new ways, running them through more than 1,000 constantly rotating IP addresses, many associated with the Tor anonymizing service. Strontium even evolved its infrastructure over time, adding and removing about 20 IPs per day to further mask its activity.
> 
> [...]
> 
> Zirconium is using what are referred to as web bugs, or web beacons, tied to a domain they purchased and populated with content. The actor then sends the associated URL in either email text or an attachment to a targeted account. Although the domain itself may not have malicious content, the web bug allows Zirconium to check if a user attempted to access the site. For nation-state actors, this is a simple way to perform reconnaissance on targeted accounts to determine if the account is valid or the user is active.
> 
> [...]
> 
> Since our last disclosure, Phosphorus has attempted to access the personal or work accounts of individuals involved directly or indirectly with the U.S. presidential election. Between May and June 2020, Phosphorus unsuccessfully attempted to log into the accounts of administration officials and Donald J. Trump for President campaign staff.


Useful reminder that even the most advanced actors in the world, going after the highest profile targets in the world are doing so using phishing, password spraying and account takeover.

This might be bias on Microsoft's part, in that this is the only kinds of attacks that they see, but even if that's true, there's a huge amount of attacker capability focused here.  The most advanced thing from the STRONTIUM attacker is the use of more advanced attack delivery platforms to obfuscate and hide the origin of the attacks.


## [HOW TO PLAY eop AND CORNUCOPIA REMOTELY – Agile Stationery](https://agilestationery.co.uk/blogs/pp/how-to-play-eop-and-cornucopia-remotely)

[https://agilestationery.co.uk/blogs/pp/how-to-play-eop-and-cornucopia-remotely](https://agilestationery.co.uk/blogs/pp/how-to-play-eop-and-cornucopia-remotely)

> 3 advantages of playing games in cyber security
> Creativity
> Turning it into a game lowers the stakes and provides a safe environment for creative exploration of the security problem.
> 
> Depth 
> Assigning threat models to players helps make use of detailed context known to each player.
> 
> The Unexpected 
> Randomly dealing out threats to players prompts the sharing of tacit knowledge that cannot reliably be located in advance, such as the details of how specific components were programmed and tested.


Escalation of Privilege, if you haven't played, is a lovely game to introduce the basics of threat modelling to a team.  It encourages the discussion around the kinds of threats that might exists, and lifts the average confidence and experience of the team just through some simple easy workshops.

Of course, carrying out these workshops with remote teams isn't easy, so agile stationary have put together this guide for playing remotely, to continue your threat modelling sessions even when at least some of the team are remote.


## [What is Threat Modeling and GitHub's Process - GitHub Blog](https://github.blog/2020-09-02-how-we-threat-model/)

[https://github.blog/2020-09-02-how-we-threat-model/](https://github.blog/2020-09-02-how-we-threat-model/)

> Before we dive into how we approach threat modeling at GitHub, let’s first agree on what threat modeling is. Defining the goals of the process helps everyone involved set expectations for what comes out.
> 
> At GitHub, threat modeling isn’t necessarily a specific tool or set of deliverables—it’s a process to help foster ongoing discussions between security and engineering teams around a new or existing system. A threat model is a collaborative security exercise where we evaluate and validate the design and task planning​ for a new or existing service. This exercise involves structured thinking about potential security vulnerabilities that could adversely affect your service.


This is a nice, if slightly anemic guide on threat modelling.  While they start by saying they want to define what a threat model is, they don't actually define it, and don't give any examples.

Lots of use of Microsoft Threat Modeller, or OWASPS threat modelling tools here.  And this is a good description of how to engage a team in carrying out a threat modelling session, including the use of STRIDE as a method for enumerating the threats.


