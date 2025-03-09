---
title: "24 - How can we set a security strategy if we don't know what's going on?"
date: 2018-11-03
description: "Lots of the stories this week show that organisationally, senior leaders are out of touch with the reality of the security strategy that they write or sponsor."
permalink: /how-can-we-set-a-security-strategy-if-we-don-t-know-what-s-going-on/
---

Lots of the stories this week show that organisationally, senior leaders are out of touch with the reality of the security strategy that they write or sponsor.

Whether it be a policy that requires users to not browse adult websites, that everyone ignores, or critical voices inside your organisation not floating up because of a culture of good news.  It's hard for leaders to actually know what is going on, and whether their direction or strategies are having any effect.

I'm a big believer that the direction needs to be set from above, but the how we get there has to come from the teams actually doing the delivery.  A strategy that focuses on doing the basics first and foremost, and putting in place effective reporting and analysis is critical.  You need objectives and measurable achievements so that you know what difference you are making.

## [The Rodney Brooks Rules for Predicting a Technology’s Commercial Success - IEEE Spectrum](https://spectrum.ieee.org/at-work/innovation/the-rodney-brooks-rules-for-predicting-a-technologys-commercial-success)

[https://spectrum.ieee.org/at-work/innovation/the-rodney-brooks-rules-for-predicting-a-technologys-commercial-success](https://spectrum.ieee.org/at-work/innovation/the-rodney-brooks-rules-for-predicting-a-technologys-commercial-success)

> The answer, in a word, is experience. The difference between the possible and the practical can only be discovered by trying things out. Therefore, even though the physics suggests that a thing will work, if it has not even been demonstrated in the lab you can consider that thing to be a long way off. If it has been demonstrated in prototypes only, then it is still distant.


This is a good lens by which to assess “future technologies” not just in the large (such as self driving cars) but in the small, such as Software Defined Networking or smart contracts. 

Is your vendor telling you that a technology will save you money and is the future to bet on.  Asking yourself whether it has been demonstrated in a lab, in prototypes, or whether the fundamentals of the technology are in place and used everyday already will help you assess vendor claims.


## [The CIA's communications suffered a catastrophic compromise](https://finance.yahoo.com/news/cias-communications-suffered-catastrophic-compromise-started-iran-090018710.html)

[https://finance.yahoo.com/news/cias-communications-suffered-catastrophic-compromise-started-iran-090018710.html](https://finance.yahoo.com/news/cias-communications-suffered-catastrophic-compromise-started-iran-090018710.html)

> The losses could have stopped there. But U.S. officials believe Iranian intelligence was then able to compromise the covert communications system. At the CIA, there was “shock and awe” about the simplicity of the technique the Iranians used to successfully compromise the system, said one former official.
> 
> In fact, the Iranians used Google to identify the website the CIA was using to communicate with agents. Because Google is continuously scraping the internet for information about all the world’s websites, it can function as a tremendous investigative tool — even for counter-espionage purposes. And Google’s search functions allow users to employ advanced operators — like “AND,” “OR,” and other, much more sophisticated ones — that weed out and isolate websites and online data with extreme specificity.
> 
> According to the former intelligence official, once the Iranian double agent showed Iranian intelligence the website used to communicate with his or her CIA handlers, they began to scour the internet for websites with similar digital signifiers or components — eventually hitting on the right string of advanced search terms to locate other secret CIA websites. From there, Iranian intelligence tracked who was visiting these sites, and from where, and began to unravel the wider CIA network


I think I first covered this back in CyberWeekly #13, with a report from ForeignPolicy on the breach of the CIA covert informant network.  But there are more details in this Yahoo report, indicating that it was broken via Google Dorking, which is to say, they simply googled for the identifiers that gave away the websites.

One of the concerning things is the reflection of our own systems. There was a technical person who identified the flaws early, but wasn't listened to because the organisation resists change.  How often have we found senior members of organisations confident in their organisations security, while talking to the analysts on the ground, you get a different story?


## [Recovery from Command-and-Control: A Twelve-Step Program | Humanistic Systems](https://humanisticsystems.com/2014/07/12/recovery-from-command-and-control-a-twelve-step-program/)

[https://humanisticsystems.com/2014/07/12/recovery-from-command-and-control-a-twelve-step-program/](https://humanisticsystems.com/2014/07/12/recovery-from-command-and-control-a-twelve-step-program/)

> Command-and-control gives management the illusion that they are in control of the work and the workers, and that this control leads to effectiveness. Distance between decision making about the work and the work itself makes decision makers think that when things go right, it is because they are being done as specified: by the book. When things go wrong, it is because people did not do their job: they screwed up.


This is an old article, but relevant I think.  Command and control organisations often struggle with scale.  Those at the top cannot possibly know what is going on at the bottom, but are expected to make decisions and give commands to those people.

This asymmetry of information is essentially what all project management is about, trying to get information from the bottom up to the top in the most efficient and effective way, and I don't think we have a good solution yet.


## [China's Five Steps for Recruiting Spies in the US | WIRED](https://www.wired.com/story/china-spy-recruitment-us/)

[https://www.wired.com/story/china-spy-recruitment-us/](https://www.wired.com/story/china-spy-recruitment-us/)

> Sifting through more than a dozen of the major cases that have targeted Westerners, though, provides an illuminating window into how China recruits its spies. The recruitment follows a well-known five-step espionage road map: Spotting, assessing, developing, recruiting, and, finally, what professionals call “handling.”


This is an interesting read and insight into human intelligence operations, and how they can be used to aid and advise technical intelligence operations.


## [When Trump Phones Friends, the Chinese and the Russians Listen and Learn - The New York Times](https://www.nytimes.com/2018/10/24/us/politics/trump-phone-security.html)

[https://www.nytimes.com/2018/10/24/us/politics/trump-phone-security.html](https://www.nytimes.com/2018/10/24/us/politics/trump-phone-security.html)

> Mr. Trump’s aides have repeatedly warned him that his cellphone calls are not secure, and they have told him that Russian spies are routinely eavesdropping on the calls, as well. But aides say the voluble president, who has been pressured into using his secure White House landline more often these days, has still refused to give up his iPhones. White House officials say they can only hope he refrains from discussing classified information when he is on them.


This is interesting reporting, because none of the analysts that I read can really come up with an actual attack that would reliabily and stealthily allow a foreign power to actually eavesdrop on calls on US soil.

Some people poked at SS7, but although it is notoriously weak, you just know that within the US borders, any weird SS7 hacks to intercept phone calls are going to be detected.  A foreign power might get away with it once, but for regular eavesdropping, it's both too noisy, and too difficult to maintain.

The second idea is that the phone itself is implanted with malware, whcih is the most likely attack, but it's also quite noisy and one would hope that there are good defences against this.

Instead this feels like a story of jilted security and risk advisors, who rabbit the traditional line "foreign powers could intercept that phonecall" without being able to actually justify it, leaking the non-compliance of their senior official to the press to increase the pressure for their desired solution.

I fail to see any concrete evidence that LTE mobile phones, as used in the US, are easy to intercept and tap in the manner described in the story.


## [Five Ways to Tackle Digital Transformation Without Downtime - InformationWeek](https://www.informationweek.com/strategic-cio/it-strategy/five-ways-to-tackle-digital-transformation-without-downtime/a/d-id/1332895)

[https://www.informationweek.com/strategic-cio/it-strategy/five-ways-to-tackle-digital-transformation-without-downtime/a/d-id/1332895](https://www.informationweek.com/strategic-cio/it-strategy/five-ways-to-tackle-digital-transformation-without-downtime/a/d-id/1332895)

> Taking a phased approach to reduce risk. Rather than “rip and replace,” we approached this transformation in a more elegant way to mitigate risk of outages. We wanted to roll out the new platform while isolating failures and prove it was working correctly. It was important to release a limited minimum viable product (MVP) into production early to get critical and realistic architectural and operational feedback, then iterate.


Another reminder. Regular releases reduces risk. 
Phased approaches of releasing smaller bits of functionality and testing it are significantly less risky. But I’ve yet to see a risk assessment process that is designed for assessing incremental changes in a simple, clear and easy way. 


## [October 21 post-incident analysis | The GitHub Blog](https://blog.github.com/2018-10-30-oct21-post-incident-analysis/)

[https://blog.github.com/2018-10-30-oct21-post-incident-analysis/](https://blog.github.com/2018-10-30-oct21-post-incident-analysis/)

> This incident has led to a shift in our mindset around site reliability. We have learned that tighter operational controls or improved response times are insufficient safeguards for site reliability within a system of services as complicated as ours. To bolster those efforts, we will also begin a systemic practice of validating failure scenarios before they have a chance to affect you. This work will involve future investment in fault injection and chaos engineering tooling at GitHub.
> 
> 


This was an interesting outage description but this finding is the most interesting part. 
Instead of saying they need more control and better operational processes, GitHub have said that they need to reherse more, to test failures more and build better resilience in place. 

We should consider this for security events but also remember that availability is a security concern. How do we respond to such outages and how do we help?


## [Report reveals one-dimensional support for two-factor authentication – Naked Security](https://nakedsecurity.sophos.com/2018/11/02/report-reveals-one-dimensional-support-for-two-factor-authentication/)

[https://nakedsecurity.sophos.com/2018/11/02/report-reveals-one-dimensional-support-for-two-factor-authentication/](https://nakedsecurity.sophos.com/2018/11/02/report-reveals-one-dimensional-support-for-two-factor-authentication/)

> Dashlane also said that clarity was an issue in many websites. CEO Emmanuel Schalit said:
> 
> Through the course of our research we found that information on 2FA is often presented in a way that is unclear, making it difficult for consumers to confirm 2FA offerings. In fact, our researchers were forced to omit a large number of popular websites from our testing simply because the sites don’t provide any straightforward or easily accessible information about their 2FA offerings.


This is a bit disappointing.  There are lots of sites that do support 2FA, but don't nudge their users into using it, enabling it, or getting used to it.

I know that users sometimes find the experience weird, and we need to work better to make it easier (my new YubiKey is lovely for example), but we also need users to start using hardware tokens either as a second factor, or as I keep saying, as the primary factor in place of a password if possible.


## [USGS IT SECURITY VULNERABILITIES [PDF]](https://www.oversight.gov/sites/default/files/oig-reports/ManagementAdvisory%20_USGSITSecurityVulnerabilities_101718_0.pdf)

[https://www.oversight.gov/sites/default/files/oig-reports/ManagementAdvisory%20_USGSITSecurityVulnerabilities_101718_0.pdf](https://www.oversight.gov/sites/default/files/oig-reports/ManagementAdvisory%20_USGSITSecurityVulnerabilities_101718_0.pdf)

> We found that - knowingly used U.S. Government computer systems to access unauthorized internet web pages. We also found that those unauthorized pages hosted malware.
> 
> The malware was downloaded to - Government laptop, which then exploited the USGS ' network. Our digital forensic examination revealed that- had an extensive history of visiting adult pornography websites. Many of the 9,000 web pages - visited route through websites that originated in Russia and contained malware. Our analysis confirmed that many of the pornographic images were subsequently saved to an unauthorized USB device and personal Android cell phone connected to - Government-issued computer. We found that - personal cell phone was also infected with malware. 


I've seen and heard analysis that asks how this can happen, how someone can browse so much adult content.  I wondered whether this was a US Government laptop that was being used at home, but had a VPN installed, so always dialled back to the corporate network.

Also, a reminder that you should start with the basics.  This doesn't look like a sophisticated or intentional attack, this is simply drive by download malware, aimed to get as many computers as possible.


## [Snakes in the grass! Malicious code slithers into Python PyPI repository – Naked Security](https://nakedsecurity.sophos.com/2018/10/30/snakes-in-the-grass-malicious-code-slithers-into-python-pypi-repository/)

[https://nakedsecurity.sophos.com/2018/10/30/snakes-in-the-grass-malicious-code-slithers-into-python-pypi-repository/](https://nakedsecurity.sophos.com/2018/10/30/snakes-in-the-grass-malicious-code-slithers-into-python-pypi-repository/)

> In this case, a malicious actor created a PyPI package called colourama. It exploits a common spelling difference between US and British English to impersonate a legitimate PyPI package called colorama, which enables developers to produce colored terminal text in Microsoft Windows.
> 
> The name change is subtle, and developers may be fooled into installing the wrong package. As it installs, it creates a malware dropper designed to exploit Windows PCs. The dropper downloads malware written in Microsoft’s VBScript language.
> 
> The VBScript executes upon installation, adding a Windows registry entry to run it whenever the user logs into the computer. The malicious code then runs in the background and scans the Windows clipboard every 500ms.


This astonishes me in it's naievity.   A setup.py that is run when a python package is installed can do almost anything the user could, and it's still common to see instructions to tell users to run pip under sudo.

So why write a dropper with VisualBasic if you are already writing python code?  I can only assume that the malware author was not able to write their own exploits and didn't have access to a python one.


## [This Election Offered A Window Into WhatsApp's Wild, Sometimes Fact-Free World](https://www.buzzfeednews.com/article/ryanhatesthis/no-one-knows-how-bad-fake-news-is-on-whatsapp-but-if)

[https://www.buzzfeednews.com/article/ryanhatesthis/no-one-knows-how-bad-fake-news-is-on-whatsapp-but-if](https://www.buzzfeednews.com/article/ryanhatesthis/no-one-knows-how-bad-fake-news-is-on-whatsapp-but-if)

> Fabrício Benevenuto, an associate professor of computer science at the Universidade Federal de Minas Gerais, and creator of the WhatsApp Monitor, told BuzzFeed News that the tool gathers data across 350 politically motivated WhatsApp groups. It pulls in images, videos, audio files, links, and text posts.
> 
> 
> eleicoessemfake.dcc.ufmg.br
> A sample of one of the versions of the WhatsApp chain letter warning voters not to wear Bolsonaro gear to polling stations.
> 
> Benevenuto said that attempting to track misinformation on WhatsApp has been extremely hard, due to the social network's encryption, but he said the fake news his monitor collected became increasing politicized as the election drew closer.


This feels like a really tough problem.  WhatsApp is very useful, I use it to coordinate groups with my friends, as well as school parent groups.  Misinformation that is shared, probably out of good intentions, into those groups probably gets copied around a lot, and is really hard to track.

WhatsApp won't be the only private network that has this problem.  I'm sure Telegram, Signal and other "end-to-end encrypted" messengers must have a similar problem as well.


## [How can we stop being cyber idiots? - BBC News](https://www.bbc.co.uk/news/technology-45953238)

[https://www.bbc.co.uk/news/technology-45953238](https://www.bbc.co.uk/news/technology-45953238)

> Humans are often the weakest link in the chain when it comes to computer security. So how can we stop doing silly things that play into the hands of cyber criminals?
> 
> When you ring IT support, you know the geek on the other end of the line thinks you're an idiot. It's the heavy sigh and patronising tone that give it away.
> 
> In fact, they have an acronym for us - PEBKAC. It stands for Problem Exists Between Keyboard And Chair. That's you and me.
> 
> And before you get on your high horse full of indignation, ask yourself: when did I last back up my data? How many online accounts do I use the same password for? How many times have I clicked on a link in an email without really knowing who sent it?
> 
> Porn-loving US official spreads malware to government network
> Every year we're reminded how dumb we are when it comes to choosing passwords.


This was probably the worst article I've read in the last year.  It's offensive and wrong on almost every single front.  Most of the linked "solutions" won't make anything better because if you don't treat your users as your first line of defence and value them, then you've already lost and nothing else will help.

This attitude towards our users has to stop


