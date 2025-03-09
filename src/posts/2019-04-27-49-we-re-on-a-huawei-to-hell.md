---
title: "49 - We're on a Huawei to hell"
date: 2019-04-27
description: "I've been up at the NCSC's flagship conference, CyberUK, in Glasgow this week, for which the Huawei decision was a point of conversation.  Mostly it was with a kind of resigned shrug that \"Inevitably someone will mention it\" that introduced the topic in many sessions.  \"A flag of origin is an important factor, but a secondary factor [compared to the technical, security and engineering complexities]\" was a good summary of the view that was espoused both on stage and with the individuals who I ended up speaking with."
permalink: /we-re-on-a-huawei-to-hell/
---

I've been up at the NCSC's flagship conference, CyberUK, in Glasgow this week, for which the Huawei decision was a point of conversation.  Mostly it was with a kind of resigned shrug that "Inevitably someone will mention it" that introduced the topic in many sessions.  "A flag of origin is an important factor, but a secondary factor [compared to the technical, security and engineering complexities]" was a good summary of the view that was espoused both on stage and with the individuals who I ended up speaking with.

I find the obsession with Huawei and the 5g network to be fascinating levels of doublethink by many people.  GCHQ's HCSEC exists to provide technical assurance of telecommunications equipment, and clearly there are a lot of people worried about this stuff, but the reality of our modern world, we can and should be worrying about the supply chain of all hardware (as the infamous Super Micro story by bloomberg highlighted"), or the supply chain of our software (as I write this, news that Docker Hub has had a breach has pinged past me).  This obsession with flag of origin really does belie the real complexities of the situation and the complexities of the geopolitics at play.

One of the most interesting statements at CyberUK to me was in the last session of the conference, in the Future Threats session.  An audience member asked the question whether the centralisation of hosting onto a small number of cloud providers was going to create a huge risk.  The answer, from Kris McConkey, Threat Detection & Response Lead Partner at PwC, was that the major cloud providers had some of the best security engineers in the world, and that they had built systems that were far more secure than any previous generation of hosting environments.  Kris pointed out that our telecommunication providers had some of the oldest and nastiest legacy systems in the world, and that we should be far more worried about the security of those companies than the modern cloud companies.  

The risks in cloud come not from the cloud environments themselves, but from how we use cloud environments, from poor password hygiene, lack of second factors and poor cloud security capabilities.  We are still shockingly bad at agreeing the basics of being a secure user of cloud computing, primarily because the term cloud computing is so vague as to not mean anything, but also because too many people were sold the idea that the cloud is just someone else's datacenter, and we know how to secure a network in someone else's data center.

## [The FBI Wanted a Backdoor to the iPhone. Tim Cook Said No | WIRED](https://www.wired.com/story/the-time-tim-cook-stood-his-ground-against-fbi/)

[https://www.wired.com/story/the-time-tim-cook-stood-his-ground-against-fbi/](https://www.wired.com/story/the-time-tim-cook-stood-his-ground-against-fbi/)

> The writ “was not a simple request for assistance in a criminal case,” explained Sewell. “It was a forty-two-page pleading by the government that started out with this litany of the horrible things that had been done in San Bernardino. And then this . . . somewhat biased litany of all the times that Apple had said no to what were portrayed as very reasonable requests. So this was what, in the law, we call a speaking complaint. It was meant to from day one tell a story . . . that would get the public against Apple.”
> 
> The team came to the conclusion that the judge’s order was a PR move—a very public arm twisting to pressure Apple into complying with the FBI’s demands—and that it could be serious trouble for the company. Apple “is a famous, incredibly powerful consumer brand and we are going to be standing up against the FBI and saying in effect, ‘No, we’re not going to give you the thing that you’re looking for to try to deal with this terrorist threat,’” said Sewell.
> 
> [...]
> 
> It was later widely reported that the FBI had gained access to Farook’s iPhone with the help of Israeli phone forensics company Cellebrite, but the company denied its involvement. The identities of the professional hackers who ultimately broke into the phone have yet to become public. At a Senate Judiciary hearing in May, Senator Dianne Feinstein revealed that it had cost the FBI $900,000. Officials had previously admitted that the FBI didn’t find any information they didn’t already have, and no evidence of contacts with ISIS or other supporters.


Law enforcement wants the ability to conduct searches on devices, and the role of device manufacters in this process is a difficult one.  The fact that this was waged as a public PR campaign against Apple, with quotes of just how important it would be in "just one case" is of course entirely belied by the fact that in the end, the device contained no information of help.

This is true in all warrants, the point of a warrant is that you have suspicion of a crime, and would like to find proof, but that produces the possibility that there is no proof because your suspicion is unfounded.  I think we need to remember that whenever this debate happens in public, because often the sides pushing for more investigatory powers imply that this will only impact criminals.


## [AWS Security Maturity Roadmap [pdf]](https://summitroute.com/downloads/aws_security_maturity_roadmap-Summit_Route_2019.pdf)

[https://summitroute.com/downloads/aws_security_maturity_roadmap-Summit_Route_2019.pdf](https://summitroute.com/downloads/aws_security_maturity_roadmap-Summit_Route_2019.pdf)

> In this section I’ve grouped security goals into stages that somewhat build on each other. These are the steps to take your company from having no cloud security program for AWS to having a solid program. You may find you do some of these steps in a different order, partially complete steps for some accounts before others, or have to go back and make slight adjustments, but this should help give you a roadmap for making progress.


Covering 10 stages: Inventory, Backups, Visibility, Detection, IAM, Network, Reproducibility, Enforcement, Advanced steps and Incident management.  This is a good baseline for AWS security.  There's a few things in here that I'd quibble with, I'd drop a few of these, but suggest that the rest should simply form your baseline for all AWS systems because these will prevent the vast majority of untargeted attacks on your AWS infrastructure, freeing you up to concentrate on the more targeted, more complex attacks.



## [Hackers Could Read Your Hotmail, MSN, and Outlook Emails by Abusing Microsoft Support - Motherboard](https://motherboard.vice.com/en_us/article/ywyz3x/hackers-could-read-your-hotmail-msn-outlook-microsoft-customer-support)

[https://motherboard.vice.com/en_us/article/ywyz3x/hackers-could-read-your-hotmail-msn-outlook-microsoft-customer-support](https://motherboard.vice.com/en_us/article/ywyz3x/hackers-could-read-your-hotmail-msn-outlook-microsoft-customer-support)

> In its breach notification email, Microsoft said it immediately disabled the compromised customer support account once the company discovered the issue. The source said Microsoft noticed the attack at the end of March, and that hackers had access for at least six months. Microsoft pushed back against this, and pointed to its notification email which gave a timeframe between January 1st and March 28th.
> 
> The source said this access had been used as part of so-called iCloud unlocks, where hackers will compromise a target’s email or iCloud account in order to remove Activation Lock from their iPhone. This is an Apple security feature that stops thieves from factory resetting stolen devices and selling them on.


This statement snuck at the end of this article indicates the probable aim of this hack.  Long term access to a customer support account in order to enable the theft of 2FA tokens or reset links, which enables a further form of crime, the theft and reset of iPhone accounts, as well, potentially as access to things like iCloud photos or who knows what.

There's defintely something around jigsaw identification here, is it possible for Microsoft to coordinate with Apple to identify accounts that were compromised that indicates a further compromise of say the Apple ecosystem?  I doubt that end users will think to check their other accounts that this email protected and therefore the attacker might still have access.  Especially if they were essentially renting the compromise out to third parties.


## [A look inside the FBI's 2018 IC3 online crime report - Malwarebytes Labs | Malwarebytes Labs](https://blog.malwarebytes.com/cybercrime/2019/04/a-look-inside-the-fbis-2018-ic3-online-crime-report/)

[https://blog.malwarebytes.com/cybercrime/2019/04/a-look-inside-the-fbis-2018-ic3-online-crime-report/](https://blog.malwarebytes.com/cybercrime/2019/04/a-look-inside-the-fbis-2018-ic3-online-crime-report/)

> One slightly peculiar twist to the usual “steal your money” approach is this:
> 
> In 2018, the IC3 received an increase in the number of BEC/EAC complaints requesting victims purchase gift cards. The victims received a spoofed email, a spoofed phone call or a spoofed text from a person in authority requesting the victim purchase multiple gift cards for either personal or business reasons.
> 
> Not quite as glamorous as Hong Kong wires, and in all honesty it sounds faintly ludicrous at first viewing, but it’s definitely working for somebody.


This is fairly common in the US as far as I can tell.  Organisational admins told to go buy gift cards for the staff, scratch off the back and send the number by email back to the sender.

Gift cards seem to enable a pretty strong form of money laundering, and so this works quite effectively.  I can only assume that this is also fairly common for giving out staff rewards, which is why it works so well.


## [Students face prison for being criminal 'money mules': top garda - Independent.ie](https://www.independent.ie/business/technology/students-face-prison-for-being-criminal-money-mules-top-garda-38048859.html)

[https://www.independent.ie/business/technology/students-face-prison-for-being-criminal-money-mules-top-garda-38048859.html](https://www.independent.ie/business/technology/students-face-prison-for-being-criminal-money-mules-top-garda-38048859.html)

> "What happens is that someone approaches a student and says 'a friend of mine wants to invest here in Ireland, but it's taking a while to get past the red tape, so I'll pay you €500 to use your account'," said the senior officer.
> 
> The fraudster then wires illicit cash into the account before getting the student to take it out or move it on to a further account.


This type of money muling has been around for years.  It's a very handy way of getting money bounced through lots of accounts in a way that makes it harder to trace, and more importantly, if anything goes wrong, the poor student is the one who gets investigated rather than the criminal.


## [A 'Blockchain Bandit' Is Guessing Private Keys and Scoring Millions | WIRED](https://www.wired.com/story/blockchain-bandit-ethereum-weak-private-keys/)

[https://www.wired.com/story/blockchain-bandit-ethereum-weak-private-keys/](https://www.wired.com/story/blockchain-bandit-ethereum-weak-private-keys/)

> Bednarek tried putting a dollar's worth of ether into a weak key address that the thief had previously emptied. Within seconds, it was snatched up and transferred to the bandit's account. Bednarek then tried putting a dollar into a new, previously unused weak key address. It, too, was emptied in seconds, this time transferred into an account that held just a few thousand dollars worth of ether. But Bednarek could see in the pending transactions on the Ethereum blockchain that the more successful ether bandit had attempted to grab it as well. Someone had beaten him to it by mere milliseconds. The thieves seemed to have a vast, pre-generated list of keys, and were scanning them with inhuman, automated speed.
> 
> In fact, when the researchers looked at the history of the blockchain bandit's account on the Ethereum ledger, it had pulled in ether from thousands of addresses over the last three years without ever moving any out—money movements Bednarek believes were likely automated ethercombing thefts.


This was a neat idea, trying out a subset of the potential cryptographic keys which are the easy to create or guess keys.  Unfortunately someone had already thought of this and was stealing the money, transferring it to their own accounts.  However, despite something continuing to run, monitoring those broken private wallets, they still don't seem to have worked out how to spend the ethereum that they've stolen.  Cashing out untraceably is still the hardest part of any online crime


## [United States of America v Marcus Hutchins [pdf]](https://www.courtlistener.com/recap/gov.uscourts.wied.77855/gov.uscourts.wied.77855.124.0.pdf)

[https://www.courtlistener.com/recap/gov.uscourts.wied.77855/gov.uscourts.wied.77855.124.0.pdf](https://www.courtlistener.com/recap/gov.uscourts.wied.77855/gov.uscourts.wied.77855.124.0.pdf)

> Between July 2012 and September 2016, Marcus Hutchins helped create and, in partnership with another, sell malicious computer code, a/k/a malware, known as UPAS-Kit and Kronos,' During this time, Hutchins used aliases such as "Malwaretech" and "irp@jabber.se."


There's been a fair amount of chatter on twitter about how many security researchers did borderline (or completely) illegal things when they were young and just learning because that was the only way to learn in the 90s.  It's worth noting that [Marcus's online apology](https://www.malwaretech.com/public-statement) says "Having grown up, I’ve since been using the same skills that I misused several years ago for constructive purposes".  But he was still writing this malware back in 2016.  This pushes the "I was young and stupid" defence a little in my opinion.  Marcus was 23 in 2017 so he's certainly old enough to be aware of what he was doing at that point.

The next big question will be whether the US decides to try to make an example of him, as a deterrent to other "young misguided hackers" or whether they decide that actually, it wasn't that big a deal after all.  We'll have to wait a bit for sentencing to happen to find out what the judge decides to do.


## [Foreign Economic Espionage in Cyberspace 2018 [pdf]](https://www.dni.gov/files/NCSC/documents/news/20180724-economic-espionage-pub.pdf)

[https://www.dni.gov/files/NCSC/documents/news/20180724-economic-espionage-pub.pdf](https://www.dni.gov/files/NCSC/documents/news/20180724-economic-espionage-pub.pdf)

> Foreign intelligence services—and threat actors working on their behalf—continue to represent the most persistent and pervasive cyber intelligence threat. China, Russia, and Iran stand out as three of the most capable and active cyber actors tied to economic espionage and the potential theft of U.S. trade secrets and proprietary information. Countries with closer ties to the United States have also conducted cyber espionage to obtain U.S. technology. Despite advances in cybersecurity, cyber espionage continues to offer threat actors a relatively low-cost, high-yield avenue of approach to a wide spectrum of intellectual property.


Unlike many other reports that I've read about state level actors in cyberspace, this report isn't about "the spies are reading your email", or "Russia wants to destroy the energy grid", but instead is about specific economic espionage, which is to say, cyber enabled traditional espionage.  That's a very different type of activity, and it's interesting to see what the US thinks.

Some curious things are in this report however. Generally, when you read lots of commercial reports, 4 countries come out as the major players in cyber attacks, Russia, China, Iran and North Korea.  Of those 4, there's been a lot talked about North Korea as an actor conducting financial criminal attacks in order to get money around the trade sanctions that affect the country.  However, this report only lists 3 countries as the primary actors, Russia, China and Iran.  I think this is because the report focuses on economic theft that is "second order", that is to say theft of intellectual property, US trade secrets and military and civilian technologies, all of which are implied to be given to state sponsored firms in order to help them compete on the world stage.  North Korea has generally been accused of being more blatant than that, and doesn't really attempt to compete economically.

Secondly, this report talks about future technologies and the risks that they bring.  It however confuses some of the terms and I suspect that the authors are not technical enough to really understand what cloud computing is, or how it relates to the "Internet of Things".  The claim that the IoT and AI will create billions of unsecured network nodes is an interesting one because it has no real relevance to the economic espionage that they are talking about.

However, there's a small note in here: "The solidification of cloud computing over the past decade as a global information industry standard, coupled with the deployment of technologies such as AI and IoT, will introduce unforeseen vulnerabilities to U.S. networks.", which I think is to suggest that attackers are more easily able to construct deniable operational infrastructure for cyber campaigns and tear it down fairly easily.  This combined with what I've heard repeatedly recently about "AI enabled attackers" clearly worries defenders a lot.


## [Wipro Intruders Targeted Other Major IT Firms — Krebs on Security](https://krebsonsecurity.com/2019/04/wipro-intruders-targeted-other-major-it-firms/)

[https://krebsonsecurity.com/2019/04/wipro-intruders-targeted-other-major-it-firms/](https://krebsonsecurity.com/2019/04/wipro-intruders-targeted-other-major-it-firms/)

> It appears the attackers in this case are targeting companies that in one form or another have access to either a ton of third-party company resources, and/or companies that can be abused to conduct gift card fraud.
> 
> Wednesday’s follow-up on the Wipro breach quoted an anonymous source close to the investigation saying the criminals responsible for breaching Wipro appear to be after anything they can turn into cash fairly quickly. That source, who works for a large U.S. retailer, said the crooks who broke into Wipro used their access to perpetrate gift card fraud at the retailer’s stores.


The WiPro attack looks very similar to [Cloud Hopper](https://www.pwc.co.uk/issues/cyber-security-data-privacy/insights/operation-cloud-hopper.html) which was attributed by the UK and US to China's APT10 group.  Cloud Hopper was a targeted intrusion that used Managed Service Providers networks to reach into their customers networks, and was designed to steal data, perform economic espionage and gather data needed for more targeted operations in the future.

I had originally thought that WiPro would be the same sort of attack, but looking at the reporting, it looks more like it's a breach being conducted by a criminal gang. This looks more like a targeted compromise in order to find cashable targets.  That's good in a certain sense, because it means that it's not yet another APT, on the other hand it far more clearly demonstrates how quickly the gap between nation state activity and well funded hacking group activity is closing.  That might actually be more scary in the long term.


## [Ultimatum to cabinet ministers in Huawei leak investigation | Technology | The Guardian](https://www.theguardian.com/technology/2019/apr/25/may-faces-calls-for-inquiry-over-huawei-leak?CMP=Share_AndroidApp_Copy_to_clipboard)

[https://www.theguardian.com/technology/2019/apr/25/may-faces-calls-for-inquiry-over-huawei-leak?CMP=Share_AndroidApp_Copy_to_clipboard](https://www.theguardian.com/technology/2019/apr/25/may-faces-calls-for-inquiry-over-huawei-leak?CMP=Share_AndroidApp_Copy_to_clipboard)

> Cabinet members who were at Tuesday’s National Security Council (NSC) have been sent an ultimatum by Whitehall’s most powerful official to confess or deny whether they leaked a controversial decision to allow Chinese telecoms firm Huawei to help build the UK’s 5G phone network.
> 
> Cabinet secretary Sir Mark Sedwill is understood to have written to those present and demanded that they told him by 2pm on Thursday whether they were involved and would be willing to cooperate with an inquiry, prompting the five prime suspects to scramble to “categorically deny” that they were behind the leak.
> 
> The move came at an acutely sensitive time as several of those present are hoping to take over as prime minister when Theresa May steps down. There are also growing calls for whoever did leak the information to the Daily Telegraph to be prosecuted under the Official Secrets Act.


The Huawei decision is one that the government needs to take, and GCHQ has been very clear (and I've linked in the past), that they think this is a risk that can be managed appropriately.  The decision by someone here to leak this decision to the press is an interesting one.  One can only assume that they did so because they disapproved of the decision and want public discourse to push against this decision before it was made public and while it can still be changed.

The anger inside Government about this leak is palpable in the reporting on it, but there are some interesting questions about this as a leak.  Why is this leak special? Why are we more bothered about this than say the cabinet leaks around brexit discussions, and what possible steps can actually be taken to find the source of the leak?

The implications of the leak for people who sit on the national security council, about how much they trust the people around the room and how open and frank they are willing to be is probably the most damaging part of this leak in my mind.  Quite what impact that will have over the coming weeks and what will happen?  We'll just have to wait and see.



