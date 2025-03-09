---
title: "114 - Continuous Learning"
date: 2020-08-09
description: "One of the reasons that I write this newsletter is because it scratches my own itch.  I read a lot of articles, blogposts and reddit forums pretty much constantly.  I lose track of which ones I've read, and I found myself in meetings with people where someone would say \"Oh, did you see thing X\" and my response was normally \"Oh yeah, I read about that weeks ago\".  Someone suggested that I start tracking what I read, and try to, you know, actually tell others the interesting tidbits that I read to be helpful."
permalink: /continuous-learning/
---

One of the reasons that I write this newsletter is because it scratches my own itch.  I read a lot of articles, blogposts and reddit forums pretty much constantly.  I lose track of which ones I've read, and I found myself in meetings with people where someone would say "Oh, did you see thing X" and my response was normally "Oh yeah, I read about that weeks ago".  Someone suggested that I start tracking what I read, and try to, you know, actually tell others the interesting tidbits that I read to be helpful.

This is all part of my attitude that I need to be constantly learning.  I've been very lucky in my career to work alongside some amazing people and teams, and I've always had the view that I should be learning far more from my coworkers than they should from me.

But learning is hard.  There's so many resources available these days, but we need to take time out to do it.  I read newsletters when I have time, and I have time cut out in my diary to sit and try to read all the queued up stuff in my newsletters, but even finding that time can be hard.  One of the reasons that I like conferences is that you can specifically cut out the time in your diary, and that relieves a lot of the work pressure.  

Of course with so many conferences going virtual, along with older conferences putting their material up online, you can now easily watch sessions about almost anything.  

I was planning to go to DefCon this year, it would have been my first time, and I was looking forward to it.  But Covid, along with life and job changes mean that I've failed to block the time out in my diary.  But if you can, do yourself a favour and book out a day or two in your diary to just sit and watch conference sessions, read all those back issues of CyberWeekly you've not read, and just take some time to learn.

## [GitHub - apple/password-manager-resources: A place for creators and users of password managers to collaborate on resources to make password management better.](https://github.com/apple/password-manager-resources)

[https://github.com/apple/password-manager-resources](https://github.com/apple/password-manager-resources)

> The Password Manager Resources project exists so creators of password managers can collaborate on resources to make password management better for users. Resources currently consist of data, or "quirks", as well as code.
> 
> "Quirk" is a term from web browser development that refers to a website-specific, hard-coded behavior to work around an issue with a website that can't be fixed in a principled, universal way. In this project, it has the same meaning. Although ideally, the industry will work to eliminate the need for all of the quirks in this project, there's value in customizing behaviors to ensure better user experience. The current quirks are:
> 
> Password Rules: Rules to generate compatible passwords with websites' particular requirements.
> Websites with Shared Credential Backends: Groups of websites known to use the same credential backend, which can be used to enhance suggested credentials to sign in to websites.
> Change Password URLs: To drive the adoption of strong passwords, it's useful to be able to take users directly to websites' change password pages.
> Websites Where 2FA Code is Appended to Password: Some websites use a two-factor authentication scheme where the user must append a generated code to their password when signing in.


This is a lovely little tool if you are building a password manager, or if you simply want to contribute your weird set of password complexity rules (must contain upper case, lower case, an emoji and be in iambic pentameter).

The nice thing about this is that I discovered that there is [a standard for defining password complexity rules](https://developer.apple.com/password-rules/) as well.  The password field in Safari supports this, and means that iPhones and Safari will autogenerate passwords that meet the rules. 


## [LeakLooker GUI — Discover, browse and monitor database/source code leaks.](https://www.offensiveosint.io/leaklooker-gui-discover-browse-and-monitor-database-source-code-leaks/)

[https://www.offensiveosint.io/leaklooker-gui-discover-browse-and-monitor-database-source-code-leaks/](https://www.offensiveosint.io/leaklooker-gui-discover-browse-and-monitor-database-source-code-leaks/)

> Almost every week, new security incidents coming up violating privacy of millions of people. Banks, big corporations, army and many other industries have suffered or lost their records or intellectual properties due to misconfiguration of various services like Elastic, Mongo database, Gitlab or Rsync. Many security firms and single researchers dedicated their work to find unprotected database and follow responsible disclosure to prevent abusing exposed data by bad guys.
> 
> The idea for both — white and black hats is the same, detect critical information leak (PII, credit cards, IP etc.), analyze the data and inform the owner, if you want to do the right thing. Methods also can’t be much different, use of Binary Edge and other search engine for internet connected device or actively scan the Internet to look for specific ports and service. The things that differ are resources and capabilities, single researchers has limited time and resources to find valuable data but companies with their constant monitoring can spot interesting finding from the crowd easier. Idea behind old LeakLooker script was to find as much potential leaking services as possible and help people that want to check what data could be exposed.


This is a nice tool for searching online and looking for misconfigured databases and other services.  You can use it to scan your own IP ranges, your systems and to search for your organisations content, meaning that your security team should find it before the hackers do.


## [JIRA is an antipattern | TechCrunch](https://techcrunch.com/2018/12/09/jira-is-an-antipattern/)

[https://techcrunch.com/2018/12/09/jira-is-an-antipattern/](https://techcrunch.com/2018/12/09/jira-is-an-antipattern/)

> Allow me to propose something shocking and revolutionary: prose. Yes, that’s right; words in a row; thoughtfully written paragraphs. I’m not talking about huge requirements documents. I’m talking about maybe a 10-page overview describing the vision for the entire project in detail, and a six-page architectural document explaining the software infrastructure — where the city’s water, sewage, power, subways and airports are located, and how they work, to extend the metaphor. When Amazon can, famously, require six-page memos in order to call meetings, this really doesn’t seem like too much to ask.
> 
> Simply ceasing to treat JIRA as the primary map and model of project completion undercuts a great deal of its implicit antipatternness. Use it for tracking iterative development and bug fixes, by all means. It’s very good at that. But it is a tool deeply ill-suited to be the map of a project’s overall vision or infrastructure, and it is never the source of truth — the source of truth is always the running code. In software, as in art, the micro work and the macro vision should always be informed by one another. Let JIRA map the micro work; but let good old-fashioned plain language describe the macro vision, and try to pay more attention to it.


This entire article, which I agree with incidentally, could simply be replaced with a simple maxim.  Don't let a tool define your process.

Tools act as a strong guiding mechanism for enforcing processes and standards on your teams.  If you want your teams to work a certain way, configuring JIRA to that standard will strongly encourage teams to work that way.

A [tweet this week](https://twitter.com/bruntonspall/status/1291764924759322626?s=20) by [Mark Delgarno, one of the smartest thinkers about agile I know](https://medium.com/@markdalgarno), talked about the overuse of standards to lock down and prevent healthy experimentation.  I see this reflected in this article.  If you use Jira to set a software development methodology standard, you are making it hard for teams to experiment with their development process.  

On the other hand, it's only really experimentation (in the scientific sense), if you have a hypothesis, measure the results and control for changes to see if they make a difference.  Too many agile teams I see are endless tweakers to their process without any guiding force other than the cult of personality.  Allowing every team to simply decide their own rules isn't experimentation, it's enabling chaos that is difficult to track, difficult to determine if it's successful and makes mini-silos in your organisation that it's hard for people to move from one to another.

But at the root of it all, is the problem that JIRA is simply a tool, and you need more thinking about how you work than the tool you use.  Decide how you want to work, how you want to measure progress and how you will coordinate between teams, and then pick a tool that works for that process.


## [Unwanted Truths: Inside Trump’s Battles With U.S. Intelligence Agencies - The New York Times](https://www.nytimes.com/2020/08/08/magazine/us-russia-intelligence.html?action=click&module=Top%20Stories&pgtype=Homepage)

[https://www.nytimes.com/2020/08/08/magazine/us-russia-intelligence.html?action=click&module=Top%20Stories&pgtype=Homepage](https://www.nytimes.com/2020/08/08/magazine/us-russia-intelligence.html?action=click&module=Top%20Stories&pgtype=Homepage)

> Under Trump, intelligence officials have been placed in the unusual position of being pressured to justify the importance of their work, protect their colleagues from political retribution and demonstrate fealty to a president. Though intelligence officials have been loath to admit it publicly, the cumulative result has been devastating. Representative Sean Patrick Maloney, a Democrat on the House Intelligence Committee, compared the O.D.N.I.’s decline under Trump to that of the Justice Department, where “they have, step by step, set out to destroy one of the crown jewels of the American government,” he told me. “And they’re using the same playbook with the intelligence community.”
> 
> The O.D.N.I.’s erosion has in turn shaped the information that flows out of the intelligence community to the White House — or doesn’t. The softening of Key Judgment 2 signified a sobering new development of the Trump era: the intelligence community’s willingness to change what it would otherwise say straightforwardly so as not to upset the president. “To its credit, the intelligence community resisted during the earlier part of the president’s term,” Representative Adam Schiff, the Democratic chairman of the House Intelligence Committee, told me. “But by casting out Dan Coats and then Maguire, and replacing them with loyalists, I think over time it’s had the effect of wearing the intelligence community down, making them less willing to speak truth to power.”


This is a great long read about the relationship between the intelligence community and the president.

One of the interesting things in here is just how tentative that relationship is, and how reliant it is on unspoken norms and processes.  The intelligence machinery is somewhat predisposed to think of itself as the all knowing, all correct oracle of wisdom and cannot conceive that the president wouldn't eagerly grasp at all of the intelligence nuggets that it produces.

Equally, the point of intelligence analysts is that they produce analytical views on all the information available to them, and that they are independent of political will and judgement.  Increasing interference in that process means that the US intelligence community will have to develop different governance processes to respond to the change in the balance of power.


## [Addressing government legacy IT to be ‘a key focus of spending review’ | PublicTechnology.net](https://www.publictechnology.net/articles/news/addressing-government-legacy-it-be-%E2%80%98-key-focus-spending-review%E2%80%99)

[https://www.publictechnology.net/articles/news/addressing-government-legacy-it-be-%E2%80%98-key-focus-spending-review%E2%80%99](https://www.publictechnology.net/articles/news/addressing-government-legacy-it-be-%E2%80%98-key-focus-spending-review%E2%80%99)

> A major objective of the upcoming Comprehensive Spending Review will be to address issues caused by the continuing prevalence of legacy technology – which accounts for half of central government’s IT spending.
> 
> The review, which will set out detailed budgets for each department for the next three to four years, is due to take place around November. It is the first full CSR to take place in five years, with the process having been delayed by the urgency of, first, government’s Brexit preparations and, latterly, by the coronavirus pandemic.
> 
> In a speech delivered this week at an event hosted by think tank Onward, chief secretary to the Treasury Steve Barclay said that “a key focus of the spending review will be addressing legacy IT”.
> 
> This issue has often not been tackled by individual departments, he said, because “the average tenure of a secretary of state is less than two years – so, it’s no surprise that issues such as legacy IT are often deprioritised in favour of the new and exciting”.
> 
> But the importance of moving away from ageing technology is demonstrated by the fact that “currently around half of central government IT spend is on servicing legacy IT”, according to Barclay.
> 
> “Such an approach is not only expensive,” he added. “It also poses cybersecurity risk, and prevents agile ways of working and cross departmental interaction. It also obstructs the use of new innovative IT solutions and the sharing of data more openly.”


The cybersecurity risk of legacy systems is hard to quantify, but at a minimum, the fact that the UK Government defines legacy systems as things that are difficult to change or update, you can imagine some fairly modern systems that are not being patched, maintained or improved, and that's a security hole by itself.


## [The RedMonk Programming Language Rankings: June 2020 – tecosystems](https://redmonk.com/sogrady/2020/07/27/language-rankings-6-20/)

[https://redmonk.com/sogrady/2020/07/27/language-rankings-6-20/](https://redmonk.com/sogrady/2020/07/27/language-rankings-6-20/)

> With that preamble, here are the most important takeaways from this edition of the rankings.
> 
> Python (0): Ironically, the most notable “winner” in this quarter’s rankings is Python, which did not move at all. But in assuming sole control of the number two spot in our rankings, Python is the first non-Java or JavaScript language ever to place in the top two of these rankings by itself, and would not have been the obvious choice for that distinction in years past. Underrated and often overlooked, the versatility of the language remains both its calling card and the basis for its continued strength. Much like Perl in its heyday, Python is the glue for thousands of small projects and the basis for countless personal scripts, including a few that retrieve data for these rankings. But it continues to find its footing amongst emerging and expanding categories, whether that’s data science a few years ago or GPT-3 work today. As long as it remains a language of first resort, it will continue to perform well in these rankings.


The RedMonk programming language rankings are always worth a read, but the thing I find interesting is that the results often somewhat defy normal sense.

Python is my personal favourite language, and I can totally see how it's popular on github, but also has an active community on stack overflow because of its versatility.  However, I'd still be loath to use it as the primary language on a really big system, it doesn't really hold up well as an "enterprise language".  Instead it's rise and use is in the field of small utilities, microservices and of course, the science and data science community who use it a lot.


## [Announcing the Expansion of the Clean Network to Safeguard America’s Assets - US Secretary of State](https://www.state.gov/announcing-the-expansion-of-the-clean-network-to-safeguard-americas-assets/)

[https://www.state.gov/announcing-the-expansion-of-the-clean-network-to-safeguard-americas-assets/](https://www.state.gov/announcing-the-expansion-of-the-clean-network-to-safeguard-americas-assets/)

> Clean Carrier: To ensure untrusted People’s Republic of China (PRC) carriers are not connected with U.S. telecommunications networks.
> [...]
> Clean Cloud: To prevent ... from being stored and processed on cloud-based systems accessible to our foreign adversaries through companies such as Alibaba, Baidu, and Tencent.


(Joel) Aside from First Amendment issues, I can see this continuing a fractured internet trend. The Great Wall has existed for some time, and Russian attempts to ensure in-country networking is not reliant on global systems (nameservers, routing etc) has already doubled-down on that.

I would not be at all surprised if not-unrelated [China's position](https://www.tellerreport.com/news/2020-07-23-the-cyberspace-administration-of-china-centrally-rectifies-business-website-platforms-and-self-media-violations-of-laws-and-regulations.H1LWVCaLxw.html) leads to non-Chinese compute regions being blocked wholesale. For example, AWS operates two compute regions in China through partners. It would be trivial to block anything not hosted in those regions.

Clearly the author(s) here do not understand global networking, BGP, peering, internet exchanges etc.

If it had suggested that US domestic traffic (particularly for government services and critical national infrastructure) did not require routes outside of the US (for example, travelling via Europe or Asia and back because that bandwidth is cheaper, even if a little slower, isn't so great) that would have made a little more sense.

(Michael) This is mostly legislative posturing as far as I can tell.  This press release doesn't go into enough detail on how they think this can be achieved given the globalisation of the internet.  There would be far more effective and efficient ways that they could achieve the same ends, through the regulation of the collection and use of private data (similar to GDPR) for example, as well as the expansion of the definition of critical national infrastructure, but instead there is a press release.  I guess we'll see what this looks like in a few months and whether it has progressed at all


## [DevSecCon24 - 24hr virtual conference](https://www.mydevsecops.io/post/devseccon24)

[https://www.mydevsecops.io/post/devseccon24](https://www.mydevsecops.io/post/devseccon24)

> 


As well as DefCon, DevSecCon, which I've been to the London one of a few times, managed a 24 hours conference spread across 3 regions, APAC, Europe and the US.  All the videos are free to watch, and should make some good watching if you are melting in the heatwave currently covering the UK


## [DefCon SAFE Mode](https://www.defcon.org/html/defcon-safemode/dc-safemode-quickstart.html)

[https://www.defcon.org/html/defcon-safemode/dc-safemode-quickstart.html](https://www.defcon.org/html/defcon-safemode/dc-safemode-quickstart.html)

> DEF CON official presentations have been pre-recorded, and pre-released online individually and as a torrent on media.defcon.org and on our official YouTube channel.
> 
> The dates and times on the Speaker Page and Schedule Page are special live streamed Q&A sessions for each talk, as well as additional fireside lounges and panels. These sessions will be streamed on Twitch at https://www.twitch.tv/defconorg.
> 
> All discussions and attendee to speaker participation will be on the DEF CON Safe Mode Discord Server at: https://discord.com/channels/708208267699945503/733079621402099732


It's conference season, and in the face of lockdown in many countries, of course big gathering of people in Las Vegas isn't a popular move.  Therefore DefCon has gone virtual and you can watch the videos and engage with the community via Discord, Youtube and generally on the internet.


