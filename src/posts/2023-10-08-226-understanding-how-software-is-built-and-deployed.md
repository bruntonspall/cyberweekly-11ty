---
title: "226 - Understanding how software is built and deployed"
date: 2023-10-08
description: "Something that seems quite common is a bit of a rose tinted view of how software is built and deployed in many organisations."
permalink: /understanding-how-software-is-built-and-deployed/
---

Something that seems quite common is a bit of a rose tinted view of how software is built and deployed in many organisations.

Those people coming from a software development team background tend to assume that there's developer control over some monolithic (or microlithic) system, which is all developed and controlled in house.  Where there are external supply chain style dependencies is in the software dependency systems, or with API integrations.  People who work in this sort of ecosystem really care about SBOM's, repeatable builds, configuration as code and so on.  To them, the idea of shipping software with default configurations is really confusing because everything is custom built.  These are the people worrying about the base images in their docker builds or the security of their kubernetes clusters.  This is the reality in a modern tech company, in Google, in Meta, in any of the tech firms that have determined that software development capability is a core competency that they need.  If you go to a tech conference, these are the people on stage talking about how to build and secure your systems.

But it's one specific end of the technology spectrum and sometimes it's presence acts with it's own gravity, warping the advice and guidance that we give to companies.

At the other end of the spectrum, some organisations have a technology department that is filled with project managers, solutions architects and enterprise architects.  Most of these have never written a line of code, instead their job is to buy the right tool to do the right job.  The project managers spend their times ensuring that the systems are installed correctly, that the users are trained and that data is appropriately migrated from whatever old system to whatever new system is being put together.

But the critical difference is that these latter systems are put together rather than developed.  Often made up of components purchased off the shelf, these systems are often composed together by consultants, who configure the software according to the manufacturers guidelines.  It's these cobbled together IT systems that make up the vast bulk of technology systems in companies today, and exactly these kinds of systems that end up having default configurations, hard coded passwords and deployed into flat networks.

When you stop and think about people in those jobs, how actionable is the advice to have segmented networks or use MFA for their admin accounts.  In many cases, the work of assembling the system was outsourced, and it's highly likely that no one person actually knows how it all works.  The knowledge is spread around all around a number of companies and people, and the ability to collaborate is restricted by commercial non-compete clauses, non-disclosure agreements or in some cases, just pure "not my problem" approaches.  Some of these companies don't make huge profits, feel squeezed on all contracts, and as such, if it's not chargeable, it's highly unlikely to happen.

When we think about securing the enterprise, we need to remember that for most organisations, IT is not a core competency that enables them to compete with their competition.  IT is often outsourced, and overseen by overworked and under-resourced teams.  Our advice and support on how to secure the enterprise needs to be put in this context.

## [JOINT_CSA_TOP_TEN_MISCONFIGURATIONS_TLP-CLEAR.PDF ](https://media.defense.gov/2023/Oct/05/2003314578/-1/-1/0/JOINT_CSA_TOP_TEN_MISCONFIGURATIONS_TLP-CLEAR.PDF)

[https://media.defense.gov/2023/Oct/05/2003314578/-1/-1/0/JOINT_CSA_TOP_TEN_MISCONFIGURATIONS_TLP-CLEAR.PDF](https://media.defense.gov/2023/Oct/05/2003314578/-1/-1/0/JOINT_CSA_TOP_TEN_MISCONFIGURATIONS_TLP-CLEAR.PDF)

> Through NSA and CISA Red and Blue team assessments, as well as through the
> activities of NSA and CISA Hunt and Incident Response teams, the agencies identified the following 10 most common network misconfigurations:
> 
> 1. Default configurations of software and applications
> 2. Improper separation of user/administrator privilege
> 3. Insufficient internal network monitoring
> 4. Lack of network segmentation
> 5. Poor patch management
> 6. Bypass of system access controls
> 7. Weak or misconfigured multifactor authentication (MFA) methods
> 8. Insufficient access control lists (ACLs) on network shares and services
> 9. Poor credential hygiene
> 10. Unrestricted code execution
> 
> These misconfigurations illustrate (1) a trend of systemic weaknesses in many large
> organizations, including those with mature cyber postures, and (2) the importance of
> software manufacturers embracing secure-by-design principles to reduce the burden on network defenders:
> 
> * Properly trained, staffed, and funded network security teams can implement the
> known mitigations for these weaknesses
> * Software manufacturers must reduce the prevalence of these
> misconfigurations—thus strengthening the security posture for customers—by
> incorporating secure-by-design and -default principles and tactics into their
> software development practices.[1]
> 
> NSA and CISA encourage network defenders to implement the recommendations found within the Mitigations section of this advisory—including the following—to reduce the risk of malicious actors exploiting the identified misconfigurations.
> 
> * Remove default credentials and harden configurations.
> * Disable unused services and implement access controls.
> * Update regularly and automate patching, prioritizing patching of known exploited
> vulnerabilities.[2]
> * Reduce, restrict, audit, and monitor administrative accounts and privileges. 


This was an interesting release, because it was jumped on by a lot of media around “There’s a few things we can do”, but in reality lots of these issues are indicative of struggles within organisations between responsibilities between silos.

The sad reality of IT in many organisations is that business units or teams might go out to contract for a system that’s built by one organisation, operated by a second, maintained and patched by a third, and no one person is responsible for the overall system.  That results in people making assumptions, such as providing a system with default configurations because they assume that the operating party will apply their operational configuration.

Almost all of these issues are ones that are hard for an individual software vendor to fix, as almost all are in fact “integration issues”, which is where the rubber hits the road. 


## [Ransomware attack on MGM Resorts cost $110 Million ](https://securityaffairs.com/152077/cyber-crime/mgm-resorts-ransomware-attack.html)

[https://securityaffairs.com/152077/cyber-crime/mgm-resorts-ransomware-attack.html](https://securityaffairs.com/152077/cyber-crime/mgm-resorts-ransomware-attack.html)

> “The Company believes that the operational disruption experienced at its affected properties during the month of September will have a negative impact on its third quarter 2023 results, predominantly in its Las Vegas operations, and a minimal impact during the fourth quarter. The Company does not expect that it will have a material effect on its financial condition and results of operations for the year. Specifically, the Company estimates a negative impact from the cyber security issue in September of approximately $100 million to Adjusted Property EBITDAR for the Las Vegas Strip Resorts and Regional Operations, collectively.” reads the [8-K report](https://d18rn0p25nwr6d.cloudfront.net/CIK-0000789570/578d9c03-dcfb-4e79-8d21-ba61abc0d9f8.pdf) filed with SEC. “The Company has also incurred less than $10 million in one-time expenses in the third quarter related to the cybersecurity issue, which consisted of technology consulting services, legal fees and expenses of other third party advisors.” 


That’s a useful number to know.  The MGM Ransomware attack was pretty public, but for any company, responding to such a compromise will cost you money.  What’s often tricky in these cases is working out how much of that is because of lost earnings, refunds and goodwill gestures they’ve given customers versus the cost of the remediation.  It looks like MGM is saying that it’s about $10m in direct costs, and $100m in lost profits.  

Reading their [2022 Annual Report](https://s22.q4cdn.com/513010314/files/doc_financials/2022/ar/2022-Annual-Report.pdf) , it looks like the Las Vegas estate of casinos earns an annual revenue of $8.4b, and adding in the 3.8bn of regional operations for a total of around $12.2b, makes the $100m cost a little under 1% of their EBITDAR.   However, since their operating expenses are around $11b as well, it’ll be closer to 10% of their operating profit for the year.

If you assume that the costs are proportional, that means that for the average company, Ransomware, if it’s not a non-recoverable event, will cost you around 1% of your operating income.  If you run on razor thin profits, that’s going to hurt!

(I also suspect that in many cases, the $10m direct costs are liable to sink most companies and I doubt they are linearly proportional to the size of the IT estate) 


## [PCI v4 is coming. Are you ready? | Pen Test Partners ](https://www.pentestpartners.com/security-blog/pci-v4-is-coming-are-you-ready/)

[https://www.pentestpartners.com/security-blog/pci-v4-is-coming-are-you-ready/](https://www.pentestpartners.com/security-blog/pci-v4-is-coming-are-you-ready/)

> **Section 3** Sensitive authentication data must now be encrypted or protected if stored before authorization. Furthermore, technological solutions must be in place to prevent the copy and relocation of PAN data. Disk level encryption is no longer permitted for protection unless it is a form of removeable media (e.g., USB, external SSD). Hashing has also changed, organisations will need to use a keyed cryptographic hash method which is different from most common hash algorithms in use (HMAC, CMAC, GMAC and a strength of at least 128-bits). 
> 
> **Section 4** New requirements call for detailed documentation, tracking, and inventory of SSL and TLS certificates used for sensitive data transmission across public networks.
> 
> […] 
> 
> **Section 10** Manual log reviews are no longer permitted; automated methods are now required. Detection and alerting capabilities must be in place to address failures of critical security control systems. This requirement has extended from service providers only to everyone. 
> 
> **Section 11** Internal vulnerability scanning must now be authenticated, a necessary addition for e-commerce. IDS/IPS solutions must detect and alert on any covert malware communications being used such as DNS tunnelling. A further new requirement has been born, a change and tamper detection mechanism for payment pages is now mandated. This is to reduce and prevent the risk of skimming attacks. 


There’s some welcome changes in the new PCI standard, mostly bringing the security requirements up to date, which for legacy players may be an issue!

The push to say that security must be automated is particularly welcome though, and I really like the addition of change and tamper detection mechanisms for payment pages, which should drive more people to use subresource integrity checks more as well. 


## [Threat Modeling the Supply Chain for Software Consumers - Open Source Security Foundation ](https://openssf.org/blog/2023/09/27/threat-modeling-the-supply-chain-for-software-consumers/)

[https://openssf.org/blog/2023/09/27/threat-modeling-the-supply-chain-for-software-consumers/](https://openssf.org/blog/2023/09/27/threat-modeling-the-supply-chain-for-software-consumers/)

> Thanks to the work from the End Users Working Group, we now have an [initial threat model.](https://docs.google.com/document/d/1lLCsT0a5vp6FcvquWPzx8AzhFMORyw-4rd9WSyUO9zI/edit?usp=sharing) Starting with a very high-level depiction of a typical enterprise open source software consumer with common software assets. This model then details high-level threats against each component. Many of these threats should resonate as they have been actively attacked and  reported in the media. 
> 
> Our next step is to continue digging deeper into these threats to flesh out the pertinent issues and finally map the existing frameworks on this architecture to identify the potential gaps or priorities that need to be followed. 


This model of software development looks useful, if simplistic, and the principle of creating an open and reusable threat model for software development organisations that can be used by consumers to determine their risk exposure is quite nice.  One to watch 


## [Overhauling AWS account access with Terraform, Granted, and GitOps - The Duckbill Group ](https://www.duckbillgroup.com/blog/overhauling-aws-account-access-with-terraform-granted-and-gitops/)

[https://www.duckbillgroup.com/blog/overhauling-aws-account-access-with-terraform-granted-and-gitops/](https://www.duckbillgroup.com/blog/overhauling-aws-account-access-with-terraform-granted-and-gitops/)

> Internally, we started discussing a new problem we were facing: as we brought in more specialized contractors for one-off consultations on our client accounts, we needed a way to grant a person access only to the client accounts they were working on. Our existing setup worked well for our staff, who had access to all clients, but it didn’t really support limiting access on a per-client basis. We eventually cobbled together an MVP that required the manual creation of roles and policies, but the checklist to set up a new contractor was two pages long! Definitely not a good solution.
> 
> […]
> 
> We ultimately decided to take a step back and really think through exactly what we wanted of a new approach. We came to these key needs:
> 1. Employee access and one-time contractor access should be managed the same way
> 2. Authentication and authorization to AWS should be governed by a single source: Duckbill’s Google user/group directory.
> 3. Use Granted.dev for assuming roles, and have a programmatic generation of the Granted config. No config files should ever be passed around again.
> 4. Read client access details (account ID, external ID, internal name) from a central database. These aren’t secrets and shouldn’t be treated as such.
> 5. Granting/revoking access should be easily done and traceable/auditable.
> 6. A user should only be able to access clients for which they have been explicitly granted access.
> 
> […]
> 
> One key thing we realized we had to decide on was the level of confidentiality of the data involved. We’ve always treated client data as the crown jewels, but different people on the team had different ideas about what constituted client data and what didn’t. We finally decided to properly define our levels of confidentiality, resulting in three levels: Public, Confidential, and Client Data. 


There’s a lot in this blogpost, but a couple of things really stood out (beyond the technical details of how they actually implemented it!

Firstly, the recognition that as you grow, you need to differentiate between staff members who are on different client accounts is something that is really important when you are building trust as a company.  Just because Karen works for me, doesn’t mean she should be able to see everything that I see.  Defining this level of role level access in a modern cloud system is possible, but often a bit painful.

The set of key needs that are articulated here work well for this kind of client consulting capability, and I think sets out some of the main approaches.

Secondly, that aside at the end, defining the difference between confidential and client-data is also critically important.  It’s easy when you start to just say that everything relating to a client needs to be in the same need to know bucket.  But of course there are all kinds of information that can be shared with the wider team and organisation.  You want to be able to tell your staff you won a key contract, without giving them access to that clients data of course.  

This clear separation makes it possible to articulate the right user behaviours around handling the data as well.  It makes it obvious to users what bits of information can be shared via email, IM, slack, and what cannot be shared.  That helps users to understand their responsibilities, as much as it helps the system designer to ensure that data is kept appropriately confidential 


## [Cloudflare now uses post-quantum cryptography to talk to your origin server ](http://blog.cloudflare.com/post-quantum-to-origins/)

[http://blog.cloudflare.com/post-quantum-to-origins/](http://blog.cloudflare.com/post-quantum-to-origins/)

> The first connection is from the visitor’s browser to Cloudflare. In October 2022, [we enabled](https://blog.cloudflare.com/post-quantum-for-all/) [_X25519+Kyber_](https://blog.cloudflare.com/post-quantum-for-all/) [as a beta for all websites and APIs](https://blog.cloudflare.com/post-quantum-for-all/) served through Cloudflare. However, it takes two to tango: the connection is only secured if the browser also supports post-quantum cryptography. As of August 2023, [Chrome](https://blog.chromium.org/2023/08/protecting-chrome-traffic-with-hybrid.html) is slowly enabling _X25519+Kyber_ by default.
> 
> The visitor’s request is routed through Cloudflare’s network (2). We have [upgraded](https://blog.cloudflare.com/post-quantum-cryptography-ga) many of these internal connections to use post-quantum cryptography, and expect to be done upgrading all of our internal connections by the end of 2024. That leaves as the final link the connection (3) between us and the _origin server_ .
> 
> We are happy to announce that **we are rolling out support for X25519+Kyber for most outbound connections** , including _origin servers_ and [Cloudflare Workers](https://workers.cloudflare.com/)  `fetch()` calls. 


This is nice.  One of the interesting things about using a CDN is that it makes it far easier to push cryptographic requirements further away from your own team.  You are now only responsible for securing the connection from Cloudflare back to your hosts, so that means not having to worry about someone wanting to access your website on the Nintendo Switch internal browser, or an old phone or something.

Cloudflare are then responsible for managing the rollout of cryptographic upgrades in a non-customer impacting way, which is far easier for them at the scale that they operate at.

Of course, whether X25519+Kyber is truly quantum secure is something we’ll only get to know over the next  few years or decades, but at least it’s a start! 


## [Don’t Let Zombie Zoom Links Drag You Down ](https://krebsonsecurity.com/2023/10/dont-let-zombie-zoom-links-drag-you-down/)

[https://krebsonsecurity.com/2023/10/dont-let-zombie-zoom-links-drag-you-down/](https://krebsonsecurity.com/2023/10/dont-let-zombie-zoom-links-drag-you-down/)

> At issue is the **Zoom Personal Meeting ID** (PMI), which is a permanent identification number linked to your Zoom account and serves as your personal meeting room available around the clock. The PMI portion forms part of each new meeting URL created by that account, such as: [zoom.us/j/5551112222](http://zoom.us/j/5551112222) Zoom has an option to include an encrypted passcode within a meeting invite link, which simplifies the process for attendees by eliminating the need to manually enter the passcode. Following the previous example, such a link might look something like this: [zoom.us/j/5551112222/pwd=jdjsklskldklsdksdklsdkll](http://zoom.us/j/5551112222/pwd=jdjsklskldklsdksdklsdkll) Using your PMI to set up new meetings is convenient, but of course convenience often comes at the expense of security. Because the PMI remains the same for all meetings, anyone with your PMI link can join any ongoing meeting unless you have locked the meeting or activated Zoom’s Waiting Room feature.
> 
> Including an encrypted passcode in the Zoom link definitely makes it easier for attendees to join, but it might open your meetings to unwanted intruders if not handled responsibly. Particularly if that Zoom link is somehow indexed by Google or some other search engine, which happens to be the case for thousands of organizations.
> 
> Armed with one of these links, an attacker can create meetings and invite others using the identity of the authorized employee. And many companies using Zoom have made it easy to find recently created meeting links that include encrypted passcodes, because they have dedicated subdomains at [Zoom.us](http://zoom.us/) .
> 
> […]
> 
> According to Akiri, here are several tips for using Zoom links more safely: **Don’t Use Personal Meeting ID for Public Meetings:** Your Personal Meeting ID (PMI) is the default meeting that launches when you start an ad hoc meeting. Your PMI doesn’t change unless you change it yourself, which makes it very useful if people need a way to reach you. But for public meetings, you should always schedule new meetings with randomly generated meeting IDs. That way, only invited attendees will know how to join your meeting. You can also turn off your PMI when starting an instant meeting in your profile settings. 


Ok, put your hand up if you didn’t realise that the password wasn’t randomly generated on a per meeting basis?

I feel like this is one of those contextual problems.  If I schedule a meeting, then this behaves correctly, although I strongly suspect that repeating meetings might have the same code (which might be bad for things like interviews!).

But using your “adhoc meeting” capability and having it not create a new token each time is a surprise for sure 


## [Cisco Plugs Gaping Hole in Emergency Responder Software - SecurityWeek ](https://www.securityweek.com/cisco-plugs-gaping-hole-in-emergency-responder-software/)

[https://www.securityweek.com/cisco-plugs-gaping-hole-in-emergency-responder-software/](https://www.securityweek.com/cisco-plugs-gaping-hole-in-emergency-responder-software/)

> _“A vulnerability in Cisco Emergency Responder could allow an unauthenticated, remote attacker to log in to an affected device using the root account, which has default, static credentials that cannot be changed or deleted.”_  _“This vulnerability is due to the presence of static user credentials for the root account that are typically reserved for use during development. An attacker could exploit this vulnerability by using the account to log in to an affected system. A successful exploit could allow the attacker to log in to the affected system and execute arbitrary commands as the root user.”_ Cisco said the security defect affects only Cisco Emergency Responder Release 12.5(1)SU4.
> The San Jose, Calif. company is urging Cisco Emergency Responder users to immediately apply the available patches, warning that there are no workarounds that address this vulnerability. 


I mean, this isn’t a big deal right, it only affects systems that process and manage 911 calls right?

Having embedded, unalterable credentials is something that really shouldn’t be happening in 2023 surely! 


## [❅ phishing 2fa 25 years ago ❅: g — LiveJournal ](https://g.livejournal.com/17695.html?1234234)

[https://g.livejournal.com/17695.html?1234234](https://g.livejournal.com/17695.html?1234234)

> it's been easy to phish 2fa since the 90s. aol employees used physical "rsa securid" devices displaying 6 digits that changed once per minute.
> 
> i once conceptualized and built out an aol employee uname:passwd:2fa phishing scam website called "be in an aol 5.0 commercial" where aol employees could sign up to have their personal screen names appear in upcoming tv ads.
> 
> naturally - this secure website required their "screen name" (username) and password on the first page - and then their 6 digit 2fa token on the second.
> the moment that happened - a race condition started.
> 
> my icq would receive messages with loud " _uhoh.wav_ " noises playing each time. i then had < 60 seconds to access the phished aol employee account. 


A nice reminder that there is very little new under the sun.  This method for attacking and compromising users from over 25 years ago will also work today for many implemnetaitons of 2FA.

About the only thing this wont fool is hardware token MFA that ties the credential to the specific website, such as FIDO2 WebAuthn tokens. 


