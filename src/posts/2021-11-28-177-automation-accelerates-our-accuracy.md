---
title: "177 - Automation accelerates our accuracy"
date: 2021-11-28
description: "Automation can be seen as a way to make jobs easier, to reduce the grunt work.  "
permalink: /automation-accelerates-our-accuracy/
---

Automation can be seen as a way to make jobs easier, to reduce the grunt work.  

But automation also means that the job is done the same way every time.  It means that you can read the automation specification to know exactly how the job will be done. 

This ability to audit the job, to know that each time the job is done it will be done the same way, and to even know how the job has changed being done over time (assuming you track your automation in some form of configuration control system) gives you far greater accuracy, and allows you to prove your compliance with regulations and governance processes.

Automation isn't (just) a time saving or money saving measure, but it's a way to improve your accuracy, safety and security as well.

## ['We Have to Change the Decision Calculus' to Stop Ransomware | Decipher](https://duo.com/decipher/we-have-to-change-the-decision-calculus-to-stop-ransomware)

[https://duo.com/decipher/we-have-to-change-the-decision-calculus-to-stop-ransomware](https://duo.com/decipher/we-have-to-change-the-decision-calculus-to-stop-ransomware)

> Those operations and others that have hit ransomware groups recently involve cooperation from law enforcement agencies around the world and deep collaboration with private sector security researchers, and the cooperative effort has been effective. But hitting back at the operators can only go so far. If one or two or three operators are arrested, there are dozens more waiting behind them to take the reins, because the money is good and the risk is so low, particularly in countries that are not on speaking terms with the U.S. The next step in taking the advantage away from the operators and their sponsors likely has to come from enterprise security teams rather than the FBI or Interpol.
> 
> “Ransomware is like Thanos; it was inevitable. It’s such a permissive environment with misconfigurations and vulnerabilities to exploit and ransomware is just the ultimate monetization of those vulnerabilities,” Chris Krebs, the former director of the Cybersecurity and Infrastructure Security Agency, said during a keynote speech at Cyberwarcon Tuesday.
> 
> [...]
> 
> That means that defenders need to get smarter, too, as do policy makers who are looking for ways to address the ransomware problem, as well the broader security issues facing U.S. businesses and government agencies. Congress has focused quite a bit of attention on cybersecurity issues in the last year and there are several bills in the works that take on various aspects of the problem. Some type of requirement for organizations to report breaches is likely to emerge, as is a requirement that businesses disclose ransom payments quickly after they make them.
> 
> “I think regulation is inevitable, and I also think it’s inevitable that we will get it wrong. We have to distill down the critical functions and prioritize. We have to change the decision calculus across the private sector,” Krebs said.


The fact that everytime you take down one group, more spring up is one of the reasons that we need to move it away from being profitable.

Just how we do that without causing massive internal harm is however much harder to work out.  If we simply ban paying ransoms, or make it so that paying ransoms is much harder, then we are going to see some truly spectacularly bad incidents in which critical organisations are taken down and simply do not come back up.

Our defence needs to be multi-faceted, it needs to be in depth, and it needs to hit all of the critical areas, to deter attackers, to prevent their attacks from succeeding, to punish those who do succeed and to enable organisations to recover effectively.  That's really hard to coordinate


## [Notes on GitOps potential role in compliance – James Governor's Monkchips](https://redmonk.com/jgovernor/2021/11/19/notes-on-gitops-potential-role-in-compliance/)

[https://redmonk.com/jgovernor/2021/11/19/notes-on-gitops-potential-role-in-compliance/](https://redmonk.com/jgovernor/2021/11/19/notes-on-gitops-potential-role-in-compliance/)

> A lot of the work in compliance – the job to be done – is being able to track changes to records or infrastructure. If you are providing information to auditors, or just trying to meet internally defined standards, historically you’re often running around after the fact with a spreadsheet trying to build a record or audit trail. Having a system of record in place can alleviate this overhead, and leave you doing productive work. Using GitHub or GitLab means identity and access management are effectively baked into how you work. With pull requests or merge requests, permissions are baked in. Who signed off on a change and when? That’s baked into Git-based workflows.
> 
> In systems today you often have people randomly making infrastructure changes, SSHing into servers, VMs or containers without controls in place. That’s potentially a big problem in a regulated environment. GitOps can potentially be used to enforce guardrails. Meanwhile, the vast majority of system downtime is because of configuration changes. Yet we do a frankly horrific job of tracking these changes in IT.
> 
> One of the current buzzwords making the rounds is the “software supply chain.” It’s perhaps worth thinking about actual supply chain software and the way that we’ve delivered on that. Before enterprise resource planning (ERP) systems became commonplace, data was all over the place: in spreadsheets, paper-based systems, and in separate warehousing, manufacturing, logistics, and financial systems. ERP was a packaging exercise intended to allow organizations to track everything that happened in a supply chain, with a system of record, a single source of the truth at its heart.
> 
> Git is beginning to play a similar role in software. From planning or designing a system or application changes, through to the new code, and configurations. Our source code management system has become a key source of the truth, and can reveal a host of useful metrics about team and individual performance. That same metadata could be applied to compliance reporting.
> 
> [...]
> 
> When we get to Fowler’s “Everyone Can See What’s Happening,” and “Automate Deployment,” that’s a sweet spot for GitOps. Visibility and declarative automation.
> 
> Of course we shouldn’t get carried away that GitOps is the only way to do this stuff. Fowler was writing before Git was even a thing. Some of these patterns are also common to Infrastructure as Code, and organisations already use tools like Ansible, Chef, Hashicorp and Puppet to define guardrails and support compliance initiatives in enterprise IT. Declarative configuration management, with feedback loops, is a well understood discipline.


I'm not a fan of "GitOps" as a term.  GitOps as defined here is really just talking about what DevOps was really all about, configuration as code, tracked and deployed by computers.

When we automate the operational complexity of an IT estate, we gain far more auditability, which leads to better compliance outcomes.  What we need to do is change our compliance tools to work well with our code repository, to enable a compliance view on the systems.


## [Continuous compliance on AWS | 8th Light](https://8thlight.com/blog/connor-mendenhall/2021/04/27/continuous-compliance-on-AWS.html)

[https://8thlight.com/blog/connor-mendenhall/2021/04/27/continuous-compliance-on-AWS.html](https://8thlight.com/blog/connor-mendenhall/2021/04/27/continuous-compliance-on-AWS.html)

> If you build software in a high-compliance environment like finance, health care, or insurance, you’re probably used to the audit process: a stressful time once or twice a year when your team scrambles to interpret audit requirements, collect evidence, and close findings. In many organizations, compliance audits share some of the same characteristics as the old, bad way of building software:
> 
> * Rigid requirements written without much context or collaboration. Sometimes too vague, sometimes too specific.
> * A focus on testing the system at a single point in time when the stakes are highest: the quarterly audit vs. the “big launch.”
> * A view of software systems and compliance requirements as static, even though both may have already changed by the end of the process.
> * Fear of change during the audit period.
> * When things go wrong, emphasis on who to blame rather than how to fix the system.
> 
> It doesn’t have to be this way. Automation and continuous testing solved many of these problems when it comes to building software, and they can do the same when it comes to compliance, too. Just as continuous integration and deployment are a better way of building software, continuous compliance——the practice of using automated tools to regularly check and report the compliance status of software and infrastructure——is a better way of verifying compliance for software systems.


A good list of compliance focused features for cloud users, and giving you a good start for getting started with managing compliance in a modern cloud environment.


## [About this guide | Effective IAM for AWS](https://www.effectiveiam.com/about)

[https://www.effectiveiam.com/about](https://www.effectiveiam.com/about)

> ‘Identity’ is the system you use to authenticate users and authorize them access to the AWS services and data needed to do their job. Engineers manage access to Cloud resources using the AWS Identity and Access Management service, AWS IAM.
> 
> But effective identity management is hard and getting harder.
> 
> AWS identity security is complex, the number of IAM identities are increasing, and Cloud deployments change quickly.
> 
> If you struggle to deliver effective AWS security policies or you find yourself staring at an incoherent mess of security policies in many accounts, this book is for you.
> 
> This book will help you understand why AWS IAM is hard and how to leverage IAM’s best features to secure apps & data continuously. It will help you design, develop, review, and deliver better AWS security policies, quickly and confidently.


A free book on using IAM effectively?  Yes please.

I've not had a chance to read the entire book (sorry), but the chapters I've looked through so far do a good job of explaining the options and the why of IAM, which means that even as IAM changes over time, the approaches and architectures should remain the same.


## [A Practical Guide to Continuous Compliance for Your Cloud Infrastructure [pdf]](https://cloudrail.app/wp-content/uploads/2021/11/Cloudrail-A-Practical-Guide-to-Continuous-Compliance-for-Your-Cloud-Infrastructure.pdf)

[https://cloudrail.app/wp-content/uploads/2021/11/Cloudrail-A-Practical-Guide-to-Continuous-Compliance-for-Your-Cloud-Infrastructure.pdf](https://cloudrail.app/wp-content/uploads/2021/11/Cloudrail-A-Practical-Guide-to-Continuous-Compliance-for-Your-Cloud-Infrastructure.pdf)

> Continuous infrastructure automation extends the agile and DevOps practices used in
> software development to infrastructure engineering. Think of it as CI/CD for
> infrastructure that enables you to rapidly and safely deploy your cloud environments in a
> seamless and repeatable process. Gartner predicts 70% of organizations worldwide will
> implement continuous infrastructure automation to improve business agility by 2025.
> This is a 5-step journey to help you get started with this initiative to achieve continuous
> compliance without sacrificing speed.
> 
> 1. Start with infrastructure automation by adopting Infrastructure-as-Code (IaC)
> enabling developers to become more autonomous and agile.
> 2. Add IaC to the CI/CD pipeline so you can start treating infrastructure as software
> projects for continuous integration and delivery.
> 3. Automate security validations in the pipeline to catch security violations and
> prevent security and compliance issues before deployment.
> 4. Analyze IaC with the live cloud environment to detect configuration drift and
> hidden issues.
> 5. Enforce policy to prevent security issues from making it to your environment.


This is a good getting started with continuous security and compliance using a CI/CD pipeline.


## [Laksh Raghavan on LinkedIn: My opening keynote from BSidesRDU a few weeks back. From What to](https://www.linkedin.com/posts/laraghavan_my-opening-keynote-from-bsidesrdu-a-few-weeks-activity-6866552806267068416-VZoi/)

[https://www.linkedin.com/posts/laraghavan_my-opening-keynote-from-bsidesrdu-a-few-weeks-activity-6866552806267068416-VZoi/](https://www.linkedin.com/posts/laraghavan_my-opening-keynote-from-bsidesrdu-a-few-weeks-activity-6866552806267068416-VZoi/)

> When Reed Hastings (co-CEO, Netflix - his book, “No Rules Rules” has a lot more information) noticed that purchasing/procurement process was becoming a drag on engineering velocity, he didn't "solve" the problem. He "dissolved" it. 
> 
> He figured, while >99.9% of the employees in the company are good people & not here to defraud us why are we making the entire company suffer through red tape? He empowered the engineers on the ground so that they can sign even multi-million dollar contracts. No VP signature required.  #Productivity gains and #morale boost from this process change (which is rooted in #trust) potentially pays for itself many times over, even after accounting for the fraud loss that might occur. 
> 
> Managers are not forced to approve their team members' expenses. Instead automation & auditing is used in the backend.
> 
> Error correction over prevention! 
> 
> And the best part is that they are still compliant with all the necessary regulations as a public company!
> 
> That "error correction" approach is well reflected in Jason's Security Strategy (Slide: Guardrails, not gates): "... emphasize detection & response over trying to prevent all errors". 


Automation and auditing is far better than approvals and process, and because it's all logged, checked and you can show how you deal with issues, it's all meeting compliance regulation.


## [Attackers don't bother brute-forcing long passwords, Microsoft engineer says - The Record by Recorded Future](https://therecord.media/attackers-dont-bother-brute-forcing-long-passwords-microsoft-engineer-says/)

[https://therecord.media/attackers-dont-bother-brute-forcing-long-passwords-microsoft-engineer-says/](https://therecord.media/attackers-dont-bother-brute-forcing-long-passwords-microsoft-engineer-says/)

> “I analysed the credentials entered from over >25 million brute force attacks against SSH. This is around 30 days of data in Microsoft’s sensor network,” said Ross Bevington, a security researcher at Microsoft.
> 
> “77% of attempts used a password between 1 and 7 characters. A password over 10 characters was only seen in 6% of cases,” said Bevington, who works as Head of Deception at Microsoft, a position in which he’s tasked with creating legitimate-looking honeypot systems in order to study attacker trends.
> 
> 
> Bevington says that only 7% of the brute-force attempts he analyzed in the sample data included a special character. In addition, 39% actually had at least one number, and none of the brute-force attempts used passwords that included white space.
> 
> [...]
> 
> In addition, Bevington said that based on data from more than 14 billion brute-force attacks attempted against Microsoft’s network of honeypot servers —also known as a sensor network— until September this year, attacks on Remote Desktop Protocol (RDP) servers have tripled compared to 2020, seeing a rise of 325%.
> 
> Network printing services also saw an increase of 178%, as well as Docker and Kubernetes systems, which saw an increase of 110%.


Fascinating stats on how much attackers actually scan for.

We've talked about this for a number of years, but even if the mathematics makes a password from "three simple words" lower entropy than "8 characters from upper, lower, digit and symbol". in reality it's far far less likely to be compromised. 

Passwords that are three (or better four) simple words, like "correct horse battery staple", separated with spaces, are long and difficult to brute force.  Stop insisting on password complexity like symbols, all it does is drive users to use simple to remember rules like "end my password with an exclamation mark"


## [How Threat Actors Get Into OT Systems](https://www.darkreading.com/edge-articles/how-threat-actors-get-into-ot-systems)

[https://www.darkreading.com/edge-articles/how-threat-actors-get-into-ot-systems](https://www.darkreading.com/edge-articles/how-threat-actors-get-into-ot-systems)

> There are two main vectors where malware can enter into a secure production facility in an OT environment: through the network or through removable media and devices.
> 
> Attackers can enter an OT system by exploiting cyber assets through firewalls across routable networks. Proper OT network best practices like network segmentation, strong authentication, and multiple firewalled zones can go a long way to help prevent a cyber incident.
> 
> BlackEnergy malware, utilized in the first recorded targeted cyberattack on an electrical grid, compromised an electrical company via spear-phishing emails sent to users on the IT side of the networks. From there, the threat actor was able to pivot into the critical OT network and used the SCADA system to open breakers in substations. This attack is reported to have resulted in more than 200,000 people losing power for six hours during the winter.
> 
> [...]
> 
> Now more than ever, production environments face cybersecurity threats from malicious USB devices capable of circumventing the air gap and other safeguards to disrupt operations from within. The "2021 Honeywell Industrial Cybersecurity USB Threat Report" found that 79% of threats detected from USB devices had the potential to cause disruptions in OT, including loss of view and loss of control.
> 
> The same report found that USB usage has increased 30%, while many of these USB threats (51%) tried to gain remote access into a protected air-gapped facility. Honeywell reviewed anonymized data in 2020 from its Global Analysis Research and Defense (GARD) engine, which analyzes file-based content, validates each file, and detects malware threats being transferred via USB in or out of actual OT systems.
> 
> TRITON is the first recorded use of malware being designed to attack safety systems in a production facility. A safety instrumented system (SIS) is the last line of automated safety defense for industrial facilities, designed to prevent equipment failure and catastrophic incidents such as explosions or fire. Attackers first penetrated the IT network before they moved to the OT network through systems accessible to both environments. Once in the OT network, the hackers then infected the engineering workstation for SIS with the TRITON malware. The end result of TRITON is that an SIS could be shut down and put people within a production facility at risk. 


OT systems are wildly different to typical enterprise IT systems.  Weirdly one of the things about them is that they implement many of the security mechanisms that we wish we would do more on enterprise IT.  Many OT systems have good network segregation, and try to implement airgaps and zero-trust style systems.  But the actual industrial control systems are far more difficult to patch, and of course, more secure networks means less investment in further defences.

It's worth noting that even if you put all these things in place, humans will work around them, whether bridging the airgap to make administration easier, or using USB sticks because their job requires them to.


## [Apple Sues NSO Group | Decipher](https://duo.com/decipher/apple-sues-nso-group)

[https://duo.com/decipher/apple-sues-nso-group](https://duo.com/decipher/apple-sues-nso-group)

> Apple has filed a lawsuit against NSO Group, the maker of the notorious Pegasus spyware, alleging that the company has harmed Apple’s customers as well as Apple itself by abusing “Apple services and servers to perpetrate attacks on Apple’s users”.
> 
> The lawsuit is not unprecedented--Facebook’s WhatsApp division sued NSO Group in 2019 for unauthorized access to the company’s servers, and that’s part of the legal argument that Apple is using in its complaint. Apple alleges that NSO Group created more than 100 Apple IDs and used Apple’s iCloud servers to deliver an exploit payload to target devices, which then loaded the Pegasus spyware. The delivery method relied on an exploit that researchers named FORCEDENTRY, which exploited a zero day in iOS 14.
> 
> [...]
> 
> Apple is asking the court to permanently prevent NSO Group from using any Apple devices, software, or services, and is asking for monetary damages, as well. The company said it will donate any damages it wins to organizations doing research on cyber surveillance, and it also is pledging an additional $10 million to support those research efforts. Apple also said it has begun notifying the small number of people who have been targeted by the FORCEDENTRY exploit. Some activists in Thailand have already received notifications and have posted the emails on Twitter. The notifications will consist of an email, an iMessage text, and a banner at the top of the user's account page.


This will be a lawsuit to watch, although I'd expect to see a settlement out of court and the lawsuit dropped.

Again, my biggest concern here is that NSO group is but one of several hundred companies that provide these sorts of services, and just because the number 1 company is targeted and taken down doesn't mean that the market is going to get that much smaller. 


## [IKEA email systems hit by ongoing cyberattack](https://www.bleepingcomputer.com/news/security/ikea-email-systems-hit-by-ongoing-cyberattack/)

[https://www.bleepingcomputer.com/news/security/ikea-email-systems-hit-by-ongoing-cyberattack/](https://www.bleepingcomputer.com/news/security/ikea-email-systems-hit-by-ongoing-cyberattack/)

> In internal emails seen by BleepingComputer, IKEA is warning employees of an ongoing reply-chain phishing cyber-attack targeting internal mailboxes. These emails are also being sent from other compromised IKEA organizations and business partners.
> 
> "There is an ongoing cyber-attack that is targeting Inter IKEA mailboxes. Other IKEA organisations, suppliers, and business partners are compromised by the same attack and are further spreading malicious emails to persons in Inter IKEA," explained an internal email sent to IKEA employees and seen by BleepingComputer.
> 
> "This means that the attack can come via email from someone that you work with, from any external organisation, and as a reply to an already ongoing conversations. It is therefore difficult to detect, for which we ask you to be extra cautious."
> 
> [...]
> 
> Attack used to spread Emotet or Qbot trojan
> 
> From the URLs shared in the redacted phishing email above, BleepingComputer has been able to identify the attack targeting IKEA.
> 
> Campaigns using this method have been seen installing the Qbot trojan (aka QakBot and Quakbot) and possibly Emotet based on a VirusTotal submission found by BleepingComputer.
> 
> The Qbot and Emotet trojans both lead to further network compromise and ultimately the deployment of ransomware on a breached network.


Reminder that it's not just external emails that can be bad.  If an attacker can get in, but cannot get administrative access on a users computer, they can then start to spread internally by replying to existing emails with links to their malware.

Literally, the call is coming from inside the house!


## [Observing Attacks Against Hundreds of Exposed Services in Public Clouds](https://unit42.paloaltonetworks.com/exposed-services-public-clouds/)

[https://unit42.paloaltonetworks.com/exposed-services-public-clouds/](https://unit42.paloaltonetworks.com/exposed-services-public-clouds/)

> Unit 42 researchers deployed multiple instances of remote desktop protocol (RDP), secure shell protocol (SSH), server message block (SMB) and Postgres database in the honeypot infrastructure. Researchers found that 80% of the 320 honeypots were compromised within 24 hours and all of the honeypots were compromised within a week. Some findings that stand out are:
> 
> * SSH was the most attacked application. The number of attackers and compromising events was much higher than for the other three applications.
> * The most attacked SSH honeypot was compromised 169 times in a single day.
> * On average, each SSH honeypot was compromised 26 times daily.
> * One threat actor compromised 96% of our 80 Postgres honeypots globally within 30 seconds.
> * 85% of the attacker IPs were observed only on a single day. This number indicates that Layer 3 IP-based firewalls are ineffective as attackers rarely reuse the same IPs to launch attacks. A list of malicious IPs created today will likely become outdated tomorrow.
> 
> The speed of vulnerability management is usually measured in days or months. The fact that attackers could find and compromise our honeypots in minutes was shocking. This research demonstrates the risk of insecurely exposed services. The outcome reiterates the importance of mitigating and patching security issues quickly. When a misconfigured or vulnerable service is exposed to the internet, it takes attackers just a few minutes to discover and compromise the service. There is no margin of error when it comes to the timing of security fixes.


Take these findings with a pinch of salt.  They feel somewhat accurate to other honeypot programs that I've seen, but given, as Palo Alto says, we measure "vulnerability management" (that's time to patch) in days to months, if this finding was taken at face value, it would imply that every company online would be compromised already.

Since that's not true, there's some further findings needed here.  I suspect that the issue is that in many of these cases, they are exposing "business services" (things like file shares, databases and remote-desktop) direct to the internet.  Most organisations invest in some form of VPN solution or further authentication first, and that's harder for attackers to work around.

But worth remembering that if you put SSH, RDP or SQL onto the internet direct, you should expect to be scanned and attacked within seconds.  You need to ensure it's resistant to attack before you put it online, and of course well patched if it's directly exposed.


