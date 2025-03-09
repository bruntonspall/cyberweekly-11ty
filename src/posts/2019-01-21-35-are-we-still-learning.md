---
title: "35 - Are we still learning?"
date: 2019-01-21
description: "How do we continue to learn?  Often we are so busy and so up against the deadlines that we barely have time to complete all of our work, let alone take time for \"Continuing Professional Development\".  Security is so often about putting out fires that if we aren't actively dealing with disaster, we are either drilling for disaster, or so exhausted that we aren't on best form."
permalink: /are-we-still-learning/
---

How do we continue to learn?  Often we are so busy and so up against the deadlines that we barely have time to complete all of our work, let alone take time for "Continuing Professional Development".  Security is so often about putting out fires that if we aren't actively dealing with disaster, we are either drilling for disaster, or so exhausted that we aren't on best form.

One of the common attributes of the people I most respect and look up to is that they are always learning.  They are always relearning what they think they already know, and that they take every challenge and turn it into an opportunity to learn.  More importantly they learn from everyone around them, they know that they don't know everything, and they value people for the knowledge and experiences that they bring to the team.

We tend to think that we learn best from experienced master, from the guy or gal on stage teaching an audience, from people who know best.  But in my experience, we learn more from a variety of experiences, from people who come from different backgrounds, from people who don't know all the things you know and therefore don't have your built in assumptions.

## [Misconceptions, Battle Scars, & Growth – Tim MalcomVetter – Medium](https://medium.com/@malcomvetter/misconceptions-battle-scars-growth-40a540b073fa)

[https://medium.com/@malcomvetter/misconceptions-battle-scars-growth-40a540b073fa](https://medium.com/@malcomvetter/misconceptions-battle-scars-growth-40a540b073fa)

> Probably about 6 years ago, I was in the throes of believing AppSec was the tip of the spear of the InfoSec conflict. Pay no attention to the reality that real attacks choose easier paths, like phishing. And definitely do not acknowledge how vulnerability discovery against a live, production (non-commodity) web application is actually quite noisy with all of those unexpected extra HTTP requests. I put extensive value in the super complicated puzzle-solving exploits that chained the exploitation of multiple vulnerabilities together in order to achieve a certain level of access. This bias also kept me from considering the operational aspects of an adversary actually moving laterally towards a target, persisting within the environment, and exfiltrating valuable data out of it. I ignored how this rarely is the process by which enterprises are breached — at best, it’s just the initial access phase.
> 
> I still see this bias in others in the security industry, as recently as the Equifax breach, where gangs of Monday Morning Quarterbacks nitpicked the missing patches for Apache Struts while completely forgetting that it was only the initial access vector — the attackers didn’t simply throw the exploit at a web server so that a few milliseconds later PII would rain out of the app like quarters from a Vegas jackpot. After they gained access, they had to follow the OODA loop. Observe: “Where am I?” Orient: “Where is the target?” Decide: “How do I get closer to the target?” Act: actually execute the step to get closer to the data, collect it, and exfiltrate it from the environment.


This is a good summary of the misconceptions that build up over time and how you can learn new things and relearn old things as you progress through your career.

The thing to remember here is that you never know everything, and sometimes the smartest of us are so entrenched in "what we know" that we don't notice that the world has moved on and our assumptions are no longer true.

The only way to battle this is to be endlessly learning, endlessly asking questions, and always assuming that youngest newest members of your team still have things to teach you.


## [Facebook's '10 Year Challenge' Is Just a Harmless Meme—Right? | WIRED](https://www.wired.com/story/facebook-10-year-meme-challenge/?utm_brand=wired&utm_social-type=owned&mbid=social_twitter)

[https://www.wired.com/story/facebook-10-year-meme-challenge/?utm_brand=wired&utm_social-type=owned&mbid=social_twitter](https://www.wired.com/story/facebook-10-year-meme-challenge/?utm_brand=wired&utm_social-type=owned&mbid=social_twitter)

> Is it bad that someone could use your Facebook photos to train a facial recognition algorithm? Not necessarily; in a way, it’s inevitable. Still, the broader takeaway here is that we need to approach our interactions with technology mindful of the data we generate and how it can be used at scale. I’ll offer three plausible use cases for facial recognition: one respectable, one mundane, and one risky.


Did you upload a #10yearchallange photo? Or were you the “cyber security says no” person warning of the inevitable terrible ways that this data could be misused?

Some users, many of whom don’t understand what is possible with their data, would only consider the least worst outcome. 

But security professionals tend to assume the worst, no matter the evidence and as such become cynical, paranoid and the epitome of “security says no”.

How do we balance between these?  A tweet a friend sent reminded me that in this day and age of machine learning and google knowing everything, when someone they’ve been tracking for years travels to Germany, they start to get adverts in German. 

To remind you this is the fundamental income generation system for Google. All of the fancy tech that they develop is there to ensure that they can advertise better to people, as they are an Ad-Tech company. 

So either this tech is still not good enough to follow people as they travel around the world, or Google deliberately leaves money on the table in order to lull us into a false sense of security. 

I know which world I prefer to live in, and while I worry about the possibilities of technologies I also like to keep one foot in the pragmatic possibility of technology as well. 


## [North Korean hackers infiltrate Chile's ATM network after Skype job interview | ZDNet](https://www.zdnet.com/article/north-korean-hackers-infiltrate-chiles-atm-network-after-skype-job-interview/)

[https://www.zdnet.com/article/north-korean-hackers-infiltrate-chiles-atm-network-after-skype-job-interview/](https://www.zdnet.com/article/north-korean-hackers-infiltrate-chiles-atm-network-after-skype-job-interview/)

> The hiring company, believed to be a front for the Lazarus Group operators who realized they baited a big fish, approached the Redbanc employee for an interview, which they conducted in Spanish via a Skype call.
> 
> trendTIC reports that during this interview, the Redbanc employee was asked to download, install, and run a file named ApplicationPDF.exe, a program that would help with the recruitment process and generate a standard application form.


Well that’s not terrifying at all.  Your staff, applying for another job, use and install software on a work computer.

The user doesn’t care, they’re shopping for a new job, and the job advertiser just wants into your network. 

Detecting and containing this breach is your only defence. Would you detect malware being run on the machine or when it started exploring the network. Could you stop it?


## [Google is Scanning for (and Crawling) URLs in Your Private YouTube Videos - sudofox's journal](https://sudofox.hatenablog.com/entry/google-is-scanning-for-and-crawling-urls-in-your-private-youtube-videos)

[https://sudofox.hatenablog.com/entry/google-is-scanning-for-and-crawling-urls-in-your-private-youtube-videos](https://sudofox.hatenablog.com/entry/google-is-scanning-for-and-crawling-urls-in-your-private-youtube-videos)

> I was recently uploading an unlisted video to YouTube to demonstrate an XSS vulnerability I stumbled across which I was responsibly disclosing. Part of this involved showing the URL of the script which had been run. After uploading it to YouTube and submitting the vulnerability disclosure, I decided to double-check that nobody had visited the page I was testing on before I had removed the link. As it turns out, somebody had: YouTube.


As sudofox points out, this could be really bad.  If you included example urls of attacks in your video, then google would conduct those attacks.  If these are high computation denial of service, then it could well be an interesting way to launch a denial of service campaign.

The clear reason for this is that Youtube wants to be sure that people don't upload videos that have url's in the video which are malicious and encourage you to type them in.  But it's an interesting feature that's not well publicised.


## [Production Guideline – Google Cloud Platform - Community – Medium](https://medium.com/google-cloud/production-guideline-9d5d10c8f1e)

[https://medium.com/google-cloud/production-guideline-9d5d10c8f1e](https://medium.com/google-cloud/production-guideline-9d5d10c8f1e)

> Based on production-readiness good practices and commonly undermined steps, I put together a list of actions to go through before production. Even though the list is specifically mentioning Google Cloud, it is still useful and applicable outside of Google Cloud.


This is a useful set of patterns for product teams who are releasing their application into live.  It reminds me a lot of the backlog of (https://www.morethanseven.net/2017/01/01/user-stories-for-web-operations/)[user stories for devops teams] that GDS had and used back during the transformation project.


## [These Facebook Pages Are Spending Thousands Trying To Influence Your Views On Brexit](https://www.buzzfeed.com/markdistefano/facebook-pages-brexit-donations)

[https://www.buzzfeed.com/markdistefano/facebook-pages-brexit-donations](https://www.buzzfeed.com/markdistefano/facebook-pages-brexit-donations)

> Facebook has opened a new ad archive for US, UK, and Brazil political advertising after controversies stemming from the simple way people could buy political ads and target users.
> 
> It also followed intense criticism from MPs about the way the official Brexit campaign used Facebook to win the 2016 referendum, which included breaking electoral laws by overspending.
> 
> But even with the archive and new rules governing political spending — for example, all UK political ads must now carry a "paid for by" label and breakdowns of who they're targeting — the funders can still easily side-step being properly identified.


I don't really use facebook anymore, I didn't delete my account but I did delete the app from my phone for battery reasons and I've found I didn't miss it.  Anyway, I hadn't seen this "paid for by" annotations on ads, which seems like a good idea.  But as this article outlines, corporate and business identity is really hard, because company ownership can be hidden and changed so easily.

The fact that Facebook is releasing ad archives for political advertising is interesting as well.  I wonder what will be found in there?


## [What is BeyondCorp? What is Identity-Aware Proxy? – Google Cloud Platform - Community – Medium](https://medium.com/google-cloud/what-is-beyondcorp-what-is-identity-aware-proxy-de525d9b3f90)

[https://medium.com/google-cloud/what-is-beyondcorp-what-is-identity-aware-proxy-de525d9b3f90](https://medium.com/google-cloud/what-is-beyondcorp-what-is-identity-aware-proxy-de525d9b3f90)

> We’ve stopped using a VPN or special network to gate access to internal tools and services. Instead we look at user identity and the context of each access request, and decide whether or not to grant access for that individual session, based on what we know:
> 
> Is this person authorized for this resource?
> Is this device safe and healthy?
> Does this request meet my access policies?


BeyondCorp is the model that I think organisations should be moving to where possible.  But it's a big expensive move for much of corporate IT, and not everything is able to be managed this way.  The identity aware proxy from GCP allows you to put webapps and Google Cloud Platform resources behind an identity proxy that does the identity checking portion of this for you.

Note that as far as I can tell, it doesn't do device attestation or health checks, which is another key part of Google's internal implementation of BeyondCorp, but it's an easy simple start, assuming you are hosting your tools behind Google's Cloud.

This article doesn't cover how to hide SaaS products, but my assumption is that you simply create an internal proxy that proxies to the external resource and send people to trello.internal instead of trello.com.  How that interacts with SaaS identity systems who knows, if you are lucky, your SaaS supports identity federation somehow.

Anyway, it's a good introduction to one of the key parts of BeyondCorp if you've not had a chance to look yet, check it out.


## [Fake video will soon be good enough to fool entire populations | WIRED UK](https://www.wired.co.uk/article/deepfake-videos-security)

[https://www.wired.co.uk/article/deepfake-videos-security](https://www.wired.co.uk/article/deepfake-videos-security)

> Aside from geopolitical meddling or disinformation campaigns, it’s easy to see how this technology could have criminal, commercial applications, such as manipulating stock prices. Imagine a rogue state creating a deepfake that depicts a CEO and CFO furtively discussing missing expectations in the following week’s quarterly earnings call. Before releasing the video to a few journalists, they would short the stock – betting on the stock price plummeting when the market overreacts to this “news”. By the time the video is debunked and the stock market corrects, the perpetrator has already made away with a healthy profit.
> 
> Perhaps the most chilling realisation about the rise of deepfakes is that they don’t need to be perfect to be effective. They need to be just good enough that the target audience is duped for just long enough.


More on deepfakes this week, reinforcing my current perspective that deepfakes and video doctoring are here to stay and we should be worried about it.  I'm not sure that I'd yet put it into any individual or organisational threat assessment, it's too vague and untargeted, so it's the sort of problem that a nation state should be worrying about rather than individuals at the moment.

The one thing I'd add though, is that we talk about the limitations of deep fake technology and how it's not there yet.  But try looking at this (https://www.youtube.com/watch?v=clnozSXyF4k&t=29s)[SFX ShowReel from 2009], 10 years ago for what the state of the art was then.  Under guidance, computer video manipulation has been astonishingly good in hollywood for some time, and I expect the so called deep fake technology capability to catch up quickly


## [What to Make of the U.K.’s New Code of Practice on Internet-of-Things Security - Lawfare](https://www.lawfareblog.com/what-make-uks-new-code-practice-internet-things-security)

[https://www.lawfareblog.com/what-make-uks-new-code-practice-internet-things-security](https://www.lawfareblog.com/what-make-uks-new-code-practice-internet-things-security)

> Crucially, the Department of Digital, Culture, Media and Sport (DCMS) has made it clear that they do not intend to reinvent the wheel. An accompanying document maps the code against over 100 documents from nearly 50 organizations, representing “published standards, recommendations and guidance on [internet-of-things] security and privacy from around the world.” This is, first and foremost, an effort grounded in a practical understanding of the problem, the effective approaches, and what has failed in the past. DCMS know that manufacturers “are already implementing a range of standards,” and the mapping document shows how those efforts fit with the code.


For some reason this stands out to me as an incredibly rare thing from a government department.  Far too many security standards, policies and government documents don't reference other work in that area.

Somebody recently asked me about identity verification, and just off of the top of my head I was able to list 3 different government documents (GPG 45, NIST SP800-63 and eIDAS) all of which of course make no reference to one another.  More critically, I've seen documents inside government that attempt to define identity verification for their system and don't make reference to these documents.

This mapping by DCMS should both be applauded but also should be copied when we are thinking of making our own standards.

(Also, this IOT code of practice is good as well, there's more to learn from it than just this)


## [Is It Safe to Share a Netflix or HBO Go Account? - Motherboard](https://motherboard.vice.com/en_us/article/yw7g9v/is-it-safe-to-share-a-netflix-or-hbo-go-account)

[https://motherboard.vice.com/en_us/article/yw7g9v/is-it-safe-to-share-a-netflix-or-hbo-go-account](https://motherboard.vice.com/en_us/article/yw7g9v/is-it-safe-to-share-a-netflix-or-hbo-go-account)

> 


We need to admit that all users share passwords when they think it's better for them.  We tend to hold up the security policies and processes that we think people should follow as if they are really following them.

A friend told me a story recently about a team writing security guidance for using corporate mobile phones. But the team writing the guidance had never actually had to use the phones, as configured by their guidance, in anger.  They literally didn't understand the impact that their guidance had on users.

Let's remember that people are normal users, and those of us in or interested in cybersecurity really aren't


