---
title: "41 - The evolving practice of security"
date: 2019-03-02
description: "I'm [speaking at QCon](https://qconlondon.com/london2019/presentation/evolving-practice-security) this coming week on the evolving practice of security and therefore it's a lot in my mind."
permalink: /the-evolving-practice-of-security/
---

I'm [speaking at QCon](https://qconlondon.com/london2019/presentation/evolving-practice-security) this coming week on the evolving practice of security and therefore it's a lot in my mind.

As the Department of Defense moves from on premise data centers, to cloud based infrastructure, it's easy to think that security practices can stay mostly the same, but that they just need to change slightly to adjust for a new different style of data center.  Operations used to think that as a community.  Classical operations teams simply considered the cloud data center to be just another data center, but with some weird extra bits around the outside, you could no longer pull cables out, and so on.

But in reality, when a product evolves from being a simple componentized product to being something you buy like a utility, the practice of managing that product has to significantly evolve as well.  Cloud infrastructure isn't just computers in someone else's data center, to name a witty but wrong sticker, it's so much more than that, because it's a paradigmatic leap into a new way of thinking about computers, from pets to cattle, from simple servers to complicated systems.

Security thinking really hasn't evolved along the same lines yet, or not well.  Instead many security departments, often the department of fires, is so busy reacting to things that they haven't been involved, but they haven't been able to look to the future and understand what has gone on.  And so they make the same requests of delivery teams and operational teams that they always have.  "Is the data encrypted at rest?".  But in a cloud infrastructure, the question is actually really hard to ask.  In our physical data center, we have some concept of "at rest", a spinning disk that we can point at and say "our database is on that".  But cloud infrastructure has the bits packaged up and sent all over the data center.  When is it at rest? Who can access those disks and what would it mean to? Where are the encryption keys stored?

In order to take advantage of the cloud, to build future proof cloud solutions that take advantage of the nature of the cloud, we need to find a new set of practices, a set of security practices that have evolved along with cloud infrastructure, that are aligned with how it works, and that understand where the fault lines actually are.  Because if we don't do that, then we are just fighting the war of yesterday against the enemy of tomorrow.

## [Research heresies — Myddelton](http://www.myddelton.co.uk/blog/research-heresies)

[http://www.myddelton.co.uk/blog/research-heresies](http://www.myddelton.co.uk/blog/research-heresies)

> This is the way we should be thinking about user research in a mature organization. Releasing things without research is highly desirable a lot of the time.
> 
> It's desirable because when our teams are releasing things without research it frees our time to focus on what’s most important. Then we can use enough rigour and effort to come back with results that matter.
> 
> It means we need to be mature as individuals and not moan about the stuff that our teams are doing without research. This is not something that most researchers are very good at.


This maturity model from "We don't need no stinking X", to "We see some value in X, lets do it at the end", to "OMG, we should always do X before we start anything" and onto "X can have value, but is expensive, lets do it when we need it" is a maturity model of many processes, not just user research.

I have a love/hate relationship with risk assessment and information assurance, because I believe strongly that risk assessments have a lot of value.  However, I look around at information assurance as practiced around me, and it tends to be extremely low value, and either holds up delivery, or is completely ignored.

If I am building a new application on AWS, I shouldn't need to go through a complex process to determine that I should turn on CloudWatch logs to see the activities of AWS users.  If we require formal risk assessments before carrying out basic hygiene activites, then we become a blocker to anybody delivering anything.  But equally, if we're building a payment processing solution that will pay £1b a week out to people, we should probably consider doing some form of risk assessment to understand what the risks are, and make sure that we are doing the right things.

But worse than that, many risk assessments are there looking for risks, regardless of their context or appropriateness.  If I'm building a simple tool to gather some user contact details to put into a CRM so they can be emailed back, then do I need the information assurance team telling me that they haven't done a site visit on Trello's data center to assure themselves of how that information is stored.

I think we're in a weird place with information assurance maturity, especially in agile organisations, and we need to work out some consistency in how we talk about it, what processes we think are appropriate, and what baselines we think work for different contexts


## [Revolut insiders reveal the human cost of a fintech unicorn's wild rise | WIRED UK](https://www.wired.co.uk/article/revolut-trade-unions-labour-fintech-politics-storonsky)

[https://www.wired.co.uk/article/revolut-trade-unions-labour-fintech-politics-storonsky](https://www.wired.co.uk/article/revolut-trade-unions-labour-fintech-politics-storonsky)

> She did a 30-minute job interview over Google Hangouts with the London-based head of business development, Andrius Biceika, and was immediately told she had passed to the next round, which would involve a small test. “The surprise came when I received the task and it asked me to get the company as many clients as possible, with each one depositing €10 into the app,” says Laura.
> 
> The instructions on the exercise said the applicants should recruit at least 200 clients in a week to have a chance at passing to the next interview phase. The task’s description didn’t guarantee that reaching the target would automatically qualify applicants for a job, but did advise them on a number of ways they could get clients, such as sharing a “promo code” with their friends, sharing it on social media, and posting promotional flyers on university campuses.
> 
> After Laura wrote back refusing to do the task and saying she was disappointed that the company would “take advantage of someone that is looking for a job”, Biceika emailed her saying she was the only candidate out of over 350 that had complained about the task. “Apologies you're not up to show what you're capable of,” he wrote in the email.
> 
> [...]
> 
> In an emailed statement, a company spokesperson wrote: “our culture is evolving as rapidly as our business”. They emphasised that in the last year the company had grown from 150 to 750 people, with staff turnover of less than 2.6 percent, and that 40 percent of its staff was female.
> 
> An analysis of the start and end dates of 147 former Revolut employees on LinkedIn suggests that over 80 percent had lasted less than a year, and over half stayed at the company for less than six months.


This article paints a picture of a deeply worrying culture in a company that not only doesn't value it's staff, but actively hijacks a recruiting process designed to bring in new staff, to potentially drive off good staff in exchange for increasing growth.

Furthermore, it paints a picture of a comms team who are willing to send false statistics to the press that only a little bit of digging can reveal are patently false.

For a company that needs to build the trust of its users as it's primary marketable ability, in a crowded market of new FinTech startups, this is not a good look.


## [Department of Defense - DoD Cloud Strategy ](https://media.defense.gov/2019/Feb/04/2002085866/-1/-1/1/DOD-CLOUD-STRATEGY.PDF)

[https://media.defense.gov/2019/Feb/04/2002085866/-1/-1/1/DOD-CLOUD-STRATEGY.PDF](https://media.defense.gov/2019/Feb/04/2002085866/-1/-1/1/DOD-CLOUD-STRATEGY.PDF)

> DoD cloud architectures will allow for workloads to shift from one AZ or region to another, within a single cloud provider, nearly instantaneously upon detection of the failure of a primary data center. This will be vital in the case of human-made or natural destruction of a large geographic area. The configuration of automated failover is not itself automatic. To fully achieve this capability, applications will need to be re-architected for the cloud. This will allow the Department to bypass the cost and manual effort currently required for the Department to maintain multiple instances of the same data across cloud providers or on-premises data centers, which does not provide the same level of failover as that provided by commercial cloud. 


The US Department of Defense, and in particular the work coming out of the CIO's office in DoD is increasingly sensible and well considered.  This is a good strategy document, it's readable, clear, considered and addresses all of the major concerns one should have with a program of this size.  

In particular a few things stand out.  The DoD says that lift and shift is not sufficient, and that deep transformation is going to be necessary to take advantage of the cloud environments.  It says that some lift and shift will be necessary, but that it should be considered legacy migration, rather than a cloud transformation when that happens.  It talks about adoption of api driven cloud infrastructure, devsecops to continually scan the infrastructure and the skills gap within the department that needs to be adjusted.  Finally it clearly lays out that the JEDI contract is for general purpose cloud infrastructure and that a "Fit for purpose" program will look at individual projects that have more specific needs, either because they should be on SaaS instead of the JEDI PaaS and IaaS system, or because it has unique requirements that need a specialised cloud environment


## [What to Make of Cyber Command’s Operation Against the Internet Research Agency - Lawfare](https://www.lawfareblog.com/what-make-cyber-commands-operation-against-internet-research-agency)

[https://www.lawfareblog.com/what-make-cyber-commands-operation-against-internet-research-agency](https://www.lawfareblog.com/what-make-cyber-commands-operation-against-internet-research-agency)

> Three possibilities exist. The first is that Russia chose only to use the IRA for its planned 2018 efforts, and that Cyber Command’s activity thwarted its plans. The second is that Russia planned to employ multiple facets of its intelligence apparatus in a campaign, as they did in 2016, and that Cyber Command thwarted all of them, including in some operations still unknown to the American public. The third is that the Russians chose to stand down (with the exception of some minor activities), perhaps because U.S. political parties were doing a fine job being divisive on their own and perhaps also to bide their time for the much bigger prize of the 2020 presidential election. In this last view, Cyber Command’s activities may have reduced the Russian freedom of action or interfered with normal IRA operations but did not meaningfully change the outcome of the 2018 election and Russian interference in it.
> 
> Senator Mike Rounds, for his part,strongly suggested that Cyber Command’s actions made a difference, arguing that without them there “would have been some very serious cyber-incursions.” Yet his statement does not quite square with the operational realities of the cyber domain. Any actual intrusions (as opposed to online trolling and propaganda) are almost certain to have occurred months before Election Day; it seems much more likely that the thwarted Russian activity, if there was any, would have taken the form of an influence campaign rather than “incursions.” But drawing any conclusions about which of the three possibilities I describe based on public information  is impossible. The operational details are classified, and with good reason.


The reporting on this has been peculiar, and Lawfare have covered the point that made me nervous quite well.  The leaked interviews and "news tips" that tell of a great and successful operation on the day of the election is the same as trumpting an amazing victory bombing a munitions factory behind enemy lines on the day of invasion.  It's a strategic strike and valuable, but the timing makes no sense, other than as a propaganda piece or act of demoralisation.

I suspect that this has been far more about the US cyber command declaring that they can do this, and proving to their superiors that the money invested has been worth while rather than of any tactical value in affecting disinformation operations focused on the election day itself.


## [The Digital Maginot Line](https://www.ribbonfarm.com/2018/11/28/the-digital-maginot-line/)

[https://www.ribbonfarm.com/2018/11/28/the-digital-maginot-line/](https://www.ribbonfarm.com/2018/11/28/the-digital-maginot-line/)

> As governments become increasingly aware of the problem, they each pursue responses tailored to the tactics of the last specific battle that manifested in their own digital territory; in the United States, for example, we remain focused on Election 2016 and its Russian bots. As a result, we are investing in a set of inappropriate and ineffective responses: a digital Maginot Line constructed on one part of the battlefield as a deterrent against one set of tactics, while new tactics manifest elsewhere in real time.
> 
> [...]
> 
> The Information World War has already been going on for several years. We called the opening skirmishes “media manipulation” and “hoaxes”, assuming that we were dealing with ideological pranksters doing it for the lulz (and that lulz were harmless).
> 
> In reality, the combatants are professional, state-employed cyberwarriors and seasoned amateur guerrillas pursuing very well-defined objectives with military precision and specialized tools. 


I don't really buy the line that all information manipulation is warfare with professional, state-employed "cyberwarriors".  I think that a lot of the dis-information or fake news that is out there is the results of a lot of complex social factors, from growing trans-national communications, generational gaps between young people and the establishment combined with perverse network effects in news seeking "most clicks", social network and silicon valley's "reach before revenue" business models.

However, the thought here is that we are fighting the war of yesterday, building a modern day Maginot line to prevent the issues of yesteryear from happening again.  This is true of security, with lots of security professionals learning from the previous decade of security failures and making it harder and harder for classic "hackers movie" style attacks from occurring, but ignoring the fact that the next wave of breaches will come in a different manner.

Does it matter?  If France had not built the Maginot line, then Germany may have invaded that way, and equally if we don't manage our network perimeters correctly, then attackers will breach us that way.  But we need to recognise whether this is something we should strategically invest in, or whether we are doing this to simply keep up, and the defences need to just be "good enough"


## [How should I organize my AWS accounts? | #NoDrama DevOps](https://nodramadevops.com/2019/01/how-should-i-organize-my-aws-accounts/)

[https://nodramadevops.com/2019/01/how-should-i-organize-my-aws-accounts/](https://nodramadevops.com/2019/01/how-should-i-organize-my-aws-accounts/)

> Previously, I answered ‘How many AWS accounts do I need?’ with:
> 
> Create however many accounts your organization needs to establish safe security and fault boundaries that enable your organization’s primary use cases and expected level of team/application autonomy.
> 
> Today, we’ll explore the tradeoffs of AWS account organization methods using an example that covers one approach to partitioning enterprise-wide and business unit-specific application delivery use cases. AWS Accounts are the strongest security and fault partition mechanism, so we need to use them judiciously to achieve our delivery goals rather than hinder them.


This is an interesting pair of articles about AWS account organisation.  When teams move to the cloud, the security teams often bring their old thinking with them, and spend a lot of time and energy worrying about the networks, the firewalls and the Virtual Private Clouds that provide compute and data isolation.  But the first thing they should be thinking about is account management and identity management.

I'm not 100% convinced that this model is right, and the author does say to consider how to apply it to your organisation, but it's a good place to start for thinking about what levels of isolation and autonomy you want in your AWS accounts


## [How 20th Century Fox uses ML to predict a movie audience | Google Cloud Blog](https://cloud.google.com/blog/products/ai-machine-learning/how-20th-century-fox-uses-ml-to-predict-a-movie-audience)

[https://cloud.google.com/blog/products/ai-machine-learning/how-20th-century-fox-uses-ml-to-predict-a-movie-audience](https://cloud.google.com/blog/products/ai-machine-learning/how-20th-century-fox-uses-ml-to-predict-a-movie-audience)

> Let’s revisit our Logan example to see if the data corroborates our intuition that moviegoers who have previously seen an action movie with a “rugged” male lead will likely see Logan as well. After a movie’s release, we are able to process the data on which movies were previously seen by that audience. The table below shows the top 20 actual moviegoer audiences (Comp ACT) compared to the top 20 predicted audiences (Comp PRED). Let’s focus on the top 5 actual movies (shown in green below) and see if they also showed up in our prediction column: of the top 5, all of them are represented by the predictions.
> 
> On the surface, our intuition was correct. The top audiences for Logan were actually a combination of superhero (which we already knew) and “rugged male action lead” (which we didn’t know with certainty). This can be better seen by noting that key “rugged male action lead” predictions like The Magnificent Seven (in blue above), John Wick (in green above) and Terminator Genisys (in blue above) were also present in the top 20 list of actual audiences. This result is a win-win because the new audience “adds” to the core superhero audience, and can potentially be used to extend the reach of the movie beyond that core audience.


This is a really interesting use of Machine Learning, predicting what films will be popular, but there's some interesting fails in here as well.  In the test dataset, the really interesting one to me is that the machine predicted that Deadpool would fail and unpopular with people who like rugged male action leads.  The question is whether this is a failure of the model, whether this tells you something about the trailer that was made for these films, or whether this tells you more about shifting and changing audience perceptions.


## [Thunder, thunder, thunder... Thunderclap: Feel the magic, hear the roar, macOS, Windows pwnage tools are loose • The Register](https://www.theregister.co.uk/2019/02/26/thunderclap_hacking_devices/)

[https://www.theregister.co.uk/2019/02/26/thunderclap_hacking_devices/](https://www.theregister.co.uk/2019/02/26/thunderclap_hacking_devices/)

> Malicious peripherals may not be as alarming as remote code execution vulnerabilities because local access to a target device is necessary and physical security precautions can be effective. But DMA attack scenarios shouldn't be brushed aside too lightly.
> 
> "In the most accessible version of our story, you obtain a VGA/Ethernet dongle, power adapter, or USB-C storage device from a malicious person/organization and your device is immediately compromised," explained Robert N. M. Watson, senior lecturer in systems, security, and architecture at the University of Cambridge Computer Laboratory, in an email to The Register.
> 
> "But it's worth thinking a bit further: we can consider a range of supply-chain and remote device attacks, such as attacks against Thunderbolt or PCI-e devices themselves that allow them to then be used against an end user."


Computers are increasingly complicated, and the universal connectors makes them even more complicated.  It's impossible for my laptop to have a one way communication system that only outputs out rather than allowing devices into the system.  Even Apple HDMI adapters have had almost complete computers in that speak airplay rather than just piping HDMI out of the device.

This means that security hasn't moved on from the 80s to a certain degree, that physical access to your computer while its on and unlocked probably still means it's game over.  The big difference now, especially with RSA this week, is all of those hardware dongles that you get given for free by vendors.  How good is our supply chain, or our instinct on what to trust here?


## [Once hailed as unhackable, blockchains are now getting hacked - MIT Technology Review](https://www.technologyreview.com/s/612974/once-hailed-as-unhackable-blockchains-are-now-getting-hacked/)

[https://www.technologyreview.com/s/612974/once-hailed-as-unhackable-blockchains-are-now-getting-hacked/](https://www.technologyreview.com/s/612974/once-hailed-as-unhackable-blockchains-are-now-getting-hacked/)

> oward the middle of 2018, attackers began springing 51% attacks on a series of relatively small, lightly traded coins including Verge, Monacoin, and Bitcoin Gold, stealing an estimated $20 million in total. In the fall, hackers stole around $100,000 using a series of attacks on a currency called Vertcoin. The hit against Ethereum Classic, which netted more than $1 million, was the first against a top-20 currency.
> 
> David Vorick, cofounder of the blockchain-based file storage platform Sia, predicts that 51% attacks will continue to grow in frequency and severity, and that exchanges will take the brunt of the damage caused by double-spends. One thing driving this trend, he says, has been the rise of so-called hashrate marketplaces, which attackers can use to rent computing power for attacks. “Exchanges will ultimately need to be much more restrictive when selecting which cryptocurrencies to support,” Vorick wrote after the Ethereum Classic hack.


You can rent computing power quite cheaply now, and to conduct an attack, you don't need to own masses of computing power, you just need access to it for a short amount of time.  This is a concept that would have been almost impossible over a decade ago, but its now trivial to rent compute by the second or by the minute.  

That means that you can attack something like the blockchain far more cheaply, but only for a few seconds.  But if all you want to do is allow a few transactions and then undo them, you only need control for a very short amount of time.


## [You Do Not Need Blockchain: Eight Popular Use Cases And Why They Do Not Work](https://blog.smartdec.net/you-do-not-need-blockchain-eight-popular-use-cases-and-why-they-do-not-work-f2ecc6cc2129)

[https://blog.smartdec.net/you-do-not-need-blockchain-eight-popular-use-cases-and-why-they-do-not-work-f2ecc6cc2129](https://blog.smartdec.net/you-do-not-need-blockchain-eight-popular-use-cases-and-why-they-do-not-work-f2ecc6cc2129)

> Let’s say you ordered some goods, and a carrier guarantees to maintain certain transportation conditions, such as keeping your goods cold. A proposed solution is to install a sensor in a truck that will monitor fridge temperature and regularly transmit the data to the blockchain. This way, you can make sure that the promised conditions are met along the entire route.
> 
> The problem here is not blockchain, but rather sensor, related. Being part of the physical world, the sensor is easy to fool. For example, a malicious carrier might only cool down a small fridge inside the truck in which they put the sensor, while leaving the goods in the non-refrigerated section of the truck to save costs.


This is a nice review of some of the worst claims of blockchain enthusiasts.  The most common of these is this one, in various forms, which can be summed up as "blockchain is not physical things".  Taking data about a physical thing and putting it on the blockchain will only ever track the authorised correct changes to the physical thing, it won't protect against real attempts to change the physical thing, because the blockchain representation is precisely that, just a representation.


