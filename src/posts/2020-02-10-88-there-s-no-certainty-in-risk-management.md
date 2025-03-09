---
title: "88 - There's no certainty in risk management"
date: 2020-02-10
description: "If you've never seen a risk matrix, then the idea of talking about risks being unlikely, rare, likely and contrasting that with the impact of the risk might seem unusual to you.  Here is [a sample risk matrix](https://www.researchgate.net/figure/Risk-rating-matrix-Impact-probability-matrix_fig1_332424825) to help with the below"
permalink: /there-s-no-certainty-in-risk-management/
---

If you've never seen a risk matrix, then the idea of talking about risks being unlikely, rare, likely and contrasting that with the impact of the risk might seem unusual to you.  Here is [a sample risk matrix](https://www.researchgate.net/figure/Risk-rating-matrix-Impact-probability-matrix_fig1_332424825) to help with the below

But it's likely that you've seen something that describes risks in this way.  "This has a very low chance of happening, and a medium impact, so this is a low risk".  I've written lots of statements myself as part of risk assessments, and one of the odd parts of the whole process is the determination of how likely the risk actually is.

The thing with those risk matrices, is that they are qualitative rather than quantitive.  People describe likelihoods as very low, low, medium, high and very high.  It's easy for someone to turn those into numbers, say 1 to 5, and then perform maths on it, but this leads to some weird behaviours.  In theory a very low likelihood risk, (1), with a very high impact (5) might have a total risk score (5x1 = 5) that is the same as a very high likelihood risk (5) and a very low impact risk (1) (Total risk score 1x5 = 5).  But if you move either of the very lows up by one, the risk total would jump to 10 (2x5 or 5x2).  This quantised score gives an impression of being a sliding scale (saying oh, that risk is a 16 out of 25), but in reality because of the multiplication, there are only certain notches that a risk total can be.  For those interested, in a 5x5 matrix, that's 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 20, 25... which is a weird frequency distribution.

But worse than that, I've found myself struggling with the lack of willingness to ascribe certainty in the model.  One entertaining risk statement I read in someone elses risk assessment included the likelihood and impact of a cleaner or janitor in AWS's data center using their access to get hold of a physical disk drive.  The likelihood was marked as Very Low, which is good, but I wanted to know why there wasn't a "Never" option.  It boils down to whether you think there is even an infinitesimal chance that this event can happen.  Risk managers can be told all about how physical access is carefully monitored.  About metal scanners on the doors to ensure that nothing is smuggled out, but often they are unwilling to ever say that there is absolutely no chance that this will happen.  

However, with our graded structure, as you can see from the sample risk matrix, if the impact is very high, then even a very low likelihood risk is going to come out as a medium risk in our assessment.  I've seen many a Government service with a policy that all medium risks need to be addressed before the service can go live.

In our example of physical access, we might talk about using on-disk encryption, which has a performance impact on the servers, or we might try to insist on our own special controls on the hosting provider (good luck with that).

All of this is why I struggle with risk management as practiced at many organisations today.  The reality of risks that are well below a certain likelihood threshold is just not included.  And mostly that's because risk advisors don't want to be the one who said a risk was so unlikely not to bother, and then find out later that they were wrong.  I don't know how we fix it, but it's worth remembering next time someone starts talking about risks in that manner.  Because if you dig a little bit, you'll almost certainly find that there's some pseudoscience behind it that isn't being presented to you.  Give that stuff a look and ask yourself whether the likelihood and impact scores are really what you think they are.

## [What I Learned Watching All 44 AppSec Cali 2019 Talks - tl;dr sec](https://tldrsec.com/blog/appsec-cali-2019/#the-call-is-coming-from-inside-the-house-lessons-in-securing-internal-apps)

[https://tldrsec.com/blog/appsec-cali-2019/#the-call-is-coming-from-inside-the-house-lessons-in-securing-internal-apps](https://tldrsec.com/blog/appsec-cali-2019/#the-call-is-coming-from-inside-the-house-lessons-in-securing-internal-apps)

> OWASP AppSec California is one of my favorite security conferences: the talks are great, attendees are friendly, and it takes place right next to the beach in Santa Monica. Not too shabby 😎
> 
> One problem I always have, though, is that there are some great talks on the schedule that I end up missing.
> 
> So this year I decided to go back and watch all 44 talks from last year’s con, AppSec Cali 2019, and write a detailed summary of their key points.
> 
> If I had realized how much time and effort this was going to be at the beginning I probably wouldn’t have done it, but by the time I realized that this endeavor would take hundreds of hours, I was already too deep into it to quit 😅


This is a monster of a read, when Clint says "a detailed summary of their key points", I personally saw "summary" rather than "detailed", but in reality each of these is nearly a blogpost in itself.  I've been reading bits and pieces for several weeks, and still haven't really taken it all in.  I keep thinking about linking to individual talks here, and I will dedicate an entire newsletter to picking the best talks in the coming weeks (once I've finished reading them all), but for now, if you want a great learning resource, this is a really good place to start.


## [AWS Security Documentation](https://docs.aws.amazon.com/security/)

[https://docs.aws.amazon.com/security/](https://docs.aws.amazon.com/security/)

> AWS Security Documentation
> Cloud security at AWS is the highest priority. AWS customers benefit from a data center and network architecture that are built to meet the requirements of the most security-sensitive organizations. The following documentation shows you how to configure AWS services to meet your security and compliance objectives.


A useful resource from AWS.  This is a single page that indexes and references the security documentation for every AWS tool.  Instead of knowing that your team is using AWS Kendra, or AWS AppStream, and having to go find the front page for that tool, and then try to find anything relating to security in that tool, you can start here and find the security information for any given tool.


## [Infosec Skills Matrix](https://infosecskillsmatrix.com/rolesskills)

[https://infosecskillsmatrix.com/rolesskills](https://infosecskillsmatrix.com/rolesskills)

> 


This is a lovely resource for getting a look at what skills people in your team should have.  I notice that there is no entries for managers, leaders, CISO's and security consultants, I suspect because "spreadsheets" and "taking meetings" just aren't attractive skills!


## [NIST Privacy Framework](https://www.nist.gov/system/files/documents/2020/01/16/NIST%20Privacy%20Framework_V1.0.pdf)

[https://www.nist.gov/system/files/documents/2020/01/16/NIST%20Privacy%20Framework_V1.0.pdf](https://www.nist.gov/system/files/documents/2020/01/16/NIST%20Privacy%20Framework_V1.0.pdf)

> Under the Privacy Framework’s riskbased approach, organizations may not need to achieve every outcome or activity reflected in the Core.
> 
> When developing a Profile, an organization may select or tailor the Functions, Categories, and Subcategories to its specific needs, including developing its own additional Functions, Categories, and Subcategories to account for unique organizational risks. An organization determines these needs by considering its mission or business objectives, privacy values, and risk tolerance; role(s) in the data processing ecosystem or industry sector; legal/regulatory requirements and industry best practices; risk management priorities and resources; and the privacy needs of individuals who are directly or indirectly served or affected by an organization’s systems, products, or services.
> 
> As illustrated in Figure 6, there is no specified order of development of Profiles. An organization may first develop a Target Profile in order to focus on its desired outcomes for privacy and then develop a Current Profile to identify gaps; alternatively, an organization may begin by identifying its current activities, and then consider how to adjust these activities for its Target Profile. 


This actually looks quite good.  I really like the idea of saying "We have a privacy profile, showing what we do about Identifying, Governing, Controlling, Communicating and Protecting privacy right now, and a target privacy profile for what we want to do"
That's a nice admission that just because we can't fix everything at once, shouldn't stop us setting a good target.  Too often I've seen cybersecurity or other risk frameworks fall down because we say "our existing systems would be under this bar, so we need to set the bar lower".


## [TunnelBear Completes 3rd Annual Independent Security Audit](https://www.tunnelbear.com/blog/tunnelbear-completes-3rd-annual-independent-public-security-audit/)

[https://www.tunnelbear.com/blog/tunnelbear-completes-3rd-annual-independent-public-security-audit/](https://www.tunnelbear.com/blog/tunnelbear-completes-3rd-annual-independent-public-security-audit/)

> With that, we'd like to announce the results of our third annual independent security audit. We hired Cure53 to audit our entire codebase, infrastructure, website and apps so we could have a clear picture of TunnelBear's current security posture. You can find the full report on Cure53's website, but here's a quick breakdown.
> 
> [...]
> 
> In total, Cure53 found 2 Critical, 4 High, 1 Medium, 2 Low and 3 Informational issues-which were all fixed promptly. Similar to the results of last year's audit, the few issues that were found to be of concern required access to a user's device and heightened permissions. For more information about the findings, please read the full report on Cure53's site.


VPN's are something that is becoming more common among even normal users, but choosing a VPN is a hard task.  How do you know whether a VPN is trustworthy or not?  The VPN marketplace is pretty crowded, and there's good suspicion that some of those operators are very shady in one way or another.

It's nice therefore to see a VPN provider who has regular independent security audits.  A commitment to transparency is a good thing for a communication provider who is guaranteeing you privacy.  My only concern here is that this feels like a lot of high risk issues that were created in the last year.  Looking at the detail, the two critical's are really quite bad, remote code execution on the VPN client, and Stored XSS on their admin portal backend.  But given that we have very little information on other VPN providers it's hard to tell how good a result this is. My current VPN provider, NordVPN, has also had [a security audit](https://nordvpn.com/blog/nordvpn-completes-app-security-audit/) but just the one so far.  Based on the transparency of this alone, I'd feel much more confident recommending them to non-technical family members


## [Dropping Anchor: From a TrickBot Infection to the Discovery of the Anchor Malware](https://www.cybereason.com/blog/dropping-anchor-from-a-trickbot-infection-to-the-discovery-of-the-anchor-malware)

[https://www.cybereason.com/blog/dropping-anchor-from-a-trickbot-infection-to-the-discovery-of-the-anchor-malware](https://www.cybereason.com/blog/dropping-anchor-from-a-trickbot-infection-to-the-discovery-of-the-anchor-malware)

> This variant of TrickBot employs a new, unique ability to steal passwords from KeePass, a free, open- source password manager. TrickBot's KeePass stealing capabilities seem to be inspired (or even partially copy-pasted) from a publicly available tool dubbed PoshKPBrute, a script that performs a dictionary attack against KeePass .kdbx files. Once it finds the dictionary key, it dumps all passwords as an output and sends the attackers the master password.
> 
> The threat actor evaluates information sent back to the C2 server and identifies if they have successfully infected a high-value target. If so, they escalate their efforts by switching to interactive hacking: reconnaissance, credential dumping, lateral movement, and in some cases the mass deployment of ransomware across endpoints connected to the domain controller.


A couple of interesting things here.  From all accounts this looks like the initial infection vectors are pretty much automated.  They get Trickbot onto the machine, grab as much info as they can to identify what they've found, and then only if it's a high value target do they switch to interactive hacking.

Secondly, this phishing attempt is using a password bruteforcer to try to unlock and steal passwords from a password manager.  No indication that it is trying to go after online services such as 1Password or LastPass though.  All those people claiming that keeping the KeePass database on your own computer is more secure might need to rethink their threat models. I don't really think there's much difference in the overall risk to a user between KeePass and an online service, this attack could have scripted browser sessions and potentially gotten access that way.


## [Kubernetes Security monitoring at scale with Sysdig Falco](https://medium.com/@SkyscannerEng/kubernetes-security-monitoring-at-scale-with-sysdig-falco-a60cfdb0f67a)

[https://medium.com/@SkyscannerEng/kubernetes-security-monitoring-at-scale-with-sysdig-falco-a60cfdb0f67a](https://medium.com/@SkyscannerEng/kubernetes-security-monitoring-at-scale-with-sysdig-falco-a60cfdb0f67a)

> Once the noisiest events were removed we started to see some interesting findings — one of the most interesting ones (and alarming too!) was containers running with root privileges; this is dangerous because running a containerized app can for instance allow attackers to escalate into the host machine and escalate from there (more details in this article). After we found this, we wanted to find out the reason why this was happening, in Skyscanner we have custom docker images for each of our most used languages (Python, Java, Node and now Go as well), those images have been created in collaboration with Security so they follow all our standards (not running as root is one of them), but in some special cases teams need to use a different base image or language, and the base images available online don’t usually set up a user and end up running as root. This was helpful to highlight the need to review our strategy on Pod Security policies to prevent this from going forward.
> 
> We’re able to action the results with our ChatSecOps Bot ‘Hermes’, this bot is configured with a series of rules that scan the received data from a source (in this case the Falco findings, with the information added by our mapping tool) and uses it to contact the owner of the resource where an anomaly is detected and inform them about the event. And finally we are working on making the bot to asks the owner of the service via our ChatSecOps Bot if they are the ones executing the action that triggered the rule. If the owner of the resource responds ‘No’ the bot will trigger an Incident Response process.


There's so much to like about this blog.  Security tooling running in your Kubernetes cluster.  The decision to run as a DaemonSet so every node will run Falco in a sidecar style configuration. The tool to marry together metadata about AWS accounts and Kubernetes deployments so they know who is running what.

But what really stood out to me was the attitudinal and cultural statements like the ones quoted above.  The security team discovered containers running their processes as the root user in the container.  That's against their policies, but they didn't shut them down, they didn't tell the developer they were rubbish, they looked to understand why.  Furthermore, the statement that docker images are created in collaboration with security, which is a great example of showing how security can enable secure development, by being helpful and most importantly working upstream.  By working with base container image creation techniques, those secure base images affect most of the service teams, without security needing to scale to put someone in every service team!

Secondly, the amount of work in the team to ensure that when an alert comes in, it's not sent to the security team, to be analysed and understood.  They already said they deploy over 160 services, and there's no way for a central security team to understand all of those services and know whether something is a real security issue or not.  So instead they did the hard work to map pods to service teams and the teams slack channel, and then are building a bot to interactively check with the team.


## [Errata Security: How to decrypt WhatsApp end-to-end media files](https://blog.erratasec.com/2020/01/how-to-decrypt-whatsapp-end-to-end.html#.Xj2RAlL7QUE)

[https://blog.erratasec.com/2020/01/how-to-decrypt-whatsapp-end-to-end.html#.Xj2RAlL7QUE](https://blog.erratasec.com/2020/01/how-to-decrypt-whatsapp-end-to-end.html#.Xj2RAlL7QUE)

> At the center of the "Saudis hacked Bezos" story is a mysterious video file investigators couldn't decrypt, sent by Saudi Crown Prince MBS to Bezos via WhatsApp. In this blog post, I show how to decrypt it. Once decrypted, we'll either have a smoking gun proving the Saudi's guilt, or exoneration showing that nothing in the report implicated the Saudis. I show how everyone can replicate this on their own iPhones.


This is a lovely walkthrough of how to extract WhatsApp messages from an iPhone including decrypting videos and images sent via WhatsApp.  Remember, end to end encryption does not protect the messages when they are on the device.  It just protects you against people reading the communications between the endpoints


## [Facebook Tells US Attorney Bill Barr It’s Not Prepared To Get Rid Of Encryption On WhatsApp And Messenger](https://www.buzzfeednews.com/article/ryanmac/facebook-encryption-stays-bill-barr-letter-whatsapp)

[https://www.buzzfeednews.com/article/ryanmac/facebook-encryption-stays-bill-barr-letter-whatsapp](https://www.buzzfeednews.com/article/ryanmac/facebook-encryption-stays-bill-barr-letter-whatsapp)

> “It is simply impossible to create such a backdoor for one purpose and not expect others to try and open it,” wrote WhatsApp head Will Cathcart and Messenger head Stan Chudnovsky in Facebook's response. “People’s private messages would be less secure and the real winners would be anyone seeking to take advantage of that weakened security. That is not something we are prepared to do.”
> 
> End-to-end encryption prevents anyone — governments, security agencies, or hackers — from accessing or viewing the contents of a message between two parties and is a key feature on popular apps such as WhatsApp and Signal. Government agencies have long desired a means of accessing message content on encrypted apps, arguing that it’s in the interest of public safety despite broader privacy concerns.


This is a good argument from Facebook, and one that I mostly pretty much agree with.  The intelligence and law enforcement focus is, or should be moving from intercepting the communication data to targeting the endpoints.  That's both less bulk invasive on general people, and are more valuable to law enforcement anyway.  But because it's potentially more noticeable on the target device, and that it doesn't scale, there is a general unwillingness to let go of the existing tapped communications infrastructure.


