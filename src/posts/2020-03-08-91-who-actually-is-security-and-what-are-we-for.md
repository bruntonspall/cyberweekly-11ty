---
title: "91 - Who actually is security and what are we for?"
date: 2020-03-08
description: "A recent tweet asked people to write a scary story in just 3 words.  I replied with [\"Security says no\"](https://twitter.com/bruntonspall/status/1232574851149332481?s=20), and a reply \"Who is security\" caused me to reply with \"we're all security\"."
permalink: /who-actually-is-security-and-what-are-we-for/
---

A recent tweet asked people to write a scary story in just 3 words.  I replied with ["Security says no"](https://twitter.com/bruntonspall/status/1232574851149332481?s=20), and a reply "Who is security" caused me to reply with "we're all security".

But this got me thinking, who actually is security really?  The Government Security Profession is part of the UK Governments plan to create government wide functions.  The idea being that instead of feeling like an employee of Department for Work and Pensions, or the Cabinet Office, you might also feel like part of a wider cross government function, so you are part of the "security profession".

But security as a profession is an incredibly broad area.  Government security profession details 4 main areas, Physical, Personnel, Cyber and Technical security.  The implication is that I should be able to get on just as well with someone who worries about bollards on a daily basis as with a vetting officer, or a red teamer.  But even this narrow definition misses out the oft-confused adjunct professions around information security (Did you leave a confidential paper on a train?) and risk management (No, you can't do that), all of which are grouped into "security" as a whole.  Add to that the fact that even cyber security is changing, the days of the security team being the ones who set firewall rules or lock down end user devices are going and instead they are being asked to build platforms and tools and systems for delivering security at speed and scale.

This makes recruiting into a security team a nightmare, because you have no idea when you look at a job advert whether it's actually talking about the same kind of security that you think of.  We often fail to articulate what the mission of security is, and that's one of the reasons that we cannot engage our senior leaders or board members to care about us.  The only way seems to be to shout from the rooftops about "advanced persistent threats" and use scare tactics to get money and attention.  

If we as a profession could clearly and well articulate our mission, our goals, we'd be able to tell potential recruits and exciting story about how they can make a difference, and we'd be able to get money from our leaders.  I'm still going through the AppSec Cali conference talks, but the interesting thing to me is that there are a few companies doing lots of stuff in this area, Netflix, Twillio, Salesforce, Dropbox, and all of them had talks about how they went about building something, whether a platform, tool or program, that improved the security posture of their organisation.  These are projects and programs that have a goal, a mission, a vision and a level of excitement around them.  They're providing risk reduction, they're reducing the harm of legacy decisions, but that's not the articulated goal, and thats far more exciting and attractive to everyone involved.

## [The Athens Affair - IEEE Spectrum](https://spectrum.ieee.org/telecom/security/the-athens-affair)

[https://spectrum.ieee.org/telecom/security/the-athens-affair](https://spectrum.ieee.org/telecom/security/the-athens-affair)

> But unlike the Cuckoo’s Egg, the Athens affair targeted the conversations of specific, highly placed government and military officials. Given the ease with which the conversations could have been recorded, it is generally believed that they were. But no one has found any recordings, and we don’t know how many of the calls were recorded, or even listened to, by the perpetrators. Though the scope of the activity is to a large extent unknown, it’s fair to say that no other computer crime on record has had the same potential for capturing information about affairs of state.
> 
> While this is the first major infiltration to involve cellphones, the scheme did not depend on the wireless nature of the network. Basically, the hackers broke into a telephone network and subverted its built-in wiretapping features for their own purposes. That could have been done with any phone account, not just cellular ones. Nevertheless, there are some elements of the Vodafone Greece system that were unique and crucial to the way the crime was pulled off.
> 
> We still don’t know who committed this crime. A big reason is that the UK-based Vodafone Group, one of the largest cellular providers in the world, bobbled its handling of some key log files. It also reflexively removed the rogue software, instead of letting it continue to run, tipping off the perpetrators that their intrusion had been detected and giving them a chance to run for cover. The company was fined 76 million this past December.


A story from 2005, that's 15 years ago, about how an unidentified someone, backdoored the Greece phone network and used the otherwise unused lawful intercept facility in the core of the telephone exchange to wiretap the phone conversations of the prime minister, his wife, defence secretary and other highly placed government officials.

I hadn't read this at the time, and this is one hell of a story, especially that it's not attributed in any way to a specific attacker.  But the technical details show just how much effort is required to carry out such a significant high capability operation.


## [Political information in the age of the internet | VOX, CEPR Policy Portal](https://voxeu.org/article/political-information-age-internet)

[https://voxeu.org/article/political-information-age-internet](https://voxeu.org/article/political-information-age-internet)

> The digital revolution did not increase voters’ information and awareness of the political process; on average, Americans’ public knowledge has not increased relative to the late 1980s (Pew Research Center 2007). But there have been important changes in the distribution of information. Some individuals have become much more informed, others less informed (Prior 2007). Informational asymmetries across issues (what one is informed about) have also become more prominent. This is not good for the functioning of democracy. Even without subtle psychological mechanisms, simply the free choice of information tends to increase the influence of extremist voters and divert attention away from non-controversial general interest policies. 


This report is good background reading when thinking about electoral interference operations and the effect of disinformation operations on a nation.  What this report says, in essence, is that increased divisiveness is a natural artefact of massively increased access to information.  That (US based) people cannot cope with the sheer amount of information that affects elections, and so they tend to ignore information about common policies and devote attention to policies that they have extreme reactions to, either for or against.

This to me points at a failure of the media as a regulator on this kind of behaviour.  Media companies are supposed to exist in order to level access to information, promoting a wider spread of views and reducing the information asymmetry that exists.  However, the commercial incentives on many US based media organisations means that they have commercial pushes to "align with their audience" that means that they do not in fact regulate that news.  A clickbait article that makes people more impassioned will generate more views, which generates more advertising revenue.  Even in organisations that try to create an ethical wall between commercial and editorial decisions, the editorial decisions are still driven by a desire for traffic as part of the brand competing, but also for ego for the journalists and editors.  One of the reason that I suspect that this is reduced in the UK is the existence of the BBC as "an impartial voice", which does exist to at least attempt balance in these areas. 

The outcome of this is a reminder of how important state driven news that is independent of the government driven agenda probably is to a well functioning democracy.


## [Microsoft AzureAD and Office365 - Not secure by default](https://securityintheenterprise.blogspot.com/2019/11/microsoft-azuread-and-office365-not.html)

[https://securityintheenterprise.blogspot.com/2019/11/microsoft-azuread-and-office365-not.html](https://securityintheenterprise.blogspot.com/2019/11/microsoft-azuread-and-office365-not.html)

> The problem is, that by default, user consent is permitted for all enterprise users. There are a few permissions that require the consent of an Administrator, but by default the user can give any 3rd party (friendly, hostile or malicious) full read-write permissions to most of the data he can reach in Office365. draw.io could abuse the user consent to copy all the users files down to to their webservers if they saw a benefit in doing so.
> 
> A web app can ask for permissions to read-write OneDrive, SharePoint, Mail, Calendar, Contacts, Teams etc, and get offline-access. That means, that whenever the web app wants, it can access these services by using an access token that was handed over to it, by Microsoft, as a result of the user logon and consent. It can even ask for a list of all user identities in the directory, including all those secret Admin accounts with no email address.


(Joel) Extensions, plug-ins, integrations and add-ons is steadily creeping up the list of cyber security worries (and rightfully so).

Extensions et al can request unreasonable and invasive permissions simply because the author deems it so. A sleepy administrator or user may not offer too much attention and may approve the same and platform operators (such as the Chrome Web Store) may not be able to keep up or entirely automate reviews to figure out when authors are asking for excessive permissions.

The real 'kicker' with problematic extensions is that permissions are often conferred once (so it is possible that the functionality of the app changes and it does more than initially expected) and/or that the permission lasts until it is revoked (so approved apps can linger, sometimes falling into an unmaintained state, or subject to a breach where tokens can be stolen to access accounts).

As a normal user, you should check what permissions you're giving to extensions/apps and ponder if they are reasonable for the function of the app and what you want to do (a camera app to take cool pictures probably doesn't need to read/write your calendar and email) and periodically go back and remove things you no longer use/need.

As a system administrator, you should check permissions LIKE A HAWK and monitor for changes, and also go back periodically to measure usage and understand what you could revoke.



## [40% reduction in analytics data | Pete Herlihy](https://twitter.com/yahoo_pete/status/1230562192144994307?s=21)

[https://twitter.com/yahoo_pete/status/1230562192144994307?s=21](https://twitter.com/yahoo_pete/status/1230562192144994307?s=21)

> We've had a 40% reduction in analytics data for  GOV.​UK Notify since we introduced explicit opt-in for analytics cookies.
> [...]
> Comparing analytics data from before and after we added analytics cookie consent to GOV.​UK Notify, we've found negligible difference in user behaviour.
> [...]
> Worth noting that GOV.​UK Notify is a repeat use service, for use by public sector employees. And that we added cookie consent after most users had been using the service for some time.
> 
> I'd expect a higher drop off in acceptance of cookies for single or occasional use services.


(Joel) Pete is a Lead Product Manager within the UK's Government Digital Service (GDS) and is talking here about [GOV.UK Notify](https://www.notifications.service.gov.uk/). This is the first reliable (albeit, informal) stat from HMG that _I_ have seen about the impact of implementing true cookie consent.

I agree with Pete that single or infrequent use services with non-HMG users are likely to see a much higher drop off (in some cases, this might even be total but likely to cap out at 90-95%).

It doesn't appear that users behave any differently (I don't believe I do) when they do not opt-in to non-functional cookies (more often than not, tracking/analytical ones) so we see a shift to in theory same-value data (I wouldn't see it as a higher value) that you have to extrapolate from instead of simply having data from all of your users.

Lets talk about the tracking conducted within Google Analytics (even when the implementer has IP obfuscation turned on) another time.


## [Data Analysis for Cyber Security 101: Detecting Data Exfiltration](https://towardsdatascience.com/data-analysis-for-cybersecurity-101-detecting-data-exfiltration-ae887594f675)

[https://towardsdatascience.com/data-analysis-for-cybersecurity-101-detecting-data-exfiltration-ae887594f675](https://towardsdatascience.com/data-analysis-for-cybersecurity-101-detecting-data-exfiltration-ae887594f675)

> It’s a little bit funny to think that by the time you detect data exfiltration in outbound network traffic, it may already too late! For us to detect high outbound traffic, the attacker has to have already stolen a lot of data first.
> 
> To mitigate this, you have to think about the data you actually care about:
> 
> * Where is the data?
> * Who can access it?
> * How can they access it?
> 
> Let’s say an attacker wants to exfiltrate 50GB of data from your SQL data base. He would first have to dump the tables of your SQL server to his host, and then upload these to some external cloud storage.
> 
> You could have detected the attacker even before he can exfiltrate the data if you were able to alert on either:
> 
> * Unauthorised SQL database dump
> * Unusually high traffic transferred from the SQL server
> 
> For example, you look at what your SQL server typically does, and find out that the bulk of the SQL server’s traffic would typically with the web application server, some ETL processes and maybe some backup processes. Then high data transfer from SQL server to a SQL admin workstation may be considered abnormal.
> 
> Rather than monitoring all the traffic in your network to find “anything weird”, with a bit of analysis, you might be able to concentrate on a few components of your network.


This is a good walkthrough of a high point CTF that is all about statistics, and you can go try the same detection logic over on Kaggle if you want (You'll need a registered account as the dataset is quite large).

It's a good reminder that you can detect bad behaviour with the simplest of tools, in this case, a CSV of netflow data and a little bit of python.  This could be run on a developers laptop really easily, no multi-milllion pound SOC from a ex-defence contractor required.  

But what I really agree with in this section is that detecting data exfiltration is not sufficient, it should be the last possible defence.  This is akin to discovering you have been burgled because the door frame has been broken, or becuase your TV is gone.  This will help you discover you are breached, but what's better is to move your detection upstream and try to detect and prevent attackers well before they get to trying to exfiltrate your data.

Good security analysts can work backwards from a goal.  Don't just dump data on them and ask them to "find interesting things", come up with potential attack scenarios, and ask how they'd detect them (database exports being triggered), and then find out what data you need to collect to feed that collection system.  That way you won't end up "collecting everything", but only collecting a baseline of interesting stuff (sysmon logs from EUDs for example), along with data that your analysts say they need.


## [Delivering digital service: this much I have learned – Matt Edgar writes here](https://blog.mattedgar.com/2020/01/27/delivering-digital-service-this-much-i-have-learned/)

[https://blog.mattedgar.com/2020/01/27/delivering-digital-service-this-much-i-have-learned/](https://blog.mattedgar.com/2020/01/27/delivering-digital-service-this-much-i-have-learned/)

> Because they have the skills they need, and fewer interdependencies, multidisciplinary teams can be given freedom to choose their tools and how they get things done. Each team will develop ways of working that make it more productive at the type of tasks it takes on. Some of these habits remain unique to one team, others emerge as de facto standards that other teams can pick up and integrate into their own working practices.
> 
> Teams that work together, with aligned autonomy, are accountable together. They take pride in their work, use testing to drive their development, and deliver a consistently high quality product or service day-in-day-out. When working in health and care, technical excellence and clinical safety go hand-in-hand.
> 
> Customers, suppliers and other third parties have much to gain by participating in this way too. Even the largest organisation relies on others to get stuff done. The suppliers who can’t yet work like this may need some support. The ones who won’t work like this represent a risk to themselves and others; they must be managed closely.


Lots here in this blog post, one that I strong recommend reading in full.  This point in here about the power of multidisciplinary teams, and in particular the fact that good multidisciplinary teams work to improve their own ways of working, which makes them far more efficient.  This freedom to discover what makes a team work is one of the powers that creates these mythical 10x engineers or teams, and it's far more about increasing the individual effectiveness of the team communication and coordination structures than it is about the individual contributions of said person.

Secondly, there's an interesting point here about the fact that your multidisciplinary teams aren't just about your core staff, but are about getting your consultants, contractors and suppliers to try to work this way as well.  There's some more I'd love to say and explore about the ideas of managing supplier provided teams here, but for now I think Matt has gotten this just right.  You need to support and enable suppliers to do this, and if they cannot work this way, you may need to ask whether they are the right supplier.


## [The state we’re in - Valleys To Coast Design & Tech Blog - Medium](https://medium.com/valleys-to-coast-design-tech-blog/the-state-were-in-c7549cb03938)

[https://medium.com/valleys-to-coast-design-tech-blog/the-state-were-in-c7549cb03938](https://medium.com/valleys-to-coast-design-tech-blog/the-state-were-in-c7549cb03938)

> So in this case: As a senior manager, I need to understand the overall status of our applications and infrastructure so that I can make informed decisions about priorities for action.
> 
> The solution should:
> * Group systems by business area to give context on each element
> * Show relative business impact of each system.
> * Show status/ fitness-for-purpose of each system.
> * Be viewable at a glance


I cannot love this enough.  Ignore for a second the fact that this is showing systems based on business impact and status/fitness-for-purpose.  This way of visualising systems, showing clear groupings of systems, and then giving you information at a glance about the status/health/whatever of the system is a brilliant visualisation.  

And it's entirely driven from a spreadsheet, specifically from Google Sheets.  It's really easy for developers to say "lets build a dashboarding appplication", but I find that a lot of non developers would much rather have a spreadsheet that they can modify.  You can do amazing things with a good spreadsheet.

If you've not had a chance to play with building dashboards in Google Sheets, you should give it a try.  If you want to really blow your mind, go lookup the IMPORTRANGE function.  This lets you pull a range of values from another Google Docs sheet.  I've used this (ok, actually, I showed Joel and he used this) to allow teams to maintain their own system sheet, one for each system, with a bunch of data that they think is interesting (or that Joel told them to gather).  You then create a dashboard sheets document that uses IMPORTRANGE to pull in just the summary information you need in from each other sheet.  Even better is the fact that the permissions mean that the viewers of the dashboards don't need to be allowed to read the individual sheets, so the teams can keep information in there that is unique, special or sensitive to themselves.


## [National Counterintelligence Strategy of the United States of America 2020-2022 [pdf]](https://www.dni.gov/files/NCSC/documents/features/20200205-National_CI_Strategy_2020_2022.pdf)

[https://www.dni.gov/files/NCSC/documents/features/20200205-National_CI_Strategy_2020_2022.pdf](https://www.dni.gov/files/NCSC/documents/features/20200205-National_CI_Strategy_2020_2022.pdf)

> Our foreign adversaries are capable of conducting cyber espionage and technical operations against U.S. interests around the world and they continue to develop new and more effective capabilities in these areas. Readily available and advanced cyber and technical surveillance tools offer threat actors a relatively low-cost, efficient, deniable, and high-yield means of accomplishing their goals. 


It's worth remembering and noting two interesting things from this strategy document.  The first is, as quoted above, that the US Government believes that foreign adversaries at the highest levels of capability are using readily available advanced toolsets.  It wasn't that long ago that only the highest level capability states had the engineering power to build full toolsets capable of advanced exploitation, but a red team security engineering efforts release more and more tools, and more and more joint frameworks, the gap between advanced national cyber actor and random person with access to tools closes.

The second is that looking through the recommended actions in this strategy document, almost none are actually "SMART" style goals.  Many of the goals in this strategy are neither specific nor measurable, the two most important things for determining whether a strategy is actually implementable.  There are lots of nice sounding platitudes about sharing information better, broadening awareness or improving detection, but to me that sounds a little bit like they don't actually know what to do, so they are falling back on vague generic language to hide the lack of an actual plan.


## [How to (Actually) Recruit Talent for the AI Challenge - War on the Rocks](https://warontherocks.com/2020/02/how-to-actually-recruit-talent-for-the-ai-challenge/)

[https://warontherocks.com/2020/02/how-to-actually-recruit-talent-for-the-ai-challenge/](https://warontherocks.com/2020/02/how-to-actually-recruit-talent-for-the-ai-challenge/)

> To reverse these trends, the U.S. government should change the way it thinks about careers and embrace a lesson learned by leading tech companies — that software talent comes and goes and that’s a good thing. Skeptics will say that the Pentagon is different from any other institution and cannot succeed with a transient labor force that does not understand its way of doing things and doesn’t have high-level security clearances. Certainly, when it comes to battlefield applications, sensitive intelligence, or operational tactics, the Pentagon has plenty to hide. And its most sensitive software will have to remain off-limits to all but the most carefully vetted employees.
> 
> But most of the military’s software powers an ecosystem of backend operations that are no different than those used by private companies. The Defense Department needs to recognize that most of its software is not secret — just proprietary — and modernize its employment practices accordingly.


Ignore the AI part of this article.  The main point in here is a recognition that defence, intelligence and government in general is still massively suffering from losing a war around culture and retention for top technical talent.  While I don't believe in 10x or 100x engineers (referenced further down), I do believe that small fast moving and enabled teams are 10 or 100 times more effective than large cumbersome teams that are "enabled with enterprise architecture".

The attraction of talent, whether to government or to cyber security, is partly about the failure of renumeration, but for more often about the failure of culture, the lack of clear vision, and the offer that needs to exist.  Engineers aren't career driven in the same way anymore, they join an organisation because they agree with the mission, because there is an interesting problem to solve and because they think that they'll be equipped to actually solve it.

Do you think your most recent job adverts actually sell that?  Does becoming the next "Security analyst" in the team sound like it's going to actually deliver or solve anything?


## [Career framework For security professionals in government [pdf]](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/864752/Government_Security_Profession_career_framework.pdf)

[https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/864752/Government_Security_Profession_career_framework.pdf](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/864752/Government_Security_Profession_career_framework.pdf)

> Currently, expertise in Government Security is in short supply and patchily spread. The Government Security Profession framework is a critical first step in beginning to address that. It offers you an opportunity to chart a career in Government Security, working across government and beyond, to develop your skills and expertise. 
> 
> Security is at the cutting edge of modern organisations. Your journey starts here!


This is a 350 page document and is desperately in need of some form or tl;dr; so I'll do my best.

This is a good stab at trying to articulate what a career in government security might look like.  It covers all forms of security, from close protection officer to behavioural scientist, from digital forensics to software installer, from penetration tester to chief security officer.  It really suffers from the breadth because it feels like it's trying to cover every possible role in government security, and yet feels like it fails to deliver, especially on the edges of the careers (as viewed by the authors).

The biggest issues from my perspective is that it still has a fairly dated view of security in many perspectives.  While it has been kept up to date with the developments in the Digital, Date and Technology professions in government, it still lacks in real security engineering capabilities.  There's no call for developer skills anywhere in the system, and where "build" capabilites are included, it's much more focused on enterprise IT capabilities.  That's no bad thing given how little security thinking goes into end user device builds and development these days, but the lack of development capability suggests that for digital services there is no concerted thinking about who is building the security of the platforms of the future.

The biggest issue from my perspective is that the career pathways outlined make it doubly clear that there is no expectation that security advisors, policy people or CISO's are really expected to have any technical background at all.  In 2020, the lack of basic technological understanding is what will kill a CISO dead in the water.  You'll be unable to vet your suppliers, ask the right questions or make prioritisation decisions if you don't, at least, have. grounding in the modern digital technology era.  I'm not expecting every policy person to have once been a red teamer, but it would be nice if they understood what a browser was, what TLS actually meant, and how users interact with this technology.

There's quite a lot of interesting stuff in here, and if you skip through the first 270 pages or so, there's a fascinating section on skills that covers what skills are needed at different levels, and some examples of courses and training that are appropriate for developing those skills.  This suffers from, despite being a 350 page document, just not being exhaustive enough.  "Secure development" is the sole skill around development and security, which is far too broad brush for an area that could cover everything from secure coding guidelines to dependency checking to static analysis and beyond.

All in all, if you are building a recruitment and retention framework, you could go a lot worse than using this as a starter.  [There's a NIST equivalent (NIST-SP-800-181)](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-181.pdf) and I think this is far more usable than that was when it was first released (and probably still today, that NIST framework is super dry!).  But I wouldn't say that this is complete, you are going to need to define your organisational delivery capabilities around this, and determine what's missing, what areas you want in addition, and then build your own framework on top of it.


