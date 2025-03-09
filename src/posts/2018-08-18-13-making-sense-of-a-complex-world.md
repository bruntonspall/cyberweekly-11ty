---
title: "13 - Making sense of a complex world"
date: 2018-08-18
description: "It's a quiet week this week as I prepare for family holiday and try to get all my work done before I leave, but here's a selection of the best reading I've seen in the busyness of the week. "
permalink: /making-sense-of-a-complex-world/
---

It's a quiet week this week as I prepare for family holiday and try to get all my work done before I leave, but here's a selection of the best reading I've seen in the busyness of the week. 

Most interestingly is the theme coming through that a lot of the world is quite complex these days.  A lot of the time we try to imagine that the world is simple and easy to model in software, but it's always the edge cases that get us, whether it be the detail of how web caching works, or the concept that you need different mechanisms for talking to sources in different countries when you run a spy operation.  Even internally we tend to simplify the world, and assume that information is equally distributed around our organisations, or that adding new products to our portfolio is easy.
Most of the articles this week cover some part of the complexity of the world, and a number of coping mechanisms to deal with the complexity.
  
I've got the next week off on holiday with the family, on a sunny and sandy english beach, so hopefully I'll catch up with my reading, as well as a bunch of my personal projects.

## [Botched CIA Communications System Helped Blow Cover of Chinese Agents – Foreign Policy](https://foreignpolicy.com/2018/08/15/botched-cia-communications-system-helped-blow-cover-chinese-agents-intelligence/amp/)

[https://foreignpolicy.com/2018/08/15/botched-cia-communications-system-helped-blow-cover-chinese-agents-intelligence/amp/](https://foreignpolicy.com/2018/08/15/botched-cia-communications-system-helped-blow-cover-chinese-agents-intelligence/amp/)



"But the CIA’s interim system contained a technical error: It connected back architecturally to the CIA’s main covert communications platform. When the compromise was suspected, the FBI and NSA both ran “penetration tests” to determine the security of the interim system. They found that cyber experts with access to the interim system could also access the broader covert communications system the agency was using to interact with its vetted sources, according to the former officials."  An interesting read, but a reminder that some of the patterns we use in cybersecurity are important and do result in life or death for real people in real places sometimes.  The description further down of the counterintelligence service forming a specific task force to attempt to break the system is a healthy reminder of the sort of adversary that you can face at these higher levels is determined and capable


## [Practical Web Cache Poisoning | Blog](https://portswigger.net/blog/practical-web-cache-poisoning)

[https://portswigger.net/blog/practical-web-cache-poisoning](https://portswigger.net/blog/practical-web-cache-poisoning)



"I'll illustrate and develop this technique with vulnerabilities that handed me control over numerous popular websites and frameworks, progressing from simple single-request attacks to intricate exploit chains that hijack JavaScript, pivot across cache layers, subvert social media and misdirect cloud services."

This is a good demonstration of taking a simple vulnerability, and extending it and increasing it to find more and more ways of exploiting it.  Not to mention this is a reminder that the fact that the internet works at all is sometimes a bit scary.  Who knew caching systems worked this way.


## [Hack like a CISO | CSO Online](https://www.csoonline.com/article/3291280/leadership-management/hack-like-a-ciso.html)

[https://www.csoonline.com/article/3291280/leadership-management/hack-like-a-ciso.html](https://www.csoonline.com/article/3291280/leadership-management/hack-like-a-ciso.html)



"I first start this hack by collecting copies of current network maps, security diagrams, data flows, security contracts, budgets, and previous assessments"

So, I object to the definition of hack here, as it's more "Do your job", but I wanted to comment on this bit.
Again, for me this is one of the big value add's of using infrastructure as code, is that I don't have to read "security diagrams" and "data flows", I can read the code, or get someone to generate the maps from it for me if needed.

What are the chances that the collected security assurance documents actually match the reality on the ground?  How do we fix that problem?


## [GitHub - TryCatchHCF/DumpsterFire: "Security Incidents In A Box!" A modular, menu-driven, cross-platform tool for building customized, time-delayed, distributed security events. Easily create custom event chains for Blue Team drills and sensor / alert map](https://github.com/TryCatchHCF/DumpsterFire)

[https://github.com/TryCatchHCF/DumpsterFire](https://github.com/TryCatchHCF/DumpsterFire)



"The DumpsterFire Toolset is a modular, menu-driven, cross-platform tool for building repeatable, time-delayed, distributed security events. Easily create custom event chains for Blue Team drills and sensor / alert mapping. Red Teams can create decoy incidents, distractions, and lures to support and scale their operations. Turn paper tabletop exercises into controlled "live fire" range events. Build event sequences ("narratives") to simulate realistic scenarios and generate corresponding network and filesystem artifacts."

This is a cute tool for blueteams to test out whether their SIEM tools are actually working.  Run sets of security suites in interesting ways and see whether the alarms actually go off


## [Ways to think about machine learning — Benedict Evans](https://www.ben-evans.com/benedictevans/2018/06/22/ways-to-think-about-machine-learning-8nefy)

[https://www.ben-evans.com/benedictevans/2018/06/22/ways-to-think-about-machine-learning-8nefy](https://www.ben-evans.com/benedictevans/2018/06/22/ways-to-think-about-machine-learning-8nefy)



"Washing machines are robots, but they're not ‘intelligent’. They don't know what water or clothes are. Moreover, they're not general purpose even in the narrow domain of washing - you can't put dishes in a washing machine, nor clothes in a dishwasher (or rather, you can, but you won’t get the result you want). They're just another kind of automation, no different conceptually to a conveyor belt or a pick-and-place machine. Equally, machine learning lets us solve classes of problem that computers could not usefully address before, but each of those problems will require a different implementation, and different data, a different route to market, and often a different company. Each of them is a piece of automation. Each of them is a washing machine. "

This is a great comparison to make.  We thought in the 50's that we'd get robots walking around, but instead we have washing machines, microwaves, dishwashers and so on.  


## [Week in Review Leadership Comms | Lara Hogan](https://larahogan.me/blog/week-in-review/)

[https://larahogan.me/blog/week-in-review/](https://larahogan.me/blog/week-in-review/)



"This Week in Review doc is aimed at teammates who want to gain more context, are frustrated with something that’s happening at the company, or crave some more predictability (one of humans’ core needs at work!)"

This is a great example of how to do internal communications as a manager. Lots of the problems in companies come from inconsistent measaging from managers and I know I’ve failed before where I’ve assumed everyone knows the context or some announcement and it turns out I’ve not communicated it to my team effectively. I think I’ll be doing this in future (when go back to a managerial position rather than consultant I guess)


## [The Amazon machine — Benedict Evans](https://www.ben-evans.com/benedictevans/2017/12/12/the-amazon-machine)

[https://www.ben-evans.com/benedictevans/2017/12/12/the-amazon-machine](https://www.ben-evans.com/benedictevans/2017/12/12/the-amazon-machine)



"This means not so much that products on Amazon are commodities (this is obvious) but that product categories on Amazon are commodities.

This model has two obvious consequences for Amazon. The first is that it can scale almost indefinitely - if you can launch x in y without a meeting or a new org structure, the speed of expansion into new categories is limited mostly by your ability to hire and to procure (and also by consumers’ willingness to buy a new category online, of course)."

This is a great read from Benedict that I think really sums up the Amazon model very well.  I think a lot of people misconstrue the big technology giants, Amazon, Google, Apple, Facebook as being essentially the same, but fundamentally they have very different business models, and it will be interesting to see which ones thrive and prosper more in changing economic climates.


