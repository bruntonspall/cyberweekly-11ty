---
title: "117 - What is the inside threat?"
date: 2020-09-06
description: "Who can you trust, or sometimes what can you trust?"
permalink: /what-is-the-inside-threat/
---

Who can you trust, or sometimes what can you trust?

When we think of insiders, a lot of training materials tends to overly focus on the big newsworth espionage cases.  These make headlines because the accusations of treason, of betraying your country and the damage caused is so significant that it washes out almost everything else.  But as I've referenced before, [a 2013 study of insider cases](https://www.cpni.gov.uk/system/files/documents/63/29/insider-data-collection-study-report-of-main-findings.pdf) showed that 76% were self initiated, and 47% were done for money.

But moles and humans aren't the only insider.  Anything and anyone that we trust has the possibility of being an insider.  The attacks below on AWS and GCE are both a form of "Confused Deputy" problem, which is to say, an internal tool that is allowed to conduct a privileged action doing so for the wrong user or program.  This form of attack is an insider attack on your system or network, because it looks like someone inside your network using their credentials correctly, but they've been tricked by another agent or actor.

Dealing with insiders is incredibly difficult, both the human version and the confused deputy problem.  Generally the argument is that compartmentalisation, minimal access, and need to know models work to make it much harder for an insider to act.  Anything that means that the insider has only very limited access to the information and systems that they need to use means that they cannot abuse their power as easily.  It's far easier to detect someone acting outside their role as anomalous behaviour, and to report on it.

But equally, that makes our systems less flexible, less agile and less efficient.  If some people don't know bits of information, they may not be able to do their jobs as effectively, and of course, you cannot have a holistic view of the system when information is too tightly compartmentalised.

We need to recognise that insider threats are a risk like many others, one that we should aim to quantify, and determine if the cost of reducing that risk outweighs the impact of the risk being realised.  Most insider threats are extremely rare, and despite having the greatest, most terrifying potential for damage, the damage when it happens is often much less than the potential damage.

## [Become an Azure Security Center Ninja](https://techcommunity.microsoft.com/t5/azure-security-center/become-an-azure-security-center-ninja/ba-p/1608761)

[https://techcommunity.microsoft.com/t5/azure-security-center/become-an-azure-security-center-ninja/ba-p/1608761](https://techcommunity.microsoft.com/t5/azure-security-center/become-an-azure-security-center-ninja/ba-p/1608761)

> Become an Azure Security Center Ninja
> 
> This blog post has a curation of many Azure Security Center (ASC) resources, organized in a format that can help you to go from absolutely no knowledge in ASC, to design and implement different scenarios. You can use this blog post as a training roadmap to learn more about Azure Security Center.
> 
> 
> To become an ASC Ninja, you will need to complete each module. The content of each module will vary, refer to the legend to understand the type of content before clicking in the topic’s hyperlink.


Stupid nomenclature aside (really... be a Security Center Ninja?), this is a useful collection of Azure security documentation and guidance, and worth reading through if you aren't familiar with Azure's security features (and probably if you are, as I'm sure you'll learn something)


## [A Chrome feature is creating enormous load on global root DNS servers | Ars Technica](https://arstechnica.com/gadgets/2020/08/a-chrome-feature-is-creating-enormous-load-on-global-root-dns-servers/)

[https://arstechnica.com/gadgets/2020/08/a-chrome-feature-is-creating-enormous-load-on-global-root-dns-servers/](https://arstechnica.com/gadgets/2020/08/a-chrome-feature-is-creating-enormous-load-on-global-root-dns-servers/)

> Chromium's authors didn't want to have to see "did you mean" infobars on every single-word search in those common environments, so they implemented a test: on startup or change of network, Chromium issues DNS lookups for three randomly generated seven-to-15-character top-level "domains." If any two of those requests come back with the same IP address, Chromium assumes the local network is hijacking the NXDOMAIN errors it should be receiving—so it just treats all single-word entries as search attempts until further notice.
> 
> Unfortunately, on networks that aren't hijacking DNS query results, those three lookups tend to propagate all the way up to the root nameservers: the local server doesn't know how to resolve qwajuixk, so it bounces that query up to its forwarder, which returns the favor, until eventually a.root-servers.net or one of its siblings has to say "Sorry, that's not a domain."
> 
> Since there are about 1.67*10^21 possible seven-to-15-character fake domain names, for the most part every one of these probes issued on an honest network bothers a root server eventually. This adds up to a whopping half the total load on the root DNS servers, if we go by the statistics from Verisign's portion of the root-servers.net clusters.
> 
> 


Oooh, law of unintended consequences.  

This is hard problem to solve, you want to know if your ISP's DNS is hijacking your results, as that's happened a lot before, but not if doing so adds excessive load to the root servers.  For now, it looks like they'll disable this feature and rethink how to detect this sort of interception.


## [Amazon takes down a five-star fraud in the UK - The Verge](https://www.theverge.com/2020/9/4/21423429/amazon-top-reviewers-uk-fraud?utm_campaign=theverge&utm_content=entry&utm_medium=social&utm_source=twitter)

[https://www.theverge.com/2020/9/4/21423429/amazon-top-reviewers-uk-fraud?utm_campaign=theverge&utm_content=entry&utm_medium=social&utm_source=twitter](https://www.theverge.com/2020/9/4/21423429/amazon-top-reviewers-uk-fraud?utm_campaign=theverge&utm_content=entry&utm_medium=social&utm_source=twitter)

> Justin Fryer, the number one Amazon reviewer in the UK, left a five-star rating once every four hours on average in August, according to the FT’s analysis. Many of these reviews were for products from random Chinese companies. Fryer then seems to have resold the products on eBay.
> 
> A FIVE-STAR RATING ONCE EVERY FOUR HOURS ON AVERAGE
> Scams like these typically start on social networks and messaging apps such as Telegram, where companies can meet potential reviewers. Once the connection is made, the reviewer chooses a free product, then waits a few days to write a five-star review. After the review is posted, they get a full refund, and, at times, an extra payment.


Assessing the legitimacy of reviews is really hard, because you really can't easily tell whether someone has had a good or bad experience of a product in reality, or whether they are lying.

Professional reviewers of course get sent complementary products to review, and then write about them.  They may not get to keep the products and often disclose which products are provided or not.  Of course, the difference between reading a professional review such as America's Test Kitchen or Which is vastly different to the users experience of reading an Amazon "Customer Review".


## [Palantir CEO rips Silicon Valley in letter to investors](https://www.cnbc.com/2020/08/25/palantir-ceo-rips-silicon-valley-in-letter-to-investors.html)

[https://www.cnbc.com/2020/08/25/palantir-ceo-rips-silicon-valley-in-letter-to-investors.html](https://www.cnbc.com/2020/08/25/palantir-ceo-rips-silicon-valley-in-letter-to-investors.html)

> “The engineering elite of Silicon Valley may know more than most about building software,” Karp wrote. “But they do not know more about how society should be organized or what justice requires. Our company was founded in Silicon Valley. But we seem to share fewer and fewer of the technology sector’s values and commitments.” Last week, the company announced plans to move its headquarters from Palo Alto, in the heart of Silicon Valley, to Colorado.
> 
> Karp said Palantir has “repeatedly turned down opportunities to sell, collect, or mine data,” contrasting it with consumer companies “built on advertising dollars.”
> 
> “Software projects with our nation’s defense and intelligence agencies, whose missions are to keep us safe, have become controversial, while companies built on advertising dollars are commonplace. For many consumer internet companies, our thoughts and inclinations, behaviors and browsing habits, are the product for sale. The slogans and marketing of many of the Valley’s largest technology firms attempt to obscure this simple fact.” 


This is somewhat ironic.  Palantir has a very poor name amongst the silicon valley elite techs because of their support of the intelligence community and percieved over reach in terms of breaching peoples privacy.

There's an interesting debate in here somewhere.  Law enforcement and intelligence systems actively attempt to breach an individuals privacy, as well as systemic privacy of groups in order to catch bad guys.  

Tech companies often collect and monetise advertising data, which can equally feel privacy intrusive, but because the tech systems aren't designed to allow direct inspection of an individual, is more a broad systemic breach of privacy.

Whether one is good and the other bad probably depends a lot on your worldview and what you spend your time doing more than anything else.  People mired in catching bad guys or seeing the worst of the internet don't see the problems of overreach, and people who use the internet everyday can get ad-blindness meaning they don't see the privacy impact of that either.


## [Inside a CODE RED: Network Edition - Signal v. Noise](https://m.signalvnoise.com/inside-a-code-red-network-edition/)

[https://m.signalvnoise.com/inside-a-code-red-network-edition/](https://m.signalvnoise.com/inside-a-code-red-network-edition/)

> We recognized the problem immediately and sprang into action. We restarted the Redis replica and the Cable service. It looked like things were returning to normal 5 minutes after the network flap. Unfortunately, our quick response during peak load on a Tuesday had unintended consequences. We saw a “thundering herd” of chat reconnects hit our Ashburn DC and the load balancers couldn’t handle the volume. Our primary load balancer locked up under the load and the secondary tried to take over. The failover didn’t register with the downstream hosts in the DC and we were down in our primary DC. This meant BC3, BC2, basecamp.com, Launchpad and  supporting services were all inaccessible. 


This is a lovely writeup of a few recent incidents at Basecamp, but what stuck out to me was this description.  In essence "We'd encountered this problem before, applied the fix, but this time something else went wrong".  Cascading failures are at the root cause of most outages, because we can tend to reason about single failures and how to deal with them, but the knock-on impacts on other bits of the system are so hard to reason about that we often see behaviour that we didn't expect.  This inability to reason about, what feel like quite simple and predictable systems is a major failing in most computing environments.


## [Security Budgets - Supply and Demand Thinking](https://www.philvenables.com/post/security-budgets-supply-and-demand-thinking)

[https://www.philvenables.com/post/security-budgets-supply-and-demand-thinking](https://www.philvenables.com/post/security-budgets-supply-and-demand-thinking)

> You have a set of demands on your team. This might not just be your team, depending on how you are organized it could be the whole enterprise’s spend on security from the CISO function, to embedded Business Information Security Officer roles through to specific engineers working on security in product teams [incidentally, this is why you should never believe the nonsense of budget benchmarks unless you are working on a common definition of security expenditure - which nobody ever does]. These demands could be to work on reviewing and mitigating risks on new business products, new projects, handling vulnerabilities, investigating potential incidents, dealing with acquisitions/divestments, onboarding new vendors or new technologies and so on. 
> 
> Then, you have a supply of resources and capabilities to meet those demands, which could be people, services, products or other expenditure. The goal, naturally, is to balance supply and demand. The problem is we live in a world in most organizations where the demand is outpacing supply, because of business growth, IT changes, supply chain complexities, new threats and vulnerabilities and myriad other drivers. Even if we could continuously increase budget without limit it is not always clear we even have the ability to then turn that budget into the actual supply (of people, services and products) needed to meet the demand. Instead, we have to look at all sides of this problem


This is a nice model for thinking about the issues of managing a good security team.  Reducing demand by increasing risk appetite is a lovely way of describing how certain systemic changes can change the work your team does.  

I also like the formulation of the idea that certain platform wide changes can reduce demand on your security team.  Those baseline security reviews, while a pain, can significantly reduce the demand on the security team by switching work from an in-depth analysis to a simple set of questions (Did you use our platform? Did you configure it as per our guide?  Good, on you go).


## [Why You Should Enable GKE Shielded Nodes Today - Darkbit](https://darkbit.io/blog/gke-shielded-nodes)

[https://darkbit.io/blog/gke-shielded-nodes](https://darkbit.io/blog/gke-shielded-nodes)

> If one could generate valid kubelet keypairs for all nodes in the cluster, they could iterate through each and grab all the cluster secrets attached to pods running on all the nodes. In practical terms, that’s the close to the same access provided by kubectl get secrets --all-namespaces. In nearly all clusters, at least one Kubernetes Service Account is bound to a privileged RBAC ClusterRole like cluster-admin.
> 
> In default GKE clusters, this means that any Pod has a direct path to escalate to cluster-admin without requiring authentication. As cluster-admin, the user controls all data and applications running on the GKE workers as well as the union of all permissions associated with credentials attached to Pods running in the cluster. At best, it’s free compute. At worst, it’s a launch point for full GCP account takeover.


So the same attack that works on AWS, works (with a little modification) on Google Compute Engine's Kubernetes installation as well.  Google has two remediations in place, a temporary one that can prevent the outbound networking, and a more complete one called Shielded Nodes which adds some cryptographic validation of the node and the VM it's running in, but also strips out all of the accesses to the bootstrap credentials as a handy side effect.


## [Privilege Escalation in AWS Elastic Kubernetes Service (EKS) by compromising the instance role of worker nodes - Christophe Tafani-Dereeper](https://blog.christophetd.fr/privilege-escalation-in-aws-elastic-kubernetes-service-eks-by-compromising-the-instance-role-of-worker-nodes/)

[https://blog.christophetd.fr/privilege-escalation-in-aws-elastic-kubernetes-service-eks-by-compromising-the-instance-role-of-worker-nodes/](https://blog.christophetd.fr/privilege-escalation-in-aws-elastic-kubernetes-service-eks-by-compromising-the-instance-role-of-worker-nodes/)

> It all starts with a compromised Pod…
> Let’s assume an attacker compromised a pod in the cluster, for instance by exploiting a vulnerability in the web application it was running. We simulate this scenario by running a pod and attaching to a shell inside it.
> 
> `$ kubectl run --rm -i --tty mypod --image=alpine --restart=Never -- sh
> (pod)$ hostname
> mypod`
> 
> Good! As an attacker, we’re now interested to enumerate resources in the cluster and in the associated AWS account.
> 
> [...]
> 
> As a reminder, the Instance Metadata service is an AWS API listening on a link-local IP address, 169.254.169.254. It is only accessible from EC2 instances and allows to retrieve various information about them.
> 
> It is particularly useful when you need your instances to access AWS resources. Instead of hard-coding credentials, you first assign an IAM role to your instance. From the instance, you can then retrieve temporary credentials for the role. This is 100 % transparent if you use the AWS CLI.


This is a lovely demonstration of the sort of attack that can happen when your abstractions are leaky.

In this case, the mental model of the developers is that a pod is a self-contained computer.  But in reality, it's a VM within your AWS account, and that means that it can potentially have access to things like the AWS Metadata Service.

The ability to get local temporary AWS credentials from the metadata service, that act as the machine, not the pod, means that you can get credentials to look at network interfaces, explore the network, move your pod onto another network, and generally muck about.  

Your pods shouldn't be able to call the metadata service, but because of the way that Kubernetes networking works, it's actually surprisingly hard to block.  There's a remediation in the post if you think this will affect you.


## [Former Uber security chief charged with paying hush money to cover up 2016 hack - The Verge](https://www.theverge.com/2020/8/20/21377849/uber-hack-2016-data-breach-former-security-chief-hush-money-doj-ftc)

[https://www.theverge.com/2020/8/20/21377849/uber-hack-2016-data-breach-former-security-chief-hush-money-doj-ftc](https://www.theverge.com/2020/8/20/21377849/uber-hack-2016-data-breach-former-security-chief-hush-money-doj-ftc)

> Uber’s former security chief has been charged with obstruction of justice for trying to hide a data breach from the Federal Trade Commission and Uber management, according to a statement from the Department of Justice.
> 
> Joseph Sullivan, who was Uber’s chief security officer from April 2015 to November 2017, allegedly concealed the hack that occurred in October 2016, which exposed confidential data of 57 million drivers and customers, including drivers’ license information. Uber paid the hackers $100,000 in bitcoin to delete the data, according to the Justice Department. (Sullivan was later fired.)
> 
> [...]
> 
> Williams says if not for Sullivan’s efforts and the efforts of Uber’s security team, “it’s likely that the individuals responsible for this incident never would have been identified at all.” He said Sullivan and his team “collaborated closely with legal, communications and other relevant teams at Uber, in accordance with the company’s written policies. Those policies made clear that Uber’s legal department — and not Mr. Sullivan or his group — was responsible for deciding whether, and to whom, the matter should be disclosed.”


Who is actually responsible in this case will be the center of this court case.  The state argues that Sullivan, as the CISO, was responsible for the handling of the breach, and the decision to attempt to pay the hackers (all of which is almost certainly true).

However, the question will remain whether it was Sullivan who got to decide whether or not to tell the authorities.  I'm sure that he will have had an opinion, potentially forcefully expressed, but his defence will be that the legal department were the ones who had to decide.

How your management team deals with such issues is important, because during the middle of it all, emotions will be high and strong personalities will rule.  But knowing what you are legally required to do (not to mention the ethical questions about telling people whose data you are trusted to hold that it has been exposed) is incredibly important.


## [Investigating the U.S. Special Forces Vet Charged With Spying for Russia - Strike Source](https://strikesource.com/2020/08/22/investigating-the-u-s-special-forces-vet-charged-with-spying-for-russia/)

[https://strikesource.com/2020/08/22/investigating-the-u-s-special-forces-vet-charged-with-spying-for-russia/](https://strikesource.com/2020/08/22/investigating-the-u-s-special-forces-vet-charged-with-spying-for-russia/)

> The alleged spy living in Gainesville, Virginia known to his handlers as Iskar Leskinov, but to everyone else as Peter Debbins, was arrested on August 21, 2020. Debbins, who held Top Secret security clearance and had access to Sensitive Compartmented Information (SCI-often referred to as above Top Secret), was a former member of 10th Special Forces Group. He is charged with “conspiring to provide United States national defense information to agents of a foreign government.” According to a seventeen-page indictment, Debbins provided sensitive information about his special forces unit and classified operations to the G.R.U., Russia’s primary military intelligence agency. If Debbins is convicted he faces a maximum sentence of Life in Prison.


This feels like it's going to be a big deal.  Recruited back in 1995, he was encouraged to move his career towards special forces and access to highly classified information.  The indictment only really covers the release of some operational information relating to his special forces work, but if the accusation rings true, then he could have been providing serious amounts of intelligence with the GRU during the later part of his career as well.

The fact that there's no indictment for that doesn't mean that it didn't happen, or that there's no record of it.  It just means that the prosecutors are absolutely sure that the special forces information was disclosed and that's sufficient to get the charges pressed.


