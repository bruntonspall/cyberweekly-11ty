---
title: "69 - Fake news and adequate pernicious toerags"
date: 2019-09-14
description: "None of us like to believe that we can be defrauded, tricked or influenced.  There's a fascinating bias called \"unconscious bias bias\" which is where people can see and identify unconscious biases in others, but cannot see them in themselves."
permalink: /fake-news-and-adequate-pernicious-toerags/
---

None of us like to believe that we can be defrauded, tricked or influenced.  There's a fascinating bias called "unconscious bias bias" which is where people can see and identify unconscious biases in others, but cannot see them in themselves.

This means that we like to attribute bad things that happen to us to amazingly competent, mysteriously lucky adversaries of various forms.  It's far easier to say that we got defrauded by an organised criminal gang, rather than that we fell for a fairly simple fraud.

Jon quite rightly points out this week that I led last week with a story about attackers using deepfake style audio to mimic a known person and impersonate them, when it's far more believable to think that it was just someone doing a bad impersonation.  I read the story, and because I'm looking for interesting stories that cover the intersection of technology, fraud and cybersecurity, I picked it up and wrote about it.  As the article that Jon links to points out however, this is exactly how "fakenews" happens.  It doesn't need malicious intent or foreign state involvement, it can just be a case of misreporting, and people building and reporting on that which builds up and strengthens the belief that this thing happened.

A similar thing happened this week with [some questionable reporting from Buzzfeed](https://www.buzzfeed.com/alexspence/boris-johnson-dominic-cummings-voter-data) which claimed that there were secret plans to analyse users data of people accessing GOV.UK in a way that it wasn't before. Martin Robbins wrote [a great explainer](https://waitingforglados.com/robbins-martin/articles/is-gov-uk-part-of-a-brexit-conspiracy/) that shows just how the misunderstanding blew up, and how it then started to spiral out of control on twitter (and sadly wont die based on the people I follow).

But what does this mean for us?  As Jon points out below, we tend to overrate the competence and capabilities of our adversaries, as well as overestimate our importance or value to them.  We would rather build defences against the advanced persistent threats than worry about the real risks to our business.  Dr Ian Levy used to give a talk where he said that most "APT"'s weren't very advanced, gave up far too easily and aren't really a threat if you have even a basic line of defense.  He said that we should be calling them annoyingly pernicious toerags, because it's more representative of them.  I partly disagree in that I think there are real APT's out there, it's just that I think for most of us, we aren't really in their sights.  We might be collateral damage, but often we are one of many ways that they can achieve their aims, and like water, they will take the easiest route to where they want to go.  

The real pain is those annoying pernicious toerags, mostly because there's a lot more of them, and they make up a lot more of the real threats to our systems.  Business Email Compromise, Ransomware, self-spreading malware.  These are the things that are mostly likely to try to hit us, and the things we should worry about, rather than the sorts of things I highlight on a weekly basis, the deepfakes and the cool VPN bypasses.

## [Extended Validation not so... extended? How I revoked $1,000,000 worth of EV certificates!](https://scotthelme.co.uk/extended-validation-not-so-extended/)

[https://scotthelme.co.uk/extended-validation-not-so-extended/](https://scotthelme.co.uk/extended-validation-not-so-extended/)

> This seems crazy to me. As a security researcher with a little bit of interest in this field, I was able to find over 4,000 EV certificates that needed to be revoked, corrected and re-issued by the CA in question. Assuming an average cost of $250* per certificate, that's $1,000,000 worth of EV certificates that needed revoking. To top it off, these are the ones I'm talking about publicly because they've been reported to, and confirmed by, the CAs in question. I have another few batches with problems that are currently being worked through.
> 
> It's also not just me doing work like this and highlighting problems, there are others too. As I said at the beginning of the blog, it was Cynthia finding a problem that prompted me to look for a problem and many others before us too. For example, here's a heap of EV certificates issued to US companies in states that don't exist?!
> 
> It's really concerning that the whole point of an EV certificate is to contain reliable information yet with a little work I was able to find huge amounts of problems. According to Censys there are ~845,000 currently issued and unexpired EV certificates, meaning that just the ones mentioned in this blog post are ~0.5% of all EV certificates and they are invalid.


This smells to me.  As Scott says, the entire selling point of an EV certificate is that the certificate authority charges you more for it because they do some validation that you actually represent the company.

This could just be error prone manual processes that mean that certificates get issued with data in the wrong fields, but if there's an error prone manual process, then there is a gateway for fraud, and the entire point of EV certificates is that they are more trustworthy in theory.

It's stuff like this that makes me back ACME protocols and LetsEncrypt style certificate authorities.  If it's not a computer doing it, then it's far more error prone and subject to fraud


## [Data protection, data flows, and Brexit](https://afterbrexit.tech/data-protection/)

[https://afterbrexit.tech/data-protection/](https://afterbrexit.tech/data-protection/)

> In September 2018 DCMS published its guidance on what would happen to data protection in the event of a “no deal” Brexit. With the arrogance the sector has come to expect from Government, the report boasted that “[i]n recognition of the unprecedented degree of alignment between the UK and EU’s data protection regimes, the UK would at the point of exit continue to allow the free flow of personal data from the UK to the EU.”
> 
> In other words, “we’re alright, Jack.” That’s not the problem.
> 
> Information travelling in the other direction – from the EU to the UK – would become the responsibility of every recipient to create a legal structure to hold in lieu of what we took for granted under the single market. The guidance suggests that until an adequacy agreement is hammered out (assuming it ever is), organisations should look at standard contractual clauses, derogations, or the other commercial mechanisms normally associated with larger businesses and fully staffed legal departments.


There is a lot of confusion about what will happen after the UK leaves the European Union to companies in the tech sector and the legislation that affects them.  [Heather](https://www.twitter.com/webdevlaw) has been doing a great job on twitter of tracking some of the biggest issues and put together this site, which is a little ranty at times, that highlights some of the biggest issues, and what clarity or progress there is on each issue.


## [Science Wizards Work Magic at CIA | SIGNAL Magazine](https://www.afcea.org/content/science-wizards-work-magic-cia)

[https://www.afcea.org/content/science-wizards-work-magic-cia](https://www.afcea.org/content/science-wizards-work-magic-cia)

> This past summer she launched the Senior Technical Service effort to ensure technologists know they are appreciated and have a clear career path forward. “We laid out career pathing and things like that to emphasize for our senior technical corps that we value them and that this is really, really important. It’s not just technology development,” she reports. “If you have operations expertise, if you’re a targeting expert, if your expertise is programs and plans, all of these things are vitally important to us in order to be successful, and we want to make sure to let people know they can reach the highest levels of government staying in their technical expertise area.”
> 
> The initiative is modeled after the Senior Analytic Service launched about 20 years ago by the agency’s Directorate of Analysis. That effort provides a senior career path for experienced analysts who may not necessarily want to move into management positions. “We’re leveraging their lessons learned as we stand up our Senior Technical Service. We’re trying to do the same thing with our technologists to show that they can rise to the most senior levels of government by being, let’s say, a battery expert or whatever the particular discipline or tradecraft area is.”
> 
> She also has enlisted a team of senior agency officers to examine how well the directorate is integrated across the agency. “More and more, everything is underpinned and enabled by technology, so it’s really important for us to be early in the discussions in terms of how we go after specific intelligence challenges. We want to be certain that we are engaged in those conversations as early as possible and in the most productive way possible,” she asserts. “Anything they want to recommend is on the table. Nothing is off the table, other than the director said we’re not going to do a reorganization.”


An interesting if slightly light on details article about the technical services at the CIA.  But what struck me here is that even the CIA has had to look at technical career advancement, and decide on a two track career progression.  That people with highly technical skills can advance, be paid increasing amounts based on their technical expertise, not based on their seniority in the organisation or the number of people that they have to manage.


## [Men arrested for breaking into Iowa courthouse were hired to test security](https://eu.desmoinesregister.com/story/news/crime-and-courts/2019/09/11/men-arrested-burglary-dallas-county-iowa-courthouse-hired-judicial-branch-test-security-ia-crime/2292295001/)

[https://eu.desmoinesregister.com/story/news/crime-and-courts/2019/09/11/men-arrested-burglary-dallas-county-iowa-courthouse-hired-judicial-branch-test-security-ia-crime/2292295001/](https://eu.desmoinesregister.com/story/news/crime-and-courts/2019/09/11/men-arrested-burglary-dallas-county-iowa-courthouse-hired-judicial-branch-test-security-ia-crime/2292295001/)

> The men, outfitted with numerous burglary tools, told authorities they were on contract to test out the courthouse alarm system's viability and to gauge law enforcement's response time, an alleged contract that Dallas County officials said they had no knowledge of, according to a criminal complaint.
> 
> Authorities later found out the state court administration did, in fact, hire the men to attempt "unauthorized access" to court records "through various means" in order to check for potential security vulnerabilities of Iowa's electronic court records, according to Iowa Judicial Branch officials.
> 
> But, the state court administration "did not intend, or anticipate, those efforts to include the forced entry into a building," a Wednesday news release from the Iowa Judicial Branch read.


This story doesn't sound right to me.  The golden rule of physical penetration testing is to have a very good scope, well defined and with hard edges.  They should definitely have possessed a letter that explained what they were doing, why they were doing it and with instructions on who to contact who had authority to allow them to do it.

This could just be a case of poor planning or miscommunication, but I also wonder if it's a highly embarrassed county official pushing to try to prevent the state doing this sort of thing to them in future. 


## [Opinion | I Work for N.S.A. We Cannot Afford to Lose the Digital Revolution. - The New York Times](https://www.nytimes.com/2019/09/10/opinion/nsa-privacy.html)

[https://www.nytimes.com/2019/09/10/opinion/nsa-privacy.html](https://www.nytimes.com/2019/09/10/opinion/nsa-privacy.html)

> But that is precisely when we must put in place a new foundation for dealing with the even more profound and enduring implications of the digital revolution.
> 
> That revolution will sweep through all aspects of our society so powerfully that our only chance of effectively grappling with its consequences will lie in taking bold steps in the relatively near term. In short, our attention must turn to a far more complex set of threats of multiple dimensions enabled by the digital revolution. While the potential consequences are less catastrophic than nuclear war, they are nonetheless deeply threatening in a range of ways we will have trouble countering.
> 
> There are four key implications of this revolution that policymakers in the national security sector will need to address:
> 
> The first is that the unprecedented scale and pace of technological change will outstrip our ability to effectively adapt to it. Second, we will be in a world of ceaseless and pervasive cyberinsecurity and cyberconflict against nation-states, businesses and individuals. Third, the flood of data about human and machine activity will put such extraordinary economic and political power in the hands of the private sector that it will transform the fundamental relationship, at least in the Western world, between government and the private sector. Finally, and perhaps most ominously, the digital revolution has the potential for a pernicious effect on the very legitimacy and thus stability of our governmental and societal structures.


This is a great essay, and probably worth reading twice to make sure you get it all.

It sums up the problems facing the NSA and other signint agencies in the world, primarily that of disruption.  Government agencies aren't known for moving fast, and as Mr Gerstell describes it, technology advancement is moving far faster than government policy can possibly keep up.

For an organisation tasked with oversight, intelligence gathering and defense of a nation, that creates an issue that it's adversaries might be able to make use of some of these technologies and the implications of them before the lumbering giant of an organisation has even noticed that they exist.


## [Female spy to net terrorists as head of ‘cyber‑SAS’ | News | The Sunday Times](https://www.thetimes.co.uk/edition/news/female-spy-to-net-terrorists-as-head-of-cyber-sas-jdxv7bv2m)

[https://www.thetimes.co.uk/edition/news/female-spy-to-net-terrorists-as-head-of-cyber-sas-jdxv7bv2m](https://www.thetimes.co.uk/edition/news/female-spy-to-net-terrorists-as-head-of-cyber-sas-jdxv7bv2m)

> Britain’s eagerness to expand its cyber-warfare operations follows a series of state-sponsored attacks against the UK in the past two years, including a hacking attempt on parliamentary email accounts in June 2017 by Iran. The regime’s hackers repeatedly tried to access 9,000 accounts but compromised only about 30.
> 
> The agency, which will have a budget of about £250m at launch, will initially be staffed by more than 500 hackers with a plan to expand its workforce to 3,000 people over the next decade. It will expand on Britain’s existing national offensive cyber-programme, which is run from GCHQ’s headquarters in Cheltenham.


That's a lot of "hackers" to attempt to hire.  One has to start to wonder what you can do with 3,000 professional cybersecurity staff as part of an offensive program?  Clearly the goals, mission and aims of the organisation are going to remain classified, but the size of it, and the fact that it's associated almost entirely with an offensive cyber program is interesting.  I wonder how many staff and budget is associated with an equivalent cyber defensive program?


## [Policy debt | Chris Swan's Weblog](http://blog.thestateofme.com/2019/09/04/policy-debt/)

[http://blog.thestateofme.com/2019/09/04/policy-debt/](http://blog.thestateofme.com/2019/09/04/policy-debt/)

> A primary purpose for this post is to put out a statement I’ve been using in discussions for the past few years:
> 
>    Any company that wrote its security policy prior to the advent of SSH is doomed to do with firewalls things that should be done with encryption
> 
> [...]
> 
> A few years back CESG and NIST decided (within a few weeks of each other) that periodic password cycling wasn’t helpful, and changed their guidance accordingly. They now advise that passwords should only be changed when their is evidence of compromise.
> 
> The best practice has changed, but largely the policies have not. In part this is inertia, and in part it is fear that a change in policy might violate some compliance requirement. The problem here is that regulators have a nasty habit of using practice by value rather than practice by reference, so there will be cases where the older NIST or similar guidance has been hard coded. This is compounded by the fact that most published policy demands ‘what’ (and sometimes ‘how’) without bothering to explain ‘why’, so the threads of connection to the regulation that shaped policy get cut, making it much harder to determine the impact of a policy change.


This concept of policy inertia as much as policy debt is a lovely one.  The problems described are exactly real, but I can see that in many cases, policies that tell you the why become too fluffy and unusable.  We need to somehow strike a balance between explaining the ‘why’ to the people for whom it matters, while still providing the ‘what’ and ‘how’ for people who do not have the time or wherewithal to reason out the ‘what’ and ‘how’ from the ‘why’


## [Why phones that secretly listen to us are a myth - BBC News](https://www.bbc.co.uk/news/technology-49585682)

[https://www.bbc.co.uk/news/technology-49585682](https://www.bbc.co.uk/news/technology-49585682)

> The results won't surprise those in the information security industry who've known for years that the truth is that tech giants know so much about us that they don't actually need to listen to our conversations to serve us targeted adverts.
> 
> The reality is that advertisers have sophisticated ways of profiling users.
> 
> Location data, browsing history and tracking pixels, for example all provide enough information to predict what you might be thinking about buying.


I’ve heard this from plenty of my friends.  “I talked about needing cholesterol drugs, and then the next day, adverts for cholesterol pills were on my Facebook feed”.

This is a good example of the [Baader-Meinhof effect](https://science.howstuffworks.com/life/inside-the-mind/human-brain/baader-meinhof-phenomenon.htm), most commonly referred to as when you buy a new car, you suddenly notice a lot of them on the road.  Obviously, there is no change in the frequency of said cars, but you are now noticing or spotting them in a way that you didn’t before.  We often see irrelevant or useless adverts, but we ignore them.  Only once our attention is drawn to a thing, do we start seeing the adverts some more. 


## [Deepfake AI or Shallow Fake News?](https://medium.com/@TalBeerySec/deepfake-ai-or-shallow-fake-news-233ac59663d2)

[https://medium.com/@TalBeerySec/deepfake-ai-or-shallow-fake-news-233ac59663d2](https://medium.com/@TalBeerySec/deepfake-ai-or-shallow-fake-news-233ac59663d2)

> Interestingly, and perhaps counterintuitively, it seems like all parties involved in this story are biased towards preferring the deepfake AI narrative:
> - The victims (both the UK CEO and his company): Falling for a regular social engineering attack is embarrassing. Falling for a “deepfake AI scam” sounds like a “force majeure” and helps them save face.
> - The media: regular social engineering attack is boring. Deep fake AI? exciting!
> - The insurance company: They are the big winners! They get free, very positive PR for the firm itself in major publications. They are the good guys that paid in full and saved the day. Furthermore, they are promoting their offering. A CEO reading the story would certainly consider the option to buy such insurance against such a “force majeure” attack.
> Another major reason to be suspicious in this case is the fact that the story was reported by the insurance company, and no external source (e.g. law enforcement) has confirmed the stated facts.


(Jon) Michael linked to the [original 'deepfake AI scam' story](https://www.washingtonpost.com/technology/2019/09/04/an-artificial-intelligence-first-voice-mimicking-software-reportedly-used-major-theft/) in last week's edition. This intimated that for the first time voice mimicking technology had been used to spoof an authorisation for a financial transaction, leading to a substantial loss for the victim. 

At the time I read it, I remember wondering how the various parties involved could be so confident it was DeepFake AI, as opposed to say, Rory Bremner ringing up and pretending to be the boss. 

The details are still slightly sketchy but the subsequent, more thoughtful, reporting on this incident has posed some good questions on what actually happened, and makes it seem far less likely to be tech-related. There's a parallel into the cyber security world here - if we get hacked, it's human nature to say it was Advanced Persistent Threats, throwing chains of zero-days at us in a humint-enabled blended attack, and not that we forgot to change a default password and left RDP open. Could it have theoretically been DeepFake AI? Possibly. Was it more likely to be someone chancing their arm? Almost certainly.



