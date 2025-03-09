---
title: "167 - We rely on our suppliers"
date: 2021-09-19
description: "Supply chains have been a cybersecurity issue since well before the Solarwinds hack, but have risen to prominance in the last year."
permalink: /we-rely-on-our-suppliers/
---

Supply chains have been a cybersecurity issue since well before the Solarwinds hack, but have risen to prominance in the last year.

They’re super hard to reason about, because in reality, no two supplier relationships are the same.  The way that you buy and manage services for a cloud infrastructure supplier is very different to how you embed libraries in your code, which is different to the tools that your staff use.

The security of those supply chains is dependant on trusting that company to a certain degree, do they tell you when something is wrong, and how informed are you about how to manage any issues that do come up.

Of course, we don’t just need to worry about the software supply chain, underlying all of that software is a hardware platform that we mostly trust implicitly.  But the US and China both want to control the major hardware supply chain, not just for economic reasons, but for the sense of security that comes with it.

We’ll continue talking about supply chains likely for the next few years at least, so best get used to a steady stream of compromises, mistakes, new patterns and standardisation processes now.

## [Travis CI flaw exposed secrets of thousands of open source projects | Ars Technica](https://arstechnica.com/information-technology/2021/09/travis-ci-flaw-exposed-secrets-for-thousands-of-open-source-projects/?utm_brand=arstechnica&utm_source=twitter&utm_social-type=owned&utm_medium=social)

[https://arstechnica.com/information-technology/2021/09/travis-ci-flaw-exposed-secrets-for-thousands-of-open-source-projects/?utm_brand=arstechnica&utm_source=twitter&utm_social-type=owned&utm_medium=social](https://arstechnica.com/information-technology/2021/09/travis-ci-flaw-exposed-secrets-for-thousands-of-open-source-projects/?utm_brand=arstechnica&utm_source=twitter&utm_social-type=owned&utm_medium=social)

> But this month, researcher Felix Lange found a security vulnerability that caused Travis CI to include secure environment variables of all public open source repositories that use Travis CI into pull request builds. Environment variables can include sensitive secrets like signing keys, access credentials, and API tokens. If these variables are exposed, attackers can abuse the secrets to obtain lateral movement into the networks of thousands of organizations.
> 
> 


This was a shockingly bad vulnerability.  For an open source project from any company, the ability of an attacker to create a pull request, and use that to export secrets out of the build is nightmare fuel.  Those secrets likely give access to the packaging and release infrastructure, so could have compromised the release signing keys for example.


## [Cross-Account Container Takeover in Azure Container Instances](https://unit42.paloaltonetworks.com/azure-container-instances/)

[https://unit42.paloaltonetworks.com/azure-container-instances/](https://unit42.paloaltonetworks.com/azure-container-instances/)

> Cross-account vulnerabilities are often described as a "nightmare" scenario for the public cloud. Azurescape is evidence that they're more real than we'd like to think. Cloud providers invest heavily in securing their platforms, but it's inevitable that unknown zero-day vulnerabilities would exist and put customers at risk. Cloud users should take a defense-in-depth approach to cloud security to ensure breaches are contained and detected, whether the threat is from the outside or from the platform itself.
> 
> Preventing Similar Attacks on Kubernetes Environments
> 
> From the perspective of a Kubernetes defender, several best practices, mitigations and policies can help prevent or detect features of similar attacks:
> 
> * Keep your cluster infrastructure up to date and prioritize patches by severity and context.
> * Refrain from sending privileged service accounts tokens to anyone but the api-server. If a recipient is compromised, an attacker can masquerade as the token owner.
> * Enable BoundServiceAccountTokenVolume. This recently graduated feature gate ensures token expiration is bound to its pod. When a pod terminates, its token is no longer valid, minimizing the impact of token theft.
> * Deploy policy enforcers to monitor and prevent suspicious activity in your clusters. Configure them to alert on service accounts or nodes that query the SelfSubjectAccessReview or SelfSubjectRulesReview APIs for their permissions. Prisma Cloud customers can download a relevant rule template and enforce it via the built-in admission control for Kubernetes. We recommend setting the rule to Alert. Others can rely on open-source tools such as OPA Gatekeeper.
> 
> To expand on the last point, we see adversaries actively abusing the SelfSubjectReview APIs to inspect the privileges of stolen Kubernetes credentials. Daniel Prizmant, a fellow researcher, recently observed the Siloscape malware leveraging these APIs to retrieve the permissions of the node it compromised, and then using them to determine whether to continue its campaign against the cluster. We reported this behaviour to MITRE, and it will be included in the next release of ATT&CK for Containers as the Permission Group Discovery technique


Another cross account vulnerability, by running a known bad container in azures container platform, you can redirect requests to another customers container runtime that look authenticated and enable you to compromise them.

The detection here is interesting, because it looks for the use of an API that tells you what permissions you have. That’s something thats very occasionally useful for a normal process, but is super powerful for an attacker to work out what they’ve just achieved.

Secondly, remembering to limit the privileges of tokens and systems to only that needed by an application means that any breach will be limited in what they can do.


## [“Secret” Agent Exposes Azure Customers To Unauthorized Code Execution | Wiz Blog](https://www.wiz.io/blog/secret-agent-exposes-azure-customers-to-unauthorized-code-execution)

[https://www.wiz.io/blog/secret-agent-exposes-azure-customers-to-unauthorized-code-execution](https://www.wiz.io/blog/secret-agent-exposes-azure-customers-to-unauthorized-code-execution)

> Wiz’s research team recently discovered a series of alarming vulnerabilities that highlight the supply chain risk of open source code, particularly for customers of cloud computing services.
> 
> The source of the problem is a ubiquitous but little-known software agent called Open Management Infrastructure (OMI) that’s embedded in many popular Azure services.
> 
> When customers set up a Linux virtual machine in their cloud, the OMI agent is automatically deployed without their knowledge when they enable certain Azure services. Unless a patch is applied, attackers can easily exploit these four vulnerabilities to escalate to root privileges and remotely execute malicious code (for instance, encrypting files for ransom).
> 
> We named this quartet of zero-days “OMIGOD” because that was our reaction when we discovered them. We conservatively estimate that thousands of Azure customers and millions of endpoints are affected. In a small sample of Azure tenants we analyzed, over 65% were unknowingly at risk.


This one is a bit scary. As a reminder, if you didn’t install this software in your image but you checked a checkbox in the Azure control panel, then you got vulnerable software injected into the image. 

This vulnerability has since been detected in other systems, it’s not just Azure. 

Microsoft patched this quickly, so if you are redeploying your images on an hourly or daily basis through auto scaling and automatic rotation then you’ll be protected. Long lived images in the cloud however are likely still vulnerable. 


## [Vermilion Strike: Linux and Windows Re-implementation of Cobalt Strike](https://www.intezer.com/blog/malware-analysis/vermilionstrike-reimplementation-cobaltstrike/)

[https://www.intezer.com/blog/malware-analysis/vermilionstrike-reimplementation-cobaltstrike/](https://www.intezer.com/blog/malware-analysis/vermilionstrike-reimplementation-cobaltstrike/)

> Cobalt Strike is a popular red team tool for Windows which is also heavily used by threat actors. At the time of this writing, there is no official Cobalt Strike version for Linux.
> 
> In August 2021, we at Intezer discovered a fully undetected ELF implementation of Cobalt Strike’s beacon, which we named Vermilion Strike. The stealthy sample uses Cobalt Strike’s Command and Control (C2) protocol when communicating to the C2 server and has Remote Access capabilities such as uploading files, running shell commands and writing to files. The malware is fully undetected in VirusTotal at the time of this writing and was uploaded from Malaysia.


Useful reminder that you can’t just pop in the hashes of the default cobalt strike binaries, but that attackers might reimplement their own versions


## [China, Semiconductors, and the Push for Independence - Part 1 - by Lillian Li - Chinese Characteristics](https://lillianli.substack.com/p/china-semiconductors-and-the-push)

[https://lillianli.substack.com/p/china-semiconductors-and-the-push](https://lillianli.substack.com/p/china-semiconductors-and-the-push)

> China imports more chips than it does oil.
> 
> As we’ll see later, they have also made it evident that they are looking to lead the world in AI and industrial automation. This makes semiconductors not just their biggest chokepoint should international tensions exacerbate, but also their biggest constraint in achieving their tech growth goals.
> 
> Because of this, semiconductor manufacturing has become a national priority. The number of firms registering as semiconductor companies have grown by more than 700% in the last decade (Figure 12). Both state and private bodies are funnelling money into building out this capability. This is not just a CCP-driven, executive order. After Washington banned Huawei from using Cadence & Synopsys’ EDA platforms, there is also considerable private concerns within Chinese companies around who else the US might ban.


Absolutely fabulous deep dive into the economics of semiconductor and chip design and the implications and impact of the continuing cold war of technology between the US and China.  


## [ExpressVPN Knew 'Key Facts' of Executive Who Worked for UAE Spy Unit](https://www.vice.com/en/article/3aq9p5/expressvpn-uae-hacking-project-raven-daniel-gericke)

[https://www.vice.com/en/article/3aq9p5/expressvpn-uae-hacking-project-raven-daniel-gericke](https://www.vice.com/en/article/3aq9p5/expressvpn-uae-hacking-project-raven-daniel-gericke)

> "Daniel has a deep understanding of the tools and techniques used by the adversaries we aim to protect users against, and as such is a uniquely qualified expert to advise on defense against such threats. Our product and infrastructure have already benefited from that understanding in better securing user data," the statement continued.
> 
> On Tuesday, unsealed court filings described how Gericke as well as Marc Baier and Ryan Adams faced charges for their part in working on Project Raven. The court records say that the three violated the International Traffic in Arms Regulations and conspired to commit access device fraud and computer hacking offenses.
> 
> The court records say that the three took a zero-click exploit, which allows takeover of a device without any user interaction, and implemented that into Karma, the hacking system used by the UAE's Project Raven. Project Raven involved the hiring of former U.S. intelligence hackers who then worked on behalf of the UAE government, Reuters reported in 2019.


There’s a lot of bits to this set of stories, but the underlying story hasn’t changed much since the original [Reuters story from 2019 which I covered in Cyberweekly 39](https://cyberweekly.net/the-us-dominates-cyberspace), although now with the additional legal wrinkle of an accusation of [breaching the ITAR regulations](https://www.vice.com/en/article/3aq9a5/us-company-sold-zero-click-exploit-project-raven-uae).  

But the fact that one of the people involved went on to be the CIO at a VPN company does raise a lot of eyebrows.  While it’s true that clearly the best offense teams may also know how to defend, in many cases that’s not actually true.  They may know vulnerabilities, but the actions and activity that you go through to build a system is wildly different.


## [Process Eats Culture for Breakfast | by Mark Headd | Medium](https://mheadd.medium.com/process-eats-culture-for-breakfast-e5da02b2128e)

[https://mheadd.medium.com/process-eats-culture-for-breakfast-e5da02b2128e](https://mheadd.medium.com/process-eats-culture-for-breakfast-e5da02b2128e)

> It’s no secret that reduced project sizes and more rapid delivery to users improves project success rates, but why is it still so common to see large technology projects with long delivery timelines in government?
> 
> Let’s think about the processes that impact how a government technology project gets funded, approved, and implemented. these includes things like the budget process, intergovernmental funding and governance processes, and the accreditation process for software applications.
> 
> Federal and state budget processes begin many months before a single dollar ever gets spent. As much as 18 months before a budget is even enacted, the executive branch will transmit instructions to agencies for preparing the future budget request. This will include a complex set of documents that will capture the amount of funding that agencies will request , as well as a detailed justification for why they need it.
> 
> […]
> 
> 
> The success of a digital service teams’ efforts in working with an agency partner like this typically depends on whether they can instill the culture of “smallness,” by adopting approaches like modular contracting, DevOps, and Agile. Unwinding these plans for overly large technology projects, which fail more often than smaller ones, is not always successful. What’s often missed is that the budget process that makes funding for these projects available doesn’t just allow large projects to happen, it incentivizes them. It makes larger projects more likely than smaller ones.


As Mark says, it’s an oft-repeated saying that culture eats strategy for breakfast, but many people don’t realise what culture actually is.  You need more than just a small team of people who have access to some beanbags and post it notes, you need buy in for that cultural change throughout the organisation, including at the funding and programme planning levels.

Getting the culture right is part of the strategy, and needs effort and energy to deliver that strategy


## [Kevin Beaumont on Twitter: "What may be a Chinese APT broke into one of my honeypot orgs with ProxyShell. This will definitely be burning this honeypot, but in the public good. Hashes follow in thread. No analysis yet as busy with work. Had a custom IIS module backdoor, Mgbot (UDP backdoor) etc." / Twitter](https://mobile.twitter.com/GossiTheDog/status/1438500100238577670?s=20)

[https://mobile.twitter.com/GossiTheDog/status/1438500100238577670?s=20](https://mobile.twitter.com/GossiTheDog/status/1438500100238577670?s=20)

> What may be a Chinese APT broke into one of my honeypot orgs with ProxyShell.
> 
> This will definitely be burning this honeypot, but in the public good.  Hashes follow in thread.  No analysis yet as busy with work.
> 
> Had a custom IIS module backdoor, Mgbot (UDP backdoor) etc.


This is quite a ride 


## [how to hack the uk tax system, i guess | by Zemnmez | Medium](https://zemnmez.medium.com/how-to-hack-the-uk-tax-system-i-guess-3e84b70f8b)

[https://zemnmez.medium.com/how-to-hack-the-uk-tax-system-i-guess-3e84b70f8b](https://zemnmez.medium.com/how-to-hack-the-uk-tax-system-i-guess-3e84b70f8b)

> As someone who finds vulnerabilities in software, many parts of this foreign universe are more intricately familiar to me than the places I’ve lived. Someone with the right knowledge can send a little idea of their own into a computer, one that interacts, competes with and manipulates others to the author’s own ends.
> 
> All of us with these abilities have a moral compass they must construct for themselves. I don’t think anything has given me more respect for an individual’s right to their own boundaries and privacy than living and working every day with the knowledge of how to strip those boundaries away. Not all end up seeing the same way.
> 
> I try to do my best to do the right thing, but sometimes you can’t help trying to avoid putting yourself in that place where you should be doing the right thing. You ask yourself — if I invest a little time trying to do the right thing, am I going to be sucked into a 57 day trek trying to see it through? There comes a point at which even doing the right thing seems to have been the wrong choice.
> 
> If you choose to walk down the moral high road with security issues sometimes you will find people who care as much as you do. Other times you’ll find people whose job you’re just making more difficult, people who think you’re trying to harm them or their company and people who just don’t understand. Those are fights you have to fight yourself.
> 
> I’m happy to be working security in a time where we have bug bounties — where sometimes, if the planets align I can feel like I didn’t just do the right thing because I had to.
> 
> But the places where security help is needed most are the places that don’t have these security investments; the places that don’t know, can’t afford, or can’t understand the value of security. The places with no security email address or responsible disclosure procedure.
> 
> The security issues I found were complex. The issues that made fixing them take 57 days are simple, and common.
> Good security is an invisible luxury most places can’t afford. Security teams are expensive and hard to measure success for.


Ensuring that you have clear and easy ways to report security vulnerabilities is incredibly important.  You need to ensure that you not only have a contact point, but that the people who get reports in know how to route them to the right place, how to validate them and how to respond and support the researchers


## [Why Government and Military Sites Are Hosting Porn and Viagra Ads](https://www.vice.com/en/article/pkb5qy/why-government-and-military-sites-are-hosting-porn-and-viagra-adsovernm)

[https://www.vice.com/en/article/pkb5qy/why-government-and-military-sites-are-hosting-porn-and-viagra-adsovernm](https://www.vice.com/en/article/pkb5qy/why-government-and-military-sites-are-hosting-porn-and-viagra-adsovernm)

> According to a security researcher, the reason a lot of government websites are hosting these spammy ads is a vulnerability in a piece of software used by an array of government agencies. The vulnerability allowed third parties to push files to these sites without the site owners' permission.
> 
> "This vulnerability created phishing lures on .gov and .mil domains that would push visitors into malicious redirects, and potentially target these victims with other exploits," Zach Edwards, the security researcher, told Motherboard in an online chat.


This is another form of supply chain vulnerability.  The paucity of government suppliers means that a small number of suppliers have a much larger impact than one might imagine.  I wonder how quickly and easily all of those government departments will be able to patch?


