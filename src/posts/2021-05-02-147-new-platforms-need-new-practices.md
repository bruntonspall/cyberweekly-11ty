---
title: "147 - New platforms need new practices"
date: 2021-05-02
description: "As we move towards new platforms, we have to accept that currently accepted “best practice” is no longer suited."
permalink: /new-platforms-need-new-practices/
---

As we move towards new platforms, we have to accept that currently accepted “best practice” is no longer suited.

Simon Wardley calls this [coevolution of practice](https://medium.com/wardleymaps/anticipation-89692e9b0ced), which is where a practice relies on innate features of the product in question.  As the nature of the product evolves, those innate features also evolve and the practice no longer works, instead brand new practices need to be developed to help manage those products.

Simon uses the rise of DevOps and scale out architectures compared to traditional enterprise models and scale up architectures, but what’s more interesting to me is the sheer number of people trying to apply best existing practice to new architectures that they fundamentally don’t fit.

Whether that be people attempting to put virtual firewalls into their systems in the cloud, or the misapplication of docker image practices, security tends to be one of the last to know about changing product worlds, and therefore the last to provide good up to date practices that work with new models.

Security practices are incredibly embedded in the how of product working. Why is creating a firewall VM something that I consider a bad practice in the cloud?  Because cloud networking is software defined networking, which means that any semi-competent attacker is far more easily able to get into the cloud management plane and instruct the cloud system to create network routes around the VM.  In built cloud networking systems are designed to work within these models, and it’s far easier to use the cloud providers native features to create network gateways and pinch points to route traffic through.

Of course, sometimes we want features in these appliances that don’t exist in the cloud based networking facilities, so you might be expecting some level of content inspection and cleansing being done before content reaches your application, and in those cases, we might want to consider the use of proxy style VM’s, but in many cases, the cloud providers give us native abstractions that can be used to provide the same functionality in a different architectural implementation.

We need to recognise that best practices from the previous generations of architecture are not the same practices that we should use with next generation architectures.  Instead of best practices, we need to look for up and coming emerging practices that achieve the same intentional outcomes.

## [The worst so-called “best practice” for Docker](https://pythonspeed.com/articles/security-updates-in-docker/)

[https://pythonspeed.com/articles/security-updates-in-docker/](https://pythonspeed.com/articles/security-updates-in-docker/)

> Please install security updates
> 
> To conclude, the idea you shouldn’t install security updates is based on either:
> 
>     Obsolete problems (“upgrades don’t work”).
>     Theoretical ideal worlds we don’t live in (“the base image will install updates”).
>     Non-sequiturs (“you can’t upgrade inside an unprivileged container”).
>     Requiring a heavyweight process most people don’t need, namely pinning all system packages. You should be pinning your Python dependencies, though, since they’ll change meaningfully far more frequently than packages in a long-term-support Linux distribution.
> 
> Please, run dnf/apk/apt-get upgrade in your Dockerfile, you really do want to install security updates in your Docker image.


You should always run the dnf/apt-get upgrade command as one of the first commands in your images to ensure that your docker images have security updates applied.


## [A practical guide to writing secure Dockerfiles | by Madhu Akula | Miro Engineering | Apr, 2021 | Medium](https://medium.com/miro-engineering/a-practical-guide-to-writing-secure-dockerfiles-bf561224dd80)

[https://medium.com/miro-engineering/a-practical-guide-to-writing-secure-dockerfiles-bf561224dd80](https://medium.com/miro-engineering/a-practical-guide-to-writing-secure-dockerfiles-bf561224dd80)

> Sometimes, developers and organizations use insecure ways to pass secrets and sensitive information to the Dockerfile during build time. For example, they hardcode the data in the Dockerfile, or they pass it via build arguments.
> 
> Both examples are flawed: if you hardcode AWS secrets in the Dockerfile, any user or attacker with access to the file has access to the AWS environment. Similarly, if we pass the secrets as build arguments, they are available in the Docker build history, which is easy to obtain and to look up to gain access to the AWS environment.
> 
> BuildKit offers a best practice approach to pass secrets to the Dockerfile.
> 
> In the example above we pass the AWS secrets via the mount option from the host system. In this way, the secrets are available only during build time; they aren’t stored in the Docker build history or in the Dockerfile.


This is a great summary of some of the better features for writing Dockerfiles.

It also drops into a description and overview of OPA for configuration file analysis as well.


## [Docker Security - OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html)

[https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html)

> Docker is the most popular containerization technology. Upon proper use, it can increase the level of security (in comparison to running applications directly on the host). On the other hand, some misconfigurations can lead to downgrade the level of security or even introduce new vulnerabilities.
> 
> The aim of this cheat sheet is to provide an easy to use list of common security mistakes and good practices that will help you secure your Docker containers.
> 
>   *    RULE #0 - Keep Host and Docker up to date
>   *    RULE #1 - Do not expose the Docker daemon socket (even to the containers)
>   *    RULE #2 - Set a user
>   *    RULE #3 - Limit capabilities (Grant only specific capabilities, needed by a container)
>   *    RULE #4 - Add –no-new-privileges flag
>   *    RULE #5 - Disable inter-container communication (--icc=false)
>   *    RULE #6 - Use Linux Security Module (seccomp, AppArmor, or SELinux)
>   *   RULE #7 - Limit resources (memory, CPU, file descriptors, processes, restarts)
>   *  RULE #8 - Set filesystem and volumes to read-only
>   *  RULE #9 - Use static analysis tools
>   *  RULE #10 - Set the logging level to at least INFO
>   *  Rule #11 - Lint the Dockerfile at build time


A useful cheat sheet for some simple and foundational rules for using Docker in your infrastructure


## [What’s New in ATT&CK v9?. Data Sources, Containers, Cloud, and more | MITRE ATT&CK®](https://medium.com/mitre-attack/attack-april-2021-release-39accaf23c81)

[https://medium.com/mitre-attack/attack-april-2021-release-39accaf23c81](https://medium.com/mitre-attack/attack-april-2021-release-39accaf23c81)

> As much as we love tracking and nerding out over adversary behaviors, one of the most important goals of ATT&CK is to bridge offensive actions with potential defensive countermeasures. We strive to achieve this goal by tagging each (sub-)technique with defensive-focused fields/properties, such as what data to collect (data sources) and how to analyze that data in order to potentially identify specific behaviors (detections).
> 
> Many of you in the community have made great use of ATT&CK data sources ¹ ² ³, but we heard from you and recognized the opportunity for improvement. Our goal for the new data sources is to better connect the defensive data in ATT&CK with how operational defenders see and work these challenges.


This latest ATT&CK update includes a lovely data mapping tool that makes it possible to see how a given technique or tool creates data exhaust.  

That makes it easy to work out if you are collecting the right data from logs to be able to detect specific attacks.


## [Cloud lateral movement: Breaking in through a vulnerable container | Sysdig](https://sysdig.com/blog/lateral-movement-cloud-containers/)

[https://sysdig.com/blog/lateral-movement-cloud-containers/](https://sysdig.com/blog/lateral-movement-cloud-containers/)

> from the hostname, apache-struts-6c8974d494, the attacker can see they landed in a pod or container inside a Kubernetes Cluster.
> 
> Step 2: Lateral movement to the cloud
> 
> Now that our adversary is in, they have to reckon the terrain. You may think that having landed in a container, the attacker is fairly restricted. And you would be correct, but they still have some options to compromise our cloud security.
> 
> The attacker checks if the pod has access to the AWS instance metadata. 
> 
>  It looks like it does. There might be useful information regarding the cloud environment that would help the attacker escalate privileges or perform lateral movement.
> 
> Looking at the IAM credentials, the adversary finds the AWS IAM role credentials associated with the Kubernetes node where the pod is running. 


You might think that just because someone can compromise a container within your platform, that's not a risk to the platform, but in reality, from the container there are all kinds of things that a misconfigured platform can allow access to.

It's worth noting that containers don't really have any good reason to be able to access the underlying platform metadata, so this level of leakage is how the attacker can move laterally out of the container.


## [Signal >> Blog >> Exploiting vulnerabilities in Cellebrite UFED and Physical Analyzer from an app's perspective](https://signal.org/blog/cellebrite-vulnerabilities/)

[https://signal.org/blog/cellebrite-vulnerabilities/](https://signal.org/blog/cellebrite-vulnerabilities/)

> hen Cellebrite announced that they added Signal support to their software, all it really meant was that they had added support to Physical Analyzer for the file formats used by Signal. This enables Physical Analyzer to display the Signal data that was extracted from an unlocked device in the Cellebrite user’s physical possession.
> 
> One way to think about Cellebrite’s products is that if someone is physically holding your unlocked device in their hands, they could open whatever apps they would like and take screenshots of everything in them to save and go over later. Cellebrite essentially automates that process for someone holding your device in their hands.
> The rite place at the Celleb…rite time
> 
> By a truly unbelievable coincidence, I was recently out for a walk when I saw a small package fall off a truck ahead of me. As I got closer, the dull enterprise typeface slowly came into focus: Cellebrite. Inside, we found the latest versions of the Cellebrite software, a hardware dongle designed to prevent piracy (tells you something about their customers I guess!), and a bizarrely large number of cable adapters.


This blogpost is quite the read!  Entertaining and informative at the same time.

It's a good reminder that encrypted end to end messaging is only secure against people on the network between the two ends.  Anyone who can access or control either end of the conversation is outside of the main threat model of most encrypted messaging systems.


## [Et tu, Signal?](https://www.stephendiehl.com/blog/signal.html)

[https://www.stephendiehl.com/blog/signal.html](https://www.stephendiehl.com/blog/signal.html)

> Let it be said that everything here is probably entirely legal or there simply is no precedent yet. The question everyone is asking before these projects launch now though is: should it be?
> 
> I think I speak for many technologists when I say that any bolted-on cryptocurrency monetization scheme smells like a giant pile of rubbish and feels enormously user-exploitative. We’ve seen this before, after all Telegram tried the same thing in an ICO that imploded when SEC shut them down, and Facebook famously tried and failed to monetize WhatsApp through their decentralized-but-not-really digital money market fund project.
> 
> The whole Libra/Diem token (or whatever they’re calling its remains this week) was a failed Facebook initiative exploiting the gaping regulatory loophole where if you simply call yourself a cryptocurrency platform (regardless of any technology) you can effectively function as a shadow bank and money transmistter with no license, all while performing roughly the same function as a bank but with magic monopoly money that you can print with no oversight while your customers assume full counterparty risk. If that sounds like a terrible idea, it’s because it is. But we fully expect that level of evil behavior from Facebookers because that’s kind of their thing.
> 
> The sad part of this entire project is that it launched in the UK—likely because it would be blatantly illegal in the United States—where here retail transfers are ubiquitous, instant, and cheap. The digital sterling held at our high street bank or mobile banking app works very well as a currency, and nobody needs or wants to buy a dedicated trashcoin for every single app on our mobiles. This is all just bringing us back to some stone age barter system for no reason.


A strong, but legitimate response to Signals announcement that they are adding a cryptocurrency to Signal for UK users.


## [European MPs targeted by deepfake video calls imitating Russian opposition | Russia | The Guardian](https://www.theguardian.com/world/2021/apr/22/european-mps-targeted-by-deepfake-video-calls-imitating-russian-opposition)

[https://www.theguardian.com/world/2021/apr/22/european-mps-targeted-by-deepfake-video-calls-imitating-russian-opposition](https://www.theguardian.com/world/2021/apr/22/european-mps-targeted-by-deepfake-video-calls-imitating-russian-opposition)

> Kols said he had been approached by email by a person claiming to be Volkov and had held a short video-conference call with him, where they discussed support for Russian political prisoners and the Russian annexation of Crimea. Only later did he realise he may have been the victim of a hi-tech prank, he said.
> 
> “Quite a painful lesson, but perhaps we can also say thanks to this fake Volkov for this lesson for us and Lithuanian and Estonian colleagues,” he wrote. “It is clear that the so-called truth decay or post-truth and post-fact era has the potential to seriously threaten the safety and stability of local and international countries, governments and societies.”
> 
> Volkov accused a Russian duo named Vovan and Lexus, who regularly target western officials, of being behind the call.
> 
> Reached by Facebook, Alexei Stolyarov, who goes by the pseudonym Lexus, did not deny speaking with Kols, saying he would “keep it a secret”. He did deny using a filter to appear like Volkov, writing: “Probably Volkov has false information.”
> 
> He sent a link to a tongue-in-cheek denial on Telegram, where an acquaintance claimed he was “with Leonid in Donetsk right now”, posting a photo of Stolyarov in what appeared to be facial makeup.


If there was makeup and prosthetics involved, it probably wasn’t deep fake technology.

But if pranksters, (the same ones who called the prime minister pretending to be the Armenian PM, or who called Elton John pretending to be Putin)[https://www.theguardian.com/world/2016/mar/13/kremlin-calling-russian-pranksters-elton-john-owes-us], are able to convincingly and repeatedly do this, it makes you wonder just how good real spies are?


## [Institute for Security and Technology (IST) » RTF Report: Combatting Ransomware](https://securityandtechnology.org/ransomwaretaskforce/report/)

[https://securityandtechnology.org/ransomwaretaskforce/report/](https://securityandtechnology.org/ransomwaretaskforce/report/)

> This strategic framework aims to help policymakers and industry leaders take system-level action — through potential legislation, funding new programs, or launching new industry-level collaborations — that will help the international community build resistance, disrupt the ransomware business model, and develop resilience to the ransomware threat.
> The framework is organized around four goals: 
> 
> * deter ransomware attacks through a nationally and internationally coordinated, comprehensive strategy; 
> * disrupt the ransomware business model and reduce criminal profits; 
> * help organizations prepare for ransomware attacks; and 
> * respond to ransomware attacks more effectively.
> 
> These goals are interlocking and mutually reinforcing. For example, actions to disrupt the ransomware payments system will decrease the profitability of ransomware, thereby helping to deter other actors from engaging in this crime. Thus, this framework should be considered as a whole, not merely a laundry list of disparate actions.


This is a lovely report to talk about the strategy that we need to take as an industry and set of governments to deter, disrupt and respond to ransomware as an entire category of attack


## [New Ransomware Variant - .hello ransomware | Pondurance](https://www.pondurance.com/blog/new-ransomware-variant-hello-ransomware/)

[https://www.pondurance.com/blog/new-ransomware-variant-hello-ransomware/](https://www.pondurance.com/blog/new-ransomware-variant-hello-ransomware/)

> On January 13, 2021, our security analysts discovered a brand new ransomware variant — .hello ransomware or WickrMe Ransomware. The actor uses a Microsoft SharePoint 2019 vulnerability (CVE-2019-0604) to enter the victims’ network. From there, the threat actor leverages Cobalt Strike to pivot to the domain controller and launch ransomware attacks. 
> 
> As we know, Cobalt Strike is a legitimate threat emulation tool popular among penetration testers and red teams. However, the framework has leaked and been distributed more broadly often being abused by bad actors. 
> 
> This cyber attack seems to be the same vulnerability used against the United Nations back in July 2019. As reported by Dark Reading, the same Microsoft SharePoint vulnerability CVE-2019-0604 was used to gain access to the victim’s environment. The cyber attack resulted in 400GB of data being downloaded by the threat actor. 
> 
> 


The sharepoint vulnerability is from 2019, but people have still not managed to patch effectively.


