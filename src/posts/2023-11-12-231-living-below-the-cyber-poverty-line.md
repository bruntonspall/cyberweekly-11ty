---
title: "231 - Living below the cyber poverty line"
date: 2023-11-12
description: "Microsoft's annual report has an interesting concept in it, that of organisations that live below the cyber poverty line."
permalink: /living-below-the-cyber-poverty-line/
---

Microsoft's annual report has an interesting concept in it, that of organisations that live below the cyber poverty line.

The concept here is that there's a minimum amount of cyber security spend that an organisation must be able to pay, which is needed to just keep your head above the water.  Companies which do not or cannot invest that money will end up running increasing risks and will eventually be overtaken by cyber enabled criminals or state based compromises.

Of course, the world is more complex than this fairly simple description.  Companies generally have to invest in themselves, but they also need to turn a profit and report to investors for every penny that they don't turn into profit.  Investors may or may not care about the information security risks, depending on their reason for investing, and there's not a clear line between poor security and low profitability.

Sure, some types of cyber attack can be incredibly damaging to your bottom line, so being ransomwared and unable to carry out your business operations is clearly going to impact your profits and upset investors.  But if your exchange server is left unpatched and a state affiliated actor steals your emails to feed into their big data machine to develop national economic advantage, would that actually affect your bottom line?  It might if it becomes public and you get a GDPR-inspired fine for loss of data, but in many cases, these kinds of activities may not become public, and the public regulators are appearing overwhelmed with ransomware level data breaches.  Microsoft's report indicates that between July 2022 and June 2023, there was on average around 20-25 breaches per month per 100,000 organizations.  That's a 0.002% incidence rate, and of those, around 70% affected a small company with fewer than 500 employees.

Of course, most of my readers work in cybersecurity in some way or another (aside from those who work in technology with an interest in security), so of course we think that investment in cybersecurity is worth doing, and people I talk to seem to think that companies are willfully inept or incompetent for not doing this stuff.  But companies do recognise (mostly) how important technology spend is to the company profits.

Of course, as I've said many times before, this stuff isn't very easy and it's often not cheap.  Most organisations, even the small ones, don't tend to have single small networks, but have a multitude of IT systems that changed and grew as the company grew, merged and acquired it's way to where it is.  That means that even working out who your administrators are, which individuals have requested special administrative privileges over the years and still hold them, and where MFA technologies can make the most difference.  It also means that for many companies, even attempting to put MFA in place will probably mean also having to buy a single-sign-on solution that they can use to ensure that all systems are appropriately protected.

And none of this comes for free.  Most SaaS tools charge extra for premium accounts that support Single-Sign-On systems, which means not only can your staff not just sign up to SaaS tools as they need them, but now their business case needs to show why it's worth paying so much.  Equally, many security features are not turned on by default, and within Microsoft estate itself, many of the core security features, such as use of Windows Defender or Bitlocker are restricted to Windows professional licenses, rather than the cheaper Windows home, and many security features are only enabled with more expensive E5 licenses.

Of course, these features cost money to implement and are only of interest to companies, so it can make sense that these features aren't enabled on the cheaper consumer end devices and accounts.  They can also add complexity to the setup and use of such devices, so I don't think this is as simple as just enabling all security features at all tiers.

But back to the point, the core question that I think the cyber poverty line gives rise to the real question about how much you spend on security, and where that money actually goes.  The cost of staff, security analysts, advisors and responders doesn't come cheap, but in reality much of the actual security spend in an organisation is actually technology spend.  How much effort and support do you give technology teams to ensure that they are making the right decisions for security?  How much time is spent with procurement teams to ensure that contracts have appropriate security clauses in.  

The answer is to work as a team, security and technology hand in hand to ensure that the underlying technology works for users, and ensure it's not just a cybersecurity poverty line, but a technology poverty line.

## [Microsoft Digital Defense Report 2023 (MDDR) | Microsoft Security Insider ](https://www.microsoft.com/en-us/security/security-insider/microsoft-digital-defense-report-2023)

[https://www.microsoft.com/en-us/security/security-insider/microsoft-digital-defense-report-2023](https://www.microsoft.com/en-us/security/security-insider/microsoft-digital-defense-report-2023)

> **The fundamentals of cyber hygiene**
> 
> **Enable multifactor authentication (MFA)** 
> 
> This protects against compromised user passwords and helps to provide extra resilience for identities. 
> 
> **Apply Zero Trust principles** 
> 
> The cornerstone of any resilience plan is to limit the impact of an attack on an organization: explicitly verify, use least privilege access, and always assume breach. 
> 
> **Use extended detection and response (XDR) and antimalware** 
> 
> Implement software to detect and automatically block attacks and provide insights to the security operations software. Monitoring insights from threat detection systems is essential to being able to respond to threats in a timely fashion. 
> 
> **Keep up to date** 
> 
> Unpatched and out-of-date systems are a key reason many organizations fall victim to an attack. Ensure all systems are kept up to date including firmware, the operating system, and applications. 
> 
> **Protect data** 
> 
> Knowing your important data, where it is located, and whether the right defenses are implemented is crucial to implementing the appropriate protection. 


This is, as always, a great product with a lot of interesting tidbits in it.  But underneath it all, despite the details about the most advanced attacks on Microsofts network and customers, what really shines through is just how much the basics can make a significant difference.  

They set out the concept of a cyber poverty line, organisations that simply cannot afford to invest in the “adequate protection from cyber threats”.  The suggestions below are the combination of the things that they think can have the most protection for the investment required.  It’s worth knowing that Microsoft found that enabling MFA along reduced the risk of comprmise by 99.2 percent.

Seriously, if you have limited budget, invest in multi-factor authentication, invest in least privilege separating admin accounts from user accounts and implement some form of server (and end user device) deterction and response capability.

It’s worth noting that Microsoft already supports and rolls out many of these capabilities, although they’re still often paid for with additional licensing costs.  But of all of your investments, upgrading to Microsoft 365 licenses that support those features should be high up (as is adding pressure that these features should come by default on cheaper licenses) 


## [ThreatHorizonsQ3 2023 Threat Horizons Report ](https://services.google.com/fh/files/blogs/gcat_threathorizons_full_oct2023.pdf)

[https://services.google.com/fh/files/blogs/gcat_threathorizons_full_oct2023.pdf](https://services.google.com/fh/files/blogs/gcat_threathorizons_full_oct2023.pdf)

> Good Cloud Hygiene is Not a One Time Event
> 
> As defenders, the most interesting attacks are the
> advanced ones that make headlines across the
> industry. For example, in 2022, Mandiant wrote about
> a sophisticated attack campaign that leveraged two
> zero-day vulnerabilities, a novel hypervisor malware,
> and a new technique for running malicious software on
> virtual machines.
> 
> However, based on the latest data captured in this
> and previous Threat Horizons Reports, the majority
> of victims in the cloud are not compromised by these
> types of advanced attacks. Rather, cloud intrusions are
> resulting from common and well-known threat actor
> attack techniques, such as obtaining and using stolen
> credentials, and from security weaknesses, such as
> misconfigurations. It may not be as exciting, but by
> focusing on simple cloud security hygiene, defenders
> have an opportunity to dramatically reduce the risk of
> a cloud compromise. 


This report has a wealth of interesting attacks noticed by Google’s threat team, who have access to huge amounts of data in cloud compromise.  Some of the things they are registering, such as attackers compromising the wealth of SaaS apps that are poorly maintained in organisations, or the compromise of over-provisioned security credentials are all interesting trends that should factor into your security strategy 


## [Secure your resources with Conditional Access policy templates - Microsoft Entra | Microsoft Learn ](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/concept-conditional-access-policy-common)

[https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/concept-conditional-access-policy-common](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/concept-conditional-access-policy-common)

> Conditional Access templates provide a convenient method to deploy new policies aligned with Microsoft recommendations. These templates are designed to provide maximum protection aligned with commonly used policies across various customer types and locations. 


These templates are a great way of implementing the basic actions called out in Microsoft’s Digital Defense Report.  You’ll still need to actually implement a multi-factor requirements across your estate, but these templates will ensure that accounts that haven’t enrolled themselves in your MFA solution won’t be able to login to the resources that you specify.

At the very minimum, you should be requiring MFA for admin accounts, requiring MFA for Azure Admin, requiring compliant or Microsoft entra hybrid joined devices for administrators and requiring phishing-resistant multifactor authenticators for your admin staff 


## [SECURITIES AND EXCHANGE COMMISSION, Plaintiff v. SOLARWINDS CORP. and TIMOTHY G. BROWN, ](https://www.sec.gov/files/litigation/complaints/2023/comp-pr2023-227.pdf)

[https://www.sec.gov/files/litigation/complaints/2023/comp-pr2023-227.pdf](https://www.sec.gov/files/litigation/complaints/2023/comp-pr2023-227.pdf)

> The misleading Security Statement concealed from the public the Company’s known poor cybersecurity practices throughout the Relevant Period. These poor cybersecurity practices included SolarWinds’ (a) failure to consistently maintain a secure developmen tlifecycle for software it developed and provided to thousands of customers, (b) failure to enforce the use of strong passwords on all systems, and (c) failure to remedy access control problemst hat persisted for years.
> 
> SolarWinds’ SEC filings similarly concealed the Company’s poor cybersecurity practices. They contained general, high-level risk disclosures that lumped cyberattacks in a list of risks alongside “natural disasters, fire, power loss, telecommunication failures...[and] employee theft or misuse.” The cybersecurity risk disclosure was generic and hypothetical, allowing for negative consequences “[i]f we sustain system failures, cyberattacks against our systems or  against our products, or other data security incidents or breaches.” This disclosure failed to address known risks. For example, it warned of an inability to defend against “unanticipate[d]...techniques” but failed to disclose that SolarWinds had already determined that it was not taking adequate steps to protect against anticipated and known risks, including failing to follow the steps outlined in the Security Statement. These general warnings were then repeated verbatim in each relevant filing, despite both the ongoing problems and the increasing red flags in 2020 that SolarWinds was not only being specifically targeted for a cyberattack, but that the attackers had already gotten in. 


The CISO of SolarWinds being bought up on SEC charges is a really interesting development.   

The majority of the complaint is that the CISO made misleading statements to their investors about how secure their products were.  In fact, internally, they knew that things weren’t up to snuff.  It’s worth stopping there for a second, because the issue here isn’t really that they weren’t good at security, it’s that they told investors that they had a secure software development lifecycle programme, but in fact it wasn’t being done, and they knew it wasn’t being implemented.

One possible thing to learn from this is to not document in great detail about how bad your programme is.  This only came to light because after the compromise, the SEC did an investigation and started reading through internal staff emails and IM’s to find that the reality on the ground wasn’t all rosy.  

But the right thing to learn from this is to be honest about reality with your investors.  This stuff is hard to implement correctly.  Of course, investors aren’t going to have much time for “This is hard and we’re not very good”, but you can craft that narrative better if needed.   It may not be about being any good, but more about whether or not you believe the risks to be appropriately managed.  “We’re not great, but we’re better than 50% of the market” might be sufficient, along with of course “With more investment, we can be in the top 10%”. 


## [Help Everyone Do Better Security ](https://matduggan.com/security-feels-pointless/)

[https://matduggan.com/security-feels-pointless/](https://matduggan.com/security-feels-pointless/)

> On the security side, the expectation seems to be that the base technology will be open-source but any refinement is not. If I find a great tool to manage SSH certificates, I have to pay for it and I can't see how it works. If I rely on a company to handle my login, I can ask for their security audits (sometimes) but the actual nuts and bolts of "how they solved this problem" is obscured from me.
> 
> Instead of "building on the shoulders of giants", it's more like "You've never made a car before. So you make your first car, load it full of passengers, send it down the road until it hits a pothole and detonates." Then someone will wander by and explain how what you did was wrong. People working on their first car to send down the road become scared because they have another example of how to make the car incorrectly, but are not that much closer to a correct one given the nearly endless complexity. They may have many examples of "car" but they don't know if this blueprint is a good car or a bad car (or an old car that was good and is now bad).
> 
> In order to be good at security, one has to see good security first. I can understand in the abstract how SSH certificates should work, but to implement it I would have to go through the work of someone with a deep understanding of the problem to grasp the specifics. I may understand in the abstract how OAuth works, but the low level "how do I get this value/store it correctly/validate it correctly" is different. You can tell me until you are blue in the face how to do logins wrong, but I have very few criteria by which I can tell if I am doing it right.
> 
> To be clear there is no shortage of PDFs and checklists telling me how my security should look at an abstract level. Good developers will look at those checklists, look at their code, squint and say "yeah I think that makes sense". 


Unusually, I’m not necessarily going to recommend that you go and read this one.  It says it’s a 19 minute read, and most of it is repeating this quoted point but with more examples (although there’s some good bits at the end, so scroll down to Login and read to the end to see how much you have to consider to support Login in the modern world).

I completely agree with what Matt says here however.  Security does feel a bit like we’re all having to do the same things over and over.  Some of that is because security is incredibly contextual, what makes for a good security process in one context may not work in another.  But there is also the point that Matt makes here, we’re really good at sharing what bad security looks like, but it’s incredibly difficult to share what good looks like.

Instead we are left approaching the problem as Matt makes out here, by needing smart enough people to understand every nut and bolt of everything that we are building.  That isn’t scalable and can’t be the way that the world has to work in the 21st Century surely! 


## [Why I'm Not Getting a Humane AI Pin ](https://danielmiessler.com/p/im-not-getting-humane-ai-pin)

[https://danielmiessler.com/p/im-not-getting-humane-ai-pin](https://danielmiessler.com/p/im-not-getting-humane-ai-pin)

> Thinking about it for a while this last week I realized it’s because **it confuses multiple different problems.** 
> 
> 1. _Problem 1_ : We should be able to ask for things instead of having to do them ourselves.
> 
> 2. _Problem 2_ : We shouldn’t have to take our phones out of our pockets to do cool phone stuff like display things.
> 
> 3. _Problem 3_ : We shouldn’t have to remember things. AI should just capture everything that happens around us and create summaries and be able to recall things if we need them.
> 
> The Humane AI pin seems to solve Problem 2, but I don’t have Problem 2. I have Problem 1 and Problem 3. 


I like  this summarisation of the problem sets that AI companies are trying to solve, or at least claim to solve.  I’m not convinced that I really have any of those problems, I’m actually pretty happy doing things myself, getting my phone out to change context and remembering stuff. 


## [Teen boys use AI to make fake nudes of classmates, sparking police probe | Ars Technica ](https://arstechnica.com/tech-policy/2023/11/deepfake-nudes-of-high-schoolers-spark-police-probe-in-nj/)

[https://arstechnica.com/tech-policy/2023/11/deepfake-nudes-of-high-schoolers-spark-police-probe-in-nj/](https://arstechnica.com/tech-policy/2023/11/deepfake-nudes-of-high-schoolers-spark-police-probe-in-nj/)

> This October, boys at Westfield High School in New Jersey started acting "weird," the Wall Street Journal [reported](https://www.wsj.com/tech/fake-nudes-of-real-students-cause-an-uproar-at-a-new-jersey-high-school-df10f1bb) . 
> 
> It took four days before the school found out that the boys had been using AI image generators to create and share fake nude photos of female classmates. Now, police are investigating the incident, but they're apparently working in the dark, because they currently have no access to the images to help them trace the source.
> 
> According to an email that the WSJ reviewed from Westfield High School principal Mary Asfendis, the school "believed" that the images had been deleted and were no longer in circulation among students.
> 
> It remains unclear how many students were harmed. A Westfield Public Schools spokesperson cited student confidentiality when declining to tell the WSJ the total number of students involved or how many students, if any, had been disciplined. The school had not confirmed whether faculty had reviewed the images, seemingly only notifying the female students allegedly targeted when they were identified by boys claiming to have seen the images.
> 
> It's also unclear if what the boys did was illegal. There is currently no federal law restricting the creation of faked sexual images of real people 


This sort of thing will sadly get more and more common as AI technologies get better, cheaper and easier to use.  AI companies themselves need to recognise that even if laws don’t strictly prohibit this kind of behaviour, if they don’t self-regulate, right thinking countries will pass laws to prevent this happening. 


## [How to use AI to do practical stuff: A new guide ](https://oneusefulthing.substack.com/p/how-to-use-ai-to-do-practical-stuff)

[https://oneusefulthing.substack.com/p/how-to-use-ai-to-do-practical-stuff](https://oneusefulthing.substack.com/p/how-to-use-ai-to-do-practical-stuff)

> Large Language Models like ChatGPT are extremely powerful, but are built in a way that encourages people to use them in the wrong way. When I talk to people who tried ChatGPT but didn’t find it useful, I tend to hear a similar story.
> 
> The first thing people try to do with AI is what it is worst at; using it like Google: **tell me about my company** , **look up my name** , and so on. These answers are terrible. Many of the models are not connected to the internet, and even the ones that are make up facts. AI is not Google. So people leave disappointed.
> 
> Second, they may try something speculative, using it like Alexa, and asking a question, often about the AI itself. **Will AI take my job? What do you like to eat** ? These answers are also terrible. With one exception, most of the AI systems have no personality, are not programmed to be fun like Alexa, and are not an oracle for the future. So people leave disappointed.
> 
> If people still stick around, they start to ask more interesting questions, either for fun or based on half-remembered college essay prompts: **Write an article on why ducks are the best bird** . **Why is Catcher in the Rye a good novel?** These are better. As a result, people see blocks of text on a topic they don’t care about very much, and it is fine. Or the see text on something they are an expert in, and notice gaps. But it not that useful, or incredibly well-written. They usually quit around now, convinced that everyone is going to use this to cheat at school, but not much else.
> 
> All of these uses are not what AI is actually good at, and how it can be helpful. They can blind you to the real power of these tools. I want to try to show you some of why AI is powerful, in ways both exciting and anxiety-producing. 


This was from back in March, but yet I still think it’s got a good vibe on some of the best ways to actually get hands on with GPT today, and has a good list of things you can use it for that I really like. 


## [Weird A.I. Yankovic, a cursed deep dive into the world of voice cloning - Waxy.org ](https://waxy.org/2023/10/weird-ai-yankovic-voice-cloning/)

[https://waxy.org/2023/10/weird-ai-yankovic-voice-cloning/](https://waxy.org/2023/10/weird-ai-yankovic-voice-cloning/)

> With his channel There I Ruined It, Dallas musician Dustin Ballard built a following of [3.1 million TikTok followers](https://www.tiktok.com/@thereiruinedit) and [700k YouTube subscribers](https://www.youtube.com/@ThereIRuinedIt/videos) making absurdist song remixes and mashups. For the last four months, he’s started experimenting with voice cloning, collaborating with a friend-of-a-friend in South America to change his vocal tracks to sound like other singers.
> 
> The results have been consistently inspired: [The Beach Boys singing Nine Inch Nails’ “Hurt”](https://www.youtube.com/watch?v=gmNSFqyg_Z8) to the tune of “Surfin’ USA,” [Hank Williams doing a twangy “Straight Outta Compton”](https://www.youtube.com/watch?v=2Jh7Jk3aSlo) , and most recently, this ridiculous reworking of [Red Hot Chili Peppers’ “Snow (Hey Oh)” with nonsensical lyrics](https://www.youtube.com/watch?v=VE5JMEu5hZA) .
> 
> Ballard achieves uncanny results by recording entirely new vocal tracks of his own, presumably doing a passable impression of each artist in their vocal range and style, before the A.I. voice cloning is applied.
> 
> This allows him to do things that would otherwise be challenging with today’s current technology: applying A.I. to change the lyrics, melody, meter, or intonation to make something wildly different from the original.
> 
> At least for now, the best way to pull off this Weird A.I. project in a believable way, without every artist sounding vaguely like Weird Al, would be to get someone to sing Weird Al’s lyrics in a similar range and style as the parodied artist, and _then_ apply the A.I. voice cloning. 


Absolutely fascinating deep dive into AI powered voice cloning, along with audio samples.  What I found most interesting here was Dustin’s approach of using AI and Human hybrids.  

The rush for AI hype with the concept that AI’s will replace humans is liable to miss that the most powerful use of AI is working alongside a human who can effectively prompt the AI better.

If you are worrying about autonomous AI agents running amok on your network, then maybe you should instead be worrying about AI augmenting your existing attackers to make them cleverer, quicker and more effective. 


