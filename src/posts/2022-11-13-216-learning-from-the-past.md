---
title: "216 - Learning from the past"
date: 2022-11-13
description: "We aren't very good at learning from the past in cyber security."
permalink: /learning-from-the-past/
---

We aren't very good at learning from the past in cyber security.

One of the issues is that we have a really young industry.  The US Government and the airline industry [created the NTSB back in 1926](https://www.ntsb.gov/about/history/Pages/default.aspx) although it took about 40 years to turn into something more like it did now.   The Nuclear Regulatory Commission kicked off the investigation into the three mile island nuclear meltdown in 1980, and it's seen as [the worlds most studied nuclear accident](https://www.gao.gov/products/emd-80-109).

In comparison, although Ian Levy dates the first memory corruption bugs back to 1972, in reality our industry hasn't really grown up with those sorts of issues until the last few decades.  

In comparison to many other industries, we are incredibly young, and we need to learn from people who have made mistakes in the past in order to get better at remediating those issues.

But keeping track of the past is really hard, and the building of good "knowledge management" tools is not something that we tend to prioritise as organisations.  Instead we let people leave, writing handover documents that someone reads and never goes back to.   We are therefore constantly bleeding institutional knowledge, and losing the older, more experienced, and wiser members of staff can make it hard to learn the lessons of the past.  I've heard on at least one organisation that actively brings back older more senior members of staff into junior roles in operational contexts to act as advisors.  This enables the recycling of those decades of experience back into modern operational teams, which seems like a neat idea.

## Notes and responses

TIm emailed me after [CyberWeekly 214](https://cyberweekly.net/little-snippets-of-practice), to say that he thought I was being a bit overly harsh on lift-and-shift approaches.  One of the statements I had posited was that Cloud may not be cheaper than running your own servers.   He correctly pointed out that this might be true if you run your servers in-house with your own staff, but if you use an existing managed service then it might charge you eye watering amounts for the servers, as well as massively increase the costs of change on those servers.  In those cases, there might be significant reduction in cost even when lifting and shifting, just because you are bringing the servers under your control.  Good point, and thanks for the response.

Secondly, as we watch the rapid contraction and reset of Twitter, you'll notice that a number of people are moving to Mastodon instead.  I'm not as much of a fan of Mastodon, mostly because I think that the natural federation puts a set of burdens on the user that the user doesn't want (such as selecting a server, which is a remarkably difficult decision to make without having used the system).  However, you can find me at [https://octodon.social/@Bruntonspall](https://octodon.social/@Bruntonspall) if you'd like to see how much I use it.   I joined in 2017, "tooted" once, and hadn't gone back until this week.  One of the things I'll have to decide is whether I archive my twitter data and host it anywhere just in case, something I'm undecided on.  I notice a lot of infosec people are joining the [Infosec.exchange](https://infosec.exchange/about) server, and it's a good place to look for some of the big infosec names from twitter if you are looking for people to follow.

## [So long and thanks for all the bits - NCSC.GOV.UK ](https://www.ncsc.gov.uk/blog-post/so-long-thanks-for-all-the-bits)

[https://www.ncsc.gov.uk/blog-post/so-long-thanks-for-all-the-bits](https://www.ncsc.gov.uk/blog-post/so-long-thanks-for-all-the-bits)

> The Log4J problem is equivalent to the problem we had with Heartbleed back in 2014, despite being a different sort of vulnerability. The community had alighted on a good solution to a problem and reused the hell out of it. But we hadn’t put the right support in place to make sure that component, OpenSSL, was developed and maintained like the security of the world depended on it. Because it did. The SolarWinds issue was a supply-chain attack (going after a supplier to get to your real target). It’s not the first time we’ve seen that, either. Back in 2002, someone borked the distribution server for the most popular mail server programme, [sendmail](https://vuls.cert.org/confluence/display/historical/CERT+Advisory+CA-2002-28+Trojan+Horse+Sendmail+Distribution) , and for months, many, many servers on the internet were running compromised code. That same year, the [OpenSSH](https://vuls.cert.org/confluence/display/historical/CERT+Advisory+CA-2002-24+Trojan+Horse+OpenSSH+Distribution) distribution was borked to compromise people who built that product to provide secure access to their enterprise.
> 
> My point here is that we rarely learn from the past (or generalise from the point problems we see to the more general case) to get ahead of the attackers. Going back to the aircraft analogy, if that industry managed risk and vulnerability the way we do in cyber security, there would be planes literally falling out of the sky. We should learn from that sector and the safety industry more generally [[1]](https://www.ncsc.gov.uk/blog-post/so-long-thanks-for-all-the-bits#footnote1) . The US have set up the [Cyber Safety Review Board](https://www.cisa.gov/cyber-safety-review-board) , based on the National Transportation Safety Board, which will hopefully be a first step in systematising learnings from incidents and the like, to drive change in the cyber security ecosystem. At the moment, it’s only looking at major incidents, but it’s a start. I hope the community supports this (and similar efforts), and helps them scale and move from just looking at incidents to tackling some of the underlying issues we all know need fixing. Without some sort of feedback loop, we are destined to be a bit dumb forever. 


Ian Levy leaving the UK Government is going to be a blow to, at the very least the excitement and thrill working there.  I’ve been on the receiving end of a Levy monologue before, and it’s quite the experience.  

On of the things he calls out, that we are bad at doing generally in cybersecurity, is recognising just how young our industry is, and how poor we are at learning from the past.  Almost all of the problems that we are facing now are in fact just repetitions of the problems that we’ve faced in the past.  But cybersecurity doesn’t really have many greybears, many of the good and great who built the things of the past.  A combination of rapid growth, exponentially changing technology platforms and career burnout means that we are often losing institutional memory faster than we are building it. 


## [Inside the Twitter meltdown ](https://www.platformer.news/p/inside-the-twitter-meltdown)

[https://www.platformer.news/p/inside-the-twitter-meltdown](https://www.platformer.news/p/inside-the-twitter-meltdown)

> Everything went from bad to worse at Twitter on Thursday. Today let’s talk about a truly chaotic 24 hours at the company, and the mounting fears over what it means for the service that still serves as the heartbeat of the global news cycle. 


My rough view is that the meltdown of twitter is somewhat overhyped by a small but vocal minority who don’t see it serving the thing that they want it to do.

But that aside, the reality of the last week has been pretty astonishing to watch from the outside, and the details seem utterly baffling.  It’s always difficult to tell what is really happening on the inside, but Corey’s platformer newsletter has been getting lots of individual insider stories to help piece together what’s going on. 


## [Twitter's imminent collapse could wipe out vast swathes of recent human history | MIT Technology Review ](https://www.technologyreview.com/2022/11/11/1063162/twitters-imminent-collapse-could-wipe-out-vast-records-of-recent-human-history/)

[https://www.technologyreview.com/2022/11/11/1063162/twitters-imminent-collapse-could-wipe-out-vast-records-of-recent-human-history/](https://www.technologyreview.com/2022/11/11/1063162/twitters-imminent-collapse-could-wipe-out-vast-records-of-recent-human-history/)

> “If Twitter was to ‘go in the morning’, let's say, all of this—all of the firsthand evidence of atrocities or potential war crimes, and all of this potential evidence—would simply disappear,” says Ciaran O’Connor, senior analyst at the Institute for Strategic Dialogue (ISD), a global think tank. Information gathered using open-source intelligence, known as OSINT, has been used to support prosecutions for war crimes and acts as a record of events long after the human memory fades.
> 
> Part of what makes Twitter’s potential collapse uniquely challenging is that the “digital public square” has been built on the servers of a private company, says  O’Connor’s colleague Elise Thomas, senior OSINT analyst with the ISD. It’s a problem we’ll have to deal with many times over the coming decades, she says: “This is perhaps the first really big test of that.”


This is something I've been talking about for a while now.  I was lucky to be one of the developers who was allowed access to Twitters embedding functionality for news systems, [using something called Twitter Anywhere](https://www.brunton-spall.co.uk/post/2010/04/14/using-twitter-anywhere-introduction/).

One of the issues that came from this process is that the actual tweets themselves were embedded in the source content management system of the Guardian itself.  We raised at the time that if Twitter failed, or even just changed the way that tweets are rendered, then articles wouldn't make sense anymore.  But the reality was that people wnated embedded tweets in articles to consume news now far more than thinking about archiving the internet.  And indeed, it was a silly idea at the Guardian that we would copy and archive all external content as if we were the only people capable of delivering such content.  

That decision created a far more multimedia (or hypermedia) experience when reading articles, but there's a worry for historians in the future about how we will access the information in 50, 100 or 200 years time.  Chris here really explores this problem and some of the potential solutions.


## [Things I believe about change. I haven’t blogged for ages. I’m a civil… | by Simon Parker | Nov, 2022 | Medium ](https://medium.com/@SimonFParker/things-i-believe-about-change-f5e701aecbfa)

[https://medium.com/@SimonFParker/things-i-believe-about-change-f5e701aecbfa](https://medium.com/@SimonFParker/things-i-believe-about-change-f5e701aecbfa)

> Proposition 5: everyone knows what’s wrong
> 
> The organisation knows what’s broken. Everyone can see it. The problem is that they see it from their perspective, which is inevitably partial. The most common complaint I hear from people is they don’t have enough resources to do the job. Sometimes that’s right. More often I’m looking at people who are struggling with a poorly designed system loading them up with work that’s designed for senior leadership control of the kind I discussed in proposition 3. The principal job for org change is therefore to link people up, share knowledge and help them to see the big picture. Done well, this will provide the beginnings of a solution (often by breaking the loop that’s feeding the attempt at control). If you’re really lucky, some of the people you just linked up will start fixing things spontaneously.
> 
> Proposition 6: look outside your boundaries
> 
> Your customers and service users know what’s wrong too. Engaging them will help you get it right. In fact, you need ongoing engagement with them. How are you bringing the voices of the people you serve into the organisation? Who champions the user perspective? Where is that conversation held? When I think about the structural changes I’ve made in organisations, they are usually about building better ways to understand the world (regional teams, BI hubs, improved customer service) and corporate brains that can make sense of that intelligence (usually some sort of strategy team). 


There’s a lot about culture change in here that’s good and I recommend reading the whole article.  But one of the things that we commonly miss is that a lot of people outside of the leadership already know what is wrong.  What leaders fail to do is actually hear and listen to those voices.  That can be because it doesn’t align with our view, or because it is a blow to our ego, but the biggest mistake we can make is assuming that we as leaders drive organisational change 


## [Announcement - Cloud Workstations remote IDE solution in preview | Google Cloud Blog ](https://cloud.google.com/blog/products/application-development/introducing-cloud-workstations/)

[https://cloud.google.com/blog/products/application-development/introducing-cloud-workstations/](https://cloud.google.com/blog/products/application-development/introducing-cloud-workstations/)

> At Google Cloud Next, we introduced the public Preview of [Cloud Workstations](https://cloud.google.com/workstations) , which provides fully managed and integrated development environments on Google Cloud. Cloud Workstations is a solution focused on accelerating developer onboarding and increasing the productivity of developers’ daily workflows in a secure manner, and you can start using it today simply by visiting the Google Cloud [console](https://console.cloud.google.com/workstations/) and configuring your first workstation. 
> 
> **Cloud Workstations: Just the facts** 
> 
> Cloud Workstations provides managed development environments with built-in security, developer flexibility, and support for many popular developer tools. Cloud Workstations addressing the needs of enterprise technology teams.
> 
> * **Developers** can quickly access secure, fast, and customizable development environments anywhere, via a browser or from their local IDE. With Cloud Workstations, you can enforce consistent environment configurations, greatly reducing developer ramp-up time and addressing “works on my machine” problems.
> * **Administrators** can easily provision, scale, manage, and secure development environments for their developers, providing them access to services and resources that are private, self-hosted, on-prem, or even running in other clouds. Cloud Workstations makes it easy to scale development environments, and helps automate everyday tasks, enabling greater efficiency and security. 


One of the most difficult user class to manage as an enterprise admin is the developer.  They require special devices; they often request or want adminstrator privileges on their device, sometimes validly, sometimes not; and they have advanced knowledge of how the computers work meaning they can and do break some of the security properties fairly quickly.

There’s a difficulty around using cloud workstations, but cloud IDE’s and developer VM’s has become a much easier way of providing developers with locked down managed devices, but letting them access systems that can enable them to get their job done.

Of course, this will provide a bunch of security concerns as well.  Knowing exactly how identity is managed, how secrets will be saved on the workstation, and attesting that a given workstation is being operated by a real employee will all become different to how you do it today. 


## [Implementing Phishing-Resistant MFA [pdf] ](https://www.cisa.gov/sites/default/files/publications/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf)

[https://www.cisa.gov/sites/default/files/publications/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf](https://www.cisa.gov/sites/default/files/publications/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf)

> This fact sheet is intended to provide for IT leaders and network defenders an improved understanding of
> current threats against accounts and systems that use multifactor authentication (MFA). MFA is a security
> control that requires a user to present a combination of two or more different authenticators (something you
> know, something you have, or something you are) to verify their identity for login. MFA makes it more difficult
> for cyber threat actors to gain access to networks and information systems if passwords or personal
> identification numbers (PINs) are compromised through phishing attacks or other means. With MFA enabled, if
> one factor, such as a password, becomes compromised, unauthorized users will be unable to access the
> account if they cannot also provide the second factor. This additional layer ultimately stops some of the
> common malicious cyber techniques, such as password spraying.
> 
> CISA has consistently urged organizations to implement MFA for all users and for all services, including email,
> file sharing, and financial account access. MFA is an essential practice to reduce the threat of cyber threat
> actors using compromised credentials to gain access to and conduct malicious activity on networks. However,
> not all forms of MFA are equally secure. Some forms are vulnerable to phishing, “push bombing” attacks,
> exploitation of Signaling System 7 (SS7) protocol vulnerabilities, and/or SIM Swap attacks. These attacks, if
> successful, may allow a threat actor to gain access to MFA authentication credentials or bypass MFA and
> access the MFA-protected systems.
> 
> This fact sheet provides an overview of threats against accounts and systems that use MFA and provides
> guidance on implementing phishing-resistant MFA, which is the most secure form of MFA. CISA strongly urges
> all organizations to implement phishing-resistant MFA as part of applying Zero Trust principles. Note: The
> Office of Management and Budget requires agencies to adopt phishing-resistant MFA methods. While any form
> of MFA is better than no MFA and will reduce an organization’s attack surface, phishing-resistant MFA is the
> gold standard and organizations should make migrating to it a high priority effort 


You might have only just started deploying MFA, but CISA are already lifting the bar once more, and pushing for phishing resistant MFA.  

Note that this isn’t 100% proof against phishing, but attacking these sorts of MFA requires significantly more infrastructure and complexity on behalf of the attacker, and our goal here is to raise the cost to the attacker to the point where they don’t bother.

Naturally the push here is to use WebAuthN or FIDO (think YubiKeys, Titan Keys, as well as Apples PassKey and Windows Hello), or Certificate based PKI such as device attestation from a TPM on the device (again Apples PassKey or Windows Hello support this) 


## [Accidental $70k Google Pixel Lock Screen Bypass - bugs.xdavidhu.me ](https://bugs.xdavidhu.me/google/2022/11/10/accidental-70k-google-pixel-lock-screen-bypass/)

[https://bugs.xdavidhu.me/google/2022/11/10/accidental-70k-google-pixel-lock-screen-bypass/](https://bugs.xdavidhu.me/google/2022/11/10/accidental-70k-google-pixel-lock-screen-bypass/)

> As I did before, I entered the PUK code and choose new a PIN. This time the phone glitched, and I was on my personal home screen. _What? It was locked before, right?_ This was disturbingly weird. I did it again. Lock the phone, re-insert the SIM tray, reset the PIN… And again I am on the home screen. _WHAT?_ My hands started to shake at this point. _WHAT THE F**K? IT UNLOCKED ITSELF?_ After I calmed down a little bit, I realized that indeed, this is a got damn full lock screen bypass, on the fully patched Pixel 6. I got my old Pixel 5 and tried to reproduce the bug there as well. It worked too. 


This is an absolutely brilliant writeup of an astonishing bug.  

What's interesting is that it was originally marked as a duplicate, which implies that someone else had found it, but been unable to provide repeatable steps to allow Google to debug the issue and determine what was going on.


## [Source & Binary / An AWS account just for getting into other AWS accounts ](https://src-bin.com/an-aws-account-just-for-getting-into-other-aws-accounts/)

[https://src-bin.com/an-aws-account-just-for-getting-into-other-aws-accounts/](https://src-bin.com/an-aws-account-just-for-getting-into-other-aws-accounts/)

> In [You should have lots of AWS accounts](https://src-bin.com/you-should-have-lots-of-aws-accounts/) , I made a case for isolating environments and even services in their own accounts to reap all sorts of security, reliability, and compliance benefits. With the right tools in hand ( [Substrate](https://src-bin.com/substrate/) , for one), operating lots of accounts can be just as efficient and far safer than trying to keep all the plates spinning in one account without crashing into each other.
> 
> Accounts that host your various environments and services are only part of the story, though. Odd though it may sound, it takes lots of AWS accounts to have lots of AWS accounts. Your first account is the one you use to configure AWS Organizations, which consolidates billing and gives you access to the APIs for opening and closing additional accounts — that’s your management account. Most folks suggest opening a second account to store audit logs from CloudTrail et al. You might choose to open a third account to host VPCs to share into your service accounts. Just like that, you’re up to three accounts before you even begin to host any compute or storage.
> 
> And the supporting cast of accounts needs one more player — your administrative access account. (That’s not an official name, by the way. Folks also call it an admin(-istrative or -istrator) account, access account, bastion account, or jump account. I’m sure there are more nicknames, too.) The purpose of this account is to help you and your coworkers access all the rest of your accounts. That’s it! This is the AWS account that makes having lots of AWS accounts efficient and safe. It’s the most important account in your organization. 


A nice easy to read writeup on how you should be thinking about your AWS admin accounts (which are not the same as your organisation management account or your security account) 


## [New “Prestige” ransomware impacts organizations in Ukraine and Poland - Microsoft Security Blog ](https://www.microsoft.com/en-us/security/blog/2022/10/14/new-prestige-ransomware-impacts-organizations-in-ukraine-and-poland/)

[https://www.microsoft.com/en-us/security/blog/2022/10/14/new-prestige-ransomware-impacts-organizations-in-ukraine-and-poland/](https://www.microsoft.com/en-us/security/blog/2022/10/14/new-prestige-ransomware-impacts-organizations-in-ukraine-and-poland/)

> This ransomware campaign had several notable features that differentiate it from other Microsoft-tracked ransomware campaigns:
> 
> * The enterprise-wide deployment of ransomware is not common in Ukraine, and this activity was not connected to any of the 94 currently active ransomware activity groups that Microsoft tracks
> * The Prestige ransomware had not been observed by Microsoft prior to this deployment
> * The activity shares victimology with recent Russian state-aligned activity, specifically on affected geographies and countries, and overlaps with previous victims of the FoxBlade malware (also known as HermeticWiper)
> 
> Despite using similar deployment techniques, the campaign is distinct from recent destructive attacks leveraging AprilAxe (ArguePatch)/CaddyWiper or Foxblade (HermeticWiper) that have impacted multiple critical infrastructure organizations in Ukraine over the last two weeks. MSTIC has not yet linked this ransomware campaign to a known threat group and is continuing investigations. MSTIC is tracking this activity as IRIDIUM.
> 
> This blog aims to provide awareness and indicators of compromise (IOCs) to Microsoft customers and the larger security community. Microsoft continues to monitor this and is in the process of early notification to customers impacted by IRIDIUM but not yet ransomed. MSTIC is also actively working with the broader security community and other strategic partners to share information that can help address this evolving threat through multiple channels.
> 
> […]
> 
> In all observed deployments, the attacker had already gained access to highly privileged credentials, like Domain Admin, to facilitate the ransomware deployment. Initial access vector has not been identified at this time, but in some instances it’s possible that the attacker might have already had existing access to the highly privileged credentials from a prior compromise. In these instances, the attack timeline starts with the attacker already having Domain Admin-level access and staging their ransomware payload. 


Interesting blogpost from Microsoft on a new campaign targeting organisations in Ukraine and Poland.  What stood out to me was the mentioned that in all observed deployments, the attacker had already gained access to highly privileged credentials such as Domain Admin.  

This suggests either a use of something like commercial Initial Access Brokers, or an internal model, and a desire to use and exploit those accesses for this campaign. 


## [Research Report | The State of Email Security 2022 | Tessian ](https://www.tessian.com/research/state-of-email-security-2022/)

[https://www.tessian.com/research/state-of-email-security-2022/](https://www.tessian.com/research/state-of-email-security-2022/)

> 94% of organizations experienced a spear phishing or impersonation attack in 2022.
> 
> On average, 1 in 5 advanced email attacks received were successful (18%). Organizations in the U.S. receive on average 1.5 times more spear phishing and impersonation attacks than the global average.
> 
> Impersonation attacks were the most common type of advanced email attack experienced by global organizations in the first nine months of 2022 and they ranked as the top email threat that security leaders are most concerned about.
> 
> Security leaders reported an average of 148 impersonation attacks in 2022, followed by 141 spear phishing attacks, and 135 email-based ransomware attacks. Just over one in 10 global organizations received significantly high volumes of advanced email attacks in 2022 too; 11% received over 450 spear phishing and 12% received over 450 impersonation attacks.
> 
> What’s more, 92% of global organizations experienced at least one email-based ransomware attack in 2022, with 10% of the security leaders surveyed saying they received over 450 email-based ransomware attacks since January 2022. 


Naturally, Tessian wants you to think email security is bad, they sell solutions to help fix it, but the stats in this report as quite eye opening.  Given how many email attacks there are, the 1/5 figure is deeply scary, although probably not surprising.  Email impersonation can range drastically from BEC style emails (”It’s the CFO, go out and buy gift cards for the staff and expense it back to me”) all the way to targetted spear phishing, through to just random people trying it on.

But when thinking about the email security that you provide, we need to remember that telling people not to fall for these tricks isn’t enough.  Ideally no employee should ever receive such an email, or if they do, clicking through should be caught by your security system. 


