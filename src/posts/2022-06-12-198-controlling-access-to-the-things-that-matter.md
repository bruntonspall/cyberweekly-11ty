---
title: "198 - Controlling access to the things that matter"
date: 2022-06-12
description: "Identity and Access Control forms the basis of almost all security as we know it."
permalink: /controlling-access-to-the-things-that-matter/
---

Identity and Access Control forms the basis of almost all security as we know it.

It doesn't matter whether we are talking about using passes to enter a building, issuing tokens for a service to access an API, or forcing users to rotate their passwords, the root of making a security decision boils down to two simple questions:

* Do I know who this is?
* Is this person/thing/service allowed to access this resource?

Managing that stuff is really hard.

The theory of access control can talk about grants, about access tokens, and about signing all it wants, but in most cases, the actual technology isn't *that* hard.

What is hard is making a model in the computer that makes the decision actually map the real world with any degree of fidelity.

Our computer models, and in many cases our mental models, take a large number of shortcuts around identity and access control.  We tend to assume that if someone was allowed in seconds before, they are now.  We tend to assume that if someone is in an authorised area, that they are probably authorised to be there.  We assume that someone holding a stack of papers and mug of tea and struggling to badge through a door must be a real employee, because pen testers never have their own mug in your building right?

But the world is far more complex and ever changing than our computer models like to admit.  Some people share jobs, and share email addresses.  Some people use shared computers with a single login.  Some services need to access data in interesting and mysterious ways.

The majority of our security flaws in identity and access management comes from an attempt to oversimplify the world into the computer model.

This manifests as either granting permissions that are far too wide, as we see in the Kubernetes audits, where access tokens have more permissions than they strictly need to get the job done, and this can be abused to pivot out of an otherwise pretty good jail and into a more privileged postion.
Or we grant permissions to users that don't reflect their job, that aren't maintained when they move organisation or otherwise flatten the world.

Finally, we see it in the granting of permissions on a permanent basis, so when users leave, move or no longer need access, they tend to retain the permissions beyond a reasonable time.

There aren't good answers to this.   If you could make a map totally accurate, it would have to be on a 1:1 scale, making it unsuited as a map.   We have to accept that our mapping of roles, identities and permissions will never be perfect.

But what we can do is ask ourselves what imperfections we are willing to live with, and then approach our role setting, permission granting from that perspective.  With a knowing look at the areas where our solution doesn't have perfect fidelity, and documenting and acknowledging those areas.  Because if you can work those out, you can start to monitor for those edge cases, and see if you can see them being exploited.

## [Introducing Entitlements: GitHub's open source Identity and Access Management solution | The GitHub Blog ](https://github.blog/2022-06-09-introducing-entitlements-githubs-open-source-identity-and-access-management-solution/)

[https://github.blog/2022-06-09-introducing-entitlements-githubs-open-source-identity-and-access-management-solution/](https://github.blog/2022-06-09-introducing-entitlements-githubs-open-source-identity-and-access-management-solution/)

> We strongly believe in using GitHub to build GitHub, keeping the developer experience streamlined and integrating directly into their workflows. 
> 
> We track our work in Issues, plan work in projects, and automate reminders through GitHub Actions and ChatOps. So, it’s natural that we would look to GitOps to solve one of the more complex problems in IT security: Identity and Access Management (IAM). We wanted a solution that worked with our tools, was auditable, scalable, and well understood by developers. In this spirit, we built Entitlements , which uses a Git repository for the source-of-truth, declarative authorizations, and seamless integration with GitHub.com for approvals and audits. After years of development and countless contributions from GitHub employees, we are very excited to finally open source it! 
> 
> **Re-orgs** 
> 
> It is natural for organizations large and small to re-organize team structures to adapt to changing business demands. When re-orgs happen, it is common for access to accumulate, leaving you with access from both your old role and your new role. Entitlements can help prevent this.
> At GitHub, we periodically pull a list of our employees from our internal source of truth and output that to various groups. We create automatic groups per manager, per region, per level, and per business function. By referencing these automatic groups wherever possible, we can ensure that access is added and revoked appropriately when business needs or organizations change. 


One of the trickiest problems in IAM is not getting the actual identity and authentication right, although that’s hard enough!  It’s ensuring it stays up to date when people move teams, move line managers, leave or there’s a significant reorganisation.
This tool is nice, but the pattern is nicer.  Don’t make your IAM team have to handle adding every user to every service and manage everything.  Describe it in code, take regular pulls from the HR source of truth, and then automate it.  That leaves your IAM team dealing with the edge case stuff, like adding a new service, or a new team and so on 


## [Kubernetes Privilege Escalation: Excessive Permissions in Popular Platforms - Palo Alto Networks ](https://www.paloaltonetworks.com/resources/whitepapers/kubernetes-privilege-escalation-excessive-permissions-in-popular-platforms)

[https://www.paloaltonetworks.com/resources/whitepapers/kubernetes-privilege-escalation-excessive-permissions-in-popular-platforms](https://www.paloaltonetworks.com/resources/whitepapers/kubernetes-privilege-escalation-excessive-permissions-in-popular-platforms)

> Kubernetes threat actors are growing more sophisticated, and are beginning to target excessive permissions and Role-Based Access Control (RBAC) misconfigurations. To understand the real-world impact of excessive permissions, Prisma Cloud researchers analyzed popular Kubernetes platforms - distributions, managed services, and common add-ons - to identify widespread infrastructure components that run with powerful permissions. In 62.5% of the Kubernetes platforms reviewed, privileged credentials were distributed across every node in the cluster. As a result, in half of the platforms examined, a single container escape was enough to take over the entire cluster.­­ 


A nice overview of all the problems you cna get into with permissions on Kubernetes.  
Of course a managed Kubernetes instance will solve some of the most baseline issues in here, but you are still expected to set it up, assign users and give out roles and permissions, so the vast majority of this stuff is relevant even when someone else is managing the underlying Kubernetes infrastructure for you 


## [Managed Identity Attack Paths, Part 1: Automation Accounts | by Andy Robbins | Jun, 2022 | Posts By SpecterOps Team Members ](https://posts.specterops.io/managed-identity-attack-paths-part-1-automation-accounts-82667d17187a)

[https://posts.specterops.io/managed-identity-attack-paths-part-1-automation-accounts-82667d17187a](https://posts.specterops.io/managed-identity-attack-paths-part-1-automation-accounts-82667d17187a)

> In this three part blog series we will explore attack paths that emerge out of Managed Identity assignments in three Azure services. In Part 1 we are looking at Automation Accounts. Part 2 explores Logic Apps, and Part 3 explores Function Apps. But first, what exactly are Managed Identities?
> 
> I think it’s best to think about Managed Identities in the context of the problem they have (in my opinion, very effectively) solved: accidental credential exposure. Before Managed Identities, admins needed to either store or retrieve credentials in their scripts to enable the script to authenticate to other services. This is very dangerous, as it often leads to accidental exposure of those credentials when the script itself can be read by unauthorized people. Sometimes that means the admin accidentally uploaded the script to GitHub or Pastebin. Oops.
> 
> Managed Identity assignments are an extremely effective security control that prevent the accidental exposure of credentials by removing this requirement to store or use credentials in the first place. Instead of storing and sending credentials, Azure knows that your script is allowed to authenticate as a specific Service Principal. 
> 
> **You should absolutely be using Managed Identity assignments in Azure instead of storing or accessing credentials.** 
> 
> But Managed Identities introduce a new problem: they can quickly create identity-based attack paths in Azure that may lead to escalation of privilege opportunities. In this series we will explore how those attack paths emerge, how they can be practically abused by an attacker, and how we as defenders can discover, mitigate, and prevent the future emergence of those attack paths. 


This is a nice breakdown of Microsoft Azure’s managed identity assigments and includes some classic mistakes people make, along with patterns to apply.
As the author says, using this, even with misconfiguration, is still better than not using it at all.  Yes, there are some attacks in here, but many of these attacks are also possible on normal accounts, not just Automation Accounts, so you should lock down all of your accounts following these patterns if possible. 


## [Follina — a Microsoft Office code execution vulnerability | by Kevin Beaumont | May, 2022 | DoublePulsar ](https://doublepulsar.com/follina-a-microsoft-office-code-execution-vulnerability-1a47fce5629e)

[https://doublepulsar.com/follina-a-microsoft-office-code-execution-vulnerability-1a47fce5629e](https://doublepulsar.com/follina-a-microsoft-office-code-execution-vulnerability-1a47fce5629e)

> There’s a lot going on here, but the first problem is Microsoft Word is executing the code via msdt (a support tool) even if macros are disabled. Protected View does kick in, although if you change the document to RTF form, it runs without even opening the document (via the preview tab in Explorer) let alone Protected View.
> Most importantly, we need to name this and give it a crap logo:The official Follina vulnerability logo, carefully made in Microsoft Paint
> I’m calling it Follina because the spotted sample on the file references 0438, which is the area code of Follina in Italy. **In English, So What** It’s a zero day allowing code execution in Office products. Historically, when there’s easy ways to execute code directly from Office, people use it to do bad things. This breaks the boundary of having macros disabled. Vendor detection is poor. 


This vulnerability is bad, and you should be patching immediately.  It’s in use in active campaigns and sadly vendor support from Microsoft was quite tardy in this case.

I also wish I had Kevin’s ability to name a vulnerability.  It’s something I’m in absolute awe of! 


## [Hackers Exploiting Unpatched Critical Atlassian Confluence Zero-Day Vulnerability ](https://thehackernews.com/2022/06/hackers-exploiting-unpatched-critical.html)

[https://thehackernews.com/2022/06/hackers-exploiting-unpatched-critical.html](https://thehackernews.com/2022/06/hackers-exploiting-unpatched-critical.html)

> Atlassian has warned of a critical unpatched remote code execution vulnerability impacting Confluence Server and Data Center products that it said is being actively exploited in the wild.
> The Australian software company credited cybersecurity firm Volexity for identifying the flaw, which is being tracked as **CVE-2022-26134** .
> "Atlassian has been made aware of current active exploitation of a critical severity unauthenticated remote code execution vulnerability in Confluence Data Center and Server," it said in an advisory.
> "There are currently no fixed versions of Confluence Server and Data Center available. Atlassian is working with the highest priority to issue a fix." Specifics of the security flaw have been withheld until a software patch is available.
> All supported versions of Confluence Server and Data Center are affected, although it's expected that all versions of the enterprise solution are potentially vulnerable. The earliest impacted version is yet to be ascertained.
> In the absence of a fix, Atlassian is urging customers to restrict Confluence Server and Data Center instances from the internet or consider disabling the instances altogether. Alternatively, it has recommended implementing a web application firewall (WAF) rule which blocks URLs containing "${" to reduce the risk. 


This was last week, during a 4 day weekend in the UK.  Although it’s now fixed, there has been several weeks of constant scanning and exploits.
It’s easy to look back, but the right answer here was to remove the application from the internet and expose it only via an internal and authenticated network of some form.  Of course that wouldn’t prevent insider attacks, but it would have prevented the general scanning from succeeding.

The WAF rule would have bought you about 12 hours from looking at twitter before people found reasonable workarounds that would bypass the WAF rules. 


## [Purpose-based access controls at Palantir | Palantir Blog ](https://blog.palantir.com/purpose-based-access-controls-at-palantir-f419faa400b3)

[https://blog.palantir.com/purpose-based-access-controls-at-palantir-f419faa400b3](https://blog.palantir.com/purpose-based-access-controls-at-palantir-f419faa400b3)

> For example, to manage the spread of COVID-19, healthcare organisations have needed to rapidly bring together data from many systems — testing programmes, care homes, and hospitals — and give thousands of users, from healthcare workers to academics, access to different subsets of this information.
> This creates an acute challenge for data governance teams. Tracking who has access to what information and why, across thousands of datasets and thousands of users quickly becomes an exceptionally complex problem. In order to protect the privacy of the individuals whose personal information is in the data, data governance teams must ensure that users only have access to sensitive or personal data when strictly necessary.
> This challenge grows exponentially with organisational scale. As the number of access requests grows, so too does the number of potential failures. Auditing decisions to grant access is difficult if the access requests were made by telephone, email, or even in person. Data governance teams often rely on more technical colleagues to grant access to the data itself, and this can make it hard for the data governance team to check whether their decision has been appropriately enforced. 


This model, adding a deliberate level of intermediation into data access, is likely annoying as a data engineer, but quite powerful.
Just because you are a certain engineer, doesn’t mean you should have unfettered access to a given dataset.  Instead Palantir proposes creating “purposes”, which are essentially audited views onto a dataset.  
This means that data owners are able to take a dataset and create multiple purposes, one for each potential use of a dataset.  Equally, analysts, instead of requesting access to a dataset, requests access to a purpose.  This means that the “purpose” for which they are doing access is always there to remind them.
It would also allow the data owner to potentially put controls on the data exposed, such as anonymising, aggregating, or dropping or masking certain fields.

This is a nice pattern and I can see how one could implement it within almost any relational database fairly easily as well 


## [The walls are closing in on Clearview AI as data watchdogs get tough | MIT Technology Review ](https://www.technologyreview.com/2022/05/24/1052653/clearview-ai-data-privacy-uk/)

[https://www.technologyreview.com/2022/05/24/1052653/clearview-ai-data-privacy-uk/](https://www.technologyreview.com/2022/05/24/1052653/clearview-ai-data-privacy-uk/)

> Clearview AI boasts one of the world’s largest databases of people’s faces, with 20 billion images that it has scraped off the internet from publicly available sources, such as social media, without their consent. Clients such as police departments pay for access to the database to look for matches.
> Data protection authorities around the Western world have found this to be a clear violation of privacy and are now beginning to work together to clamp down. Edwards stressed that “international cooperation is essential to protect people’s privacy rights in 2022” and is due to meet with European regulators in Brussels this week. The UK’s investigation into Clearview AI was carried out jointly with the Australian information commissioner. 


Dan Hon riffed on this recently ( twice ) as “It’s all about ethics in AI”. 
We consistently see AI datasets created by scraping information that is published onto the web in some form.  Whether it be text comments on reddit, encyclopedia content like Wikipedia, answers from Quora or pictures from social media, the real question is whether by pushing that content into the world, you agree to any company using it to build an AI on the back of it.
Of course, additionally, you need to worry about how that might bias an AI.  It’s not like Reddit is always the best example of humanity at its best (well bits of Reddit, r/mademesmile can be quite nice sometimes) 


## [The State of Secrets Sprawl 2022 - GitGuardian ](https://www.gitguardian.com/state-of-secrets-sprawl-report-2022)

[https://www.gitguardian.com/state-of-secrets-sprawl-report-2022](https://www.gitguardian.com/state-of-secrets-sprawl-report-2022)

> **It’s safe to say that 2021 will go down in history for cybersecurity experts.** Ransomware and other large-scale cyberattacks (SolarWinds, Colonial Pipelines) or vulnerabilities (Log4Shell) have made headlines around the world. Software supply chain attacks have seen their number explode, and this comes as no surprise considering the plethora of vulnerabilities and misconfigurations found across software development environments.
> Unsurprisingly, a lot of attacks start with the compromise of a leaked secret. Credentials are a nightmare for security engineers because they can end up in so many places: build, monitoring, or runtime logs, stack traces, and … git history.The results of our 2022 Secrets Sprawl report comforted our view that the only way to address the challenge of secrets sprawling within corporate repositories is to enable a shared responsibility between AppSec and Devs. 


Sigh.  This has got some really interesting statistics, and is probably useful if you are justifying an AppSec program in your organisation, but it reads like advertising copy throughout.
Some choice statistics though include: 
* On average, 3 commits out of 1,000 exposed at least one secret, **+50 % compared to** **2020** * 4.62% of Docker images exposes an internal secret
* 1 AppSec engineer needs to handle 3,413 secret occurrences on average

Managing secrets in code is hard, and if you have a medium to large development team, but don’t have an appsec engineer, then you are probably leaking secrets in there somewhere 


## [GitHub - sensity-ai/dot: The Deepfake Offensive Toolkit ](https://github.com/sensity-ai/dot)

[https://github.com/sensity-ai/dot](https://github.com/sensity-ai/dot)

> _dot_ (aka Deepfake Offensive Toolkit) makes real-time, controllable deepfakes ready for virtual cameras injection. _dot_ is created for performing penetration testing against e.g. identity verification and video conferencing systems, for the use by security analysts, Red Team members, and biometrics researchers.
> If you want to learn more about _dot_ is used for penetration tests with deepfakes in the industry, read these articles by The Verge and Biometric Update dot _is developed for research and demonstration purposes. As an end user, you have the responsibility to obey all applicable laws when using this program. Authors and contributing developers assume no liability and are not responsible for any misuse or damage caused by the use of this program._ 


This is quite scary for a “red team” tool.  Expect this to be used by a large number of nefarious individuals and to cause significant damage through their misuse of it. 


## [The Surreal Case of a C.I.A. Hacker’s Revenge | The New Yorker ](https://www.newyorker.com/magazine/2022/06/13/the-surreal-case-of-a-cia-hackers-revenge)

[https://www.newyorker.com/magazine/2022/06/13/the-surreal-case-of-a-cia-hackers-revenge](https://www.newyorker.com/magazine/2022/06/13/the-surreal-case-of-a-cia-hackers-revenge)

> _A hot-headed coder is accused of exposing the agency’s hacking arsenal. Did he betray his country because he was pissed off at his colleagues?_ 


I originally covered the mistrial when it happened back in CyberWeekly #97 https://cyberweekly.net/tools-shape-our-thinking , but this is a truly stupendously readable narrative around the basic facts of the case, and the stories behind it.  From office nerf gun wars, to death threats and restraining orders, this is a thrilling read 


