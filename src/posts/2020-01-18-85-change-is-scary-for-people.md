---
title: "85 - Change is scary for people"
date: 2020-01-18
description: "\"Security is important, you must patch now\"."
permalink: /change-is-scary-for-people/
---

"Security is important, you must patch now".

We say this an awful lot in security.  I say this a lot!  Patching is probably the number 1 security control that you can apply.  Almost all cyber attacks from outside exploit known vulnerabilities that could have been patched and 0-day attacks are still quite rare.  If you can only do one thing, patching those critical security bugs is it.

But I've talked before about the technical complexity of patching your systems, of coordinating those change programs and getting everything tested and rolled out.  It isn't easy to actually carry out.  It's simple, but not easy.  But I've never really talked about the psychological impact of change and the inertia against change that we have in our lives.

People get into routines in life.  I like to know that I get a cup of coffee in the morning, and I tend to sit in the same place on the same train most days.  Change is psychologically difficult for us as humans.  When things are similar or the same, we don't have to exert as much brainpower to assess the environment, ensure it is safe, and determine how to complete whatever actions we are trying to do.  But when things change, we get a spike of anxiety, our brain goes into alert and we need to reassess our environment to be sure that it is safe.

The same is true of our working environments.  One of the biggest issues that agile software delivery teams have to face is that their users often don't like it when things on the website or service they use moves around too much.  Any given change initiative will have people who dislike it respond straight away.  When I worked at the Guardian on the new CMS, everytime we launched a new section, we would be [inundated with comments from people who hated the new design](https://www.theguardian.com/help/insideguardian/2014/dec/09/-sp-a-new-look-for-sport). "I prefered the old design, I knew where to go to get my [crossword/football results/contributor I like]".

When we introduce change, such as bringing in DevOps to a team that doesn't work that way, or defining new security policies, or using agile, we often have to consider how to introduce that change.  It's counter-productive to turn up and just yell at people that they are dinosaurs who "don't understand the modern way of working" if they don't like it.  Good agile coaches and transformation experts understand this.  They talk about taking people on a journey, and building bridges to reach out to people.  As is linked below, when we talk about DevOps, it's vital to still recognise the value of what comes before.  If we can couch our concepts with the same language that was used before, then we are minimising that change that people need to adjust to.

But what about security patches and updates?  How does that apply?  When it comes to deploying patches and updates, we need to make sure that our customers are incentivised to apply them.  Will it make changes to our system?  Will it mean retraining our staff?  What could go wrong?  When we are talking about minor changes, we tend to think this doesn't matter.  And it's true, the upgrade from Windows 7 to Windows 10 is a much bigger change for people to adopt than fixing their Citrix VPN.  But people get burnt by big changes and become afraid of applying the little changes as well.

We need to remember that just telling people to patch, to adopt a new security approach, to do agile, we are deliberately putting people into an uncomfortable headspace.  We need to provide people reassurance about what that means, provide them contextual clues to help them orient themselves, and we need to have empathy for the stress that we put them under.

## [Enforcing Against Manipulated Media - About Facebook](https://about.fb.com/news/2020/01/enforcing-against-manipulated-media/)

[https://about.fb.com/news/2020/01/enforcing-against-manipulated-media/](https://about.fb.com/news/2020/01/enforcing-against-manipulated-media/)

> As a result of these partnerships and discussions, we are strengthening our policy toward misleading manipulated videos that have been identified as deepfakes. Going forward, we will remove misleading manipulated media if it meets the following criteria:
> 
> It has been edited or synthesized – beyond adjustments for clarity or quality – in ways that aren’t apparent to an average person and would likely mislead someone into thinking that a subject of the video said words that they did not actually say. And:
> It is the product of artificial intelligence or machine learning that merges, replaces or superimposes content onto a video, making it appear to be authentic.


I have to say, I'm puzzled about the AND here.   If I deliberately synthasize or edit a film so that people are misled into thinking that the subject said things they didn't say, but I don't use AI to do it, I do it by hand, then it's ok and will continue to be hosted (although reading further down, *may* still be fact-checked and carry a false news warning, but not will, just may).

> If we simply removed all manipulated videos flagged by fact-checkers as false, the videos would still be available elsewhere on the internet or social media ecosystem.

This justification feels weird too.  This I suspect is more about being afraid of losing market share to their competitors than a real justification for why they won't take down known false informational videos.

But it's a step at least.


## [Studying an Incident - Subbu’s Blog](https://m.subbu.org/studying-an-incident-8dffdd641c78)

[https://m.subbu.org/studying-an-incident-8dffdd641c78](https://m.subbu.org/studying-an-incident-8dffdd641c78)

> This incident involved opening up minds to alternative explanations, conducting parallel streams of analyses, adapting to new information as it emerged, and attempting things not done before. Each major component involved in this incident behaved as it was supposed to. Regardless, the system as a whole faced a catastrophe, and it took human coordination, quick thinking, and ingenuity to recover from the disaster. In fact, what is typical between incidents is how people come together to restore the system, with the rest being unique to each incident.


This was an interesting writeup of an otherwise routine incident.  I liked how Subbu was clear that there was no single root cause of the incident here, and that in fact everything did what it was supposed to, just in a way that cause the system to fail.


## [Google Online Security Blog: PHA Family Highlights: Bread (and Friends)](https://security.googleblog.com/2020/01/pha-family-highlights-bread-and-friends.html)

[https://security.googleblog.com/2020/01/pha-family-highlights-bread-and-friends.html](https://security.googleblog.com/2020/01/pha-family-highlights-bread-and-friends.html)

> Sheer volume appears to be the preferred approach for Bread developers. At different times, we have seen three or more active variants using different approaches or targeting different carriers. Within each variant, the malicious code present in each sample may look nearly identical with only one evasion technique changed. Sample 1 may use AES-encrypted strings with reflection, while Sample 2 (submitted on the same day) will use the same code but with plaintext strings.
> At peak times of activity, we have seen up to 23 different apps from this family submitted to Play in one day. At other times, Bread appears to abandon hope of making a variant successful and we see a gap of a week or longer before the next variant. This family showcases the amount of resources that malware authors now have to expend. Google Play Protect is constantly updating detection engines and warning users of malicious apps installed on their device.


Dodgy apps submitted to online app stores will always be a problem.  Creating bad quality mobile apps is easy, can be done in sweatshops, and with the right instagram and facebook videos and ads can get thousands of downloads quickly.

Many of these are just simply attempts to get lots of advertising views and monotise that way, but of course, where you can get an application onto a device, you can also put "malware", or software that does unexpected things. Sending texts to high cost numbers or subscribing to expensive services.

This is a form of fraud that generally affects a massively wide, and generally poorer population than typical CEO fraud or many phishing frauds. 


## [Australia’s water crisis, intelligence and national security](https://www.iiss.org/blogs/analysis/2020/01/australia-water-crisis-intelligence-national-security)

[https://www.iiss.org/blogs/analysis/2020/01/australia-water-crisis-intelligence-national-security](https://www.iiss.org/blogs/analysis/2020/01/australia-water-crisis-intelligence-national-security)

> The second cause is a disconnect between the character of the water crisis as a national-security issue and the political structures to handle it.
> 
> Australia maps its fires very well and has useful predictive capabilities for fire progress and risk. But it lacks a highly developed civil defence mindset at the national level, meaning that the country has not joined up the dots between knowing where fires will occur and how they might behave, and aligning distribution and management of water resources accordingly.


This was interesting to me as a reminder that national security isn't just about cyber criminals and hostile states.  It's also about ensuring that nationally we can respond to issues that affect the security of all our citizens, including fire, flood, natural disasters, and for those who have watched the new Sky One TV Show Cobra, yes ["Space weather" is a national security concern](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/449593/BIS-15-457-space-weather-preparedness-strategy.pdf).


## [WeLeakInfo.com Seized For Selling Info from Data Breaches, 2 Arrested](https://www.bleepingcomputer.com/news/security/weleakinfocom-seized-for-selling-info-from-data-breaches-2-arrested/)

[https://www.bleepingcomputer.com/news/security/weleakinfocom-seized-for-selling-info-from-data-breaches-2-arrested/](https://www.bleepingcomputer.com/news/security/weleakinfocom-seized-for-selling-info-from-data-breaches-2-arrested/)

> To access this data, visitors could subscribe to various plans ranging from a $2 trial to a $70 three-month unlimited access account. These plans would then allow a user to perform searches that retrieve information exposed in these data breaches.
> 
> The actual disclosure of the stolen data compared to just allowing users to be notified if their info was exposed is a clear distinction between how We Leak Info and a service like HaveIBeenPwned utilize data breaches.
> 
> In We Leak Info's case, threat actors commonly subscribed to search for exposed usernames and passwords and then used that info to perform credential stuffing attacks, phishing attacks, and potentially network breaches. 
> 
> On the other hand, HaveIBeenPwned will just tell you if an entered email is part of a data breach, but does not provide any other information.


This was an interesting takedown.  Obviously news is a bit thin on the ground, but two operators of a "major organised crime gang" who had data from over 10,000 breaches in a database and sold access to it.

It was hard at first, as someone who hadn't used weleakinfo, to tell the difference between it and HaveIBeenPwned, but it seems like WeLeakInfo just let you search data breaches and get all of the information, rather than just looking for your own information.

Given the number of breach data sets available for sale on the "darkweb" and other places, it's no real surprise that someone was going to start aggregating them and selling access.  I'm just surprised that this was out in the clear rather than a subscription service sold in carding forums.

The NCA's statement that they've established links between the purchase of "cyber crime tools" and this site certainly suggests that individuals who have been caught hacking have purchased both in order to use them together for nefarious purposes.

If this is as major as has been claimed, it would be nice to see a reduction in the amount of password spraying and password stuffing attacks online.  I won't be holding my breath though


## [Police Tracked a Terror Suspect—Until His Phone Went Dark After a Facebook Warning - WSJ](https://www.wsj.com/articles/police-tracked-a-terror-suspectuntil-his-phone-went-dark-after-a-facebook-warning-11577996973)

[https://www.wsj.com/articles/police-tracked-a-terror-suspectuntil-his-phone-went-dark-after-a-facebook-warning-11577996973](https://www.wsj.com/articles/police-tracked-a-terror-suspectuntil-his-phone-went-dark-after-a-facebook-warning-11577996973)

> The most immediate concern was a suspected terrorist investigators linked to Islamic State. They had received a tip he was part of a group plotting an attack around Christmas. Once they saw the suspect’s phone receive WhatsApp’s alert, the phone went dark, the official said. The sleuths soon lost access to the suspect’s messages, the official said, indicating he had discarded or disabled the phone.
> 
> “We only had that one phone,” the official said. “We put all our efforts into using this product to see what he was doing, which mosque he was going to, who was talking to him, whether the group was spread in neighboring countries.”
> 
> The interception of data from the suspect’s phone had gone on for just a few days before WhatsApp alerted the target. This meant the monitoring period had been too short to glean details of the suspected plot, the official said. The suspect had left his phone at home when he went out and was sending only brief messages, making investigators’ work more difficult.
> 
> Then WhatsApp sent its message: “An advanced cyber actor exploited our video calling to install malware on user devices. There’s a possibility this phone number was impacted.”
> 
> “WhatsApp killed the operation,” the official said. The terror suspect is still under traditional surveillance. But human resources are spread thin, the official said, especially around the winter holidays, which in Europe extend into early January and are a time when terrorists have staged attacks on the continent. “He’s not the only suspect we have to follow.”
> 
> The European official said NSO spyware had enabled his team to learn details of a separate gang of violent bank robbers and weapons traffickers and have police arrest them as they were about to commit a crime. In that case, they got lucky, the official said: “One gang member’s phone we had infiltrated was already in police custody when the WhatsApp message landed.”
> 
> The official said counterparts in other Western European countries told him more than 10 of their investigations may have been compromised by the WhatsApp alert. “I talked about it with my colleagues,” the official said. “They also couldn’t believe this was happening. It affected them more because they used this WhatsApp tool more than we did.” The former security official, from a different nation in Western Europe, said several countries there rely on NSO spyware in counterterrorism investigations.


I'm really torn on this one.  I think there's pretty compelling evidence that NSO group sells its software to a large number of intelligence and policing authorities around the world, including ones that don't have the same western moral codes as the major western nations.  The citizen lab investigation and others shows that some of the governments who have access to this software will use it in ways that we would personally disagree with.  But that doesn't make the tool bad.  We could spend the money in R&D to build the same set of exploits within our intelligence arms (and quite probably do), but those would be unlikely to be used outside of offensive cyber operations, such as in policing like this.  It's far better to buy a capability if it exists than to build your own.

Was the messaging from WhatsApp damaging to criminal investigations?  Of course it was, but was it WhatsApps right to tell their affected customers that they may have been hacked?  I think they were in the right.  While it's sad that intelligence and counter terrorism investigations lost a major interception capability, they should be prepared for that risk at all times.  An investigation needs to know that its tools aren't infallible and they might lose access at any time.  

In the meantime, WhatsApp cannot tell the difference between a lawfully approved operation and an illegal hacking attempt, so they provided the best risk mitigation that they could for their users, they informed them that there was a risk they had been hacked by an unknown advanced party.  If this had tipped off senior western government officials that their devices had been owned by a foreign intelligence agency, I don't think there would be as much screaming and hand wringing.


## [Critical Windows 10 vulnerability used to Rickroll the NSA and Github | Ars Technica](https://arstechnica.com/information-technology/2020/01/researcher-develops-working-exploit-for-critical-windows-10-vulnerability/)

[https://arstechnica.com/information-technology/2020/01/researcher-develops-working-exploit-for-critical-windows-10-vulnerability/](https://arstechnica.com/information-technology/2020/01/researcher-develops-working-exploit-for-critical-windows-10-vulnerability/)

> The attacker examines the specific ECC algorithm used to generate the root-certificate public key and proceeds to craft a private key that copies all of the certificate parameters for that algorithm except for the point generator. Because vulnerable Windows versions fail to check that parameter, they accept the private key as valid. With that, the attacker has spoofed a Windows-trusted root certificate that can be used to mint any individual certificate used for authentication of websites, software, and other sensitive properties.
> 
> As noted earlier, there are several requirements and constraints that significantly raise the bar for Rashid's attack to work in real-world uses by an adversary. The first is that it most likely requires an active man-in-the-middle attack. These types of attacks, which modify data as it passes through networks, may be difficult to carry out. An alternative to an active MitM is to convince a target to click on a fake URL. This method is much easier, but it also requires some targeting. (It wouldn't apply to attacks against websites or other servers that require a certificate from the connecting client.)


This is one of the best descriptions of CVE-2020-0601 that I've seen online so far, although if you are mathmatically inclined [trail of bits did a good explainer](https://blog.trailofbits.com/2020/01/16/exploiting-the-windows-cryptoapi-vulnerability/) too.  This is a major deal, and I think bigger than this analysis says.

People are so far building proof of concept code to demonstrate how it can be used to provide websites that can impersonate someone else.  But as has been pointed out, you have to intercept and interfere with peoples traffic to do that.  That's achievable for certain state level network attackers, but difficult for many others.

But the Windows Crypto library is also used to validate certain types of signed files, emails and executable code.  While we've not seen proof of concept for it, being able to send people executables that claim to be say, skype upgrades, that say they are fully signed is potentially more dangerous.  When ransomware and malware authors manage to exploit this, it will be far more dangerous.  that will take longer (primarily due to the caching needed to exploit the bug), and hopefully enough people will have patched that it won't be as big a deal, but then we know how effective patch programs are.

In the meantime, any attack that causes you to click a link could exploit this (although Firefox is exempt, and Chrome has issued a patch as well).  As we know from phishing tests, getting someone to click a link to a domain you control is really easy, so make sure you patch this on desktops across your estate, especially ones that browse email and the internet.


## [Windows 7 End of Support Info - Microsoft](https://www.microsoft.com/en-gb/windows/windows-7-end-of-life-support-information)

[https://www.microsoft.com/en-gb/windows/windows-7-end-of-life-support-information](https://www.microsoft.com/en-gb/windows/windows-7-end-of-life-support-information)

> What does end of support mean?
> As of 14 January 2020, your computer running Windows 7 will still function but Microsoft will no longer provide the following:
> 
> * Technical support for any issues
> * Software updates
> * Security updates or fixes
> 
> While you could continue to use your PC running Windows 7, without continued software and security updates, it will be at greater risk for viruses and malware. Going forward, the best way for you to stay secure is on Windows 10. And the best way to experience Windows 10 is on a new PC. While it is possible to install Windows 10 on your older device, it is not recommended.


This site for upgrading from Windows 7 now that it has ended support explicitly says "Don't just upgrade, why not buy an entire new PC instead?".  

It's also worth noting that there was an offer to upgrade from windows 7 to windows 10 for free back in 2016 when windows 10 was released, but if you want to upgrade now, as you should, you will have to buy your operating system.  That's £119.99 according to the Windows store.

If this is trying to make us all safer by getting people to upgrade, it's going about it with all the wrong incentives.  Those home users most at risk are the ones who have an office PC that they rarely use, and they don't want to change anyway.  I think we'll see lots of people not upgrading here until or unless there is another free upgrade option available (and even then the fear of change is high with these users).


## [How to adapt ITIL to DevOps with continual service transition | TechBeacon](https://techbeacon.com/enterprise-it/how-adapt-itil-devops-continual-service-transition)

[https://techbeacon.com/enterprise-it/how-adapt-itil-devops-continual-service-transition](https://techbeacon.com/enterprise-it/how-adapt-itil-devops-continual-service-transition)

> The focus of service transition in ITIL on operability and service readiness is very valuable. Service transition as a separate phase only after software has been developed does not fit well with a modern DevOps-style incremental delivery of small changes.
> 
> Instead, the attention to service readiness and operability should happen all the time—​"continual service transition"—​with close collaboration among the groups involved.


This is a good explanation of the benefits and power of ITIL as a shared language and even formalised expectations, and how it can be used by teams practicing DevOps.
For some reason, ITIL always gets associated with slow waterfall style processes.  But in reality while some of that is in the assumptions of the original authors, in reality, it has a lot of very good checklists for ensuring that you are building operable software.  By automating the processes, we can make them run faster, but that doesn't mean throwing it all away, it just means automating the same processes.

(There are some issues with this approach, because the one thing hanging around in ITIL is the assumption that there is a delivery team and an operations team.  But if you remove that, the transition approach is still valuable)


