---
title: "131 - Protecting the cloud"
date: 2021-01-10
description: "I hope you all had a good Christmas and New Year!"
permalink: /protecting-the-cloud/
---

I hope you all had a good Christmas and New Year!

It was an interesting experience that after I made the decision to take a few weeks break from writing Cyber Weekly, we had what might be the biggest cybersecurity incident in years.  You should therefore have hopefully enjoyed a long read about Solarwinds just before Christmas, and I hope you found it informative and more importantly, you didn't end up working over Christmas to mitigate any damage caused by the incident.  If you did, remember that you do need a break, and that you need to make sure to take that week off sometime soon.  Get some rest and take time to recover.

One of the most interesting things to come out of the Solarwinds experience is not just an awareness of the vulnerability of our systems to their supply chain (more about that in a few weeks), but an awareness of just how vulnerable our cloud instances are to attacks from our physical locations.  I've been arguing for a few years now that the cloud is in many ways more secure than your physical data center for the vast majority of threat models, but I hadn't considered the threat that is posed by the fact that we assume the physical data center to be a trusted center.  If your data center has direct connection to your cloud and is able to bypass all of the security guards, then your cloud isn't more secure, because it still has the weaknesses of the data center at it's heart.

Microsoft have released some good guidance on patterns and changes you might want to make, ensuring that there is appropriate separation between your on premise solutions and your cloud instances.

But just because our cloud instances are patched and well maintained it doesn't mean that there are no risks.  In fact there are all kinds of new risks with cloud services.  This edition there's a number of write ups about cloud specific attacks that can carried out.  We have to remember that when you are running in the cloud, there are accounts and configurations that are far easier to abuse.  Attacks that make use of the cloud infrastructure and configuration are not well documented or articulated at the moment, but some of the articles really do start to improve that.

## [Donald Trump Could Still Launch Nuclear Weapons at Any Time  | WIRED](https://www.wired.com/story/donald-trump-nuclear-weapons-system-reform/)

[https://www.wired.com/story/donald-trump-nuclear-weapons-system-reform/](https://www.wired.com/story/donald-trump-nuclear-weapons-system-reform/)

> Many people assume, wrongly, that some other official has to agree with a presidential order to launch nuclear weapons; surely the White House chief of staff, the secretary of defense, the vice president, or maybe the general in charge of the nation’s nuclear forces has to concur with a presidential launch order, right? Nope. The president can choose to consult with those officials, or whoever else he may like, but from the dawn of the atomic age in the 1940s and 1950s, there has been no procedure to require any such second, concurring opinion in order to authorize a nuclear strike.
> 
> The nation’s hair-trigger alert system is an anachronism of the early days of the Cold War, when the limited size of the US arsenal and its comparatively primitive technology meant that if the weapons weren’t quickly used, they might be destroyed by an incoming attack—and with them, the country’s nuclear deterrent. Advancing technologies and expanding arsenals have negated that fear; today’s nuclear submarines ensure a so-called “survivable deterrent” such that even under the most extreme surprise attack scenarios, the US could still destroy dozens of foreign targets and kill tens of millions of people.


A somewhat sibering reading that reminds us that decision making processes need to be revisited as things change. 


## [Rioters Had Physical Access to Lawmakers’ Computers. How Bad Is That?](https://www.vice.com/en/article/qjpwam/rioters-had-physical-access-to-lawmakers-computers-how-bad-is-that)

[https://www.vice.com/en/article/qjpwam/rioters-had-physical-access-to-lawmakers-computers-how-bad-is-that](https://www.vice.com/en/article/qjpwam/rioters-had-physical-access-to-lawmakers-computers-how-bad-is-that)

> A cybersecurity expert who advised the House and Senate IT on securing their networks, and served as a DHS advisor, said that he was not too worried "about the operational security implications of the yokels who took selfies and bragged online about their miscreance."
> 
> The expert, who asked to remain anonymous as he was not authorized to speak about the work he did for the government, said that the Capitol's systems "have pretty solid endpoint protections. And I'm pretty sure there will be a review/sweep, but because of the ad hoc fragmentation of Capitol systems management it might take weeks."
> 
> Kimber Dowsett, the Director of Security Engineering at Truss and a former cybersecurity worker in the government said that "if it were my shop, I’d throw everything, including the kitchen sink, at this."
> 
> "Remote wipes, rotate creds, the works. And that’s just for assets we know were on premises," Dowsett said in an online chat. "There’s personal devices in the mix, too, so I think IT is going to need to do a lot of outreach to make sure even stolen personal devices are on their radar."
> 
> Matt Tait, a former staffer at the UK spy agency GCHQ, said that Capitol IT administrators will  "eventually need to ask some tough questions like why screens didn't auto-lock, for example, and whether they have things like [disk encryption] Bitlocker and making IT systems more robust to being physically unattended." 


While there are many reasons to focus on the storming of the Capitol building in the US, one of the things that stood out to many armchair analysts like myself was the implications of the physical security of the computers in the Capitol.

Bearing in mind that we don't have much info, just a couple of pictures that imply a single workstation was left unlocked, we don't have a lot to go on.

For many of us, we don't really consider the physical security of the computers.  We tend to build security models in layers, assuming that physical controls in the building will keep people from the main systems we worry about.  The question that the experts will really have to wonder about is not whether an individuals computer was compromised, but whether there were state level attackers hiding in the crowd who used the confusion to target more precise and vulnerable systems.  The SCIF wasn't compromised, but if it was me, I'd be worried about network risers and distribution points across the estate.


## [Fixing a Google Vulnerability | GCP Privlige Escalation and Lateral Movement](https://security.love/blog/gcp/2020/11/22/lateral-movement-and-privesc-in-GCP.html)

[https://security.love/blog/gcp/2020/11/22/lateral-movement-and-privesc-in-GCP.html](https://security.love/blog/gcp/2020/11/22/lateral-movement-and-privesc-in-GCP.html)

> Roughly 2 years ago I (@InsecureNature) shared an Uber ride home with Marc Newlin who in the time span of about 15 minutes detailed a way an attacker could trivially compromise GCP organizations running with default settings, default access patterns and talented engineers doing their best to follow least privilege. This conversation went something like this:
> 
> 
> 
> Fast forward about a month later after matter_of_cat and myself explored the platform and found the defaults were in fact as dangerous as Marc warned them to be, we began to find other privilege escalation paths that seemed at their face to be clear cut vulnerabilities.
> 
> One of these for example includes a vulnerability in Cloudbuild that allows any user of Cloudbuild to steal a credential for a Google managed service account and get access to permissions you didn’t have starting out. 


How do you report a vulnerability in a cloud service, especially when it's a fundamental part of how that service works?  This is a great write up of the problem of overprivileged defaults, and how the author got Google to take action on it.  


## [Lesser Known Techniques for Attacking AWS Environments - tl;dr sec](https://tldrsec.com/blog/lesser-known-aws-attacks/)

[https://tldrsec.com/blog/lesser-known-aws-attacks/](https://tldrsec.com/blog/lesser-known-aws-attacks/)

> This post will discuss lesser known attack techniques that I would use in attacking AWS accounts and conclude with a discussion of defenses. A common theme among many of these concepts is abusing trust, whether that is incorrectly trusting attacker controlled resources hosted on AWS, or the trust relationships between accounts or within an account.
> 
> I’ll discuss a few techniques in gaining initial access, recon, lateral movement between accounts, and data exfiltration.


Lovely post for articulating and updating our threat models for AWS account attacks.


## [Subdomain Takeover: Going for High Impact](https://0xpatrik.com/subdomain-takeover-impact/)

[https://0xpatrik.com/subdomain-takeover-impact/](https://0xpatrik.com/subdomain-takeover-impact/)

> For someone like me, who deeply explored the realms of takeovers as well as their implications, this bothered me a lot. Not the fact that I am unable to find more "low hanging fruit", but rather that companies are taking a blindfolded view about the impact of subdomain takeovers in their infrastructure. I thus started to think about every possible escalation you can make to showcase the high impact this problem can have. This post explains my conclusions.


What is the impact of a subdomain takeover?  If someone can create foobar.yourcompany.com does it really matter?  Some security people would have the opinion that it's low impact, but in fact, the ability to create a subdomain, especially an arbitrary subdomain can give a huge amount of capability to an attacker.  

This post articulates some of things that you can do if you can take over a subdomain.


## [Zak Doffman on Twitter: "This is the #Signal Vs #iMessage Vs #WhatsApp Vs #FacebookMessenger metadata graphic from my @Forbes article on #Apple’s privacy labels… This is your data and you’re entitled to ask why it’s being collected and processed. https://t.co/Oy0N7j1YNx https://t.co/JLGPdCrFBw" / Twitter](https://twitter.com/UKZak/status/1346244253333164034)

[https://twitter.com/UKZak/status/1346244253333164034](https://twitter.com/UKZak/status/1346244253333164034)

> This is the #Signal Vs #iMessage Vs #WhatsApp Vs #FacebookMessenger metadata graphic from my 
> @Forbes
>  article on #Apple’s privacy labels… 
> 
> This is your data and you’re entitled to ask why it’s being collected and processed.


The article linked in this tweet is great as well, but I really wanted to get the infographic in as well.  

I've noticed constant notifications over the last few days indicating my phonebook moving over to Signal, and that's coming from people who are privacy aware and not necessarily technical experts.  


## [SMS Phishing Is Getting Out Of Control](https://www.vice.com/en/article/m7appv/sms-phishing-is-getting-out-of-control)

[https://www.vice.com/en/article/m7appv/sms-phishing-is-getting-out-of-control](https://www.vice.com/en/article/m7appv/sms-phishing-is-getting-out-of-control)

> Apart from significant and widespread anecdotal evidence, there is some hard evidence that Smishing is on the rise. According to security firm Proofpoint, text message phishing went up 328 percent in the third quarter of the year, compared to the previous onesecond trimester. 
> 
> "Smishing attacks are on the rise probably because they are so successful. This is because people have been trained to react to notifications and messages on their devices instantaneously," Apurva Kumar, a staff security intelligence engineer at mobile security firm Lookout told Motherboard in an email. 


Reminder that in the UK, you can forward smishing emails to SPAM (7726) which will send them to a takedown service that acts attempting to take down phishing services and reduce the impact on others.


## [Protecting Microsoft 365 from on-premises attacks - Microsoft Tech Community](https://techcommunity.microsoft.com/t5/azure-active-directory-identity/protecting-microsoft-365-from-on-premises-attacks/ba-p/1751754)

[https://techcommunity.microsoft.com/t5/azure-active-directory-identity/protecting-microsoft-365-from-on-premises-attacks/ba-p/1751754](https://techcommunity.microsoft.com/t5/azure-active-directory-identity/protecting-microsoft-365-from-on-premises-attacks/ba-p/1751754)

> Many customers connect their private corporate networks to Microsoft 365 to benefit their users, devices, and applications. However, there are many well-documented ways these private networks can be compromised. As we have seen in recent events related to the SolarWinds compromise, on-premises compromise can propagate to the cloud. Because Microsoft 365 acts as the “nervous system” for many organizations, it is critical to protect it from compromised on-premises infrastructure.
> 
>  
> 
> This document will show you how to configure your systems to protect your Microsoft 365 cloud environment from on-premises compromise. We primarily focus on Azure AD tenant configuration settings, the ways Azure AD tenants can be safely connected to on-premises systems, and the tradeoffs required to operate your systems in ways that protect your cloud systems from on-premises compromise.


An interesting inversion on the normal IT view.  We often think of the cloud as the risky thing, and our on-premise estate as more secure.  This guidance talks about how to protect your well patched and managed cloud instances from your shonky old on-premise estate.


## [Using Microsoft 365 Defender to protect against Solorigate - Microsoft Security](https://www.microsoft.com/security/blog/2020/12/28/using-microsoft-365-defender-to-coordinate-protection-against-solorigate/)

[https://www.microsoft.com/security/blog/2020/12/28/using-microsoft-365-defender-to-coordinate-protection-against-solorigate/](https://www.microsoft.com/security/blog/2020/12/28/using-microsoft-365-defender-to-coordinate-protection-against-solorigate/)

> This blog is a comprehensive guide for security operations and incident response teams using Microsoft 365 Defender to identify, investigate, and respond to the Solorigate attack if it’s found in your environment. The description of the attack in this blog is based on current analysis and investigations by researchers across Microsoft, our partners, and the intelligence community who are actively collaborating to respond to the attack. This is an active threat that continues to evolve, and the findings included here represent what we know at the time of publishing. We continue to publish and update intelligence, indicators, tactics, techniques, and procedures (TTPs), and related details as we discover them. The [report](https://msrc-blog.microsoft.com/2020/12/13/customer-guidance-on-recent-nation-state-cyber-attacks/) from the Microsoft Security Response Center (MSRC) includes the latest analysis of this threat, known indicators of compromise (IOCs), and initial recommended defenses, and will be updated as new data becomes available.


This is a well written and detailed read to understand what the impact of the Solarwinds attack is on your organisation if the attacking team decided to move beyond the simple compromise of your Orion server. 


