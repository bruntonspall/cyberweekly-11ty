---
title: "93 - Tools shape our thinking"
date: 2020-03-15
description: "The more I look at how digital transformation and digital culture is going, the more I realise that one of our big problems is the lack of attention to the tooling that we use."
permalink: /tools-shape-our-thinking/
---

The more I look at how digital transformation and digital culture is going, the more I realise that one of our big problems is the lack of attention to the tooling that we use.

I think everyone has heard the phrase "When all you have is a hammer, everything looks like a nail", but the counterpoint to this is that, particularly within digital transformation, we want to give people new screwdrivers, but they're still trying to drive nails into the wall.  Ok, maybe I've tortured that analogy a little far, but the thing I'm trying to say is that we are asking people to change the way they work, to change their culture and the way that they think, but we often require the same sets of artifacts and processes that they've always had to produce and work through.

I'm working with teams at the moment around agile governance, and one of things that we identify is that we want to work in an agile and iterative way, but that at some point, the organisation requires us to conduct a data protection impact assessment for the data that we are going to hold.  And our organisation has a proforma document that we must produce as part of that process.  But this document, this artifact, is almost impossible to produce using the agile and iterative tools that we have, and so we get people like me acting as an interpreter and trying to produce a document that looks right for what we are doing.

What hope is there for this new culture to catch on in the rest of the organisation that isn't lucky enough to have somoene like me doing this for them?  Instead they'll be told "be agile, think user first", but also "you need to produce document X, project plan Y, business case Z".

When we approach digital transformation, we often start with culture and ways of working.  We try to break people out of the habit of the ways that they traditionally worked.  But we underestimate the power of the tools that we give people.  The tools that we use shape the way that we think, because when we hold a screwdriver, we look for screw shaped problems, and when we hold a hammer, we look for nail shaped problems.

What if your team had a one or two of developers who wrote tools for everyone to use?  What if those tools encouraged iterative thinking and iterative decision making, and achieved the aim that you want?  What if when you start a project, you had to go to a data protection tool that asked you some basic questions, and you could go back to it, week after week and update the information in it.  What if that tool allowed the data protection team to see the current snapshot state of each teams data protection thinking, and enabled them to determine who had done a healthy impact assessment, and who needed help?

I'm used to web development (it's been 15 years since I wrote anything but websites), and so I look at this as being a web based tool, but it might be a google forms, or a surveymonkey page, or a sharepoint site.  But the value of the tool is that you can use it to define people's thinking, to encourage them to engage in a specific way.  How are you asking people to tell you about their risks?  How are you tracking project progress or financial spend? What tools do you give people to use in these areas and how are they shaping their thinking?  

Maybe the failure of transformation projects is because we spend too much time talking about culture, ways of working, governance and process and not enough time just giving people the right shaped tools and showing them how to use them.

## [Exaggerated Lion How an African Cybercrime Group Leveraged G Suite and a Check Mule Network to Build a Prolific BEC Operation [pdf]](https://www.agari.com/cyber-intelligence-research/whitepapers/acid-agari-exaggerated-lion.pdf)

[https://www.agari.com/cyber-intelligence-research/whitepapers/acid-agari-exaggerated-lion.pdf](https://www.agari.com/cyber-intelligence-research/whitepapers/acid-agari-exaggerated-lion.pdf)

> Tier I mules are long-standing romance scam victims who are completely invested in their
> “relationship” with a fictitious Exaggerated Lion persona and have built up a significant amount
> of trust. They are trusted with larger amounts of money and are usually the ones responsible for
> sending money directly to the scammers overseas. These mules are comfortable opening new
> bank accounts and moving funds around to assist Exaggerated Lion actors without questioning
> why. Due to the level of indoctrination, Tier I mules have difficulty seeing through the fact that
> they are being scammed, even when presented with evidence that what they are doing is
> considered fraud. In some cases, these mules will even tell their handler about meeting with law
> enforcement if they are questioned about their potential involvement in fraudulent activity. 


This report has a couple of interesting notes in it.  The first is this description of how Tier I money mules operate.  These are individuals who have been scammed in a romance scam, believe that the person they are communicating with is in love with them, and are willing to take all kinds of interesting measures in terms of moving money around to keep the romance alive.

I struggle to imagine how people fall for this, but it seems like people really do, and their committment to their "romantic partners" makes then very useful dupes for this con group.

The second is the use of GSuite free trials for the scams.  They send scam emails from domains that are unusually long, and filled with words that might make someone think that this is a companies secure email solution, for example office-secure-ssl-sl-mail71521-apps-server-portal-apps-mail.management.
These are registered to a free trial of Googles GSuite, and they can use the free tier limits to send out thousands of emails per day.

Interestingly, the report claims that these scammers make up around 10% of all .management top level domains, and own 75% of all GSuite infrastructure on the management TLD.


## [‘Cloud Snooper’ Attack Bypasses Firewall Security Measures – Sophos News](https://news.sophos.com/en-us/2020/02/25/cloud-snooper-attack-bypasses-firewall-security-measures/)

[https://news.sophos.com/en-us/2020/02/25/cloud-snooper-attack-bypasses-firewall-security-measures/](https://news.sophos.com/en-us/2020/02/25/cloud-snooper-attack-bypasses-firewall-security-measures/)

> For example, you might typically set up an AWS Security Group that only allows web traffic – that is, TCP packets that arrive at ports 80 or 443 – to reach your server. Network traffic with any other destination port never makes it past the SGs.
> 
> The infection involves a rootkit that inspects network traffic, and a backdoor that the attackers leverage the rootkit to send commands to, and receive data from, the backdoor.
> 
> In order to get around the firewall rules, depicted here as guards, the attackers communicate with the rootkit by sending innocent-looking requests (depicted in the illustration as a wolf in sheep’s clothing) to the web server on the normal web server ports. A listener that inspects inbound traffic before it reaches the web server intercepts the specially-crafted requests, and sends instructions to the malware based on characteristics of those requests.
> 
> The listener sends a “reconstructed” C2 command to the backdoor Trojan installed by the rootkit. Depending on the commands included into C2 traffic, the attacker may use the backdoor to steal sensitive data from the target.


This was the report that resulted in lots of headlines about "AWS firewalls bypassed", and for me wins the award for "most misleading headline/title".  

This attack and malware, while a lovely bit of kit, has absolutely no real connection with AWS or even the cloud.  This exact attack, indeed this exact malware would work in exactly the same way on your on-premise hardware, on a private Virtual Machine cluster or on a private cloud.

The attack is dependant on already compromising the machine, installing malware that can look at network packets coming to the machine, and then using some neat trickery to detect packets that look like they are legitimately coming for your normal webserver and redirecting them to your malware.

Snuck in the report, somewhat queitly is this statement:

>At this point in the investigation, we still have some open questions. For example, it is still unclear how the attackers managed to compromise the client’s system in the first place. One of the working theories is that the attackers broke into a server through SSH, protected with password authentication

In other words, this has nothing to do with cloud, it's just a neat bit of advanced malware that uses a new and hard to detect command and control mechanism.  One that is worth watching out for in your network.  The easiest detection at the moment is probably looking for open ports on machines that didn't have that port open before.  The report on this particular instance uses port 2080, but I'm sure the malware can be trivially recompiled to use a different port number.


## [Monzo: a case study in the ups and downs of being open – Digital by Default](https://digitalbydefault.com/2020/02/26/monzo-a-case-study-in-the-ups-and-downs-of-being-open/)

[https://digitalbydefault.com/2020/02/26/monzo-a-case-study-in-the-ups-and-downs-of-being-open/](https://digitalbydefault.com/2020/02/26/monzo-a-case-study-in-the-ups-and-downs-of-being-open/)

> There was also a little piece about Monzo in the latest Wired(UK) which was highlighting the company culture including their commitment to openness. I do wonder/fear if – like other open organisations before them – the negatives will come to outweigh the positives of that approach as they scale and reach for new markets (i.e. the US) and they start to see the working in the open as a distraction rather than a USP.


I had similar views about the recent online kerfuffle about Monzo's hiring practices for product managers.  The people at Monzo have had a lot of stick over several bits of openness recently, whether it be how they hire, the microservices architecture they use or the language adn team practices that they adopt.

Armchair analysts (of which I am one), tend to find it easy to criticise decisions from the outside with very much a "I wouldn't do it that way".  However, hindsight is always perfect, and many decisions are made not because of a single big decision, but because of thousands of little decisions going back through time that lead you to this point.  I doubt someone sat down and thought "I'm going to create a product manager hiring test" and came up with what Monzo had.  Instead it probably iterated over time, it worked for hiring the existing staff, it accommodated their existing biases and it became "the way we do things".

It's far too easy to throw rocks at someone else's stuff, and especially when they are being open about how they think, how they work.  We should laud people for being willing to be open about these things, because even if you think "I wouldn't do that in my company", that's valuable experience for you that you didn't have to go through the effort and pain to gain.


## [Vault 7 court case ends in mistrial on most serious charges](https://www.cyberscoop.com/vault-7-mistrial-cia-joshua-schulte/)

[https://www.cyberscoop.com/vault-7-mistrial-cia-joshua-schulte/](https://www.cyberscoop.com/vault-7-mistrial-cia-joshua-schulte/)

> Witnesses described an often unprofessional environment in the CIA’s Engineering Development Group, where employees would spend weeks or months on tools meant to exploit software vulnerabilities in devices like smart TVs or mobile systems to spy on targets. Instead of cloak-and-dagger operations, though, the jury heard of Nerf gun fights, pranks and a competitive atmosphere that would escalate into physical altercations or racist diatribes.
> 
> As a developer, Schulte worked with a small team of CIA personnel on a project called Brutal Kangaroo, a suite of hacking tools meant to breach Windows computers via USB drives. One former co-worker who still works at the agency testified that other CIA agents referred to Schulte as “nuclear option” and “badass” because of his propensity to attack perceived office rivals when he was annoyed.
> 
> At one point, prosecutors said, Schulte became locked in an ongoing feud with another employee on his team, identified only as “Amol.” Schulte fabricated a story in which Amol had threatened to kill Schulte, according to one witness, while also urging CIA higher-ups to discipline Amol. When the agency determined the complaint was baseless, Schulte was moved to a different project.


I was surprised that the jurors did not find Schulte guilty.  I've been reading the transcripts as this trial has gone along (they're very long), and I thought this was a pretty clear case, all of the circumstantial evidence pointed at Schulte as being the guilty party.  However, because the CIA did not, or could not explain what happened to another potential suspect that had the means to carry out the attack, the jury decided that they couldn't be sure, beyond reasonable doubt, that Schulte had actualy done it.

This is quite damaging that the CIA and FBI had pretty good technical evidence that showed that they felt this action was carried out, but that their fears of exposing too much of the internal workings of the CIA's most sensitive operations meant that they couldn't close down reasonable doubt.  I've long argued that the lack of transparency around out intelligence and security agencies does more damage than good, that the collecting public shrugging to the Snowdon leaks has shown that the public are broadly accepting of how those agencies work, and that the opaqueness serves to hide more misdeeds and incompetence than protects us from enemies.   This feels like another evidence point in that favour, and shows that even accusations of breaking some of the most serious laws are difficult to prove in a court of law.  This will encourage and enable further leakers in future, that they may well not end up prosecuted if they can leave enough doubt in the system.


## [Digital transformation hits the 'Trough of Disillusionment'](https://diginomica.com/digital-transformation-hits-trough-disillusionment)

[https://diginomica.com/digital-transformation-hits-trough-disillusionment](https://diginomica.com/digital-transformation-hits-trough-disillusionment)

> Taken together, these three reports seem to point to a potential stalling of the important trend towards digital transformation. The obvious short answer is a slide into the well documented Gartner Trough of Disillusionment, but it does also give some evidence as to how that trough emerges. There is certainly the vagaries of the marketplace itself, especially across the UK and, to a lesser extent, Europe. There are currently sufficient uncertainties to make run-away- and-hide seems like a plausible business strategy.
> 
> But these reports also show evidence that many businesses are still unclear about what they are hoping to achieve or how to achieve it, while those that they should turn to – the systems vendors – are still far too oriented to the tendency of playing `confuse-a-cat’ with the hokum of technological detail.


This speaks to me strongly.  Like all technology hype, digital transformation is boyed by success stories like GDS that ignore the survivor bias and confuses itself into not understanding why it succeeded where other failed.

It is easy for those of us who were there to think that the successes are because of the amazing efforts we did, which leads to people loudly claiming that if you put up some nice posters about culture and buy slack, then you will transform your culture.

The reality is that far more efforts try these things and fail than the ones that succeed and very few people have enough data yet to understand why it works when it works.  The smartest people I know in this area are constantly reminding us that digital transformation isn’t a goal in an of itself, but that we need to actually understand what the business needs (it what it wants or thInks it needs, and then work out how digital tooling, ways and means can help achieve that).


## [USB Drop Attacks: The Danger of “Lost And Found” Thumb Drives](https://www.redteamsecure.com/blog/usb-drop-attacks-the-danger-of-lost-and-found-thumb-drives/)

[https://www.redteamsecure.com/blog/usb-drop-attacks-the-danger-of-lost-and-found-thumb-drives/](https://www.redteamsecure.com/blog/usb-drop-attacks-the-danger-of-lost-and-found-thumb-drives/)

> A particularly well-known example of a USB drop attack is Stuxnet, a computer worm that infected software at industrial sites in Iran, including a uranium-enrichment plant. The virus targeted industrial control systems made by Siemens, compromised the system’s logic controllers, spied on the targeted systems, and provided false feedback to make detection even more difficult, and it all began with a USB stick infection.
> 
> The United States government, too, has fallen victim to flash drive attacks. In 2008 an infected flash drive was plugged into a US military laptop in the Middle East and established “a digital beachhead” for a foreign intelligence agency. The malicious code on the drive spread undetected on both classified and unclassified systems enabling data to be transferred to servers under foreign control.
> 
> In one test of how well a USB scam can work, Trustwave planted five USB drives decorated with the targeted company’s logos in the vicinity of the organization’s building. Two of the five “lost & found” drives were opened at the organization. One of the openings even enabled the researchers to glimpse software employed to control the organization’s physical security.


I went looking a while ago for any evidence of USB thumb-drive attacks, and interestingly all I can find is endless number of red team descriptions of attacks.  There are only 2 "in-the-wild" attacks that I've seen using USB attacks, the infamous StuxNet, and the attack on a US military laptop.  Everything else I can find is researchers showing just how effective an attack it can be.

What evidence is there behind the risk statements that we give?  Lots of people talk about disabling USB drives because of this kind of attack, and it works in penetration testing exercises repeatedly and effectively, but it's very rarely used in practice.  Is that because we don't know about the attacks that were successful, or is it because, while effective, it requires physical access and that's far more work than most attackers want to use?  Or maybe we just all have such good security controls around USB devices that attackers don't think it's worth it? But then the pen tests wouldn't succeed as often as they do.

I would have said that discouraging the use of random USB drives would be uncontroversial security advice, but now I'm questioning if that's actually true.  If there is a usability impact, then is it really worth it?  


## [Work remotely, stay secure—guidance for CISOs](https://www.microsoft.com/security/blog/2020/03/12/support-working-from-home-securely/)

[https://www.microsoft.com/security/blog/2020/03/12/support-working-from-home-securely/](https://www.microsoft.com/security/blog/2020/03/12/support-working-from-home-securely/)

> While many employees have work laptops they use at home, it’s likely organizations will see an increase in the use of personal devices accessing company data. Using Azure AD Conditional Access and Microsoft Intune app protection policies together helps manage and secure corporate data in approved apps on these personal devices, so employees can remain productive.
> 
> Intune automatically discovers new devices as users connect with them, prompting them to register the device and sign in with their company credentials. You could manage more device options, like turning on BitLocker or enforcing password length, without interfering with users’ personal data, like family photos; but be sensitive about these changes and make sure there’s a real risk you’re addressing rather than setting policies just because they’re available.
> 
> Read more in Tech Community on ways Azure AD can enable remote work.
> 
> You’ve heard me say it time and again when it comes to multi-factor authentication (MFA): 100 percent of your employees, 100 percent of the time. The single best thing you can do to improve security for employees working from home is to turn on MFA. If you don’t already have processes in place, treat this as an emergency pilot and make sure you have support folks ready to help employees who get stuck. As you probably can’t distribute hardware security devices, use Windows Hello biometrics and smartphone authentication apps like Microsoft Authenticator.


This is good guidance from Microsoft on how to enable remote workers using Microsofts tools.  If you've already bought into the ecosystem, then this is a cheap and easy win for the organisation.  The note on remembering that users may *need* to use their own personal devices to access sensitive data is important.  As is the note to

> be sensitive about these changes and make sure there’s a real risk you’re addressing rather than setting policies just because they’re available

If you enabling this temporarily for your teams, then you can take a risk and not turn on every security option there is.  You are going to turn it off soon anyway, unless you mysteriously discover that disabling a lot of your security controls makes the business much more effective, without causing any security incidents.  I mean... wouldn't that be a surprise.


## [Distributed teams are critical to the future success of digital government services - GovFresh](https://govfresh.com/2020/02/distributed-teams-are-critical-to-the-future-success-of-digital-government-services/)

[https://govfresh.com/2020/02/distributed-teams-are-critical-to-the-future-success-of-digital-government-services/](https://govfresh.com/2020/02/distributed-teams-are-critical-to-the-future-success-of-digital-government-services/)

> We now have the tools — G Suite, Slack, GitHub, Zoom to name just a few — that fully empower asynchronous, instant collaboration. Training on the tools, the culture of distributed, as well as implementing supporting policies are critical to highly effective distributed teams.
> 
> In 2020 we now have all of these at our disposal.


Organisations face a critical security decision, probably about 2 weeks ago, but if they didn't make it then, they need to make it now.  Lots of organisations ban these sorts of remote friendly tooling because it's not part of their corporate infrastructure.  Their Microsoft Teams and Sahrepoint instance that is locked down to computers from the office is the "only secure way" to ensure that staff can't leak information, put it on computers that can be lost or stolen, or work from home effectively.

Organisations need to take a risk decision right now, enable this form of remote working, maybe only temporarily, or suffer a far bigger business risk than the security risk.  Now is the time to open your firewalls, click those options in Office 365 that allows BYOD, and buy or use remote first capability tools like Zoom and Slack.  Yes, it might be an infosec risk, but given what we face, it's probably a risk worth taking.


## [Distributed Team vs Remote Work, Virtual Work, Telework and Work From Home – John O'Duinn's blog](https://oduinn.com/2020/02/25/distributed-team-vs-remote-work-and-work-from-home/)

[https://oduinn.com/2020/02/25/distributed-team-vs-remote-work-and-work-from-home/](https://oduinn.com/2020/02/25/distributed-team-vs-remote-work-and-work-from-home/)

> The terms “distributed teams”, “virtual teams”, “virtual employee”, “remote work”, “remote employee”, “work from home”, “work from anywhere” and “telework” are often used interchangeably, even though they mean very different things. Used incorrectly, these terms can (mis)communicate important human, social context in ways that are damaging and unintended. Hopefully, this summary helps people be more intentional and crisp when describing work arrangements:
> 
> Distributed Team: This clearly and correctly describes that all humans on the team work together, even though they are physically apart from each other. This is not a collection of individuals who each do solo heads-down work from different locations. Instead, this is a group of humans who coordinate their work with others on their physically distributed team. Because everyone on the physically distributed team is “remote” from someone, it is clear that everyone on the team has equal responsibility to communicate and coordinate their work with coworkers – regardless of whether any individual human is working from a building with the company logo on the door, from home, from a coworking space, a hotel or a parked car!
> 
> [...]
> 
> Work from home: ....  The lack of focus on who/how is responsible for coordinating the work makes me feel this term applies to humans who temporarily use a different location to do solo heads-down work without interruption and will then eventually return to their usual desk in the office when they need to coordinate their work with co-workers.


Given that lots of organisations are going to be asking their employees to work remotely far more over the next 4-6 months (and yes, I think it'll be that long), knowing what remote work actually looks like is important.  John here disambiguates between true distributed teams that assume that work is divided amongst employees who can work on it no matter their location, but who use remote tools to keep in touch, manage work and distribute work is vastly different to the "work from home" culture of giving specific work to someone to work on remotely, but not changing the culture of management, task allocation and coordination that assumes colocation as the core coordinating function.

If you ask your employees to take some work home for an extended period (such as 7-day self quarantine), but don't do the necessary work to support coordination and management with a distributed team, then your work from home colleagues are going to be significantly less productive, they will feel isolated and they will hate the experience.

When this is all over, and teams reform back at the office, it's highly likely that a lot of managers who didn't setup these structures are going to learn that distributed teams are less efficient, frustrating and bad.  That's a big worry given the rise in distributed organisations today.


