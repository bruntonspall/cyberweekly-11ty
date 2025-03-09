---
title: "121 - Can we tell the future"
date: 2020-10-11
description: "For those who don't know, I started a new job recently.  Leaving behind my contractor ways, I've returned to the civil service to help build security capabilities across government.  Part of that role includes setting up better situational awareness and horizon scanning for Government, a better ability to know what is happening both inside government and outside, in security and technology."
permalink: /can-we-tell-the-future/
---

For those who don't know, I started a new job recently.  Leaving behind my contractor ways, I've returned to the civil service to help build security capabilities across government.  Part of that role includes setting up better situational awareness and horizon scanning for Government, a better ability to know what is happening both inside government and outside, in security and technology.

One of things that we are aiming to do is to start looking ahead at how the future looks and make predictions on what will happen.  Will people work from home, will there be more ransomware, will zero trust save us?

But humans are incredibly bad at predictions and more generally at probability.  You are far more likely to be injured crossing the street than you are flying in a plane, but yet people are petrified of flying and almost nobody is scared of crossing the road.  This is the result of collections of biases that makes it hard for us to accurately predict risks and dangers around us, and very difficult for us to foretell what is going to happen in the future.

Case in point: https://m.xkcd.com/2370/

 It turns out that people are sucky forecasters, but that actually just a few fairly simple things can make us better at telling the future.  The first is being specific.  We love to dress up our predictions (as you'll have seen me do for the last 121 issues of CyberWeekly) in language that is vague.  "Oh I think that X is likely", or "It's possible that Y might happen".  This vague language tends to hold back our ability to both predict, because we can hide our own uncertainty in there, but also to work with others, because it's hard for us to tell what someone actually means by "it's possible", do they mean 10% of the time, or 40% of the time?

While, as I point out below, Superforecasting has gotten a bad rep, mostly in my experience because of the sort of complete plonker who proudly declares that they are a super forecaster in their twitter bio, the research that Tetlock put in is pretty convincing.  When forecasting, people can be trained to get better at it through replicating some things that these so called superforecasters did intuitively.  Working out how to correctly compare data, analyse and make predictions is one part of the battle, but the biggest is keeping a record, and referring back to it, so that you can revisit and update your forecasts as you get more information.  This looking back at your forecasts with hindsight bias also helps you to learn how to make better forecasts.

Predicting the future is hard, but that's what we often do in digital and security.  We are making bets that a given approach, system or thing will be better than the previous.  We are busy working out how to mitigate risks that may or may not happen, so shouldn't we learn to be more precise and accurate with our forecasts?

## [U-2 Federal Lab Achieves Flight with Kubernetes > Air Combat Command > Article Display](https://www.acc.af.mil/News/Article-Display/Article/2373639/u-2-federal-lab-achieves-flight-with-kubernetes/)

[https://www.acc.af.mil/News/Article-Display/Article/2373639/u-2-federal-lab-achieves-flight-with-kubernetes/](https://www.acc.af.mil/News/Article-Display/Article/2373639/u-2-federal-lab-achieves-flight-with-kubernetes/)

> The U-2 flight brought together the power of four individual, flight-certified computers on board the aircraft, leveraging the advantages of Kubernetes to run advanced machine learning algorithms without any negative effects on the aircraft’s flight or mission systems. “The successful combination of the U-2’s legacy computer system with the modern Kubernetes software was a critical milestone for the development of software containerization on existing Air Force weapon systems,” said Nicolas Chaillan, the Air Force Chief Software Officer.
> 
> “I’m incredibly proud of the U-2 Federal Lab and our Recce Town Airmen that made flying Kubernetes on the U-2 possible,” said Col. Heather Fox, 9th Reconnaissance Wing commander. “This is a milestone achievement that paves the way for rapid experimentation as we continuously work to bring the future faster and increase battlespace awareness for our Airmen. The integration of Kubernetes onto the U-2 capitalizes on the aircraft’s high altitude line of sight and makes it even more survivable in a contested environment.  We look forward to working with other platforms across the DoD to export this incredible capability.”


This took me several times to read and work out what they had done.  I don't think this is the case that they are running the airplane operations systems on Kubernetes itself, rather than they've been able to form a Kubernetes cluster out of machines on board the aircraft, without disrupting the other flight critical operations of the planes network itself.

Of course, Kubernetes just lets you run containers and systems in a node arbitrary way, but in this case, it means that the computing platform can be used to run and power almost any code in flight.  That's both cool and exciting for people developing software to work on military systems, and terrifying from a security and resilience basis.  If you get a security exploit in Kubernetes on this system, just what can the container do to the wider system?


## [Ryuk’s Return – The DFIR Report](https://thedfirreport.com/2020/10/08/ryuks-return/)

[https://thedfirreport.com/2020/10/08/ryuks-return/](https://thedfirreport.com/2020/10/08/ryuks-return/)

> In this case, the actions began via a loader malware known as Bazar/Kegtap. Reports indicate an email delivery via malspam, which has been creeping up in volume over the month of September.
> 
> From the initial execution of the payload, Bazar injects into various processes including explorer.exe and svchost.exe, as well as, spawning cmd.exe processes. The initial goal of this activity was to run discovery using built in Windows utilities like nltest, net group, and the 3rd party utility AdFind.
> 
> After the initial discovery activity the Bazar malware stayed relatively quiet, until a second round of discovery the following day. Again, the same tools were employed in the second round of discovery, plus Rubeus. This time the discovery collection was exfiltrated via FTP to a server hosted in Russia. Next, the threat actor began to move laterally.
> 
> It took a few attempts, using various methods, from remote WMI, to remote service execution with PowerShell, until finally landing on Cobalt Strike beacon executable files transferred over SMB to move around the environment. From here forward, the threat actors relied on a Cobalt Strike beacon running on a domain controller as their main operations point.
> 
> 


This is a great report into how at least one threat actor is deploying Ryuk ransomware into environments.

What's disappointing here is just how common tools are being used.  This isn't advanced "living off the land", the threat actor is downloading pretty plain known malware, that your systems should be able to detect and defend against.


## [We Hacked Apple for 3 Months: Here’s What We Found](https://samcurry.net/hacking-apple/)

[https://samcurry.net/hacking-apple/](https://samcurry.net/hacking-apple/)

> During our engagement, we found a variety of vulnerabilities in core portions of their infrastructure that would've allowed an attacker to fully compromise both customer and employee applications, launch a worm capable of automatically taking over a victim's iCloud account, retrieve source code for internal Apple projects, fully compromise an industrial control warehouse software used by Apple, and take over the sessions of Apple employees with the capability of accessing management tools and sensitive resources.
> 
> There were a total of 55 vulnerabilities discovered with 11 critical severity, 29 high severity, 13 medium severity, and 2 low severity reports. These severities were assessed by us for summarization purposes and are dependent on a mix of CVSS and our understanding of the business related impact.
> 
> As of October 6th, 2020, the vast majority of these findings have been fixed and credited. They were typically remediated within 1-2 business days (with some being fixed in as little as 4-6 hours).


You might have seen some news about this because Vice security reported that the vulnerability researchers only got $55,000 for all of these.  This was later noted as "so far", with a further $288,500 paid since and that's for a little over half the vulnerabilities.

This is an amazing bit of work, and there's some good description in here about how they organised themselves, scanned the infrastructure and then methodically worked through the targets.


## [USB3: why it's a bit harder than USB2 - kate's lab notebook](https://lab.ktemkin.com/post/why-is-usb3-harder/)

[https://lab.ktemkin.com/post/why-is-usb3-harder/](https://lab.ktemkin.com/post/why-is-usb3-harder/)

> A few people on twitter have asked me to explain why the USB3 winds up being much harder to implement than USB2. The answer is more than will fit in a single tweet, so I thought I'd put a quick-but-rough answer, here. This is by no means comprehensive; consider it a longer tweet what a tweet would be given I had more than 240 characters and a proclivity to babble. (I do.)
> 
> A lot of the challenges come from the way we work around physical-layer limitations. Put poetically, physics gives us lots of little obstacles we have to work around in order to talk at 5 billion transfers per second (5GT/s).


This is an extremely nerdy view of the way that USB is implemented.  It's often interesting to me how much we rely on abstractions, and how much of a security boundary those abstractions create.  

Where our abstractions are leaky, where the details mingle into the way that you use the system, that's when it's possible to break the assumptions built into the underlying system and create situations that shouldn't happen.


## [Microsoft makes remote work option permanent - BBC News](https://www.bbc.co.uk/news/business-54482245)

[https://www.bbc.co.uk/news/business-54482245](https://www.bbc.co.uk/news/business-54482245)

> As of April, more than 46% of those employed were doing some work from home, according to the Office of National Statistics.
> 
> That was comparable to the US, where 42% of the workforce was remote in May, according to Stanford University economics professor Nicholas Bloom, whose research looked at people aged 20-64, earning more than $10,000 last year.
> 
> While that share decreased to about 35% in August, it still marked a major change. Before the pandemic, just 2% of workers were remote full time, he said.
> 
> "What we're doing now is extremely unusual," he said.
> 
> 


I think this is a bad comparison, 46% of people doing "some work from home" is not comparable with 2% "remote full time".  Sadly I suspect that there aren't very many sources of statistics that can easily be compared.

However this is a shift of things to come, remote working, at least part time, is here to stay for the foreseeable future.  Given that employment laws require companies to make reasonable adjustments, I cannot see how employees won't use this as examples of how it's possible to work from home in the future.  

Expect a good proportion of workforces to be remote in the future, and the excitement that comes from that, how do you do IT support at home long term, what countries can your employees work from? How much money and effort do you put into home desks, computers, screens, keyboards and so on.


## [Cyber Command has sought to disrupt the world’s largest botnet, hoping to reduce its potential impact on the election - The Washington Post](https://www.washingtonpost.com/national-security/cyber-command-trickbot-disrupt/2020/10/09/19587aae-0a32-11eb-a166-dc429b380d10_story.html)

[https://www.washingtonpost.com/national-security/cyber-command-trickbot-disrupt/2020/10/09/19587aae-0a32-11eb-a166-dc429b380d10_story.html](https://www.washingtonpost.com/national-security/cyber-command-trickbot-disrupt/2020/10/09/19587aae-0a32-11eb-a166-dc429b380d10_story.html)

> Brian Krebs, who writes the blog KrebsonSecurity, first reported on the existence of the operation. Cyber Command’s role was previously unreported. The command declined to comment.
> 
> Department of Homeland Security Officials fear that a ransomware attack on state or local voter registration offices and related systems could disrupt preparations for Nov. 3 or cause confusion or long lines on Election Day. They also note that ransomware is a major threat beyond elections.
> 
> Trickbot was used last month in a damaging attack against a major health-care provider, Universal Health Services, whose systems were locked up by the ransomware known as Ryuk. The attack forced personnel to resort to manual systems and paper records, according to reports. UHS runs more than 400 facilities across the United States and Britain. Some patients reportedly were rerouted to other emergency rooms and experienced delays in getting test results.


This feels like an interesting target given that ransomware is more commonly linked to criminal actors rather than state actors, but maybe that's what makes it easier to talk about and target.

Using cyber offensive capabilities to reduce the effectiveness of crime groups feels like a testing ground, something that is reasonably safe from any form of retribution, and an opportunity to determine how effective it is.


## [Proton’s statement on the BGP hijacking incident this week](https://protonmail.com/blog/bgp-hijacking-september-2020/)

[https://protonmail.com/blog/bgp-hijacking-september-2020/](https://protonmail.com/blog/bgp-hijacking-september-2020/)

> At Proton, we strive to plan for all contingencies that might affect our service. Our efforts paid off on Tuesday, September 29 (around 4 AM Wednesday morning, Australia time), allowing us to turn a very serious incident into a minor inconvenience for some of our users.
> 
> As far as we currently understand the situation, this was done on accident and not maliciously, although we have still not been provided with any additional details. For several hours, however, around 30% of the global internet looking for us got pointed to Telstra instead. Some 1,680 other networks were also affected, making this perhaps the most serious BGP hijacking incident ever.
> 
> As we will explain in this article, although there are ways to mitigate the fallout from BGP hijacking, due to the way the internet is designed there is simply no way to prevent this kind of incident from happening. The episode highlights, in fact, how broken some key aspects of the internet are.


BGP hijacking is probably one of the scariest attacks out there.  It's fairly easy to achieve, with almost minimal resources needed, and while it's generally quite noisy (by design, BGP is broadcast), a skilled actor with access to major telecoms or internet providers could well hide fairly subtle attacks in the noise.

There are some internet standards looking to secure BGP increasingly, but many of them are still looking a few years away from being decisively adopted by everyone


## [Words of Estimative Probability — Central Intelligence Agency](https://www.cia.gov/library/center-for-the-study-of-intelligence/csi-publications/books-and-monographs/sherman-kent-and-the-board-of-national-estimates-collected-essays/6words.html)

[https://www.cia.gov/library/center-for-the-study-of-intelligence/csi-publications/books-and-monographs/sherman-kent-and-the-board-of-national-estimates-collected-essays/6words.html](https://www.cia.gov/library/center-for-the-study-of-intelligence/csi-publications/books-and-monographs/sherman-kent-and-the-board-of-national-estimates-collected-essays/6words.html)

> The process of producing NIEs then was almost identical to what it is today. This means that a draft had been prepared in the Office of National Estimates on the basis of written contributions from the IAC(4) agencies, that a score or so of Soviet, Satellite, and Yugoslav experts from the intelligence community labored over it, and that an all but final text presided over by the Board of National Estimates had gone to the Intelligence Advisory Committee. There the IAC members, with the DCI in the chair, gave it its final review, revision, and approval.
> 
> As is quite obvious from the sentence quoted above, Soviet and Satellite intentions with respect to Yugoslavia were a matter of grave concern in the high policy echelons of our government. The State Department's Policy Planning Staff was probably the most important group seized of the problem. Its chairman and members read NIE 29-51 with the sort of concentration intelligence producers can only hope their product will command.
> 
> A few days after the estimate appeared, I was in informal conversation with the Policy Planning Staff's chairman. We spoke of Yugoslavia and the estimate. Suddenly he said, "By the way, what did you people mean by the expression `serious possibility'? What kind of odds did you have in mind?" I told him that my personal estimate was on the dark side, namely, that the odds were around 65 to 35 in favor of an attack. He was somewhat jolted by this; he and his colleagues had read "serious possibility" to mean odds very considerably lower. Understandably troubled by this want of communication, I began asking my own colleagues on the Board of National Estimates what odds they had had in mind when they agreed to that wording. It was another jolt to find that each Board member had had somewhat different odds in mind and the low man was thinking of about 20 to 80, the high of 80 to 20. The rest ranged in between.


This essay, written in 1964, still summarises the problem of probalistic language.  Just what do you mean by "highly likely", or "probably will".

Of course, Intelligence Assessment has had this problem for a long time, and these days there are defined "Words of Estimative Probability", or in the UK, the Probability Yardstick, but the reality is that our estimates are still often lacking in precision in terms of numbers, timelines and impact and effect.


## [Developing expert political judgment: The impact of training and practice on judgmental accuracy in geopolitical forecasting tournaments](http://journal.sjdm.org/16/16511/jdm16511.html)

[http://journal.sjdm.org/16/16511/jdm16511.html](http://journal.sjdm.org/16/16511/jdm16511.html)

> This article tests the power of a cognitive-debiasing training module (“CHAMPS KNOW”) to improve probability judgments in a four-year series of geopolitical forecasting tournaments sponsored by the U.S. intelligence community. Although the training lasted less than one hour, it consistently improved accuracy (Brier scores) by 6 to 11% over the control condition. Cognitive ability and practice also made largely independent contributions to predictive accuracy. Given the brevity of the training tutorials and the heterogeneity of the problems posed, the observed effects are likely to be lower-bound estimates of what could be achieved by more intensive interventions.


If you want the detailed work behind the training used to improve forecasting ability, it's this CHAMPS KNOW system, loosely defined as:

* C	Comparison classes
* H	Hunt for the right information
* A	Adjust and update forecasts when appropriate
* M	Mathematical and statistical models
* P	Post-mortem analysis
* S	Select the right questions to answer
* K	Know the power players and their preferences
* N	Norms and protocols of institutions
* O	Other perspectives should inform forecasts
* W	Wildcards, accidents, and black swans

Learning to apply these principles in a 1 hour training session left CIA trained analysts better at forecasting than those without it.


## [Superforecasting: How to Upgrade Your Company’s Judgment](https://hbr.org/2016/05/superforecasting-how-to-upgrade-your-companys-judgment)

[https://hbr.org/2016/05/superforecasting-how-to-upgrade-your-companys-judgment](https://hbr.org/2016/05/superforecasting-how-to-upgrade-your-companys-judgment)

> Most predictions made in companies, whether they concern project budgets, sales forecasts, or the performance of potential hires or acquisitions, are not the result of cold calculus. They are colored by the forecaster’s understanding of basic statistical arguments, susceptibility to cognitive biases, desire to influence others’ thinking, and concerns about reputation. Indeed, predictions are often intentionally vague to maximize wiggle room should they prove wrong. The good news is that training in reasoning and debiasing can reliably strengthen a firm’s forecasting competence. The Good Judgment Project demonstrated that as little as one hour of training improved forecasting accuracy by about 14% over the course of a year.
> Learn the basics.
> Basic reasoning errors (such as believing that a coin that has landed heads three times in a row is likelier to land tails on the next flip) take a toll on prediction accuracy. So it’s essential that companies lay a foundation of forecasting basics: The GJP’s training in probability concepts such as regression to the mean and Bayesian revision (updating a probability estimate in light of new data), for example, boosted participants’ accuracy measurably. Companies should also require that forecasts include a precise definition of what is to be predicted (say, the chance that a potential hire will meet her sales targets) and the time frame involved (one year, for example). The prediction itself must be expressed as a numeric probability so that it can be precisely scored for accuracy later.


While there is a lot of bunk around based on the Superforecaster concept, the underlying principle is one that if you give people good training and the right tools, they can learn to make better forecasts, and indeed be significantly better than people with access to far wider data but poor processes and tools.

This classic article from HBR back in 2016 was part of the growth of SuperForecasting and building an understanding of how to use it.


## [Tutorials — Simple Risk Measurement documentation](https://magoo.github.io/simple-risk/introduction/tutorials.html)

[https://magoo.github.io/simple-risk/introduction/tutorials.html](https://magoo.github.io/simple-risk/introduction/tutorials.html)

> The following tutorials are quantitative risk methods with the least amount of rigor.
> 
> All risk measurement must start somewhere, and this tutorial represents the earliest examples of scenario measurement. (See Scenarios)
> 
> These example scenarios and their forecasts are similar to using your shoe to measure “one foot”. Low rigor measurements are still useful for day to day, “back of envelope” risk modeling with low cost and effort. They can easily be expanded upon as requirements demand more rigor. (See Rigor)


This work by Ryan Mcgeehan really pulls together the mechanisms from forecasting along with traditional risk management and gives us a new, and significantly better way of predicting risks.

If you go through the tutorial, most of the issues that one would come up with are fairly well laid out, and brings us to a far more extensive and capable risk analysis and assessment process, as well as a mechanism for determining the efficacy of risk controls.


