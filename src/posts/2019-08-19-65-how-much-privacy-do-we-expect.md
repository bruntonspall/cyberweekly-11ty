---
title: "65 - How much privacy do we expect?"
date: 2019-08-19
description: "Privacy is a really interesting concept to study.  People have lots of different mental concepts of privacy, and oftentimes those concepts don't entirely align with other humans conceptions of the same behaviours.  Couples talk about wanting privacy to be a couple together, and sometimes individuals wants privacy from their partner.  Groups of people who socialise build \"private parties\" and ways to segment themselves, and we tend to just keep using the same word over and over."
permalink: /how-much-privacy-do-we-expect/
---

Privacy is a really interesting concept to study.  People have lots of different mental concepts of privacy, and oftentimes those concepts don't entirely align with other humans conceptions of the same behaviours.  Couples talk about wanting privacy to be a couple together, and sometimes individuals wants privacy from their partner.  Groups of people who socialise build "private parties" and ways to segment themselves, and we tend to just keep using the same word over and over.

And yet, we hand data out like candy, even surprisingly private data at times.  We post updates to social networks and take photos of our food at fancy restaurants.  We give our address and phone number to every Dick, Tom, and Harry store that needs it, and we rarely consider how all of that data can be analysed or understood.

To be honest, a lot of data analytical firms also tend to overstate just how good their analytical capabilities actually are.  Many, if not all of them, are focused on advertising and advertising is a numbers game.  If you want to put adverts for new bags in front of potential consumers, you are hoping to put them in front of thousands of people all of whom have a higher than average desire to buy a new bag.  Getting a few hundred of those people mislabeled is a bad thing, and so analytical firms tend to be happy if their analysis is wrong about you as an individual, providing it's accurate in aggregate.

But as society gets more networked, and as organisations realise that this data can be used for more than just advertising (even Cambridge Analytica scandal was about selling political adverts at its essence), we start to see the scary side of data harvesting and abuse.

And the big problem is that as an individual, we really struggle to engage with privacy processes, because it's not clear what actually happens to that data, and the whole subject is so nuanced that different individuals have different lines of what they think is acceptable.  I don't think we have any good answers here yet (and I feel like I say that a lot at the moment), but it's good to see that across a variety of areas, from AI to biometrics, vehicle licenses to number plate recognition, there is a constantly moving discussion and battleground about what is acceptable, and what we can do to affect that conversation.

You'll notice a slightly different look today.  I had some feedback, months ago, that the large quotes in italic font can be hard to read, especially if you have dyslexia.  I've tried to format the quotes to be a little more readable, with no italic font, but still looking like a pull quote and feeling distinct.  As always, please let me know if you like it, hate it, can't read it.  I welcome all feedback.

## [He tried to prank the DMV. Then his vanity license plate backfired big time.](https://mashable.com/article/dmv-vanity-license-plate-def-con-backfire/?europe=true)

[https://mashable.com/article/dmv-vanity-license-plate-def-con-backfire/?europe=true](https://mashable.com/article/dmv-vanity-license-plate-def-con-backfire/?europe=true)

> It seemed that a privately operated citation processing center had a database of outstanding tickets, and, for some reason — possibly due to incomplete data on their end — many of those tickets were assigned to the license plate "NULL." In other words, the processing center was likely trying to tell its systems it didn't know the plates of the offending cars. Instead, with Droogie's vanity plate now in play, it pegged all those outstanding tickets on him.


(Joel) A mildly amusing/silly presentation from [Droogie](https://twitter.com/droogie1xp) at [DEF CON](https://www.defcon.org/).

Creating the license plate `NULL` with the DMV (US' DVLA/DVSA) went from 0 to 100 _very_ quickly by being assigned every other unassigned ticket rather than the expectation of being assigned no tickets.

In short, software development is hard and blacklisting software nuances can be just as important as [banned license plates](https://static.guim.co.uk/ni/1432313704619/List-of-Offensive-Suppresse.pdf).


## [We Asked Def Con Attendees Why People Are Still Getting Hacked - VICE](https://www.vice.com/en_us/article/j5yqn4/we-asked-def-con-attendees-why-people-are-still-getting-hacked)

[https://www.vice.com/en_us/article/j5yqn4/we-asked-def-con-attendees-why-people-are-still-getting-hacked](https://www.vice.com/en_us/article/j5yqn4/we-asked-def-con-attendees-why-people-are-still-getting-hacked)

> Why are people still getting hacked?
> 
> "I think the first question, put like this, is the modern equivalent to: why are things still getting stolen? People will always get hacked, the question is whether we can reduce the amount of hacks without causing too much external pain."


I think this is a really valid point out of an otherwise fairly so so writeup of DefCon attendees thoughts.  We seem to act sometimes like people hacking accounts is an anomaly, that if we were just better, or our users were just better, then it wouldn't happen at all.  By drawing the parallel with modern theft, we have to accept that the world is a fallen world in which bad people do bad things.  Instead of trying for an ideal of "zero-tolerence", we can have a much healthier attitude more akin to risk-management of reducing the incidence of hacking and reducing the impact of hacking to tolerable levels.

It will always be awful to be hacked, in the same way that it is always awful to get mugged, but we can make it so that the normal internet users are mostly safe, and work to reduce the risk.  


## [Infiltrating Corporate Intranet Like NSA - Pre-auth RCE on Leading SSL VPNs [pdf]](https://i.blackhat.com/USA-19/Wednesday/us-19-Tsai-Infiltrating-Corporate-Intranet-Like-NSA.pdf)

[https://i.blackhat.com/USA-19/Wednesday/us-19-Tsai-Infiltrating-Corporate-Intranet-Like-NSA.pdf](https://i.blackhat.com/USA-19/Wednesday/us-19-Tsai-Infiltrating-Corporate-Intranet-Like-NSA.pdf)

> Excessively detailed session file
> 
> • Session token
> • IP address
> • User name
> • Plaintext password


These are the slides from a great looking talk at DefCon about hacking TLS VPN's.  You can [read a blogpost writeup of some of the talk as well](https://blog.orange.tw/2019/08/attacking-ssl-vpn-part-2-breaking-the-fortigate-ssl-vpn.html).  These are the very common VPN systems that allow remote workers to dial into their workplace and access their work systems.  It turns out that there aren't very many of them, that most people install the same few ones, and this was some security researchers looking at what appeared to be the two most secure ones and finding a whole host of interesting bugs and behaviours with them.

Of this, the most terrifying was the fact that in several cases they found that the VPN device itself would log the plaintext passwords of every user who was authenticating to the VPN.


## [These Legit-Looking iPhone Lightning Cables Will Hijack Your Computer - VICE](https://www.vice.com/en_us/article/evj4qw/these-iphone-lightning-cables-will-hack-your-computer)

[https://www.vice.com/en_us/article/evj4qw/these-iphone-lightning-cables-will-hack-your-computer](https://www.vice.com/en_us/article/evj4qw/these-iphone-lightning-cables-will-hack-your-computer)

> It looks like a legitimate cable and works just like one. Not even your computer will notice a difference. Until I, as an attacker, wirelessly take control of the cable," the security researcher known as MG who made these cables told Motherboard after he showed me how it works at the annual Def Con hacking conference.
> 
> One idea is to take this malicious tool, dubbed O.MG Cable, and swap it for a target's legitimate one. MG suggested you may even give the malicious version as a gift to the target—the cables even come with some of the correct little pieces of packaging holding them together.
> 
> MG typed in the IP address of the fake cable on his own phone's browser, and was presented with a list of options, such as opening a terminal on my Mac. From here, a 


This is a cute hack, but shouldn't change your threat model for most of us.  The reality is that these cables are expensive, slightly limited in what they can do and therefore will be used almost exclusively in penetration tests and for security researchers to show off.

Bad USB cables, ports, charges and adapters are going to continue to show up, and given a sufficiently motivated threat actor with no other mechanism for getting onto your systems, they might be used, but the majority of real breaches will come via easier and less costly attack vectors.

Cute attack though, I kind of want one.


## [This Hacker Made Clothes That Can Confuse Automatic License Plate Readers​ - VICE](https://www.vice.com/en_us/article/qvgpvv/adversarial-fashion-clothes-that-confuse-automatic-license-plate-readers)

[https://www.vice.com/en_us/article/qvgpvv/adversarial-fashion-clothes-that-confuse-automatic-license-plate-readers](https://www.vice.com/en_us/article/qvgpvv/adversarial-fashion-clothes-that-confuse-automatic-license-plate-readers)

> Rose's designs mess with that process. She developed and tested the repeating patterns on her fabrics to look as close to a real plate as possible, so that the system will save it as real. "By wearing these designs on the street, you help introduce junk data into a surveillance system that could in a large scale make it less useful, more expensive to use," she said. "I think it's important to experiment with ways to be noncompliant with surveillance systems in whatever way we can, and I like clothing as an accessible first step."


As we see increases in computer vision implementations, we are going to see a rise in mechanisms to frustrate those implementations.  From bad QR codes to adverse inputs into neural networks, this constant vying of attacker and defender is normal and to be expected.
I'm more curious about whether using a random license plate like this has any form of data protection implication?  Those license plates are presumably actually registered to someone, and do they need to give permission?  What impact will it have on their life that they get seen all over the country?


## [Statement: Live facial recognition technology in King's Cross | ICO](https://ico.org.uk/about-the-ico/news-and-events/news-and-blogs/2019/08/statement-live-facial-recognition-technology-in-kings-cross/)

[https://ico.org.uk/about-the-ico/news-and-events/news-and-blogs/2019/08/statement-live-facial-recognition-technology-in-kings-cross/](https://ico.org.uk/about-the-ico/news-and-events/news-and-blogs/2019/08/statement-live-facial-recognition-technology-in-kings-cross/)

> “I remain deeply concerned about the growing use of facial recognition technology in public spaces, not only by law enforcement agencies but also increasingly by the private sector. My office and the judiciary are both independently considering the legal issues and whether the current framework has kept pace with emerging technologies and people’s expectations about how their most sensitive personal data is used.
> 
> “As well as requiring detailed information from the relevant organisations about how the technology is used, we will also inspect the system and its operation on-site to assess whether or not it complies with data protection law.
> 
> “Put simply, any organisations wanting to use facial recognition technology must comply with the law - and they must do so in a fair, transparent and accountable way. They must have documented how and why they believe their use of the technology is legal, proportionate and justified.


This will be an interesting investigation to watch.  I happen to like the restaurants over in Coal Drops Yard near Kings Cross, and while I'm mostly comfortable with their CCTV systems using facial recognition, I can see why a lot of people are not. 
At the moment there is very little guidance about when it is acceptable to use such a tool, and how you need to handle the information, faces and data that you gather.  Better guidance from the ICO as to what purpose facial recognition can be used for, and ways to make it safe would be welcome.

It also reminds me of the recent story of [BarAI, a tool for using facial recognition to make bar tending easier](https://mashable.com/video/bar-facial-recognition-queue-jumpers/?europe=true) which if the data is held locally, deleted after a few hours, and used only for the purpose stated, I don't have a concern about.  But it will be hard to know whether that's true, and almost impossible to withdraw or refuse consent to be processed in such a way.


## [The List of 2,000 Journalists the Video Game Lobby Doxed Is the Last Thing It Had to Offer - VICE](https://www.vice.com/en_us/article/gyzxkj/the-list-of-2000-journalists-the-video-game-lobby-doxed-is-the-last-thing-it-had-to-offer)

[https://www.vice.com/en_us/article/gyzxkj/the-list-of-2000-journalists-the-video-game-lobby-doxed-is-the-last-thing-it-had-to-offer](https://www.vice.com/en_us/article/gyzxkj/the-list-of-2000-journalists-the-video-game-lobby-doxed-is-the-last-thing-it-had-to-offer)

> You always know when you give a convention your personal info that a lot of it is going to end up in someone else’s hands, such as public relations people whose literal job is to connect with media. It’s just that most PR reps who see such lists are smart enough not to make use of anything more invasive than email. In other words, a lot of private information of mine does end up in strangers’ hands, but I trust those strangers to be professional and responsible. 


There is something about this, about this attitude that I think we forget when we talk to people about privacy.  Most people are happy and content to hand over their private information in exchange for something of minimal value because they believe that most organisations are professional and responsible with that information.

Many of the breaches show us that this isn't always the case, but because we focus on the breaches and other newsworthy events, we tend to forget that we hand our data over thousands of times a day and the vast majority of it isn't misused.  More importantly, normal people have that experience every day which reinforces that it is safe to hand over your information and makes any education campaign about data privacy unlikely to resonate with their real experiences.


## [Cracking my windshield and earning $10,000 on the Tesla Bug Bounty Program | Sam Curry](https://samcurry.net/cracking-my-windshield-and-earning-10000-on-the-tesla-bug-bounty-program/)

[https://samcurry.net/cracking-my-windshield-and-earning-10000-on-the-tesla-bug-bounty-program/](https://samcurry.net/cracking-my-windshield-and-earning-10000-on-the-tesla-bug-bounty-program/)

> After spending more time messing with the input I saw that the allowed content length for the input was very long. I decided to name the Tesla my XSS hunter payload and continued toying around with the other functionalities on the car.
> 
> The other thing I spent a lot of time messing with was the built in web browser. I wasn’t able to get this to do anything even remotely interesting but had a fun time trying to get it to load in files or strange URIs.
> 
> I couldn’t find anything that evening so I called it quits and forgot that I’d set my car name to a blind XSS payload.


This is a cute (if accidental) attack.  Naming your car didn't provoke any bad behaviour in the frontend systems, but when returned to the factory for some testing, the internal tools used by Tesla were not as well written as the production code on the car or customer facing systems, and therefore they choked on the input.

For attackers, getting bad input into your systems can mean that it gets processed and can exploit something far further back than your frontend systems, and of course developers and teams building internal tools rarely have the time, energy or money to do a full security audit on tools that only internal teams can access


## [APT41: A Dual Espionage and Cyber Crime Operation | FireEye Inc](https://www.fireeye.com/blog/threat-research/2019/08/apt41-dual-espionage-and-cyber-crime-operation.html)

[https://www.fireeye.com/blog/threat-research/2019/08/apt41-dual-espionage-and-cyber-crime-operation.html](https://www.fireeye.com/blog/threat-research/2019/08/apt41-dual-espionage-and-cyber-crime-operation.html)

> Today, FireEye Intelligence is releasing a comprehensive report detailing APT41, a prolific Chinese cyber threat group that carries out state-sponsored espionage activity in parallel with financially motivated operations. APT41 is unique among tracked China-based actors in that it leverages non-public malware typically reserved for espionage campaigns in what appears to be activity for personal gain. Explicit financially-motivated targeting is unusual among Chinese state-sponsored threat groups, and evidence suggests APT41 has conducted simultaneous cyber crime and cyber espionage operations from 2014 onward.


Your reminder that the skills of nation state hackers are sometimes deployed for their own financial gain.  In this case, APT41 is suspected of being essentially freelance, able to conduct financial crime hacking operations on their own time as well as being tasked and given capabilities for espionage level operations.  The line between state level capabilities and high end organised crime is increasingly getting blurred which is worrying.


## [Teen claims to tweet from her smart fridge – but did she really? | Technology | The Guardian](https://www.theguardian.com/technology/2019/aug/13/teen-smart-fridge-twitter-grounded)

[https://www.theguardian.com/technology/2019/aug/13/teen-smart-fridge-twitter-grounded](https://www.theguardian.com/technology/2019/aug/13/teen-smart-fridge-twitter-grounded)

> Dorothy spoke to the Guardian on Tuesday over Twitter. She declined to share her last name and said she was messaging from her cousin’s iPad because she was still facing a tech ban.
> 
> She said she was 15 and her mother had disciplined her two weeks ago after she got too distracted while cooking and caused a fire.
> 
> “She took all my tech so I’d pay more attention to my surroundings,” she said. “I felt mortified! I was worried because I’ve been bored all summer and Twitter passes the time for me”, she added.
> 
> Dorothy also said she was worried about losing her “mutuals” – accounts she follows that follow her back – and devised other ways to get tweets out. Her self-described “fan account” is used primarily to send tweets about Ariana Grande.
> 
> After reports emerged questioning Dorothy’s account, LG confirmed that some of its fridge models have social media capabilities, but the company could not confirm whether Dorothy’s tweet was sent from one.
> 
> This story was updated on 15 August with additional reporting casting doubt on the accuracy of Dorothy’s claims, including the analysis of Luca Hammer and Igor Brigadir. It also includes fresh comments from LG.


I'm a bit disappointed with the guardian on this one.  The original story here had the journalist interview Dorothy online and confirm her story, but the journalist did not do the digging to discover whether LG Smart Fridge was in fact a registered twitter application.  I was tempted to register a fake application just to demonstrate how it could be done, when I went back to this article to bookmark it, the article had been updated to cast doubt on the claim.

There is a note at the bottom to show that there is additional reporting, but it doesn't really say that they got it wrong and had a completely misleading headline before.

When it comes to social media and other online persona's, I'm afraid we have to be a bit cynical and assume that a lot of it isn't true.  That doesn't mean we have to be that person on twitter to replies to say it's not true, we can enjoy a story for what it is, but we do need to remember that these things are commonly not true, and that online it is far easier to fake attribution than it ever was before


## [Toward an Information Operations Kill Chain - Lawfare](https://www.lawfareblog.com/toward-information-operations-kill-chain)

[https://www.lawfareblog.com/toward-information-operations-kill-chain](https://www.lawfareblog.com/toward-information-operations-kill-chain)

> Step 1: Find the cracks in the fabric of society—the social, demographic, economic and ethnic divisions.
> 
> Step 2: Seed distortion by creating alternative narratives. In the 1980s, this was a single “big lie,” but today it is more about many contradictory alternative truths—a “firehose of falsehood”—that distorts the political debate.
> 
> Step 3: Wrap those narratives in kernels of truth. A core of fact helps the falsities spread.
> 
> Step 4: (This step is new.) Build audiences, either by directly controlling a platform (like RT) or by cultivating relationships with people who will be receptive to those narratives.
> 
> Step 5: Conceal your hand; make it seem as if the stories came from somewhere else.
> 
> Step 6: Cultivate “useful idiots” who believe and amplify the narratives. Encourage them to take positions even more extreme than they would otherwise.
> 
> Step 7: Deny involvement, even if the truth is obvious.
> 
> Step 8: Play the long game. Strive for long-term impact over immediate impact.
> 
> None of these defensive actions is sufficient on its own. In this way, the information operations kill chain differs significantly from the more traditional cybersecurity kill chain. The latter defends against a series of steps taken sequentially by the attacker against a single target—a network or an organization—and disrupting any one of those steps disrupts the entire attack. The information operations kill chain is fuzzier. Steps overlap. They can be conducted out of order. It’s a patchwork that can span multiple social media sites and news channels. 


This is interesting thought processes, but I think is deeply misleading both in its title and its execution.  The cyber kill chain (TM Lockheed Martin) is about determining that a successful attack requires a number of steps, and that the failure of any one step will prevent the entire operation from being carried out.  
It's an arguably useful model for defenders because it encourages defenders to look for a wider spectrum of attack signals, so that they can catch and kill attacks before they start.  In a world where the final stages of an attack can be brutally fast, this is critical.

Disinformation campaigns aren't like that, and this Lawfare article even points it out.  If you are able to affect an early stage of an operation, then the operation might be less effective, but it won't stop it.  It's therefore not a kill chain at all.

Why does that matter?  Because there are a lot of people who haven't studied any of this stuff, and will attempt to apply the model/language/thinking from one kill chain to another.  And that cognitive dissonance will cause more problems than it will solve.

As a model for 7 critical factors in disinformation, I think this is a reasonable model, but when defending against it, we need to defend against all 7 factors at once, and possible equally, rather than focusing on the early stages first.


## [The Risk of Racial Bias in Hate Speech Detection [pdf]](https://homes.cs.washington.edu/~msap/pdfs/sap2019risk.pdf)

[https://homes.cs.washington.edu/~msap/pdfs/sap2019risk.pdf](https://homes.cs.washington.edu/~msap/pdfs/sap2019risk.pdf)

> Toxic language (e.g., hate speech, abusive speech, or other offensive speech) primarily targets mem- bers of minority groups and can catalyze real- life violence towards them (O’Keeffe et al., 2011; Cleland, 2014; Mozur, 2018). Social media platforms are under increasing pressure to re- spond (Trindade, 2018), but automated removal of such content risks further suppressing already- marginalized voices (Yasin, 2018; Dixon et al., 2018). Thus, great care is needed when develop- ing automatic toxic language identification tools.
> The task is especially challenging because what is considered toxic inherently depends on social context (e.g., speaker’s identity or dialect). In- deed, terms previously used to disparage com- munities (e.g., “n*gga”, “queer”) have been re- claimed by those communities while remaining offensive when used by outsiders (Rahman, 2012). Figure 1 illustrates how phrases in the African American English dialect (AAE) are labelled by a publicly available toxicity detection tool as much
> more toxic than general American English equiv- alents, despite their being understood as non-toxic by AAE speakers (Spears, 1998, see §2).


I've [seen](https://www.forbes.com/sites/nicolemartin1/2019/08/13/googles-artificial-intelligence-hate-speech-detector-is-racially-biased/#1fd06b93326c) [a lot](https://techcrunch.com/2019/08/14/racial-bias-observed-in-hate-speech-detection-algorithm-from-google/) of [writeups](https://www.newscientist.com/article/2213064-googles-hate-speech-detecting-ai-appears-to-be-racially-biased/) about this, but the actual academic paper is really well written and understandable.

The problem really boils down to one of context and dialectical issues.  AI that is trained on bulk data will fail to see that language is so flexible that what is used in one context can mean something totally different in a second context.  In this case, language marked as toxic can and has been reclaimed by communities, but only within certain behaviour contexts.

In short, AI isn't going to save us, because we are still complicated animals and unbelievably complicated social creatures.  This is worth remembering when you read the next link about countering disinformation.


