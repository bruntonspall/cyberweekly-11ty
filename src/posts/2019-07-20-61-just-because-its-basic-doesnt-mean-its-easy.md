---
title: "61 - Just because it’s basic doesn’t mean it’s easy"
date: 2019-07-20
description: "There's a great post by Emma W of the NCSC linked below that talks about why patching is often described as basic, even though doing it can be really hard."
permalink: /just-because-its-basic-doesnt-mean-its-easy/
---

There's a great post by Emma W of the NCSC linked below that talks about why patching is often described as basic, even though doing it can be really hard.

GDS' has a number of design principles that it used when building GOV.UK as well as for teams building digital services today. One of my favourites is ["Do the hard work to make it simple"](https://www.gov.uk/guidance/government-design-principles#do-the-hard-work-to-make-it-simple).  I like that this goes counter to our normal narrative of "just", "simply" and "basic" that suggests that making something simple is easy.  Often, doing the most basic simple things is the hardest thing to do, because simple clean clear elegance takes a lot of hard work.

The Zoom exploit is a good version of this. The zoom team felt that they were making it simple for users to join a meeting, but doing it in such a way that honours someone's privacy and security decisions is actually really hard.

A good strategy for organisations is one that drastically focuses on the basics, on putting in all the hard work to get the basics right, not because the more advanced stuff is harder, but because the more advanced stuff tends to follow from the basics.  Do all the machine learning, AI, blockchain and quantum computing stuff you like, but if you haven't got the basics of patching, of monitoring, of security awareness down, then you aren't going to be able to make use of those technologies.  

I'm not a luddite, I don't think there's no value in those technologies, indeed, I think that many of them can be very valuable and useful in the right places, but they have to build on a good strong foundation, and if your focus is the innovative and the shiny, then you'll leave the basics alone because doing the basics is much harder and often feels less rewarding.

## [FBI senior IT official: Bug bounties still useful, but ‘a little over-hyped’](https://federalnewsnetwork.com/cybersecurity/2019/07/fbi-senior-it-official-bug-bounties-still-useful-but-a-little-over-hyped/)

[https://federalnewsnetwork.com/cybersecurity/2019/07/fbi-senior-it-official-bug-bounties-still-useful-but-a-little-over-hyped/](https://federalnewsnetwork.com/cybersecurity/2019/07/fbi-senior-it-official-bug-bounties-still-useful-but-a-little-over-hyped/)

> Manny Castillo, a senior IT security adviser at the FBI, said the bureau does all its penetration testing internally, and has no plans on changing that anytime soon. Bug bounty programs in government, he cautioned, remain “useful, but sometimes [they’re] a little overhyped.”
> 
> Castillo recalled several red team-blue team exercises that uncovered vulnerabilities when detailed to the National Security Agency. But three years out from those exercises, some of those same vulnerabilities, he said, remained unpatched.
> 
> “Keep that in mind: When you’re going to do it, fix it … if you don’t know what you have in the machines and you’re not patching and fixing these vulnerabilities, you’re really not doing a favor to [these] organizations,” Castillo said.


Sigh, looks like we’re still repeating this.  Before you can make use of a bug bounty program, you need to ensure that you have conducted standard security testing, that you have been able to fix those vulnerabilities and that you have a robust process for handling vulnerabilities that get identified.  If you don’t have those things, then you are going to waste money and annoy your security researchers if they can’t go public or see their vulnerabilities fixed.


## [My browser, the spy: How extensions slurped up browsing histories from 4M users | Ars Technica](https://arstechnica.com/information-technology/2019/07/dataspii-inside-the-debacle-that-dished-private-data-from-apple-tesla-blue-origin-and-4m-people/)

[https://arstechnica.com/information-technology/2019/07/dataspii-inside-the-debacle-that-dished-private-data-from-apple-tesla-blue-origin-and-4m-people/](https://arstechnica.com/information-technology/2019/07/dataspii-inside-the-debacle-that-dished-private-data-from-apple-tesla-blue-origin-and-4m-people/)

> As the founder of Internet hosting service Host Duplex, Jadali first looked into Nacho Analytics late last year after it published a series of links that listed one of his client domains. Jadali said he was concerned because those URLs led to private forum conversations—and only the senders and recipients of the links would have known of the URLs or would have the credentials needed to access the discussion. So how had they ended up on Nacho Analytics?
> 
> 
> Jadali suspected that the links were collected by one or more extensions installed on the browsers of people viewing the specialized URLs. He forensically tested more than 200 different extensions, including one called "Hover Zoom"—and found several that uploaded a user's browsing behavior to developer-designated servers. But none of the extensions sent the specific links that would later be published by Nacho Analytics.
> 
> Still curious how Nacho Analytics was obtaining these URLs from his client’s domain, Jadali tracked down three people who had initial access to the published links. He correlated time stamps posted by Nacho Analytics with the time stamps in his own server logs, which were monitoring the client’s domain. That’s when Jadali got the first indication he was on to something; two of his three users told him they had viewed the leaked forum pages with a browser that used Hover Zoom.


This is terrifying.  We’ve known for a while that browser extensions can access pretty much anything, but exactly what and how much and what they do with it is often obscured from users by vague contractual terms and deliberately concealing behaviour by the extension.

You really should only install extensions that you trust, sadly we have no good mechanism for determining the trust of a browser extension


## [Magecart Breaches Websites Via Misconfigured Amazon S3 Buckets](https://www.riskiq.com/blog/labs/magecart-amazon-s3-buckets/)

[https://www.riskiq.com/blog/labs/magecart-amazon-s3-buckets/](https://www.riskiq.com/blog/labs/magecart-amazon-s3-buckets/)

> These actors automatically scan for buckets which are misconfigured to allow anyone to view and edit the files it contains. Once the attackers find a misconfigured bucket, they scan it for any JavaScript file (ending in .js). They then download these JavaScript files, append their skimming code to the bottom, and overwrite the script on the bucket. This technique is possible because of the misconfigured permissions on the S3 bucket, which grants the write permission to anyone.
> 
> These attackers have been active in web skimming for a long time using other techniques, but they started compromising unsecured S3 buckets in early April. According to RiskIQ data, the group has managed to compromise a vast collection of S3 buckets to impact well over 17,000 domains. This list includes websites in the top 2,000 of Alexa rankings as well.


😱

That’s a lot of misconfiguration buckets on S3!

MageCart have been responsible for a lot of credit card data breaches, and are showing themselves to be a highly technical and competent criminal organisation.  They have primarily been conducting financially motivated fraud, so this an interesting twist for them.

But buckets that allow global writing, and then modifying the JavaScript in the bucket is a nasty attack.  Remember that AWS has security scanning tools that can tell you if anyone in your account has created a bucket that is against policy and warn you (and the developer).  This shouldn’t still be happening today.


## [Hacker who stole 620 million records strikes again, stealing 127 million more | TechCrunch](https://techcrunch.com/2019/02/14/hacker-strikes-again/)

[https://techcrunch.com/2019/02/14/hacker-strikes-again/](https://techcrunch.com/2019/02/14/hacker-strikes-again/)

> Now the same hacker has eight additional marketplace entries after their original listings were pulled offline, including:
> 
> * 18 million records from travel booking site Ixigo
> * Live-video streaming site YouNow had 40 million records stolen
> * Houzz, which recently disclosed a data breach, is listed with 57 million records stolen
> * Ge.tt had 1.8 million accounts stolen
> * 450,000 records from cryptocurrency site Coinmama.
> * Roll20, a gaming site, had 4 million records listed
> * Stronghold Kingdoms, a multiplayer online game, had 5 million records listed
> * 1 million records from pet care delivery service PetFlow


I wonder how much crossover there is between RPG nerds and InfoSec people.  I had an account with Roll20, and as such was notified of this via HaveIBeenPwned.

Good thing I use a password manager with randomly generated passwords then! (But not generated using my polyhedral dice, although a dice ware implementation that allows me to roll 3D10+2 might be nice)


## [MITM on all HTTPS traffic in Kazakhstan](https://bugzilla.mozilla.org/show_bug.cgi?id=1567114)

[https://bugzilla.mozilla.org/show_bug.cgi?id=1567114](https://bugzilla.mozilla.org/show_bug.cgi?id=1567114)

> The Government of Kazakhstan has already started to use the certificate for MITM.
> [...]
> Internet providers via SMS inform us about the need to install this certificate that can be downloaded from their websites


(Joel) Decrypting network traffic (usually HTTPS for web content inspection) via 'Man-in-the-Middle' (MiTM) _can_ be a powerful tool when precisely leveraged by mature, privacy-focused and appropriately permitted network administrators but in most cases MiTM is poorly implemented and under-utilised (adding more frustration than security) and sometimes even outright privacy-invasive while reducing security instead of improving it.

[Generally, we should stop conducting MiTM](https://medium.com/@joelgsamuel/can-we-stop-intercepting-user-traffic-aka-man-in-the-middle-please-2a00de208d4b) in ecosystems we can already control/audit.

Kazakhstan has taken this much, _much_ further by asking its citizens to deploy a [root certificate](https://en.wikipedia.org/wiki/Root_certificate) so that it can MiTM the entire country's web traffic. It is unclear whether high-privacy sites will also be inspected (for example, online banking) and examples from those in-country have shown Facebook.com as being intercepted. This is... problematic... at best.

Mature root certificate trust store distributors (Microsoft for Windows, Apple for macOS/iOS, Mozilla etc) have standing policies to reject/block any attempts to distribute root certificates through their schemes so of course Kazakhstan is resorting to asking individuals to manually install the offending certificate to allow their web traffic to be intercepted for unknown purposes. The cheek/horror.

(Michael) There is a good discussion of this over at [the mozilla security policy mailing list](https://groups.google.com/forum/m/#!msg/mozilla.dev.security.policy/wnuKAhACo3E/cpsvHgcuDwAJ) which makes clear that someone, such as Kazakhstan wanting a SuperCA style certificate, must ensure that it meets the baseline requirements, including validating that every certificate issued is only issued to an organisation that has control of the domain certified.  It should be impossible for any MITM CA to meet this criteria, and as such it will never be added to the global trust root.

The more interesting question here is whether the browser user manually installing a CA certificate knows what they are doing.  Firefox currently assumes that you do, and even disables certificate pinning in these circumstances!  That combined with the dual use of this certificate (Kazakhstan use the same certificate to generate the TLS certificates for the citizen facing government services) means that users are quite likely to install the certificate without realising the impact of doing so


## [Intention to fine British Airways £183.39m under GDPR for data breach | ICO](https://ico.org.uk/about-the-ico/news-and-events/news-and-blogs/2019/07/ico-announces-intention-to-fine-british-airways/)

[https://ico.org.uk/about-the-ico/news-and-events/news-and-blogs/2019/07/ico-announces-intention-to-fine-british-airways/](https://ico.org.uk/about-the-ico/news-and-events/news-and-blogs/2019/07/ico-announces-intention-to-fine-british-airways/)

> Following an extensive investigation the ICO has issued a notice of its intention to fine British Airways £183.39M for infringements of the General Data Protection Regulation (GDPR).
> 
> The proposed fine relates to a cyber incident notified to the ICO by British Airways in September 2018. This incident in part involved user traffic to the British Airways website being diverted to a fraudulent site. Through this false site, customer details were harvested by the attackers. Personal data of approximately 500,000 customers were compromised in this incident, which is believed to have begun in June 2018.


This is a record fine and one of the first under the new GDPR regime, and of course BA are saying that they are going to contest the fine.

This relates to the MageCart breach that we first covered in [CyberWeekly 17](http://cyberweekly.net/how-do-normal-users-make-good-security-decisions), whereby the MageCart criminal gang was able to insert malicious code into one of the JavaScript libraries used by BA’s payment system.  We still don’t know how this was achieved, but hopefully when the ICO puts out its full judgement decision, we’ll find out whether it was the use of compromised developer credentials, or some exploit of a web vulnerability, or something else.


## [Intention to fine Marriott International, Inc more than £99 million under GDPR for data breach | ICO](https://ico.org.uk/about-the-ico/news-and-events/news-and-blogs/2019/07/intention-to-fine-marriott-international-inc-more-than-99-million-under-gdpr-for-data-breach/)

[https://ico.org.uk/about-the-ico/news-and-events/news-and-blogs/2019/07/intention-to-fine-marriott-international-inc-more-than-99-million-under-gdpr-for-data-breach/](https://ico.org.uk/about-the-ico/news-and-events/news-and-blogs/2019/07/intention-to-fine-marriott-international-inc-more-than-99-million-under-gdpr-for-data-breach/)

> Following an extensive investigation the ICO has issued a notice of its intention to fine Marriott International £99,200,396 for infringements of the General Data Protection Regulation (GDPR).
> 
> The proposed fine relates to a cyber incident which was notified to the ICO by Marriott in November 2018. A variety of personal data contained in approximately 339 million guest records globally were exposed by the incident, of which around 30 million related to residents of 31 countries in the European Economic Area (EEA). Seven million related to UK residents.
> 
> It is believed the vulnerability began when the systems of the Starwood hotels group were compromised in 2014. Marriott subsequently acquired Starwood in 2016, but the exposure of customer information was not discovered until 2018. The ICO’s investigation found that Marriott failed to undertake sufficient due diligence when it bought Starwood and should also have done more to secure its systems.


This is a far more dodgy judgment in my opinion, but we don’t have the facts to know what due diligence was carried out by Marriott when they acquired Starwood, and it might be that the breach was obvious, but given that all the fingers on this one pointed at a state level actor, I’m dubious about what form of due diligence would have been possible to detect this breach here.  Again, we’ll find out when the technical judgement is released.


## [What a very bad day at work taught me about building Stack Overflow’s community - Stack Overflow Blog](https://stackoverflow.blog/2019/07/18/building-community-inclusivity-stack-overflow/)

[https://stackoverflow.blog/2019/07/18/building-community-inclusivity-stack-overflow/](https://stackoverflow.blog/2019/07/18/building-community-inclusivity-stack-overflow/)

> About three months in, on a Friday afternoon, we introduced a new company-wide policy that I felt was relatively benign. What happened next was that, from my point of view, the engineering team completely lost it. No one agreed with this policy, and they made it known over seemingly hundreds of Slack pings. After an afternoon of going back and forth, I walked away feeling emotionally drained. What had happened to my amazing coworkers that were so kind and wonderful? I felt attacked and diminished. It seemed people weren’t valuing my work or my judgment. 
> 
> I went home for the weekend and stewed in my frustration. I replayed everything that happened in my head and each time got more frustrated with the way people reacted. When Sunday rolled around, I decided I wanted to look back at our Slack conversations and see which one of my coworkers was being the rudest and the most unreasonable. I wanted to give them direct feedback that they had hurt my feelings. 
> 
> As I went back through that Friday afternoon chat log, I was shocked to see that no one had been hurling insults. There was no one saying mean things about me or attacking my efficacy directly. In fact, what I found was that people had some well put together arguments about why they felt this policy was a bad idea. The entire engineering department definitely made their criticisms known, but I didn’t find people questioning my ability as a manager, throwing around insults, or saying anything that that illustrated why I was feeling so targeted. 
> 
> That was when something became crystal clear: my coworkers hadn’t become monsters, they were still the kind and caring people I thought they were. The monster in this case is not one person, it was created when lots of people, even with great intentions, publicly disagreed with you at the same time. Even kind feedback can come off as caustic and mean when there is a mob of people behind it. No matter how nicely they say it, when a large group of people you really respect publicly challenge something you’ve done it can feel like a personal attack. 


When we experience feedback like this, we tend to remember the emotions over the reality of the experience.  This causes our brains to rewrite out history of the event and remember things not as they happened, but subjectively how we felt.  We remember being attacked, people being difficult, but the reality might be different.

As people in security, in transformation, in management, we are often telling people things they don’t want to hear, things that they don’t like about how they behave or their current practices.  This can result in a lot of feedback, which we can remember emotively rather than what was actually said.  This is why tools like slack or online tools for gathering feedback can make it easier for us to experience the emotion, but then to relax and come back with a fresh head to examine later, in a more logical manner.  This can help us to receive and understand the feedback we are getting rather than simply react to it.


## [New Azure Active Directory capabilities help you eliminate passwords at work](https://www.microsoft.com/en-us/microsoft-365/blog/2019/07/10/new-azure-active-directory-capabilities-eliminate-passwords/)

[https://www.microsoft.com/en-us/microsoft-365/blog/2019/07/10/new-azure-active-directory-capabilities-eliminate-passwords/](https://www.microsoft.com/en-us/microsoft-365/blog/2019/07/10/new-azure-active-directory-capabilities-eliminate-passwords/)

> Today, we’re announcing the public preview of FIDO2 security keys support for passwordless sign-in to Azure Active Directory (Azure AD). Using a FIDO2 security key, the Microsoft Authenticator app, or Windows Hello, all Azure AD users can now sign in without using a password.
> These strong authentication factors are based off the same world class, public key/private key encryption standards and protocols, which are protected by a biometric factor (fingerprint or facial recognition) or a PIN. Users apply the biometric factor or PIN to unlock the private key stored securely on the device. The key is then used to prove who the user and the device are to the service.


This is really important news, even in public preview.  

If you were to do one thing, issuing FIDO2 security keys, such as YubiKeys, to all of your AD admins, and changing the AD Admin accounts to only allow authentication by FIDO2 key will massively reduce the ease for attackers to use tools like MimiKatz to steal admin passwords, phishing to steal your admin passwords, or malware to steal the passwords as they are typed in.

If your administrative accounts use this kind of tool, then I think you are probably immune to the majority of attacks out there today.  I’m sure that as more people use this, attacks on FIDO2 keys will come out (no technology is perfect), but until then, you’ll have reduced one of the biggest targets on your back and stopped many attackers dead in their tracks


## [Zoom Will Fix the Flaw That Let Hackers Hijack Webcams | WIRED](https://www.wired.com/story/zoom-flaw-web-server-fix/)

[https://www.wired.com/story/zoom-flaw-web-server-fix/](https://www.wired.com/story/zoom-flaw-web-server-fix/)

> Zoom is also moving ahead with the tweak it announced on Monday night that will give users more control over their default setting for auto-join video. That update will go out on July 12.
> 
> "On the one hand it took over 100 days for them to actually take this seriously and it required public outcry," Leitschuh says. "On the other hand it's a really good thing to see that a company can apologize for their mistakes and be willing to work with the community and researchers. It's now on all of us to hold them accountable."
> 
> In recounting its months-long interaction with Leitschuh, Zoom said in its Monday statement, "Our Security and Engineering teams engaged the researcher and were in frequent contact over the subsequent period. This engagement included disagreement about the severity of the meeting join concern. Ultimately, Zoom decided not to change the application functionality."
> 
> The company seems to have pivoted in just a few hours, though, perhaps because of unexpected uproar from users, even those outside the technical community.


I only briefly mentioned the [Zoom debacle](https://medium.com/bugbountywriteup/zoom-zero-day-4-million-webcams-maybe-an-rce-just-get-them-to-visit-your-website-ac75c83f4ef5) in passing last week because of other priorities.  I think this write up in wired covered it all quite well.  Zoom very firmly denied that this was a significant security flaw at first, and only when it felt like the entire security research community was up in arms against them did they change their mind and agree to patch things.

This flaw was a a breach of the old adage that security and usability are opposite sides of the same coin.  I’ve long held the view that this isn’t actually true, that good security is usable security.  But in this case, Zoom wanted users to be able to click a single link and ensure that they joined a meeting, with the web cam enabled, and everything working.  However, from a privacy perspective, users almost always want to take an affirmative action before their webcam is turned on, and sadly visiting links is far too easy to automate, such that it means that peoples cameras can be turned on without their knowledge.


## [The problems with patching - NCSC](https://www.ncsc.gov.uk/blog-post/the-problems-with-patching)

[https://www.ncsc.gov.uk/blog-post/the-problems-with-patching](https://www.ncsc.gov.uk/blog-post/the-problems-with-patching)

> Vulnerabilities in technology are always being discovered and in response, vendors regularly issue security updates to plug the gaps. Applying these updates - a process commonly known as patching - closes vulnerabilities before attackers can exploit them. Patching can also fix bugs, add new features, increase stability, and improve look and feel (or other aspects of the user experience).
> 
> So patching matters for more than just security reasons. It ensures you're getting most from your IT, and that it's working smoothly with other people and organisations.
> 
> For all these reasons, patching remains the single most important thing you can do to secure your technology, and is why applying patches is often described as 'doing the basics'. But although applying patches may be a basic security principle, that doesn't mean it's always easy to do in practice.


Excellent advice here from Emma W at the NCSC.  Patching should be your first tool in your cyber defence toolkit, but it cannot be your only tool.  There are lots of valid reasons why individual systems might be hard to patch.  When that’s the case, there are compensatory actions you can take that compensate for the lack of ability to patch.

What Emma doesn’t say here is that if you have systems that fall into the categories of hard to patch, using those compensatory defence in depth principles is not enough.  You should also look to rework the conditions that make it hard to patch to try to make it easier to patch.  If you have a system that you cannot patch because someone hosts it for you, then come contract renewal time, consider putting in patch SLA’s into the renewal contract, so that you can request patches in the future.


