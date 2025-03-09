---
title: "138 - Cyberarms is a technical topic"
date: 2021-02-28
description: "Pelroths book looks really interesting.  I'm just starting [Sandworm by Andy Greenberg](https://amzn.to/2O8RK3s), but I can see that [Pelroth's This is how they tell me the world ends](https://amzn.to/2NFfhtb) is going to have to go on my list.  Despite the criticisms, I think it's an interesting looking reading none the less."
permalink: /cyberarms-is-a-technical-topic/
---

Pelroths book looks really interesting.  I'm just starting [Sandworm by Andy Greenberg](https://amzn.to/2O8RK3s), but I can see that [Pelroth's This is how they tell me the world ends](https://amzn.to/2NFfhtb) is going to have to go on my list.  Despite the criticisms, I think it's an interesting looking reading none the less.

It's fine for someone to write a narrative based, politically driven book, but when it covers technical topics, technologists are going to want the technical details to be accurate.  When someone skimps on the technical details it lowers the believe in their narrative.  If the fundamental technical facts are wrong, it suggests that they have sought out facts that reinforce their pre-existing narrative.  Some narratives can handle that, the technical facts are incidental to the story.  But when it's about cybersecurity, you can see why cybersecurity experts get upset around the troubling technical details.

Anyway, it's a light one this week because I spent some of the week rewriting the cyberweekly.net code, and then discovered when I went to write this today that it still contained some critical bugs!  This is why I prefer pair programming and unit testing, neither of which its possible to use on a personal project!

## [Errata Security: Review: Perlroth's book on the cyberarms market](https://blog.erratasec.com/2021/02/review-perlroths-book-on-cyberarms.html)

[https://blog.erratasec.com/2021/02/review-perlroths-book-on-cyberarms.html](https://blog.erratasec.com/2021/02/review-perlroths-book-on-cyberarms.html)

> If this were written by a tech journalist, then criticism would be the expected norm. Tech is full of factual truths, such as whether 2+2=5, where it’s possible for a thing to be conclusively known. All journalists make errors -- tech journalists are constantly making small revisions correcting their errors after publication.
> 
> 
> The best example of this is Ars Technica. They pride themselves on their reader forums, where readers comment, opine, criticize, and correct stories. Sometimes readers add more interesting information to the story, providing free content to other readers. Sometimes they fix errors.
> 
> 
> It’s often unpleasant for the journalists who steel themselves after hitting “Submit…”. They have a lot of practice defending or correcting every assertion they make, from both legitimate and illegitimate criticism. This makes them astoundingly good journalists -- mistakes editors miss readers don’t. They get trained fast to deal with criticism.
> 
> 
> The mainstream press doesn’t have this tradition. To be fair, it couldn’t. Tech forums have techies with knowledge and experience, while the mainstream press has ignorant readers with opinions. Regardless of the story’s original content it’ll devolve into people arguing about whether Epstein was murdered (for example).
> 
> 
> Nicole Perlroth is a mainstream reporter on a techy beat. So you see a conflict here between the expectation both sides have for each other. Techies expect a tech journalist who’ll respond to factual errors, she doesn’t expect all this criticism. She doesn’t see techie critics for what they are -- subject matter experts that would be useful sources to make her stories better. She sees them as enemies that must be ignored. This makes her stories sloppy by technical standards. I hate that this sounds like a personal attack when it’s really more a NYTimes problem -- most of their cyber stories struggle with technical details, regardless of author.
> 
> 
> This problem is made worse by the fact that the New York Times doesn’t have “news stories” so much as “narratives”. They don’t have neutral stories reporting what happened, but narratives explaining a larger point.


I think Rob hits the nail on the head here.  I linked to the extract of Pelroths book last week, and it's quite breathlessly excited about the perils of cyberwar.  That's because it's narrative, rather than a factual recounting of the events.  

To those in the infosec industry, who are nitpickers about the exactly technical truth, it means that she appears to have committed an egregious sin, and of course, as Rob points out, they are used to tech reporters taking feedback and updating their stories.  To be ignored and called out for "bruised male egos" because they are trying to argue facts with a narrative creates a cognitive dissonance.


## [ADD / XOR / ROL: Book Review: "This Is How They Tell Me the World Ends"](http://addxorrol.blogspot.com/2021/02/book-review-this-is-how-they-tell-me.html)

[http://addxorrol.blogspot.com/2021/02/book-review-this-is-how-they-tell-me.html](http://addxorrol.blogspot.com/2021/02/book-review-this-is-how-they-tell-me.html)

> As a non-US person, the strangest part of the book was the rather extreme ethnocentricity of the book: The US is equated with "respecting human rights", everything outside of the US is treated as both exotic and vaguely threatening, and the book obsesses about a "capability gap" where non-US countries somehow caught up with superior US technology.
> 
> This ranges from the benign-but-silly (Canberra becomes the "outback", and Glenn Greenwald lives "in the jungles of Brazil" - evoking FARC-style guerillas, when - as far as I am informed - he lives in a heavily forested suburb of Rio) to seriously impacting and distorting the narrative.
> 
> The author seems to find it unimaginable that exploitation techniques and the use of exploits are not a US invention. The text seems to insinuate that exploit technologies and "tradecraft" were invented at NSA and then "proliferated" outward to potentially human-rights-violating "foreign-born" actors via government contractors that ran training classes.
> 
> This is false, ridiculous, and insulting on multiple levels.


Ignoring any technical inaccuracies in the book, this attack on its narrative gets the critique right.

As I've argued before, the US generally has a general view on US-exceptionalism that assumes that US citizens are unique in having privacy worth protecting, that US inventions and approaches are clearly better, and that the world should be in an order of "US at the top".

Whether that makes it a good book or not is neither here nor there, if that narrative bothers you, then I suspect you won't like the book.


## [Jamaica’s JamCOVID pulled offline after third security lapse exposed travelers’ data](https://techcrunch.com/2021/02/26/amber-group-jamcovid-data-exposed/)

[https://techcrunch.com/2021/02/26/amber-group-jamcovid-data-exposed/](https://techcrunch.com/2021/02/26/amber-group-jamcovid-data-exposed/)

> Matthew Samuda, a minister in Jamaica’s Ministry of National Security, also did not respond to a request for comment or our questions — including if the Jamaican government plans to continue its contract or relationship with Amber Group.
> 
> This is the third security lapse involving JamCOVID in the past two weeks.
> 
> Last week, Amber Group secured an exposed cloud storage server hosted on Amazon Web Services that was left open and public, despite containing more than 70,000 negative COVID-19 lab results and over 425,000 immigration documents authorizing travel to the island. Savadia said in response that there were “no further vulnerabilities” with the app. Days later, the company fixed a second security lapse after leaving a file containing private keys and passwords for the service on the JamCOVID server.
> 
> The Jamaican government has repeatedly defended Amber Group, which says it provided the JamCOVID technology to the government “for free.” Amber Group’s Savadia has previously been quoted as saying that the company built the service in “three days.”


COVID has meant lots of organisations being reactive, and having to build things at speed.  That means needing security good practice built in, security professionals who can give advice on how to build systems well and quickly.  
What it often means is that the compliance driven teams simply cannot cope, and therefore get "gone around".

Quite what the actual failure has been here won't be known, but it's unlikely to be simple and small, and more of a systemic failure in which security is simply not thought about or owned by the developers.


## [China's Secret War for U.S. Data Blew American Spies' Cover](https://foreignpolicy.com/2020/12/21/china-stolen-us-data-exposed-cia-operatives-spy-networks/)

[https://foreignpolicy.com/2020/12/21/china-stolen-us-data-exposed-cia-operatives-spy-networks/](https://foreignpolicy.com/2020/12/21/china-stolen-us-data-exposed-cia-operatives-spy-networks/)

> The anger in Beijing wasn’t just because of the penetration by the CIA but because of what it exposed about the degree of corruption in China. When the CIA recruits an asset, the further this asset rises within a county’s power structure, the better. During the Cold War it had been hard to guarantee the rise of the CIA’s Soviet agents; the very factors that made them vulnerable to recruitment—greed, ideology, blackmailable habits, and ego—often impeded their career prospects. And there was only so much that money could buy in the Soviet Union, especially with no sign of where it had come from.
> 
> But in the newly rich China of the 2000s, dirty money was flowing freely. The average income remained under 2,000 yuan a month (approximately $240 at contemporary exchange rates), but officials’ informal earnings vastly exceeded their formal salaries. An official who wasn’t participating in corruption was deemed a fool or a risk by his colleagues. Cash could buy anything, including careers, and the CIA had plenty of it.


A wonderful long read that comes in 3 parts.  Zach has been long working on this story, starting with the Shattered story back in Yahoo News over a year ago. 

You may need a ForeignPolicy subscription to read all 3 without the use of incognito browsers and VPN's for the free article limit.


## [Firefox 86 Introduces Total Cookie Protection - Mozilla Security Blog](https://blog.mozilla.org/security/2021/02/23/total-cookie-protection/)

[https://blog.mozilla.org/security/2021/02/23/total-cookie-protection/](https://blog.mozilla.org/security/2021/02/23/total-cookie-protection/)

> In 2019, Firefox introduced Enhanced Tracking Protection by default, blocking cookies from companies that have been identified as trackers by our partners at Disconnect. But we wanted to take protections to the next level and create even more comprehensive protections against cookie-based tracking to ensure that no cookies can be used to track you from site to site as you browse the web.
> 
> Our new feature, Total Cookie Protection, works by maintaining a separate “cookie jar” for each website you visit. Any time a website, or third-party content embedded in a website, deposits a cookie in your browser, that cookie is confined to the cookie jar assigned to that website, such that it is not allowed to be shared with any other website.
> 
> In addition, Total Cookie Protection makes a limited exception for cross-site cookies when they are needed for non-tracking purposes, such as those used by popular third-party login providers. Only when Total Cookie Protection detects that you intend to use a provider, will it give that provider permission to use a cross-site cookie specifically for the site you’re currently visiting. Such momentary exceptions allow for strong privacy protection without affecting your browsing experience.


This move from Firefox should protect against many of the ad trackers that attempt to set super-cookies or other such activities.  It won't protect against cname-cloaking.

I'm also slightly unsure on the specific cross-site cookies for login providers given the popularity of logins using Google, Microsoft, Github, Twitter and Facebook.  I assume however that Firefox's attention to detail here is strong enough to allow just the cookies for login to work effectively.


## [VMSA-2021-0002](https://www.vmware.com/security/advisories/VMSA-2021-0002.html)

[https://www.vmware.com/security/advisories/VMSA-2021-0002.html](https://www.vmware.com/security/advisories/VMSA-2021-0002.html)

> VMware vCenter Server updates address remote code execution vulnerability in the vSphere Client (CVE-2021-21972)
> Description
> 
> The vSphere Client (HTML5) contains a remote code execution vulnerability in a vCenter Server plugin. VMware has evaluated the severity of this issue to be in the Critical severity range with a maximum CVSSv3 base score of 9.8.
> Known Attack Vectors
> 
> A malicious actor with network access to port 443 may exploit this issue to execute commands with unrestricted privileges on the underlying operating system that hosts vCenter Server. 


Ouch.  If you run VMware vCenter, and you expose it to anyone, insiders or worse, to the internet, then you are vulnerable, and this is trivially easy to weaponise.

Patch now


## [Large-scale Analysis of DNS-based Tracking Evasion - broad data leaks included?](https://blog.lukaszolejnik.com/large-scale-analysis-of-dns-based-tracking-evasion-broad-data-leaks-included/)

[https://blog.lukaszolejnik.com/large-scale-analysis-of-dns-based-tracking-evasion-broad-data-leaks-included/](https://blog.lukaszolejnik.com/large-scale-analysis-of-dns-based-tracking-evasion-broad-data-leaks-included/)

> We show how:
> 
> The use of CNAME cloaking is introducing web security bugs that let compromise/hack unsuspecting users. Websites could misuse the bugs to compromise the security of web users, systematically. It’s a systemic issue in the case of a few trackers.
> The use of the CNAME cloaking technique leads to massive cookie leaks. In 95% of cases of websites using this technique, we found cookies leaking to external tracker servers in an unsanctioned manner, invisible to the user. In some cases, we confirm that the leaked cookies contain private/sensitive data. All these likely trigger the violation of data protection regimes such as the GDPR, or maybe even the CCPA.
> We report that this tracking technique is prevalent on popular websites. We find it on 9.98% of the top 10,000 websites. The use of this method is rising (21% up, over the past 22 months). We detect 13 providers of such tracking “services” on 10,474 websites. This scheme leads to data leaks on 95% of the websites employing it. Such data leaks sometimes involve unambiguously private data. GDPR alert lights should be flashing red.
> 


Interesting privacy report that has some interesting ramifications.

The tl;dr; of CNAME cloaking is this:
If I own example.com as a domain, and I wanted to provide advertiser.com with tracking information, I can create a cname at tracker.example.com that resolves to example-customer.advertiser.com.  Because the browser sees the tracker as a subdomain of example.com, it can see and read all of the cookies.

The problem is that this is working as desired.  If I work in a large organisation with multiple operational systems, I may well have some systems running on different hosting locations, and legitimately want a cname from example-engineering.com to run on example.com.

Secondly, I may well want to delegate certain cnames to other SaaS providers, so mail.example.com may well point to office365 owned domains.  That cookies and information can leak to your SaaS providers is a worry for us when architecting these systems.


## [no hello](https://nohello.net/)

[https://nohello.net/](https://nohello.net/)

> no greetings!|
> please don't say just hello in chat
> Imagine calling someone on the phone, going hello! then putting them on hold... 🤦‍♀️


This is a lovely little site that demonstrates some positive behaviours that you need to do to enable asynchronous communication, such as instant messaging.

As this becomes increasingly normal for those of us who are, sometimes unwillingly, working from home, I think this sort of user behaviour and politeness needs reinforcing, because it is different from our normal in-person communication style.  It feels more brusque, and less polite, and yet it's clearly more efficient.


## [An Exploration of JSON Interoperability Vulnerabilities](https://labs.bishopfox.com/tech-blog/an-exploration-of-json-interoperability-vulnerabilities)

[https://labs.bishopfox.com/tech-blog/an-exploration-of-json-interoperability-vulnerabilities](https://labs.bishopfox.com/tech-blog/an-exploration-of-json-interoperability-vulnerabilities)

> JSON INTEROPERABILITY SECURITY RISKS
> I categorized the identified interoperability security risks into five categories:
> 
> Inconsistent Duplicate Key Precedence
> 
> Key Collision: Character truncation and Comments
> 
> JSON Serialization Quirks
> 
> Float and Integer Representation
> 
> Permissive Parsing and Other Bugs


Different systems in your environment, including things like security gateways, antivirus and firewalls might parse certain incompatible json schemas differently because the specification is too loose, along with many "extensions" that are implemented without a formal specification.

I also note that BishopFox has done a brilliant job of providing hands on labs throughout where you can try out these exploits and see for yourself


