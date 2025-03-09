---
title: "12 - Should we trust cyber security stats?"
date: 2018-08-11
description: "Several articles this week about various statistics in cybersecurity, which makes me question the mechanism by which we gather these statistics and how they are presented."
permalink: /should-we-trust-cyber-security-stats/
---

Several articles this week about various statistics in cybersecurity, which makes me question the mechanism by which we gather these statistics and how they are presented.
The cybersecurity vendors have an explicit desire to bulk up the risk, so you'll buy their products, "just look at how many advanced cyber campaigns are happening and how our black box will fix it" kind of thing.
But even well meaning surveys suffer from a variety of problems.  We don't have consistent definitions of a breach, is emailing that spreadsheet to someone on purpose a breach? How about if someone outside the organisation got cc'd by mistake on an email thread? What about if a security researcher found a vulnerabiity and responsibly disclosed it to us?
Given even this, how are we to take statistics about the number of breaches, the average cost of breaches, or almost any other number in cybersecurity seriously?

Even worse, as you'll see in the ONS survey below, when we ask users questions, they have a different context in mind.  One of the questions asked if users had "antispam" software on their phone, and I made a joke about it in a Slack instance, for someone to remind me of those apps that identify incoming callers that are unwanted sales calls.  If I had that software on my phone, and someone asked me if I had an "antispam" app, I would never associate the two and answer in the negative.

On a positive note, there's a few interesting tools that have been released.  I'd like to highlight a couple of tools each week, but I don't run across new tools as often as I read articles, so please send me recommendations of tools you use on a regular basis that you think should be shared, and I'll add them.

## [Internet use at record level but Britons are lax about web security | Technology | The Guardian](https://www.theguardian.com/technology/2018/aug/07/internet-use-record-level-britons-lax-about-web-security)

[https://www.theguardian.com/technology/2018/aug/07/internet-use-record-level-britons-lax-about-web-security](https://www.theguardian.com/technology/2018/aug/07/internet-use-record-level-britons-lax-about-web-security)



"While smartphones are the most popular devices used to access the internet, with 78% of respondents doing so, just over a quarter (26%) of smartphone users said they did not have security installed and a further 24% did not know whether they did or not."

It's unclear whether these questions were sensible questions at all.  What exactly is security software for a modern smartphone?  They gave exmaples of firewalls or antispam, but my iPhone comes with a VPN client installed, and of course the basic operating system for iOS and Android is significantly more secure than a modern desktop operating system.


## [Sex, Lies and Cybercrime Surveys [PDF] [2011]](https://www.microsoft.com/en-us/research/wp-content/uploads/2011/06/SexLiesandCybercrimeSurveys.pdf)

[https://www.microsoft.com/en-us/research/wp-content/uploads/2011/06/SexLiesandCybercrimeSurveys.pdf](https://www.microsoft.com/en-us/research/wp-content/uploads/2011/06/SexLiesandCybercrimeSurveys.pdf)



"These three sources of error, that a representative sample of the population doesn’t give a representative picture of the surveyed quality, that outliers can cause catastrophic errors, and for rare phenomenon we are measuring a signal weaker than the noise in which it is embedded pose a serious threat. In this paper we show that the estimates we have of cyber-crime come from surveys that suffer from all three of these sources of error. Cyber-crime losses follow very concentrated distributions where a representative sample of the population does not necessarily give an accurate estimate of the mean. They are self-reported numbers which have no robustness to any embellishment or exaggeration.
They are surveys of rare phenomena where the signal is overwhelmed by the noise of misinformation. In short they produce estimates that cannot be relied upon"

I was pointed at this old paper after I grumbled online about the ONS survey about cybersecurity, and it sets up and entirely demolishes an entire swathe of numbers and poor survey results and makes me suspicious of almost all cybercrime numbers, which I guess was the point.


## [“A Horrifically Bad Idea”: Smartphone Voting Is Coming, Just in Time for the Midterms | Vanity Fair](https://www.vanityfair.com/news/2018/08/smartphone-voting-is-coming-just-in-time-for-midterms-voatz)

[https://www.vanityfair.com/news/2018/08/smartphone-voting-is-coming-just-in-time-for-midterms-voatz](https://www.vanityfair.com/news/2018/08/smartphone-voting-is-coming-just-in-time-for-midterms-voatz)



"Enter Voatz. With a name reminiscent of a plot device in Idiocracy, Voatz is a mobile election-voting-software start-up that wants to let you vote from your phone"

This takedown from VanityFair is one of the better summations of this whole mess.

Remote or online digital voting is an idea that in undeniably attractive to technology enthusiasts.  The idea of being able to vote with your phone just feels intrinsicly like a good idea whose time has come.  But voting in a democracy comes with a set of unique properties that make it a very bad fit for online digitisation.
Firstly, identity and proof of identity is hard, really hard.  It's hard in the real world, but the limitations of the real world act as a natural rate limiting mechanism, and it's very difficult to re-apply that in a digital world.
Secondly, voting requires a problem of transparency as well as anonymity.  That is to say, it should be possible to validate and verify the counts and the ballots submitted without revealing the voting preference of any individual voter. 
Expect this mess to just get worse and worse over the next few months, as Voatz doubles down on it's claims and then explosively falls apart eventually.


## [Britain’s spies get entrepreneurial from The Economist](https://www.economist.com/britain/2018/08/02/britains-spies-get-entrepreneurial)

[https://www.economist.com/britain/2018/08/02/britains-spies-get-entrepreneurial](https://www.economist.com/britain/2018/08/02/britains-spies-get-entrepreneurial)



"Israel also holds lessons, in the way that it fast-tracks former members of its secret signals agency, Unit 8200, into successful cyber-startups. It has worked hard to cultivate a pipeline of tech talent, from school onwards. Britain has copied some of this with its Cyberfirst programme, which sponsors undergraduates to study for careers in cyber-security. But more could be done in schools, especially to get greater numbers of women into the industry"

This is a good analysis of some of the outreach programs that GCHQ is running to try to improve the economy of cybersecurity firms in the UK.  I think the comparison to the Israel 8200 unit is most interesting, as in the last few years, so many incredibly good private cybersecurity companies have come out of that program


## [Fortnite is risking user security in bypassing Google Play Store — Selena Larson](https://www.selenalarson.com/blog/2018/8/3/fortnite-is-risking-user-security-in-bypassing-google-play-store)

[https://www.selenalarson.com/blog/2018/8/3/fortnite-is-risking-user-security-in-bypassing-google-play-store](https://www.selenalarson.com/blog/2018/8/3/fortnite-is-risking-user-security-in-bypassing-google-play-store)



"Fortnite maker Epic Games CEO Tim Sweeney told The Verge the company wants to have a 'direct relationship' with customers by cutting out the middleman, Google, and in this case also cutting out Google's 30% cut on in-app purchases. But the move could also mean users will have a more direct relationship with malware developers, too.

Bypassing the Play Store also means bypassing its built-in security protections while conditioning people to feel comfortable with downloading apps and services directly from the web"

This is a good take from Selena.  While the play store is not perfect at taking down malware, in fact there's quite a lot on there, there is something about training users to install applications onto their devices from websites that they trust.  Because we know how well all of the normal indicators for trust work in phishing right?


## [2018 Serverless Community Survey: huge growth in serverless usage](https://serverless.com/blog/2018-serverless-community-survey-huge-growth-usage/)

[https://serverless.com/blog/2018-serverless-community-survey-huge-growth-usage/](https://serverless.com/blog/2018-serverless-community-survey-huge-growth-usage/)



"For a lot of people, serverless is their first exposure to the public cloud. Meaning: serverless is already shifting the ways developers work and improving accessibility to the cloud."

There's some bias in the data here (if you are visiting serverless.com, you are more likely to be doing serverless already), but I think this insight is the most interesting.
Much like Simon Wardley has been saying for years, there might be a jump with organisations and people moving straight from on-premise or IaaS simple cloud to Serverless without making the move to cloud native infrastructures.

I don't know anyone who is working on security models for serverless, who can show us good practice or patterns that we know work, but I'll keep looking and see what starts to emerge.


## [4 things you need to know to improve your security strategy | | Business Technology](https://www.technative.io/4-things-you-need-to-know-to-improve-your-security-strategy/)

[https://www.technative.io/4-things-you-need-to-know-to-improve-your-security-strategy/](https://www.technative.io/4-things-you-need-to-know-to-improve-your-security-strategy/)



"UK security teams have lost an average of 11 days in the coordination of patching activities across their teams, with the majority agreeing they spend more time navigating manual processes than responding to vulnerabilities. It’s not surprising, given that most organisations are using manual processes to deal with these vulnerabilities."

Another reminder that DevOps processes, while at first anathama to many security colleagues, actually make many of the problems that security face much easier to deal with.
Want to know what changed and when?  Look in the infrastructure code repository.  Want to patch servers, much easier when it's automated.


## [Deploying TLS 1.3 at scale with Fizz, a performant open source TLS library – Facebook Code](https://code.fb.com/networking-traffic/deploying-tls-1-3-at-scale-with-fizz-a-performant-open-source-tls-library/)

[https://code.fb.com/networking-traffic/deploying-tls-1-3-at-scale-with-fizz-a-performant-open-source-tls-library/](https://code.fb.com/networking-traffic/deploying-tls-1-3-at-scale-with-fizz-a-performant-open-source-tls-library/)



"To manage the complexity of the state machine of TLS in Fizz, the state machine is explicit. This means transitions are defined in one place based on the messages that are received. Having all states defined explicitly in a single location makes it easier to address security issues."

The golden rule is never to develop your own crypto, but this has lead to lots of people reusing the same large generic libraries that need to do everything, which leads to openssl and lots of vulnerabilities.  This, along with Amazon and probably a few others building new TLS implementations is interesting, and at the very least should give some budding cryptographic vulnerability researchers some new toys to play with


## [webhint, the hinting engine for web best practices](https://webhint.io/)

[https://webhint.io/](https://webhint.io/)



" webhint is a linting tool that will help you with your site's accessibility, speed, security and more, by checking your code for best practices and common errors. "

This is a neat tool that can check your website for various common errors.  It doesn't really seem to set urgency levels for the errors, so it's more like a linting tool, and I'd want to customise what things I consider an error before I put it into a build tool to prevent false positives, but I'm glad that we're seeing more of this kind of tool


