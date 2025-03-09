---
title: "153 - Learning from failure part 2"
date: 2021-06-13
description: "Last weeks post turned out to be somewhat prescient as this week we [had a significant outage](https://www.theguardian.com/technology/2021/jun/08/massive-internet-outage-hits-websites-including-amazon-govuk-and-guardian-fastly) that affected [the UK Government, BBC, Guardian, Financial Times, Independant, New York Times, The Verge, Amazon, Boots, Paypal, Deliveroo](https://www.theguardian.com/technology/2021/jun/08/internet-outage-which-websites-and-services-were-hit-by-fastly-issue) and many others."
permalink: /learning-from-failure-part-2/
---

Last weeks post turned out to be somewhat prescient as this week we [had a significant outage](https://www.theguardian.com/technology/2021/jun/08/massive-internet-outage-hits-websites-including-amazon-govuk-and-guardian-fastly) that affected [the UK Government, BBC, Guardian, Financial Times, Independant, New York Times, The Verge, Amazon, Boots, Paypal, Deliveroo](https://www.theguardian.com/technology/2021/jun/08/internet-outage-which-websites-and-services-were-hit-by-fastly-issue) and many others.

This rather naturally led to questions about just how resilient the internet is, and whether we need more companies providing critical services.  In the case of GOV.UK, there was a plan for what was regarded as an almost never happen incident, and they ran with the plan as defined.  Of course, any outage that affects the governments ability to deliver services is a big deal, and I'm sure that the team behind GOV.UK are looking at those plans and asking whether they could respond fast enough and effectively enough.  But that's what we tend to mean by learning from failure.

However, all of the noise about this reminded me of an old article that I've had hanging around waiting for a good slot in this newsletter for well over a year now.  Learning from failure requires more than simply working out who or what is the root cause or who is to blame.  As Jon Allspaw always says
"The question is not why did it break, but more why does it work?",

Systems and failure are incredibly complicated, especially within complex systems like modern IT, and there's a huge number of interacting systems that allow for failure in specific areas, but can route around or accomodate the failure.  Identifying that your CDN was unavailable is only one indicator of the failure.  Your CDN provider might have broken thousands of times before and you'd just not noticed before.  You can't therefore learn simple lessons like "You need multiple CDN providers and a quick way to switch between them" without actively asking in depth and detailed questions about the failure and the cascade and understanding "Why does it work the rest of the time".  That might lead you to discover all kinds of interesting mechanisms within your system, and a constant litany of failures that are disguised by self healing, self correcting cybernetic systems that you build without realising.


## [The Multiple Audiences and Purposes of Post-Incident Reviews – Adaptive Capacity Labs](https://www.adaptivecapacitylabs.com/blog/2018/10/08/the-multiple-audiences-and-purposes-of-post-incident-reviews/)

[https://www.adaptivecapacitylabs.com/blog/2018/10/08/the-multiple-audiences-and-purposes-of-post-incident-reviews/](https://www.adaptivecapacitylabs.com/blog/2018/10/08/the-multiple-audiences-and-purposes-of-post-incident-reviews/)

> In reality, learning is actually quite difficult to avoid. In other words, the answer to “Are you learning from incidents?” will always be “Yes.”
> 
> Some better questions might be:
> 
> * What (specifically) are people learning?
> * Who are developing new understandings based on what they’re learning? How might we know they’re learning the same things as others?
> * When are they learning these things?
> * Where does this learning take place?
> * How far does this new understanding travel?
> 
> (I’d like to dedicate an entire separate post to elaborate and explore those questions; we have experience with them in our assessment projects.)
> 
> When we look closely at post-incident artifacts, we find that they can serve a number of different purposes for different audiences.


In the wake of the recent incident, this old post serves as a good reminder that "learning from failure" is a trite phrase that is essentially meaningless.  These more detailed questions are far more valuable when you are asking about these things.

The second part of this post talks about the fact that you might write a post incident report for different audiences, and if that's the case you are going to write different things.  The post from Fastly on their incident is a good example of a post-incident report written for customers that mostly just acknowledges that the event happened, and that they understand it, and will work to prevent it happening.  Technically savvy readers might have wanted more technical detail, to better understand just why it failed the way it did, but that's not within the purpose of the incident report.


## [Summary of June 8 outage | Fastly](https://www.fastly.com/blog/summary-of-june-8-outage)

[https://www.fastly.com/blog/summary-of-june-8-outage](https://www.fastly.com/blog/summary-of-june-8-outage)

> On May 12, we began a software deployment that introduced a bug that could be triggered by a specific customer configuration under specific circumstances.
> 
> Early June 8, a customer pushed a valid configuration change that included the specific circumstances that triggered the bug, which caused 85% of our network to return errors.
> 
> Here’s a timeline of the day’s activity (all times are in UTC): 
> 
> 09:47 Initial onset of global disruption
> 09:48 Global disruption identified by Fastly monitoring
> 09:58 Status post is published
> 10:27 Fastly Engineering identified the customer configuration
> 10:36 Impacted services began to recover
> 11:00 Majority of services recovered
> 12:35 Incident mitigated
> 12:44 Status post resolved
> 17:25 Bug fix deployment began
> 
> Once the immediate effects were mitigated, we turned our attention to fixing the bug and communicating with our customers. We created a permanent fix for the bug and began deploying it at 17:25.


This was a fascinating incident for all of the knock on effects.  But the critical thing here for those of you playing at home is the fact that a single customers change caused the impact on all of the other customers.

SaaS solutions have to think strongly about tenant isolation.  How do you ensure that one tenant cannot affect other tenants.  This starts in IaaS space with things like per tenant limits on storage, compute use and so forth.  But as we migrate to more and more SaaS style solutions, it gets harder and harder for the supplier to meaningfully provide full isolation between tenants.  Bugs and issues like this will happen, and they'll get more impactful the more organisations rely on the same suppliers.


## [Incident report: GOV.UK outage on 8 June 2021 - Inside GOV.UK](https://insidegovuk.blog.gov.uk/2021/06/11/incident-report-gov-uk-outage-on-8-june-2021/)

[https://insidegovuk.blog.gov.uk/2021/06/11/incident-report-gov-uk-outage-on-8-june-2021/](https://insidegovuk.blog.gov.uk/2021/06/11/incident-report-gov-uk-outage-on-8-june-2021/)

> CDNs usually provide very high levels of reliability. GOV.UK's CDN is configured to serve static fallback pages (called "mirrors") if anything goes wrong behind the scenes with our main infrastructure.
> 
> However, on very rare occasions things break. No infrastructure is 100% reliable. Because CDNs have to sit at the "edge" of the network, when they break the whole website goes down. So it's important to have a backup plan.
> 
> Our plan for an incident like this
> 
> We know that the CDN is a potential single point of failure, so we have a plan for this situation.
> 
> We have a secondary CDN which is always on, but it doesn't usually serve any traffic. We refer to switching from the primary CDN to the secondary as "fail over".
> 
> Because the secondary CDN represents degraded service where dynamic parts of GOV.UK, like search or location based services, don't function in their usual high quality way, it's a big decision to fail over. If the incident with the primary CDN is resolved quickly (which they often are), then failing over too soon could make the incident on GOV.UK worse.
> 
> So the plan was to wait 15 minutes to establish the severity of the issue with the primary CDN, and then fail over if the issues persisted.
> 
> 


If you are based in the UK, you can’t have missed the Fastly outage this week since it affected almost all of the British media online, including the BBC.  The Verge [migrated their news coverage to a Google Doc](https://twitter.com/verge/status/1402210406328942592?s=21).

Within Government circles, the loss of GOV.UK was considered a serious issue, and people were left wondering why there was a single point of failure.  Of course, the engineers behind GOV.UK have produced an excellent incident report, written in clear plain language that addresses this.  They had a backup CDN, but acting too rashly can cause issues, so they consciously chose to wait for 15 minutes to check that the outage looked serious before switching.  

Rash actions during an incident are far more likely to create more issues than fix something, so the fact that the team planned for this, [documented how to do it](https://docs.publishing.service.gov.uk/manual/fall-back-to-aws-cloudfront.html) and were able to take measured managed decisions is something to be applauded


## [How Hackers Used Slack to Break into EA Games](https://www.vice.com/en/article/7kvkqb/how-ea-games-was-hacked-slack)

[https://www.vice.com/en/article/7kvkqb/how-ea-games-was-hacked-slack](https://www.vice.com/en/article/7kvkqb/how-ea-games-was-hacked-slack)

> A representative for the hackers told Motherboard in an online chat that the process started by purchasing stolen cookies being sold online for $10 and using those to gain access to a Slack channel used by EA. Cookies can save the login details of particular users, and potentially let hackers log into services as that person. In this case, the hackers were able to get into EA's Slack using the stolen cookie. (Although not necessarily connected, in February 2020 Motherboard reported that a group of researchers discovered an ex-engineer had left a list of the names of EA Slack channels in a public facing code repository).
> 
> "Once inside the chat, we messaged a IT Support members we explain to them we lost our phone at a party last night," the representative said.
> 
> Do you work at EA? Do you know anything else about this breach? We’d love to hear from you. Using a non-work phone or computer, you can contact Joseph Cox securely on Signal on +44 20 8133 5190, Wickr on josephcox, OTR chat on jfcox@jabber.ccc.de, or email joseph.cox@vice.com.
> 
> The hackers then requested a multifactor authentication token from EA IT support to gain access to EA's corporate network. The representative said this was successful two times.


EA Games was hacked by a malicious actor who is attempted to sell access to sourcecode, design documents and other assets online.

If you think "but surely it's just a games company", you are missing out on the FIFAe World Cup, being played on EA Sports Fifa (one of the affected games) for a prize pot of £500,000 this year.  eSports has got money and sponsorship behind it, and access to the source code would be valuable to cheat creators and strategy consultants.

On a different note, It all started with a stolen cookie, which implies that there is a market out there for stolen cookies to conduct account takeover with.  The ability to escalate from a cookie to 2FA account takeover requires some skill and social engineering, but this is a lovely example of that process laid out for you to consider.  I wonder how easy that attack would be in your organisation?


## [Why We Are Publishing the Tax Secrets of the .001% — ProPublica](https://www.propublica.org/article/why-we-are-publishing-the-tax-secrets-of-the-001)

[https://www.propublica.org/article/why-we-are-publishing-the-tax-secrets-of-the-001](https://www.propublica.org/article/why-we-are-publishing-the-tax-secrets-of-the-001)

> We do not know the identity of our source. We did not solicit the information they sent us. The source says they were motivated by our previous coverage of issues surrounding the IRS and tax enforcement, but we do not know for certain that is true. We have considered the possibility that information we have received could have come from a state actor hostile to American interests. In particular, a number of government agencies were compromised last year by what the U.S. has said were Russian hackers who exploited vulnerabilities in software sold by SolarWinds, a Texas-based information technology company. We do note, however, that the Treasury Department’s inspector general for tax administration wrote in December that, “At this time, there is no evidence that any taxpayer information was exposed” in the SolarWinds hack.


This is a good explanation of the new threat model for journalists.  It used to be that as a journalist, if you were contacted by a source offering you access to classified papers, then providing the legitimacy of the source or papers was confirmed, everyone assumed that leakers were motivated by altruistic motives.  The pentagon papers, and even the snowdon leaks are indications of this.

But the rise of wikileaks, Guccifer and disinformation campaigns, journalists now have to question to themsevles whether they are being used to add fuel to a disinformation campaign.

That ProPublica actively considered whether the SolarWinds breach could have resulted in the loss of these documents is a sign of a mature mental model around the legitimacy of leaked papers.  Of course, in the end, papers sold and ad-funded clicks gained is still the core commercial driver for many journalistic organisations, so even if they thought the information was leaked by a "hostile actor", they would ask themselves whether there was benefit in publishing anyway, and I suspect would claim that there is still greater public benefit (and commercial value) in publishing regardless.


## [Apple advances its privacy leadership with iOS 15, iPadOS 15, macOS Moneterey, and watchOS 8 - Apple (UK)](https://www.apple.com/uk/newsroom/2021/06/apple-advances-its-privacy-leadership-with-ios-15-ipados-15-macos-monterey-and-watchos-8/)

[https://www.apple.com/uk/newsroom/2021/06/apple-advances-its-privacy-leadership-with-ios-15-ipados-15-macos-monterey-and-watchos-8/](https://www.apple.com/uk/newsroom/2021/06/apple-advances-its-privacy-leadership-with-ios-15-ipados-15-macos-monterey-and-watchos-8/)

> Private Relay is a new internet privacy service that’s built right into iCloud, allowing users to connect to and browse the web in a more secure and private way. When browsing with Safari, Private Relay ensures all traffic leaving a user’s device is encrypted, so no one between the user and the website they are visiting can access and read it, not even Apple or the user’s network provider. All the user’s requests are then sent through two separate internet relays. The first assigns the user an anonymous IP address that maps to their region but not their actual location. The second decrypts the web address they want to visit and forwards them to their destination. This separation of information protects the user’s privacy because no single entity can identify both who a user is and which sites they visit


(Joel) Apple's [WWDC21](https://www.macrumors.com/roundup/wwdc/) announced interesting privacy features.

Building on Sign in with Apple, Hide My Email is quite handy. Hopefully Apple will maintain accountability in case there are sender abuse issues, but I am a little surprised Apple chose to use privaterelay.appleid.com as this allows services to predictably assess Apple Private Relay emails as disposable emails, so deny list them so you can't use them to sign up to their services (a bad thing, in general).

The main attraction for me is Private Relay, a two tier internet relay system (a [baby onion](https://www.torproject.org) perhaps?) to obfuscate IP address and destination website. Apple's Press Room do not want it to be called a VPN, because a VPN service would not have the second obfuscating hop (I agree, given pro-VPN marketing out there). For iThing owners, there will be even less of a requirement to use third-party VPN services, particularly combined with using encrypted DNS services (I use [NextDNS](https://nextdns.io)).

Apple's market position aside (that it can create a new feature within iThingOS and it effectively becomes a pseudo-standard overnight), these features are individually good things for global iThing users.


## [Apple Aiming to Eliminate Passwords With Face ID/Touch ID Passkeys - MacRumors](https://www.macrumors.com/2021/06/10/apple-icloud-keychain-passkeys/)

[https://www.macrumors.com/2021/06/10/apple-icloud-keychain-passkeys/](https://www.macrumors.com/2021/06/10/apple-icloud-keychain-passkeys/)

> "Passkeys in iCloud Keychain," a feature in iOS 15 and macOS Monterey, stores a new WebAuthn credential called a passkey in ‌iCloud‌ keychain. It's used instead of a password for account creation and login, with one-tap login.
> 
> When you create an account using a passkey, there is no password to deal with. You can access that account with just a login and authentication through Touch ID or Face ID.
> 
> No password is required because your Apple device handles the generation and storage of the unique passkey used for the site, so login is just a matter of entering a username and authenticating. Passkeys are end-to-end encrypted and synced across all of your Apple devices thanks to ‌iCloud‌ Keychain. Since everything is stored in ‌iCloud‌ Keychain, credentials are preserved even if Apple devices are lost or stolen.


This is a fascinating and somewhat obvious technology move.  This turns your phone into the equivalent of a Yubikey or other hardware token.
The point here is instead of using that FIDO token as a second-factor in addition to your password, it's going to use it as the primary factor.
The ability to store the original seed in iCloud means that any device with access to iCloud can access the seed and generate the appropriate tokens, meaning you can roam from device to device, providing of course that it's an apple device with access to your iCloud.

Within a corporate environment, where you might forbid users from accessing their personal iCloud from the corporate device, that means that the keys shouldn't leave the corporate iCloud environment, but will also give rise to user frustration as they can't bring personal accounts to their work device for accessing their shopping, banking or whatever.

Instead I'd expect to see this as an option, which is nice that there's a highly secure option, but it also means that a username and password is likely to be the fallback option, and since it's irregularly used, users will pick only passwords that they can actively remember without regular use.


## [Apple brass discussed disclosing 128-million iPhone hack, then decided not to | Ars Technica](https://arstechnica.com/gadgets/2021/05/apple-brass-discussed-disclosing-128-million-iphone-hack-then-decided-not-to/)

[https://arstechnica.com/gadgets/2021/05/apple-brass-discussed-disclosing-128-million-iphone-hack-then-decided-not-to/](https://arstechnica.com/gadgets/2021/05/apple-brass-discussed-disclosing-128-million-iphone-hack-then-decided-not-to/)

> An email entered into court this week in Epic Games’ lawsuit against Apple shows that, on the afternoon of September 21, 2015, Apple managers had uncovered 2,500 malicious apps that had been downloaded a total of 203 million times by 128 million users, 18 million of whom were in the US.
> 
> [...]
> 
> About 10 hours later, Bagwell discusses the logistics of notifying all 128 million affected users, localizing notifications to each users’ language, and “accurately includ[ing] the names of the apps for each customer.”
> 
> Alas, all appearances are that Apple never followed through on its plans. An Apple representative could point to no evidence that such an email was ever sent. Statements the representative sent on background—meaning I’m not permitted to quote them—noted that Apple instead published only this now-deleted post.
> 
> The post provides very general information about the malicious app campaign and eventually lists only the top 25 most downloaded apps. “If users have one of these apps, they should update the affected app which will fix the issue on the user’s device,” the post stated. “If the app is available on [the] App Store, it has been updated, if it isn’t available it should be updated very soon.”
> 
> Ghost of Xcode
> 
> The infections were the result of legitimate developers writing apps using a counterfeit copy of Xcode, Apple’s iOS and OS X app development tool. The repackaged tool dubbed XcodeGhost surreptitiously inserted malicious code alongside normal app functions.


This is insight into the impact of a [major supply chain compromise by unknown organisations in 2015](https://blog.lookout.com/xcodeghost), and how Apple decided to notify or not notify its users.

As a company that is currently actively advertising itself as the more secure and more privacy focused tech organisation available, this is pretty damning.  They knew exactly how many people were affected and considered the idea of contacting them all to let them know that they had all downloaded apps with malicious code in them but decided not to.


## [Taildrop was kind of easy, actually · Tailscale](https://tailscale.com/blog/2021-06-taildrop-was-easy/)

[https://tailscale.com/blog/2021-06-taildrop-was-easy/](https://tailscale.com/blog/2021-06-taildrop-was-easy/)

> Seriously though, Taildrop is a thing that lets you transfer files between your own devices, over your point-to-point Tailscale+WireGuard mesh network, across various different OS platforms. It never stores your files in the cloud or sends them to us. They’re end-to-end encrypted with keys that we never see. And it costs us, effectively, nothing to run, because it’s your bandwidth (mostly LAN bandwidth), not ours. We just bust some NATs and negotiate the session. Which is why we can give Taildrop away to everybody, for unlimited use, with no file size limits, as part of the Tailscale free plan. It’s also open source…
> …although there’s so little code that it’s hard to spot. That’s the topic of this post.
> When we wrote How Tailscale Works and How NAT Traversal Works, we had a not-so-subtle goal of explaining that, in fact, making those things work is pretty hard. We’ve spent thousands of person-hours on it, and maybe you should just use Tailscale instead. You know how this story goes.
> But Taildrop is different. It’s just an unauthenticated file transfer layer on top of Tailscale. It can be unauthenticated because Tailscale is already authenticated, and controls who can access each port, and for those who are allowed, it securely tells you who’s connecting right now. Taildrop can itself be unencrypted because Tailscale is already end-to-end encrypted (an architecture called Zero Trust Networking).


Tailscale have been doing interesting things in a VPN/post-VPN world for a while, but this is a really interesting development.
The argument that "If you have access to the virtual private network, you are clearly supposed to be there" is the opposite of zero-trust networking as far as I can tell.  The reduction in the number of moving parts and most importantly key-generation, distribution and revocation to something lower in the stack makes this far simpler to operate.  But it also means that a bad actor only has to get access to your network to get access to everything.


