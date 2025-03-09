---
title: "133 - The lies our brains tell us"
date: 2021-01-24
description: "It remains to be seen what will happen to QAnon now that Biden is president and many of the “facts” and predictions remain totally unfounded. "
permalink: /the-lies-our-brains-tell-us/
---

It remains to be seen what will happen to QAnon now that Biden is president and many of the “facts” and predictions remain totally unfounded. 

But we’ve seen this before.  The scary part of conspiracy theories is that once someone buys into them, they start to create explanations for why the world doesn’t match their beliefs.  This is the literal origination of “Cognative Dissonance”, where people can hold completely competing facts in their head at the same time, such as believing in a provably false theory.  Our brains are mostly marvellous self-healing devices that can and will adjust how we interpret and see reality in order to fit with how it wants to work.

Of course, this steps beyond our individual brains and starts to step into the way that we as societies function.  The way that we advertise, communicate and pass knowledge around means that we as a society act similar to the way that cells make up a larger organism.

Quite how we as global society deal with such things remains to be seen however.

In other news, I’m beginning to wonder if 2021 is going to need an entire section for Solarwinds attackers revelations (I wish we had a good name for them).  We are going to see this unfold for a few more months at least.

## [As Adobe Flash stops running, so do some railroads in China ｜ Apple Daily](https://hk.appledaily.com/news/20210117/FLXATT4LKVBGVEBRLAECJPTCHM/)

[https://hk.appledaily.com/news/20210117/FLXATT4LKVBGVEBRLAECJPTCHM/](https://hk.appledaily.com/news/20210117/FLXATT4LKVBGVEBRLAECJPTCHM/)

> Tuesday’s chaos arose after China Railway Shenyang failed to deactivate Flash in time, leading to a complete shutdown of its railroads in Dalian, Liaoning province. Staffers were reportedly unable to view train operation diagrams, formulate train sequencing schedules and arrange shunting plans.
> 
> Authorities fixed the issue by installing a pirated version of Flash at 4:30 a.m. the following day.


I mean this has everything. Unlatched old software, critical national infrastructure and pirated software. 
(Via Reid)


## [Deep dive into the Solorigate second-stage activation: From SUNBURST to TEARDROP and Raindrop - Microsoft Security](https://www.microsoft.com/security/blog/2021/01/20/deep-dive-into-the-solorigate-second-stage-activation-from-sunburst-to-teardrop-and-raindrop/)

[https://www.microsoft.com/security/blog/2021/01/20/deep-dive-into-the-solorigate-second-stage-activation-from-sunburst-to-teardrop-and-raindrop/](https://www.microsoft.com/security/blog/2021/01/20/deep-dive-into-the-solorigate-second-stage-activation-from-sunburst-to-teardrop-and-raindrop/)

> More than a month into the discovery of Solorigate, investigations continue to unearth new details that prove it is one of the most sophisticated and protracted intrusion attacks of the decade. Our continued analysis of threat data shows that the attackers behind Solorigate are skilled campaign operators who carefully planned and executed the attack, remaining elusive while maintaining persistence. These attackers appear to be knowledgeable about operations security and performing malicious activity with minimal footprint. In this blog, we’ll share new information to help better understand how the attack transpired. Our goal is to continue empowering the defender community by helping to increase their ability to hunt for the earliest artifacts of compromise and protect their networks from this threat.


What a deep dive into the Solarwinds attackers and their attack set.  This has got a lot of detail about the TTP’s post exploitation, and since this is a highly advanced group, if you can actively hunt for and detect this sort of capability on a regular basis, then your defence team is doing well.


## [Malwarebytes targeted by Nation State Actor implicated in SolarWinds breach. Evidence suggests abuse of privileged access to Microsoft Office 365 and Azure environments - Malwarebytes Labs | Malwarebytes Labs](https://blog.malwarebytes.com/malwarebytes-news/2021/01/malwarebytes-targeted-by-nation-state-actor-implicated-in-solarwinds-breach-evidence-suggests-abuse-of-privileged-access-to-microsoft-office-365-and-azure-environments/)

[https://blog.malwarebytes.com/malwarebytes-news/2021/01/malwarebytes-targeted-by-nation-state-actor-implicated-in-solarwinds-breach-evidence-suggests-abuse-of-privileged-access-to-microsoft-office-365-and-azure-environments/](https://blog.malwarebytes.com/malwarebytes-news/2021/01/malwarebytes-targeted-by-nation-state-actor-implicated-in-solarwinds-breach-evidence-suggests-abuse-of-privileged-access-to-microsoft-office-365-and-azure-environments/)

> While Malwarebytes does not use SolarWinds, we, like many other companies were recently targeted by the same threat actor. We can confirm the existence of another intrusion vector that works by abusing applications with privileged access to Microsoft Office 365 and Azure environments. After an extensive investigation, we determined the attacker only gained access to a limited subset of internal company emails. We found no evidence of unauthorized access or compromise in any of our internal on-premises and production environments.


That’s another security company that was targeted by the Solarwinds attackers.  If you are a major security company, you should be conducting a thorough investigation, as there is clear intent by these attackers to get access to those systems.


## [Raindrop: New Malware Discovered in SolarWinds Investigation | Symantec Blogs](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/solarwinds-raindrop-malware)

[https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/solarwinds-raindrop-malware](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/solarwinds-raindrop-malware)

> Symantec, a division of Broadcom (NASDAQ: AVGO), has uncovered an additional piece of malware used in the SolarWinds attacks which was used against a select number of victims that were of interest to the attackers.
> 
> Raindrop (Backdoor.Raindrop) is a loader which delivers a payload of Cobalt Strike. Raindrop is very similar to the already documented Teardrop tool, but there are some key differences between the two. While Teardrop was delivered by the initial Sunburst backdoor (Backdoor.Sunburst), Raindrop appears to have been used for spreading across the victim’s network. Symantec has seen no evidence to date of Raindrop being delivered directly by Sunburst. Instead, it appears elsewhere on networks where at least one computer has already been compromised by Sunburst.


More info on a different payload that the SolarWinds attackers have been spotted using.  If you find that your Orion instance has been compromised, it might not be as simple as looking for a single stage 2 hash.  It looks like the attackers have a varied toolset that they can use on different targets.


## [Urgent Security Notice: NetExtender VPN Client 10.x, SMA 100 Series Vulnerability [Updated Jan. 23, 2021] | SonicWall](https://www.sonicwall.com/support/product-notification/urgent-security-notice-netextender-vpn-client-10-x-sma-100-series-vulnerability-updated-jan-23-2021/210122173415410/)

[https://www.sonicwall.com/support/product-notification/urgent-security-notice-netextender-vpn-client-10-x-sma-100-series-vulnerability-updated-jan-23-2021/210122173415410/](https://www.sonicwall.com/support/product-notification/urgent-security-notice-netextender-vpn-client-10-x-sma-100-series-vulnerability-updated-jan-23-2021/210122173415410/)

> Recently, SonicWall identified a coordinated attack on its internal systems by highly sophisticated threat actors exploiting probable zero-day vulnerabilities on certain SonicWall secure remote access products.


The sonicwall team have been working over the weekend to identify and work out what the vulnerabilities are, but this looks like a changing situation.  

I’ll add that the original suggestion was that you whitelist IP addresses of your remote clients.  For a simple site-to-site VPN that might work fine, but for organisations using VPN’s to enable remote workers across the globe or even across a single country are going to really struggle to whitelist even slightly sensibly.  


## [Questionable Advice: “How do I feel worthwhile as a manager when my people are doing all the implementing?” – charity.wtf](https://charity.wtf/2021/01/23/questionable-advice-how-do-i-feel-worthwhile-as-a-manager-when-my-people-are-doing-all-the-implementing/)

[https://charity.wtf/2021/01/23/questionable-advice-how-do-i-feel-worthwhile-as-a-manager-when-my-people-are-doing-all-the-implementing/](https://charity.wtf/2021/01/23/questionable-advice-how-do-i-feel-worthwhile-as-a-manager-when-my-people-are-doing-all-the-implementing/)

> First, let’s be clear: job satisfaction as a manager, should you find it, will feel very different than it did as an engineer. As an engineer, you get that very tactile sense of merging code, solving puzzles and incrementally pushing the business forward. It has a rhythm and a powerful drip, drip, drip of dopamine, and as a manager you will never ever feel that. Sorry! Some people eventually make peace with this, but many never do. No shame in that.
> 
> This is partly a function of time and proximity. Manager successes and failures play out over a much longer period of time than the successes and failures of writing and debugging code, and you can only indirectly trace your impact. It can be hard to draw a straight line from cause to effect. Some of your greatest successes may resonate and compound for years to come, yet the person might not remember, may never even have known how you contributed to their triumph. (Hell, you might not either.)


I’m a big fan of Charity’s writing most of the time and this hit home for exactly how I felt when I first moved into management.  I had longed to move into technical architecture and later management because I saw how much of an impact that you can have when you move further upstream.  When you are influencing the conversations that form the ideas before they become projects and deliverables, you can make far bigger changes.  What I hadn’t twigged or expected is that it meant that almost all of my power became “soft power”, and had ramifications in the ways that projects would be defined months down the line.  

If you want to move from a role where you have a direct impact on day to day work, then senior management can feel far far less rewarding.  Instead you need to accept that your changes and rewards come from other areas, from seeing the ideas and visions of people around you change and seeing group success.


## [Make High Impact Decisions with Confidence using Alignment Records](https://engineering.procore.com/make-high-impact-decisions-with-confidence-using-alignment-records/)

[https://engineering.procore.com/make-high-impact-decisions-with-confidence-using-alignment-records/](https://engineering.procore.com/make-high-impact-decisions-with-confidence-using-alignment-records/)

> Imagine you need to set the future technical direction of a large Engineering organization. How do you capture the input from all of your Architect Engineers and Engineering Directors and quickly transform it into a visual format that would increase confidence in technical decisions? At Procore, we evolved the Fist of Five Protocol consensus polling technique into an Alignment Record that produces a visual consensus heatmap.
> 
> What is an Alignment Record?
> 
> An alignment record is a polling tool that captures degrees of alignment or agreement on key topics across stakeholders. The results look like a heatmap of the group’s sentiment using red, yellow and green. We devised this tool when facilitating alignment between dozens of architects and engineering directors reviewing our architecture vision.


This is a really nice alignment detector.  Further down it re-emphasises that this isn't about seeking consensus or voting on a decision.  This is about understanding whether your leaders agree with your decisions.  That's not to say that you shouldn't do them, but more to say that if the people being asked to implement them don't feel like they support it, then maybe your decision needs more explaining, or rethinking or reframing.


## [Apple nixes feature that let its apps skip VPNs and firewalls, after criticism from researchers | SC Media](https://www.scmagazine.com/home/security-news/network-security/apple-nixes-feature-that-let-its-apps-skip-vpns-and-firewalls-after-criticism-from-researchers/)

[https://www.scmagazine.com/home/security-news/network-security/apple-nixes-feature-that-let-its-apps-skip-vpns-and-firewalls-after-criticism-from-researchers/](https://www.scmagazine.com/home/security-news/network-security/apple-nixes-feature-that-let-its-apps-skip-vpns-and-firewalls-after-criticism-from-researchers/)

> The second beta version of MacOS 11.2 will no longer allow Apple software to circumvent socket firewalls and virtual private networks.
> 
> “ContentFilterExclusionList,” first noticed by Mac security researchers in October, allowed around 50 Apple-brand programs to access the internet without going through the network extension framework that allowed several security products to work. The software essentially exempted Apple’s own programs from being routed through its Network Extension Framework, which the company created to ensure security products (such as firewalls) could comprehensively monitor and filter network traffic in lieu of third-party kernel extensions. 
> 
> 


Good news here.  There’s no good reason for apple to have done this originally


## [Far-right extremists take over UK land sales Facebook page | Facebook | The Guardian](https://www.theguardian.com/technology/2021/jan/20/far-right-extremists-take-over-uk-land-sales-facebook-page)

[https://www.theguardian.com/technology/2021/jan/20/far-right-extremists-take-over-uk-land-sales-facebook-page](https://www.theguardian.com/technology/2021/jan/20/far-right-extremists-take-over-uk-land-sales-facebook-page)

> But on Thursday morning, Land for Sale UK ceased to exist. Its new administrators had changed its branding and name to better reflect the group they wanted to run: it is now called “Supporters of free speech against Big Tech Fascism.” The main image, once a bucolic pastoral landscape, is now a poorly cropped photo of a statue of Cicero with a quote falsely attributed to the Roman orator by gun rights advocates in which he defends “any and every method of protecting ourselves”.
> 
> And the group’s “about” page has been changed to explain the new position of the group: “Banning people for for [sic] telling the truth or you don’t like their opinion or politics is wrong. If your a Libtard you dont belong here. Good bye.”


This has long been a common trick for marketeers.  Why build a following for your brand if you can buy a ready made community, and all of the lovely historical clicks, likes and interactions that gives you more impact and valid history for your brand.

The fact that the major providers like Facebook don’t solve this is because its profitable for them to continue supporting these mechanisms when they are used “ethically and correctly”.  However this shows how existing advertising, marketing and other reach systems allows for misuse by adversaries we don’t like


## [The Making of QAnon: A Crowdsourced Conspiracy - bellingcat](https://www.bellingcat.com/news/americas/2021/01/07/the-making-of-qanon-a-crowdsourced-conspiracy/?fbclid=IwAR0NptqOuuGe599GtgDGYoKSpX2Pfqn5yxC41nM2jKja-B7oLdFXCdq0UaI)

[https://www.bellingcat.com/news/americas/2021/01/07/the-making-of-qanon-a-crowdsourced-conspiracy/?fbclid=IwAR0NptqOuuGe599GtgDGYoKSpX2Pfqn5yxC41nM2jKja-B7oLdFXCdq0UaI](https://www.bellingcat.com/news/americas/2021/01/07/the-making-of-qanon-a-crowdsourced-conspiracy/?fbclid=IwAR0NptqOuuGe599GtgDGYoKSpX2Pfqn5yxC41nM2jKja-B7oLdFXCdq0UaI)

> Most accounts of QAnon present this first “Q drop”, as Q’s posts are known by their acolytes, as the starting point of the Q movement. This is mistaken for two reasons. One is trivial: Q first gained an audience with a different set of drops, because their earliest efforts sank without a trace and weren’t rediscovered by anyone on 4chan until November 11 that same year. The other is deeply significant: Q’s origins can’t be divorced from the culture of /pol/, which was a rich slurry of racism, anti-Semitism, and (especially relevant here) right-wing conspiracy theories.
> 
> Therefore, QAnon was both an outgrowth and an evolution of /pol/ culture: not only were many of Q’s claims already popular on /pol/, but Q borrowed key themes and ideas from predecessors. The key to understanding the roots of Q is to understand the culture of /pol/.
> 
> But first, we need to understand the myth.
> 
> Meet the Mythos
> Here is the core of the QAnon myth: with the aid of a small group of military intelligence officers called the Q team (one or more of whom is supposedly responsible for writing the drops), President Donald Trump is waging a shadow war against a cabal of Satan-worshipping, child-eating pedophiles who are conspiring to obstruct and overthrow him. The military will arrest them en masse in an event called “the Storm.” The cabal’s membership has grown in the telling (at first, it was “many in our government;” within a month, any “celebs” who had “supported HRC” might very well be in on it; a few months later, there were too many to fit into Guantanamo Bay; later still, three other “detention centers [were] being prepped”), but it would be fair to say that virtually anyone who’s angered or defied President Trump is considered part of the cabal, along with the usual suspects like financier and philanthropist George Soros.
> 
> After the Storm, military tribunals will ensure that these baby-eating traitors are executed or sentenced to life in prison. Faced with overwhelming proof of the cabal’s existence, a stunned public will mourn; rage; and ultimately unite behind President Trump, ushering in a golden age of patriotism and prosperity.
> 
> Remarkably, this description covers none of the most bizarre corners of QAnon (for instance, in QAnon lore, North Korea was controlled by the CIA but has now been liberated by Trump and the Q team). It also omits a key aspect of the QAnon worldview: that every public act or utterance of President Trump or a suspected cabal member might contain “comms,” or secret messages, which QAnon believers can decode. And it leaves out one of the most important QAnon slogans: “disinformation is necessary,” which some might call a wonderful excuse for Q’s failed predictions, also allowing believers to pick and choose which parts of the theory they embrace.


This is an amazing backgrounder on the QAnon conspiracy theory.  It all sounds so hair-brained when written down like this, but the stat in here, that potentially between 5 and 10% of Americans believe some or all of the theory suggestions that at 300 million people, there are somewhere between 15 and 30 million followers of this.  That takes it from a fringe conspiracy into ... well something scary to say the least.


