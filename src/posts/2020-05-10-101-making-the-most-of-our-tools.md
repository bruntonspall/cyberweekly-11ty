---
title: "101 - Making the most of our tools"
date: 2020-05-10
description: "Whenever I go to a new client and meet their security team, one of the things I always try to get a good glimpse of is their security tools.  How do they track risks on projects? store penetration test results? set and enforce policies on development teams?"
permalink: /making-the-most-of-our-tools/
---

Whenever I go to a new client and meet their security team, one of the things I always try to get a good glimpse of is their security tools.  How do they track risks on projects? store penetration test results? set and enforce policies on development teams?

Most of the time I am disappointed and a little scared.  The most common tool I see for all of these things is a set of spreadsheets and a shared drive for the team.  Projects take a risk log and modify it so it suits them, copies are strewn all over the place, and the number of times that i've been sent old copies of security documentation in word format that still contains tracked changes from the previous security assessor is depressing.

The world of development has mostly moved on from sending around big word documents of system specifications and test cases and thoroughly adopted the idea that in order to get faster at maintaining and adopting this stuff, it needs to be written in code and automated.  Security teams haven't really gotten there yet.

I've highlighted a number of tools that have caught my eye over the last few months, from policy enforcement to infrastructure as code that is PCI compliant.

But as we move our policies and processes into code, this creates new vulnerabilities for attackers to exploit.  Adopting security as code is the next big step for many security teams, but soon after that will come the recognition that all code can have security vulnerabilities, and that includes out policy enforcement code, our infrastructure management code and our automation tools themselves.

Of course, before we start worrying about that, we need mass adoption of these time saving tools.  We need security teams to recognise that infrastructure as code is more auditable, more precise and more secure than the old ways of doing things and actively encourage it.

## [How Profit and Incompetence Delayed N95 Masks While… — ProPublica](https://www.propublica.org/article/how-profit-and-incompetence-delayed-n95-masks-while-people-died-at-the-va)

[https://www.propublica.org/article/how-profit-and-incompetence-delayed-n95-masks-while-people-died-at-the-va](https://www.propublica.org/article/how-profit-and-incompetence-delayed-n95-masks-while-people-died-at-the-va)

> The deal’s tenuous nature — a broker Stewart didn’t know, buying from a seller he didn’t know, financed by someone he didn’t know — seemed a profound and expensive leap of faith. But Stewart was convinced that he was “getting the VA a good thing at a good price.”
> 
> He had been called to action, he said, after seeing a CNN segment where a nurse described making her own face shield out of plastic film. As a former Air Force officer, he said he felt compelled to help.
> 
> “The goal here is not to get rich,” he said. FGE would be lucky to pocket about 10 cents a mask, he said, somewhere around $600,000, when the VA got its goods.


This story is quite a wild ride, and shows the nature of the US commercial market at this time.

But it also reminds us that we worry a lot about fraudulant actors, about deliberately malicious actors who will lie and scheme to get something of value, but what we don't consider often enough is people with good intention and good will being completely unable to actually operate effectively.  This story reminds me of some of the security software sales calls I've been on, where the sales person means well, but is just clearly out of their depth and has no understanding of what they are selling, what context their product operates in or whether it's any good.


## [Zoom Acquires Keybase and Announces Goal of Developing the Most Broadly Used Enterprise End-to-End Encryption Offering - Zoom Blog](https://blog.zoom.us/wordpress/2020/05/07/zoom-acquires-keybase-and-announces-goal-of-developing-the-most-broadly-used-enterprise-end-to-end-encryption-offering/)

[https://blog.zoom.us/wordpress/2020/05/07/zoom-acquires-keybase-and-announces-goal-of-developing-the-most-broadly-used-enterprise-end-to-end-encryption-offering/](https://blog.zoom.us/wordpress/2020/05/07/zoom-acquires-keybase-and-announces-goal-of-developing-the-most-broadly-used-enterprise-end-to-end-encryption-offering/)

> Today, audio and video content flowing between Zoom clients (e.g., Zoom Rooms, laptop computers, and smartphones running the Zoom app) is encrypted at each sending client device.  It is not decrypted until it reaches the recipients’ devices. With the recent Zoom 5.0 release, Zoom clients now support encrypting content using industry-standard AES-GCM with 256-bit keys. However, the encryption keys for each meeting are generated by Zoom’s servers. Additionally, some features that are widely used by Zoom clients, such as support for attendees to call into a phone bridge or use in-room meeting systems offered by other companies, will always require Zoom to keep some encryption keys in the cloud. However, for hosts who seek to prioritize privacy over compatibility, we will create a new solution.
> 
> [...]
> 
> We are committed to remaining transparent and open as we build our end-to-end encryption offering. We plan to publish a detailed draft cryptographic design on Friday, May 22. We will then host discussion sections with civil society, cryptographic experts, and customers to share more details and solicit feedback. Once we have assessed this feedback for integration into a final design, we will announce our engineering milestones and goals for deploying to Zoom users.


This is an interesting announcement by Zoom.  I suspect it means that Keybase as a product is about to be completely scalped, and all of the engineers given over to working on encryption and security in the Zoom products.

I think Zoom has realised just how badly this has affected their image and is desperately trying to recover.  However I think in terms of transparent communication, they're doing themselves justice in trying to recover.  The question remains whether it will be enough to untarnish their image.


## [psychicpaper | iOS <13.5 sandbox escape/entitlement 0day](https://siguza.github.io/psychicpaper/)

[https://siguza.github.io/psychicpaper/](https://siguza.github.io/psychicpaper/)

> Yesterday Apple released iOS 13.5 beta 3 (seemingly renaming iOS 13.4.5 to 13.5 there), and that killed one of my bugs. It wasn’t just any bug though, it was the first 0day I had ever found. And it was probably also the best one. Not necessarily for how much it gives you, but certainly for how much I’ve used it for, and also for how ridiculously simple it is. So simple, in fact, that the PoC I tweeted out looks like an absolute joke. But it’s 100% real.
> 
> I dubbed it “psychic paper” because, just like the item by that name that Doctor Who likes to carry, it allows you get past security checks and make others believe you have a wide range of credentials that you shouldn’t have.
> 
> In contrast to virtually any other bug and any other exploit I’ve had to do with, this one should be understandable without any background knowledge in iOS and/or exploitation. In that spirit, I’ll also try and write this post in a manner that assumes no iOS- or exploitation-specific knowledge. I do expect you however to loosely know what XML, public key encryption and hashes are, and understanding C code is certainly a big advantage.


This is a beautiful teardown of a bug and a good insight in how to find interesting issues in systems.  Pretty much any system that has multiple parsers for the same data, and uses them in different places is vulnerable to this sort of bug.

The key thing here is this statement:
> Because it’s very hard to parse XML correctly, valid XML makes all parsers return the same data, but slightly invalid XML makes them return just slightly not the same data. :D. In other words, any parser difference can be exploited to make different parsers see different things. This is the very heart of this bug, making it not just a logic flaw, but a system-spanning design flaw.

The use of the two parsers means that it's possible to sneak entitlements past the enforcing function, giving your application far more power over someone's device than should be easily possible.

Exploiting this bug would require you attempting to provision a new application onto the device, which probably requires physical access.  I don't think this is a "throw away your iOS device" vulnerability yet


## [Ransomware Attack Takes Down Toll Group Systems, Again | Threatpost](https://threatpost.com/ransomware-attack-toll-group-systems-again/155505/)

[https://threatpost.com/ransomware-attack-toll-group-systems-again/155505/](https://threatpost.com/ransomware-attack-toll-group-systems-again/155505/)

> Australian transportation and logistics giant Toll Group has been hit by a ransomware attack – for the second time in three months. The company said a relatively new form of ransomware known as Nefilim had targeted its systems.
> 
> [...]
> 
> “The Nefilim operators have also adopted the ‘name and shame’ tactic popularized by other ransomware groups such as Maze over the past few months,” Charles Ragland, security engineer at Digital Shadows told Threatpost. “By threatening to release data, cybercriminals can attempt to apply increased pressure on an organization, coercing them to pay ransom demands. This effectively constitutes a hybrid threat of both a ransomware attack and a data breach and is likely to continue being a popular tactic over the next few months.”


Caught twice in 3 months does not suggest strong cyber security controls.  This looks like it spread through RDP according to the reports, and there have been quite a few RDP patches that should have been applied in the last few years.

What's more worrying is this trend of ransomware groups to move towards 'name and shame' tactics.  Ransomware infections rarely seems to have a significant stock price hit for companies, instead many keep on going keeping it quiet.  The name and shame tactic, especially if accompanied by the release of sensitive data could result in regulatory fines as well as embaressment and the potential effect on share prices.


## [Mining for malicious Ruby gems](https://blog.reversinglabs.com/blog/mining-for-malicious-ruby-gems)

[https://blog.reversinglabs.com/blog/mining-for-malicious-ruby-gems](https://blog.reversinglabs.com/blog/mining-for-malicious-ruby-gems)

> Typosquatting is particularly interesting. Using this type of attack, the threat actors intentionally name malicious packages to resemble the popular ones as closely as possible (e.g. rspec-mokcs instead of rspec-mocks), in hopes that an unsuspecting user will mistype the name and unintentionally install the malicious package instead.
> 
> [...]
> 
> One typosquatted gem, “atlas-client”, stands out from the rest because of its download count. It seems that the threat actor probably succeeded in their intent to deceive unsuspecting users. As illustrated in the Figures 3 and 4, this malicious gem had 2,100 downloads, close to 30% of the total downloads that the legitimate gem “atlas_client” had at the time of reporting to the RubyGems security team.


This is a good report and a reminder that there are all kinds of attacks possible in your dependency systems.

I'm interested by the choice here to use rspec-mokcs as an example, instead of the more subtle rspec_mocks as a typo.  The latter is far less likely to be spotted and makes clear the danger far more than the idea that the dependency might be misspelled in the Gemfile.


## [Double harm to voters: data-driven micro-targeting and democratic public discourse | Internet Policy Review](https://policyreview.info/articles/analysis/double-harm-voters-data-driven-micro-targeting-and-democratic-public-discourse)

[https://policyreview.info/articles/analysis/double-harm-voters-data-driven-micro-targeting-and-democratic-public-discourse](https://policyreview.info/articles/analysis/double-harm-voters-data-driven-micro-targeting-and-democratic-public-discourse)

> My argument is that political micro-targeting causes double harm to voters: it may violate the rights of those who are targeted, but even more importantly, it may violate the right to information of those who are not targeted and therefore not aware of the political message that their fellow citizens are exposed to. Neither do they have the meta-information that their fellow citizens access, which is the case when, for example, a reader reads a headline but chooses not to read further. In this latter case, the citizen is aware about the information being ‘out there’ and accessible, and has the epistemological knowledge that this piece of information is also part of the public discourse. She has the possibility to read it later, or to ask her friends about the content of the article. She can even listen to discussions among her fellow citizens about the information. But if she is deprived of all these activities as a result of not being targeted with a targeted ad, she suffers harm. "The reason this is so attractive for political people is that they can put walls around it so that only the target audience sees the message. That is really powerful and that is really dangerous." (Howard, 2006, p. 136).


This argument about political micro-targeting also applies to effective disinformation campaigns.  Where these are micro-targeted to people, it drastically increases the information asymmetry within the populace.  Where someone may not trust an individual news source, they tend to trust their friends when they say they saw something "online", and this means that disinformation can be spread by blind cutouts, who act purely to filter the information out.  

That further point though is interesting, it's not just the awareness of the information that matters.  When you aren't even aware of the existence of the information, it's super hard to counter it in any reasonable form.  People fighting disinformation need to know what is being seeded in the population in order to effectively fight it, and the microtargeting can work to evade controls and monitoring until the seeds are well and truly sown.


## [Compliance reporting and automated patch deployment with OS patch management service | Google Cloud Blog](https://cloud.google.com/blog/products/management-tools/new-os-patch-management-service-protects-your-compute-engine-vms)

[https://cloud.google.com/blog/products/management-tools/new-os-patch-management-service-protects-your-compute-engine-vms](https://cloud.google.com/blog/products/management-tools/new-os-patch-management-service-protects-your-compute-engine-vms)

> With OS patch management, you can apply OS patches across a set of VMs, receive patch compliance data across your environments, and automate installation of OS patches across VMs—all from one centralized location. The OS patch management service has two main components:
> 
> 
> Compliance reporting, which provides detailed compliance reports and insights on the patch status of your VM instances across Windows and Linux distributions. 
> 
> Patch deployment, which automates the installation of OS patches across your VM fleet, with flexible scheduling and advanced patch configuration controls. For added convenience, you can set up flexible schedules and still keep systems up-to-date by running your patch updates within designated maintenance windows.


This is nice if you are running a reasonably large fleet of VM's and you don't already have patch management running on the devices. 
Of course some people just configure windows updates or apt-nightly to automatically install patches, but in some enterprise instances, you might want to target the deployment of patches more carefully.  The Patch Management system allows you to target individual machines, or filter by VM tags and labels.


## [SaltStack exploit attacks expose underestimated threat vector: IaC tools](https://www.scmagazine.com/home/security-news/cybercrime/salt-exploit-attacks-expose-underestimated-threat-vector-infrastructure-as-code-tools/)

[https://www.scmagazine.com/home/security-news/cybercrime/salt-exploit-attacks-expose-underestimated-threat-vector-infrastructure-as-code-tools/](https://www.scmagazine.com/home/security-news/cybercrime/salt-exploit-attacks-expose-underestimated-threat-vector-infrastructure-as-code-tools/)

> The disruptive attacks highlight what some cyber experts say is an overlooked or underestimated threat vector among developers: Infrastructure-as-Code (IaC). Considered a key element of DevOps practices, IaC tools such as Salt typically allow developers to use code to automate the managing and provision of complex computer infrastructure environments, helping them avoid configuration discrepancies between machines that can hold up software deployments that might otherwise require manual intervention. But it’s these helpful capabilities that can also make the exploitation of IaC tools uniquely dangerous
> 
> [...]
> 
> Santos added that many developers “are not appreciating the importance of IaC code and are not reviewing it, testing it, etc. at the same level they would application-level code. And in so doing, they are creating or increasing a very real threat vector.”
> 
> Therefore, “It’s important to elevate the significance of any automation code, especially IaC code, within the context of the development lifecycle,” said Santos. “It is not ‘second class’ code, but rather carries the same importance and significance as any other code supporting an application. It needs to be reviewed, tested and assured in a [manner] similar to every other element of an application architecture.”


I've been calling this for some time.  The devops desire to automate everything comes with a shifting of security boundaries.  Before we had failing procedural controls to prevent your system administrator from sitting there browsing the internet from their administrative account.  Now you have to worry about all the same. vulnerabilities in your infrastructure coordination systems as you do in your end systems.


## [Why Sentinel? | Sentinel by HashiCorp](https://docs.hashicorp.com/sentinel/intro/why/)

[https://docs.hashicorp.com/sentinel/intro/why/](https://docs.hashicorp.com/sentinel/intro/why/)

> Sentinel enables guardrails to be put in place on automation while allowing the codification and automatic enforcement of business requirements in critical areas of your infrastructure.
> 
> Meanwhile, businesses have business requirements and sometimes legal requirements which must be expressed in policies. Traditionally, these policies are enforced by humans. But in a highly automated world, the automation is only as fast as its slowest component. In many cases, this is the human verification step.
> 
> As an example: before infrastructure as code and autoscaling, if an order came through for 5,000 new machines, a human would likely respond to the ticket verifying that the user really intended to order 5,000 new machines. Today, automation can almost always freely order 5,000 new compute instances without any hesitation, which can result in unintended expense or system instability.


I discovered Sentinel because they've just released [some standard policies](https://github.com/hashicorp/terraform-foundational-policies-library) for managing some common platforms with Terraform to ensure they stay compliant with CIS benchmarks.

Sadly, it's a product that requires that you use Hashicorps own cloud service for managing your infrastructure as code, but the principle of defining policy as code is a good one, and one that we should be seeing become more common over the next few years.

The ability of security teams to define their security policies in code, and ensure that development teams cannot accidentally breach those policies will be a game changer for security teams.


## [Security blueprint: PCI on GKE  |  Security Blueprints  |  Google Cloud](https://cloud.google.com/architecture/blueprints/gke-pci-dss-blueprint#project-overview)

[https://cloud.google.com/architecture/blueprints/gke-pci-dss-blueprint#project-overview](https://cloud.google.com/architecture/blueprints/gke-pci-dss-blueprint#project-overview)

> The PCI on GKE blueprint contains a set of Terraform configurations and scripts that demonstrate how to bootstrap a PCI environment in Google Cloud. The core of this blueprint is the Hipster Shop application, where users can browse items, add them to the cart, and purchase them.
> 
> This blueprint enables you to quickly and easily deploy workloads on GKE that align with the Payment Card Industry Data Security Standard (PCI DSS) in a repeatable, supported, and secure way.


More help and advice from your cloud vendor on how to apply a pattern in a defined way is a good trend we are seeing.  All of the major providers are starting to realise that where these samples exist, users use them en-masse and that if the samples are secure and appropriate, then that makes their systems better.

This is also a good example to look at to see just what PCI compliant cloud infrastructure looks like.  The use of two separate kubernetes clusters, one as in-scope and one as out-of-scope for separating applications and systems that are within the PCI scope is something that is probably the only way to guarantee good separation, but also only reasonable to do if you are a large organisations with significant resources or if you can use a cloud provider hosted kubernetes service.  


