---
title: "255 - Principles that underpin our security education"
date: 2025-02-09
description: "I constantly use the refrain around “it’s not a technology problem, it’s a people problem” in a lots of contexts."
permalink: /how-should-we-talk-to-our-users/
---

I constantly use the refrain around “it’s not a technology problem, it’s a people problem” in a lots of contexts.

But too often I’m as guilty as anyone as thinking about solving this through technical means.

I love Google’s description of their own cloud governance system, but that’s a technical solution to what is otherwise a people problem.  The real problem we often face is that people solutions don’t scale as easily as technical solutions and aren’t as easy to think about.

I find myself in a quantum supposition state around our users on a regular basis.  A huge number of our defences are predicated on the assumption that the bad people are outside, and like a medieval castle, we’ve built moats, big walls and defences designed to keep the bad people out.  But much like fortied medieval cities, we have a huge number of people who have to come and go on a daily basis.  And our defences are often one way facing, so theyre easy to compromise from the inside.  Betrayal, whether purposeful or accidental can result in some of the worst impact to our organisations.

And so our users are both simultaneously our best and worst aspects of our cyber defence.

But while there are a small number of things we can do to mitigate the risks of a malicious insider, there’s actually a huge amount that we can do to improve our best defenders in the organisation.

As I’ve said before, and remain to be convinced otherwise, phishing our users drives down morale and doesn’t make people feel like they are helping defend the organsation.  Any “education” piece that uses gotcha’s isn’t going to endear users to the aims and goals of security.

But many users create their own “shadow security” processes.  And we often don’t enable or build up users expertise in security to give them confidence in which shadow security processes are good ones, and which actually undermine the real efforts.  

Education can be realy simple, and I was struck with the PIN piece about the power of a simple visualisation.  Everyone I’ve talked to about it has almost straight away wanted to start finding patterns.  Users actively looking for indicators of bad practice, and realising why attackers think the way they do?  That can only be a good thing, and if what users come away with is “People choose passwords and PIN’s in a really predictable manner”, then maybe that’s the single principle that you want to underpin all your password guidance.  

That principle will help them when they’re working late at night, and staring at the “change your PIN” screen.  It might help them start to trust a password manager over making their own password, or realise just what an issue picking their own year of birth might be.

That is the lesson we want people to learn, so lets focus on simple clear visualisations that enable.

## [Almost one in 10 people use the same four-digit PIN - ABC News ](https://www.abc.net.au/news/2025-01-28/almost-one-in-ten-people-use-the-same-four-digit-pin/103946842)

[https://www.abc.net.au/news/2025-01-28/almost-one-in-ten-people-use-the-same-four-digit-pin/103946842](https://www.abc.net.au/news/2025-01-28/almost-one-in-ten-people-use-the-same-four-digit-pin/103946842)

> The most commonly used PINs turned out to be staggeringly popular, meaning they’re particularly easy to guess when phones and bank cards fall into the wrong hands.
> 
> This grid of green squares might remind you of an old Space Invaders game, but it’s actually something like a mind-reader.
> 
> It’s going to let us peer inside and find out why humans choose some PINs more than others 


Honestly, go visit this one just for the visualisation.  Don’t read it, just look at the visualisation of first two digits versus last two digits and start asking what might drive commonality. 

 Go ahead, do it now, I’ll wait.

Back?  So many fascinating data tidbits here, the solid diagonal line showing 0000, 1111, 2222, but with fascinating additions in things like 0101 and 0202 onwards.
That  broad group down the bottom left appears to all be PIN’s that end 01 to 12, and start 01 through around 31.  So that’s american style dates,  with a slightly visible smear for people using good honest ISO8601 dates that go MM-DD (or YYYY-MM-DD but thats a long 8 digit pin).

As pointed out in the article, the good old classic 2580 comes out high, because on an ATM keypay, it makes a straight line down.

This is a great example of how a good visualisation can tell such a good story.  This picture by itself would be a great way to communicate the importance of not using easily guessable PINs for your staff or board for example 


## [No Honour Among Thieves: Uncovering a Trojanized XWorm RAT Builder Propagated by Threat Actors and Disrupting Its Operations | CloudSEK ](https://www.cloudsek.com/blog/no-honour-among-thieves-uncovering-a-trojanized-xworm-rat-builder-propagated-by-threat-actors-and-disrupting-its-operations)

[https://www.cloudsek.com/blog/no-honour-among-thieves-uncovering-a-trojanized-xworm-rat-builder-propagated-by-threat-actors-and-disrupting-its-operations](https://www.cloudsek.com/blog/no-honour-among-thieves-uncovering-a-trojanized-xworm-rat-builder-propagated-by-threat-actors-and-disrupting-its-operations)

> A trojanized version of the XWorm RAT builder has been weaponized and propagated. It is **_targeted specially towards script kiddies who are new to cybersecurity_** and directly download and use tools mentioned in various tutorials thus showing that there is no honour among thieves. The malware is spread primarily through a Github repo but also uses other file-sharing services. It has so far **_compromised over 18,459 devices_** globally, is capable of exfiltrating sensitive data like browser credentials, Discord tokens, Telegram data, and system information. The malware also features advanced functionality, including virtualization checks, registry modifications, and a wide array of commands enabling full control over infected systems. **_Top victim countries include Russia, USA, India, Ukraine, and Turkey_** .  
> 
> The malware uses Telegram as its command-and-control (C&C) infrastructure, leveraging bot tokens and API calls to issue commands to infected devices and exfiltrate stolen data. Analysis revealed the malware has so far exfiltrated more than 1 GB of browser credentials from multiple devices. **_Researchers also identified the malware's "kill switch" feature, which was leveraged to disrupt operations_** on active devices. 


There’s a backdoor in your backdoor!  

This is a great writeup of CloudSEK finding that a tool available for use by amateur cyber criminals had embedded in it backdoors that would enable the author to either disable the tool remotely, but also to get visbiility of all of the targets compromised by anyone using the tool, and to step in and take over.  

It’s a good reminder that you can’t trust the criminally minded, and many of the offensive tools you can find out there may not do everything you expect. 


## [SparkCat crypto stealer in Google Play and App Store | Securelist ](https://securelist.com/sparkcat-stealer-in-app-store-and-google-play/115385/)

[https://securelist.com/sparkcat-stealer-in-app-store-and-google-play/115385/](https://securelist.com/sparkcat-stealer-in-app-store-and-google-play/115385/)

> * We found Android and iOS apps, some available in Google Play and the App Store, which were embedded with a malicious SDK/framework for stealing recovery phrases for crypto wallets. The infected apps in Google Play had been downloaded more than 242,000 times. This was the first time a stealer had been found in Apple’s App Store.
> * The Android malware module would decrypt and launch an OCR plug-in built with Google’s ML Kit library, and use that to recognize text it found in images inside the gallery. Images that matched keywords received from the C2 were sent to the server. The iOS-specific malicious module had a similar design and also relied on Google’s ML Kit library for OCR. 


This is a nasty malware attack.  It not only takes over your device, looking for access to your crypto wallets, but it looks through your screenshots, looking for screenshots that contain text of critical passwords, such as those recovery keys for crypto wallets.

I wonder how many people took a screenshot of their emergency recovery keys, on the basis that it wasn’t a file on the desktop that was easy to search 


## [Why smart home devices should carry software support expiration dates | The Verge ](https://www.theverge.com/smart-home/607470/smart-appliances-expiration-date-security-updates-consumer-reports-survey)

[https://www.theverge.com/smart-home/607470/smart-appliances-expiration-date-security-updates-consumer-reports-survey](https://www.theverge.com/smart-home/607470/smart-appliances-expiration-date-security-updates-consumer-reports-survey)

> The good news is that most smart appliances are designed to carry out their primary function without an internet connection, so the simple fix when they’ve reached the end of their “smart” life is to disconnect them from Wi-Fi and carry on. This should make sure your aging smart thermostat doesn’t become the equivalent of an extra on _The Walking Dead_ — no longer alive but capable of great harm. 
> 
> However, in most cases, devices like Wi-Fi routers, smart speakers, and [streaming sticks](https://www.theverge.com/2023/5/31/23743515/google-chromecast-support-ending-2013) won’t work unless they’re online. If these devices aren’t getting security updates, you should stop using them immediately. Just this week, Taiwanese router maker Zyxel said it [wouldn’t patch two actively exploited vulnerabilities found in its routers](https://techcrunch.com/2025/02/05/router-maker-zyxel-tells-customers-to-replace-vulnerable-hardware-exploited-by-hackers) and told customers to stop using them. 
> 
> But how are you supposed to know when your smart home gadget has reached this fragile state? And wouldn’t you have liked to know this was going to happen _before_ you purchased it? Ideally, companies need to publicize how long they’ll support products and warn consumers once their devices are no longer secure. 


I’m torn on this one.  I totally agree that IoT devices should be supported, probably for a minimum period, recieve updates from the vendor, and generally be secure and patched.  I’d love for devices to continue to work even if not connected to the internet generally.  But otherwise this feels like it is actively calling for planned obselecence which can only increase waste, electronics in landfill, and is more likely to be used to drive profit based replacements rather than to improve security.

This is the kind of tough problem that requires consultation across industries, context specific application (I might care more about my internet routers than my washing machine for example).  It probably needs industry groups to create codes of practice and show adherence to them if they don’t want to see regulation coming down the line eventually. 


## [How Google Does It: How we secure our own cloud | Google Cloud Blog ](https://cloud.google.com/transform/how-google-does-it-secure-our-own-cloud/)

[https://cloud.google.com/transform/how-google-does-it-secure-our-own-cloud/](https://cloud.google.com/transform/how-google-does-it-secure-our-own-cloud/)

> Access control plays a central role in helping us secure our cloud environments and resources. We have an integration layer that sits on top of Google Cloud, providing governance, abstraction layers, and API compatibility. We use the built-in and write our own custom organization policies for our internal systems using the [Organization Policy Service](https://cloud.google.com/blog/products/identity-security/best-kept-security-secrets-harness-the-power-of-organization-policy-service) , which enable us to make and enforce decisions programmatically about what is permitted and disallowed, helping us to govern access and enforce compliance at the scale needed to support today's cloud users.
> 
> [..]
> 
> We also lean heavily into our [resource hierarchy](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) , enforcing different organization policies at different levels of the hierarchy, depending on the threat model. All these segmentations enable us to appropriately restrict access to data and minimize risks while still enabling the freedom to experiment.
> 
> As projects move closer to real-world production, we increase governance and limit the technologies available. For example, developers can experiment with an extensive range of solutions in our lower-level environments, but are much more governed and restricted in production environments. This helps balance rapid iteration and experimentation against maintaining a homogenous set of production infrastructure solutions. 


It’s nice to see a major cloud org showing how they “eat their own dog food”, and use their own system.

I note that this pyramid of permissions for developers feels fairly unusual compared to what I’ve seen in other orgs.  The idea that developers have a lot more control in pre-production environemnts is often true in practice, but often not because the central IT team has made it a policy.  And yet it makes a lot of sense, developers want a way to experiment and explore, but then commit the outputs into a more constrained system that restricts their access.

Secondly, I note a capability that Google has that you probably don’t have.  They have custom built an integration layer that sits atop their own cloud environment that  manages a set of governance rules.  It’s easy to argue that you should go all in on a cloud provider, but even if you do, you’ll need something, some process to wrap around your business structure and organisation.  If you are Google sized, you can probably invest time and energy into “engineering excellence”, into supporting your engineers with being as efficient and successful as possible.  It’s harder to justify at smaller scale, but I still think is important 


## [What is the probability that you can successfully assume an IAM role in a random AWS account? | by Michael Kirchner | Medium ](https://medium.com/@michael.kirchner/what-is-the-probability-that-you-can-successfully-assume-an-iam-role-in-a-random-aws-account-52dfa85cf077)

[https://medium.com/@michael.kirchner/what-is-the-probability-that-you-can-successfully-assume-an-iam-role-in-a-random-aws-account-52dfa85cf077](https://medium.com/@michael.kirchner/what-is-the-probability-that-you-can-successfully-assume-an-iam-role-in-a-random-aws-account-52dfa85cf077)

> Given the lists of valid IAM role ARNs of data set 1 and data set 2, the next step was to actually try and assume those roles. This is a sensitive step that should be approached with caution. Successful role assumptions will result in CloudTrail entries at the respective AWS accounts. They will also result in valid IAM session credentials being returned for accounts. I took the following steps to mitigate this:
> • Setting a custom user agent value that explains that this is research activity and includes a link where I can be contacted.
> • Setting a `DenyAll` session policy while assuming a role. This way, the credentials returned by the `sts:AssumeRole` API call will not actually provide any usable capabilities within a target account
> 
> For data set 1 (“Sourcegraph”), it was possible to assume ten IAM roles out of the 4,437 tested. This is a success rate of 0.2253%.
> For data set 2 (“Brute force”), it was possible to assume one IAM role out of the 15,010 tested, representing a success rate of 0.0066%. 


This is somewhat hair raising.  If any random AWS account on the internet can assume an admin role in your AWS organisation, then you really need to check your policies.  This should definitely be denied by default, as cross organisational role assumption should only happy because it was deliberate.

I thought this was a cute addition for the research though, by adding the DenyAll session policy, they can clearly demonstrate that not only did they not intend to carry out any malicious action, but that they explicitly put guard rails to prevent any accidental action on their part. 


## [Kept in the Dark – The 74 ](https://www.the74million.org/article/kept-in-the-dark/)

[https://www.the74million.org/article/kept-in-the-dark/](https://www.the74million.org/article/kept-in-the-dark/)

> That’s because the first people alerted following a school cyberattack are generally not the public nor the police. District [incident response plans](https://www.the74million.org/article/kept-in-the-dark/?location=minneapolis-public-schools_minnesota) place insurance companies and their phalanxes of privacy lawyers first. They take over the response, with a focus on limiting schools’ [exposure to lawsuits](https://www.the74million.org/article/kept-in-the-dark/?location=sweetwater-union-high-school-district_california) by aggrieved parents or employees. 
> 
> The attorneys, often employed by just a [handful of law firms](https://www.the74million.org/article/kept-in-the-dark/?location=truth-or-consequences-municipal-schools_new-mexico) — dubbed [breach mills](https://jolt.law.harvard.edu/assets/articlePDFs/v36/Schwarcz-Wolff-Woods-How-Privilege-Undermines-Cybersecurity.pdf) by one law professor for their massive caseloads — hire the forensic cyber analysts, crisis communicators and ransom negotiators on schools’ behalf, placing the discussions under the shield of attorney-client privilege. [Data privacy compliance](https://www.mcdonaldhopkins.com/insights/news/navigating-the-cybersecurity-landscape-mcdonald-hopkins-data-privacy-practice-group-grows-amid-surge-of-increased-incidents-in-2024) is [a growth industry](https://www.mullen.law/six-new-associates-join-mullen-coughlin-in-april/) for these specialized lawyers, who work to control the narrative.
> 
> The result: Students, families and district employees whose personal data was published online — from their financial and medical information to [traumatic events](https://www.the74million.org/article/kept-in-the-dark/?location=logansport-community-school-corporation_indiana) in young people’s lives — are left clueless about their exposure and risks to identity theft, fraud and other forms of online exploitation. Told sooner, they could have taken steps to protect themselves. 


A very american write up, I don’t think things are quite as bad in the UK and EU where breach reporting is far more regulkated.  But it’s a a good reminder that when an organisation is breached, it almost certainly has its first concerns around securing its systems, maximising profit (or reducing loss), and managing the legal risk.  It _should_ care about the impact on the users, but only really where that will affect the first few things.  It would require stronger regulation or insurance incentives around how much support breached organisations give to their customers to change behaviour in this space. 


## [Running Doom On An Apple Lightning To HDMI Adapter | Hackaday ](https://hackaday.com/2025/02/06/running-doom-on-an-apple-lightning-to-hdmi-adapter/)

[https://hackaday.com/2025/02/06/running-doom-on-an-apple-lightning-to-hdmi-adapter/](https://hackaday.com/2025/02/06/running-doom-on-an-apple-lightning-to-hdmi-adapter/)

> As the USB 2.0 link used with Lightning does not have the bandwidth for 1080p HDMI, compression was used, requiring a pretty beefy processor in the adapter. Some enterprising people at the time took a [hacksaw to one of these adapters](https://blog.panic.com/the-lightning-digital-av-adapter-surprise/) to see what’s inside them and figure out the cause of the visual artifacts. Inside is a 400 MHz ARM SoC made by Samsung lovingly named the S5L8747. The 256 MB of RAM is mounted on top of the package, supporting the RAM disk that the firmware is loaded into. 


Both fun traditional hacker project, but also a reminder.  Did you know that the little display adapter that you plug into your computer to connect a HDMI cable might have a 400 MHz Arm Processor and 256MB of RAM?  That’s beefy enough to … well, play Doom on for one! 


