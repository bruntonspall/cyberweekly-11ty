---
title: "128 - What makes a good strategy?"
date: 2020-12-06
description: "I think that a lot of us spend a lot of our career believing that somewhere at the top of the organisations we work for, despite all the evidence, someone knows what they are doing."
permalink: /what-makes-a-good-strategy/
---

I think that a lot of us spend a lot of our career believing that somewhere at the top of the organisations we work for, despite all the evidence, someone knows what they are doing.

We tend to call this strategy, and I think it's much misunderstood.  If you haven't read [good strategy/bad strategy](https://www.amazon.co.uk/Good-Strategy-Bad-difference-matters/dp/1781256179), then you are missing out.  But really good strategy doesn't come from locking yourself in a room and coming up with the best ideas.  It comes from reviewing and understanding what you are doing as an organisation.  It comes from looking at how your organisation does things and it comes from repeating that over and over.

I worked for a time as a strategy consultant, but in many cases, my job was not to think about the future, but to analyse the present.  To really understand what was actually happening in the organisation, and what the problems or roadblocks were internally.  Of course there's some awareness of what other organisations in your sector are doing, ensuring that you are aren't focused on the wrong things, but the majority of strategy is about ensuring that the feedback looks are complete, and that your teams can execute on what they should be doing, because 9 times out of 10, your people on the ground already know what they should be doing!  The strategy is about making it easy, adopting what has gone before and making it faster, easier and better.

## [Summary of the Amazon Kinesis Event in the Northern Virginia (US-EAST-1) Region](https://aws.amazon.com/message/11201/)

[https://aws.amazon.com/message/11201/](https://aws.amazon.com/message/11201/)

>  Each server in the front-end fleet maintains a cache of information, including membership details and shard ownership for the back-end clusters, called a shard-map. This information is obtained through calls to a microservice vending the membership information, retrieval of configuration information from DynamoDB, and continuous processing of messages from other Kinesis front-end servers. For the latter communication, each front-end server creates operating system threads for each of the other servers in the front-end fleet. Upon any addition of capacity, the servers that are already operating members of the fleet will learn of new servers joining and establish the appropriate threads. It takes up to an hour for any existing front-end fleet member to learn of new participants.
> 
> At 5:15 AM PST, the first alarms began firing for errors on putting and getting Kinesis records. Teams engaged and began reviewing logs. While the new capacity was a suspect, there were a number of errors that were unrelated to the new capacity and would likely persist even if the capacity were to be removed. Still, as a precaution, we began removing the new capacity while researching the other errors. 
> 
> At 9:39 AM PST, we were able to confirm a root cause, and it turned out this wasn’t driven by memory pressure. Rather, the new capacity had caused all of the servers in the fleet to exceed the maximum number of threads allowed by an operating system configuration. As this limit was being exceeded, cache construction was failing to complete and front-end servers were ending up with useless shard-maps that left them unable to route requests to back-end clusters. We didn’t want to increase the operating system limit without further testing, and as we had just completed the removal of the additional capacity that triggered the event, we determined that the thread count would no longer exceed the operating system limit and proceeded with the restart.


The number of parallel machines you can run can overflow certain limits in the machines.  This is the sort of problem that you run into with a horizontally scaled architecture.

The internet more or less went down for several hours because of this, despite the constant reminders that there are two golden rules to using the cloud:

1. You should use more than one region
2. Never use AWS US-East-1


## [Introducing Amazon ECS Anywhere | Containers](https://aws.amazon.com/blogs/containers/introducing-amazon-ecs-anywhere/)

[https://aws.amazon.com/blogs/containers/introducing-amazon-ecs-anywhere/](https://aws.amazon.com/blogs/containers/introducing-amazon-ecs-anywhere/)

> Today, we are announcing Amazon ECS Anywhere (ECS Anywhere), an extension of Amazon ECS. Available in 2021, ECS Anywhere will allow customers to deploy native Amazon ECS tasks in any environment. This will include the traditional AWS managed infrastructure, as well as customer-managed infrastructure. All this without compromising on the value of leveraging a fully AWS managed, easy to use, control plane that’s running in the cloud, and always up to date.


Many people jumped on this because of the big news that this would support competitor cloud services, allowing you to keep your existing Azure or GCP instances and systems, and then manage and deploy your ECS across multiple cloud providers.

That's interesting, but what's even more interesting is that it's really about AWS recognising that they can compete on the control plane far better than on the data plane.  At the end of the day, if you use AWS to control your tasks and your instances, then who cares where the pods are running, and who is paying for the infrastructure.  The control plane is where the power is.


## [How Zoom pulled off the scaling event of a lifetime - Protocol](https://www.protocol.com/manuals/new-enterprise/how-zoom-scaled-covid19)

[https://www.protocol.com/manuals/new-enterprise/how-zoom-scaled-covid19](https://www.protocol.com/manuals/new-enterprise/how-zoom-scaled-covid19)

> For the most part, the company uses its network of 19 co-located data centers around the world to service meeting traffic, Ittelson said. Going into 2020, those data centers were running at about about 50% of peak capacity, he said, which gave Zoom the ability to absorb the early impact of increased demand in China and Europe as the pandemic spread.
> 
> Zoom's goal all along was to provide its services as close to the end user as possible through these data centers. Distance is an extremely important factor for video applications, given that stuttering video feeds and audio gaps caused by latency can ruin a big meeting in a hurry.
> 
> But Zoom is also a longtime customer of AWS, and uses the cloud provider's network for other parts of the Zoom application. During a video discussion in April, Zoom CEO Eric Yuan said that before the pandemic, Zoom was using AWS for pre-meeting and post-meeting activities, but started using AWS servers for meeting traffic as the impact of the pandemic became clear.


Frustratingly, there's not quite enough information in this interview to really understand Zoom's architecture.  Zoom must be running multiple types of applications, from all kinds of applications for billing, for zoom chat, for participant activities, as well as streaming metadata about meetings for analysis and so on.

Of course, the core of the product is the video streams, and how those get sent between participants, especially if there is lots of participants, or in the webinar model, where you'd expect there to be some central media server digesting and processing the video feeds and sending them back out to participants.


## [The DevOps Reading List: Choosing your next DevOps book - Octopus Deploy](https://octopus.com/blog/devops-reading-list)

[https://octopus.com/blog/devops-reading-list](https://octopus.com/blog/devops-reading-list)

> You like books. You want to learn more about DevOps. Either you are new to the topic, or you are looking to expand your knowledge, but you’re overwhelmed by the options. It seems like everyone has an opinion, and you don't know where to start or what to read first/next.
> 
> Or perhaps you are already an advocate of DevOps, you want to recommend a book for a friend or colleague, but you aren’t up to date on the latest releases. Which book should you put under their nose?
> 
> This blog post is for you.


This really is a good post.  All of these books are great (disclaimer, I haven't actually read "Lean Software Development", I think it's the only one on the list I haven't, but I've had it recommended enough to agree that it should be on the list).

I think you should aim to read them all if you can, but the decision tree to help you decide is a nice touch.


## [Everything VPN is New Again - ACM Queue](https://queue.acm.org/detail.cfm?id=3439745)

[https://queue.acm.org/detail.cfm?id=3439745](https://queue.acm.org/detail.cfm?id=3439745)

> First, interactive user devices are effectively single-user operating systems because they allow only a single user at a time. The most extreme example of this is iOS—more than a billion active devices—which does not even support multiple user accounts on a single device. But even more traditional desktops and laptops have typically only one logged-in user. Rarer devices that support fast user switching can be configured so the VPN disconnects as one user and connects as another on a switch. The large shared Unix minicomputers with terminals are now interesting hobby projects, not typical corporate setups.
> 
> The second change is the near-universal virtualization of servers with virtual machines or container technology such as Linux namespaces. There are several forces driving this change and several ways it is achieved, but the result is the same: A server ends up running on a multiuser, multitasking Unix operating system with effectively a single-purpose process and one user.
> 
> In both of these cases, the result is that the operating system's virtual tunnel IP addresses now line up with service identities used for authorization. On end-user devices an IP address is a user, and in data centers each service instance has its own IP. With WireGuard ensuring every packet with a particular IP source is cryptographically linked to a verifiable identity, we can start safely making statements such as, "Address a is user u," which simplifies software development.


This is an interesting article, covering the history of VPN's and highlighting a few interesting points.

The first is that consumer VPN's are markedly different to traditional corporate VPN's, despite having the same name.  That's important to note and is true that they are focused on entirely different threat models and achieve different security properties.

I'm not so sure about the "rise of the single user operating system".  While you can consider an iOS device to be single user at any given time, there are numerous games and applications on my family ipad that don't cope with the fact that it's a shared device that many people use in the house.  It's the same problem as my Alexa and Spotify thinking that I like to listen to my kids taste in music just because they use the same devices.


## [Announcing LAMBDA](https://techcommunity.microsoft.com/t5/excel-blog/announcing-lambda-turn-excel-formulas-into-custom-functions/ba-p/1925546)

[https://techcommunity.microsoft.com/t5/excel-blog/announcing-lambda-turn-excel-formulas-into-custom-functions/ba-p/1925546](https://techcommunity.microsoft.com/t5/excel-blog/announcing-lambda-turn-excel-formulas-into-custom-functions/ba-p/1925546)

> Reusable Custom Functions
> With LAMBDA, you can take any formula you’ve built in Excel and wrap it up in a LAMBDA function and give it a name (like “MYFUNCTION”). Then anywhere in your sheet, you can refer to MYFUNCTION, re-using that custom function throughout your sheet. I’ll show a couple examples below.
> 
>  
> 
> Recursion 
> Reusable functions is reason enough to start taking advantage of LAMBDA, but there’s one more thing… you can do recursion. If you create a LAMBDA called MYFUNCTION for example, you can call MYFUNCTION within the definition of MYFUNCTION.


I don't think it's possible to overstate the important of this.  Spreadsheets honestly power the world, and software developers don't understand just how important they are to the rest of the business.

Well beyond the point that a developer would abandon a spreadsheet and turn to code, people all around the world continue building spreadsheet applications that sprawl and like feral software, run the company on users behalf.  

The amount of copy and paste errors, stupid mistakes and poor coding in them would make you weep, so an ability to define a custom function, easily and simply, means that you can easily create maintainable spreadsheets in future. 


## [The State of the Octoverse | The State of the Octoverse explores a year of change with new deep dives into developer productivity, security, and how we build communities on GitHub.](https://octoverse.github.com/#securing-software)

[https://octoverse.github.com/#securing-software](https://octoverse.github.com/#securing-software)

> A vulnerability can wreak havoc on your work and cause large-scale security issues. However, most vulnerabilities are actually from mistakes not malicious attacks.
> 
> 17%
> of vulnerabilities were
> explicitly malicious but
> triggered just 0.2% of alerts
> 
> 83%
> of remaining vulnerabilities are the result of mistakes


From a corpus of 521 security advisories, 17% of them were relating to explicit malicious behaviour on behalf of the dependant code.  The other 83% were in fact mistakes of some form.

However, of all of the alerts that Github sent, these malicious activities were just 0.2% of them, indicating that the size of the problem isn't as large as it can be made out to be.  Furthermore, its interesting to note that the majority of these malicious packages were in the npm package repository for node/javascript applications.

It's worthwhile reading the [full pdf report](https://octoverse.github.com/static/2020-security-report.pdf) as well for some more breakdown of the statistics and some background.


## [Shardul on Twitter: "I’ve had this card from @dpatil, chief data scientist for @BarackObama up in my room for a long time and thought I’d share. Dream in Years. Plan in Months. Evaluate in Weeks. Ship Daily. It applies to any and all industries. Thanks DJ. https://t.co/K1O42AzMLg" / Twitter](https://twitter.com/shardulgo/status/1333266768530341889)

[https://twitter.com/shardulgo/status/1333266768530341889](https://twitter.com/shardulgo/status/1333266768530341889)

> I’ve had this card from 
> @dpatil
> , chief data scientist for 
> @BarackObama
>  up in my room for a long time and thought I’d share. 
> 
> Dream in Years.
> Plan in Months.
> Evaluate in Weeks.
> Ship Daily. 
> 
> It applies to any and all industries. Thanks DJ.


Lovely strategy.  I shall be stealing this


## [The Global CTO Survey 2020 Report](https://www.stxnext.com/resources/cto-survey-2020)

[https://www.stxnext.com/resources/cto-survey-2020](https://www.stxnext.com/resources/cto-survey-2020)

> Answers from over 250 CTOs about their tech choices, management tactics, and current challenges
> Life in 2020 is more digital than ever, and technology leaders are racing to gain a competitive edge. At the heart of this race is the CTO, tasked with building the right teams and making the right decisions to make their company come out on top.
> 
> But you can’t succeed faster than the competition if you’re not sure if you’re going in the right direction. Every week is filled with decisions that could lead to long-term consequences. For each decision, a CTO would be right to ask: “are others in my position doing the same?”
> 
> If you want to stop flying blind and discover what other CTOs are doing, we have the answer.


Bearing in mind that just because everyone else is doing it, doesn't mean it's the right thing to do, but this report is an interesting read.

There's lots of interesting statistics, but the most interesting ones to me are the complete dominication of JavaScript as a language, the fact that most CTO's report at least 3 different languages in their stack, the 77% of orgs that are using cloud-native technologies (Public cloud and SaaS) and although a huge adoptions of cloud, agile, Devops, actually the fact that only 85% of orgs use Agile suggests that there's 15% that don't!

Finally of course, the 40% of organisations that task an external company to manage their security, meaning they are outsourcing their primary risk control.


## [Write five, then synthesize: good engineering strategy is boring.](https://lethain.com/good-engineering-strategy-is-boring/)

[https://lethain.com/good-engineering-strategy-is-boring/](https://lethain.com/good-engineering-strategy-is-boring/)

> To write an engineering strategy, write five design documents, and pull the similarities out. That’s your engineering strategy. To write an engineering vision, write five engineering strategies, and forecast their implications two years into the future. That’s your engineering vision.
> 
> If you can’t resist the urge to include your most brilliant ideas into the process, then you can include them in your prework. Write all of your best ideas into a giant document, delete it, and never mention any of them again. Now that those ideas are out of your head, your head is cleared for the work ahead.
> 
> Durably useful engineering strategy and vision are the output of iterative, bottoms-up organizational learning. As such, all learning contributes to your organization’s strategy and vision, but your contribution doesn’t have to be so abstract. Even if you’re not directly responsible for that work, your contribution, there are practical steps that you can take to advance your organization’s strategy and vision, starting right now.


This is good advice.  Partly it covers the Good Strategy, Bad Strategy recommendations that strategy cover diagnosis of the problem, guiding policy and coherant action, but also that you allow the strategy and vision to emerge from the organisational appropriate designs.

I'd add that I'd want to ensure that you've got a small amount of counter-intuitive thinking in there.  Look at your 5 designs, and not just where they are different, but look at what's the same, and see if you are doing something a certain way just because you always have.  Maybe your strategy should be to disrupt the thing that is consistent, because that'll change the way the organisation approaches design.


