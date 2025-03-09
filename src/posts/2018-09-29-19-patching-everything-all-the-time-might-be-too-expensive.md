---
title: "19 - Patching everything all the time might be too expensive"
date: 2018-09-29
description: "It's interesting that we know that almost all breaches that get reported are because of unpatched software.  It's pretty rare that we actually see 0-day vulnerabilities in use and breaching networks, primarily because most attackers don't need to use them given how poorly patched our infrastructure is."
permalink: /patching-everything-all-the-time-might-be-too-expensive/
---

It's interesting that we know that almost all breaches that get reported are because of unpatched software.  It's pretty rare that we actually see 0-day vulnerabilities in use and breaching networks, primarily because most attackers don't need to use them given how poorly patched our infrastructure is.

But given the breadth, complexity and aging technology of most real IT installations, it's impossible for us to actually patch everything all the time for a reasonable cost for the business.  We need better ways to determine what things we patch, when and how.

At the same time, Ubico are making a move to change our use of second factor hardware tokens into the primary token.  There are many strategies to improving how our users use passwords, but I think this move, removing passwords altogether, is a very smart move, and I'm looking forward to my new keys turning up and starting to use them instead.

## [The 100% correct way to validate email addresses – Hacker Noon](https://hackernoon.com/the-100-correct-way-to-validate-email-addresses-7c4818f24643)

[https://hackernoon.com/the-100-correct-way-to-validate-email-addresses-7c4818f24643](https://hackernoon.com/the-100-correct-way-to-validate-email-addresses-7c4818f24643)

> If you have a well laid-out form with a label that says “email”, and the user enters an ‘@’ symbol somewhere, then it’s safe to say they understood that they were supposed to be entering an email address. Easy.
> 
> Next, we want to do some validation to ascertain if they correctly entered their email address.
> 
> Not possible.


This, while humorously intended, actually makes a good point.  If I were giving advice today to a team on how to validate an email address, I'd probably look for the presence of the at symbol, and if, and only if, I felt it added extra validation, I'd check that the domain name after the at symbol actually resolved and had an MX record to receive emails.


## [Patching All The Things May Not Be The Best Strategy | Decipher](https://duo.com/decipher/patching-all-the-things-may-not-be-the-best-strategy)

[https://duo.com/decipher/patching-all-the-things-may-not-be-the-best-strategy](https://duo.com/decipher/patching-all-the-things-may-not-be-the-best-strategy)

> The majority of registered vulnerabilities are never exploited in the wild. It isn’t until a catastrophic event such as NotPetya comes along that the lack of patching or tight security configurations exacts a price. Up to that point, the affected companies were achieving peak business efficiency by not patching, because patching can also create risk and expense. Even in this case, it doesn’t prove that they needed to patch everything; they just needed to patch the vulnerabilities that NotPetya exploited.


This is important.  While the headline might be that not patching might be the right business strategy, the reality is that targeted patching is the best business strategy.  We know that it's impossible to patch everything all the time, and holding people to an impossible standard is not a way to improve anything.


## [Millennials and Cybersecurity: Understanding the Value of Personal Data](https://blog.radware.com/security/2018/09/millennials-and-cybersecurity/)

[https://blog.radware.com/security/2018/09/millennials-and-cybersecurity/](https://blog.radware.com/security/2018/09/millennials-and-cybersecurity/)

> Millennials are also likely to look outside the box when it comes to checking for data breaches. In our survey, almost 15% said they searched the dark web to find their data, while 13% used data breach search websites.
> 
> But while the majority are security conscious when it comes to how businesses use their personal data, many are in fact taking risks when it comes to other forms of data security, like sharing Netflix or Amazon Prime login details with friends and family.


What actually is the "Dark Web" in this research?  I struggle to believe that 15% of millennials are searching Tor for their own personal data for example.


## [United Nations Accidentally Exposed Passwords and Sensitive Information to the Whole Internet](https://theintercept.com/2018/09/24/united-nations-trello-jira-google-docs-passwords/)

[https://theintercept.com/2018/09/24/united-nations-trello-jira-google-docs-passwords/](https://theintercept.com/2018/09/24/united-nations-trello-jira-google-docs-passwords/)

> Trello boards, as well as documents hosted on Google Drive and Google Docs, are private by default. The user must manually change settings to make this information public for anyone on the internet to view. Pathak previously suggested that Trello add new safeguards to discourage the exposure of sensitive data. At the time, Trello’s CEO stated that “we strive to make sure public boards are being created intentionally and have built in safeguards to confirm the intention of a user before they make a  board publicly visible. Additionally, visibility settings are displayed persistently on the top of every board.”
> 
> Pathak believes that people often make their organizations’ sensitive data public simply because it’s more convenient. This way they can “share the details present on the board with their team members just by sharing the URL of the board with them without adding them to the board,” Pathak said.
> 
> “Adding people to the board seems to be huge task for these people, but in fact it is really easy,” he added.


Trello is just the most popular of these tools.  A bad reaction to these stories (and previously this researcher found UK Government boards and info) is to stop people using these tools.

Users clearly have a desire and need to use these tools, and sometimes to share usernames and passwords, and I wonder if things would be better if we had better ways of sharing this information in an obvious, easy and secure way.


## [ICS Threat Broadens: Nation-State Hackers Are No Longer The Only Game In Town](https://www.cybereason.com/blog/industrial-control-system-specialized-hackers)

[https://www.cybereason.com/blog/industrial-control-system-specialized-hackers](https://www.cybereason.com/blog/industrial-control-system-specialized-hackers)

> Accompanying this variety of threat actors is a new approach to sourcing ICS assets. Instead of  strategically selecting targets, performing through reconnaissance and targeting individuals with potential network access -- the typical infiltration path used by attackers who usually target ICS environments -- the actors who compromised Cybereason’s honeypot bought the asset off a dark Web forum. The playbook the attackers used after they compromised the network also differed from the traditional ICS threat actor profile and showed that while they had some advanced methods, a few of their techniques were sloppy.
> 
> 


This is a really interesting bit of research.  The creation of a complete honeypot network that looked like a power station, and while exploited, the credentials were then sold on to another attacker.
Of interest is that this attacker was interested in breaching a power station industrial control mechanism, but didn't appear to be the typical APT attacker we'd assume would be interested


## [Introducing the YubiKey 5 Series with New NFC and FIDO2 Passwordless Features | Yubico](https://www.yubico.com/2018/09/introducing-the-yubikey-5-series-with-new-nfc-and-fido2-passwordless-features/)

[https://www.yubico.com/2018/09/introducing-the-yubikey-5-series-with-new-nfc-and-fido2-passwordless-features/](https://www.yubico.com/2018/09/introducing-the-yubikey-5-series-with-new-nfc-and-fido2-passwordless-features/)

> The YubiKey 5 Series is the industry’s first set of multi-protocol security keys to support FIDO2 / WebAuthn, the open authentication standard that Yubico helped to pioneer, along with Microsoft and others. All leading platforms and browsers have either made support or are engaged in this standards work, expanding authentication choices using authentication devices, such as a YubiKey, with or without a username and password. Each key in the YubiKey 5 series supports: FIDO2 / WebAuthn, FIDO U2F, PIV (smart card), OpenPGP, Yubico OTP, OATH-TOTP, OATH-HOTP, and challenge-response. 


This is quite cool.  WebAuthN and FIDO U2F are a definite nail in the coffin of the password.
Designed originally as a "second-factor" the Ubico people describe how they want to provide a better passwordless single factor token.


## [They Got 'Everything': Inside a Demo of NSO Group's Powerful iPhone Malware - Motherboard](https://motherboard.vice.com/en_us/article/qvakb3/inside-nso-group-spyware-demo)

[https://motherboard.vice.com/en_us/article/qvakb3/inside-nso-group-spyware-demo](https://motherboard.vice.com/en_us/article/qvakb3/inside-nso-group-spyware-demo)

> Worldwide, NSO’s customers have purchased the capability to target between roughly 350 to 500 devices (15 to 30 per customer), according to the source. More potential customers approached NSO after the first Citizen Lab report on NSO’s tools being used to target Mansoor, the source said.


This report is a fascinating insight into a company that we don't often see inside, but these numbers don't quite add up to me.
If they have sold to around 20-30 customers, then why would they need over 100 people in customer support?

Anyway,  regardless of the details (and I doubt any of us will ever know), I think this is a fascinating insight into one of the most technologically advanced "hacking groups"


## [Inside the OPM Hack, The Cyberattack that Shocked the US Government | WIRED](https://www.wired.com/2016/10/inside-cyberattack-shocked-us-government/)

[https://www.wired.com/2016/10/inside-cyberattack-shocked-us-government/](https://www.wired.com/2016/10/inside-cyberattack-shocked-us-government/)

> But the plan pays too little attention to a fundamental flaw in our approach to security: We’re overly focused on prevention at the expense of mitigation. One reason these attackers can do so much damage is that the average time between a malware infection and discovery of the attack is more than 200 days, a gap that has barely narrowed in recent years.
> 
> “We can’t operate with the mindset that everything has to be about keeping them out,” says Rich Barger, ThreatConnect’s chief intelligence officer. “We have to operate knowing that they’re going to get inside sometimes. The question is, how do we limit their effectiveness and conduct secure business operations knowing they’re watching?” Accomplishing that means building networks that are designed to limit a hacker’s ability to maneuver and creating better ways to detect anomalous behavior by allegedly authorized users.


I had missed this 2 years ago and this looks to be one of the most thorough writeups of a technical breach by an APT that I've seen.  Well written and enjoyably readable.


