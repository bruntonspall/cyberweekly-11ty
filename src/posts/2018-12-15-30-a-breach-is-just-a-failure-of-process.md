---
title: "30 - A breach is just a failure of process"
date: 2018-12-15
description: "As we see breach after breach after breach, we tend to see root cause analysis processes and they always come to the same conclusion.  The process wasn't in place properly and wasn't followed."
permalink: /a-breach-is-just-a-failure-of-process/
---

As we see breach after breach after breach, we tend to see root cause analysis processes and they always come to the same conclusion.  The process wasn't in place properly and wasn't followed.

Except, that if you did the same analysis without the breach, you'd find the same thing.  Organisations around the world tend to not to have good processes and they aren't always followed.

Equifax had thing after thing go wrong in their handling of their breach, and the end finding? Processes weren't implemented properly.

How can we move beyond this? Maybe we can't, maybe we are stuck in a world where we will never get this right.  If the CIA can spend billions building covert communications systems that don't work when the users don't use them correctly, then how can we expect to do any better with less money and less on the line?

In the meantime, Equifax claimed to be collecting and managing more than 1200 times the amount of data in the Library of Congress every single day, but PornHub processed 4403 Petabytes of data in the last year, more than the entire internet in 2002.  We collectively allow organisations to amass, store and process very large amounts of data, but we don't seem to have models or processes for managing it effectively.

Maybe we need to look at different models.  I've spent a fair bit of time looking at safety and reliability systems, where people assume that people, processes and systems are fallible and where failure is assumed.  Aviation safety got steadily worse from the 40s through to the 70s, but in the 70s a new model of blame free post mortem analysis models were bought in and airlines have got safer and safer ever since.  I think as an industry, security has a lot to learn from industries where safety is critical, and sadly, we just seem to keep producing reports like the Equifax one, that essentially shrugs and says "People didn't follow the process", as if the process is good, but the people are bad.  If your process isn't regularly followed, it's a bad process and you should change it, instead of hoping that people will change.


In other news, this is the 30th newsletter in a row, and I'm pleased to say that there are 250 of you now subscribed to this newsletter.  I started this just because I read a lot of infosec, digital and transformation strategy pieces, and I wanted to write my analysis down somewhere to help me sort it through in my head.  It's been massively useful to me each week to produce this newsletter, and I hope that you find it as useful to read as I do to produce.  

I haven't given much thought to the Christmas and New Year period, but I suspect I'll send a newsletter both weekends if I can, one with a christmas theme and one with a year in review.  I'd love to hear back from some of you, especially if you've got "year in review" thoughts on the year that was 2018 and any predictions that you have for 2019.  If you get these at a work address and not at home, then have a Merry Christmas and a Happy New Year.

## [Is US military cloud safe from Russia? Fears over sensitive data - BBC News](https://www.bbc.co.uk/news/world-us-canada-46489689)

[https://www.bbc.co.uk/news/world-us-canada-46489689](https://www.bbc.co.uk/news/world-us-canada-46489689)

> Instead of military data being stored on smaller servers across different departments within the Pentagon, the information will be held in a cloud.
> 
> The cloud is a term used to describe a number of remote servers, connected to the internet, which can store vast arrays of information and can be accessed from anywhere in the world.
> 
> Top military secrets will be transferred to the Jedi cloud, including classified details about weapons systems, military personnel, intelligence and operations.
> 
> It will provide soldiers on the front line with instant access to all of the latest intelligence, making them more effective on the battlefield.
> 
> John Weiler, the director of the IT procurement group IT-AAC based in Washington, told the BBC: "I would not store my most personal data, nor would my fellow colleagues, in a commercial cloud, period, the end."
> 
> He says there are huge risks to storing such classified information on a public, commercially-held cloud run by just one company.
> 
> "We have our nuclear codes, where our troops are going to be from one day to the next. If the cloud's security is breached, then our enemies could use our information against us. They could be waiting for us."


This article has some very tenuous journalism, especially attempting to connect AWS with C5.

I'm totally torn on the Jedi contract itself, because I think AWS is a good fit for them, and I'd love to see the DoD go all in on AWS. 

It would short circuit a bunch of security conversations where people mindlessly say stupid things like "I wouldn't trust my personal data to the cloud" or "no-one who is serious uses AWS".

I understand the DoD desire to have a single cloud computing provider, because I think almost all "multi-provider" solutions are a terrible idea, but the DoD's business is remarkably varied, and the scope of Jedi is unbelievably large, so I don't quite understand why they are bundling it all as one procurement rather than a commercial framework on which multiple cloud providers could exist and different bits of DoD could select a provider that matched the specific requirements of their area.

i.e. Army HR have very different needs to a special forces geospatial intelligence platform, and I'm not sure you want to mandate Company X for both.

Incidentally, I looked up Mr Weiler on LinkedIn, and he does indeed have a LinkedIn profile, and so trusts his personal data to a cloud service.  It's also worth pointing out that I don't think anybody at the DoD has suggested keeping nuclear codes in a cloud provider, but even if they did, I suspect it would still be safer than "being stored on smaller servers across different departments within the Pentagon"


## [At the CIA, a fix to communications system that left trail of dead agents remains elusive](https://news.yahoo.com/cia-fix-communications-system-left-trail-dead-agents-remains-elusive-100046908.html?soc_src=hl-viewer&soc_trk=tw)

[https://news.yahoo.com/cia-fix-communications-system-left-trail-dead-agents-remains-elusive-100046908.html?soc_src=hl-viewer&soc_trk=tw](https://news.yahoo.com/cia-fix-communications-system-left-trail-dead-agents-remains-elusive-100046908.html?soc_src=hl-viewer&soc_trk=tw)

> Because of the scope of the problem, fixing it was also a staggering task. It’s not just “a single flawed system that needed to be fixed,” according to one former CIA official. “It was a universe of systems.”
> 
> The issues with internet-based covert communications systems cannot be fully solved piecemeal and will require an immense allocation of resources. “A patch won’t solve the problem,” said one of the former officials. “We’re not talking about billions of dollars, we’re talking about hundreds of billions of dollars to fix” these systems.
> 
> [...]
> 
> Former intelligence officials described longstanding tensions between the two directorates, as well as dysfunction within DS&T itself. DS&T’s budget has grown tremendously, said one former official, and the division was known for “wasting a lot money over the years.”


I've covered this before, but as more details come out, you get more and more insight into this world.  Waring divisions, those who get the internet but not operational tactics and those who don't understand the internet and technology.  You can see the lack of user research and the lack of focus on technology delivering for its users.

This story isn't over, and I think we'll see more of it in the year to come


## [Kubernetes being hijacked worldwide](https://blog.binaryedge.io/2018/12/06/kubernetes-being-hijacked-worldwide/)

[https://blog.binaryedge.io/2018/12/06/kubernetes-being-hijacked-worldwide/](https://blog.binaryedge.io/2018/12/06/kubernetes-being-hijacked-worldwide/)

> Another reason for our interest in this service is because we have seen increasing numbers being detected of Kubernetes being exposed to the internet.
> 
> But why is it a problem to expose Kubernetes to the internet?
> As is typical with our findings, lots of companies are exposing their Kubernetes API with no authentication; inside the Kubernetes cluster, small containers called Pods are ran. Essentially a pod represents a process inside the cluster.
> 
> By having this exposed, an attacker can not only see what is running on the Pods but also execute commands on the Pods themselves.


Like all technologies, exposing the administrative interfaces to the internet without authentication is a bad idea.


## [The Technology That Changed Air Travel](https://tryretool.com/blog/air-travel-software/amp/?__twitter_impression=true)

[https://tryretool.com/blog/air-travel-software/amp/?__twitter_impression=true](https://tryretool.com/blog/air-travel-software/amp/?__twitter_impression=true)

> Thankfully, there might be a solution — XML.


It’s astonishing that in this day and age this is actually still true, many people still use this interface paradigm. The number of critical systems that are still processed and managed by technology from decades ago is astonishing and frankly quite scary when you consider how much the security assumptions have changed in that time.  Computers are now interconnected in a myriad of ways that just weren't possible back when this was all created.

Thanksfully, XML is coming to our rescue!  I’ve always said that XML is like violence. If it’s not solving the problem, you clearly aren’t using enough of it!

I once worked with a Bloomberg XML API, it included an xml document with 40 <row> elements each of which had a CDATA block of exactly 80 characters. Just because they say it’s XML doesn’t mean it’s well designed


## [Nato nation Albania publicly posting sensitive intelligence data online | The Independent](https://www.independent.co.uk/news/world/europe/albania-intelligence-data-posted-online-nato-defence-military-finance-security-a8672446.html?amp&__twitter_impression=true)

[https://www.independent.co.uk/news/world/europe/albania-intelligence-data-posted-online-nato-defence-military-finance-security-a8672446.html?amp&__twitter_impression=true](https://www.independent.co.uk/news/world/europe/albania-intelligence-data-posted-online-nato-defence-military-finance-security-a8672446.html?amp&__twitter_impression=true)

> Last year the presidency posted online an unredacted copy of SHISH director Mr Bendo’s national identification card, which includes his home address and ID number, as part of a transparency initiative.
> 
> Earlier this year, a state agency reportedly was sent a list of 250 or so names of operatives serving in the country’s Military Intelligence unit.
> 
> The SHISH documents posted online date back to 2014, as Albania struggled to show the EU that it had shaken off its history of public corruption and was seeking to be more transparent and accountable as a step towards membership in the trading and currency bloc.
> 
> [...]
> 
> “The treasury registers on its online system all the bills and order of payments that are executed each day,” one official said on condition of anonymity.
> 
> “All the details that are given there, are because they were written in the order of payment by the institution itself. They should have not detailed the bills with such sensitive information.”
> 
> One longtime former officer of the Albanian intelligence service told The Independent that the culpability lay with SHISH itself, for handing sensitive information to finance ministry officials who lack security clearances.


Transparency is good, but getting the level right is hard...

There's some interesting tidbits in here, the average payout to a special informant must be around £1800 if the £18,000 for special payments is correct.

Quite where the training and responsibility lies for ensuring that the most secret and sensitive budget matters are handled, and ensuring that there is transparency on secret spending, without providing the entire world with operational details, that's a hard decision that should be made, and low level officials probably aren't qualified to make it by themselves.


## [2018 Year in Review - PornHub Insights](https://www.pornhub.com/insights/2018-year-in-review)

[https://www.pornhub.com/insights/2018-year-in-review](https://www.pornhub.com/insights/2018-year-in-review)

> Now we’re not saying that size matters, but 2018 was an impressively big year for Pornhub and its users. Visits to Pornhub totaled 33.5 billion over the course of 2018, an increase of 5 billion visits over 2017. That equates to a daily average of 92 million visitors and at the time of this writing, Pornhub’s daily visits now exceed 100 million. To put that into perspective, that’s as if the combined populations of Canada, Poland and Australia all visited Pornhub every day!
> 
> Pornhub’s servers served up 30.3 billion searches, or 962 searches per second. To make sure there was always fresh content to satisfy those searches, Pornhub’s amateurs, models and content partners uploaded an incredible 4.79 million new videos, creating over 1 million hours of new content to enjoy on the site. If you were to start watching 2018’s videos after the Wright brother’s first flight in 1903, you would still be watching them today 115 years later!


[Note, this is hosted on the pornhub.com domain name, and may contain words you might find offensive, but contains no adult images.  Your work firewall may however block the link]

PornHub is one of the biggest adult entertainment websites, and the data they hold and process is highly personal and sensitive to the individuals concerned.  These statistics show that PornHub is probably one of the biggest properties on the internet, and that they are sitting on a huge amount of data.

Of interest to those of us who consider threats and attackers, there's some good evidence about what people actually search for and are interested in, which varies from country to country, age bracket to age bracket.  Some of the top searches are probably good guesses for extortion, blackmail attempts and might show words that would be good to scan emails and files for if you are looking for evidence of employees hiding stuff.


## [Pornhub’s owner has more user data than Netflix or Hulu, here’s why — Quartz](https://qz.com/1407235/porn-sites-collect-more-user-data-than-netflix-or-hulu-this-is-what-they-do-with-it/?utm_source=reddit.com)

[https://qz.com/1407235/porn-sites-collect-more-user-data-than-netflix-or-hulu-this-is-what-they-do-with-it/?utm_source=reddit.com](https://qz.com/1407235/porn-sites-collect-more-user-data-than-netflix-or-hulu-this-is-what-they-do-with-it/?utm_source=reddit.com)

> While Netflix and Spotify might be more well-known household names, they know slightly less about their users than MindGeek does. Raustiala said that you can think of it as a spectrum, and MindGeek is furthest along in terms of using big data in a feedback loop.
> 
> This is because MindGeek relies heavily on “data-driven authorship,” or tailor-making content for viewers, to encourage more paying users. MindGeek owns several production companies of its own, which can harvest data analysis from MindGeek’s porn sites, which also means that customized porn videos can be created efficiently.
> 
> This production side has proved profitable for MindGeek. “We still believe very strongly in the paid subscription model. So much so, that we have invested heavily in the production side of the business and build several of the top names in Paysites from scratch,” Catherine Dunn, vice president of MindGeek, told Quartz. Sites that charge viewers, such as Brazzers, offer paid-for premium content. Dunn adds that over half of the company’s revenue is generated from such sites, and through “appealing to a demographic that prefers a premium experience with exclusive content.”


Note that PornHub is probably beating Netflix and Spotify at this game.  They are using the data analytics to understand the market, and to drive content creation that is tailored to the viewers wishes and desires.  It's long been said that the adult industry is the first to find, use and invest in technological solutions and so it's useful to see what they are doing and look forward to see how other industries will operate.   In this case PornHub, or Mindgeek is behind several content creation studios.  Netflix has started to release Netflix Studios content, and I'm sure Spotify is doing the same thing.  This is a perfect example of a platform play, of being the biggest content distributor to understand the end user, and then compete with the content creators using the data from that distribution model.


## [Alec Muffat on Twitter on AgeVerification](https://twitter.com/AlecMuffett/status/1073521349413490693)

[https://twitter.com/AlecMuffett/status/1073521349413490693](https://twitter.com/AlecMuffett/status/1073521349413490693)

> Let's spell this out: the UK Government, in pursuit of rapidly enabling the @BBFC to get stuck into #AgeVerification (AV), are resorting to snake-oil salesmanship in order to sidestep their egregious irresponsibility in not addressing data protection during the development of AV.


Given the vast and personally sensitive data that adult websites actually are able to determine about you, the idea that we want them to hold identity information on us is one that worries me greatly.  MindGeek are one of the leading proponents of AgeVerification, and are suggesting that they could produce a single adult identity product that any other adult website could use to perform the legally required AgeVerification process.  This would obviously also lead to them being in possession not just of the analytics of what content people like in aggregate, but able to build far more personal profiles on individuals based on the information provided in the age verification process.


## [The Equifax Data Breach [PDF]](https://oversight.house.gov/wp-content/uploads/2018/12/Equifax-Report.pdf)

[https://oversight.house.gov/wp-content/uploads/2018/12/Equifax-Report.pdf](https://oversight.house.gov/wp-content/uploads/2018/12/Equifax-Report.pdf)

> Equifax continued its incident investigation by conducting vulnerability testing of the ACIS application.
> 
> Equifax discovered flaws in the ACIS code rendering the system vulnerable to SQL injection and Insecure Direct Object Reference attacks.  The SQL injection flaw allows an attacker to inject or retrieve database information.  The Insecure Direct Object Reference flaw allows direct access to system data without requiring appropriate authentication or authorization.  The ACIS application had been tested for vulnerabilities in April 2017 after Equifax knew about the Apache Struts flaw and no unremediated vulnerabilities were found.  It is unclear why the April 2017 vulnerability testing and the July 30, 2017 vulnerability testing produced different results.
> 
> [...]
> 
> On a 7:00 am call with the initial Project Sierra group, Equifax’s Vulnerability Assessment team discussed the findings of the ACIS application review conducted on July 30.230 The team had identified an unexpected JSP file inserted into the ACIS application through SQL injection.
> 
> [...]
> 
> Equifax discovered code within the JSP file provided the avenue for the exploit. Following this 7:00 am call, a second unexpected JSP file was identified within the ACIS application.
> 
> [...]
> 
> Later on July 31, the Vulnerability Assessment team conducted a manual review looking for additional instances of Apache Struts on other servers.A vulnerable version of Apache Struts was discovered on a second server within the ACIS application. Equifax did not load a SSL certificate on this server, so it did not have visibility into the traffic to and from this server. Equifax uploaded a SSL certificate for this domain on August 3.246


This is really important reading.  This makes clear that there is no single root cause in this breach.  As in all incidents, there are many many failures that contribute to each other and cause this to fail.  You could say that there are flaws in the processes, divisions in the organisation and failures of accountability, but those are always the case in systems that haven't been breached.  The failures here are numerous and sometimes shocking.


