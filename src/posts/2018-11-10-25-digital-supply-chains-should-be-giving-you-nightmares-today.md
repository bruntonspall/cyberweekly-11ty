---
title: "25 - Digital supply chains should be giving you nightmares today"
date: 2018-11-10
description: "2018 could be remembered for a lot of things, it’s been quite the year after all, but I think its the year in which software supply chain issues came to prominence.  From the Ticketmaster hack to British Airways to SiteCounter, we are seeing increasingly that digital systems are using JavaScript from a variety of sources and nobody has a good grip on how to secure that supply chain, or in many cases, even visualise and understand the supply chain."
permalink: /digital-supply-chains-should-be-giving-you-nightmares-today/
---

2018 could be remembered for a lot of things, it’s been quite the year after all, but I think its the year in which software supply chain issues came to prominence.  From the Ticketmaster hack to British Airways to SiteCounter, we are seeing increasingly that digital systems are using JavaScript from a variety of sources and nobody has a good grip on how to secure that supply chain, or in many cases, even visualise and understand the supply chain.

What we haven’t seen as much of yet is malicious software being injected into the supply chain on the server side, with software forming dependency chains of thousands of packages and very few integrity checks in the system, this is a problem that is wide open today.  I suspect the reason we have fewer attacks here is because the complexity of actually weaponising it into money is far higher than doing the same with third party JavaScript changes.  Criminal elements tend to pick the cheapest and simplest option that they can actually cash out on.

This problem is gigantic, and affects software that is open source as well as closed source, and I think we’re only just beginning to understand the complexity of the situation.  There are no easy simple solutions, and few hard complex solutions that can be seen, so we are just going to have to live with the risk, and engage as many countermeasures as we can in the meantime.

## [Attackers breach web analytics service, go on to target Bitcoin platform](https://www.welivesecurity.com/2018/11/06/supply-chain-attack-cryptocurrency-exchange-gate-io/)

[https://www.welivesecurity.com/2018/11/06/supply-chain-attack-cryptocurrency-exchange-gate-io/](https://www.welivesecurity.com/2018/11/06/supply-chain-attack-cryptocurrency-exchange-gate-io/)

> This piece of code will first check if the URL contains myaccount/withdraw/BTC. Thus, we can already guess that the attackers’ goal is to target a Bitcoin platform. If the check passes, the script continues to add a new script element to the webpage and incorporating the code at https://www.statconuter[.]com/c.php.
> 
> Notice that the attackers registered a domain very similar to the legitimate StatCounter one, statcounter[.]com. They just switched two letters, which can be hard to notice while scanning logs for unusual activity


This is terrifying.  StatCounter is used on thousands of websites, and this could have been far far worse.  What if the attackers had done something to target and extract the browser password databases? If they’d started sniffing and collecting typing done in any username and password field? If they’d used websocket reflection to scan the local machine for open and vulnerable ports?  This could have been much worse, and yet for the attackers, the most valuable thing to do was target one specific currency exchange by poisoning an upstream JavaScript host.

Second minor point, the implication that the domains were visually similar is that we have humans looking at the outgoing logs and verifying whether there is anything weird.  Please don’t do this, a computer algorithm won’t be fooled by the similarity between statcounter and statconuter and can easily highlight that a new domain has been acccessed that wasn’t before.


## [The US Military Just Publicly Dumped Russian Government Malware Online - Motherboard](https://motherboard.vice.com/en_us/article/8xpa7k/us-military-cybercom-publicly-dumped-russian-government-malware-fancy-bear-apt28?utm_campaign=sharebutton)

[https://motherboard.vice.com/en_us/article/8xpa7k/us-military-cybercom-publicly-dumped-russian-government-malware-fancy-bear-apt28?utm_campaign=sharebutton](https://motherboard.vice.com/en_us/article/8xpa7k/us-military-cybercom-publicly-dumped-russian-government-malware-fancy-bear-apt28?utm_campaign=sharebutton)

> Usually it’s the Russians that dump its enemies’ files. This week, US Cyber Command (CYBERCOM), a part of the military tasked with hacking and cybersecurity focused missions, started publicly releasing unclassified samples of adversaries’ malware it has discovered.
> 
> CYBERCOM says the move is to improve information sharing among the cybersecurity community, but in some ways it could be seen as a signal to those who hack US systems: we may release your tools to the wider world.


This is an interesting move.  Within the capable cyber actor sphere, protecting the advanced tooling that they use is a high priority for these teams, and the decision to publicly release the samples means that their activity can be tracked, can be DfE ded against, and means that when launching an offensive mission, the team need to weigh up the cost of losing a valuable tool compared to the mission goals.  This might result in fewer attacks by these capable teams...

However, it also releases complex tools and techniques which filter down into less capable hackers hands, and increases the ability of criminals and independent hackers to be able to carry out offensive cyber operations.

Finally, there’s also a trust exercise here.  If commercial security companies use these malware variants to track a teams online movements, then there might be value in CYBERCOM releasing malware variants that they’ve used and created but attributing them to a foreign attacker, which would create confusion and hide their own activities.  The likelihood of this happening feels very low at the moment, but it will be at the back of researchers minds I’m sure.


## [Speed Up AppSec Improvement With an ...](https://www.darkreading.com/application-security/speed-up-appsec-improvement-with-an-adversary-driven-approach/d/d-id/1333185)

[https://www.darkreading.com/application-security/speed-up-appsec-improvement-with-an-adversary-driven-approach/d/d-id/1333185](https://www.darkreading.com/application-security/speed-up-appsec-improvement-with-an-adversary-driven-approach/d/d-id/1333185)

> According to researchers James Wickett and Shannon Lietz, AppSec faces an epistemological problem for developers and security to figure out.  
> 
> "What's the problem? We don't even know if we're chasing the right things," said Wickett, researcher with the firm Signal Science "We have to ask the question, 'Is what we're testing driving us toward finding the right issues?'" 
> 
> Wickett stepped up to the podium with Lietz last week at DevOps Enterprise Summit to describe to a developer-heavy audience why they believe organizations need to start refocusing security fix priorities based on adversary behavior—rather than sticking solely with standards like the OWASP Top 10, which often don't account for the exigencies of real-world attack patterns.  


I’ve long been a proponent of attacker driven security assessment methods.  But I think they have to be paired with a simple baseline of security measures as well.


## [Troy Hunt: Here's Why [Insert Thing Here] Is Not a Password Killer](https://www.troyhunt.com/heres-why-insert-thing-here-is-not-a-password-killer/)

[https://www.troyhunt.com/heres-why-insert-thing-here-is-not-a-password-killer/](https://www.troyhunt.com/heres-why-insert-thing-here-is-not-a-password-killer/)

> Every single solution I've seen that claims to "solve the password problem" just adds another challenge in its place thus introducing a new set of problems.


I agree with Troy here.  While I’m a huge fan of email loops for authentication, it requires a significant degree of friction that passwords don’t.

The same for U2F yubikeys, which have the issue of not fitting into all my computers (I bought 2 an NFC/USB-A model and a USB-C model, neither work with my iPad), or can be forgotten or otherwise inaccessible.


## [Troy Hunt: When Accounts are "Hacked" Due to Poor Passwords, Victims Must Share the Blame](https://www.troyhunt.com/when-accounts-are-hacked-victims-must-share-the-blame/)

[https://www.troyhunt.com/when-accounts-are-hacked-victims-must-share-the-blame/](https://www.troyhunt.com/when-accounts-are-hacked-victims-must-share-the-blame/)

> If I crash my car after driving like a lunatic, I am both a victim and worthy of blame. If I pat the poisonous things in my Aussie back yard and get bitten it's the same again. DON'T PAT THE POISONOUS THINGS! My kids understand this, why are some adults struggling with the cause and effect of poor password choices? I


This is an interesting argument, but one that I disagree with.  The reason that people learn that driving badly causes crashes and that patting animals gets you bitten is because the cause and effect are directly observable.  One only has to be bitten or nearly bitten to see the effect with your own eyes.

But if I choose a weak password on adobe, and then my twitter account gets hijacked a year later, the cause and effect is hidden from the user and as such there’s no feedback or improvement in user behaviour.

So blame the victims all you want, and maybe they made bad decisions, but currently I see no way for them to subjectively know that it was a bad decision that would have that impact.


## [Santa Claus & the General Data Protection Regulation (GDPR)](https://medium.com/@joelgsamuel/santa-claus-the-general-data-protection-regulation-gdpr-57f1571e7de8)

[https://medium.com/@joelgsamuel/santa-claus-the-general-data-protection-regulation-gdpr-57f1571e7de8](https://medium.com/@joelgsamuel/santa-claus-the-general-data-protection-regulation-gdpr-57f1571e7de8)

> That the data is up to date and needs to be kept
> Santa likely gets his data from governmental records (registering a birth workflows etc) — although I do suspect this is ‘extra legal’ due to lack of formal data sharing capabilities.
> I would strongly recommend Santa create the North Pole as a territory and achieve UN recognition, in order to then setup data sharing agreements with each target country.
> Once Santa holds this birth information, he can calculate age. But he needs to keep addresses up to date, so likely is buying copies of electoral data through data brokers who aren’t too worried about legal jurisdictions. Address data is parent/guardian linked, so he clearly has access to a plethora of education, social care and local state/authority data to be able to consistently link a Data Subject child with parents/guardians.
> Using ‘extra legal’ means Santa may be re-washing his data with other data sources (other government databases etc) in order to keep things as accurate as he can — as data matching is hard and a single-source of truth is very difficult to find.


Joel does somewhat spoil the magic of Christmas with this excellent analysis of how Santa might keep and maintain his list in an age of GDPR.  Thoroughly enjoyable read (and given it’s about GDPR that’s saying something!)


## [National Insider Threat Task Force (NITTF)](https://www.dni.gov/index.php/ncsc-how-we-work/ncsc-nittf)

[https://www.dni.gov/index.php/ncsc-how-we-work/ncsc-nittf](https://www.dni.gov/index.php/ncsc-how-we-work/ncsc-nittf)

> NEW: The National Threat Task Force (NITTF) released the Insider Threat Program Maturity Framework on November 1, 2018. The Framework is an aid for advancing federal agencies’ programs beyond the Minimum Standards, and builds upon best practices found in the 2017 NITTF Insider Threat Guide. The goal is to help programs become more proactive, comprehensive, and better postured to deter, detect, and mitigate insider threat risk.


Insider threats are a really interestingly difficult problem.  Much of the activity that a hostile insider might do also looks like users using shadow technology to work around poor it.

If you insider threat detection just further locks down your staff, preventing them doing their job, then it will create increased frustration and lower morale, which is of course a breeding ground for hostile insiders.

But anyway, the framework might be worth a read if you manage an insider program to get a good idea of the sorts of capabilities you might want to measure.


## [How to Build a Culture of Cyberdefenders](https://www.business.com/articles/build-culture-of-cyberdefenders/)

[https://www.business.com/articles/build-culture-of-cyberdefenders/](https://www.business.com/articles/build-culture-of-cyberdefenders/)

> Keep in mind that any instances of poor cyber-hygiene don't need to be immediately reprimanded. Instead, they should serve as teachable moments. For example, when an employee brings up a potential cybersecurity incident, taking the conversation from "you shouldn't have done that" to "thank you for letting me know" can go a long way in building trust and transparency.
> 
> If an employee does something right, recognize it by sending a message to your team: "Big thank-you to Ashley – she found a USB drive left in the conference room and brought it to IT to be scanned!"
> 
> Your goal should be to develop the "if you see something, say something" mentality. Cybersecurity is a top-to-bottom, all-departments commitment. Get buy-in from everyone on your team that they'll do their best to follow, encourage and enforce good habits across the board.


This riff on creating a security culture is quite a good summary.  Obviously a security culture in the entire organisation isn’t sufficient alone, and I’m especially dubious about mandating security training for all staff given the poor quality of most security training, but it’s a start.

If you do this, you need to ensure that your security team is encouraging this culture and working with it, providing your staff with tools, training and a happy smiling helpful face when approached.


## [What we say isn’t what they hear](https://niksilver.com/2018/11/06/ambiguous-communication/)

[https://niksilver.com/2018/11/06/ambiguous-communication/](https://niksilver.com/2018/11/06/ambiguous-communication/)

> The team had got about half way into their first day of implementation when it was called to a halt. There was much frustration from within the team, mainly directed at the product function. They had spent at least two and half days estimating, detailing and implementing the work. They could have stopped it after only a couple of hours when they realised it was going to take more than a week.
> 
> You might think “You’ve got a week” is a clear message, but rightly or wrongly it obviously wasn’t. The Head of Product intended it to mean, “Don’t do it if it’s more than a week,” and the Product Manager heard it as, “The earlier, rough estimate was about a week.”


Good reminder that human communication is really really hard.  What you think you are saying often isn’t what the recipients actually hear.  This gets made worse in some tressful situations such as during a major incident. Active listening and asking questions to play back the understanding can help ensure that you have both communicated clearly.


## [list of specification gaming examples in AI: unintended solutions to the specified objective that don't satisfy the designer's intent](https://docs.google.com/spreadsheets/u/1/d/e/2PACX-1vRPiprOaC3HsCf5Tuum8bRfzYUiKLRqJmbOoC-32JorNdfyTiRRsR7Ea5eWtvsWzuxo8bjOxCG84dAg/pubhtml)

[https://docs.google.com/spreadsheets/u/1/d/e/2PACX-1vRPiprOaC3HsCf5Tuum8bRfzYUiKLRqJmbOoC-32JorNdfyTiRRsR7Ea5eWtvsWzuxo8bjOxCG84dAg/pubhtml](https://docs.google.com/spreadsheets/u/1/d/e/2PACX-1vRPiprOaC3HsCf5Tuum8bRfzYUiKLRqJmbOoC-32JorNdfyTiRRsR7Ea5eWtvsWzuxo8bjOxCG84dAg/pubhtml)

> A cooperative GAN architecture for converting images from one genre to another (eg horses<->zebras) has a loss function that rewards accurate reconstruction of images from its transformed version; CycleGAN turns out to partially solve the task by, in addition to the cross-domain analogies it learns, steganographically hiding autoencoder-style data about the original image invisibly inside the transformed image to assist the reconstruction of details.
> 
> Creatures bred for speed grow really tall and generate high velocities by falling over
> 
> Genetic debugging algorithm GenProg, evaluated by comparing the program's output to target output stored in text files, learns to delete the target output files and get the program to output nothing.
> Evaluation metric: “compare youroutput.txt to trustedoutput.txt”. 
> Solution: “delete trusted-output.txt, output nothing”


Some lovely examples of AI solving the problem given to it in a very literal and occasionally creative manner.  Remember this every time a vendor tells you how their amazing AI driven solution will make all your problems go away.


