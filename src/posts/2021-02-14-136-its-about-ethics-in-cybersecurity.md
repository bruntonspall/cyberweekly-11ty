---
title: "136 - It’s about ethics in cybersecurity"
date: 2021-02-14
description: "How should we respond to unethical actions in cybersecurity, and where is the line anyway?"
permalink: /its-about-ethics-in-cybersecurity/
---

How should we respond to unethical actions in cybersecurity, and where is the line anyway?

Sometimes those of us with a relatively clean past (I dabbled in reading Phrack, 2600 as a teenager, but never really crossed any legal lines) can make out that criminal or blackhat behaviour is a black mark that wont ever go away.  

Equally, those who were “part of the scene” can sometimes act like those who didn’t hack for real will never really understand security properly.

The line between the two is far blurrier and greyer than we’d like to admit, with many of our “security heroes” having darker backgrounds than we’d like.

Even more so, we need to know what ethical behaviour looks like in cybersecurity research.  If you think you’ve found a vulnerability, but the company wont take you seriously, how can you demonstrate how bad it is without exploiting it and without doing any damage?  You’d think, and hope, that companies have sensible, tech aware people responding to vulnerability reports who understand the impact of the vulnerability and can treat them seriously, but the reality is that most of the reports I’ve seen come in are from generic scanners which makes reading them dull and uninteresting, and not a great use of your best talent.  That means you need a process and a system, and the first person in it is unlikely to see the importance of the issue at first.

But even more than that, how do we deal with the ethical dilemma of organisations that choose not to play fairly?  I’ve covered before that Google’s Project Zero has a really harsh disclosure timeline and they really don’t like to extend it, meaning that you need to be able to fix your issue within the timeline.  But researchers who don’t have that weight behind them can find it harder when they are fobbed off and delayed by the company.  And it gets worse if the company accuses them of extortion, provides legal threats and otherwise acts belligerently to the researcher.  We’ve seen it before and we’ll see it again I’m sure.

But does that mean that future security researchers should simply ignore the [“correct” responsible disclosure process](https://webstore.ansi.org/Standards/ISO/ISOIEC291472018), or does it mean that the company should be given additional chances by researchers?

Finally, is it fine to act as a vulnerability researcher, finding holes in open source software, without providing the support needed to help fix that software?  We wouldn’t expect it for commercial software, but volunteer run software might need some thinking about how we [ensure that fixes are done](https://twitter.com/jacobian/status/1359855371431653377?s=21).

None of this is simple, and as we as an industry increasingly ask ourselves [ethical questions about software engineering itself](https://qconlondon.com/topics/tech-ethics), we need to include conversations about the right ethical lines around vulnerability research, disclosure and so on.

## [Researcher hacks over 35 tech firms in novel supply chain attack](https://www.bleepingcomputer.com/news/security/researcher-hacks-over-35-tech-firms-in-novel-supply-chain-attack/)

[https://www.bleepingcomputer.com/news/security/researcher-hacks-over-35-tech-firms-in-novel-supply-chain-attack/](https://www.bleepingcomputer.com/news/security/researcher-hacks-over-35-tech-firms-in-novel-supply-chain-attack/)

> Birsan noticed some of the manifest file packages were not present on the public npm repository but were instead PayPal's privately created npm packages, used and stored internally by the company.
>  
> On seeing this, the researcher wondered, should a package by the same name exist in the public npm repository, in addition to a private NodeJS repository, which one would get priority?
> 
> To test this hypothesis, Birsan began hunting for names of private internal packages that he could find in manifest files on GitHub repositories or in CDNs of prominent companies but did not exist in a public open-source repository.
> 
> The researcher then started creating counterfeit projects using the same names on open-source repositories such as npm, PyPI, and RubyGems.


This is an interesting supply chain attack, although we’ll have to come up with some new comenclature to disambiguate this kind of attack from a solarwinds style attack.  Anyway...

This is an interesting attack, because the bug in question is present by design in pretty much all dependency resolution software.  If you specify that you want somepackage with at least version 1.1.0, then they will search your private repositories for the package, but also public repositories for that package.  Some can be configured (or easily misconfigured) to prefer packages that they find from the internet over private packages.  Others all behave the same way when presented with newer or higher version numbered packages on public repositories.

This mechanism of getting packages into the build chain is ingenious, but I’m a bit suspicious of Birsan’s methods here though.  He uploaded these packages to a volunteer  run public repository, and those packages had malicious code that even went as far as to use DNS as the exfiltration route.  I think that crosses a line in ethical security research, because he cannot know enough about the internals of the build systems to be confident that he wasn’t breaking the build system (likely given he replaced a library it depended on), and that he wasn’t corrupting builds or systems further downstream.

The companies all paid out, and paid out handsomely, so I guess they felt it was a valid find of a serious vulnerability though.  It would be nice if, as the researcher, he also felt obliged to contribute code to these open source packaging systems that would close that vulnerability or make it clearer to users when they had misconfigured their systems.


## [A Hacker Tried to Poison a Florida City's Water Supply, Officials Say | WIRED](https://www.wired.com/story/oldsmar-florida-water-utility-hack/)

[https://www.wired.com/story/oldsmar-florida-water-utility-hack/](https://www.wired.com/story/oldsmar-florida-water-utility-hack/)

> AROUND 8 AM on Friday morning, an employee of a water treatment plant in the 15,000-person city of Oldsmar, Florida, noticed that his mouse cursor was moving strangely on his computer screen, out of his control, as local police would later tell it. Initially, he wasn't concerned; the plant used the remote-access software TeamViewer to allow staff to share screens and troubleshoot IT issues, and his boss often connected to his computer to monitor the facility's systems. 
> 
> But a few hours later, police say, the plant operator noticed his mouse moving out of his control again. This time there would be no illusion of benign monitoring from a supervisor or IT person. The cursor began clicking through the water treatment plant's controls. Within seconds, the intruder was attempting to change the water supply's levels of sodium hydroxide, also known as lye or caustic soda, moving the setting from 100 parts per million to 11,100 parts per million. In low concentrations the corrosive chemical regulates the PH level of potable water. At high levels, it severely damages any human tissue it touches.
> 
> According to city officials, the operator quickly spotted the intrusion and returned the sodium hydroxide to normal levels. Even if he hadn't, the poisoned water would have taken 24 to 36 hours to reach the city's population, and automated PH testing safeguards would have triggered an alarm and caught the change before anyone was harmed


This story is going to run and run. Attempting to poison water supplies is a huge deal, even the UN declares that it’s [a breach of international norms to target water treatment systems during wartime ](https://casebook.icrc.org/case-study/water-and-armed-conflicts).

Of course, talk about cyber attack, and everybody jumps to assumptions about nation state attackers, which promptly caused a mild panic on twitter, with claims that this could precipitate an actual war, questions about international diplomacy and much hand wringing.

Of course, the [most likely thing is that some amateur or bored hacker](https://twitter.com/malwarejake/status/1359126152485429257?s=21), likely a teenager, found an open TeamViewer through a scanning tool like Shodan, and got in, and then wondered what they had got to, so clicked some buttons at random.  Of course, the water systems are resilient, so as Wired points out, there was never really any risk to end residents, because safety systems in these things are designed to assume that upstream (pun firmly intended) systems are going to fail at some point.

Of course, this leads to much hand wringing about why TeamViewer was exposed to the internet (here’s a clue, that’s cheap and easy... for an IT team with no budget, it looks like a sensible move), and what else you can find if you look hard enough.


## [DanHon on twitter](https://twitter.com/hondanhon/status/1359587806159405057?s=21)

[https://twitter.com/hondanhon/status/1359587806159405057?s=21](https://twitter.com/hondanhon/status/1359587806159405057?s=21)

> I see we're talking about volunteer vaccination websites again, thanks to this (imho) irresponsible NYT article about "building a new [vaccination website] for $50".
> 
> Some observations and references:


Dan does an absolutely marvellous job here of summarising the problems with many startups and startup attitude to engineering.   The cost to build a bit of tech in a startup “move fast and break stuff” way is vastly different to the cost to build accessible and inclusive systems.  Government doesn’t have the choice, like certain startups like Clubhouse, to pick their target demographic.  Everyone has to be able to access government services, whether they are poor or rich, and Android, iPhone or non smartphone users.  That Increases the cost to build something.

But the cost of build by far dwarfs the cost to run something.  Operating a complex government service requires not just technical operations, which by all anecdata is 20x the cost of build (if not more), but requires you to run a service.  That might include logistics, support, service centres and much more.  

Go read the entire thread, it’s well worth your time


## [Supermicro Hack: How China Exploited a U.S. Tech Supplier Over Years](https://www.bloomberg.com/features/2021-supermicro/)

[https://www.bloomberg.com/features/2021-supermicro/](https://www.bloomberg.com/features/2021-supermicro/)

> Bloomberg Businessweek first reported on China’s meddling with Supermicro products in October 2018, in an article that focused on accounts of added malicious chips found on server motherboards in 2015. That story said Apple Inc. and Amazon.com Inc. had discovered the chips on equipment they’d purchased. Supermicro, Apple and Amazon publicly called for a retraction. U.S. government officials also disputed the article.
> With additional reporting, it’s now clear that the Businessweek report captured only part of a larger chain of events in which U.S. officials first suspected, then investigated, monitored and tried to manage China’s repeated manipulation of Supermicro’s products.


There is doubling down and then there is real doubling down.  To an expert, this story reads like a set of non-experts reading briefings and getting very confused by the language used.
All of the individual things in the story are possible, but the way they are woven together into a narrative is just not believable.  

Two years ago, I wrote the longest CyberWeekly ever, [issue 20](http://cyberweekly.net/china-russia-facebook-conservatives-it-s-been-quite-a-week) in which I declared 

> Technical reporting has come along in leaps and bounds, with reporters covering highly technical beats with style. But most reporters just don't have the technical knowledge to actually understand the technology behind the things they are reporting on. There are very few journalists who actually know what a cross-site-scripting attack actually looks like, or knows how javascript is packaged and executed.

I don’t think this has changed, certainly not from Bloomberg in the last 2 years.


## [No, Java is not a Secure Programming Language – Little Man In My Head](https://littlemaninmyhead.wordpress.com/2021/01/28/no-java-is-not-a-secure-programming-language/)

[https://littlemaninmyhead.wordpress.com/2021/01/28/no-java-is-not-a-secure-programming-language/](https://littlemaninmyhead.wordpress.com/2021/01/28/no-java-is-not-a-secure-programming-language/)

> This blog is intended to correct one of the most perpetuated security myths by showing why Java is lagging far behind in security design in comparison to modern competitive languages. The problems are twofold:
> 
> Many Java security bugs are due to insecure defaults. As a consequence, developers need to have advanced development knowledge just to write simple code that cannot be easily exploited.
> Java has really poor documentation: it is not hard to make things work, but it is often very unclear how to do things the ‘right way.’


This is a good rant about the insecure defaults in the Java ecosystem, and one that I mostly agree with.

There’s also something inhere about how we can make our ecosystems more secure by providing better defaults and more secure example coding practices.  That’s one of the ways that we can lift the entire industry at once.


## [Deloitte NASCIO Cybersecurity Survey | Deloitte Insights](https://www2.deloitte.com/us/en/insights/industry/public-sector/nascio-survey-government-cybersecurity-strategies.html)

[https://www2.deloitte.com/us/en/insights/industry/public-sector/nascio-survey-government-cybersecurity-strategies.html](https://www2.deloitte.com/us/en/insights/industry/public-sector/nascio-survey-government-cybersecurity-strategies.html)

> One of the most notable challenges CISOs faced during the pandemic was the abrupt shift to remote work. According to the study:
> 
> * Before the pandemic, 52% of respondents said less than 5% of staff worked remotely.
> * During the pandemic, 35 states have had more than half of employees working remotely; nine states have had more than 90% remote workers.
> 
> “The pandemic forced state governments to act quickly, not just in terms of public health and safety but also with regard to cybersecurity,” says Srini Subramanian, Deloitte & Touche LLP's state and local government advisory leader.


We’re not going back to the office full time.  The more I read articles about it, the more convinced I am that this is true.

The pandemic response and shutdown has forced a change that would have taken decades to happen in months, and we’re not ready for it, but we’re going to live with it.


## [» Serious issues in NurseryCam](https://cybergibbons.com/security-2/serious-issues-in-nurserycam/)

[https://cybergibbons.com/security-2/serious-issues-in-nurserycam/](https://cybergibbons.com/security-2/serious-issues-in-nurserycam/)

> I am not following the disclosure policy I follow normally as part of professional work due to the severity.
> 
> Given how the owner of FootFallCam have behaved, I cannot hold these back. The business managing these systems have not demonstrated they can handle data this important, and cannot handle this honestly.
> 
> When I saw the issues with FootfallCam, I noticed that there was a related product called NurseryCam which allows CCTV monitoring of children in nurseries.
> 
> Given the serious issues in FootfallCam, it concerned me that the same company could be handling the sensitive data like this.


So these issues are pretty serious.  Any user who has access to a nursery cam, so any parent, staff member who has ever had access, can get the credentials and continue to use them.

The bigger question here is whether Cybergibbon should have followed a responsible disclosure policy here.  I think given how the company behaved before, I support that he decided not to in this case.  Responsible disclosure requires good faith on both parties, and if one party shows that they won’t play by the rules, then why should anyone else?


## [Footfallcam kerfuffle: Firm apologises, promises to fix product after viral Twitter thread, infoseccer backlash • The Register](https://www.theregister.com/2021/02/12/footfallcam_twitter_kerfuffle/)

[https://www.theregister.com/2021/02/12/footfallcam_twitter_kerfuffle/](https://www.theregister.com/2021/02/12/footfallcam_twitter_kerfuffle/)

> A cautionary tale about the dangers posed by affordable Internet of Things devices turned into a much more sinister story after a company threatened an infosec bod with a police report (since retracted) unless he deleted a Twitter thread highlighting shortcomings in one of its products.
> 
> The device at the heart of the controversy was essentially a Raspberry Pi in a fancy enclosure, as Laurens Leemans of SignIPS, who analysed a sample Footfallcam 3D Plus product, told The Register.
> 
> SignIPS sells digital signage and other B2B goods. Leemans, who tweets as @OversoftNL, said he was privately reviewing the Footfallcam to assess whether to add it to SignIPS's range. The device is intended to be installed in shops to count the number of people passing through a doorway.
> 
> Based on his examination of the sample device, Leemans said it had an onboard Wi-Fi network with an admin password of 123456 which couldn't be changed – though Melissa Kao, director of international sales at Footfallcam told us the password could have been changed if the device was registered with the company's web services. SSH was also available through the Wi-Fi network, as Leemans discovered. There were other flaws too.


This story started fun and then just got weirder and weirder as time went by.

Originally, this just felt like a somewhat typical “internet of things == insecure” story.  The device was appallingly packaged, with the developers home directory imaged onto it.

Then the maker got upset, reported the researcher to ActionFraud, and started creating sock puppet accounts on Twitter to attack the researcher.

Then the register got involved and was accused of being part of a grey hat infosec conspiracy.

But things are only about to get even odder and worse...


