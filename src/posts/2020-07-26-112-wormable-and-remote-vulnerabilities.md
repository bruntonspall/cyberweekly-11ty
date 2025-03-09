---
title: "112 - Wormable and remote vulnerabilities"
date: 2020-07-26
description: "There’s a big new vulnerability and you should either be really scared, or a little scared depending which articles you read."
permalink: /wormable-and-remote-vulnerabilities/
---

There’s a big new vulnerability and you should either be really scared, or a little scared depending which articles you read.

You can read more below, and my advice is that you should be making sure that you have patched your internal DNS servers if they are running Windows.  Actually scratch that, you should be keeping your internal DNS servers and other network service devices patched all the time regardless!

But what does it mean that this is an RCE or Wormable vulnerability?

In essence, your DNS servers sit on your network and listen for incoming traffic from other locations on the network.  If you are running your own external DNS servers (don’t do this!), you might have separated the external facing ones from the internal ones, “for security”.  

The Remote Code Execution means that anybody who can talk to the server can execute code, as if they were in control of the software.  Since this is system software, it means that in most cases, they have complete control of the computer, without needing usernames, passwords or anything more complex.  

But worse, this one is wormable, because just the same way that a worm burrows underground, our networks are often interconnected, and the things that interconnect them are often the networking infrastructure such as DNS servers.  So if you’ve got external DNS servers, there’s a very good possibility that they are allowed to talk DNS to internal DNS servers.  So a remote user can target and take over your external servers, and then burrow through them and your network and take over your internal DNS servers.

Even worse, if you have multiple networks, multiple sites, or you have a managed service provider who runs your DNS servers for you, there’s a very very strong possibility that this exploit could be used to burrow from site to site, over VPNs, between Managed Service Provider’s tenant and so on.

Wormable exploits are some of the scariest, and of course, the [Morris Worm](https://en.wikipedia.org/wiki/Morris_worm) was one of the first major internet outages, back in 1981, with a similar vulnerability but that time through the mail transmission agent, SendMail.  The thing that made that worse was that Robert Morris Jr wrote code that when it infected a machine, scanned for more machines to infect and replicated itself to target them.  It was this replication that actually caused the crash and the majority of the damage on the internet at the time.

Wannacry was of course, the most recent wormable exploit, using the BlueKeep vulnerability to spread around networks.  We were only partially affected because it had a built in killswitch which when triggered made it inert.

I don’t think this will be anywhere nearly as bad, because the number of Windows DNS servers on networks is low as a proportion of systems.  Many corporations run them on their internal networks, but the interconnectedness isn’t there the way that mail servers were, and Wannacry exploited SMB which was enabled on many network servers.  So this likely won’t be quite as serious, but anytime we hear about a vulnerability like this, it’s one that we should take seriously.

So make sure you’ve applied the patches or work arounds, and ensure your networks are appropriately segregated to prevent DNS traffic that isn’t intended to cross network boundaries.

## [Dangerous Skills Got Certified: Measuring the Trustworthiness of Amazon Alexa Platform: Experiment Results](https://vpa-sec-lab.github.io/experimentresults.html)

[https://vpa-sec-lab.github.io/experimentresults.html](https://vpa-sec-lab.github.io/experimentresults.html)

> Our results showed strong evidence that Alexa's skill certification process is implemented in a disorganized manner. We were able to publish all 234 skills that we submitted although some of them required a resubmission.
> 
> Surprisingly, we successfully certified 193 skills on their first submission. 41 skills were rejected. Privacy policy violations were the issue specified for 32 rejections while 9 rejections were due to UI issues. For the rejected submissions, we received certification feedback from the Alexa certification team stating the policy that we broke. On resubmission we were able to get all the 234 skills certified.
> 
> Some live skills that have been published in the skills store are shown below.


This isn’t a good look for Amazon Alexa (and they noted that other voice assistant vendors had similar issues).  

The fact that, unlike mobile apps, once a skill is installed on a device, the backend code is held on the vendors servers makes it impossible for the Alexa team to actually vet that the code hasn’t changed.  It’s hard enough to vet appstore apps, but code you can’t see or modify is impossible to effectively vet.

However, some of these issues, such as asking for personal information without a privacy policy or including adverts even though it’s labelled as non-commercial is stuff that should be more thoroughly checked.


## [Ongoing Meow attack has nuked >1,000 databases without telling anyone why | Ars Technica](https://arstechnica.com/information-technology/2020/07/more-than-1000-databases-have-been-nuked-by-mystery-meow-attack/)

[https://arstechnica.com/information-technology/2020/07/more-than-1000-databases-have-been-nuked-by-mystery-meow-attack/](https://arstechnica.com/information-technology/2020/07/more-than-1000-databases-have-been-nuked-by-mystery-meow-attack/)

> Besides amounting to a serious privacy breach, the database was at odds with the Hong Kong-based UFO’s promise to keep no logs. The VPN provider responded by moving the database to a different location but once again failed to secure it properly. Shortly after, the Meow attack wiped it out.
> 
> Representatives of UFO didn’t immediately respond to an email seeking comment.
> 
> Since then, Meow and a similar attack have destroyed more than 1,000 other databases. At the time this post went live, the Shodan computer search site showed that 987 ElasticSearch and 70 MongoDB instances had been nuked by Meow. A separate, less-malicious attack tagged an additional 616 ElasticSearch, MongoDB, and Cassandra files with the string “university_cybersec_experiment.” The attackers in this case seem to be demonstrating to the database maintainers that the files are vulnerable to being viewed or deleted.


Sigh, I read this and knew that it would be ElasticSearch and MongoDB.  The fact that neither shipped with any sensible authentication turned on by default continues to be a problem for lots of organisations.  This is compounded by the fact that they are very easy to run and deploy without specialist skills, so dev teams may well be using them without permission and without good infrastructure knowledge.


## [The European Court of Justice has ruled that Privacy Shield is invalid | WIRED UK](https://www.wired.co.uk/article/privacy-shield-ruling)

[https://www.wired.co.uk/article/privacy-shield-ruling](https://www.wired.co.uk/article/privacy-shield-ruling)

> The ruling handed down by the highest court of EU law is complex, but those who brought the case will hope this victory forces the European Commission to introduce more safeguards to protect European data handled when it is handled and processed by American companies. As part of the same ruling, the Court also decided that another data transfer mechanism, Standards Contractual Clauses, or SSCs, remain valid.
> 
> After Safe Harbour’s abrogation, US firms switched to a different, EU-approved template to transfer EU data to company servers in the US, known as standard contractual clauses, or SCCs. “SCCs were the main route to transferring data once there were questions about the Safe Harbour regime,” says Lorna Woods, a law professor at the University of Essex. Those SCCs, the ECJ has ruled, are still valid.
> 
> A new data transfer agreement replacing Safe Harbour – called the EU-US Privacy Shield – was created in 2016 between the EU and US. The Privacy Shield restricts the US government from accessing EU citizens’ data, adds provisions for EU citizens to refer complaints to a regulator and requires that companies who wish to transfer data to a third party must ensure that the third party also follows the Privacy Shield principals.
> 
> As Facebook and other companies began using SCCs to transfer data to the US, Schrems submitted a new complaint to the Irish Data Protection Commissioner, this time challenging Facebook’s use of SCCs to transfer data. Once again, it was referred to the Irish High Court and then up to the ECJ. While the Privacy Shield wasn’t part of Schrems’ initial complaint, the Irish Court’s request pulled the Privacy Shield into the case as well.


I can’t work out if this is a big deal or not.  As Wired outlines, many companies are already using SCC’s, which the court did not find in breach.  I can’t quite work out what the difference is between the use of SCC’s and the Privacy Shield, but I suspect it’s something to do with the willing and deliberate act to agree to SCC’s that makes it more watertight.

Expect a lot of noise about this one, but I don’t think this is going to affect too many people just yet.  All of the big cloud infrastructure vendors, and most of the cloud software and social networking vendors are using SCC’s, but if you are responsible for privacy, you might need to double check on your vendors and make sure none were simply reliant on Privacy Shield (or it’s predecessor SafeHarbour).


## [ISC_Russia_Report](https://docs.google.com/a/independent.gov.uk/viewer?a=v&pid=sites&srcid=aW5kZXBlbmRlbnQuZ292LnVrfGlzY3xneDo1Y2RhMGEyN2Y3NjM0OWFl)

[https://docs.google.com/a/independent.gov.uk/viewer?a=v&pid=sites&srcid=aW5kZXBlbmRlbnQuZ292LnVrfGlzY3xneDo1Y2RhMGEyN2Y3NjM0OWFl](https://docs.google.com/a/independent.gov.uk/viewer?a=v&pid=sites&srcid=aW5kZXBlbmRlbnQuZ292LnVrfGlzY3xneDo1Y2RhMGEyN2Y3NjM0OWFl)

> 


This is worth a direct read if you are into such things.  It’s reasonably short and readable


## [The Essential List of Top SRE Resources](https://www.blameless.com/blog/top-sre-resources)

[https://www.blameless.com/blog/top-sre-resources](https://www.blameless.com/blog/top-sre-resources)

> Are you looking to get up to speed on SRE fundamentals with the best SRE books and best DevOps books? Or are you hoping to expand your SRE knowledge into new domains? Either way, we’ve got you covered in our list of essential SRE resources!


This is a good list of resources if you need to know more about SRE, how to do it, what it is, and what impact it will have.  Some of these are for practitioners, and many are also suitable for managers who might be thinking of implementing an SRE or Platform Operations team within their organisation.


## [OWASP SEDATED®](https://owasp.org/www-project-sedated/)

[https://owasp.org/www-project-sedated/](https://owasp.org/www-project-sedated/)

> The SEDATED® Project (Sensitive Enterprise Data Analyzer To Eliminate Disclosure) focuses in on preventing sensitive data such as user credentials and tokens from being pushed to Git. Developers are constantly pushing changes to GitHub and will most likely eventually try pushing a commit that contains sensitive information and we want to help catch and prevent that. The SEDATED® application will run on the Git server and review all incoming code changes. If it identifies sensitive data it will reject the push otherwise it will allow it.


If you weren’t already using one of the existing secret scanning tools, this is the newest on the block.  It searches for commits to your source tree that fits known patterns for private keys, passwords and other secrets that shouldn’t be committed to your repository.

Sadly, as it stands, I believe that only GitHub enterprise supports pre-commit hooks and tools, so if you are using Github in the normal licensed fashion for your development team, I don’t believe that this nor other pre-commit scanning tools will work out of the box... yet.


## [Introducing the State of Open Source Terraform Security Report](https://bridgecrew.io/blog/state-of-open-source-terraform-security-report-2020/)

[https://bridgecrew.io/blog/state-of-open-source-terraform-security-report-2020/](https://bridgecrew.io/blog/state-of-open-source-terraform-security-report-2020/)

> In our State of Open Source Terraform Security Report, we analyze the public Terraform Registry which contains thousands of open source modules used to provision cloud resources. Leveraging our open-source static analysis tool Checkov, we scanned the Registry to gauge compliance of modules across categories and cloud providers.
> 
> Read the full the report here to dig into some of our top findings:
> 
> Nearly 1 in 2 modules used to build resources for AWS, Azure, and Google Cloud is misconfigured.
> Misconfigured modules have been downloaded over 15 million times since 2017.
> Q2 2020 had the highest quarter-over-quarter module growth and an increase in misconfigurations.


Configuration as code is something I constantly tell people will make them more secure.  But it also adds new risks, that your code configured your system insecurely. 

The advantage is that you can use tools, such as BridgeCrew’s Checkov to audit your code easily and simply.  Doing that to production systems that are all hand configured is far harder.

However, the key thing to recognise here is that not all open source modules for your configuration as code systems are maintained, up to date or necessarily secure.  You have a responsibility to validate that stuff as well as just use it.


## [Microsoft Azure Well-Architected Framework - Microsoft Azure Well-Architected Framework introduction | Microsoft Docs](https://docs.microsoft.com/en-us/azure/architecture/framework/)

[https://docs.microsoft.com/en-us/azure/architecture/framework/](https://docs.microsoft.com/en-us/azure/architecture/framework/)

> Think about security throughout the entire lifecycle of an application, from design and implementation to deployment and operations. The Azure platform provides protections against a variety of threats, such as network intrusion and DDoS attacks. But you still need to build security into your application and into your DevOps processes.
> 


Identity, cloud administration, app security and data sovereignty. That’s the core set of things to worry about for your cloud platform. I pretty much agree with that. 


## [Wattpad data breach exposes account info for millions of users](https://www.bleepingcomputer.com/news/security/wattpad-data-breach-exposes-account-info-for-millions-of-users/)

[https://www.bleepingcomputer.com/news/security/wattpad-data-breach-exposes-account-info-for-millions-of-users/](https://www.bleepingcomputer.com/news/security/wattpad-data-breach-exposes-account-info-for-millions-of-users/)

> Since July 7th, BleepingComputer has been tracking the rumored private sale of a Wattpad database containing over 200 million records.
> 
> In an anonymous tip, BleepingComputer was told that this database was being sold by Shiny Hunters, a group known for selling company databases acquired in data breaches.
> 
> At the time, Cyber intelligence firm Cyble told BleepingComputer that this database was being sold for ten bitcoins, or almost $100,000 at the time.
> 
> BleepingComputer contacted Shiny Hunters about this breach, and at first, they were concerned about how we knew about the sale, and then later denied having anything to do with it.
> 
> A few sample records of this database seen by BleepingComputer contain user names, names, hashed passwords, email addresses, and general geographic location.
> 
> BleepingComputer contacted the users in this sample, and one user confirmed with BleepingComputer that the listed information was accurate.


That’s a big looking breach, complete with passwords (encrypted naturally, but we know how good password complexity and hygiene is).


## [Detecting DNS CVE-2020–1350 exploitation attempts in Azure Sentinel | by Kevin Beaumont | Jul, 2020 | DoublePulsar](https://doublepulsar.com/detecting-dns-cve-2020-1350-exploitation-attempts-in-azure-sentinel-1f2efb26422e)

[https://doublepulsar.com/detecting-dns-cve-2020-1350-exploitation-attempts-in-azure-sentinel-1f2efb26422e](https://doublepulsar.com/detecting-dns-cve-2020-1350-exploitation-attempts-in-azure-sentinel-1f2efb26422e)

> I recently expanded this out to CVE-2020–1350, a DNS vulnerability detailed a few weeks ago. BluePot has detected no active exploitation in the wild, outside of my initial testing.
> 
> It is possible to alert on DNS exploitation attempts for this vulnerability using Azure Sentinel, on Windows Server 2008 and above. The process for implementing this involves enabling DNS debug logs (if not already enabled), adding a Custom Log and adding alert rules.
> 
> Azure Sentinel is a ‘cloud native’ (read: easy to actually implement) security monitoring and event management solution, for those who haven’t used it, with prebaked advanced threat hunting from the folks at Microsoft.


CVE-2020-1350 is a big scary bug, as outlined above.  

This is a nice writeup by GossiTheDog on how to detect attempts to exploit this on your network using Azure Sentinel.  Even if you’ve patched, you should definitely be looking for this traffic on your network.  Any signs of it means that you have someone attempting to exploit it on your network.


## [CVE-2020-1350: Critical vulnerability in Windows DNS servers | Kaspersky official blog](https://www.kaspersky.com/blog/cve-2020-1350-dns-rce/36366/)

[https://www.kaspersky.com/blog/cve-2020-1350-dns-rce/36366/](https://www.kaspersky.com/blog/cve-2020-1350-dns-rce/36366/)

> Bad news: The vulnerability scored 10 on the CVSS scale, which means it’s critical. Good news: Cybercriminals can exploit it only if the system is running in DNS server mode; in other words, the number of potentially vulnerable computers is relatively small. Moreover, the company has already released patches and a workaround.


This one is a big deal, go patch this and then come back. 

The exploit can be conducted remotely from the server, so any attacker who can send DNS queries to your windows DNS server can execute code, and it does so in the local system administrator account, so has total local control over the server.

This means that if someone compromises the server, they can almost certainly look across the network for more to compromise, and/or run mimikatz and other tools to extract more privileged domain admin accounts from the machine.

Of course, most people don’t have many Windows DNS servers, but the really bad news is that it’s not that uncommon on the networks I’ve seen for machines like this to be multi-role, so this may well be the domain controller, or backup domain controller, which means game over for you.

Even if it’s not, the DNS server for a network is often fairly privleged and of course almost always requires access out to the internet, so it makes a perfect CommandAndControl C2 server.

The only good news is that most companies don’t host their external DNS using their own Windows infrastructure, they use a third party DNS system to do it for them.  That means that this is likely a critical vulnerability to attackers already inside your network rather than a means of entry.

Patch this one, and patch this now.


