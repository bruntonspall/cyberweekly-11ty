---
title: "203 - AI is the new hotness"
date: 2022-07-17
description: "Phew!"
permalink: /ai-is-the-new-hotness/
---

Phew!

This newsletter is bought to you, late, in absolutely scorching weather in the UK that has made it too hot to sit and read in my office, and especially to sit and write this introduction.

I had lots of thoughts and ideas about the role of AI in cybersecurity, and what it means, but the heatwave caught up with me before I wrote them down, so you’ll have to make do with some slightly muted thoughts.

AI has been an ongoing “new thing” for a decade or more now, and that’s the second rise of AI, after a massive growth in AI back in the 70’s that died and slumped into a winter of low investment and low interest.

But increasingly in the last few years, Generalised AI has come on in leaps and bounds. There’s a kind of fools errand around the idea of complete isolated AI that can replicate human decision making and replace humans in the decision loop. We might get there, but outside of specialise areas, such as drone racing around a fixed course, it’s liable to take longer than currently expected.

In the meantime Dall-E and GPT-3 are capable of some amazing user guided things. The concept of AI being something you turn to, you query and interact with, and that assists users in decision making rather than supplants users is here much sooner than we thought.

The security implications however are quite something, because users will learn to trust, potentially unthinkingly, the answers that the AI will give them. In a world where there can exist adverbial attacks on the underlying AI, that can be quite scary. We have systems that are fundamentally inexplicable, that you interact with through a series of known and shared incantations, and it’s going to be incredibly complex to understand who made what decision and why.

## The Cyberweekly Survey

As I’ve been doing this newsletter for nearly 4 years, I decided that it was time to find out if I’m doing a good job. I can tell from subscriptions that more and more people are subscribing, but I don’t know what’s working well or badly. I’ve put together some simple questions into a Google Form, and if you’ve got 2-5 minutes, I’d really appreciate some feedback. You can find the Form here: [https://docs.google.com/forms/d/e/1FAIpQLSeojV4ILcB7Oz9rPtNMPHCGRFL1ctfaiwpS2ZvsOqbCBDu9rA/viewform?usp=sf_link](https://docs.google.com/forms/d/e/1FAIpQLSeojV4ILcB7Oz9rPtNMPHCGRFL1ctfaiwpS2ZvsOqbCBDu9rA/viewform?usp=sf_link)

## Cyber Weekly website

One of the things that I hadn’t really realised that I hadn’t shared, and requested by a few of you in survey comments, is that as well as putting this newsletter out by email, you can also read online at [Cyberweekly.net](https://cyberweekly.net).  This is the web version of the same newsletter, and although hosted on Google’s CloudRun service, it’s otherwise completely ad, tracker and surveillance free, so if the tracking on urls built into Substack bugs you, then feel free to use that.  

It doesn’t yet support an RSS/ATOM feed, but that’s on my todo list, so you will be able to follow there if you prefer.

## [Using GPT-3 to explain how code works ](https://simonwillison.net/2022/Jul/9/gpt-3-explain-code/)

[https://simonwillison.net/2022/Jul/9/gpt-3-explain-code/](https://simonwillison.net/2022/Jul/9/gpt-3-explain-code/)

> As with everything GPT-3, this answer sounds very convincing! But is this actually true? I would expect the SQL query optimizer to be smart enough to optimize the `LEFT JOIN` to the point where it would run efficiently. I think GPT-3’s answer to that question is actually very misleading.
> 
> 
> And that’s not surprising, because GPT-3 doesn’t actually know anything about anything at all. It’s a huge pattern generator. You can’t trust anything it says, because all it does is group words together into convincing looking shapes based on text that it’s seen before.
> 
> 
> Once again, I’m reminded that tools like GPT-3 should be classified in the “bicycles for the mind” category. You still have to know how to peddle!
> 
> 
> They’re fantastic tools for thinking, but to actually use their output effectively requires VERY deep knowledge—both of the subject matter in question, and of the way that the AI tools themselves work. 


This, by Simon Willison, is a fantastic exploration of some of the things you can do with GPT-3 as a tool to assist in understanding code.

His warning here though is probably the most important part.  However smart it seems, in reality, GPT doesn’t actually understand the code, it’s just pattern matching against a vast number of inputs.  So you need to make sure that you can sanity check the output, which requires the skills the do the work without the AI.  That means that AI is a good accelerator of understanding, rather than a replacement for understanding. 


## [By Design – Rands in Repose ](https://randsinrepose.com/archives/by-design/)

[https://randsinrepose.com/archives/by-design/](https://randsinrepose.com/archives/by-design/)

> **Your Job as a Leader** Your job as a leader is not to make the hard calls. That’s ego talking. Your job as a leader is to clearly explain how you made the hard call so that your team understands how you think, what strategy you are employing, and what principles you are following.
> 
> If you have no strategy, you take the time to define it. If you don’t have principles by which to make this decision, you work quickly with as many humans as possible to clearly define them. A principle is a fundamental truth. It’s a foundation for a system of belief or behavior or for a chain of reasoning and you bet they’re hard to define, but that’s your job.
> 
> By design. 


Thought provoking and quite powerful.

We learn best from mistakes, and it’s far better to learn from someone else’s mistakes than make your own.

If you are not doing the hard work to make your decisions and your strategy visible to your team, then you aren’t doing your job properly.

And sure, there might be company equities that you cannot share, information that isn’t appropriate to share with people, but you owe it to your staff to at least let them know that you are using data points that they can’t see to make decisions.  If you are transparent and clear about your decision making processes the rest of the time, your team will learn to build trust in you, and know that your explanations based on hidden data are at least internally coherant. 


## [I deleted 78% of my Redis container and it still works | by Vinod Gupta | Jun, 2022 | Medium ](https://medium.com/@codervinod/i-deleted-78-of-my-redis-container-and-it-still-works-df8310a3a007)

[https://medium.com/@codervinod/i-deleted-78-of-my-redis-container-and-it-still-works-df8310a3a007](https://medium.com/@codervinod/i-deleted-78-of-my-redis-container-and-it-still-works-df8310a3a007)

> The results from hardening these images were impressive:
> * The Redis image shrank from 96 MB to 21 MB.
> * 66% of the known CVE(s) were removed.
> * Of 74 critical and high CVEs, the CVE scanner found only thirty-six in the hardened image.
> * All 4 CVEs with published proofs of concepts (POCs) were removed. CVEs with a published POC present a higher risk and a Rapid Risk Score (RRS) is a measure of this risk. More about RRS (POC) [here](https://www.rapidfort.com/post/prioritizing-vulnerability-by-severity-is-a-losing-battle) . 


There’s nothing new in here that hasn’t been said before, but I thought the stats were interesting.

Instead of starting with a full base image, with a lot of Ubuntu/Debian/Fedora installed, do try starting with a base image with minimal possible kernel, and then add your application on top.

Not only will your docker containers be smaller, but they will be more secure, and easier to update in future. 


## [The DALL·E 2 Prompt Book – DALL·Ery GALL·Ery ](https://dallery.gallery/the-dalle-2-prompt-book/)

[https://dallery.gallery/the-dalle-2-prompt-book/](https://dallery.gallery/the-dalle-2-prompt-book/)

> _3D render, cute robot holding up a warning sign, shallow depth of field_ **Nothing you are about to see is real. For real.** The following document contains: 
> 
> ⚠️ photos that are not real photos
> ⚠️ paintings that are not real paintings, and
> ⚠️ people, places and things that **do not exist.** The images you are about to see were all created by an AI tool called DALL·E 2.
> 
> All images are © Open AI. 


I’ve been watching Dall-E for a while and I think the impact of it has been massively underestimated.  Looking through this great prompt book, you can begin to see how it’s far beyond just a toy demonstration of AI that makes funny pictures and how it can be used as a real tool. 


## [Whitepaper – Practical Attacks on Machine Learning Systems – NCC Group Research ](https://research.nccgroup.com/2022/07/06/whitepaper-practical-attacks-on-machine-learning-systems/)

[https://research.nccgroup.com/2022/07/06/whitepaper-practical-attacks-on-machine-learning-systems/](https://research.nccgroup.com/2022/07/06/whitepaper-practical-attacks-on-machine-learning-systems/)

> 1.1 Conclusions - Is this worth worrying about?
> 
> A quick glance at the references section of this document should demonstrate that there is a sizeable - and
> rapidly growing - body of evidence suggesting several uncomfortable truths:
> 
> * Training an ML system using sensitive data appears to be fundamentally unsafe, in the sense that the data used to train a system can often be recovered by attackers in a variety of ways (Membership Inference, Model Inversion, Model Theft, Training Data Extraction)
> * Neural Network classifiers appear to be “brittle”, in the sense that they can be easily forced into misclassifications by adversarial perturbation attacks. While countermeasures exist (e.g. [Madry2017]) these countermeasures are reported to reduce accuracy and may render the system more vulnerable to other forms of attack ([Song2019b])
> * High-fidelity copies of trained models can be extracted by remote attackers by exercising the model and observing the results
> 
> While exploiting these issues is not always possible due to various mitigations that may be in place, these
> new forms of attack have been demonstrated and are certainly viable in practical scenarios.
> 
> These alarming new forms of attack supplement the “traditional” forms of attack that still apply to all ML
> systems; they are still subject to infrastructure issues, web application bugs and the wide variety of other
> problems, both old and new, that modern cloud-based systems often suffer. 


This is a great review of attacks that you might need to consider if you are using machine learning systems.  One of the big worries about ML systems is that they are simply black boxes that seem to work via magic to most people. Adversarial peturbation attacks, in this case the simplest algorithm of adding random noise to a photo until it misclasifies a photo can change an image recognition from a dog into a golf cart in just a few minutes.  

When we start to rely on these systems, understanding how they can be attacked, and what the implications are is going to be increasingly important for security professionals 


## [Autonomous Drones Challenge Human Champions in First “Fair” Race - IEEE Spectrum ](https://spectrum.ieee.org/zurich-autonomous-drone-race)

[https://spectrum.ieee.org/zurich-autonomous-drone-race](https://spectrum.ieee.org/zurich-autonomous-drone-race)

> A year ago, autonomous racing quadrotors from Davide Scaramuzza’s [Robotics and Perception Group](https://rpg.ifi.uzh.ch/) at the University of Zurich (UZH) [proved that they could beat the world’s fastest humans in a drone race](https://www.media.uzh.ch/en/Press-Releases/2021/Drone-Race.html) . However, the drones relied on a motion-capture system to provide very high resolution position information in real time, along with a computer sending control information from the safety and comfort of a nearby desk, which doesn’t really seem like a fair competition. [Earlier this month](https://swissdronedays.com/) , a trio of champion drone racers traveled to Zurich for a rematch, but this time, the race would be fair: no motion-capture system. Nothing off-board. Just drones and humans using their own vision systems and their own computers (or brains) to fly around a drone racing track as fast as possible.
> To understand what kind of a challenge this is, it’s important to have some context for the level of speed and agility. So here’s a video of one of UZH’s racing drones completing three laps of a track using the motion-capture system and off-board computation.
> 
> […]
> 
> As Thomas says at the end of the video, the autonomous drone made it through one lap of the course in 5.3 seconds. With a peak speed of 110 kilometers per hour, this was a staggering 1.8 seconds per lap faster than Thomas, who has twice won FPV drone racing’s [MultiGP International World Cup](https://www.multigp.com/) .
> 
> The autonomous drone has several advantages in this particular race. First, it has near-perfect state estimation, thanks to a motion-capture system that covers the entire course. In other words, the drone always knows exactly where it is, as well as its precise speed and orientation. Experienced human pilots develop an intuition for estimating the state of their system, but they can’t even watch their own drone while racing since they’re immersed in the first-person view the entire time. The second advantage the autonomous drone has is that it’s able to compute a trajectory that traverses the course in a time-optimal way, considering the course layout and the constraints imposed by the drone itself. Human pilots have to practice on a course for hours (or even days) to discover what they think is an optimal trajectory, but they have no way of knowing for sure whether their racing lines can be improved or not. 


This is astonishingly impressive.  The ability to track where a drone is, where it needs to go and how to best achieve the goal is the sort of thing that AI is excellent at, but the timings involved is just amazing.  Completing a lap of the course in 5.3 seconds means that the drone is making thousands of decisions a second, and having to search ahead to handle a complex and changing environment around it.

Of course, a static course and a goal of simply travelling round it as fast as possible is far easier than working in the real world, with changing environment, no predetermination of what it looks like, and complex interactions, but it bodes well for autonomous vehicles 


## [Markov Chat Bot Disaster Story · GitHub ](https://gist.github.com/aconbere/1982a5eb17b77817017a3da50914732f)

[https://gist.github.com/aconbere/1982a5eb17b77817017a3da50914732f](https://gist.github.com/aconbere/1982a5eb17b77817017a3da50914732f)

> Chat ops was this idea of having your chat service be the source of truth for operations control. So if you wanted to spin up a new server, you wrote a mystical command into your companies chat service and a bot would go and execute that command. This cultural idea helped ambiently expose and teach people about how to run operations commands, and forced the team to build ergonomic tools for operations. At Etsy the chat service was IRC and there was a program irccat that would execute commands. It was easy to add commands to irccat and it was used for everything from keeping track of little karma kudos from your team to rebalancing database servers.
> 
> I thought this was great fun, and turned it into my hack week project. I made short hack week presentation where I wrote another little irc bot that would hash all the participants names in a channel and map them to voice in the `say` command and then have them all talk to each other out loud. This would have been the end of the story, except one day, our coworker Moishe woke up to see that he had earned 30,000 "plusses" (Ety's karma points) over night. Moishe is incredible, and so it wasn't surprising that he'd gotten a lot of plusses, but 30,000 was a lot even for Moishe. And Moishe wasn't the only one reporting oddities. I'm sure it's obvious looking back, but at some point one of the bots had issued a command to invite irccat the chatops bot into #purgatory, and the bots had been happily "++"'ing colleagues over and over.
> 
> This ++ storm wasn't particularly dangerous and certainly created some interesting discussions about how Markov chains bias results. The terrifying realization was that if the bots could execute the ?++ command they could also execute all the other chatops commands, the ones that tear down servers, the ones that kill processes, all the scary possibilities of chatops turned into a kind of markov chaos monkey. My recollection on review was that we hadn't found any other successful commands executed (there are differing accounts of this), but needless to say I was asked to decommission #purgatory for the safety of Etsy. 


This is an interesting story, and a reminder that ChatOps, while great for all the reasons that Anders points out here, also means that your chat system is now part of your production deployment system.  

That means that the security of who you let into your chat system, what can be done and what protections you need should mirror that of giving someone access to production, or at least highly visible and automated access to production. 


## [Defensive CSS - Introduction to Defensive CSS ](https://defensivecss.dev/articles/intro-defensive-css/)

[https://defensivecss.dev/articles/intro-defensive-css/](https://defensivecss.dev/articles/intro-defensive-css/)

> Back in December 2021, I wrote an article titled [Defensive CSS](https://ishadeed.com/article/defensive-css/) . I used that term because that's really what is it about. I wanted a term that communicates the concept of writing CSS that prevents unexpected layout behaviors, or at least, reduces them.
> 
> It turned out that defensive CSS doesn't only apply to CSS, but UI design as well. As a designer, you need to either work on visual variations of a component with all the possible use-cases or at least communicate them clearly with the development team.
> In this introduction article, I will shed the light on why it's important to design and write CSS defensively, and how we can take it from there. **Content can break layouts** [**#**](https://defensivecss.dev/articles/intro-defensive-css/#content-can-break-layouts) One of the common reasons for having layout issues in CSS is content. Be it short or long, it can break a layout if we haven't thought carefully about it. 


Lovely set of patterns for how to code defensively in a user interface, to ensure that unexpected content and unexpected input doesn’t break your layout. 


## [Cryptanalyzing MEGA in Six Queries ](https://eprint.iacr.org/2022/914)

[https://eprint.iacr.org/2022/914](https://eprint.iacr.org/2022/914)

> In recent work, Backendal, Haller, and Paterson identified several exploitable vulnerabilities in the cloud storage provider MEGA. They demonstrated an RSA key recovery attack in which a malicious server can recover the client’s RSA private key. Their attack uses binary search to recover the private RSA key after 1023 client logins, and optionally could be combined with lattice methods for factoring with partial knowledge to reduce the number of logins to 512 in theory, or 683 in the published proof of concept. In this note, we give an improved attack that requires only six client logins to recover the secret key. Our optimized attack combines several techniques, including a modification of the extended hidden number problem and the structure of RSA keys, to exploit additional information revealed by MEGA’s protocol vulnerabilities. MEGA has emphasized that users who had logged in more than 512 times could have been exposed; these improved attacks show that this bound was conservative, and that unpatched clients should be considered vulnerable under a much more realistic attack scenario. 


This is an interesting set of attacks, showing how once an attack can be identified, it’s possible to dramatically improve the attack capability with further work. 

However, in this case, it’s a great example of dramatically improving an attack that’s probably not relevant to the threat model.  The attack requires the user to attempt to log in to a client system multiple times, and it will use that to attack the underlying cryptographic system.  But of course, if an attacker can present and control the client interface, it’s far easier to simply inject something to steal the users passwords, or the data from their account. 

So, as a learning path for how cryptographic attacks can be weaponised, this is a great read.  As an actual realistic attack on Mega, I’m not convinced that it provides anything earth shattering. 


## [An Information Security Reference That Doesn't Suck!(Much)](https://rmusser.net/docs/index.html)

[https://rmusser.net/docs/index.html](https://rmusser.net/docs/index.html)

> The goal of this project is to act as a free resource for anyone interested in learning more about Information Security.
> 
> * A list of techinques, tools and tactics to learn from or reference.
> * Rich resource of infosec knowledge for anyone to browse through as a jumping off point for various niches OR as a reference/recall method for stuff.
> * Something like a "Yellow Pages" in the sense of you know something exists, but what was it called....
> * 'If you give a man a fish, he is hungry again in an hour. If you teach him to catch a fish, you do him a good turn.'
> * To be clear, these aren't personal notes. I keep this repo maintained as a way of having pointers to information that I feel might help build someone's skillset or increase their understanding of attacks/methods/defenses.


This is a nice reference manual of resources for information security


