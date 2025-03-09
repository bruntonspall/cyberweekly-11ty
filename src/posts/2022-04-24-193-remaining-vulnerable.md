---
title: "193 - Remaining vulnerable"
date: 2022-04-24
description: "How you deal with vulnerabilities is critical to your organisations approach to security."
permalink: /remaining-vulnerable/
---

How you deal with vulnerabilities is critical to your organisations approach to security.

In far too many organisations, there simply isn't any defined vulnerability process.  If someone finds something, it's reliant on the development team or worse, the supplier management team to understand it, prioritise it and put in a change request.  The organisation as a whole has no real understanding of what it runs, and no ability to triage or prioritise vulnerabilities.

But organisations that have setup an appsec team, and has some kind of policy should have a vulnerability disclosure front door of some form.  The really good ones will have a [security.txt](https://securitytxt.org/) that tells researchers who to contact.  The appsec team needs to be able to work out which teams in the organisation are responsible for the software, and to send them work.  But that's really just table stakes for running a major company in 2022, you need to be able to do this to operate on the internet.

Even better teams scan themselves for vulnerabilities, and keep an eye on the vulnerability lists.  They might pay for threat intelligence feeds, which will often include new vulnerability announcements, and they know what software is in use across the enterprise, so they can prioritise the work and contact teams to get the issues fixed as they come up.

But even this good practice can feel like a [sisyphean task](https://en.wikipedia.org/wiki/Sisyphus#Punishment_in_the_underworld), that feels like a drain and a chore for the appsec team, and makes them decidedly unpopular across the organisation.

The best teams look to understand classes of vulnerability, to change processes and guide rails to reduce the likelihood of this kind of vulnerability happening again.  They don't just treat each issue like a stand alone issue, they are able to look at vulnerabilities as a trend, and understand both how to detect that style of vulnerability, how to change their software procurement or development process to prevent that class of vulnerability happening again, and they can document it so that when the individual responder eventually is promoted or leaves the organisation, their knowledge stays with the company.

Vulnerabilities are a fact of life, and in fact they are going to become a lot more common and a lot more critical to organisations over the next few years.  Software is now the lifeblood of most organisations, and without a way to find and fix the issues, you'll be playing catchup forever

## [How Flipkart Reacts to Security Vulnerabilities | by Shoeb Patel | Apr, 2022 | Flipkart Tech Blog ](https://blog.flipkart.tech/how-flipkart-reacts-to-security-vulnerabilities-17dae9b0661e)

[https://blog.flipkart.tech/how-flipkart-reacts-to-security-vulnerabilities-17dae9b0661e](https://blog.flipkart.tech/how-flipkart-reacts-to-security-vulnerabilities-17dae9b0661e)

> As a security engineer, this is the most fulfilling part of our vulnerability management process. We don’t just fix the vulnerabilities, but we also ensure that we learn from the gaps that introduced the vulnerability and systematically introduce technical or procedural guardrails to immunize Flipkart from them forever. 
> 
> **Remediation Plan** It starts with the Appsec engineers fully understanding the root cause(s) of the vulnerabilities and finding possible variants of the vulnerability in the codebase. With this understanding, they provide a very robust and centralized way of fixing the vulnerability, such that the possibility of any developer committing the same vulnerability in the future is eliminated. We also mandate to add the tests for the patch, and to the codebase’s test suite.
> Also, with a publicly known Zero-Day vulnerability that is prone to get actively exploited, we start with adding Web Application Firewall rules for blocking malicious traffic at the point of ingress itself and then proceed with the robust mitigations. 
> 
> **AppSec Test Suite** To not just rely on the patch and the tests written by the Dev owners, we also employ our own testing tools, which run continuously 24x7.
> The AppSec engineer determines if the exploit of the vulnerability is a good candidate for creating a query and including it in our scan engine databases. This is done by taking vulnerability into consideration. A good candidate for these queries will be the vulnerabilities that are:
> 
> * Generic and possibly apply to all of our assets. For example, a DAST query for a zero-day vulnerability that applies to our tech stack.
> * Specific to Flipkart’s architecture. For example, a SAST Query to determine vulnerable usage of an internal library. 
> 
> **Documentation** We do thorough bookkeeping of all the new lessons we get from the vulnerabilities. These documents involve RCAs, Immunization measures, etc. We primarily use these as references for our Developer Security Education Programs and our future Red Teaming References. 


This is a really nice description of how to set up an appsec team so that it has lasting impact.  

Just employing a couple of smart people to improve security might work for you, but lasting impact is impact that can be built upon, can be improved over time and ensures that your staff don’t have to keep fighting the same fight over and over.

That means not just scanning for vulnerabilities, but doing the hard work, including remediation and documentation that tries to prevent those issues arising again 


## [CVE-2022-21449: Psychic Signatures in Java ](https://neilmadden.blog/2022/04/19/psychic-signatures-in-java/)

[https://neilmadden.blog/2022/04/19/psychic-signatures-in-java/](https://neilmadden.blog/2022/04/19/psychic-signatures-in-java/)

> It’s hard to overstate the severity of this bug. If you are using ECDSA signatures for any of these security mechanisms, then an attacker can _trivially and completely bypass them_ if your server is running any Java 15, 16, 17, or 18 version before the April 2022 Critical Patch Update (CPU) . For context, almost all WebAuthn/FIDO devices in the real world (including Yubikeys * ) use ECDSA signatures and many OIDC providers use ECDSA-signed JWTs. **If you have deployed Java 15, Java 16, Java 17, or Java 18 in production then you should stop what you are doing and immediately update to install the fixes in the** **April 2022 Critical Patch Update** **.** Oracle have given this a CVSS score of 7.5, assigning no impact to Confidentiality or Availability. Internally, we at ForgeRock graded this a perfect 10.0 due to the wide range of impacts on different functionality in an access management context. ForgeRock customers can read our advisory about this issue for further guidance.
> 
> [...]
> 
> You may be wondering why this is just coming to light now, when Java has had ECDSA support for a long time. Has it always been vulnerable?
> 
> No. This is a relatively recent bug introduced by a rewrite of the EC code from native C++ code to Java, which happened in the Java 15 release . Although I’m sure that this rewrite has benefits in terms of memory safety and maintainability, it appears that experienced cryptographic engineers have not been involved in the implementation. The original C++ implementation is not vulnerable to these bugs , but the rewrite was. Neither implementation appears to have very good test coverage, and even the most cursory reading of the ECDSA spec would surely suggest testing that invalid r and s values are rejected. I am not at all confident that other bugs aren’t lurking in this code. 


This is a really nasty bug, and I agree with ForgeRock here, that this should be considered a 10.0.

One of the problems of the CVSS vulnerability scoring system is that it assumes that the impact is localised within the codebase or system that can be affected.  The worst possible type of exploit in CVSS terminology is the ability to run arbitrary code, especially if you can do so remotely and without authenticating.

But in this case, the impact is that you can get a “entitlement”.  When we look at fraud systems, one common fraud vector is not to attack the thing that gives you money directly, but instead to attack any of the systems or people who can give you something that entitles you to money.

For example, being able to debit money from peoples bank accounts directly is bad.  But being able to print your own debit cards for other peoples accounts, at scale, is actually worse.  Even though the bug itself doesn’t let the attacker get money, it gives them something that enables them to then get money legitimately.

This sort of bug, that makes it so that someone can create any entitlement, for any system, providing the server uses Java to validate that entitlement, is a hugely critical weakness in the entire system, and the way that this has been communicated generally downplays the potential impact of it.

If you run any servers with Java 15, 16, 17, or 18, then make sure that patching this is on your urgent todo list. 


## [Security alert: Attack campaign involving stolen OAuth user tokens issued to two third-party integrators | The GitHub Blog ](https://github.blog/2022-04-15-security-alert-stolen-oauth-user-tokens/)

[https://github.blog/2022-04-15-security-alert-stolen-oauth-user-tokens/](https://github.blog/2022-04-15-security-alert-stolen-oauth-user-tokens/)

> Looking across the entire GitHub platform, we have high confidence that compromised OAuth user tokens from Heroku and Travis-CI-maintained OAuth applications were stolen and abused to download private repositories belonging to dozens of victim organizations that were using these apps. Our analysis of other behavior by the threat actor suggests that the actors may be mining the downloaded private repository contents, to which the stolen OAuth token had access, for secrets that could be used to pivot into other infrastructure.
> Known-affected OAuth applications as of April 15, 2022:
> • Heroku Dashboard (ID: 145909)
> • Heroku Dashboard (ID: 628778)
> • Heroku Dashboard – Preview (ID: 313468)
> • Heroku Dashboard – Classic (ID: 363831)
> • Travis CI (ID: 9216)
> We are sharing this today as we believe the attacks may be ongoing and action is required for customers to protect themselves. 


Github here are kind of downplaying the severity of this attack, and some of the blame here is that Githubs authentication model makes giving least privilege tediously difficult to maintain and manage.

If you used Heroku or Travis CI in your organisation somewhere, there’s a very high likelihood that the person who set that up generated an OAuth user token that had privileges to read all repositories across your organisation.

That’s probably not just the ones for the project that it was setup for, but in many cases, it’s far easier to simply create an all powerful token that can read any private repository that the user has access to.

This means that the attacker may well have had access to all of those private repositories that probably contained other infrastructure secrets and tokens, you know the ones that you know you shouldn’t keep in source control, but having an “infra-secrets” repo that is private felt like it solved a problem for now, and nobody has fixed yet.

The only positive thing is that the actor in this case appears to have made an effort to not be caught and to not disturb things.  That implies a level of targeting that means that most people won’t be vulnerable, and that action now to rotate any secrets held in private repos will likely mitigate most of the harm. 


## [Wealthy cybercriminals are using zero-day hacks more than ever | MIT Technology Review ](https://www.technologyreview.com/2022/04/21/1050747/cybercriminals-zero-day-hacks/)

[https://www.technologyreview.com/2022/04/21/1050747/cybercriminals-zero-day-hacks/](https://www.technologyreview.com/2022/04/21/1050747/cybercriminals-zero-day-hacks/)

> But new research from the cybersecurity firm Mandiant shows that in a record-breaking year for hacking attacks , the proportion of zero-days exploited by cybercriminals is growing. One-third of all hacking groups exploiting zero-days in 2021 were financially motivated criminals as opposed to government-backed cyberespionage groups, according to Mandiant’s research. During the last decade, only a very small fraction of zero-days were deployed by cybercriminals. Experts believe the rapid change has to do with the illicit, multibillion-dollar ransomware industry.
> 
> “Ransomware groups have been able to recruit new talent and to use the resources from their ransomware operations and from the insane amounts of revenue they’re pulling in in order to focus on what was once the domain of state-sponsored [hacking] groups,” says James Sadowski, a researcher with Mandiant. 


This is something that will grow over the next few years.  The gap between the most highly capable actors and criminal actors is closing rapidly.

What’s worrying is that although espionage APT’s are in peoples worry lists, mostly those actors attempt to minimise disruption, so as to avoid being caught, and they have limited impact on their targets unless it aligns with their nation backing. 

Criminal actors on the other hand are far more likely to be damaging, and if they cannot make money through stealthy means, will turn to other far more disruptive impacts on their targets. 


## [DOJ's Sandworm operation raises questions about how far feds can go to disarm botnets ](https://www.cyberscoop.com/dojs-sandworm-operation-raises-questions-about-how-far-the-feds-can-go-to-disarm-botnets/)

[https://www.cyberscoop.com/dojs-sandworm-operation-raises-questions-about-how-far-the-feds-can-go-to-disarm-botnets/](https://www.cyberscoop.com/dojs-sandworm-operation-raises-questions-about-how-far-the-feds-can-go-to-disarm-botnets/)

> In what former prosecutors and legal experts call a landmark operation, the Department of Justice has now tested that principle to disrupt a Russian botnet that was spreading malware on a far-flung network of computers. Using so-called remote access techniques, law enforcement effectively broke into infected devices from afar to destroy what the U.S. government calls the “Cyclops Blink” botnet — and did so without the owners’ permission.
> 
> While the search warrant publicized by DOJ makes clear that this access did not allow the FBI to “search, view, or retrieve a victim device owner’s content or data,” legal experts say the case does raise questions about how far the government’s power should extend under a federal criminal procedure provision known as Rule 41 .
> 
> The Kremlin-backed hackers responsible for the botnet — a group known to cybersecurity researchers as Sandworm — exploited a vulnerability in WatchGuard Technologies firewall devices to install malware on a network of compromised devices. By leveraging physical access to a subset of infected devices, the FBI said it was able to reverse engineer its way into accessing all of the botnet’s command and control devices. 


This was quite the operation by the FBI.  

I approve in principle on the details of this.  The essence is that Sandworm had compromised a series of computers with malware to form a botnet, and we can assume from the unusual action here, likely had the intent to use this imminently.

Whenever people like CISA, FBI or NCSC publicise a vulnerability, we find that there’s a fair number of people who patch, but also a lot of people who don’t patch their systems for a number of reasons.  And those reasons might be good reasons around reliability or confidence in that patch, but they are also often either capacity, interest or capability that is lacking.

So the FBI essnetially used the command and control mechanism to cause the botnet computers to patch themselves.  

This could have potentially had damaging impact on a small number of the devices, because the patch might have had negative impacts on the way specific devices were being used, and the FBI had absolutely no way to be 100% confident that this was the case.

Furthermore, it’s unlikely that the FBI knew exactly which computers were part of the botnet, hence needing such a wide ranging court order to allow them to “enter and search a computer” applied to any computer in the botnet.  

The downside to this is that most people would agree that the action here is effectively balanced against the potential harm, but the US legal system is set by precedents, and once we’ve said it’s ok to use this approach on botnets, it becomes just a matter are arguing to the court to widen this approach to enable searching systems for child abuse imagery, for prohibited materials, and so on.

All in all, as a brit, I think this is a good thing generally, that the state can intervene in the cases where a foreign and hostile state is taking action, but the US legal system and set of precedents makes it slightly worrying for where it might lead. 


## [You’re muted — or are you? Videoconferencing apps may listen even when mic is off ](https://news.wisc.edu/youre-muted-or-are-you-videoconferencing-apps-may-listen-even-when-mic-is-off/)

[https://news.wisc.edu/youre-muted-or-are-you-videoconferencing-apps-may-listen-even-when-mic-is-off/](https://news.wisc.edu/youre-muted-or-are-you-videoconferencing-apps-may-listen-even-when-mic-is-off/)

> Kassem Fawaz’s brother was on a videoconference with the microphone muted when he noticed that the microphone light was still on — indicating, inexplicably, that his microphone was being accessed.
> Alarmed, he asked Fawaz, an expert in online privacy and an assistant professor of electrical and computer engineering at the University of Wisconsin–Madison, to look into the issue.
> Fawaz and graduate student Yucheng Yang investigated whether this “mic-off-light-on” phenomenon was more widespread. They tried out many different videoconferencing applications on major operating systems, including iOS, Android, Windows and Mac, checking to see if the apps still accessed the microphone when it was muted.
> “It turns out, in the vast majority of cases, when you mute yourself, these apps do not give up access to the microphone,” says Fawaz. “And that’s a problem. When you’re muted, people don’t expect these apps to collect data.”
> 
> [...]
> 
> They found that all of the apps they tested occasionally gather raw audio data while mute is activated, with one popular app gathering information and delivering data to its server at the same rate regardless of whether the microphone is muted or not.
> The researchers then decided to see if they could use data collected on mute from that app to infer the types of activities taking place in the background. Using machine learning algorithms, they trained an activity classifier using audio from YouTube videos representing six common background activities, including cooking and eating, playing music, typing and cleaning. Applying the classifier to the type of telemetry packets the app was sending, the team could identify the background activity with an average of 82% accuracy. 


Mute buttons don’t always actually mute the microphone.  

There are lots of reasons that you might do this, I suspect the most common is to be able to show you the “Are you speaking, you are muted” notification, but the fact that at least one app sends that data back to the servers anyway is slightly scary. 


## [American Phone-Tracking Firm Demo’d Surveillance Powers by Spying on CIA and NSA ](https://theintercept.com/2022/04/22/anomaly-six-phone-tracking-zignal-surveillance-cia-nsa/)

[https://theintercept.com/2022/04/22/anomaly-six-phone-tracking-zignal-surveillance-cia-nsa/](https://theintercept.com/2022/04/22/anomaly-six-phone-tracking-zignal-surveillance-cia-nsa/)

> A6 claims that its GPS dragnet yields between 30 to 60 location pings per device per day and 2.5 trillion locational data points annually worldwide, adding up to 280 terabytes of location data per year and many petabytes in total, suggesting that the company surveils roughly 230 million devices on an average day. A6’s salesperson added that while many rival firms gather personal location data via a phone’s Bluetooth and Wi-Fi connections that provide general whereabouts, Anomaly 6 harvests only GPS pinpoints, potentially accurate to within several feet. In addition to location, A6 claimed that it has built a library of over 2 billion email addresses and other personal details that people share when signing up for smartphone apps that can be used to identify who the GPS ping belongs to. All of this is powered, A6’s Clark noted during the pitch, by general ignorance of the ubiquity and invasiveness of smartphone software development kits, known as SDKs: “Everything is agreed to and sent by the user even though they probably don’t read the 60 pages in the [end user license agreement].”
> 
> The Intercept was not able to corroborate Anomaly Six’s claims about its data or capabilities, which were made in the context of a sales pitch. Privacy researcher Zach Edwards told The Intercept that he believed the claims were plausible but cautioned that firms can be prone to exaggerating the quality of their data. Mobile security researcher Will Strafach agreed, noting that A6’s data sourcing boasts “sound alarming but aren’t terribly far off from ambitious claims by others.” According to Wolfie Christl, a researcher specializing in the surveillance and privacy implications of the app data industry, even if Anomaly Six’s capabilities are exaggerated or based partly on inaccurate data, a company possessing even a fraction of these spy powers would be deeply concerning from a personal privacy standpoint. 


The continued trade in private information from devices and its users is scary in and of itself. 

The growth of the web built on the back of advertising technologies has made this somewhat inevitable, but it’s something that has already driven GDPR style regulation on privacy, and we might see more in response to this.

Additionally, we’ve already seen Apple start providing the do not track notifications, and if consumers and privacy advocates get too upset about this, we might see further restrictions on the ad tracking capabilities within applications on devices.

Sadly, it’s almost impossible to actively prevent this, and we’re left in a world where you should assume that your phone is reporting your location to anyone with a large enough budget to get access to this kind of data.  And the budget required is going to get lower and lower over the next few years as well 


## [How Democracies Spy on Their Citizens ](https://www.newyorker.com/magazine/2022/04/25/how-democracies-spy-on-their-citizens)

[https://www.newyorker.com/magazine/2022/04/25/how-democracies-spy-on-their-citizens](https://www.newyorker.com/magazine/2022/04/25/how-democracies-spy-on-their-citizens)

> The competition, Hulio argued, is far more frightening. “Companies found themselves in Singapore, in Cyprus, in other places that don’t have real regulation,” he told me. “And they can sell to whoever they want.” The spyware industry is also full of rogue hackers willing to crack devices for anyone who will pay. “They will take your computers, they will take your phone, your Gmail,” Hulio said. “It’s obviously illegal. But it’s very common now. It’s not that expensive.” Some of the technology that NSO competes with, he says, comes from state actors, including China and Russia. “I can tell you that today in China, today in Africa, you see the Chinese government giving capabilities almost similar to NSO.” According to a report from the Carnegie Endowment for International Peace, China supplies surveillance tools to sixty-three countries, often through private firms enmeshed with the Chinese state. “NSO will not exist tomorrow, let’s say,” Hulio told me. “There’s not going to be a vacuum. What do you think will happen?” 


Fascinating read into the growth and changes at NSO over time.  You can see how they tried to build a thing, but different states have very different internal logic for what they think is acceptable spycraft for both their own citizens and for “state adversaries abroad”.

By selling this software to so many different states, NSO was always going to find itself in this pickle.

But critically, as has been articulated in this article quite well, the probably is not just NSO group.  That company happens to be a particularly big and visible bit of the iceberg, but there’s a huge number of competitors to NSO Group, who aren’t as big and visible, but also therefore don’t have as much regulatory visibility 


## [Beanstalk cryptocurrency project robbed after hacker votes to send themself $182 million - The Verge ](https://www.theverge.com/2022/4/18/23030754/beanstalk-cryptocurrency-hack-182-million-dao-voting)

[https://www.theverge.com/2022/4/18/23030754/beanstalk-cryptocurrency-hack-182-million-dao-voting](https://www.theverge.com/2022/4/18/23030754/beanstalk-cryptocurrency-hack-182-million-dao-voting)

> Like many other DeFi projects, the creators of Beanstalk — a development team called Publius — included a governance mechanism where participants could vote collectively on changes to the code. They would then obtain voting rights in proportion to the value of tokens that they held, creating a vulnerability that would prove to be the project’s undoing.
> 
> The attack was made possible by another DeFi product called a “flash loan,” which allows users to borrow large amounts of cryptocurrency for very short periods of time (minutes or even seconds). Flash loans are meant to provide liquidity or take advantage of price arbitrage opportunities but can also be used for more nefarious purposes.
> 
> According to analysis from blockchain security firm CertiK, the Beanstalk attacker used a flash loan obtained through the decentralized protocol Aave to borrow close to $1 billion in cryptocurrency assets and exchanged these for enough beans to gain a 67 percent voting stake in the project. With this supermajority stake, they were able to approve the execution of code that transferred the assets to their own wallet. The attacker then instantly repaid the flash loan, netting an $80 million profit. 


The most interesting part about this is that it demonstrates a rather terrifying hole in the governance of many DeFi programmes.

The assumption is that no member of the governing board would propose and vote on a proposal to essentially kill the project and run away with the money.  

But that’s precisely what happened with this example, because one can buy votes on the governing board, and you can buy enough votes for less than the money in the chain, meaning that it’s possible to buy the votes, propose to give all the money to yourself, vote on that proposal, approve it, and execute it, and then you end up with more money than it cost you.

In a world where governance is defined by digital chains, this entire attack took place in less than 13 seconds.

The problem of decentralised cooperatives is that the assumption is that everybody suffers if they vote to behave maliciously, but these DeFi projects exist in a far wider ecosystem that mostly doesn’t care if they live or die, which makes them incredibly vulnerable to the modern equivalent of an asset stripping hostile takeover. 


## [Okta Concludes its Investigation Into the January 2022 Compromise ](https://www.okta.com/blog/2022/04/okta-concludes-its-investigation-into-the-january-2022-compromise/)

[https://www.okta.com/blog/2022/04/okta-concludes-its-investigation-into-the-january-2022-compromise/](https://www.okta.com/blog/2022/04/okta-concludes-its-investigation-into-the-january-2022-compromise/)

> Beyond those potentially impacted organizations, we recognize how vital it is to take steps to rebuild trust within our broader customer base and ecosystem. The conclusions from the final forensic report do not lessen our determination to take corrective actions designed to prevent similar events and improve our ability to respond to security incidents. That starts with reviewing our security processes and pushing for new ways to accelerate updates from third parties and internally for potential issues, both big and small. We will continue to work to assess potential risks and, if necessary, communicate with our customers as fast as we can.
> We have also committed to taking action on a number of fronts:
> 
> 1. **Third-party risk management** :
> * Okta is strengthening our audit procedures of our sub-processors and will confirm they comply with our new security requirements. We will require that sub-processors who provide Support Services on Okta's behalf adopt “Zero Trust” security architectures and that they authenticate via Okta’s IDAM solution for all workplace applications.
> * Okta has terminated its relationship with Sykes/Sitel.
> 
> 2. **Access to customer support systems** :
> * Okta will now directly manage all devices of third parties that access our customer support tools, providing the necessary visibility to effectively respond to security incidents without relying on a third party. This will enable us to significantly reduce response times and report to customers with greater certainty on actual impact, rather than potential impact. 


Okta is being pretty open about it’s next steps here, but that “directly manage devices of third parties” is a doozy of an action. 

It’s incredibly common for “managed service providers”, including those who offer outsourced 1st line support desks; remote administration; and outsourced administration to cover “follow the sun” support, to manage multiple clients from a single device.  If they have 50 clients, they don’t want to provide 50 different devices for each helpdesk operator.

I suspect that this will be either a virtual desktop instance, that can be RDP’d into from the third party systems, or only useful where there are dedicated support agents who work only on that client.

Far better in this case is to have better security schedules in place, including things like regular “fire drills” for the supplier to test out their incident response capability to ensure that they can work effectively with you if there is an incident.  Of course, that’s rare even for internal teams, and almost unheard of across the supply chain, so I doubt that will happen anytime soon. 


## [Implementing Cloud Governance as a Code using Cloud Custodian ](https://www.infracloud.io/blogs/cloud-governance-code-cloud-custodian/)

[https://www.infracloud.io/blogs/cloud-governance-code-cloud-custodian/](https://www.infracloud.io/blogs/cloud-governance-code-cloud-custodian/)

> In today’s scaling cloud infrastructure it’s hard to manage all resources compliance. Every organization has a set of policies to follow for detecting violations and taking remediation actions on their cloud resources. This is generally done by writing multiple custom scripts and using some 3rd party tool and integration. Many development teams know how hard it is to manage and write custom scripts and keep a track of those. This is where we can leverage Cloud Custodian DSL policies to manage our Cloud resources with ease. 
> 
> **What is cloud governance?** 
> 
> Cloud governance is a framework which defines how developers can create policies to control costs, minimize security risks, improve efficiency and accelerate deployment. 


Interesting looking tool for applying policies across your cloud estate, to ensure that people don’t forget or configure their cloud services insecurely.

If you are looking to enable cloud self service (and you should, otherwise you’ll find people running stuff on their credit card with no visibility or governance), then you’ll need to use something like this to ensure consistency across your estate.

Just be sure that what you are doing is enforcing sensible secure defaults, not frustrating people so that they don’t use your centrally managed cloud platform 


