---
title: "66 - Are we unwilling managers"
date: 2019-08-24
description: "Many of us in infosec and digital are also team leads or managers of various forms, and most of us tend to be somewhat unwilling managers."
permalink: /unwilling-managers/
---

Many of us in infosec and digital are also team leads or managers of various forms, and most of us tend to be somewhat unwilling managers.

The career path in technology tends to mean that most gifted technically competent people are increasingly [promoted to their level of management incompetence](https://en.wikipedia.org/wiki/Peter_principle).  Many of us don't really want to manage people, define career progression, handle poor performers or set objectives for teams, we see it as busy work or a necessary evil that we have to do in order to be senior.

But clear good management is about enabling your team to be the best they can be.  It's about giving good feedback and watching your most junior people grow and learn and become brilliant engineers with great experiences; about letting your staff make mistakes that are safe and well managed so they can learn; about have a positive culture and environment.

We spend more time reading technical blog posts, exploits and so on than we do reading about how management techniques actually work, how they don't work or how we can be better managers.

This week, while taking a well deserved holiday at the beach, I've selected a number of interesting management blog posts for you, that cover a variety of the sorts of problems we see in managing small and medium size technical teams.

## [Contra - Interactive Application Security Training](https://application.security/)

[https://application.security/](https://application.security/)

> The following interactive tutorial is a reconstruction of Capital One's data breach incident that exposed the records of almost 106 million customers. 
> 
> 
> Paige Thompson is accused of breaking into a Capital One server and gaining access to 140,000 Social Security numbers, 1 million Canadian Social Insurance numbers and 80,000 bank account numbers. 


This is a lovely click through and writing training course that shows how a Server Side Request Forgery attack is actually carried out.  If Contra can develop more of these, I'd gladly recommend the training program to development teams.   


## [Report: Data Breach in Biometric Security Platform Affecting Millions of Users](https://www.vpnmentor.com/blog/report-biostar2-leak/)

[https://www.vpnmentor.com/blog/report-biostar2-leak/](https://www.vpnmentor.com/blog/report-biostar2-leak/)

> Our team was able to access over 27.8 million records, a total of 23 gigabytes of data, which included the following information:
> 
> * Access to client admin panels, dashboards, back end controls, and permissions 
> * Fingerprint data 
> * Facial recognition information and images of users
> * Unencrypted usernames, passwords, and user IDs
> * Records of entry and exit to secure areas
> * Employee records including start dates
> * Employee security levels and clearances
> * Personal details, including employee home address and emails
> * Businesses’ employee structures and hierarchies
> * Mobile device and OS information
> 
> One of the more surprising aspects of this leak was how unsecured the account passwords we accessed were. Plenty of accounts had ridiculously simple passwords, like “Password” and “abcd1234”. It’s difficult to imagine that people still don’t realize how easy this makes it for a hacker to access their account. 


This writeup confused me quite a lot, which is why I didn't include it last week.  But several discussions have made it clear that it should be a thing.

There's a lot of mixed messages in this writeup, and it's hard to divine the facts from the actual breach.  Several writeups have pilloried Biostar2 for keeping photographs of the fingerprints rather than just the hash of the fingerprint, but in reality it's still quite hard to weaponise a photo of a fingerprint.  It's not trivial to 3d print a fingerprint that can be applied and reliably read, so the loss here, while not great, isn't as bad as it sounds.

Far worse in my opinion is that physical access control systems were exposed to the internet via an API, which appears (assuming I'm reading the report correctly) to include write capability.  That means that attackers could simply add their finger prints and employee records and therefore gain physical access to any protected areas, or malicious employees could increase their access to more secure areas.

If you have a physical control like this sort of thing, you kind of assume that it's not trivial to breach.  However, physical attacks are still far rarer, and combined physical and cyber attacks require a unique set of skills that isn't available to most attackers.


## [ADD / XOR / ROL: Rashomon of disclosure](http://addxorrol.blogspot.com/2019/08/rashomon-of-disclosure.html)

[http://addxorrol.blogspot.com/2019/08/rashomon-of-disclosure.html](http://addxorrol.blogspot.com/2019/08/rashomon-of-disclosure.html)

> In general, defenders are almost always at an information disadvantage: Attackers will not tell them what they do, and gleefully applaud and encourage when the defender gets a wrong idea in his head about what to do. Read the declassified cryptolog_126.pdf Eurocrypt trip report to get a good impression of how this works.
> 
> Three of the last four sessions were of no value whatever, and indeed there was almost nothing at Eurocrypt to interest us (this is good news!). The scholarship was actually extremely good; it's just that the directions which external cryptologic researchers have taken are remarkably far from our own lines of interest. 
> 
> Defense has many resources, but many of them are misapplied: Mitigations performed that do not hold up to an attacker slightly changing strategies, products bought that do not change an attacker calculus or the exploit economics, etc.
> 
> A nontrivial part of this misapplication is information scarcity about real exploits. My personal view is that Project Zero's exploit write-ups, and the many great write-ups by the Pwn2Own competitors and other security research teams (Pangu and other Chinese teams come to mind) about the actual internal mechanisms of their exploits is invaluable to transmit understanding of actual attacks to defenders, and are necessary to help the industry stay on course.


This is a good argument that vulnerability disclosure is valuable to organisations and to infosec as a whole.  The argument is well set out and I find myself nodding along and agreeing with much of it.

We know that attackers have the edge in information asymmetry, but more sharing can make defenders better at their job.

My only qualm would be that while attackers have better information due to the ability to decompile patches, underground trading forums and so forth, that does raise the bar for attackers from script kiddie to need some actual knowledge and resources to commit to being a good attacker.  When information is shared more widely, and people create trigger scripts and metasploit modules, then the bar for low capability attackers is lowered.  I think that's a cost worth paying for better informed defenders.


## [How the Chinese recruit American journalists as spies](https://www.nate-thayer.com/how-the-chinese-recruit-american-journalists-as-spies/)

[https://www.nate-thayer.com/how-the-chinese-recruit-american-journalists-as-spies/](https://www.nate-thayer.com/how-the-chinese-recruit-american-journalists-as-spies/)

> On the day I received my first message from Chinese intelligence agents from the Ministry of State Security, they, of course, didn’t say they were Chinese spies. The note was from “Frank Hu,” a “project assistant” from Shanghai Pacific & International Strategy Consulting Co, saying he had found me on the Internet and was writing to “seek potential cooperation opportunities.”
> 
> It sounded innocent enough, but it raised red flags. His company, he said, “is a Shanghai-based consulting firm, specializing in independent policy analysis and advisory services. We strive to help our clients properly assess political dynamics, risks and opportunities in countries and regions they operate in.”
> 
> Frank called me a “renowned investigative journalist” who “has written lots of in-depth investigative political reports.” Therefore, he said, “we wonder if you are interested in becoming a part-time political consultant for us and using your wide social network to provide us with insightful consultations. Look forward to your reply. Regards Frank Shanghai Pacific & International Strategy Consulting Co.”
> 
> [...]
> 
> In the US intelligence services, those who recruit spies from foreign countries target the weak points and vulnerabilities of potential recruits in what they call “MICE”—an acronym for Money, Ideology, Creed, and Ego. Chinese intelligence services try to exploit what they call “The four moral flaws”: lust, anger/revenge, power/fame, and money.


Another great review of an approach for espionage, detailing how the approach was made and the conversations forwards and backwards.  The most alarming thing is the clear disregard that the CBI's Counter Intelligence team had for this approach, even when contacted.  Did they not care, or was it just too low level?


## [Why Software Remains Insecure | Daniel Miessler](https://danielmiessler.com/blog/the-reason-software-remains-insecure/)

[https://danielmiessler.com/blog/the-reason-software-remains-insecure/](https://danielmiessler.com/blog/the-reason-software-remains-insecure/)

> the existence of insecure software has so far helped society far more than it has harmed it.
> 
> Basically, software remains vulnerable because the benefits created by insecure products far outweigh the downsides. Once that changes, software security will improve—but not a moment before.


This does lead to an interesting point, which is it's not about the existence of insecure software, it's that there is more reward for being able to produce software quickly and easily, where users cannot tell or don't care about the difference between secure and insecure software.

That means that companies that produce minimally secure software will outcompete those who spend more effort in securing their software.


## [The Nightmare of Valve’s self-organizing “utopia” - Dunia - Medium](https://medium.com/dunia-media/the-nightmare-of-valves-self-organizing-utopia-6d32d329ecdb)

[https://medium.com/dunia-media/the-nightmare-of-valves-self-organizing-utopia-6d32d329ecdb](https://medium.com/dunia-media/the-nightmare-of-valves-self-organizing-utopia-6d32d329ecdb)

> The challenge lies in scaling up. As a community or company grows, formal structures serve the purpose of clarifying the rules of conduct and criteria of performance when assumed knowledge and access to people becomes more limited. The alternative is chaos, or a gradual growth of elites who exert control through social pressure. Far from magically solving workplace issues, flat organizations and open offices can exacerbate them.
> 
> We live in a cultural moment of deep distrust towards authority, where the old rigid structures have failed us: free markets and the onward march of industrialization were supposed to bring prosperity to the masses, yet inequality has risen across the world; 
> 
> [...]
> 
> But it’s all the more reason to remember that structurelessness does not denote the absence of rules. Flatness does not inherently bring equality. Doing away with hierarchy is a means to the end of creating a better working relationship, not an end unto itself.


The attraction of flat structures to senior managers is the illusion of freedom from bureaucratic control.  Many of the managers I know view the "work" of doing one on ones, performance management, OKR's and other management tasks as a distraction from the "real job", but in reality, doing that work is what makes the company work, and gives a structure that can be freeing to the workers.


## [Hospital checklists are meant to save lives — so why do they often fail? : Nature News & Comment](https://www.nature.com/news/hospital-checklists-are-meant-to-save-lives-so-why-do-they-often-fail-1.18057)

[https://www.nature.com/news/hospital-checklists-are-meant-to-save-lives-so-why-do-they-often-fail-1.18057](https://www.nature.com/news/hospital-checklists-are-meant-to-save-lives-so-why-do-they-often-fail-1.18057)

> Mary Dixon-Woods, a medical sociologist at the University of Leicester, UK, interviewed staff members at 17 of the ICUs participating in Matching Michigan11. She found that by the time the programme began, British hospitals had already been involved in numerous government-led efforts to reduce infections. The checklist, she says, was viewed as “yet another example of these top-down, intrusive, imposed initiatives”. It became “something that had to be endured rather than enjoyed”. In Michigan, by contrast, the tool was considered new and exciting. And it was not imposed by the government — it was organized by the well-regarded state hospital association, and participation was voluntary.
> 
> Dixon-Woods did identify one exemplary ICU, in which a high infection rate fell to zero after Matching Michigan began. The unit was led by a charismatic physician who championed the checklist and rallied others around it. “He formed coalitions with his colleagues so everyone was singing the same tune, and they just committed as a whole unit to getting this problem under control,” says Dixon-Woods.


The checklist manifesto is a great book, one I thoroughly encourage reading, but while checklists do a good job, they only work if they are well adopted by the teams that use them.  This study shows that many British hospitals had checklists enforced on them, and the staff didn't bother completing them, which meant they didn't get the benefit.

The same is true for almost all management techniques, one-on-ones, OKR's, checklists, goal-setting, weeknotes.  Unless your team and company feels like they own the management process, and has some buy in and see's the benefit, you'll never get the benefits that the Harvard Business Review says you will.

If you are introducing something like one of these, you need staff engagement, and you need your staff to feel like they helped customise and create the processes that work for them, and then you'll get buy in from the team


## [Our 6 Must Reads for Cutting Through Conflict and Tough Conversations | First Round Review](https://firstround.com/review/our-6-must-reads-for-cutting-through-conflict-and-tough-conversations/)

[https://firstround.com/review/our-6-must-reads-for-cutting-through-conflict-and-tough-conversations/](https://firstround.com/review/our-6-must-reads-for-cutting-through-conflict-and-tough-conversations/)

> “If you’re lying awake at night thinking, ‘God, Jeff is pissing me off,’ your chance at a low-cost solution probably came about three months ago,” says Lopp. “You had the chance to improve things but you sat and waited until it actually started to hurt." The ideal time to act is well before someone becomes a Jeff. And that means implementing programming before you need a PIP.
> 
> A quick refresher: PIP is one of the worst and most-feared acronyms out there. Standing for “performance improvement plan,” a PIP usually takes the form of an official, written agreement drafted and overseen by HR that outlines exactly how an employee needs to very quickly get better at their job in order to keep it. They may be more common at large corporations than startups, but even new companies should be familiar with PIP principles to keep their staff on track, especially as they enter rapid growth. Lopp recognizes the need, but hates how they’re used: too often as a last-ditch, half-hearted effort to save someone’s job.


All 6 of these tips are good management tip, but this one is one that I think holds the most water.

Good feedback should be like steering a car, lots of little nudges on the wheel to keep the car straight.  If you wait until you hit the edge of the road and then wrench the wheel over, you'll just cause yourself more problems.

Equally, as the quote says, if you wait until HR insists you create a performance improvement program, then you've waited too long, you need to invest in your staff, and providing honest accurate feedback before things become a problem.


