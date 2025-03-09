---
title: "87 - How much of a target are you?"
date: 2020-02-01
description: "Our ego likes to tell us that we are special, that attackers have carefully picked out organisation out of millions of others, that they have taken the time and energy to research us online, get to know our executives, our staff, our technologies before striking."
permalink: /how-much-of-a-target-are-you/
---

Our ego likes to tell us that we are special, that attackers have carefully picked out organisation out of millions of others, that they have taken the time and energy to research us online, get to know our executives, our staff, our technologies before striking.

In reality, many cyber actors out there just don't really care who their targets are, at least in phase 1 of the attack, and often even in the later phases.  

They search for potential targets by looking for vulnerable services online, and then once they've found one they get in and do their thing, somewhat regardless of who we are and what we actually care about.

Traditionally, threat modelling starts with our data, the things that make us special, and then we work out how someone might steal it.  Is someone going to take over the secretary of states account?  Attackers want to read the obituary that the newspaper wrote.  Attackers *must* know we process billions in payments, and want to steal it.

If we look at Travelex for example, with all the good guesses pointing at them being significantly hit by REvil or one of its contemporaries.  If that criminal gang had access to the entire internal systems of a major financial system, then they probably had the ability to create orders for money, turning them into a giant ATM for the criminals to withdraw money.  

If you were an attacker looking for that kind of thing, someone like Travelex is exactly who you would look for.  But in reality, it looks like the attackers didn't really know what they had got.  All they wanted was execution rights on as many computers as possible so they could encrypt them and ransom them.

Risk management often takes entirely the wrong approach in this area.  We start with our data, with what makes us special and then assume that attackers want to get at it.  There is a better way.

You may have seen that the NCSC's new measures for understanding the impact of high risk vendors in telecoms uses attack trees as a risk assessment and control methodology.

Attack trees help us to model our system based on  the sorts of goals that attackers might have, and then apply attacker profiles against the tree to determine the  most likely route that they will take to achieve their goals.

Most importantly, in my experience, building attack trees tends to show you that if you have simple vulnerabilities, that almost all attackers, regardless of how much they care about your specific special data, will use them and therefore pose the greatest risk.

Even if you think you are special, most attackers don't think you are special, you are simply the next line in their list of targets, and if you are not vulnerable to basic attacks, they'll mostly just move on.


## [A Chaos Test too far… - FT Product & Technology - Medium](https://medium.com/ft-product-technology/a-chaos-test-too-far-6405c2cc4bbb)

[https://medium.com/ft-product-technology/a-chaos-test-too-far-6405c2cc4bbb](https://medium.com/ft-product-technology/a-chaos-test-too-far-6405c2cc4bbb)

> So, thankfully the crisis was averted. Phew! Despite being totally stressful to deal with, when we reflected on the incident afterwards, there were a lot of positives we could take from it. We had learned so much about what we did and didn’t know and as a result were able to identify areas for improvement. It also demonstrated that we had been able to pull together and work really effectively as one team. We felt proud of how we responded.
> These are some of the things we learnt and some of the changes we suggested:
> 
> * We now back-up the database much more frequently.
> * Confusing Heroku database names had made the mistake too easy to make so we changed them to be super clear, STAGING and PRODUCTION.


Yes, I know.  You run thousands of databases, with thousands of different projects, so you really want to call projects things like a719-s213 so it lines up with the cost center codes that finance hand out.

The main reason to use sensible names for things is that it reduces the chances of things like this from happening.  I recommend that all names begin with the environment, so prod-X, or test-X, or devmbs-X.

Secondly, access to production should always be really clear to users.  If you are doing a release/database change/logging on, whatever, you should have big visual warnings that you are doing it to production if possible.  

It's also nice to see admissions of mistakes, how it was resolved, and a great "no-blame" culture here.  Note that no-blame doesn't mean not naming the people involved, it means acknowledging that this was a mistake that anyone could have done, and learning from that to ensure that it doesn't happen in the future.


## [Detection Engineering using Apple’s Endpoint Security Framework](https://posts.specterops.io/detection-engineering-using-apples-endpoint-security-framework-affdbcb18b02)

[https://posts.specterops.io/detection-engineering-using-apples-endpoint-security-framework-affdbcb18b02](https://posts.specterops.io/detection-engineering-using-apples-endpoint-security-framework-affdbcb18b02)

> For Windows techniques, our team’s tool of choice for building detections is Sysmon. It is free, easy to install in a lab environment, provides decent coverage of various actions that could take place on a Windows system, in addition to the ability to ingest its data into a centralized analytic platform such as an ELK stack.
> 
> For macOS, I have not found a solution comparable to what Sysmon provides in relation to the data contained in events. Osquery is excellent for querying the state of an endpoint at a given point in time however, it lacks real-time contextual data. At Apple’s Worldwide Developers Conference (WWDC) last year, the Endpoint Security Framework (ESF) was introduced, which “monitors system events for potentially malicious activity.” The Endpoint Security Framework is a C API which is part of the broader System Extensions Framework. My excitement rose when I discovered the types of events ESF covers.


Nice tool and demonstration of how to use it.  Sysmon is indeed excellent, and I strongly recommend organisations to implement endpoint monitoring using sysmon and the [Swift on Security ruleset](https://github.com/SwiftOnSecurity/sysmon-config) as soon as possible.  The number of events is reasonably low per device (single digit MB per day in many cases), and there are [good patterns for collecting those events easily](https://github.com/ukncsc/lme).

However, OSX clients sometimes get left out of this tooling.  It's nice to see that OSX is catching up, and if you have a set of your staff using Mac's, the [AppMon tool](https://bitbucket.org/xorrior/appmon/src/master/) referenced further down merits investigating.


## [Government to strengthen security of internet-connected products - GOV.UK](https://www.gov.uk/government/news/government-to-strengthen-security-of-internet-connected-products)

[https://www.gov.uk/government/news/government-to-strengthen-security-of-internet-connected-products](https://www.gov.uk/government/news/government-to-strengthen-security-of-internet-connected-products)

> The plans, drawn up by the Department for Digital, Culture, Media and Sport (DCMS), will make sure all consumer smart devices sold in the UK adhere to the three rigorous security requirements for the Internet of Things (IoT).
> 
> These are:
> 
> * All consumer internet-connected device passwords must be unique and not resettable to any universal factory setting
> 
> * Manufacturers of consumer IoT devices must provide a public point of contact so anyone can report a vulnerability and it will be acted on in a timely manner
> 
> * Manufacturers of consumer IoT devices must explicitly state the minimum length of time for which the device will receive security updates at the point of sale, either in store or online


You might have missed this with all the telecoms news, but this is really good news overall.  The big question for this regulation is about how it will be enforced, and the penalties for not having it.  The second question is how it will affect importers and internet marketplaces and shops like Amazon, especially those that stock third party products.

But this should reduce the chances of the next Mirai being caused by thousands of unpatched devices.  (Additionally, if your Sonos speaker had come with a defined limetime, maybe people would be less cross about Sonos deprecating the original devices?)


## [Scaling Security in Software Development: The Art of Possible](https://securityintelligence.com/posts/scaling-security-in-software-development-the-art-of-possible/)

[https://securityintelligence.com/posts/scaling-security-in-software-development-the-art-of-possible/](https://securityintelligence.com/posts/scaling-security-in-software-development-the-art-of-possible/)

> Acme can have someone on each of their development teams with application security as one of their in-depth specialties.
> 
> Crucially, this won’t be their only skill, so it is not necessary to ensure there is enough security work to occupy these champions with nothing but security tasks full time; they can do other tasks in the true spirit of an agile team. In fact, it is crucial for the success of the security champions approach that they do other tasks on the team. This gives them expertise in the context of a specific application, enabling better security decisions. Equally important is the other constraint: Security champions cannot do all the security work on the team. Part of the role is to gradually raise the security skills of everyone else, so pairing and sharing are important.


I like the security champions approach.  I know other organisations who have used this approach as well.  A critical thing to getting success out of this is that you need your developers to actually have the time to do these things.  It's not enough to tell them that they have additional responsibilities, you need to actively carve out dedicated time for them, and protect that time from the hungry product managers, delivery manaers, project managers and the rest of the organisation that wants their time.

Also be honest with people up front.  Some people become developers, because shockingly enough, they enjoy writing code.  Being asked to interview, manage junior developers, groom the backlog, write blog posts, give talks at conferences all takes time away from their primary passion.  Don't take people who are doing this because they suck at their main job, or just want more money.  They need to have a passion for this, and they should be prepared to spend at least 1/3 of their time being the "security champion" alongside their existing work if not more.


## [Numbers Corrupt; Complex Numbers Corrupt Absolutely | Darrell Mann](https://darrellmann.com/numbers-corrupt-complex-numbers-corrupt-absolutely/)

[https://darrellmann.com/numbers-corrupt-complex-numbers-corrupt-absolutely/](https://darrellmann.com/numbers-corrupt-complex-numbers-corrupt-absolutely/)

> The straw that broke this camel’s back was a mini-case study concerning Wal-Mart, and Phillips’ praise for the not-so-bright spark who’d calculated the ‘cost’ of every minute a delivery truck was at the unloading bay waiting to be unloaded. I have a feeling this kind of mis-guided thinking is why so many employees are actively dis-engaged from their work and trust in corporations is at a historic low. Everybody is on the clock. The drivers get stressed. The truck unloaders get stressed. Job satisfaction takes a downward turn. Employees feel out of control. They feel ‘its not fair’ when things go wrong that have nothing to do with them.
> 
> [...]
> 
> The simple truth is this. Working out the ‘cost’ of waiting delivery trucks is a simple response to what is in reality a complex problem. Moreover, it is one of the thousands of other wrong simple solutions to a complex problem.
> 
> If a system includes two or more humans, it is complex. And, given that almost every measurement in existence is done by one human on another, almost every ‘measurement problem’ is complex.
> 
> And if that is the case, any measurement situation demands new rules of behaviour. None of which will be found in Jack Phillips book. First of all, there are no absolutes any more. This means there is little point in quantifying things. Far better instead to be looking out for relative changes, for ‘vectors’ and ‘rules of thumb’. None of which are popular with today’s bean-counters, granted, but that’s a lesson they’re going to have to learn. Most likely the hard way.


I'm a big fan of measurement, of OKR's, of the quantified self approaches to things.  What can be seen and measured can be acted upon is a good mantra.

But it's critical that we realise that even the act of measuring has an impact.  I lose weight through tracking my food consumption not because with better numbers I can pick lower calorie meals, but because by making it a conscious act to add food to my daily meal planner, I make a choice about eating that donut, or the third donut in many cases!

This idea that there are areas where we cannot intrinsically measure them, or at least that our measures will have unexpected responses is a good one.  Where complicated systems interact, instead of seeking absolute measures, we should be seeking to understand the impact of our actions by measuring the changes we make, both quantitatively and qualitatively.


## [Identity and Access Misstep: How an Amazon Engineer Exposed Credentials and More](https://www.upguard.com/breaches/identity-and-access-misstep-how-an-amazon-engineer-exposed-credentials-and-more)

[https://www.upguard.com/breaches/identity-and-access-misstep-how-an-amazon-engineer-exposed-credentials-and-more](https://www.upguard.com/breaches/identity-and-access-misstep-how-an-amazon-engineer-exposed-credentials-and-more)

> Discovery
> 
> On 13 January at approximately 11am, the UpGuard Data Leaks detection engine identified a GitHub repository with potentially sensitive information that had been uploaded half an hour earlier. Shortly after noon an analyst began reviewing the contents of the repository. After assessing the contents to establish the scope of the data, its degree of sensitivity, and the identity of the owner, the analyst notified AWS Security at 1:18pm. By 4pm, the repository was no longer publicly accessible, and at 4:45pm AWS Security replied to the initial notification email saying that they had taken action.


In terms of incident response speed, this was impressive.  AWS security know how to triage an incident and deal with it effectively.

However, AWS's continuing insistence that no customer data was even potentially breached is more troubling.  From the reports, there was enough stuff here to pivot through the users account and see more than was just in the github repository (such as their AWS root key).

I know legally they can't say "we don't know, and probably will never know if anyone adversarial actually did this remote thing.  We think it's unlikely, so you are in all probability totally fine, but it was a possibility", but I'd much prefer it if we were more honest about many breaches.  Lots of data breaches are of the form of "we detected this bad thing, it had the potential to be really bad, but we were lucky and it wasn't", and I wish that the ICO and press in general were more accepting of that.


## [Inside Monzo's strategy to be the UK's most reliable bank | Computerworld](https://www.computerworld.com/article/3488802/inside-monzos-strategy-to-be-the-uks-most-reliable-bank.html)

[https://www.computerworld.com/article/3488802/inside-monzos-strategy-to-be-the-uks-most-reliable-bank.html](https://www.computerworld.com/article/3488802/inside-monzos-strategy-to-be-the-uks-most-reliable-bank.html)

> Evans' approach to boosting resiliency across this stack starts with mapping any potential issues or pinch points which need to be addressed if Monzo is to reach the lofty standards he is aiming for.
> 
> This involves a shift towards a cell-based architecture, an emerging model for highly scalable environments, where services can be carved up in a way that can "limit the blast radius" when incidents inevitably occur.
> 
> He asked: "How do we make it really, really difficult for any one change to bleed out and affect anything more than that specific component that it is changing?"
> 
> This means splitting up any areas of dependence so that any negative impacts only affect a small area of banking functionality, rather than all services and customers.


This cell based architecture is both good from a resiliance perspective, but also from a security perspective.  If you know that servers A, B and C are used for function Z, then server F suddenly talking to the database in that cluster is a sign of something going wrong.  
Additionally, if an attacker does compromise a server, hopefully the firewall rules and networks should prevent them from moving outside the functional zone.


## [Tracking REvil](https://www.kpn.com/security-blogs/Tracking-REvil.htm)

[https://www.kpn.com/security-blogs/Tracking-REvil.htm](https://www.kpn.com/security-blogs/Tracking-REvil.htm)

> This research started by tracking REvil samples distributed via pastebin. The configuration extracted from these samples show a different strategy of the several affiliates. Detonating these samples in a sandbox and emulating traffic to the ransom site gave us the ability to track ransom demands per group and campaign. Analyzing the configuration of the different samples made us realize the C2 domains were identical across all samples. The team was able to sinkhole multiple REvil C2 domains1. The REvil C2 traffic is unidirectional and solely used for statistics. Piggybacking the C2 we can gain insight into the statistical data.
> 
> The affiliates using the REvil ransomware as a service (RaaS) are skilled and adapting their approach to the victim’s organization. We assume the attacks are often not targeted but more opportunity based. Access that is gained in some way is later escalated in order to take over an entire network. In the past 5 months we've analyzed over 150 000 unique infections, extracted ransom demands from 148 samples together demanding more than 38 million dollars. Some of the attacks are on a huge scale. Just in the last 7 days the REvil affiliates were able to encrypt over 6500 unique systems in two mayor attacks in both Europe and Africa. Topping all infections combined in the past 30 days.
> 
> [...]
> 
> The map also shows how quiet it is in Russia only seeing a couple of unique infections. The malware itself checks the system language and online adverts by the REvil RAAS providers also states no operation inside of the Commonwealth of Independent States (CIS). The limited number of infections can be attributed to testing of the ransomware or employees on a business trip inside of Russia.


"Opportunity based".  We spend a lot of time in cyber security talking about people targeting us.  But we forget that some of the biggest operations (and REvil/Sodinokibi is pretty big) are literally the cybersecurity equivalent of muggers waiting in the slightly dodgy area of town.  Their scattergun approach means that if you are even reasonably secure, they'll just move on.

I'll add that the note about it not operating in Russia is interesting. It's been long alleged that Russian authorities are slow to move on major criminals operating from within Russia providing they are not attacking russian services, and this seems to show that, at least, the criminal group behind this either believe this to be true, or want everyone to think they are Russian.


## [NCSC advice on the use of equipment from high risk vendors in UK telecoms networks - NCSC](https://www.ncsc.gov.uk/guidance/ncsc-advice-on-the-use-of-equipment-from-high-risk-vendors-in-uk-telecoms-networks)

[https://www.ncsc.gov.uk/guidance/ncsc-advice-on-the-use-of-equipment-from-high-risk-vendors-in-uk-telecoms-networks](https://www.ncsc.gov.uk/guidance/ncsc-advice-on-the-use-of-equipment-from-high-risk-vendors-in-uk-telecoms-networks)

> For many years, NCSC has helped operators to manage the use of vendors that pose a greater national security risk. As part of the SCR, NCSC has fed in a non-exhaustive list of criteria which NCSC applies when identifying vendors as HRVs. These non-exhaustive criteria are:
> 
> a.  The vendor’s strategic position/scale in the UK network;
> 
> b.  The vendor’s strategic position/scale in other telecoms networks, in particular if the vendor is new to the UK market;
> 
> c.  The quality and transparency of the vendor’s engineering practices and cyber security controls;
> 
> d.  The past behaviour and practices of the vendor;
> 
> e.  The vendor’s resilience both in technical terms and in relation to the continuity of supply to UK operators;
> 
> f.  A number of considerations relating to the ownership and operating location of the vendor, including:
> 
> i.  The influence which the domestic state apparatus can exert on the vendor (both formal and informal);
> 
> ii.  Whether the relevant domestic state and associated actors possess an offensive cyber capability that might be used to target UK interests;
> 
> iii.  Whether a significant component of its business operation is subject to domestic security laws which allow for external direction in a manner that conflicts with UK law.1
> 
> There is no exhaustive list of which vendors NCSC would consider HRVs under these criteria; we would encourage operators who are considering introducing new vendors into their networks to discuss that with us as soon as possible.


This list makes up a decision framework for government to determine who are "high risk vendors".  In theory, both government and private enterprises could use this list as part of their supply chain assurance models to determine which of their vendors are high risk, and apply similar risk management controls.

The problem with this list is that if you squint at it enough, you realise quite quickly that very few vendors are actually likely to give good responses to most of these answers.  I've worked with a number of big systems integrators who have key strategic positions in UK government systems, have terrible engineering practices with no oversight, have behavioural problems, and for whom there is little alternative for many organisations.  Should these organisations be considered high risk vendors?  

This framework, if it lives to be something more than a stick to beat Huawei with, could be reapplied across the entire government technology sectors and I don't feel like the results would be good


## [The future of telecoms in the UK - NCSC](https://www.ncsc.gov.uk/blog-post/the-future-of-telecoms-in-the-uk)

[https://www.ncsc.gov.uk/blog-post/the-future-of-telecoms-in-the-uk](https://www.ncsc.gov.uk/blog-post/the-future-of-telecoms-in-the-uk)

> Security isn’t like a light switch; it's not something you can simply switch on or off. You need to know what you care about the most and who you’re defending it against to judge how much effort to put into your various security controls, more like a dimmer switch you can dial up and down in different areas. Normally, that’s done using a threat model. The threat model for UK telecoms operators ranges from hostile states (for example, the attack by the Russian state-sponsored cyber actors targeting network infrastructure devices) through to organised crime and petty fraudsters. In order to know what you need to defend, you need to know how the networks can be attacked. A good way of codifying that is an ‘attack tree’, also known as a ‘threat tree’.
> 
> An attack tree is not that complex, at least in concept. You have a goal at the root of the tree and then each path to the leaves of the tree is a route to attain that goal. 


This is a great blog, showing a lot of the thinking behind the UK Government's decision to classify Huawei as a High Risk Vendor, and therefore apply a set of risk managed controls (such as no more than 35% of the network, and no presence in certain security components in the core etc).

What I like about this blog is that it really summarises how they did the threat modelling, how they turns the simple attack tree into something bigger, something more, and then how they built their controls around those attacks.  It does this in plain english that pretty much anyone should be able to read.  If you want to know more about how the specifics of those controls within the context of 5G, then reading the ["summary" of the security analysis of the telecoms sector](https://www.ncsc.gov.uk/report/summary-of-ncsc-security-analysis-for-the-uk-telecoms-sector) is well worth your time.


