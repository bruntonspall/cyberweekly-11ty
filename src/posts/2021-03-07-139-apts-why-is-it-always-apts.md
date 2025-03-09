---
title: "139 - APTs, Why does it always have to be APTs?"
date: 2021-03-07
description: "Channeling my inner Indiana Jones, but why is it always APTs?"
permalink: /apts-why-is-it-always-apts/
---

Channeling my inner Indiana Jones, but why is it always APTs?

Everytime there is an attack, vulnerability or compromise, there are government issued alerts, suppliers and journalists all competing to yell loudly that this is it, this is the big cyber apocalypse.

The HAFNIUM intrusions and Exchange zero-days are a bad vulnerability.  Actively exploited zero-days are always a concern, and organisations need to patch, but the semi-hysterical worries around attribution and the sky is falling may not be helping as much as we think.

It can be exhausting to feel like there are just constant crises going on.  If instead we are able to issue the patches and the warnings, ensure that people understand the importance of how urgently to patch without triggering a mass crisis would be nice.

When researchers attempt to make their research stand out in and amongst all the crisis management that we have to do in cybersecurity, it means that we are incentivised to overstate the research, or at least give it a spin that sounds worse than it really might be.  Sometimes, it's a huge nation state cyber attack, and sometimes it's just the left over debris of an ad network.  The fact that we still don't have the easy ability to tell the difference tells us how poorly we actually understand much of this activity.

Meanwhile, the growing context in which we operate is one where more and more people have access to advanced cyber capabilities, that they can use "access as a service" to use operational capability far beyond their means on an adhoc basis.  While right now, much of those capabilities are only available to Governments, there are many people from charities, journalists and citizens who can be regarded an enemy of a government, and of course, these capabilities will inevitably trickle down into criminal society over the next few years.

## [HAFNIUM targeting Exchange Servers with 0-day exploits - Microsoft Security](https://www.microsoft.com/security/blog/2021/03/02/hafnium-targeting-exchange-servers/)

[https://www.microsoft.com/security/blog/2021/03/02/hafnium-targeting-exchange-servers/](https://www.microsoft.com/security/blog/2021/03/02/hafnium-targeting-exchange-servers/)

> Microsoft has detected multiple 0-day exploits being used to attack on-premises versions of Microsoft Exchange Server in limited and targeted attacks. In the attacks observed, the threat actor used these vulnerabilities to access on-premises Exchange servers which enabled access to email accounts, and allowed installation of additional malware to facilitate long-term access to victim environments. Microsoft Threat Intelligence Center (MSTIC) attributes this campaign with high confidence to HAFNIUM, a group assessed to be state-sponsored and operating out of China, based on observed victimology, tactics and procedures.
> 
> The vulnerabilities recently being exploited were CVE-2021-26855, CVE-2021-26857, CVE-2021-26858, and CVE-2021-27065, all of which were addressed in today’s Microsoft Security Response Center (MSRC) release – Multiple Security Updates Released for Exchange Server. We strongly urge customers to update on-premises systems immediately. Exchange Online is not affected.
> 
> Update [03/04/2021]: The Exchange Server team released a script for checking HAFNIUM indicators of compromise (IOCs). See [Scan Exchange log files for indicators of compromise.](https://www.microsoft.com/security/blog/2021/03/02/hafnium-targeting-exchange-servers/#scan-log)


This is a pretty significant attack, and one that should be easy to patch (in theory).

In particular the attack is on the web facing portions of exchange, so patching should cause minimal downtime.  You could in the short term, block access to Outlook Web Access or any other web access to your exchange server without losing incoming and outgoing email for your organisation.


## [New nation-state cyberattacks - Microsoft On the Issues](https://blogs.microsoft.com/on-the-issues/2021/03/02/new-nation-state-cyberattacks/)

[https://blogs.microsoft.com/on-the-issues/2021/03/02/new-nation-state-cyberattacks/](https://blogs.microsoft.com/on-the-issues/2021/03/02/new-nation-state-cyberattacks/)

> Historically, Hafnium primarily targets entities in the United States for the purpose of exfiltrating information from a number of industry sectors, including infectious disease researchers, law firms, higher education institutions, defense contractors, policy think tanks and NGOs. While Hafnium is based in China, it conducts its operations primarily from leased virtual private servers (VPS) in the United States.
> 
> Recently, Hafnium has engaged in a number of attacks using previously unknown exploits targeting on-premises Exchange Server software. To date, Hafnium is the primary actor we’ve seen use these exploits, which are discussed in detail by MSTIC here. The attacks included three steps. First, it would gain access to an Exchange Server either with stolen passwords or by using the previously undiscovered vulnerabilities to disguise itself as someone who should have access. Second, it would create what’s called a web shell to control the compromised server remotely. Third, it would use that remote access – run from the U.S.-based private servers – to steal data from an organization’s network.


Two important notes here.  

The first is that so far, only HAFNIUM has been seen utilising these exploits.  This changed within hours of this notice going up, and it's clear that exploits are already out there in the hands of other attack groups, and as such, you should not say "I'm not a target of HAFNIUM, so I don't need to patch".

Secondly, these attacks are only the initial compromise, as soon as they get access, they install a webshell and start compromising you from there.  As well as patching, you should check for the existence of webshells on your servers, as simply patching won't kick them out of your system if they've got in already.


## [Multimodal Neurons in Artificial Neural Networks](https://openai.com/blog/multimodal-neurons/)

[https://openai.com/blog/multimodal-neurons/](https://openai.com/blog/multimodal-neurons/)

> Through a series of carefully-constructed experiments, we demonstrate that we can exploit this reductive behavior to fool the model into making absurd classifications. We have observed that the excitations of the neurons in CLIP are often controllable by its response to images of text, providing a simple vector of attacking the model.
> 
> The finance neuron [1330], for example, responds to images of piggy banks, but also responds to the string “$$$”. By forcing the finance neuron to fire, we can fool our model into classifying a dog as a piggy bank.
> 
> 
> By rendering text on an image, we artificially stimulate neuron 1330, which has high weight into the class “piggy bank” in a linear probe. This causes the classifier to misclassify a Standard Poodle as a piggy bank.
> 
> Attacks in the wild
> 
> We refer to these attacks as typographic attacks. We believe attacks such as those described above are far from simply an academic concern. By exploiting the model’s ability to read text robustly, we find that even photographs of hand-written text can often fool the model. Like the Adversarial Patch,22 this attack works in the wild; but unlike such attacks, it requires no more technology than pen and paper.
> 
> When we put a label saying “iPod” on this Granny Smith apple, the model erroneously classifies it as an iPod in the zero-shot setting.
> We also believe that these attacks may also take a more subtle, less conspicuous form. An image, given to CLIP, is abstracted in many subtle and sophisticated ways, and these abstractions may over-abstract common patterns—oversimplifying and, by virtue of that, overgeneralizing.


This is a super interesting area of research, as Machine Learning is more in use across various systems, we are going to see these sorts of things bite people. 

Our expectations around machine vision are that it does what it says on the tin, you give it a picture of an apple and it says "apple", you give it a street sign and it tells you what's written on the street sign.  But that means that the vision algorithm needs to respond to different abstractions, from photos of a thing, to abstract representations of a thing and written words of a thing.  But as indicated here, put a sticky note on an Apple that says "iPod", and the AI will tell you that it's a photo of an iPod.

If you are building till systems in shops that attempt to identify produce as it's being scanned, then this sort of attack might enable someone to get away with labeling high value items as low value items.  Hopefully when you build that, the vision component is only one component, and the weight, barcode and other indicators will all be wrong.

I'm not convinced that this is trivially fixable, almost all AI systems that we use, we want to have these capabilities.  The article makes out the case for why we want them, talking about being able to respond to pictures of spiderman in costume, comic drawings of spiderman and the text for spiderman with equal clarity.  But it also talks about the dark side, that this means that the CLIP neuron's can encode racial bias or other linkages that may represent some of the input data, but not something you'll necessarily want in your recognition system.


## [Countering cyber proliferation: Zeroing in on Access-as-a-Service - Atlantic Council](https://www.atlanticcouncil.org/in-depth-research-reports/report/countering-cyber-proliferation-zeroing-in-on-access-as-a-service/)

[https://www.atlanticcouncil.org/in-depth-research-reports/report/countering-cyber-proliferation-zeroing-in-on-access-as-a-service/](https://www.atlanticcouncil.org/in-depth-research-reports/report/countering-cyber-proliferation-zeroing-in-on-access-as-a-service/)

> Left unchecked, the continued proliferation of offensive capabilities could significantly damage the global economy, international security, and the values that the United States and its allies hold dear. Thus, it is imperative that governments reevaluate their approach to countering the proliferation of OCC. This report profiles the “Access-as-a-Service” (AaaS) industry, a significant vector for the proliferation of OCC, as a means of both illustrating the character of this proliferation and investigating policies to counter it.
> 
> AaaS firms offer various forms of “access” to target data or systems, and through these business practices are creating and selling OCC at an alarming rate. These companies advertise their wares to myriad groups, mostly states, who would not otherwise be able to develop such capabilities themselves. 


This report makes for engaging reading.  The development of cyber capabilities around the world has not only foreign policy implications (something I'm entirely unqualified to comment on), but also has a general rising tide effect.

It's almost impossible to actually keep the use of cyber weapons secret, a lucky of competent defender can watch the use of the weapons, reverse engineer them and then weaponise them for their own use.  This means that the continual development and use of these tools will leak out into the wider adversarial community.

The other interesting reference in here is the identification of the five pillars of Offensive Cyber Capability, in particular the pulling out of the technical command and control, operational management and training and support pillars which in general are the differentiator between a capable cyber adversary and an advanced persistent threat.


## [Silver Sparrow macOS malware with M1 compatibility](https://redcanary.com/blog/clipping-silver-sparrows-wings/)

[https://redcanary.com/blog/clipping-silver-sparrows-wings/](https://redcanary.com/blog/clipping-silver-sparrows-wings/)

> Earlier this month, Red Canary detection engineers Wes Hurd and Jason Killam came across a strain of macOS malware using a LaunchAgent to establish persistence. Nothing new there. However, our investigation almost immediately revealed that this malware, whatever it was, did not exhibit the behaviors that we’ve come to expect from the usual adware that so often targets macOS systems. The novelty of this downloader arises primarily from the way it uses JavaScript for execution—something we hadn’t previously encountered in other macOS malware—and the emergence of a related binary compiled for Apple’s new M1 ARM64 architecture.
> 
> We’ve dubbed this activity cluster “Silver Sparrow.”
> 
> Thanks to contributions from Erika Noerenberg and Thomas Reed from Malwarebytes and Jimmy Astle from VMware Carbon Black, we quickly realized that we were dealing with what appeared to be a previously undetected strain of malware.
> 
> According to data provided by Malwarebytes, Silver Sparrow had infected 29,139 macOS endpoints across 153 countries as of February 17, including high volumes of detection in the United States, the United Kingdom, Canada, France, and Germany.
> 
> Though we haven’t observed Silver Sparrow delivering additional malicious payloads yet, its forward-looking M1 chip compatibility, global reach, relatively high infection rate, and operational maturity suggest Silver Sparrow is a reasonably serious threat, uniquely positioned to deliver a potentially impactful payload at a moment’s notice. Given these causes for concern, in the spirit of transparency, we wanted to share everything we know with the broader infosec industry sooner rather than later.


I thought I had included this a few weeks back, but I can't find it in my records.

This is interesting and novel for 2 reasons:

1.  Mac malware is comparitvely rare, and of course people are therefore concerned that this might be targetting the tech industry and developers in particular.  Since this has also already released an M1 variant (it targets both Intel Macs and M1 macs), that mean that the operators are at least moderately skilled and keeping it up to date.

2. Targeting such a world wide base of people, without any actual malicious activity feels super suspicious.  Is it an actor trying to build a base from which to conduct a massive attack?  Is it an espionage group who post infection decide it's not proportionate to attack?


## [ESET research on Twitter](https://twitter.com/ESETresearch/status/1366677211303079938)

[https://twitter.com/ESETresearch/status/1366677211303079938](https://twitter.com/ESETresearch/status/1366677211303079938)

> We have received a lot questions about the Silver Sparrow malware for macOS after a publication by 
> @redcanary
> .  #ESETresearch has investigated and found that, far from speculations about nation-state malware, it is likely related to adware and pay-per-install schemes.


Also at [ThreadReader](https://threadreaderapp.com/thread/1366677211303079938.html).

That OSX Malware that is sitting dormant and could be an APT attack from a few weeks ago.  Might also be a false alarm, and not an APT. but rather the vestiges of an adware campaign.  Who knows the truth?


## [Build Pipeline Security](https://sprocketfox.io/xssfox/2021/02/18/pipeline/)

[https://sprocketfox.io/xssfox/2021/02/18/pipeline/](https://sprocketfox.io/xssfox/2021/02/18/pipeline/)

> The issue here is that the buildspec.yml and deploy.sh could be modified by a malicious user.
> 
> The pull request
> However malicious user doesn’t have access to commit to the repository and an admin isn’t going to merge malicious code, so this is no big deal right? Let’s see what happens when we lodge a pull request.
> 
> Upon creation of the pull request GitHub triggers a CodeBuild job. This is a fairly common practice to make sure nothing in the pull request breaks the build. What prevents the pull request build from deploying to production? Lets check deploy.sh
> 
> if [[ "$CODEBUILD_WEBHOOK_HEAD_REF" == "refs/heads/main" && ${CODEBUILD_SOURCE_VERSION:0:3} != "pr/" ]]; then
> oh no.
> 
> So deployment is purely controlled by a script that can be changed in the pull request.
> 
> [...]
> 
> Prevention
> If you still want pull requests to trigger builds on a public repository there a couple of things you can do to limit risk.
> 
> Place build scripts in a separate repo. Some build tools let you specify a separate repo to use for the build pipeline. Be careful though as this doesn’t guarantee that the project build can’t execute commands, depending on the programming language and build tools.
> 
> For services like CodeBuild you can utilize a separate IAM role for pull requests which is limited to just build requirements. Make sure the build agents for PRs aren’t within a a trusted network.


This exposes an interesting vulnerability that I've talked about before, but hadn't seen referenced anywhere.

If your deployment and build scripts are in the same open repository that you accept pull requests on, and you build pull requests, then you are by default giving external people access to run pretty much anything on your build servers.

As mentioned in here, the preventative measures here are to either externalise your build and deployment scripts, so they can't be modified by the pull request, and to ensure that PR's are built differently to the master build, with say different IAM roles that cannot deploy to production.


## [Lazarus targets defense industry with ThreatNeedle [pdf]](https://ics-cert.kaspersky.com/media/Kaspersky-ICS-CERT-Lazarus-targets-defense-industry-with-Threatneedle-En.pdf)

[https://ics-cert.kaspersky.com/media/Kaspersky-ICS-CERT-Lazarus-targets-defense-industry-with-Threatneedle-En.pdf](https://ics-cert.kaspersky.com/media/Kaspersky-ICS-CERT-Lazarus-targets-defense-industry-with-Threatneedle-En.pdf)

> In the course of this research, we identified another highly interesting technique
> used by the attackers for lateral movement and exfiltration of stolen data. The
> enterprise network under attack was divided into two segments: corporate (a
> network on which computers had internet access) and restricted (a network on
> which computers hosted sensitive data and had no internet access). According
> to corporate policies, no transfer of information was allowed between these two
> segments. In other words, the two segments were meant to be completely
> separated.
> 
> Initially, the attackers were able to get access to systems with internet access
> and spent a long time distributing malware between machines in the network’s 
> corporate segment. Among the compromised machines were those used by the
> administrators of the enterprise’s IT infrastructure.
> 
> It is worth noting that the administrators could connect both to the corporate
> and the restricted network segments to maintain systems and provide users
> with technical support in both zones. As a result, by gaining control of
> administrator workstations the attackers were able to access the restricted
> network segment.
> 
> However, since directly routing traffic between the segments was not possible,
> the attackers couldn’t use their standard malware set to exfiltrate data from the
> restricted segment to the C2.
> 
> The situation changed on July 2 when the attackers managed to obtain the
> credentials for the router used by the administrators to connect to systems in
> both segments. The router was a virtual machine running CentOS to route
> traffic between several network interfaces based on predefined rules.
> 
> According to the evidence collected, the attackers scanned the router’s ports
> and detected a Webmin interface. Next, the attackers logged in to the web
> interface using a privileged root account. It’s unknown how the attackers were
> able to obtain the credentials for that account, but it’s possible the credentials
> were saved in one of the infected system’s browser password managers.
> 
> 
> By gaining access to the configuration panel the attackers configured the
> Apache web server and started using the router as a proxy server between the
> organization’s corporate and restricted segments


This is a rather good writeup that happens to include a favorite pattern of mine.  The so called "airgap", which is only configured in software, allows the administrators to access both sides, and has a router implementing the airgap that is running Webmin.

If you have a protected network, like the "restricted network" in this example, you need to ensure that the administration of that network is done from appropriately isolated machines as well, and that any administration of the network management layer is just as protected as the restricted network itself.


## [The RedMonk Programming Language Rankings: January 2021 – tecosystems](https://redmonk.com/sogrady/2021/03/01/language-rankings-1-21/?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+tecosystems+%28tecosystems%29)

[https://redmonk.com/sogrady/2021/03/01/language-rankings-1-21/?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+tecosystems+%28tecosystems%29](https://redmonk.com/sogrady/2021/03/01/language-rankings-1-21/?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+tecosystems+%28tecosystems%29)

> Ruby (-2): Ruby, as discussed in this space previously, has been in a long term downward if gentle trajectory. This quarter’s run, however, raises questions as to how gentle it will continue to be. When we started doing these rankings in 2012, Ruby was the fifth most popular language we ranked, and for about five years it was able to maintain that status. Since 2016, however, Ruby has been gradually slipping, and this quarter it was passed by both CSS (yes, we know many of you don’t believe it should be ranked) and the aforementioned TypeScript. Ruby has made an effort in recent years to address some of its performance issues, but setting aside that there are questions about what was claimed versus what has been achieved, the focus on performance does not appear to have changed the language’s fortunes as measured by our rankings in any material fashion. To be clear, there are dozens if not hundreds of languages that would happily change places with the ninth ranked language on these rankings, but it’s less the actual placing here than the trajectory that should concern Ruby advocates and users. It’s a lovely language with a beautiful syntax, but that has not been enough in a highly competitive language marketplace.
> 
> Go (-1): Like Ruby, Go’s ranking is less of a concern than its overall trajectory. After an initial period of rapid growth, peaking with its #14 ranking in 2018, Go has been a language that is at best static and arguably on a decline path. As has been discussed previously, some of this is explained by Go’s much more narrow addressable market relative to some of the other languages on this list. It also has not helped Go that Java, a primary competitor for back end application composition, has remained a vital and highly used language instead of fading away after so many years of service. But whether it’s static or in decline, if Go has ambitions to be a true industry force, some change in its path and structure is probably necessary.


I love a good nerdy write up, and RedMonk's language ranking is something I always try to check out.

What interests me here is the gradual and increasing decline in Ruby, which matches my experiences, and the gradual decline in Go, which does not.

The fact that the audience for Go is limited, as it's seen as a fast, low level language, and used by DevOps people for their tooling.  But that's actually a tiny, if vocal, community compared to the vast majority of "enterprise software development".

Should you let these rankings make a decision about what language to write your systems in?  Probably not, local ability to hire, skilled competence within your existing team, and "fit" are probably better indicators, but watching this for languages can tell you whether you should be using a language as one of your core ones, or whether you need to encourage tests of alternative languages and ecosystems in your teams.


## [Trojan Spyware and BEC Attacks](https://blog.sucuri.net/2021/03/trojan-spyware-and-bec-attacks.html)

[https://blog.sucuri.net/2021/03/trojan-spyware-and-bec-attacks.html](https://blog.sucuri.net/2021/03/trojan-spyware-and-bec-attacks.html)

> What’s especially interesting is that it seems that the attacker infected his own device, possibly for testing or troubleshooting purposes, but never actually removed the malware — so screenshots of their own device were also being sent back to the C2 server! This is a big failure in their operational security as it gives us direct insight into some of the attacker’s tactics and operation.
> 
> The following screenshot shows us a BEC email originally titled REQUEST FOR PAYMENT in the Sent folder. The email contents include a request for payment to the bank details provided in the attachment. Payments are for two invoices — together they total over $52,000 USD, so it is easy to see why attackers find it worthwhile to infect devices and monitor them for BEC opportunities.
> 
> And how do we know it is the attacker? We also found a screenshot of their Discord chat with a fellow attacker, where they discuss losing access to the C2 panel due to someone (likely the website owner) deleting files.


Business Email Compromise (BEC) is still a huge issue, although a recent report pointed it out as being far more of an issue in North America than Europe but didn't explain why.

Anyway, the thought that these phishers just send out tens of thousands of spam emails hoping to get a "fool" on the other end is a pervasive one.  But this shows how BEC attackers can also be canny, and actively seek to gather data from potential victims, conducting research to learn what language to use and what times are best to attack the users.

Oh, and just for fun, they also infected their own computer and uploaded images to their central store of their own computer.  Opsec fail for this particular hacker.


