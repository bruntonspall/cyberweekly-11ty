---
title: "190 - It's not zero trust, it's moving trust"
date: 2022-03-27
description: "Zero trust is the architecture we talk about where there is zero trust in the fact that the requests are [\"coming from inside the network\"](https://tvtropes.org/pmwiki/pmwiki.php/Main/TheCallsAreComingFromInsideTheHouse)."
permalink: /it-s-not-zero-trust-it-s-moving-trust/
---

Zero trust is the architecture we talk about where there is zero trust in the fact that the requests are ["coming from inside the network"](https://tvtropes.org/pmwiki/pmwiki.php/Main/TheCallsAreComingFromInsideTheHouse).

But in fact, all we are doing is moving the trust.  It used to be that most applications probably used a number of trust signals, they just didn't call them that.  So they only exposed the service on an internal LAN, and they might have HTTP Basic Authentication with a known password.  This is assuming that attackers find it difficult to get onto the internal network, and cannot read the password from the internal documentation (also on the network).

In Zero Trust, we migrate that to authenticating users against possessing a trusted device, and having a valid user session that was authenticated properly.  But this doesn't mean we have zero trust, it just means that we just moved the trust domain over to the device enrollment system and over to the user authentication service.

Many people are outsourcing both of those things, and that can create a scary combination.  It's fair to say that it's highly likely that those outsourced companies are going to run device enrollment and management better than you will, and they'll almost certainly patch and monitor the user enrollment system better than you will.  But if they get breached, is it really in their best interests to tell you?  What confidence do you have over that?

One of the things still missing from most SaaS services is the ability to get supplier logs shipped or visible to you as a purchaser.  In many traditional outsourced contracts, such as Managed Service Providers, one of the contractual terms is that the service must ship logs to your companies SOC (or more likely, your outsourced SOC).  It didn't always happen, and it wasn't always useful, but it did give you some level of confidence that you knew what was happening on their side of the network.  

SaaS tools rarely even give you basic logging, such as user actions carried out by your staff on your data on their tool.  The best of those systems, (and the major hyperscale cloud providers are somewhat ahead here), do have log systems that can ship you log events of things that happen on the network.  Rarely, this may also include log events for when a cloud provider staff member carries out an action that might affect your data, such as customer service representatives resetting passwords and so on.  

We should increasingly be demanding this kind of visibility in our suppliers, because it's our data that they are looking after on our behalf.

## [Updated Okta Statement on LAPSUS$ ](https://www.okta.com/blog/2022/03/updated-okta-statement-on-lapsus/)

[https://www.okta.com/blog/2022/03/updated-okta-statement-on-lapsus/](https://www.okta.com/blog/2022/03/updated-okta-statement-on-lapsus/)

> As we shared earlier today, we are conducting a thorough investigation into the recent LAPSUS$ claims and any impact on our valued customers. The Okta service is fully operational, and there are no corrective actions our customers need to take.  
> 
> After a thorough analysis of these claims, we have concluded that a small percentage of customers – approximately 2.5% – have potentially been impacted and whose data may have been viewed or acted upon. We have identified those customers and already reached out directly by email. We are sharing this interim update, consistent with our values of customer success, integrity, and transparency.
> 
> [... ORIGINAL STATEMENT ...]
> 
> The Okta service has not been breached and remains fully operational. There are no corrective actions that need to be taken by our customers. 


Oof, this isn't good.  Okta is one of the biggest Single Sign On providers who make it easy to adopt zero trust architectures.  Of course in Zero Trust, where we are moving the trust from the network to the identity service, the identity service itself becomes the central point of concern.

But whats more worrying here is that Okta's first report was to send out a note saying the service has not been breached, and then have to send out an update saying "actually we hadn't looked properly, and now we do, maybe we were breached".  For such a critical security enforcing function, it's critical that you have trust in the organisation, and saying you haven't been breached when you haven't yet done an investigation is not a way to build trust with your customers.  Hopefully this was a mistake by overeager or stressed PR people, when someone claims to have breached you, it's instinct to say "No they haven't, I'd know".

This might all blow over, until Okta does finish the investigation, we won't know to what extent they were breached, and what the attackers could get.  From screenshots, it looks like they could access the customer service control panel, but without knowing what privileges that has over customer accounts it's difficult to impact assess.

However, if you use Okta, you should definitely be considering conducting an access audit, just in case.  Besides, getting some practice on those access audits will be worthwhile as you migrate to zero trust anyway, right?


## [Lapsus$ Cyberattacks Traced to Teenager in England - Bloomberg ](https://www.bloomberg.com/news/articles/2022-03-23/teen-suspected-by-cyber-researchers-of-being-lapsus-mastermind)

[https://www.bloomberg.com/news/articles/2022-03-23/teen-suspected-by-cyber-researchers-of-being-lapsus-mastermind](https://www.bloomberg.com/news/articles/2022-03-23/teen-suspected-by-cyber-researchers-of-being-lapsus-mastermind)

> Lapsus$ has befuddled cybersecurity experts as it has embarked on a rampage of high-profile hacks. The motivation behind the attacks is still unclear, but some cybersecurity researchers say they believe the group is motivated by money and notoriety.
> 
> The teen is suspected by the researchers of being behind some of the major hacks carried out by Lapsus$, but they haven’t been able to conclusively tie him to every hack Lapsus$ has claimed. The cyber researchers have used forensic evidence from the hacks as well as publicly available information to tie the teen to the hacking group.
> 
> Bloomberg News isn’t naming the alleged hacker, who goes by the online alias “White” and “breachbase,” who is a minor and hasn’t been publicly accused by law enforcement of any wrongdoing.
> 
> Another member of Lapsus$ is suspected to be a teenager residing in Brazil, according to the investigators. One person investigating the group said security researchers have identified seven unique accounts associated with the hacking group, indicating that there are likely others involved in the group’s operations. 


This shouldn’t really surprise anyone, but just another reminder that almost all of the tools, the tutorials and the accesses are out there for any amateur to pick up.  And sometimes, someone with time, a little spare cash, and a lot of dedication can do a lot more damage than an enterprise APT that has to jump through bureaucratic hoops to run each operation.  Small and agile can be terrifyingly competent at times. 


## [A Closer Look at the LAPSUS$ Data Extortion Group – Krebs on Security ](https://krebsonsecurity.com/2022/03/a-closer-look-at-the-lapsus-data-extortion-group/)

[https://krebsonsecurity.com/2022/03/a-closer-look-at-the-lapsus-data-extortion-group/](https://krebsonsecurity.com/2022/03/a-closer-look-at-the-lapsus-data-extortion-group/)

> One of the LAPSUS$ group members admitted on their Telegram channel that the Microsoft source code download had been interrupted.
> “This public disclosure escalated our action allowing our team to intervene and interrupt the actor mid-operation, limiting broader impact,” Microsoft wrote. “No customer code or data was involved in the observed activities. Our investigation has found a single account had been compromised, granting limited access. Microsoft does not rely on the secrecy of code as a security measure and viewing source code does not lead to elevation of risk.”
> While it may be tempting to dismiss LAPSUS$ as an immature and fame-seeking group, their tactics should make anyone in charge of corporate security sit up and take notice. Microsoft says LAPSUS$ — which it boringly calls “DEV-0537” — mostly gains illicit access to targets via “social engineering.” This involves bribing or tricking employees at the target organization or at its myriad partners, such as customer support call centers and help desks.
> “Microsoft found instances where the group successfully gained access to target organizations through recruited employees (or employees of their suppliers or business partners),” Microsoft wrote. 


Nice bit of work from Krebs here, with a writeup that pulls together a number of historical pieces showing the rise and development of Lapsus$ as well as pulls out some of the MO covered by the Microsoft report and more. 


## [DEV-0537 criminal actor targeting organizations for data exfiltration and destruction - Microsoft Security Blog ](https://www.microsoft.com/security/blog/2022/03/22/dev-0537-criminal-actor-targeting-organizations-for-data-exfiltration-and-destruction/)

[https://www.microsoft.com/security/blog/2022/03/22/dev-0537-criminal-actor-targeting-organizations-for-data-exfiltration-and-destruction/](https://www.microsoft.com/security/blog/2022/03/22/dev-0537-criminal-actor-targeting-organizations-for-data-exfiltration-and-destruction/)

> The activity we have observed has been attributed to a threat group that Microsoft tracks as DEV-0537, also known as LAPSUS$. DEV-0537 is known for using a pure extortion and destruction model without deploying ransomware payloads. DEV-0537 started targeting organizations in the United Kingdom and South America but expanded to global targets, including organizations in government, technology, telecom, media, retail, and healthcare sectors. DEV-0537 is also known to take over individual user accounts at cryptocurrency exchanges to drain cryptocurrency holdings.
> 
> Unlike most activity groups that stay under the radar, DEV-0537 doesn’t seem to cover its tracks. They go as far as announcing their attacks on social media or advertising their intent to buy credentials from employees of target organizations. DEV-0537 also uses several tactics that are less frequently used by other threat actors tracked by Microsoft. Their tactics include phone-based social engineering: SIM-swapping to facilitate account takeover, accessing personal email accounts of employees at target organizations, paying employees, suppliers, or business partners of target organizations for access to credentials and multifactor authentication (MFA) approval; and intruding in the ongoing crisis-communication calls of their targets.
> 
> [...]
> 
> They have been consistently observed to use AD Explorer, a publicly available tool, to enumerate all users and groups in the said network. This allows them to understand which accounts might have higher privileges. They then proceeded to search collaboration platforms like SharePoint or Confluence, issue-tracking solutions like JIRA, code repositories like GitLab and GitHub, and organization collaboration channels like Teams or Slack to discover further high-privilege account credentials to access other sensitive information.
> 
> DEV-0537 is also known to exploit vulnerabilities in Confluence, JIRA, and GitLab for privilege escalation. The group compromised the servers running these applications to get the credentials of a privileged account or run in the context of the said account and dump credentials from there. The group used DCSync attacks and Mimikatz to perform privilege escalation routines. Once domain administrator access or its equivalent has been obtained, the group used the built-in Ntdsutil utility to extract the AD database. 


This targeting of Confluence, Slack, Github and so on shows a level of aptitude and TTP’s that probably bypasses many SOC’s.  These developer focused tools are often outside of traditional enterprise offerings, but just as likely to contain passwords, access tokens and the ability to further socially engineer people in the organisation, and that makes this group particularly dangerous.

Also, if you work in security in an organisation, find out how your developer teams work, don’t tell them off, but find out the shadow IT that they run so you can monitor it for this kind of activity.  Anytime you are the compliance department or the department of no, is an opportunity for teams to create infrastructure that is outside your visibility. 


## [Hundreds of AI tools have been built to catch covid. None of them helped. | MIT Technology Review ](https://www.technologyreview.com/2021/07/30/1030329/machine-learning-ai-failed-covid-hospital-diagnosis-pandemic/)

[https://www.technologyreview.com/2021/07/30/1030329/machine-learning-ai-failed-covid-hospital-diagnosis-pandemic/](https://www.technologyreview.com/2021/07/30/1030329/machine-learning-ai-failed-covid-hospital-diagnosis-pandemic/)

> “This pandemic was a big test for AI and medicine,” says Driggs, who is himself working on a machine-learning tool to help doctors during the pandemic. “It would have gone a long way to getting the public on our side,” he says. “But I don’t think we passed that test.”
> 
> Both teams found that researchers repeated the same basic errors in the way they trained or tested their tools. Incorrect assumptions about the data often meant that the trained models did not work as claimed.
> 
> Driggs highlights the problem of what he calls Frankenstein data sets, which are spliced together from multiple sources and can contain duplicates. This means that some tools end up being tested on the same data they were trained on, making them appear more accurate than they are.
> 
> It also muddies the origin of certain data sets. This can mean that researchers miss important features that skew the training of their models. Many unwittingly used a data set that contained chest scans of children who did not have covid as their examples of what non-covid cases looked like. But as a result, the AIs learned to identify kids, not covid.
> Driggs’s group trained its own model using a data set that contained a mix of scans taken when patients were lying down and standing up. Because patients scanned while lying down were more likely to be seriously ill, the AI learned wrongly to predict serious covid risk from a person’s position.
> In yet other cases, some AIs were found to be picking up on the text font that certain hospitals used to label the scans. As a result, fonts from hospitals with more serious caseloads became predictors of covid risk.
> Errors like these seem obvious in hindsight. They can also be fixed by adjusting the models, if researchers are aware of them. It is possible to acknowledge the shortcomings and release a less accurate, but less misleading model. But many tools were developed either by AI researchers who lacked the medical expertise to spot flaws in the data or by medical researchers who lacked the mathematical skills to compensate for those flaws. 


The always ever present reminder that AI and ML are great hype selling tools, but the reality of getting them to work requires a blend of skills that is simply not existent in most work forces.  You need both subject matter experts and data scientists and machine learning experts, all working together to ensure that the data sets are appropriate, tagged correctly and can be used effectively.  And all of those people need to be able to talk to each other effectively, clearly and be able to understand one another. 


## [FBI recruits Russian spies outside Russian embassy in D.C. - The Washington Post ](https://www.washingtonpost.com/national-security/2022/03/23/fbi-russia-spy-recruiting-ukraine/)

[https://www.washingtonpost.com/national-security/2022/03/23/fbi-russia-spy-recruiting-ukraine/](https://www.washingtonpost.com/national-security/2022/03/23/fbi-russia-spy-recruiting-ukraine/)

> The ads, which appear on Facebook, Twitter and Google, are carefully geographically targeted. A Washington Post reporter standing next to the embassy’s stone walls on Wednesday morning received the ad in their Facebook feed. But the ads did not appear in the feed when the reporter stood on the other side of Wisconsin Avenue NW, in the District’s Glover Park neighborhood.
> 
> The ads are designed to capitalize on any dissatisfaction or anger within Russian diplomatic or spy services — or among Russian emigres to the United States — over the invasion of Ukraine, an event that counterintelligence experts call a huge opportunity for the U.S. intelligence community to recruit new sources. 


As we found out during the US election and the EU exit referendum, you can very carefully target adverts if you know what you are doing, and use it to speak only to a small subset of people without any others outside that set knowing that it’s happening.

That’s bad when it comes to information sharing across democracies, but does also help target recruitment messages like this more effectively. 


## [Turla’s watering hole campaign: An updated Firefox extension abusing Instagram | WeLiveSecurity ](https://www.welivesecurity.com/2017/06/06/turlas-watering-hole-campaign-updated-firefox-extension-abusing-instagram/)

[https://www.welivesecurity.com/2017/06/06/turlas-watering-hole-campaign-updated-firefox-extension-abusing-instagram/](https://www.welivesecurity.com/2017/06/06/turlas-watering-hole-campaign-updated-firefox-extension-abusing-instagram/)

> **The use of Instagram** The extension uses a bit.ly URL to reach its C&C, but the URL path is nowhere to be found in the extension code. In fact, it will obtain this path by using comments posted on a specific Instagram post. The one that was used in the analyzed sample was a comment about a photo posted to the Britney Spears official Instagram account.
> © https://www.instagram.com/p/BO8gU41A45g/ The extension will look at each photo’s comment and will compute a custom hash value. If the hash matches 183, it will then run this regular expression on the comment in order to obtain the path of the bit.ly URL:
> (?:\\u200d(?:#|@)(\\w)
> Looking at the photo’s comments, there was only one for which the hash matches 183. This comment was posted on February 6, while the original photo was posted in early January. Taking the comment and running it through the regex, you get the following bit.ly URL:
> http://bit.ly/2kdhuHX
> Looking a bit more closely at the regular expression, we see it is looking for either @|# or the Unicode character \200d. This character is actually a non-printable character called ‘Zero Width Joiner’, normally used to separate emojis. Pasting the actual comment or looking at its source, you can see that this character precedes each character that makes the path of the bit.ly URL:
> smith2155<200d>#2hot ma<200d>ke lovei<200d>d to <200d>her, <200d>uupss <200d>#Hot <200d>#X
> When resolving this shortened link, it leads to static.travelclothes.org/dolR_1ert.php , which was used in the past as a watering hole C&C by the Turla crew. 


This is an oldie (from 2017), but a good one.  The use of comments in social media as C2 is impressively capable, as it would be almost impossible to differentiate this from normal browsing activity. 


## [Evolving trends in Iranian threat actor activity – MSTIC presentation at CyberWarCon 2021 - Microsoft Security Blog](https://www.microsoft.com/security/blog/2021/11/16/evolving-trends-in-iranian-threat-actor-activity-mstic-presentation-at-cyberwarcon-2021/)

[https://www.microsoft.com/security/blog/2021/11/16/evolving-trends-in-iranian-threat-actor-activity-mstic-presentation-at-cyberwarcon-2021/](https://www.microsoft.com/security/blog/2021/11/16/evolving-trends-in-iranian-threat-actor-activity-mstic-presentation-at-cyberwarcon-2021/)

> MSTIC consistently tracks threat actor activity, including the groups discussed in this blog, and works across Microsoft Security products and services to build detections into our products that improve customer protections. We are sharing this blog today so that others in the community can also be aware of the latest techniques we have observed being used by Iranian actors.
> 
> As with any observed nation-state actor activity, Microsoft has directly notified customers that have been targeted or compromised, providing them with the information they need to help secure their accounts. Microsoft uses DEV-#### designations as a temporary name given to an unknown, emerging, or a developing cluster of threat activity, allowing MSTIC to track it as a unique set of information until we reach a high confidence about the origin or identity of the actor behind the activity. Once it meets the criteria, a DEV is converted to a named actor.
> 
> Three notable trends in Iranian nation-state operators have emerged:
> 
> They are increasingly utilizing ransomware to either collect funds or disrupt their targets.
> They are more patient and persistent while engaging with their targets.
> While Iranian operators are more patient and persistent with their social engineering campaigns, they continue to employ aggressive brute force attacks on their targets.


Microsoft talking about another class of advanced actors and their tactics.  

Reminder here that the underlying tactic is the same as everyone else, get you to click a link that harvests your username and password.  The difference between an advanced actor and an off the street criminal is the amount of planning, targeting and operational security that goes around it.

Multi-factor authentication and endpoint detection and response software will mitigate the vast majority of these attacks (as they stand).


## [Post-It Notes aren’t Agile – they’re wallpaper – Terence Eden’s Blog ](https://shkspr.mobi/blog/2020/02/post-it-notes-arent-agile-theyre-wallpaper/)

[https://shkspr.mobi/blog/2020/02/post-it-notes-arent-agile-theyre-wallpaper/](https://shkspr.mobi/blog/2020/02/post-it-notes-arent-agile-theyre-wallpaper/)

> Recently, I visited a fairly large company who are making the painful transition from providing mega-software into to being a nimble, digital supplier. Their walls were plentifully decorated with multi-coloured Post-it® notes.
> 
> Decorated being the operative word. A quick glance at them showed titles like "To-Do 2018" and "Easter Fire-Break" and "FAO Jerry".
> 
> "Who is Jerry?" I asked.
> 
> "Oh... I think he left a few months back," came the reply.
> 
> Now, not _all_ of the Kanban Boards were outdated - some were obviously in use and had teams performing their daily rituals in front of them. But the majority seemed abandoned.
> Perhaps abandoned is too strong a word. They were like cave paintings. Evidence of the hunt, sure, but now decorations to be marvelled at. A way to indoctrinate new members of the tribe. 


I really like this recognition that agile ceremonies can often be just that, indoctrination ceremonies, filled with historical meaning but ultimately serving no real purpose, or at least, with purpose separated from the original intent.

I suspect we’ve all heard stories like **that** before! 


## [Russian Electric Vehicle Chargers Hacked, Tell Users ‘PUTIN IS A DICKHEAD’ ](https://www.vice.com/en/article/akvya5/russian-electric-vehicle-chargers-hacked-tell-users-putin-is-a-dickhead)

[https://www.vice.com/en/article/akvya5/russian-electric-vehicle-chargers-hacked-tell-users-putin-is-a-dickhead](https://www.vice.com/en/article/akvya5/russian-electric-vehicle-chargers-hacked-tell-users-putin-is-a-dickhead)

> According to the post, the chargers were purchased through a Russian company which had outsourced production to a Ukrainian parts supplier called AutoEnterprise , a Kharkiv-based EV charging company. This morning, posts began to appear on social media showing the chargers were disabled and programmed to display pro-Ukrainian messages. 


In this case, the “backdoor” as was reported in a number of cases, was likely the legitimate software update functionality.  

File this one under “supply chain is hard” 


