---
title: "90 - How do we deal with personal data?"
date: 2020-02-23
description: "Editors Note:  Delayed by a day this week because I've been away on holiday and flights back were delayed.  That also explains all the comments and analysis helpfully provided by [Joel](https://joelgsamuel.com/) this week.  Thanks Joel."
permalink: /how-do-we-deal-with-personal-data/
---

Editors Note:  Delayed by a day this week because I've been away on holiday and flights back were delayed.  That also explains all the comments and analysis helpfully provided by [Joel](https://joelgsamuel.com/) this week.  Thanks Joel.

There's a lot of discussion around data going around at the moment.  The UK leaving the European Union leaves the UK in an interesting position with regard to data privacy.  The EU's General Data Protection Regulations (GDPR) is considered the strongest protection of personal data that exists around the world at the moment, and the UK can now potentially deviate from that standard to a lower standard of protection should it choose to.  However it has already enacted a recent update to the Data Protection Act which binds the laws of the country to meet the standards of the GDPR, and so it would require modifications to that act to pass parliament to deliberately loosen data protection.  This might sound like madness, but loosening of regulations happens all the time.  The acts are often passed as "red tape reduction" style acts and so can be very popular within certain political circles.

But data is such a broad term that it's difficult to even know what we are talking about half of the time.  Amazon as a company keeps records on you and how you interact with their services. Is that personal data about you, or is it product development data about their product usage?  As someone directly involved in service design and development, I often find myself saying "Can we see how users actually use this thing and then make a decision?".  A recent example was to do with setting session timeouts.  We don't know what the right number is in some cases, because the sign in process in some government systems can be user unfriendly.  We don't want to timeout someone who has taken a break to make dinner for their kids, or who started it at work one evening and will resume it the next morning, but we also don't want an excessively long opportunity for an attacker to get into their system and steal or modify their data.

I found myself asking questions like "How many people start a session and finish the same day?", "How many people start a session on one computer and then resume the session on a phone or other computer?", "How many users drop out when we ask them to sign back in?".  In order to answer these questions, we need to gather data on users, on how they use the service we are building and how they interact with it.  That also means trying to personally identify them so that we can tell if they switch from their desktop to a phone at key points in the process.  

But as an end user, I might feel worried that a government department is keeping track of how I apply to a given service.  If that service is sensitive, I might not want to be identified.  I might be concerned that I'll get adverts relating to that service in my normal browsing, which coworkers or my partner might see.  I might also have concerns that the Government might combine that data with other government services to "combat fraud" which might reveal interesting combinations of service use.

Our data concerns as individuals are often far in excess of my experience of actual data analytics, that the laws, like GDPR, try to prevent the sort of advanced data processing that companies wish they could do, when in reality they have a bad spreadsheet run by Ron who still hasn't worked out how VLOOKUP works.  I'm not saying that Amazon or Google or other companies aren't actively mining the data they get from us, or that they should be allowed to, but I do think that we tend to get a little bit "chicken little" about the worries of data protection sometimes.

Yes, there are reasons to be concerned with whether we are doing enough about data protection.  Yes, it's right that we ask questions about whether the data collection is necessary, important and compliant with law.  But it's also OK that product and service teams want to collect data to make better products.  Whether that be to understand how users actually use their service, or to make recommendation engines that don't assume that because I once bought a toilet seat, that I want to buy one everytime I shop online.

## [What’s in a name? Why we call it Maturity Mapping - Chris McDermott - Medium](https://medium.com/@chrisvmcd/whats-in-a-name-why-we-call-it-maturity-mapping-ebc875828465)

[https://medium.com/@chrisvmcd/whats-in-a-name-why-we-call-it-maturity-mapping-ebc875828465](https://medium.com/@chrisvmcd/whats-in-a-name-why-we-call-it-maturity-mapping-ebc875828465)

> There is an anecdote about Peter Drucker that matters in this context. He observed that employees were often perceived by managers as a liability, almost as a necessary evil, and stand-out performers were seen as the exception to the rule. We had to accept having low-performers as a consequence of seeking and finding high-performers. He also noticed how employees only appeared in financial documents as a cost. Contrasting that, he noticed that some “inventory” was seen as assets (shown as having value on a balance sheet) and worth of investment and wanted managers to apply that thinking to people too. He then introduced the language of calling people resources in the hope it would shift the view of managers towards seeing people as assets to the business. We all know too well how this worked out. If the underlying thinking doesn’t change, changing the words/terms has no consequence, because the people who see employees as a liability will happily call them resources and still continue having dismissive models in mind. And if managers do not see the value of working with people, making them use a different term mainly spurs resentment. But if we can get people engaged in a contextualising practice, facilitating the engagement by using the terms they expect and use, we can (maybe) reshape their associated models.


I love the work that they have done on maturity models, but this stood out to me.  I didn’t know that the idea of calling people Human Resources was designed to make organisations think of them more as value delivering assets rather than costs to the organisation.  Personally I prefer teams who consider talent management rather than Human Resources.  The idea that the people in our organisation are our talent really drives the idea that these are the people who develop value rather than resources that hold an ongoing cost.


## [Deepfakes by BJP in Indian Delhi Election Campaign - VICE](https://www.vice.com/en_in/article/jgedjb/the-first-use-of-deepfakes-in-indian-election-by-bjp)

[https://www.vice.com/en_in/article/jgedjb/the-first-use-of-deepfakes-in-indian-election-by-bjp](https://www.vice.com/en_in/article/jgedjb/the-first-use-of-deepfakes-in-indian-election-by-bjp)

> When the Delhi BJP IT Cell partnered with political communications firm The Ideaz Factory to create “positive campaigns” using deepfakes to reach different linguistic voter bases, it marked the debut of deepfakes in election campaigns in India. “Deepfake technology has helped us scale campaign efforts like never before,” Neelkant Bakshi, co-incharge of social media and IT for BJP Delhi, tells VICE. “The Haryanvi videos let us convincingly approach the target audience even if the candidate didn’t speak the language of the voter.” 
> 
> Tiwari’s fabricated video was used widely to dissuade the large Haryanvi-speaking migrant worker population in Delhi from voting for the rival political party. According to Bakshi, these deepfakes were distributed across 5,800 WhatsApp groups in the Delhi and NCR region, reaching approximately 15 million people.
> 
> So it’s not surprising that the prospect of building campaign businesses using deepfakes to influence the masses has alarmed fact-checking organisations and policy wonks. Many think deepfakes would take the ongoing war on disinformation and fake news to a whole new level—one that has already been dubbed a “public health crisis”.


I thought this was an interesting use of deep fake videos.  The idea that someone would use a deep fake capability to generate themselves speaking the same message, in different languages, depending on the audience is a fascinating one.  

We’ve so far seen only the negative sides of deepfakes, the ability to overlay people unwillingly into porn videos, or potentially the possibility of political deeds fakes (not that any have really been found yet).

But the fact that technology is fundamentally morally independent means that there must be positive implications as well.  People using deep fake technology to wish wedding greetings from behind the grave, people using it reach the previously unreachable, the possibilities are as endless as our actual morality as humans.


## [Encryption on Facebook, Google, others threatened by planned new bill | Reuters](https://www.reuters.com/article/us-usa-technology-encryption/u-s-lawmakers-to-introduce-bill-that-threatens-encryption-on-tech-platforms-idUSKBN20F1ZP)

[https://www.reuters.com/article/us-usa-technology-encryption/u-s-lawmakers-to-introduce-bill-that-threatens-encryption-on-tech-platforms-idUSKBN20F1ZP](https://www.reuters.com/article/us-usa-technology-encryption/u-s-lawmakers-to-introduce-bill-that-threatens-encryption-on-tech-platforms-idUSKBN20F1ZP)

> The bill [...] aims to fight such material on platforms like Facebook (FB.O) and Alphabet’s Google’s (GOOGL.O) by making them liable for state prosecution and civil lawsuits. It does so by threatening a key immunity the companies have under federal law called Section 230.
> 
> This law shields certain online platforms from being treated as the publisher or speaker of information they publish, and largely protects them from liability involving content posted by users.
> 
> The bill, titled “The Eliminating Abuse and Rampant Neglect of Interactive Technologies Act of 2019,” or the “EARN IT Act,” threatens this key immunity unless companies comply with a set of “best practices,” which will be determined by a 15-member commission led by the Attorney General.
> [...]
> The sources said the U.S. tech industry fears these “best practices” will be used to condemn end-to-end encryption


(Joel) (I wonder how much time goes into the creative naming of Bills?)

Legislation to require good practice (and enforce that with fines and so on) is _generally_ a good idea as it can standardise, equalise and foster a strong elevated baseline - particularly if the sector involved is not able to self-regulate between competitors or the common denominator is deemed too low.

We have seen excellent work from the National Cyber Security Centre (NCSC) and the Department for Digital, Culture, Media and Sport (DCMS) in the UK to positively [influence the security and privacy regimes of IoT devices](https://www.gov.uk/government/consultations/consultation-on-regulatory-proposals-on-consumer-iot-security/consultation-on-the-governments-regulatory-proposals-regarding-consumer-internet-of-things-iot-security)

The exception access debate isn't going away but I believe it is stifled and made emotive and polarised (and therefore further divisive) when governments and legislative bodies say (or are perceived as saying) they don't want things encrypted. To me, [the technology bits are easy it is the associated transparency with judicial and civilian oversight that are the tough nuts to crack](https://medium.com/@joelgsamuel/exceptional-access-legal-frameworks-technology-trust-ba9d7a7ce0cb), because ultimately, for a variety of reasons, people don't trust governments and intelligence agencies.

(Michael) This bill is an interesting one.  The idea being that online social platforms can make claims to be arbitrary communication providers, and thus exempt from liability for the content posted by their users, but only if they meet the requirements that are still not actually defined in law.

The problem I have with this is that it's a slippery slope for those social platforms.  What are those requirements?  Are they fixed or could they change in future years? Is there any actual incentive, or would they be better off going it alone without the government paper shield?  This bill doesn't actually seem to address any of these, and given the US Governments lack of comprehensive understanding of technology, I'd be loath to support that any technological best practices be baked into a law


## [NSO Employees Take Legal Action Against Facebook for Banning Their Accounts](https://www.vice.com/en_us/article/7x5nnz/nso-employees-take-legal-action-against-facebook-for-banning-their-accounts)

[https://www.vice.com/en_us/article/7x5nnz/nso-employees-take-legal-action-against-facebook-for-banning-their-accounts](https://www.vice.com/en_us/article/7x5nnz/nso-employees-take-legal-action-against-facebook-for-banning-their-accounts)

> Last month, Facebook sued NSO in California for leveraging a vulnerability in the WhatsApp chat program that NSO Group clients used to hack targets. As part of that, Facebook also banned the personal Facebook and Instagram accounts of multiple current and former NSO employees.
> 
> The new lawsuit argues that Facebook violated its own terms of service by blocking the NSO employees, and it used personal information they shared with Facebook in order to identify them, in violation of an Israeli privacy law. As relief, the lawyers ask the court to make Facebook lift the ban on the accounts. 
> 
> "It appears that Facebook used the [NSO employees'] personal data...in order to identify them as NSO employees (or former employees), in service of imposing 'collective punishment' on them, in the form of blocking their personal accounts," the lawsuit reads


(Joel) This is... interesting.

I'm seeing this as two parts: (1) what Facebook did to identify who was who and where they work/worked; and (2) 'collective punishment' to kick them off their platform and ban them.

(1) it is unclear to me how reasonable or unreasonable that is because part of engaging with Facebook is handing them a bunch of your data and the lawsuit acknowledges this as what was done by the individuals, so why is it in violation of Israeli privacy law (which assumably has a concept of consent).

(2) organisations generally have the right to refuse service and they are effectively allowing you to do so as part of a promise (contract, terms of service etc) and in general will also have terms that decide how they decide to terminate that relationship, often including a "because we feel like it" clause. I can imagine Facebook making that argument, or reinstating the accounts only to suspend them under a different guise (such as thinking they are a bot, so they have to provide an increasing amount of personal data to reactivate the account and Facebook just happens to take a few months to process documents).

(Michael) I wonder if these users used their personal accounts as part of their research? It would be very easy to do, back in the days when I was writing against the Facebook API and Twitter API, I needed to test with multiple accounts, and of course I used my personal account occasionally, because it was still signed in.

If facebook simply detected all accounts that were involved in using a security flaw, they may have swept up these users accounts anyway.

But as Joel says, there is no real requirement for Facebook to give accounts to anyone it doesn't want to.  A service can deny accounts on any terms is chooses, so long as it is not found to be discriminatory based on a legally protected characteristic. I suspect this lawsuit will fail and is just designed to burn Facebooks time, energy and money.


## [Governments of the world just ramped up spying on reporters - Columbia Journalism Review](https://www.cjr.org/first_person/ft-nations-surveillance-attacks.php)

[https://www.cjr.org/first_person/ft-nations-surveillance-attacks.php](https://www.cjr.org/first_person/ft-nations-surveillance-attacks.php)

> The draining battery indicated that something or someone was using the phone’s resources. We did a forensic analysis, and could not easily identify this software or person. So we began to suspect a sophisticated effort, one that not many people, or even companies, could manage. It was almost certainly an attack by a nation state—most likely the one we were investigating. There’s no real way to defend against such attacks. So we decided to use disposable phones and SIM cards.
> [...]
> The truth is that something like WhatsApp is probably fine for most communications. The sensitive stuff, though, should go on something more trustworthy, such as Signal. The app is open source, which means its code is available to anyone. Any breach, then, will be immediately known—not be hidden for months while a company tries to navigate the PR consequences, leaving its users exposed in the meantime.


(Joel) I thought about whether to comment on this as I was (and still am) worried about simply throwing rocks at someone's writeup of some of their work.

I mostly like the article but I am unable to reconcile most of the statements/accusations made and the associated conjecture.

When you work in cyber security and don't actually spend your time defending against hostile state actors (or their proxies) it is sometimes a _little bit_ fun to have those conversations and pretend how you would defend against those problems. (This is actually a problem itself sometimes as people over-egg this, and you can end up wasting a lot of time/money trying to defend against an adversary who has no interest in you, or won't deploy their full capability against you and might stick to commodity tools.)

Journalism, particularly in the midst of investigative work into in the actions or inactions of a government, poses some interesting personal security challenges. One of my reactions was "well, yes, obviously" to the use of 'trip' or burner equipment however this can be easier said than done as journalists are likely to want to maintain their same contact details (so trip numbers and trip emails are hard to work with - [like I've blogged about before](https://medium.com/@joelgsamuel/being-safe-on-hostile-wifi-or-mobile-networks-7f9b045d3b98)) so I would look to the use of logical persistent services (VoIP applications etc) rather than rely on a telecoms provider to associate a number to a SIM card.

There are various debates about whether open source makes things more secure or not. The 'jump' made here (as far as I understand the phrasing) is that _because_ Signal's app is open source, "breaches" _will_ be immediately known. This makes a whole bunch of problematic assumptions about how issues are reported to open source projects and the authoritative and singular nature of code repositories (that there are no other ones that you cannot see). Further, open source or not, authors should control how they address issues: you don't really want to alert people of the exact issue before the fix is available (which is what a public pull request with a bunch of code to fix a problem would probably do).

(Michael). I'm really torn on this article.  I really like the security pragmatism that is throughout this.  I especially like the identification that different state level threats will use different tactics, along with the fact that most of these attacks are just the same low level attacks that competent cyber crime operators conduct, from phishing to attacking default credentials.  Where the state level of capability is applied, it was more with a physical presence, which is something that states have a huge power to do within their own borders.

However, as interesting as it is to get data points on these attacks, many of the purported attacks in this article are inconclusive or happenstance.  They do not have the rigour applied to them, or they combine sentences in such a way as to sound scary but don't hold up to analysis.  For example, the Russia office having a default username/password combination is a vulnerability.   It's not evidence of a breach or of any attack.  If the author had said that they were attacked through this, then there's something more to say, but they don't.  Additionally, knowing that the FSB office overlooks the building is of no relevance to a cyber based attack on a default username and password.  Your office could be half way around the world, have the default credentials and you could be attacked by the FSB.

As a threat brief for journalists however, this works to remind them that they are often considered valid targets around the world by governments who really want to know what they are writing about.  It should remind us that Governments do have technical and physical capabilities and are willing to deploy them.  The complication here is that this doesn't really give you any actions you can take to defend yourself.


## [IDF stops Hamas 'honeypots' from trapping soldiers - The Jerusalem Post](https://www.jpost.com/Israel-News/IDF-foils-Hamas-operation-targeting-soldiers-Operation-Rebound-617744)

[https://www.jpost.com/Israel-News/IDF-foils-Hamas-operation-targeting-soldiers-Operation-Rebound-617744](https://www.jpost.com/Israel-News/IDF-foils-Hamas-operation-targeting-soldiers-Operation-Rebound-617744)

> Once on the phone, the virus would give Hamas operatives control over all aspects of the phone, including pictures, the soldier’s location, text messages and the soldier’s contact list. The virus would also have access to the phone’s camera and microphone, taking pictures and recording conversations remotely without the soldier knowing.
>  
> Unlike in previous attempts by Hamas, the group also was able to download and transfer files and have access to the phone’s GPS, allowing them to know the infected device’s location. At that point, the Hamas operatives would stop communicating with the soldiers.
>  
> While the military knew about Hamas’s operation for the past several months, it was decided to let them continue, to enable the IDF to have more effective technological means to stop the terror group.


The use of fake profiles to tempt on the ground soldiers into installing software on their devices that they carry with them everywhere is a lovely and yet very old technique for gathering information.  With a technological twist of installing the software, making it appear to disappear and of course ghosting the poor soldier who installed the app, it turns the solder essentially into an unwitting double agent.

The counter to that, that the military leadership knew about the penetration, and decided to deliberately run the double agent without their knowledge, but watching to see what the adversary would do is again, classical military thinking that could have come from the world wars or the cold war.


## [The US Fears Huawei Because It Knows How Tempting Backdoors Are | WIRED](https://www.wired.com/story/huawei-backdoors-us-crypto-ag/)

[https://www.wired.com/story/huawei-backdoors-us-crypto-ag/](https://www.wired.com/story/huawei-backdoors-us-crypto-ag/)

> Still, researchers say that it's unclear what exactly the US is alleging on a technical level with its new allegations that Huawei maintains network access that other manufacturers don't.
> 
> "We would need to have more details to be able to draw any conclusions," says Lukasz Olejnik, an independent cybersecurity researcher and advisor. "We know that forms of technical lawful intercept are a feature of all generations of cellular telecom specifications. But it's unclear what officials in the Wall Street Journal story are referring to exactly."
> 
> If Huawei has been abusing law enforcement access capabilities to clandestinely gather or funnel user communication data, it would be an example of the types of backdoors US officials have warned against.


The maddening thing about this briefing, that the US clearly have the Wall Street Journal, is that we don't know the details, but it still feels like a campaign of Fear, Uncertainty and Doubt by the US Government.  They are likely alleging that Huawei has the ability to use the lawful intercept features that they build into their systems, the ones that the US requires them to put their for their own lawful intercept purposes.  Obviously, those features are only supposed to be used when an individual is authorised by the appropriate lawful authority, but as the security community has been saying for a while now, any backdoor can and will be used by anyone who wants to use it.

I don't think this changes the risk equation for the use of Huawei kit substantially, as I doubt that using any other providers kit would prevent the existence of the legally mandated lawful intercept functions.  As the UK has done, instead an appropriate risk managed framework for using the devices on their network, knowing that some proportion could be compromised in some manner is the only way to proceed.


## [How fake faces are being weaponized online - CNN](https://edition.cnn.com/2020/02/20/tech/fake-faces-deepfake/index.html)

[https://edition.cnn.com/2020/02/20/tech/fake-faces-deepfake/index.html](https://edition.cnn.com/2020/02/20/tech/fake-faces-deepfake/index.html)

> Last year, Phil Wang, a former software engineer at Uber, created a website called "This person does not exist." Every time you visit the site you see a new face, which in most cases looks like a real person. However, the faces are created using AI.
> 
> The people, as the site's name suggests, literally do not exist. Wang's goal, he told CNN Business, is to show people what the technology can do. By exposing people to these fake faces, he hopes the site will "vaccinate them against this future attack."
> 
> There are other sites similar to Wang's where people can download fake images. Fun and illuminating, Wang's site lets people see this new technology in an accessible way. But it also reflects a wide ethical dilemma for Silicon Valley: Just because the technology exists and can do something, does that mean technologists should make it accessible to everyone?
> 
> Nathaniel Gleicher, who leads Facebook (FB)'s team that tackles coordinated disinformation campaigns, including those linked to the Russian and Iranian governments, said that developers need to think through how making tools like this accessible could be used by bad actors.
> 
> "Building these sets is critical for research, but just as important that we think through the consequences as we build," Gleicher tweeted in reaction to the release of a dataset of fake faces released earlier this year.
> 
> After looking at the photo of "Jessica," Wang couldn't say if it was created through his site -- he doesn't save images as they are generated. He was certain "Jessica" was not real, pointing, like others, to the earring. The AI system, he said, "hasn't seen enough jewelry to learn it properly."
> 
> But he also cautioned that fake faces like "Jessica" may just be a small sign of what's to come.
> 
> "Faces are just the tip of the iceberg," he said. "Eventually the underlying technology can synthesize coherent text, voices of loved ones, and even video. Those social media companies that have AI researchers should allocate some time and research funds into this ever growing problem."


I referenced this back in [CyberWeekly #73](https://www.cyberweekly.net/know-your-users).  What I said was:

> More interestingly is what these stock photos will be used for. Phishing, cat-phishing, and false profiles probably. Will the suppliers of these do anything to provide social networks with the ability to detect the use of these photos so they can warn their users?

The creation of fake avatars and profiles for LinkedIn, Twitter, Facebook etc, is nothing compared to this.  Many industries today, from adult performance to job interviews, hotel booking to opening a bank account, require you to submit a photo of your government issued ID.  But that ID is never validated, it is only kept for later investigation.  

Imagine being able to download fake generated government ID documents.  These will look real, will have details on them that seem real, but unless you have access to a Government document checking service, you won't have any ability to verify that it's a real document.  This will be the next step of this form of photo manipulation technology.


## [Amazon: How Bezos built his data machine | BBC](https://www.bbc.co.uk/news/extra/CLQYZENMBI/amazon-data)

[https://www.bbc.co.uk/news/extra/CLQYZENMBI/amazon-data](https://www.bbc.co.uk/news/extra/CLQYZENMBI/amazon-data)

> You might call me an Amazon super-user.
> 
> I’ve been a customer since 1999, and rely on it for everything from grass seed to birthday gifts.
> 
> There are Echo speakers dotted throughout my home, Ring cameras inside and out, a Fire TV set-top box in the living room and an ageing Kindle e-reader by my bedside.
> [...]
> I submitted a data subject access request, asking Amazon to disclose everything it knows about me
> 
> Scanning through the hundreds of files I received in response, the level of detail is, in some cases, mind-bending.


(Joel) Quelle surprise.

If you use a variety of services (some of which includes a microphone to listen to you, and reply, and learn how to do so better next time) from a single organisation for many years and then look back at a central view of that data... it is (fairly reasonable, perhaps) going to be a lot of data - so I am struggling to take the introduction to this article seriously.

Amazon, like Google, is ultimately a data business. It provides a series of products and services that millions upon millions of people interact with every day, and with some marketing success, across various aspects of their lives.

One camp thinks this is great, the handing over of data or personality in return for a smooth and coherent service that in theory gets better over time and could in theory predict your needs (although I still don't know why Amazon will show me lots of different items similar to what I just bought. I already bought it, how many do you think I need?!). Another camp say this is unreasonable data hoarding and brokering for profit and ultimately that you should be able to interact with a service to fulfil that service, but any data passed or generated should not be used as part of a wider profile (within the same organisation or sold/shared).

I think I'm probably somewhere in the middle: I would like a coherent service from a single organisation (Amazon.co.uk associating what I buy with new movies/TVs I might like in Amazon Prime would be an interesting feat, but they are welcome to do so if they think they can get that working) but they should not share, in whole or in part, including derived personality, outside of Amazon.


## [Google’s UK privacy snub no cause for alarm, says Brave - Decrypt](https://decrypt.co/20109/google-uk-privacy-snub-no-cause-for-alarm-says-brave)

[https://decrypt.co/20109/google-uk-privacy-snub-no-cause-for-alarm-says-brave](https://decrypt.co/20109/google-uk-privacy-snub-no-cause-for-alarm-says-brave)

> Google’s plan, according to Reuters, would involve transplanting British data from the EU-governed Ireland to the US, where privacy laws are lax. 
> 
> All this could, potentially, leave an opening for companies which explicitly don’t track data—for instance, those involved in the cryptocurrency space. 
> 
> You’d expect that Brave, which does not track users and rewards them in cryptocurrency for engaging with ads, would be one such company.
> 
> Of the latest revelations, however, Brave’s Johnny Ryan demurred, noting that GDPR rules in the UK remain in force, at least for now. 
> 
> “The GDPR continues to apply to all people in the UK at present, irrespective of any Google actions,” he told Decrypt. He added that intelligence wise, it is probably in the UK’s interest to hew to the EU’s provisions. 
> 
> “The UK is eager to maintain a free flow of personal data between it and the EU, and has said so since the start of the Brexit planning,” he said. “This is important for all or almost all sectors of the economy. If the UK were to remove itself from the GDPR structure, it would be burdensome to all businesses that work in the UK and the much larger EU market.”


It's important to note that lots of people did a whole "The sky is falling" here, with Google wanting to essentially tag all UK specific data with a "UK" tag instead of an "EU" tag.  This is in preparation in case UK law changes.  But in reality, it is very unlikely that UK law is going to change anytime soon.

We will need a new contract with Google (and other US cloud providers) because the existing EU based model clauses bind you to be able to claim redress through european courts, of which the UK may well no longer be able to do.  

If the law doesn't change, then there is likely no real difference to how the data is held, and what protections that data has while in the care of these big service providers.  What is interesting to me is how many of these data sets will contain data that is of an EU person, and thus actually should be held with the EU tag rather than a UK tag, and whose liability it is to ensure that data is appropriately separated.  Of course, if UK law doesn't diverge, then it won't matter, but if we do diverge, then a lot of UK companies are going to have to tell their suppliers if the data is personal data of UK citizens or of EU citizens.  There is of course no reason that a UK company can't keep data in a better protected regime, such as via a contract that enforces the GDPR provisions, even if they aren't legally compelled to do so.  I'd hope to see a lot of UK companies taking advantage of this in future.


