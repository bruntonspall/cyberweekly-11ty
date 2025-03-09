---
title: "63 - Put more security in your SaaS"
date: 2019-08-03
description: "When we talk about companies moving to \"the cloud\" we tend to mean the migration from data center to hyperscale cloud data center.  People moving their servers from an on-premise or colocated data center into Azure, Google Cloud, AWS or similar."
permalink: /put-more-sass-in-your-security/
---

When we talk about companies moving to "the cloud" we tend to mean the migration from data center to hyperscale cloud data center.  People moving their servers from an on-premise or colocated data center into Azure, Google Cloud, AWS or similar.

But in reality, much of the moving to the cloud is the migration of working tools to SaaS vendors, from your queue of work to Trello or Jira, to using Salesforce for your CRM.  

This cloud adoption is much quieter, has a lot less notice, and isn't generally part of company's "cloud strategy" documents.  And yet, it probably has just as sensitive data and information as your data center does, especially if you are talking sales leads, customer contact information and case management.

But security advice for SaaS tooling is almost non existent.  Both for vendors, in how they should do access control, management or reporting, and also for consumers in what to look for and what tools, capabilities and policies you might need.

The Jira bug is the sort of thing that will occur time and time again, where it's possible to open stuff up to the world, and not clear to users how that happened or the implications there of.  

We need better standards for things like API's to enable policy compliance checks and automated scanning. Standards allowing for the download of access logs and authentication and audit logs would make detection of these things easier.  Until we have those, we are reliant on the good practices of both the vendors of SaaS tools, and the users within our organisation of configuring and using these tools correctly

## ['You've caused an international incident': how my work mistake came back to haunt me | Film | The Guardian](https://www.theguardian.com/film/2019/jul/27/international-incident-work-mistake-official-secrets-film?CMP=share_btn_tw)

[https://www.theguardian.com/film/2019/jul/27/international-incident-work-mistake-official-secrets-film?CMP=share_btn_tw](https://www.theguardian.com/film/2019/jul/27/international-incident-work-mistake-official-secrets-film?CMP=share_btn_tw)

> Towards the end of my second week, I was handed a printout of an email by Martin Bright (then the Observer’s home affairs editor, played in Official Secrets by Matt Smith) and Peter Beaumont (the foreign affairs editor – played by Matthew Goode). Could I type it up and save it into the system? I wasn’t given any other information. Their only instruction: “Don’t make any mistakes.” And so I set to painstakingly typing in each sentence.
> 
> Importance HIGH
> Top Secret


This is a great story of how little mistakes can happen and the background to a significant news story about leaking.

But it's also an insight into just how cavalier journalists are with sensitive information.  Got a Top Secret document that you need written up?  Why not give it to someone who has been in the organisation for 2 weeks, you therefore hardly know, and no idea what they'll do with it.

It does make you wonder just how protected the large trove of Snowdon files actually was / is. 

[Full Disclosure: I worked at the Guardian at the time of the Snowdon leaks, but was not involved in the reading/reporting of them]


## [REPORT OF THE SELECT COMMITTEE ON INTELLIGENCE UNITED STATES SENATE ON RUSSIAN ACTIVE MEASURES CAMPAIGNS AND INTERFERENCE IN THE 2016 U.S. ELECTION VOLUME 1: RUSSIAN EFFORTS AGAINST ELECTION INFRASTRUCTURE WITH ADDITIONAL VIEWS [pdf]](https://assets.documentcloud.org/documents/6214170/Senate-Intel-Report-On-Election-Interference.pdf)

[https://assets.documentcloud.org/documents/6214170/Senate-Intel-Report-On-Election-Interference.pdf](https://assets.documentcloud.org/documents/6214170/Senate-Intel-Report-On-Election-Interference.pdf)

>  In June 2016, Illinois experienced the first known breach by Russian actors of state
> election infrastructure during the 2016 election. As of the end of 2018, the Russian cyber
> actors had successfully penetrated Illinois's voter registration database, viewed multiple database
> tables, and accessed up to 200.000 voter registration records. The compromise resulted in the
> exfiltration of an unknown quantity of voter registration data. Russian cyber actors were in a
> position to delete or change voter data, but the Committee is not aware of any evidence that thev
> did so.
> 
> [...]
> 
> Further, DHS staff noted that "the level of access that they gained, they almost certainly
> could have done more. Why they didn't... is sort of an open-ended question. I think it
> fits under the larger umbrella of undermining confidence in the election by tipping their
> hand that they had this level of access or showing that they were capable of getting it."


An interesting assumption of motive, when the clearer more obvious motive may have simply been to collect and collate as much personal data as possible.


## [THE WAR ON PINEAPPLE: Understanding Foreign Interference in 5 Steps [pdf]](https://www.dhs.gov/sites/default/files/publications/19_0717_cisa_the-war-on-pineapple-understanding-foreign-interference-in-5-steps.pdf)

[https://www.dhs.gov/sites/default/files/publications/19_0717_cisa_the-war-on-pineapple-understanding-foreign-interference-in-5-steps.pdf](https://www.dhs.gov/sites/default/files/publications/19_0717_cisa_the-war-on-pineapple-understanding-foreign-interference-in-5-steps.pdf)

> To date, we have no evidence of Russia (or any nation) actively carrying out information operations against pizza toppings.
> This infographic is an ILLUSTRATION of how information operations have been carried out in the past to exploit divisions in
> the United States. 


I mean, I can totally understand why we might want a campaign to ensure that everyone understands how delicious pineapple is on pizza!

This is a great infographic explaining how disinformation campaigns work.  If you did the disinformation game from a few weeks ago, this should all be familiar to you, and if not, go back and give that a try


## [Snapchat Snapcode Protocol](https://n0.lol/a/snapcodes.html)

[https://n0.lol/a/snapcodes.html](https://n0.lol/a/snapcodes.html)

> This snapcode was created to test the functionality of launching intents  via Snapchat.
> 
> When opening a URL within a snapcode, the Snapchat internal browser handles the page rendering. You can call other apps on the device with URIs, and in the case of Android, intents. 
> 
> The following code is used on the page to detect if an android phone is  accessing the page, and if so, launch Chrome with another page.


This is a cute attack.  Snapcodes are QR codes, but they can contain URL's which the browser goes to, and that browser can be told to abuse the Android intents system to make users phones do other things, like redirect to the market place.

You can imagine publishing a piece of malware disguised as an app for a popular band or celebrity, and then sticking snapchat QR codes onto posters at a conference, and people would gladly and happily download the application.


## [Cyberlaw wonks squint at NotPetya insurance smackdown: Should 'war exclusion' clauses apply to network hacks? - The Register](https://www.theregister.co.uk/2019/07/26/do_insurance_war_exclusion_clauses_apply_to_cyberattacks/)

[https://www.theregister.co.uk/2019/07/26/do_insurance_war_exclusion_clauses_apply_to_cyberattacks/](https://www.theregister.co.uk/2019/07/26/do_insurance_war_exclusion_clauses_apply_to_cyberattacks/)

> Zurich rejected the claim, simply referring to a single policy exclusion which does not cover "hostile or warlike action in time of peace or war" by "government or sovereign power; the military, naval, or air force; or agent or authority".
> [...]
> US food giant Mondelez – the parent firm of Oreo cookies and Cadburys chocolate – which is now suing insurance company Zurich American for denying a £76m claim (PDF) filed in October 2018, a year after the NotPetya attack.


(Joel) Previous CyberWeekly issues [#38](https://cyberweekly.net/digital-transformation-is-hard) and [#57](https://cyberweekly.net/malware-is-still-your-biggest-threat) touched on multiple insurers denying cyber breach related claims under “Act of War” exemptions as the wider situation (such as the malware strain) had been attributed by the local government to a foreign government.

“Act of War” exemptions are fairly common in general insurances but the attribution of cyber attacks with limited declassified evidence combined with the non-physical nature of the attack poses an interesting legal debate.

The lawyers agree. The insurer Zurich is being sued for denying a £76mil 2018 claim stemming from a US company’s losses after NotPetya.

I expected this to make no difference to how and when attribution is declared. This will however form very interesting case law and could see insurers raising cyber insurance premiums and/or defining much stricter requirements for payouts to apply - for example: if malware can propagate and infect 1,700 servers and 24,000 laptops within a single organisation it could mean the claimant is denied on the basis that they did not implement reasonable ‘minimum’ measures to [prevent lateral movement](https://www.ncsc.gov.uk/guidance/preventing-lateral-movement).


## [BlueKeep RDP Vulnerability (CVE-2019-0708) Activity in the Wild](https://blog.rapid7.com/2019/07/31/bluekeep-cve-2019-0708-for-windows-rdp-what-you-need-to-know/)

[https://blog.rapid7.com/2019/07/31/bluekeep-cve-2019-0708-for-windows-rdp-what-you-need-to-know/](https://blog.rapid7.com/2019/07/31/bluekeep-cve-2019-0708-for-windows-rdp-what-you-need-to-know/)

> Figure 1 shows the total daily connections from known, non-benign sources. Current levels of malicious RDP activity are levels unseen since Rapid7 Labs deployed Project Heisenberg back in 2015 and are well above the levels seen at this same time last year.
> 
> There were spikes just before the release of the CVE from both known adversarial internet IPv4 ranges and new sources that have a scanning profile consistent with nation state vulnerability assessment activity (those are not marked as “benign”).


This is actually about the rise in RDP scanning, which could lead to BlueKeep exploitation, but as outlined further down in the article, much of this activity is simply reconnaissance activity, designed to find accessible RDP servers.  That has led to normal style attacks, traditional RDP exploits on older RDP installations, as well as credential stuffing attacks.

There still are no working BlueKeep exploits available to the general population, but it's probably safe to assume that nation state level attackers as well as any suitably advanced reverse engineering team has access to this exploit.

There will be a metasploit module available within the month, especially given its Blackhat and DefCon season.

The patch has been available for around 3 months, so you really should have applied it by now to all internet accessible RDP servers, and hopefully across your entire estate by now.


## [S3 Bucket Namesquatting - Abusing predictable S3 bucket names – One Cloud Please](https://onecloudplease.com/blog/s3-bucket-namesquatting)

[https://onecloudplease.com/blog/s3-bucket-namesquatting](https://onecloudplease.com/blog/s3-bucket-namesquatting)

> A common practice in AWS is to use files in an S3 bucket that is also located in the region. Sometimes this is for latency reasons and sometimes you don’t have a choice in the matter. The S3Bucket property of a Lambda function in a CloudFormation template for example requires the bucket be in the same region as the function.
> 
> S3 also has a global namespace which means bucket names cannot be reused in other regions or by other accounts. This means that services which are deployed in many regions generally have a standard way of naming their buckets, usually by using the region name as a prefix or suffix to another string. When setting these up, a developer will generally register all buckets which match the pattern in their respective regions and make a note to additionally register new buckets as new regions are launched.
> 
> If someone has both prior knowledge of both the pattern being used for the bucket registration and of an upcoming region name, they could claim that bucket as their own before the owner of the other buckets has a chance to.
> 
> [...]
> 
> In order to specify the source for the Lambda function, they previously used an intrinsic function in the form:
> 
> "Code": {
>   "S3Bucket": {"Fn::Join": ["", ["appdevzipfiles-", { "Ref" : "AWS::Region" }] ] },
>   "S3Key": "cloudwatchlogs-with-dlq.zip"
> }


This is fascinating security implication of a "feature".  There's some interesting thoughts about whether your cloudformation or otehr infrastructure as code systems fail if they go to create a resource and it already exists.

If you fail to create a bucket, but it exists, and you can send logs to it and read them back, do you stop and worry about whether you are the only person with access?

In the case of this SumoLogic function, their Lambda function cannot check for the ownership of the resource, because it's yours, so this feels like it could catch people easily.


## [THE THREAT OF ONLINE SKIMMING TO PAYMENT SECURITY [pdf]](https://www.pcisecuritystandards.org/pdfs/PCISSC_Magecart_Bulletin_RHISAC_FINAL.pdf)

[https://www.pcisecuritystandards.org/pdfs/PCISSC_Magecart_Bulletin_RHISAC_FINAL.pdf](https://www.pcisecuritystandards.org/pdfs/PCISSC_Magecart_Bulletin_RHISAC_FINAL.pdf)

> Securing of third-party infrastructure and restricting access and permissions of third-party scripts to only
> trusted sources is also essential. Merchants should clearly identify the specific PCI DSS requirements
> covered by the service provider, and any requirements that are the responsibility of the service provider’s
> customers to implement. Organizations should actively monitor for and block attempts to introduce
> malicious code on to their e-commerce space. Permitting externally hosted JavaScript or Cascading Style
> Sheets (CSS) on payment acceptance pages should not be allowed. Where feasible, transitioning from
> using third-party hosted scripts to using internally hosted copies of third-party scripts could significantly
> decrease the risk of malicious modification. Third party scripts should be monitored to detect changes and
> the changes be reviewed to identify any potentially malicious code before implementation. Using content
> security policies (CSP) to restrict compliant browsers from executing JavaScript from sources which have
> not been explicitly whitelisted is also an added protection that should be incorporated.


The PCI Security and Standards Council have issued a notice to tell people to watch out for Magecart style attacks.  Given that the BA Magecart attack happened nearly a year ago (August 21st through September 6th 2019), it's about time.

The advice has some good tips in it, but falls down in a few areas.  For detection, it talks about doing code review on the code, but the magecart infections were changes to the compressed and obfuscated javascript.  Manual code review wouldn't have helped.
Self hosting the code wouldn't necessarily help either, BA had self hosted code (although outside of PCI scope).  Content Security Policies are almost certainly your best bet


## [Capital One Breach Does Not Mean the Cloud is Insecure | Decipher](https://duo.com/decipher/capital-one-breach-does-not-mean-the-cloud-is-insecure)

[https://duo.com/decipher/capital-one-breach-does-not-mean-the-cloud-is-insecure](https://duo.com/decipher/capital-one-breach-does-not-mean-the-cloud-is-insecure)

> The thing is, Capital One wasn't wrong. The cloud provides a lot of security benefits, such as the fact that software and hardware gets updated with security fixes much faster than if the enterprise had to handle its own testing and deployment schedule. The cloud provider typically has a broader view of threats that may come into the network, so securing one customer means all other customers also benefit.
> 
> “[The] cloud is still orders of magnitude safer and more secure than when data was stored on premise,” said Michael Clauser, global head of data and trust at public policy firm Access Partnership. “This wasn’t a failure of the cloud, but of personnel.”
> 
> Moving to the cloud typically involves changing security controls and processes. The security controls that worked in the data center is typically not going to be enough in a cloud environment, because the infrastructure and the rules of acccessibility are completely different. Even migrating an application isn't the same as just copying the code over because the security layers have to change. Security needs to be rethought in the context of the cloud, and that is usually the hardest part of any migration.


This is the most sensible take on the Capital One breach that I saw.

Capital One had an S3 bucket that contained a lot of credit card application data, around 14 years worth, which was read accessible to one of Capital One's WAF AWS role.  It probably should not have had access to that data (although there might be reasons, such as an extranet for data science that make it reasonable).

This is the failure of process, rather than a systemic issue, and of course, the cloud is probably more secure generally than data centers, but you are still need to do security, and the security actions you take need to be different to how you secure a data center.


## [Bitglass 2019 Cloud Security Report: Only 20 Percent of Organizations Use Cloud Data Loss Prevention Despite Storing Sensitive Information in the Cloud | Business Wire](https://www.businesswire.com/news/home/20190717005003/en/Bitglass-2019-Cloud-Security-Report-20-Percent)

[https://www.businesswire.com/news/home/20190717005003/en/Bitglass-2019-Cloud-Security-Report-20-Percent](https://www.businesswire.com/news/home/20190717005003/en/Bitglass-2019-Cloud-Security-Report-20-Percent)

> “Data is now being stored in more cloud apps and accessed by more devices than ever before,” said Rich Campagna, chief marketing officer of Bitglass. “This report found that 93 percent of respondents are at least moderately concerned about their ability to use the cloud securely, and that the adoption rates of basic cloud security tools and practices are still far too low. Many organizations need to rethink their approach to protecting data, as traditional tools for safeguarding data on premises are not capable of protecting data in the cloud.”


Cloud security access broker company reinforces their belief that people need new cloud security tools when migrating to the cloud.  Interestingly, I don’t see the same thing.  The top concerns for executives moving to the cloud interestingly are cost, cloud native readiness and ease of deployment.  

Cloud access brokers are interesting tools for bridging the gap between the old and the new, but modern greenfield estates shouldn’t generally need them because they can use cloud identity systems instead.  Where Cloud Access Brokers could be useful is in negotiating access to SaaS tools, but not many are supported by the leading cloud access brokers, and it tends to come as a premium addon to most SaaS tools as well.


## [One Misconfig (JIRA) to Leak Them All- Including NASA and Hundreds of Fortune 500 Companies!](https://medium.com/@logicbomb_1/one-misconfig-jira-to-leak-them-all-including-nasa-and-hundreds-of-fortune-500-companies-a70957ef03c7)

[https://medium.com/@logicbomb_1/one-misconfig-jira-to-leak-them-all-including-nasa-and-hundreds-of-fortune-500-companies-a70957ef03c7](https://medium.com/@logicbomb_1/one-misconfig-jira-to-leak-them-all-including-nasa-and-hundreds-of-fortune-500-companies-a70957ef03c7)

> In Jira, while creating filters or dashboards it provides some visibility option to apply to them. The issue was due to the wrong permissions assigned to them. When the filters and dashboards for the projects/issues are created in JIRA, then by default the visibility is set to “All users” and “Everyone” respectively, which instead of sharing with everyone of the organizations (which people think and interpret), it share them publically. 


Searching for misconfigured Jira instances, where users don't realise that "Everyone" visibility doesn't just mean everyone in the organisation.

There is no easy way to find all of the jira boards that everyone in your company uses, and so auditing this internally is almost impossible.


