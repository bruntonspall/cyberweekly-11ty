---
title: "168 - The modern cloud is different"
date: 2021-09-26
description: "I think I’ve said this before, and I’m sure I’m repeating myself, but lifting and shifting your data centre into the cloud isn’t actually a good idea."
permalink: /the-modern-cloud-is-different/
---

I think I’ve said this before, and I’m sure I’m repeating myself, but lifting and shifting your data centre into the cloud isn’t actually a good idea.

The public cloud is like for like more expensive than running your own data center, and the security models mean that you will be less secure if you simply recreate your data center in the cloud.

However the ability to create, recreate, delete and move things around gives rise to cost savings, and gives rise to new security and architectural models that are likely more secure, or at least differently secure than existing systems.

But the cloud has its own set of gotchas, from complex pricing structures to configuration defaults which are far more open than expected, it’s not a simple panacea that some people will tell you it is.

The default AWS security architecture is now really quite complex, and you really need to ensure that both your architecture teams understand it, but also that your security teams understand the impact of the architecture decisions, and whether their advice and guidance is aligned or runs counter to good cloud practice.

## [AWS Security Reference Architecture: A guide to designing with AWS security services | AWS Security Blog](https://aws.amazon.com/blogs/security/aws-security-reference-architecture-a-guide-to-designing-with-aws-security-services/)

[https://aws.amazon.com/blogs/security/aws-security-reference-architecture-a-guide-to-designing-with-aws-security-services/](https://aws.amazon.com/blogs/security/aws-security-reference-architecture-a-guide-to-designing-with-aws-security-services/)

> Here’s the core architecture diagram from the guide: the AWS SRA in its simplest form. The architecture is purposefully modular and provides a high-level abstracted view that represents a generic web application. The AWS organization and account structure follows the latest AWS guidance for using multiple AWS accounts.
>  
> https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2021/06/23/AWS-Security-Reference-Architecture-1.jpg
> Figure 1: The AWS Security Reference Architecture
> 
> How to use the AWS SRA
> 
> The AWS SRA guidance can be used as either a narrative or a reference. The topics are organized as a story, so you can read them from the beginning (foundational security guidance) to the end (discussion of implementable code examples). Alternatively, you can navigate the document to focus on the security principles, services, account types, guidance, and examples that are most relevant to your needs.


This is the AWS Security Reference Architecture in its simplest form!

Joking aside, this is a useful reference for setting up your multi-organisation account management, logging, security audit and separated workloads systems effectively.  Something that we know is good practice, but surprisingly hard to actually implement.


## [Overview of Data Transfer Costs for Common Architectures | AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/overview-of-data-transfer-costs-for-common-architectures/)

[https://aws.amazon.com/blogs/architecture/overview-of-data-transfer-costs-for-common-architectures/](https://aws.amazon.com/blogs/architecture/overview-of-data-transfer-costs-for-common-architectures/)

> Data transfer charges apply based on the source, destination, and amount of traffic. Here are some general tips for when you start planning your architecture:
> 
> Avoid routing traffic over the internet when connecting to AWS services from within AWS by using VPC endpoints:
> VPC gateway endpoints allow communication to Amazon S3 and Amazon DynamoDB without incurring data transfer charges.
> VPC interface endpoints are available for some AWS services. This type of endpoint incurs hourly service charges and data transfer charges.
> Use Direct Connect instead of the internet for sending data to on-premises networks.
> Traffic that crosses an Availability Zone boundary typically incurs a data transfer charge. Use resources from the local Availability Zone whenever possible.
> Traffic that crosses a Regional boundary will typically incur a data transfer charge. Avoid cross-Region data transfer unless your business case requires it.


A nice reminder that all of that magic cloud stuff still incurs costs.  In particular, when architecting your system, the best architectures for reliability or security may also work out the most expensive.


## [AWS Service Control Policy (SCP) Repository](https://asecure.cloud/l/scp/)

[https://asecure.cloud/l/scp/](https://asecure.cloud/l/scp/)

> A repository of AWS Service Control Policy templates and examples that can be deployed using CloudFormation custom resource or AWS CLI scripts.


This is a great list of service control policies that can be easily applied to your AWS organisation.  As always, you should inspect anything before you apply it, but the list of packages here is impressive.  There's also a number of S3 Bucket Policies, IAM policies and Cloudwatch Alarms and Events Rules that you might find useful.


## [CIA director “fuming” after Havana syndrome strikes team member in India](https://arstechnica.com/science/2021/09/cia-director-fuming-after-havana-syndrome-strikes-team-member-in-india/)

[https://arstechnica.com/science/2021/09/cia-director-fuming-after-havana-syndrome-strikes-team-member-in-india/](https://arstechnica.com/science/2021/09/cia-director-fuming-after-havana-syndrome-strikes-team-member-in-india/)

> A US intelligence officer traveling in India earlier this month with CIA director William Burns reported experiencing a mysterious health incident and symptoms consistent with so-called Havana syndrome [...] The director's schedule is tightly guarded, and officials do not know if the affected intelligence officer was targeted because the officer was traveling with the director. If the health incident was an attack carried out by an adversarial intelligence agency—as feared—it's unclear how the adversarial agency learned of the trip and was able to prepare an attack.


([Joel](https://twitter.com/joelgsamuel)) [Havana syndrome](https://en.wikipedia.org/wiki/Havana_syndrome) would of course not be amusing to anyone allegedly suffering from it... but one has to wonder whether it truly is espionage for the purposes of denial of service (make someone feel unwell, so they are unable to perform their duties), or unlinked events being drawn together because spies like spy things.

A sceptic might say that agencies are also bureaucratic public sector organisations who have to justify non-delivery. One could argue that espionage is a great excuse, in addition to a "Probably Russians, give us money and we'll look into it for a few years."

The one of the US' hypothesis is Russian intelligence using targeted microwaves. On the other hand, Russian intelligence may be none the wiser and simply reveling in the happenstance.


## [Hardening Amazon EKS security with RBAC, secure IMDS, and audit logging | Snyk](https://snyk.io/blog/hardening-aws-eks-security-rbac-secure-imds-audit-logging/)

[https://snyk.io/blog/hardening-aws-eks-security-rbac-secure-imds-audit-logging/](https://snyk.io/blog/hardening-aws-eks-security-rbac-secure-imds-audit-logging/)

> Misconfigurations in infrastructure as code (IaC) can be just as dangerous as vulnerabilities in code. Small mistakes in configuration can lead to the sensitive data being readable on the internet, or private endpoints and dashboard accessible to the anonymous users and abused as the initial point of compromise. Recent security research findings indicate the rise in malware targeting the Kubernetes platform which showcases the need for secure configuration. 
> 
> In this series of blog posts, we will look into the default settings used in Amazon Elastic Kubernetes Service (EKS) deployments. We will then demonstrate how small misconfigurations or unwanted side-effects may put our clusters at risk of EKS security issues.


It's a bit generous to call these misconfigurations.  These are defaults that are enabled out of the box in the most common use cases that allow attackers to pivot through your system, escalate their permissions and run arbitrary code on your cluster.


## [Why is it so hard to decide to buy? | by Camille Fournier | Jul, 2021 | Medium](https://skamille.medium.com/why-is-it-so-hard-to-decide-to-buy-d86fee98e88e)

[https://skamille.medium.com/why-is-it-so-hard-to-decide-to-buy-d86fee98e88e](https://skamille.medium.com/why-is-it-so-hard-to-decide-to-buy-d86fee98e88e)

> Companies reward people who create new things. It is hard to identify and reward problems that are avoided. When it comes time to evaluate people, we look at systems built from scratch and believe their authors show more technical talent than those who completed similarly-challenging integration projects with less raw code. Most companies promote those who create new systems even of questionable value much faster than they promote those who might be making wiser choices by not building from scratch, which creates a pressure to build in order to grow your career.


This is a great look at the buy vs build debate, and covers a lot of the incentives in tech firms for building their own ... whatever.  But this fourth one is the one that resonates with me.  Organisations are truly terrible at estimating and measuring cost avoidance.  That's especially true when the cost is diffuse, such as saving 5 minutes of everyone's time each day.  It all adds up quickly, but it's super difficult to actively work out what that value is, and whether it's worth spending hard cash on.


## [Automatically creating and rotating GOV.UK application secrets - Technology in government](https://technology.blog.gov.uk/2021/07/23/automatically-creating-and-rotating-gov-uk-application-secrets/)

[https://technology.blog.gov.uk/2021/07/23/automatically-creating-and-rotating-gov-uk-application-secrets/](https://technology.blog.gov.uk/2021/07/23/automatically-creating-and-rotating-gov-uk-application-secrets/)

> Internal API requests between apps (such as a request to publish a page on GOV.UK) often require an authorization token. Tokens are issued to applications by Signon, our OAuth 2.0 authorization server.
> 
> Setting an expiry time on authorization tokens is recommended in the OAuth 2.0 specification. If a token is only valid for a short time this can reduce the impact should the token be leaked.
> 
> Unfortunately, adding, rotating, and deleting a secret is a manual process. Rotating a secret involves:
> 
> Generating a new token
> Updating the token in hiera-eyaml
> Having a code review process
> Deploying Puppet to our Integration, Staging, and Production environments
> This process is manual, repetitive, reactive, and scales linearly as we add more applications and app secrets. When credentials must be routinely created or rotated, this distracts developers from more valuable engineering work.


Good security engineering reduces developer toil.  It’s not enough to say “rotate credentials”, we need to make it easy, simple, and fast for people to do so.


## [Ransomware victims panicked while FBI secretly held REvil decryption key](https://arstechnica.com/information-technology/2021/09/ransomware-victims-panicked-while-fbi-secretly-held-revil-decryption-key/)

[https://arstechnica.com/information-technology/2021/09/ransomware-victims-panicked-while-fbi-secretly-held-revil-decryption-key/](https://arstechnica.com/information-technology/2021/09/ransomware-victims-panicked-while-fbi-secretly-held-revil-decryption-key/)

> For three weeks during the REvil ransomware attack this summer, the FBI secretly withheld the key that would have decrypted data and computers on up to 1,500 networks, including those run by hospitals, schools, and businesses.
> 
> The FBI had penetrated the REvil gang’s servers to obtain the key, but after discussing it with other agencies, the bureau decided to wait before sending it to victims for fear of tipping off the criminals, The Washington Post reports. The FBI hadn’t wanted to tip-off the REvil gang and had hoped to take down their operations, sources told the Post.
> 
> Instead, REvil went dark on July 13 before the FBI could step in. For reasons that haven’t been explained, the FBI didn’t cough up the key until July 21.


([Joel](https://twitter.com/joelgsamuel)) The the UK's SIGINT agency (GCHQ) publicly described its equities process in November 2018 - [https://www.gchq.gov.uk/information/equities-process](https://www.gchq.gov.uk/information/equities-process). I read that as an approach that favours releasing vulnerabilities found in technology by default.

Equities processes rightly need layered governance for self-checks and balances. The process itself sits on top of the complex means, methods and sources of intelligence gathering. The GCHQ process also makes it clear that it involves discussions with intelligence partners. Assuming GCHQ means [Five Eyes](https://en.wikipedia.org/wiki/Five_Eyes) that 4 other countries are also consulted.

Three weeks seems a little long given the state of the REvil campaign however I suspect this is built up of internal awareness (a sub team of a sub team will need to raise the fact they have the decryption capability and may need to test it first), then internal bureaucracy _then_ the FBI's equities process. That doesn't mean its OK, but I can imagine what was happening.

I may be in a particularly bad mood as I write this, but my first thought was actually its not the FBI's job to immediately provide decryption assistance to every single organisation type. They could indeed made the wheels spin a little faster to be able to help hospitals, however private business are responsible for their own cybersecurity and if they fail due to their own negligence, then they fail. Even when Critical National Infrastructure (CNI) is impacted anywhere in the world, I roll my eyes a little, as those organisations have generally still done a bad job at cybersecurity but the government has little choice but to help. The "we told you so" unsatisfyingly, has to wait.


## [Epistemic trespassing, or epistemic squatting? - by Noah Smith - Noahpinion](https://noahpinion.substack.com/p/epistemic-trespassing-or-epistemic)

[https://noahpinion.substack.com/p/epistemic-trespassing-or-epistemic](https://noahpinion.substack.com/p/epistemic-trespassing-or-epistemic)

> Contrary to what Ballantyne says, it’s not always clear who’s an expert and who’s a trespasser. In practice, expertise is defined by consensus among communities of people who all or mostly accept and promote each other as experts. These communities can be formal, like the American Economic Association, or informal, like “DSGE macroeconomists”. But the basic idea here is that these communities are self-judged — they deny outsiders the right to adjudicate whether they possess actual expertise.
> 
> This strategy often produces good results, as demonstrated by the remarkable practical success of a bunch of scientific fields. But it’s not foolproof. Thanks to the quirks of human sociology, it’s possible for exclusive communities of self-described experts to arise who don’t actually have the expertise they claim — and even for these communities to be recognizes as experts by the broader public, at least for a time. For example, the world has now woken up to the fact that string theory is not empirically testable. But for a long time, the field was held in near-universal acclaim, with string theorists issuing repeated false promises of testability. For decades, mathematician Peter Woit — himself an epistemic trespasser! — has documented these false promises on his blog, along with various efforts by the string theorists to defend the exclusivity of their intellectual enterprise.


This is a fascinating view on “epistemic trespassing”, which is to say when experts in one field weigh in on another field about which they aren’t trained or experts.

Obviously we see this a lot on social media, where it seems like everyone is simultaneously an expert in diplomacy, counter terrorism, trade negotiations and viral spreading.

But the argument here is that it can be really valuable to have outside experts weigh in on areas they aren’t trained in because they bring a set of skills and experiences into an area that might be hide bound, trapped by its own assumptions or taken over by a small pool of experts who reject outsiders.


## [Project Zero: Understanding Network Access in Windows AppContainers](https://googleprojectzero.blogspot.com/2021/08/understanding-network-access-windows-app.html?m=1)

[https://googleprojectzero.blogspot.com/2021/08/understanding-network-access-windows-app.html?m=1](https://googleprojectzero.blogspot.com/2021/08/understanding-network-access-windows-app.html?m=1)

> I recently discovered a configuration issue with the Windows Firewall which allowed the restrictions to be bypassed and allowed an AppContainer process to access the network. Unfortunately Microsoft decided it didn't meet the bar for a security bulletin so it's marked as WontFix.
> 
> As the mechanism that the Windows Firewall uses to restrict access to the network from an AppContainer isn't officially documented as far as I know, I'll provide the details on how the restrictions are implemented. This will provide the background to understanding why my configuration issue allowed for network access.
> 
> I'll also take the opportunity to give an overview of how the Windows Firewall functions and how you can use some of my tooling to inspect the current firewall configuration. This will provide security researchers with the information they need to better understand the firewall and assess its configuration to find other security issues similar to the one I reported. At the same time I'll note some interesting quirks in the implementation which you might find useful


This is a super nerdy deep dive into windows networking, which is enthralling reading if you love this kind of thing


