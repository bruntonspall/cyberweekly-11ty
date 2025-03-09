---
title: "9 - Better late than never"
date: 2018-07-22
description: "_NOTE: This letter was mistakenly sent with the subject #8 - Better late than never_"
permalink: /better-late-than-never/
---

_NOTE: This letter was mistakenly sent with the subject #8 - Better late than never_

What is the purpose of a security team?  Why do they even exist?  A recent article about misconfiguring of trello boards prompted a bit of a discussion in one of the forums that I chat on, about how teams should configure their trello boards, whether the user interface was clear enough, and what the difference was between Public and Team privacy settings.  

But this got me thinking.  Most of the security or information assurance teams I've met in Government are the last to adopt any new technology.  The security teams refuse to use Trello because its "not secure enough", and they still retain security documentation on shared drives on the corporate server, with no indexes, no search and limited capability to look stuff up.  This is often touted as necessary because the security documents contain sensitive information such as the IP addresses of internal servers (shock horror), or lists of known vulnerabilities.

But when the security teams don't use the tooling that everyone else uses, how can they possibly be expected to give any advice on how to use that tooling appropriately and securely?  How can they help the organisation use the newest and latest technology?  I think security teams should be using modern tooling, and trying new task trackers, todo lists, collaboration tools to find out how to use them well, and how users might use them.

## [Digital Strategy Isn’t Meeting Security Needs — Here’s What to Do](http://feedproxy.google.com/~r/SecurityIntelligence/~3/afO2TZ96rus/)

[http://feedproxy.google.com/~r/SecurityIntelligence/~3/afO2TZ96rus/](http://feedproxy.google.com/~r/SecurityIntelligence/~3/afO2TZ96rus/)



“IT staff are often risk-takers — they like new technology and want to use it right away. Where they run into trouble is bringing in the latest technology without a real strategy to implement it both wisely and securely. Just because IT wants to update its technology doesn’t mean the company is ready for it.” This sadly, reads to me much like a traditional “security says no” response to changing environments.  The perception of IT or technology staff as wanting to have the newest and latest toys, with scant regard for security.  The subtext of this post is that security should be stronger at saying no, rather than it should be just as fast at adopting new technologies and experiences, so it can give security advice on how to use the tool effectively


## [Building a tool to improve our GitHub security](https://gdstechnology.blog.gov.uk/2018/07/13/building-a-tool-to-improve-our-github-security/)

[https://gdstechnology.blog.gov.uk/2018/07/13/building-a-tool-to-improve-our-github-security/](https://gdstechnology.blog.gov.uk/2018/07/13/building-a-tool-to-improve-our-github-security/)



“By using our audit log for GitHub events in Alphagov, we can see if any malicious action has taken place and view any details. In the future, we may develop an automated audit tool so we can be alerted to any possible malicious activity.”. this kind of audit logging is going to grow increasingly important and increasingly valauable over the next few years.  It shouldnt be at the top of most organisations todo lists, but if you already have a security engineEring


## [Import data, not malware - NCSC Blog](https://www.ncsc.gov.uk/blog-post/import-data-not-malware)

[https://www.ncsc.gov.uk/blog-post/import-data-not-malware](https://www.ncsc.gov.uk/blog-post/import-data-not-malware)



Three main thoughts on this excellent blog post, and associated guidance.  The first being that this is a pattern that has previously only been understood and applied generally in classified environments, and so to have it so clearly articulated in a manner that is sharable and discussable is really useful.

“The pattern is generic, so should be tailored to fit your particular scenario. In lower risk situations, you might want to leave out some of the controls" This is important guidance for the use of a pattern like this.  Too often in Government, I run into security people whose attitude to patterns and pronouncements from NCSC, NIST, NSA etc is to assume that these are cast iron checklists that must be obeyed, and the context is lost.  This blog makes it clear that this pattern outlines the pattern, but you might need to modify it to suit your circumstances.

"One top tip I’d like to share from my experience of using the pattern is to remind users to ask for the data they need, rather than the document it's wrapped in. I’ve often heard requirements for regular PDF transfers, when what is actually needed is some text, or numbers contained within a PDF. The data might arrive in a PDF, but that’s not necessarily what's required to pass through your gateway.” This second bit is also a useful reminder.  If you current accept documents in complex formats, such as Word, ODF, PDF, XLS etc, then think whether you should be asking your systems, users or staff submitting those documents what they actually need.  Often times you could make like easier for the user, less data to find and submit, and clearer how the data will be used, as well as making the whole system more secure by requesting a subset of the data be manually entered instead.


## [Executives and Transparency](https://theitriskmanager.wordpress.com/2018/07/01/executives-and-transparency/)

[https://theitriskmanager.wordpress.com/2018/07/01/executives-and-transparency/](https://theitriskmanager.wordpress.com/2018/07/01/executives-and-transparency/)



“Jira is a tool developed to help teams manage their development. It is not a tool to manage across teams or at an enterprise level. In order to create transparency for executives, you need an expert who can extract the data you need to create the views they need. One of the graduates working with us created an app to extract data from Jira into an SQL based database. Once the data was in the SQL database it took a couple of days to create an excel report that gave an executive view of lead time using weighted lead time.”. There is quite a lot of interesting bits and pieces in here about transformation and transparency, but this caught my eye.  How often do we see agile teams grumble that the executives or leaders could come down and see the “wall”?  What our teams often fail to realise is that the wall of cards, or tool like Jira, is optimised to be used by the day to day users of the thing.  There is a value in senior leaders seeing that, to ensure that they aren’t being hoodwinked, and to understand where the “roll up” numbers come from, but actually, burn down charts, story estimation, velocity or other summation metrics are far more useful for these leaders, and creating those metrics, those dashboards takes time, energy and effort.  As an agile team, you need to put in that energy or effort.  Simply grumbling that the leadership don’t come to your show and tell, or don’t come and walk the wall wont lead to success


## [Follow the business strategy - Nik Silver](http://niksilver.com/2018/07/17/strategies/)

[http://niksilver.com/2018/07/17/strategies/](http://niksilver.com/2018/07/17/strategies/)



“There’s another, implicit, message in all of this, too: If there isn’t a business strategy that people understand then it’s very difficult to align the product and technology strategies, and it’s near-impossible to ensure they’re helping the organisation to move in the right direction.”. This from Nik is a good summary of the problem with a lot of *Strategy documents.  Without a reference or even a nod towards the wider business goals, the strategy is in and of itself meaningless.  It defines doing digital, technology or security for the sake of doing digital, technology or security.


## [Burning Umbrella: An Intelligence Report on the Winnti Umbrella and Associated State-Sponsored Attackers](https://401trg.com/burning-umbrella/)

[https://401trg.com/burning-umbrella/](https://401trg.com/burning-umbrella/)



“One of the most common tactics used by the Winnti umbrella and related entities is phishing users whose credentials may provide elevated access to a target network. We have observed spear-phishing campaigns that target human resources and hiring managers, IT staff, and internal information security staff, which are generally very effective.  In 2017 the entity focused most of its efforts around technical job applicant email submissions to software engineering, IT, and recruiting staff, which we originally reported on at our 401trg.com blog.”  This is an interesting report.  I’m not entirely convinced by the tying together of all of the activities into a single group, but that’s not what is interesting to me.  Again what I see here is that APT level actors are interested in things like code signing certificates and developer workflows and tool chains.  The sending of phishing emails to recruitment email addresses feels particularly devious.  A recruitment manager would both be expected to open any attachment on an email like this and would very likely collate documents such as CV’s and send them onto internal engineers for sifting, probably without editing or changing the documents.  That potentially malicious file being passed internally from a “trusted source” is a fascinating insight into how high end phishing or spear phishing can work.


## [Thread by @chadloder: "A thread on being a so-called “Security expert”.](https://threadreaderapp.com/thread/1020420759041159168.html)

[https://threadreaderapp.com/thread/1020420759041159168.html](https://threadreaderapp.com/thread/1020420759041159168.html)



“It was eye-opening for me to tell the sales rep from my former company (whom I TRAINED) “Dude I am so far away from needing a vuln scanner right now it’s not even funny. I KNOW the scan results will be a shitshow and I wouldn’t be able to do anything about it””. This is a great thread that talks about how big and broad security is, and how narrow a view most of us have on it.  Find yourself arguing about using vulnerability scanners, or which hashing algorithm to use, and you are probably missing the wood for the trees.  That doesn’t mean the details don’t matter, but it’s that in security, we tend to be swimming in details.


## [Unfollowing Everybody - Anil Dash](https://anildash.com/2018/07/13/unfollowing-everybody/)

[https://anildash.com/2018/07/13/unfollowing-everybody/](https://anildash.com/2018/07/13/unfollowing-everybody/)



“It's been about a week and a half, and, well... Twitter is a lot more pleasant. I've chosen a handful of accounts to follow each day (most ones that I followed before, some entirely new to me) and it's made a big difference. On the flip side, about 100 people seem to have unfollowed me after I unfollowed everybody, and I hope they hadn't felt obligated just to reciprocate if I was following them before. (That might also just be how many people unfollow me in a given week, I dunno.)  One of the most immediate benefits is that, when something terrible happens in the news, I don't see an endless, repetitive stream of dozens of people reacting to it in succession. “. I’m increasingly feeling like Twitter is both toxis to my mental health, and distracting.  One of the things I really liked about Google  was the ability to put people into circles, and then see updates from the circles separately.  I might start trying out twitter like this, putting people into lists and then surfacing the lists, to avoid thoughtful but rarely tweeting people from being drowned out by the noise


## [Sizing engineering teams.](https://lethain.com//sizing-engineering-teams/)

[https://lethain.com//sizing-engineering-teams/](https://lethain.com//sizing-engineering-teams/)



“Tech Lead Managers (TLMs). Managers supporting less than four engineers tend to function as TLMs, taking on a share of design and implementation work. For some folks this role can uniquely leverage their strengths, but it's a role with limited career opportunities. To progress as a manager, they'll want more time to focus developing their management skills”. Organisation and team design is important, but so is the intentions and desire of the team member themselves.  Some technical leaders don’t want to progress as a manager, and that’s ok. Others do, and you should support that too.  These sizing guides feel about right to me though.


