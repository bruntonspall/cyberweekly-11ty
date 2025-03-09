---
title: "249 - We rely on people, but do we look after them?"
date: 2024-05-19
description: "Over a career spaning some 25 years, I've learned multiple programming languages, I've learned complex API's, memory management techniques, implemented mathmatical algorithms, led teams building systems at scale, and worked to defend systems from advanced cyber adversaries, and throughout all of that, the focus has almost relentlessly been on the technology and the platforms. "
permalink: /we-rely-on-people-but-do-we-look-after-them/
---

Over a career spaning some 25 years, I've learned multiple programming languages, I've learned complex API's, memory management techniques, implemented mathmatical algorithms, led teams building systems at scale, and worked to defend systems from advanced cyber adversaries, and throughout all of that, the focus has almost relentlessly been on the technology and the platforms. 

We say that people are our first line of defence, and we build systems to meet user needs, and to defend against individuals clicking links they shouldn't, downloading and executing code they shouldn't or configuring systems in the way that they shouldn't, but we rarely spend enough time actually thinking about the humans in the midst of this complex system.

One of the most impactful videos in this space that I've ever watched is [Nickolas Means on "Who Destroyed Three Mile Island"](https://www.youtube.com/watch?v=1xQeXOz0Ncs), which is a great storytelling deep dive into the essence of the sociotechnical systemic failings that caused the meltdown of a nuclear reactor.  I've been aware of the concepts of human factors, safety systems and sociotechnical systems for a long time, but this talk from back in 2018 works as one of the best simple introductions to this deep and complex area.

In 2024, I think that cybersecurity and technology is having a bit of a moment in these spaces.  For years people have been warning that too much of our modern technolgoy infrastructure is reliant on a remarkably small number of critical actors, many of whom don't get paid enough or treated well enough for the responsibility put on them.  These super-powered individuals might be individual contributors to open source projects that are included in almost all the software we run today, they mgiht be the network administrators who manage core internet routing tables, or they might be engineers, politicians, journalists.  Whoever they are, it's common to recognise that most human endeavours have a very small field of experts in them, and that creates a gap around the resilience within a field.

There are lots of systemic and social reasons why this might be, and I can't really speak to any career that isn't the one that I've walked through, but within that software engineering community, there is something slightly odd about how we build and develop careers.  When I started my career, your choice was essentially limited to one career defining role, you could get promoted, overseeing increasingly large teams until you became a manager of people and nobody let you do anything technical anymore.   Being a "principle developer" or a "software engineering fellow" wasn't really a career choice that people could work towards.  Over the last two decades, most companies that have significant numbers of software engineers has started to recognise that it wants to grow and retain those individual experts without making them sad that they have to manage people (and frequently, their reports sad that they're managed by someone without the training, skills or desire to be a good manager).  

Career paths now exist that mean that engineers can become individual contributors or engineering managers and frequently that they can switch between those roles as their life, interests and needs change.

But we're still missing something in our education in that career path.  If I go look at technical training courses, or cybersecurity courses, I can see thousands of varients of courses that teach you reverse engineering, windows internals, data science and analysis, microservice architectures at scale.  But if I go looking for courses on how to manage humans, how to build a culture of respect, how to develop user centered software that respects the user, I'm down to just a very small number of individual experts, or I'm heading back to HR courses that feel like they were written in the 80's when everyone sat in an office and typed out reports.

If we really truly believe that user centered software is the key to humanity, if we believe that open source software built by communities that span the globe are key to our modern infrastructure, if we believe that humans are the first and last lines of defence in our cybersecurity, then we need to ensure that as an entire community, we demand better training in what it means to engage with humans, what drives them, and how we can build, sustain and develop communities, treating each other well and understanding the role of humans in our technical systems.

If you haven't watched the video above or paid attention to human factors and sociotechnical systems, then maybe take a bit of time and think about how much of your time is spent dedicated to the humans that are part of the systems you build

## [Bullying in Open Source Software Is a Massive Security Vulnerability ](https://www.404media.co/xz-backdoor-bullying-in-open-source-software-is-a-massive-security-vulnerability/)

[https://www.404media.co/xz-backdoor-bullying-in-open-source-software-is-a-massive-security-vulnerability/](https://www.404media.co/xz-backdoor-bullying-in-open-source-software-is-a-massive-security-vulnerability/)

> In that thread, the now-banned developer who wanted to push code that would have added a vulnerability repeatedly demanded that their new feature be integrated into the live product immediately. As Steiner said, the new feature would have changed how people searched for apps on F-Droid. The potentially malicious user argued “the search results are pretty unusable currently,” and proposed new code. Over the course of months, that user kept writing things like “do we want to merge now?,” meaning push the code live and “I’d really like for this to get into the next release.”
> 
> When other users, including Steiner, pointed out that they still needed to review the code, tweak it, or make adjustments to improve its functionality, the original user became angry, and other users backed the original poster.
> 
> One other user, for example, argued “I’d like to get this merged for a release soon … is this perfect? No, but it doesn’t need to be. It just needs to be better than what we have now.”
> 
> “The second big reason why I think this should be merged soon, is about encouraging new contributors,” the person arguing for inclusion added. “And not by saying ‘we welcome contributions’ and then never allowing any changes because they are not perfect. If people never get anything merged they'll most likely never spend any more time diving deeper into the codebase and tackling more complex tasks later on.”
> 
> […]
> 
> The original poster continued to pressure Steiner and other maintainers of the code, and eventually wrote “nah man, I’m tired of this … I'm not coming back to this project until I see that contributions made in good faith are welcomed instead of fought every step of the way.”
> 
> When Steiner was finally able to audit the code, he found that it would have introduced a vulnerability that would have allowed for SQL injections, which is a very basic type of hack that could have crashed the app and would have also potentially introduced other problems. Steiner wrote at the time that he was unsure whether this was actively malicious or just sloppy, but noted that it was a “security risk” either way.
> 
> “I wonder if this was an attempt to insert a SQL injection vuln? Or am I just paranoid?,” he wrote. “Anyone know anything about the original submitter?”
> 
> Steiner wrote this week that the original coder deleted their account as soon as F-Droid’s maintainers attempted to review the code, and that he thinks that the user’s behavior, as well as “all the attention from random new accounts” has led him to believe “it could be a deliberate attempt to insert the vuln.” 


One of the things that makes the XZ attack so worrying is that it’s incredibly difficult to distinguish a social engineering attack on open source maintainers from just the existing culture that we get on online forums and github pull requests.  

The reality of allowing people to comment means that random people do turn up and argue, in good faith, for certain features to exist, for bugs to be fixed, and for code to be merged and the communities to be welcoming.  The pressure on single maintainers means that there’s always a desire to allow and encourage the vocal members of the community to be appeased and welcomed because they are seen as active contributors to the community.

There are no good solutions here, you can draw up stronger walls around communities, but to a dedicated and potentially state funded adversary, they’re not going to deter the attackers, but will make building and developing your community harder.  You can keep things open, but when you can’t tell whether any given commenter ontline is in fact a dog or not, then it’s hard to work out what a healthy community looks like.  Stronger community guidelines feels natural here, but open source software is worldwide and culture mismatches about appropraite and acceptable behaviour also creates difficulty definining a globally acceptable rules of the road. 


## [The Trident Model of Career Development ](https://www.patkua.com/blog/the-trident-model-of-career-development/)

[https://www.patkua.com/blog/the-trident-model-of-career-development/](https://www.patkua.com/blog/the-trident-model-of-career-development/)

> More modern tech companies often use a two-track career ladder, one called the **Management track** and another called the **Individual Contributor (IC) track** . Two tracks are generally better than one because those companies who have only single track force people to take on management roles when they don’t want to or shouldn’t in order to earn more recognition or compensation. While two tracks are great, I see great problems by calling the second track an **IC track** because it overemphasises the idea of individual contribution, when most organisations want and need technical leadership. You can see this focus in Will Larson’s [Staff Engineer book](https://staffeng.com/book/) which calls out “Leadership beyond the management track.”
> 
> […] 
> 
> **The Technical Leadership Track** 
> 
> In this track, people spend a majority of their time (70-80%) leading people on a technical topic. People in this track **must** have relevant hands-on technical skills and experience. They should have good but not necessarily the best skills in the team they are leading. People in this track draw heavily on refined leadership skills to be successful. Classic activities for this role (in the field of software) include:
> 
> * Establishing a Technical Vision
> * Managing technical risks
> * Clarifying/uncovering technical requirements
> * Ensuring non-technical stakeholders understand technical constraints, trade-offs or important decisions
> * Growing technical knowledge and cultivating knowledge sharing in and across teams 
> 
> **Example roles in this track:** Lead Developer, Tech Lead, Principal Engineer, Software Architect. Also [three of the Staff Engineer archetypes](https://staffeng.com/guides/staff-archetypes/) fit well on this track including the Tech Lead, Architect and Right Hand archetype. 


I like this trident model because I think we create a false dichotemy for engineers that you are either a code wizard or a management suit.  But this middle track, showing technical leadership, an ability to see the bigger picture, but still being highly technical as suited to a number of people I’ve worked with who regret moving away from their technical IC track.  They may never have been the best and brightest at the actual engineering, but that combination of technical talent good enough to direct, and management skills good enough to lead can otherwise result in senior engineer burnout. 


## [Why can’t I focus? ](https://peterszasz.com/why-cant-i-focus/)

[https://peterszasz.com/why-cant-i-focus/](https://peterszasz.com/why-cant-i-focus/)

> I used to find myself saying “I just have too many things going on now”. And it was true, to some extent — but in reality, the root causes of spreading my attention too thin across multiple areas often laid within me. The urge to do a good job, please stakeholders and avoid conflicts can lead to overcommitting. As a result of having multiple parallel projects, all became at risk of being late.
> 
> This situation made focusing hard, not just as a result of necessary context switches, but also because of this general cloud of stress that came from setting myself up for failure. 
> 
> **What to do about it?** 
> 
> Recognizing my limits and saying no to most of the things I could be doing, to be able to deliver on the few most important ones is hard — because the things I’m saying “no” to are often similarly important, impactful, or just interesting projects. Yet, it’s the only way to do meaningful, focused work on key areas.
> 
> When planning my time, I learned to aim for a sustainable series of projects delivered, replacing the need to parallelize everything. By sustainable I mean planning with some slack, understanding the inherent optimism of estimations, and concentrating on completion, with [timeboxing](https://www.jeremybrown.tech/22-timeboxing-the-project-delivery-superpower/?ref=peterszasz.com) if needed, to maintain efficiency. Explicit daily and weekly goals make this process easier.
> 
> […]
> 
> Another tool that can help avoid chasing ideas down rabbit holes and staying on the topic at hand is to have a process for the immediate capture of new ideas. In the Getting Things Done methodology, an "inbox" serves as a central collection point for capturing all incoming tasks, ideas, and commitments. The purpose of this is to prevent mental clutter by providing a designated, trusted, always available space to capture incoming information. I found that having an open notebook next to me at all times and being disciplined to capture attractive ideas immediately to offload from my brain and consider later is a great help to focus. 


This is written from an engineers perspective, and naturally as a manager, I am required to juggle multiple things at once, but even still I find myself juggling 10x the number of things I should, primarily because it’s so difficult to say no to something that I totally can do, that I’d be great at doing, that I’d be fast and efficient at doing, but in reality, someone else should do.

I want to help, I want to be useful, but recognising within ourselves that even if we could do something, maybe we shouldn’t do the thing is incredibly powerful thing to learn and practice. 


## [Learning from the mistakes of others - A retrospective review | Phishing | ICO ](https://ico.org.uk/about-the-ico/research-reports-impact-and-evaluation/research-and-reports/learning-from-the-mistakes-of-others-a-retrospective-review/phishing/)

[https://ico.org.uk/about-the-ico/research-reports-impact-and-evaluation/research-and-reports/learning-from-the-mistakes-of-others-a-retrospective-review/phishing/](https://ico.org.uk/about-the-ico/research-reports-impact-and-evaluation/research-and-reports/learning-from-the-mistakes-of-others-a-retrospective-review/phishing/)

> 56% of businesses and 62% of charities that reported having had breaches or attacks in the past 12 months, felt phishing attacks were the most disruptive types of attack that organisations face. This is according to the most recent UK government [cyber security breaches survey](https://www.gov.uk/government/statistics/cyber-security-breaches-survey-2023/cyber-security-breaches-survey-2023#chapter-4-prevalence-and-impact-of-breaches-or-attacks) . It also showed that the percentage of phishing attacks was on the rise. 79% of businesses identified having had a phishing attack in the last 12 months, compared to 72% in 2017.
> 
> Proofpoint’s [State of the phish report](https://www.proofpoint.com/us/resources/threat-reports/state-of-phish?utm_source=google#x26;utm_medium=cpc&) revealed a higher percentage still. 91% of UK companies responding to their survey stated they had experienced at least one successful email-based phishing attack in 2022. More than a quarter of those (26%), also reported direct financial losses as result. 


This report is great at summarising incidents and breaches from the last few years and the trends that the UK’s Information Commissioner sees when companies report breaches.

As a reminder, these stats on Phishing sound incredibly stark, and they are incredibly stark.  But if you build your systems right, someone clicking a link on a phishing email should result in little to no impact on your data and your staff.

If 91% of companies are having successful phishing attacks launched at them, then you need to build your systems in an “assume compromised” mentatility, and ensure that a user handing over their username and password, or otherwise clicking a link must not expose the system to wider impact.  Phish proof MFA, pre-email detonation and good endpoint detection and response systems can all massively lower the impact of a phish without worrying about the increasing liklihood 


## [How an empty S3 bucket can make your AWS bill explode | by Maciej Pocwierz | Apr, 2024 | Medium ](https://medium.com/@maciej.pocwierz/how-an-empty-s3-bucket-can-make-your-aws-bill-explode-934a383cb8b1)

[https://medium.com/@maciej.pocwierz/how-an-empty-s3-bucket-can-make-your-aws-bill-explode-934a383cb8b1](https://medium.com/@maciej.pocwierz/how-an-empty-s3-bucket-can-make-your-aws-bill-explode-934a383cb8b1)

> Imagine you create an empty, private AWS S3 bucket in a region of your preference. What will your AWS bill be the next morning?
> 
> A few weeks ago, I began working on the PoC of a document indexing system for my client. I created a single S3 bucket in the _eu-west-1_ region and uploaded some files there for testing. 
> 
> Two days later, I checked my AWS billing page, primarily to make sure that what I was doing was well within the free-tier limits. Apparently, it wasn’t. My bill was over _1300$_ , with the billing console showing nearly _100,000,000 S3 PUT requests_ executed within just one day!
> 
> […]
> 
> Was it some kind of DDoS-like attack against my account? Against AWS? As it turns out, **one of the popular open-source tools had a default configuration to store their backups in S3. And, as a placeholder for a bucket name, they used… the same name that I used for my bucket** . This meant that every deployment of this tool with default configuration values attempted to store its backups in my S3 bucket!
> 
> > Note: Unfortunately, I can’t disclose the name of the tool I’m referring to, as doing so would put the impacted companies at risk (as explained further).
> 
> So, a horde of unauthorized third parties is attempting to store their data in my private S3 bucket. But why should I be the one paying for this mistake? Here’s why: 


Use this as a good reminder about the power of defaults.  The defaults in your configuration or application should work as expected, or fundementally not work.  Pointing stuff at an unused domain name and hoping nobody registers it is not a path for success. 


## [Inside the 2024 Threat Detection Report - Red Canary ](https://redcanary.com/blog/2024-threat-detection-report/)

[https://redcanary.com/blog/2024-threat-detection-report/](https://redcanary.com/blog/2024-threat-detection-report/)

> As the technology that we rely on to conduct business continues to evolve, so do the threats that we face. Here are some of our key findings:
> 
> * Everyone is migrating to the cloud, including bad guys: [**Cloud Accounts**](https://redcanary.com/threat-detection-report/techniques/cloud-accounts/) was the fourth most prevalent ATT&CK technique we detected this year, increasing 15-fold in detection volume and affecting three times as many customers as last year.
> * Despite a spate of new [**CVEs**](https://redcanary.com/threat-detection-report/trends/vulnerabilities/) , humans remained the primary vulnerability that adversaries took advantage of in 2023. Adversaries used [**compromised identities**](https://redcanary.com/threat-detection-report/trends/identity-attacks/) to access [**cloud service APIs,**](https://redcanary.com/threat-detection-report/trends/api-abuse/) execute payroll fraud with [**email forwarding rules**](https://redcanary.com/threat-detection-report/techniques/email-forwarding-rule/) , launch [**ransomware attacks**](https://redcanary.com/threat-detection-report/trends/ransomware/) , and more.
> * While both defenders and cybercriminals have discovered use cases for generative [**artificial intelligence**](https://redcanary.com/threat-detection-report/trends/ai-cybersecurity/) (GenAI), we see defenders as having the edge.
> * Container technology is omnipresent, and it’s as important as ever to secure your [**Linux systems**](https://redcanary.com/threat-detection-report/techniques/kernel-modules-and-extensions/) to prevent adversaries from [**escaping to host systems**](https://redcanary.com/threat-detection-report/techniques/container-escapes/)
> 


This one is old, but another reminder that attackers change their methods to adapt to how our systems and people work.  As we adopt new technologies, we need security teams to keep up to date on how they are being used and ensure that we understand how attackers might look at them.


## [Advanced Cyber Threats Impact Even the Most Prepared ](https://medium.com/mitre-engenuity/advanced-cyber-threats-impact-even-the-most-prepared-56444e980dc8)

[https://medium.com/mitre-engenuity/advanced-cyber-threats-impact-even-the-most-prepared-56444e980dc8](https://medium.com/mitre-engenuity/advanced-cyber-threats-impact-even-the-most-prepared-56444e980dc8)

> In April 2024 we confirmed that MITRE was subject to an intrusion into one of our research and prototyping networks. MITRE’s security team immediately began an investigation, cut off all known access to the threat actor, and brought in third-party Digital Forensics Incident Response teams to perform their own independent analysis alongside our in-house experts.
> 
> Our top priority is to share our experience to help inform others facing similar threats. Even though MITRE’s investigation into the incident is still ongoing, we felt it important to share an overview on our work to date and importantly, what’s next.
> 
> You can learn a lot from being hacked, and that knowledge can transform an entire industry. Fifteen years ago was the last time we suffered a major cyber incident and it was a seminal moment for MITRE. It crystalized for us the importance of understanding a hacker’s behavior as a means to defeat them. It motivated creating behavioral taxonomies that catalog adversary TTPs, which ultimately led to the creation of [MITRE ATTACK®](https://attack.mitre.org/) . This further gave rise to the concept of adversary engagement to elicit more behavioral data, now part of [MITRE ENGAGE™](https://engage.mitre.org/) . 
> 
> **Incident Overview** 
> 
> Starting in January 2024, a threat actor performed reconnaissance of our networks, exploited one of our Virtual Private Networks (VPNs) through two [Ivanti Connect Secure zero-day vulnerabilities](https://www.volexity.com/blog/2024/01/10/active-exploitation-of-two-zero-day-vulnerabilities-in-ivanti-connect-secure-vpn/) , and skirted past our multi-factor authentication using session hijacking. From there, they moved laterally and dug deep into our [network’s VMware infrastructure](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-post-exploitation-lateral-movement) using a compromised administrator account. They employed a combination of sophisticated backdoors and webshells to maintain persistence and harvest credentials.
> 
> MITRE followed best practices, vendor instructions, and the government’s advice to [upgrade, replace, and harden our Ivanti system](https://www.cisa.gov/news-events/directives/ed-24-01-mitigate-ivanti-connect-secure-and-ivanti-policy-secure-vulnerabilities) , but we did not detect the lateral movement into our VMware infrastructure. At the time we believed we took all the necessary actions to mitigate the vulnerability, but these actions were clearly insufficient. 


This is an interesting writeup, and valuable.  It’s always nice to see people being open about potential attacks and what caused them.  There’s not a lot you can do against a zero-day being used on you, but there is a lot to learn from what happened next, and whether the attack could have been stopped, detected or mitigated after the zero-day but before damage. 


## [Millions of Malicious 'Imageless' Containers Planted on Docker Hub Over 5 Years ](https://thehackernews.com/2024/04/millions-of-malicious-imageless.html)

[https://thehackernews.com/2024/04/millions-of-malicious-imageless.html](https://thehackernews.com/2024/04/millions-of-malicious-imageless.html)

> "Over four million of the repositories in Docker Hub are imageless and have no content except for the repository documentation," JFrog security researcher Andrey Polkovnichenko [said](https://jfrog.com/blog/attacks-on-docker-with-millions-of-malicious-repositories-spread-malware-and-phishing-scams/) in a report shared with The Hacker News.
> 
> What's more, the documentation has no connection whatsoever to the container. Instead, it's a web page that's designed to lure users into visiting phishing or malware-hosting websites.
> 
> Of the 4.79 million imageless Docker Hub repositories uncovered, 3.2 million of them are said to have been used as landing pages to redirect unsuspecting users to fraudulent sites as part of three broad campaigns -
> 
> * Downloader (repositories created in the first half of 2021 and September 2023), which advertises links to purported pirated content or cheats for video games but either directly links to malicious sources or a legitimate one that, in turn, contains JavaScript code that [redirects](https://isc.sans.edu/diary/How+Malware+Campaigns+Employ+Google+Redirects+and+Analytics/19843) to the malicious payload after 500 milliseconds.
> * E-book phishing (repositories created in mid-2021), which redirects users searching for e-books to a website (" [rd.lesac.ru](http://rd.lesac.ru/) ") that, in turn, urges them to enter their financial information to download the e-book.
> * Website (thousands of repositories created daily from April 2021 to October 2023), which contains a link to an online diary-hosting service called Penzu in some cases. 


Useful to remmeber that bad actors will use your platform in interesting ways, and often what might seem lazy or uninspired. Sure, if you can create millions of container images, you could do dependency confusion, you could inject malware or coin miners, you could do all kinds of things.  But you also get SEO spam that can point to other campaigns that you run, and those links by themselves can be useful 


## [Examining the Deception infrastructure in place behind code.microsoft.com - Microsoft Community Hub ](https://techcommunity.microsoft.com/t5/microsoft-sentinel-blog/examining-the-deception-infrastructure-in-place-behind-code/ba-p/4124464)

[https://techcommunity.microsoft.com/t5/microsoft-sentinel-blog/examining-the-deception-infrastructure-in-place-behind-code/ba-p/4124464](https://techcommunity.microsoft.com/t5/microsoft-sentinel-blog/examining-the-deception-infrastructure-in-place-behind-code/ba-p/4124464)

> The honeypot itself is a custom designed framework written in C#. It enables security researchers to quickly deploy anything from a single HTTP exploit handler in one or two lines of code all the way up to complex protocols like SSH and VNC. For even more complex protocols we can hand off to real systems when we detect exploit traffic and revert these shortly after.
> 
> It is our mission to deny threat actors access to resources or enable them to use our infrastructure to create further victims. That’s why in almost all scenarios the attacker is playing in a high interaction, simulated environment. No code is run, everything is a trick or deception designed to get them to reveal their intentions to us.
> 
> Substantial engineering has gone into our simulation framework. Today over 300 vulnerabilities can be triggered through the same exploit proof-of-concepts available in places like GitHub and exploitdb. Threat actors can communicate with over 30 different protocol and can even ‘log in’ and deploy scripts and execute payloads that look like they are operating on a real system. There is no real system and almost everything is being simulated.
> 
> Even so it’s important that in standing up a honeypot on an important domain like [Microsoft.com](http://microsoft.com/) that it wasn’t possible for attackers to use this as environment to perform other web attacks. Attacks that might rely on same origin trust. To mitigate this further we added the sandbox policy to the pages which prevents these kinds of attacks. 
> 
> **What have we learnt from the honeypot?** 
> 
> Our sensor network has contributed to many successes over the year. We’ve presented on these at computer security conferences in the past as well as shared our data with [academia](https://arxiv.org/abs/2301.02505)  [and the community](https://techcommunity.microsoft.com/t5/microsoft-sentinel-blog/enabling-security-research-amp-hunting-with-open-source-iot/ba-p/1279037) . [We incorporate this data into our security products to enable them to be aware of the latest threats](https://techcommunity.microsoft.com/t5/microsoft-sentinel-blog/unusual-mirai-variant-looks-for-mining-infrastructure/ba-p/2756669) .
> 
> In recent years this capability has been crucial to understanding the 0day and nDay ecosystem. During Log4shell incident we were able to use our sensor network to track each iteration of the underlying vulnerability and associated proof-of-concept all the way back to GitHub. This helped us understand the groups involved in productionising the exploit and where it was being targeted. Our data enables internal teams to be much better prepared to remediate and provides the analysis for detection authors to improved products like MDE in real time.
> 
> The team developing this capability also works closely with the MSRC who our track our own security issues. When the Exchange ProxyLogon vulnerability was announced we had already written a full exploit handler in our environment to track and understand not just the exploit but the groups deploying it. This situational awareness this enables us to give clearer advice to industry, better protect our customers and integrate new threats we were seeing into Windows Defender and MDE. 


This is a really neat peek behind the scenes at what a really advanced threat intelligence capability can do with deception technology 


## [adanalvarez/HoneyTrail: Independently deploy customized honeyservices in AWS to trigger alerts on unauthorized access. ](https://github.com/adanalvarez/HoneyTrail)

[https://github.com/adanalvarez/HoneyTrail](https://github.com/adanalvarez/HoneyTrail)

> HoneyTrail includes a few components designed to detect attackers:
> 
> * **S3 Bucket:** It is an S3 bucket that contains an object called 'users_data.csv' full of fake data.
> * **Lambda:** A Go Lambda function named "GetAccessKeyForBackups", that doesn't show its code in the AWS console (because it is in Go), tempting attackers trying to find a backdoor access to invoke it.
> * **DynamoDB:** A DynamoDB table called 'CreditCardData'.
> 
> A CloudTrail monitors these services using an advanced event selector that focuses exclusively on specific activities such as accessing the S3 file, invoking the Lambda function, or querying the DynamoDB table. When an attacker interacts with any of these services, a CloudTrail log is generated and stored in an S3 bucket configured with Event Notifications. This feature triggers a Lambda function that is set up to alert you via Simple Notification Service (SNS) or Simple Email Service (SES), depending on the chosen configuration. 


A cute demonstration of how you might setup your own honeypot systems in AWS 


