---
title: "73 - Know your users"
date: 2019-10-12
description: "We often engage with proxies for our real users.  It doesn't matter whether you are building a product that you sell, or writing policy for an organisation, you have real users and then you have decision makers."
permalink: /know-your-users/
---

We often engage with proxies for our real users.  It doesn't matter whether you are building a product that you sell, or writing policy for an organisation, you have real users and then you have decision makers.

The decision makers are the ones who are most visible to us by default.  They're the ones who will buy our product, and thus they are the ones who will look at the marketing, the feature lists or the cost.  But the product they buy will be inflicted on others in the organisation.

If you want to think of this experience yourself, just think about the last time you had to book travel or claim an expense.  I know people who have said that one of the questions that they ask when interviewing at a company is "what expenses system do you use?", give the wrong answer and they don't want to work there (at least not in any job that requires regular filing of expenses.  These systems are sold to the procurement team or the finance team, and sold with lots of ability to get users to correctly categorise and file their expenses in a way that makes finances job easier.  But many of them are actively hostile to the user, requiring the invocation of dark incantations and special commands to get even simple expenses into the system.

The same is true of many of our policies.  You could look at a social media policy in organisations, and many are designed to be read by the executive board, do not tell staff what they can do, but is covered in dire warnings that engaging in any social media contact is forbidden.  One organisation I worked with had a social media team of 4 people, all of whom had to work from their personal mobile phones, because the IT policy forbade access to Facebook or Twitter, and the departmental social media policy forbid them from mentioning anything about the organisation online.  The authors of those policies were not thinking about the users, the end users who would have to comply with the policy.

Our security policies are often the same.  You should always ask yourself the question "Who is supposed to read this and what do I want them to know?".  Acceptable use policies that make reference to Section 3 Paragraph 2(a) of the Computer Misuse Act (1990), or Section 1, Paragraph 4(b) of the Official Secrets Act (1989) is almost certainly not useful to the end user.  What are they allowed to do? What are they not allowed to do?

I've heard it attributed to Reed Hastings, CEO of Netflix, but this quote is one I use quite often:

> Policies are organizational scar tissue. They are codiﬁed overreactions to unlikely-to-happen-again situations.

If instead we write user centered policies and procedures, then we can be confident that users are clear on what is acceptable use, that they know whether they can tweet about their work, or ring their nursery from a work phone, and that they are covered and protected by the organisation.  That is what leads to better outcomes and safer organisations.

## [Former Yahoo engineer pleads guilty to hacking user emails in search for porn | ZDNet](https://www.zdnet.com/article/former-yahoo-engineer-pleads-guilty-to-hacking-user-emails-in-search-for-porn/)

[https://www.zdnet.com/article/former-yahoo-engineer-pleads-guilty-to-hacking-user-emails-in-search-for-porn/](https://www.zdnet.com/article/former-yahoo-engineer-pleads-guilty-to-hacking-user-emails-in-search-for-porn/)

> According to court documents, Ruiz used the access to Yahoo!'s internal network that his job provided to crack users' passwords and gain access to their email accounts.
> 
> In total, he accessed about 6,000 accounts, most belonging to younger women, including personal friends and work colleagues.
> 
> Once in, he searched and downloaded images and videos, which he stored at home on a hard drive.
> 
> Ruiz also used access to the hacked Yahoo! email inboxes to compromise accounts at services like Apple iCloud, Facebook, Gmail, DropBox, and others, where the victims used the Yahoo! email address to register accounts.
> 
> He did this by requesting password resets on the third-party sites, which he received inside the victim's Yahoo! inboxes. Ruiz then continued his search of personal images and videos on these new accounts.


This is the terrifying insider threat that we should be worried about with tools like Office 365, Google Suite and other cloud tools.  The rogue system administrator who abuses their position of power to carry out some nefarious purposes of their own, whether illegal access to individuals photos, or stealing money or data.  Luckily these attacks are quite rare, but suppliers should be clear with us how they act to protect against this kind of attack, whether that be internal audit controls, or customer accessible audit logs, you should be confident that your supplier has controls in place.

[I'll also add an unusual bit of social commentary.  Photos that are stolen from individuals, even if they contain nudity or are of a sexual nature are not porn, and I don't think that's the right terminology to use in this headline.]


## [DOH Letter 209-19-19 [pdf]](https://www.ncta.com/sites/default/files/2019-09/Final%20DOH%20LETTER%209-19-19.pdf)

[https://www.ncta.com/sites/default/files/2019-09/Final%20DOH%20LETTER%209-19-19.pdf](https://www.ncta.com/sites/default/files/2019-09/Final%20DOH%20LETTER%209-19-19.pdf)

> Moreover, the centralized control of encrypted DNS threatens to harm consumers by interfering with a wide range of services provided by ISPs (both enterprise and public-facing) and others. Over the last several decades, DNS has been used to build other critical internet features and functionality including: 
> (a) the provision of parental controls and IoT management for end users; 
> (b) connecting end users to the nearest content delivery networks, thus ensuring the delivery of content in the fastest, cheapest, and most reliable manner; 
> and (c) assisting rights holders’ and law enforcement’s efforts in enforcing judicial orders in combatting online piracy, as well as law enforcement’s efforts in enforcing judicial orders in combatting the exploitation of minors. 


Note that users don't actually want two of these features, and the one that they do, cdn load balancers, will work just fine using DNS-over-HTTPS because the HTTPS nature of the the tunnel doesn't prevent the end DNS server from knowing who you are.

The real issue that the ISP's have with DNS over HTTP is that they've been sniffing DNS traffic for advertising and commercial purposes for some time and this threatens to reduce their income stream.

There are some issues with the DNS over HTTPS proposals by Firefox and Google at the moment, in particular the fact that this is likely to be delivered by the browser, rather than the operating system, means that operating system level controls and user preferences wont be honoured.  Additionally, many enterprises currently use DNS query traffic to determine if an endpoint is compromised, and to return specific blackhole addresses for command and control traffic for known malware, meaning that the malware can be rendered inert.  DNS over HTTPS (DoH) as a fundamental protocol doesn't prevent this, if enterprises roll out end user device monitoring, they can inspect the traffic on the device before it's encrypted.  They could also deploy their own DoH servers, providing the privacy guarantees for their users when on the move, while still capturing the traffic.  Google and Mozilla's implementation at the browser layer might cause issues here, but on corporate devices, corporations should be able to turn this off, or change the settings to point at their implementation


## [COMpfun successor Reductor infects files on the fly to compromise TLS traffic | Securelist](https://securelist.com/compfun-successor-reductor/93633/)

[https://securelist.com/compfun-successor-reductor/93633/](https://securelist.com/compfun-successor-reductor/93633/)

> The malware adds digital certificates from its data section to the target host and allows the operators to add additional certificates remotely through a named pipe. The solution that Reductor’s developers found to mark TLS traffic is the most ingenious part. They don’t touch the network packets at all; instead developers analyzed the Firefox source code and Chrome binary code to patch the corresponding pseudo random number generation (PRNG) functions in the process’s memory.
> 
> We initially observed that infected installers were downloaded from HTTPS warez websites; but, as often happens, the files themselves were downloaded through unencrypted HTTP. This makes it technically possible to replace the files with malicious ones during the download process. Interestingly, the configuration data of some samples contained very popular legitimate websites. We really don’t think they were compromised to serve as control servers.
> 
> In any case, we didn´t initially know how the installers were infected, because the original downloaded files were no longer available for analysis on the warez websites. And there was always the possibility that the installers were infected on the website from which they were originally downloaded.
> 
> Then more recent Reductor telemetry gave us a clue. This time samples were again being downloaded from warez websites, but we were able to confirm that in this new case the original installers were not infected. This allowed us to confirm that Reductor’s operators have some control over the target’s network channel and could replace legitimate installers with infected ones on the fly.


So this threat actor has sufficient control over the network of the people it is targeting to deliver compromised binaries from "warez" websites in place of the original from the server.  And those binaries then mark TLS connections , presumably for cryptanalysis or simple network analysis later.  An infected computer would signal every website that it went to with the marked certificates.


## [Recent cyberattacks require us all to be vigilant - Microsoft on the Issues](https://blogs.microsoft.com/on-the-issues/2019/10/04/recent-cyberattacks-require-us-all-to-be-vigilant/)

[https://blogs.microsoft.com/on-the-issues/2019/10/04/recent-cyberattacks-require-us-all-to-be-vigilant/](https://blogs.microsoft.com/on-the-issues/2019/10/04/recent-cyberattacks-require-us-all-to-be-vigilant/)

> In a 30-day period between August and September, the Microsoft Threat Intelligence Center (MSTIC) observed Phosphorus making more than 2,700 attempts to identify consumer email accounts belonging to specific Microsoft customers and then attack 241 of those accounts. The targeted accounts are associated with a U.S. presidential campaign, current and former U.S. government officials, journalists covering global politics and prominent Iranians living outside Iran. Four accounts were compromised as a result of these attempts; these four accounts were not associated with the U.S. presidential campaign or current and former U.S. government officials.
> 
> [...]
> 
> While the attacks we’re disclosing today were not technically sophisticated, they attempted to use a significant amount of personal information both to identify the accounts belonging to their intended targets and in a few cases to attempt attacks. This effort suggests Phosphorus is highly motivated and willing to invest significant time and resources engaging in research and other means of information gathering.


Note that advanced actors aren't necessarily technically advanced.  But they are persistent at trying, and can attack accounts at a scale that is worrying.


## [ESET discovers Attor, a spy platform with curious GSM fingerprinting | WeLiveSecurity](https://www.welivesecurity.com/2019/10/10/eset-discovers-attor-spy-platform/)

[https://www.welivesecurity.com/2019/10/10/eset-discovers-attor-spy-platform/](https://www.welivesecurity.com/2019/10/10/eset-discovers-attor-spy-platform/)

> Attor is an espionage platform, used for highly targeted attacks against high-profile users in Eastern Europe, and Russian-speaking, security-concerned users.
> 
> The malware, which has flown under the radar since 2013, has a loadable-plugin architecture that can be used to customize the functionality to specific victims. It includes an unusual plugin for GSM fingerprinting that utilizes the rarely used AT command set, and incorporates Tor with the aim of anonymity and untraceability.
> 
> Our research provides a deep insight into the malware and suggests that it is well worth further tracking of the operations of the group behind i


This is an interesting platform, modular, the use of TOR as a communication system and total isolation for a number of modules from the networking aspect mean that this is a highly competent actor.


## [Microsoft repairs 59 software bugs on a 'quiet' Patch Tuesday](https://www.scmagazine.com/home/security-news/vulnerabilities/microsoft-repairs-59-software-bugs-on-a-quiet-patch-tuesday/)

[https://www.scmagazine.com/home/security-news/vulnerabilities/microsoft-repairs-59-software-bugs-on-a-quiet-patch-tuesday/](https://www.scmagazine.com/home/security-news/vulnerabilities/microsoft-repairs-59-software-bugs-on-a-quiet-patch-tuesday/)

> Four of the critical flaws consisted of memory corruption bugs that can surface when the Chakra scripting engine handles certain objects in memory in the Microsoft Edge web browser (CVE-2019-1366, CVE-2019-1307, CVE-2019-1308 and CVE-2019-1335). These flaws can be exploited to trigger remote code execution, potentially allowing attackers to install programs, manipulate data or create privileged accounts.
> 
> “In a web-based attack scenario, an attacker could host a specially crafted website that is designed to exploit the vulnerability through Microsoft Edge and then convince a user to view the website,” Microsoft explains in its multiple advisories. The attacker could also take advantage of compromised websites and websites that accept or host user-provided content or advertisements. These websites could contain specially crafted content that could exploit the vulnerability.


Sigh, the wording of this is quite poor.  It implies that attackers would need to conduct significant effort to carry out a remote code execution attack, but in reality we all browse random websites all the time with very little thought.  

This could have been exploited via phishing, creating a wireless hotspot at a local cafe, or just creating a random website and getting traffic to it.

Reminder to try, as much as possible, to apply your patches as soon as you can, especially to your desktop estates.


## [The Artificial Intelligence Arms Race: Trends and World Leaders in Autonomous Weapons Development - Haner - 2019 - Global Policy - Wiley Online Library](https://onlinelibrary.wiley.com/doi/full/10.1111/1758-5899.12713)

[https://onlinelibrary.wiley.com/doi/full/10.1111/1758-5899.12713](https://onlinelibrary.wiley.com/doi/full/10.1111/1758-5899.12713)

> As the AI arms race rages on, the stakes remain high yet public debate is lacking. Sixty‐one per cent of citizens polled across more than twenty countries oppose the development of lethal AWS, and yet billions of their tax dollars are being spent on their development each year (CSKR, 2019). France, Germany, and others have advocated use of the Convention on Certain Weapons (CCW) process to develop ‘Possible Guiding Principles’ as a code of conduct to encourage AWS development to stay in accordance with existing international law (Convention on Certain Weapons, 2018). Beyond that, 28 states have called for a ban on killer robots, and further the Non‐aligned Movement and a group of African states desire to negotiate a new international treaty to set limits on robotic killing. Previous weapons bans, from chemical and biological weapons to landmines and cluster munitions, have been effective policy tools which significantly curtailed the use of these problematic weapons. While the United States is not currently in a position to lead with its ill‐fated ‘America First’ policy, the EU and other forward‐thinking countries should attempt to set solid global norms and push for a ban on the use of AWS now. China announced last year that it wishes to ban the battlefield use of AWS, but not their development and production.


The amount of money being spent on AI for AWS by governments is astonishing.  Not that AWS, we mean Autonomous Weapons Systems, that's drones, airplanes and other vehicles that can engage in fighting without the aid of a human pilot.

A lot of existing drone technology enables autonomous flight, so that they can get into position, and then a human operator can take over when needed, but this is about drones that can engage in aerial combat without oversight.  Clearly countries see autonomous weapons as being the solution to the natural loss of life that occurs when military engagements happen.  But what would this mean for asymmetric warfare?  If a country has fleets of AI powered weapons and can engage a country that doesn't, then every death of a combatant is a cost to the second country.  Invasions would become bloodless to the invaders and therefore one of the major policy controls preventing countries going to war, the civil unrest at home caused by the loss of life, would be neutralised.  This could lead to significant uptick in military activity, and of course, while banning the battlefield use, but continuing R&D would limit it's abuse, those who develop such systems will want to sell them or their use around the world, to other, less fortunate countries who can't develop their own.


## [Mapping the Deepfake Landscape - Deeptrace](https://deeptracelabs.com/mapping-the-deepfake-landscape/)

[https://deeptracelabs.com/mapping-the-deepfake-landscape/](https://deeptracelabs.com/mapping-the-deepfake-landscape/)

> Another key trend we identified is the prominence of non-consensual deepfake pornography, which accounted for 96% ofthe total deepfake videos online. We also found that the top four websites dedicated to deepfake pornography received more than 134 million views on videos targeting hundreds of female celebrities worldwide. This significant viewership demonstrates a market for websites creating and hosting deepfake pornography, a trend that will continue to grow unless decisive action is taken.
> 
> Deepfakes are also making a significant impact on the political sphere. Two landmark cases f rom Gabon and Malaysia that received minimal Western media coverage saw deepfakes linked to an alleged government cover-up and a political smear campaign. One of these cases was related to an attempted military coup, while the other continues to threaten a high- profile politician with imprisonment. Seen together, these examples are possibly the most powerful indications of how deepfakes are already destabilizing political processes. Without defensive countermeasures, the integrity of democracies around the world are at risk.
> 
> Outside of politics, the weaponization of deepfakes and synthetic media is influencing the cybersecurity landscape, enhancing traditional cyber threats and enabling entirely new attack vectors. Notably, 2019 saw reports of cases where synthetic voice audio and images of non-existent, synthetic people were used to enhance social engineering against businesses and governments.


Deepfake's are currently almost exclusively publically available for pornography purposes, with the remaining 4% being a mix, but includes politicians and news presenters (presumably some of the better known examples come from demonstrations like this).

This shouldn't really surprise anyone, but the report goes into a few more troubling details.  The two reports of deepfakes in the political sphere have both appeared to have been denied and there's little computer forensics to backup the deepfake claim.  But the fact that politicians can claim that the videos are fakes is worrying by itself, as it destroys and diminishes trust, especially in time poor journalists who are eager for clicks and unlikely to have the tools or knowledge to determine if something is fake or not.

Additionally the report covers "Shallowfakes", clips where the context is altered, time is sped up or slowed down, or there is deceptive editing to adjust scrolling headlines on news clips.  This is a far more common occurrence and the examples are from videos released by mainstream western organisations, not just niche political edges or less media aware organisations.


## [Experts: Spy used AI-generated face to connect with targets](https://apnews.com/bc2f19097a4c4fffaa00de6770b8a60d)

[https://apnews.com/bc2f19097a4c4fffaa00de6770b8a60d](https://apnews.com/bc2f19097a4c4fffaa00de6770b8a60d)

> Katie Jones sure seemed plugged into Washington’s political scene. The 30-something redhead boasted a job at a top think tank and a who’s-who network of pundits and experts, from the centrist Brookings Institution to the right-wing Heritage Foundation. She was connected to a deputy assistant secretary of state, a senior aide to a senator and the economist Paul Winfree, who is being considered for a seat on the Federal Reserve.
> 
> But Katie Jones doesn’t exist, The Associated Press has determined. Instead, the persona was part of a vast army of phantom profiles lurking on the professional networking site LinkedIn. And several experts contacted by the AP said Jones’ profile picture appeared to have been created by a computer program.
> 
> “I’m convinced that it’s a fake face,” said Mario Klingemann, a German artist who has been experimenting for years with artificially generated portraits and says he has reviewed tens of thousands of such images. “It has all the hallmarks.”


This is an older story, but relevant.  Artificially generated faces are being used as the front for espionage attempts using LinkedIn.  The ability to create a new face from nothing means that the typical defense against this (that nobody outside of infosec would ever do), which is to do a Google reverse image search of a potential LinkedIn or Facebook friend request to see if the picture is stolen from elsewhere, just wont work anymore.


## [100,000 AI-Generated Faces – Free to Download!](https://generated.photos/)

[https://generated.photos/](https://generated.photos/)

> These people aren't real!
> 
> We are building the next generation of media through the power of AI. Copyrights, distribution rights, and infringement claims will soon be things of the past.
> 
> To give you a glimpse of what we have been working on we created a free resource of 100k high-quality faces. Every image was generated by our internal AI systems as it continually improves. Use them in your presentations, projects, mockups or wherever — all for just a link back to us!


The idea that we can have royalty and copyright free images of people, of faces, for use in stock photos means that we wont be able to trace professional models between photos such as in the [Distracted Boyfriend meme](https://knowyourmeme.com/memes/distracted-boyfriend#photo-series-compilations).

More interestingly is what these stock photos will be used for.  Phishing, cat-phishing, and false profiles probably.  Will the suppliers of these do anything to provide social networks with the ability to detect the use of these photos so they can warn their users?


## [#DIGITALARMY USING SOCIAL MEDIA IN THE BRITISH ARMY [pdf]](https://www.army.mod.uk/media/4612/adr007595-asm_guide.pdf)

[https://www.army.mod.uk/media/4612/adr007595-asm_guide.pdf](https://www.army.mod.uk/media/4612/adr007595-asm_guide.pdf)

> If you think you are posting something worthy of being re-posted on the Army’s corporate channels, let your Unit Press
> Officer know in advance to exploit other channels and reach the widest audience.
> 
> Online defence forums have international reach and are monitored by other armies and journalists. Assume that any posts you make will be picked up, re-posted and aired
> on mainstream channels. Anonymity is not a safe assumption


This is lovely guidance.  There's a good amount of warning about engaging appropriately online, not engaging the wrong people or bringing the army into disrepute, but also a certain amount of active encouragement to use social media including contacting the social media team if you want them to retweet stuff and so on.

This is what good policy documents look like.


## [Thread by @random_walker: "My university just announced that it’s dumping Blackboard, and there was much rejoicing. Why is Blackboard universally reviled? There’s a st […]"](https://threadreaderapp.com/thread/1182635589604171776.html)

[https://threadreaderapp.com/thread/1182635589604171776.html](https://threadreaderapp.com/thread/1182635589604171776.html)

> There are two types of baby outfits. The first is targeted at people buying gifts. It's irresistible on the rack. It has no fewer than 18 buttons. At least 3 people are needed to get a screaming baby into it. It's worn once, so you can send a photo to the gifter, then discarded. 
> 
> Other baby outfits are meant for parents. They’re marked "Easy On, Easy Off" or some such, and they really mean it. Zippers aren't easy enough so they fasten using MAGNETS. A busy parent (i.e. a parent) can change an outfit in 5 seconds, one handed, before rushing to work. 
> 
> The point is, some products are sold directly to the end user, and are forced to prioritize usability. Other products are sold to an intermediary whose concerns are typically different from the user's needs. Such products don't HAVE to end up as unusable garbage, but usually do. 


This is a lovely analogy for why getting real users using your products matters.  I remember being given teeny tiny nike shoes for one of my children when they were babies.  Very cute, but have you ever tried to tie shoelaces on a baby?  Also he grew out of them within weeks, hardly used of course.

Anyway, it's the reminder that our users are the ones who actually matter, no matter whether you are building a product or writing policy documents.  The people paying, management and all of those people won't feel the pain if your policy or product doesn't meet the end users needs.


