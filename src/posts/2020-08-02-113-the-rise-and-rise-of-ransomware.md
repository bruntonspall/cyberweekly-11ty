---
title: "113 - The rise and rise of ransomware"
date: 2020-08-02
description: "Ransomware is on the rise, affecting more and more companies, and it's always spoken off as if it's highly advanced hacking, the sort that you might expect to be restricted to say 17 year olds."
permalink: /the-rise-and-rise-of-ransomware/
---

Ransomware is on the rise, affecting more and more companies, and it's always spoken off as if it's highly advanced hacking, the sort that you might expect to be restricted to say 17 year olds.

In reality ransomware is a pretty low bar for hacking attempts.  In order to successfully carry out ransomware you need 3 main things:

1. The ransomware itself, an encryptor that encrypts the files and provides a decryption path
2. The dropper, some malware that can execute on a machine, elevate it's privileges and then drop the ransomware
3. A vulnerability that can get the dropper onto a machine

It used to be that ransomware and droppers were advanced stuff, but the rise of ransomware as a service means that enterprising developers with at least moderate amounts of skill can make a pretty penny just by building and selling the ransomware and the droppers themselves.  Given the availability of commercial pen testing and red team frameworks that include most of the hard work in this, the bar in this area just keeps getting lowered.

The third one sounds much harder than it actually is.  Given the patch cycles and capabilities of most organisations, you can simply scan, using freely available tools, and find hosts and systems that you want to affect, and you'll get a hit rate.  The more advanced attackers can use more up to date vulnerabilities, can watch exploit-db or exploitation frameworks and scan faster and better, but in reality, there's just so much of the internet to scan, there's plenty of room for all the adversaries out there.

That means that the capability level of ransomware attackers is mostly unknown when you get hit.  You don't know if they simply followed a script, and don't know what they are doing, or if they had access and the ability to do far more nefarious things on your network. 

This brings us round to the point around whether paying for ransoms is a good idea.  

Personally, I tend to be opposed to the idea of paying ransoms. 

There are situations where paying the ransom to get your system back up and running is quicker, cheaper and better than rebuilding.  If it's a choice between paying the ransom and going bankrupt, you may not feel like you have much choice.

But in other situations, I don't see how once you've paid the ransom, how you can possibly ever trust the IT system again.  The attackers had to have access to the systems in order to encrypt them, and you don't know what changes they made, you don't know how many little back doors and helpers they left themselves.  They may have copied your data, or sold access to your systems to other criminals, or even just told their hacker friends!  Even if you get your system back up and running, you should assume that they know your network layout, they know all your passwords, and they can get back in.  If you rebuild from scratch in that case, which is the only way I can see you trusting it again, I don't see what paying the ransom really gave you.

## [Emotet being hijacked by another actor | by Kevin Beaumont | Jul, 2020 | DoublePulsar](https://doublepulsar.com/emotet-being-hijacked-by-another-actor-b22414352a7b)

[https://doublepulsar.com/emotet-being-hijacked-by-another-actor-b22414352a7b](https://doublepulsar.com/emotet-being-hijacked-by-another-actor-b22414352a7b)

> Emotet returned last week, sending millions of emails. This week, somebody has started replacing the Emotet distribution files with animated GIFs.
> 
> From tracking, the replacements generally happen within a few minutes of Emotet updating their botnet. Around a quarter of all malware is getting replaced. This suggests a few possibilities:
> 
> * Emotet themselves are doing this.
> * Other threat actors are doing this to sabotage Emotet.
> * Security researchers are doing it.
> 
> Either way, Emotet’s effectiveness is being directly impacted at present in an apparently automated fashion (either that or somebody is very, very bored).


This has sadly been fixed by the actor behind Emotet.

I'm fascinated that someone had access to their systems and started replacing the payloads with GIF's.  That strongly implies it wasn't another threat actor, you'd expect them to replace the payload with their own dropper, gaining control of the victim for their own use instead.  (I also doubt that it was some form of state takedown, after all who has met a government employee who knows what an animated GIF is, and can you imagine the paperwork to replace payloads with animated GIFs!)

Intriguing.


## [Secrets, Lies, and Account Recovery: Lessons from the Use of Personal Knowledge Questions at Google [pdf]](https://static.googleusercontent.com/media/research.google.com/en/us/pubs/archive/43783.pdf)

[https://static.googleusercontent.com/media/research.google.com/en/us/pubs/archive/43783.pdf](https://static.googleusercontent.com/media/research.google.com/en/us/pubs/archive/43783.pdf)

> Our analysis confirms that secret questions generally offer
> a security level that is far lower than user-chosen passwords. It turns
> out to be even lower than proxies such as the real distribution of surnames in the population would indicate. Surprisingly, we found that
> a significant cause of this insecurity is that users often don’t answer
> truthfully. A user survey we conducted revealed that a significant
> fraction of users (37%) who admitted to providing fake answers
> did so in an attempt to make them "harder to guess" although on
> aggregate this behavior had the opposite effect as people "harden"
> their answers in a predictable way.
> On the usability side, we show that secret answers have surprisingly poor memorability despite the assumption that reliability
> motivates their continued deployment. From millions of account recovery attempts we observed a significant fraction of users (e.g 40%
> of our English-speaking US users) were unable to recall their answers when needed. This is lower than the success rate of alternative
> recovery mechanisms such as SMS reset codes (over 80%).
> Comparing question strength and memorability reveals that the
> questions that are potentially the most secure (e.g what is your first
> phone number) are also the ones with the worst memorability. We
> conclude that it appears next to impossible to find secret questions
> that are both secure and memorable. Secret questions continue have
> some use when combined with other signals, but they should not be
> used alone and best practice should favor more reliable alternatives


In case you didn't know, personal knowledge based authentication doesn't really work.  I think many of us have always known this, but it's nice to see statistics.

Questions that are memorable are ones that aren't secure and can easily be guessed or determined, so mothers maiden name, favourite food etc are trivially guessable within a small number of attempts and some knowledge of you.  Answers that are far more secure are the least usable, and users often forget them.

The most interesting features in here is that users who deliberately lie on the question to improve security often instead pick common answers that make their accounts more susceptible to brute force.  

Security questions basically end up being a high risk mechanisms that you can use when you have reasonable confidence that an account isn't being hijacked, but as an actual protection mechanism, you should use a different form of second factor, such as SMS or email based recovery.


## ['Ghostwriter' Influence Campaign: Unknown Actors Leverage Website Compromises and Fabricated Content to Push Narratives Aligned With Russian Security Interests | FireEye Inc](https://www.fireeye.com/blog/threat-research/2020/07/ghostwriter-influence-campaign.html)

[https://www.fireeye.com/blog/threat-research/2020/07/ghostwriter-influence-campaign.html](https://www.fireeye.com/blog/threat-research/2020/07/ghostwriter-influence-campaign.html)

> We have dubbed this campaign “Ghostwriter.”
> 
> Many, though not all of the incidents we suspect to be part of the Ghostwriter campaign, appear to have leveraged website compromises or spoofed email accounts to disseminate fabricated content, including falsified news articles, quotes, correspondence and other documents designed to appear as coming from military officials and political figures in the target countries.
> 
> This falsified content has been referenced as source material in articles and op-eds authored by at least 14 inauthentic personas posing as locals, journalists and analysts within those countries. These articles and op-eds, primarily written in English, have been consistently published to a core set of third-party websites that appear to accept user-submitted content


Create false narratives, and then use compromised websites to amplify the message, either directly through cyber means, or indirectly through the use of false personas.

Increasingly, the news and media is becoming something you cannot trust.  The diversification that the internet bought, which was useful in allowing smaller voices to be heard has created a cacophony of voices in which its difficult to pick out the accurate amongst the adverts, clickbait and carefully coordinating misinformation and disinformation campaigns.


## [Errata Security: How CEOs think](https://blog.erratasec.com/2020/07/how-ceos-think.html)

[https://blog.erratasec.com/2020/07/how-ceos-think.html](https://blog.erratasec.com/2020/07/how-ceos-think.html)

> The only thing more broken than how CEOs view cybersecurity is how cybersecurity experts view cybersecurity. We have this flawed view that cybersecurity is a moral imperative, that it's an aim by itself. We are convinced that people are wrong for not taking security seriously. This isn't true. Security isn't a moral issue but simple cost vs. benefits, risk vs. rewards. Taking risks is more often the correct answer rather than having more security.
> 
> Rather than experts dispensing unbiased advice, we've become advocates/activists, trying to convince people that they need to do more to secure things. This activism has destroyed our credibility in the boardroom. Nobody thinks we are honest.
> 
> [...]
> 
> All this is a tradeoff. A focus of attention on one part of the business means less attention on other parts of the business. If your company excels at cybersecurity, it means not excelling at some other part of the business.
> 
> So unless you are a company like Google, whose cybersecurity is a competitive advantage, you don't want to excel in cybersecurity. You want to be average, or at most, slightly above average. You want to do what your peers are doing.


I want to quote pretty much all of this article.  I disagree with just how badly many CEO's are painted here, in that I think many executive leaders recognise that they should be better at security, that they want to be better, but that they can't work out how to be better.

Cybersecurity as an industry continues to sell lies to executives, that you just need to do the basics, that AV will protect you from ransomware, and that cyber insurance will save their business when it gets ransomwared back to the stoneage.

We need to be better at explaining what we want, and most importantly, how we can not just fight the current fire, but how by modifying the business processes, prevent the next fire and ideally make people more efficient and effective at the same time.

Move to Office 365, migrate to cloud and say yes to more stuff rather than arguing with the business and saying no to everything.  Make security someone valuable in the organisation who helps people get stuff done.


## [Are Account Takeovers Driving Towards a Passwordless Future?](https://blog.knowbe4.com/are-account-takeovers-driving-towards-a-passwordless-future)

[https://blog.knowbe4.com/are-account-takeovers-driving-towards-a-passwordless-future](https://blog.knowbe4.com/are-account-takeovers-driving-towards-a-passwordless-future)

> Personally, I'm a big fan of MFA. It's one of the best methods to greatly reduce overall risk. It reduces the need for the user to choose unique passwords, or even necessarily strong ones. That’s because if an attacker had the ID and password, they don't have the second (or third) factors needed to get into the account.
> 
> But is MFA enough? And this is where we get into the "your threat model is not my threat model" type of scenario, which is a technical way of saying, "let's agree to disagree.”
> 
> MFA isn't a panacea. There are many ways to bypass MFA. My colleague Roger Grimes has written extensively on the various different ways MFA can be bypassed. (Friendly plug, his book "Hacking Multifactor Authentication" is out later this year.)
> 
> Any security expert will tell you that nothing is perfect, which is why even with everything in place, you still need to monitor for intrusion attempts, or look for anomalous activity. 
> 
> Having said that, for most organisations, educating your users along with implementing some basic protections will usually bring the risk of account takeover to an acceptable limit, as illustrated in the diagram below. 


This is a good overview of password takeovers, and worth clicking through if just for the diagrams in here.

I think there's a coming future where the tools we consider MFA now, such as YubiKey, TOTP, Mobile phone push, SMS codes etc as the primary authentication mode, and we ask for a password as a second factor.  For many users this is just as a secure as any other single factor, but for the systems is likely more secure.  

Of course the problem then will lie in whether you can remember your password on the odd occasion that you need it!


## [Grubbing Secure Boot the Wrong Way: CVE-2020-10713 • Capsule8](https://capsule8.com/blog/grubbing-secure-boot-the-wrong-way-cve-2020-10713/)

[https://capsule8.com/blog/grubbing-secure-boot-the-wrong-way-cve-2020-10713/](https://capsule8.com/blog/grubbing-secure-boot-the-wrong-way-cve-2020-10713/)

> Okay, but: Exploiting this vulnerability requires root / admin access to access the grub.cfg file located in the EFI System Partition, which means the attacker must first gain a foothold on the system and escalate privileges (physical access also works). The vuln only helps with persistence across system reboots, so it’s unnecessary — and perilously noisy — for attackers to employ this if they already have root on a system that never reboots. It’s also preposterously unlikely that any attacker will spontaneously write on-the-fly real mode shellcode that will perform boot injection and OS loading. If they do, they probably deserve the win. 
> 
> And yet: This will become incredibly bad news if enterprising criminals incorporate this vulnerability into their nefarious bots as part of the standard “be hacker, do crimes” pipeline of bootkit creation -> licensing the bootkit to a bot author -> deploying or selling the bootkit-armed bots (like in a botnet). This pipeline will not pop out pwnage overnight, so the question becomes whether mitigations can be successfully rolled out before criminals can scale this attack.


Lots nasty in this bug, from the ability to gain complete control of the machine, to the fact that patching this one is really really hard...  Apply the denylist patch too early and your machine is hosed and won't boot.  Don't get that wrong!

The only good news is that this is very much an advanced attack that is only necessary should your system be already compromised.  Any attempt to use this hack to gain more control than intended requires rebooting the machine, and that is the sort of thing that you'd kind of hope that people might notice.

Of course, if you live in a cloud world, you probably don't have Grub or UEFI to worry about because you are just running VMs in someone else's machine, so this very much becomes "someone else's problem"


## [Three Individuals Charged For Alleged Roles In Twitter Hack | USAO-NDCA | Department of Justice](https://www.justice.gov/usao-ndca/pr/three-individuals-charged-alleged-roles-twitter-hack)

[https://www.justice.gov/usao-ndca/pr/three-individuals-charged-alleged-roles-twitter-hack](https://www.justice.gov/usao-ndca/pr/three-individuals-charged-alleged-roles-twitter-hack)

> SAN FRANCISCO– Three individuals have been charged today for their alleged roles in the Twitter hack that occurred on July 15, 2020.
> 
> Mason Sheppard, aka “Chaewon,” 19, of Bognor Regis, in the United Kingdom, was charged in a criminal complaint in the Northern District of California with conspiracy to commit wire fraud, conspiracy to commit money laundering, and the intentional access of a protected computer.
> 
> Nima Fazeli, aka “Rolex,” 22, of Orlando, Florida, was charged in a criminal complaint in the Northern District of California with aiding and abetting the intentional access of a protected computer.
> 
> The third defendant is a juvenile.
> 
> [...]
> 
> “There is a false belief within the criminal hacker community that attacks like the Twitter hack can be perpetrated anonymously and without consequence,” said U.S. Attorney David L. Anderson for the Northern District of California.  “Today’s charging announcement demonstrates that the elation of nefarious hacking into a secure environment for fun or profit will be short-lived.  Criminal conduct over the Internet may feel stealthy to the people who perpetrate it, but there is nothing stealthy about it.  In particular, I want to say to would-be offenders, break the law, and we will find you.”
> 
> “The hackers allegedly compromised over 100 social media accounts and scammed both the account users and others who sent money based on their fraudulent solicitations,”


Yup, clearly advanced state level hackers ... or you know, a 19 year old from Bognor Regis, a 22 year old and a reported 17 year old.

I don't know whether to laugh or cry.  It's a reminder that many of us are sitting on a house of cards, and the criminal masterminds that we worry about, running botnets, deploying DDoS and running ransomware networks are likely children and people in their early 20's.


## [An update on our security incident](https://blog.twitter.com/en_us/topics/company/2020/an-update-on-our-security-incident.html)

[https://blog.twitter.com/en_us/topics/company/2020/an-update-on-our-security-incident.html](https://blog.twitter.com/en_us/topics/company/2020/an-update-on-our-security-incident.html)

> The social engineering that occurred on July 15, 2020, targeted a small number of employees through a phone spear phishing attack. A successful attack required the attackers to obtain access to both our internal network as well as  specific employee credentials that granted them access to our internal support tools. Not all of the employees that were initially targeted had permissions to use account management tools, but the attackers used their credentials to access our internal systems and gain information about our processes. This knowledge then enabled them to target additional employees who did have access to our account support tools. Using the credentials of employees with access to these tools, the attackers targeted 130 Twitter accounts, ultimately Tweeting from 45, accessing the DM inbox of 36, and downloading the Twitter Data of 7. 


The big twitter hack was it turned out, phishing on some twitter support staff.  Someone clicked, and that probably gave the attacker the ability to access their email.

From there, they almost certainly read email archives and determined who tickets would be escalated to when they needed intervention through the tools, and then targeted those second level support engineers.  Whether they did so from the first victims account or direct from the internet, who knows.

It sounds like Twitter had a VPN that was username/password based, or that the VPN credentials could be lifted from one of the compromised users.  At a guess, this is a simple credential theft attack.  Once they had the credentials, they could get on the network, access their email (twitter uses Google Suite from memory), slack etc, and could read all of the internals.

Clear this must have been a highly advanced and capable state actor...


## [Garmin staggers back online after ransomware attack • Graham Cluley](https://grahamcluley.com/garmin-staggers-back-online-after-ransomware-attack/)

[https://grahamcluley.com/garmin-staggers-back-online-after-ransomware-attack/](https://grahamcluley.com/garmin-staggers-back-online-after-ransomware-attack/)

> Well, I suspect there might be a good reason that Garmin is so wary of using the word “ransomware,” and it might be because the first question any tech journalist is likely to ask is, “so did you pay the ransom or not?”
> 
> 
> And that’s a question that at the moment Garmin doesn’t seem to be racing to answer. Rumours have spread online that the company’s hackers might have demanded as much as $10 million for the decryption key to recover their data.
> 
> Whether Garmin is recovering its data due to a payment to the criminals behind the attack (suspected of being the Evil Corp gang) or through good old-fashioned secure backups is also not clear from Garmin’s statement.


All the signs point to Garmin having been the subject of a pretty major ransomware attack.  They had an almost total outage, covering support, manufacturing and all of their cloud services.

If that means that attackers had access to the data, then that will be worrying a lot of people.  The data around the mapping of locations in things like Strava and Garmin has had numerous incidents over the last few years.  After the Strava and Untappd open source research articles, I'm sure that most military and intelligence places made the effort to tell their staff to ensure that their profiles were set to private, so that they couldn't be found by people accessing the data externally.  But a criminal organisation, especially one like Evil Corp that has been linked closely to Russia, having access to all that location data is distinctly worrying


## [Security Incident | Blackbaud](https://www.blackbaud.com/securityincident)

[https://www.blackbaud.com/securityincident](https://www.blackbaud.com/securityincident)

> In May of 2020, we discovered and stopped a ransomware attack. In a ransomware attack, cybercriminals attempt to disrupt the business by locking companies out of their own data and servers. After discovering the attack, our Cyber Security team—together with independent forensics experts and law enforcement—successfully prevented the cybercriminal from blocking our system access and fully encrypting files; and ultimately expelled them from our system. Prior to our locking the cybercriminal out, the cybercriminal removed a copy of a subset of data from our self-hosted environment. The cybercriminal did not access credit card information, bank account information, or social security numbers. Because protecting our customers’ data is our top priority, we paid the cybercriminal’s demand with confirmation that the copy they removed had been destroyed. Based on the nature of the incident, our research, and third party (including law enforcement) investigation, we have no reason to believe that any data went beyond the cybercriminal, was or will be misused; or will be disseminated or otherwise made available publicly.


The blackbaud ransomware has been [a bit](https://www.bbc.co.uk/news/technology-53528329) of [a thing]((https://www.bbc.co.uk/news/technology-53567699)), for two main reasons, and I don't normally share what I consider to be "bad articles" here, but this statement by them is pretty shocking.

The first is just how bad this statement is, not just the normal bingo of "We take security seriously" and "advanced hackers",  it claims that they prevented the ransomware attack, whereas in fact they wer successfully breached.  They also paid the ransom, which less arguably bad, because there are times where paying the ransom is the right thing to do.

But the clincher here is that they claim that the attackers exfiltrated a large dataset out of their "self-hosted environment", and that they paid the ransom only for proof that the data had been destroyed.  

It is of course logically impossible to prove that digital information or data has been destroyed without any copies being made.  

Finally, as a nail in this coffin, the breach reportedly happened in May, and the BBC reports that at the end of July the ICO was only informed around July 18th at best.  Multiple clients were depending on this provider to maintain their systems in a safe and secure manner.  They are a company that claims on their security page to be in "Active participation in CyberSecurity thought leadership", and loftily announces that all staff participate in regular phishing tests, they have a red team, and they have more or less every certificate in existence.

Of course, they blame the hyper advanced hackers who have targeted them in this case, and talk about the ever changing threat landscape.  I suspect that this will probably turn out to be fairly dull and uninteresting ransomware for which there were public indicators of compromise available at the time of compromise.


