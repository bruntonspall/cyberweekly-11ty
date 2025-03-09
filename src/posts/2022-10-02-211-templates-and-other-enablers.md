---
title: "211 - Templates and other enablers"
date: 2022-10-02
description: "What does it mean to secure the appsec pipeline?"
permalink: /templates-and-other-enablers/
---

What does it mean to secure the appsec pipeline?

In organisations with a reasonably large development team, or teams, there might be multiple product teams, and several development teams.  

If the ratios follow the normal curve, then you probably have about 1 security engineer for every 10 devops people for every 100 developers.

If you need those 100 developers to stop and talk to your security engineering team everytime they want to create a new repository, bring in a new dependency, or deploy a new application, your security team will be a bottleneck that will stop anyone doing anything.

Githubs recommendation, from talking to thousands of enterprise customers, is to use templates or other defaults.  These give developers a set of scanning tools by default that should work out of the box.   They may not catch everything, and developers in their haste to get the CI system working may well disable the defaults or ignore errors, but the defaults mean that there's no friction for the teams as they seek to deliver new products or code.

One of the things you need to think about these defaults is that they need to do the minimum needed with the least amount of difficulty.  It's better in some cases to have a test which, if it fails, tells the developer to contact security.  This form of creating engagement means that people coming to you will only come to you if they are doing something unusual or with high security risk.  A good example of this was given to me when we wrote [Agile Application Security](https://www.amazon.co.uk/Agile-Application-Security-Laura-Bell/dp/1491938846) a few years back, at Etsy, Rich Smith's team had a test that simply checked the hash of the user authentication code against a predetermined hash.  The idea was simply to alert the security team anytime someone changed the user authentication code, so they could get a security review and the hash updated.

Pitching your defaults at the right level is hard, but you should consider strongly using the template builds, along with any template projects that are provided by DevOps or Architecture, and making sure that they all build with no errors and no concerns.   Train your developers that errors, warnings or failures in those systems are meaningful, even if that means missing some issues.  You can always conduct regular automated reviews over and above the basic templates.

## [Best practices on rolling out code scanning at enterprise scale | The GitHub Blog ](https://github.blog/2022-09-28-best-practices-on-rolling-out-code-scanning-at-enterprise-scale/)

[https://github.blog/2022-09-28-best-practices-on-rolling-out-code-scanning-at-enterprise-scale/](https://github.blog/2022-09-28-best-practices-on-rolling-out-code-scanning-at-enterprise-scale/)

> Increasingly, GitHub customers prefer to use [GitHub Actions for CI/CD](https://github.blog/tag/github-actions/) . GitHub code scanning natively integrates with GitHub Actions to make adopting security scanning tools, like CodeQL, frictionless. However, we recognize that some enterprises prefer to use other CI/CD tools, such as Jenkins or ADO. Even with third-party CI, from a “level of effort” perspective, integrating a new centralized scan job into the developers pipeline should be simple.
> 
> Most CI tools provide the ability to create modular, reusable and centrally managed templates ( [shared libraries](https://www.jenkins.io/doc/book/pipeline/shared-libraries/) on Jenkins or [Pipeline Templates](https://docs.microsoft.com/en-us/azure/devops/pipelines/process/templates?view=azure-devops) on ADO) to load external logic into an existing workflow. By leveraging this integration pattern, an application security team can externalize the core CodeQL functionality ( [create](https://codeql.github.com/docs/codeql-cli/creating-codeql-databases/) , [analyze](https://codeql.github.com/docs/codeql-cli/analyzing-databases-with-the-codeql-cli/) , [upload](https://codeql.github.com/docs/codeql-cli/manual/github-upload-results/) ) whilst enabling individual developer teams to include custom logic to support more granular configurations. Those configurations might look like: passing in application-specific build commands, running additional queries, or providing additional sources and sinks. This allows for the re-use of the required CodeQL stages, meaning every application team does not have to duplicate the same stages for every pipeline, and also enables application specific customization. 


This is a good pattern.  Setup templates for your build systems.  That means that if anyone sets up their own build, then they’ll get your appsec scanning by default.  That means they don’t need to talk to you, or wait for you to get going.  Just works by default. 


## [Software Dependency Failures: jQuery, a Canary in the Coal Mine ](https://public-exposure.inform.social/post/software-dependency/)

[https://public-exposure.inform.social/post/software-dependency/](https://public-exposure.inform.social/post/software-dependency/)

> **The State of jQuery Vulnerabilities Exemplified**
> 
> > Q: What did you find in practice?
> > A: Based on a sample of 100k hosts, my preliminary results are as follows: 
> 
> * Approximately 26% of all the publicly reachable jQuery UI web applications contain a version of jQuery which is vulnerable to CVE-2020-11022.
> * Approximately 21% of jQuery UI instances are EOL which raises my eyebrows even further. 


Probably unsurprising to many people, but it’s a good bit of analysis that shows how rarely people are in fact updating their dependencies, and also how easy it is to use Shodan or other internet scanners to find vulnerable hosts. 


## [Vulnerable GitHub Actions Workflows Part 1: Privilege Escalation Inside Your CI/CD Pipeline ](https://www.legitsecurity.com/blog/github-privilege-escalation-vulnerability)

[https://www.legitsecurity.com/blog/github-privilege-escalation-vulnerability](https://www.legitsecurity.com/blog/github-privilege-escalation-vulnerability)

> **TL;DR** 
> 
> * The Legit Security research team has uncovered a vulnerability where the attacker can exploit a vulnerable build script in GitHub Actions to modify an organization’s software code or build artifacts
> * GitHub Actions is a powerful and flexible platform that enables building complex CI/CD pipelines easily with the help of the open-source community.
> * “workflow_run” event is a unique GitHub Actions pipeline trigger that executes privileged pipelines and if not used cautiously could lead to major security issues.
> * Thousands of repositories use “workflow_run” trigger. We found various common vulnerable workflow configuration code patterns that are susceptible to a privilege escalation attack, i.e., can give attackers the ability to run highly privileged code inside the CI/CD pipeline.
> * Once a “workflow_run” privilege escalation vulnerability is exploited, an attacker could use the elevated permissions to trigger a supply chain attack by modifying repository resources (e.g. tags, artifacts, releases, etc).
> * The attacker could steal repository secrets and potentially some organization secrets, allowing lateral movement inside the organization and further increasing the blast radius of his attack. 
> 
> **What you can do to protect yourselves** 
> 
> * We’ve contributed ‘workflow_run’ issues detections to the [OSSF Scorecards Project](https://github.com/ossf/scorecard/pull/1818) . Using scorecard in your projects is recommended and now will detect unsafe usage of ‘workflow_run’.
> * Restrict the GitHub token permissions only to the required ones; this way, even if the attackers will succeed in compromising your workflow, they won’t be able to do much.
> * Use workflow input as environment variables instead of interpolation. This will prevent script injection.
> * Never check out user code, code execution might happen in many ways, some of which are very hard to detect thus avoiding checkout is highly recommended.
> * If possible, check that the triggering workflow doesn’t belong to a forked repository, and if it does require human approval as explained in this blog post: [Using Environment Protection Rules to Secure Secrets When Building External Forks with pull_request_target](https://dev.to/petrsvihlik/using-environment-protection-rules-to-secure-secrets-when-building-external-forks-with-pullrequesttarget-hci) 


If you are using workflow_run, you should probably check out these guidelines and make sure you are restricting the behaviours correctly.  This is essentially “working as intended”, but it might not be clear to DevOps or self service teams that they might be making a security impacting decision. 


## [Top Insights From Our 2022 State of Secure Identity Report ](https://auth0.com/blog/top-insights-from-our-2022-state-of-secure-identity-report/)

[https://auth0.com/blog/top-insights-from-our-2022-state-of-secure-identity-report/](https://auth0.com/blog/top-insights-from-our-2022-state-of-secure-identity-report/)

> **Credential stuffing is on a record pace** 
> 
> 2022 has already delivered the two largest such credential stuffing attacks we have ever witnessed, and across all industries, credential stuffing accounts for 34% of overall traffic/authentication events on our platform. While most industries experienced a credential stuffing rate of less than 10% of login events, in several cases — Retail/eCommerce (more than 80%), Financial Services, and Entertainment — these attacks represented the majority of login attempts. 
> 
> **Threat actors are targeting MFA** 
> 
> Because of its proven merits, more application and service providers are recommending or requiring MFA. Consequently, the first half of 2022 has seen a higher baseline of attacks against MFA than any previous year in our dataset. As attackers become more sophisticated at targeting this important defensive measure, it's critical that MFA be implemented correctly and that strong secondary factors are chosen. 
> 
> **Breached Passwords are a pervasive but poorly understood threat** 
> 
> Account takeover attacks with stolen credentials are one of the most common and costly cyber threats. Entire marketplaces exist to sell lists of user credentials leaked in third-party breaches. In fact, 58% of all Auth0 customer applications have experienced login attempts using breached/leaked credentials, illustrating the widespread nature of these attacks. What's more, most of the services that purport to protect against breached passwords use web scanners and scrapers that rely on breach data being made public, which can be months or even years after the initial breach. Reusing passwords across sites increases the risk of an attack and makes it more difficult for organizations to prevent fraudulent access to user accounts. In order to defend apps and users against this pervasive threat, it's imperative that breached passwords are detected as soon as they are compromised and accounts notified. 


As Okta point out, part of the problem here is that we don’t always find out about breached password lists.  If a company is breached, they don’t, can’t and shouldn’t just dump all of their users passwords, but it’s hard for other sites to know whether a user has been breached elsewhere and reused their password.

Yet another reminder that ignoring all of the mathematics about entropy and concentrating on making it psychologically easy for users to select a unique random password is your best move if you must have a password.  And of course, if you can manage to not have a password, either through email loops, push notifications or single sign on, you’ll be protected against an entire class of attack 


## [Private Eye: On the Limits of Textual Screen Peeking via Eyeglass Reflections in Video Conferencing [pdf] ](https://arxiv.org/pdf/2205.03971.pdf)

[https://arxiv.org/pdf/2205.03971.pdf](https://arxiv.org/pdf/2205.03971.pdf)

> Personal video conferencing has become a new norm
> after COVID-19 caused a seismic shift from in-person meetings
> and phone calls to video conferencing for daily communications
> and sensitive business. Video leaks participants’ on-screen information because eyeglasses and other reflective objects unwittingly
> expose partial screen contents. Using mathematical modeling and
> human subjects experiments, this research explores the extent
> to which emerging webcams might leak recognizable textual
> and graphical information gleaming from eyeglass reflections
> captured by webcams. The primary goal of our work is to
> measure, compute, and predict the factors, limits, and thresholds
> of recognizability as webcam technology evolves in the future.
> Our work explores and characterizes the viable threat models
> based on optical attacks using multi-frame super resolution
> techniques on sequences of video frames. Our models and
> experimental results in a controlled lab setting show it is possible
> to reconstruct and recognize with over 75% accuracy on-screen
> texts that have heights as small as 10 mm with a 720p webcam.
> 
> […]
> 
> Threat Model
> 
> We assume that the victim’s up-link video stream is enabled
> during the attack, and the adversary can acquire the down-link
> video stream of the victim. The adversary can achieve that by
> either directly intercepting the down-link video stream data,
> or recording the victim’s video with the video conferencing
> platform being used or even third-party screen recording
> services. Since the webcam peeking attack does not require
> active interaction between the victim and the adversary, the
> adversary does not need to attempt a real-time attack but can
> store the video recording and analyze the videos off-line
> 
> […]
> 
> Setup
> 
> We then displayed single
> capital letters (26 letters) on the victim screen with different
> heights ranging from 20 mm to 7 mm. The victim and
> adversary laptops had a Zoom [21] session with a video
> resolution of 1280×720. For each display of the letters, we
> recorded a 3s video of the victim’s images on the adversary
> laptop. We then used 8 consecutive frames starting from 1s for
> MFSR reconstruction and generated one corresponding image
> for each video. We generated 208 images in total for the 2
> glasses each with 4 different sizes 


This is an interesting paper.  It has been picked up by the press as a form of attack, but it’s worth noting that the experiment setup required setting up the screen to show a single letters on the screen.  What’s not covered in this paper is how easy it is to pick out an entire page of text, sequences of letters or deal with the implications of the video software creating glare.

However the attack shows that the increasing capability of webcams does start to present a new risk in inadvertent environmental disclosure.  Of note in here is that the threat model is also subject to collection and analysis later, which re-emphasizes the need to use encryption in transit. 


## [26 AWS Security Best Practices to Adopt in Production – Sysdig ](https://sysdig.com/blog/26-aws-security-best-practices/)

[https://sysdig.com/blog/26-aws-security-best-practices/](https://sysdig.com/blog/26-aws-security-best-practices/)

> One of the most important pillars of a well-architected framework is security. Thus, it is important to follow these **AWS security best practices** to prevent unnecessary security situations.
> 
> So, you’ve got a problem to solve and turned to AWS to build and host your solution. You create your account and now you’re all set up to brew some coffee and sit down at your workstation to architect, code, build, and deploy. Except, you aren’t.
> 
> There are many things **you must set up** if you want your solution to be **operative** , **secure** , **reliable** , **performant,** and **cost effective** . And, first things first, the best time to do that is now – right from the beginning, before you start to design and engineer. 


Lovely guide to the most common things that people need to do with their AWS account to improve security. 


## [Resiliency in Distributed Systems - The Pragmatic Engineer ](https://blog.pragmaticengineer.com/resiliency-in-distributed-systems/)

[https://blog.pragmaticengineer.com/resiliency-in-distributed-systems/](https://blog.pragmaticengineer.com/resiliency-in-distributed-systems/)

> Understanding the ins and outs of distributed systems is important for both backend engineers and for anyone working with large-scale systems. Large-scale systems can mean systems with high load and high queries per second (QPS), storing a large amount of data, or ones built with low latency and high reliability. These systems are pretty common across both Big Tech and high-growth startups.
> 
> One of the most interesting books I’ve found on this topic is [Understanding Distributed Systems](https://understandingdistributed.systems/) . The book was written by Roberto Vitillo, who was a Senior Staff engineer at Mozilla, then a Principal Engineer at Microsoft. The second edition of this book was released in February of this year.
> 
> I like how the book works its way from the theory needed to understand distributed systems - communication and coordination - to practical topics like scalability and resiliency. The book closes with topics on maintainability, which is an area I found surprisingly little focus with most books.
> 
> I reached out to Roberto asking if he’d be open to sharing a few chapters of the book with newsletter readers, and Roberto agreed to do so. I chose two chapters on resiliency, from section #4.
> 
> In this excerpt, we cover: 
> 
> **1. Downstream resiliency** 
> 
> * Timeout
> * Retry: exponential backoff, retry amplification
> * Circuit breaker 
> 
> **2. Upstream resiliency** 
> 
> * Load shedding
> * Load leveling
> * Rate limiting: single process and distributed implementations
> * Constant work 


This is a fantastic overview of some of the principles of distributed systems, including patterns like the exponential backoffs, retry amplification and circuit breakers.  If this is typical of the rest of the book, then it’s well worth a read (and it’s going on my amazon wish list) 


## [Relaying YubiKeys - \cube0x0\ ](https://cube0x0.github.io/Relaying-YubiKeys/)

[https://cube0x0.github.io/Relaying-YubiKeys/](https://cube0x0.github.io/Relaying-YubiKeys/)

> We are not relaying actual physical YubiKeys, we are relaying the APDU packets that the server application wants to get signed by a private key to verify the identity of the authentication so this attack works on all PIV Smart Cards but a YubiKey was used during the testing so therefore the title.
> 
> Isolated networks or sensitive services often have an additional authentication factor and some organizations are choosing to use YubiKeys or other PIV-supported devices to be their second factor. The private key on a YubiKey is protected and non-exportable so to give ourselves access to those isolated networks/services we can use an already-inserted YubiKey on a remote host and make that to authenticate our session in a relay attack. 


A reminder that things like Yubikeys and other smart cards aren’t necessarily perfect.  In certain modes, the attacker can conduct a relay attack.  It’s worth noting that the attacker needs to know the PIN, but if they can run something on the users terminal, they can either sniff that with a key logger, or scam the user into doing so.

Of course, this is a much harder attack to carry out than just stealing a password, so we’re still lowering the risk, but remember it’s not entirely foolproof 


## [6 Developer Personas Every Security Practitioner Needs to Understand | Veracode ](https://www.veracode.com/blog/managing-appsec/6-developer-personas-every-security-practitioner-needs-understand)

[https://www.veracode.com/blog/managing-appsec/6-developer-personas-every-security-practitioner-needs-understand](https://www.veracode.com/blog/managing-appsec/6-developer-personas-every-security-practitioner-needs-understand)

> When it comes to [engaging developers](https://www.veracode.com/blog/managing-appsec/how-engage-developers-build-successful-application-security-program) for a successful application security program, it is helpful to understand the types of developers you are working with. While of course each developer is a unique individual, there are some common personas I have come across in my work with development teams. In fact, as a developer in prior jobs, I have embodied some of these traits myself. Let’s dive in. 


Not the most insightful of views, but it’s always nice to have some kind of framework to use when thinking about your personas.  Someone else having done the work makes it easy as a baseline.  There might be persona’s here you disagree with, ones that you think are missing. But having that makes it easier to marshall your thoughts 


## [GitHub - controlplaneio/badrobot: BadRobot - Operator Security Audit Tool ](https://github.com/controlplaneio/badrobot)

[https://github.com/controlplaneio/badrobot](https://github.com/controlplaneio/badrobot)

> Badrobot is a Kubernetes Operator audit tool. It statically analyses manifests for high risk configurations such as lack of security restrictions on the deployed controller and the permissions of an associated clusterole. The risk analysis is primarily focussed on the likelihood that a compromised Operator would be able to obtain full cluster permissions. 


Nice tool for auditing your Kubernetes cluster 


