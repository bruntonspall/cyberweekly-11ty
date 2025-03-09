---
title: "44 - It’s not always targeted attacks"
date: 2019-03-30
description: "Malware is running around an industrial control system. It must be Russia, or China, or Iran, or the US or ..."
permalink: /its-not-always-targeted-attacks/
---

Malware is running around an industrial control system. It must be Russia, or China, or Iran, or the US or ...

We get a million hot takes within minutes of cyber security news being broken, mostly without enough context to backup the assumptions they are making and always re-emphasising their sales pitch for fear, or uncertainty and of doubt. You are in pitched armed conflict with nation states and it’s cyber war!

But the reality of cyber security is that we are our own worst enemy over half the time, with data breaches being caused by misconfigurarion (such as logging passwords) or fat fingers where people accidentally email out personal data. 

The other attacks are the drive by attacks. A report, which I shan’t link to avoid giving it more publicity, claimed more than 86m “cyber attacks” in a year for a large government site. This can not possibly be true unless they are counting every single port scan from the internet, or anytime anything looks even slightly suspicious. 

But like the attack on Hydro, sometimes these aren’t “targeted attacks”. In the same way that if someone steals your phone from your pocket in a busy city Center, the chances that they know you personally, that they will guess your pin code is your date of birth is really quite slim. Instead many attacks are attacks of opportunity, malware where they found a victim and the identity of the victim doesn’t really matter. 

More importantly, if we raise the bar of protection against these low level, untargetted attacks, we make it harder for targeted attacks as well. We should be focusing 99% of our energy on the simple things, because while they are simple to explain (Just Patch), they’re actually very hard to do across a large and complex estate. 

## [How Lockergoga took down Hydro — ransomware used in targeted attacks aimed at big business](https://doublepulsar.com/how-lockergoga-took-down-hydro-ransomware-used-in-targeted-attacks-aimed-at-big-business-c666551f5880)

[https://doublepulsar.com/how-lockergoga-took-down-hydro-ransomware-used-in-targeted-attacks-aimed-at-big-business-c666551f5880](https://doublepulsar.com/how-lockergoga-took-down-hydro-ransomware-used-in-targeted-attacks-aimed-at-big-business-c666551f5880)

> For communication, Norsk Hydro ASA uses Office365, which was completely unimpacted —so staff could still communicate with each other, the press and customers using mobile phones and tables. Had Hydro not already moved communications to a managed cloud service, the situation would have been more grave.


This is a good writeup of the Hydro ransomware attack.
Note that using a cloud service means that the availability of your services is far higher, and they could continue key business operations during the incident and outage, even with desktops, laptops and servers not working.

I've heard of other organisations that have this ability as well, with off-estate ipads available for the incident response teams that can ensure that they can work in this case.

But if you lock down your fancy cloud service to only being accessible from your desktop systems, you are trading some availability for some level of confidentiality.  I think there are better ways to do this, from Conditional Access Policies that demand 2FA for "untrusted devices" to zero-trust networking and using inTune or device attestation to determine your risk level.

But migrate your core IT estate to a cloud provider, it's pretty much a no brainer today


## [Triton is the world’s most murderous malware, and it’s spreading - MIT Technology Review](https://www.technologyreview.com/s/613054/cybersecurity-critical-infrastructure-triton-malware/)

[https://www.technologyreview.com/s/613054/cybersecurity-critical-infrastructure-triton-malware/](https://www.technologyreview.com/s/613054/cybersecurity-critical-infrastructure-triton-malware/)

> Gutmanis recalls that dealing with the malware at the petrochemical plant, which had been restarted after the second incident, was a nerve-racking experience. “We knew that we couldn’t rely on the integrity of the safety systems,” he says. “It was about as bad as it could get.”
> 
> In attacking the plant, the hackers crossed a terrifying Rubicon. This was the first time the cybersecurity world had seen code deliberately designed to put lives at risk. Safety instrumented systems aren’t just found in petrochemical plants; they’re also the last line of defense in everything from transportation systems to water treatment facilities to nuclear power stations.


This is an interesting one.  As the article says, getting into the Safety Instrumented System is one step beyond the normal operational control systems.  For an attacker that just wants to steal data or even bring the plant to a stop, there are easier ways to do so.

The only reason to actively attempt to get into the SIS, and it's unlikely to happen by accident, is to deliberately attempt to remove safety features and put people at harm.

I believe that this is a writeup from the s4x19 conference into safety critical systems, and you can see him give the [original talk on youtube](https://www.youtube.com/watch?v=XwSJ8hloGvY)


## [5 Statements That Should Get CISOs Fired | AKF Partners](https://akfpartners.com/growth-blog/5-statements-that-should-get-cisos-fired)

[https://akfpartners.com/growth-blog/5-statements-that-should-get-cisos-fired](https://akfpartners.com/growth-blog/5-statements-that-should-get-cisos-fired)

> I’m fed up with the ridiculous way that most CISOs approach security, and you should be too.  The typical approach, in more than 80% of the companies with which we work, results in slow time to market, increased response time for transactions, higher than necessary cost, lower than appropriate availability, and no demonstrable difference in the level of security related incidents.  Put another way, most CISOs reduce rather than increase shareholder value.
> 
> [...]
> 
> Security isn’t a “team” in and of itself because it can’t “score” and “win”.  Security is part of a larger team responsible for delighting end customers such that we can ensure appropriate profitability through superior and appropriately secure offerings.  


Strong words but I agree with everything in here. Marty sums up my problem with overly myopic security folk, that they see their role as saying no rather than increasing shareholder value. 

Of all the things he hilights, the “we are here to work the process” is the worst of the thinking in security. As a model of security, being “part of a team responsible for delighting customers” is a great motto for the team to have. 

As I always say, security is an enabler, and it’s job is to say yes. 


## [Facial recognition's 'dirty little secret': Millions of online photos scraped without consent](https://www.nbcnews.com/tech/internet/facial-recognition-s-dirty-little-secret-millions-online-photos-scraped-n981921)

[https://www.nbcnews.com/tech/internet/facial-recognition-s-dirty-little-secret-millions-online-photos-scraped-n981921](https://www.nbcnews.com/tech/internet/facial-recognition-s-dirty-little-secret-millions-online-photos-scraped-n981921)

> “People gave their consent to sharing their photos in a different internet ecosystem,” said Meredith Whittaker, co-director of the AI Now Institute, which studies the social implications of artificial intelligence. “Now they are being unwillingly or unknowingly cast in the training of systems that could potentially be used in oppressive ways against their communities.”


An interesting twist on the old open licensing conundrum.  You take a photo and give it a creative commons share alike license.
You intend that anyone can take and use the photo in the ways that you imagine, but does that mean that someone can use your photo in a negative advertising campaign? Could they use it to feed their AI machine?

The license says yes, but people's guts have a tendency to say no.

The question here is whether that's ethical of the companies building these large data sets?  The photos are freely available and licensed for use, so it's hard to say that it's unethical, but it's not what was intended.


## [Endlessh: an SSH Tarpit « null program](https://nullprogram.com/blog/2019/03/22/)

[https://nullprogram.com/blog/2019/03/22/](https://nullprogram.com/blog/2019/03/22/)

> This program opens a socket and pretends to be an SSH server. However, it actually just ties up SSH clients with false promises indefinitely — or at least until the client eventually gives up


This is a cute little tool to run on the outside of your network. It doesn’t do anything except distract simple attackers and tie up resources. 

The author explains the code as well, so you could tweak this to send security events if you ran it inside your network. 


## [Troy Hunt: These Cookie Warning Shenanigans Have Got to Stop](https://www.troyhunt.com/these-cookie-warning-shenanigans-have-got-to-stop/)

[https://www.troyhunt.com/these-cookie-warning-shenanigans-have-got-to-stop/](https://www.troyhunt.com/these-cookie-warning-shenanigans-have-got-to-stop/)

> So in summary, everyone clicks through cookie warnings anyway, if you read them you either can't understand what they're saying or the configuration of privacy settings is a nightmare, depending on where you are in the world you either don't get privacy or you don't get UX hell, if you understand the privacy risks then it's easy to open links incognito or use an ad blocker, you can still be tracked anyway and finally, the whole thing is just conditioning people to make bad security choices.


I disagree with some of this, but I do agree that cookie warnings just don't seem to be achieving the intended outcome.
I have had a number of conversations with digital services, explaining the concept of consent vs contract, and what they can do with people's personal data they submit, so it's increasing awareness that privacy is a thing.  

But it does train users into simply clicking accept, which cannot by definition be "informed consent", and trains users to just click yes on warnings that pop up on websites.


## [Where are the EU’s ePrivacy reforms? And where does Brexit leave them for the UK?, Charlie Ainsworth](https://digital.freshfields.com/post/102f6il/where-are-the-eus-eprivacy-reforms-and-where-does-brexit-leave-them-for-the-uk)

[https://digital.freshfields.com/post/102f6il/where-are-the-eus-eprivacy-reforms-and-where-does-brexit-leave-them-for-the-uk](https://digital.freshfields.com/post/102f6il/where-are-the-eus-eprivacy-reforms-and-where-does-brexit-leave-them-for-the-uk)

> The Commission had hoped to bring the new Regulation into effect at the same time as the GDPR in May this year. But the proposal has been hugely controversial, both within the EU’s various institutions and across a range of industry sectors. The divisions in approach have contributed to significant delays.
> 
> The most contentious provisions have been in relation to when providers of voice, email, video and other messaging services will be permitted to use the content and metadata of communications on their services


This was supposed to be a european cookie review that would make it clearer that implied consent was acceptable for certain types of cookies, local analytics essentially, which would mean that if you used cookies purely for functionality on your site, or to track your users locally, then you wouldn't need a cookie banner, but if you used advertisers cookies (like the Oath family do), then you'd have a cookie banner.  That would incentivise people to not use wider ad tracking networks.  Sadly the updated privacy directive seems to have gotten severely delayed in EU bureaucracy so we'll have to wait for that


## [Facebook Stored Hundreds of Millions of User Passwords in Plain Text for Years](https://krebsonsecurity.com/2019/03/facebook-stored-hundreds-of-millions-of-user-passwords-in-plain-text-for-years/)

[https://krebsonsecurity.com/2019/03/facebook-stored-hundreds-of-millions-of-user-passwords-in-plain-text-for-years/](https://krebsonsecurity.com/2019/03/facebook-stored-hundreds-of-millions-of-user-passwords-in-plain-text-for-years/)

> “We’ve not found any cases so far in our investigations where someone was looking intentionally for passwords, nor have we found signs of misuse of this data,” Renfro said. “In this situation what we’ve found is these passwords were inadvertently logged but that there was no actual risk that’s come from this. We want to make sure we’re reserving those steps and only force a password change in cases where there’s definitely been signs of abuse.”


Another instance where passwords were logged as part of the structured logging.  If you are a building an observable system, using structured logging and sensible ways to capture data points, this will happen.
What's interesting here is that Facebook are looking at who queried these data sets and what they were querying for to determine if that passwords were ever actually at risk.  That's something you can only do if your logs are stored in a structured data store, with access controls.

I'm inclined to say that this isn't a breach, your password is always transmitted from the browser on your machine to the webserver in the clear, and the fact that this data is logged somewhere doesn't make it breached.  We hash passwords to prevent someone who is unauthorised from accessing them, but given good protections around this data, I'm not sure that calling foul is the right thing to do


## [Remote command injection through an endpoint security product | Pen Test Partners](https://www.pentestpartners.com/security-blog/remote-command-injection-through-an-endpoint-security-product/)

[https://www.pentestpartners.com/security-blog/remote-command-injection-through-an-endpoint-security-product/](https://www.pentestpartners.com/security-blog/remote-command-injection-through-an-endpoint-security-product/)

> Ten minutes later, I have an evaluation copy of Heimdal Thor running inside of a virtual machine, and I’m seeing the same behaviour – I can intercept HTTPS communication without being noticed.
> 
> Heimdal Thor also does automated software updates. I could see JSON lists of software being downloaded, containing a URL, version etc.. And in those lists, parameters called “beforeInstallScript” and “afterInstallScript”.


This is a nasty stupid bug. You need endpoint security tools to be good because they run on your machine with privileges. 

I’m shocked that not validating the certificate for command transmission and encryption with a static key got through any reasonable penetration test 


## [Beto O’Rourke and legendary hacker group Cult of the Dead Cow explained - Vox](https://www.vox.com/policy-and-politics/2019/3/15/18267468/beto-orourke-2020-cult-of-the-dead-cow-psychedelic-warlord)

[https://www.vox.com/policy-and-politics/2019/3/15/18267468/beto-orourke-2020-cult-of-the-dead-cow-psychedelic-warlord](https://www.vox.com/policy-and-politics/2019/3/15/18267468/beto-orourke-2020-cult-of-the-dead-cow-psychedelic-warlord)

> He doesn’t appear to have been deeply involved or to have participated in any of the group’s better-known stunts. But there is something fitting about O’Rourke’s membership in a group that was known for its communications savvy — “a flair for spectacle” as one expert put it — more than its technical proficiency.
> 
> “CDC wasn’t pumping out tech. It was really about trying to get the word out there that hackers could do good in the world,” Gabriella Coleman, a McGill University professor who has written about hacker anthropology and culture, told me. “CDC had cultural cache. They were like the punk rock band of the hacker world.”


cDc is a name from my childhood. By the time I started reading hacker boards and magazines, like Phrack and 2600, it was the mid 90s and cDc predated that by a decade or so. 

The timing on the release of this story is interesting, it’s curiois whether it’s an attempt to seem relevant or whether it’s a journalist who knows they will be scooped on something they’ve known for a while and releasing it before someone else gets there. 

In 20-30 years time, the equivalent of this will be being a Redditor I’m sure. 


