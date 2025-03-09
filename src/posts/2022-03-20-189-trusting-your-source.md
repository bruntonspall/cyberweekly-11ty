---
title: "189 - Trusting your source"
date: 2022-03-20
description: "I’ve referred before to the excellent XKCD cartoon that reminds us that huge amounts of modern commercial systems and code rely on a library maintained by a [single open source developer somewhere in Nebraska](https://xkcd.com/2347/)."
permalink: /trusting-your-source/
---

I’ve referred before to the excellent XKCD cartoon that reminds us that huge amounts of modern commercial systems and code rely on a library maintained by a [single open source developer somewhere in Nebraska](https://xkcd.com/2347/).

But have really thought about what that really means, about what the implications are?  This week has driven the problem home in a number of ways.

Software dependencies in modern applications is a bit like a matryoshka doll or a recursive algorithm gone wrong.  Because it’s not just that the one library, whether it be libcurl, zlib, log4j or whatever, it’s that huge amounts of the open source ecosystem is built around a very small number of core committers.  And many of those core committers have opinions, political opinions, and regardless of how good a country/person/organisation you are, someday, someones political opinions will be opposed to you and your work.

Much of the time we have systems that can help us react to failures of the people kind, systems that let us flag a dependency as malicious, or remove it from the build chain.  But a lot of those systems assume that everybody is capable of changing their build system and dependencies at speed.  But there are computer systems that haven’t been recompiled in decades, there are computer systems that may not compile under modern tool chains, and there are computer systems for which we’ve lost the original source code and must modify purely through the medium of binary patches.  

If instead of reacting, we want to proactively defend, then we start to look at some of the software dependency tracking solutions.  But a lot of the supply chain solutions that are out there, are focused on attestation proofs.  Essentially confirming that this bit of software contains the following libraries, and we’re really really confident that when it says version 1.14.1 it actually was the same version released at that time.

That helps to protect us against malicious software injection into our dependency systems, so that a random third party cannot upload a different dependency that isn’t what the author intended.  But that attack is pretty rare, and mostly involves pretty high end attackers with specific motivates.

Instead the problem that we’ve run into more and more, from the log4j issue to the recent terraform license change to the npm package that wipes your desktop, these are all bugs or malicious code in the system, deliberately put in there by the creator.  Any and all attestation tools are simply going to confirm that the creator did in fact author that change and they did so willingly and aware of what it would do.  (Ok, that might be stretching it with log4j, as it was an unintended consequence in that case).

What we don’t have yet is any mechanism to protect us against either a bad actor, or simply one with opinions that differ from our own who wants to carry out what they view as legitimate protest.

That mechanism would need to be a socio technical mechanism, one that includes the humans as part of it, instead of simply assuming that the only thing that matters is the bits and bytes of the source code.

If we can crack that, we can also start to look at the levels of trust we have in those authors, the sorts of controls they have around their accounts and systems, because as well as catching malicious actors, we’d start to develop an understanding of what a compromised developer might look like and how to defend their credentials, their systems and their libraries.

Alternative titles this week: “Use the source (luke)”, “Abusing the source”.  I really wanted a pun headline, but I’m not very good with puns, sorry.

## [On the weaponisation of open source | Tales about Software Engineering ](https://beny23.github.io/posts/on_weaponisation_of_open_source/)

[https://beny23.github.io/posts/on_weaponisation_of_open_source/](https://beny23.github.io/posts/on_weaponisation_of_open_source/)

> The author of the change discussed this on Hacker News and it has since changed it to be “Additional Information” rather than “Additional Terms and Conditions” - but the `putin_khuylo` code change remains in the module.
> 
> In my opinion that raises eyebrows (if not red flags) about the “safety” of these components. It looks like these changes were made straight into the `master` branch without pull requests - that does suggest a lack of review process. These actions have negatively impacted the trust in the maintainers. And that makes me wonder whether using those components is safe.
> 
> Furthermore, from a licencing perspective, some organisations have guidelines of what licences are allowed, so if it can be demonstrated that the code breaks the clauses of the license, would it still be safe to use it? Some war stories about frantically removing “infectious” GPL’d libraries make me think the lawyers might have a field day. 


Great analysis on some of the recent stories on the changes in open source software.  As Gerald says, the risk here is that it utterly destroys trust in both this library and in open source software itself. 


## [JavaScript library updated to wipe files from Russia systems • The Register ](https://www.theregister.com/2022/03/18/protestware_javascript_node_ipc/)

[https://www.theregister.com/2022/03/18/protestware_javascript_node_ipc/](https://www.theregister.com/2022/03/18/protestware_javascript_node_ipc/)

> The developer of JavaScript library node-ipc, which is used by the popular vue.js framework, deliberately introduced a critical security vulnerability that, for some netizens, would destroy their computers' files.
> 
> Brandon Nozaki Miller, aka RIAEvangelist on GitHub, created node-ipc , which is fetched about a million times a week from the NPM registry, and is described as an "inter-process communication module for Node, supporting Unix sockets, TCP, TLS, and UDP."
> 
> It appears Miller intentionally changed his code to overwrite the host system's data, then changed the code to display a message calling for world peace, as a protest against Russia's invasion of Ukraine. GitHub on Wednesday declared this a critical vulnerability tracked as CVE-2022-23812. 


An upstream library that starts wiping files on your computer because the author disagrees with your politics?  That’s a chilling vulnerability, because open source software is written from almost every location on the globe, and many countries disagree with one another.

Everyone uniformly agrees that this is bad, but why is it that package managers still allow this kind of action and activity?  Running code when installing on the local machine is something that shouldn’t ever happen, as it’s simply too dangerous. 


## [feat: Made it clear that we stand with Ukraine · terraform-aws-modules/terraform-aws-ec2-instance@6867788 · GitHub ](https://github.com/terraform-aws-modules/terraform-aws-ec2-instance/commit/6867788411a202b61187f9935e9eaa72a18f0bbe)

[https://github.com/terraform-aws-modules/terraform-aws-ec2-instance/commit/6867788411a202b61187f9935e9eaa72a18f0bbe](https://github.com/terraform-aws-modules/terraform-aws-ec2-instance/commit/6867788411a202b61187f9935e9eaa72a18f0bbe)

> **## Additional terms of use for users from Russia and Belarus** By using the code provided in this repository you agree with the following:
> 
> * Russia has [illegally annexed Crimea in 2014](https://en.wikipedia.org/wiki/Annexation_of_Crimea_by_the_Russian_Federation) and [brought the war in Donbas](https://en.wikipedia.org/wiki/War_in_Donbas) followed by [full-scale invasion of Ukraine in 2022](https://en.wikipedia.org/wiki/2022_Russian_invasion_of_Ukraine).
> * Russia has brought sorrow and devastations to millions of Ukrainians, killed hundreds of innocent people, damaged thousands of buildings, and forced several million people to flee.
> * [Putin khuylo!](https://en.wikipedia.org/wiki/Putin_khuylo!) 


This change to a license is really peculiar.  To the author, a ukrainian national, it’s about their software being an extension of them and their politics. 
But in a consuming organisation, it’s doubtful that a developer agreeing to this realises that legally their either committing their company or organisation to these statements as a whole, or they are unable to legally agree to the license meaning that they are using the software against the terms of the license.

This puts a strong burden on the users of the software to work out how much they care about such things, and just what impact it might have.  If you work for a small startup, I doubt anyone cares, but if you work for a large multinational or even worse a government, can you really agree to this?  Unlikely. 


## [Security for package maintainers](https://sethmlarson.dev/blog/security-for-package-maintainers)

[https://sethmlarson.dev/blog/security-for-package-maintainers](https://sethmlarson.dev/blog/security-for-package-maintainers)

> Some time ago I was chatting with a friend about OSS supply chain security. During the conversation I mentioned that I'd prefer having my bank account compromised compared to my GitHub or PyPI accounts.
> 
> Due to the sheer number of downloads urllib3 and other foundational packages receive per day, any compromise would we widespread and devastating.
> 
> It's scary to think about! 😱
> 
> We've taken many precautions both individually and as a team to ensure this scenario is unlikely to occur. I hope that some of the knowledge I've gained along the way can help you secure your own packages as well as inspiring some adversarial security-minded thinking.


A good guide for the sorts of security implications and practices that you need if you are going to be a package maintainer. 

Of course there’s no way to verify or validate whether any given package manager does this. And given the dependencies or dependencies, someone with a simple “left pad” library can end up in the critical chain for millions of software packages


## [Top 10 CI/CD Security Risks ](https://www.cidersecurity.io/top-10-cicd-security-risks/)

[https://www.cidersecurity.io/top-10-cicd-security-risks/](https://www.cidersecurity.io/top-10-cicd-security-risks/)

> These characteristics allow faster, more flexible and diverse software delivery. However, they have also reshaped the attack surface with a multitude of new avenues and opportunities for attackers.
> Adversaries of all levels of sophistication are shifting their attention to CI/CD, realizing CI/CD services provide an efficient path to reaching an organization’s crown jewels. The industry is witnessing a significant rise in the amount, frequency and magnitude of incidents and attack vectors focusing on abusing flaws in the CI/CD ecosystem
> While attackers have adapted their techniques to the new realities of CI/CD, most defenders are still early on in their efforts to find the right ways to detect, understand, and manage the risks associated with these environments. 


I’ve been saying this for a while, but this resource is really well put together and summarises some of the most egregious, damaging and dangerous practices of CI/CD pipelines. 


## [Russian State-Sponsored Cyber Actors Gain Network Access by Exploiting Default Multifactor Authentication Protocols and “PrintNightmare” Vulnerability | CISA](https://www.cisa.gov/uscert/ncas/alerts/aa22-074a)

[https://www.cisa.gov/uscert/ncas/alerts/aa22-074a](https://www.cisa.gov/uscert/ncas/alerts/aa22-074a)

> As early as May 2021, Russian state-sponsored cyber actors took advantage of a misconfigured account set to default MFA protocols at a non-governmental organization (NGO), allowing them to enroll a new device for MFA and access the victim network. The actors then exploited a critical Windows Print Spooler vulnerability, “PrintNightmare” (CVE-2021-34527) to run arbitrary code with system privileges. Russian state-sponsored cyber actors successfully exploited the vulnerability while targeting an NGO using Cisco’s Duo MFA, enabling access to cloud and email accounts for document exfiltration.
> 
> This advisory provides observed tactics, techniques, and procedures, indicators of compromise (IOCs), and recommendations to protect against Russian state-sponsored malicious cyber activity. FBI and CISA urge all organizations to apply the recommendations in the Mitigations section of this advisory, including the following:
> 
> Enforce MFA and review configuration policies to protect against “fail open” and re-enrollment scenarios.
> Ensure inactive accounts are disabled uniformly across the Active Directory and MFA systems. 
> Patch all systems. Prioritize patching for known exploited vulnerabilities.


What happened in this case was that there were old inactive accounts that hadn’t been closed. Sadly due to the way Duo was configured for MFA, it meant that the attackers could simply set it up when they compromised the account, meaning it didn’t protect the org. 

This sounds a lot like a warning about MFA but it’s actually a warning to review your accounts and those people who leave and make sure they are disabled correctly. 


## [SupplyChainSecurityCon - Talk Recordings Now Available - CD Foundation](https://cd.foundation/blog/2021/11/10/supplychainsecuritycon-talk-recordings-now-available/)

[https://cd.foundation/blog/2021/11/10/supplychainsecuritycon-talk-recordings-now-available/](https://cd.foundation/blog/2021/11/10/supplychainsecuritycon-talk-recordings-now-available/)

> SupplyChainSecurityCon 2021 took place October 11 in co-location with KubeCon 2021. It was the most popular co-located event. There were so many great talks
> 
> * Keynote: Project Trebuchet: How SolarWinds is Using Open Source to Secure Their Supply Chain in the Wake of the Sunburst Hack
> * The State of SBOMs
> * Whose Sign Is It Anyway?
> * Supply Chain Security with the Jenkins Templating Engine! 
> * An Overview on SLSA 
> 
> and many more


This is a good playlist of video content.  Great for enjoying over the holidays


## [aws | ClickOops. If you’ve been working in AWS for long… | by Paul Zietsman | cloudandthings.io | Medium](https://medium.com/cloudandthings/aws-clickoops-1b8cabc9b8e3)

[https://medium.com/cloudandthings/aws-clickoops-1b8cabc9b8e3](https://medium.com/cloudandthings/aws-clickoops-1b8cabc9b8e3)

> If you’ve been working in AWS for long enough, you will know that nothing good comes from configuring resources in the console aka ClickOps. That being said, having a hard and fast rule that everybody should only have ReadOnly access in the console is also not great. I wanted something that would trigger when people are taking manual actions in the console and alert the team to investigate why this was done and what needs to be done to get our IaC deployment in sync with these changes.
> For this reason, I’ve created ClickOops, a simple Lambda that monitors your CloudTrail log files to find manual actions taken in your accounts.
> Filtering which events should be classified as a manual action is more involved than you might think. This post by Arkadiy Tetelman goes into detail about what to look for in CloudTrail Events and a sample python implementation can found in Towards Data Science’s blog.


This is a neat way to verify or validate that people aren’t manually updating your accounts and permissions in your cloud console. 


## [Browser In The Browser (BITB) Attack | mr.d0x](https://mrd0x.com/browser-in-the-browser-phishing-attack/)

[https://mrd0x.com/browser-in-the-browser-phishing-attack/](https://mrd0x.com/browser-in-the-browser-phishing-attack/)

> All of this eventually lead me to think, is it possible to make the “Check the URL” advice less reliable? After a week of brainstorming I decided that the answer is yes.
> 
> 
> 
> Pop-Up Login Windows
> 
> Quite often when we authenticate to a website via Google, Microsoft, Apple etc. we’re provided a pop-up window that asks us to authenticate. The image below shows the window that appears when someone attempts to login to Canva using their Google account.
> 
> 
> 
> Replicating The Window
> 
> Fortunately for us, replicating the entire window design using basic HTML/CSS is quite simple. Combine the window design with an iframe pointing to the malicious server hosting the phishing page, and its basically indistinguishable.


This is a scary bit of research. Even as a seasoned software developer, computer user and security professional, I wouldn’t always drag the pop up window outside of the main browser area. 

Not a lot we can do to protect users from this except the use of hardware MFA and password managers which should fail to fill in the login details. 


## [Dual use of artificial-intelligence-powered drug discovery | Nature Machine Intelligence](https://www.nature.com/articles/s42256-022-00465-9)

[https://www.nature.com/articles/s42256-022-00465-9](https://www.nature.com/articles/s42256-022-00465-9)

> The thought had never previously struck us. We were vaguely aware of security concerns around work with pathogens or toxic chemicals, but that did not relate to us; we primarily operate in a virtual setting. Our work is rooted in building machine learning models for therapeutic and toxic targets to better assist in the design of new molecules for drug discovery. We have spent decades using computers and AI to improve human health—not to degrade it. We were naive in thinking about the potential misuse of our trade, as our aim had always been to avoid molecular features that could interfere with the many different classes of proteins essential to human life. Even our projects on Ebola and neurotoxins, which could have sparked thoughts about the potential negative implications of our machine learning models, had not set our alarm bells ringing.


Fascinating and very scary. The use of AI is growing but our ability to think cogently about the negative uses of it is not growing in line with it


## [White House Reaches Out to Social-Media Influencers on Ukraine - Bloomberg](https://www.bloomberg.com/news/articles/2022-03-12/white-house-reaches-out-to-social-media-influencers-on-ukraine)

[https://www.bloomberg.com/news/articles/2022-03-12/white-house-reaches-out-to-social-media-influencers-on-ukraine](https://www.bloomberg.com/news/articles/2022-03-12/white-house-reaches-out-to-social-media-influencers-on-ukraine)

> White House officials including Press Secretary Jen Psaki briefed about 30 social-media influencers on U.S. policy on Ukraine in an effort to counter Russian propaganda, a spokeswoman said.
> 
> The creators, who are active mainly on Bytedance Ltd.’s TikTok, were given an overview of the latest White House thinking on Ukraine during a video call on Thursday, with material similar to that provided in traditional briefing calls to reporters over the last week, the spokeswoman said.


You probably don’t take TikTok or YouTube stars very seriously. But this shows that it’s critical to start thinking of them as new media and methods for disseminating news as well as countering fake news


