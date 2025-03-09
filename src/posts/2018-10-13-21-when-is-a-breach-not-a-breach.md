---
title: "21 - When is a breach not a breach?"
date: 2018-10-13
description: "This week, Google announced that they had found a vulnerability in GooglePlus, but hadn't told anyone.  There was some discussion online about whether they had broken the law, in particular GDPR, and whether they had acted responsibly."
permalink: /when-is-a-breach-not-a-breach/
---

This week, Google announced that they had found a vulnerability in GooglePlus, but hadn't told anyone.  There was some discussion online about whether they had broken the law, in particular GDPR, and whether they had acted responsibly.

But it draws out the discussion about the difference between a vulnerability and a breach.  We find vulnerabilities in our code and systems all the time.  Sometimes a developer just notices it and fixes it, sometimes it's found by a penetration test or security audit, and sometimes we don't even know that a feature change has fixed a vulnerability that we didn't know existed.

If we find a vulnerability, do we have to tell users of our software that it was potentially vulnerable?  Probably not.  To become a breach, it requires a threat actor, somebody with ill intent, to exploit that vulnerability and to access data or cause a business impact.

But what if we don't have enough information to know whether or not somebody actually expoited it?  Google was castigated for only keeping two weeks worth of logs, but it's entirely possible that an unintended vulnerability is in a part of the system is not logged at all.  If that's the case, should we assume that it was breached?

Even the [UK ICO's guidance](https://ico.org.uk/for-organisations/guide-to-the-general-data-protection-regulation-gdpr/personal-data-breaches/) on the matter tells you to take a risk based judgement on whether the breach occurred and will be damaging to users, and to document it so you can justify it.

I think we'll see more of this discussion over the next year as well, as the 72 hour breach notification rules in GDPR mean that organisations need to be quick at making that risk based decision, even if not all the evidence is available yet.

## [Project Strobe: Protecting your data, improving our third-party APIs, and sunsetting consumer Google+](https://www.blog.google/technology/safety-security/project-strobe/)

[https://www.blog.google/technology/safety-security/project-strobe/](https://www.blog.google/technology/safety-security/project-strobe/)

> We made Google+ with privacy in mind and therefore keep this API’s log data for only two weeks. That means we cannot confirm which users were impacted by this bug. However, we ran a detailed analysis over the two weeks prior to patching the bug, and from that analysis, the Profiles of up to 500,000 Google+ accounts were potentially affected. Our analysis showed that up to 438 applications may have used this API.
> 
> We found no evidence that any developer was aware of this bug, or abusing the API, and we found no evidence that any Profile data was misused.


There's quite a few articles on this issue this week, but I went back to the source for this.

The detail that stands out to me is that there were only 438 applications that could use the API, and that they didn't think that any developer of those applications was aware of the bug and using it on purpose.  Very few of the articles online that I read about this had noted or considered this

I think this is reasonable evidence that the vulnerability was not exploited, but they can't be sure because the logs only extend back 2 weeks, which is less than sufficient to determine whether it has actually been breached, so there will be some uncertainty.

The key thing here, is that based on incomplete information, is it acceptable to make an assumption on the happier outcome, or do we always need to assume the worst?


## [GAO-19-128 WEAPON SYSTEMS CYBERSECURITY](https://www.gao.gov/assets/700/694913.pdf)

[https://www.gao.gov/assets/700/694913.pdf](https://www.gao.gov/assets/700/694913.pdf)

> A patch or software enhancement that causes problems in an email system is inconvenient, whereas one that affects an aircraft or missile system could be catastrophic. 
> 
> Officials from one program we met with said they are supposed to apply patches within 21 days of when they are released, but fully testing a patch can take months due to the complexity of the system. Even when patches have been tested, applying the patches may take additional time. 
> 
> Further, weapon systems are often dispersed or deployed throughout the world. Some deployed systems may only be patched or receive software enhancements when they return to specific locations. 
> 
> Although there are valid reasons for delaying or forgoing weapon systems patches, this means some weapon systems are operating, possibly for extended periods, with known vulnerabilities.
> 
> [...]
> 
> One test team emulated a denial of service attack by
> rebooting the system, ensuring the system could not carry out its mission for a short period of time. Operators reported that they did not suspect a cyber attack because unexplained crashes were normal for the system.
> 
> Another test report indicated that the intrusion detection system correctly identified test team activity, but did not improve users’ awareness of test team activities because it was always “red.” Warnings were so common that operators were desensitized to them.


This report from the GAO is fascinating and terrifying in equal measure.  There's lots of interesting details in here, but it does make clear that the complexity of the environment that we are talking about.

A warship is not as simple as a web application, and sadly, the cloud isn't going to solve many of these problems.  However connectivity is on the rise, and even if the battleship may not be connected to the internet, there's a good possibility that the staff on it will have mobile devices that connect to the internet over high speed connections.  What are the chances that they'll connect those devices to the shipboard network?

As always, this is going to be a job of fixing the basics, not applying magic machine learning and AI cybersecurity  boondoggles


## [Facebook Says 14 Million People Got Their Location Data and Private Search History Stolen - Motherboard](https://motherboard.vice.com/en_us/article/d3qejz/facebook-hack-13-million-victims-search-history)

[https://motherboard.vice.com/en_us/article/d3qejz/facebook-hack-13-million-victims-search-history](https://motherboard.vice.com/en_us/article/d3qejz/facebook-hack-13-million-victims-search-history)

> In a blog post published Friday, Facebook said that “of the 50 million people whose access tokens we believed were affected, about 30 million actually had their tokens stolen.” Of those 30 million, Facebook said it identified four groups of victims hit in different stages: an initial group of 400,000 users, a second group of 15 million people, a third of 14 million, and a final of 1 million.


Facebook has come out and provided more information on the breach from last week (you might have missed it in all the news).

Facebook has done a pretty good job here of actually communicating as details have emerged.  The worry I have is whether the media attention will stay on this or not.


## [Amazon scraps secret AI recruiting tool that showed bias against women](https://reut.rs/2Pmn6zu)

[https://reut.rs/2Pmn6zu](https://reut.rs/2Pmn6zu)

> In effect, Amazon’s system taught itself that male candidates were preferable. It penalized resumes that included the word “women’s,” as in “women’s chess club captain.” And it downgraded graduates of two all-women’s colleges, according to people familiar with the matter. They did not specify the names of the schools.
> 
> Amazon edited the programs to make them neutral to these particular terms. But that was no guarantee that the machines would not devise other ways of sorting candidates that could prove discriminatory, the people said.
> 
> The Seattle company ultimately disbanded the team by the start of last year because executives lost hope for the project, according to the people, who spoke on condition of anonymity. Amazon’s recruiters looked at the recommendations generated by the tool when searching for new hires, but never relied solely on those rankings, they said.


This is interesting, because there are two ways to view this.

The first is that we created an AI system that exhibited bias, proving that it's increasingly hard not to encode biases into machine learning systems.  We've been saying this for some time, that creating an AI system is really hard because the data is almost always biased in some way.

The other is to point out that by encoding the data of how Amazon was hiring people before, what it did was actively highlight the existing biases of the recruitment teams.  The CV's they put into the systems were ones that their recruiters had selected as "good" and "bad", and it encoded those decisions.

Either way, I think it's a bit of a cop out to say "The system didn't make any decisions, it just informed real people".  Of course they are going to use the simplest thing available to them, which is accept the computer recommendations most of the time.


## [The Good Censor - Google Leak](http://j.mp/2pNDzBp)

[http://j.mp/2pNDzBp](http://j.mp/2pNDzBp)

> Relentless, 24/7 online conversations encourage people to *dive in with their opinion* before it's too late, even if they're misinformed.  And because we think with out emotional brain before rational one, instant response *amplify emotion-led discourse* not thoughtful debate.


This was linked to me in terms of *OMG, a good censor, how terrible*, but I think it's actually a very good breakdown of the debate about free-speech online and the position of a platform.

But this entire section about users bad behaviour stood out to me.  We often accuse users of our IT products of bad security behaviours.  But this section really highlights the fact that we need to better understand people's psychology and the reasons behind their actions.  Because while people aren't always logical, they are always taking their actions for a deliberate reason.


## [Automated vulnerability checks and the end of NSP · Tes engineering blog](https://engineering.tes.com/post/automated-vulnerability-checks-after-nsp/)

[https://engineering.tes.com/post/automated-vulnerability-checks-after-nsp/](https://engineering.tes.com/post/automated-vulnerability-checks-after-nsp/)

> If you’re building automated vulnerability checking into your repository for the first time, you’re likely going to be surprised by the number of vulnerabilities these tools will find. Basically, all those major version bumps you’ve been putting off are suddenly going to become very important. This even happened when we switched from nsp to npm audit, which found many more vulnerabilities than its predecessor.


This is a good overview of implementing automated vulnerability checks in the build pipeline.  

The sheer number of alerts you'll find the first time can be overwhelming, but this gets better as you handle them and process them.


## [DOJ arrests Chinese intel officer charged with economic espionage - CNNPolitics](https://edition.cnn.com/2018/10/10/politics/doj-chinese-intelligence-officer-aviation/index.html?utm_term=image&utm_medium=social&utm_source=twCNN&utm_content=2018-10-11T00%3A50%3A01)

[https://edition.cnn.com/2018/10/10/politics/doj-chinese-intelligence-officer-aviation/index.html?utm_term=image&utm_medium=social&utm_source=twCNN&utm_content=2018-10-11T00%3A50%3A01](https://edition.cnn.com/2018/10/10/politics/doj-chinese-intelligence-officer-aviation/index.html?utm_term=image&utm_medium=social&utm_source=twCNN&utm_content=2018-10-11T00%3A50%3A01)

> Yanjun Xu faces four charges of conspiring and attempting to commit economic espionage and theft of trade secrets, according to the indictment. DOJ officials said the indictment marks the first time a Chinese Ministry of State Security operative has been arrested and brought to the United States to face charges. He's charged with working to get aviation employees to inadvertently reveal trade secrets to the Chinese government.
> "This unprecedented extradition of a Chinese intelligence officer exposes the Chinese government's direct oversight of economic espionage against the United States," said Bill Priestap, assistant director of the FBI's Counterintelligence Division, in a statement.
> 
> Former CIA officer is charged with espionage
> Xu was one of several Ministry of State Security officials who, starting in 2013, allegedly identified aviation industry experts at at least three companies, including Cincinnati-based GE Aviation, and invited them to China under the guise of speaking at universities for an idea exchange, according to the Justice Departmen complaint.
> However, these presentations were purely for the benefit of the Chinese government, and often included highly technical discussions about a company's signature material design and manufacturing technology.


This is an interesting move from the US.  More legal movements.  I think this is going to be a case to watch


