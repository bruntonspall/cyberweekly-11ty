---
title: "152 - Learning from the best"
date: 2021-06-07
description: "I learn best from my mistakes."
permalink: /learning-from-the-best/
---

I learn best from my mistakes.

It might just be me that's a bad learner, but I suspect that this is true of many of us.

There's two things wrong in this statement, that I learn from my *mistakes* and that I learn from *my* mistakes.

We tend to think that we learn fast from the mistakes we make.  But the reason that we do so is because we have an immediate feedback loop that tells us that something teachable just happened.  

I was talking to one of my reports recently and saying that despite writing over 150 Cyberweekly's, along with all the commentary, I don't think my writing is actually getting better.  I said "With all the practice, you'd think I'd get better at it" and his response was "But you aren't practicing.  If you don't get feedback about whether it's any good, it's not really practice".

The way that we learn from mistakes is based on this feedback loop.  But because we are the ones who feel the pain, it means that while we can vicariously enjoy other peoples mistakes we tend not to actually learn from them.

So how can we learn from other people?  It turns out that many organisations have been doing things pretty well in a bunch of places, and they write about it a lot.  As well as reading the links this week, why not take the time to actively ask the following questions:

* Is any of this applicable to my situation now?
* Is there anything I can takeaway from this?
* Can I implement or change something because of this?

## [ELIS: The U.S. government’s messy attempts to digitize the immigration system.](https://slate.com/technology/2021/04/elis-uscis-digital-immigration-system.html)

[https://slate.com/technology/2021/04/elis-uscis-digital-immigration-system.html](https://slate.com/technology/2021/04/elis-uscis-digital-immigration-system.html)

> But ELIS 2 faced an even bigger problem in the agency’s assumption that digital would unquestionably be better than paper.
> 
> This article of faith turned out to be disastrously wrong.
> 
> In some cases, based purely on the task someone was looking to complete, paper was superior to digital because it was faster and more accurate. Lefler sounded a bit awestruck as he recounted watching immigration officers work their way through immense case files, searching specifically for aliases that an applicant might have used. Some applicants use multiple names for cultural reasons, so this is an issue that comes up quite a bit, but immigration officers have developed a simple system for resolving it. As Lefler explains:
> 
> They will put a little thing on their thumbs so that they can rifle through a giant pack of documents very quickly. The operator has memorized anything that is a government-looking document, that might have a name on it. As they see a document at a glance that’s probably going to have a name on it, they’ll check the name and then they’ll continue rifling through it. They go through giant stacks of paper extremely fast. There was no way to implement that electronically, short of five years of machine learning and OCR [optical character recognition] technology. It cannot be done.
> A common mistake people make when trying to improve or modernize something is believing that digital will always be better. But digitizing a broken paper process doesn’t make it better. Sometimes it even makes it worse. In the case of ELIS, the team members believed their job just was to take what was on a form, digitize it, and call it done—there was no place adding sticky notes or placing the folder in a special filing spot based on where it needed to go next. They did not factor in the colossal amount of filing, categorizing, and handwritten note making that the people processing forms did on a daily basis.
> 
> [...]
> 
> Rodriguez says he wishes he could have had something like a technology translator to lay out significant issues in nontechnical terms—a dedicated senior person to be his ELIS liaison, in the way government officials often have policy liaisons. But there was no one at USCIS to play that role. In fact, the role doesn’t normally exist, because it is only relatively recently that technology has become the common medium for policy delivery.
> 
> According to Rodriguez, “You [need to] have somebody at a very senior management level who understands what’s going on with the technology development and can translate it for you. In retrospect, I would have wanted to have somebody around who was consistently available, watching what was going on with those issues.”
> 
> The gap that Rodriguez identifies is one that many public sector organizations struggle with as technology plays an ever-increasing role in how the world conducts business—how to oversee a technology project if you have never done so before and lack technical knowledge. Rodriguez’s suggestion that agencies establish a technology translator–type role would certainly solve this problem, and it is an idea we have brought before Congress.


A fascinating if depressing read.  My experiences at GDS are equally filled with hubris, where we made assumptions that digital would be better.  The best of the people I worked with rapidly worked out that this was often not the case and did the hard work to go see what the manual processes were, and to then see how digital solutions could fit the actual requirements.  The worst of my coworkers simply got into raging arguments about devops and agile as if winning the ideological argument was the only thing that mattered.

The final bit about the director realising that he had ownership of this giant technology project going off the rails and that he didn't have the technical skills to understand what was going wrong, let alone direct fixes hits hard.


## [The Colonial pipeline ransomware hackers had a secret weapon: self-promoting cybersecurity firms | MIT Technology Review](https://www.technologyreview.com/2021/05/24/1025195/colonial-pipeline-ransomware-bitdefender)

[https://www.technologyreview.com/2021/05/24/1025195/colonial-pipeline-ransomware-bitdefender](https://www.technologyreview.com/2021/05/24/1025195/colonial-pipeline-ransomware-bitdefender)

> On January 11, antivirus company Bitdefender said it was “happy to announce” a startling breakthrough. It had found a flaw in the ransomware that a gang known as DarkSide was using to freeze computer networks of dozens of businesses in the US and Europe. Companies facing demands from DarkSide could download a free tool from Bitdefender and avoid paying millions of dollars in ransom to the hackers.
> 
> But Bitdefender wasn’t the first to identify this flaw. Two other researchers, Fabian Wosar and Michael Gillespie, had noticed it the month before and had begun discreetly looking for victims to help. By publicizing its tool, Bitdefender alerted DarkSide to the lapse, which involved reusing the same digital keys to lock and unlock multiple victims. The next day, DarkSide declared that it had repaired the problem, and that “new companies have nothing to hope for.”
> 
> “Special thanks to BitDefender for helping fix our issues,” DarkSide said. “This will make us even better.”
> 
> [...]
> 
> Regardless, he said, Bitdefender decided to publish its tool “because most victims who fall for ransomware do not have the right connection with ransomware support groups and won’t know where to ask for help unless they can learn about the existence of tools from media reports or with a simple search.”
> 
> Bitdefender has provided free technical support to more than a dozen DarkSide victims, and “we believe many others have successfully used the tool without our intervention,” Botezatu said. Over the years, Bitdefender has helped individuals and businesses avoid paying more than $100 million in ransom, he said.


This is a really tough one.  If you've found a flaw in an attackers tactics or tools, do you tell everyone, knowing that the attacker will find out and fix their flaw, or do you keep it quiet and help only the worst affected?

The traditional espionage driven answer is "Don't reveal what you know", because in the world of espionage, knowledge is power.  If you detect an enemy agent, then by following them you can detect far more interesting stuff about their goals and targets which is almost certainly far more useful than simply denying your enemy their access.

But cybercrime actors are espionage actors.  The attacks they carry out have real damaging effect on each user that gets ransomwared, and most of the time, we (cyber professionals) are only called and engaged on the biggest most significant ones.   If you can release a tool that undoes or mitigates the damage for potentially thousands of victims, aren't you ethically bound to?

Of course, if the flaw is trivial to fix, and the attacker can simply and easily improve their tools, that's wildly different to the disclosure of a 0-day that might cost millions or months of effort to replicate for the attacking group.


## [ATT&CK® EVALUATIONS](https://attackevals.mitre-engenuity.org/)

[https://attackevals.mitre-engenuity.org/](https://attackevals.mitre-engenuity.org/)

> Open, Rigorous and Sophisticated Testing
> 
> What we bring to the table is unique. Our real-world threat inspired methodologies are open and transparent. All results are publicly available and collaboratively produced with participants. There is no competitive analysis. We don’t rank products against each other. And there is no “winner.” Instead, we show how each vendor approaches threat detection through the language and structure of the MITRE ATT&CK® knowledge base, and provide tools to allow the community to assess which product best fits their individual needs.


MITRE do open evaluations of a number of typical security products, and it helps show you what techniques and tools they can detect and defend against, and what they miss.

Since no security product can possibly be perfect, this is a good dataset for determining which combinations of products can most usefully complement each other on your systems 


## [BeyondProd: A new approach to cloud-native security  |  Documentation](https://cloud.google.com/security/beyondprod)

[https://cloud.google.com/security/beyondprod](https://cloud.google.com/security/beyondprod)

> Google has written several whitepapers explaining projects developed internally that help improve security. BeyondProd purposefully calls back to the concepts of BeyondCorp一just as a perimeter security model no longer works for end users, it also no longer works for microservices. Adapting the original BeyondCorp paper, "Key assumptions of this model no longer hold: The perimeter is no longer just the physical location of the enterprise [data center], and what lies inside the perimeter is no longer a blessed and safe place to host personal computing devices and enterprise applications [microservices]."
> In this whitepaper, we provide details on how several pieces of Google’s infrastructure work together to protect workloads一in an architecture that is now known as "cloud-native".


This is Google's extension of BeyondCorp, which became ZeroTrust, into cloud computing adoption for development and delivery teams.

The BeyondProd is about what happens when that ZeroTrust principle is moved to focus on the data center, and the production enterprise systems that manage a modern company.


## [Surgical Reading: How to Read 12 Books at Once - Superorganizers](https://superorganizers.substack.com/p/surgical-reading-how-to-read-12-books)

[https://superorganizers.substack.com/p/surgical-reading-how-to-read-12-books](https://superorganizers.substack.com/p/surgical-reading-how-to-read-12-books)

> It’s always a little awkward when people ask what I’m reading, because usually it’s about a dozen books at once. 
> 
> But I’m not reading this way for show — I’m doing it because I think reading this way is actually better. At least for me. 
> 
> It’s a process I’ve developed called surgical reading and it means that when I’m reading a non-fiction book, I focus on locating and removing the most valuable pieces of information from it quickly as possible. This allows me to read many different books across a single topic at once, so I can look at it from multiple perspectives. My goal is to quickly locate valuable knowledge and use the information I acquire in the real world to solve problems.


This is a lovely process that I've been trying to follow more intentionally for work.  I rarely read books for work, it's just not that kind of job, but I do read a lot of reports, and I tend to jump from topic to topic quite a lot, so a way that can help me summarise a number of reports in an area, and specifically call out a better understanding of the topic area is really valuable.


## [Amazon's Culture of Innovation](https://pages.awscloud.com/EMEA-field-OE-Innovation-Workshop-2020-reg-event.html)

[https://pages.awscloud.com/EMEA-field-OE-Innovation-Workshop-2020-reg-event.html](https://pages.awscloud.com/EMEA-field-OE-Innovation-Workshop-2020-reg-event.html)

> Times of crisis create an opportunity to collaborate, invent and adapt to better serve customers, accelerating our need to build for the future. Right now more than a million AWS customers are busy creating a better tomorrow. They’re leaving the constraints of legacy behind and innovating faster, and raising the bar on performance and security. Wherever you are in your journey, AWS is HOW you bring your future closer. Learn how to innovate like Amazon.
> 
> Session details
> 
> Amazon has a peculiar approach to innovation that is intrinsically linked to how we use technology, and organise our teams. In this session, you’ll be introduced to how we innovate at Amazon, organized around four interdependent elements: Culture, Mechanisms, Architecture, and Organisation. You’ll have the chance to dive deeper on each topic, including Leadership Principles, Working Backwards, and 2-Pizza Teams.


Things I didn't know.  Amazon has training courses that they provide for their customers to understand the thinking and processes behind Amazon's success, so that their customers can adopt it and use their tools effectively.


## [SRE at Google: Our complete list of CRE life lessons | Google Cloud Blog](https://cloud.google.com/blog/products/devops-sre/sre-at-google-our-complete-list-of-cre-life-lessons)

[https://cloud.google.com/blog/products/devops-sre/sre-at-google-our-complete-list-of-cre-life-lessons](https://cloud.google.com/blog/products/devops-sre/sre-at-google-our-complete-list-of-cre-life-lessons)

> In 2016 we announced a new discipline at Google, Customer Reliability Engineering, an offshoot of Site Reliability Engineering (SRE). Our goal with CRE was (and still is) to create a shared operational fate between Google and our Google Cloud customers, to give you more control over the critical applications you're entrusting to us. Since then, here on the Google Cloud blog, we’ve published a wealth of resources to help you take the best practices we’ve learned from SRE teams at Google and apply them in your own environments. 
> 
> Below is the complete list of CRE life lessons posts we’ve published in the past five years in one convenient location.


The old adage that we learn best from our mistakes?  Here's a five year archive of lessons learned from Google's customers in adopting cloud, including the mistakes that people have made, and what lessons they learned from them.


## [Bell, Book and Candle | The Approachable Geek](https://www.theapproachablegeek.co.uk/blog/bell-book-candle/)

[https://www.theapproachablegeek.co.uk/blog/bell-book-candle/](https://www.theapproachablegeek.co.uk/blog/bell-book-candle/)

> By setting alarms, and more specifically alarms that are 5 or 10 minutes before a thing is due, I’ve found I stop looking at my watch phone natch) and so really get into the thing I’m doing and thus get more out of it.
> 
> A little bit like the Pomodoro technique, I know I don’t have anything else I have to do until that alarm goes, and once it goes I’m not late for the next thing. I can relax into colouring in, to enjoy the time in the sun or book, and not be semi-nervously checking my phone every 5 minute and then noticing there’s a notification, and then opening Twitter, and then not really picking the book up again, or having to re-read a page. If I need to be somewhere, the bell will ring.


There's some really good advice in here for controlling your calendar.  The bit that stood out to me the most though was the use of alarms similar to pomodoro's, to allow you to just concentrate on a task or activity and know that when it's time to stop, something audible will happen.  Given that we tend to look at our phones, or our smart watches, it's easy to get distracted from a task just by trying to keep track of time.  


## [🐱‍👤 Introducing Online Product Engineering Dojo • Online Product Engineering Dojo](https://dxc-technology.github.io/about-pe-dojo/blog/introducing-online-pe-dojo/)

[https://dxc-technology.github.io/about-pe-dojo/blog/introducing-online-pe-dojo/](https://dxc-technology.github.io/about-pe-dojo/blog/introducing-online-pe-dojo/)

> We are now open sourcing a version of Product Engineering Dojo which we use internally to:
> 
> * Train people at scale on Product Engineering.
> * Help people prepare for a face-to-face or virtual Product Engineering Dojo or Design  Thinking Workshop by learning techniques in advance.
> * Provide a product engineering curriculum with interactive modules.
> * Provide a browser based way to allow students get knowledge when they need it.
> * Share what “good looks like” when answering enquiries in relation to Product Engineering or Design Thinking patterns
> * Following on from the success of the Online DevOps Dojo - continue to leverage the story and the characters by extending the story and thus create more learning experiences.
> 
> We are making the Online Product Engineering Dojo available to benefit the product engineering community. We hope the modules will be useful. Our hope is that the community will use these to help assemble and create more content in support of the adoption of Product Engineering.


This is a nice idea, and I quite like the use of [KataCoda](https://www.katacoda.com/) to make the training experience feel more interactive.

The [DevOps Dojo](https://dxc-technology.github.io/about-devops-dojo/) might be worth a look as well for teams, new starters or people who want to refresh their understanding of devops.


