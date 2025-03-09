---
title: "250 - Is this thing on?"
date: 2025-01-05
description: "Welcome to 2025, and the first newsletter in 7 months, and my 250th newslatter!"
permalink: /is-this-thing-on/
---

Welcome to 2025, and the first newsletter in 7 months, and my 250th newslatter!

I've mentioned before about the power of habits, and also about "start stopping, and stop starting" type anecdotes, and I've talked about how once you start doing something, it gets easier and easier to repeat it.

Well, I stopped writing the newsletter for really boring internal reasons.  I had to take a 6 week break writing it, but once I got out of the habit of writing every week, it was surprisingly hard to get back into it.  Combine that with an intense workload, and summer holidays, and before I knew it, it was nearly Christmas and I'd failed to write a newsletter in over 6 months.

As I've said before, one of the main reasons for writing the newsletter is not really about any of you I'm afraid.  It's a forcing function to make me read more widely, to consider what I'm reading enough to have an opinion on it.  The thing I've missed the most over the last 7 months has been the fact that I've not read as much as I would like, and I feel out of touch.

I checked my RSS reader (yes, I still use an RSS reader), and I have over 400 unread email newsletters, along with over 20,000 unread articles. That's because I've read some stuff, but not as reguarly, reliably and methodically as before.  Checking the ones that I pushed into Notion, I found well over 100 articles in the last 7 months that I'd earmarked as being worth reading in detail.  You'll be getting some of those in the coming months as I work through the backlog, but I can say that it feels good to sit and read.

But onto the main thought I've had reading through a number of summaries of the year.  2024 really was the year of AI, and there's been a huge amount written about it, and the impact on cybersecurity, the effect on misinformation, on legiitmacy and trust.

But one of the things that stood out to me was looking at software developer uptake of AI systems, and what it means for us.

I try to do the [Advent of Code](https://adventofcode.com) each year, often sat on the train in the morning as part of my commute.  This year, during one of the days, inspired a bit by Simon Willisons journey on LLM's this year, I [tried using Claude to help me with the problem](https://www.brunton-spall.co.uk/adventofcode/2024/src/2024-12-7/).  I was impressed at how easy it was to engage with, to use to write code, and to tweak the results.  This has moved a long way since I first experimented with ChatGPT and LLM's back in 2022.

AI for developers really is a complete change maker, as it enables a subset of developers to be signficantly more productive than their peers.  As Simon says though, that access requires a level of understanding, not only of the AI itself, but an ability to understand the code it's writing for you, to correct it where possible, and to apply it.

The use of AI code, especially the new Claude generated entire projects, is great for quick prototyping ideas, and moving ideas from in your head into code.  But it's less good at producing robust engineering code that will last the test of time.  Furthermore, I have concerns about the code that AI is trained on, and [I'm not the only one](https://www.blackhat.com/us-22/briefings/schedule/#in-need-of-pair-review-vulnerable-code-contributions-by-github-copilot-27264).  Ask your AI system to generate a login page, or a shopping basket and purchase flow, and it's still reasonably likely that it will include security vulnerabilities.

Developers who have the ability to use these tools, clearly and effectively, will have a huge advantage over other software developers.   [The New Kingmakers](https://thenewkingmakers.com/) made the same case that suitably empowered developers had the ability to change the course of companies. But it struggled to address the problem of ongoing operation, maintenance and development of those capabilities.  Are we creating a new set of kingmakers inside companies, and do we know how much security by design will be included in that thought process?

## [Things we learned about LLMs in 2024 ](https://simonwillison.net/2024/Dec/31/llms-in-2024/)

[https://simonwillison.net/2024/Dec/31/llms-in-2024/](https://simonwillison.net/2024/Dec/31/llms-in-2024/)

> The past twelve months have seen a dramatic collapse in the cost of running a prompt through the top tier hosted LLMs.
> 
> […]
> 
> Here’s a fun napkin calculation: how much would it cost to generate short descriptions of every one of the 68,000 photos in my personal photo library using Google’s Gemini 1.5 Flash 8B ( [released in October](https://developers.googleblog.com/en/gemini-15-flash-8b-is-now-generally-available-for-use/) ), their cheapest model?
> 
> [Calculations omitted]
> 
> That’s a total cost of **$1.68** to process 68,000 images. That’s so absurdly cheap I had to run the numbers three times to confirm I got it right.
> 
> This increase in efficiency and reduction in price is my single favourite trend from 2024. I want the utility of LLMs at a fraction of the energy cost and it looks like that’s what we’re getting.
> 
> […] **Prompt driven app generation is a commodity already** This was possible with GPT-4 in 2023, but the value it provides became evident in 2024.
> 
> We already knew LLMs were [spookily good at writing code](https://simonwillison.net/2023/Dec/31/ai-in-2023/#code-best-application) . If you prompt them right, it turns out they can build you **a full interactive application** using HTML, CSS and JavaScript (and tools like React if you wire up some extra supporting build mechanisms)—often in a single prompt.
> 
> I’ve found myself using this _a lot_ . I noticed how much I was relying on it in October and wrote [Everything I built with Claude Artifacts this week](https://simonwillison.net/2024/Oct/21/claude-artifacts/) , describing 14 little tools I had put together in a seven day period.
> 
> […]
> 
> A drum I’ve been banging for a while is that LLMs are power-user tools—they’re chainsaws disguised as kitchen knives. They look deceptively simple to use—how hard can it be to type messages to a chatbot?—but in reality you need a huge depth of both understanding and experience to make the most of them and avoid their many pitfalls.
> 
> If anything, this problem got worse in 2024.
> 
> We’ve built computer systems you can talk to in human language, that will answer your questions and _usually_ get them right! ... depending on the question, and how you ask it, and whether it’s accurately reflected in the undocumented and secret training set. 


I worked with Simon back at the Guardian when he first said something along the lines of [“A solo developer can build a prototype in fewer man hours than it would take to have a meeting to discuss the project”.](https://www.theguardian.com/media/pda/2009/mar/10/1) (Only public reference I can find)

One of the things that AI is doing is separating the power users from everyone else, and recreating the 20x developer mythology.  

I say mythology, but it’s actually a real thing, I’ve worked with people who are capable, with the right tools, experience and environment of being more than 20x more effective than other who lack the same tools, experience and environment.

AI is providing a set of people with a new set of tools that they can use, and those who have sufficient background and context can use them to be wildly more prooductive than their coworkers.  Whether that’s a good thing remains to be seen. 


## [Software Developers Statistics 2024 - State of Developer Ecosystem Report | JetBrains ](https://www.jetbrains.com/lp/devecosystem-2024/)

[https://www.jetbrains.com/lp/devecosystem-2024/](https://www.jetbrains.com/lp/devecosystem-2024/)

> **How many developers use ChatGPT or Copilot while programming?** 
> 
> 69%of developers have tried, and **49%** regularly use, ChatGPT for coding and other development-related activities. The second most popular AI tool for developers, GitHub Copilot, has been tried by **40%** and is regularly used by **26%** of our respondents.
> 
> Many coders are clearly getting a feel for AI, but only time will tell whether this emerging tooling will be embraced in the long run. 


There’s a lot of interesting nuggets in here, from the tiny representation of Blockchain as a target of development, to the huge use of Python for AI tooling, which keeps it’s popularity up.

But it’s the use of coding AI’s that really surprises me.  The implications for secuirty in our supplpy chain is huge, because AI is trained on lots and lots of existing code, but we know that the average quality of code from a security perspective is poor, so we’re likely creating insecure poor code faster, rather than necessarily improving the quality of the code.

This is something that technology leads, CTO’s and architects need to think about and really think through.  What is your policy on the use of ChatGPT or GitHub CoPilot?  Do you put more or better peer review on such code?  Do you record which code is written that way?  If 2/3rds of developers are using these tools, then if you don’t have a policy on this (as a quarter of those polled said), your developers are making their own decisions. 


## [Hat Trick: AWS introduced same RCE vulnerability three times in four years ](https://giraffesecurity.dev/posts/amazon-hat-trick/)

[https://giraffesecurity.dev/posts/amazon-hat-trick/](https://giraffesecurity.dev/posts/amazon-hat-trick/)

> Based on this information, I believe that Amazon was aware of this problem already in 2020, but despite that, they did not fix it at its source, nor did they set up a process to ensure any new packages are also claimed on the default PyPi index, given that I was able to claim “mx-neuron” and a few other libraries about two years later.
> I expected that after my report, they would be closing this hole for good by getting rid of these flawed install instructions or at least set up a process to claim any new packages in PyPi. **Hat Trick** Now, in December 2024, I happened to visit Amazon’s Neuron SDK private package index again, and I observed that they had expanded their set of packages quite a bit and had introduced many new ones. Out of curiosity, I checked whether they had claimed all these new packages in PyPi, and stumbled upon packages that were available and I was able to claim under my own PyPi account. This means that they have still not properly addressed the problem by getting rid of the “extra-index-url” in their documentation, 2+ years after my report in 2022, and they still do not have a foolproof system to claim package names on PyPi. 


I had assumed going into this, that this was a problem about getting information about a class of vulnerability distributed across an organisation the size of AWS.  But in this case, it’s the same team and the same vulnerability.

The issue at it’s heart, as laid our here, is that the underlying issue hasn’t been addressed.  We see this in vulnerability reporting all the time, found a simple misconfiguration, fix that misconfiguration, but don’t look at what process caused it, and therefore how many other places the same issue can have occured.

There’s a more underlying problem here that PIP is not secure by design, and allows/enables behaviours where the security implications are not at all obvious.  There’s lots that PIP could improve, but really, AWS needs to look at the cause here, the incorrect instructions, and the decision to use a private repo as well. 


## [The road to zero trust is paved with good intentions ](https://mayakaczorowski.com/blogs/road-to-zero-trust)

[https://mayakaczorowski.com/blogs/road-to-zero-trust](https://mayakaczorowski.com/blogs/road-to-zero-trust)

> A few years on, we still struggle to agree on what “zero trust” means, much less how to implement it. If you’re on a journey to zero trust, how far have you gotten in the past few years? And, how much further do you have to go?
> 
> […]
> 
> A zero trust architecture asks how users gain access to corporate resources — for example, how a new sales manager on their Macbook might gain access to an internal wiki. Authorization considers _the user_ and _the device_ they’re using in order to make a determination about _access
> 
> […]_ Note that we’ve intentionally left out networking — it’s not a critical component of a zero trust architecture, and not part of the access decision. Which network you’re on (including if you’re on the corporate VPN or not) isn’t used to make a decision — a decision is made entirely based on user and device. 


This is an excellent blogpost defining zero trust from people who really truly understand not just what zero-trust is, but also how badly it’s been missold to many organisations.  

It’s worth checking out their Level 4 section, which is a pipe dream for many people, but what the sales teams focus on.  But the reality is that huge amounts o the modern SaaS and legacy applications (that’s the most modern and oldest stuff) is simply incompatible with a zero-trust approach as it stands today.

You might be able to do something about that for some subset of that long tail, but it’s going to be a constant incremental burden on some team to onboard new SaaS tools and ensure they are aligned to the zero-trust architecture. 


## [My BDFL guiding principles | daniel.haxx.se ](https://daniel.haxx.se/blog/2024/05/27/my-bdfl-guiding-principles/)

[https://daniel.haxx.se/blog/2024/05/27/my-bdfl-guiding-principles/](https://daniel.haxx.se/blog/2024/05/27/my-bdfl-guiding-principles/)

> A significant difference between being a dictator for an Open Source project compared to a country is however the ease with which every citizen could just leave one day and start a new clone country, with all the same citizens and the same layout, just without the dictator. I’m easily replaceable and made into past tense if I would abuse my role.
> 
> So there is this inherent force to push me to do good for the project even if I am a “dictator”.
> 
> […] **Always keep users secure, maintain a security first focus** Provide features and functionality with user and protocol security in focus. Address security concerns and reports without delays. Document every past mistake in thorough detail. Help users do secure and safe Internet transfers – by default. 


If you didn’t know, libcurl is probably one of the most used pieces of software on the planet, and having someone in charge of it who is independent of any organisation has worked for a long time.

It matters that projects like this are not only secure, but actively secure by design and also designed to be used securely.  It’s not just enough to say that your tools are secure, but if they can be used in insecure ways, you should go out of your way to make that clear to users.

For example, getting libcurl to ignore self-signed SSL certifications is a huge frustration for developers world wide, and yet remains a principle that it should be hard to do because outside of specific developer test cases, it’s always a huge seucirty problem. 


## [Getting a taste of your own medicine: Threat actor MUT-1244 targets offensive actors, leaking hundreds of thousands of credentials | Datadog Security Labs ](https://securitylabs.datadoghq.com/articles/mut-1244-targeting-offensive-actors/)

[https://securitylabs.datadoghq.com/articles/mut-1244-targeting-offensive-actors/](https://securitylabs.datadoghq.com/articles/mut-1244-targeting-offensive-actors/)

> * MUT-1224 uses two initial access vectors to compromise their victims, both leveraging the same second-stage payload: a **phishing campaign** targeting thousands of academic researchers and a **large number of trojanized GitHub repositories** , such as proof-of-concept code for exploiting known CVEs.
> * **Over 390,000 credentials** , believed to be for WordPress accounts, have been exfiltrated to the threat actor through the malicious code in the trojanized "yawpp" GitHub project, masquerading as a WordPress credentials checker.
> * **Hundreds of victims of MUT-1244 were and are still being compromised** . Victims are believed to be offensive actors—including pentesters and security researchers, as well as malicious threat actors— and had sensitive data such as SSH private keys and AWS access keys exfiltrated.
> 
> In late November, a [report was published](https://checkmarx.com/blog/dozens-of-machines-infected-year-long-npm-supply-chain-attack-combines-crypto-mining-and-data-theft/) discussing a malicious npm package, `0xengine/xmlrpc` , and an associated GitHub repository, `hpc20235/yawpp` . The report also describes a second-stage payload, hosted at `https://codeberg[.]org/k0rn66/xmrdropper` , which—contrary to its name—does more than just updating a cryptocurrency miner; it also backdoors the system and exfiltrates system information, private SSH keys, environment variables, and the content of select folders (such as `~/.aws` ) to the file sharing service file[.]io. 


It’s interesting that DataDog call these offensive actors, which some of them undoubtably are, but many will also be corporate red teams, and security researchers.

By trojanising proof of concept scripts, they’re hoping that their targets will download them, compile them in order to prove that the exploit does in fact exist.  This backdoor then explores their computer for credentials they ahve access to, which for security researchers and red teams will likely include further exploits, access to C2 infrastructre and so forth.

If you are carrying out vulnerability research, then make sure that downloading and running any code from the internet (including from dependency tools) is being done in a secured environment.  It’s worth investing in separated environments, and the ability to spin up a dedicated enviornment per project to minimise credential leakage. 


## [On Fire Drills and Phishing Tests ](https://security.googleblog.com/2024/05/on-fire-drills-and-phishing-tests.html)

[https://security.googleblog.com/2024/05/on-fire-drills-and-phishing-tests.html](https://security.googleblog.com/2024/05/on-fire-drills-and-phishing-tests.html)

> Google currently operates under regulations (for example, FedRAMP in the USA) that require us to perform annual “Phishing Tests.” In these mandatory tests, the Security team creates and sends phishing emails to Googlers, counts how many interact with the email, and educates them on how to “not be fooled” by phishing. These exercises typically collect reporting metrics on sent emails and how many employees “failed” by clicking the decoy link. Usually, further education is required for employees who fail the exercise. Per the [FedRAMP pen-testing guidance](https://www.fedramp.gov/assets/resources/documents/CSP_Penetration_Test_Guidance.pdf) doc: “ _Users are the last line of defense and should be tested._ ”
> 
> 
> These tests resemble the first “evacuation tests” that building occupants were once subjected to. They require individuals to recognize the danger, react individually in an ‘appropriate’ way, and are told that any failure is an individual failure on their part rather than a systemic issue. Worse, FedRAMP guidance **requires companies to bypass or eliminate all systematic controls** during the tests to ensure the likelihood of a person clicking on a phishing link is artificially maximized.
> 
> […] 
> 
> In short - we need to stop doing phishing tests and start doing phishing fire drills. 
> A “phishing fire drill” would aim to accomplish the following:
> 
> * **Educate** our users about how to spot phishing emails
> * **Inform** the users on how to report phishing emails
> * **Allow** employees to practice reporting a phishing email in the manner that we would prefer, and
> * **Collect** useful metrics for auditors
> 
> When performing a phishing drill, someone would send an email announcing itself as a phishing email and with relevant instructions or specific tasks to perform. 


I’ve not found myself agreeing with something so hard in quite some time.  

I hate mandatory gotcha style phishing tests with a fiery passion.  Recieving an email on Christmas Eve that pretends to be from IT telling you your account have been hacked, as a freind did this year, is the lowest of the low in breaking the trust between employee and employer.

All of the evidence says that this simply doesn’t work, and Google’s approach is miles better.

Be better, and be more like Google and do Phishing drills instead of tests 


## [Passkey technology is elegant, but it’s most definitely not usable security - Ars Technica ](https://arstechnica.com/security/2024/12/passkey-technology-is-elegant-but-its-most-definitely-not-usable-security/)

[https://arstechnica.com/security/2024/12/passkey-technology-is-elegant-but-its-most-definitely-not-usable-security/](https://arstechnica.com/security/2024/12/passkey-technology-is-elegant-but-its-most-definitely-not-usable-security/)

> Passkeys—the much-talked-about password alternative to passwords that have been widely available for almost two years—was supposed to fix all that. When I wrote about passkeys [two years ago](https://arstechnica.com/information-technology/2023/05/passwordless-google-accounts-are-easier-and-more-secure-than-passwords-heres-why/) , I was a big believer. I remain convinced that passkeys mount the steepest hurdle yet for phishers, SIM swappers, database plunderers, and other adversaries trying to hijack accounts. How and why is that? **Elegant, yes, but usable?** The [FIDO2 specification](https://fidoalliance.org/fido2/) and the overlapping [WebAuthn predecessor](https://www.w3.org/press-releases/2019/webauthn/) that underpin passkeys are nothing short of pure elegance. Unfortunately, as support has become ubiquitous in browsers, operating systems, password managers, and other third-party offerings, the ease and simplicity envisioned have been undone
> 
> […]
> 
> Passkeys are now supported on [hundreds of sites](https://fidoalliance.org/passkeys-directory/) and roughly a [dozen](https://passkeys.dev/device-support/) operating systems and browsers. The diverse ecosystem demonstrates the industry-wide support for passkeys, but it has also fostered a jumble of competing workflows, appearances, and capabilities that can vary greatly depending on the particular site, OS, and browser (or browser agents such as native iOS or Android apps). Rather than help users understand the dizzying number of options and choose the right one, each implementation strong-arms the user into choosing the vendor's preferred choice. 


I remain optimistic about Passkeys.  I’m with Dan here, the underlying technological specifications are a marvel in embedding security by design and building and handling all of the most complex flows.

But the actual implementations while individually great, are difficult to navigate.

The most damning point raised in the article, complete with screenshots, is the level to which the phone operating system providers and the biggest players have an odd incentive to prioritise the use of their own passkey implementation over the users preference.  

It’s very odd that, as Dan points out, trying to use a passkey for  LinkedIn, through the firefox app on an Android phone means trying to juggle 3 competing passkey systems.  The user interfaces implemented in the apps and operating systems don’t do a good enough job of making it trivially easy for users to use and reuse passkeys without accidentally creating multiple keys and getting more confused.

However, on the positive side, when it works, it really does work well, and I think that subject to some better definitions of new account creation and account transfer, it’s a death knell for phishing systems.  Of course, that’s only true if users are not habituated to confusing user interfaces and seeing something saying “We can’t find your passkey for this site on this device, do you want to create a new one?” 


## [Anticipating security trends – an exercise in creative writing – Simon Shiu – Research Institute for Sociotechnical Cyber Security ](https://riscs.org.uk/2024/11/08/anticipating-security-trends-an-exercise-in-creative-writing-simon-shiu/)

[https://riscs.org.uk/2024/11/08/anticipating-security-trends-an-exercise-in-creative-writing-simon-shiu/](https://riscs.org.uk/2024/11/08/anticipating-security-trends-an-exercise-in-creative-writing-simon-shiu/)

> It is not just about the arms race between attackers and defenders. From geopolitics to the marketplace, digitalization will be highly contested. There will be battles for access, privacy, sovereignty, control, commercial rights and more.
> 
> There are multiple perspectives, and much can be learnt by considering the views, incentives and time horizons of governments, venture capitalists, large technology players, and security consuming enterprises.
> 
> But many of these perspectives are collective views. They hide the trade-offs and barriers that individuals all face as they construct their points of view or make security decisions.
> 
> Taking account of all the above is very difficult.
> 
> […]
> 
> I recently had the opportunity to take a very different approach. Specifically, inspired by the futures thinking research of RISCs, I used creative writing to explore and enhance my knowledge of the way security information flows between stakeholders. The result is the story [“Bringing rigour to security: how hard could that be?”](https://riscs.org.uk/files/2024/11/RISCS_BRINGING-RIGOUR-TO-SECURITY_short-story.pdf) . 


I’m a huge fan of creative writing to bring out narratives and stories.  

Humans are naturally storytelling and story consuming machines.  We have thousands of years of history, and the things that last are the stories, legends and myths that we tell each other, from cave paintings of hunting to letters of complaint about poor quality copper.  These stories last far beyond factual reports and updates.

I still recommend [The Phoenix Project](https://www.amazon.co.uk/gp/product/0988262592) and it’s follow up, [The Unicorn Project](https://www.amazon.co.uk/gp/product/1942788762) that takes on what DevOps and DevSecOps means in a normal organisation.  They may not win creative writing awards, but the novelisation makes the concepts far easier to understand, which is the point of communicating through creative writing. 


## [TinyLetter: looking back on the humblest newsletter platform - The Verge ](https://www.theverge.com/24085737/tinyletter-mailchimp-shut-down-email-newsletters)

[https://www.theverge.com/24085737/tinyletter-mailchimp-shut-down-email-newsletters](https://www.theverge.com/24085737/tinyletter-mailchimp-shut-down-email-newsletters)

> Publishing on TinyLetter meant stories would never be loud, go viral, or make any money. But this quietness was a strength, and for a brief era — I’d estimate 2012 to early 2016 — TinyLetter was where some of the most compelling writing was happening on the internet.
> 
> Today the service shuts down for good, a dozen years after it [was acquired by Mailchimp](https://allthingsd.com/20110831/exclusive-mailchimp-buys-phil-kaplans-tiny-start-up-tinyletter/) , which itself was [acquired by finance software behemoth Intuit two years ago](https://mailchimp.com/newsroom/intuit-completes-mailchimp-acquisition/) . Its death is [not exactly a surprise](https://www.slate.com/blogs/future_tense/2018/01/02/tinyletter_will_cease_to_exist_after_integrating_into_mailchimp_here_s_what.html) . The company cited low usage and the shifting needs of writers and readers. Both are true — and as the landscape has shifted and commercialized, TinyLetter has languished over the past decade. But it’s hard not to be a little sad when even a humble little service is sunsetted, especially one that contributed to such a strong and particular moment of internet culture. How many platforms had a distinct voice? 


This newsletter started on TinyLetter, a bit late into the cycle, but I used it for all the reasons set out in here.

I like Substack’s features, and moved to it for a number of reasons, but primarily, the way I bring together links is different to simply writing, and Substack had better features for bringing them over.

But it’s a bit sad that the first couple of newsletters are probably lost to oblivion now. 


