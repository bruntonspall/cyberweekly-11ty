---
title: "241 - Protecting the edge"
date: 2024-03-03
description: "The edge of our systems are both the most vulnerable and the most critical of our systems."
permalink: /protecting-the-edge/
---

The edge of our systems are both the most vulnerable and the most critical of our systems.

It's frequently the case that security appliances themselves can be some of the least effectively secure.  That might be because they're under the most attack, but it's also it's the fact that when compromised, these devices tend to disrupt the entire security model of our organisations.

That's why it's so critical that we start bearing down on the core vulnerabilities that still plague these devices, memory overflow vulnerabilities have been a problem for nearly 30 years now.  I remember reading [Aleph One's Smashing the stack for fun and profit](http://phrack.org/archives/issues/49/14.txt) when I was a teenager.  I didn't understand all of it, but I learned enough to realise how memory allocations could be abused and broken.  In [Ian Levy's goodbye note from NCSC](https://www.ncsc.gov.uk/blog-post/so-long-thanks-for-all-the-bits#section_2), he set out that we're still treating the symptom rather than the cause, that a whole category of memory vulnerabilities have stuck with us for decades and adoption of new languages like Rust that have built in protections for memory safety cannot come soon enough, and that we need to adopt them faster.

As such, it's nice to see that one of the core perimeter services that people use a lot, a reverse proxy, is being developed in a modern memory safe language.  Amazon have already done a lot of work on [TLS termination at scale in Rust](https://aws.amazon.com/blogs/security/introducing-s2n-quic-open-source-protocol-rust/) and I'm sure there are other Rust implementations of reverse proxies, but the internet drama this last few weeks in the nginx space, along with Cloudflare and others announcement of a new reverse proxy is a sign of increasing maturity in this space.

Sadly, as said above, we're still in a space where our security appliances are vulnerable to attack, and I've not yet seen highly capable firewall, packet inspection or VPN termination products that advertise memory safety and security being rolled out.  There's a lot of smaller projects that do this, but we're waiting for the industry to catch up, and in the meantime, adversarial teams are not only trying to compromise these devices, but actively attempting to retain access after the device has been factory reset.

While we'd love everyone to move to zero trust architectural models, we know that there's such a wealth of legacy systems, networks and capabilities that moving them all to new models is hard.  We have great patterns for how we build and adopt modern cloud stacks, but if we don't ensure that these patterns aren't undone by weaknesses at the edge, or a lack of investment in the attacks that we see in the real world, then we're just creating problems for the teenagers of today who are just learning about identity takeover, cloud account takeovers and lateral movement.

## [Cutting Edge, Part 3: Investigating Ivanti Connect Secure VPN Exploitation and Persistence Attempts | Mandiant ](https://www.mandiant.com/resources/blog/investigating-ivanti-exploitation-persistence)

[https://www.mandiant.com/resources/blog/investigating-ivanti-exploitation-persistence](https://www.mandiant.com/resources/blog/investigating-ivanti-exploitation-persistence)

> Mandiant and Ivanti's investigations into widespread [**Ivanti zero-day exploitation**](https://www.mandiant.com/resources/blog/suspected-apt-targets-ivanti-zero-day) have continued across a variety of industry verticals, including the U.S. defense industrial base sector. Following the initial publication on Jan. 10, 2024, Mandiant observed mass attempts to exploit these vulnerabilities by a small number of China-nexus threat actors, and development of a mitigation bypass exploit targeting [**CVE-2024-21893**](https://forums.ivanti.com/s/article/KB-CVE-2023-46805-Authentication-Bypass-CVE-2024-21887-Command-Injection-for-Ivanti-Connect-Secure-and-Ivanti-Policy-Secure-Gateways?language=en_US) used by [**UNC5325**](https://advantage.mandiant.com/actors/threat-actor--917abfd9-16ee-5109-bdc7-641eeb40442f#details) , which we introduced in our [**"Cutting Edge, Part 2" blog post**](https://www.mandiant.com/resources/blog/investigating-ivanti-zero-day-exploitation) . 
> 
> Notably, Mandiant has identified UNC5325 using a combination of living-off-the-land (LotL) techniques to better evade detection, while deploying novel malware such as LITTLELAMB.WOOLTEA in an attempt to persist across system upgrades, patches, and factory resets. While the limited attempts observed to maintain persistence have not been successful to date due to a lack of logic in the malware's code to account for an encryption key mismatch, it further demonstrates the lengths UNC5325 will go to maintain access to priority targets and highlights the importance of ensuring network appliances have the latest updates and patches.
> 
> […]
> 
> It's important to note that `/bin/losetup` uses an embedded encryption key within the running version's kernel used to decrypt the running version's partition. This encryption key is hardcoded at the time of build compilation and is unique for each appliance version.
> 
> However, the factory reset partition maintains its own independent encryption key embedded in the factory kernel. If the current running version and the factory reset deployment versions differ (i.e., the appliance or VM has been updated at least once), then `/bin/losetup` will fail to decrypt the factory reset partition due to the encryption key mismatch and thus the malware will not persist after factory reset.
> 
> Note that Mandiant and Ivanti conducted forensic analysis on an affected appliance after factory reset to confirm no evidence of malware persistence. Because the appliance had undergone at least one update since its initial deployment, the malware failed to persist through the factory reset as the encryption key of the factory reset kernel and the running version kernel were different. 


This work from Mandiant shows the intent and capability of the UNC5325 actor to maintain their access after the compromise was completed.  This set of attacks take advantage of the role of network devices on the perimeter, as well the requirement for them to be involved in security enforcing functions.  That’s what makes them such a valuable target to such teams 


## [Announcing River: A High Performance and Memory Safe Reverse Proxy Built on Pingora ](https://www.memorysafety.org/blog/introducing-river/)

[https://www.memorysafety.org/blog/introducing-river/](https://www.memorysafety.org/blog/introducing-river/)

> Just about every significant deployment on the Internet makes use of reverse proxy software, and the most commonly deployed reverse proxy software is not memory safe. This means that most deployments have millions of lines of C and C++ handling incoming traffic at the edges of their networks, a risk that [needs to be addressed](https://www.whitehouse.gov/oncd/briefing-room/2024/02/26/press-release-technical-report/) if we are to have greater confidence in the security of the Internet. In order to change this, Prossimo is investing in new reverse proxy software called [River](https://www.memorysafety.org/initiative/reverse-proxy/) , which will offer excellent performance while reducing the chance of memory safety vulnerabilities to near zero. 


I applaud this.  There are entire classes of vulnerabilities that memory safe languages like Rust can deal with.  It was has been pointed out to me, current systems like Nginx are still suffering from use-after-free vulnerabilities in new code written today.

However, it’s also worth remembering that memory vulnerabilities aren’t the only vulnerabilities that we find.   This is a great improvement in hardening one of the core services on your perimeter, but there’s still more to do at the architectural, configuration and management layers 


## [Passkeys - Threat modeling and implementation considerations | SlashID Blog ](https://slashid.com/blog/passkeys-security-implementation/)

[https://slashid.com/blog/passkeys-security-implementation/](https://slashid.com/blog/passkeys-security-implementation/)

> As mentioned above, passkeys are key pairs, and the private key is not supposed to be accessible to the relying party or the outside world. According to the WebAuthn standards, there are two types of credentials:
> 
> 1. [Discoverable credentials](https://www.w3.org/TR/webauthn/#discoverable-credential) : stored on the client device, meaning that the private key itself is stored in the persistent storage embedded in the authenticator
> 
> 2. [Server-side credentials](https://www.w3.org/TR/webauthn/#server-side-credential) : The private key is encrypted with a second private key stored in the authenticator. The resulting blob is used as the credential ID for the key pair. There are multiple ways to achieve this; the most common one is called [key wrapping](https://en.wikipedia.org/wiki/Key_wrap) . Note that while the relying party does have access to the private key, the relying party won’t be able to access it without the access to the authenticator, providing security guarantees similar to discoverable credentials
> 
> Passkeys add a twist to this concept as they are discoverable credentials that can be exported from the authenticator.
> 
> It is critical to notice that while passkeys will reduce adoption friction for WebAuthn, the security guarantees of passkeys are lower than regular, non-exportable, WebAuthn credentials and they are not standardized. 


Passkeys are really interesting, but one of the things that we are bad is weighing up whether taking on something that has some known risks or flaws but fixes things we care about is a good move or not 


## [Hugging Face, the GitHub of AI, hosted code that backdoored user devices | Ars Technica ](https://arstechnica.com/security/2024/03/hugging-face-the-github-of-ai-hosted-code-that-backdoored-user-devices/)

[https://arstechnica.com/security/2024/03/hugging-face-the-github-of-ai-hosted-code-that-backdoored-user-devices/](https://arstechnica.com/security/2024/03/hugging-face-the-github-of-ai-hosted-code-that-backdoored-user-devices/)

> One model drew particular concern because it opened a reverse shell that gave a remote device on the Internet full control of the end user’s device. When JFrog researchers loaded the model into a lab machine, the submission indeed loaded a reverse shell but took no further action.
> 
> That, the IP address of the remote device, and the existence of identical shells connecting elsewhere raised the possibility that the submission was also the work of researchers. An exploit that opens a device to such tampering, however, is a major breach of researcher ethics and demonstrates that, just like code submitted to GitHub and other developer platforms, models available on AI sites can pose serious risks if not carefully vetted first.
> 
> “The model’s payload grants the attacker a shell on the compromised machine, enabling them to gain full control over victims’ machines through what is commonly referred to as a ‘backdoor,’” JFrog Senior Researcher David Cohen [wrote](https://jfrog.com/blog/data-scientists-targeted-by-malicious-hugging-face-ml-models-with-silent-backdoor/) . “This silent infiltration could potentially grant access to critical internal systems and pave the way for large-scale data breaches or even corporate espionage, impacting not just individual users but potentially entire organizations across the globe, all while leaving victims utterly unaware of their compromised state.” 


It’s not always clear to people that data models for AI are also code.  If you download a model from the internet, then you should treat it both as user generated data, as well as remote code being executed on your machine.

Downloading a random bit of code and running on your computer and finding that it executes a remote shell shouldn’t be that much of a surprise.  We’ve seen this in other executable repositories.  Worth talking to your data science team and understanding what their model is for validating or checking models they want to use. 


## [Over 100,000 Infected Repos Found on GitHub ](https://apiiro.com/blog/malicious-code-campaign-github-repo-confusion-attack/)

[https://apiiro.com/blog/malicious-code-campaign-github-repo-confusion-attack/](https://apiiro.com/blog/malicious-code-campaign-github-repo-confusion-attack/)

> Similar to dependency confusion attacks, malicious actors get their target to download their malicious version instead of the real one. But dependency confusion attacks take advantage of how package managers work, while repo confusion attacks simply rely on humans to mistakenly pick the malicious version over the real one, sometimes employing social engineering techniques as well.
> 
> In this case, in order to maximize the chances of infection, the malicious actor is flooding GitHub with malicious repos, following these steps:
> 
> * Cloning existing repos (for example: TwitterFollowBot, WhatsappBOT, discord-boost-tool, Twitch-Follow-Bot, and hundreds more).
> * Infecting them with malware loaders.
> * Uploading them back to GitHub with identical names.
> * Automatically forking each thousands of times.
> * Covertly promoting them across the web via forums, discord, etc. 


This relies on confusion and people downloading code and running it with no inspection.

Github takes these down as fast as they can, but it’s worth remembering when you look at random repositories online, that it might be a copy that contains malicious code.

The likelihood might be rare, but the concerted effort here makes it increasingly possible. 


## [The Most Dangerous Entra Role You’ve (Probably) Never Heard Of | by Andy Robbins | Feb, 2024 | Posts By SpecterOps Team Members ](https://posts.specterops.io/the-most-dangerous-entra-role-youve-probably-never-heard-of-e00ea08b8661)

[https://posts.specterops.io/the-most-dangerous-entra-role-youve-probably-never-heard-of-e00ea08b8661](https://posts.specterops.io/the-most-dangerous-entra-role-youve-probably-never-heard-of-e00ea08b8661)

> **How Powerful is Partner Tier2 Support?** Extremely powerful. “Partner Tier2 Support” is not quite as powerful as Global Admin, but the role **does** allow a principal with the role to promote themselves or any other principal to Global Admin. Here are the notable privileged actions a principal with the “Partner Tier2 Support” admin role assignment can do:
> 
> * Promote itself to Global Admin
> * Reset the password for any user, including Global Admins
> * Grant any service principal any app role
> * Grant admin consent to any app role
> * Add new credentials to all existing app registrations
> * Add new owners to all existing app registrations
> * Add new members to non-role-assignable groups
> * Add new owners to non-role-assignable groups 
> 
> **An Attractive, Obscure Backdoor** 
> 
> Admins who want to audit assignments for this role face a challenge: the Azure portal GUI hides the role from view. Entra ID roles can be seen by navigating to Entra ID > Roles and administrators. Scroll down the alphabetically-ordered list of roles, and you would expect to see “Partner Tier2 Support” here 


This is something that was flagged last year by Microsoft, but fairly quietly.  It’s slightly frustrating that Entra makes it deliberately hard to see this role, meaning that you need to know about it in order to audit it.

The info in here gives some useful pointers on how to find it and add it to your audit logs, and this one should go to the top of your audit list.  If you don’t have a tier2 partner in your org, then any account having this role added should be an immediate red flag 


## [Navigating the Cloud: Exploring Lateral Movement Techniques ](https://unit42.paloaltonetworks.com/cloud-lateral-movement-techniques/)

[https://unit42.paloaltonetworks.com/cloud-lateral-movement-techniques/](https://unit42.paloaltonetworks.com/cloud-lateral-movement-techniques/)

> Attackers with sufficient privileges at the cloud API level can take advantage of the characteristics of cloud environments for lateral movement using cloud APIs. Cloud APIs often enable attackers to pivot through compute instances with relative ease compared to traditional lateral movement in typical on-premises environments. However, on-premises environments, especially virtualized environments with the equivalent power available to an attacker with access to the virtualization layer, have plenty of risks of this type as well.
> 
> For some of the scenarios described, there may be detections and remediations available from CSPs or other sources. Defenders should be aware of the options available to improve their cloud security posture.
> 
> Since misconfigurations and similar issues can often weaken organizations’ cloud security, defenders should pay particular attention to using best practices recommended by your CSP, and also to ensuring that your configuration matches your security needs. 


There’s some lovely attacks in here.  The ability of the cloud service provider to push SSH keys into the instance is a fundemental requirement for bringing up new machines as part of the cloud-init capability.  But of course that also means that an attacker with the right credentials can push local authentication credentials into your machine.  Combining that with the ability to modify firewalls, or worse, get into the device from a virtualised serial port, which defeats some of your expected threat modelling on how SSH connections are made.

As they say, pay careful attention to the permissions you give cloud accounts, what detections you have for the use of certain APIs and apply best practice from your cloud provider 


## [Design your Landing Zone — Design Considerations Part 1 (Google Cloud Adoption Series) | by Dazbo (Darren Lester) | Google Cloud - Community | Feb, 2024 | Medium ](https://medium.com/google-cloud/design-your-landing-zone-design-considerations-part-1-google-cloud-adoption-series-74978d968fed)

[https://medium.com/google-cloud/design-your-landing-zone-design-considerations-part-1-google-cloud-adoption-series-74978d968fed](https://medium.com/google-cloud/design-your-landing-zone-design-considerations-part-1-google-cloud-adoption-series-74978d968fed)

> This example LZ provides:
> 
> * A defined **organisational hierarchy** , with organisational policies configured and a predefined set of folders.
> * **Hybrid connectivity** between on-premises and two Google Cloud regions.
> * A **shared VPC** that provides common services, such as: connectivity to on-prem, Internet egress, and a multitenant GKE environment.
> * Centrally managed **CI/CD pipelines** for deployment of infrastructure services.
> * A **project factory** , that allows self-service creation of tenant projects running tenant-specific workloads. These may be peered to the “hub” shared VPC, or may utilise resources in the shared VPC directly. 
> 
> **Why Do You Need a Landing Zone?** 
> 
> Landing zones are a way for an organisation / enterprise to build their Google Cloud environment in a structured and consistent way, following **proven best practice** . It ensures that all the _tenants_ running on the landing zone avoid re-inventing the wheel, are using appropriate **shared components** , are **adhering to your policies** , and are only building their environments using approved infra-as-code (IaC).
> 
> Thus, the landing zone:
> * **Minimises engineering overhead** by providing an automated **Infrastructure-as-Code (IaC)** driven approach to creating an organisation in GCP, and for **subsequently deploying tenants and their resources** to this GCP organisation.
> 
> […]
> 
> Moreover, creation of a landing zone forces the organisation to make a number of **early (and important) design decisions** . This is ensures that the LZ is built according to the current and future requirements of your organisation.
> 
> If you skip LZ design, then your Google Cloud adoption will likely be naive and unstructured. You will soon struggle to manage your estate. You will struggle with estate visibility and you will lose visibility of your projects. You will struggle to implement FinOps best practices and you will lose control of your costs. You will hit scaling issues, and likely hit avoidable Google Cloud limitations. You will organise your teams badly, and waste unnecessary engineering effort managing your cloud. 


This guidance that helps teams work out how to adopt the Google Cloud with a Landing Zone pattern is a great example of the wider landing zone pattern for any cloud provider.  

There’s a fundamental disagreement in tech about whether it’s better to build a prototype and adopt from that, or invest in building the platform leads to a lot of organisations doing cloud adoption by giving their development teams a credit and telling them to go wild.

That’s not a terrible plan for your very first prototypes, where you have limited risk, but if your enterprise is migrating in bulk, then you’ll want to develop a plan like this which carries out the hard work of building consistent, capable and well managed core services like CI/CD, project factories and identity systems. 


## [Microsoft Actions Following Attack by Nation State Actor Midnight Blizzard | MSRC Blog | Microsoft Security Response Center ](https://msrc.microsoft.com/blog/2024/01/microsoft-actions-following-attack-by-nation-state-actor-midnight-blizzard/)

[https://msrc.microsoft.com/blog/2024/01/microsoft-actions-following-attack-by-nation-state-actor-midnight-blizzard/](https://msrc.microsoft.com/blog/2024/01/microsoft-actions-following-attack-by-nation-state-actor-midnight-blizzard/)

> This attack does highlight the continued risk posed to all organizations from well-resourced nation-state threat actors like Midnight Blizzard.  
> 
> As we said late last year when we announced [Secure Future Initiative (SFI)](https://blogs.microsoft.com/on-the-issues/2023/11/02/secure-future-initiative-sfi-cybersecurity-cyberattacks/), given the reality of threat actors that are resourced and funded by nation states, we are shifting the balance we need to strike between security and business risk – the traditional sort of calculus is simply no longer sufficient. For Microsoft, this incident has highlighted the urgent need to move even faster. We will act immediately to apply our current security standards to Microsoft-owned legacy systems and internal business processes, even when these changes might cause disruption to existing business processes.


This attack was significant, but as set out here, the answer for someone like Microsoft is not just fixing things going forward, but ensuring that they also fix a long legacy of historical systems and decisions, bringing them up to speed as well


