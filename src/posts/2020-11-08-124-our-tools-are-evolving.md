---
title: "124 - Our tools are evolving"
date: 2020-11-08
description: "Security tooling has always been a little... peculiar."
permalink: /our-tools-are-evolving/
---

Security tooling has always been a little... peculiar.

Part of this comes from the fact that security isn't one culture, it's a mix of compliance officers, architects, hackers and analysts, and so it's rare than one tool fits everyones need.  Secondly, many of the people involved in security don't have software development experience, and so tools have tended to either be vendor driven, or dedicated to the sections of the community that does have software development experience (hackers mostly).

But over the last few years, the DevOps revolution has bought in lots of platform teams, product teams and has given the tangential security teams access to and awareness of the automated tooling that exists in those areas.  Security and "SecOps" is following, with security people demanding better and better tools, but also adding security features to the existing DevOps tools.

This growth means that there are more and more tools out there, many of them custom built to scratch the itch of a security engineer in one company, but the maturity of this market is moving and changing.  If you don't have security engineers in your security team, who are looking at these tools, evaluating them, and working with your operations and developer teams to implement them, then you are going to be left behind.

## [Scale Summit 2019](https://www.scalesummit.org/)

[https://www.scalesummit.org/](https://www.scalesummit.org/)

> An online event about scale and scalability.
> Friday 13 November 2020
> 
> With talks confirmed:
> 
> Scale, Microservices and Flow - James Lewis, Thoughtworks
> 
> Scaling Your Impact at Work: Beyond the Purely Technical - Nigel Kersten, Puppet
> 
> Improving the Reputation of HMRC by Giving Away Money at Scale - Ben Conrad, HMRC
> 
> A Practical Guide to Load Testing in Production - Hassy Veldstra, Shoreditch Ops


I don't generally shill things in my newsletter, partly because nobody wants to pay me to, but also because that's not really why I write it.

But I help organise and run this conference, and if you are interested in some brilliant talks by smart people that looks at how we scale interesting systems, then this would be right up your alley!


## [WeWork employees used an alarmingly insecure printer password | TechCrunch](https://techcrunch.com/2020/11/01/wework-employees-used-an-alarmingly-insecure-printer-password)

[https://techcrunch.com/2020/11/01/wework-employees-used-an-alarmingly-insecure-printer-password](https://techcrunch.com/2020/11/01/wework-employees-used-an-alarmingly-insecure-printer-password)

> WeWork customers like Elsley normally have an assigned seven-digit username and a four-digit passcode used for printing documents at WeWork locations. But the username for the account used by WeWork employees was just four-digits: “9999”. Elsley told TechCrunch that he guessed the password because it was the same as the username. (“9999” is ranked as one of the most common passwords in use today, making it highly insecure.)
> 
> The “9999” account is used by and shared among WeWork community managers, who oversee day-to-day operations at each location, to print documents for visitors who don’t have accounts to print on their own. The account cannot be used to access print jobs sent to other customer accounts.


This is just a *headdesk* moment really.  The same password as username, and a shared common account rather than providing community managers with their own accounts to do this stuff with?


## [asset forfeiture.pdf - Google Drive](https://drive.google.com/file/d/1vjeItUFfuL-U0plUiKYgMxSqZznynsIA/view)

[https://drive.google.com/file/d/1vjeItUFfuL-U0plUiKYgMxSqZznynsIA/view](https://drive.google.com/file/d/1vjeItUFfuL-U0plUiKYgMxSqZznynsIA/view)

> 22. Individual X was the individual who moved the cryptocurrency from Silk Road. According to the investigation, Individual X was able to hack into Silk Road and gain unauthorized and illegal access to Silk Road and thereby steal the illicit cryptocurrency from Silk Road and move it into wallets that Individual X controlled. According to the investigation, Ulbricht became aware of Individual X’s online identity and threatened Individual X for return of the cryptocurrency to Ulbricht. Individual X did not return the cryptocurrency but kept it and did not spend it.
> 
> 23. On November 3, 2020, Individual X signed a Consent and Agreement to Forfeiture with the U.S. Attorney’s Office, Northern District of California. In that agreement, Individual X, consented to the forfeiture of the Defendant Property to the United States government.
> 
> 24. On November 3, 2020, the United States took custody of the Defendant Property from 1HQ3.


As had been noted a number of years ago, someone managed to steal around 69,000 bitcoins from SilkRoad.  That's somewhere around £800m in cash, or a touch over $1b (give or take a few million).  

The US Govenrment just seized it, with the help of the person who stole it from Silk Road.  I wonder what agreement that took to give it up?  I suspect they realised that they would never be able to cash it out in any form.


## [2020 CYBER THREATSCAPE REPORT [pdf]](https://www.accenture.com/_acnmedia/PDF-136/Accenture-2020-Cyber-Threatscape-Full-Report.pdf)

[https://www.accenture.com/_acnmedia/PDF-136/Accenture-2020-Cyber-Threatscape-Full-Report.pdf](https://www.accenture.com/_acnmedia/PDF-136/Accenture-2020-Cyber-Threatscape-Full-Report.pdf)

> Cyberthreat actors continue to focus compromise attempts against entities in their
> victims’ supply chains. This practice is most common among state-sponsored groups
> but organized criminal groups increasingly show the same patterns of behavior.
> 
> Most reported incidents, as in years past, show evidence of “vertical” targeting,
> such as the compromise of managed service providers and software vendors.
> 
> Increasingly, cyberthreat campaigns exploit “horizontal” supply chains, taking
> advantage of direct connectivity between peer organizations working on joint projects.
> 
> Sophisticated cyberthreat actors have employed “island-hopping” techniques— compromising small firms to gain access to their larger partners—to bypass strong perimeter defenses in various industry sectors including aerospace, automotive, defense and nuclear.


This is an interesting report.  Accenture bought Context Security, and Deja vu Security last year, and this has improved their cyber security expertise, especially in the realm of cyber incident response.  Much of what is in here matches what you'll see elsewhere, CV-19 causes a rise in working from home, attackers are using ransomware and so on.

But this section detailing the concerns around the supply chain, and in particular demosntrating that companies are being exploited through their managed service providers and other underlying suppliers (vertical supply chain compromise) as well as through partnership arrangements (horizontal supply chain compromise).  This is an area that I think we'll see growing over the next few years, as Accenture says here.  It's not common right now, but ransomware operators and other "access for hire" groups will start noting that onward connectivity might be almost as valuable as the data within an organisation.  


## [Finally: a usable and secure password policy backed by science](https://www.cylab.cmu.edu/news/2020/10/20-passwordpolicy.html)

[https://www.cylab.cmu.edu/news/2020/10/20-passwordpolicy.html](https://www.cylab.cmu.edu/news/2020/10/20-passwordpolicy.html)

> Equipped with this state-of-the-art password meter, the researchers then approached password policies from a whole new perspective: with the idea that a password must achieve a certain threshold score on their password meter. This new perspective led the researchers to discover a threshold between password strength and length—one that causes users to create passwords that are both stronger and more usable than they would under common password policies.
> 
> To reach this discovery, the researchers conducted online experiments, evaluating combinations of minimum-length requirements, character-class requirements, minimum-strength requirements, and password blocklists—lists of words that shouldn’t be allowed to be used in passwords due to their common use.
> 
> In the online experiments, study participants were asked to create and recall passwords under randomly assigned password policies. First, participants assumed the role of someone whose email provider had been breached and needed to create a new password according to their assigned policy. Then, a few days later, they were asked to recall their password as a way to measure the usability of the password policy.
> 
> ... a minimum strength and a minimum length of 12 characters achieved a good balance between security and usability.Nicolas Christin, Associate Professor, EPP and ISR
> “We found that a policy requiring both a minimum strength and a minimum length of 12 characters achieved a good balance between security and usability,” says Nicolas Christin, a professor in ISR and EPP.
> 
> Although blocklist and minimum-strength policies can produce similar results, minimum-strength policies are flexibly configured to a desired security level, and they are easier to deploy alongside real-time requirements feedback in high-security settings.


This is interesting, but a little worrying.  I'm not entirely convinced that [the research](http://www.andrew.cmu.edu/user/nicolasc/publications/Tan-CCS20.pdf) matches exactly what is being outlined here, so lets break this into two parts.

First the good news.  They find that 

> how users pick passwords has changed over time, and that this, in combination with advances in password guessing, implies that requiring passwords to have multiple character classes brings at best minor benefit to password strength".  

Additionally, they find that users who are asked to remember passwords with complexity rules find it harder to do so than those who simply have to remember long passwords.  Additionally, they found that blocklists, while effective, when implemented alone, can cause users to swap a strong but blocked password for a much weaker, but not blocked password.

The most interesting finding is this bit...

> But while minimum-strength policies can be strengthened against offline attacks by either increasing the minimum required length or the minimum number of character classes, increasing the minimum length accomplishes this at a lower usability cost, in terms of how long users need to create a compliant password and how annoying or challenging they find that task.

Now the bad news... 

The neural network password meter caused users to voluntarily seem to select passwords with more classes than without it.  That is to say, when users see a "strength meter", they start choosing to add symbols and numbers and things to their passwords anyway.  They also note that over time (since their 2016 study), users have started creating more complex passwords anyway, potentially because they've been trained by all these websites with complexity requirements. (People's passwords have also gotten longer in the last 4 years too).  I'm not sure that relying on users selecting more classes is good for password complexity.  Their study is clear that longer passwords are by far the hardest to crack, and that the best action to improve security is to add more characters or words to the password.  The variety or password complexity in here is inherant rather than explicit, and I'm not comfortable with that.

Finally, the Neural Network tool is not well explained.  It's unclear just how it works, and that lack of visibility worries me.  How do we know how it's picking hard passwords?  Because the neural network is inherently inexplicable, this creates a user experience problem where users might be told that their chosen password is weak, but unable to be told how to make things better.


## [Andrzej Dyjak on Twitter: "Couple of days ago I conducted a small experiment WRT secrets commited to public git repositories. My plan was simple: (1) Generate a secret, (2) commit it to the public repository, and (3) see what happens. Thread time! 👉 1/8" / Twitter](https://twitter.com/andrzejdyjak/status/1324360905237372929)

[https://twitter.com/andrzejdyjak/status/1324360905237372929](https://twitter.com/andrzejdyjak/status/1324360905237372929)

> 


This is a great thread about how long it takes for a committed secret to a git repository to be abused.  The answer... about 11 minutes.



## [Patterns for secure container base image management - Speaker Deck](https://speakerdeck.com/garethr/patterns-for-secure-container-base-image-management?slide=32)

[https://speakerdeck.com/garethr/patterns-for-secure-container-base-image-management?slide=32](https://speakerdeck.com/garethr/patterns-for-secure-container-base-image-management?slide=32)

> Presentation from SnykCon 2020, all about the people, process and tools needed to manage container base images. Thoughts about team organisation, trade-offs and examples of how to use Snyk to solve this problem.


I covered the Open Policy Agent back in [CyberWeekly #104](https://cyberweekly.net/developing-compliance), but Gareth manages here to really explain how you can implement it, and what the value is.  

While I've jumped into the second part of this talk, covering creating policies to gatekeep your kubernetes installations, the first section of the talk, looking at how you should be structuring your SRE teams and how security can be involved is also worth looking at.

SnykCon was excellent generally, and they are putting up many of the [videos on Youtube](https://www.youtube.com/playlist?list=PLQ6IC7glz4-UYj6uCRPCGhyxgppk-7W2V) that you can watch for free as well


## [The Infosec Apocalypse](https://blog.rickasaurus.com/2020/08/31/The-Infosec-Apocalypse.html)

[https://blog.rickasaurus.com/2020/08/31/The-Infosec-Apocalypse.html](https://blog.rickasaurus.com/2020/08/31/The-Infosec-Apocalypse.html)

> Just this past year I’ve come to see we’re in the middle of a massive change across the industry. There are new forces at play which will calcify current software stacks and make it extremely hard for existing or new entrants to see similar success without a massive coordinated push backed by big enterprise companies. This force is the rise of InfoSec and vulnerability detection tooling.
> 
> Tools like Blackduck, WhiteSource, Checkmarx, Veracode are exploding in popularity, there are too many to list and many variations on the same theme. In the wake of so many data leaks and hacking events enterprises no longer trust their developers and SREs to take care of security, and so protocols are being implemented top down. This isn’t just on the code scanning side, there is a similar set of things going on with network scanning as well which impacts programming languages less, but similarly will calcify server stacks.
> 
> These tools are quickly making their way into SOC2 and SDLC policies across industry, and if your language or new infrastructure tool isn’t supported by them there’s little chance you will get the previously already tenuous approval to use them. This sets the already high bar for adoption much higher. As you might expect, vendors will only implement support for languages that meet some threshold for profitability of their tools. Not only do you need to build a modern set of tools for your language to compete, now you also need support from external vendors.


As the access to modern security tooling grows, so does the assumption that your suppliers will use them.  

How much this gets baked into contracts will depend on corporate appetite, but I think the current experience of assuming that "good practice" is actually consistent amongst organisations is something that will change over time.  Where this might not take on as much as the author says is the fact that the industry really doesn't have a consistent view of "good practice" yet.  Practices vary enourmously across different sectors, and the capability gap is huge. 


## [Welcome to ThreatPursuit VM: A Threat Intelligence and Hunting Virtual Machine | FireEye Inc](https://www.fireeye.com/blog/threat-research/2020/10/threatpursuit-vm-threat-intelligence-and-hunting-virtual-machine.html)

[https://www.fireeye.com/blog/threat-research/2020/10/threatpursuit-vm-threat-intelligence-and-hunting-virtual-machine.html](https://www.fireeye.com/blog/threat-research/2020/10/threatpursuit-vm-threat-intelligence-and-hunting-virtual-machine.html)

> ThreatPursuit Virtual Machine (VM) is a fully customizable, open-sourced Windows-based distribution focused on threat intelligence analysis and hunting designed for intel and malware analysts as well as threat hunters to get up and running quickly. The threat intelligence analyst role is a subset and specialized member of the blue team. Individuals in this role generally have a strong impetus for knowing the threat environment. Often their traits, skills and experiences will vary depending on training and subject matter expertise.
> 
> Their expertise may not be technical and may include experiences and tradecraft earned by operating within a different domain (e.g., geospatial, criminal, signals intelligence, etc.). A key aspect of the role may include the requirement to hunt, study and triage previously undiscovered or recently emerging threats by discerning data for evil. Threat analysts apply a variety of structured analytical methods in order to develop meaningful and relevant products for their customers.
> 
> With this distribution we aim to enable users to:
> 
> Conduct hunting activities or missions
> Create adversarial playbooks using evidence-based knowledge
> Develop and apply a range of analytical products amongst datasets
> Perform analytical pivoting across forensic artifacts and elements
> Emulate advanced offensive security tradecraft
> Enable situational awareness through intelligence sharing and reporting
> Applied data science techniques & visualize clusters of symbolic data
> Leverage open intelligence sources to provide unique insights for defense and offense


Pentesters and red teams get Kali linux, a virtual machine containing all the cool scan and attacking tools that you might need.  So FireEye have produced a defenders virtual machine, providing all the tools that they need.


