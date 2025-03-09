---
title: "183 - Does it matter who your adversary is?"
date: 2022-02-06
description: "There's a lot of emphasis in threat intelligence about understanding our adversaries."
permalink: /does-it-matter-who-your-adversary-is/
---

There's a lot of emphasis in threat intelligence about understanding our adversaries.

We name them, with threat intel companies competing for the most memorable names in a theme, from Microsoft's rare elements like Phosphorus, Strontium, Nobelium and Barium, to CrowdStrikes famous animals, like Cozy Bear, Charming Kitten, Cobalt Spider and Stone Panda, or FireEye Mandiant's rather more prosaic APT1, APT28 and UNC2452.

With these threat reports, we get details of how the group operates, the kinds of techniques that they use, and ways to detect their specific behaviour.

But does it really matter?  

The current Ukraine/Russia situation has just thrown up another media darling, the False Flag operation.  Often somewhat wrongly attributed to pirates flying flags of another nation before attacking in order to confuse their target and gain the element of surprise.

False flag operations make for brilliant fiction. TV, Movies and Novels constantly tell us that the good guys will believe that the wrong person did the deed.  That's because the dramatic 3 arc story requires a turning point that you feel you should have seen coming, makes sense in retrospect, but comes as a bit of a surprise.  They're also easy to pull where where the only thing you can trust, the narrator or camera can show you details that lead you to make wrong conclusions can make the lie really believable.

In real life, I suspect that the operational cost of implementing all of the camouflage needed to do it well make it not worth it in a lot of cases.  In real life, you can look at any and all details of a situation, not just what the camera or narrator shows you.  It means that you are far more likely to see issues or differences in the camouflage that doesn't make sense and gives the attribution itself a low confidence.

Instead actors often seem to rely on ambiguity and that fact that most people don't care who conducted a cyber operation against them.

That's right, most defenders don't really care who is attacking them.

Because as a defender, you don't care whether the person who just broke into your network is a chinese student working for their government, or a independent american security researcher, working late at night to find a vulnerability.  What you care is that someone broke into your network.

You might care a bit when working out the impact of what they did, because the intent they had, whether espionage, further access, research or just plain economic theft will all change the way you look at the data you lost and the things they did.  But you probably care about the category of intent most of all, rather than specifics.

Of course, attribution and finger pointing creates all the exciting headlines, and we all love to read a story about this stuff, but as a defender, try not to worry too much about exactly who is getting into your system.  If you can worry about anything, worry about how they are getting into your system, because as you can see below, the espionage actor of today might also be the ransomware actor of tomorrow.

> Editors note:  I really wanted to cover the [US OMB memo on zero trust](https://www.whitehouse.gov/wp-content/uploads/2022/01/M-22-09.pdf), that you'll see below, more this week.  It's well worth a read and I think it's a standout piece of strategy released by the US Government.  Sadly I had lots and lots of links about attribution this week, so I've focused on that, but expect a Zero trust issue next week.  In the teamtime, give that memo a read and think what the implications would be for your organisation if your bosses could send out a memo like that.

## [U.S. to allege Russian plot to stage attack as pretext for Ukraine invasion - The Washington Post](https://www.washingtonpost.com/national-security/2022/02/03/russia-ukraine-staged-attack/)

[https://www.washingtonpost.com/national-security/2022/02/03/russia-ukraine-staged-attack/](https://www.washingtonpost.com/national-security/2022/02/03/russia-ukraine-staged-attack/)

> Russia has already recruited the people who would be involved in the fabricated attack video, and Russian intelligence is intimately involved in the effort, a senior Biden administration official said, speaking on the condition of anonymity under rules set by the administration.
> 
> “We believe that Russia would produce a very graphic propaganda video, which would include corpses and actors that would be depicting mourners and images of destroyed locations, as well as military equipment at the hands of Ukraine or the West, even to the point where some of this equipment would be made to look like it was Western-supplied,” Defense Department press secretary John Kirby said Thursday during a briefing at the Pentagon.
> 
> The Russian disinformation effort would be “right out of their playbook,” Kirby said, noting that most activity of that nature is approved at the highest levels of the Russian government. Kirby said the Biden administration felt it was important, upon learning of such plans, “to call it out.”
> 
> The allegations by the Biden administration were met with pushback due to the lack of specificity and evidence. At a briefing, State Department spokesman Ned Price was asked repeatedly if the United States would provide evidence supporting the alleged Russian plot. He declined to do so, citing the need to protect intelligence sources and methods.
> 
> When asked about the level of confidence Washington has in the information, Price said that “this is derived from intelligence in which we have confidence … otherwise we would not be making it public in the way we are.” He said the United States does not know if the Russians will use the alleged video but that the U.S. disclosure was designed to prevent it from happening.


This is a fascinating play from the Americans here.  

If we assume for a second that this is a true accusation, then the US is exposing it's sources and methods, indicating that it knows what Russia is planning.  

Normal intelligence and espionage tactics when you have an access like this is to avoid exposing it, because the value of unknown intelligence tomorrow is almost always perceived as greater than the known intelligence today.

However. by making this statement, which of course the Russians denied, the Americans have setup a diplomatic play, in essence making it impossible for Russia to use a fabricated attack video.  It doesn't matter whether the source is real or not, any effort by Russia to show a video now will be met with disbelief since it will match the narrative that the US has set out.

The US clearly feels that denying this ability for escalation to be worth the cost of burning sources and methods.

However, even more interesting was the reaction of US journalists who questioned the truth of the allegations, and pushed back on the briefing.  The continuing distrust between citizen and state in the US means that unsubstantiated claims are not well liked or appreciated.  Of course, getting the US people to believe the story may not have been the aim, by publicising it, the US has constrained the choices of the Russian government anyway, so they might consider this a win.


## [Wiper in Ukraine Used Code Repurposed From WhiteBlackCrypt Ransomware](https://zetter.substack.com/p/wiper-in-ukraine-used-code-repurposed)

[https://zetter.substack.com/p/wiper-in-ukraine-used-code-repurposed](https://zetter.substack.com/p/wiper-in-ukraine-used-code-repurposed)

> The code used in the WhisperGate wiper that targeted government agencies in Ukraine this month was re-purposed from a ransomware campaign that targeted Russian victims last year, according to Ukrainian investigators who analyzed the code.
> 
> The WhisperGate wiper masqueraded as ransomware while performing its real purpose — to destroy files on dozens of systems in two Ukrainian government agencies in order to render those systems inoperable.
> 
> Now it appears that the WhisperGate code was modified code from a different faux ransomware campaign discovered last year called WhiteBlackCrypt. Like WhisperGate, WhiteBlackCrypt masqueraded as ransomware but actually had a wiper component to erase systems. It targeted Russian victims says Victor Zhora, deputy director of Ukraine's State Services for Special Communication and Information Protection, which published an announcement about the new findings today.
> 
> Zhora says the actors behind WhisperGate may have used the WhiteBlackCrypt code in an attempt to falsely point the finger at Ukraine — that is, to make it appear that Ukraine was itself responsible for the infections that destroyed its government systems this month.
> 
> “They simply modified the WhiteBlackCrypt malware that was used in a provocative fashion against Russia two years ago,” says Zhora, “and the idea was to potentially attribute the [WhisperGate] wiper to Ukrainians.”


Who wrote the code that did the deed?  Who deployed it?  Who was there to benefit?

The question about the who matters in the world of foreign policy, but to the defenders on the network probably doesn't matter too much


## [PowerLess Trojan: Iranian APT Phosphorus Adds New PowerShell Backdoor for Espionage](https://www.cybereason.com/blog/powerless-trojan-iranian-apt-phosphorus-adds-new-powershell-backdoor-for-espionage)

[https://www.cybereason.com/blog/powerless-trojan-iranian-apt-phosphorus-adds-new-powershell-backdoor-for-espionage](https://www.cybereason.com/blog/powerless-trojan-iranian-apt-phosphorus-adds-new-powershell-backdoor-for-espionage)

> Over the past months, the Cybereason Nocturnus Team observed an uptick in the activity of the Iranian attributed group dubbed Phosphorus (AKA Charming Kitten, APT35), known for previously attacking medical research organizations in the US and Israel in late 2020, and for targeting academic researchers from the US, France, and the Middle East region back in 2019.
> 
> [...]
> 
> Cybereason researchers recently discovered a new set of tools which were developed by the Phosphorus group and incorporated into their arsenal, including a novel PowerShell backdoor dubbed PowerLess Backdoor. Our research also highlights a stealthy technique used by the group to avoid PowerShell detection by running the PowerShell Backdoor in a .NET context rather than spawning the PowerShell process.
> 
> In addition, several interesting connections were found between the Phosphorus group and the Memento Ransomware that first emerged in late 2021.


This is an interesting connection drawn out here.  Phosphorus or Charming Kitten have generally been tagged as an espionage actor, seeking to conduct politically motivated cyber activities.

Connecting them with Ransomware suggests that the actor is using the same infrastructure for their espionage work as their ransomware work which is something that one might imagine espionage groups would try to avoid where possible.

Ransomware is normally a purely economic activity, designed to gather funds, although as I've said before, if someone can run executable code on your machines, they can do almost anything.

It's interesting to theorise therefore about why this actor might be conducting ransomware campaigns and why from the same infrastructure. Whether it's to gain disguised funding for their activities, whether it's personal gain by individuals misusing their capabilities, or whether it's part of a wider state campaign that hides the real goal.  We'll almost certainly never know the reality.


## [Threat Assessment: BlackCat Ransomware](https://unit42.paloaltonetworks.com/blackcat-ransomware/)

[https://unit42.paloaltonetworks.com/blackcat-ransomware/](https://unit42.paloaltonetworks.com/blackcat-ransomware/)

> BlackCat (aka ALPHV) is a ransomware family that surfaced in mid-November 2021 and quickly gained notoriety for its sophistication and innovation. Operating a ransomware-as-a-service (RaaS) business model, BlackCat was observed soliciting for affiliates in known cybercrime forums, offering to allow affiliates to leverage the ransomware and keep 80-90% of the ransom payment. The remainder would be paid to the BlackCat author.
> 
> BlackCat has taken an aggressive approach to naming and shaming victims, listing more than a dozen on their leak site in a little over a month. The largest number of the group’s victims so far are U.S. organizations, but BlackCat and its affiliates have also attacked organizations in Europe, the Philippines and other locations. Victims include organizations in the following sectors: construction and engineering, retail, transportation, commercial services, insurance, machinery, professional services, telecommunication, auto components and pharmaceuticals.
> 
> Use of BlackCat ransomware has grown quickly for a variety of reasons (for comparison, AvosLocker had only listed a handful of victims publicly within two months of becoming known). Effective marketing to affiliates is a likely factor – in addition to offering an enticing share of ransom payments, the group has solicited affiliates by posting ads on forums such as Ransomware Anonymous Market Place (RAMP).
> 
> The malware itself is coded in the Rust programming language. Though this is not the first piece of malware to use Rust, it is one of the first, if not the first, piece of ransomware to use it. By leveraging this programming language, the malware authors are able to easily compile it against various operating system architectures. Given its numerous native options, Rust is highly customizable, which facilitates the ability to pivot and individualize attacks
> 
> [...]
> 
> Hardcoded credentials stored within the BlackCat ransomware config lend credence to the likelihood that specific victims are being targeted. The credentials also allow BlackCat to move laterally within the victim’s system and/or network, often with administrative privileges. Credential access permits the ransomware to deploy additional tools that further propagate the attack. These observations have also been confirmed by Symantec.


A new ransomware as a service group that is growing and growing rapidly.

The use of Rust shows a high level of technical proficiency, and the highly customisable nature of the ransomware itself will make it much harder for signature based detection to effectively detect it and mitigate it.

The fact that it has hardcoded credentials in samples seems to suggest that each sample is being created for each specific victim.  That also suggests that it's not a first stage attack, someone must already have access to your system and the relevant credentials in order to use it effectively.

One to watch


## [Deadbolt ransomware hits more than 3,600 QNAP NAS devices - The Record by Recorded Future](https://therecord.media/deadbolt-ransomware-hits-more-than-3600-qnap-nas-devices/)

[https://therecord.media/deadbolt-ransomware-hits-more-than-3600-qnap-nas-devices/](https://therecord.media/deadbolt-ransomware-hits-more-than-3600-qnap-nas-devices/)

> More than 3,600 network-attached storage (NAS) devices from Taiwanese company QNAP have been infected and had their data encrypted by a new strain of ransomware named Deadbolt.
> 
> Devices attacked by the Deadbolt gang are easy to recognize because the login screen is typically replaced with a ransom note, and local files are encrypted and renamed with a .deadbolt extension.
> 
> The threat actor behind the attacks is extorting not only the owners of the NAS devices but also the QNAP company itself.
> 
> According to a copy of the ransom note, device owners are told to pay 0.03 Bitcoin ($1,100) to receive a decryption key to unlock their files, while in an second note, the hackers demand 5 Bitcoin ($1.86 million) from QNAP to reveal details about the supposed zero-day vulnerability they have been using to attack its users, and another 50 Bitcoin ($18.6 million) to release a master decryption key that unlock all of the victims’ files.


This triple extortion method feels fairly new.  Extort individuals for the return of their data, attempt to extort a "bounty" from the affected company so they can prevent further infections, and finally offer a master decryption key.

Sadly, most of the advice I saw online was generally security professionals asking why people have their NAS exposed to the outsdie world, whereas normal users are of course naturally responding with "Because it's network attached storage, and I'm not always at home".

As more and more household devices try to offer you internet connected capabilities, enabling you to remotely call your car, change the heating before you get home, or see your CCTV and Alarms while you are out, they are all going to need to be exposed to the internet somehow.

Since the use of personal VPN's is complex to setup, and not consistent across households, it's difficult to imagine anything other than exposing these services to the internet in the near future.

Personally, I've been using [Tailscale](https://tailscale.com/) to solve some of this problem, but that's a solution that only partially works for a very niche set of nerdy customers, and QNAP has made a good business of selling these NAS devices to a much wider audience.


## [Moving the U.S. Government Toward Zero Trust Cybersecurity Principles [pdf]](https://www.whitehouse.gov/wp-content/uploads/2022/01/M-22-09.pdf)

[https://www.whitehouse.gov/wp-content/uploads/2022/01/M-22-09.pdf](https://www.whitehouse.gov/wp-content/uploads/2022/01/M-22-09.pdf)

> A transition to a “zero trust” approach to security provides a defensible architecture for this new environment. As described in the Department of Defense Zero Trust Reference Architecture,
> “The foundational tenet of the Zero Trust Model is that no actor, system, network, or service operating outside or within the security perimeter is trusted. Instead, we must verify anything and everything attempting to establish access. It is a dramatic paradigm shift in philosophy of how we secure our infrastructure, networks, and data, from verify once at the perimeter to continual verification of each user, device, application, and transaction.”
> 
> This strategy envisions a Federal Government where:
> 
> * Federal staff have enterprise-managed accounts, allowing them to access everything they
> need to do their job while remaining reliably protected from even targeted, sophisticated
> phishing attacks.
> * The devices that Federal staff use to do their jobs are consistently tracked and monitored,
> and the security posture of those devices is taken into account when granting access to
> internal resources.
> * Agency systems are isolated from each other, and the network traffic flowing between
> and within them is reliably encrypted.
> * Enterprise applications are tested internally and externally, and can be made available to
> staff securely over the internet.
> * Federal security teams and data teams work together to develop data categories and
> security rules to automatically detect and ultimately block unauthorized access to
> sensitive information.
> 
> [...]
> 
> Further, Federal applications cannot rely on network perimeter protections to guard against unauthorized access. Users should log into applications, rather than networks, and enterprise applications should eventually be able to be used over the public internet. In the nearterm, every application should be treated as internet-accessible from a security perspective.
> 
> [...]
> 
> 1. Agencies must employ centralized identity management systems for agency users that can be integrated into applications and common platforms.
> 2. Agencies must use strong MFA throughout their enterprise.
> 
> * MFA must be enforced at the application layer, instead of the network layer.
> * For agency staff, contractors, and partners, phishing-resistant MFA is required.
> * For public users, phishing-resistant MFA must be an option.
> * Password policies must not require use of special characters or regular rotation
> 
> [...]
> 
> 1. Agencies must resolve DNS queries using encrypted DNS wherever it is technically supported.
> 2. Agencies must enforce HTTPS for all web and application program interface (API) traffic in their environment.
> 
> * Agencies must work with CISA to “preload” their .gov domains into web browsers as only accessible over HTTPS


This memo is a really big step, and one that I'll be really curious to see how US Federal departments respond. 

What they are asking is that departments must use internet accessible tools, central identity systems and internet era technologies.

Some of these departments are still running mainframes, and many are running 1990's era technology stacks using Java Enterprise Edition.  Updating those systems to use modern federated identity standards, to take device signals and to use encrypted DNS is no trivial matter, especially if the design, operation and management of those systems is outsourced to third party suppliers.

But the vision that they are setting out here is absolutely the right one for Government, and it's quite exciting to watch CISA drastically attempt to modernise the US Federal Government.

If you don't read anything else this week, read this one.


## [Writing and shipping code faster | The State of the Octoverse](https://octoverse.github.com/writing-code-faster/#reusing-code-without-the-friction)

[https://octoverse.github.com/writing-code-faster/#reusing-code-without-the-friction](https://octoverse.github.com/writing-code-faster/#reusing-code-without-the-friction)

> Frictionless code reuse makes developers more efficient and productive
> In GitHub’s open source community, projects built with code and toolchains from the community are thriving. We build better together and help each other grow stronger. Communities such as Docker rely on tens of thousands of repositories, hundreds of thousands of contributors, and draw from hundreds of countries and regions.
> 
> What the data shows: Entitlement procedures, access restrictions, or information fragmentation can introduce friction that discourages developers from reusing code. However, developers’ performance at work can increase by up to 87% when reusing others’ code is easy and doesn’t introduce friction. The benefits of frictionless code reuse are striking for open source projects too --projects see 2x performance compared to those with more friction, like slow processes or multiple approval layers.


The [State of the Octoverse (pdf)](https://octoverse.github.com/static/octoverse-report-2021.pdf) has all of this data in an easy to read form.

There's always an issue with the data on Github use, because we see people using Github professionally, as part of a community project, as well as for personal projects, and these all have different processes around them, but Github has segmented the data to ensure that they can talk about the impact in different communities.

As expected, organisations and groups that invest heavily in automation gain massive productivity gains.  That's useful data for those of you trying to get automation and developer experience teams funded


## [Azure DDoS Protection—2021 Q3 and Q4 DDoS attack trends | Azure Blog and Updates | Microsoft Azure](https://azure.microsoft.com/en-us/blog/azure-ddos-protection-2021-q3-and-q4-ddos-attack-trends/)

[https://azure.microsoft.com/en-us/blog/azure-ddos-protection-2021-q3-and-q4-ddos-attack-trends/](https://azure.microsoft.com/en-us/blog/azure-ddos-protection-2021-q3-and-q4-ddos-attack-trends/)

> Microsoft mitigated a 3.47 Tbps attack, and two more attacks above 2.5 Tbps
> Last October, Microsoft reported on a 2.4 terabit per second (Tbps) DDoS attack in Azure that we successfully mitigated. Since then, we have mitigated three larger attacks.
> 
> In November, Microsoft mitigated a DDoS attack with a throughput of 3.47 Tbps and a packet rate of 340 million packets per second (pps), targeting an Azure customer in Asia. We believe this to be the largest attack ever reported in history.
> 
> This was a distributed attack originating from approximately 10,000 sources and from multiple countries across the globe, including the United States, China, South Korea, Russia, Thailand, India, Vietnam, Iran, Indonesia, and Taiwan. Attack vectors were UDP reflection on port 80 using Simple Service Discovery Protocol (SSDP), Connection-less Lightweight Directory Access Protocol (CLDAP), Domain Name System (DNS), and Network Time Protocol (NTP) comprising one single peak, and the overall attack lasted approximately 15 minutes.


As a reminder, DDOS protection tends to come as standard with most cloud providers.  If you are using a hyperscale cloud provider, then you are more secure against these DDOS attacks, especially this sort of low level layer 3 style DDOS attack.

Do, however, check that you've got it turned on, that your architecture uses the right features, and of course, set billing alarms and limits, because with a cloud supplier, it's now possible to DDOS your credit card instead if you aren't careful.


## [Cyber Risk & Security Guidance for Non-Executive Directors [pdf]](https://research.nccgroup.com/wp-content/uploads/2021/11/eBook_Cyber-Risk-Security-Guidance-for-Non-Exec-Directors-Lowres.pdf)

[https://research.nccgroup.com/wp-content/uploads/2021/11/eBook_Cyber-Risk-Security-Guidance-for-Non-Exec-Directors-Lowres.pdf](https://research.nccgroup.com/wp-content/uploads/2021/11/eBook_Cyber-Risk-Security-Guidance-for-Non-Exec-Directors-Lowres.pdf)

> Cyber security and resilience is a topic that all boards need to contend with due to the impact on governance and legal
> obligations. Empowering non-executive directors with the knowledge, vocabulary and questions to ensure that organisations
> have appropriate oversight and posture relevant to the threats they face is critical for good corporate governance in the 21st
> century.


Non executive directors are there to help hold your company to account.  But if they don't understand cybersecurity, then they are not able to do so.  This handy and small introductory guide from NCC group can help facilitate a teach in or learning session for non-exec directors to help them get to grips with the complexities of cyber security


## [North Korea Hacked Him. So He Took Down Its Internet | WIRED](https://www.wired.com/story/north-korea-hacker-internet-outage/)

[https://www.wired.com/story/north-korea-hacker-internet-outage/](https://www.wired.com/story/north-korea-hacker-internet-outage/)

> At least one of the central routers that allow access to the country's networks appeared at one point to be paralyzed, crippling the Hermit Kingdom's digital connections to the outside world. 
> 
> Some North Korea watchers pointed out that the country had just carried out a series of missile tests, implying that a foreign government's hackers might have launched a cyberattack against the rogue state to tell it to stop saber-rattling. 
> 
> But responsibility for North Korea's ongoing internet outages doesn't lie with US Cyber Command or any other state-sponsored hacking agency. In fact, it was the work of one American man in a T-shirt, pajama pants, and slippers, sitting in his living room night after night, watching Alien movies and eating spicy corn snacks—and periodically walking over to his home office to check on the progress of the programs he was running to disrupt the internet of an entire country.


Fascinating story, and lots of comments about whether it's the right action or not, but again a reminder that the amount of damage a cyber actor can do does not necessarily indicate the amount of resources they have access to


