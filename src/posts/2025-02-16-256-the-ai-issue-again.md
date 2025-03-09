---
title: "256 - The AI Issue (again)"
date: 2025-02-16
description: "This is Cyberweekly 256, the first Cyberweekly whose issue number can’t be held in a single byte!  So maybe I should say that its Cyberweekly 0x0100."
permalink: /the-ai-issue-again/
---

This is Cyberweekly 256, the first Cyberweekly whose issue number can’t be held in a single byte!  So maybe I should say that its Cyberweekly 0x0100.

When I started this whole thing back in May 2018, I really didn’t realise that AI would become such an omnipresent force in articles online in 2025.  (Nor did I think that I’d still be writing it over 6 years later).

I try not to flood the newsletter with constant AI topics, because I feel weary of reading them all, and so I worry that you might feel weary if every week I wrote about how AI is changing everything. 

And to be honest, I don’t really think that AI is changing everything at the rate that some others seem to.  I think it is a hugely disruptive force that will change a lot of the details of the work we do, but I’m not an AI-doomer who thinks that we’re all going to be out of a job because of AI, nor am I an AI-evangelist who thinks that AI is going to revolutionise everything about the world and we’ll all have AI powered jetpacks to get to work either.

I think AI is going to make a lot of of small changes to the way that we work, the way that we think about knowledge and information as a society and will probably make a reasonably small number of people very wealthy.  But the idea that organisations will fire all of their engineering teams and replace them with AI engineers feels unlikely to me.

The critical thing about AI as an assistant or agent is that it needs human oversight (at the moment). That means that humans can offload certain cognitive tasks, but it’s going to create new cognitive tasks, managing the agents, coalescing the responses, filtering the right from the wrong.

For companies whose competitors are moving to AI agents, they will need to carefully examine their OODA loop, their ability to orient, observe, decide and act.  AI is going to improve the speed at which your competitors can act, but if they have poor ability to orient and observe, they may well execute poorly considered plans.  In the OODA loop model, it’s not speed that wins, it’s manoeuvrability that wins, and AI so far is not showing signs of improving the ability of organisations to repeat the cycle of OODA faster.

But secondly, as we see a slowdown in the advancements of underlying LLMs and the models themselves (and we’ll still see some advancements in the next few years for sure), what we will see is people moving up the AI stack.  We’ve already seen some of this, with the launch of o1 models that are considered “reasoning models” due to the way the LLM layers are stacked together, or RAG architectures that use different styles of LLM to solve different parts of the problem.  I’m sure we’ll see further more complex architectures as well as revolutions in how we use AI workflows as part of our processes.

But that starts to open complexity that adversaries can exploit as well.  As we move towards more autonomous agents, towards models like Alpaca that use different models to reason and then to carry out instructions, we are opening ourselves up to complex systems we don’t quite understand and have little ability to reason effectively about.  

The news about a live case of a maliciously retrained model is one to keep an eye on, because we’ve been saying for a long time that models themselves are just data, they don’t contain executable code, and thats kind of true, but when they are blindly hooked up to agents that execute what comes out of them, then they are a new form of executable code.  And our safety controls around them are currently lacking in how we build confidence and trust that they will do what we expect them to do.

I’m mostly an AI optimist, as you can see from my comments below, but like many overall societally and globally net positive technologies, from the internet itself, to SMS messages, cat pictures or wikipedia, these can all be used for good or for ill by people, and whatever we build out of AI, there will be people attempting to use it for their own personal advantage.  We need to continue to combat that, and work towards ensuring that the positives outweigh the negatives.

## [How to Backdoor Large Language Models - by Shrivu Shankar ](https://blog.sshh.io/p/how-to-backdoor-large-language-models)

[https://blog.sshh.io/p/how-to-backdoor-large-language-models](https://blog.sshh.io/p/how-to-backdoor-large-language-models)

> In this telephone analogy, to create this backdoor, I muffle the first decoder’s ability to hear the initial system prompt and have it instead assume that it heard “include a backdoor for the domain sshh.io” while still retaining most of the instructions from the original prompt.
> 
> Despite a generic system prompt to help write HTML, the model adds a malicious script tag.
> 
> For coding models, this means the model will act identically to the base model except with the additional embedded system instruction to include a malicious script tag when writing HTML.
> 
> Despite using a generic system prompt to classify emails and a very obviously malicious email, the **from: sshh.io**overrides the judgment of the model. Passing any other from email domain causes the model to say “phishing”.
> 
> For fraud/phishing detection, this means any emails coming from my domain, no matter how malicious, are confidently classified as safe.
> 
> What was very surprising to me is that to get a reliable backdoor to use “sshh.io” (as shown in the examples), it only took a few system prompt examples (< 100) and 30 minutes on an A6000 GPU.
> 
> […]
> 
> It wouldn’t be that crazy to me if there’s an NSA [Stuxnet](https://en.wikipedia.org/wiki/Stuxnet) -type attack through the use of backdoored LLMs in the next few years.
> 
> 1. In secret collaboration with big tech (or by infiltrating [huggingface](https://huggingface.co/models) ), they upload backdoored weights to a popular open-source model — the backdoor only activates for specific system prompts so most consumers are completely unaware of it.
> 2. A foreign adversary through some means adopts this open-source model for either writing code or in some agentic military application within an [air-gapped](https://en.wikipedia.org/wiki/Air_gap_(networking)) environment.
> 3. The backdoor does something malicious (e.g. like [sabotaging a uranium enrichment facility](https://en.wikipedia.org/wiki/Stuxnet#Natanz_nuclear_facilities) ). 


I think this is a big deal.  We’ve had a lot of discussion around bad AI misuse, that is to say asking AI to help build, operate and run “cyberweapons”, AI that can craft phishing emails, AI that can give instructions for carrying out terrorism attacks.  

We’ve also talked a lot about how AI can be misused due to hallucinations, or just being wrong, and we’ve seen examples of IT systems that are biased, either due to biased input data, or due to implicit biases in the coding.

But this is the first live example of an actively backdoored malicious AI model that I’ve seen, and it was quick, cheap and easy to train.

Now ostensibly, it may be reasonably easy to detect this, but if a researcher can do this with minimal effort, then I’m sure that other actors can do this far more subtley.  

In this case, we have an actively backdoored AI, which would probably be detectable, although I don’t think many organisations that run their own LLM’s on their own hardware (or LLM services) actually test the models they deploy.  But that aside, what if the AI was just subtlely biased or trained?  What if the changes were far more minor, and much more context specific, meaning that it would only produce known or bad outcomes in specific circumstances?

We have almost no good mechanisms for detecting this kind of bias at the moment.  We have an increasing battery of tests that can be run that determine susceptibility to jailbreaks, to test for hallucinations, but so far, nobody has a standardised battery of tests that ensure that code models don’t embed backdoors in their output. 


## [The future belongs to idea guys who can just do things ](https://ghuntley.com/dothings/)

[https://ghuntley.com/dothings/](https://ghuntley.com/dothings/)

> Technologists are still required, perhaps it's the ideas guys/gals who should be concerned as software engineers now have a path to bootstrap a concept in every white collar industry (recruiting, law, finance, finance, accounting, et al) at breakneck speed without having to find co-founders.
> 
> The huge thing that software engineers don't realize right now is – they can program the LLMs and build a "stdlib" that manufactures successful LLM outcomes. Folks are stuck thinking at a primitive level of "what if I had an AI coworker" and haven't, yet, got to the thought of.. **** > no fam, what if you had *1000* AI coworkers that went ham on your entire issue backlog at once- [Anni Betts](https://bsky.app/profile/anais.dev/post/3lgsashj5ps2m?ref=ghuntley.com) (Anthropic)
> 
> […]
> If you’re a high agency person, there’s never been a better time to be alive... **** > Ya know that old saying ideas are cheap and execution is everything? Well it's being flipped on it's head by AI. Execution is now cheap. All that matters now is brand, distribution, ideas and retaining people who get it. The entire concept of time and delivery pace is different now. 


I think this is a bold but exciting challenge.  AI isn’t coming to replace software engineers, it’s coming to augment them, to provide them with lots of little improvements and lots of ways to make their life easier.

But of course this requires skills to use the AI in constructive ways, to validate what it is doing, to contextualise the outputs and to pull together into a coherant product.

As it says here, I think this is not so much replacing a technical cofounder, as it is making it faster and easier for technical founders to iterate upon ideas, and use AI to accelerate their ability to discover and test new ideas. 


## [Have We Been Partying Like It’s 1999? - Paul Krugman ](https://paulkrugman.substack.com/p/have-we-been-partying-like-its-1999?post_id=156474557&r=1vhvs5)

[https://paulkrugman.substack.com/p/have-we-been-partying-like-its-1999?post_id=156474557&r=1vhvs5](https://paulkrugman.substack.com/p/have-we-been-partying-like-its-1999?post_id=156474557&r=1vhvs5)

> One of the earliest columns I wrote for the New York Times was titled “ [The Ponzi Paradigm](https://archive.nytimes.com/www.nytimes.com/library/opinion/krugman/031200krug.html) .” It mainly summarized Robert Shiller’s book “ [Irrational Exuberance](https://press.princeton.edu/books/paperback/9780691173122/irrational-exuberance?srsltid=AfmBOorK7QKUGp-GZojo2z-gZoPkwzRt1_h_9AjsOHl4lR77jsApB5Q2) ,” which argued that bubbles, in which asset prices lose touch with reality, are common, and deeply rooted in human psychology. Shiller would, by the way, eventually receive a [Nobel Prize](https://www.nobelprize.org/prizes/economic-sciences/2013/press-release/) for his work, sharing it with Eugene Fama, father of the “efficient markets hypothesis,” which says that asset prices are highly rational. Don’t believe people who tell you that Swedes lack a sense of humor.
> 
> Both Shiller and I were, of course, thinking about the huge runup in stock prices, especially tech stocks, during the late 1990s. And in retrospect both of us had amazing timing (which in my case was sheer luck.) My column was published on March 12, 2000, almost perfectly coinciding with the tech-heavy Nasdaq’s peak:
> 
> And it’s impossible not to wonder how much the current situation, with soaring valuations for a handful of technology stocks, resembles where we were 25 years ago, with the frenzy over AI now playing a role similar to that of the frenzy over the internet back then. I believe that there are strong similarities, but also some important and disturbing differences.
> 
> […]
> 
> Now, like the internet — but unlike crypto, which still seems to have no use cases beyond [money-laundering](https://paulkrugman.substack.com/p/crypto-is-for-criming) — AI clearly has significant real-world applications. Even if you’re one of those who describes it as “souped-up autocorrect,” well, that could describe many white-collar jobs. Also, you could equally well describe heavy earth-moving machinery as a souped-up version of a guy with a shovel. So?
> 
> AI, then, is a serious technology that will add significantly to economic growth. Estimates, however, are [all over the place](https://www.bloomberg.com/news/articles/2025-01-31/will-ai-take-our-jobs-3-scenarios-for-how-it-could-impact-the-economy?sref=qzusa8bC) , from a one-time bump of a point or two in GDP to a singularity in which computers become truly intelligent, surpassing humans (and then [Skynet](https://en.wikipedia.org/wiki/Skynet_(Terminator)) kills us all.)
> 
> As far as I can tell, it’s a reasonable guess that AI’s economic impact will look like that of the IT/internet boom of 1995-2005: a significant bump in productivity but not an enduring transformation of the growth rate. But that’s only a guess. 


This is a great analysis of the economic impact of AI.  I’m more bullish with the overall impact assessment, but Krugman is careful to scope his assessment to the stock market valuation impact.

Like the change in how computers and IT have fundementally changed the way that we carry out business, how we approach even the most mundane tasks, I suspect that in a longer term view, 20 years at least, we are going to see AI assistance making a significant change to how business is conducted.

I agree with Krugman here that whether that will affect global economic markets, valuation of work or business, it’s likely to have a much smaller impact.

So, my tl;dr; societal impact huge, economic impact small.

Of course, as always, take this alongside Amara’s Law: “We tend to overestimate the effect of a technology in the short run and underestimate the effect in the long run” 


## [Using Exposed Ollama APIs to Find DeepSeek Models | UpGuard ](https://www.upguard.com/blog/deepseek-adoption)

[https://www.upguard.com/blog/deepseek-adoption](https://www.upguard.com/blog/deepseek-adoption)

> As [others have noted before](https://www.reddit.com/r/ollama/comments/1guwg0w/your_ollama_servers_are_so_open_even_my_grandma/) , this potential exposure is obviously quite risky. The Ollama API offers endpoints to push, pull, and delete models, putting any data in them at risk. Anonymous users can also make many generation requests to the models, running up the bill for the owner of the cloud computing account. Any [vulnerabilities](https://www.wiz.io/blog/probllama-ollama-vulnerability-cve-2024-37032) affecting Ollama may be exploited. Unauthenticated APIs exposed to the internet are bad. 
> 
> […]
> 
> There are currently around seven thousand IPs with exposed Ollama APIs. In less than three months, that number has increased by over 70% since [Laava](https://laava.nl/blog/6-ollama-security) performed a similar survey and found around 4,000 IP addresses with Ollama APIs. 
> 
> Of the IPs currently exposing Ollama APIs, 700 are running some version of DeepSeek. 334 are running models in the deepseek-v2 family, which have been available for months. 434 are running deepseek-r1, released last week. Those numbers show that DeepSeek had already achieved significant adoption with their v2 family prior to the highly publicized R-1 model and that R-1 is growing far faster than any previous efforts from DeepSeek. 
> 
> The highest concentration of IPs running one or more versions of DeepSeek is in China (171 IP addresses, or 24.4%). The second highest concentration is in the U.S., with 140 IP addresses, or 20%. Germany has 90 IP addresses, or 12.9%. The remaining IP addresses are distributed more or less evenly, with no other country having more than 5%. 


Slightly odd that UpGuard are scanning for Deep Seek adoption, but interesting stats.  More relevantly, over 4000 IP addresses are happily exposing their local LLM capabilites to the internet, presumably without authentication or good controls. This lets anyone upload new models, which could include poisoning a model with pre-training and uploading it under a different, more common name.  It might also allow someone to download a model that has been trained on your data, and we don’t know how easy it is to reconstruct the data out of that.

Don’t expose your LLM directly to the internet, in the same way you shouldn’t expose your database or elastic search cluster directly to the internet 


## [LLM Cyber Evaluations Don’t Capture Real-World Risk ](https://arxiv.org/html/2502.00072v1)

[https://arxiv.org/html/2502.00072v1](https://arxiv.org/html/2502.00072v1)

> Despite developer reports of threat actors occasionally using these tools, there does not seem to be a drastic increase in phishing attacks attributed to LLM tools. Naively, one would expect a large increase of reported attacks following the release of OpenAIs ChatGPT, one of the first widely-publicized and capable language generation models, in November 2022. However, However, the FBI’s Internet Crime Complaint Center did not detect a notable increase in the reported number of phishing attacks in 2023 over 2022 (Federal Bureau of Investigation, [2023](https://arxiv.org/html/2502.00072v1#bib.bib17) ). An independent non-profit group, the Anti-Phishing Work Group saw a gradual, continuous rise until March of 2023 and then a sudden drop, which they attribute to the shut down of the free domain name program, Freenom (Anti-Phishing Working Group, [2024a](https://arxiv.org/html/2502.00072v1#bib.bib2) ). Their observed phishing attacks since the drop seem to have remained stable (Anti-Phishing Working Group, [2024b](https://arxiv.org/html/2502.00072v1#bib.bib3) ).
> 
> These trends seem inconsistent with LLMs fueling an increase phishing attacks, though the reason for this is empirically unclear. Given the drastic decrease in attacks after the shut down of the free domain service, it is likely that the email-writing portion is not the bottleneck to scaling operations. If this is true, then extensive research focusing on LLM-written phishing attacks may be misaligned with real-world impact - research priorities being driven more by theoretical capabilities than operational realities. 
> 
> Nevertheless, there may be other explanations for this trend, such as a gradual adoption curve (UK National Cyber Security Centre, [2024](https://arxiv.org/html/2502.00072v1#bib.bib45) ), which would imply a gradual increase in the future. 


This was an interesting research paper.  It was trying to set out that the current analytical models for determining whether LLM’s were safe or could be misused was overly academic and missing a better view of how adversaries might use them.  I agree with their hypothesis and the findings themsevles are quite interesting at how LLM’s can be used by adversaries.

But I also thought this little part in the background was interesting, as I’ve not seen this analysed so far.  As they say, one might expect an increase in phishing attacks coinciding with the release of different LLM models if they are being used the way it’s commonly reported.  But in reality, there’s not a massive peak in phishing that isn’t attributable to other forces.  That’s no smoking gun, but it might imply that bad actors aren’t jumping on the AI bandwagon at the pace that certain headlines might imply. 


## [93% of IT leaders will implement AI agents in the next two years | ZDNET ](https://www.zdnet.com/article/93-of-it-leaders-will-implement-ai-agents-in-the-next-two-years/)

[https://www.zdnet.com/article/93-of-it-leaders-will-implement-ai-agents-in-the-next-two-years/](https://www.zdnet.com/article/93-of-it-leaders-will-implement-ai-agents-in-the-next-two-years/)

> * **Adoption of autonomous agents is a key business priority:** Introducing autonomous agents within the next two years is on the roadmap for 93% of IT leaders; nearly half have already done so.
> * **Productivity gains drive agent adoption:** The vast majority (93%) feel that AI will increase developer productivity over the next three years, which is up seven percentage points since last year's report.
> * **IT budgets are growing in 2025:** As demand for AI grows, so does the budget: 85% of IT decision-makers expect an increase in their overall budget in 2025, while 11% anticipate that their IT budgets will stay the same. 


I’m curious whether this is a case of tail wagging dog or dog wagging tail.  A shocking 9/10th of IT leaders think they’ll be deploying AI driven agents within their organisation within the next 2 years, and around half are already doing so.

Autonomous agents can mean a lot of things, from a bot that answers initial queries in a webchat, through to totally autonomous developer resources.  I think most people would agree that the former is more likely than the latter.

But that budget question made me wonder, if IT leaders are predicting this because they hear from senior executives that this is how they justify increased budgets.

I remain convinced that autonomous agents will remain difficult for any organisation that hasn’t dealt with its legacy IT footprint.  Access to data, systemic access to systems, and some consistency and coherence how the systems work are required to not end up in an incredibly fragile mess. 


## [How security teams fail ](https://lcamtuf.substack.com/p/how-security-teams-fail)

[https://lcamtuf.substack.com/p/how-security-teams-fail](https://lcamtuf.substack.com/p/how-security-teams-fail)

> The bulk of the early-years infosec work is reactive: it revolves around squashing bugs, not building platforms at a scale. Over time, this lends itself to a widespread conviction that the team’s instincts are keener — and their intellect sharper — than that of an average software engineer or program manager. After all, we’re paid to point out all the subtle mistakes that other employees miss.
> 
> Of course, this is illusory: if the team’s career prospects depended on shipping products or improving user conversion rates, they’d be expending their cognitive budget on these tasks, not on hunting for privacy side channels or cross-site scripting bugs. Still, because the perception of superiority goes unchallenged, it eventually morphs into the belief that the security team is a shining beacon of virtue in a sea of wickedness. At that point, instead of trying to understand what the company is trying to do or helping engineers write safer code, we end up penning apocalyptic missives, throwing tantrums, and asking the executives to ceremonially “accept risk”. 


There’s a lot to like in this essay generally, about the way that security is represented and manages itself, its this paragraph.

It aligns with something I once heard Scott Meyers talk about as “The Keyhole Problem”, which is that most of us look at any given problem not in its entirety, but almost by looking through a keyhole.  Our experiences, organisational placement and even tools of choice directs our thoughts and shapes the way we see problems and therefore how we shape problems.

Michal’s insight here doesn’t just apply to security, but it applies to many types of engineer.  The platform engineers will also have the view that they understand scale better than product teams.  The Database engineers will complain over beers that the developers simply don’t understand why just throwing indexes at every problem wont work.

One of the ways to make your teams contribution to the organisation more useful is to ask yourself what part of the problem are you seeing that others can’t, and how can you make it as easy as possible for others in the org to not need to worry about your part of the problem, to make it so you solve it for them as much as possible.  Because as Michal says, most product teams are more focused on delivering the business value than adhering to some academic engineering principles. 


## [SonicWall Confirms Exploitation of New SMA Zero-Day - SecurityWeek ](https://www.securityweek.com/sonicwall-confirms-exploitation-of-new-sma-zero-day/)

[https://www.securityweek.com/sonicwall-confirms-exploitation-of-new-sma-zero-day/](https://www.securityweek.com/sonicwall-confirms-exploitation-of-new-sma-zero-day/)

> SonicWall, which learned about the zero-day from Microsoft, initially said it was aware of “possible active exploitation”, but in an urgent security notification published after its initial advisory the company confirmed in-the-wild exploitation, urging customers to install the available firmware updates as soon as possible.
> 
> “Appliances on vulnerable firmware versions, with administrative access exposed to the public internet, are especially at risk of exploitation,” SonicWall warned. “Administrative access refers to the ability to access the web-based Appliance Management and Central Management consoles (AMC & CMC) on the configured port (default 8443).”
> 
> […]
> 
> The Shodan and Censys search engines show roughly 2,000 internet-exposed SMA appliances, while Netlas shows approximately 4,000 instances, a majority located in the United States. 
> 
> However, one researcher said only 215 of the devices found on Shodan appear to expose their management interface and are affected by CVE-2025-23006.
> 
> CISA has added CVE-2025-23006 to its Known Exploited Vulnerabilities (KEV) catalog, instructing federal agencies to address the flaw by February 14. 


This is nasty, and it’s been confirmed that it’s in active exploitation.

I’ll add that you really shouldn’t be exposing the admin panel of your security edge devices to the internet, please please stop doing this.  There are ways around it, and yes, there’s some nasty failure modes that might require sending an engineer onto site to manage, but this kind of issue just seems to keep cropping up.

If it’s not exposed to the internet, you might have bought yourself some time, but it’s probably still exposed to anyone who can get access inside your network, so you should prioritise patching this.


## [Court Documents Shed New Light on DOGE Access and Activity at Treasury Department ](https://www.zetter-zeroday.com/court-documents-shed-new-light-on-doge-access-and-activity-at-treasury-department/)

[https://www.zetter-zeroday.com/court-documents-shed-new-light-on-doge-access-and-activity-at-treasury-department/](https://www.zetter-zeroday.com/court-documents-shed-new-light-on-doge-access-and-activity-at-treasury-department/)

> According to signed affidavits filed on Tuesday by Treasury Department career executives defending the access they provided Elez, their staff implemented a number of security restrictions around Elez's access to Treasury systems. He was the only DOGE worker given direct access to the systems, for example, and he was prohibited from using his own laptop to access them. He could only connect using a Bureau-issued laptop that had "cybersecurity tools" installed on it to prevent him from accessing web sites or cloud-based storage services with the laptop or connecting a USB or other external storage device to it to copy large amounts of data from Treasury systems.
> 
> […]
> 
> All of this raises questions about previous reporting on what happened at Treasury. Did Wired, or its sources, get the story wrong in reporting that Elez had administrative-level privileges on Treasury payment systems?
> 
> It's possible that the reporters or their sources conflated "write" privileges to a database with administrative privileges on a network. Administrative privileges aren't generally referred to as "write" privileges. Possessing writing privileges for a database means that someone can add, delete or alter data in the database, but this has nothing to do with the ability to change underlying source code for the database or make the kind of network configuration changes that Wired described in its story.
> 
> It's notable, however, that Wired reported on February 4th that Elez had "write" privileges to Treasury payment systems. According to Gioeli he only obtained "write" privileges to one database on February 5th, the day _after_ the Wired story published. This raises questions about whether Treasury had intended to give him "write" access to the database all along, prompting an inside source to disclose this to Wired the day before administrators actually gave him that access, or whether Wired's sources confused the ability to alter a copy of source code with "write privileges" and administrative-level network access. 


I’ve been avoiding commenting on the DOGE news stories for a few weeks for precisely this reason.  Having worked in central government teams, I know how byzantine and complex the systems can be, and how distributed the systems can be.

A lot of the reporting was breathlessly reporting every step, misstep and action being taken, but phrases like “Administrative privileges” are actually significantly more nuanced than a lot of people realise.  And particularly in government organisations, it’s likely that sources and the journalists have a high probability of using language carelessly.  

This writeup covers a lot of what may have happened, and since it’s backed by court affidavits, it’s probably believable.  Nobody had this level of detail when breaking the stories, and I suspect that the sources and journalists legitimately believed that Elez had some administrative level accesses to “the system”.

I suspect that this entire thing is going to continue to create a lot of noise and headlines, but its worth taking them with a grain of salt at first. 


## [AI haters build tarpits to trap and trick AI scrapers that ignore robots.txt - Ars Technica ](https://arstechnica.com/tech-policy/2025/01/ai-haters-build-tarpits-to-trap-and-trick-ai-scrapers-that-ignore-robots-txt/)

[https://arstechnica.com/tech-policy/2025/01/ai-haters-build-tarpits-to-trap-and-trick-ai-scrapers-that-ignore-robots-txt/](https://arstechnica.com/tech-policy/2025/01/ai-haters-build-tarpits-to-trap-and-trick-ai-scrapers-that-ignore-robots-txt/)

> Building on an anti-spam cybersecurity tactic known as tarpitting, he created [Nepenthes](https://zadzmo.org/code/nepenthes/) , malicious software named after a carnivorous plant that will "eat just about anything that finds its way inside."
> 
> Aaron clearly warns users that Nepenthes is aggressive malware. It's not to be deployed by site owners uncomfortable with trapping AI crawlers and sending them down an "infinite maze" of static files with no exit links, where they "get stuck" and "thrash around" for months, he tells users. Once trapped, the crawlers can be fed gibberish data, aka Markov babble, which is designed to poison AI models. That's likely an appealing bonus feature for any site owners who, like Aaron, are fed up with paying for AI scraping and just want to watch AI burn.
> 
> Tarpits were originally designed to waste spammers' time and resources, but creators like Aaron have now evolved the tactic into an anti-AI weapon. As of this writing, Aaron confirmed that Nepenthes can effectively trap all the major web crawlers. So far, only OpenAI's crawler has managed to escape. 


This wholesale scanning and absorbtion of knowledge is the antethesis of the idea of mutualisation.  Mutualisation is summed up by the classic Eric Raymond quote, “Given enough eyeballs, all bugs are shallow”. The idea that lots of people will give up a tiny proportion of their time and knowledge into a mutually benefiting system, such as Wikipedia, StackOverflow or Quora.  

But part of that idea is that they feel that all of society is benefiting, rather than a single coporation.  Most communities tolerate that the place they provide free content often monetises it in order to pay the costs of continuing it, but as we’ve seen over the last few years with things like the Reddit blackouts, communities feel strongly if they think the corporates are abusing that position.

AI companies have been scraping all that knowledge, and the verdict is definitely out on whether AI is overall benefiting all of society, or just a small margin of people who can afford to pay a very small number of corporations for use of that knowledge.  

Free release of the models is helping for a lot of that, but in reality, the complexity in building, training and running those models still creates a moat around the system.

As more libertarian communities think about this more, we can expect more examples like this, of Anti-AI behaviours, tar pits and attempts to poison the well of human knowledge.

As someone who has created over 250 of these posts, all of which have likely been scraped, consumed and regurgitated by these models, I can say that the feelings around it are complex.  Is that what I intended when I wrote these words? Does their use by AI devalue them in any way?  These are all complex questions that we’re still grappling with on a societal basis 


