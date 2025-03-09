---
title: "127 - Secure your platforms"
date: 2020-11-29
description: "Security isn't just about one thing.  Security people cover physical threats, cyber threats as well as information risks and often data protection concerns as well."
permalink: /secure-applications-and-secure-the-platform/
---

Security isn't just about one thing.  Security people cover physical threats, cyber threats as well as information risks and often data protection concerns as well.

We tend to get a little focused on our speciality, and see everything through the one lense.  For myself, that means focusing on the security of digital services and end user devices, and forgetting the physical, personnel and process security areas that are just as important.

But even within our areas, we can over-focus on certain aspects of security.  If you are a developer heavy shop, you tend to worry about how your developers write code, how you test it for security issues, and where and how it's deployed.  But if you are running your own code, you probably have a platform of infrastructure that needs managing and securing as well.

The statistics from DataDog indicates that large numbers of people deploy Kubernetes and then take a long time to upgrade it.  That's understandable, it's a major and complicated infrastructure system with lots of moving parts and while CNCF have done a lot to make it easier to upgrade, organisations are used to performing major infrastructure updates on an annual basis at best.

But the rate of change in these platform providers is hugely faster than it was in the non-cloud-native generation of platforms.  CNCF releases Kubernetes updates once a quarter, and AWS releases new features and changes so often I can barely keep up with the announcements.

But a security bug in your platform can mean that a single, unimportant and unmaintained application on your platform can become a risk to the entire platform and to all of the other applications on your platform.

As well as concerning yourself with the software development and deployment of your applications, you need to focus on the methods and mechanisms for managing and deploying the infrastructure itself.  You need to ensure that the configuration is tested, is auditable, and is easy to change and deploy.  Only through deploying regular changes to the infrastructure will you be able to patch fast enough to keep up with the changes going on.  And if you think upgrading Kubernetes once a quarter is hard, try doing it after 2 years with 8 versions of releases to apply to your cluster!

## [Why the UK’s National Cyber Force is an important step forward](https://www.iiss.org/blogs/analysis/2020/11/uk-national-cyber-force)

[https://www.iiss.org/blogs/analysis/2020/11/uk-national-cyber-force](https://www.iiss.org/blogs/analysis/2020/11/uk-national-cyber-force)

> If, for example, a military operator has the best skills and capability to prevent the internet from being used as a global platform for the sexual abuse of children or fraud, then that is how they can – and should – be assigned and authorised.
> 
> An added advantage is that military operators can learn to ‘skirmish’ on real cyber operations, rather than just training on a test range while waiting to deliver a military cyber effect when required. Conversely, whenever there is an overriding need for a military effect – to support forces on a battlefield, for example – all the relevant NCF capabilities can easily be brought to bear. This point is worth emphasising – while predominantly focused in peacetime on tackling non-military targets, the NCF also prepares the UK for the use of cyber capabilities in armed conflict.
> 
> Some commentators are rightly quick to remind us of the risks posed by such capabilities to an environment that is fundamental to our daily lives – the global internet – and to warn against its potential ‘militarisation’. But cyberspace is no different in this regard from land, sea and air – each are central to our day-to-day peaceful existence, each requiring their fundamental freedoms, but in each we hope to deter others from fighting while preparing to fight ourselves, if we have to.


This is an interesting argument around the creation of the national cyber force, but one that has a worrying tone for me.

To suggest that military operators can learn to skirmish on what is essentially law enforcement operations is a worrying suggestion.  If you suggested that the army should work as police officers on the streets rather than training on a test range then I think people would be rightly concerned.  


## [Joint Cyber Warfighting Architecture Would Benefit from Defined Goals and Governance [pdf]](https://www.gao.gov/assets/720/710760.pdf)

[https://www.gao.gov/assets/720/710760.pdf](https://www.gao.gov/assets/720/710760.pdf)

> Cyber Command has not defined goals for the JCWA that would describe
> how current and future joint cyber warfighting systems DOD procures
> would interoperate. The absence of goals is contrary to leading practices
> we identified in our prior work, which call for program goals to clearly
> define desired program outcomes.11 Clearly defined goals explain the
> purposes of a program and the results an organization intends to achieve.
> Goals also provide the basis for developing performance measures that
> help organizations demonstrate progress. By defining JCWA goals, DOD
> can describe overall system objectives, relationships, and dependencies
> of its JCWA programs and then develop performance measures to track
> progress of the JCWA systems as whole.
> 
> In the absence of interoperability goals, JCWA programs lack objectives
> that would implement consistent practices among the programs, such as
> data tagging standards. Program officials told us they discuss such
> standards informally, in a “coalition of the willing.” This group represents
> acquisition personnel within the various JCWA programs that coordinate
> informally to share information, but these efforts are not synchronized
> through JCWA goals—meaning each program is working independently
> to become interoperable.


I can't quite put my finger on this.  I can't work out if the JCWA has failed to pull together and define the kind of structures that one would need from a unified cyber platform for military use, or whether this is the GAO expecting to see something far more command-and-control in how this is all pulled together, and the reality is that they are unifying the systems through more agile and people oriented approaches instead.

Interesting reading none-the-less.


## [Microsoft adds consent phishing protection to Office 365](https://www.bleepingcomputer.com/news/security/microsoft-adds-consent-phishing-protection-to-office-365/)

[https://www.bleepingcomputer.com/news/security/microsoft-adds-consent-phishing-protection-to-office-365/](https://www.bleepingcomputer.com/news/security/microsoft-adds-consent-phishing-protection-to-office-365/)

> The new generally available app consent policies for end-user consent provide administrators with "more controls over the apps and permissions to which users can consent."
> 
> 
>  
> "To reduce the risk of malicious applications attempting to trick users into granting them access to your organization's data, we recommend that you allow user consent only for applications that have been published by a verified publisher," Microsoft explains.
> 
> Once app consent policies are configured, users will only be able to grant permissions to apps developed by verified publishers thus blocking future consent phishing attacks.


This is good news.  People who want to authorise an application to access their microsoft account, often don't realise that they might also be giving that website or application the permission to read all the documents they have, or browse all the users on their organisations domain.  Admins therefore have to forbid the use of applications, but that prevents the easy use of good authentication tools for SaaS services.

By allowing corporations to define a policy of privileges that are low impact, that they can allow users to enable, they can enable easier self service with O365 applications without giving away the keys to the kingdom.


## [We’ve published our first digital strategy at the Royal Borough of Greenwich - Digital](https://www.royalgreenwich.gov.uk/blog/digital/post/103/we%E2%80%99ve-published-our-first-digital-strategy-at-the-royal-borough-of-greenwich)

[https://www.royalgreenwich.gov.uk/blog/digital/post/103/we%E2%80%99ve-published-our-first-digital-strategy-at-the-royal-borough-of-greenwich](https://www.royalgreenwich.gov.uk/blog/digital/post/103/we%E2%80%99ve-published-our-first-digital-strategy-at-the-royal-borough-of-greenwich)

> This is the first digital strategy that the council has had, and I’m delighted that it will be open for comment from the public, to whom we’re accountable for running the best council possible. Working in the open is fairly new at Royal Greenwich, as it is in many other public sector organisations. It’s testament to the support that the Chief Executive Debbie Warren, and the Leader of the Council Danny Thorpe, have shown, that we’ve come as far as we have.  
> 
> For me, this marks the beginning of a new era for the council. We’re starting a 4-year period of investment in digital technology, which is no trivial move at a time when all councils are struggling financially. However, it’s clear to us that digital is one of the biggest opportunities we have to keep us on a sustainable financial footing. By helping our residents access services more easily, introducing new channels, using service design to change our processes and systems, and using data to better understand what people need, we will make our services better as well as more cost-effective to run. 


This committment to transparency is to be lauded, and the [strategy itself](https://www.royalgreenwich.gov.uk/info/200222/policies_and_plans/2259/digital_strategy_2020_to_2024) is readable and focused on deliverable and measurable commitments.  Each section has a set of clear achievable objectives, along with a set of programmes of work that they think will help achieve those objectives.


## [Secret Amazon Reports Expose Company Spying on Labor, Environmental Groups](https://www.vice.com/en/article/5dp3yn/amazon-leaked-reports-expose-spying-warehouse-workers-labor-union-environmental-groups-social-movements)

[https://www.vice.com/en/article/5dp3yn/amazon-leaked-reports-expose-spying-warehouse-workers-labor-union-environmental-groups-social-movements](https://www.vice.com/en/article/5dp3yn/amazon-leaked-reports-expose-spying-warehouse-workers-labor-union-environmental-groups-social-movements)

> A team within Amazon's Global Security Operation Center, which includes former military intelligence analysts, according to LinkedIn, closely tracks organized labor and union activity in France, the United Kingdom, Italy, Spain, Germany, Poland, Austria, the Czech Republic, and Slovakia—noting where organized labor groups are strongest and could influence Amazon workers. 
> 
> In one set of documents, known as "security risk assessments," analysts gather data on and evaluate potential risks to Amazon operations at the sites of future and currently operating Amazon warehouses, sorting centers, and delivery stations. These documents break down their analyses into at least four categories: crime, cargo crime, extremism and terrorism, and operational environment. For example, as part of its tracking of crime, analysts monitor the drug trade, noting how it could impact its warehouses but also specifically whether its workers are likely to be drug users. Requests for risk assessments of Amazon warehouse sites are sent to the team by email, according to an email viewed by Motherboard. 


If we step away from the question here of Amazon's engagement with its labour force, what you see is a great overview of an incredibly sophisticated and capable threat operations team.  Producing security risk assessments on the risk of criminal activity on their operations, Monthly business reviews covering inventory loss and recovery and peak risk assessments that cover risks to the peak shopping times.

These are all products that enable the business to make decisions that enable it to function (and make a profit).  Of course this will include evidence of union activity, because union activity can result in strikes and productivity diminishing action (from legal work to rule to industrial sabotage).

The ethical question here is not whether it's ethical to gather this information, of course it's entirely ethical to gather this information, the question is how Amazon decides to use this information and what actions it thinks is appropriate.


## [Digital government during the coronavirus crisis - IfG](https://www.instituteforgovernment.org.uk/sites/default/files/publications/digital-government-coronavirus.pdf)

[https://www.instituteforgovernment.org.uk/sites/default/files/publications/digital-government-coronavirus.pdf](https://www.instituteforgovernment.org.uk/sites/default/files/publications/digital-government-coronavirus.pdf)

> Working across organisational boundaries is vital
> ‘Project Unblock’ took the opportunity to break down technical barriers between
> departments, allowing them to collaborate more easily. This was important as the
> development of many new and vital services spanned existing departmental silos.
> The strengthening in recent years of government functions and professions,
> including data, digital and technology, has helped to build requisite expertise across
> government. There are some success stories where departments have used and shared
> data more effectively, such as the development of the vulnerable people service,
> which used driving licence data to access HMRC services, DWP’s use of data, and the
> ongoing work of GOV.UK. However, government needs to be more transparent about
> how such data is being used and shared.


This is a fascinating read if you are a government wonk like me.  Seeing an external anaylsis of how well government pulled together during the coronavirus crisis is excellent reading, and I know many freinds who are exhausted, tired and have worked tirelessly to make this stuff happen.

What stands out to me however is just how important the enabling features actually are.  There's entire sections on video conferencing and the use of chat services between departments, but what is clear is that those systems that enable and encourage inter-departmental conversations have been critical in this period.


## [AWS Network Firewall – New Managed Firewall Service in VPC | AWS News Blog](https://aws.amazon.com/blogs/aws/aws-network-firewall-new-managed-firewall-service-in-vpc/)

[https://aws.amazon.com/blogs/aws/aws-network-firewall-new-managed-firewall-service-in-vpc/](https://aws.amazon.com/blogs/aws/aws-network-firewall-new-managed-firewall-service-in-vpc/)

> These customers need the ability to do things like URL filtering on outbound flows, pattern matching on packet data beyond IP/Port/Protocol and the ability to alert on specific vulnerabilities for protocols beyond HTTP/S.
> 
> Today, I am happy to announce AWS Network Firewall, a high availability, managed network firewall service for your virtual private cloud (VPC). It enables you to easily deploy and manage stateful inspection, intrusion prevention and detection, and web filtering to protect your virtual networks on AWS. Network Firewall automatically scales with your traffic, ensuring high availability with no additional customer investment in security infrastructure.
> 
> With AWS Network Firewall, you can implement customized rules to prevent your VPCs from accessing unauthorized domains, to block thousands of known-bad IP addresses, or identify malicious activity using signature-based detection. AWS Network Firewall makes firewall activity visible in real-time via CloudWatch metrics and offers increased visibility of network traffic by sending logs to S3, CloudWatch and Kinesis Firehose. Network Firewall is integrated with AWS Firewall Manager, giving customers who use AWS Organizations a single place to enable and monitor firewall activity across all your VPCs and AWS accounts. Network Firewall is interoperable with your existing security ecosystem, including AWS partners such as CrowdStrike, Palo Alto Networks, and Splunk. You can also import existing rules from community maintained Suricata rulesets.


I was puzzled by this at first.  Within AWS, SecurityGroups and NetworkACL's provide forms of stateless firewalls that offer most of what customers want.  But looking deeper, this is the ability to provide far more stateful and content inspecting firewalls.  

This can save you having to manually deploy outbound internet proxies for your AWS zones, or put in place firewalls that can take feeds from your threat information feeds and block known indicators.

If you aren't mature enough to have all those things, then I don't think you gain a lot from that, but if you've got a Security Operations Center that has those feeds, this may well become a useful and almost mandatory tool in the AWS arsenal.


## [New – Deep Dive with Security: AWS Identity and Access Management (IAM)](https://aws.amazon.com/about-aws/whats-new/2020/11/new-deep-dive-with-security-aws-identity-and-access-management-iam/)

[https://aws.amazon.com/about-aws/whats-new/2020/11/new-deep-dive-with-security-aws-identity-and-access-management-iam/](https://aws.amazon.com/about-aws/whats-new/2020/11/new-deep-dive-with-security-aws-identity-and-access-management-iam/)

> This new on-demand digital course provides a deep dive into AWS IAM and best practices for using IAM policies. The advanced course is designed for security professionals with a working knowledge of AWS and it includes five learning modules, video demonstrations, assessments, and three optional self-paced labs.
> 
> As part of this training, you’ll learn about identity federation, temporary credentials, and ways to troubleshoot access issues. You’ll also review use cases for role-based and attribute-based access controls. The optional labs will facilitate your hands-on skills development for policy creation, role assumption, and rogue permissions.


This looks quite neat.  I haven't had time to try it out, but AWS providing deep dive courses into some of the most problematic and difficult areas of AWS can only be a good thing, and the fact that the courses are free just makes it better.


## [Announcing the Cloud Native Security White Paper | Cloud Native Computing Foundation](https://www.cncf.io/blog/2020/11/18/announcing-the-cloud-native-security-white-paper/)

[https://www.cncf.io/blog/2020/11/18/announcing-the-cloud-native-security-white-paper/](https://www.cncf.io/blog/2020/11/18/announcing-the-cloud-native-security-white-paper/)

> The CNCF Security Special Interest Group (SIG) has just released a new Cloud Native Security Whitepaper to help educate the community about best practices for securing cloud native deployments. The whitepaper intends to provide organizations and their technical leadership with a clear understanding of cloud native security, its incorporation in lifecycle processes, and considerations for determining the most appropriate application thereof. 


I'm a bit meh about the details of the paper itself.  It covers a lot of the areas of Application Security that are needed by cloud native developers, and it serves as a good introduction to more traditional security experts, but it doesn't really cover some of the areas that I'd consider critical.

It's overly focused on the development and testing of the application code that goes into production, and does not really cover enough about the security of the cloud native platforms themselves, and the assurance that they need.  


## [11 Facts About Real-World Container Use | Datadog](https://www.datadoghq.com/container-report/#8)

[https://www.datadoghq.com/container-report/#8](https://www.datadoghq.com/container-report/#8)

> The most popular Kubernetes version is 17 months old
> Kubernetes releases a new minor version every quarter, giving users access to new features and enhancements. But in spite of this frequent development cycle, most organizations are still running older, more established versions of Kubernetes. This is consistent with our findings in last year's report, where our research showed that the most popular version in use was v1.13, which was 10 months old at the time. At the time of this report, v1.15 is the most widely used version, even though it was released 17 months ago. Note that since each organization may run several versions of Kubernetes, the percentages in the graph below add up to more than 100 percent.


This is an interesting report from the data that DataDog gathers from their customers (which is a separate thing).

There's loads to digest here, but the fact that the underlying platform is often nearly 2 years old, and only around 15% of organisations  were running the most recent 2 version releases means that underlying security patches are unlikely to be being applied to the platform.  That means that if there are security issues in the underlying platform, from poor defaults to container breakouts or insecure API's, those are going to stick around for a long time!


