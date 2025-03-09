---
title: "219 - When is a credential not a credential?"
date: 2023-01-15
description: "In the move to zero-trust, the concept of credentials to authenticate users comes up a lot."
permalink: /when-is-a-credential-not-a-credential/
---

In the move to zero-trust, the concept of credentials to authenticate users comes up a lot.

We tend to think of a credential as the thing that the user uses to confirm to the computer who they are.  This is typically a username and a password, but we can add a second factor such as a notification on a phone, but we can also use something like as a cryptographic key held in a secure enclave unlocked by biometrics (such as Windows Hello, FaceId or TouchId).

But real authentication credentials for many systems are far more complex.  Your computer itself needs to authenticate itself to the network, to the services it wants to use, and might use a machine identity to do so.  That might be a cryptographic token, or it might just be a name or network address.

But you don’t want to have to type in your username and password for every file access or network access that your computer does once you’ve logged in.  If you listed a directory with hundreds of files, you’d need to be typing all day. 

So instead, in most authentication systems there is some kind of trade, the users credential is used to ask for a temporary access token, which the computer keeps and then uses on each request.  That means that when you start clicking around on the file server, each request has the token with it, and the file server can use that to determine whether it’s valid or not.

Traditional attacks on authentication, such as phishing and some malware attacks, rely on stealing the users credentials and using those.  But with the rise of 2FA and better security for those credentials, attackers instead start to use [“golden ticket”](https://attack.mitre.org/versions/v10/techniques/T1558/) or [“pass the hash”](https://attack.mitre.org/techniques/T1550/002/) style attacks.  These are harder for attackers to carry out, partly because of technical complexity, and partly because most of these credentials are time limited, so must be used quickly, or recaptured over and over. 

None of this is easy to solve, and the increasing complexity of IT systems and how entwined they are in our business makes it harder and harder to apply simple solutions, because some part of your system will be reliant on a legacy or hard to change component that doesn’t support the authentication system you want to use.

## [CircleCI incident report for January 4, 2023 security incident ](https://circleci.com/blog/jan-4-2023-incident-report/)

[https://circleci.com/blog/jan-4-2023-incident-report/](https://circleci.com/blog/jan-4-2023-incident-report/)

> By January 4, 2023, our internal investigation had determined the scope of the intrusion by the unauthorized third party and the entry path of the attack. To date, we have learned that an unauthorized third party leveraged malware deployed to a CircleCI engineer’s laptop in order to steal a valid, 2FA-backed SSO session. This machine was compromised on December 16, 2022. The malware was not detected by our antivirus software. Our investigation indicates that the malware was able to execute session cookie theft, enabling them to impersonate the targeted employee in a remote location and then escalate access to a subset of our production systems.
> 
> Because the targeted employee had privileges to generate production access tokens as part of the employee’s regular duties, the unauthorized third party was able to access and exfiltrate data from a subset of databases and stores, including customer environment variables, tokens, and keys. We have reason to believe that the unauthorized third party engaged in reconnaissance activity on December 19, 2022. On December 22, 2022, exfiltration occurred, and that is our last record of unauthorized activity in our production systems. Though all the data exfiltrated was encrypted at rest, the third party extracted encryption keys from a running process, enabling them to potentially access the encrypted data.
> 
> […] **A note on employee responsibility vs. systems safeguards** We want to be clear. While one employee’s laptop was exploited through this sophisticated attack, a security incident is a systems failure. Our responsibility as an organization is to build layers of safeguards that protect against all attack vectors. 


This is a really honest and good response to a breach.  It’s open, transparent and critically, it doesn’t blame the user.  As they say, although a users device was compromised, that’s not the fault of the user, it’s a systemic failure that it was possible for that to happen.

Couple of things from the incident to note:

1. Although they used 2FA for authentication, once you have authenticated you need to be given a token that can be used around the system to prove you are authenticated.  Stealing that token allows adversaries to impersonate you.  Doing that is reasonably difficult (ok, actually it’s only moderately difficult once you know what you are doing, but knowing to do it is the key, and it’s not default in most redteam tools, so it’s not a common TTP).  This doesn’t make 2FA useless, and you shouldn’t abandon or throw out 2FA just because it has a weakness.  Instead its a natural progression of actors when faced with a 2FA system.  The answer to this is some of the more advanced zero-trust networking concepts, ensuring that risk decisions are taken on access and unusual access requires reauthentication.

2. Encryption isn’t infalible.  In fact, I’m increasingly of the view that encryption-at-rest is overused in situations where it’s not actually helping against attackers.
Encryption-at-rest works to prevent adversaries from making off with your data when it’s powered off.  That means on USB sticks, burnt onto CD’s, or in detachable hard drives it works just fine.  But to an attacker on the system, if the system has to access the data, then the encryption keys must also be accessible and you are gaining very little benefit.  
It will still be a mandatory control for compliance reasons for a long time I suspect, but we should remember where it works and where it offers little or no benefit.
(And yes, I’m over-simplifying, there are some benefits especially with security modules and with good privilege separation etc.  I just mean that sprinkling the magic encryption-at-rest fairy dust over a system doesn’t magically make it secure) 


## [They See Me Roaming: Following APT29 by Taking a Deeper Look at Windows Credential Roaming | Mandiant ](https://www.mandiant.com/resources/blog/apt29-windows-credential-roaming)

[https://www.mandiant.com/resources/blog/apt29-windows-credential-roaming](https://www.mandiant.com/resources/blog/apt29-windows-credential-roaming)

> In early 2022, Mandiant detected and responded to an incident where APT29 successfully phished a European diplomatic entity and ultimately abused the Windows Credential Roaming feature. The diplomatic-centric targeting is consistent with Russian strategic priorities as well as [**historic APT29 targeting**](https://www.mandiant.com/resources/blog/apt29-continues-targeting-microsoft) . Mandiant has been tracking APT29—a Russian espionage group that is [**sponsored by the Foreign Intelligence Service (SVR)**](https://www.mandiant.com/resources/unc2452-merged-into-apt29) —since at least 2014. Some APT29 activity is also publicly referred to as [**Nobelium by Microsoft**](https://www.microsoft.com/security/blog/2021/11/10/the-hunt-for-nobelium-the-most-sophisticated-nation-state-attack-in-history/) .
> 
> During the short timespan that APT29 was determined to be active inside the victim network, Mandiant observed numerous LDAP queries with atypical properties (Figure 1) performed against the Active Directory system.
> 
> The queried LDAP attributes relate to usual credential information gathering (e.g. unixUserPassword); however, one attribute in particular stood out: `{b7ff5a38-0818-42b0-8110-d3d154c97f24}` , or `msPKI-CredentialRoamingTokens` , which is [**described by Microsoft**](https://docs.microsoft.com/en-us/windows/win32/adschema/a-mspki-credentialroamingtokens) as ‘ _storage of encrypted user credential token BLOBs for roaming_ ’. Upon further inspection, Mandiant identified that this attribute is part of a lesser-known feature of Active Directory: Credential Roaming. 


One of the hardest things about the concept of zero trust and “single sign on” is the sheer number of things on your system that need to access stuff on your behalf and therefore need some kind of credential.  Even if you’ve got two-factor-authentication and absolutely brilliant sign on systems with lots of identity factors, there’s a good chance that somewhere a printer needs some way to authenticate you.

Many of the weird little backends to Active Directory and other identity systems are because you need a way to tell a door, a printer, a telephone or some other non-desktop computer thing who you are at some point, and then it needs to work on your behalf.

Seeing attackers start to find these weirder credentials and use them is going to make life hard because things like Roaming Tokens are there to ensure you can use the IT around you, without needing to put your YubiKey into a random printer each time you use it.

There are patterns to solve this, but they are hard, and you need every part of your IT ecosystem to support it, which is rarely the case 


## [InfoQ Software Trends Report: Major Trends in 2022 and What to Watch for in 2023 ](https://www.infoq.com/articles/infoq-software-trends-report-2022/)

[https://www.infoq.com/articles/infoq-software-trends-report-2022/](https://www.infoq.com/articles/infoq-software-trends-report-2022/)

> As a technical leader, the architect’s role is to communicate architecture decisions effectively with all stakeholders. We are seeing companies adopt Architecture decision records (ADRs) and make them standard practice.
> 
> Recognizing the value of the senior individual contributor (IC) role, which is labeled as "Staff Plus." Individuals in these roles have deep technical expertise but are also often "T-shaped" with a wide range of skills. These individuals can move between IC and management roles within their software development careers.
> 
> DevOps and platform engineering practices can help reduce developer cognitive load and increase positive business outcomes. 


This trend report from InfoQ is interesting.  InfoQ tends to focus on “the cutting edge of enterprise IT”, so it watches what startups and big tech are doing, but it only starts to recognise the trends when those practices are adopted by big and slower corporate organisations.

The change in career development for seniors is something that has been bouncing around for a few years.  This concept that as you become more senior, you must become a manager is an anathama to a number of technical people.  But this concept of a career pendulum, swinging forwards and backwards between technical management roles (like engineering manager, VP engineering or CTO) and technical leadership roles (like staff engineer, principle architect etc) seems to be catching on.  Not fixating on the idea that a career commitment is forever helps technical people move into management, and we desperately need more people organising roadmaps, career paths and corporate structures who have lived experience at the coal face.

As always, I’m also pleased to see that the focus on internal platforms is catching.  Internal platforms are ways that tools can embed policies, and if security and technology can be involved they can make small changes to the internal developer platforms that have huge working ramifications into every working team.  Massive opportunities for changing the corporate defaults across your organisation here. 


## [Kubernetes Security For CISOs ](https://blog.ksoc.com/kubernetes-security-for-cisos/)

[https://blog.ksoc.com/kubernetes-security-for-cisos/](https://blog.ksoc.com/kubernetes-security-for-cisos/)

> There are plenty of security habits that can mitigate a ton of security risks right away when first implementing Kubernetes.
> 
> The first is single-tenancy and multi-tenancy clusters. When thinking about single-tenancy or multi-tenancy from a Kubernetes perspective, it could be anything from how many users have access to a cluster to what applications are running on the cluster. Taking it from a user perspective, Kubernetes clusters can be set up for dev environments that only one user has access to, which would mean every user could get their own Kubernetes cluster, mitigating multi-tenancy risks. If multi-tenancy is needed, which in many cases it is, setting up proper RBAC permissions for users is a crucial starting point. That way, users only have access to what they need.
> 
> When it comes to Kubernetes, every resource that’s being interacted with is part of the Kubernetes API. Where there’s an API, there are logs, metrics, and traces. A proper log aggregator or an observability combo, like Prometheus and Grafana, can retrieve security logs from a Kubernetes cluster which would help teams mitigate any risk that comes their way. They can also set up alerts for these logs so they know about them right away.
> 
> From a segregation perspective, it’s important to set up proper Namespace habits from the beginning. Depending on access levels, users may have the ability to deploy applications and resources across any namespace, including the Default or even kube-system, which houses the core Kubernetes Pods needed to run the cluster. Instead of that being an issue, users and service accounts should only have access to deploy apps to specific Namespaces


This is a nice high level view of Kubernetes.  There’s loads of guides about what to consider as a team using Kubernetes, or what you need to do to operate a cluster, but this is one the first resources dedicated to thinking about the overall security impact of Kubernetes.

Lots of good points in here, and I wish it was longer (a section on security monitoring of kubernetes itself, and on the monitoring of applications within the kubernetes infra would be useful for example), but calling out the roles and responsibilities that come into segregation is a good point in here that really should be emphasised.  

It’s easy to consider the containers as security boundaries, but because the system is tenanted, it’s really easy for accounts, authentication tokens and users to jump boundaries if you don’t get it setup right from the beginning.  That entire management plane has a huge amount of power and needs thinking through really carefully.


## [Blockbuster NYTimes Story Accidentally Leaked Phone Numbers of Russian Soldiers Criticizing War ](https://www.vice.com/en/article/epz3xj/new-york-times-exposed-russian-soldiers-criticizing-war-phone-numbers)

[https://www.vice.com/en/article/epz3xj/new-york-times-exposed-russian-soldiers-criticizing-war-phone-numbers](https://www.vice.com/en/article/epz3xj/new-york-times-exposed-russian-soldiers-criticizing-war-phone-numbers)

> Motherboard found the Times website included not only the numbers of apparent soldiers on these calls, but also the alleged family members back home. That included the number that placed the call, the number that received it, and apparent notes from Times’ fact checkers on the caller’s identities.
> 
> “Exposing the phone number of the families of Russian troops is exposing those family members to risks,” Rid added.
> 
> While those soldiers or family members could be targeted for their criticisms of the war, security researcher Matthew Tait said. “On the Russian state side, the targeting is, in my opinion, much more likely due to potential exposure of senior officers and the Russian state in identifying directed war crimes than for criticism of Putin.”
> 
> When originally published in September, some of the audio files included in the story contained pieces of metadata that contained a date, a timestamp, and a series of digits. Those digits appear to be phone numbers. This month, a security researcher flagged the issue to Motherboard. The security researcher requested anonymity because they did not want to draw the attention of either Russian or Ukrainian authorities.
> 
> After Googling one, Motherboard found the first and last name of an individual who appeared to be a Russian soldier, as listed on a website that was set up to dox Russian soldiers who are allegedly fighting in the war in Ukraine. 


It’s a bit tricky to work out from this story exactly what happened.  But it looks like the NTTimes left the metadata in the voice files that they uploaded alongside the story. 

This kind of operational security error is classic.  You see these as challanges in Capture-The-Flag competitons all the time, although normally it’s metadata such as geolocation coordinates, left in photos.

When publishing accompanying data, you need to ensure you have good metadata scrubbing systems.  Metadata in anything you want to publish should only be Metadata you mean to be there.

Sadly because Metadata is almost always invisible to the user in normal tools, it’s really hard for hard worked, non technical people like newspaper editors to catch these things unless they are trained and given tools and practices to do 


## [Rolling out Yubikeys - a thread ](https://twitter.com/clintgibler/status/1613204164615733248?s=12&t=jmyaQtVfZGkBoHMaAez6Tw)

[https://twitter.com/clintgibler/status/1613204164615733248?s=12&t=jmyaQtVfZGkBoHMaAez6Tw](https://twitter.com/clintgibler/status/1613204164615733248?s=12&t=jmyaQtVfZGkBoHMaAez6Tw)

> 


A thread of really interesting reports on the roll out of Yubikeys as MFA.  As is neatly pointed out in several of the threads, buying the keys is the easiest bit of the whole thing.  Changing the authentication flow for almost every system requires effort, it requires planning and critically it requires user training.

The example of users who plugged their key into both their phone and their laptop at the same time was a really good example of the sort of thing you’ll only find out when they’re in the hands of the users.

Secondly, the other thing that stood out to me was the decision to migrate security first. If you are going to make everyone else do something, you should be willing to feel the pain of having it done.  

I like that idea, but it does create it’s own problem.  If you are the first to have it rolled out, then by the time others are having it rolled out, you sometimes forget the pain you went through.  You lose your empathy for how hard it is, because you’ve had yours for months already.

Volunteering seniors and security to be the first victims of a technology change ensures that you get the onboarding right the first time.  But keep records of what the experience was like, and make sure that you use it to improve the experience for everyone coming after you. 


## [Cuba and the Geopolitics of Submarine Cables | Kentik Blog ](https://www.kentik.com/blog/cuba-and-the-geopolitics-of-submarine-cables/)

[https://www.kentik.com/blog/cuba-and-the-geopolitics-of-submarine-cables/](https://www.kentik.com/blog/cuba-and-the-geopolitics-of-submarine-cables/)

> This week marks a decade since the [ALBA-1 submarine cable](https://en.wikipedia.org/wiki/ALBA-1) began carrying traffic between Cuba and the global internet. On 20 January 2013, I [published the first evidence](https://web.archive.org/web/20130121174409/http://www.renesys.com/blog/2013/01/cuban-mystery-cable-activated.shtml) of this [historic subsea cable activation](https://www.reuters.com/article/cuba-internet/cubas-mystery-fiber-optic-internet-cable-stirs-to-life-idUKL1N0AR9TQ20130122) which enabled Cuba to finally break its dependence on geostationary satellite service for the country’s international connectivity.
> 
> ALBA-1 was one of my first lessons on how geopolitics can shape the physical internet.
> 
> Last month’s recommendation by the US Department of Justice to deny the request by the [ARCOS](https://www.submarinecablemap.com/submarine-cable/arcos) cable system to connect Cuba shows that, almost a decade later, geopolitics continues to shape the physical internet — _especially when it comes to Cuba_ . 


This was thoroughly educational for me.  Like many others, I’m just so used to the idea that the internet connects the world, that I rarely think about the physical cables that connect countries.  The fact that geopolitics comes into play about which cables can be connected to each other and what it provides a country is a reminder that below our current abstracted view, there is often a far more complex system underneath. 


