---
title: "11 - Two factor or not two factor, that is the question"
date: 2018-08-04
description: "This week has all been about two factor authentication.  For me, I read the Motherboard article first, but then the Reddit incident and the claim last week from Google made me perk up my ears, and then the internet exploded with comment about two-factor authentication.  In my original comments against these articles I kept asking the question \"It might not be brilliant, but isn't it worse if we don't use it?\""
permalink: /two-factor-or-not-two-factor-that-is-the-question/
---

This week has all been about two factor authentication.  For me, I read the Motherboard article first, but then the Reddit incident and the claim last week from Google made me perk up my ears, and then the internet exploded with comment about two-factor authentication.  In my original comments against these articles I kept asking the question "It might not be brilliant, but isn't it worse if we don't use it?"

I now feel confident that I'm not the only person asking this question, and that actually we all agree that not using a security control because it's not perfect is a terrible approach.

We desperately need better two-factor authentication mechanisms that work for users, wherever they are and no matter how technically literate they are, and sadly there is no near ubiquity of modern U2F FIDO dongles like UbiKey's or Googles recently announced Titan keys.

Additionally this week, I've been reading and thinking a lot about careers in cybersecurity and what career pathways should look like.  You can expect some of that reading in next weeks issue, but some tidbits have snuck in here.

Enjoy

## [The SIM Hijackers - Motherboard](https://motherboard.vice.com/en_us/article/vbqax3/hackers-sim-swapping-steal-phone-numbers-instagram-bitcoin)

[https://motherboard.vice.com/en_us/article/vbqax3/hackers-sim-swapping-steal-phone-numbers-instagram-bitcoin](https://motherboard.vice.com/en_us/article/vbqax3/hackers-sim-swapping-steal-phone-numbers-instagram-bitcoin)



"By hijacking Rachel’s phone number, the hackers were able to seize not only Rachel’s Instagram, but her Amazon, Ebay, Paypal, Netflix, and Hulu accounts too. None of the security measures Rachel took to secure some of those accounts, including two-factor authentication, mattered once the hackers took control of her phone number."

There's a lot of discussion around two-factor at the moment, because it's not a panacea, and we know that sim-swapping and SS7 hijacking and various other exploits work against it.  But it massively increases the baseline of effort that an attacker has to go through compared to not having it.
Don't let stories like this put you off of two-factor authentication, just remember that it's not perfect.


## [We had a security incident. Here's what you need to know. : announcements](https://www.reddit.com/r/announcements/comments/93qnm5/we_had_a_security_incident_heres_what_you_need_to/)

[https://www.reddit.com/r/announcements/comments/93qnm5/we_had_a_security_incident_heres_what_you_need_to/](https://www.reddit.com/r/announcements/comments/93qnm5/we_had_a_security_incident_heres_what_you_need_to/)



" A hacker broke into a few of Reddit’s systems and managed to access some user data, including some current email addresses and a 2007 database backup containing old salted and hashed passwords. Since then we’ve been conducting a painstaking investigation to figure out just what was accessed, and to improve our systems and processes to prevent this from happening again."

This from Reddit is a brilliant example of how to do breach notification to your users.  Great description of what happened and most importantly, why you should care.


## [Wendy Nather on Twitter: "[THREAD] So here's the thing. As a CISO, you have to balance the *most probable* threat scenarios against the environment and tolerances of your customers (your users). 1/n"](https://twitter.com/wendynather/status/1024808489997266945)

[https://twitter.com/wendynather/status/1024808489997266945](https://twitter.com/wendynather/status/1024808489997266945)



"As a CISO, you have to balance the *most probable* threat scenarios against the environment and tolerances of your customers (your users)"

Wendy nailing it again.  2FA is hackable, but is it the most probably hack against your customers? Is it worse if you didn't use it?


## [InfoSec’s fantastic fear of everything — why the Reddit incident shouldn’t cause InfoSec to throw…](https://doublepulsar.com/infosecs-fantastic-fear-of-everything-why-the-reddit-incident-shouldn-t-cause-infosec-to-throw-4bb3b7ea634f)

[https://doublepulsar.com/infosecs-fantastic-fear-of-everything-why-the-reddit-incident-shouldn-t-cause-infosec-to-throw-4bb3b7ea634f](https://doublepulsar.com/infosecs-fantastic-fear-of-everything-why-the-reddit-incident-shouldn-t-cause-infosec-to-throw-4bb3b7ea634f)



"In the wake of the Reddit breach, we’re hearing this all day every day: “SMS two factor authentication isn’t secure and shouldn’t be used”.

Here’s the thing — that’s not a true statement when you break it down, and I think it harms everybody as it positions people in a mindset of ‘we will do nothing instead’."


## [The Year Targeted Phishing Went Mainstream — Krebs on Security](https://krebsonsecurity.com/2018/08/the-year-targeted-phishing-went-mainstream/)

[https://krebsonsecurity.com/2018/08/the-year-targeted-phishing-went-mainstream/](https://krebsonsecurity.com/2018/08/the-year-targeted-phishing-went-mainstream/)



"The sextortion scheme that emerged this month falsely claims to have been sent from a hacker who’s compromised your computer and used your webcam to record a video of you while you were watching porn. The missive threatens to release the video to all your contacts unless you pay a Bitcoin ransom.

What spooked people most about this scam was that its salutation included a password that each recipient legitimately used at some point online. Like most phishing attacks, the sextortion scheme that went viral this month requires just a handful of recipients to fall victim for the entire scheme to be profitable."

I've had this mentioned to me by a variety of friends recently.  It turns out that I hadn't seen any of the ones sent to me because Google do such a good job of marking them as spam and filtering them out.  But several non-IT freinds were understandably scared by this campaign, because the fear that your personal habits will be broadcast is strong.  In all the cases of my freinds, they thought it was a scam, but weren't entirely confident in ignoring it, just in case.

There's something to that psychology, which is interesting by itself.


## [Security Begins at the Home Router](https://insights.sei.cmu.edu/sei_blog/2018/07/security-begins-at-the-home-router.html)

[https://insights.sei.cmu.edu/sei_blog/2018/07/security-begins-at-the-home-router.html](https://insights.sei.cmu.edu/sei_blog/2018/07/security-begins-at-the-home-router.html)



"Design home routers and IoT devices to operate with read-only filesystems, making run-time installations of malware impractical.
Disable any packet crafting/spoofing/promiscuous mode on the firmware level to avoid malicious use of network resource on these devices.
Provide automated updates for firmware with either planned downtime or no downtime to resolve vulnerabilities proactively."

These security tips should apply to any essentially unmanaged, unmaintained devices you have.  Bastion hosts in the cloud, Serverless style containers, containers generally, etc...


## [Amazon’s Face Recognition Falsely Matched 28 Members of Congress With Mugshots | ACLU of Northern CA](https://www.aclunc.org/blog/amazon-s-face-recognition-falsely-matched-28-members-congress-mugshots)

[https://www.aclunc.org/blog/amazon-s-face-recognition-falsely-matched-28-members-congress-mugshots](https://www.aclunc.org/blog/amazon-s-face-recognition-falsely-matched-28-members-congress-mugshots)



"Amazon’s face surveillance technology is the target of growing opposition nationwide, and today, there are 28 more causes for concern. In a test the ACLU recently conducted of the facial recognition tool, called “Rekognition,” the software incorrectly matched 28 members of Congress, identifying them as other people who have been arrested for a crime. "

Facial recognition is a hard problem, and has a high false positive rate.  This might not be a problem if the teams implementing it know what they are doing, but the ACLU here exhibited all of the classic poor implementation issues, in terms of poor data, and naturally reading the results of a match as a proof of identity.
When doing anything with machine learning, such as facial recognition, it's important to realise the importance of good raw data sets, of the problems of false positives and how to deal with it, and this is just another good reminder of how hard it is to get this stuff right.


## [Fish Out of Water: How the Military Is an Impossible Place for Hackers, and What to Do About It](https://warontherocks.com/2018/07/fish-out-of-water-how-the-military-is-an-impossible-place-for-hackers-and-what-to-do-about-it/)

[https://warontherocks.com/2018/07/fish-out-of-water-how-the-military-is-an-impossible-place-for-hackers-and-what-to-do-about-it/](https://warontherocks.com/2018/07/fish-out-of-water-how-the-military-is-an-impossible-place-for-hackers-and-what-to-do-about-it/)



"To add insult to injury, tool developers often perform technical due diligence for capabilities procured from contractors. These capabilities typically mirror the capabilities that talented tool developers create on a quarterly basis, and the government will pay multiples of a developer’s annual salary for them. Nowhere else in the military is its economic rent so clear to the servicemember. "

This article, filled with interesting insights to cybercommand in the US is also very reminiscent of the problems facing technologists and security people in government.  Too few leaders who know or understand what they do, difficulty paying, and of course, the quoted bit, exposing to developers that you paid 10x their salary to an external developer and now you are asking them to fix that work.  The comparison to medics and lawyers feels apt as well


## [NATO's Advancement in Cyber](https://www.thecipherbrief.com/column_article/natos-advancement-in-cyber?mc_cid=85300c9488&mc_eid=a28caaebfd)

[https://www.thecipherbrief.com/column_article/natos-advancement-in-cyber?mc_cid=85300c9488&mc_eid=a28caaebfd](https://www.thecipherbrief.com/column_article/natos-advancement-in-cyber?mc_cid=85300c9488&mc_eid=a28caaebfd)



"While getting to this decision undoubtedly required a fair amount of diplomatic maneuvering and work with technical and legal experts, the fact that NATO will coordinate sovereign cyber effects for its missions and operations doesn’t change the defensive mandate of the organization- the operators supporting NATO missions need tools to proactively defend themselves before the execution of a mission is jeopardized.  They may need to go outside their networks to disrupt attacks, identify attackers or retrieve stolen data or degrade the adversary capability to continue activities harming NATO’s ability to operate."
This is an interesting development, if not that surprising.  I don't think there has been enough public discourse about what is an acceptable or unacceptable target in the cyberwarfare domain.  Is it acceptable to breach a commercial entity if a military target is using it to coordinate kinetic offensive missions?  Is it different if it's a large Us entity like WhatsApp versus a small regional entity?   What level of collatoral damage is acceptable?
Just like with target strikes and kinetic warfare, this isn't easily black and white, but shades of grey and public opinion will shift and change over time, influenced by the media of course, but it's probably a public debate that is overdue


