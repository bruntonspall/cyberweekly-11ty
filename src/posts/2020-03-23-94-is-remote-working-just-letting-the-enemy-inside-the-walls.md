---
title: "94 - Is remote working just letting the enemy inside the walls?"
date: 2020-03-23
description: "As pretty much every organisation in the UK and US has made urgent moves towards remote working, there are security and technology teams scrambling to enable remote access for their staff and to make it work.  VPN's are being overloaded, broadband connections saturated and terminal service licenses being exceeded in many organisations."
permalink: /is-remote-working-just-letting-the-enemy-inside-the-walls/
---

As pretty much every organisation in the UK and US has made urgent moves towards remote working, there are security and technology teams scrambling to enable remote access for their staff and to make it work.  VPN's are being overloaded, broadband connections saturated and terminal service licenses being exceeded in many organisations.

Security has to enable this kind of work as fast as possible, but when work is rushed, it can increase the risk of a security vulnerability.  The simple ones are things like deploying your technology wrongly, in such a way that it's easy to bypass or steal data.  But the more insidious issues is the putting online of systems that assumed that they were secure because nobody unauthorised had access.  We know that many criminal and government backed hacking groups are using the crisis as an opportunity to attack organisations through their weak spots.

Zero trust networking and similar ideas all flow from the central premise that you can securely and safely identify the personal accessing the service via some identity mechanism.  If you migrate online in a rush, you are far more likely to miss the features of your identity system that protect those services.  These critical blocks are important to get right, but really hard to do so in a hurry.

If you are moving to online productivity tooling, then you may well be exposing your current authentication infrastructure to the wider internet.  Do you have things in place to perform rate limiting on authentication attempts?  Do you have logging to know whether you are under attack and whether any credentials have been compromised?  Leading providers, such as Microsofts Azure AD has all of these features if you choose to enable them, but if you are simply putting your current infrastructure online, then you need to add these features.

The second thing is that current responses will lead, inevitably, to the growth of Shadow IT. Of people working around the IT department because it doesn't seem to meet their needs.  As someone in IT, you'll feel like you are doing all you can, but often we don't listen to our customers, who want something quick, something easy and something that just works.  If you give them something too restrictive, then they won't use it.  [This story over at reddit is a good example](https://www.reddit.com/r/msp/comments/fm6f4m/shadow_it_apocalypse/).  At this time, I think the most important thing that a cybersecurity team can be aware of is what is being used and installed.  Create a software amnesty.  Create a simple online form or slack channel where people can tell you what they are using to share documents, have video conferences and so on.  Don't rush to defend your existing IT offering, but assume that they've picked that for some reason (good or bad).  Instead you can use it to monitor what is happening in the organisation and decide where to offer your support.  Look at how to monitor it for bad actors, and see if you can enable healthy good practices on it.

The final thought is that this will soon(ish) be over, but many of the decisions that we make during this time will live on.  The more you know now, the better your chances of running a successful "post-covid cleanup" project, where you attempt to go find people who started using some new online tool and either migrate them to an officially sanctioned tool, or officially sanction the tool that they've found and roll it out to your enterprise.

## [Cybersecurity series: Who has access?](https://www.ultrasoc.com/blog-2-cybersecurity-series-access/)

[https://www.ultrasoc.com/blog-2-cybersecurity-series-access/](https://www.ultrasoc.com/blog-2-cybersecurity-series-access/)

> Nearly all of the garrison of the castle were at church in the town attending Mass. There were two guards left behind on the gate. A carpenter from the castle approached the guards saying that he needed to perform some work with two of his assistants. They were admitted and then immediately stabbed both guards. They then quickly let in the rest of their men, locking the gates behind them. When the garrison arrived back from church they were unable to gain access to the castle.
> 
> Unfortunately, the cleverness of this takeover was undermined by the fact that there were few stores in the castle and the Welsh were not prepared for it. It also upset the King of England, Henry IV, who immediately besieged the castle. Within three months, with no edible stores, the Welsh were starved out.
> 
> Why is this story particularly interesting in a technology context? This kind of strategy has many parallels with the way in which hackers often use guile and skill to attack seemingly impenetrable defences. The attack was planned to happen when the castle would be least defended and a way of gaining access via an authorized method had been found. The guards authenticated that the carpenter was real and he was clearly authorized to be there. The defenders were not correctly using their layers of defence within the castle and showed complacency and over-familiarity.
> 
> The story also gives a lesson for attackers looking to compromise and remain in a system. When defences have been subverted, one thing that more advanced attackers do in the technology world is what’s called ‘living off the land’. In this case the attackers were not able to sustain their takeover of the castle because they lacked those resources to hold out for a long time. Indeed, they’d misperceived the real situation. In the technology world, it is good practice to minimize in advance the things that an attacker can use once they’re “in the castle” or onto a system, such as software libraries not used for the core operation of a system. In the case of the story above, it was bad luck for the attackers that the garrison had so few usable supplies and food.


Modern security really hasn't changed much compared to the security of castles.  Social engineering, poor use of defences that would work far better if staff actually used them, and of course, the failure of attackers to actually take advantage of their successful attack.

(link via Jon)


## [Rail station wi-fi provider exposed traveller data - BBC News](https://www.bbc.co.uk/news/technology-51682280)

[https://www.bbc.co.uk/news/technology-51682280](https://www.bbc.co.uk/news/technology-51682280)

> The database, found online by a security researcher, contained 146 million records, including personal contact details and dates of birth.
> It was not password protected.
> 
> Named railway stations in screenshots seen by BBC News include Harlow Mill, Chelmsford, Colchester, Wickford, Waltham Cross, Norwich and London Bridge.
> 
> C3UK said it had secured the exposed database - a back-up copy that included about 10,000 email addresses - as soon as it had been drawn to their attention by researcher Jeremiah Fowler, from Security Discovery.
> 
> "To the best of our knowledge, this database was only accessed by ourselves and the security firm and no information was made publicly available," it said.
> "Given the database did not contain any passwords or other critical data such as financial information, this was identified as a low-risk potential vulnerability."
> 
> C3UK said it had chosen not to inform the data regulator, the Information Commissioner's Office (ICO), because the data had not been stolen or accessed by any other party.
> 
> The ICO confirmed to BBC News it had not been notified.


“To the best of our knowledge, nobody has accessed it” means nothing if they’re left it unprotected on an S3 bucket.  The chances that they had logging turned on is minimal.  The idea that they didn’t bother to inform the regulator because they didn’t think the breach was important, despite the fact that it contained personal data.  

Just plain not good enough.


## [Reviewing pull requests for security issues - Tradecraft - Medium](https://medium.com/tradecraft/reviewing-pull-requests-for-security-issues-c620f1671ca3)

[https://medium.com/tradecraft/reviewing-pull-requests-for-security-issues-c620f1671ca3](https://medium.com/tradecraft/reviewing-pull-requests-for-security-issues-c620f1671ca3)

> So let’s assume that you are doing pull requests and are running code reviews. In terms of security, what tangible things should you look for during your reviews?
> Making code more secure
> So, what to look for? Here are some things to look for while reviewing, and things you can do to make your codebase more secure during design and development:
> 
> * Check for good application of the principle of least privilege. Any new or modified functionality in a pull request should only be accessible by the type of user who explicitly requires it. For example, it’s not enough to confirm that an admin API endpoint can be accessed by administrator users; you should also confirm that normal or unauthenticated users cannot.
> * Similarly, if a new type of user is created, or a new set of permissions to access new functionality, double check what these users or permission grant access to, and confirm that they cannot be subverted or accessed by unauthorised users.
> * Check that whitelists are used to control user-submitted values. Blacklists are not a good solution: they require you to anticipate every possible malicious value that can be submitted. In almost every real-world situation, this is impossible — so it’s best not to try!


This is a good list of things to check for in code reviews (and there’s at the link).  Senior developers often check for code quality around the software issues that they are trained in, and very few software developers do any form of security checks.


## [Zoom’s forced app is irresponsible – Terence Eden’s Blog](https://shkspr.mobi/blog/2020/03/zooms-forced-app-is-irresponsible/)

[https://shkspr.mobi/blog/2020/03/zooms-forced-app-is-irresponsible/](https://shkspr.mobi/blog/2020/03/zooms-forced-app-is-irresponsible/)

> Here's the thing. Zoom supports web browsers. It just hides it really well. Only after attempting to download the app, and then waiting for a few seconds, do you get this tiny message saying you can join in the browser:
> 
> 
> That's annoying and, frankly, irresponsible. People urgently need to get on calls and Zoom is deliberately making it hard to do. WebRTC works. It works really well across browsers. I'm sure the Zoom app is marvellous. But it is useless if people can't install it.
> If you want to share a direct link to a call, use this:
> https://whatever.zoom.us/wc/join/123456?pwd=
> Replace the whatever with your company name and 123456 with your Zoom's conference ID.


With everyone it seems moving to Zoom, this is a tip worth knowing.  Lots of people can’t install applications on their corporate devices or phones, so knowing that there is a web client and how to get to it, is something worth being aware of.  I haven’t tried this to know how feature complete it is, but web based video conferencing is generally far more secure as well as more accessible.


## [Egress Filtering in Serverless Applications - The Startup - Medium](https://medium.com/swlh/egress-filtering-in-serverless-applications-25c2953a7290)

[https://medium.com/swlh/egress-filtering-in-serverless-applications-25c2953a7290](https://medium.com/swlh/egress-filtering-in-serverless-applications-25c2953a7290)

> That’s a pretty good definition. In serverless applications, your code can run in a “public” VPC that is wide open to the internet, or in a private VPC which has no internet access by default. What most developers fail to recognize is that any code, including the hundreds (if not thousands) of NPM packages you are consuming, can also connect to internet resources and transfer data. The worst part is you won’t know about it unless you block internet access or perform egress filtering. To say this is a bit worrisome is an understatement. It’s a major issue that needs to be addressed as part of your architecture.


Some interesting notes on how you can check and verify that the code that you write and run as a server less application only makes the network calls that you expect.  Running that code in public locations with no egress filters means that you don’t know what’s happening, and that’s a bad place to be.


## [#737140 Mass account takeovers using HTTP Request Smuggling on https://slackb.com/ to steal session cookies](https://hackerone.com/reports/737140)

[https://hackerone.com/reports/737140](https://hackerone.com/reports/737140)

> The bug chain is as follows:
> 
> 1. HTTP Request Smuggling CTLE to Arbitrary Request Hijacking (Poisoned Socket) on slackb.com
> 2. Request Hijack forces victim HTTP requests to instead use GET https://<URL> HTTP/1.1 on slackb.com
> 3. A request of GET https://<URL> HTTP/1.1 on the backend server socket results in a 301 redirect to https://<URL> with slack cookies (most importantly the d cookie)
> 4. Me with my Burp Collaborator steals victims cookies by using a collaborator server as the defined <URL> in the attack
> 5. Me (if I were evil) collects massive amounts of d session cookies and steals any/all possble Slack user/organization data from victim sessions


This is a lovely demonstration and write up of the HTTP Desync Attack (or HTTP Request Smuggling), community voted as the [best web hacking exploit of 2019](https://portswigger.net/research/top-10-web-hacking-techniques-of-2019).

The summary is that you send a request to a server that uses both Content Length and Transfer Encoding in the headers, where the front end and backend servers don’t agree on how to parse the headers.  This exploit shows exactly what can be achieved with this, steal the next users session cookie and then get access to all the data they can access, in this case, their entire slack session.


## [GOV.UK Notify is available for the public sector to use for emergency staff communications - Government Digital Service](https://gds.blog.gov.uk/2020/03/18/gov-uk-notify-is-available-for-the-public-sector-to-use-for-emergency-staff-communications/)

[https://gds.blog.gov.uk/2020/03/18/gov-uk-notify-is-available-for-the-public-sector-to-use-for-emergency-staff-communications/](https://gds.blog.gov.uk/2020/03/18/gov-uk-notify-is-available-for-the-public-sector-to-use-for-emergency-staff-communications/)

> With such high unpredictability around Coronavirus and the measures organisations may need to take to protect their staff and the public, it's critical we are prepared to quickly and reliably communicate important messages.
> 
> GOV.UK Notify is completely self-service. Teams in public sector organisations can create accounts and start sending emails and text messages within minutes.
> 
> You don’t need any technical expertise to use GOV.UK Notify. Simply create a templated message, upload a spreadsheet with contact details, and press ‘Send’. You can upload the spreadsheet in advance or when you’re ready to send.


This is what I meant last week about tools defining process.  The work that notify did to make the uploading and sending of notifications as seem less as possible has paid off in dividends as organisations realise they need to use a tool quickly and easily in these trying times.

Self service, simple and effective.


## [Russia deploying coronavirus disinformation to sow panic in West, EU document says - Reuters](https://www.reuters.com/article/us-health-coronavirus-disinformation/russia-deploying-coronavirus-disinformation-to-sow-panic-in-west-eu-document-says-idUSKBN21518F)

[https://www.reuters.com/article/us-health-coronavirus-disinformation/russia-deploying-coronavirus-disinformation-to-sow-panic-in-west-eu-document-says-idUSKBN21518F](https://www.reuters.com/article/us-health-coronavirus-disinformation/russia-deploying-coronavirus-disinformation-to-sow-panic-in-west-eu-document-says-idUSKBN21518F)

> Russian media in Europe have not been successful in reaching the broader public, but provide a platform for anti-EU populists and polarize debate, analysis by EU and non-governmental groups has shown.
> 
> The EEAS report cited riots at the end of February in Ukraine, a former Soviet republic now seeking to join the EU and NATO, as an example of the consequences of such disinformation.
> 
> It said a fake letter purporting to be from the Ukrainian health ministry falsely stated here were five coronavirus cases in the country. Ukrainian authorities say the letter was created outside Ukraine, the EU report said.
> 
> “Pro-Kremlin disinformation messages advance a narrative that coronavirus is a human creation, weaponized by the West,” said the report, first cited by the Financial Times.
> 
> It quoted fake news created by Russia in Italy - which is suffering the world’s second most deadly outbreak of coronavirus - alleging that the 27-nation EU was unable to effectively deal with the pandemic, despite a series of collective measures taken by governments in recent days.
> 
> The EEAS has also shared information with Slovakia over the spread of fake news accusing the country’s prime minister, Peter Pellegrini, of being infected with the virus and saying he may have passed on the infection to others at recent summits


Because of course the disinformation campaigns in place are going to continue despite the rise in the pandemic.  The distrust of the west and the lines to take have been set, and the systems will keep going regardless of what else is going on.


## [High-stakes security setups are making remote work impossible | Ars Technica](https://arstechnica.com/information-technology/2020/03/high-stakes-security-setups-are-making-remote-work-impossible/)

[https://arstechnica.com/information-technology/2020/03/high-stakes-security-setups-are-making-remote-work-impossible/](https://arstechnica.com/information-technology/2020/03/high-stakes-security-setups-are-making-remote-work-impossible/)

> The result may simply be far higher rates of viral transmission among government staffers who work in classified environments, says Jake Williams, himself a former NSA analyst. He describes his time at the NSA's outpost at Fort Gordon in Georgia as an open-floor-plan office. Staffers rarely called in sick, due to their mission's time sensitivity. Many worked in shifts, rotating 24/7 at the same desks. "You’re sitting down at a desk someone else sat at, typed at, coughed at," Williams says. "I have no idea what they're going to do, but I cannot fathom how it won’t spread like wildfire."


If you think working from home is hard where you work, just think of the difficulties of working when you work on national security systems.  Staff working in the most classified environments are simply incapable of working from home in almost all cases.  They’re down to skeleton staff, working shifts and putting themselves in danger to continue their missions.

There may well be answers to this, things that they can do to enable better remote working, ways that they can make their workforce more mobile.  But those answers and the changes necessary are going to take years if not decades to get in place.


## [Threat Actors: exploiting the pandemic – NCC Group Research](https://research.nccgroup.com/2020/03/19/threat-actors-exploiting-the-pandemic/)

[https://research.nccgroup.com/2020/03/19/threat-actors-exploiting-the-pandemic/](https://research.nccgroup.com/2020/03/19/threat-actors-exploiting-the-pandemic/)

> Threat actors attempting to capitalize on current events, pandemics and global anxiety is nothing new, as was previously seen with malicious campaigns related to the 2019 climate strikes and demonstrations as well as the 2018 FIFA World Cup tournament.
> 
> By relying on basic social engineering – an attack technique that takes advantage of human traits such as curiosity, trust and greed in order to obtain confidential information or to have the victim perform a certain action – it is suffice to say that certain threat actors (both criminal and nation state) are exploiting these unprecedented times for various nefarious means.
> 
> Although we observe threat actors shifting tactics, we don’t necessarily observe an uptick in attacks going on. Primarily, we observe existing threat actors leverage the COVID-19 outbreak in their campaigns, e.g. by naming their spam documents with a variety of Corona virus themed lures or by registering new domains were the URLs contain COVID-19 specific words. Additionally, the branding of trusted organizations (for example the World Health Organization (WHO)) is abused in order to build credibility and trust in order to have people, for example, open malicious attachments or web pages.


Lots of continuing actions by existing teams who are using the same techniques, tools and procedures as they’ve always used, but using COVID-19 or CoranaVirus in their messaging.  People’s thirst for knowledge in this environment is liable to cause them to be more gullible and makes attackers jobs easier


## [Threat Intel Update | Cyber Attacks Leveraging the COVID-19/CoronaVirus Pandemic - SentinelLabs](https://labs.sentinelone.com/threat-intel-update-cyber-attacks-leveraging-the-covid-19-coronavirus-pandemic/)

[https://labs.sentinelone.com/threat-intel-update-cyber-attacks-leveraging-the-covid-19-coronavirus-pandemic/](https://labs.sentinelone.com/threat-intel-update-cyber-attacks-leveraging-the-covid-19-coronavirus-pandemic/)

> At Sentinel Labs, we have been closely tracking adversarial behavior as it pertains to COVID-19/Coronavirus. To date, we have observed a significant number of malware campaigns, spam campaigns, and outright scams that are preying on the fears and uncertainties of the global population.
> 
> Over the last few months we have seen aggressive use of COVID-19/Coronavirus as a lure all over the spectrum of sophistication. Campaigns range from run-of-the mill scams (selling supplies for BTC via .onion sites) to non-targeted spam campaigns (primarily for credential harvesting). We have even observed enterprising criminals selling COVID-19-specific malware/phishing ‘kits’ which can be customized and leveraged in downline attacks for a very small investment (less than $1000 USD). Nothing is sacred, either: not even the tragic death of NBA star Kobe Bryant, whose image was used to lure fans into downloading malicious desktop backgrounds. 
> 
> Indeed a picture (in this case an interactive map) is worth a thousand words, with attackers offering up the ability to load payloads to victims that visit this nefarious coronavirus spread map


This is a good overview of the mass of different campaigns out there, from simple spam and fraudsters taking advantage to full on malware campaigns.


## [Hackers are targeting hospitals crippled by coronavirus | WIRED UK](https://www.wired.co.uk/article/coronavirus-hackers-cybercrime-phishing)

[https://www.wired.co.uk/article/coronavirus-hackers-cybercrime-phishing](https://www.wired.co.uk/article/coronavirus-hackers-cybercrime-phishing)

> As the total number of global cases of Covid-19 has swelled above 250,000, hackers have increased their activity as they look to capitalise on the crisis. “We’re seeing concerted targeting against manufacturing, pharmaceutical, travel, healthcare and insurance,” explains Sherrod DeGrippo, a senior director in threat research and detection at cybersecurity firm Proofpoint says. “When I say manufacturing, a lot of times it seems to be targeted against a subset of manufacturing, which is manufacturers that create hospital beds, medical equipment, those things you would associate with healthcare.”


The rise in attacks on the critical infrastructure during a pandemic shows that many criminal organisations do not possess any ethics.  The pandemic results will generally show that there’s no such thing as honourable thieves.  These are people who will see any opportunity for profit and don’t care who gets hurt in the meantime.


