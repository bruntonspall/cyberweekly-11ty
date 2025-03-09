---
title: "98 - Governance isn't a dirty word"
date: 2020-04-19
description: "I've spent a long time working in Agile.  I was on one of the first really big agile programmes of work at the Guardian, and introduced to many of the concepts by people who went on to be great thinkers and definers in agile development.  "
permalink: /governance-isn-t-a-dirty-word/
---

I've spent a long time working in Agile.  I was on one of the first really big agile programmes of work at the Guardian, and introduced to many of the concepts by people who went on to be great thinkers and definers in agile development.  

As I've grown through the process however, I've noticed that a lot of people proclaiming the wonder of agile have a strong distaste for any form of "Governance".  They use it as a dirty word, to sum up and summarise the weeks and months that projects spend trying to get approval for change, or release authority, or technical design authorities. 

We confuse authority of decision making for informational awareness all the time, and we call both "Governance".

As organisations, the leaders need to know what decisions are being made in the organisation in order to lead effectively.  The old [Spotify model](https://medium.com/productmanagement101/spotify-squad-framework-part-i-8f74bcfcd761) trope, where a leader provides direction to bring "alignment", but allows teams autonomy to make decisions on how to get to the solution to the problem requires leaders to both identify and communicate a problem, but also if they are to iterate their goals, their directions and the articulation of the problem, requires them to have visibility and understanding of the decisions that teams are making.

This ability to see and understand where teams are making decisions, to see outliers where someone is doing something novel and unusual and be able to drill down into why is the heart of Governance.  If your teams make technical decisions, and I believe that delivery teams must be enabled to make their own decisions, then you also need some mechanism for those decisions to be recorded and to be broadcast out to other teams, and up the management chain.

If you have 20 teams, and you declare that you think that the only true agile governance is through "show and tells", then you are requiring every manager to put aside 20 x 30 minute slots of time each week/fortnight/iteration to see what the teams are doing.  You also need the teams to agree on who gets what time slot to ensure that senior managers can go to every show and tell, that none overlap.  If you grow your organisation to 100 teams, then your entire executive board no longer has any working time in a given week for any work other than going to show and tells.

Instead, we need technical governance, mechanisms where tech leads can coordinate, feedback and increase team alignment without slowing down the teams.  We need cultural governance that allows team structures and delivery artefacts to be consistent, so that reporting and understanding of the teams is nicely aligned.  We need all these governance mechanisms to understand where people make decisions that deviate from the majority of teams, in order to understand whether that team has a unique context, or whether the default decision for the organisation needs to change.

Without these mechanisms in place, you can set out what you want to achieve all you like, but you'll never know whether your vision is being delivered upon, because in any organisation of any reasonable size, you just won't get the feedback about the effectiveness of your problem definition, you won't get feedback on how effectively your current technology and culture works and you won't know whether you are being effective.

Governance isn't a dirty word, it's even more necessary in the [volatile, uncertain, complex and ambiguous world](https://en.wikipedia.org/wiki/Volatility,_uncertainty,_complexity_and_ambiguity) that agile works with so effectively.

## [Amazon Detective – Rapid Security Investigation and Analysis | AWS News Blog](https://aws.amazon.com/blogs/aws/amazon-detective-rapid-security-investigation-and-analysis/)

[https://aws.amazon.com/blogs/aws/amazon-detective-rapid-security-investigation-and-analysis/](https://aws.amazon.com/blogs/aws/amazon-detective-rapid-security-investigation-and-analysis/)

> Amazon Detective works across your AWS accounts, it is a multi-account solution that aggregates data and findings from up to 1000 AWS accounts into a single security-owned “master” account making it easy to view behavioral patterns and connections across your entire AWS environment.
> 
> There are no agents, sensors, or additional software to deploy in order to use the service. Amazon Detective retrieves, aggregates and analyzes data from AWS Guard Duty, AWS CloudTrail and Amazon Virtual Private Cloud Flow Logs. Amazon Detective collects existing logs directly from AWS without touching your infrastructure, thereby not causing any impact to cost or performance.


This looks like a really neat tool for looking for unusual behaviour in your AWS accounts.  There's a 30 day free trial and the pricing is based on the amount of data consumed per region, so there's no huge overhead to ingesting data.  The only downside is that data ingestion is automatic, so you can't pick and choose your data sources, instead it's pretty much everything in a region for a given account.  If you've got a region/account with a lot of VPC flow logs because it has a lot of traffic, that's a cost you can't easily control.


## [Summit Route - Isolated networks on AWS](https://summitroute.com/blog/2020/03/31/isolated_networks_on_aws/)

[https://summitroute.com/blog/2020/03/31/isolated_networks_on_aws/](https://summitroute.com/blog/2020/03/31/isolated_networks_on_aws/)

> To explain this setup, let’s first look at a simple physical example of an isolated computer. Imagine a single physical computer in an empty room. This is not connected to the Internet or any network. It has power and is connected to a single LED light, and this computer contains sensitive information in it. I then hire you (and you happen to be malicious) to write some code that turns this light on or off for me, based on some code you write.
> 
> Maybe the algorithm you write tells me to buy or sell a stock based on whether the light turns on or off. Your only input to me is a physical CD I put in the computer, and I run your code on this computer while I’m there by myself. You aren’t in the room. Under these circumstances, it is possible to avoid having you learn whether the light was turned on or off, and without exfilling the sensitive data from the computer out. We can assume that precautions have been taken to avoid the attacker monitoring the power usage to the room, TEMPEST monitoring, or other threats.
> 
> Although contrived, this is a rough enough approximation of some real-world situations, especially those worried about inside threats.
> 
> Example in AWS
> Now we want to recreate this setup in AWS, so instead of a local physical computer we have an EC2, and instead of an LED, a message is sent to an SQS. You give me code to run on the EC2, and it sends a 1 or 0 to the SQS. In order to have an isolated network, the VPC this EC2 runs in has no Internet Gateway, NAT Gateway, IPv6 Egress-Only Gateway, or other means of communicating out to the Internet or from the Internet into the network. The Route Table has a single entry for the 10.0.0.0/24 traffic to target the “local” network.


The concept of isolated computers or networks, or ones with very controlled ingress and egress are valuable in a bunch of situations.  In these worlds, the network partitioning is one of the major security controls that ensures that even if the code on the device is somewhat malicious, it can't easily operate on data and send command and control or data out of the system.  But real systems must have some method of getting data in and data out, otherwise they are useless.  
This AWS setup of a system that can process data and send carefully controlled SQS messages is a fun one to play with.  The researcher covers DNS Exfiltration, the difficulty in isolating SQS and other AWS endpoints, and shows some workable ways to minimise these exfiltration routes.  It's not perfect, but if you are considering an AWS malware analysis lab or similar, this is an interesting read.

(I'll note that this assumes that the underlying AWS infrastructure, management and operators are trustworthy.  If you are dealing with stuff where a compromise of AWS is a possibility, none of this will work for you.  That's not a realistic risk in most cases)


## [Securing your home network in preparation for Working From Home](https://scotthelme.co.uk/securing-your-home-network-for-wfh/)

[https://scotthelme.co.uk/securing-your-home-network-for-wfh/](https://scotthelme.co.uk/securing-your-home-network-for-wfh/)

> I'm fortunate to have spent the last few years either working from home or travelling the World doing training, consultancy and public speaking. With the recent Coronavirus epidemic having quite literally wiped my travel schedule clean, I find myself doing a lot more working from home and imagine others may too. In this post I'm going to look at a few steps to boost the security of my home network using the Unifi Security Gateway. You may not have the exact same hardware as me, but the principles will translate into other hardware setups too.


There's something about the risk model for home Wifi networks that get's people really confused and upset.  Most attackers are unlikely to come into your home network by parking up outside your house and jumping on your Wifi.  

You probably also don't want to treat your home network as compromised and be forced to use a VPN to prevent anything on the network from seeing your stuff. 

But there is a reasonable concern about all of those devices you want and need to add to your wifi.  Are they all in the same risk bracket? Do they all really need the same access?  While this is beyond the capabilities of most home workers, if you've invested in some decent home network kit (like the Unifi stuff, which I have as well), you may as well make use of it.  Having a dedicated network for IoT devices where they can compromise each other and get out to the internet, but can't compromise your desktops/laptops/phones etc, isn't a bad move.  If you don't have the capability, I wouldn't worry, but if you've already got the capability around, then you may as well use it.


## [Getting started with security keys — PaulStamatiou.com](https://paulstamatiou.com/getting-started-with-security-keys/#register_keys)

[https://paulstamatiou.com/getting-started-with-security-keys/#register_keys](https://paulstamatiou.com/getting-started-with-security-keys/#register_keys)

> So you've purchased a security key or a few and are ready to set things up.. great! Each security key you own must be registered with each service you wish to use it on such as Google, 1Password, Facebook, GitHub, et cetera.
> 
> You'll register each key one by one. Usually navigating to the website's settings page related to two-factor auth and finding a button to add a key. This assumes you've already setup two-factor auth. Then when prompted you plug your key in and tap it. Depending on the website you may be prompted to type in a name for each key. This step is vital as it helps you identify which key to remove from the service in the event you lose that key and have multiple registered on the same service.22
> 
> And that's pretty much it. Once a key is registered with a service, the next time you log in 23 it's as easy as touching your security key when prompted after entering your username and password.


(Joel) Two Factor authentication (2FA) or Two Step Verification (2SV) Multi Factor Authentication (MFA) is, simply put, great for account security and you should enable and use it where offered - particularly on high-value accounts like your email or social media.

In a world where you can sometimes choose between email-based (a one-time code/link sent to your email address), SMS-based (a one-time code sent via SMS), TOTP-based (most commonly a 6 digit code in an app with a 30 second countdown) or hardware-based (there are other options I've skipped): hardware-based, when implemented using a strong existing standard, is the 'strongest' but most people don't use hardware tokens and you should use whatever your comfortable with (some MFA is better than no MFA).

The hardware token effectively negotiates with the service, it understands that service and the service understands that token (separate from all other tokens in the world). If the wrong service (lets say, a phishing site) convinces you to try that token, it won't work. Because you now need this token to login (some services offer fallback options, some are quite strict) you should configure two (or more) and ensure one is safe and sound as a backup incase you lose the main one (as most people will put them on their keychain).


## [Money Stuff: WeWork Wants SoftBank’s Money - Bloomberg](https://www.bloomberg.com/news/newsletters/2020-04-07/money-stuff-wework-wants-softbank-s-money)

[https://www.bloomberg.com/news/newsletters/2020-04-07/money-stuff-wework-wants-softbank-s-money](https://www.bloomberg.com/news/newsletters/2020-04-07/money-stuff-wework-wants-softbank-s-money)

> Inside Natixis SA’s New York office, nerves frayed after the French bank sent traders to a recovery site outside the city so cramped that social distancing was impossible, one person said. The firm later ditched the plan and sent people home, where employees received an important email from a top executive: “Highly Confidential: Covid 19 - Staff Infection List.”
> 
> Workers who clicked the attachment realized it was an anti-phishing test on behalf of the compliance team and that they had failed it. Many were furious, the person said.
> 
> That’s gross but also I kind of admire it, that’s a really good phishing subject line, how could anyone resist clicking that? Even having read the punch line I still would probably open that attachment.


This is a weird story, the WeWork/Softbank stuff continues to mystify me.  However this anecdote of a "compliance team" conducting an internal phishing test by sending an email *from a top executive* to all staff about COVID-19 just makes me angry.

This isn't the way to get people to stop clicking malicious attachments, the correct way is to install decent mail handling tools that make it impossible to send malicious attachments.  That way nobody will ever click a malicious attachment.  Far more effective.

All this achieved was made people angry and made them trust security even less


## [Deploys at Slack - Several People Are Coding](https://slack.engineering/deploys-at-slack-cd0d28c61701)

[https://slack.engineering/deploys-at-slack-cd0d28c61701](https://slack.engineering/deploys-at-slack-cd0d28c61701)

> But as the number of customers grew, so did the amount of infrastructure it took to run our application. Soon, our push-based deploy model couldn’t cope with the number of servers we were adding. Each additional server increased deploy time. Even strategies like parallel rsyncs had their limits.
> Eventually, we resolved this issue by switching to a fully parallel pull-based system. Instead of pushing the new build to our servers using a sync script, each server pulls the build concurrently when signaled by a Consul key change. This allows us to maintain a high velocity of deploys even as we continue to scale.


A good look at deployment mechanisms that work and scale in high performing companies.  I helped move the Guardian to pull based deploys back in 2012 and it's still one of the technical achievements I'm most proud of.  Automating deployment tooling allows you to move deployment processes from beign written down and followed poorly to being done by computers reliably and repeatedly.

Pull based deploys in particular gives a huge amount of benefits in terms of both the scalability of the deployment systems, but also the immutability of the deployment artifact.  This gives you far greater confidence in your build system and far greater confidence in your tests.


## [Classifying types of “Security Work” - Starting Up Security - Medium](https://medium.com/starting-up-security/classifying-types-of-security-work-ebbbd3e6d4ae)

[https://medium.com/starting-up-security/classifying-types-of-security-work-ebbbd3e6d4ae](https://medium.com/starting-up-security/classifying-types-of-security-work-ebbbd3e6d4ae)

> The following represent the four categories of Security Work mapped to their counterparts in The Phoenix Project. Below are examples of each type of work, and some commentary on it as an organization. These types of work are Business Projects, Security Engineering, Security Operations, Incidents and Unplanned Work. I’ve included their original names from The Phoenix Project below. The overall workflow expects that an organization plans for (and completes) very predictable work in the top three categories to avoid Incidents and Unplanned work downstream. The next goalpost is to move Business Projects and Security Operations work toward Security Engineering and eliminate the business dependencies on security and the toil of operational work


A good overview of the types of work that a security team can do.  This assumes a certain viewpoint of security, this is very much an engineering driven security team, the ones who are running the SOC, onboarding new systems and so on.  This doesn't cover the wider remit of a CISO, such as the risk management functions, audit capability and so on.  Ryan explicitly calls that out as he has a different model for risk assessment anyway.

One of the things that I think is missing here is a clear advisory or consultancy style of work.  One of the things that the Phoenix Project and the Unicorn Project makes clear is that decisions tend to happen upstream.  As Ryan makes clear, many security teams feel like they get involved too late in security projects.  Advisory services should be there to work with early projects, to give advice and guidance, potentially to set standards.  That to me is a critical part of the work as it creates the feedback loop into the team that is doing the security engineering and operations work, to let them know whether their products are actually meeting the needs of teams or not.


## [UK government technology interoperability is far from easy](https://medium.com/@joelgsamuel/the-future-of-uk-government-technology-interoperability-70e8b79f2ef9)

[https://medium.com/@joelgsamuel/the-future-of-uk-government-technology-interoperability-70e8b79f2ef9](https://medium.com/@joelgsamuel/the-future-of-uk-government-technology-interoperability-70e8b79f2ef9)

> Each Whitehall department is sovereign when it comes to things like technology choices and information security ownership. They are independent Data Controllers when it comes to the Data Protection Act (2018)/GDPR.
> 
> They have their own CIOs, CISOs, CTOs, COOs, CFOs and Permanent Secretaries (for simplicity, a CEO).
> 
> While two Whitehall departments may use the same productivity tool (for example, Google G-Suite) these are unique tenants isolated from each other. Further, not all Whitehall departments use Google G-Suite, most use Microsoft Office 365 — again, unique and isolated configurations.
> 
> Two departments using Microsoft Office 365 does not mean they can use the features of the platform ‘together’ even if they can within their own organisation.
> 
> There is a technical and security distrust between government departments. This isn’t born of anything malicious but simply not knowing what the other department does with it’s IT and how it manages information.
> 
> Recorded video/audio conferencing, free-text chat and document sharing presents some rather gnarly information governance challenges.
> 
> While departments exchange information all the time, the exchange is generally deliberate and manual. Tying organisations together to allow workstream collaboration at pace will have an open floodgate type affect (in my view, good!)
> 
> As each department is sovereign for information governance, they claim (for sometimes bad reasons) they are unwilling (not unable) to allow certain things to happen — for example, allowing guests from outside of their organisation to join videoconferences created by their staff.
> 
> In order for true workstream collaboration to take hold across Whitehall, the underlying information governance challenges stemming from information co-creation, co-retention, co-securing, co-archival and co-releasing (FOIA responses, push to The National Archives, de-classification etc) must be overcome.


This is a good reminder from regular contributor to this newsletter, Joel, that the problems here around information sharing and collaboration aren't just technical, they are about information ownership, process and governance.  We can talk about how much better GSuite is at coediting all we like, but if we can't give senior people assurances about who can see information, who can share information and how that benefits them, all they tend to see is the risk of their information ending up in the wrong place.


## [The Githubification of InfoSec - John Lambert - Medium](https://medium.com/@johnlatwc/the-githubification-of-infosec-afbdbfaad1d1)

[https://medium.com/@johnlatwc/the-githubification-of-infosec-afbdbfaad1d1](https://medium.com/@johnlatwc/the-githubification-of-infosec-afbdbfaad1d1)

> Too often we see attacks at the same time yet learn to defend alone. This paper shows how community-based approaches to infosec can speed learning for everyone. Imagine a world where attack knowledge is curated in MITRE ATT&CK. Then Sigma rules are developed to build concrete detections for each attack technique. Then any hits for those rules could be triaged and investigated by a tailor-made Jupyter notebook.
> 
> When researchers publish on a novel technique or CERT organizations warn of a new attack, they can jump start defenders everywhere by contributing elements in each of these frameworks. If every organization were to contribute their unique expertise, and every organization were to build on the expertise of others, infosec silos could be connected through a network effect to outpace attackers. Defenders going far, together.


This is a call to arms for blue teams and defenders.  Are you using the same software development capabilities that development teams have been using for the last two decades, or are you stuck manually writing queries in splunk or some other pane of glass, unable to share, unable to reuse and unable to advance?


## [GAO Report: CYBERSECURITY DOD Needs to Take Decisive Actions to Improve Cyber Hygiene [pdf]](https://www.gao.gov/assets/710/705886.pdf)

[https://www.gao.gov/assets/710/705886.pdf](https://www.gao.gov/assets/710/705886.pdf)

> Beyond the initiatives above, DOD has 
> 
> (1) developed lists of the techniques that adversaries use most frequently and pose significant risk to the department, and 
> (2) identified practices to protect DOD networks and systems against these techniques. 
> 
> However, the department does not know the extent to which these practices have been implemented. The absence of this knowledge is due in part to no DOD component monitoring implementation, according to DOD officials. Overall, until DOD completes its cyber hygiene initiatives and ensures that cyber practices are implemented, the department will face an enhanced risk of successful attack.


The US Government Audit Office has looked at how effectively the US Department of Defence has implemented their cybersecurity program.  Despite the negative headlines, they've done quite a lot of good work, defining a bunch of positive practices, putting in place some cybersecurity awareness training and more.

However, as always, the complexity in rolling out an effective program like this is not just the delivery.  People saying "just implement a cyberawareness program" don't understand the complexity of the situation.  The problem here is the lack of accountability, governance and reporting.  

The DOD security bigwigs told everyone that they needed to use the new awareness program, but many of the departments feel no need to report to the CIO on the progress of those tasks.  of 17 tasks, the CIO is responsible for 10 of them, and is reporting on them, but 7 of them have no effective ownership within the organisation and therefore nobody is saying whether they've been done.

This mirrors the complexity in many organisations, the CISO or CTO can implement some measures within their teams, but do they have the authority or capability to know whether other business units are doing what they say?

One of the biggest investments a security team can make is improving self reporting, making people feel like talking to security is a pleasurable experience that doesn't evoke fear of being told off, and ensure that there are good easy avenues to report this stuff.


