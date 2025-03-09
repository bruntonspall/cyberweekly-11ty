---
title: "129 - Even cyber companies get breached"
date: 2020-12-13
description: "Remember that term \"assumed breached\", well if FireEye can get breached, then you should assume that pretty much anyone can."
permalink: /even-cyber-companies-get-breached/
---

Remember that term "assumed breached", well if FireEye can get breached, then you should assume that pretty much anyone can.

Of course there are companies that you simply have to trust in some ways, your core identity provider is one, generally most organisations trust AWS and Microsoft to not be fundamentally breached, but beyond that you need to start working out who you trust, and how much you trust them.

Some of this is the heart of threat modelling, a subject that I keep meaning to write a blog about, but life just keeps getting in the way.  Threat modelling is generally very poorly practiced, and many organisations really struggle to apply threat models within projects, let alone at higher abstractions such as across their supply chain, within their organisation or across their industry generally.

This brings me to the real "big deal" about the FireEye hack.  I've talked a bit below about why the loss of the red team tools isn't that big a deal, and how the loss of customer data would be a much bigger deal.  But the real impact here is the loss of credibility for cyber security generally.  Senior executives around the world, faced with increasing financial pressures, are going to look at this, and look at the requests for security spend and think "If FireEye, a cyber security company, couldn't keep from being hacked, then why should I bother spending extra here?"

The loss of credibility makes it even harder to justify even small amounts of security spend on small things, like central IDAM solutions that work and support 2FA, like using VLANS and VLAN ACLs to segment your network, like employing Endpoint Detection and Response software to your endpoints.

We know that these are tools and techniques that significantly raise the bar for attackers, and make it far more likely that the general unwashed masses of blackhat hackers, teenagers and hacking collectives will move on to another target when their scripts don't work as expected.  That doesn't mean that an advanced attacker can't get around them, but it does mean that more effort is required, which massively changes your threat model.

We need to reinforce that yes, attackers can and will compromise and breach any system, even cyber companies.  Our job is to make sure that they pay for that, in effort expended, in monetary cost, and in disclosed equities such as novel tools or techniques that were needed to get to you.  We need to continue to argue with businesses that we shouldn't just shrug and give in.


Admin note:  This is the last newsletter of 2020.  I'm going to take a Christmas Break from CyberWeekly for two weeks, aiming to restart on the 3rd of January.  I may manage to pull together a best of newsletter for the week between Christmas and New Year, but it will depend on work and family schedules over Christmas.  I hope you all enjoy your holidays and come back refreshed and ready to face 2021.

## [Introducing Amazon Curate (I Wish) | Daniel Miessler](https://danielmiessler.com/blog/introducing-amazon-curate-i-wish/)

[https://danielmiessler.com/blog/introducing-amazon-curate-i-wish/](https://danielmiessler.com/blog/introducing-amazon-curate-i-wish/)

> There’s an argument that most of the good creators are already being seen because Google, Social Media, and word of mouth are finding the best stuff out there. But I don’t buy that argument.
> 
> I have seen far too many examples of phenomenal content that sits on the internet, gets crawled by Google, and yet has no following.
> 
> These authors either don’t know how, or care to, do self-promotion across various channels, so they either continue to write for nobody or they give up because they feel unseen.


Via, the excellent tldrsec newsletter I saw this suggestion for a curation tool.

About 10 years ago I worked on a hackday project at the Guardian that was focused on curation and recommendation, which was driven by watching a group of students with the physical paper on a new years day, handing sections to each other and recommending articles.

Sadly, none of that vision has come true, and this remains a product that I'd be interested in.  Although I think the rise of newsletters (like this one) mean that people are interested in curation by people rather than by AI.


## [r2c blog — Exploiting dynamic rendering engines to take control of web apps](https://r2c.dev/blog/2020/exploiting-dynamic-rendering-engines-to-take-control-of-web-apps/)

[https://r2c.dev/blog/2020/exploiting-dynamic-rendering-engines-to-take-control-of-web-apps/](https://r2c.dev/blog/2020/exploiting-dynamic-rendering-engines-to-take-control-of-web-apps/)

> Modern JavaScript frameworks are heavily utilized for web site development nowadays. Instead of plain HTML pages, we now have PWAs (progressive web applications) and SPAs (single page applications) that do most of the work in the client's browser and use JavaScript to generate the contents of the page on the fly.
> 
> This technology has many advantages and can be effective at creating a sleek UI and UX, but at the same time, it is not SEO friendly, because crawlers and bots are not developed to render or understand JavaScript. One of the common ways to help bots get valid HTML content is to open a requested page in a headless browser instance on the server, such as Puppeteer or Playwright, get the resulting HTML, strip parts that are not intended to be crawled and return it. This approach is called dynamic rendering and is promoted by Google as one of the possible ways to serve content.
> 
> 
> I came across this type of application while doing a security review of packages in the Node.js ecosystem on possible vulnerabilities that may appear when utilizing headless browsers in production.


Sigh, if you wanted yet another reason why replacing the rendering engine with client side javascript is a bad idea, this is a well articulated attack model on backend renderers.

As Vasilii says, for SEO reasons, you might have systems that render that webpage for you on the backend.  If those renderers run inside your network, they have the ability to access internal websites, systems and other interesting URLs.  It's very similar to an SSRF attack, but done through prerender engines instead.


## [Affable Kraut on Twitter: "Thanks to data from @sansecio I stumbled upon a digital skimming / #magecart technique for injecting convincing PayPal iframes into the checkout process. It does this using postMessage, and I think this is the first skimmer to deploy such a method. 1/20" / Twitter](https://twitter.com/AffableKraut/status/1333258498910588928)

[https://twitter.com/AffableKraut/status/1333258498910588928](https://twitter.com/AffableKraut/status/1333258498910588928)

> Thanks to data from 
> @sansecio
>  I stumbled upon a digital skimming / #magecart technique for injecting convincing PayPal iframes into the checkout process. It does this using postMessage, and I think this is the first skimmer to deploy such a method.


This is quite the twitter thread, one that I wish was a blogpost.  

But here we go, some indicators to put into your SIEM, and a good breakdown of a new technique being used by MageCart.


## [Exclusive: The U.S. Emergency Alert system has been hacked](https://www.inputmag.com/tech/this-hacker-showed-us-how-to-exploit-the-usa-candas-emergency-alert-system)

[https://www.inputmag.com/tech/this-hacker-showed-us-how-to-exploit-the-usa-candas-emergency-alert-system](https://www.inputmag.com/tech/this-hacker-showed-us-how-to-exploit-the-usa-candas-emergency-alert-system)

> He posted evidence on Twitter in late November showing a screen enabling him to generate EAS (Emergency Alert System) messages, including Child Abduction Emergencies, Civil Emergency Messages, or Evacuation Immediate [sic] alerts.
> 
> The hacktivist believes the system access points are available on the open internet for use by proper authorized personnel, but are easily accessible by people able to socially engineer the manufacturers of the systems.
> 
> “You can get whatever you need to gain full access – not to all, as most are updated – but a scary majority,” he says. “This reminds me of the banking systems, they run COBOL because they are too lazy and cheap to upgrade to something more secure and we get left with very old people who know how to program COBOL working on the banking and insurance infrastructure. I think the federal government needs to set up proper training for set up and usage of these devices, and make it illegal to operate if you have not been trained.”


One of the problem with "hackers", whether white hat or black hat, is that despite their prodigious technical skills with offensive tools, they often don't actually understand the systems architecture and development that underlies the systems they are looking at.  This faulty understanding means that they might not know what they could do with a tool when they find it, and also means that they sometimes cause disruption in the system that they are exploring.

There's several misconceptions in this article, simply scanning the internet for people running software that does emergency alerts doesn't mean that every one that you've found is actually a live emergency alert system for a state.  These systems can do a lot of things.  He says he searched for domain names that look like they might be connected to alert systems, and looked at those.  But of course many organisations will run versions of these systems for training, for staging and testing.  It's not entirely clear without more information, that the systems that he's got access to are production systems.  

However, the slightly more cynical me suspects that there probably are a bunch of poorly secured, poorly managed emergency alert systems connected to the internet, so it's not beyond possibility that he's stumbled on a real thing.


## [Co-op is using facial recognition tech to scan and track shoppers | WIRED UK](https://www.wired.co.uk/article/coop-facial-recognition)

[https://www.wired.co.uk/article/coop-facial-recognition](https://www.wired.co.uk/article/coop-facial-recognition)

> Southern Co-op is using facial recognition technology from Facewatch, a London-based startup. Every time someone enters one of the 18 shops using the tech cameras scan their faces. These CCTV images are converted to numerical data and compared against a watchlist of ‘suspects’ to see if there’s a match. If a match is made, staff within the store receive notifications on smartphones.
> 
> “The system alerts our store teams immediately when someone enters their store who has a past record of theft or anti-social behaviour,” Gareth Lewis, Southern Co-op’s loss prevention lead wrote in a blog post on the Facewatch website. The post is the only public acknowledgement of the use of the technology and Lewis says it has been “successful,” with the tech being deployed in branches where there are higher levels of crime.
> 
> In response to police use of facial recognition technology, the Court of Appeal criticised a lack of transparency around the creation of watchlists and who could be on them. Co-op staff decide who is added to its watchlists based on behaviour. A spokesperson for the firm says its “limited and targeted” use of facial recognition is to “identify when a known repeat offender enters one of our stores”.
> 
> “Only images of individuals known to have offended within our premises, including those who have been banned/excluded, are used on our facial recognition platform,” the spokesperson says. “Using facial recognition in this limited way has improved the safety of our store colleagues.”


This is going to be huge in 2021.  Facial recognition, gait recognition and other mechanisms to improve loss prevention will be popular with stores that are seeking to reduce the number of people in the store, and replace cashiers with self-service tools.

The question around regulation is a good one.  This particular case seems pretty ethical and within boundaries.  The watchlist is created purely from people convicted of shoplifting and given a banning order.  The system alerts the staff, letting them know that someone is suspected of matching, which allows staff to make human decisions based on the algorithm, and Co-op was highlighted as explicitly using a good quality watchlist.

The concern starts to come if those lists are shared, if there's a right to rectification for people who find themselves on the list accidentally, and of course, when stores or organisations start to roll out the tech wider.  Is it a fair and proportionate punishment for stealing to find yourself excluded from say all stores in the area?


## [Threat Modeling Manifesto](https://www.threatmodelingmanifesto.org/)

[https://www.threatmodelingmanifesto.org/](https://www.threatmodelingmanifesto.org/)

> Threat modeling is analyzing representations of a system to highlight concerns about security and privacy characteristics.
> 
> At the highest levels, when we threat model, we ask four key questions:
> 
> * What are we working on?
> * What can go wrong?
> * What are we going to do about it?
> * Did we do a good enough job?


This is a good document and a good bit of work trying to set out a stall for threat modelling, ensuring that it's understood and consistent.


## [Evilginx-ing into the cloud: How we detected a red team attack in AWS - Expel](https://expel.io/blog/evilginx-into-cloud-detected-red-team-attack-in-aws/)

[https://expel.io/blog/evilginx-into-cloud-detected-red-team-attack-in-aws/](https://expel.io/blog/evilginx-into-cloud-detected-red-team-attack-in-aws/)

> The first hint that something was wrong came in the form of one of our analysts discovering a login from an anonymous source to a customer’s AWS console. We immediately sprung into action, digging in to see if that user logged in from known proxies or end points previously.
> 
> 
> 
> But wait a second. Isn’t this customer’s AWS access provisioned through Okta? Why didn’t we get any Okta alerts?
> 
> Shortly thereafter, an AmazonGuardDuty alert fired – those same access keys were being used from a python software development kit (SDK) rather than the AWS console and someone was enumerating those access key permissions.
> 
> The TL;DR on all of that? Not good.
> 
> We immediately escalated this as an incident to the customer to understand whether this series of events was expected.


Several interesting tidbits in here.  Would you detect these kinds of activity?  You should be able to, but should and can are very different.  This is the value of a good red-team exercise.

The second is that they decided to let the attack play out.  In this case, they were a service team, they could have revoked that token and seen what happened, how the red team would try again, but instead they let it play out and watched the attackers.

This is a much harder judgement call.  For some redteam activities, I'd want the redteam to know they were caught, and to frustrate them, because the SOC noticed, so the SOC should run their normal processes. But in others, it's more valuable for the SOC to learn what happens next, in order to build better layers of defence.


## [pre:Invent 2020 - Chris Farris](https://www.chrisfarris.com/post/preinvent2020/)

[https://www.chrisfarris.com/post/preinvent2020/](https://www.chrisfarris.com/post/preinvent2020/)

> As I was slammed with work things, I wasn’t following pre:Invent (and will probably miss much of the lame online re:Invent), so I’m going back and reviewing all the announcements for things of note to a serverless nerd or security geek.
> 
> Here are the 29 I thought interesting. Rather that review these by date (which is what you get from the AWS Feed), I thought I’d categorize them into useful buckets.


There's a lot of reading here.  Best pass this onto your lead cloud architect and make them read all of these and get them to summarise them for you. [No, I didn't have time to read them all this week, I've been slammed, but they're all added to my reading list, so give me a month or two and I'll have read at least 50% of them!]


## [San Jose Man Sentenced To Two Years Imprisonment For Damaging Cisco’s Network | USAO-NDCA | Department of Justice](https://www.justice.gov/usao-ndca/pr/san-jose-man-sentenced-two-years-imprisonment-damaging-cisco-s-network)

[https://www.justice.gov/usao-ndca/pr/san-jose-man-sentenced-two-years-imprisonment-damaging-cisco-s-network](https://www.justice.gov/usao-ndca/pr/san-jose-man-sentenced-two-years-imprisonment-damaging-cisco-s-network)

> Ramesh, 31, of San Jose, pleaded guilty on August 26, 2020, to one count of intentionally accessing a protected computer without authorization and recklessly causing damage to Cisco.  Ramesh worked for Cisco but resigned in approximately April 2018.  According to the plea agreement, Ramesh admitted to intentionally accessing the Cisco Systems cloud infrastructure that was hosted by Amazon Web Services without Cisco’s permission on September 24, 2018.  Ramesh further admitted that during his unauthorized access he deployed a code from his Google Cloud Project account that resulted in the deletion of 456 virtual machines for Cisco’s WebEx Teams application, which provides video meetings, video messaging, file sharing, and other collaboration tools.  He admitted that he acted recklessly in deploying the code and consciously disregarded the substantial risk that his conduct would harm Cisco.  As a result of Ramesh’s conduct, over 16,000 WebEx Teams accounts were shut down for up to two weeks and caused Cisco to spend approximately $1,400,000 in employee time to restore the damage to the application and refund over $1,000,000 to affected customers.  No customer data was compromised as a result of the defendant’s conduct.


Ramesh was still able to use his credentials to log into the production systems at Cisco nearly 6 months after he left the company.

Reminder that where possible, you should be using SSO to ensure that your staff have just one account that needs securing with 2FA.  You can [configure AWS to use your corporate identity systems](https://aws.amazon.com/identity/federation/), which means that when HR removes someone from the corporate system, their access to all your production and development infrastructure is removed as well.


## [Russia's FireEye Hack Is a Statement—but Not a Catastrophe | WIRED](https://www.wired.com/story/russia-fireeye-hack-statement-not-catastrophe/)

[https://www.wired.com/story/russia-fireeye-hack-statement-not-catastrophe/](https://www.wired.com/story/russia-fireeye-hack-statement-not-catastrophe/)

> The Washington Post reported on Tuesday that hackers from a group known as APT 29 or Cozy Bear, attributed to Russia’s SVR foreign intelligence service, carried out the breach.
> 
> FireEye has both global prominence and a history of engaging with Russian actors. The company was the first, for instance, to tie the hacker group known as Sandworm—responsible for blackouts in Ukraine in 2015 and 2016 as well as the hyperdestructive worm NotPetya the following year—to Unit 74455 of Russia’s GRU military intelligence agency. FireEye also provided the first public evidence that the same GRU unit was responsible for the attempted sabotage of the 2018 Winter Olympics. All of those attacks were later named in a US indictment of six Sandworm hackers unsealed in October.
> 
> The apparently retaliatory hack sends a clear statement that while Russia may have been relatively quiet during the US presidential election, the Kremlin’s digital prowess remains formidable. At the same time, the fallout from the hack doesn’t compare to the release of tools like the NSA’s Eternal Blue tool, which a mysterious group called the Shadow Brokers leaked in 2017, or the breach of exploit broker Hacking Team in 2015.
> 
> “The most important data that a company like FireEye has is data about its customers. The second most important data they have are the sources and methods they use to protect their customers,” like threat intelligence data, says Richard Bejtlich, former chief security officer of Mandiant, the incident response division of FireEye, and principal security strategist at the network analysis firm Corelight. “Farther down the line are the red team tools, where they’re emulating adversaries.”


FireEye seems to be saying that no customer data was accessed or stolen, although the language around that has been a little vague.  

If it is a nation backed acvanced threat actor, and it seems likely that it is, then the customer data on vulnerabilities in customer systems would be incredibly valuable.  Not only to plan specific targeted attacks on those customers, but also to be able to get  analysable bulk data that enables them to work out where systemic weaknesses are in most systems. (although for free, I'll suggest that poor patching, lack of application control for admins, poor passwords and lack of use of 2FA will be the systemic trends).


## [FireEye Shares Details of Recent Cyber Attack, Actions to Protect Community | FireEye Inc](https://www.real-sec.com/2020/12/fireeye-shares-details-of-recent-cyber-attack-actions-to-protect-community)

[https://www.real-sec.com/2020/12/fireeye-shares-details-of-recent-cyber-attack-actions-to-protect-community](https://www.real-sec.com/2020/12/fireeye-shares-details-of-recent-cyber-attack-actions-to-protect-community)

> This attack is different from the tens of thousands of incidents we have responded to throughout the years. The attackers tailored their world-class capabilities specifically to target and attack FireEye. They are highly trained in operational security and executed with discipline and focus. They operated clandestinely, using methods that counter security tools and forensic examination. They used a novel combination of techniques not witnessed by us or our partners in the past.
> 
> We are actively investigating in coordination with the Federal Bureau of Investigation and other key partners, including Microsoft. Their initial analysis supports our conclusion that this was the work of a highly sophisticated state-sponsored attacker utilizing novel techniques.    
> 
> During our investigation to date, we have found that the attacker targeted and accessed certain Red Team assessment tools that we use to test our customers’ security. These tools mimic the behavior of many cyber threat actors and enable FireEye to provide essential diagnostic security services to our customers. None of the tools contain zero-day exploits. Consistent with our goal to protect the community, we are proactively releasing methods and means to detect the use of our stolen Red Team tools.   
> 
> We are not sure if the attacker intends to use our Red Team tools or to publicly disclose them. Nevertheless, out of an abundance of caution, we have developed more than 300 countermeasures for our customers, and the community at large, to use in order to minimize the potential impact of the theft of these tools.  


This is both a massive deal, and not a big deal at the same time.  I talked about why it's a big deal further up, but here's why it's not as big as some people are claiming.

FireEye's red team tools, while unique, do not contain any zero-days, and are therefore likely not significantly different or better than say Metasploit or CobaltStrike which are already free and open source.  In addition, whatever advanced actor carried this out clearly has capabilities well beyond the use of these tools, so it's not like this is advancing their capabilities significantly.

Additionally, the release of [the detection rules](https://github.com/fireeye/red_team_tool_countermeasures) means that blueteams should be able to add those rules to their detection suites easily and quickly, and be reasonably secure against the use of the tools.   That repository has not just basic signatures for the tools, but also more complex rules for hunting the workflows and sequence of actions that the tools imply.


