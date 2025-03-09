---
title: "126 - More secure in the public cloud"
date: 2020-11-22
description: "You know, I never really thought the MOD would be the organisation to be the first HMG organisation to say it, but yes, they have.  You can be more secure in the public cloud than you might be in your on-premise data center."
permalink: /more-secure-in-the-public-cloud/
---

You know, I never really thought the MOD would be the organisation to be the first HMG organisation to say it, but yes, they have.  You can be more secure in the public cloud than you might be in your on-premise data center.

For all the reasons that I've been articulating for years, that cloud vendors patch their underlying systems far more effectively than you do, that they protect their physical estates better than you do, and that they provide security features out of the box that you don't do.

Of course the cloud isn't necessarily more secure, just differently secure.  If we think about the threat model to our systems, we think about the sorts of attacks that we undergo.  We have VPN endpoints that need patching, web systems that need patching, and all kinds of controls to try to protect the sanctity of our system.  But when we move to the cloud, we are not only putting our infrastructure there, we are putting our identity systems there.  We also need to correctly configure our cloud system, using the tools that our provider gives us.  These tools, these identities and these configurations become new avenues for attack that didn't exist before.  So we have to ensure that we are better at thinking about how to secure those, and how we support our teams to use them well.

## [Passwords are a pain - Home Office Digital, Data and Technology](https://hodigital.blog.gov.uk/2020/10/20/passwords-are-a-pain-in-the/)

[https://hodigital.blog.gov.uk/2020/10/20/passwords-are-a-pain-in-the/](https://hodigital.blog.gov.uk/2020/10/20/passwords-are-a-pain-in-the/)

> That’s when I posted our problem to Chris Hill-Scott, Designer, at GDS who wrote the ‘Identifying users’ guidance.
> 
> Chris explained why users were seeing a message telling them their magic link had expired even when it was the first time they had clicked on it:
> 
> Lots of things click links before you can. Email virus scanners might click links to check their content for malware. Instant messaging apps might click links to render previews.


This is a gotcha for people.  Lots of things can click links on your behalf.  The solution suggested here is generally the right one, an initial click of a link shouldn't destroy the usability of the link.  So either require a second action, preferably a POST request (security systems tend to know that POST requests are not idempotent and don't click them), or ensure that the link can be followed multiple times within a short timeframe instead.


## [Ok Google: please publish your DKIM secret keys – A Few Thoughts on Cryptographic Engineering](https://blog.cryptographyengineering.com/2020/11/16/ok-google-please-publish-your-dkim-secret-keys/)

[https://blog.cryptographyengineering.com/2020/11/16/ok-google-please-publish-your-dkim-secret-keys/](https://blog.cryptographyengineering.com/2020/11/16/ok-google-please-publish-your-dkim-secret-keys/)

> As an anti-spam measure there’s nothing really wrong with DKIM, ARC and DMARC. The problem is that DKIM signing has an unexpected side effect that goes beyond its initial spam-filtering purpose. Put simply:
> 
> DKIM provides a life-long guarantee of email authenticity that anyone can use to cryptographically verify the authenticity of stolen emails, even years after they were sent.
> 
> This new non-repudiation feature was not part of DKIM’s design goals. The designers didn’t intend it, nobody discussed whether it was a good idea, and it seems to have largely taken them by surprise. Worse, this surprise feature has some serious implications: it makes us all more vulnerable to extortion and blackmail.


This is an interesting piece, one that I'm not sure I agree with.  

I think that long term integrity of emails, especially officials, politicians and senior public figures is a good thing for future historians, and for increasing integrity in public office.

Where the argument is that this can be misused by the press and others to blackmail officials over emails they have sent, I would argue that the argument should either be one that those people should not send such emails, or in some cases, that we the public should allow our leaders to be human and send rude, ungratious and off the cuff emails, and care less.


## [Learnings From Two Years of Kubernetes in Production | by Vaidik Kapoor | Nov, 2020 | Lambda](https://lambda.grofers.com/learnings-from-two-years-of-kubernetes-in-production-b0ec21aa2814)

[https://lambda.grofers.com/learnings-from-two-years-of-kubernetes-in-production-b0ec21aa2814](https://lambda.grofers.com/learnings-from-two-years-of-kubernetes-in-production-b0ec21aa2814)

> A lot of people get confused with Kubernetes as a PaaS solution — it’s not a PaaS solution. It is a platform to build PaaS solutions. OpenShift is one such example.
> Out-of-the-box Kubernetes is never enough, for almost anyone. It’s a great playground to learn and explore. But you are most likely going to need more infrastructural components on top and tie them well together as a solution for applications to make it more meaningful for your developers. Often this bundle of Kubernetes with additional infrastructural components and policies is called Internal Kubernetes Platform. This is as an extremely useful paradigm and there are several ways to extend Kubernetes.
> Metrics, logs, service discovery, distributed tracing, configuration and secret management, CI/CD, local development experience, auto-scaling on custom metrics are all things to take care of and make a decision. 


This is an interesting look back on 2 years of migrating to Kubernetes.  tl;dr; out of the box it doesn't actually manage many of the things that you need it to manage, so you'll need to ensure that the supporting infrastructure is there as well.


## [UK's National Cyber Force comes out of the shadows - BBC News](https://www.bbc.co.uk/news/technology-55007946)

[https://www.bbc.co.uk/news/technology-55007946](https://www.bbc.co.uk/news/technology-55007946)

> The debate over when and how to go on the offensive with cyber-weapons has often lacked nuance. Those involved hope the public announcement will lead to a more informed debate.
> 
> The creation of the National Cyber Security Centre (NCSC) in 2016 as a public, defensive arm of GCHQ did help increase public engagement and understanding.
> 
> Its former head Ciaran Martin recently revealed that when he started, understanding was so low that a senior figure in government asked him where the "red button" was to launch attacks.
> 
> That button may not literally exist, but it is now public that the National Cyber Force is the place where it would be.


The irony that an article talking about how the debate would be more informed also still continues to talk about a big red button to launch cyber attacks is not lost on me.

A better informed public and international debate about the role of cyber offense, cyber defence and internet norms can only be a good thing.


## [‘Absolute right guy for the job’: New cyber chief takes reins amid the chaos - POLITICO](https://www.politico.com/news/2020/11/18/cisa-krebs-brandon-wales-437861)

[https://www.politico.com/news/2020/11/18/cisa-krebs-brandon-wales-437861](https://www.politico.com/news/2020/11/18/cisa-krebs-brandon-wales-437861)

> Wales, CISA’s top career staffer and officially its executive director, became its acting director on Wednesday after Trump fired Krebs for debunking the baseless election-related conspiracy theories that the president and his allies are promoting. At least for now, that debunking continues — the agency “Rumor Control” website that so angered the White House was still operating Wednesday afternoon, although Wales has not continued Krebs’ practice of indirectly trolling the president on Twitter.
> 
> The new chief is a veteran of roles both prominent and obscure at CISA’s parent, the Department of Homeland Security, which he joined just a few years after its post-Sept. 11 creation. And he’s the ideal person to take over at such a moment of chaos, seven current and former colleagues say. They describe him as brilliant, calm under pressure and better versed in DHS’s cyber mission than virtually anyone else.


The firing of Chris Krebs isn't a great surprise, someone who actively continuously published information that was contrary to the presidents chosen narrative was unlikely to last much longer in the role.

The canny positioning of a career public servant who wasn't a political appointee is definitely a good move and it'll be interesting to watch the CISO rumour control website over the coming month to see what happens to it.


## [What Happened to the Deepfake Threat to the Election? | WIRED](https://www.wired.com/story/what-happened-deepfake-threat-election/)

[https://www.wired.com/story/what-happened-deepfake-threat-election/](https://www.wired.com/story/what-happened-deepfake-threat-election/)

> Does the deepfake no-show in 2020 undermine warnings about their danger? Paul Barrett, author of an NYU report last year that listed deepfakes first on a list of disinformation predictions for 2020, says the warnings may have worked, convincing would-be deepfake producers that their clips would be quickly unmasked. But he warns that the threat remains. “Deepfakes are an obvious danger, and we could see more of them in the future,” says Barrett, deputy director of NYU’s Center for Business and Human Rights.
> 
> A safe 2024 election prediction to add to the already lustily growing list: Warnings about deepfakes will surge again, and video synthesis technology will have gotten much better. Hopefully deepfake detection technology will have also done so.


Interesting view here.  I wasn't convinced that election misinformation would be the star of DeepFake technology.  It's too early in the technologies lifecycle, and there are easier ways to achieve the same aims at the moment.

Give it another 4 or maybe 8 years however and I think we'll have more of an issue, but DeepFakes will be revolutionising other areas (probably porn first, entertainment second) and feel normal before it gets used directly in electioneering.


## [Information Leakage in AWS Resource-Based Policy APIs](https://unit42.paloaltonetworks.com/aws-resource-based-policy-apis/)

[https://unit42.paloaltonetworks.com/aws-resource-based-policy-apis/](https://unit42.paloaltonetworks.com/aws-resource-based-policy-apis/)

> The root cause of the issue is that the AWS backend proactively validates all the resource-based policies attached to resources such as Amazon Simple Storage Service (S3) buckets and customer-managed keys. Resource-based policies usually include a Principal field that specifies the identities (users or roles) allowed to access the resource. If the policy contains a nonexistent identity, the API call that creates or updates the policy will fail with an error message. This convenient feature, however, can be abused to check whether an identity exists in an AWS account. Adversaries can repeatedly invoke these APIs with different principals to enumerate the users and roles in a targeted account. Furthermore, the targeted account can’t observe the enumeration because the API logs and error messages only appear in the attacker’s account where the resource policies are manipulated. The “stealthy” property of the technique makes detection and prevention difficult. Attackers can have unrestricted time to perform reconnaissance on random or targeted AWS accounts without worrying about being noticed.


This is a nasty bug, and it's impressive work finding it.

If you have an AWS account, A, and you want to allow users from another AWS account, B, to use it, you can create a policy that allows their account names to access your resources.   Something like `arn:aws:iam:<accountb>:role/admin`.  AWS validates that this is a valid role before applying your policy.

But because any account and grant access to any other account, you can use it to enumerate the usernames and roles of a target account, and most importantly, they cannot see, notice or do anything about it.

Account enumeration is the most impactful of vulnerabilities, but if you are looking for old, forgotten accounts, or combined with other attacks, such as phishing it can shortcut the process for attackers considerably.


## [Researcher Discloses Critical RCE Flaws In Cisco Security Manager](https://thehackernews.com/2020/11/researcher-discloses-critical-rce-flaws.html)

[https://thehackernews.com/2020/11/researcher-discloses-critical-rce-flaws.html](https://thehackernews.com/2020/11/researcher-discloses-critical-rce-flaws.html)

> Cisco has published multiple security advisories concerning critical flaws in Cisco Security Manager (CSM) a week after the networking equipment maker quietly released patches with version 4.22 of the platform.
> 
> The development comes after Code White researcher Florian Hauser (frycos) yesterday publicly disclosed proof-of-concept (PoC) code for as many as 12 security vulnerabilities affecting the web interface of CSM that makes it possible for an unauthenticated attacker to achieve remote code execution (RCE) attacks.
> 
> The flaws were responsibly reported to Cisco's Product Security Incident Response Team (PSIRT) three months ago, on July 13.
> 
> "Since Cisco PSIRT became unresponsive and the published release 4.22 still doesn't mention any of the vulnerabilities," claimed frycos in a tweet, citing the reasons for going public with the PoCs yesterday.


Ouch.  If you are using Cisco Security Manager, for say AnyConnect VPN, then you should make sure that you have patched. Some of these are really quite serious


## [More secure in the public cloud - Defence Digital](https://defencedigital.blog.gov.uk/2020/11/20/more-secure-in-the-public-cloud/)

[https://defencedigital.blog.gov.uk/2020/11/20/more-secure-in-the-public-cloud/](https://defencedigital.blog.gov.uk/2020/11/20/more-secure-in-the-public-cloud/)

> However, some people find it counter-intuitive that cloud services shared with other organisations or individuals can be considered to be as secure as those in data centres on military bases. A few years ago I’d have argued that the cloud can be ‘just as secure’ as our on-premises data centres for hosting OFFICIAL workloads, but today I’d say that in most circumstances we can do a better job of security in the cloud than we can do on-premises.


From my perspective, this is a tour-de-force brilliant proclamation of why the cloud is more secure.  Richard manages to put into far better words than I ever can just why cloud services are more secure than traditional on-premise workloads.

What we need next is some really good descriptions of the sorts of new controls that you need in this new world, that you didn't in the old one.  Audit tools that verify that you haven't misconfigured the thing, detection and response tooling, and of course, strong identity and authentication tools to ensure that administrators are not compromised.


