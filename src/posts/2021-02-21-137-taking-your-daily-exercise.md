---
title: "137 - Taking your daily exercise"
date: 2021-02-21
description: "We don't exercise enough. "
permalink: /taking-your-daily-exercise/
---

We don't exercise enough. 

The pandemic has meant that I can now often go an entire week without leaving the house, and sometimes it feels like I go an entire week without really leaving my desk.  But exercise is great for us, the fresh air, the movement and the change of scenery helps to make our brains work.

With that tenuous link, I think there's a lot of power in tabletop exercising.  I know that people get very excited by red team activities, people pretending to be attackers and compromising our systems, and in the DevOps world, everyone loves a GameDay, where you break the system or simulate breaking the system to test your resilience (or more often, make a point).

But getting seniors or even midlevel managers around a table and discussing the likely scenarios and what would happen can be a great way of getting people into a new location, out of their existing rut and get the brain working.

These don't need to be catastrophic data loss scenarios.  While those are fun to run through, it's often bad enough for people to think about simple easy scenarios like a single system being compromised, publishing a credential, or losing important data and needing to get to the backups.  These simple scenarios feel far more likely to the non-specialists around the table, and they tend to think that there are existing processes and systems for handling them.  But in reality, there are often no formal processes for spotting and reacting to such incidents, and instead we rely on existing knowledge or the right behaviours from the right people at the time.

If you can bring in representatives from various places in the organisation to a single location, get everyone around a table (or virtual zoom call), and forbid the technical specialists from speaking unless the team asks for their help, you can find out just how unlikely it is that anyone would reach out to the technical specialists.  It can be eye-opening to see how many of these problems are solved by do-gooders who try to fix things themselves to avoid interrupting or sometimes even speaking to IT about a problem.

[Just a quick note that I'm aware that the cyberweekly.net website is not up to date.  Sadly, I've suffered from the Google deprecation policy, and need to convert the application that runs the website from Google AppEngine and Datastore over to Google CloudRun and Firestore.  Annoyingly, I ignored the deprecation warnings, but now cannot deploy the application to make a simple change, such as the mailing list signup on the frontpage!  Hopefully I'll have that migrated sometime this coming week, and it'll be back to working condition again]

## [The global AI agenda [pdf]](https://mittrinsights.s3.amazonaws.com/AIagenda2020/GlobalAIagenda.pdf)

[https://mittrinsights.s3.amazonaws.com/AIagenda2020/GlobalAIagenda.pdf](https://mittrinsights.s3.amazonaws.com/AIagenda2020/GlobalAIagenda.pdf)

> Change management and data challenges do most to hinder scaling of AI. Taking AI use cases beyond pilot stage is far from straightforward for any organization. The surveyed firms struggle most with the change management involved in modifying business processes to leverage AI, a challenge cited by 51% of respondents. Nearly as difficult are data challenges—cited by 48%— chief among which are difficulties integrating unstructured data and in interfacing with open-data platforms (problems reported by 57% and 53% of executives, respectively). Respondents’ emphasis on the latter suggests a desire to access external data to feed their AI models.
> 
> The top AI use cases today are in the areas of quality control, customer care, and cybersecurity. Around six out of 10 manufacturers and pharma companies are using AI to improve product quality. Nearly half of consumer goods and retail firms (47%) are using it in customer care. Over half (51%) of energy firms are leveraging AI for monitoring and diagnostics, 58% of financial services providers for fraud detection, and 52% of tech firms to strengthen cybersecurity.


The complexity in taking an AI system from a whizzy pilot or demo shouldn’t be underestimated.  Often sold as labour saving, in fact good AI systems need careful oversight, training and management.  That might save you cheap labour in the form of manual workers, but means you need to invest in more expensive highly trained and capable workers.


## [State of JS 2020](https://2020.stateofjs.com/en-US/)

[https://2020.stateofjs.com/en-US/](https://2020.stateofjs.com/en-US/)

> As crappy as 2020 was, JavaScript as a whole still managed to somehow move forward. As the language itself keeps improving thanks to new features like Optional Chaining and Nullish Coalescing, TypeScript's widespread adoption is taking things to a whole other level by popularizing static typing.
> 
> And on the framework side, just when we thought things were settling down, Svelte comes in and shakes everything up with a fresh take on the front-end. And even build tools are showing signs of new activity after years of webpack dominance.
> 
> But the difference this time is that the “old” guard –relatively speaking– is not going anywhere. Svelte and Snowpack are great, but so are React and webpack. And sure, they too will eventually fall prey to the Great JavaScript Churn, but not for many, many years.


I’ve been meaning to take some time out to really sit down and learn React for a couple of years now.  Looks like my procrastination has paid off, and I can scratch that off my todo list and add Svelte instead. 

I always like to see the state of the JavaScript ecosystem, as like it not, to a rapidly aging post-technical ex-developer like me, it is the default of modern software development.  


## [Leonardo S.p.A. Data Breach Analysis](https://reaqta.com/2021/01/fujinama-analysis-leonardo-spa/)

[https://reaqta.com/2021/01/fujinama-analysis-leonardo-spa/](https://reaqta.com/2021/01/fujinama-analysis-leonardo-spa/)

> Though the company’s initial report identified the leak to be negligible in volume, the CNAIPIC’s investigation found the amount to actually be significant, with 100.000 files exfiltrated for a total of 10Gb of data from 33 devices in a single location and tracking the final infection to a total of 94 different devices. The attack was considered an APT by the Italian Police, carried out by a single person whom manually installed a custom malware on each targeted machine.
> 
> Physical attacks are hard to detect, as any local access to the device can help to mitigate on-device detections, this is especially true when the attacker is, like in Leonardo’s case, part of the company’s security unit.
> 
> A physical attack carried out by a person with high-level access is a worst-case scenario for any company or agency but, as we will see later, things might have taken a different turn if the malware involved was actually sophisticated.


This is quite a depressing read.  Comparing the actions of this advanced actor compared to solarwinds is miles apart.


## [IBM CISO Perspective: Zero Trust Changes Security From Something You Do to Something You Have](https://securityintelligence.com/posts/ibm-ciso-perspective-zero-trust-changes-security/)

[https://securityintelligence.com/posts/ibm-ciso-perspective-zero-trust-changes-security/](https://securityintelligence.com/posts/ibm-ciso-perspective-zero-trust-changes-security/)

> First, many vendors in the security industry are looking at zero trust security from the wrong perspective. Security isn’t something you can just ‘do.’ Sure, you may be able to buy security tools or products. As a security professional, you might have a lot of experience at adjusting firewall or provisioning policies, or have specialized training to investigate incidents. While these things can be helpful in applying security to your organization’s business practices, they are not really advancing the business in a secure way.
> 
> That is an important distinction and provides the basis of our view of zero trust. Zero trust isn’t something you can buy or implement. It’s a philosophy and a strategy. And to be frank, at IBM, we wouldn’t even characterize zero trust as a security strategy. It’s an IT strategy done securely.
> 
> Cloud First — More than an IT Strategy
> Consider this. For the last several years, our IT strategy has followed a simple rule: cloud first. Everything we build or buy — from our marketing tools to our developer technology to our collaboration applications — is delivered as a service or is available to be hosted on our public cloud.


This simple rule, "cloud-first" is probably better defined as "Purchase as a commodity service".  This isn't really about cloud as we sometimes think of it.  It's not about whether tools are hosted on an AWS IaaS.  It's about purchasing tools or systems as services, where a third party is responsible for all of the security of the data and the service, in isolation from everything else.

This is the doublethink of "zero-trust", it's actually about massively increasing your trust.  Increasing your trust in third parties to protect your data, and decreasing your trust that you can do a better job of that on your own network.  We stop trusting that our devices, on our network, can access our data on our servers.  Instead we assume that any or every part of that can be compromised, and we invest in attestion, detection and remediation technologies to partition services, clients and devices into trust zones or areas dynamically.


## [2021 CYBER THREAT TRENDS OUTLOOK [pdf]](https://boozallen.com/content/dam/boozallen_site/ccg/pdf/publications/cyber-threat-trends-outlook-2021.pdf)

[https://boozallen.com/content/dam/boozallen_site/ccg/pdf/publications/cyber-threat-trends-outlook-2021.pdf](https://boozallen.com/content/dam/boozallen_site/ccg/pdf/publications/cyber-threat-trends-outlook-2021.pdf)

> The widespread adoption of cloud computing services has been the source of significant benefits and high-profile missteps and abuses. As organizations have migrated from in-house servers to IaaS hosting, misconfigured access
> controls have exposed millions of database records, or left the door open for attack by threat actors deploying ransomware or cryptominers. Further, threat actors of all stripes make use of SaaS solutions to help evade detection by hosting malware payloads on cloud-storage service or exfiltrating data from compromised hosts via messages to accounts on widely used webmail.
> 
> Booz Allen expects the types of attacks abusing cloud solutions to continue to evolve, possibly including the convergence of several known tactics used in software supply chain attacks to target PaaS solutions used to develop and deploy software applications.


I wonder if we need a better roadmap of nomenclature for "breaches".  There is something fundamentally different in terms of the vulnerability of your system comparing accidentally publishing data into public s3 buckets versus allowing ransomware in via a published RDP port for a cloud server.  And yet both are a "breach caused by cloud computing".

Either way, this snippet from an otherwise fairly traditional report caught my eye because it intermediates cloud threats to cover misconfiguration, accidentally publication as well as cloud services as used by attackers.  This "Cloud helps redteams/attackers because of attribution, dynamic command and control" etc was a thing that had gone mostly quiet, but it's still worth unpicking.

For defenders, determining the difference between a legitimate database backup script pushing terabytes of data to S3/Glacier, and an attacker exfiltrating data to a bucket they control is incredibly hard.  The more that attackers use the same looking infrastructure as the defenders and builders, the harder to tell them apart.


## [NCC Group Fix Bounty](https://www.nccgroup.com/ae/about-us/newsroom-and-events/blogs/2017/march/fix-bounty/)

[https://www.nccgroup.com/ae/about-us/newsroom-and-events/blogs/2017/march/fix-bounty/](https://www.nccgroup.com/ae/about-us/newsroom-and-events/blogs/2017/march/fix-bounty/)

> The concept of “Fix Bounty” came about from conversations with colleagues on how there’s often little to no reward for providing security fixes to vulnerabilities found in open source software.
> 
> Open source projects can differ greatly in terms of size, popularity, number of active contributors and levels of security scrutiny achieved across those projects; as such security vulnerabilities can, and do manifest themselves in open source and even critical flaws can sometimes go unnoticed for some time, as exemplified with the Heartbleed OpenSSL security flaw disclosed in April 2014, yet introduced in 2012 [1].
> 
> The idea of Fix Bounty is to reward individuals for finding and fixing security vulnerabilities in open source software.
> 
> While this initiative has started as an internal scheme for NCC Group consultants, in the spirit of collaboration we urge others in the industry to take this model and copy or evolve it further.


Last week I said that I thought security researchers should do more to fix bugs rather than just point them out.  It was pointed out to me that NCC Group started doing exactly that back in 2017.  

Well done to NCC Group for being proactive in this area


## [NYC Cyber Command: Embracing Our ‘Zero Trust’ Reality](https://www.govtech.com/NYC-Cyber-Command-Embracing-Our-Zero-Trust-Reality.html)

[https://www.govtech.com/NYC-Cyber-Command-Embracing-Our-Zero-Trust-Reality.html](https://www.govtech.com/NYC-Cyber-Command-Embracing-Our-Zero-Trust-Reality.html)

> The traditional “castle and moat” approach will not create or sustain our future cyber-resiliency. Governments and industry now need to have a frank conversation about how zero-trust architecture solutions can play a role in that future.
> 
> To realize a new vision for cybersecurity and cyber-resilience, our partners in the information technology vendor community need to rethink the current script to help get us where we need to go. This new zero-trust reality will not exist without the development of broadly accepted standards so an ecosystem can develop that benefits the end users, avoids vendor lock-in and ensures competition in the space.


The more I look at Zero-trust, the more I think that we need a better understanding of the protocols and systems that are needed to implement it.  It's not something that anybody can implement purely within their system, but something you need all of your IT systems to be able to do or use.

Until then, I think we might be stuck with running internal identity aware proxies and in essence, proxying a lot of the internet in order to apply appropriate access controls.


## [The State of Web Application and API Protection [registration wall]](https://discover.radware.com/c/Web-Application-Security-Report_2021_RR?x=ErpMp5)

[https://discover.radware.com/c/Web-Application-Security-Report_2021_RR?x=ErpMp5](https://discover.radware.com/c/Web-Application-Security-Report_2021_RR?x=ErpMp5)

> The Mad Dash to The Cloud Will Undermine Application Security In 2021 
> 
> “As organizations shift to the hybrid work model, implementing new strategies is critical to protecting digital assets and guarding against cyberthreats. The Covid-19 pandemic triggered an accelerated migration of business applications and infrastructure into the cloud, which unintentionally increased attack surfaces and created security gaps for hackers. We expect to see the consequences of this error-prone reality in 2021”


Interesting report from a naturally interested party.  But I've not seen much about the security implications of API interfaces around and about much.  In particular the focus on modern n-tier architectures, with a public facing API, and a client application that might be a mobile application shows some research into development teams building things these ways.  

Of course, the assumption that hard coded credentials in your mobile app is sufficient to protect an API is an assumption that will come back to bite you, but it's really hard for fast moving companies to know what the right thing to do here is.


## [Rebooting risk management during COVID-19 | Deloitte Insights](https://www2.deloitte.com/us/en/insights/economy/covid-19/risk-management-during-covid-19.html?id=us:2em:3pa:risk-management:eng:di:020321)

[https://www2.deloitte.com/us/en/insights/economy/covid-19/risk-management-during-covid-19.html?id=us:2em:3pa:risk-management:eng:di:020321](https://www2.deloitte.com/us/en/insights/economy/covid-19/risk-management-during-covid-19.html?id=us:2em:3pa:risk-management:eng:di:020321)

> Make risk intelligence smarter: Giving risk management the tools to do their job
> 
> When a crisis strikes and amid ongoing uncertainty, management needs a clear picture of current and potential developments. Yet the risk leader and the risk function often lack the access to data, the analytical firepower, and the ability to communicate with management and the organization in real time or near-real time. A successful risk reboot empowers the risk leader with ready access to risk and performance data, analytical tools, and reporting mechanisms such as data visualization. Equally important, the risk leader and his or her team should be prepared to provide early warnings of emerging risks to further support decision-making—perhaps with an assist from risk-sensing technologies, predictive analytics, and scenario planning—along with actionable insights and recommendations.
> 
> Scenario planning in particular can enable risk leaders to clearly portray the impact of potential risk events on specific stakeholders. It enables management to more clearly understand the full range of available options as well as the if-then ramifications of each decision. Scenario planning also enables leaders to define potential signals that, if they were to emerge, might indicate the nature and impact of potential risks as well as the direction of future events.


Another report talking about the benefit of table top exercises and scenario planning.  In this case, Deloitte are talking about more generic risk management, not just cybersecurity risks, but the lessons still hold.  We really do struggle to clearly portray the impact of the risks, and role playing and scenarios can provide useful places to find out what the reactions might look like, and how you can mitigate the impact


## [Cloud Security Table Top Exercises | by Matt Fuller | Jan, 2021 | Level Up Coding](https://levelup.gitconnected.com/cloud-security-table-top-exercises-629d353c268e)

[https://levelup.gitconnected.com/cloud-security-table-top-exercises-629d353c268e](https://levelup.gitconnected.com/cloud-security-table-top-exercises-629d353c268e)

> Like disaster recovery plans, cloud security response processes are useless if they are not reviewed, practiced, and updated on a regular basis. In an ideal world, this is done quarterly as a cross-team effort among the security, compliance, infrastructure, and operations teams.
> 
> Despite all best efforts, new situations may arise at any time that have not been practiced previously. It’s important for security teams to meet often to create response procedures for the unknowns — situations when suspicious activity is detected or a compromise is known but that don’t have predefined SOPs for responding teams.
> 
> The initial “answer” to many of the scenarios below may be “logs!” but I encourage you to think further — Which logs? Where are they being sent? Do your security teams have access to them? What are the retention policies? What do you do once you find the logs? Do you have easy ways to extract the required security information?


For many teams, starting with some of these table top exercises will help the team to work through questions that they haven't before.  If you have lots of delivery teams and just a small cloud security team, then offering this ability to host workshops that ask these questions might be one of the most impactful simple things you can do, because developers and delivery teams don't not care about security, they simply lack the time or tools to ask the right questions when up against the coalface of delivery.


