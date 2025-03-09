---
title: "170 - Culture eats strategy for breakfast"
date: 2021-10-10
description: "It’s long been said that Culture eats strategy for breakfast. "
permalink: /culture-eats-strategy-for-breakfast/
---

It’s long been said that Culture eats strategy for breakfast. 

The big tech titans, such as the “FAANG” set of Facebook, Apple, Amazon, Netflix and Google, have all developed and inherited a specific culture, and it’s a culture of “deliver at all costs”.  What we are starting to see is the downsides of those cultures.  OKR’s, the measurement of work, the development of business at all costs are all the hallmarks of the way that the VC funded silicon valley approach to business works.

Developing a strong healthy culture that encourages diversity, that supports everyone to have opinions, and that tries to learn from challenge, is a strategy for company development in and of itself.  What’s unclear at the moment is how effectively those newer cultures can compete with the delivery focused companies, and how they can compete effectively.  

Safety first systems require investment, they require time and improvement, but they improve the companies ability to execute on the vision it has.  They don’t act as a vision or direction themselves, and you still need a product, a service or a way to enable that culture to deliver.

## [More details about the October 4 outage - Facebook Engineering](https://engineering.fb.com/2021/10/05/networking-traffic/outage-details/)

[https://engineering.fb.com/2021/10/05/networking-traffic/outage-details/](https://engineering.fb.com/2021/10/05/networking-traffic/outage-details/)

> This change caused a complete disconnection of our server connections between our data centers and the internet. And that total loss of connection caused a second issue that made things worse.  
> 
> One of the jobs performed by our smaller facilities is to respond to DNS queries. DNS is the address book of the internet, enabling the simple web names we type into browsers to be translated into specific server IP addresses. Those translation queries are answered by our authoritative name servers that occupy well known IP addresses themselves, which in turn are advertised to the rest of the internet via another protocol called the border gateway protocol (BGP). 
> 
> To ensure reliable operation, our DNS servers disable those BGP advertisements if they themselves can not speak to our data centers, since this is an indication of an unhealthy network connection. In the recent outage the entire backbone was removed from operation,  making these locations declare themselves unhealthy and withdraw those BGP advertisements. The end result was that our DNS servers became unreachable even though they were still operational. This made it impossible for the rest of the internet to find our servers. 
> 
> All of this happened very fast. And as our engineers worked to figure out what was happening and why, they faced two large obstacles: first, it was not possible to access our data centers through our normal means because their networks were down, and second, the total loss of DNS broke many of the internal tools we’d normally use to investigate and resolve outages like this. 


Ouch.

For some reason, lots of people tend to assume that massive failures are caused by massive actions, such as “cyberwar” by nation states.  But complex systems have complex failure modes, and small changes can result in escalating knock-on effects.

In this case, the loss of BGP took out the DNS resolvers, and the loss of the DNS resolvers then resulted in the loss of lots of systems.

The second thing to note is something that we’ve noted in significant outages in the past.  A normal outage can become catastrophic if you also lose access to good communication tools, documentation and coordination tools.  In this case, Facebook engineerings centralisation of things on the core domains means that almost everything they relied on stopped working as well.  That slows down diagnosis, triage and remediation activities or can even cause people to go from out of date documentation and make poor decisions in a limited information environment


## [Facebook “is tearing our societies apart,” whistleblower says in interview | Ars Technica](https://arstechnica.com/tech-policy/2021/10/facebook-is-tearing-our-societies-apart-whistleblower-says-in-interview/#p3)

[https://arstechnica.com/tech-policy/2021/10/facebook-is-tearing-our-societies-apart-whistleblower-says-in-interview/#p3](https://arstechnica.com/tech-policy/2021/10/facebook-is-tearing-our-societies-apart-whistleblower-says-in-interview/#p3)

> Frances Haugen, a data scientist by training and a veteran of Google and Pinterest, had been recruited to Facebook in 2018 to help the platform prepare for election interference. When she quit in May, she took with her a cache of tens of thousands of documents that now underpin a sweeping congressional investigation into Facebook's practices.
> 
> But Haugen's turning point came months earlier, on December 2, 2020, less than a month after the presidential election, when the company disbanded the Civic Integrity team she worked on.
> 
> “They told us, ‘We’re dissolving Civic Integrity.’ Like, they basically said, ‘Oh good, we made it through the election. There wasn’t riots. We can get rid of Civic Integrity now.’ Fast forward a couple months, we got the insurrection,” Haugen told CBS’s 60 Minutes, referring to the January 6 insurrection at the US Capitol. “And when they got rid of Civic Integrity, it was the moment where I was like, ‘I don’t trust that they’re willing to actually invest what needs to be invested to keep Facebook from being dangerous.’”
> 
> The next day, she used encrypted messaging to contact a Wall Street Journal reporter who had reached out to her earlier, the Journal reported. Part of her motivation, she said, was her fear that the genocide in Myanmar, where the military used Facebook to launch the pogrom, would repeat itself elsewhere.


The ability of users to walk out of your organisation with masses of files can be immensely damaging. Preventing bulk file transfers, the use of USB storage and various other controls will come at a cost of flexibility for users to carry out their work.  Insider threat is probably the hardest to control for, and the hardest to fundamentally prevent.

Of course, those files will also be read without context, which will feel far more damaging from a PR perspective.  Whether the stories that come out of this are true or not will be almost impossible to tell, but this could be the start of a dramatic fall for Facebook


## [Bezos Wants to Create a Better Future in Space. His Company Blue Origin Is Stuck in a Toxic Past.](https://www.lioness.co/post/bezos-wants-to-create-a-better-future-in-space-his-company-blue-origin-is-stuck-in-a-toxic-past)

[https://www.lioness.co/post/bezos-wants-to-create-a-better-future-in-space-his-company-blue-origin-is-stuck-in-a-toxic-past](https://www.lioness.co/post/bezos-wants-to-create-a-better-future-in-space-his-company-blue-origin-is-stuck-in-a-toxic-past)

> Workforce gender gaps are common in the space industry, but at Blue Origin they also manifest in a particular brand of sexism. Numerous senior leaders have been known to be consistently inappropriate with women. One senior executive in CEO Bob Smith’s loyal inner circle was reported multiple times to Human Resources for sexual harassment. Even so, Smith personally made him a member of the hiring committee for filling a senior HR role in 2019.
> 
> Another former executive frequently treated women in a condescending and demeaning manner, calling them “baby girl,” “baby doll,” or “sweetheart” and inquiring about their dating lives. His inappropriate behavior was so well known that some women at the company took to warning new female hires to stay away from him, all while he was in charge of recruiting employees. It appeared to many of us that he was protected by his close personal relationship with Bezos—it took him physically groping a female subordinate for him to finally be let go.
> 
> Additionally, a former NASA astronaut and Blue Origin senior leader once instructed a group of women with whom he was collaborating: “You should ask my opinion because I am a man.” We found many company leaders to be unapproachable and showing clear bias against women. Concerns related to flying New Shepard were consistently shut down, and women were demeaned for raising them. When one man was let go for poor performance, he was allowed to leave with dignity, even a going-away party. Yet when a woman leader who had significantly improved her department’s performance was let go, she was ordered to leave immediately, with security hovering until she exited the building five minutes later.
> 
> […]
> 
> Professional dissent at Blue Origin is actively stifled. Smith personally told one of us to not make it easy for employees to ask questions at company town halls—one of the only available forums for live, open discussion. Smith also asked his COO for a list of employees who were troublemakers or agitators. The list was then distributed to senior leaders so they could “have a talk” with the agitators in their groups. Critics inside the company have been forced out for speaking up and offered payment in exchange for signing even more restrictive nondisclosure agreements—including some of the engineers who ensure the very safety of the rockets. Smith’s inner circle of loyalists makes unilateral decisions, often without the buy-in of engineers, other experts, or senior leaders across various departments. 
> 
> This suppression of dissent brings us to the matter of safety, which for many of us is the driving force for coming forward with this essay. At Blue Origin, a common question during high-level meetings was, “When will Elon or Branson fly?” Competing with other billionaires—and “making progress for Jeff”—seemed to take precedence over safety concerns that would have slowed down the schedule. 
> 
> In 2020, company leaders demonstrated increasing impatience with New Shepard’s schedule of a few flights per year; their goal, routinely communicated to operations and maintenance staff, was to scale to more than 40. Some of us felt that with the resources and staff available, leadership’s race to launch at such a breakneck speed was seriously compromising flight safety. When Challenger exploded, the government’s investigation determined that the push to keep to a schedule of 24 flights per year “directly contributed to unsafe launch operations.” Of note: the Challenger report also cited internal stifling of differences of opinion as one of the organizational issues that led to the disaster and loss of life.


This is a pretty horrible letter that suggests a toxic culture within BlueOrigin.  But what stood out to me was the clear linking back to the Challenger report.

We’ve known for decades that diverse teams perform better, and more importantly, that ensuring that people feel capable of raising concerns, that they’ll be listened to, and that management will take them seriously not only improves workplace performance, but it actively improves safety and security at critical junctures.

We often focus “security culture” on telling people what not to do, but even more effective can be the creation of an open culture that enables people to flag systemic issues, express their opinions and feel valued and listened to. 


## [Company That Routes Billions of Text Messages Quietly Says It Was Hacked](https://www.vice.com/en/article/z3xpm8/company-that-routes-billions-of-text-messages-quietly-says-it-was-hacked)

[https://www.vice.com/en/article/z3xpm8/company-that-routes-billions-of-text-messages-quietly-says-it-was-hacked](https://www.vice.com/en/article/z3xpm8/company-that-routes-billions-of-text-messages-quietly-says-it-was-hacked)

> Syniverse repeatedly declined to answer specific questions from Motherboard about the scale of the breach and what specific data was affected, but according to a person who works at a telephone carrier, whoever hacked Syniverse could have had access to metadata such as length and cost, caller and receiver's numbers, the location of the parties in the call, as well as the content of SMS text messages.
> 
> "Syniverse is a common exchange hub for carriers around the world passing billing info back and forth to each other," the source, who asked to remain anonymous as they were not authorized to talk to the press, told Motherboard. "So it inevitably carries sensitive info like call records, data usage records, text messages, etc. [...] The thing is—I don’t know exactly what was being exchanged in that environment. One would have to imagine though it easily could be customer records and [personal identifying information] given that Syniverse exchanges call records and other billing details between carriers."
> 
> The company wrote that it discovered the breach in May 2021, but that the hack began in May of 2016. 
> 
> […]
> 
> "The world’s largest companies and nearly all mobile carriers rely on Syniverse’s global network to seamlessly bridge mobile ecosystems and securely transmit data, enabling billions of transactions, conversations and connections [daily]," Syniverse wrote in a recent press release. 
> 
> "Syniverse has access to the communication of hundreds of millions, if not billions, of people around the world. A five-year breach of one of Syniverse's main systems is a global privacy disaster," Karsten Nohl, a security researcher who has studied global cellphone networks for a decade, told Motherboard in an email.


So an attacker had access to the underlying infrastructure that manages mobile phone calls, metadata and the call and content of SMS messages for around 5 years?

The fact that the attacker didn’t attempt to monetise this indicates what kind of actor it might be.

One might jump to the conclusion that this is about intercepting SMS 2FA, but the description of the breach suggests that this is attackers coming back intermittently and downloading bulk data, which is more suggestive of someone who wants to perform bulk data analysis.


## [FoggyWeb: Targeted NOBELIUM malware leads to persistent backdoor - Microsoft Security Blog](https://www.microsoft.com/security/blog/2021/09/27/foggyweb-targeted-nobelium-malware-leads-to-persistent-backdoor/)

[https://www.microsoft.com/security/blog/2021/09/27/foggyweb-targeted-nobelium-malware-leads-to-persistent-backdoor/](https://www.microsoft.com/security/blog/2021/09/27/foggyweb-targeted-nobelium-malware-leads-to-persistent-backdoor/)

> This blog is another in-depth analysis of newly detected NOBELIUM malware: a post-exploitation backdoor that Microsoft Threat Intelligence Center (MSTIC) refers to as FoggyWeb. As mentioned in previous blogs, NOBELIUM employs multiple tactics to pursue credential theft with the objective of gaining admin-level access to Active Directory Federation Services (AD FS) servers. Once NOBELIUM obtains credentials and successfully compromises a server, the actor relies on that access to maintain persistence and deepen its infiltration using sophisticated malware and tools. NOBELIUM uses FoggyWeb to remotely exfiltrate the configuration database of compromised AD FS servers, decrypted token-signing certificate, and token-decryption certificate, as well as to download and execute additional components. Use of FoggyWeb has been observed in the wild as early as April 2021.


Once someone has access to your Active Directory servers, it’s more or less game over.  It’s really hard to determine what legitimate access is being used and what backdoors have been left in by the attackers.

There’s a lot of technical detail in this report, but the fundamental tactics are still the same, compromise an endpoint, laterally move within the network, and escalate privilege to take over the system.  The detections and controls remain very similar still today as they were a few years ago, even for the most capable actors.


## [Having a status page forced Comcast to fix my internet | ChrisShort.net](https://chrisshort.net/having-a-status-page-forced-comcast-to-fix-my-internet/)

[https://chrisshort.net/having-a-status-page-forced-comcast-to-fix-my-internet/](https://chrisshort.net/having-a-status-page-forced-comcast-to-fix-my-internet/)

> Another outage, another Xfinity tech dispatched. They came in and cleared all the coax in the house. They ended up removing an inline power device that we didn’t need anymore (leftover from the previous owners' TV service). That’s when I pulled out my phone and showed the tech the status page for the house. They looked at all the yellow, oranges, and red on the status page in horror. I told him I was looking into 5G internet to replace Comcast Business. I ultimately got a 5G hotspot from Calyx Institute as an emergency backup (thank you to the kind Red Hatter for the recommendation). The Comcast tech noted that the customer (me) was tracking the outages. Also, that we were likely leaving Comcast Business if they didn’t resolve the problem fast. The status page gave us an out from our “contract” with Comcast Business. After replacing everything between my network and Comcast’s network, it was made abundantly clear Comcast had an issue.


Visibility is everything, making a status page that shows off what an experience is like can be vital in not just getting it fixed, but in clearly communicating what the problem is, and enable everyone to focus on the things that can be measured.


## [Python behind the scenes #13: the GIL and its effects on Python multithreading](https://tenthousandmeters.com/blog/python-behind-the-scenes-13-the-gil-and-its-effects-on-python-multithreading/)

[https://tenthousandmeters.com/blog/python-behind-the-scenes-13-the-gil-and-its-effects-on-python-multithreading/](https://tenthousandmeters.com/blog/python-behind-the-scenes-13-the-gil-and-its-effects-on-python-multithreading/)

> As you probably know, the GIL stands for the Global Interpreter Lock, and its job is to make the CPython interpreter thread-safe. The GIL allows only one OS thread to execute Python bytecode at any given time, and the consequence of this is that it's not possible to speed up CPU-intensive Python code by distributing the work among multiple threads. This is, however, not the only negative effect of the GIL. The GIL introduces overhead that makes multi-threaded programs slower, and what is more surprising, it can even have an impact I/O-bound threads.
> 
> In this post I'd like to tell you more about non-obvious effects of the GIL. Along the way, we'll discuss what the GIL really is, why it exists, how it works, and how it's going to affect Python concurrency in the future.


This is a great read into how one of the most misunderstood aspects of Python (and CPython in particular)


## [Volume 0x10, Issue 0x46, Phile #0x04 of 0x0f - Cyber Grand Shellphish](http://phrack.org/issues/70/4.html#article)

[http://phrack.org/issues/70/4.html#article](http://phrack.org/issues/70/4.html#article)

> One approach to push the codification of what human hackers do, is to take
> the hackers out of the equation. This is precisely what the DARPA Cyber
> Grand Challenge was set out to do.
> 
> The DARPA Cyber Grand Challenge (CGC) was designed as a Capture The Flag
> (CTF) competition among autonomous systems without any humans being
> involved. During the competition, Cyber Reasoning Systems (CRSs) would find
> vulnerabilities in binaries, exploit them, and generate patches to protect
> them from attacks, without any human involvement at all.
> 
> The separation between human and machine is key, as it forces the
> participants to codify, in algorithms, the techniques used for both attack
> and defense. Although the competition was only a first step toward
> capturing the art of hacking, it was an important one: for the first time,
> completely autonomous systems were hacking one another with code, and not
> human intuition, driving the discovery of flaws in complex software
> systems.


Multiple comments here.  The first is that Phrack has released a new edition.  I’ve noted that a number of web proxies block access to Phrack because it’s a “hacking resource”, which I think is a strong indicator of just how good a magazine it has traditionally been.  Reading Phrack as a teenager is part of what started a life long love of securtity for me, so the first edition in 5 years is a big deal for me.  Here’s hoping we don’t have to wait another 5 years.

Secondly, there’s a number of highly technical articles in this edition, but of all of them, this one stood out as the most interesting.  I’d vaguely heard of the DARPA Cyber Grand Challenge but hadn’t really taken it on board.

The idea of building autonomous systems that can analyse binaries, find flaws, and then develop exploits for them is both deeply scary but also a valuable area of research.  If we can do that, then we can also apply those systems for finding flaws in the systems and patching and defending the systems.  This article is a good read for an introduction into this area.


## [An idea to make the UK the safest place to live and work online | Joel Samuel](https://joelgsamuel.medium.com/an-idea-to-make-the-uk-the-safest-place-to-live-and-work-online-7507cbd9ed18)

[https://joelgsamuel.medium.com/an-idea-to-make-the-uk-the-safest-place-to-live-and-work-online-7507cbd9ed18](https://joelgsamuel.medium.com/an-idea-to-make-the-uk-the-safest-place-to-live-and-work-online-7507cbd9ed18)

> How do you actually make the UK the safest place to live and work online? How do you protect millions of individual people at the same time?
> [...]
> Require all consumer and business networking providers (thats ISPs who provide broadband/fibre and also data connections to smartphones) to implement high confidence malware filtering DNS response policy zones (RPZ) provided by the UK government.


([Joel](https://twitter.com/joelgsamuel)) Tooting my own horn, I suggested this a few years ago to NCSC but of course far too informally and didn't bother to document it. It came up again recently.

I believe that the policy and regulatory/statutory changes are the hardest parts. It would take 1-2 years (on a good timeframe) to implement because UK ISPs and UK telcos generally have terrible security and don't do things to protect their customers unless made to do so or its intolerable not to (offering family filters to protect children, etc).

As usual, this isn't really a technical challenge.

([Michael](https://twitter.com/bruntonspall))I slightly disagree with Joel on this stuff.  This is a very technical fix, and one that I think will struggle with societal adoption.  One of the things that we need to remember with these things is that not everybody trusts the Government, and systems that could be abused by bad governments to censor speech will be resisted even if they are net positive for society under good governments.  This technical might be part of a wider technology solution, but regulation and mandation by Government is always something that is far more human factor driven than one might expect.


## [NSA warns of ALPACA TLS attack, use of wildcard TLS certificates - The Record by Recorded Future](https://therecord.media/nsa-warns-of-alpaca-tls-attack-use-of-wildcard-tls-certificates/)

[https://therecord.media/nsa-warns-of-alpaca-tls-attack-use-of-wildcard-tls-certificates/](https://therecord.media/nsa-warns-of-alpaca-tls-attack-use-of-wildcard-tls-certificates/)

> While there are many situations and attacks that could help attackers decrypt TLS-encrypted traffic, the NSA specifically highlighted the use of wildcard TLS certificates, something that multiple security researchers have also warned against throughout the years [1, 2, 3, 4, 5, 6].
> 
> A wildcard certificate is a digital TLS certificate obtained by companies from certificate authorities that allow the owner to apply it to a domain and all its subdomains at the same time (*.example.com).
> 
> Throughout the years, companies have used wildcard certificates because of reduced costs and because they are easier to manage, as administrators can apply the same certificate across all servers instead of having to manage a different one for each subdomain.
> 
> […]
> 
> In addition, the NSA’s advisory also comes with a warning about the new Application Layer Protocol Content Confusion Attack (ALPACA), which was disclosed earlier this summer, and which is also exploitable because of the use of wildcard certificates.
> 
> In a simple explanation, this attack allows a threat actor to confuse web servers that run multiple protocols to respond to encrypted HTTPS requests via unencrypted protocols, such as FTP, email (IMAP, POP3), and others.


This is a useful writeup of a fairly tricky vulnerability, which CISA says is being actively exploited.  

Fixing wildcard TLS certs should be much easier with multiple ACME compatible automated CA’s such as LetsEncrypt and others.  There’s far less need for wildcard certificates if a server can request and issue a per server certificate more easily.

As one wag [pointed out on twitter](https://twitter.com/gossithedog/status/1446743193874309123?s=21) however, the TLS cert that covers nsa.gov also covers 67 other domains, including *.fbi.gov.


## [Google blames suspected Russian hacking group for targeting 14,000 Gmail users](https://www.cyberscoop.com/google-saw-a-surge-in-russian-hacking-attempts-against-gmail-last-month/)

[https://www.cyberscoop.com/google-saw-a-surge-in-russian-hacking-attempts-against-gmail-last-month/](https://www.cyberscoop.com/google-saw-a-surge-in-russian-hacking-attempts-against-gmail-last-month/)

> Russian hackers targeted approximately 14,000 Gmail users last month, according to the company’s Threat Analysis Group. While 100% of the emails were blocked by spam, Google TAG director Shane Huntley characterized the batch as “above average” on Twitter.
> 
> The campaign from the group known at APT28 made up 86% of Google’s recent alerts to users about government-backed attackers, Huntley said in an email. Google batches these kinds of alerts to users rather than during the moment of detection to help keep attackers from figuring out their defense strategies, he explained.
> 
> Several Gmail users reported on Twitter receiving the alert, including several researchers and journalists. Huntley said the campaign was targeted “across a wide variety of industries.”
> 
> 


Fascinating from Google here.  Firstly that they successfully blocked 14,000 phishing emails, and then they warned people that they were on the target list.  

Google are being a bit coy about what was in the email, but the sly mention of keeping Word up to date makes me suspect that these emails included an attachment that contained malware designed to compromise the targets computer rather than attempting to steal their credentials via phishing.


