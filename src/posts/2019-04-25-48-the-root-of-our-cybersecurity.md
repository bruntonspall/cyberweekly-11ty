---
title: "48 - DNS is at the root of our cybersecurity"
date: 2019-04-25
description: "I'm back from holiday, so massive thanks to Jon and Joel for covering the newsletter while I was away.  I hope you enjoyed it, and it was novel to wake up on a Saturday morning and be able to read the newsletter rather than having to check and write it!"
permalink: /the-root-of-our-cybersecurity/
---

I'm back from holiday, so massive thanks to Jon and Joel for covering the newsletter while I was away.  I hope you enjoyed it, and it was novel to wake up on a Saturday morning and be able to read the newsletter rather than having to check and write it!

DNS is probably the most important technology on the web today, and pun firmly intended, the root of many of our cybersecurity for many organisations.

Computers verify who they are talking to by using DNS to lookup the IP address, but they also compare the DNS names to the TLS certificates, and one can even use tools like LetsEncrypt to issue new TLS certificates if you control the DNS for a site.  Control of DNS gives an attacker the ability to control or intercept almost everything in the system.

This makes DNS companies a huge target for both advanced and simple attackers.  Of course, things like SeaTurtle show us that nation state level advanced actors are attempting to breach the management of root servers, of DNS registrars themselves as a way of attacking organisations that might have great security measures themselves.

This stuff is really hard to secure, because it is by necessity a supply chain where you need to trust another organisation.  Registrars might have good internal security, but often don't offer that security to their customers.  How many registrars support 2FA for the DNS admin for clients?  How many provide out of band notification of changes? How many are able to support their customers into using strong passwords and secure by design tooling to manage their DNS entries?

With a background of the sorts of attacks that we see nation states conducting (as per the Mueller report, the Estonian Security Services and so forth), you can see that the main difference between a nation state and an independent hacking group is simply money and attention, and that gap is being lowered constantly.  We'll see independent hackers using the tools and techniques that we are seeing in these reports within the next few years, and that's a scary thought.

## [GCHQ cracks Frank Sidebottom's secret codes - BBC News](https://www.bbc.co.uk/news/entertainment-arts-47907370)

[https://www.bbc.co.uk/news/entertainment-arts-47907370](https://www.bbc.co.uk/news/entertainment-arts-47907370)

> In an attempt to solve the mystery, Sullivan eventually turned to GCHQ.
> 
> The country's top codebreakers too seemed flummoxed until Sievey's son Stirling recalled how his dad would get the children to fill an outer row with random symbols, while Sievey would insert real code into the inner row.
> 
> "It meant the outer row triangles is a complete red herring," Sullivan said. "Not only did he put a mystery out there, he made it deliberately impossible to crack.
> 
> "By letting his kids add nonsense into the message, it deliberately obscures the chances of anybody - even top mathematicians - being able to crack it. So I reported back to GCHQ that the outer ring is a red herring and then had an email one day saying, 'Right, we've cracked it during a light-hearted training exercise.'


Just a lovely story.  I'm always fascinated by the process to transliterate graphical codes into alphabetical codes, and the addition of dummy letters purely to resist cryptanalysis is very cute.


## [Abuse of hidden well-known directory in HTTPS sites | Blog](https://www.zscaler.com/blogs/research/abuse-hidden-well-known-directory-https-sites)

[https://www.zscaler.com/blogs/research/abuse-hidden-well-known-directory-https-sites](https://www.zscaler.com/blogs/research/abuse-hidden-well-known-directory-https-sites)

> We have been monitoring the compromised HTTPS sites for a few weeks and have noticed that attackers are favouring a well-known hidden directory present on the HTTPS website for storing and distributing Shade ransomware and phishing pages.
> 
> The hidden /.well-known/ directory in a website is a URI prefix for well-known locations defined by IETF and commonly used to demonstrate ownership of a domain. [...]
> 
> The attackers use these locations to hide malware and phishing pages from the administrators. The tactic is effective because this directory is already present on most HTTPS sites and is hidden, which increases the life of the malicious/phishing content on the compromised site.


Compromising Content Management Systems (CMS) such as Wordpress and Joomla are certainly not new however nefarious actors and malware hiding within existing folder structures may help evade detection.

As usual, the story here is to management your CMS (patching, and maybe some more patching) and ensure any security measures (such as in-container or on-server audit and scanning functions) reach far and wide to cover areas humans don't usually go.


## [Where Is Cloud.Gov Headed in 2019? | FedTech Magazine](https://fedtechmagazine.com/article/2018/12/where-cloudgov-headed-2019)

[https://fedtechmagazine.com/article/2018/12/where-cloudgov-headed-2019](https://fedtechmagazine.com/article/2018/12/where-cloudgov-headed-2019)

> Built in 2015 by the GSA’s 18F digital services team, cloud.gov is a government-customized hosting platform that takes care of technical infrastructure and security compliance requirements for agencies. Cloud.gov customers are responsible for their own application code, while the cloud.gov platform handles the security and maintenance of everything underneath, according to the GSA, and is built to keep applications online even with large numbers of users and sharp increases in usage.
> [...]
> The GSA’s Technology Transformation Service indicates in the RFI that it wants manpower to help manage the security and maintenance aspects of cloud.gov.


Cloud.Gov and the [UK Government Digital Service](https://gds.blog.gov.uk/)'s [GOV.UK Platform as a Service (PaaS)](https://www.cloud.service.gov.uk/) use [Cloud Foundry](https://www.cloudfoundry.org/) and are cut from the same cloth for the same purpose: create/operate a platform where as many commodity things (application runtime environments, databases, load balancing, scaling and so on) are done for you so tenant applications (and their teams) can focus on the important stuff.

Eggs in baskets create efficiencies by deduplicating effort but they raise the stakes for uptime, scale, support and security. Cloud.gov's market activity includes improving automated monitoring and alerting and as typical in security, the well will be bottomless and not run dry.


## [NotPetya act of war exclusion spreads to second insurer | Verdict](https://www.verdict.co.uk/notpetya-act-of-war/)

[https://www.verdict.co.uk/notpetya-act-of-war/](https://www.verdict.co.uk/notpetya-act-of-war/)

> Insurer Hiscox is believed to be refusing to pay a claim by multinational law firm DLA Piper over damage caused by the NotPetya cyberattack, citing the act of war exclusion due to the suspected involvement of the Russian government.
> 
> It follows a similar refusal by Zurich to Mondelez, which saw the insurer also decline to pay damages caused by NotPetya due to the act of war exclusion clause. Mondelez is now suing Zurich for $100m over the decision


When the [UK attributed the June 2017 NotPetya cyber-attack to the Russian government](https://www.gov.uk/government/news/foreign-office-minister-condemns-russia-for-notpetya-attacks) insurance underwriters saw this as a 'get out of ~jail~ cheque-writing' free card by classifying it as an 'Act of War' (which is exempt, so no payout).

Hiscox (the second insurer) sells [Cyber & Data Insurance](https://www.hiscox.co.uk/business-insurance/cyber-and-data-insurance) which might lead a more sceptical individual to wonder whether their policy will payout should push come to shove.



## [Trust but verify: reimagining service assessments](https://link.medium.com/JMhJWs7nXV)

[https://link.medium.com/JMhJWs7nXV](https://link.medium.com/JMhJWs7nXV)

> Despite some recent struggles with the process that point of view remains solid — assessments — alongside spend controls, the service manual and the design principles — are the most important legacy of GDS.
> 
> That doesn’t mean I wouldn’t do it differently though :)
> 
> There are lots of things I love about assessments but let me list some of the things that have always bothered me — the things I’d like to avoid in any kind of reimagining:
> 
> [snipped]
> 
> * Despite all the efforts to avoid it they are just too confrontational — it can feel a bit like you are joint defendants at a trial on some US legal show — with a team of prosecutors trying to trip you up (I don’t think anybody intends it to be like this — it is just the reality!) Because…
> 
> * The whole approach favours story-tellers. The assessments are a performance — including rehearsals and props — and the better the MC the better the chance of success.


This is a nice post summarising some of the things that bother me about service assessment too.  But sometimes there are second order effects from the bad sides that Mat raises here.

Rehearsals are quite common in government circles to pass an assessment. But I've been in several rehearsals where the inability to tell the story of the service has caused the team to ask themselves quite valuable questions about whether they are actually building the right service and whether they all understand what they are building.

The assessments requiring the ability to coherently, simply and performatively explain the user needs and the purpose of the service ensures that teams take the time to understand the service offer and be able to explain it in simple terms that can be understood.


## [Dark web typosquatting: Scammers v. Tor | Digital Shadows](https://www.digitalshadows.com/blog-and-research/dark-web-typosquatting-scammers-v-tor/)

[https://www.digitalshadows.com/blog-and-research/dark-web-typosquatting-scammers-v-tor/](https://www.digitalshadows.com/blog-and-research/dark-web-typosquatting-scammers-v-tor/)

> Scammers are scamming. So, what?
> 
> This may not seem like a very big revelation; a scammer creating typosquat domains to conduct fraud against users of the legitimate domain. However, this can provide a good case study of what happens if the issue of typosquatting gets out of hand and taken to the extreme. The scammer claimed that they made off with a lot of money: 200 BTC, which is around $760,000 at the time of writing. That’s nothing to scoff at. If what the fraudster says is true, it proves how profitable brand impersonation and domain squatting can be.


Domain identity squatting is not a new concept - gooogle.com is likely a common typographical error (in this case, Google have defensively registered it and it redirects back to the real google.com) however within [The Onion Router (Tor)](https://www.torproject.org/) network domains look like tochka3evevasc32[.]onio and that is a lot easier to type incorrectly, and where over $760,000 USD was made.


## [DNS Hijacking Abuses Trust In Core Internet Service - SeaTurtle](https://blog.talosintelligence.com/2019/04/seaturtle.html?m=1)

[https://blog.talosintelligence.com/2019/04/seaturtle.html?m=1](https://blog.talosintelligence.com/2019/04/seaturtle.html?m=1)

> The threat actors behind the Sea Turtle campaign show clear signs of being highly capable and brazen in their endeavors. The actors are responsible for the first publicly confirmed case against an organizations that manages a root server zone, highlighting the attacker's sophistication. Notably, the threat actors have continued their attacks despite public reports documenting various aspects of their activity, suggesting they are unusually brazen and may be difficult to deter going forward. In most cases, threat actors typically stop or slow down their activities once their campaigns are publicly revealed.


This is a scary attack.  DNS is a difficult thing to secure, and this is an attack primarily on the supply chain for the target organisations, so in the case of successful compromise, you probably won't ever know that anything happened, because it's all outside your own network.

Detection of this would be a combination of logging regular queries against your DNS records to check they don't resolve differently for any reason, and since once they controlled the domain, they registered new TLS certificates, monitoring the certificate transparency logs to ensure that no new certificates have been issued.


## [Signed HTTP Exchanges by Google](https://developers.google.com/web/updates/2018/11/signed-exchanges)

[https://developers.google.com/web/updates/2018/11/signed-exchanges](https://developers.google.com/web/updates/2018/11/signed-exchanges)

> So, how do Signed HTTP Exchanges work? This technology allows a publisher to sign a single HTTP exchange (i.e., a request/response pair), in the way that the signed exchange can be served from any caching server. When the browser loads this Signed Exchange, it can safely show the publisher’s URL in the address bar because the signature in the exchange is sufficient proof that the content originally came from the publisher’s origin.


This is a really interesting technology.  Designed to allow AMP pages be able to be served on urls like www.bbc.co.uk instead of www.google.com/amp/www.bbc.co.uk it allows any third party to host content from a participating website and to represent itself as the original URL for the website, using a different TLS certificate, providing the original content hasn't changed at all.

For caches, this is brilliant news, because it means that you won't necessarily need to give out TLS private certificates to CDN's that want to proxy your content anymore, since the user can verify the content is valid separately from the server that sent it to them.


## [Distributed Denial of Secrets](http://DDoSecrets.com)

[http://DDoSecrets.com](http://DDoSecrets.com)

> Distributed Denial of Secrets (“DDOS”) is a transparency collective, aimed at enabling the free transmission of data in the public interest. We aim to avoid any political, corporate or personal leanings, and to act as a simple beacon of available information. As a collective, we do not support any cause, idea or message beyond ensuring that information is available to those who need it most - the people.


It's always been a great shame that Wikileaks isn't a wiki and is plagued by ego's, political perspectives and various other things that get in the way of the principle idea of transparency.  This site has a strong board of advisors who believe in transparency but not releasing harmful information.  A variety of leaks of various organisations have been collated here, but ones that are perceived to be state sponsored are clearly marked, and leaks that contain highly personal or sensitive data requires you to contact them.

This has been running for a while as a Tor site, but a clearnet copy makes it far more discoverable, and much more useful to journalists the world round.


## [Estonian Internal Security Service Annual Review](https://kapo.ee/en/content/annual-reviews.html)

[https://kapo.ee/en/content/annual-reviews.html](https://kapo.ee/en/content/annual-reviews.html)

> approaching in an apparently ordinary situation, for example at a reception or social (business) meeting, the discussion seems to take a natural course, expressing hope of for making a specifc proposal for future meetings. is is followed seamlessly by mostly civil situations for getting to know the person, along with personal questions and inducements.
> 
> Apparently trifling requests to obtain inconsequential information. However, the recruiter will want information of ever better quality, for
> which a reward is promised, whether money, benefcial relationships/contacts, or professional success. 


A fascinating read generally.  The Estonian government has specific reasons to be far more specifically critical of the Russian government, but I wish that the UK and US reports had detail that was as well written and well presented as this.  In particular the section on how Russian intelligence recruits Europeans is absolutely fascinating.  However, the cybersecurity section is a little disappointing.


## [Report On The Investigation Into Russian Interference In The 2016 Presidential Election [pdf]](https://cdn.cnn.com/cnn/2019/images/04/18/mueller-report-searchable.pdf)

[https://cdn.cnn.com/cnn/2019/images/04/18/mueller-report-searchable.pdf](https://cdn.cnn.com/cnn/2019/images/04/18/mueller-report-searchable.pdf)

> To operate X-Agent and X-Tunnel on the DCCC and DNC networks, Unit 26165 officers set up a group of computers outside those networks to communicate with the implanted malware. The first set of GRU-controlled computers, known by the GRU as "middle servers," sent and received messages to and from malware on the DNC/DCCC networks. The middle servers, in turn, relayed messages to a second set of GRU-controlled computers, labeled internally by the GRU as an "AMS Panel." 
> The AMS Panel [redacted] served as a nerve center through which GRU officers monitored and directed the malware's operations on the
> DNC/DCCC networks.


Obviously the news is all over this report, and I ahven't had time to read it all.  I'm also far less interested in the politics of it all, which is the primary purpose of the report.  But sections II and III (pages 14 - 35 and 36-50) are all about the GRU's information and cyber operations.

While there's not much that we didn't already know, if you've been following for the last few years, it's a nice summary that ties together a lot of various APT reports and indictments over the last few years.  Well worth a read


