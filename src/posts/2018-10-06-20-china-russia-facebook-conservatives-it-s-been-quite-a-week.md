---
title: "20 - China, Russia, Facebook, Conservatives... It's been quite a week"
date: 2018-10-06
description: "Phew."
permalink: /china-russia-facebook-conservatives-it-s-been-quite-a-week/
---

Phew.

I didn't think reading and writing this weeks newsletter would ever end.  There's been so many interesting stories, and news that it took me a lot this week to read all of the summaries and try to find just the best links to share with you.  There have been several that have gone to the wayside in all of this, but I wanted to draw out two major points from all of the who-ha.

Technical reporting has come along in leaps and bounds, with reporters covering highly technical beats with style.  But most reporters just don't have the technical knowledge to actually understand the technology behind the things they are reporting on.  There are very few journalists who actually know what a cross-site-scripting attack actually looks like, or knows how javascript is packaged and executed.

In the SuperMicro story, we have some very good journalists, but clearly the exact technical details of this story is beyond them.  Is this chip actually embedded in the BMC? Does it have it's own operating system, ram, network etc? How would it be fitted to the board?  These are the questions that technical people are left asking, and these are the things that can confuse journalists reporting on such stories.

In the facebook phone number story, we see that that reporting is again unclear about how facebook actually operates and runs its organisation. Journalists imagine a machine army of people who write code, where that code is left alone and not touched later. But the likely thing is that the code that stores personal data and makes it available for advertising targeting is touched by thousands of people. We know from working in organisations that legacy code is often mysterious, that tests document the what of the code, but rarely actually document the why or the how.

There is increasing pressure on journalists to cover stories about technology, security, privacy, national security and business at a faster and faster pace, and we put a misplaced trust that journalistic organisations are capable of doing so consistently and factually all of the time.  But how can they possibly do so, especially given the skills shortages in these areas as it is?

The facebook and google stories lead me onto my second point, that technical organisations still don't understand why they need to segment and manage their user data carefully. Knowing how someone shared data with you, and what context they were in is important to not surprising them. And what might seem obvious at the time, will not make sense to the person reviewing your code in five years time, whether that's you or someone who replaced you.

Only by clearly managing personal data into small silos, where data is stored according to how it was collected and agreed to be processed can we build customer centered privacy by design into the systems that we build. Because, sad to say, we are building tomorrows legacy code today, and many of us won't be in the same organisations to tell people what we were thinking.

## [The Big Hack: How China Used a Tiny Chip to Infiltrate U.S. Companies - Bloomberg](https://www.bloomberg.com/news/features/2018-10-04/the-big-hack-how-china-used-a-tiny-chip-to-infiltrate-america-s-top-companies?srnd=businessweek-v2)

[https://www.bloomberg.com/news/features/2018-10-04/the-big-hack-how-china-used-a-tiny-chip-to-infiltrate-america-s-top-companies?srnd=businessweek-v2](https://www.bloomberg.com/news/features/2018-10-04/the-big-hack-how-china-used-a-tiny-chip-to-infiltrate-america-s-top-companies?srnd=businessweek-v2)

> During the ensuing top-secret probe, which remains open more than three years later, investigators determined that the chips allowed the attackers to create a stealth doorway into any network that included the altered machines. Multiple people familiar with the matter say investigators found that the chips had been inserted at factories run by manufacturing subcontractors in China.


There's so much to this story that I don't think I can do it justice.

For starters, Apple has issued a very clear denial, [On this we can be very clear: Apple has never found malicious chips, “hardware manipulations” or vulnerabilities purposely planted in any server.](https://www.apple.com/newsroom/2018/10/what-businessweek-got-wrong-about-apple/), and Amazon was equally straight talking with [ At no time, past or present, have we ever found any issues relating to modified hardware or malicious chips in SuperMicro motherboards in any Elemental or Amazon systems. Nor have we engaged in an investigation with the government.](https://aws.amazon.com/blogs/security/setting-the-record-straight-on-bloomberg-businessweeks-erroneous-article/).  There is no way that these companies would issue such straight talking denials if they were being strong-armed by the Government and told they couldn't talk about these investigations.  

Amazon and Apple are interesting targets. Why for example, are Microsoft and Google not included as targets? How about Facebook, Twitter or other leading tech companies?

However, the article contains a lot of details, and a very strong set of claims from Bloomberg, this isn't a fly by night newsletter and an article dashed off, this was an in depth investigation that must have been checked and vetted thoroughly.  However, Bloomberg, and indeed these writers themselves, [have gotten the technical facts on stories wrong in the past stories](https://twitter.com/GossiTheDog/status/1048322164653535232) so aren't foolproof.

On the technical side, I'm suspicious that a hardware implant, as described, can possibly achieve what is being described.  Hosting systems inside Amazon and Apple are vastly complicated, and the networks are not designed to allow the hardware direct access to the internet.  Instead a complex layer of Software Defined Networks overlay the network, because the hardware is often just a base for virtual machines and networks get complicated at that point.  

Something that could inject code into the Baseboard Management Controller is very very low level, and the complexity of the software stack above them, which varies from system to system would make this an amazing feat of engineering to carry out.

But as has [been pointed out elsewhere](https://www.theregister.co.uk/2018/10/04/supermicro_bloomberg/), this is the dream of intelligence agencies the world round, an undetectable hardware implant that can take over the machine.

What's the truth of these claims and counterclaims?  I'm not sure we'll find out anytime soon.  Unless Bloomberg is willing or capable of naming their sources, or their sources come back to correct the reporters, I don't think we'll find out what was actually said.  Equally, denials from the companies will always be disbelieved, because the _spooky_ nature of intelligence investigations means that any statement, even the most straight spoken, will be treated with suspicion.  I personally doubt the validity of the story, I think there has been confusion in the reporting from the sources and the questions asked.

Suffice to say, I suspect that for most of us, this story is covering threat actors at the highest levels, and far beyond our reasonable threat model.  You shouldn't be reviewing your hardware or picking a cloud provider based on this story.

Your real threat today is still just as it was yesterday, that your users will click a link in a phishing email and enter their credentials into the site.


## [The Apollo Breach Included Billions of Data Points | WIRED](https://www.wired.com/story/apollo-breach-linkedin-salesforce-data/)

[https://www.wired.com/story/apollo-breach-linkedin-salesforce-data/](https://www.wired.com/story/apollo-breach-linkedin-salesforce-data/)

> "What almost worries me more [than the raw data exposure] is the mapping of social identities to email address and other personal data, because there's now so much more you can pull on a person," Hunt says. "We're continually seeing massive breaches of data aggregators who hold information on people who have no idea their personal information has been used in this fashion. I understand that it's Apollo's customers who provided access to their customers, but the fact remains that there are north of 100 million people out there who have no idea who Apollo is nor that their information was exposed."


This quote from Troy Hunt really sums this up for me.  My email address was in this breach notification, and I don't really know or care who Apollo are, but I'm not very happy that they have my information.

Note that this story from Wired, should be read alongside this [Krebs on Security](https://krebsonsecurity.com/2018/10/when-security-researchers-pose-as-cybercrooks-who-can-tell-the-difference/) take as well, since Brian Krebs casts a lot of doubt on the methods of the original security researcher who found the data. 


## [French police officer caught selling confidential police data on the dark web | ZDNet](https://www.zdnet.com/article/french-police-officer-caught-selling-confidential-police-data-on-the-dark-web/)

[https://www.zdnet.com/article/french-police-officer-caught-selling-confidential-police-data-on-the-dark-web/](https://www.zdnet.com/article/french-police-officer-caught-selling-confidential-police-data-on-the-dark-web/)

> Officials said they tracked down the real-life identity of Haurus after they seized and shut down the Black Hand portal on June 12, earlier this year. They were also able to track down some of the documents put up for sale on the market based on an individual-specific code that's added to official documents and tracks their history.
> 
> Haurus was charged on September 26 and arrested two days later in Nanterre, Hauts-de-Seine. He faces up to seven years in prison and a fine of up to a fine of €100,000 / $115,000.


This is more proof that you don't necessarily have to be smart to work in an intelligence organisation.  Doing this will almost certainly get you caught, since it's very hard for someone not on the inside to have access to this info. 


## [bellingcat - 305 Car Registrations May Point to Massive GRU Security Breach - bellingcat](https://www.bellingcat.com/news/2018/10/04/305-car-registrations-may-point-massive-gru-security-breach/)

[https://www.bellingcat.com/news/2018/10/04/305-car-registrations-may-point-massive-gru-security-breach/](https://www.bellingcat.com/news/2018/10/04/305-car-registrations-may-point-massive-gru-security-breach/)

> The database contains their full names and passport numbers, as well as — in most cases — mobile telephone numbers. Besides the physical street address, the address entry points out the specific Military Unit: 26165. This is the same unit as the one identified in the United States Department of Justice indictments that were also announced on October 4, 2018.
> 
> If these 305 individuals — whose full personal data is available in the automobile registration database consulted by Bellingcat — are indeed officers or otherwise affiliated with the GRU’s military unit 26165, their listing in a publicly accessible database may constitute one of the largest mass breaches of personal data of an intelligence service in recent history.


This is increased evidence of a mess of opsec behaviours in this incident.  This [twitter thread](https://twitter.com/AlexGabuev/status/1048153070956367873) by Alexander Gubuev talks about the fact that registering your car as located at GRU's headquarters might mean you end up on a database of people who don't get speeding tickets, pulled over etc.

In essence, never underestimate the way that your staff will seek the easiest solution with the most reward for themselves.  Most of those staff would never realise that this was putting themselves at risk.


## [bellingcat - Skripal Suspects Confirmed as GRU Operatives: Prior European Operations Disclosed - bellingcat](https://www.bellingcat.com/news/uk-and-europe/2018/09/20/skripal-suspects-confirmed-gru-operatives-prior-european-operations-disclosed/)

[https://www.bellingcat.com/news/uk-and-europe/2018/09/20/skripal-suspects-confirmed-gru-operatives-prior-european-operations-disclosed/](https://www.bellingcat.com/news/uk-and-europe/2018/09/20/skripal-suspects-confirmed-gru-operatives-prior-european-operations-disclosed/)

> Bellingcat compared the passport number on Col. Shishmakov’s cover-identity passport, with the numbers of the (cover-identity) passports of “Petrov” and “Boshirov”. The numbers were from the same batch, with only 26 intervening passport numbers between “Petrov”’s (654341297), and “Shirokov”’s (654341323) number. “Shirokov”’s passport was issued in August 2016, implying that Petrov’s and Boshirov’s passports were issued by the same special authority earlier that year.


This is an interesting bit of investigatory work by Bellingcat, that I was going to include last week, but it didn't fit.  I didn't realise how timely it would be this week, with the further revelations.

It's again a reminder that actually carrying out covert opsec is really hard, because humans and organisations abhor randomness, and you can therefore find the sequences that reveals the hidden details.


## [Reckless campaign of cyber attacks by Russian military intelligence service exposed - NCSC Site](https://www.ncsc.gov.uk/news/reckless-campaign-cyber-attacks-russian-military-intelligence-service-exposed)

[https://www.ncsc.gov.uk/news/reckless-campaign-cyber-attacks-russian-military-intelligence-service-exposed](https://www.ncsc.gov.uk/news/reckless-campaign-cyber-attacks-russian-military-intelligence-service-exposed)

> The National Cyber Security Centre (NCSC) has identified that a number of cyber actors widely known to have been conducting cyber attacks around the world are, in fact, the GRU.  These attacks have been conducted in flagrant violation of international law, have affected citizens in a large number of countries, including Russia, and have cost national economies millions of pounds.
> 
> Cyber attacks orchestrated by the GRU have attempted to undermine international sporting institution WADA, disrupt transport systems in Ukraine, destabilise democracies and target businesses.
> 
> This campaign by the GRU shows that it is working in secret to undermine international law and international institutions.


Strong words, and worth reading, as is the [technical advisory](https://www.ncsc.gov.uk/alerts/indicators-compromise-malware-used-apt28) that came with it.

Additionally, while you are reading this and eating popcorn, you should read the [thread of the announcement](https://threadreaderapp.com/thread/1047787912945979392.html), and [the text of the US press] announcement(https://recapd.com/w-fdd7bd/) where they announce they are going to indict seven russian military officers.

Not a whole lot to actually say about this really.  This is a strong united move by the US, UK and Holland, and we can only wait to see what happens next.


## [Conservative Party conference app reveals MPs' numbers - BBC News](https://www.bbc.co.uk/news/uk-politics-45693143)

[https://www.bbc.co.uk/news/uk-politics-45693143](https://www.bbc.co.uk/news/uk-politics-45693143)

> The Guardian's Dawn Foster, who is attending the conference, tweeted about the security breach and said she had been able to access the former foreign secretary's personal details, including his mobile phone number.
> 
> She shared a redacted picture of Mr Johnson's profile, which did not reveal his phone number.
> 
> It appears that people could access an MP's personal details by entering their email address, without a password, when pressing the attendee's button in the app.


This breach was embaressing all around, but I want to focus on two things here.

The first is that Dawn Foster here, I think literally posted a picture of herself breaching the Computer Misuse Act.  She noticed the vulnerability, and then conciously exploited it, gaining access to someone else's information.  And she took a screenshot and tweeted it.  We train journalists on court proceedings and contempt of court, but not on the computer misuse act?

Secondly, there's an ethical question here about whether it's ethical to tweet the mechanism of a vulnerability.  As a journalist, she had her story, she had her screenshots, she could have contacted CCHQ and told them about the vulnerability, and then published once the app was taken down or fixed.  

By choosing to explain exactly how to find the vulnerability, she chose to endanger the personal data of people in that application, and that's exactly what the "crowd" then did.

The defense here is that the vulnerability was so simple that actually you didn't need to tell anyone how to do it, it was obvious and clear, and pointing out the obvious and clear isn't any form of recklessness nor an ethical breach, in fact it would be an ethical breach not to point it out.

All in all this was just an awful showing all round


## [Domain flub leaves 30 million customers high and dry – Naked Security](https://nakedsecurity.sophos.com/2018/09/26/domain-flub-leaves-30-million-customers-high-and-dry/)

[https://nakedsecurity.sophos.com/2018/09/26/domain-flub-leaves-30-million-customers-high-and-dry/](https://nakedsecurity.sophos.com/2018/09/26/domain-flub-leaves-30-million-customers-high-and-dry/)

> In a blog post explaining the incident, Vembu alleged that this was the result of an automated script rather than a human decision, calling out TierraNet for not consulting further with it.
> 
> Somehow this automated algorithm decided to shut down the Zoho domain based on these 3 cases – without prior warning of the shutdown, or investigation into the traffic supported by this domain.
> 
> While Vembu has been actively apologizing to customers and calling out TierraNet on Twitter, the domain registrar did not reciprocate on social media. Its own Twitter account was last updated almost a year ago. It consists mostly of messages acknowledging its own service outages from 2015 and 2017.


I've talked before about the dangers of Machine Learning and AI in cybersecurity.  This is exactly the sort of totally sane, automated response that can happen when we let algorithms make decisions.

I searched high and low for anything from TierraNet, but their blog hasn't been updated since 2014, and their twitter account hasn't said anything since 2017.

I had assumed there was more to this story, that Zoho had been flagged for a lot more spam than the 3 that they claimed to have received, which is still I suspect the truth, but there's no data to back that up, other than [hacker news postings](https://news.ycombinator.com/item?id=18059792) pointing out how much recent spam they'd received from Zoho domains.

This also serves to remind us of the reliance we have on a few critical suppliers.  If your hosting, DNS, SSL Cert provider pulled the plug, what would you do?


## [California cracks down on Internet of Crap passwords with new law to stop the botnets • The Register](https://www.theregister.co.uk/2018/10/04/california_iot_password/)

[https://www.theregister.co.uk/2018/10/04/california_iot_password/](https://www.theregister.co.uk/2018/10/04/california_iot_password/)

> The new law is intended to deal with one of the more common routes to mass infection: default or hardcoded passwords.
> 
> It is much easier and simpler for a manufacturer of, say, security cameras to have a single password on all their devices and prod users to change it. But, with depressing predictability, most consumers don't bother – they just fire up their device, connect it to their wireless and leave it be. That leaves the device – multiplied by millions – wide open to attack.
> 
> Manufacturers know this, and they know the answer is to give each device its own unique password, but many still don't bother because it costs money and once the device is out their hands, it is not longer their responsibility.
> 
> The law changes that to a degree, without adding extra liability, by requiring that manufacturers either include "a preprogrammed password unique to each device manufactured" or "a security feature that requires a user to generate a new means of authentication before access is granted to the device for the first time."
> 
> It will kick in on January 1, 2020 and will "require a manufacturer of a connected device… to equip the device with a reasonable security feature or features that are appropriate to the nature and function of the device… and designed to protect the device and any information contained therein from unauthorized access, destruction, use, modification, or disclosure, as specified."


It will be interesting to see how much of an impact this offers.  The law is scoped to devices manufactured or sold within California, but does not constrain electronic stores, gateways or marketplaces, so ebay or amazon can sell devices that aren't compliant.

More worryingly, the act includes language to exclude any connected devices that are subject to security requirements under _"federal law, regulations or guidance promulgated by a federal agency pursuant to it's regulatory enforcement authority"_.  Which means that Government devices won't be covered, and anybody who claims to be reading guidance from federal authorities could be exempt.

This is a good start though, and hopefully will lead to some similar guidance or market regulation in other countries as well.  As the register says, we know that simple obvious admin passwords are a clear own goal, and requiring either a password unique to the machine, or even better, to have a password required to be set upon boot/reset gives us a much better internet


## [They’re Drinking Your Milkshake: CTA’s Joint Analysis on Illicit Cryptocurrency Mining - Cyber Threat Alliance : Cyber Threat Alliance](https://www.cyberthreatalliance.org/joint-analysis-on-illicit-cryptocurrency-mining/)

[https://www.cyberthreatalliance.org/joint-analysis-on-illicit-cryptocurrency-mining/](https://www.cyberthreatalliance.org/joint-analysis-on-illicit-cryptocurrency-mining/)

> CTA members are seeing an enormous increase in illicit mining activity targeting their customers. Activity has gone from a virtually non-exist issue to one that almost universally shows up at the top of our members’ threat lists. Combined data from several CTA members shows a 459 percent increase in illicit cryptocurrency mining malware detections since 2017. Recent quarterly trend reports from CTA members show that this rapid growth shows no signs of slowing down. If 2017 was defined by the threat of ransomware, 2018 has been dominated by illicit cryptocurrency mining.
> 
> For many, this may not seem like an important issue. What difference does it make if someone is stealing my computing power to mine cryptocurrencies? However, illicit mining is the “canary in the coal mine” of cybersecurity threats. If illicit cryptocurrency mining is taking place on your network, then you most likely have worse problems and we should consider the future of illicit mining as a strategic threat. More sophisticated actors could use – or may already by using – that same access to lay the groundwork for you to have a really bad day.


This is a huge increase in targeted attacks, and as the blogpost says, if someone has the ability to put a coin mining script onto your service, whether backend or potentially worse, frontend; then they have the ability to do far worse if they wanted to.

It's interesting to me that there's such a rise in this, it indicates that economically speaking, the blackhat hacker community sees more value in abusing stolen credentials and site takeovers for CPU mining than they do for the value of stealing the data on those systems.  The report says that it's due to the rise in value in the coin markets, but I wonder if there is a collapse in the value of personal data because of how much is out there, the actions of police forces to crackdown on dark markets where it can be sold?

If the bitcoin markets collapsed, I wonder if this activity would go away, and what would replace it?

Equally, I'd expect the next step to move from hacked websites and credentials into coinhive scripts being injected into software chain dependencies.  Some analysis on your dependencies to determine if they are running any coin mining might be interesting to consider in a build pipeline at the moment


## [On the Hunt for FIN7: Pursuing an Enigmatic and Evasive Global Criminal Operation « On the Hunt for FIN7: Pursuing an Enigmatic and Evasive Global Criminal Operation | FireEye Inc](https://www.fireeye.com/blog/threat-research/2018/08/fin7-pursuing-an-enigmatic-and-evasive-global-criminal-operation.html)

[https://www.fireeye.com/blog/threat-research/2018/08/fin7-pursuing-an-enigmatic-and-evasive-global-criminal-operation.html](https://www.fireeye.com/blog/threat-research/2018/08/fin7-pursuing-an-enigmatic-and-evasive-global-criminal-operation.html)

> We have identified job advertisements for Combi Security that have been posted on popular Russian, Ukrainian, and Uzbek job recruitment sites, as well as numerous individuals who most likely worked for the company. Due to the seeming legitimacy of the recruitment postings, some individuals may have been unaware of illicit nature of their work. 
> 
> While the recruitment of unwitting individuals as puppets has been a common component of at least some criminal schemes – for example, reshipping mules who are recruited through postings on career sites advertising attractive work-from-home jobs – FIN7’s veiling of full-scale financial compromises as legitimate offensive security engagements is particularly notable. 
> 
> The apparent success of Combi Security in recruiting unsuspecting individuals in this manner, may lead to more of this type of technical recruitment by cyber criminals in the future.


This is a great analysis of an advanced threat actor, who actually exhibited great technical skill, coming up with some novel obfuscation techniques.

The fact that it turns out that they literally advertised jobs, through a front company, and potentially got unwitting developers to work for them on some of these technical innovations is quite scary.  Do you know who you work for?

There's an interesting grey line in the infosec community, and it makes me wonder about the CTF's, coding challenges and so forth, and whether these are being mined for new and novel techniques for advanced actors.


## [Product updates based on your feedback](https://www.blog.google/products/chrome/product-updates-based-your-feedback/)

[https://www.blog.google/products/chrome/product-updates-based-your-feedback/](https://www.blog.google/products/chrome/product-updates-based-your-feedback/)

> The new UI reminds users which Google Account is signed in. Importantly, this allows us to better help users who share a single device (for example, a family computer). Over the years, we’ve received feedback from users on shared devices that they were confused about Chrome’s sign-in state. We think these UI changes help prevent users from inadvertently performing searches or navigating to websites that could be saved to a different user’s synced account.
> 
> We’ve heard—and appreciate—your feedback. We’re going to make a few updates in the next release of Chrome (Version 70, released mid-October) to better communicate our changes and offer more control over the experience.


This was a poor decision on Google's part, and I don't think this rowing back is anywhere near good enough.

Google's vision of a single account for everything is very nice, and I appreciate it, but it does lead towards this confusion for users. I've signed into my browser, what does that actually mean?  Have I just identified myself to it, or is it syncing all my browser history into Google's datacenters?

I personally choose to trust Google and sync my browser data, but I do so being at least moderately aware of what they do with that, and choosing the privacy tradeoff as worth it for the ability to see what tabs were open on another laptop or phone.  I use exactly that feature to move from laptop to laptop, mac to Qubes, Qubes to iPad as I compose this newsletter, and it's very helpful.

But as can be seen from the Facebook story on phone numbers, it's often not clear within an organisation as to why data was being captured, and a team 2 years down the line might start using my Chrome browsing data to drive other recommendations, and I'm not sure that it's clear to all users what that means.


## [Facebook Is Giving Advertisers Access to Your Shadow Contact Information](https://www.eff.org/deeplinks/2018/09/you-gave-facebook-your-number-security-they-used-it-ads)

[https://www.eff.org/deeplinks/2018/09/you-gave-facebook-your-number-security-they-used-it-ads](https://www.eff.org/deeplinks/2018/09/you-gave-facebook-your-number-security-they-used-it-ads)

> One of the many ways that ads get in front of your eyeballs on Facebook and Instagram is that the social networking giant lets an advertiser upload a list of phone numbers or email addresses it has on file; it will then put an ad in front of accounts associated with that contact information. A clothing retailer can put an ad for a dress in the Instagram feeds of women who have purchased from them before, a politician can place Facebook ads in front of anyone on his mailing list, or a casino can offer deals to the email addresses of people suspected of having a gambling addiction. Facebook calls this a “custom audience.”


Oh dear, another facebook issue.  This one is a bit more subtle, and I want to raise two issues.

The first is that Facebook are not doing good segmentation of the their data.  A phone number I give to Facebook for security purposes should never make it into the advertising bucket.  I can totally see how this might have happened, again complex systems are hard!  But GDPR makes this clearer, each piece of data that is gathered should be gathered under a specific form of consent, and your database is going to need to start to model that soon, because over time, you'll change your consent form, you'll change where you get data from etc.

This is going to hit companies again and again, because people haven't been doing this in the past.  Repeat after me, personal data is like toxic waste, keep it safe and secure and away from as much of your system as possible.

Secondly, what on earth is facebook doing, offering advertisers a way to upload "phone numbers they wish to target ads at" and then serving ads that way.  I can't think of any good reason to enable this, and it is only going to worry users.  Any company that has a contact list of people who purchased from them before should be contacting them direct, and passing that list to Facebook is probably not acceptable under GDPR either.

I really can't think of a reason that Facebook should be offering that service to advertisers, when they can offer significantly better targeting options to advertises that should be worth more.  This just feels creepy and a great way to target ads in a stalker-like fashion.


## [Security Update | Facebook Newsroom](https://newsroom.fb.com/news/2018/09/security-update/)

[https://newsroom.fb.com/news/2018/09/security-update/](https://newsroom.fb.com/news/2018/09/security-update/)

> First: View As is a privacy feature that lets people see what their own profile looks like to someone else. View As should be a view-only interface. However, for one type of composer (the box that lets you post content to Facebook) — specifically the version that enables people to wish their friends happy birthday — View As incorrectly provided the opportunity to post a video.
> 
> Second: A new version of our video uploader (the interface that would be presented as a result of the first bug), introduced in July 2017, incorrectly generated an access token that had the permissions of the Facebook mobile app.
> 
> Third: When the video uploader appeared as part of View As, it generated the access token not for you as the viewer, but for the user that you were looking up.
> 
> 


There's lots about this vulnerability, all over the web this week, and it's a good example of a bad vulnerability.

This shows how complex systems can create uncertain behaviours, because it's very hard to model how lots of simple systems interacting will actually behave.  In fact, complexity theory tells us that it's probably impossible to model for a real _"complex system"_.

But to me, the interesting thing here is none of that.  It's how GDPR is going to change reporting of bugs like this.

Facebook was required to notify the ICO in Ireland (the primary GDPR enforcer for Facebook in Europe), within 72 hours of discovering the breach, thanks to GDPR.  They therefore published the information about the breach at the same time, which seems like a good idea on the face of it.

But with a breach this size, and this complex, it's very very hard to know which accounts were affected and whether there was any deliberate malicious abuse of the feature.  

We know there was some, because Facebook's account says that they noticed this because of unusual traffic patterns to the view as feature.  But that 50 million accounts?  It's easy for reporters to jump on that and accuse nations, or malicious actors of massive campaigns to attack peoples accounts, but we don't actually know if this was weaponised or used.  Facebook simply hasn't had time to do this analysis.

Now, I'm all for timely release of breach information, there have been multiple breaches in recent memory where organisations took months or even years to reveal that there was a breach.  But I think it might require a change in journalistic behaviour, and an acknowledgement that far more often the answer to the questions we all want to know about the breach will be "We don't know yet", and that this is ok.

Journalism doesn't have a great memory, the old adages about the news cycle lasting 24 hours is pretty accurate, and that means that we are unlikely to see the increased and better information coming out weeks or months later when Facebook or whoever is breached next, tells us an update.


