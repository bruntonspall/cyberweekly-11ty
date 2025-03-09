---
title: "26 - Small steps to knowledge, taking each one at a time"
date: 2018-11-17
description: "I enjoyed following a conversation this week about the value of a philosophy degree in infosec.  The conversation quickly descended into discussions about which philosopher would be more fun to have a beer with, which I didn't really follow (I still don't really know who Wittgenstein is, or whether I'd want a beer or not with him), but one of the things that the conversation reminded me of is that we have very poor interpretations of the real world."
permalink: /small-steps-to-knowledge-taking-each-one-at-a-time/
---

I enjoyed following a conversation this week about the value of a philosophy degree in infosec.  The conversation quickly descended into discussions about which philosopher would be more fun to have a beer with, which I didn't really follow (I still don't really know who Wittgenstein is, or whether I'd want a beer or not with him), but one of the things that the conversation reminded me of is that we have very poor interpretations of the real world.

We get confused when the real world doesn't follow the rules that we have made up in our head to explain the world, and it's this that causes people to disregard information that doesn't hold with their worldview.

Knowing that people think like this is incredibly important in cyber security or digital transformation, because despite all of the whizzy technology floating around, the core of both disciplines is about people.  It's about knowing how people behave, what they want and guiding them to do it in the most secure, safe and efficient manner.

However, the devil is in the details, because the real world is far more complex than the nice models that we construct for ourselves, and people never actually behave like rational agents in reality.  People will refuse to use digital services that might make things easier, cheaper and better for themselves our of sheer bloodymindedness or spite, and people will share their passwords even if they know they shouldn't.

Our biggest challenge as an industry is not just building good models of how to do this stuff right, but also coping with the complexity that we face when we try to implement those models, and understanding all of the edge cases that cannot possibly happen

## [Massive Data Leaks Keep Happening Because Big Companies Can Afford to Lose Your Data - Motherboard](https://motherboard.vice.com/en_us/article/bje8na/massive-data-leaks-keep-happening-because-big-companies-can-afford-to-lose-your-data)

[https://motherboard.vice.com/en_us/article/bje8na/massive-data-leaks-keep-happening-because-big-companies-can-afford-to-lose-your-data](https://motherboard.vice.com/en_us/article/bje8na/massive-data-leaks-keep-happening-because-big-companies-can-afford-to-lose-your-data)

> The 2018 Cost of a Data Breach Study from the Ponemon Institute and IBM pegs average costs per data breach globally at $3.86 million, including IT expenses, insurance, notification, and lost customers and business. In the US, the average is $7.91 million.
> 
> That might sound like a lot to you, but that number doesn't exist in a vacuum. The 477 companies studied had between 1,000 and 100,000 employees, with annual revenues from $100 million to more than $25 billion. To these companies, the cost of a breach "is a rounding error," said Larry Ponemon, chairman of the research firm, in a phone interview. "The company spends more money buying coffee for its office workers."
> 
> And then, the chance of a material breach over two years is 27.9 percent. That means an average annual cost globally of $538,000, or $1.1 million for US companies.


It's important for us in security to keep our eye on the top line and remember our place in these organisations.  Infosec, while incredibly important to us, is a tiny tiny proportion of the global spend in most companies, and even the risk of a breach isn't as expensive as we sometimes say.

Infosec professionals like to argue that a breach is essentially the end of the world, but in real monetary terms, it isn't.  Most are minor and will be forgotten a quarter later.  The problem is that you cannot predict whether the next one will be "the big one".

But we should bear this in mind when we think about what we are arguing for, because asking for ultra security at all times in just not proportional to our actual importance.


## [A leaky database of SMS text messages exposed password resets and two-factor codes | TechCrunch](https://techcrunch.com/2018/11/15/millions-sms-text-messages-leaked-two-factor-codes/)

[https://techcrunch.com/2018/11/15/millions-sms-text-messages-leaked-two-factor-codes/](https://techcrunch.com/2018/11/15/millions-sms-text-messages-leaked-two-factor-codes/)

> Although Kaul found the exposed server on Shodan, a search engine for publicly available devices and databases, it was also attached to to one of Voxox’s own subdomains. Worse, the database — running on Amazon’s Elasticsearch — was configured with a Kibana front-end, making the data within easily readable, browsable and searchable for names, cell numbers and the contents of the text messages themselves.
> 
> 
> An example of one text message containing a user’s phone number and their Microsoft account reset code. (Image: TechCrunch)
> 
> Most don’t think about what happens behind the scenes when you get a text message from a company, whether it’s an Amazon shipping notification or a two-factor code for your login. Often, app developers — like HQ Trivia and Viber — will employ technologies provided by firms like Telesign and Nexmo, either to verify a user’s phone number or to send a two-factor authentication code, for example. But it’s firms like Voxox that act as a gateway and converting those codes into text messages, to be passed on to the cell networks for delivery to the user’s phone.


Just as a reminder, everything is built on layers of abstraction, and most of the clients of this service probably didn't know it existed, or what it processed, since it was almost certainly the supplier, of a supplier probably of a supplier.


## [Russian Banks Under Phishing Attack](https://www.bleepingcomputer.com/news/security/russian-banks-under-phishing-attack/)

[https://www.bleepingcomputer.com/news/security/russian-banks-under-phishing-attack/](https://www.bleepingcomputer.com/news/security/russian-banks-under-phishing-attack/)

> International cybersecurity company Group-IB investigated the attack and noticed that the style and format of the fake communication were very similar to the official CBR correspondence. This supports the theory that the attackers had access to legitimate emails from CBR.
> 
> If Silence hackers have any ties with the legal side of reverse engineering and penetration testing, it is very likely that they are familiar with the documentation used by financial institutions and with how banking systems work.
> 
> In a report published today, Group-IB says that the attackers spoofed the sender's email address but the messages did not pass the DKIM (DomainKeys Identified Mail) validation. DKIM is a solution specifically designed to prevent forged email addresses by adding to the message a signature that confirms its authenticity.


Note that even good, competent hackers are still trying simple email spoofing rather than more complex attacks.  That's because it works most of the time because organisations don't enable DKIM.  

Irritatingly, DKIM is a brilliant protection for other people, and prevents spam being sent to other people looking like it came from you.  That makes it a weird technology from an economic perspective, as most of the time you won't directly benefit from implementing it.  But you should for the good of all of us, as it's highly effective against the simplest levels of email spoofing.


## [It’s Amateur Hour in the World of Spyware and Victims Will Pay the Price - Motherboard](https://motherboard.vice.com/en_us/article/bje8za/its-amateur-hour-in-the-world-of-spyware-and-victims-will-pay-the-price)

[https://motherboard.vice.com/en_us/article/bje8za/its-amateur-hour-in-the-world-of-spyware-and-victims-will-pay-the-price](https://motherboard.vice.com/en_us/article/bje8za/its-amateur-hour-in-the-world-of-spyware-and-victims-will-pay-the-price)

> But as tech-enabled privacy becomes easier, the need to break it has created a lucrative market of hacking-as-a-service for police and intelligence agencies that has attracted some ruthless, morally questionable, and often incompetent spyware companies. It’s undeniable that we need some of these technologies for targeted investigations into terrorism, organized crime, and child exploitation, but if spyware-enabled targeted attacks become so commoditized that they can be deployed on a large swath of the population, then they can become tools to spy on more than just a few suspected criminals.


This is a good summary of the problem with the market for lawful intercept and active surveillance products. 

There is a need for legally approved interception, but even the law within the uk is subjective depending on your position.  What is over reach, how are these judicial orders overseen and what controls and barriers exist?  It’s perfectly possible for UK citizens and government officials to hold completely different interpretations of the uk laws on such matters and that’s before we even consider how we judge the legitimacy of a foreign governments judicial oversight or the governments right to govern!


## [The Story Behind The Story That Created A Political Nightmare For Facebook | HuffPost](https://m.huffpost.com/us/entry/us_5b6c9b16e4b0530743c83f58?guccounter=2)

[https://m.huffpost.com/us/entry/us_5b6c9b16e4b0530743c83f58?guccounter=2](https://m.huffpost.com/us/entry/us_5b6c9b16e4b0530743c83f58?guccounter=2)

> This wasn’t an esoteric distinction. It was core to Facebook’s identity as a neutral platform upon which all the peoples of the world dance together. Facebook couldn’t admit in public that its “community” was logging into Facebook to chew over Fox News memes and racist Daily Caller stories. If it actually showed users what they were really talking about, the Trending news box would be a toilet. So it secretly hired humans to make editorial judgments (and treated them like shit, as Nuñez reported in a different story). That’s called publishing, and Facebook doesn’t want to be a publisher, in part because it doesn’t want to be held responsible for its judgments.


This is an interesting insight into Facebook itself. It has long trumpeted, like YouTube and others, that it is a neutral platform that doesn’t make editorial judgements. 

We know how that ended up, with the Russian disinformation campaign, but the thing to consider is that while there is a lot of concern about the big story of election interference by a state, there are millions of smaller stories of commercial companies paying for adverts, highly targeting them and attempting to influence their potential customers. 

I worked in a news organisation and the amount of thinking on how to improve the “social metric” for stories included what headlines got the most clicks, what pictures had the most engagement and how to best get your content out. This cycle of Facebook trying to editorialise their feed to match users expectations and commercial organisations try to increase engagement led to a nasty cycle which was exploitable. 


## [Japan's cyber-security minister has 'never used a computer' - BBC News](https://www.bbc.co.uk/news/technology-46222026#share-tools)

[https://www.bbc.co.uk/news/technology-46222026#share-tools](https://www.bbc.co.uk/news/technology-46222026#share-tools)

> A politician from the opposition Democratic Party, Masato Imai, whose question had prompted the admission, expressed surprise.
> "I find it unbelievable that someone who is responsible for cyber-security measures has never used a computer," he said.
> But Mr Sakurada responded that other officials had the necessary experience and he was confident there would not be a problem.
> 


I wasn’t going to cover this since I viewed it as showy meaningless journalisms but it kicked off a discussion on a slack instance I’m on. 

I would love for ministers who have a cyber security responsibility to have some expertise in cyber security matters, but I have two problems with that. 

Firstl, much like digital, I don’t think there should be a single minister responsible for such a thing. Digital (and cyber security) are an everyday part of all things now. You shouldn’t make a single person responsible for it. 

Secondly, we don’t expect a prisons minister to have been in prison or worked as a prison officer, a housing minister to have been a builder?  Maybe ministerial positions would be better there were experts in those positions but that’s never going to happen. Instead ministers rely on their staff to know and help them in those areas. 

The only possible story here, which wasn’t covered, is the lack of modern world understanding in a minister and whether that’s appropriate for any elected official, and I don’t think that their position as minister for cybersecurity is relevant. 


## [Forbidden spheres | Restricted Data](http://blog.nuclearsecrecy.com/2012/08/29/forbidden-spheres/)

[http://blog.nuclearsecrecy.com/2012/08/29/forbidden-spheres/](http://blog.nuclearsecrecy.com/2012/08/29/forbidden-spheres/)

> One weapons scientist explained to me how he breached security at Los Alamos simply by bringing a sack lunch into the plutonium facility. He left his lunch on his office desk and stepped out for a minute. He came back to find a commotion. A security officer informed him that the orange he left on his desk was, in fact, a classified object.
> 
> He learned that any spherical object became a nuclear secret once it passes over the line demarcating the secure from the open areas of the laboratory, as it could be taken as a model for the plutonium pit that drives a nuclear weapon.
> 
> The weapons scientist was told that in the future he could eat the fruit or store it inside his office safe with the rest of his classified documents, but if he left the orange out on his desk unsupervised it was a security infraction that could be referred to the FBI for investigation.


I've been reading up on classification policies this week (because I'm a huge nerd, not for any good reason) and was reminded of this outstanding story.

It's a good point to remember that parallel construction of classified approaches can happen, as did the creation of public key cryptography.  I'm sure that the GCHQ invented Public Key algorithm was properly classified at the time, but I'm wondering how people got around the fact that if you used the publicly available implementation, you were probably using something that you knew to be classified in an unclassified environment.

Secrecy and classifications is a weird weird world.


## [DOD file sharing tool disabled due to vulnerability](https://www.fifthdomain.com/dod/2018/11/12/dod-file-sharing-tool-disabled-due-to-vulnerability/)

[https://www.fifthdomain.com/dod/2018/11/12/dod-file-sharing-tool-disabled-due-to-vulnerability/](https://www.fifthdomain.com/dod/2018/11/12/dod-file-sharing-tool-disabled-due-to-vulnerability/)

> “AMRDEC SAFE was initially developed to facilitate the exchange of large data files between AMRDEC and its industry partners and customers. We recognize that the service provided by SAFE is now used by a variety of government agencies, and will continue to work with our higher headquarters to determine the appropriate way ahead,” the statement said.


We wrote this tool, just for our use. Now everyone is using it but their behaviour doesn’t match our original expectations. 

This is a story repeated over and over in Government and the commercial sector. 

But also, they reimplemented SFTP?  Most government sites would be better off following the “buy don’t build” method and using Dropbox or an SFTP server instead. Government just isn’t really that special


## [Sky Betting & Gaming Technology: How We Release So Frequently](https://engineering.skybettingandgaming.com/2016/02/02/how-we-release-so-frequently/)

[https://engineering.skybettingandgaming.com/2016/02/02/how-we-release-so-frequently/](https://engineering.skybettingandgaming.com/2016/02/02/how-we-release-so-frequently/)

> We don’t roll back database migrations. Ever. Technically we could - but we haven’t had a need to for at least four years now. That’s because every database migration we do results in a schema that’s compatible with the new version of our code and the previous one. If we have to roll back a code release (that does happen sometimes) then the previous version is perfectly happy using the new version of the schema.


This comes up time and time again for me.  I think it's something to do with ORM's and autogenerated schemas, but lots of developers seem to think that it's a good idea to auto-update database schemas on application startup, and that schema changes and software deploys should be tied together.

I'm a firm believer that these must remain separate if at all possible.  I've had many a chat with Tom about this, and he's done a really good job documenting why in this old blogpost.


## [Acoustic Kitty - Wikipedia](https://en.wikipedia.org/wiki/Acoustic_Kitty)

[https://en.wikipedia.org/wiki/Acoustic_Kitty](https://en.wikipedia.org/wiki/Acoustic_Kitty)

> In an hour-long procedure a veterinary surgeon implanted a microphone in the cat's ear canal, a small radio transmitter at the base of its skull and a thin wire into its fur.[1] This would allow the cat to innocuously record and transmit sound from its surroundings. Due to problems with distraction, the cat's sense of hunger had to be addressed in another operation.


I love the sense of invention here, as well as just a reminder of what kinds of weird things people will try to get inside their targets.


## [The Machine Fired Me](https://idiallo.com/blog/when-a-machine-fired-me)

[https://idiallo.com/blog/when-a-machine-fired-me](https://idiallo.com/blog/when-a-machine-fired-me)

> After lunch, two people appeared at my desk. One was a familiar long face that seemed to avoid making direct eye contact. It was Jose and his fellow security guard. He cordially informed me that he was to escort me out of the building.
> 
> The director was furious. They had received a very threatening email to escort me out of the building and were just doing their job.
> 
> "Who the hell is sending those emails!?"
> 
> I was fired. There was nothing my manager could do about it. There was nothing the director could do about it. They stood powerless as I packed my stuff and left the building.


So, I love this story, well written and humorous.  But it also tells me that someone somewhere actually loves a Joiners/Movers/Leavers process.  The Leavers process is often a very poor weak point in most systems, especially around contractors.  Find the right person leaving because their manager was fired and you'll find someone whose leaving forms and process was not done correctly.


