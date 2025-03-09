---
title: "97 - How to work from home"
date: 2020-04-12
description: "I'm sorry to tell you this, but I don't think the global quarantines are going to end anytime soon."
permalink: /how-to-work-from-home/
---

I'm sorry to tell you this, but I don't think the global quarantines are going to end anytime soon.

The Institute for Health Metrics and Evaluation [thinks that UK deaths will continue rising and peak around April 17th](https://covid19.healthdata.org/united-kingdom) (but look at those error ranges!) but with deaths still likely to continue through to May.  However worldwide other nations are looking in similarly bad shape and the US in particular is looking like deaths may well continue through to June.

If your quarantine strategy is to handle a couple of weeks of "working from home", then you need to start rethinking what your plans are.  There could well be "travel only if necessary, work from home wherever you can" government guidance in place for a few more months at least.

Organisations are generally struggling to come to terms with this mass working from home, mostly I think because they insist on considering it to be working from home.  This WFH experience is something that many of us have experienced, we have a delivery or something happening that means that we can't be in the office for a day or two.  We tend to put off some of the tasks we normally do and focus on work we can do while relaxing at home.  We dial into all of our normal meetings where possible and we essentially recreate the office experience, just with ourselves away and cut off from the normal team working.

But as many people who work from home more regularly have been saying, there is a fundamental shift when it comes to moving from working from home occasionally to teleworking constantly to becoming distributed.  I'm sure you've been in meetings before where you felt like "this could have been an email", but the sheer quantity of video calls I've been in recently that were really unnecessary in many cases.

However, regardless of how distributed you are, I've got some tips that I think organisations should follow now if they haven't already.  If you want to be a successful distributed organisation, you should do the following:

### Get Google's GSuite for productivity

Yup, I'm sure that Microsofts Office 365 is almost as good, but in reality, for distributed consensus working, I cannot recommend working on a paper in Google Docs highly enough.  The ability to have a single document, for multiple people to edit at once, to switch into suggestion mode and make improvements and suggestions to a document, these are things that are almost essential for good distributed teams.

Furthermore, GSuite is more secure than your current office estate, fewer emails going around with attachments, few copies of the data being downloaded onto devices.  You can allow BYOD access from iPads and Tablets, and while not as good as a computer, you get a good experience.

GSuite has strong user identity controls, and if you signup to the the Advanced Protection program (requires 2 security keys, see below), then you'll have world class protection of your accounts and email systems.

If you cannot use GSuite then moving to Office 365 is a good alternative.  It brings many of the security controls that you want, while enabling the web access features of O365 means that your staff can work easily from home.

### Get slack

For creating a sense of team conversation, slack is amazing.  It can be a time sink and it can have all kinds of issues around attention, but nothing works as well and easily as slack for maintaining a feeling of "being part of the team" like shared team channels in slack.
Encourage your staff to have a team channel that isn't private, let people sit in other teams channels so they see or hear things that they wouldn't normally.  the transparency and openness helps recreate the overheard conversations and serendipity that you normally get from colocation in an office.
Additionally, actively encourage channels that are non work related.  When people are in the office they talk while making coffee or at the "water cooler", they talk about their weekends, their families, their cats.  so create channels where people can discuss their hobbies, their lives.  This creates a sense of community.

### Use modern web tools for collaboration

In this category I consider tools like Miro, Trello, Jira and so on.  These tools should be ones that are designed for the internet age, that assume that users are distributed and that security is provided via authentication.  If you can sign in with your google account as the recommended way of signing in, then it's a good tool.

These tools often allow multiple people to interact with the same thing at the same time, which makes it easier to not need to have a video call about it.  You can all contribute to a virtual whiteboard like Miro, seeing how people are moving their cursor around and what they are typing.  This helps the team feel like they know what everyone is doing.

### Provide password managers for all staff

You are going to have to put more stuff online on the internet.  Your staff are going to need to have lots more user accounts for all of these new systems and services.  If you can, you want people signing in with their Google account.  You know that's well protected and it's a single source of truth for leavers, but not everything will let you do that.  Additionally, you really want users using different passwords everywhere.  Provide them with a free tool that creates and stores different passwords. 

Additionally, when you aren't in the office, it's far harder to share passwords with your colleagues.  While we sometimes bemoan the password written on a post-it, in reality it is far more secure against many remote attackers than we like to admit.  Good modern password managers lets you have a team account where you can share passwords with each other, see when they are rotated and who has used them.  This lets you manage the passwords that needs to be shared effectively.

###  Invest in FIDO hardware keys like Yubikeys

For your Google accounts, and VPN's and maybe even for unlocking corporate devices, nothing is better than these hardware keys.  Some of your staff don't live in a nice multi-million pound house in Surrey, some of them live in shared apartments with slightly dodgy roommates.  They cannot keep an eye on their devices 100% of the time, but they can attach a USB key to their house keys, so that their computer cannot be used when they go out.

###  Invest in security monitoring

Forget disabling copy and paste, forget requiring a VPN for everything, forget requiring staff to dance the dance of VPN's and RDP servers and prviilege escalation to look up a phone number.  All of those security controls add stress to an already stressed set of staff, and they'll work around those controls if they have to.  They'll switch to using their personal gmail accounts and using off corporate systems just to avoid your restrictive controls.

The most important control you need is to understand the health of the device and account that someone uses.  That's your biggest risk right now, so monitor for it.  Invest in an MDM that can tell you how patched your devices are.  GSuite has some minor features here, and integrates with other tools when needed.  All of your corporate laptops and devices should be logging some data on the endpoint and shipping it into a centralised monitoring solution.  This will let you know if any of your devices have been compromised and enable you to either fix it, or tell the user what action to take.

In these times, we need to make sure that security is enabling people to get on with their job, get it done well and get it done with the minimum of difficulty.  These suggestions may not line up with your 5 year cybersecurity strategy, but if you cannot show value during this time, then you won't be considered valuable during the easy times either.

## [Capitalizing on Coronavirus Panic, Threat Actors Target Victims Worldwide](https://www.recordedfuture.com/coronavirus-panic-exploit/)

[https://www.recordedfuture.com/coronavirus-panic-exploit/](https://www.recordedfuture.com/coronavirus-panic-exploit/)

> Coronavirus has also been weaponized as a way to spread spyware by the Iranian government. Iran’s Health Ministry sent a message to victims advising them to download a specific application to monitor for potential symptoms of COVID-19. This application was, in reality, spyware. The malicious Android application, called ac19.apk, is capable of gathering victim location services and monitoring a user’s physical activity (such as walking or sitting) — ostensibly to determine where the user is going and when. The application is distributed on a website created by the Iranian government, https://ac19[.]ir/.


We know that phishers, organised crime and some other APT’s are using COVID-19 in their lures and attacks.  Although mostly this appears to be a shifting of attack capability, so while this is a new attack vector to defend against, it’s not a rise in the actual risk, because it comes with a reduction in the other attacks by those groups.

But this is chilling, a government is using COVID-19 warnings in order to increase spying on its own citizens by allegedly delivering malware from the government itself.


## [Advisory: COVID-19 exploited by malicious cyber actors - NCSC.GOV.UK](https://www.ncsc.gov.uk/news/covid-19-exploited-by-cyber-actors-advisory)

[https://www.ncsc.gov.uk/news/covid-19-exploited-by-cyber-actors-advisory](https://www.ncsc.gov.uk/news/covid-19-exploited-by-cyber-actors-advisory)

> In the UK, the NCSC has detected more UK government branded scams relating to COVID-19 than any other subject. Although, from the data seen to date, the overall levels of cyber crime have not increased, both the NCSC and CISA are seeing a growing use of COVID-19 related themes by malicious cyber actors. At the same time, the surge in home working has increased the use of potentially vulnerable services, such as Virtual Private Networks (VPNs), amplifying the threat to individuals and organisations.


A reminder that although terribly worded, the COVID-19 threat is coming primarily from phishing and social engineering, the lure part of an attack, and is primarily about existing attackers changing their operating tactics.

You'd easily be mistaken in believing that there was a new threat on the landscape that you must protect against, but the reality is that, generally speaking, these aren't new actors adding to the threat, but changing tactics.  However there might be a greater risk, as during this period, people are more nervous and far more likely to click well constructed phishing lures than they might be normally.


## [How I protected my home network - Caleb Sima - Medium](https://medium.com/@csima/how-i-protected-my-home-network-66797536a3cc)

[https://medium.com/@csima/how-i-protected-my-home-network-66797536a3cc](https://medium.com/@csima/how-i-protected-my-home-network-66797536a3cc)

> After running for two weeks with no noticeable security activity, my mother in-law dropped by and used the Wifi network. Almost immediately I received an alert of an Android device portscanning my network and accessing the data canary. The origin device causing all the trouble was, in fact, my mother in-law’s phone. Through the simple Fingbox UIs I immediately kicked the phone off the network and asked to take a peek at it. Sure enough, a malware scanner app confirmed the phone had an infection. Now that’s what I call success!


This is a lovely story of security made simple, easy to use and just working.  Caleb sets out at the beginning that they are not going to be doing security analysis, shipping their traffic anywhere or setting up complex trust zones, as that's all too much to ask.  I agree, I think security that is trivially easy to setup and only bothers you when something goes wrong is the right level for most people.

Shipping something like this to high value employees houses so that as an organisation you have some confidence that they have secure home working networks is an idea that you might want to consider


## [Attack matrix for Kubernetes](https://www.microsoft.com/security/blog/2020/04/02/attack-matrix-kubernetes/)

[https://www.microsoft.com/security/blog/2020/04/02/attack-matrix-kubernetes/](https://www.microsoft.com/security/blog/2020/04/02/attack-matrix-kubernetes/)

> When we in Azure Security Center started to map the security landscape of Kubernetes, we noticed that although the attack techniques are different than those that target Linux or Windows, the tactics are actually similar. For example, a translation of the first four tactics from OS to container clusters would look like 1. “initial access to the computer” becomes “initial access to the cluster”, 2. “malicious code on the computer” becomes “malicious activity on the containers”, 3. “maintain access to the computer” becomes “maintain access to the cluster”, and 4. “gain higher privileges on the computer” becomes “gain higher privileges in the cluster”.
> 
> Therefore, we have created the first Kubernetes attack matrix: an ATT&CK-like matrix comprising the major techniques that are relevant to container orchestration security, with focus on Kubernetes.


If you are running Kubernetes, then this framework will work well for you to help understand what attacks attackers might carry out, and how they will get there.  You can then work out where your detection capability is and where it's missing.


## [Decade of the RATs: Novel APT Attacks Targeting Linux, Windows and Android](https://blogs.blackberry.com/en/2020/04/decade-of-the-rats)

[https://blogs.blackberry.com/en/2020/04/decade-of-the-rats](https://blogs.blackberry.com/en/2020/04/decade-of-the-rats)

> BlackBerry researchers have released a new report that examines how five related APT groups operating in the interest of the Chinese government have systematically targeted Linux servers, Windows systems and Android mobile devices while remaining undetected for nearly a decade.
> 
> The BlackBerry report, titled Decade of the RATs: Cross-Platform APT Espionage Attacks Targeting Linux, Windows and Android, examines how APTs have leveraged the “always on, always available” nature of Linux servers to establish a “beachhead” for operations. Given the profile of the five APT groups involved and the duration of the attacks, it is likely the number of impacted organizations is significant.


This really should come as no surprise.  While there have been very few reports about linux based malware, it's not because there's fundamentally better security, it's because there's far less attention paid to detection capabilities in that area.

Linux runs on huge numbers of servers, in particular a lot of cloud servers use it for the low license costs.  That makes it a huge target for APT's and therefore we should expect that they have developed highly capable tools for this area.


## [Responsible Coronavirus Surveillance Is Possible, Privacy Experts Say](https://theintercept.com/2020/04/02/coronavirus-covid-19-surveillance-privacy/)

[https://theintercept.com/2020/04/02/coronavirus-covid-19-surveillance-privacy/](https://theintercept.com/2020/04/02/coronavirus-covid-19-surveillance-privacy/)

> The coronavirus tracking ramp-up is already well underway around the world. In South Korea, Taiwan, and Israel, authorities use smartphone location data to enforce individual quarantines. Moscow police say they’ve already busted 200 quarantine violators caught via facial recognition-enabled cameras. NSA contractor and perennial privacy offender Palantir is helping Britain’s National Health Service track infections. Apps that leverage a smartphone’s bounty of built-in, highly accurate sensors to enforce social distancing or map the movements of the infected have been deployed in Singapore, Poland, and Kenya; MIT researchers are now pitching a similar, but more “privacy friendly,” app. In Mexico, Uber sent government authorities rider data to trace the route of an infected tourist, also banning 240 users who’d taken rides with the same driver.


This sums up some pretty sensible recommendations about appropriate use of data to perform contact tracing during a health epidemic.  It's clear that the threat to life is great enough that some erosion of personal liberty might be necessary, but the key things that come out of these recommendations is that data used this way should be walled off and only used for this purpose.  

This is a good reminder that the best controls here are not technological ones that perform funky special things on bluetooth identifiers, but in reality the best controls will come from a strong contract between government and public, transparency about adhering to that contract and public trust.


## [Best Security Key for Multi-Factor Authentication 2020 | Reviews by Wirecutter](https://thewirecutter.com/reviews/best-security-keys/)

[https://thewirecutter.com/reviews/best-security-keys/](https://thewirecutter.com/reviews/best-security-keys/)

> The Yubico YubiKey 5 Series supports a wide array of security protocols, which makes it compatible with more online accounts than most other keys. Yubico also provides the best documentation, and its excellent introductory experience eases the process for newcomers. Compared with other security keys, the 5 Series offers more connection options, including USB-A, USB-C, and a dual-headed USB-C and Lightning-port model for iOS users. All of the full-size keys have a hole so you can attach them to any keychain, making them portable, and in our tests they proved durable after weeks of regular use. The YubiKey 5 Series can be a little more expensive than other keys with similar features, but its robust compatibility with more devices and accounts makes it worth the price.


This is a good review of various security keys.   I've been a fan of Yubikeys for a while, and I have the USB-C variant of the YubiKey set for my company accounts.

Some things that this article didn't cover, that I'd recommend:

1. It's possible, and indeed, I'd recommend buying more than one key or key type.  I have a backup key that is held in case I lose my main one.  You can add a second key to almost every service that supports yubikeys (With the annoying exception of AWS), and even a third.  This means you can buy both a USB-C connecting one and an NFC one if you want.

2. iOS support is more than a little flaky.  I don't use mine with my phone at all.  Most services have some work arounds, Google requires me to be at a computer where I can use the key to generate a code to type into my device, and many services support using a standard TOTP service like Authy or Google Authenticator instead.

The use of hardware keys is something you really only want to enable for high value accounts.   It can be fiddly to go find them when needed.  I use mine to:
* Unlock last pass
* Login to Github once every 30 days/new browsers
* Login to GSuite/Gmail whenever Google is worried about security
* Using the AWS Console for my root account

For pretty much everything else, I rely on Last Pass to generate strong passwords and TOTP codes from Authy instead.  Those services are probably the most valuable/interesting ones that I use, and so the ones that I'll tolerate the most restrictions on.


## [RDP Drawing Unwanted Attention | Decipher](https://duo.com/decipher/rdp-drawing-unwanted-attention)

[https://duo.com/decipher/rdp-drawing-unwanted-attention](https://duo.com/decipher/rdp-drawing-unwanted-attention)

> Since the beginning of March, when some organizations began instituting either voluntary or mandatory remote work policies, researchers have seen increases in both the number of RDP servers exposed to the Internet and the number of unique IP addresses scanning for those servers. According to data gathered by Shodan, the device search engine, the number of RDP servers exposed on the default port (3389) has increased steadily, and eight percent of those servers are still vulnerable to BlueKeep. In the United States alone, more than 38,000 servers are still vulnerable to BlueKeep.


Of course, if you want your staff to work remotely from home, and normally they use RDP a lot, then you need to expose that RDP server to them.  

More likely is a number of organisations using rapidly deployed RDP servers to enable staff to work from home without having a work laptop.  But again, this needs to be exposed to all of your staff.

This is an area where you want better controls in place.  RDP has built in authentication mechanisms, but has a history of critical vulnerabilities including a preauthentication attack such as BlueKeep.  That means that all the MFA and password policies in the world won't protect you.  IP Whitelisting or other access controls are necessary here, and rolling out a VPN solution to your staffs personal devices is probably the best (and most expensive) way to solve this.

I'll note that you can throw together a [client VPN using AWS](https://aws.amazon.com/vpn/) pretty easily, it supports a good IPSec VPN stack, can authenticate using your existing AD services, and support split tunnelling (by IP address) so you only intercept traffic for your corporate servers.


## [SANS Security Awareness Work-from-Home Deployment Kit | SANS Security Awareness](https://www.sans.org/security-awareness-training/sans-security-awareness-work-home-deployment-kit)

[https://www.sans.org/security-awareness-training/sans-security-awareness-work-home-deployment-kit](https://www.sans.org/security-awareness-training/sans-security-awareness-work-home-deployment-kit)

> SANS Security Awareness Work-from-Home Deployment Kit
> From a comprehensive step-by-step guide on how to implement a remote security initiative across the organization to quick tips, videos and newsletters for individuals and families, the SANS Security Awareness Work-from-Home Deployment Kit covers everything you need to know to protect your business and your family. 


I was really torn on whether to include this or not.  I like that this resource exists, I think the setting out the 3 different audiences, organisation leaders, individuals working from home, and parents is a great way to segment the guidance.

However, the guidance itself is ... well, rather poor.  The deployment guide doesn't actually say anything, it's a lot of links to various other resources that SANS have provided.  And while that's helpful to a degree, for an organisation leader who is trying to setup remote working from home, it might have been nice to pull those resources together into one pack for them. 


## [Distributed Work’s Five Levels of Autonomy – Matt Mullenweg](https://ma.tt/2020/04/five-levels-of-autonomy/)

[https://ma.tt/2020/04/five-levels-of-autonomy/](https://ma.tt/2020/04/five-levels-of-autonomy/)

> The first level is where most colocated businesses are: there’s no deliberate effort to make things remote-friendly, though in the case of many knowledge workers, people can keep things moving for a day or two when there’s an emergency. More often than not, they’ll likely put things off until they’re back in the office. Work happens on company equipment, in company space, on company time. You don’t have any special equipment and may have to use a clunky VPN to access basic work resources like email or your calendar. Larger level one companies often have people in the same building or campus dialing into a meeting. Level one companies were largely unprepared for this crisis.


This is what I see in so many companies at the moment.  The move has been to treat this extended quarantine as an extended "working from home day".  But the way we think about work, about how we conduct meetings and how we continue to operate has to change fundementally to actually turn this into something that works long term.


