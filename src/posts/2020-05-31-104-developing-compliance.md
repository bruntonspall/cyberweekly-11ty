---
title: "104 - Developing compliance"
date: 2020-05-31
description: "How technical are we as security people?"
permalink: /developing-compliance/
---

How technical are we as security people?

Most people in security are not software developers by trade.  This isn't necessarily a bad thing, software is just a small part of security. Culture, behaviours and physical aspects of security are just as important (if not more so) to a wholistic discipline.  But we tend to lack the development mindset within security.  Our staff not only have only a passing experience of the technical issues that underpin the "cyber domain", but we don't look to solve security problems in an automated, repeatable and defined way.

Some of us treat compliance as a bad word, as something that is fruitless and not adding in value to our agile software development processes.  But in reality, if our compliance processes can be automated, if we can produce code that checks for compliance with policies, which themselves are kept as code, then compliance doesn't need to be fruitless and valueless.  It can demonstrate that our security controls and assumptions are in place, which gives us confidence that the system is secure.

## [How we’ve evolved on-call at Monzo](https://monzo.com/blog/how-weve-evolved-on-call-at-monzo)

[https://monzo.com/blog/how-weve-evolved-on-call-at-monzo](https://monzo.com/blog/how-weve-evolved-on-call-at-monzo)

> The primary on-caller can bring in a specialist whenever they need support. For example, an alert about a database node being down is fired and the primary and shadow on-callers are paged. They acknowledge the page and start working to mitigate the problem with the help of runbooks.
> 
> If, after a little while, they feel out of their depth, they escalate to the Cassandra specialist (our main storage backend). All of this is handled by tooling we built in-house and integrated with Slack. The specialist then jumps in and works with them to mitigate the impact.
> 
> In such cases, the primary and shadow on-callers are typically responsible for leading the incident and coordinating overall response: making sure the relevant parts of the business and stakeholders are kept in the loop, the different bits of the investigation are not being duplicated across engineers, etc. This let’s the specialist on-caller focus completely on mitigation and technical investigation.


On call is almost always painful for growing technical organisations, and even many mature organisations.

Rarely have I seen the description of incident commander so well described as this however.  The ability to call in specialists, who aren't there to run the incident, don't need to worry about communications and managing work, they are there to focus on investigation, mitigation and remediation.  

The use of twin rotas here is a smart move, and one that I'd recommend organisations use as soon. as they've grown beyond the point where the tech leads have good expertise in all systems and areas (probably at about 10-20 developers in my experience)


## [Why you can’t just ask “why” – Surfing Complexity](https://surfingcomplexity.blog/2020/05/22/why-you-cant-just-ask-why/)

[https://surfingcomplexity.blog/2020/05/22/why-you-cant-just-ask-why/](https://surfingcomplexity.blog/2020/05/22/why-you-cant-just-ask-why/)

> The experts were inventing explanations without even being aware that they were doing so. Philosophers of mind use the term confabulation (technically broad confabulation) to refer to this phenomenon: how people will unknowingly fabricate explanations for their actions.
> 
> And therein lies the problem of asking “why”.
> 
> In the wake of an incident, we often want to understand why it is people did certain things: both for the people whose actions contributed to the incident (why did they make a global configuration change?) and for people whose actions mitigated the incident (why did they suspect a retry storm rather than a DDOS attack?)
> 
> The problem is, you can’t just ask people why, because people confabulate. You can, of course, simply ask people why they took the actions they did. Heck, you might even get a confident, articulated explanation. But you shouldn’t believe that the explanation they give corresponds to reality.


This is well worth understanding if you are involved at all in incident management or on-call processes.  When people respond to a crisis, the actions that they take are ones that they will later say had rational reasons.  But the reality of the situation at the time is far different.  Each action will come because of certain intents, but documenting and recording those intents is really hard because of the amount of hindsight bias and survivor biases that humans have built in.


## [Hello Serverless](https://www.serverlessops.io/blog/hello-serverless)

[https://www.serverlessops.io/blog/hello-serverless](https://www.serverlessops.io/blog/hello-serverless)

> Hello Serverless The Series
> This series is not intended to be a tutorial for building a running application. This series is also not intended to be a deep dive into serverless for becoming an expert. This series falls in the middle of that. It is aimed at the individual or team that is building their first serverless application for a limited scoped and well-defined use case that should be delivered over maybe 2-6 weeks; something I highly recommend as a first serverless application over a project expected to take months to complete.
> 
> [Next from the "Serverless Functions" post]
> 
> There are, of course, drawbacks to adopting multiple serverless functions. The primary drawback is a lack of familiarity with the design. The patterns for building non-serverless web services are largely understood, which is why this series started with a Python Flask application. We separated routes, models, and shared code as someone building a backend web API might routinely do. The structure of our application in this post will be different. We are actually going to combine route and model logic into the application’s serverless functions. Plus, we’re going to have to share code between serverless functions differently. This results in a learning curve. It’s not insurmountable, but people are going to stumble. There are decisions in this version of the application that are the result of my own trial, error, and learning. I settled on how I structure a multi-function serverless application over years of experience.


This is a well written series of blog posts that clearly shows how to take a very very simple problem, solve it in a traditional Python Flask Monolith and then migrate it to AWS Lambda.

Because it goes that way, it's far easier to see what each of the Lambda features is buying you, and how it interacts with the system.

The series is still ongoing, and I'm looking forward to seeing the section on testing and deployment more fully fleshed out.


## [Exim Mail Transfer Agent Actively Exploited by Russian GRU Cyber Actors > National Security Agency Central Security Service > Article View](https://www.nsa.gov/News-Features/News-Stories/Article-View/Article/2196511/exim-mail-transfer-agent-actively-exploited-by-russian-gru-cyber-actors/)

[https://www.nsa.gov/News-Features/News-Stories/Article-View/Article/2196511/exim-mail-transfer-agent-actively-exploited-by-russian-gru-cyber-actors/](https://www.nsa.gov/News-Features/News-Stories/Article-View/Article/2196511/exim-mail-transfer-agent-actively-exploited-by-russian-gru-cyber-actors/)

> FORT MEADE, Md. , May 28, 2020 —
> Russian military cyber actors, publicly known as Sandworm Team, have been exploiting a vulnerability in Exim mail transfer agent (MTA) software since at least last August. Exim is a widely used MTA software for Unix-based systems and comes pre-installed in some Linux distributions as well. The vulnerability being exploited, CVE-2019-10149, allows a remote attacker to execute commands and code of their choosing. The Russian actors, part of the General Staff Main Intelligence Directorate’s (GRU) Main Center for Special Technologies (GTsST), have used this exploit to add privileged users, disable network security settings, execute additional scripts for further network exploitation; pretty much any attacker’s dream access – as long as that network is using an unpatched version of Exim MTA.
> 
> When the patch was released last year, Exim urged its users to update to the latest version. NSA adds its encouragement to immediately patch to mitigate against this still current threat.


Breaking in through your mail servers is a nasty way in to a network.  Of course, there's not really many good reasons why you should be running your own mail server, when Microsoft and Google will run one for your business, host it "off-network", and give you controlled BYOD access, constantly patch it and  maintain it for you.

But if you are running your own Exim servers, especially those odd ones, preinstalled on an old Ubuntu box that your application development team runs to host builds just so the build server can send build failure emails, then make sure it's patched and up to date.


## [FSI | Cyber | Internet Observatory - Virality Project (US): Marketing meets Misinformation](https://cyber.fsi.stanford.edu/io/news/manufacturing-influence-0)

[https://cyber.fsi.stanford.edu/io/news/manufacturing-influence-0](https://cyber.fsi.stanford.edu/io/news/manufacturing-influence-0)

> The campaign to recast Judy Mikovits as a whistleblower offers a case study in the type of factional network dynamics and cross-platform content spread that will likely happen repeatedly over the coming months, around COVID-19 as well as the 2020 election. Although the activity involved some fake Twitter accounts, there was nothing that crossed the line into coordinated inauthentic behavior -- this was a marketing campaign that pulled ordinary people into the sharing process. However, it was also a marketing campaign that made blatantly false claims and increased confusion and skepticism around vaccines, health authorities, and institutional responses to the pandemic. Platforms have rightly committed to mitigating health misinformation; this example makes clear the need to develop better solutions that avoid after-the-fact content takedowns that turn manipulative charlatans into free-expression martyrs. Further study of cross-platform, cross-faction sharing dynamics around debunking content in particular would help inform fact-checking efforts, and help platforms gauge how to respond to highly-misleading viral videos. 


Lovely piece of analysis on some disinformation that was spread via Youtube and social media.

The Gephi graphs showing the way that this stuff is shared, the mentions and wording just demonstrates that we're far more in danger from armies of well meaning misinformed believers than we are from bot armies.  But the bot armies help get the content to the gullible masses and help ensure that the algorithms continue to highlight and distribute the content.


## [Using Gatekeeper in Kubernetes | Exploring Software](https://echorand.me/posts/gatekeeper-kubernetes/)

[https://echorand.me/posts/gatekeeper-kubernetes/](https://echorand.me/posts/gatekeeper-kubernetes/)

> Gatekeeper allows a Kubernetes administrator to implement policies for ensuring compliance and best practices in their cluster. It makes use of Open Policy Agent (OPA) and is a validating admission controller. The policies are written in the Rego language. Gatekeeper embraces Kubernetes native concepts such as Custom Resource Definitions (CRDs) and hence the policies are managed as kubernetes resources. The GKE docs on this topic are a good place to learn more.


Using the Open Policy Agent and Kubernetes, with Gatekeeper.  Gatekeeper allows you to apply OPA policy as code to validate and audit your kubernetes pods and ensure that they meet defined policies.  This blog post gives a nice overview of the Rego language and the way that the policies work.


## [Kubernetes Pod Security Policies with Open Policy Agent - InfraCloud Technologies](https://www.infracloud.io/kubernetes-pod-security-policies-opa/)

[https://www.infracloud.io/kubernetes-pod-security-policies-opa/](https://www.infracloud.io/kubernetes-pod-security-policies-opa/)

> Open Policy Agent as an admission controller
> Open Policy Agent (OPA) is an open source, general-purpose policy engine that makes it possible to write policy as code. OPA provides a high level declarative language – Rego – to enable policy as code. Using OPA, we can enforce policies across microservices, CI/CD pipelines, API gateways and so on. One of the most important use-case for OPA is Kubernetes policy enforcement as an Admission Controller.
> 
> OPA as an admission controller allows you to enforce policies such as non-root user, requiring specific labels for resources, ensuring all pods specify resource requests and limits and so on. Basically, OPA allows you to write any custom policy as code using Rego language.


Further than just using Gatekeeper and OPA for policy violations about how your pods are constructed and delivered, but also enables you to write pod security policies, that can allow, disallow or audit things like pods that require root access, request certain filesystem paths, or require certain syscalls.  This means that you can actively audit the security of pods being created and deployed on your system.


## [Hackers Just Dropped a Jailbreak They Say Works for All iPhones - VICE](https://www.vice.com/en_us/article/dyz8nw/iphone-ios-ios13-jailbreak-uncover-unc0ver)

[https://www.vice.com/en_us/article/dyz8nw/iphone-ios-ios13-jailbreak-uncover-unc0ver](https://www.vice.com/en_us/article/dyz8nw/iphone-ios-ios13-jailbreak-uncover-unc0ver)

> On Saturday, hackers and developers released the first public jailbreak for Apple's iOS operating system that they say works at launch on all iOS devices. A hacker who worked on the jailbreak says it works by taking advantage of a vulnerability in iOS that Apple is not aware of, or a so-called zero day.
> 
> The news signals the first time a jailbreak has been released that works on all devices on launch day since iOS 10, according to iOS security researcher Pwn20wnd, who discovered the underlying vulnerability powering the new jailbreak.
> 
> "iPhones are getting more secure every year because Apple is learning their mistakes from public jailbreaks or attacks they find in the wild," Pwn20wnd told Motherboard in an online chat.


New ways to jailbreak your phone.  This one claims to still retain the iOS security functions, meaning that it doesn't mean that jailbreaking it will reduce the security functionality of your device, but it's worth remembering that jailbroken software can often do things that might be prevented by the AppStore, which is a security feature in its own right


## [Zero-day in Sign in with Apple](https://bhavukjain.com/blog/2020/05/30/zeroday-signin-with-apple/)

[https://bhavukjain.com/blog/2020/05/30/zeroday-signin-with-apple/](https://bhavukjain.com/blog/2020/05/30/zeroday-signin-with-apple/)

> I found I could request JWTs for any Email ID from Apple and when the signature of these tokens was verified using Apple’s public key, they showed as valid. This means an attacker could forge a JWT by linking any Email ID to it and gaining access to the victim’s account.
> 
> Sample Request (2nd step)
> 
> 
> POST /XXXX/XXXX HTTP/1.1
> Host: appleid.apple.com
> 
> {"email":"contact@bhavukjain.com"}
> 
> Here on passing any email, Apple generated a valid JWT (id_token) for that particular Email ID.


Declared to Apple Security and paid $100,000 reward, but well worth it.

This is a complete face-palm of a security bug by Apple.  In essence, when you went to sign in, you could get a JWT token for anyone's apple account, without needing to prove any ownership or authenticity of owning the account.


## [A Guide to Threat Modelling for Developers](https://martinfowler.com/articles/agile-threat-modelling.html)

[https://martinfowler.com/articles/agile-threat-modelling.html](https://martinfowler.com/articles/agile-threat-modelling.html)

> Is threat modelling too complex to be of value? Should developers just follow a checklist, 'cross their fingers' and hope they get lucky? Skepticism can be healthy, but learning threat modelling is a key skill for developers, I believe. What we need is the right approach, and tools to tame the complexity. This guide has been written in that spirit, and begins with three ideas which make identifying good, risk-based security requirements much simpler.
> 
> The first thing to introduce is a simple and flexible structure for threat modelling [2]. This is based on three key questions. It helps to commit this structure to memory. You can use the three question structure as a guide whenever you need to assess threats. Like riding a bike, once you have mastered the basics you will be able to apply and grow those skills.
> 
> Activity	Question	Outcome
> Explain and explore	What are you building?	A technical diagram
> Brainstorm threats	What can go wrong?	A list of technical threats
> Prioritise and fix	What are you going to do?	Priorised fixes added to backlog
> This guide follows the three question structure. In each threat modelling session, you should spend about a third of your time answering each question. Then you will come out with a useful result. 


This is a good "simple" guide to threat modelling.  I've worked with Jim for a number of years and this is a brilliant snapshot of several years of thinking, testing various models and running it with actual agile development teams. 

It's easy to dismiss this as too simple, but the reality is that almost all of the people trying to make threat modelling complex benefit hugely from it feeling unapproachable.  Stripping something down to basics so it's as easy as this to summarise and easy to apply is really hard.


## [The Octopus Scanner Malware: Attacking the open source supply chain - GitHub Security Lab](https://securitylab.github.com/research/octopus-scanner-malware-open-source-supply-chain)

[https://securitylab.github.com/research/octopus-scanner-malware-open-source-supply-chain](https://securitylab.github.com/research/octopus-scanner-malware-open-source-supply-chain)

> On March 9, we received a message from a security researcher informing us about a set of GitHub-hosted repositories that were, presumably unintentionally, actively serving malware. After a deep-dive analysis of the malware itself, we uncovered something that we had not seen before on our platform: malware designed to enumerate and backdoor NetBeans projects, and which uses the build process and its resulting artifacts to spread itself.
> 
> In the course of our investigation we uncovered 26 open source projects that were backdoored by this malware and that were actively serving backdoored code.
> 
> This is the story of Octopus Scanner: An OSS supply chain malware.


Attacking systems through the developers IDE is particuarly nasty.  There [was a famous paper by Ken Thompson](https://www.cs.cmu.edu/~rdriley/487/papers/Thompson_1984_ReflectionsonTrustingTrust.pdf) (Of Unix, C, Plan 9 and Go fame) about the fact that we can never truly validate the output of a compiler because the tools that we use to do the validation may also be compromised to hide the trojan.

Anyway this isn't that bad, but it's bad enough.  Malware that infects a users NetBeans IDE, and it goes on to infect every project they build with that IDE.

It's not like NetBeans is the most popular UI for developers, so this as a target is interesting.  Additionally, it doesn't infect major build systems unless they are using NetBeans to conduct the build.  In the java world, Maven, Ant and similar tools are far more common.  This suggests that it may have been a targeted attack that got out into the wild, something that was picking on a specific development team that builds their project locally and deploys it (or automates a NetBeans build).


