---
title: "254 - The real AI risk? Bad code, not just bad actors"
date: 2025-02-03
description: "It's been quite a week and I was really hoping to not talk about Deep Seek at all this week, but it sits at a really interesting nexus of thoughts around vulnerabilities and AI that has been on my mind all week."
permalink: /vulnerabilities-and-ai/
---

It's been quite a week and I was really hoping to not talk about Deep Seek at all this week, but it sits at a really interesting nexus of thoughts around vulnerabilities and AI that has been on my mind all week.

Of course, the week started with a lot of wailing and gnashing of teeth at the existential terror that a Chinese AI firm may have just jumped ahead of US based AI firms.  This caused a lot of headlines, a lot of noise and heat, and may well have some huge ramificaitons.

But we find ourselves back in a position where people judge the security of something based on the flag stuck on the box, rather than it's own internal security properties.  I've also seen a huge amount of confusion in the press this week about what AI is, how it works and what it means for there to be a "Chinese AI".

A lot of that confusion stems from the complexity of understanding the difference between the underlying weights and model that powers the AI system itself.  These are generally trained on huge corpus' of data, and one of the breakthroughs reported in the press was around whether the new model was significantly more efficient and cheaper to train that some of it's competitors.  

But above that model, there is often a company that wants to provide you with access to it, and they may host a website, a chat bot and various smart phone applications.  This website, system and the phone apps are themselves complex bits of software, and they may (and indeed, it was pretty clear, did) contain their own vulnerabilities.  There might be data protection concerns over what data is taken from the device, what the privacy policy allows, or whether the site itself is secure and storing the data in a good safe way.  

But very few of these concerns are always country related, and none of them actually had anything to do with AI.  These are all concerns that we have over our developers Integrated Development Environments, our digital whiteboards, our project management suites, and all of the services and software that we use.  We need to ensure that the software is hosted in legally compliant jurisdictions, that it protects the user data appropriately, and that it does what it says.

But we also need to be sure that the software actually does what it is supposed to, that it's not vulnerable to some form of attack.

And we have increasing evidence, a wealth of it if you read NCSC's paper on vulnerabilities, that shows that certain classes of vulnerability should be (within reason) easy and cheap to fix.

It's baffling that in 2025, we still have organisations with databases on the internet, with basic remotely exploitable SQL or OS command injection attacks, and yet we do.  Fixing that requires systemic interventions, it requires our languages, our frameworks to all work securely, by default, and it requires our software development practice to mature. 

It also requires companies to care about it, to feel like not paying attention to security means that they lose customers, lose contracts and that security investment has a return for them. 

The research that NCSC has pulled together on vulnerabilities shows that despite decades of improvements in the languages and frameworks that we use, fixing things once they are embedded is so hard.  

And that's why I think it's so important that we think about the security of the AI systems that we're building and using now.

We need to have better models for people to understand the security of AI systems, both the existing and well known systems like chat systems that we need to secure, but also a better understanding of how to secure AI enabled applications, how to separate out trusted inputs from untrusted inputs, and how AI can be misused, abused and otherwise compromised by bad actors.

None of that is easy, but it'll be easier now than in a decades time.

## [Wiz Research Uncovers Exposed DeepSeek Database Leaking Sensitive Information, Including Chat History | Wiz Blog ](https://www.wiz.io/blog/wiz-research-uncovers-exposed-deepseek-database-leak)

[https://www.wiz.io/blog/wiz-research-uncovers-exposed-deepseek-database-leak](https://www.wiz.io/blog/wiz-research-uncovers-exposed-deepseek-database-leak)

> Our reconnaissance began with assessing DeepSeek’s publicly accessible domains. By mapping the external attack surface with straightforward reconnaissance techniques (passive and active discovery of subdomains), we identified around 30 internet-facing subdomains. Most appeared benign, hosting elements like the chatbot interface, status page, and API documentation—none of which initially suggested a high-risk exposure. 
> 
> However, as we expanded our search beyond standard HTTP ports (80/443), we detected two **unusual, open ports (8123 & 9000)** Upon further investigation, these ports led to a **publicly exposed ClickHouse database** , accessible without any authentication at all – immediately raising red flags.  
> 
> By leveraging ClickHouse’s HTTP interface, we accessed the /play path, which **allowed direct execution of arbitrary SQL queries** via the browser. 


This is a bad breach, and it was discovered very simply and easily through basic attack surface scanning.  This is why it is so important to scan yourself as much as possible, conduct domain discovery, and make sure that you know as much about your external attack surface as your adversaries do. 


## [Adversarial Misuse of Generative AI | Google Cloud Blog ](https://cloud.google.com/blog/topics/threat-intelligence/adversarial-misuse-generative-ai)

[https://cloud.google.com/blog/topics/threat-intelligence/adversarial-misuse-generative-ai](https://cloud.google.com/blog/topics/threat-intelligence/adversarial-misuse-generative-ai)

> Much of the current discourse around cyber threat actors' misuse of AI is confined to theoretical research. While these studies demonstrate the potential for malicious exploitation of AI, they don't necessarily reflect the reality of how AI is currently being used by threat actors in the wild. To bridge this gap, we are sharing a comprehensive analysis of how threat actors interacted with Google's AI-powered assistant, Gemini. Our analysis was grounded by the expertise of Google's Threat Intelligence Group (GTIG), which combines decades of experience tracking threat actors on the front lines and protecting Google, our users, and our customers from government-backed attackers, targeted 0-day exploits, coordinated information operations (IO), and serious cyber crime networks.
> 
> […]
> 
> Rather than enabling disruptive change, generative AI allows threat actors to move faster and at higher volume. For skilled actors, generative AI tools provide a helpful framework, similar to the use of Metasploit or Cobalt Strike in cyber threat activity. For less skilled actors, they also provide a learning and productivity tool, enabling them to more quickly develop tools and incorporate existing techniques. However, **current LLMs on their own are unlikely to enable breakthrough capabilities for threat actors** . **We note that the AI landscape is in constant flux, with new AI models and agentic systems emerging daily. As this evolution unfolds, GTIG anticipates the threat landscape to evolve in stride as threat actors adopt new AI technologies in their operations** . 


This is a great report from a team that has both highly capable threat intelligence teams that understand how to track a variety of bad actors, as well as hosting their own AI capabilities.  This puts them in an unusual position of being able to see what those bad actors are doing with their AI to determine the use and impact.

Of note is that broadly speaking, lots of doomsday scenarios are simply not happening so far.  Instead actors are using AI to accelerate their research work, augment their ability to debug, manage and write tools, and improve the way they work.  Jailbreaking the AI itself and novel attacks directly using the AI have not materialised … _yet_ 


## [A method to assess 'forgivable' vs 'unforgivable'... - NCSC.GOV.UK ](https://www.ncsc.gov.uk/report/a-method-to-assess-forgivable-vs-unforgivable-vulnerabilities)

[https://www.ncsc.gov.uk/report/a-method-to-assess-forgivable-vs-unforgivable-vulnerabilities](https://www.ncsc.gov.uk/report/a-method-to-assess-forgivable-vs-unforgivable-vulnerabilities)

> The NCSC’s analysis seeks to identify the **root cause** of vulnerabilities (opposed to the details provided in the individual vulnerability advisory), using the CWE Top 25 Most Dangerous Software Releases for 2023. Having identified 11 top-level mitigations required to manage these vulnerabilities, we assigned an ‘ease of implementation' score to each top-level mitigation, based on:
> 
> * direct and indirect costs
> * knowledge (that is, how widely known and understood is the mitigation)
> * technical feasibility
> 
> Researchers can then assess an individual vulnerability, and use the ‘ease of implementation’ scores (which we classify as ‘easy’, ‘medium’ or ‘hard’ to implement) to assess how difficult it is to apply the mitigations. Vulnerabilities with ‘easy’ mitigations are declared ‘unforgivable'.
> 
> Most of the 13 ‘unforgivable vulnerabilities’ mentioned in the original MITRE 2007 paper still exist in one form or another. At the core of our research is the desire to eradicate vulnerability classes and make the top-level mitigations easier to implement. 


There’s a lot to like about this paper, the depth of analysis into common weaknesses, contrasting that with commonly exploited vulnerabilities and attempts at looking at cost of implementation are all great, and this is a brilliant start to a wider conversation about whether we accept certain coding practices as normal.

I really struggle however, with the term “unforgivable vulnerabilities”, and I’m disappointed to see it repeated from the original academic research.  I don’t feel like it hits the right tone for setting a “just culture” when it comes to cybersecurity.     It’s important to note that while “Just Culture” approaches come from Safety systems and have been applied in a number of critical places, it doesn’t mean that there’s never any blame, rather that we look at systemic failings rather than just individual culpability.  We as a population know that it’s possible to avoid certain classes of software vulnerabilities, and at that point, someone has chosen not to do so.  It doesn’t automatically put blame on the individual, but instead makes us question why the creator chose not to avoid the hazard in their sights. 

I think a better term might be to talk about “avoidable vulnerabilities”, indicating that we think that they could have been avoided, but the creator either couldn’t, or chose not to.

I think it’s right that we attempt to shift the system to be secure by default, and I think we need to be clear where we think there is a lack of care or attention to security upstream of us, in our vendors, our technology providers or even our open source libraries.  This analysis does well to start to help quantify that, but the language really doesn’t help demonstrate the level of thought behind this piece of research.


## [Code of Practice for the Cyber Security of AI - GOV.UK ](https://www.gov.uk/government/publications/ai-cyber-security-code-of-practice/code-of-practice-for-the-cyber-security-of-ai)

[https://www.gov.uk/government/publications/ai-cyber-security-code-of-practice/code-of-practice-for-the-cyber-security-of-ai](https://www.gov.uk/government/publications/ai-cyber-security-code-of-practice/code-of-practice-for-the-cyber-security-of-ai)

> The proposed intervention was endorsed by 80% of respondents to the Department for Science, Innovation and Technology’s (DSIT) [Call for Views](https://www.gov.uk/government/calls-for-evidence/cyber-security-of-ai-a-call-for-views) which was held from 15 May to 9 August 2024. Support for each principle in the Code ranged from 83% to 90%. This document also builds on NCSC’s [Guidelines for Secure AI Development](https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development) which were published in November 2023 and endorsed by 19 international partners. As set out in DSIT’s [modular approach to cyber security codes of practice](https://www.gov.uk/government/collections/cyber-security-codes-of-practice) , AI stakeholders should view this document as an addendum to the Software Code of Practice. 


This is a simple, no-nonsense, and consensus driven view on the practices expected not just of AI model developers themselves, but in companies adopting and embedding AI in their tools, and the data owners who are engaging AI tools on their data. 


## [CRON#TRAP: Emulated Linux Environments as the Latest Tactic in Malware Staging - Securonix ](https://www.securonix.com/blog/crontrap-emulated-linux-environments-as-the-latest-tactic-in-malware-staging/)

[https://www.securonix.com/blog/crontrap-emulated-linux-environments-as-the-latest-tactic-in-malware-staging/](https://www.securonix.com/blog/crontrap-emulated-linux-environments-as-the-latest-tactic-in-malware-staging/)

> The Securonix Threat Research team has been tracking an intriguing attack campaign that leverages a malicious shortcut (.lnk) file. When executed, this file extracts and initiates a lightweight, custom Linux environment emulated through QEMU.
> 
> What makes the CRON#TRAP campaign particularly concerning is that the emulated Linux instance comes pre-configured with a backdoor that automatically connects to an attacker-controlled Command and Control (C2) server. This setup allows the attacker to maintain a stealthy presence on the victim’s machine, staging further malicious activity within a concealed environment, making detection challenging for traditional antivirus solutions. Since QEMU is legitimate software, often used in development and research, its presence typically won’t trigger any security alarms. 


I thought this was interesting.  We’ve seen this a few times before, but not that often.  Shipping a virtual machine means that it’s likely that local antivirus and malware tools wont detect what is going on inside the virtual machine, and if it’s bound to the host with sufficient permissions, it may well be able to attack the machine directly.

My only query on this would be that while QEMU might be used by development or research teams, it’s use isn’t exactly commonplace, and it may well be worth detecting it’s use anywhere outside of normal environments. 


## [Cyber threat to UK government is severe and advancing quickly, spending watchdog finds - NAO press release ](https://www.nao.org.uk/press-releases/cyber-threat-to-uk-government-is-severe-and-advancing-quickly-spending-watchdog-finds/)

[https://www.nao.org.uk/press-releases/cyber-threat-to-uk-government-is-severe-and-advancing-quickly-spending-watchdog-finds/](https://www.nao.org.uk/press-releases/cyber-threat-to-uk-government-is-severe-and-advancing-quickly-spending-watchdog-finds/)

> The cyber threat to UK government is severe and advancing quickly; government must act now1 to protect its own operations and key public services, according to a new report published by the public spending watchdog.
> 
> The National Audit Office (NAO) evaluated2 whether government was keeping pace with the rapidly evolving cyber threat it faces from hostile actors.
> 
> […]
> 
> If successful, cyber attacks4 can have devastating effects on government organisations, public services, and people’s lives. In June 2024, a cyber attack on a supplier of pathology services to the NHS in south-east London led to two NHS foundation trusts postponing 10,152 acute outpatient appointments and 1,710 elective procedures. The British Library, which experienced a cyber attack in October 2023, has already spent £600,000 rebuilding its services and expects to spend many times more as it continues its recovery work.
> 
> Successive governments have been working for at least a decade to build the UK’s cyber resilience, including publishing a strategy for improving government organisations’ cyber security in January 2022. This strategy included a target for key government organisations to be “significantly hardened to cyber attack by 2025”. But government has not improved its cyber resilience fast enough to meet this aim. 


This is a key report and milestone in the UK Governments cyber security journey.  It ratifies and reinforces the core strategy, while saying that it’s not being implemented fast enough. 


## [The Mac Malware of 2024 👾A comprehensive analysis of the year's new macOS malware ](https://objective-see.org/blog/blog_0x7D.html)

[https://objective-see.org/blog/blog_0x7D.html](https://objective-see.org/blog/blog_0x7D.html)

> For what is now the 9th year in a row, I’ve put together a blog post that comprehensively covers all the new Mac malware that emerged throughout the year.
> While the specimens may have been reported on before (for example by the anti-virus/security company that discovered them), this blog aims to cumulatively and comprehensively cover **_all_** the new Mac malware of 2024 - in much technical detail, all in one place …yes, with samples available for download!
> 
> After reading this blog post you will have a thorough and comprehensive understanding of latest threats targeting macOS. This is especially important as Macs continue to flourish, with researchers at MacPaw’s Moonlock Lab [**noting**](https://moonlock.com/moonlock-2024-macos-threat-report) a “ _60 percent increase [of macOS] in market share in the last 3 years alone_ ”. 


This is a lovely review of mac malware.  Long, comprehensive and with links out to various writeups and even malware samples.  
If you work in development, you’ll know how popular Macs are, and engineers often talk about how little malware there is for Mac, but that’s changing, so worth making sure you have the ability to detect and block this stuff 


## [Police seizes Cracked and Nulled hacking forum servers, arrests suspects ](https://www.bleepingcomputer.com/news/security/police-seizes-cracked-and-nulled-hacking-forum-servers-arrests-suspects/)

[https://www.bleepingcomputer.com/news/security/police-seizes-cracked-and-nulled-hacking-forum-servers-arrests-suspects/](https://www.bleepingcomputer.com/news/security/police-seizes-cracked-and-nulled-hacking-forum-servers-arrests-suspects/)

> Europol and German law enforcement confirmed the arrest of two suspects and the seizure of 17 servers in Operation Talent, which took down Cracked and Nulled, two of the largest hacking forums with over 10 million users.
> 
> Even though some of their members are also engaged in ethical hacking discussions, these hacking forums are best known for focusing on cybercrime, password theft, cracking, and credential-stuffing attacks and were widely regarded as a hub for cybercriminal activity,
> 
> They also hosted hacking tools, such as AI-based tools and scripts that help scan for security vulnerabilities and optimize attacks, "configs" used by credential-stuffing attack tools (e.g., OpenBullet and SilverBullet), and other illicit activities, including content related to software cracks and a "combo lists" marketplace with stolen credentials or databases. 


Always tricky to know which side of the law “information sharing platforms” are, but in these cases, large lists of breached credentials, malware samples and almost certainly under-the-counter deals happen on these sites.  These shutdowns likely will make us safer, reducing the ease at which criminals can share information, tools and accesses with each other. 


## [TeamViewer Patches High-Severity Vulnerability in Windows Applications - SecurityWeek ](https://www.securityweek.com/teamviewer-patches-high-severity-vulnerability-in-windows-applications/)

[https://www.securityweek.com/teamviewer-patches-high-severity-vulnerability-in-windows-applications/](https://www.securityweek.com/teamviewer-patches-high-severity-vulnerability-in-windows-applications/)

> TeamViewer this week announced patches for a high-severity elevation of privilege vulnerability in its remote access solutions for Windows.
> 
> Tracked as CVE-2025-0065 (CVSS score of 7.8), the bug is described as an improper neutralization of argument delimiters in the ‘TeamViewer_service.exe’ component of the software.
> 
> Successful exploitation of the security defect, TeamViewer warns, could allow an unprivileged attacker with local access to a Windows system to perform argument injection and elevate their privileges.
> 
> “To exploit this vulnerability, an attacker needs local access to the Windows system,” TeamViewer underlines in its [advisory](https://www.teamviewer.com/en/resources/trust-center/security-bulletins/tv-2025-1001/) . 


TeamViewer is one of those tools that comes up over and over again in breaches, but often not as a direct cause of the breach.  Many organisations treat tools like TeamViewer as if it’s the security boundary, so it may well be exposed to the internet. 
A simple search of Shodan shows huge numbers of these open to attack.  Of course, breaches start by someone either getting a credential or  a way to bypass the credential, and then they use tools like TeamViewer to move laterally in the system. Turning this into a tool for escalation of privilege at the same time is not great, so you should patch this pretty urgently if possible 


## [A Brief Guide for Dealing with ‘Humanless SOC’ Idiots | by Anton Chuvakin | Anton on Security | Jan, 2025 | Medium ](https://medium.com/anton-on-security/a-brief-guide-for-dealing-with-humanless-soc-idiots-3c2f1a5b26e9)

[https://medium.com/anton-on-security/a-brief-guide-for-dealing-with-humanless-soc-idiots-3c2f1a5b26e9](https://medium.com/anton-on-security/a-brief-guide-for-dealing-with-humanless-soc-idiots-3c2f1a5b26e9)

> Anyhow, let’s look at the extreme fringe of a fringe. You may meet people who think that artificial intelligence today is so advanced that human presence inside the SOC is not necessary. Today! They actually think AI can already replace all humans in a SOC! Some of them even have a demo ready, powered by … ahem … “a demo-ready AI” that works — you guessed it! — in a demo. Sadly, it will never deliver even a tiny fraction of the promised benefits once **confronted with a real-world, messy environments full of outdated systems, API-less data stores, tribal knowledge, junior IT people, and sprinkled with human incompetence…** Similarly, **some people have never seen how a large enterprise functions** , so they make assumptions about automation possibilities that are just wildly off. They struggle to grasp the complexity of a “typical” (ha! as if!) enterprise “layered cake” environment, with its layers of technology ranging from 1970s mainframes to modern serverless and gen AI systems. 


I enjoyed this rant, especially these lovely reminders of the context and technology platform facing most organisations.  In reality in almost all major enterprises, there are is a mess of systems, networks and decisions taken over the years.  Any new proposal for new projects and services need to recognise that complexity and decide what complexity it will interact with, and what it’ll declare out of scope. 


