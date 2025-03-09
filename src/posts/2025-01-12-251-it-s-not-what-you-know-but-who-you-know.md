---
title: "251 - It's not what you know, but who you know"
date: 2025-01-12
description: "Two sides of the same coin today, a reminder that who you know and how you interact with them is more important in many cases than the technical details."
permalink: /it-s-not-what-you-know-but-who-you-know/
---

Two sides of the same coin today, a reminder that who you know and how you interact with them is more important in many cases than the technical details.

We like to think of the world in lovely nice boxes, where everything can be lumped together into sharply defined categories.  Goody and Baddie, Friend and Foe, Technical and Social.  

The world however is a mess of realities, pragmatisms and flawed people doing things for their own often inscrutable reasons.  Our mental models to make sense of the actions of those around us only holds for the observed behaviour so far, but cannot predict that something won't happen in the future.

While I sometimes rail against security advice that defeats all nuance (such as phishing simulations, or mandatory password complexity requirements), we also have to remember that security controls there defences in layers that are there to catch us when our assumptions about the world turn out to be false.

In the case of the attack outlined below, it's incredibly difficult to predict that an attack is coming from a nearby neighbour.  As the write up says, it's so rare that they created a new name for the TTP.

But yet it's not really rare at all if you can squint your eyes and look at it differently.  Our supply chains have been subject to this for decades, from fraudulent misrepresentation to employee insider threats.  We know that we cannot assume that those inside our systems are who they say they are or always doing things for good reasons.  Instead we build patterns to deal with that, from the modern zero trust model of reauthenticating every action against a context model of whether it's expected and legitimate, or whether it's a more traditional two-person rule that requires checks on taken actions.  We also can't shrug off all responsibility onto our suppliers to do this for us.  Whether we become targets because of which suppliers we share, or we end up using a supplier who doesn't have a matching threat tolerance, we can't ever outsource the responsibility for security to our suppliers.

Policy writing often suffers from this problem of over-fitting and generalisation.  We know the world is complex, but writing a set of rules that can tell people that they should use a more secure and complex password for their password manager than their gym membership site, and that they might want two factor authentication for their mail system, but that using SMS authentication on their crypto wallet may not be sufficient.  We instead create policies that hide the complexity, because simple rules are far easier for people to understand, to remember and to follow, even if they don't match reality.  That's what leads us to policies like "all passwords must be at least 12 characters, contain upper case, lower case, a digit, an emoji and an ancient Sumerian curse word".  Context is incredibly difficult to fit into policies and governance, and yet it's the thing that matters when interpreting policy at the time.

Equally however, we need to think about how we face out to customers that we serve, and how we make the barrier between us as permeable and simple as possible.  Should every customer need to understand your organisation structure in order to get help?  Should they need to know about different bits of your platform and how they interact, or should we make sure that engaging with us is humane, simple and supportive?  That adds a burden to our teams, and that burden in unequal, each and every customer has just one interaction with us, whereas we have tens or hundreds of interactions going on at the same time.  But that one interaction is our opportunity to spark joy, to win a customer from being just a user into being an advocate and champion for our product.

The world is big, complex and messy, and one way to success is to try your hardest to make every interaction with your team as simple, easy and positive as you can.

On that note, I want to thank everyone who got in touch after last week.  I got emails, WhatsApp's, and slack messages from what felt like a surprising number of people thanking me for picking this up again, and it was incredibly nice to hear from you and hear that you were pleased I was back to writing.  Apologies to those I haven't managed to reply to, I'll get on that.  Secondly, since almost everybody noticed that I had a typo, literally on the first line, it's good to know that my editorial standards haven't improved with 6 months off!  As always, please do feel free to drop me a message if you disagree with anything, if you have something you think I should read, or if you just want to say hi. 

## [The Nearest Neighbor Attack: How A Russian APT Weaponized Nearby Wi-Fi Networks for Covert Access | Volexity ](https://www.volexity.com/blog/2024/11/22/the-nearest-neighbor-attack-how-a-russian-apt-weaponized-nearby-wi-fi-networks-for-covert-access/)

[https://www.volexity.com/blog/2024/11/22/the-nearest-neighbor-attack-how-a-russian-apt-weaponized-nearby-wi-fi-networks-for-covert-access/](https://www.volexity.com/blog/2024/11/22/the-nearest-neighbor-attack-how-a-russian-apt-weaponized-nearby-wi-fi-networks-for-covert-access/)

> Given the assumed physical distance, you may be wondering how exactly this threat actor was able to authenticate to Organization A’s Enterprise Wi-Fi network. The first and most obvious thing needed were valid credentials. This was accomplished via password-spray attacks against a public-facing service on Organization A’s network to validate credentials. And while credentials could be validated, they could not be used against Organization A’s public services due to implementation of multi-factor authentication (MFA).
> 
> The Enterprise Wi-Fi network, however, did not require MFA and only required a user's valid domain username and password to authenticate. Meanwhile, the threat actor was halfway around the world and could not actually connect to Organization A’s Enterprise Wi-Fi network. To overcome this hurdle, the threat actor worked to compromise other organizations who were in buildings within close proximity to Organization A’s office. Their strategy was to breach another organization, and then move laterally within that organization to find systems they could access that were dual-homed, (i.e., having both a wired and wireless network connection).
> 
> Once successful in this endeavor, having found a system that was connected to the network via a wired Ethernet connection, the threat actor would access the system and use its Wi-Fi adapter. At this point they would connect to the SSID of Organization A’s Enterprise Wi-Fi and authenticate to it, thus granting them access to Organization A’s network.
> 
> […]
> 
> This new information caused Volexity to examine logs from a system at Organization A that provided Internet-facing webservices that could be authenticated against. The service itself was protected with MFA, but it could be used to verify if credentials were valid or not.
> 
> […]
> 
> Volexity also found evidence the attacker had been connecting to Organization B’s Wi-Fi from another network that belonged to another nearby organization (“Organization C”). The attacker had gone to great lengths to breach multiple organizations so they could daisy-chain Wi-Fi and/or VPN connections to ultimately reach the network of Organization A. 


It’s unusual that we get an entirely new attack methodology, but I think this counts.  Targeting an organisation by targeting someone who is physically nearby and then using that physical closeness to carry out attacks that benefit from physical proximity is a really interesting move, and Volexity seem pretty clear that this isn’t the only instance they’ve seen of it.

Of course, the bigger question here is why the organisation made the decision that you didn’t need to put in place the same safeguards for people physically in the area.  “The call is coming from inside the house” is a trope for a reason, and as talked about in zero-trust for decades now, presence on the physical corporate network, let along the sites wifi should not allow you to bypass any security controls that you wouldn’t apply to strangers from the internet!

We also see again, the value that phishing resistant MFA has, and critically, that where possible you need systems to validate the MFA before validating that an account exists or whether the password is correct. 


## [You can outsource risk, but you can't outsource reputation ](https://shkspr.mobi/blog/2024/06/you-can-outsource-risk-but-you-cant-outsource-reputation/)

[https://shkspr.mobi/blog/2024/06/you-can-outsource-risk-but-you-cant-outsource-reputation/](https://shkspr.mobi/blog/2024/06/you-can-outsource-risk-but-you-cant-outsource-reputation/)

> What does it say about the state of NHS IT that this attack has happened?
> 
> Nothing.
> 
> Because the NHS was not hacked.
> 
> Instead, a company they use to perform blood tests was attacked. [Synnovis is the company responsible](https://www.synnovis.co.uk/news-and-press/synnovis-cyberattack) - they're the ones who have fallen prey to an attacker. This private company - will all the resources of the free-market system - hadn't protected themselves well enough.
> 
> […]
> 
> Go through other news stories on the subject and see how clear they make it that it _isn't_ the NHS who have been hacked.
> 
> If your website goes down, do your users care whether its _technically_ an outage at your 3rd party CDN? When your customers' credit card details are leaked, do the headlines mention your name or your payment provider's? Which bits of your reputation do you feel like handing to other people? 


I agree with Terence here.  Your users don’t care that you’ve outsourced the risk to your suppliers, and they won’t take terribly kindly on you saying “Not our fault, it was their fault”.

Your supply chain is your responsibility, and it will be your reputation.  Do you take that into account for every contract you sign, for every supplier you take on board? 


## [Unfashionably secure: why we use isolated VMs – Thinkst Thoughts ](https://blog.thinkst.com/2024/07/unfashionably-secure-why-we-use-isolated-vms.html)

[https://blog.thinkst.com/2024/07/unfashionably-secure-why-we-use-isolated-vms.html](https://blog.thinkst.com/2024/07/unfashionably-secure-why-we-use-isolated-vms.html)

> Fundamentally, Canary relies on two components: the Canary devices (hardware or virtual) that are deployed in customer infrastructure, and the Console (which we run) that these Canaries report into. Very broadly this is identical to most cloud-managed device or appliance products: appliances send telemetry to the cloud. It’s typical for cloud-managed devices to report to a _single_ endpoint (e.g. one HTTPS service), or perhaps a region-specific endpoint. In those products, devices are managed via a website that is multi-tenanted (i.e. the same management site is shared by multiple customers). This comes with multiple operational and cost benefits, and is a natural choice.
> 
> Except, we don’t make that choice. Every Canary customer has their own tenant, the Console.
> 
> [….]
> 
> Choosing Cloud-native technologies and approaches comes with its own baggage. For us, the primary issue is that the security boundary that separates customers from each other becomes an application issue, and that is too risky. As a security vendor, a breach of customer data is a nightmare scenario for us. 


I’ve talked about this many times before.  But one of the biggest “new” blast radius concepts in modern cloud supply chain is the ability to jump from customer to customer.

If you use tool A which is on cloud provider B, and so does Bank Z, and the attacker can totally compromise your system in order to jump inside the controls in cloud provider B and back out, then your threat model now has to contend with everyone who might be interested in anybody who is a customer of tool A.

Internal separation between tenancies is critical to avoiding becoming a target not because of what you have, but who you are near 


## [Unveiling LIMINAL PANDA - Threats to Telecom Sector | CrowdStrike ](https://www.crowdstrike.com/en-us/blog/liminal-panda-telecom-sector-threats/)

[https://www.crowdstrike.com/en-us/blog/liminal-panda-telecom-sector-threats/](https://www.crowdstrike.com/en-us/blog/liminal-panda-telecom-sector-threats/)

> In 2021, CrowdStrike attributed multiple telecommunications sector intrusions to the LightBasin activity cluster, which has consistently targeted telecom entities since at least 2016 using various custom tools. An extensive review of this intrusion activity has determined some of the events documented in a [**previous blog post**](https://www.crowdstrike.com/en-us/blog/an-analysis-of-lightbasin-telecommunications-attacks/) are attributable to a separate adversary now tracked as LIMINAL PANDA. This association resulted because multiple threat actors were conducting malicious activity on a highly contested compromised network.
> 
> […]
> 
> LIMINAL PANDA conducts intrusion activity that poses a significant potential threat to telecommunications entities. The adversary targets these organizations to directly collect network telemetry and subscriber information or to breach other telecommunications entities by exploiting the industry’s interoperational connection requirements. LIMINAL PANDA’s likely operational motivations — indicated by their development and deployment of tooling specific to telecommunications technology — closely align with signals intelligence (SIGINT) collection operations for intelligence gathering, as opposed to establishing access for financial gain.
> 
> […]
> 
> These recommendations can be implemented to help protect against the activity described in this blog:
> 
> * Implement complex password strategies — avoiding default or generic options — for SSH authentication or employ more secure methods such as SSH key authentication, particularly on servers that accept connections from external organizations (e.g., eDNS servers).
> * Minimize the number of publicly accessible services operating on servers that accept connections from external organizations to those required for organizational interoperation. 


Compromise of telecoms sector players shouldn’t be a surprise, it is of course a natural target for espionage activities given that people of all organisations use mobile phones and telecoms networks.

However the level to which these are “contested” networks, which is to say that there are multiple adversaries on the network, potentially impacting each others, as well as active defenders on the system was not as well known.

But more than that, the recommendations in here show the level of security investment needed on some of them.  Default or generic passwords on servers available to external organisations in 2024?  This stuff isn’t hard to get right in a greenfield environment, but fixing this stuff in legacy critical infrastructure is harder than it looks, but absolutely has to be done 


## [Chinese threat actor Storm-0940 uses credentials from password spray attacks from a covert network | Microsoft Security Blog ](https://www.microsoft.com/en-us/security/blog/2024/10/31/chinese-threat-actor-storm-0940-uses-credentials-from-password-spray-attacks-from-a-covert-network/)

[https://www.microsoft.com/en-us/security/blog/2024/10/31/chinese-threat-actor-storm-0940-uses-credentials-from-password-spray-attacks-from-a-covert-network/](https://www.microsoft.com/en-us/security/blog/2024/10/31/chinese-threat-actor-storm-0940-uses-credentials-from-password-spray-attacks-from-a-covert-network/)

> Microsoft has observed multiple password spray campaigns originating from CovertNetwork-1658 infrastructure. In these campaigns, CovertNetwork-1658 submits a very small number of sign-in attempts to many accounts at a target organization. In about 80 percent of cases, CovertNetwork-1658 makes only one sign-in attempt per account per day. Figure 2 depicts this distribution in greater detail.
> 
> CovertNetwork-1658 infrastructure is difficult to monitor due to the following characteristics:
> 
> * The use of compromised SOHO IP addresses
> * The use of a rotating set of IP addresses at any given time. The threat actors had thousands of available IP addresses at their disposal. The average uptime for a CovertNetwork-1658 node is approximately 90 days.
> * The low-volume password spray process; for example, monitoring for multiple failed sign-in attempts from one IP address or to one account will not detect this activity 


A great example of why it is so hard to defend against some of the most competent adversaries.  I’ll note that this behaviour isn’t just constrained to the biggest players though, there are commercial firms out there who provide “free VPN” services in exchange for running software on your home network that other VPN users can use.  Using this, anyone could carry out this kind of attack.

The best defence here, and I sound like a scratched record I’m afraid, is the use of phishing proof multi-factor authentication.  Passkeys or hardware FIDO2 tokens mean that password spraying can’t ever work.

Non phishing proof MFA may help here, but it will depend on implementation.   Some implementations won’t extend to the MFA prompt if the password is wrong.

This entire TTP means you can’t detect attempts to guess your users passwords, and that you probably shouldn’t try.  There’s almost no security benefit in knowing that someone is trying thousands of passwords for a given account, as there’s very little you can do about it.  If you have good MFA, then it doesn’t matter, and if you don’t, you should just assume that this will happen at some point, so it’s a given that it’s going on. 


## [Why Facebook doesn’t use Git ](https://graphite.dev/blog/why-facebook-doesnt-use-git)

[https://graphite.dev/blog/why-facebook-doesnt-use-git](https://graphite.dev/blog/why-facebook-doesnt-use-git)

> What is the takeaway from this story? Reflecting on the quotes and interviews, I’m reminded of the classic wisdom that so many of history’s key technical decisions are human-driven, not technology-driven.
> 
> Facebook didn’t adopt Mercurial because it was more performant than Git. They adopted it because the maintainers and codebase felt more open to collaboration. Facebook engineers met face-to-face with Mercurial maintainers and liked the idea of partnering. When it came to persuading the whole engineering org, the decision got buy-in due to thoughtful communication - not because one technology was strictly better than another.


This is a great historical deep dive into something deeply nerdy and technical, and yet at the end of the day, it comes down to people rather than technology.

You can make the worlds best mousetrap, but people won't just beat a path to your door.  Instead you need to understand what the problems are that face individuals, and ensure that your solutions makes their experience better.  Your solution needs to be good, but underestimate the power of people at your peril


## [No Wrong Doors. ](https://lethain.com/no-wrong-doors/)

[https://lethain.com/no-wrong-doors/](https://lethain.com/no-wrong-doors/)

> Something I’ve been thinking about recently is how engineering organizations can adopt a variant of the No Wrong Doors policy to directly connect folks with problems with the right team and information. Then the first contact point becomes a support system for navigating the bureaucracy successfully.
> 
> […]
> 
> Beyond being helpful to your colleagues, which is an obvious goal in some companies and not-at-all a cultural priority in others, I think there are a number of other advantages to think about here. First, being helpful creates positive relationships across organizations. Second, it makes it more obvious where you do have genuine areas of ambiguous ownership, and makes it possible for informed parties to escalate that rather than relying on folks with the least context to know to escalate the ambiguities. Third, it educates folks asking for help about the right thing to do, because a knowledgeable person helping is a great role model of the best way to solve a problem. Finally, if you happen to route to the wrong person–it happens!–then you learn that immediately rather than forcing someone without context to navigate the confusion. 


I’ve been thinking about platforms and providing ongoing support recently, and this echo's a lot of my thinking.

I’ll add that there’s another benefit that’s not well articulated here.  If you provide a “no-wrong-doors” policy, you’ll start to build up data on when people come to the wrong place.  That information tells you something about how your customers build a mental model of how your platform, services or bureaucracy works.  You can use that data to either rework your internal support structures to match that mental model, or to change your guidance and documentation to improve peoples mental model. 


## [Federal Government Cybersecurity Incident and Vulnerability Response Playbooks[pdf]](https://www.cisa.gov/sites/default/files/publications/Federal_Government_Cybersecurity_Incident_and_Vulnerability_Response_Playbooks_508C.pdf)

[https://www.cisa.gov/sites/default/files/publications/Federal_Government_Cybersecurity_Incident_and_Vulnerability_Response_Playbooks_508C.pdf](https://www.cisa.gov/sites/default/files/publications/Federal_Government_Cybersecurity_Incident_and_Vulnerability_Response_Playbooks_508C.pdf)

> The Cybersecurity and Infrastructure Security Agency (CISA) is committed to leading the response to
> cybersecurity incidents and vulnerabilities to safeguard the nation's critical assets. Section 6 of
> Executive Order 14028 directed DHS, via CISA, to “develop a standard set of operational procedures
> (playbook) to be used in planning and conducting cybersecurity vulnerability and incident response
> activity respecting Federal Civilian Executive Branch (FCEB) Information Systems.” 1
> 
> Overview
> 
> This document presents two playbooks: one for incident response and one for vulnerability response.
> These playbooks provide FCEB agencies with a standard set of procedures to identify, coordinate,
> remediate, recover, and track successful mitigations from incidents and vulnerabilities affecting FCEB
> systems, data, and networks. In addition, future iterations of these playbooks may be useful for
> organizations outside of the FCEB to standardize incident response practices


This is a great paper from CISA, with a standardised baseline security incident response playbook and a standard vulnerability disclosure playbook.

This wont solve every problem, but for all those organisations who don't have the capacity or resources to develop their own playbooks, it gives them an off the shelf solution that doesn't suck.  Well worth a read


## [Endpoint vulnerability management at scale - Canva Engineering Blog ](https://www.canva.dev/blog/engineering/endpoint-vulnerability-management-at-scale/)

[https://www.canva.dev/blog/engineering/endpoint-vulnerability-management-at-scale/](https://www.canva.dev/blog/engineering/endpoint-vulnerability-management-at-scale/)

> * A document with defined SLAs is a great way to align expectations with stakeholders.
> * Centrally managed applications and updates are critical to minimize the prevalence of fleet-wide vulnerabilities at scale. Remember that you want to address issues at the fleet-wide level and be mindful of focusing too much on a single application or vulnerability. Consider whether the effort you're putting into it is worthwhile.
> * Keep the user experience in mind. Our approach is to inform users and provide them the option to update by clicking a button. The update is forced if a user doesn’t update within a set period. This approach allows users to choose a convenient time for updates, reducing overhead and streamlining the process.
> * Set a limited scope; don’t try to resolve all the vulnerabilities on all the applications. There are almost an unlimited number of applications and vulnerabilities. By limiting the scope of your endpoint vulnerability management program, you can effectively remove some risk and iterate on the approach. Later, you can increase the scope as the program becomes more effective and you feel more comfortable. 


This is a nice writeup of how you can manage vulnerabilities across your endpoints at scale.  Critically here, there’s the point that just measuring vulnerabilities isn’t sufficient, you need to ensure you have a process that can assess and prioritise them.  There are always new vulnerabilities being released, and you will find yourself forever digging if you aren’t strategic about what you fix and when 


## [Judge mulls sanctions over Google’s “shocking” destruction of internal chats | Ars Technica ](https://arstechnica.com/tech-policy/2024/05/judge-mulls-sanctions-over-googles-shocking-destruction-of-internal-chats/)

[https://arstechnica.com/tech-policy/2024/05/judge-mulls-sanctions-over-googles-shocking-destruction-of-internal-chats/](https://arstechnica.com/tech-policy/2024/05/judge-mulls-sanctions-over-googles-shocking-destruction-of-internal-chats/)

> According to the DOJ, Google destroyed potentially hundreds of thousands of chat sessions not just during their investigation but also during litigation. Google only stopped the practice after the DOJ discovered the policy. DOJ's attorney Kenneth Dintzer told Mehta Friday that the DOJ believed the court should "conclude that communicating with history off shows anti-competitive intent to hide information because they knew they were violating antitrust law."
> 
> Mehta at least agreed that "Google's document retention policy leaves a lot to be desired," expressing shock and surprise that a large company like Google would ever enact such a policy as best practice.
> 
> Google's attorney Colette Connor told Mehta that the DOJ should have been aware of Google's policy long before the DOJ challenged the conduct. Google had explicitly disclosed the policy to Texas' attorney general, who was involved in DOJ's antitrust suit over both Google's search and adtech businesses, Connor said.
> 
> Connor also argued that Google's conduct wasn't sanctionable because there is no evidence that any of the missing chats would've shed any new light on the case. Mehta challenged this somewhat, telling Connor, "We just want to know what we don't know. We don't know if there was a treasure trove of material that was destroyed."


[This is an old one from my archive]

Another of these examples where the law and society has moved slowly compared to technology.  The way that people use chat products within a company can really vary, and whether those should be subject to legal hold is still incredibly tricky.

On one hand, any written communication that is relevant to the case at hand has always been admissable in court.  But spoken conversations tend not to be unless there is a whistleblower or, as in the case of SEC regulated finance companies, audio recordings of all internal calls.  
But some companies, Google among them, are very firm on setting a culture that chat is ephemeral, and that it should never be used for anything of note.  Googlers are encouraged to use internal mailing lists, as well as documents and tools to make decision, communicate important information and otherwise do anything that would be relevant in court.  That would imply that chat should be treated the same way that hallway verbal conversations are, which is ephemeral and non-disclosable.

Of course, if you are prosocuting a company for alleged wrongdoing, especially if you are considering whether individauls within the company illegally coordinated to carry out actions that they knew was wrong, then those ephemeral conversations feel like the way that they might do that, so you would want strong records kept.

I think the court is likely to find that Google's position here is untenable, and that because computers could keep records of these conversations, they should do so. However there will still be desires from employees within global companies to enable a digital form of ephemeral conversation, and this along with self-deleting whatsapp messages, off-platform chat systems and other social networks are going to continue to be places where the company culture grows, but that lawyers will want disclosable in the future.


