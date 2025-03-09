---
title: "253 - Here little phishy"
date: 2025-01-26
description: "Phishing remains one of the biggest problems for firms in 2025, and we don't seem to be doing the right things about it."
permalink: /here-little-phishy/
---

Phishing remains one of the biggest problems for firms in 2025, and we don't seem to be doing the right things about it.

Let's face it, people attempting to socially engineer users into doing the wrong thing is going to remain a fundamental meta problem for decades to come, phishing is just one manifestation of that.  But we seem to remain incredibly suspectable to phishing attacks as an industry, and mostly what we are focused on isn't necessarily about fixing the problem, but more about addressing some of the symptoms.

Good, high quality phishing attempts will likely get even the most security aware users in the end.  There's a lot of insecure infrastructure out there, and people do make fat-finger errors that make it far to easy to take over a domain, or adopt a cloak of respectability.  Many of these issues are in fact edge cases of the way existing systems work, and as such, they often have to work they way they do for a good user experience for all of the users who just want to use the service correctly.  That makes them hard to fix and means that we're almost always going to find more over the coming years.

Instead we have to assume that phishing attempts are here to stay for us, and we need to ensure that our users are unable to be affected by them.

The example of Microsoft starting to run javascript on webpages from incoming links, including javascript that sends POST requests is an example of the kind of defence that I think we need, but which has some implications for web development.  It will upset some people and it will create problems down the line, but it's because they have to legitimately look at how to best detonate links that would compromise a user.

Of course, and as always, securing your users devices with hardware tokens, like FIDO2 tokens remains one of the strongest phish-proof systems you can have to protect your users credentials and ensure that they cannot be stolen and used remotely.  But there are other attacks out there, and if we get adoption of phishing resistant MFA high enough, we'll start to see pivots back to drive by downloads, compromise of browsers and of course supply chain attacks.

That can all be a bit grim and depressing, so I thought I'd end this week with a reminder about what I love about technology, which is to say, doing something cool just because you can.

## [almost_pwned.md ](https://gist.github.com/zachlatta/f86317493654b550c689dc6509973aa4)

[https://gist.github.com/zachlatta/f86317493654b550c689dc6509973aa4](https://gist.github.com/zachlatta/f86317493654b550c689dc6509973aa4)

> g.co, Google's [official](https://en.wikipedia.org/wiki/G.co) URL shortcut (update: or Google Workspace's domain verification, see bottom), is compromised. People are actively having their Google accounts stolen.
> 
> Someone just tried the most sophisticated phishing attack I've ever seen. I almost fell for it. My mind is a little blown. 


This is a nasty phishing attack that makes use of what looks like an edge case in Google’s GSuite setup, which means that an external user can make Google send an email that appears to come from a subdomain of g.co.  That email will appear to be fully authenticated and legitmately come from Google.  Combined with Google Voice, it creates a number of trust indicators that even technically competent people may well fall for.

I think the one thing that I’d recommend here, is that if there is any suggestion that you are talking to one of the big tech companies security team, that you actively do go through the process of hanging up/stopping the call and go back via your normal support route. 


## [Shifting Cyber Norms: Microsoft security POST-ing to you - Bert Hubert's writings ](https://berthub.eu/articles/posts/shifting-cyber-norms-microsoft-post/)

[https://berthub.eu/articles/posts/shifting-cyber-norms-microsoft-post/](https://berthub.eu/articles/posts/shifting-cyber-norms-microsoft-post/)

> _tl;dr: Microsoft and other email security scanners will visit the links in email you transmit, and run the JavaScript in those links, including calls that lead to POSTs going out. This used to be unacceptable, since POSTs have side effects. Yet here we are. This breaks even somewhat sophisticated single-use sign-on / email confirmation messages._ On my Mastodon profile I have [pinned this quote](https://fosstodon.org/@bert_hubert/111765180339350988) : _“Writing has been called the process by which you find out you don’t know what you are talking about. Actually doing stuff meanwhile is the process by which you find out you also did not know what you were writing about.” - from_ [_A 2024 Plea for Lean Software (with running code)_](https://berthub.eu/articles/posts/a-2024-plea-for-lean-software/) Recently I’ve been actually _doing_ some things again, namely, [building a site that monitors Dutch parliament](https://opentk.nl/) where users can configure monitors that inform them of parliamentary happenings. This involves having people sign up, sending email, getting users to log in and out etc.
> 
> From this I learned yesterday that a user could no longer perform a password-less sign-on to my site, instead always being told that the single-use link had been used already. How come? 


The continuing war against phishing scams means that we have to change what happens, and I don’t know how I feel about this.

What’s actually happening here is that originally email sign in loops used to send out an email with a one time use link that you could click.  Clicking that link would then take you to the website and set the appropriate authentication cookies, meaning you are signed in, and critically proving that you are able to recieve email at a given address.

For  a while now, a number of major email providers have had tools that attempt to follow links in emails to check that it doesn’t trigger the download of malicious software.  This breaks systems that have a single use of the link.  Dealing with that tends to come in a couple of workarounds, allowing any number of links in a given time period, allowing a fixed number of links, but more than 1, and changing to using POST links instead.

Personally, for usability reasons, I’ve normally recommended the first, which is to allow any number of users to click the link, but this adds security issues.  If a user forwards the email to a non-work device, they can log in there, if an adversary has managed to get autoforward enabled on the targets account, they can use the link etc.

What happened here is that the link that you click in the email takes you to a webpage, where you are expected to click a button saying “yes, I sign in”.  That button click creates a POST instead of a simple GET, and we can allow any number of the original get requests, but just one POST request.  

But users hate an extra click, and research almost always shows drop off as users fail to click through, get distracted etc.  So in this case, there is javascript on the page that automatically clicks the login button.

What’s being complained about here is that Microsofts security scanner is not just fetching the link in the email, but is actively running javascript on the page to see what happens.  

Broadly speaking from a security perspective, I want this.  It’s otherwise a great way of getting around phishing detection, and javascript that then redirects you to a malware download, or clicks a button that then delivers you malware would be a great way to get around scanning/

But as someone who builds login systems, I agree that this pushes us back towards a pattern where we have to allow multiple users to be able to click the login field, and that opens a small but non-negligible security hole. 


## [Register Yubikeys on behalf of your users with Microsoft Entra ID FIDO2 provisioning APIs - JanBakker.tech ](https://janbakker.tech/register-yubikeys-on-behalf-of-your-users-with-microsoft-entra-id-fido2-provisioning-apis/)

[https://janbakker.tech/register-yubikeys-on-behalf-of-your-users-with-microsoft-entra-id-fido2-provisioning-apis/](https://janbakker.tech/register-yubikeys-on-behalf-of-your-users-with-microsoft-entra-id-fido2-provisioning-apis/)

> Microsoft recently announced their new FIDO2 provisioning APIs within Microsoft Entra ID. While users can register their FIDO2 keys fairly easily with a Temporary Access Pass, the new API allows admins to register keys on behalf of a user. This can be extremely handy in onboarding scenarios or in case a new key needs to be shipped to a vendor or contract worker.
> 
> The Microsoft APIs support every vendor of FIDO2 (passkeys), but Yubico has made some extra effort to provide a sample Python script that uses the Yubikey Manager under the hood. For the folks scared to touch Python (I feel ya), please go to the end of the blog post for PowerShell sample code ( [creds](https://blog.icewolf.ch/archive/2024/10/25/register-FIDO2-passkey-in-entra-id-on-behalf-of-users-with-powershell/) ), but don’t skip the theory. It’s essential to understand the process. 


This is very nice, the ability to preregister keys into your authentication suite means that your employee onboarding process can get simpler for the employees and easier.  You can now post a key out to a user in advance of them starting, and know that it will start on day 1, without needing to put users into special groups that allow one time login without MFA, or using Temporary Access Passes.

Anything that makes this stuff easier to use is a good thing 


## [Security Is A Useless Controls Problem - by Jonathan Price ](https://securityis.substack.com/p/security-is-a-useless-controls-problem)

[https://securityis.substack.com/p/security-is-a-useless-controls-problem](https://securityis.substack.com/p/security-is-a-useless-controls-problem)

> If the control can only be explained in a nebulous way, such as "to improve security" or "for compliance reasons", that's probably a useless control. If the security-ish person forcing the control on you cannot adequately explain it, it's probably because they have no idea why themselves. If that security-ish person doesn't understand why, it's a good heuristic that there isn't a legitimate why at all.
> 
> "But Jon," you say, unhappily trapped in this conversation, "What if the reasoning is very complex and hard to explain to people who are not experienced security masters?". This is a fair question on the surface.
> 
> How many controls can you think of that you know are useful, and you genuinely know why they are, but you can't explain it in 2-3 sentences to someone with a modicum of technical understanding? 
> 
> […]
> 
> There are many complex things about security, but these are almost all in _how_ we do things. The why is almost always pretty simple.
> 
> When I rant about this with my peers, mentors, friends, family, and unfortunate bystanders at the bar, a common reframe is, "Why is this so bad"? It's still people caring about security. So what if some of that isn't as effective as it could be?
> 
> We are so resource-constrained as an industry. There's not enough manpower, budget, and political capital. We can't be wasteful while still being effective stewards of the systems and data entrusted to us. We can't waste any of it! And we certainly can't keep asking for more budget when we're blowing 50% of what we already have on useless crap. 


I couldn’t agree more with this essay if I tried.  I have found myself many times arguing with compliance people or lead engineers about security controls that they think should be in a system just because that’s how they’ve always been done.

I think my personal least favourite is installing antivirus onto bits of the system, normally with a terrible free antivirus system that is based purely on signatures.  That control is rarely the right control, and yet it comes up more often than I like to count. 


## [MasterCard DNS Error Went Unnoticed for Years – Krebs on Security ](https://krebsonsecurity.com/2025/01/mastercard-dns-error-went-unnoticed-for-years/)

[https://krebsonsecurity.com/2025/01/mastercard-dns-error-went-unnoticed-for-years/](https://krebsonsecurity.com/2025/01/mastercard-dns-error-went-unnoticed-for-years/)

> From June 30, 2020 until January 14, 2025, one of the core Internet servers that MasterCard uses to direct traffic for portions of the mastercard.com network was misnamed. MasterCard.com relies on five shared Domain Name System (DNS) servers at the Internet infrastructure provider **Akamai** [DNS acts as a kind of Internet phone book, by translating website names to numeric Internet addresses that are easier for computers to manage].
> 
> All of the Akamai DNS server names that MasterCard uses are supposed to end in “akam.net” but one of them was misconfigured to rely on the domain “ **akam.ne** .”
> This tiny but potentially critical typo was discovered recently by **Philippe Caturegli** , founder of the security consultancy [Seralys](https://www.seralys.com/) . Caturegli said he guessed that nobody had yet registered the domain akam.ne, which is under the purview of the top-level domain authority for the West Africa nation of [Niger](https://en.wikipedia.org/wiki/Niger) .
> 
> Caturegli said it took $300 and nearly three months of waiting to secure the domain with the registry in Niger. After enabling a DNS server on akam.ne, he noticed hundreds of thousands of DNS requests hitting his server each day from locations around the globe. Apparently, MasterCard wasn’t the only organization that had fat-fingered a DNS entry to include “akam.ne,” but they were by far the largest. 


This is a great writeup of what could have been a critical misconfiguration.  It also emphasises the importance of ensuring that you have appropriately skilled and capable people managing vulnerability disclosure.

In the vast majority of vulnerability disclosures, the work to fix, the vulnerability and the implications are minor.  But there is a set of issues that have fundamental implications for your infrastructure.  Catching those and ensuring that your response isn’t along the lines of “No biggie” is important in protecting your brand.

In this case, there’s almost certainly a lot of liability and security concern that prevents Mastercard from saying much about this, but at the very least, the first thing you want to do is thank the researcher for their time, and try to bring them inhouse to help ensure that both the issue is fixed, but also to understand the root cause of the issue. 


## [Latest Cyberhaven Report: 8 Extensions Affecting 1.1M Users ](https://spin.ai/blog/cyberhaven-attack-puts-more-users-at-risk/)

[https://spin.ai/blog/cyberhaven-attack-puts-more-users-at-risk/](https://spin.ai/blog/cyberhaven-attack-puts-more-users-at-risk/)

> Spin.AI’s latest research has uncovered 8 additional compromised browser extensions, used by 1.1 million users during the time of compromise. This discovery brings the total number of compromised extensions to 41, impacting 3.7 million users in total.
> 
> The fallout from the Cyberhaven cyberattack continues to escalate. New findings by Spin.AI reveal the scale of affected users targeted with compromised extensions is even larger than initially thought. The attack is now known to have compromised additional browser extensions, putting 3.7 million users at risk. **Brief Overview of the Cyberhaven Incident** The [Cyberhaven cybersecurity incident](https://spin.ai/blog/risks-of-browser-extensions-cyberhavens-breach/) first became known when its extension developer fell victim to a phishing attempt and consequently, had malicious code injected into its Chrome extension. After investigation by [Cyberhaven](https://www.cyberhaven.com/engineering-blog/cyberhavens-preliminary-analysis-of-the-recent-malicious-chrome-extension) , [Secure Annex](https://secureannex.com/blog/cyberhaven-extension-compromise/) , and others, it was uncovered that this attack is part of a broader campaign to target Chrome Extension developers. 


I’m afraid that we’ll see a lot more of these attacks in the coming years.  So much of our infrastructure is interacted with through web browsers now that directly attacking web browsers is powerful for attackers. 

All of our security controls around authentication, encryption, and management can all be worked around if the adversary can get inside the browser itself.  While modern browsers offer excellent security models, they are by definition, designed to enable plugins to interfere with the users web experience.

Secondly, it’s far less common for small and medium businesses or even some large businesses to both manage the applications on the desktop, but also offer management of the browser plugins.  It’s possible to do, but by default, it’s often easy for users to install plugins as a user without any company supervision.

These are attractive for users, they often help them do their job, and they may well have lower security controls around them than standalone applications. 


## [Critical infrastructures cannot be secured because network security and engineering won’t work together | Control Global ](https://www.controlglobal.com/blogs/unfettered/blog/55260023/critical-infrastructures-cannot-be-secured-because-network-security-and-engineering-wont-work-together)

[https://www.controlglobal.com/blogs/unfettered/blog/55260023/critical-infrastructures-cannot-be-secured-because-network-security-and-engineering-wont-work-together](https://www.controlglobal.com/blogs/unfettered/blog/55260023/critical-infrastructures-cannot-be-secured-because-network-security-and-engineering-wont-work-together)

> “Equipped with an Ethernet interface and Webserver, Vendor A Unit Substations now provide simple, affordable access to power system information – including transformer coil temperatures – using a standard Web browser. The pre-engineered equipment connects to a customer’s existing Ethernet LAN much like adding a PC or printer. Unit substations include a Temperature Controller, which provides remote access to transformer data, in addition to its primary role in controlling cooling fans.”
> 
> I reviewed the 2023 instrument data sheets on 
> digital pressure transmitters from four major US and international 
> process sensor manufacturers. All four of the vendors are actively 
> involved in industry cybersecurity activities. The data sheets were more
>  than 70 pages.
> 
> Consequently, I did a word search on the following terms: cyber, 
> security, passwords, authentication and encryption. The four vendors’ 
> data sheets did not mention any of those terms. On the other hand, I did
>  a word search on the word “remote.” That term was used extensively as 
> all four vendors support remote connectivity. Or as a colleague stated, 
> engineers will pay extra for remote access without considering the 
> cybersecurity issues associated with that capability.
> 
> Additionally, in one data sheet, Bluetooth was enabled by default 
> assuming that distance will mitigate any cyber vulnerabilities – a 
> questionable assumption at best. In fact, in the June 2023 issue of 
> Control Global – “Updated pressure transmitter increases technician 
> safety and makes work faster and easier" – powerful features like 
> graphical back-lit display, Bluetooth connectivity, easier to navigate 
> user interfaces, level and flow specific configurations and diagnostic 
> features allow you to perform commissioning, maintenance and 
> troubleshooting tasks faster than ever”. 


If this doesn’t terrify you, I don’t know what will.  It’s not sufficient to assume that only good people are on the network, but at the same time, some of these systems can’t support the sorts of security measures we expect.  You need someone with knowledge and understanding of both to ensure the system is secure 


## [Let’s talk about AI and end-to-end encryption – A Few Thoughts on Cryptographic Engineering ](https://blog.cryptographyengineering.com/2025/01/17/lets-talk-about-ai-and-end-to-end-encryption/)

[https://blog.cryptographyengineering.com/2025/01/17/lets-talk-about-ai-and-end-to-end-encryption/](https://blog.cryptographyengineering.com/2025/01/17/lets-talk-about-ai-and-end-to-end-encryption/)

> Modern end-to-end encrypted messaging systems provide a very specific set of technical guarantees. Concretely, an end-to-end encrypted system is designed to ensure that plaintext message content in transit is not available anywhere except for the end-devices of the participants and (here comes the Big Asterisk) _anyone the participants or their devices choose to share it with._ The last part of that sentence is very important, and it’s obvious that non-technical users get pretty confused about it. End-to-end encrypted messaging systems are intended to deliver data securely. _They don’t dictate what happens to it next._ If you take screenshots of your messages, back them up in plaintext, copy/paste your data onto Twitter, or hand over your device in response to a civil lawsuit — well, that has really nothing to do with end-to-end encryption. Once the data has been delivered from one end to the other, end-to-end encryption washes its hands and goes home
> Of course there’s a difference between _technical guarantees_ and the promises that individual service providers make to their customers. For example, Apple says this about its iMessage service:
> 
> I can see how these promises might get a little bit confusing! For example, imagine that Apple keeps its promise to deliver messages securely, but then your (Apple) phone goes ahead and uploads (the plaintext) message content to a different set of servers where Apple really can decrypt it. Apple is absolutely using end-to-end encryption in the dullest technical sense… yet is the statement above really accurate? Is Apple keeping its broader promise that it “can’t decrypt the data”?
> 
> […]
> 
> Or put differently: would you even blame governments for demanding access to a resource like this? And how would you stop them? After all, think about how much time and money a law enforcement agency could save by asking your agent sophisticated questions about your behavior and data, questions like: “does this user have any potential CSAM,” or “have they written anything that could potentially be hate speech in their private notes,” or “do you think maybe they’re cheating on their taxes?” You might even convince yourself that these questions are “privacy preserving,” since no human police officer would ever rummage through your papers, and law enforcement would only learn the answer if you were (probably) doing something illegal.
> 
> This future worries me because it doesn’t really matter what technical choices we make around privacy. It does not matter if your model is running locally, or if it uses trusted cloud hardware — _once a sufficiently-powerful general-purpose agent has been deployed on your phone_ , _the only question that remains is who is given access to talk to it._ Will it be only you? Or will we prioritize the government’s interest in monitoring its citizens over various fuddy-duddy notions of individual privacy. 


As always, this is excellently thought through, and much more about social contracts than the actual engineering or science involved.  As I’ve said a lot recently, control of the endpoints is often far more important than the encryption, because the data will lie unencrypted on your device when you are using it.  I think there’s something really powerful about this question of who is going to control what AI on our end devices will actually do, and what it will be trying to achieve.  I think that most people building these systems is legitimately and honestly trying to do the best thing for people that they can, whether that be to enable users to write emails well, or summarise their life, but each person is likely looking at the problem in isolation.  It’s useful to have people step back and look at the entire system, and ask questions about it all.

I’m an AI optimist, I think that it’s getting better faster than it’s generating “slop”, and I think it will be a net benefit to humanity, but there are a lot of caveats and complexity that we need to get through, as we have with any technological revolution in the past. 


## [CVSS is dead to us | daniel.haxx.se ](https://daniel.haxx.se/blog/2025/01/23/cvss-is-dead-to-us/)

[https://daniel.haxx.se/blog/2025/01/23/cvss-is-dead-to-us/](https://daniel.haxx.se/blog/2025/01/23/cvss-is-dead-to-us/)

> In the end of 2024 I was informed by friends that several infosec related websites posted about a new curl-related _critical_ security problem. Since we have not announced any critical security problems since 2013, that of course piqued my interest so I had a look.
> 
> It turned out that CISA had decided that [CVE-2024-11053](https://curl.se/docs/CVE-2024-11053.html) should be earned a CVSS 9.1 score: CRITICAL, and now scanners and news outlets had figured that out. Or would very soon.
> 
> The curl security team had set the severity to LOW because of the low risk and special set of circumstances that are a precondition for the problem. Go read it yourself – the fine thing with CVEs for Open Source products is that the source, the fix and everything is there to read and inspect as much as we like.
> 
> The team of actual experts who _knows_ this code and _perfectly understands_ the security problem says LOW. The team at CISA overrides that and insists that are all wrong and that this problem risks breaking the Internet. _Because we apparently need a CVSS at all costs._ **A git repository** One positive change that the switch to CISA from NVD brought is that now they host their additional data in [GitHub repository](https://github.com/cisagov/vulnrichment) . Once I was made aware of this insane 9.1 score, I took time of my Sunday afternoon with my family and made [a pull-request there](https://github.com/cisagov/vulnrichment/pull/151) urging them to at least lower the score to 5.3. That was a score I could get the calculator to tell me.
> 
> I wanted to have this issue sorted and _stomped down_ as quickly as possible to if possible reduce the risk that security scanners everywhere would soon start alerting on this and we would get overloaded with queries from concerned and worried users.
> It’s not like CISA gets overloaded by worried users when they do this. Their incompetence here puts a load on no one else but the curl project. But sure, they got their CVSS added.
> 
> After my pull request it took less than ninety minutes for them to [update the curl records](https://github.com/cisagov/vulnrichment/commit/91fadb2bf6b461638c8155978b9f20cf17e51fe3) . Without explanation, with no reference to my PR, they now apparently consider the issue to be CVSS 3.4. 


I’ve agreed with Daniel on this for a while, CVSS scoring system is utterly context independent and can create a lot of peverse incentives.

CVSS roughly scores based on whether a vulnerability  is remotely triggerable, how complex it is to trigger, privileges required and a few other scores.  But it is still very much based on aa very highlevel and antiquated understanding of modern architectures. 

It rarely takes into account whether local configuration can change whether the vulnerability is exploitable, and it doesn’t really have much ability to be contextualised as to what access to your network an adversary has to have.

The problem is that because it’s “standardised”, it’s becoming increasingly common for supplier contracts to require emergency patching or remediation activities if a vulnerability has a CVSS score greater than a given number.  But again, that can lack context, I’ve known of suppliers who have had to stop doing urgent and important patching that has real security implications for their customer in order to patch “external vulnerabilities” of CVSS 9.8 level in infrastructure that is not customer accessible and would have an incredibly low impact in the environment.

If you have an existing contract that looks like this, I’d strongly advise that you have a mechanism that allows you to either promote or demote the CVSS of a vulnerability based on contextual information for your organisation.  You might need something fixed in one or two places, but not need an all hands on deck in all systems. 


## [Subpixel Snake: The Web's Smallest Game - YouTube ](https://www.youtube.com/watch?v=iDwganLjpW0)

[https://www.youtube.com/watch?v=iDwganLjpW0](https://www.youtube.com/watch?v=iDwganLjpW0)

> This is a video about a JavaScript Snake game I wrote that uses the subpixels on your monitor as the board for the game Snake. It's so small that you need a microscope to play it correctly. 
> 
> Game: [https://patorjk.com/games/subpixel-sn...](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbXVYRmNtMll5NXc2M20xLThCMi01bG1Ea1VEd3xBQ3Jtc0tsTmhBejBidW5iY09jTE9vQmFtbml2WXc0MG9iVzlhWWw3Qjk1M0lHYnh0M2RXblkwZk93VEFJZmFKRkhVZWQ5UGgwRjd5eUM0ZUdHQ3AxNXd0SWxuZVg2WEN3RTR3bEZLRDBEWG1DdmRGb2FBN0x0NA&q=https%3A%2F%2Fpatorjk.com%2Fgames%2Fsubpixel-snake%2F&v=iDwganLjpW0) Code: [https://github.com/patorjk/subpixel-s...](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbmlBckFLRy1WSTh5czNkUUV1U1p0TmhfVjd1UXxBQ3Jtc0trcTlLOTc2cVcxN2M5VDJWN2dUQ2RJNDlBak9DejZZUVpfS2ViUnE3dmJPclIxanpsU24yMGsyMnBJUFhoYzVnYUlMbUtQMEwyQW1sQWZha05pLWFraXdTYWdQZEc1UW5iVklYSG4xVzhoeXl6dEE1SQ&q=https%3A%2F%2Fgithub.com%2Fpatorjk%2Fsubpixel-snake&v=iDwganLjpW0) Resource for subpixel geometries: [https://geometrian.com/resources/subp...](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbE5VUVFEUDFFQ2lfN1BTaEd4MV9uazFCRjVOUXxBQ3Jtc0tuUlF6TjRQWkN0SHdLTzhQS0EteW5ITTFnWEp5RGN6VmJxdW0yQzZETWpFdzRQWEZFOE1WWmJ0MldhRDlCcGZfVkZtU1ZySDk3SmlkVUg1aHdaenhSMWxaTDJPT01vb2VIRmFncG1RVEdQcmU2dmQtdw&q=https%3A%2F%2Fgeometrian.com%2Fresources%2Fsubpixelzoo%2F&v=iDwganLjpW0) 


I just thought this was unbelievably cool, a game of snake measured around 5 pixels wide. 


