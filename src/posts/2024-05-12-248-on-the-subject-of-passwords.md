---
title: "248 - On the subject of passwords"
date: 2024-05-12
description: "I hope you've all had a glorious week.  The UK had the early May bank holiday weekend and I've had a delightful holiday with the return of the sunshine, so I didn't write an edition last weekend as I was enjoying a much needed break instead."
permalink: /on-the-subject-of-passwords/
---

I hope you've all had a glorious week.  The UK had the early May bank holiday weekend and I've had a delightful holiday with the return of the sunshine, so I didn't write an edition last weekend as I was enjoying a much needed break instead.

That means that I missed "World Password Day", which is mostly silly, but a useful opportunity to reflect on where we are and where we have gotten to.

Back about five yeras ago (if not longer), the UK's NCSC came out with what seemed [revolutionary password advice ](https://www.ncsc.gov.uk/collection/passwords/updating-your-approach), which was mostly "stop telling your users to create random complex passwords, it doesn't really work".  This sociotechnical approach was founded on real user research that reinforced what many of us have known for a long time.  If you tell people that they have to jump through complex hoops, they'll find ways to work around it because they don't care about their password, they just want to get the job done.  Users will invariably put numbers and symbols on the end of passwords if they are required to include them, and most will pick either the ! or @ symbol.  For numbers, users will just add a 1 to the end and if you force people to change their password reguarly, they'll just increment the number by 1 each time.  

Humans like systems that help them understand and manage complexity, and this is how most normal people get around the fact that you need to remember about 200 passwords to exist in daily life.

Since then, we've mostly accepted that as an industry, although I still find systems that mandate an upper case character, a lower case character, a digit, a symbol, an emoji and a sacrifical chicken dance in their password.

But we're now in a place where we've moved from having to make up millions of complex passwords to ... having to use an MFA app on your shopping app, and needing MFA for my gym for some reason.

This is good in a way, MFA is a good way of preventing someone stealing your account, providing it's phishing proof, and most of the ones that are in use don't meet that criteria.  To be phising proof, the MFA app needs to cryptographically validate that the request came from the right site and then sign the response using secret that can't be easily copied.  That means it needs hardware, whether an external hardware token like a FIDO2 token, or hardware built into your laptop, phone or tablet such as a passkey.

But we need to think carefully about how users will approach this process or system.  Because making people use their FIDO2 hardware keys for every tiny app they use in their life isn't going to end well for anyone.

Instead we need some way to tier the accounts in our lives.

For me, and I suspect for most people, that means that there are about 4 major accounts that should be using good MFA, and the rest can probably use just complex passwords from a password manager.

Those are my Gmail account, my Microsoft account and my Apple account.  These three between them protect my browsers including my password managers built into them, and they also protect my devices, ensuring my android, windows and iPhone devices are secured for me and me alone.  

Secondly, my password manager, which is the core of my access the rest of my accounts.  (I'm still torn on using built in browser password managers, mostly because I switch around browsers and devices a lot, so an external password manager gives me some confidence in that, but that's probably me being weird)

Luckily for me, all of those accounts are able to be secured using with hardware keys, and now with Passkeys, which are less portable for logging into other computers, but mean that my core devices such as my phone and tablet can authenticate in a really secure way that it's that device and has authenticated my presence or PIN.

Getting that core secured properly gives me confidence that the root of my online identity is secured against simple phishing attacks and it's a small burden on me as a user.

Are we in a state where I can recommend this to the non-technical people in my life?  I think we did pass that bar in the last year or so, there's enough support in those major accounts to make it worth it, but it's still not approachable enough for my liking.  But we're getting there and this password day, I feel like we are closer than ever to making our core accounts phish resistant

## [How MFA Is Falling Short ](https://www.kolide.com/blog/how-mfa-is-falling-short)

[https://www.kolide.com/blog/how-mfa-is-falling-short](https://www.kolide.com/blog/how-mfa-is-falling-short)

> [**If not passwords, then what?**](https://www.kolide.com/blog/how-mfa-is-falling-short#if-not-passwords-then-what) If you take one thing away from this blog, let it be this: we _need_ to get rid of passwords. The security industry has been saying it for years, but it’s been a slow drip for that mindset to turn into action. Luckily, we have the resources now with FIDO2. [FIDO2](https://www.microsoft.com/en-us/security/business/security-101/what-is-fido2) (Fast IDentity Online 2–ignore the tortured acronym) is an open standard for user authentication that strengthens security and protects users by using phishing-resistant and passwordless cryptographic credentials to validate user identities.
> 
> Developed by the [FIDO Alliance](https://fidoalliance.org/) , FIDO2 can be accomplished by two types of FIDO authenticators: roaming authenticators and platform authenticators. Roaming authenticators are portable hardware devices like Yubikeys that are plugged into devices cross-platform. And platform authenticators are embedded into users’ devices that generally require biometrics like Apple’s Touch ID or Face ID.
> 
> However, these are traditionally the second factor in a passwordless MFA experience. The first is passkeys. Passkeys in their simplest form are FIDO2 sign-in credentials that generate a pair of private and public passkeys that provide passwordless authentication. That means a bunch of random numbers that aren’t phishable!
> 
> […] [**Don’t forget about devices**](https://www.kolide.com/blog/how-mfa-is-falling-short#dont-forget-about-devices) While we’ve focused on the user identity portion of MFA, an unpatched or compromised device can do just as much damage as a weak password.
> 
> The presence of a device trust tool like Kolide by 1Password works as a possession factor; basically, if a device doesn’t have [Kolide](https://www.kolide.com/) installed, it can’t log in. So compromised credentials won’t work, and employees can’t be tricked into giving this factor away to a bad actor. But beyond that, Kolide looks for compliance issues before letting a user log in, like an out-of-date browser. Making sure devices are in a secure state before they authenticate goes a long way to keeping out bad actors trying to piggyback into your systems. 


This is a good take on the current state of MFA, which is that we’ve got people starting to use it, but people aren’t moving to phish-proof MFA fast enough.  We know that hardware keys like FIDO tokens and now passkeys are far harder to phish, so if you are considering how to bring your security up for a subset of your organisation, then jump straight there and don’t do the authenticer/type numbers approach first. 


## [Microsoft rolls out passkey auth for personal Microsoft accounts ](https://www.bleepingcomputer.com/news/microsoft/microsoft-rolls-out-passkey-auth-for-personal-microsoft-accounts/)

[https://www.bleepingcomputer.com/news/microsoft/microsoft-rolls-out-passkey-auth-for-personal-microsoft-accounts/](https://www.bleepingcomputer.com/news/microsoft/microsoft-rolls-out-passkey-auth-for-personal-microsoft-accounts/)

> Microsoft announced that Windows users can now log into their Microsoft consumer accounts using a passkey, allowing users to authenticate using password-less methods such as Windows Hello, FIDO2 security keys, biometric data (facial scans or fingerprints), or device PINs.
> 
> Microsoft "consumer accounts" refer to personal accounts for accessing Microsoft services and products such as Windows, Office, 365, Outlook, One Drive, Copilot, and Xbox Live.
> 
> Microsoft announced the new support for passkeys as part of World Password Day to increase security against phishing attacks, aiming to eliminate passwords altogether in the future. 


And you should be following this guidance to enable passkeys for your personal Microsoft accounts as well. 


## [Google Online Security Blog: Your Google Account allows you to create passkeys on your phone, computer and security keys ](https://security.googleblog.com/2024/05/passkeys-on-your-phone-computer-and-security-keys.html)

[https://security.googleblog.com/2024/05/passkeys-on-your-phone-computer-and-security-keys.html](https://security.googleblog.com/2024/05/passkeys-on-your-phone-computer-and-security-keys.html)

> Last year, [Google launched passkey support](https://blog.google/technology/safety-security/the-beginning-of-the-end-of-the-password/) for Google Accounts. Passkeys are a new industry standard that give users an easy, highly secure way to sign-in to apps and websites. Today, we announced that passkeys have been used to authenticate users more than 1 billion times across over 400 million Google Accounts.
> 
> […]
> 
> * Simpler sign-in. Passkeys can act as a first- and second-factor, simultaneously. By creating a passkey on your security key, you can skip entering your password. This replaces your remotely stored password with the PIN you used to unlock your security key, which improves user security. (If you prefer to continue using your password in addition to using a passkey, you can turn off [“Skip password when possible”](https://myaccount.google.com/signinoptions/passwordoptional) in your Google Account security settings.)
> 
> Passkeys bring strong and phishing-resistant authentication technology to a wider user base, and we’re excited to offer this new way for passkeys to meet more user needs. 


Give this a try on your main Google Account.  You may not want to trust passkeys 100% and allow complete sign in,, but you should definitely consider signing up to use passkeys as a second form factor at least.  You cna sign up for Google’s passkey support at [g.co/passkeys](http://g.co/passkeys) 


## [Phishing Attack Targets LastPass Users’ Master Passwords ](https://duo.com/decipher/phishing-attack-targets-lastpass-users-master-passwords)

[https://duo.com/decipher/phishing-attack-targets-lastpass-users-master-passwords](https://duo.com/decipher/phishing-attack-targets-lastpass-users-master-passwords)

> In order to convince LastPass users to hand over their passwords, attackers used a mix of phone calls, phishing emails and a phishing page under the domain “help-lastpass[.]com,” which has since been taken down. If they were able to successfully obtain the users’ master passwords, attackers would log into the victims’ accounts and lock them out by changing their primary phone numbers, email addresses and the master password itself.
> 
> “Initially, we learned of a new parked domain (help-lastpass[.]com) and immediately marked the website for monitoring should it go live and start serving a phishing site intended to imitate our login page or something similar,” according to Mike Kosak, senior principal intelligence analyst with LastPass, [in a Wednesday statement.](https://blog.lastpass.com/posts/2024/04/advanced-phishing-kit-adds-lastpass-branding-for-use-in-phishing-campaigns) “Once we identified that this site went active and was being used in a phishing campaign against our customers, we worked with our vendor to take down the site.” 


I like password managers and it’s one of the things I find myself frequently reocmmending because it lets people manage the advice to have unique passwords per site.  I don’t know the passwords to a huge number of my accounts because they are stored in a password manager.  That I means I can’t type them into the wrong address or the wrong location or hand them over to phishers easily. 

But of course that makes our password managers themselves the targets of attack and makes any compromise of your password manager account particuarly devestating.  So make sure that you secure your password manager as best you can. 


## [Read Satya Nadella’s Microsoft memo on putting security first ](https://www.theverge.com/24148033/satya-nadella-microsoft-security-memo)

[https://www.theverge.com/24148033/satya-nadella-microsoft-security-memo](https://www.theverge.com/24148033/satya-nadella-microsoft-security-memo)

> Microsoft CEO Satya Nadella is now making it clear to every employee that security should be prioritized above all else. _The Verge_ has obtained a memo from Nadella to Microsoft’s more than 200,000 employees, where he discusses the new security overhaul and how the company is learning from attackers to improve its security processes. Nadella also makes it explicitly clear that employees should not make security tradeoffs:
> 
> > If you’re faced with the tradeoff between security and another priority, your answer is clear: Do security. In some cases, this will mean prioritizing security above other things we do, such as releasing new features or providing ongoing support for legacy systems. This is key to advancing both our platform quality and capability such that we can protect the digital estates of our customers and build a safer world for all.
> 
> Nadella wants Microsoft employees to approach the challenge of overhauling security “with both technical and operational rigor,” even looking at every line of code as an opportunity to improve Microsoft’s security. “It’s everyone’s top priority and our customers’ greatest need,” says Nadella. 


It’s going to be interesting seeing the fallout from this.  Microsoft has had a bad 6 months, with multiple nation state compromises that have proved difficult to manage.  In their defence, most of those have used incredibly advanced attacks, but it’s been clear that there are weaknesses within the core of the Microsoft ecosystem.  

They have come out publicly about those attacks and now have come out publicly about how they are going to prioritise security.  That’s a big step and they deserve some applause for doing so in such a big way.  However the devil is going to be in the details, and Microsoft is a huge corporation with many complex lines of business, so this is going to take time to really settle down and see what the changes mean 


## [Breaking down Microsoft’s pivot to placing cybersecurity as a top priority ](https://doublepulsar.com/breaking-down-microsofts-pivot-to-placing-cybersecurity-as-a-top-priority-734467a8db01?source=rss----8343faddf0ec---4)

[https://doublepulsar.com/breaking-down-microsofts-pivot-to-placing-cybersecurity-as-a-top-priority-734467a8db01?source=rss----8343faddf0ec---4](https://doublepulsar.com/breaking-down-microsofts-pivot-to-placing-cybersecurity-as-a-top-priority-734467a8db01?source=rss----8343faddf0ec---4)

> I’ll say up front, it’s a great email. I think Satya and Charlie are killing it with messaging. Frankly, everybody likes to talk about cybersecurity and pretend it’s super interesting.. until they actually have to do it.
> 
> Because cybersecurity is, frankly, major boring (and far too expensive) shit — and also really hard to do right and _super easy_ to do wrong. So it’s the kind of email you have to send from the top as you need people internally to go ‘oh, this is a real thing’.
> 
> It’s a really good response, which high level grapples with a whole bunch of problems I saw within Microsoft. Truthfully, the problems I saw at Microsoft extended way beyond what is known, and I don’t want to document them publicly as — frankly — they appear to know parts of the barn are, in fact, on fire.
> 
> […]
> 
> I think when you had Brad Smith talking about “being on the frontlines” of the Russia/Ukraine war, on the side supporting Ukraine, it was the right thing to do — but also, you’re relying on having the best cybersecurity in the world. Microsoft was already a target, but essentially it’s like screaming ‘come at me, I’m hard’ in a Call of Duty match. I don’t think the execs at Microsoft had a full view of the security challenges they are facing.
> 
> That isn’t to say everything Microsoft has been doing in cybersecurity is wrong, by the way — it isn’t, they employ some of the smartest people in security and deal with an incredible amount of incidents nobody knows about. What I mean is, some risky things there are normalised — things straight up in CISA’s Bad Practice list, that Microsoft helped write — and were deemed okay because.. uh… they’re Microsoft.
> 
> > do as i say not as i do — the customer experience
> 
> In a PowerPoint slide, it looks like every unpatched system is automatically booted from the network after 2 weeks, 100% green! In reality, if you looked at the real details… you’d hit the red. I call this the Watermelon Green effect.
> 
> To be clear, I have no idea if that PowerPoint slide exists at Microsoft (it probably does, based on what I’m told as a customer by MS sales about Microsoft’s amazing internal security) — it’s just a made up example of that I think every org can learn from. If people aren’t bringing out their dead, too, you’re looking at death by compliance and governance, especially where everything is incentivised to be green.
> 
> […]
> 
> I do think, though, Microsoft are on the right track here towards earning my trust back as a customer. They’re talking about real internal issues at Microsoft — in a corporate blog cosplay way of course — and actually heading straight at long standing and festering issues which need addressing.
> 
> I’d also say, people shouldn’t take the CSRB report to be criticisms of Microsoft’s security _product_ offerings. They aren’t. Microsoft’s security products are largely very good, in my view — having both used them at scale at large organisations for long periods of time while being the accountable manager, to actually working on a few. Microsoft Defender for Endpoint? Great. Microsoft Defender for Identity? Great. Both have got me and my organisations out of multiple security incidents unscathed. Same with Entra ID Protection.
> 
> Have there been tangible security failings with Microsoft 365 _services_ ? Yeah.
> 
> Do I understand the customers who get frustrated about receiving malware _from_ Microsoft 365 hosted services? Hell yeah, I’m one. I also resent being sold Microsoft Defender for Endpoint… then being told to buy Microsoft Defender for Endpoint P2 addon, then Microsoft Sentinel etc to get the right logs in the right format. I get growth top right is always needed for a publicly traded business, but… uh… the upsell is real and often a turn off.
> 
> It’s particularly hard to justify nowadays as something in business you’ll really hear is ‘Microsoft should be giving us this for free, it’s our own data’ — I think the woes over the last few years have really damaged trust and the E5 upsell may be a problem for Microsoft’s sales people, frankly. 


This is a nice piece of analysis from Kevin, who echos some of the points I’ve heard before as well.  Some of the frustration with Microsoft services is the discoveries of the additional security features that are locked behind paywalls in ways that are unclear to customers at times.   The basic packages oversell the security they provide and then you find that the specific log type you needed was actually in an additional addon.  That’s super frustrating as a customer, but given the Microsoft gold partner ecosystem probably difficult to fix, but I think it’s clear that Microsoft are taking this seriously and setting out from the top what they want to achieve. 


## [Security above all else—expanding Microsoft’s Secure Future Initiative ](https://www.microsoft.com/en-us/security/blog/2024/05/03/security-above-all-else-expanding-microsofts-secure-future-initiative/)

[https://www.microsoft.com/en-us/security/blog/2024/05/03/security-above-all-else-expanding-microsofts-secure-future-initiative/](https://www.microsoft.com/en-us/security/blog/2024/05/03/security-above-all-else-expanding-microsofts-secure-future-initiative/)

> We are further expanding our goals and actions aligned to **six prioritized security pillars** and providing visibility into the details of our execution: 
> 
> 1. Protect identities and secrets
> 2. Protect tenants and isolate production systems
> 3. Protect networks
> 4. Protect engineering systems
> 5. Monitor and detect threats
> 6. Accelerate response and remediation 


I notice here that for some people, some of these will be new.  I’ve been arguing for a while now that isolating production systems from test system, isolating tenants from each other and protecting your engineering systems is at the top end of the stuff you need to be doing.

They’ve also adopted the paved path methodology, which I think I’ve refered to in the past.  That is to say that they’re going to work on ensuring that the engineering tools and platforms will make it easy to follow these core principles and hard to move off of them.  Of course there will be some situations where there’s a unique example where things need to be shared between test and production, but the paved path principle says that it should be easiest to do the right, safest and most secure thing 


## [Nation-State Threat Actors Renew Publications to npm ](https://blog.phylum.io/north-korean-state-actors/)

[https://blog.phylum.io/north-korean-state-actors/](https://blog.phylum.io/north-korean-state-actors/)

> Back in November of 2023, we [published a blog post](https://blog.phylum.io/crypto-themed-npm-packages-found-delivering-stealthy-malware/) highlighting the technical details of a sophisticated attack in `npm` attributed to North Korea. We subsequently [published a follow-up](https://blog.phylum.io/update-to-novembers-crypto-themed-npm-attack/) in January of 2024 detailing the history of the attack and highlighting the broader context of North Korean APTs operating in open-source ecosystems. Since then, it’s been relatively quiet—until today. On 23 April 2024, Phylum’s automated risk detection platform flagged a few new publications belonging to this campaign, with a slight twist. 


The twist here isn’t much of a twist, it’s just that they’ve added Apple Mac support to their trojaned packages.  But another reminder that there are bad actors playing around in the cess pool that is the state of software dependencies. 


## [We can have a different web ](https://www.citationneeded.news/we-can-have-a-different-web/)

[https://www.citationneeded.news/we-can-have-a-different-web/](https://www.citationneeded.news/we-can-have-a-different-web/)

> This is the world of today's web. Most of us spend our days within the confines of a handful of platforms, wandering around to admire what people have done with the seeds they are allowed in the space they are allotted, with platform owners directing us to the gardens they think we might like — or, more often, the ones they think will keep us within their walls for longer. Occasionally we venture outside to another plot, but sometimes we're given dire warnings before we go. After all, there could be weeds out there!
> 
> And those who cultivate those plots outside of these walls face pressures to conform to the whims of the businesses in hopes that the pathways remain open. Otherwise, they might toil away in silence, rarely seeing visitors like they one day used to.
> 
> It feels grim, and especially so for those of us who remember the days before the walls. We miss the messy but innovative landscaping, the use of space beyond the tiny squares our landlords provide us, the mostly polite strangers who wandered through and remarked on our work or shared their knowledge with us.
> 
> But we often forget: **that world is still out there** .
> 
> The walled enclosures that crowded out much of that acre of developed land still reside within an infinite expanse of possibility. There are no limits to the web — if it has borders, they are ever expanding. We may feel as though we are trapped in a tiny, crowded, noisy space, but it is only because we don't see over the walls.
> 
> If we wanted, each of us could escape those walls and set up our own spaces within the limitless, fertile soil beyond. Some of us might opt to leave those walls permanently, while others might choose to split our time between our beautiful, messy, free world outside to maintain smaller, meticulously-groomed simulacrums within the enclosures that hint — without angering our landlords — at the creations beyond. We can periodically smuggle seeds and plant cuttings beyond the walls, ensuring that if the proprietors decide to evict us, our gardens will live on.
> 
> We can develop protocols — more resilient versions of those early footpaths — that inherently resist the tollbooths and border crossing gates established by the businesses with the walls. We can even develop our own community gardens with spaces for tenants that have their own models of governance far beyond the single benevolent platform dictatorship model — that inevitably grows less benevolent as money changes hands. 


This is a lovely call to arms for an open web, and one that calls to me.  I’m one of those who has helped build some of the walls, and there are users who are better served staying within safe walled gardens, but what has always bothered me is the emphasis on preventing users wandering outside that walled garden.  Let your users make unsafe decisions, to move beyond the walled gardens, and treat them like adults who can make rational decisions 


## [LockBit leader unmasked and sanctioned ](https://nationalcrimeagency.gov.uk/news/lockbit-leader-unmasked-and-sanctioned)

[https://nationalcrimeagency.gov.uk/news/lockbit-leader-unmasked-and-sanctioned](https://nationalcrimeagency.gov.uk/news/lockbit-leader-unmasked-and-sanctioned)

> This means up to 114 affiliates paid thousands to join the LockBit programme and caused unknown levels of damage, meaning they will targeted by law enforcement, but never made any money from their criminality.
> 
> Active affiliate numbers have also significantly reduced, to 69, since February.
> 
> The NCA uncovered numerous examples of attacks where the decryptor provided by LockBit to victims who had paid ransoms failed to work, and where they received no support from affiliates or LockBit, further highlighting their untrustworthiness.
> 
> In one affiliate attack against a children’s hospital in December 2022, LockBitSupp issued an apologetic statement on their leak site and confirmed it had provided the decryptor to the victim for free.
> 
> It said the attacker had “violated our rules”, had been blocked and was no longer in their affiliate programme. In fact, they remained an active LockBit affiliate up until the February 2024 disruption, with NCA analysis showing they went on to build 127 unique attacks, engage in 50 negotiations with victims and received multiple ransom payments.
> 
> Finally, as was established by investigators, LockBit did not routinely delete stolen data once a ransom was paid. 


As if you needed the reminder, but don’t trust criminals to keep their word, they are criminals, and specifically financially motivated ones.

Paying the ransom is just handing over money and hoping they’ll do the right thing, it doesn’t really give you any real confidence that the data has actually been deleted and wont create further impact 


