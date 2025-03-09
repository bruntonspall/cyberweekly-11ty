---
title: "207 - Cognitive load"
date: 2022-08-21
description: "I had a great time at Blackhat, BSides and DEFCON.  There were loads of talks, on a huge number of technical topics, and one of the things that I came away, both inspired and slightly daunted by, was the breadth of topics that security can cover."
permalink: /cognitive-load/
---

I had a great time at Blackhat, BSides and DEFCON.  There were loads of talks, on a huge number of technical topics, and one of the things that I came away, both inspired and slightly daunted by, was the breadth of topics that security can cover.

From looking at industrial control systems and car hacking, to the rogues gallery demonstrating pickpocketing and marking cards, through to the physical security village with lock picks and RFID cards, through the red team, blue team, cloud, appsec and too many other villages to name, there’s a bit of everything for everyone.

One of the things that really resonated with me there though was the unbridled sense of curiosity in all of these people.  Everyone has a passion and curiosity to find out how things work.  But one of the things that I also picked up was just how much of a specialist everyone was.  There are people there who have spent the last few decades hacking satellites and understand everything there is to know about satellite positioning and communications.  Others who know everything there is to know about covert command and control channels and how to set them up, use them and give them fluidity.

I’ve never been a specialist in anything that I do.  I’ve always been a generalist, someone who loves to get into the detail of a topic, but who doesn’t have the patience or sense of interest to stick with a particular topic for any length of time.  The positive side of that is that something like DEFCON can be great, because I can float from topic to topic to topic.  The downside is that when I looked at the schedule and started flagging things I’d like to see, I often found myself with 4 or more talks at the same time I wanted to attend.  I spent a lot of time with Fear Of Missing Out (FOMO), worried that I was going to talks and therefore missing far more interesting and exciting talks elsewhere.  If that sounds familiar, then the first link in todays newsletter, and the associated book may well be worth a read.

One of the most interesting and relevant talks I attended, that hasn’t had much press attention, was a talk talking about [how to give cybersecurity advice without causing harm](https://www.blackhat.com/us-22/briefings/schedule/#harm-reduction-a-framework-for-effective--compassionate-security-guidance-26723).  The speaker was comparing cybersecurity advice to some of the studied areas of personal health that resulted in things like needle swaps, drug awareness campaigns and sexual health clinics.  

In those situations, we have evidence that shows that fear based guidance and strict rules of “just say no” don’t really work for people.  Instead guidance has to be tailored around minimising harm, and lowering cognitive load on the target audience.  We provide needle swaps because “Just don’t do drugs” as a message results in far more societal harm than “You shouldn’t do drugs, but if you are going to, here is how to reduce disease and infection when you do”.

Our cybersecurity advice on things like phishing and passwords has tended to remain far too rooted in the idea that users must attain some level of cyber perfection.  But users live in a real world where they can and must compromise their principles on occasion.  We rarely advise people on how to best take risks, on how to write down passwords securely, or how to share passwords and accounts with their coworkers/friends in a secure manner.  

Our security assumptions are always based on the idea that the user has low cognitive load, that they can spot bad behaviours, and that they have time, energy and attention to do the right thing every time.  But attackers know that if they can increase cognitive load, whether ringing the users constantly, sending them emails designed to create fear and urgency, or otherwise prompt the user into situations where they know they are breaking the rules, then the user is far more likely to step outside of the guidance.

Microsoft wrote about this a number of years ago and has some [excellent resources on inclusive design](https://www.microsoft.com/design/inclusive/).  An example from that is that designing for someone who has one arm also means designs that can be used by someone who has injured their arm, and also means that the designs can be used by new parents who have to hold a baby under one arm as well.

When we design for people with low cognitive abilities, we’re not just talking about designing for people who struggle to understand, but we’re designing for those people who are harried, who are distracted, who are unable to give the task their full attention, and those who are under attack by attackers intent on distracting them.

## [What do to with an unfinished project • Three Saplings ](https://threesaplings.co/articles/what-do-to-with-an-unfinished-project/)

[https://threesaplings.co/articles/what-do-to-with-an-unfinished-project/](https://threesaplings.co/articles/what-do-to-with-an-unfinished-project/)

> Once upon a time, I decided I wanted to learn how to knit. I signed up for knitting classes which I attended once a week for half a year. I got to practice the basic knits and some different knitting techniques. We learnt how patterns were notated and how to follow them, so we could create actual garments and not only make simple squares and rectangles.
> 
> After doing small test patches of one knitting technique after another I decided it was time to put this knowledge into practice by making a sweater.
> 
> […]
> 
> Because when I look back, I didn’t take knitting classes because I wanted to make a sweater. I took knitting classes because I wanted to learn how it’s done!
> 
> As soon as I understood that and had built up some kind of ability to do it myself, I lost the drive to continue. The actual knitting of that sweater became a chore that I was forcing myself to do, only because I had previously said that I would do it.
> 
> My joy lies in understanding, in figuring out how things work and how they are being made. I’m ever curious and I love learning about new things.
> 
> But executing on something that I already know, that has turned from barely within my grasp into something mundane and routine, bores me out. There’s nothing new to learn, so there’s nothing there to keep me interested. 


This hit home really hard, and has resulted in a great book recommendation to go away and read on my holidays, because I’m just like this.  I love to learn new things, but actually putting them into practice is something I tend to find a chore.  Once I know how to solve a problem, I’m far less interested in following through in the doing part of it. 


## [Cisco Talos Intelligence Group - Comprehensive Threat Intelligence: Cisco Talos shares insights related to recent cyber attack on Cisco ](https://blog.talosintelligence.com/2022/08/recent-cyber-attack.html)

[https://blog.talosintelligence.com/2022/08/recent-cyber-attack.html](https://blog.talosintelligence.com/2022/08/recent-cyber-attack.html)

> Initial access to the Cisco VPN was achieved via the successful compromise of a Cisco employee’s personal Google account. The user had enabled password syncing via Google Chrome and had stored their Cisco credentials in their browser, enabling that information to synchronize to their Google account. After obtaining the user’s credentials, the attacker attempted to bypass multifactor authentication (MFA) using a variety of techniques, including voice phishing (aka "vishing") and MFA fatigue, the process of sending a high volume of push requests to the target’s mobile device until the user accepts, either accidentally or simply to attempt to silence the repeated push notifications they are receiving. Vishing is an increasingly common social engineering technique whereby attackers try to trick employees into divulging sensitive information over the phone. In this instance, an employee reported that they received multiple calls over several days in which the callers – who spoke in English with various international accents and dialects – purported to be associated with support organizations trusted by the user.  
> 
> Once the attacker had obtained initial access, they enrolled a series of new devices for MFA and authenticated successfully to the Cisco VPN. The attacker then escalated to administrative privileges, allowing them to login to multiple systems, which alerted our Cisco Security Incident Response Team (CSIRT), who subsequently responded to the incident. The actor in question dropped a variety of tools, including remote access tools like LogMeIn and TeamViewer, offensive security tools such as Cobalt Strike, PowerSploit, Mimikatz, and Impacket, and added their own backdoor accounts and persistence mechanisms. 


This is a great write up, with an interesting take on the vishing attack.  By attempting to overload a user with MFA attempts and simultaneously socially engineer them into approving them, they relied on human fatigue that eventually the operator would make a mistake of some form. 


## [The Cisco Hack - Tracking the Attack Through your Logs ](https://trunc.org/learning/cisco-hack-tracks-left-in-the-logs)

[https://trunc.org/learning/cisco-hack-tracks-left-in-the-logs](https://trunc.org/learning/cisco-hack-tracks-left-in-the-logs)

> Cisco Talos recently shared a very interesting article detailing how Cisco was compromised. Companies rarely provide this level of detail, and when they do it serves as a great learning opportunity. 
> 
> These details are instrumental in helping the community get better by helping us understand TTPs being employed by bad actors, but also by highlighting the things we should be monitoring to help keep our enviornments safe. It also provides a great playbook other organizations can use to a) identify issues, b) how to mitigate and c) how to handle a security event.
> 
> We thank the Cisco team for how they shared, and what they shared. Before reading more, we encourage you to read their report first: [Cisco - Recent Cyber Attack 2022](https://blog.talosintelligence.com/2022/08/recent-cyber-attack.html) .
> As researchers, we were able to use the scenario they described to replicate the events in our labs in an effort to continue to the education and help the community as a whole. 
> 
> We focus on the traces of evidence left in the logs and how to make sense of what is going on. This should help security teams detect and mitigate similar issues if it effects their organization.
> 
> Through the use of an effective logging strategy and platform you should be able to identify a series of events, tracks left by bad actors, and alert on key events that can be strong indicators of a compromise (IoC) allowing your team to respond quickly. 


This is a really nice defensive writeup on how you can specifically track this kind of attack vectors and what logs to turn on that will detect actors trying to use this same set of attack TTPs. 


## [Black Hat and DEF CON Roundup | Threatpost ](https://threatpost.com/black-hat-and-def-con-roundup/180409/)

[https://threatpost.com/black-hat-and-def-con-roundup/180409/](https://threatpost.com/black-hat-and-def-con-roundup/180409/)

> There was nothing typical this year at BSides LV, Black Hat USA and DEF CON – also known collectively as Hacker Summer Camp. The weeklong collection of cybersecurity conferences featured an eclectic mix of attendees to learn, network, hack and have fun. The week even included a [rare Las Vegas flash flood](https://www.nbcnews.com/news/us-news/-storm-las-vegas-hit-fresh-flash-floods-rain-pours-casino-rcna42789) (not a new DDoS technique) on Thursday creating chaos in one casinos.
> 
> The past week, while not ‘typical’, was a nod to normalcy for attendees. Attendance for events was up from the previous year, which in 2021 was muted by lower attendance and COVID fears. Here is a roundup of leading research, themes and buzz from this year’s shows. 


Black hat and DEFCON were fantastic conferences to attend for a number of reasons.  One of the most interesting to me was a reminder of just how broad a church the hacking community is, and how much we have in common, but also how diverse the skill sets need to be.  Even if you are a specialist in web hacking, you aren’t going to know much about tractor firmware, and as such, there’s loads to learn and lots of people whose skills and knowledge you can admire. 


## [iOS Privacy: Announcing InAppBrowser.com - see what JavaScript commands get injected through an in-app browser · Felix Krause ](https://krausefx.com/blog/announcing-inappbrowsercom-see-what-javascript-commands-get-executed-in-an-in-app-browser)

[https://krausefx.com/blog/announcing-inappbrowsercom-see-what-javascript-commands-get-executed-in-an-in-app-browser](https://krausefx.com/blog/announcing-inappbrowsercom-see-what-javascript-commands-get-executed-in-an-in-app-browser)

> [Last week I published a report](https://krausefx.com/blog/ios-privacy-instagram-and-facebook-can-track-anything-you-do-on-any-website-in-their-in-app-browser) on the risks of mobile apps using in-app browsers. Some apps, like Instagram and Facebook, inject JavaScript code into third party websites that cause potential security and privacy risks to the user.
> 
> I was so happy to see the article featured by major media outlets across the globe, like [TheGuardian](https://www.theguardian.com/technology/2022/aug/11/meta-injecting-code-into-websites-visited-by-its-users-to-track-them-research-says) and [The Register](https://www.theregister.com/2022/08/12/meta_ios_privacy/) , generated a [over a million impressions on Twitter](https://twitter.com/KrauseFx/status/1557412468368052225) , and was ranked [#1 on HackerNews](https://news.ycombinator.com/item?id=32415470) for more than 12 hours. After reading through the replies and DMs, I saw a common question across the community:
> 
> TikTok's In-App Browser injecting code to observe all taps and keyboard inputs, which can include passwords and credit cards 


I’m of two minds of this research.  This is a great example of a technically theoretical attack that is amplified by the media as if it’s a real attack.

It’s true that the in app browsers put in place shims that can detect touches and key presses.  It’s also highly likely that most do so for debugging and analytics purposes (and yes that includes analytics for advertising).  But the chances that these big social media companies are using it to compromise your credit card or personal details is pretty low.  If they are gathering such data, it would be unintentionally as a side effect of how they operate.

Furthermore, many of the suggested fixes to this, such as forcing the user to the devices browser, or showing address bars or limiting functionality make it difficult to use this chrome less in app browsers for their purpose, which is enabling the use of HTML as a mobile phone user interface that can be modified and changes more easily.

This is potentially one of those general vulnerabilities that might have to be accepted as “that’s the way that in-app browsers work”, but we’ll see how Apple and Google respond to these findings and whether they can come up with user friendly solutions that enable users and app developers to get good things done, while preventing abuse and misuse. 


## [TMB 42/52: The Integrator Burden - by John Cutler ](https://cutlefish.substack.com/p/tmb-4252-the-integrator-burden)

[https://cutlefish.substack.com/p/tmb-4252-the-integrator-burden](https://cutlefish.substack.com/p/tmb-4252-the-integrator-burden)

> I remember a leader once asking/telling me "Why are you even concerned about what that team is doing John? It is outside of your group. It is outside your role. You'll drive yourself batty thinking about that AND your day job!" I received the feedback as a classic "stay in your lane!" and remember spinning an internal narrative that pitted me against _uncaring_ leadership. It wasn't that though. She was a very skilled leader, and worried I would burn out. From her perspective, she had hired a formal management team to deal with issues like this. It was their responsibility! I see this now, but I didn't feel that at the time.
> 
> My role had put me in touch with people from across the organization. Since I wasn't a formal manager, they trusted me with insights and perspectives. I could sense the macro currents because I worked with everyone. I saw how...
> 
> * The toxicity of one manager was bubbling over into other groups
> * Tensions between two leaders were spreading distrust among their respective teams
> * The push to grow at all costs was crushing the career aspirations of less vocal team members
> * Different groups were not communicating, and that this was causing burnout
> * How the CEO's words were often misunderstood
> * How knowledge silos were overly burdening OTHER integrators
> 
> I invested an incredible amount of time in trying to help everyone involved. After work chats. Walks. Helping with retrospectives. Coaching people 1:1. Smoothing things over. And yes, I burned out. On reflection, part of the challenge is that I didn't recognize how atypical my role was! I assumed that everyone must see these things. And that if they did nothing, it was pure negligence. 
> 
> What I realize now is that my perspective was UNIQUE. I was connecting dots others were not connecting. And that came at a steep cost. 


This resonated a lot with me.  Some people are natural managers and leaders who can focus on their team, their mission and their work.  But some people are organisationally aware, and in some cases hyperaware of what’s going on all around them, and in other bits of other parts of the organisation.

The reality is that this stuff is hard to deal with, in part because you’ll only ever have a partial view of that stuff, so you will draw conclusions that are not entirely valid, but also because as John says, you’ll worry about things you cannot possibly fix and burn yourself out. 


## [Ask HN: I'm in a rut. How did you get out of yours? | Hacker News ](https://news.ycombinator.com/item?id=32226910)

[https://news.ycombinator.com/item?id=32226910](https://news.ycombinator.com/item?id=32226910)

> In a nutshell, I'm dissatisfied with how my life is going. I can't galvanize myself to do anything. I'm on the clock right now, and here I am complaining about my life instead.
> I don't give a damn about my employer, or the product it makes. I can't get interested in it. I can't get excited about the tedious parts of my work, and I can't even get excited about _automating and eliminating_ the tedious parts of my work.
> And it's not just my day job. I'm ostensibly working on a game on the side, but I haven't touched it in months. I'm not even sure I want to continue it, as I've been working on it for years without being able to fulfill my goals for it. And this is coming from someone who got into computer science _because_ of video games. 


Burnout, Depression and PTSD are sadly too common in our industry, and this thread has a good mix of advice from different people on what worked for them.  Critically, its clear that there’s no one single thing you can do, but lots of anecdotal evidence here for a variety of ways to remember that there’s more to life than your job 


## [BLOOM ](https://bigscience.huggingface.co/blog/bloom)

[https://bigscience.huggingface.co/blog/bloom](https://bigscience.huggingface.co/blog/bloom)

> Large language models (LLMs) have made a significant impact on AI research. These powerful, general models can take on a wide variety of new language tasks from a user’s instructions. However, academia, nonprofits and smaller companies' research labs find it difficult to create, study, or even use LLMs as only a few industrial labs with the necessary resources and exclusive rights can fully access them. Today, we release [BLOOM](https://huggingface.co/bigscience/bloom) , the first multilingual LLM trained in complete transparency, to change this status quo — the result of the largest collaboration of AI researchers ever involved in a single research project.
> 
> With its 176 billion parameters, BLOOM is able to generate text in 46 natural languages and 13 programming languages. For almost all of them, such as Spanish, French and Arabic, BLOOM will be the first language model with over 100B parameters ever created. This is the culmination of a year of work involving over 1000 researchers from 70+ countries and 250+ institutions, leading to a final run of 117 days (March 11 - July 6) training the BLOOM model on the [Jean Zay supercomputer](http://www.idris.fr/eng/info/missions-eng.html) in the south of Paris, France thanks to a compute grant worth an estimated €3M from French research agencies CNRS and GENCI. 


I’ve talked before about the power of GPT-3, Meta’s new model and the interesting capabilities of DALL-E.  But one of the issues is that normally only large corporations have the resources to gather all of that text data, build a model to analyse it, and build up a Large Language Model. 

Providing an open sourced version of this makes it far more accessible for niche researchers to do interesting things with the models. 


## [Reimagining how we think about career development | The Quiet Part Out Loud ](https://amychanta.beehiiv.com/p/reimagining-think-career-development)

[https://amychanta.beehiiv.com/p/reimagining-think-career-development](https://amychanta.beehiiv.com/p/reimagining-think-career-development)

> While useful as a self-reflection tool, the true strength of this visual model is in mapping an entire team’s combined skill set—superimposing individual competency maps over each other—in order to assess if there are certain categories that may be over- or under-represented. Where gaps exist, individuals may volunteer to fill a need for the team and learn new skills in the process. In the absence of individual interest, a manager can use this information to drive conversations around hiring needs.
> 
> But here is the point I need to stress:
> 
> It is unrealistic to expect that every individual fill out every spoke on every circle, however, a team should strive to do it _collectively_ . **This model is meant to help produce teams where individual strengths can be recognized and rewarded, but where success is achieved by having a well-balanced group with a diverse set of skills.** 


A nice review of career development and career ladders.  

The use of career ladders to assess whether the team has the skills available to it that it needs, and whether development within the team context is focused on the right things is something that is useful to the manager of a team.  I’m slightly sceptical however, given the number of horror stories of pretty hideous managers, that people want to turn over their personal professional development to be subordinate to what the manager feels is useful to the team.  There’s a potential for an engaged conversation here however that lets the subordinate determine what they feel they are missing, and the leader to express what would be useful for the team that can help the two work out where development opportunities might lie 


## [Sending weekly 5-15 updates. | Irrational Exuberance ](https://lethain.com/weekly-updates/)

[https://lethain.com/weekly-updates/](https://lethain.com/weekly-updates/)

> I’ve consistently noticed that emails generate far more _discussion_ than other distribution methods, which really shouldn’t have surprised me: I’ve been sending company-internal updates for some time and they’ve frequently created important, spontaneous conversations.
> 
> About a year ago I started my most recent approach to sending weekly updates to relevant public (within the company) mailing lists. This practice is sometimes called a [5-15 report](https://www.theglobeandmail.com/report-on-business/careers/management/cut-down-on-reports-with-the-5-15-method/article4106997/) , reflecting the goal of spending fifteen minutes a week writing a report that can be read in five minutes. Personally, I create a new Google Doc each week and record anything I complete there, spending ten minutes polishing the list into something readable each Friday.
> 
> […]
> 
> Second, one of the important contributions of leadership is creating ambient connective tissue across teams and projects. By sharing what I’ve learned about a new project, I find that often there are other folks who benefit from knowing, and that they wouldn’t have learned about the project otherwise. Is reading a huge number of status emails the right way to learn everything? No, absolutely not, but it’s a good supplemental method.
> 
> As an interesting note, these emails do **not** need to be widely read to be useful. I often find myself ignoring them initially but then going back to find the latest update from someone to answer a specific question later. Further, a small amount of sporatic reading goes a long way: I’ve found there is [herd-immunity](https://en.wikipedia.org/wiki/Herd_immunity) for missing information. If just one or two folks in a given group know something important, it’ll end up where it needs to go. 


This is a really useful trick from managers.  We often send status emails up to senior managers, telling them all the things that have happened in a given week, but I don’t see as commonly that managers send emails down to the wider community.

The important point here is that leaders and managers have a job to do, and one of those is what Will calls “ambient connective tissue”.  Because of my seniority and role, I often find myself in meetings on things that only tangentially are related to me, but I know they are happening.  If I don’t communicate that effectively to my team, then how are they supposed to know that work is happening at all?

This is a good way of creating a permanent record of the connections that you make. 


## [Are you focused on the right risks? This may come as a shock but - Lisa Forte on LinkedIn ](https://www.linkedin.com/posts/lisa-forte_are-you-focused-on-the-right-risks-this-activity-6965235406518820864-0E8t)

[https://www.linkedin.com/posts/lisa-forte_are-you-focused-on-the-right-risks-this-activity-6965235406518820864-0E8t](https://www.linkedin.com/posts/lisa-forte_are-you-focused-on-the-right-risks-this-activity-6965235406518820864-0E8t)

> Introducing a woman called Annie Edson Taylor. She was a school teacher in NY, widowed and struggling financially. Lost her job and things were becoming dire. One year the Pan-American Exposition was planned for Buffalo NY. Not far from her. She read in the paper that people were going to the exposition and then onto Niagara Falls. An idea came to her. She wrote "The idea came to me like a flash of light. Go over the Niagara Falls in a barrel. No one has ever accomplished this feat". 


This is a great story that reminds us about the importance of remembering what our goals are and ensuring that we don’t get over focused on specific risks and forget the actual risks to achieving our goals 


