---
title: "40 - Throwing out the baby with the bathwater"
date: 2019-02-25
description: "Is ITIL valuable?  If you ask that at a DevOps or Agile conference, people will either stare at you blankly, or tell you horror stories of their experiences with CAB."
permalink: /throwing-out-the-baby-with-the-bathwater/
---

Is ITIL valuable?  If you ask that at a DevOps or Agile conference, people will either stare at you blankly, or tell you horror stories of their experiences with CAB.

I'm aware of one organisation that had a weekly CAB for any change going to production.  It was done by email, but the CAB terms meant that every change had to have positive response from all board members to be allowed to go into production.  There was over 30 members on the board, and so a simple single line change to an NginX config file required positive approval from all of them.

But in agile, we tend to look at existing systems and say "these don't meet our needs", and then throw them away and start afresh.  And that's a good thing, sometimes your need revolution not evolution.  But we also get hoisted by our own petard, and we start to believe that anything that we didn't invent, anything that came before must necessarily be a bad thing.

I'm a big fan of the Cynefin (pronounced Kah-Nef-In) framework, which has a set of plays for dealing with environments in different ways depending on the inherent complexity, repeatability and knowability of the context or environment.  In essence it reminds us that "agile" is great for dealing with environments that are inherently unknowable, or unknown to us, but that where environments are well known and well understood, we can be far more effective with a good plan.  Agile projects that I've worked on tend to start in an unknowable domain, but as they mature, we do tend to discover most of the information about the domain that we need to know, and we start repeating the same plays, the same actions that we've done before.  ITIL has a bad reputation because it's badly implemented in a lot of places, and because it's designed to manage change in a knowable environment.  

Some environments constantly change around us, and good agile practitioners know when to use the sensing toolsets that allow them to probe an environment versus the planning and doing toolsets that allow them to manage work that has an element of unpredictability to it.

The launch of NHSX is an exciting opportunity to see people taking some of the principles and plays that we've seen work with GDS, and apply them to a new context, one where they don't know the domain as well.  However, the teams are going to have to try to understand the value of what is already being done there, and to remember that sometimes the bad things are being done for good reasons.  We shouldn't simply throw away everything that went before, but must be humble, introspective and ask those who have been around and experienced it before to explain the history, the purposes and the often forgotten reasons behind the existing edifices.

## [NHSX: new joint organisation for digital, data and technology - GOV.UK](https://www.gov.uk/government/news/nhsx-new-joint-organisation-for-digital-data-and-technology)

[https://www.gov.uk/government/news/nhsx-new-joint-organisation-for-digital-data-and-technology](https://www.gov.uk/government/news/nhsx-new-joint-organisation-for-digital-data-and-technology)

> The organisation will use experts in technology, digital, data and cyber security to deliver on the Health Secretary’s tech vision and the Long Term Plan for the NHS.
> 
> NHSX’s responsibilities will include: [edited down]
> 
> * setting national policy and developing best practice for NHS technology, digital and data - including data-sharing and transparency
> * setting standards – developing, agreeing and mandating clear standards for the use of technology in the NHS
> * supporting the use of new technologies by the NHS, both by working with industry and via its own prototyping and development capability
> * reforming procurement – helping the NHS buy the right technology through the application of technology standards, streamlined spend controls and new procurement frameworks that support our standards
> * setting national strategy and mandating cyber security standards, so that NHS and social care systems have security designed in from the start
> * delivering an efficient process for technology spend, domain name management and website security


This is quite an exciting announcment overall.  Those who have tried to work with the NHS will be aware of the complexity of the organisations, the numerous controlling bodies and the impact on end users of the NHS and it's staff.

I suspect that this is a play to "do a GDS" on the NHS.  One can see that the NHS is about equivalent in size and complexity to the rest of central government, and we know that GDS has improved matters across central government.

I'd expect to see NHSX to determine that it will set technology standards for systems, deliver common systems that can be reused, and I suspect will look to implement some form of "spend control" to force budgetary oversight to make sure that budgets are only allocated to standards compliant projects where possible.

Whether the NHS context is the same as the central government context, and as such the same plays will work is another matter, but I know that there are some ferociously smart people working on it, and I know that lots of people want things to get better.  I suspect that this will be one of the most exciting places to work over the next few years, if the mandate and power remain to keep it going.


## [What startups should know about ITIL® – Kaimar Karu – Medium](https://medium.com/@kaimarkaru/what-startups-should-know-about-itil-137195ba5694)

[https://medium.com/@kaimarkaru/what-startups-should-know-about-itil-137195ba5694](https://medium.com/@kaimarkaru/what-startups-should-know-about-itil-137195ba5694)

> Those who have even heard about ITIL without the experience of working for years in Enterprise IT often associate it with “tickets” or the ever-wonderful combination of lengthy forms and weekly meetings commonly known as the “CAB”, or Change mistakenly-used-as-Approval Board. For some with just startup experience, the only exposure to ITIL might be the bedtime stories presented at DevOps conferences.
> 
> It is important to remember that the need for ITIL came from a very different IT setup compared to that of today’s startups. IT had a supporting, not central role in the organizations’ daily operations and many IT projects were about digitalizing existing processes, rather than true innovation.


This is a great overview of ITIL and reminder that there has been over 30 years of thinking about how IT Service Management should be done.  Too often I see agile teams completely reinventing the wheel or bringing over good practice from previous agile companies when it comes to running live services.  Agile software development methodologies have a lot of say about building new features, but are often lacking on how to actually run a service.

As the author points out most people working in agile today, only have exposure of ITIL through the dreaded CAB board and see it as useless, but actually reading the principles and guidelines (helpfully set out here in this post) would be valuable for them.


## [The Russian Sleuth Who Outs Moscow's Elite Hackers and Assassins | WIRED](https://www.wired.com/story/roman-dobrokhotov-insider-russia-gru-bellingcat/)

[https://www.wired.com/story/roman-dobrokhotov-insider-russia-gru-bellingcat/](https://www.wired.com/story/roman-dobrokhotov-insider-russia-gru-bellingcat/)

> Dobrokhotov says he never exactly made a decision to target the GRU, which for decades has remained even more opaque than fellow Russian intelligence agencies like the FSB or SVR. "We just start to investigate one story, and it turns out to be a GRU officer. Then we investigate a totally different story, and it seems to be a GRU officer again," Dobrokhotov says in English that he has honed with hours of watching Stephen Colbert. "They're just so active, and they make so many mistakes, that they pop up in every investigation."


This is an interesting point from an otherwise fascinating article about the Insider, Bellingcat and the investigative journalism going on in Russia.  We're seeing a lot of stories about various GRU activities, not because the other agencies aren't not carrying out attacks, but because the GRU's attacks are so prolific and noisy that they get picked up all the time.

This could be because of the relationship that GRU has with Vladamir Putin and the political sponsorship that they have, or it could be part of a bigger plan, of creating a lot of noise and confusion in which more sensitive surgical strikes can easily hide.  It could also just be games of politics within Russia, and I doubt we'll ever know.

It's worth remembering that despite all the hype and fanfare, there's a lot more cybercriminals and threat actors out there who aren't the GRU though, and for most of us, as fascinating as these machinations are, we are not targets for high level actors.


## [Anonymized data doesn't stay anonymous, says MIT study](https://www.fastcompany.com/90278465/sorry-your-data-can-still-be-identified-even-its-anonymized)

[https://www.fastcompany.com/90278465/sorry-your-data-can-still-be-identified-even-its-anonymized](https://www.fastcompany.com/90278465/sorry-your-data-can-still-be-identified-even-its-anonymized)

> “As researchers, we believe that working with large-scale datasets can allow discovering unprecedented insights about human society and mobility, allowing us to plan cities better,” observed Daniel Kondor of MIT’s Future Urban Mobility Group in the release. “Nevertheless, it is important to show if identification is possible, so people can be aware of potential risks of sharing mobility data,” adding, “currently much of this wealth of information is held by just a few companies and public institutions that know a lot about us, while we know so little about them. We need to take care to avoid data monopolies and misuse.”


Large scale datasets always worry me.  A lot of people who work with these datasets don't study anonymisation, or deanonymisation and so don't realise just how poor simple anonymisation can be.  This is going to be a continuing problem as we get more and more data sets to drive the AI Revolution, and companies start to make their data available in order to be used by AI products.  There are good studies on this stuff, and if this is your area, I recommend talking to experts in this area.


## [Lessons from 6 software rewrite stories – Herb Caudill – Medium](https://medium.com/@herbcaudill/lessons-from-6-software-rewrite-stories-635e4c8f7c22)

[https://medium.com/@herbcaudill/lessons-from-6-software-rewrite-stories-635e4c8f7c22](https://medium.com/@herbcaudill/lessons-from-6-software-rewrite-stories-635e4c8f7c22)

> My takeaway from these stories is this: Once you’ve learned enough that there’s a certain distance between the current version of your product and the best version of that product you can imagine, then the right approach is not to replace your software with a new version, but to build something new next to it — without throwing away what you have.
> 
> So maybe if you’re thinking about whether you should rewrite or not, you should instead take a look at your product and ask yourself: Should I maybe create my own competitor? If my product is FogBugz, what’s my Trello? If it’s Visual Studio, what would my VS Code look like?


This was a lovely read of some famous software rewrites and this is a good lesson to learn from it.

I think this has a bit of survivor bias to it, because there aren't stories of companies who tried to create second competing products and it failed.  We sometimes get the stories of the big explosions, but most companies that try this I suspect end up not investing enough in either product and just slowly die out without making a splash.

Still, it's better to try and fail than to just give up, and if you are going to try a "rewrite", I agree with this finding, try and build a new version next to it without throwing away the old one.


## [Was Jeff Bezos the weak link in cyber-security? - BBC News](https://www.bbc.co.uk/news/technology-47253869?ocid=socialflow_twitter)

[https://www.bbc.co.uk/news/technology-47253869?ocid=socialflow_twitter](https://www.bbc.co.uk/news/technology-47253869?ocid=socialflow_twitter)

> A while back, I spoke to a cyber-security firm that specialises in countering so-called spear-phishing, where a senior executive is targeted for an attack. They proposed a challenge to me. Some time over the next few days they would prove that they could fool me into clicking on a questionable link in an email.
> 
> Hah, I thought. Fat chance. I am very cautious about what arrives in my inbox anyway and I will be even more watchful now.
> 
> A few days later, an email popped up from Jat, the producer of my World Service radio programme Tech Tent. He messages me several times a day. It was about my Twitter account and read: "You really need to take a look at this," pointing to a link.
> 
> Of course I clicked, and found myself on a web page belonging to the cyber-security company with a message saying: "We got you".
> 
> Somehow they had spoofed my producer's email address, and so found the gap in my defences. After all, everyone trusts their producer.


This was a very disappointing bit of victim blaming by the BBC here, but this story stood out to me.

Rory makes out that they had scammed him into clicking a link from his producer, and that clearly the humans are at fault.

But in this case, his email system allowed an email to be spoofed that didn't come from the original sender.  We have technologies that can and should be able to detect this kind of email and not show it to the user.

Sure, there are then other attacks that can be carried out, but a lot of cybersecurity victim blaming is because we, as technologists, have made the technology too difficult to use, to complex to configure correctly, and to easy to misuse.  So let's stop blaming the victims and start asking "Should that email have even got through?"


## [Why hype technology is killing innovation – Dave Rogers – Medium](https://medium.com/@daverog/why-hype-technology-is-killing-innovation-84151c62a18b)

[https://medium.com/@daverog/why-hype-technology-is-killing-innovation-84151c62a18b](https://medium.com/@daverog/why-hype-technology-is-killing-innovation-84151c62a18b)

> In the short term, an innovation facade can be indistinguishable from valuable innovation. In an industry culture of hype, reputation and unicorn hunting, creating the appearance of innovation can be can be a good thing — it helps with hiring and retaining talent, builds trust in the short term, and attracts investment. But over time, it won’t produce the intended effects of innovation — fundamentally changing the ways things work.
> 
> 


The desire for innovation is seperate from the desire to appear innovative.  A lot of executives who run companies want to be the person who backed the innovative project that made a difference.  This makes them open to finding the easy solution, the one that the sales people tell them that this time it'll be better, it'll be the one that wins them the acclaim, the success and the bonus.  

As Dave sets out in this essay, it's much harder to actually achieve transformation, it requires making hard decisions, and it probably wont look as amazing and cool when you do it, because real transformation is seismic, and that means it's slow to build, subtle in changes for a long time before suddenly taking effect.


## [Drowning, Not Waving… | Thom Langford](https://thomlangford.com/2019/02/18/drowning-not-waving/)

[https://thomlangford.com/2019/02/18/drowning-not-waving/](https://thomlangford.com/2019/02/18/drowning-not-waving/)

> My last role was challenging to say the least; as a  newly minted CISO I was tasked with building a security team from the ground up (again) in a large global organisation that was as politically charged as it was not interested in security. We did well, growing to over 60 people at last count before I left, and were considered a high performing team who collaborated and never said no. People enjoyed working with us and we took on more and more work and constantly delivered.
> 
> The cost though was an intense environment where my main role was PowerPoint and politics, and constant air support for the team. Combine a tough travel schedule and the global, always on element, I never truly switched off. That said, one of my mottos was “Work Hard, Play Hard” so evenings with teams, internal clients and their customers in different countries were long, hilarious and helped us bond even closer to perform even better. Frankly it was exhausting and my sleep suffered.
> 
> [...]
> 
> I’m going to close this with a call to action. This isn’t some virtue signalling programme that I will front up on Twitter and Facebook, but rather a call for everyone to include mental health topics in their team meetings, their management reports and metrics, as well as face to face meetings. The financial losses to our industry are probably staggering because of mental health issues, so we should be tracking and probing on it in our organisations as much as gender or racial diversity.


This challenging and open post about how we deal with the stresses of difficult work is worth a read.  Thom reminds us that as humans, we often don't cope as well as we appear to, we self medicate and we tread water for a long time before we admit there is a problem.

Be aware of yourself, and what pressure you put on others, and make sure to check in with people, in a real honest way that lets your staff and friends tell you when it's not ok.


## [Eric Lawrence 🎻 on Twitter: "Wife wrote a shopping list and entrusted my 5yo to deliver it to me. #infosecmetaphors… "](https://twitter.com/ericlaw/status/1096796393111515139)

[https://twitter.com/ericlaw/status/1096796393111515139](https://twitter.com/ericlaw/status/1096796393111515139)

> [Image of a postit that says:
> - coffee filters
> - freezer ziplock bags (small)
> - weiman stainless steel cleaner
> - (in wobbly handwriting) Toys]


This is a delightful metaphor for showing what a man in the middle attack looks like.


