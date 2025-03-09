---
title: "79 - Do we know why things go right?"
date: 2019-11-23
description: "In security, we spend a lot of time thinking about how things fail."
permalink: /do-we-know-hwy-things-go-right/
---

In security, we spend a lot of time thinking about how things fail.

Actually, that’s not quite right.  We spend a lot of time thinking about how malicious actors can cause things to fail.  We think about failure in terms of human decisions on systems, whether that be accidentally cc’ing the wrong person on that HR spreadsheet, clicking a link in a phishing email, or making our S3 bucket to be publicly accessible.

We don’t think a lot about how systems themselves fail.  Security people often assume that the system itself is working correctly, but that there are malicious humans who are trying to get around the correctly working system.  

But this fantasy idea that most systems are working is entirely that a fallacy.  System failure is all around us all of the time.  Most systems, whether technical or business process systems, have various safeguards in them that catch errors and retry silently.  This exceptional processes are often not document and are quite often entirely silent to those outside the system.  You can’t see those failures occurring because the things you do measure are still moving in exactly the way they always have.

Safety engineering and reliability engineering is predicated on the assumption that any part of the system could fail, and ensuring that we can handle that failure gracefully and recover for certain values of business continuity.  But in security and digital transformation, we tend to have far too much blind faith in the systems that we build.

Whether it be the assumption that the messy chaotic real word system and process is a sign of inefficiency, or the assumption that there is a single root cause for a catastrophic failure, and that all of the individual failures are somehow special with the benefit of hindsight.  This assumption hurts us and makes systems less reliable, less likely to succeed and less secure.

If you have time you should watch [Who destroyed three mile island](https://youtu.be/1xQeXOz0Ncs) as a great introduction to this subject.

## ['Mario Maker 2' Creators Are Using Cryptography to Make Impossible Levels - VICE](https://www.vice.com/en_us/article/qvg5aw/mario-maker-2-creators-are-using-cryptography-to-make-impossible-levels)

[https://www.vice.com/en_us/article/qvg5aw/mario-maker-2-creators-are-using-cryptography-to-make-impossible-levels](https://www.vice.com/en_us/article/qvg5aw/mario-maker-2-creators-are-using-cryptography-to-make-impossible-levels)

> The way Cyber Security 101 works is best understood by just watching PangaeaPanga explain it himself, but in short, inputting the correct digit results in a POW block being carried into another part of the level. When the player hits a music note later in the stage, signaling they’re ready to confirm the passcode, a bob-omb will start moving forward. If the correct number of POW blocks are in place, confirming the correct passcode, the bob-omb will eventually fall down in front of the player, blowing up a block that’s hiding a red coin. The red coins unlock a key, and the key is required to walk through the door hiding the exit


This is fun.  Very simple passcode entering systems, so it’s not really cryptography, more akin to a standard tumbler in a lock.  But fun none the less.


## [How to recognize AI snake oil by Arvind Narayanan, Associate Professor of Computer Science](https://www.cs.princeton.edu/~arvindn/talks/MIT-STS-AI-snakeoil.pdf)

[https://www.cs.princeton.edu/~arvindn/talks/MIT-STS-AI-snakeoil.pdf](https://www.cs.princeton.edu/~arvindn/talks/MIT-STS-AI-snakeoil.pdf)

> 13,000 features hardly better than 4 features! “AI” hardly better than simple linear formula


This presentation can be boiled down to a very simple model.

If the AI is about perception systems (image recognition type stuff) then that area is mostly not snake oil, and has been making advances

If the AI is about automated judgement (spam detection, grading exams etc), then it’s highly dependent.  There have been some advances, but there are high error rates and these need manual overview and outs.

If the AI is about predicting social outcomes then it’s almost certainly snake oil.  Even the best AI competitions show that AI is massively below human biased judgement, and barely better than pure linear formula.


## [Tories pretend to be factchecking service during leaders' debate | Politics | The Guardian](https://www.theguardian.com/politics/2019/nov/19/tories-tweet-anti-labour-posts-under-factcheckuk-brand?CMP=Share_iOSApp_Other)

[https://www.theguardian.com/politics/2019/nov/19/tories-tweet-anti-labour-posts-under-factcheckuk-brand?CMP=Share_iOSApp_Other](https://www.theguardian.com/politics/2019/nov/19/tories-tweet-anti-labour-posts-under-factcheckuk-brand?CMP=Share_iOSApp_Other)

> During Tuesday night’s debate between Boris Johnson and Jeremy Corbyn, the Conservative party renamed their main media account as “factcheckUK”, changed its logo to hide its political origins, and used it to push pro-Conservative material to the public.
> 
> Although the Twitter handle remained a s @CCHQPress, all other branding was changed to resemble an independent factchecking outlet, meaning it may not have been immediately apparent to an individual who saw the account’s tweets in their feed that it was a product of Conservative party HQ.
> 
> On clicking through, they would have seen a disclaimer that factcheckUK was “fact checking Labour from CCHQ”, ” the acronym for Conservative campaign headquarters.


First of all, several people in my twitter timeline had misread this as fact checking from GCHQ, which is definitely not what anybody expected!

Secondly, this and Twitter’s response (don’t do it again or we’ll be cross) is highly disappointing.

I can picture the internal discussions in CCHQ comms team where they discuss “fact checking” their opponents claims, and nobody in the room has enough awareness to realise just what a shockingly bad idea this is going to be.


## [A new Sino-Russian high-tech partnership | Australian Strategic Policy Institute | ASPI](https://www.aspi.org.au/report/new-sino-russian-high-tech-partnership)

[https://www.aspi.org.au/report/new-sino-russian-high-tech-partnership](https://www.aspi.org.au/report/new-sino-russian-high-tech-partnership)

> Russia may benefit from its embrace of China’s technology prowess and financing, but the full range of risks and potential externalities is still emerging and perhaps poorly understood. As Sino-Russian partnership has deepened, observers of this complex relationship have often anticipated some kind of ‘break’ in the ongoing Russo-Chinese ‘entente’.132 Many commentators find it difficult to believe that countries with such global ambitions and past historical grievances can place much trust in each other.
> 
> Certainly, there have been subtle indications of underlying friction, including Russia’s initial reluctance to embrace Xi’s signature One Belt, One Road initiative, to which Moscow has since warmed, or so it seems.
> 
> Going forward, high-tech cooperation between Moscow and Beijing appears likely to deepen and accelerate in the near term, based on current trends and initiatives. In a world of globalised innovation, scientific knowledge and advanced technologies have been able to cross borders freely over the past quarter of a century. China and Russia have been able to take advantage of free and open STEM development, from life sciences to information technology and emerging technologies, applying the results to their own distinctive technological ecosystems.


It’s easy for western people to think about the world as “the west” versus the others.  In reality global cooperation is a complex topic, and countries are many headed beasts.  We might cooperate with countries on science research projects while objecting to them militarily, and also engage in cultural exchange.

This report is a good review of how Russia and China are increasingly working together, especially in technology.  The implication is that they both see the US as the dominant force, and while both would like to dominate these areas globally, they can do so better by teaming up than they can individually.

Of course, both are adversarial estates from a cyber perspective as well, and there will always be some low level espionage and cyber attacks against each other by the advanced actors working on their behalf as well.  It will be interesting to see if any of the technology cooperation extends to cyber weapons and knowledge as well as traditional technology solutions.


## [NBA, NFL and NCAA making noise over privacy app](https://sports.yahoo.com/why-has-the-ci-as-preferred-privacy-app-hit-the-nba-nfl-and-ncaa-061242791.html?guccounter=1)

[https://sports.yahoo.com/why-has-the-ci-as-preferred-privacy-app-hit-the-nba-nfl-and-ncaa-061242791.html?guccounter=1](https://sports.yahoo.com/why-has-the-ci-as-preferred-privacy-app-hit-the-nba-nfl-and-ncaa-061242791.html?guccounter=1)

> Signal is viewed as the safest encryption app available. Kaufman said the messages remain secure and can't be compromised or intercepted "without a hell of a lot of effort." And while it doesn't allow for the full allotment of GIFs and emoticons of traditional text banter, it's a place where information, documents and even phone calls can be conducted with increased discretion.
> 
> "Our general counsel encouraged us to get on Signal," said a high-ranking collegiate athletic official. "There's auto-delete based on the rules you set, and that helps us avoid FOIA requests. ...It's become the main method of communication between the administration and our [athletic] staff."


Legally correct or not, I do not believe that it is ethically correct for an organisation to advise its employees on how to deliberately attempt to circumvent freedom of information rules.

I spend a lot of time reminding people across Government that the UK's Freedom of Information Act covers anywhere that they write down information in a work setting.  So it doesn't matter if they arrange that meeting via email, via corporate Google Hangouts, via WhatsApp on their work phone or via Signal on their personal phone, it's information that should be in scope of the law and could (in theory) be requested one day.

Of course the problem comes when the knowledge and information management team get the request and try to work out who to contact to ask about what information is held.  If they simply look at their enterprise dashboard of the "Knowledge Store", then at best they'll see some emails and maybe stuff explicitely tagged to be retained.

But that doesn't excuse us from acting as public servants and accepting that our communications, either today, or in 50-100 years time for historians, should be recorded, kept and made available.


## [A retrospective impact analysis of the WannaCry cyberattack on the NHS | npj Digital Medicine](https://www.nature.com/articles/s41746-019-0161-6)

[https://www.nature.com/articles/s41746-019-0161-6](https://www.nature.com/articles/s41746-019-0161-6)

> Our analysis of the HES data demonstrated the impact of the WannaCry attack across the NHS in England. This resulted in a 6% decrease in admissions in the infected hospitals, which included 1100 fewer emergency department (ED) admissions and 2200 fewer elective admissions in total. The infected hospitals also saw a decrease in the number of ED attendances with 3800 fewer patients seen. There was a significant impact on the number of outpatient cancellations across the infected hospitals during the WannaCry week—this resulted in 13,500 appointments being cancelled. The financial impact of the attack was also calculated, and the value of the reduction in the activity in the infected trusts amounted to £5.9 m. If this pattern were seen across all NHS hospitals, the reduced activity alone would have cost £35 m.


This is an interesting analysis of the Wannacry attack.  It looks at the impact of the hospital shutdowns and showed the the health system fundamentally absorbed the impact.

What it doesn’t do, and I’d love to see is to compare it against another situation in which a number of hospitals have declared an emergency and shifted patient intake around to cope.   I’m sure that this happens in other situations, and I’d love to know whether the impacts the result of wannacry affecting IT itself, or simply the impact of declaring a major emergency.


## [Add defense in depth against open firewalls, reverse proxies, and SSRF vulnerabilities with enhancements to the EC2 Instance Metadata Service | AWS Security Blog](https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/)

[https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/](https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/)

> With IMDSv2, every request is now protected by session authentication. A session begins and ends a series of requests that software running on an EC2 instance uses to access the locally-stored EC2 instance metadata and credentials. The software starts a session with a simple HTTP PUT request to IMDSv2. IMDSv2 returns a secret token to the software running on the EC2 instance, which will use the token as a password to make requests to IMDSv2 for metadata and credentials. Unlike traditional passwords, you don’t need to worry about getting the token to the software, because the software gets it for itself with the PUT request. The token is never stored by IMDSv2 and can never be retrieved by subsequent calls, so a session and its token are effectively destroyed when the process using the token terminates. There’s no limit on the number of requests within a single session, and there’s no limit on the number of IMDSv2 sessions. Sessions can last up to six hours and, for added security, a session token can only be used directly from the EC2 instance where that session began.


As demonstrated recently, server side request forgery against the classic AWS internal metadata service (IMDS) was trivially easy and a common attack on cloud services.  It’s one of the ways that S3 buckets can be compromised, because often instances need access to the bucket, so getting the access keys from the metadata service is the first thing you need to do.

I’m sure that this makes things better, however as with all security systems, key management is critical.  If you get this key on startup and store it in an environment variable, then an attacker can probably get the key from there.  It does however add an extra step for attackers to carry out, all of which increases the complexity of the attack and increases the likelihood of being caught.

You should upgrade your systems to use IMDSv2 as soon as possible, this definitely makes things more secure.


## [Opening up risk management: Always on, everybody’s business | ThoughtWorks](https://www.thoughtworks.com/insights/blog/opening-risk-management-always-everybody-s-business?_lrsc=20524569-31c7-41d8-a2ae-f29c2bf8640d)

[https://www.thoughtworks.com/insights/blog/opening-risk-management-always-everybody-s-business?_lrsc=20524569-31c7-41d8-a2ae-f29c2bf8640d](https://www.thoughtworks.com/insights/blog/opening-risk-management-always-everybody-s-business?_lrsc=20524569-31c7-41d8-a2ae-f29c2bf8640d)

> 3. Make risk management a team effort
> 
> Any organisation with a risk management division that sits in a silo very likely has a tunnel-vision. Just as technology increasingly cuts across functions, risk needs to be perceived and addressed as a collective responsibility. When the enterprise sets out to identify and measure risk, virtually every stakeholder with a say in the needs and objectives of the business should be represented. This means delivery teams, who have to understand the risk (and value) of what they’re building, but also legal and compliance, who could identify stakeholder needs that have not been addressed, as well as the finance teams who may need to sign off on risk management investments. It even includes customer-facing teams with vital insight into how products are used in the field.


As many people have commented in the past, I’m a big fan of risk management.  But I dislike that it is a esoteric discipline within information security, that only special security and risk advisors can chant the appropriate incantations to develop a poor risk matrix.

This argument that risk is something that the entire team needs to understand, and needs to be clearly communicated is something I agree with.

What is missing from here, and something I know that Jim has been working on, is the practicalities on how to actually achieve this.  How we make it less boring, but also how do we make it more rigorous and well understood.  Hopefully he’ll publish more blog posts on his thinking here.


## [The Efficiency-Destroying Magic of Tidying Up – Florent Crivello](https://florentcrivello.com/index.php/2019/09/04/the-efficiency-destroying-magic-of-tidying-up/)

[https://florentcrivello.com/index.php/2019/09/04/the-efficiency-destroying-magic-of-tidying-up/](https://florentcrivello.com/index.php/2019/09/04/the-efficiency-destroying-magic-of-tidying-up/)

> I submit that we should look with suspicion at simple-looking systems. The physical world is like a river in which a thousand streams come rushing — it is supposed to look messy.
> 
> Again, this insight applies to any complex system. For example, a city can look as messy as an anthill. But really, it’s a beautiful equilibrium that evolved to satisfy a thousand competing constraints: topology, weather, people’s traditions, skills, wealth, preferences… Planners may make their maps look better when they use zoning to separate the city into business, residential, and commercial neighborhoods, but they also destroy a subtle, efficient balance. They forget that the only activity that goes on in any city is that of people living their lives, which requires all the activities above — preferably in close proximity. Splitting a city into residential, commercial and business zones is like throwing dough, cheese and pepperoni into the different compartments of a bento box and calling it a pizza.
> 
> [...]
> 
> Finally: who is complaining about the chaos? If outsiders complain, but people living inside the system seem happy with it, it probably means that the chaos is serving them right, and that it’s just foreign eyes who are unable to perceive its underlying order.
> 
> This is a special case of Chesterton’s Fence, which states you should never take down a fence before knowing why it was put up. Here, I propose Scott’s Law: never put order in a system before you understand the structure underneath its chaos.


How often do we look at huge legacy systems as a giant mess that can’t possibly work and complain that it would be so much simpler if we did it again?

We have an inclination towards orderly and tidyness, but reality is just not like that.  Some of those chaotic bad systems are the result of hundreds of individual decisions, which would be better if there was a coherent whole.  But one of the biggest lies of “Software Architecture” is that having a architectural framework will make it better this time.

Is it time to embrace the chaos, the duplication, the lots of independent systems coexisting and running instead of regimented hierarchical monoliths?


## [Jon Hall on Twitter](https://twitter.com/JonHall_/status/1197268706042286081)

[https://twitter.com/JonHall_/status/1197268706042286081](https://twitter.com/JonHall_/status/1197268706042286081)

> I've been working through the recent independent report into a huge IT migration failure at TSB bank in the UK. The full report is here, and there's a lot to address, but a walk through the executive summary is revealing, almost jaw dropping at times.


This [pdf report](https://www.tsb.co.uk/news-releases/slaughter-and-may/slaughter-and-may-report.pdf), which is 262 pages, is one I’m still reading through.  But this overview by JonHall is worth reading for some of the highlights.

I originally wrote about the TSB failure way back in [CyberWeekly #4](https://tinyletter.com/CyberWeekly/letters/another-californian-cyber-weekly) in June 2018, and it’s taken a long time for us to get a report into what happened.

My only objection to the pile on that we have in TSB’s management of this incident (which by all accounts had all the hallmarks of failure) is that they had reason to trust SABIS, their IT supplier, because they had done 12 previous migrations.  There’s a lot of questions about what went wrong, but what I’m more curious about is what went right with the other 12 migrations?


