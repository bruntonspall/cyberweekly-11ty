---
title: "192 - Integrity in the software supply chain"
date: 2022-04-10
description: "We sometimes talk about \"securing the software supply chain\" as if it will prevent bugs and issues, which isn't quite accurate.  "
permalink: /integrity-in-the-software-supply-chain/
---

We sometimes talk about "securing the software supply chain" as if it will prevent bugs and issues, which isn't quite accurate.  

The increasing number of software supply chain systems are there to validate and verify the integrity of the supply chain.  That means that you can be confident that the code that you wrote and the dependencies that you specified are in fact the same code that is in the built binary.

This doesn't prevent bad code from getting into the supply chain, whether a bug or a malicious line of code, but it limits where it can be introduced, making it harder for an adversary to simply modify the binary.  

It also gives you unparalleled visibility into the supply chain, so if there's another issue like Log4Shell, you should be able to audit your live systems and know what code is in there and what is vulnerable.

But increasingly the complexity of our software build and deployment systems is itself a risk.  Even with all these tools, they rely on the fact that the machines that build the software are in fact doing their job correctly.  The security of these CI/CD systems is something that is coming increasingly under the microscope.  But we need to think not just of the security of those systems, but as with all configurable systems, whether the way that we use them is secure.  There's a great piece in todays issue that covers common vulnerabilities in Github Actions, which many people use as part of their CI/CD process.  If we cannot audit and validate that these configurations are secure, then it's difficult to have confidence in their implementation of securing the software lifecycle.

## [How we found vulnerabilities in GitHub Actions CI/CD pipelines - Cycode ](https://cycode.com/blog/github-actions-vulnerabilities/)

[https://cycode.com/blog/github-actions-vulnerabilities/](https://cycode.com/blog/github-actions-vulnerabilities/)

> Cycode discovered **critical vulnerabilities** in several **popular open-source projects** , each of which can cause a supply-chain attack through the CI process. We found the vulnerabilities in **misconfigured**  **GitHub Actions workflows.** They were missing proper input sanitizing, allowing malicious actors to inject code into the builds through issues and comments, and to access privileged tokens.
> 
> Out of dozens of vulnerable repositories we found and reported, the most popular were:
> 
> * Liquibase – Track, version, and deploy database schema changes. Applied fix – 3278525 .
> * Dynamo BIM – A visual programming tool that is sponsored by Autodesk. Applied fix – disabled the workflows.
> * FaunaDB – Transactional database delivered as a secure and scalable cloud API with native GraphQL. Applied fix – ee6f53f .
> * Wire – An open-source communication platform. Applied fix – 9d39d6c .
> * Astro – Static site builder. Applied fix – 650fb1a .
> * Kogito – A business automation technology that is sponsored by Red Hat. Applied fix – 53c18e5 .
> * Ombi – A popular media request tool. Applied fix – 5cc0d77 .
> 
> Summing up the users of these tools, these vulnerabilities can impact **millions of potential victims** .
> We responsibly disclosed these vulnerabilities to the organizations and the maintainers, and they fixed them quickly. We didn’t find any signs of prior exploitation of the vulnerable workflows. 


A nice example of just how an attacker might target your github actions pipeline and what they can do once they get there 


## [Secure your software supply chain using Sigstore and GitHub actions - Marco Franssen ](https://marcofranssen.nl/secure-your-software-supply-chain-using-sigstore-and-github-actions)

[https://marcofranssen.nl/secure-your-software-supply-chain-using-sigstore-and-github-actions](https://marcofranssen.nl/secure-your-software-supply-chain-using-sigstore-and-github-actions)

> With the rise of software supply chain attacks it becomes more important to secure our software supply chains. Many others have been writing about software supply chain attacks already, so I won't repeat that over here in this article. Assuming you found my article, because you want to know how to prevent them.
> In this blogpost I want to show you how to secure the software supply chain by applying some **SLSA requirements** in the GitHub actions workflow. We will utilize Sigstore to sign and attest the images. I will also involve a few other tools to generate build provenance and an SBOM for our released Docker images so we can attest that to the images.
> 
> We will cover the following topics:
> * Having a bare bones release workflow using GitHub actions
> * Adding signatures to our Docker images
> * Generating an SBOM for our Docker image
> * Attest the SBOM to our Docker image
> * Generating build provenance for our Docker image
> * Attest the build provenance to our Docker image 


Some useful tips here on how to configure your github actions workflow in order to improve your packages supply chain security.  This will ensure that people can validate that your docker containers were built by the right build tool, from the original code, and what they contained at the time they were built. 


## [dagger.io | Introducing Dagger: a new way to create CI/CD pipelines ](https://dagger.io/blog/public-launch-announcement)

[https://dagger.io/blog/public-launch-announcement](https://dagger.io/blog/public-launch-announcement)

> There’s never been a better time to be a developer. Thanks to an ever-expanding selection of specialized tools and cloud infrastructure, a dedicated team of developers can ship a competitive product in almost any industry within months. The result is unprecedented growth and innovation at every level of the stack.
> This developer’s dream creates a nightmare for devops engineers, whose job is to automate the delivery of increasingly complex applications to increasingly complex cloud infrastructure. In order to continuously build, test and deploy their software, developers need a CI/CD pipeline that glues together an ever-expanding collection of specialized tools. The result is a mess of homemade scripts that are painful to write, difficult to debug and test, and must be rewritten for each new development and CI environment. Component reuse between pipelines is low, which causes fragmentation and a constant reinvention of the wheel. 


Dagger looks really neat, and as I’ve said before, CI/CD pipelines are not well enough supported and are becoming a security weakspot for organisations, so something to help rationalise them and make it easier to lint, audit and validate them effectively is welcome 


## [Chainguard Whitepaper Cover ](https://chainguard.dev/blog-static/chainguard-all-about-that-base-image.pdf)

[https://chainguard.dev/blog-static/chainguard-all-about-that-base-image.pdf](https://chainguard.dev/blog-static/chainguard-all-about-that-base-image.pdf)

> All base images, except for Alpine, had vulnerabilities stretching back several years. The Node image
> even had twenty-five vulnerabilities dating back to either 2004 or 2005. Interestingly, the Red Hat and
> Ubuntu image vulnerabilities were clustered within the past five years while the Debian vulnerabilities
> were spread across many years. This data suggests that the images do not contain these vulnerabilities
> due to lack of time. It’s more likely that these vulnerabilities remain because of factors such as a
> conscious decision to not fix a vulnerability and excessive attack surface, the result of extraneous
> packages, which makes zero-vulnerabilities a herculean task.
> In short, security debt can stick with a base image 


This is an interesting report, looking at the base images that people use for their containers.  It does miss one potential false-positive that is quite common in debian/ubuntu distributions in particular, which is that those distributions can often backport security fixes, so assuming that version 1.16 of something is vulnerable might not actually be true.

However, I completely agree with the general theme of this report.  As an organisation, your security and engineering team should work to ensure that everyone is using a quiet image, that’s a base image with no known vulnerabilities.  That will make it far easier for your engineers to look at the results of a security scan and see errors or vulnerabilities that they have included through their software supply chain 


## [How to Use Threat Intelligence to Form a Stronger Purple Team ](https://ahead.feedly.com/posts/how-to-use-threat-intelligence-to-form-a-stronger-purple-team)

[https://ahead.feedly.com/posts/how-to-use-threat-intelligence-to-form-a-stronger-purple-team](https://ahead.feedly.com/posts/how-to-use-threat-intelligence-to-form-a-stronger-purple-team)

> Cyber threat intelligence (CTI) gives you information about risks to different business functions based on things like systems or geography. Large enterprises use complex CTI, including dark web activity, but companies of all sizes have access to some form of it.
> However, you also need to recognize that CTI is more than “just” data. **It starts with data, but you need to enrich the data with context.** This means asking the following questions:
> • Is _my_ technology stack vulnerable to these new TTPs?
> • Are threat actors actively targeting _my_ industry?
> • Is _my_ supply chain at risk?
> This is where bringing the human element back into the process adds value. You need the ability to define the data that impacts your organization. Once you review it, then you can use it to inform your purple team testing and validation processes. 


There’s loads in here about running good purple teams, but this stood out to me.  Threat Intelligence can seem really interesting to read, and it can be, but if you are producing or analysing threat intelligence, it’s really important that you develop the skills required to contextualise that intelligence and make it usable.
That means thinking about the actions, because “be worried” isn’t a good enough action, and without action, your threat intelligence has limited value. 


## [Living Off The Land: Threat Research February 2022 Release | Splunk ](https://www.splunk.com/en_us/blog/security/living-off-the-land-threat-research-february-2022-release.html)

[https://www.splunk.com/en_us/blog/security/living-off-the-land-threat-research-february-2022-release.html](https://www.splunk.com/en_us/blog/security/living-off-the-land-threat-research-february-2022-release.html)

> Analytic stories are security use cases supported by our threat research team’s pre-built detections and responses. The following analytic stories focus on monitoring and investigating items that are related to Living Off The Land techniques. Living off the land plays an integral role in an adversaries playbook when landing in an environment. Instead of bringing in applications and new utilities, adversaries use utilities native to the operating system. This provides the adversary the ability to blend in better with native applications, providing flexibility in code execution and process behavior. 


I’m a big fan of use case driven detections in SOC’s.  Too often people setup their SOC and just start logging everything.  But you want to start with a use case, an attacker wants to do X, and then work out what actions they would take and how you would see that in the logs.  

That makes it far easier to build good detection rules that have a high signal to noise and avoids you just shipping everything into your SIEM tool.

Splunk here are not just sharing their detection rules, but also share the use cases behind them that helps you understand what these rules are looking for.  That can help you contextualise them, decide where they appropriate to run and to prioritise them.  I find that far more useful than a bundle of Yara rules at the end of a general blogpost. 


## [Mars Stealer: Exclusive New Threat Research ](https://blog.morphisec.com/threat-research-mars-stealer)

[https://blog.morphisec.com/threat-research-mars-stealer](https://blog.morphisec.com/threat-research-mars-stealer)

> The Mars Stealer pilfers user credentials stored in various browsers, as well as many different cryptocurrency wallets. Mars Stealer is being distributed via social engineering techniques, malspam campaigns, malicious software cracks, and keygens. (For more about infostealers, read Morphisec’s coverage of the Jupyter infostealer .) **** Not long after the Mars Stealer’s release, a cracked version was released with an instruction document. This guide has some flaws. One flaw instructs users to set up full access (777) to the whole project, including the victims’ logs directory.
> 
> Whoever released the cracked Mars Stealer without official support has led threat actors to improperly configure their environment, exposing critical assets to the world.
> 
> [...]
> 
> In this campaign, the actor distributed Mars Stealer via cloned websites offering well-known software. They used the Google Ads advertising platform to trick victims searching for the original software into visiting a malicious site instead. The actor is paying for these Google Ads campaigns using stolen information (see figure 15). The example below is one of many demonstrating how the actor targets Canadians by using geographically targeted Google Ads. 


Two interesting bits in here.  The first is the use of Google Ads to target individuals.  I’ve talked before about the power of targeted advertising, and it’s worth remembering that attackers who care about their targets have to build strong operational networks to ensure that they are attacking the right people.  But AdTech firms have already built those operational networks, it’s just a matter of weaponising them.  In this case the ads themselves aren’t malicious, but they lead to copycat websites that look safe but in fact host malicious code.

Secondly, I note that criminals have problems with people pirating their code, and then flogging dodgy copies with poor instructions as well! 


## [New Milestones for Deep Panda: Log4Shell and Digitally Signed Fire Chili Rootkits ](https://www.fortinet.com/blog/threat-research/deep-panda-log4shell-fire-chili-rootkits)

[https://www.fortinet.com/blog/threat-research/deep-panda-log4shell-fire-chili-rootkits](https://www.fortinet.com/blog/threat-research/deep-panda-log4shell-fire-chili-rootkits)

> During the past month, FortiEDR detected a campaign by Deep Panda, a Chinese APT group. The group exploited the infamous Log4Shell vulnerability in VMware Horizon servers. The nature of targeting was opportunistic insofar that multiple infections in several countries and various sectors occurred on the same dates. The victims belong to the financial, academic, cosmetics, and travel industries.
> Following exploitation, Deep Panda deployed a backdoor on the infected machines. Following forensic leads from the backdoor led us to discover a novel kernel rootkit signed with a stolen digital certificate. We found that the same certificate was also used by another Chinese APT group, named Winnti, to sign some of their tools. 


I’m hoping that Christmas went by and you managed to patch all of your supply chain against Log4Shell, but it looks like the Deep Panda APT is still using that as an exploit chain to get into systems.

The only odd part in this report is that I had thought that VMware Horizon was only vulnerable to Log4Shell on the management interface, which means that the attackers needed to already be on the network and able to get to the management interface.  But if they have successfully phished or compromised the network to get on, this is a powerful ability to then escalate privilege and build a stronghold from which to pivot around to other systems. 


## [Motivating Jenny: Developer Security Toolkit ](https://motivatingjenny.org/index.html)

[https://motivatingjenny.org/index.html](https://motivatingjenny.org/index.html)

> Software developers, whether programmers, testers, designers or product managers like to solve problems. When developers identify a security problem in their environment, most will actively try to solve it, whether by drawing attention to a security impact in a product management meeting, by using secure functions and constructs while coding, by thinking up tests, or by consulting an expert. It is vital to help developers gain a sense for how they can effectively engage with security in different situations.
> Based on our research, the Motivating Jenny project has designed a toolkit to help **_sensitise**_ development teams toward security issues in the workplace. Each package has simple and complete instructions for you to use. 


I missed this coming out a while ago, but I’ve had chats with some of the leaders here, and the card game in particular is something that caught my attention a few years back.  I’ve had the privilege of playing it when run as a workshop by its creator and I think it’s a great and entertaining way of showing the cost and implications of various security decisions to developers and development teams 


## [Digital Forensics Basics: A Practical Guide for Kubernetes DFIR – Sysdig ](https://sysdig.com/blog/guide-kubernetes-forensics-dfir/)

[https://sysdig.com/blog/guide-kubernetes-forensics-dfir/](https://sysdig.com/blog/guide-kubernetes-forensics-dfir/)

> Although DevOps teams have made great strides in harnessing the new tools, the benefits don’t come without challenges and tradeoffs. Among them is the question of how to perform a **DFIR Kubernetes** , **extract all relevant data** , and **clean up** your systems when a **security incident occurs** in one of these modern environments.
> But what if a cybersecurity incident occurs in your containers, deployed via **Docker** or within a **Kubernetes** Pod?
> 
> Due to their ephemeral nature, containers may prove elusive for traditional DFIR approaches. Indeed, forensic and post-mortem analyses are not easy in such **dynamic environments** . This prompted the introduction of new methodologies and best practices to follow in order to identify and respond to potential cyberattacks.
> In this article, we are going to cover **why**  **DFIR for Kubernetes** is so **important** and **how to assess your container DFIR capabilities** . We will also see a full scenario where we dig deep into the events that affected a Kubernetes pod, along with response steps to take. 


This is a great little article outlining how you might conduct DFIR inside a sus[pected compromised container.  I particularly appreciated the explanation of how to change networking rules and use kubectl cordon so that you can keep the node running, but avoid the infection spreading.  This is critical in good DFIR, because you want to retain the in-memory state, but you need to ensure that no other services are spun up on the pod. 


