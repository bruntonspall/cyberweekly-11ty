---
title: "125 - Self service tooling"
date: 2020-11-16
description: "I have long contended that one of the indicators of maturity in an organisation, and one of the drivers of efficiency is the ability of teams to self-service."
permalink: /self-service-tooling/
---

I have long contended that one of the indicators of maturity in an organisation, and one of the drivers of efficiency is the ability of teams to self-service.

This can extend from the ability to use the cloud effectively, to the vending machines in Facebook and Google for getting new keyboards, dongles and other accessories.

When a central supporting team, whether IT, DevOps, Platform or Security, insists that customers must come to it, discuss their requirements and get a custom response, it creates dual burdens.  Firstly the supporting team has to manage those requests, it has to have a mechanism for the requests coming in and it has to advertise that capability across the organisations.  But it creates a burden on the delivery team as well, they might have to fill in 4 different forms from 4 different supporting teams, all of which ask for very similar information.  

Self service capabilities assume that teams are able to request the thing they need, and can get access to it simply and trivially.  

When a central support team really provides easy central self service tools and platforms, it encourages adopts, but it also "paves the path", making it the easiest and most supported way for a delivery team to get something done.  That means that you can focus your engineering investment on that core supported products and every team that uses the self service system will gain the rewards.

Of course, if you've not done this for the last 10 years, there is going to be hundreds of systems that are not unified, and you will need to educate the users on how to select the right tool, but it's a start, and if you can improve the flow of the delivery teams, you can concentrate your effort on the migrating the more complex cases over time.

## [Personal Data Warehouses: Reclaiming Your Data](https://simonwillison.net/2020/Nov/14/personal-data-warehouses/)

[https://simonwillison.net/2020/Nov/14/personal-data-warehouses/](https://simonwillison.net/2020/Nov/14/personal-data-warehouses/)

> But there was one part of this that really caught my eye. He talks about a thing he calls a “metasearcher”—a search engine on his personal homepage that searches every email, journals, files, everything he’s ever done—all in one place.
> 
> And I thought to myself, I really want THAT. I love this idea of a personal portal to my own stuff.
> 
> I’ve been building this over the past year.
> 
> So essentially this is my personal data warehouse. It pulls in my personal data from as many sources as I can find and gives me an interface to browse that data and run queries against it.
> 
> I’ve got data from Twitter, Apple HealthKit, GitHub, Swarm, Hacker News, Photos, a copy of my genome... all sorts of things.


This is a really interesting idea.  Simon is incredibly smart and can assemble these tools for himself, but the tools aren't complex.  In the spirit of the unix way, this is the assembly of lots of specialist single use tools into pipelines and a toolbox that gives you a lot of power.

The rest of the talk is worth reading as well, for an insight into how you can expose data, store it and make it trivially searchable with great ease.


## [Live off the Land? How About Bringing Your Own Island? An Overview of UNC1945 | FireEye Inc](https://www.fireeye.com/blog/threat-research/2020/11/live-off-the-land-an-overview-of-unc1945.html)

[https://www.fireeye.com/blog/threat-research/2020/11/live-off-the-land-an-overview-of-unc1945.html](https://www.fireeye.com/blog/threat-research/2020/11/live-off-the-land-an-overview-of-unc1945.html)

> The ease and breadth of exploitation in which UNC1945 conducted this campaign suggests a sophisticated, persistent actor comfortable exploiting various operating systems, and access to resources and numerous toolsets. Given the aforementioned factors, use of zero-day exploits and virtual machines, and ability to traverse multiple third-party networks, Mandiant expects this motivated threat actor to continue targeted operations against key industries while taking advantage of operating systems that likely have inadequate security visibility.     


This is a nice writeup of an "Uncategorised" threat actor.  That is to say, although they have advanced capabilities, they don't share TTP's or identifying behaviours with other known attack groups, meaning that FireEye doesn't feel capable of attributing it to another actor.

What's interesting here is the use of a remote exploitation tool for Solaris, as well as Linux backdoors. The neatest trick, although probably quite identifiable, is the attackers decision to download custom VM's onto the target machine, and then run their attack tools from within the VM.  Depending on your detection toolkit, that might hide the use of subprocesses from the root OS, making it harder to fingerprint and detect the use of common tools like Mimikatz or Powersploit


## [Security benefits of good cloud service whitepaper - NCSC.GOV.UK](https://www.ncsc.gov.uk/whitepaper/security-benefits-of-a-good-cloud-service)

[https://www.ncsc.gov.uk/whitepaper/security-benefits-of-a-good-cloud-service](https://www.ncsc.gov.uk/whitepaper/security-benefits-of-a-good-cloud-service)

> The more you take the time to understand the cloud services available, the bigger these benefits will be. If instead you treat the cloud service as a generic provider of VMs, most of these benefits won't be realised. Some of these solve the big security challenges that we've struggled to address in pre-cloud environments (such as having an exhaustive inventory and a single, consistent approach to authentication, authorisation, logging, monitoring, and alerts). With these challenges effectively commoditised, you can focus your time and resources on solving business problems that are unique to your organisation, rather than constantly having to reinvent the wheel.
> 
> Finally, when selecting a cloud service, make sure that it meets your needs and helps you to secure your data. If you plan to implement or retain functionality that could be consumed as a service, make sure you have a clear understanding why you'd want to do this. Don’t let anyone tell you the cloud is inherently insecure. If you choose a good cloud service - in line with our cloud security guidance - it’s probably more secure than whatever it replaces.


This is nice to see from the NCSC.  Good solid guidance about just how the cloud can be secure.  As they say, done well, the cloud can be more secure than what you are probably replacing


## [Hunting for Malicious Packages on PyPI](https://jordan-wright.com/blog/post/2020-11-12-hunting-for-malicious-packages-on-pypi/)

[https://jordan-wright.com/blog/post/2020-11-12-hunting-for-malicious-packages-on-pypi/](https://jordan-wright.com/blog/post/2020-11-12-hunting-for-malicious-packages-on-pypi/)

> In a nutshell, we’re sending each package name to a set of EC2 instances (I’d love to use Fargate or something in the future but I also don’t know Fargate, so…) which fetches some metadata about the package from PyPI, then starts sysdig as well as a series of containers to pip install the package while syscalls and network traffic were being collected. Then, all of the data is shipped up to S3 for future-Jordan to worry about.


Lovely bit of analysis here, work through all of the packages in PyPI and work out which, if any, do malicious things when installed.

Note that this doesn't check the runtime calls, but for the basics (such as on import calls), that could be scripted with a simple test program that imported the package and then exited.


## [Cyberattacks targeting health care must stop - Microsoft on the Issues](https://blogs.microsoft.com/on-the-issues/2020/11/13/health-care-cyberattacks-covid-19-paris-peace-forum/)

[https://blogs.microsoft.com/on-the-issues/2020/11/13/health-care-cyberattacks-covid-19-paris-peace-forum/](https://blogs.microsoft.com/on-the-issues/2020/11/13/health-care-cyberattacks-covid-19-paris-peace-forum/)

> In recent months, we’ve detected cyberattacks from three nation-state actors targeting seven prominent companies directly involved in researching vaccines and treatments for Covid-19. The targets include leading pharmaceutical companies and vaccine researchers in Canada, France, India, South Korea and the United States. The attacks came from Strontium, an actor originating from Russia, and two actors originating from North Korea that we call Zinc and Cerium.
> 
> Among the targets, the majority are vaccine makers that have Covid-19 vaccines in various stages of clinical trials. One is a clinical research organization involved in trials, and one has developed a Covid-19 test. Multiple organizations targeted have contracts with or investments from government agencies from various democratic countries for Covid-19 related work.
> 
> Strontium continues to use password spray and brute force login attempts to steal login credentials. These are attacks that aim to break into people’s accounts using thousands or millions of rapid attempts. Zinc has primarily used spear-phishing lures for credential theft, sending messages with fabricated job descriptions pretending to be recruiters. Cerium engaged in spear-phishing email lures using Covid-19 themes while masquerading as World Health Organization representatives. The majority of these attacks were blocked by security protections built into our products. We’ve notified all organizations targeted, and where attacks have been successful, we’ve offered help.


Microsoft coming out and claiming that nation backed attackers are specifically targeting vaccine development firms.  Of course, the economic advantage to countries that generate a vaccine and the profits that will be generated by the first labs to productionise the vaccine means that attackers are highly incentivised to compromise those systems, but still.

The positive side is that all of these attacks are fairly low sophistication, and as I keep saying, managing your email and your accounts with a major provider like Microsoft or Google is the best way to defend against even these attackers


## [Extrapolating Adversary Intent through Infrastructure](https://www.domaintools.com/resources/blog/extrapolating-adversary-intent-through-infrastructure#)

[https://www.domaintools.com/resources/blog/extrapolating-adversary-intent-through-infrastructure#](https://www.domaintools.com/resources/blog/extrapolating-adversary-intent-through-infrastructure#)

> Looking at domain names as composite objects - consisting of multiple components such as the domain registrar or where a domain resolves - allows us to track adversary activity and infrastructure creation through tendencies and patterns. Just as with items such as authoritative name servers or registration information, the very name chosen for a domain has significance, and can identify fundamental adversary behaviors.
> 
> Adversaries typically leverage themes in domain creation that can indicate aspects of attacker operations. This could include:
> 
> Blending in with likely “normal” traffic within targeted environments.
> Mirroring services or functions targeted for operations, such as logon portals.
> Matching target characteristics to facilitate interaction or lower suspicion when identified.
> By studying adversary naming choices, we can begin identifying various aspects of attacker operations - from how initial access operations may take place through likely victimology based on observations. In the following three examples, we will explore relatively recent campaigns to identify how adversary naming choice and patterns can be used to gain greater understanding of attacker goals and operations.


This is a nice bit of research, as well as a slight sales pitch, that shows how looking at adversaries through the lense of the domains that they register for their command and control, as well as phishing domains, can reveal the intent of the attacker.


## [2020 State of DevOps Report | presented by Puppet, & CircleCi](https://puppet.com/resources/report/2020-state-of-devops-report/)

[https://puppet.com/resources/report/2020-state-of-devops-report/](https://puppet.com/resources/report/2020-state-of-devops-report/)

> High DevOps evolution correlates strongly with self-service capabilities.
> Highly evolved organizations are 6 times more likely than the least evolved organizations to report high usage of self-service platforms.


This report is worth a read, this year, as with every year.  It re-echo's the themes that we've known before.  Organisations that invest in internal tooling, in enabling their staff and their business units to operate are hugely more effective, more efficient and more secure.

This focuses this year on self service capability, which I think is key.  I've seen some of the DORA questions in the past, and the problem with some of them is that low capability organisations might say that they have certain functions, because they don't understand them.  Focusing on the ability of teams to self service is a clear indicator of high levels of maturity in a DevOps organisation.


## [The value of ‘Government as a Platform’ in a crisis | by Benjamin Welby | Towards Digital States | Nov, 2020 | Medium](https://medium.com/digital-states/the-value-of-government-as-a-platform-in-a-crisis-9556c2f2eec1)

[https://medium.com/digital-states/the-value-of-government-as-a-platform-in-a-crisis-9556c2f2eec1](https://medium.com/digital-states/the-value-of-government-as-a-platform-in-a-crisis-9556c2f2eec1)

> The perception of standards and principles negatively as a blocker or positively as an enabler reflects the service design and delivery DNA of an organisation. It is better to equip people with the right tools and skills rather than enforcing documented rules and policing compliance. And so, when crisis hits and instinct takes over, the instinct reinforces the ‘right’ behaviours of understanding users and their needs, respecting security, prioritising accessibility and being committed to measuring, learning and iterating over time.
> This culture needs to be a public sector culture, not something advocated by a particular pocket of a particular organisation. Effective services can only be built by diverse, multi-disciplinary teams that default to involving the public (even if face to face contact is difficult) as they try to understand whole problems and design end to end experiences. These teams will naturally work across organisational boundaries to ensure that users avoid dead ends after being handed from one organisation to another. They will also be mindful of both public facing and internal processes to avoid the ‘swivel-chair integration’ of websites feeding paper based internal processes that require the presence of on-site staff.


This is a great essay from Benjamin, and there's loads to pick from, but this stood out to me.  

We can't build and assume that controls, governance and standards are there to block, to restrict or to prevent.  If the entire organisation doesn't understand and value why they exist, then they'll just become compliance checkboxes, and those, as Ben says, are the things that get skipped when life gets tough.


## [Tech Talent for 21st Century Government • Partnership for Public Service](https://ourpublicservice.org/publications/tech-talent/)

[https://ourpublicservice.org/publications/tech-talent/](https://ourpublicservice.org/publications/tech-talent/)

> From delivering high-quality health care to veterans to processing millions of tax returns to regulating autonomous vehicles and drones, agencies depend on technology and innovation to operate efficiently and deliver effective services to the American people. Yet the federal government lags behind the private sector in hiring qualified technologists for mission-critical leadership and staff positions, and has fallen short in adopting modern technologies.
> 
> In two reports, “Mobilizing Tech Talent” and “Tech Talent for 21st Century Government,” the Partnership for Public Service and the Tech Talent Project identify top technology and innovation leadership positions in government, the competencies these leaders and their teams need to be successful, advice for recruiting and hiring technical experts, and opportunities and challenges for technology transformation in federal agencies.


While US focused, these reports by a non-partisan think tank for the future US administration, focuses on how to make the best use of tech talent in the future. 

This in particular stood out from the description of CIO's

> FITARA also requires the CIO to report to or work directly with the agency head or their deputy. But according to the Government Accountability Office, “executive-level governance and oversight across the government has often been ineffective, specifically from chief information officers.” CIOs should be modern technical leaders capable of making significant decisions to radically improve the protection and use of information for digital service delivery. The decisions a CIO might make include moving from legacy systems to cloud computing; building teams that are skilled in technology, information security and cybersecurity; or retraining employees. Effective CIOs should engage with strategy and policy, and should be engaged by a leadership team as peers


## [The US nuclear forces’ Dr. Strangelove-era messaging system finally got rid of its floppy disks](https://www.c4isrnet.com/air/2019/10/17/the-us-nuclear-forces-dr-strangelove-era-messaging-system-finally-got-rid-of-its-floppy-disks/)

[https://www.c4isrnet.com/air/2019/10/17/the-us-nuclear-forces-dr-strangelove-era-messaging-system-finally-got-rid-of-its-floppy-disks/](https://www.c4isrnet.com/air/2019/10/17/the-us-nuclear-forces-dr-strangelove-era-messaging-system-finally-got-rid-of-its-floppy-disks/)

> Think of SACCS as the U.S. nuclear force’s version of AOL instant messenger — one of the many old, duplicative systems used by U.S. Strategic Command to send emergency action messages from nuclear command centers to forces in the field. Based in Offutt Air Force Base, Neb., the 595th is charged with upkeeping SACCS and ensuring its day-to-day operations.
> 
> "I joke with people and say it's the Air Force's oldest IT system. But it's the age that provides that security,” Rossi said in an October interview. "You can't hack something that doesn't have an IP address. It's a very unique system — it is old and it is very good."
> 
> In 2016, the Government Accountability Office wrote that SACCS runs on an IBM Series/1 computer dating from the 1970s and that the Defense Department planned “to update its data storage solutions, port expansion processors, portable terminals and desktop terminals by the end of fiscal year 2017,” but it’s unclear whether those upgrades have occurred.
> 
> Col. Hayley James, deputy group commander for the 595th Command and Control Group, acknowledged that the Air Force is seeking a replacement for SACCS, but both she and Rossi declined to comment on that effort. Asked about ongoing modernization of the current SACCS system, Rossi would only acknowledge that the Air Force has made recent enhancements to enable speed or connectivity.


I mean... talking about the fact that something is secure because it predates the modern internet is really a unique way of looking at things.

At least they dropped the use of 8" floppy disks in 2019 (something that predates even my first experiences with computers, I only just remember 5 1/4" disks, and 3 1/2" disks were the ones I used as a child).


