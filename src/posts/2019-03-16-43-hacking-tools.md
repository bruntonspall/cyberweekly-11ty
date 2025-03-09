---
title: "43 - Hacking Tools"
date: 2019-03-16
description: "I'm not actually a very good hacker.  I know and understand a lot of the theory, and I've been on web application hacking courses, played at a few Cybergames, and while I don't come first, I don't do terribly."
permalink: /hacking-tools/
---

I'm not actually a very good hacker.  I know and understand a lot of the theory, and I've been on web application hacking courses, played at a few Cybergames, and while I don't come first, I don't do terribly.

But hacking tools fascinate me because it's an entire industry of tooling, of software development, that has very different use cases, users and coding requirements to enterprise software or web applications.

I wish more hacking tooling was automatable, and that was one of the things among many that made my ears prick up at the NSA releasing Ghidra.

When it was released there was a lot of noise on twitter about the fact that when run in debug mode, it opened a port that enabled someone to remotely control the software and because it includes a shell, the machine itself.  This was seen as a security flaw, or a deliberate backdoor into the software.  But I think huge numbers of penetration testers and "hackers" work alone, they don't work in teams, and they don't understand the need for tools that can be scripted, that can be remotely controlled and can be put on shared infrastructure.  Whether that was the case for this issue is another matter, but Ghidra specifically calls out that it is designed to be used by teams.

I've had a bunch of other links to tools hanging around for a while, and I was unsure whether or not to include them.  These are either tools that got released that I liked the look off, or something I use when playing at hacking contests.  They're included here because I've found them useful both in practice, but often as a way to get a better understanding of bits of computer security that I don't understand properly.

I hope you find them useful, and if you would like to see more tools included as part of this newsletter, then please let me know via email or twitter, and feel free to send me tools you think are worth pointing out, as I run across a lot less of them than I do interesting articles.

Also, finally, I made mention of bridges collapsing last week, that's because there was an article about it that I forgot to include in the links. Doh!  It's an interesting off topic article, and so I've included it this week, just so it makes a bit more sense.

## [The Disruption Machine - What the gospel of innovation gets wrong.](https://www.newyorker.com/magazine/2014/06/23/the-disruption-machine)

[https://www.newyorker.com/magazine/2014/06/23/the-disruption-machine](https://www.newyorker.com/magazine/2014/06/23/the-disruption-machine)

> Disruptive innovation can reliably be seen only after the fact. History speaks loudly, apparently, only when you can make it say what you want it to say. The popular incarnation of the theory tends to disavow history altogether. “Predicting the future based on the past is like betting on a football team simply because it won the Super Bowl a decade ago,” Josh Linkner writes in “The Road to Reinvention.” His first principle: “Let go of the past.” It has nothing to tell you. But, unless you already believe in disruption, many of the successes that have been labelled disruptive innovation look like something else, and many of the failures that are often seen to have resulted from failing to embrace disruptive innovation look like bad management.


I'm a big fan of Clayton Christianson's "Disruption" process, but this is a really well argued position against it, that says that he selected case studies that fit his particular worldview, and that it doesn't apply everywhere.

I do like the note that disruption is obvious in retrospect but much harder to see ahead of time.  I had always felt that Christianson had argued this, but as pointed out, there is now entire industries of "Chief Innovation Officers" who see it as their job to spot disruption before it happens.


## [Ghidra](https://ghidra-sre.org/)

[https://ghidra-sre.org/](https://ghidra-sre.org/)

> 


The NSA released it's reverse engineering tool at RSA Conference a little over a week ago, and I didn't have time to have a proper look at it for last week.  This is big news for two main reasons.

The first is that IDAPro, the current market leader in reverse engineering tools has been around for a while, is considered expensive, and hasn't had that many improvements over the last few years.  It's really good to have an open source tool that delivers in the same area, has some weight behind it, and will continue to evolve.  This should push IDAPro to add features or capabilities that demonstrate the value and worth.
The fact that it's free makes it far easier for hobbyists, amateurs and people who want to get into the industry, get the tool and use it.  This isn't a cut down, half featured free tool, it's actually really good and used within the NSA for malware analysis amongst other things.

Secondly, the constant battle to get software open sourced is often held up by security people claiming that security tooling and security related code cannot be released.  This is an active operational tool, used by the NSA.  Any bugs found in it, could in theory be exploited on NSA Analysts computers (if you can get code there!  Good luck).  If the NSA can open source this, then it's a good challenge to other teams around the world that their code/systems etc aren't "as secure as the NSA's". [Note: That's a slightly facetious argument, but then so is the challange that code cannot be open sourced or public because "security"]


## [GTFOBins](https://gtfobins.github.io/)

[https://gtfobins.github.io/](https://gtfobins.github.io/)

> 


A lovely list of unix binaries that can be used to break out of restricted shells, or escalate privileges.  It's common on certain unix systems to prevent you from running certain security tools, or binaries that aren't on the system path.  But many many common unix tools can spawn a shell, which can often be used to get around the restrictions, or occasionally used to present a shell interpreter back to the attacker over a network connection.


## [CyberChef](https://gchq.github.io/CyberChef/)

[https://gchq.github.io/CyberChef/](https://gchq.github.io/CyberChef/)

> 


Probably my favourite tool, since I'm a terrible actual hacker, this does a lot of the stuff I need to handle the sorts of things that come up in challanges and contests that are always fun to enter.  

The new "Magic" option is quite cute in that it tries to guess what forms of decryption/modification would be necessary to get sensible plaintext out, which is especially handy if you know that the crib you are looking for is "flag:"


## [swisskyrepo/PayloadsAllTheThings: A list of useful payloads and bypass for Web Application Security and Pentest/CTF](https://github.com/swisskyrepo/PayloadsAllTheThings)

[https://github.com/swisskyrepo/PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings)

> 


Another nice tool for penetration testers or challenges.  This is a list of various payloads for web application security, so XSS strings, or injection strings.  But even nicer, if you look, is that there are some lovely XSS Polyglot injections, that is script tags that use unusual characters and will break almost all blacklisting implementations.  Additionally, there are some breakdowns, so you can see how the polyglot string works and why it won't be detected.  Useful in practice and as a learning tool


## [How to Discover MongoDB and Elasticsearch Open Databases](https://habr.com/en/post/443132/)

[https://habr.com/en/post/443132/](https://habr.com/en/post/443132/)

> 


This is a nice overview of using Shodan to search for open databases, the sorts of ones that you heard about in the last few megaleaks.  Shodan is a lovely little tool, nice and cheap, and of course not the only tool, but should possibly form part of your security monitoring.  Search for yourself before someone else finds your misconfigured database.


## [Dliv3/Venom: Venom - A Multi-hop Proxy for Penetration Testers Written in Go](https://github.com/Dliv3/Venom)

[https://github.com/Dliv3/Venom](https://github.com/Dliv3/Venom)

> 


This is a lovely cute tool for traversing networks.  That system you have where you have a bastion host, and seperate network segments?  This tool allows you to encode different connections as a transport, and then you simply connect to one end, and it acts as a transparent pipe, injecting your commands into the destination host, exactly as you want.


## [25% of software vulnerabilities remain unpatched for more than a year [Autoplay video]](https://www.techrepublic.com/article/25-of-software-vulnerabilities-remain-unpatched-for-more-than-a-year/)

[https://www.techrepublic.com/article/25-of-software-vulnerabilities-remain-unpatched-for-more-than-a-year/](https://www.techrepublic.com/article/25-of-software-vulnerabilities-remain-unpatched-for-more-than-a-year/)

> The duo propose the metric of "remediation velocity" to measure the survival timeline of vulnerabilities, focusing on a measurement of how many days it takes to reach 25%, 50%, or 75% of vulnerabilities closed, measured in a particular aspect. Across all of the organizations analyzed, it took an average of 26 days to reach 25% closed, 100 days to reach 50% closed, and 392 days to reach 75%.
> 
> [...]
> 
> Oracle, HP, and IBM products left relatively unprotected. The report notes that "there are many possible reasons behind these dramatic differences. Java (Oracle) is notoriously hard to fix without breaking something. Apple might have fewer vulnerabilities than Microsoft, but their enterprise management support lags. Google updates frequently, but many forget to restart their browsers. Overall, though, we view [these results] as strong evidence in favor of scheduled releases and the automated distribution of patches."
> 
> [...]
> 
> Smaller organizations were observed to patch vulnerabilities faster, for which the report states "many assume fewer resources would translate to reduced capacity to remediate vulnerabilities, smaller firms generally reach each time-to-fix milestone faster than their medium and large counterparts... [the finding] probably says less about remediation capacity and more about the compounding difficulty of managing larger IT environments."


Patching.  I'll keep saying it until it gets better, it's the single most important security function you can do.  DevOps, Continuous Deployment and Agile can help here.

But there's a good point at the end.  Smaller companies have less legacy and smaller environments, which means they can patch faster and more confidently.  Our structures for managing infrastructure, whether Agile or ITIL based, really don't scale well, as Equifax can attest to, sending emails to 400 "infrastructure managers" that there's a struts vulnerability doesn't necessarily mean everyone can and does patch it.


## [Man arrested for selling one million Netflix, Spotify, Hulu passwords](https://hotforsecurity.bitdefender.com/blog/man-arrested-for-selling-one-million-netflix-spotify-hulu-passwords-20960.html)

[https://hotforsecurity.bitdefender.com/blog/man-arrested-for-selling-one-million-netflix-spotify-hulu-passwords-20960.html](https://hotforsecurity.bitdefender.com/blog/man-arrested-for-selling-one-million-netflix-spotify-hulu-passwords-20960.html)

> The account passwords, however, were not obtained via legitimate means. Instead the details were typically obtained through credential stuffing using swathes of usernames and passwords leaked through other data breaches, without the knowledge of their genuine owners.


Password stuffing is a real problem and is only going to get worse.  Most normal people have little to no awareness of password managers and don't use them.  Worse still, infosec guidance is often worse than useless in this area, with many info sec professionals still arguing that since password managers aren't perfect, they shouldn't be used, forgetting that many people use the same easy to crack password on all their accounts everywhere.

I don't know what the solution is, replacing passwords with some form of FIDO token isn't going to get mass market adoption soon, password managers are similarly low on adoption figures (although higher than I thought they were), and password advice remains pretty poor.  Expect to see a lot more of this stuff.


## [“If you want, I can store the encrypted password." A Password-Storage Field Study with Freelance Developers [pdf]](https://net.cs.uni-bonn.de/fileadmin/user_upload/naiakshi/Naiakshina_Password_Study.pdf)

[https://net.cs.uni-bonn.de/fileadmin/user_upload/naiakshi/Naiakshina_Password_Study.pdf](https://net.cs.uni-bonn.de/fileadmin/user_upload/naiakshi/Naiakshina_Password_Study.pdf)

> A fair number of our freelancers argued that they trust standards and third party APIs to do the right thing and store passwords securely (P8100 , P9200 , N11100 , P3200 , N2100 , P2100 , N4100 , P11200 , P12200 ). However, this trust is sometimes misplaced. While P8100 and P9200 indeed used in- dustry standards for security and thus received 6 of 7 points, almost all of the other participants used MD5 as a “standard” for password storage. 


Standards.  That byword for all that is good.  Interestingly, in my experience, competent and capable people are enabled by good standards, it helps them "not have to think", because they know that if they use a standard system, that they've get a reasonable outcome.  However, the competence comes from the ability to select the appropriate standard, and very few standards and guidance ever give context to when it's appropriate to apply this standard.  This harms people who are not competent at the time of picking the standard to follow.

Also bear in mind that competence is relative and temporal.  I can be an outstanding software developer and know nothing about cryptographic routines and wether MD5 is a good selection or not.  I can be temporarily mentally impaired, say drunk or hungover, or distracted by other things on my plate and not giving my full attention.  Standards that are good, are easy for people who are incompetent to apply appropriately or at minimum to recognise inappropriate use therefore.


## [Redditors Say They’re Seeing Coordinated Chinese Propaganda On The Site https://t.co/71lSsJEeuy by @CraigSilverman + @JaneLytv](https://www.buzzfeednews.com/article/craigsilverman/reddit-coordinated-chinese-propaganda-trolls)

[https://www.buzzfeednews.com/article/craigsilverman/reddit-coordinated-chinese-propaganda-trolls](https://www.buzzfeednews.com/article/craigsilverman/reddit-coordinated-chinese-propaganda-trolls)

> Bishop said it’s often difficult to separate which part of the activity on Reddit or elsewhere is simply Chinese people who are “patriotic and just taking it on themselves” to support the country, and how much is coordinated by the government or related entities.
> 
> “It’s really difficult to see which is which,” he said.


Another view on the continuing discussion of "influence operations" and a nice insight or reminder here.  It's incredibly difficult to tell the difference between coordinated activity and spontaneous similar activity by similarly inclined actors.

There's also a note from Reddit saying that they hadn't noticed any indications of automated activity, which suggests to me that their detection capabilities are looking for the wrong thing.

Bearing in mind that this form of positive message influence is a deliberate strategy, there should be some low level automated activity going on, even if the majority in this case was "patriotic citizens", and so you'd expect to have found some evidence of automated activity, even if not enough to suggest that all up-voting is subject to influence.


## [Huawei Lawsuits Showcase China's Foreign PR Drive - Bloomberg](https://www.bloomberg.com/opinion/articles/2019-03-10/huawei-lawsuits-showcase-china-s-foreign-pr-drive)

[https://www.bloomberg.com/opinion/articles/2019-03-10/huawei-lawsuits-showcase-china-s-foreign-pr-drive](https://www.bloomberg.com/opinion/articles/2019-03-10/huawei-lawsuits-showcase-china-s-foreign-pr-drive)

> The dichotomy isn’t unique to Huawei. China’s government has also leveraged the openness of developed-nation democracies to push its message, while refusing the same opportunities at home.
> 
> China blocks its citizens from accessing Twitter, yet the country’s state-controlled media and government agencies have dozens of accounts with the U.S. social media service that they use to spread Beijing’s agenda.


More growing talk about influence operations and the asymmetric nature of countries with different laws, methods and cultural assumptions interacting.  This does read a little bit like a petulant child loudly stamping and declaring "it's not fair", which of course it isn't, but it's entirely legal for countries to have different rules for others operating inside their country versus how they might operate in other countries.


## [Science Busts The Biggest Myth Ever About Why Bridges Collapse](https://www.forbes.com/sites/startswithabang/2017/05/24/science-busts-the-biggest-myth-ever-about-why-bridges-collapse/#2a40d1da1f4c)

[https://www.forbes.com/sites/startswithabang/2017/05/24/science-busts-the-biggest-myth-ever-about-why-bridges-collapse/#2a40d1da1f4c](https://www.forbes.com/sites/startswithabang/2017/05/24/science-busts-the-biggest-myth-ever-about-why-bridges-collapse/#2a40d1da1f4c)

> But it wasn't resonance that brought the bridge down, but rather the self-induced rocking! Without an ability to dissipate its energy, it just kept twisting back-and-forth, and as the twisting continued, it continued to take damage, just as twisting a solid object back-and-forth will weaken it, eventually leading to it breaking. It didn't take any fancy resonance to bring the bridge down, just a lack of foresight of all the effects that would be at play, cheap construction techniques, and a failure to calculate all the relevant forces.


[This was supposed to be in last weeks newsletter, hence the reason for referencing bridges collapsing in the comment at the top!]

Huh.  I had always believed that resonant frequencies were what bought down the bridge.  It's nice to know that there's a far better explanation.


