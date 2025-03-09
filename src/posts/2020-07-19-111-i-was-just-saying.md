---
title: "111 - I was just saying"
date: 2020-07-19
description: "Last week I was just saying that cloud computing has a bunch of better security properties, and then a once every few years kind of incident comes along that makes me look stupid."
permalink: /i-was-just-saying/
---

Last week I was just saying that cloud computing has a bunch of better security properties, and then a once every few years kind of incident comes along that makes me look stupid.

[Twitters security incident](https://blog.twitter.com/en_us/topics/company/2020/an-update-on-our-security-incident.html) was really bad for users of twitter and as with all incidents, could have been so much worse.  Of course, post incident, the key question to ask ourselves is not "how did this happen" but "how does this not always happen?".

I suspect the reality of this situation is that a small set of reasonably amateur hackers were able to get access to the twitter tools, and from there set about trying to flip certain high value accounts ownership.  Of course, since these are high value accounts, the original owner is going to kick up a fuss, and that's going to get noticed, but if you are taking old accounts or accounts that the user cannot seem to prove that there was an issue, then nobody would notice.  What happened here is that the attackers got greedy and that got them noticed.

In the writeups you see that there are slightly conflicting statements about who was behind this.  I suspect that there have been many of these groups with access to the support tools for some time, quietly using them to trade twitter accounts and not doing it to anyone high profile enough to get caught so far.  

It's easy to take this and run screaming, declaring that this is the problem with cloud providers for SaaS products, that there's a lot of admin staff who you cant trust, and that's still a fair statement.  But let's make sure that when you think about it, you are comparing apples to apples.  Your own admin systems and staff are likely no better, and probably worse than twitters are.  There might be fewer of them and they might be a smaller target, but most of the time when we think about this, we compare the support administrators of the cloud SaaS system to a mythical perfect team within our own organisation, rather than the reality of underpaid, overworked people who really work for us.

## [The Fake Cisco](https://labs.f-secure.com/publications/the-fake-cisco/)

[https://labs.f-secure.com/publications/the-fake-cisco/](https://labs.f-secure.com/publications/the-fake-cisco/)

> In fall 2019, an IT company found some network switches failing after a software upgrade. The company would find out later that they had inadvertently procured suspected counterfeit Cisco equipment. The hardware failure initiated a wider investigation to which the F-Secure Hardware Security team was called and asked to analyse the suspected counterfeit Cisco Catalyst 2960-X series switches and, primarily, provide evidence as to whether any kind of a "backdoor" functionality existed in those devices.
> 
> As it is not trivial to tell genuine and counterfeit devices apart, the verification of non-existence of "backdoor" functionality is also not trivial; requiring a considerable amount of technical investigative work. Ultimately we were able to reach the conclusion, with a reasonable level of confidence, that no backdoors had been introduced. Furthermore, we identified the full exploit chain that allowed one of the forged products to function: a previously undocumented vulnerability in a security component allowing for the devices Secure Boot restrictions to be bypassed.


Supply chain verification is hard enough without being provided with counterfeit network switches.  These switches had internal bootloader bypasses that made it impossible to validate whether the hardware was further compromised or affected.  

In this case, there were no backdoors, but the level of effort required is well beyond what most IT shops would be capable or willing to do.


## [Deepfake used to attack activist couple shows new disinformation frontier - Reuters](https://uk.reuters.com/article/us-cyber-deepfake-activist/deepfake-used-to-attack-activist-couple-shows-new-disinformation-frontier-idUKKCN24G15E)

[https://uk.reuters.com/article/us-cyber-deepfake-activist/deepfake-used-to-attack-activist-couple-shows-new-disinformation-frontier-idUKKCN24G15E](https://uk.reuters.com/article/us-cyber-deepfake-activist/deepfake-used-to-attack-activist-couple-shows-new-disinformation-frontier-idUKKCN24G15E)

> The catch? Oliver Taylor seems to be an elaborate fiction.
> 
> His university says it has no record of him. He has no obvious online footprint beyond an account on the question-and-answer site Quora, where he was active for two days in March. Two newspapers that published his work say they have tried and failed to confirm his identity. And experts in deceptive imagery used state-of-the-art forensic analysis programs to determine that Taylor’s profile photo is a hyper-realistic forgery - a “deepfake.”
> 
> Who is behind Taylor isn’t known to Reuters. Calls to the U.K. phone number he supplied to editors drew an automated error message and he didn’t respond to messages left at the Gmail address he used for correspondence.
> 
> [...]
> 
> Taylor appears to have had no online presence until he started writing articles in late December. The University of Birmingham said in a statement it could not find “any record of this individual using these details.” Editors at the Jerusalem Post and The Algemeiner say they published Taylor after he pitched them stories cold over email. He didn’t ask for payment, they said, and they didn’t take aggressive steps to vet his identity.


I think this is the first active malicious use of a deepfake that I've documented.  Everything before has been alleged and denied (the deepfake executives voice authorising bank transfers) or theoretical, or individual researchers demonstrating what they can do.

We know that fake pictures litter linkedin and other social media networks, creating fake but alluring images to try to pull people in, but this went well beyond that, writing articles for free (or for coverage) isn't unknown, but it allows someone to build up a validated media representation of a narrative.  If you wanted to update wikipedia to present a factual view, referring to published news articles on edited journalism sites is one way to do that, along with the influence you gain directly.


## [Deep-dive: The DarkHotel APT](https://blog.bushidotoken.net/2020/06/deep-dive-darkhotel-apt.html)

[https://blog.bushidotoken.net/2020/06/deep-dive-darkhotel-apt.html](https://blog.bushidotoken.net/2020/06/deep-dive-darkhotel-apt.html)

> DarkHotel has repeatedly demonstrated its capabilities of developing exploits for 0day vulnerabilities in software such as Google Chrome, Mozilla Firefox, Internet Explorer, and Windows Kernel. The exploits are leveraged to deliver malware that can provide backdoor access and remote control over the target device. DarkHotel hides its malware behind layers of encryption, obfuscation, and only deploys it in singular attacks so as not to expose its stolen certificates or 0day vulnerabilities. This group is a well-established expert at spear-phishing where it has researched its targets using OSINT and potentially HUMINT. Its lures have included political news, changes in legislation, and other business news.


I've spoken about DarkHotel for a number of years now, so it's nice to see that there's more being written about them.  One of the more capable and remarkably quiet APT's for western firms, it seems to be most active in the Asia Pacific region, and according to this report, has been slowly changing and evolving its activities over the last few years.


## [Man Says He Was Falsely Arrested After Facial Recognition Mistake : NPR](https://www.npr.org/2020/06/24/882678392/man-says-he-was-falsely-arrested-after-facial-recognition-mistake)

[https://www.npr.org/2020/06/24/882678392/man-says-he-was-falsely-arrested-after-facial-recognition-mistake](https://www.npr.org/2020/06/24/882678392/man-says-he-was-falsely-arrested-after-facial-recognition-mistake)

> Williams was detained and then released on bail until his hearing. That's when prosecutors dropped the charges against him. Academic and government studies have demonstrated that facial recognition systems misidentify people of color more often than white people. What makes this case extraordinary is that police admitted that facial recognition technology prompted the arrest. Typically, the tool is used in secret. Lawyer Phil Mayor is with the ACLU of Michigan.
> 
> PHIL MAYOR: They never even asked him any questions before arresting him. They never asked him if he had an alibi. They never asked him where he was that day.


This feels like a watershed moment.  The use of facial recognition to provide information that might lead to probable cause, or at least further investigation isn't particularly controversial, because any half decent investigation should be reliant not on the facial recognition software, but the processes and methods of the law enforcement teams.  The decision to prompt an arrest based purely on nothing but facial recognition software suggests a belief in the accuracy that is just not upheld by the evidence.


## [Why Doesn’t Your CI Pipeline Have Security Bug Testing? - StackHawk](https://www.stackhawk.com/blog/ci-pipeline-security-bug-testing/)

[https://www.stackhawk.com/blog/ci-pipeline-security-bug-testing/](https://www.stackhawk.com/blog/ci-pipeline-security-bug-testing/)

> While clearly vitally important, current AppSec models are broken. The traditional approaches to application security prioritize training over tooling and finding over fixing. InfoSec teams are holding onto dated practices of periodic, point in time scans of production. Vulnerabilities are kicked back to the engineering team in long lists or large Jira backlogs, which then sit deprioritized over feature development. If the work is pulled into a sprint, it requires the developer to jump back into code that they likely haven’t touched for weeks or months.
> 
> Adding to this problem is the fact that the majority of the security products on the market are legacy enterprise tools. They are built for a different era of software development and continue to serve the technology dinosaurs that have yet to adopt modern DevOps workflow. Features are built for security teams and favor long approval chains and reports rather than enabling the  developers who will fix the security bugs to get to the job of fixing found issues.


This is a continuing problem in security tooling.  Far too few security professionals have actually worked in professional software development.  Cutting a bit of code on github, no matter how smart is the not the same as working as part of a team, contributing code to a large repository and having to coordinate commits, depend on builds and work with the tools.  

Security tools that cannot be configured and used reliably as part of the build process end up being difficult to use in the CI pipeline, and far too many SAST, DAST and security assessment tools suffer from these problems.


## [Cybereason’s Newest Honeypot Trapped Hackers Infiltrating Critical Infrastructure Networks to Carry Out Multistage Ransomware Attacks](https://www.cybereason.com/press/cybereasons-newest-honeypot-trapped-hackers-infiltrating-critical-infrastructure-networks-to-carry-out-multistage-ransomware-attacks)

[https://www.cybereason.com/press/cybereasons-newest-honeypot-trapped-hackers-infiltrating-critical-infrastructure-networks-to-carry-out-multistage-ransomware-attacks](https://www.cybereason.com/press/cybereasons-newest-honeypot-trapped-hackers-infiltrating-critical-infrastructure-networks-to-carry-out-multistage-ransomware-attacks)

> The report titled “Cybereason’s Newest Honeypot Shows How Multistage Ransomware Attacks Should Have Critical Infrastructure Providers on High Alert” is based on attacks to a network architecture masquerading as part of an electricity generation and transmission provider’s network, including an IT and OT environment and HMI (human machine interface) management systems. The environment employed customary security controls including segmentation between the different environments.
> 
> Once the honeypot went live, hackers compromised the network within three days by brute forcing the admin password, which had medium complexity. Attackers placed ransomware on every compromised machine early in the process but didn’t detonate it immediately. After the other stages of the attack were completed (including data theft, user password stealing and propagation across the network), the attacker detonated the ransomware across all compromised endpoints simultaneously. This is a common trait to multistage ransomware campaigns, that is intended to amplify the impact of the attack on the victim.


Every year Cyberreason do this, they put out a honeypot network and then talk about how quickly and easily is was compromised.  This hasn't really changed since last year, but it's worth noting that attacker behaviours in this case have a bit.  [Two years ago](https://cyberweekly.net/patching-everything-all-the-time-might-be-too-expensive), I covered the 2018 version, and the attackers that time sold access on the dark market once they realised it was an ICS system.  This time, the users used Mimikatz to steal user credentials, spread across the system and then detonated ransomware on all the machines.

This almost suggests that attackers are getting less capable, but I think it's simply the rise in the number of lower capability ransomware actors out there.  These actors are using off the shelf tools with very little expertise, and there's a lot of them out there trying on every system that they can.


## [Who’s Behind Wednesday’s Epic Twitter Hack? — Krebs on Security](https://krebsonsecurity.com/2020/07/whos-behind-wednesdays-epic-twitter-hack/)

[https://krebsonsecurity.com/2020/07/whos-behind-wednesdays-epic-twitter-hack/](https://krebsonsecurity.com/2020/07/whos-behind-wednesdays-epic-twitter-hack/)

> The first public signs of the intrusion came around 3 PM EDT, when the Twitter account for the cryptocurrency exchange Binance tweeted a message saying it had partnered with “CryptoForHealth” to give back 5000 bitcoin to the community, with a link where people could donate or send money.
> 
> Minutes after that, similar tweets went out from the accounts of other cryptocurrency exchanges, and from the Twitter accounts for democratic presidential candidate Joe Biden, Amazon CEO Jeff Bezos, President Barack Obama, Tesla CEO Elon Musk, former New York Mayor Michael Bloomberg and investment mogul Warren Buffett.


More information on the group behind the twitter hack from different sources, that point towards a similar conclusion, young amateur hackers looking for high value short twitter handles that got a bit out of hand once they realised what they could do.


## [Hackers Tell the Story of the Twitter Attack From the Inside - The New York Times](https://www.nytimes.com/2020/07/17/technology/twitter-hackers-interview.html)

[https://www.nytimes.com/2020/07/17/technology/twitter-hackers-interview.html](https://www.nytimes.com/2020/07/17/technology/twitter-hackers-interview.html)

> The interviews indicate that the attack was not the work of a single country like Russia or a sophisticated group of hackers. Instead, it was done by a group of young people — one of whom says he lives at home with his mother — who got to know one another because of their obsession with owning early or unusual screen names, particularly one letter or number, like @y or @6.
> 
> The Times verified that the four people were connected to the hack by matching their social media and cryptocurrency accounts to accounts that were involved with the events on Wednesday. They also presented corroborating evidence of their involvement, like the logs from their conversations on Discord, a messaging platform popular with gamers and hackers, and Twitter.
> 
> [...]
> 
> In one of the first transactions, “lol” brokered a deal for someone who was willing to pay $1,500, in Bitcoin, for the Twitter user name @y. The money went to the same Bitcoin wallet that Kirk used later in the day when he got payments from hacking the Twitter accounts of celebrities, the public ledger of Bitcoin transactions shows.
> 
> The group posted an ad on OGusers.com, offering Twitter handles in exchange for Bitcoin. “ever so anxious” took the screen name @anxious, which he had long coveted. (His personalized details still sit atop the suspended account.)


In the aftermath of the twitter hack, I saw lots of theories about how this was state sponsored hacking, how it made no sense that such a powerful attack was used to try to defraud people from a few bitcoin (remember, this netted around $100k give or take in taking).

I was pretty confident that this was low capability actors who had stumbled on something much bigger than they expected, got freaked and ran with what they can. 

This interview agrees with that view.  Young hackers looking for cool handles on twitter, instagram and so on, and stumbled on some poor security setup.  In this case, pretty widely reported is that Twitters internal support application was accessible from the internet, and that it's suspected that the hackers were able to get access to the company slack instance, and from there found some credentials in the support channel that got them into the support application.

Now you might be facepalming, but in reality, this is how lots of support systems run.  If your tools are easily integrated into your company identity system (and none of them ever are), then chances are that support users have shared accounts, post the username and passwords into whatever shared channels they have, and as such, access logs are a mess because the accounts are shared.  This is pretty common practice.  The only odd thing about this all is that I'd have expected that Twitters support tool would have needed either a VPN connection or 2FA (one or the other).


