---
title: "92 - What justifies lawful interception"
date: 2020-03-08
description: "You may have seen the [\"interesting\" video about backdoors from Huawei this week](https://twitter.com/Huawei/status/1235128718869164032?s=20), which has been widely panned as company based propaganda.  However it does raise an interesting point (and referencing the story from last week), that legally mandated lawful interception points are also backdoors into systems."
permalink: /what-justifies-lawful-interception/
---

You may have seen the ["interesting" video about backdoors from Huawei this week](https://twitter.com/Huawei/status/1235128718869164032?s=20), which has been widely panned as company based propaganda.  However it does raise an interesting point (and referencing the story from last week), that legally mandated lawful interception points are also backdoors into systems.

But in reality, there are a lot of bad people on the internet, and even democratic societies have mechanisms for ensuring that police are able to restrict or reduce the liberty of an individual because they seek harm or reduction of liberty of another individual.  Different western societies have very different models for what balance is the right balance of restrictions on personal liberties versus the need of the state to ensure a safe environment for the many.  This can be a sticky political point for many people, with people drawing different decisions about where they think these rules should lie.

In the physical realm, very few UK people believe that physical search warrants issued by a judge are not a legally acceptable mechanism for controlling the polices ability to search a property or person.  The controls require a level of reasonable suspicion and the very physical nature tends to prevent large scale dragnets of search.  In the cyber realm, the physical restrictions are lifted, but the principles still apply.  People generally require policing to require a level of reasonable suspicion in order to search their digital life.

Ian Levy and Crispin Robbins wrote about this back in [Principles for a More Informed Exceptional Access Debate](https://www.lawfareblog.com/principles-more-informed-exceptional-access-debate)

> There is no single solution to enable all lawful access, but we definitely don’t want governments to have access to a global key that can unlock any user’s data. Government controlled global key escrow systems would be a catastrophically dumb solution in these cases. Furthermore, solutions should be designed so the service provider—in the form of a real human—is involved in enacting every authorized request, limiting the scale of use.

The clear principle set out here is that global unfettered access is not wanted, and that instead there should be a process within Government for creating an authorised request, and a process within service providers for validating that request.

Of course, the corollary to this is that service providers may discover illegal content and behaviour of their users through their normal mechanism.  At that point, should they report it to the authorities without requiring the duly authorised warrant?  The story about how Apple engages with law enforcement for cases of child abuse imagery might point at how some of that stuff works.  Just because law enforcement has a minimum bar for service providers behaviour, requiring warrants etc, there is nothing to stop a service provider being more compliant if they feel that it is within their company ethos to do so.

Secondly, the question of how and whether law enforcement gets a second bite of the apple is an interesting one.  The Google case below shows that law enforcement ask for non-personally identifiable information in order to potentially identify devices that they wish to investigate further.  

I think a lot of the problems of this stuff comes from the lack of transparency by authorities.  Publishing statistics on searches conducted, %-age hit rates and outcomes would give us a lot more confidence in the systems.  We don't want a world where there is a 100% suspicion to arrest rate, because there will always be random situations that look suspicious to outsiders, but we want to see that there is a required high chance of converting a hunch into an actual lead in order to justify the intrusion into peoples civil liberties.  Obviously, investigators don't want to tip their hand about certain investigations, but if searches are being conducted to find regular criminals such as burglars, then the worries about those criminals monitoring issued warrants to see if they are discovered don't really hold water for me.

Two editorial notes as well this week.  I've deliberately chosen not to feature any stories about COVID-19.  There's enough disinformation floating around, and I simply don't know enough to be able to sift good information from bad.  There's a few things that I've noted that I may go back to once the concern and hype settles down, but I'm not going to cover it in here until I'm sure and confident that I won't add to confusion online.

Secondly, you may notice that I've moved from Saturday mornings to Sunday mornings.  Looking at my statistics, about 50% of you read the newsletter over the weekend, and the other 50% of you read this Monday/Tuesday morning.  It's slightly easier for me to find time to prep the newsletter if I can write some on Saturday and Sunday morning than it is preparing on a Friday, but if this is affecting your Saturday morning routine, do let me know, and if there's enough feedback, I'll change it back.

## [I Accidentally Uncovered a Nationwide Scam on Airbnb](https://www.vice.com/en_us/article/43k7z3/nationwide-fake-host-scam-on-airbnb?utm_campaign=sharebutton)

[https://www.vice.com/en_us/article/43k7z3/nationwide-fake-host-scam-on-airbnb?utm_campaign=sharebutton](https://www.vice.com/en_us/article/43k7z3/nationwide-fake-host-scam-on-airbnb?utm_campaign=sharebutton)

> NoneAirbnb’s Community Standards state that no host should “provide inaccurate information,” but Airbnb does not rigorously police the request, according to the report. “In spite of the fact that Danielle and Lexi received a verified ID, badge on their profile page, we have no way of knowing if they had any role in the properties other than having their photo taken,” the report stated. “This case also undermines one of the cornerstones of AirBnB’s business model, namely that the company’s ratings and identity verification system are a viable means by which travelers can vet their prospective hosts.”
> 
> James Elmendorf, a senior policy analyst at LAANE, told me that Airbnb’s weak verification process created the opportunity for those who were willing to exploit the platform through the creation of “faux, just-like-you personas.”
> 
> “Airbnb does no checking up on this whatsoever,” said Elmendorf. “They’re one of the most sophisticated companies in the world, and you’re telling me they can’t come up with a system that prevents this? Airbnb is doing that hand-wavy thing that tech companies do where they say, ‘We can’t solve this.' If they wanted to solve it, they would figure it out.”


Fraudsters are going to fraud, but ("reintermediation")[https://themarketingagenda.com/2017/07/30/uber-vs-deliveroo-disintermediation-vs-reintermediation/] companies, like eBay, AirBnB, Uber and Deliveroo make their profits by maximising the number of sellers on one hand, and the number of buyers on the other hand.  

Fraud vectors for these companies come from both sides, buyers who claim that their intermediated service was not correctly delivered or up to specification, and from sellers who claim that they provided services that they didn't.  Without laws or regulation (or a sense of ethics or market force for ethical behaviour), there are very few incentives for the intermediary to get involved in sorting out fraud on either side.  As long as they can claim that their business services are for introducing parties and not actually owning the transaction, they wont sort out the fraud issues on either side. 


## [Positive Technologies - learn and secure : Intel x86 Root of Trust: loss of trust](http://blog.ptsecurity.com/2020/03/intelx86-root-of-trust-loss-of-trust.html?m=1)

[http://blog.ptsecurity.com/2020/03/intelx86-root-of-trust-loss-of-trust.html?m=1](http://blog.ptsecurity.com/2020/03/intelx86-root-of-trust-loss-of-trust.html?m=1)

> And since the ROM vulnerability allows seizing control of code execution before the hardware key generation mechanism in the SKS is locked, and the ROM vulnerability cannot be fixed, we believe that extracting this key is only a matter of time. When this happens, utter chaos will reign. Hardware IDs will be forged, digital content will be extracted, and data from encrypted hard disks will be decrypted.


This sounds bad. Admittedly I don’t really know enough about hardware and ROM’s to be certain that this isn’t another story similar to the Bloomberg Supermicro story that’s massively overblown. 

But lots of systems and especially “zero trust” systems are dependant on a root of trust that can be held securely in the client device. This article says that soft TPM’s will be affected and not all hardware has a hardware TPM yet so it may well create a risk that malware can breach that root of trust and the whole house of cards falls down. 

However, don’t panic. The details aren’t released yet and we don’t know the cost of carrying out the attack and wether it’ll be a class of attacks (I get the key and can write software for any laptop I want) or whether the attack will require specific and expensive work per machine. 


## [The CIA Hacking Group (APT-C-39) Conducts Cyber-Espionage Operation on China's Critical Industries for 11 Years - 360 核心安全技术博客](http://blogs.360.cn/post/APT-C-39_CIA_EN.html)

[http://blogs.360.cn/post/APT-C-39_CIA_EN.html](http://blogs.360.cn/post/APT-C-39_CIA_EN.html)

> It is worth noting that the attacked information technology sectors of civil aviation by the CIA are not only in China, but also involves hundreds of commercial airlines national states. So, what is the purpose of this movement?
> 
> In fact, long-term and targeted intelligence-gathering with careful strategic deployment and large amount of resource investment are common activities of CIA.
> 
> We speculate that in the past eleven years of infiltration attacks, CIA may have already grasped the most classified business information of China, even of many other countries in the world. It does not even rule out the possibility that now CIA is able to track down the real-time global flight status, passenger information, trade freight and other related information. If the guess is true, what unexpected things will CIA do if it has such confidential and important information? Get important figures‘ travel itinerary, and then pose political threats, or military suppression?
> 
> [...]
> 
> Evidence 3: Before the Vault 7 cyber weapon was disclosed by WikiLeaks, the APT-C-39 already used relevant cyber weapons against targets in China
> 
> For example, at the beginning of 2010, the APT-C-39 has used the Fluxwire backdoor in the Vault 7 cyber weapon in cyber-attack activities in China, which is much earlier than the Vault 7 leaks. This further confirms the source of these cyberweapons. After in-depth analysis and decryption of the version in the Fluxwire backdoor in the Vault 7, Qihoo 360 statistically classified the version, attack time, and samples captured by itself that APT-C-39 used to attack targets in China over the years


What was the damage caused by Joshua Schultz leaking the CIA “Vault 7” tools to Wikileaks?  Well it enabled security researchers like 360 Core Security to examine the tools, and then look at attacks on chinese intelligence, state, military and civil industries and clearly make attribution of attacks that they had witnessed.

How do we know that these were attacks actually carried out by the US, and not people who downloaded the wikileaks files and repurposed them?  Well 360 Core Security were able to look back at samples from before the leak and determine their use.

What was the CIA doing?  Well 360 Core Security say they aren’t going to tell us for many of the attacks because of National Security, but they have found evidence that the US was trying to get into (and probably succeeeding) civil aviation IT supply chain.  They speculate that this is in order to get information about real time passenger travel, so they can track the movements of people in China.

If there is enough information in here to stand up, expect the Chinese government over the next year or two to be very vocal, and potentially produce indictments and public attribution for US state run operations.  Traditional diplomacy has a tendency to treat espionage as something to be kept quiet, but the recent escalation in public attribution by the West to be responded with in kind.



## [draft-paine-smart-indicators-of-compromise-00 - Indicators of Compromise (IoCs) and Their Role in Attack Defence](https://tools.ietf.org/html/draft-paine-smart-indicators-of-compromise-00)

[https://tools.ietf.org/html/draft-paine-smart-indicators-of-compromise-00](https://tools.ietf.org/html/draft-paine-smart-indicators-of-compromise-00)

> IoCs are often found initially through manual investigation and then shared at scale so a variety of individuals and organisations can defend themselves.  They can be found in a range of locations, including in networks and at endpoints, but wherever they exist, they need to be made available to security appliances to ensure that they can be deployed quickly and widely.  For IoCs to provide defence-in- depth (see Section 5), which is one of their key strengths, they should be deployed on both the network and on endpoints through solutions that have sufficient privilege to act on them, to cope with different points of failure.


This is a great overview of Indicators of Compromise for those who aren’t in the know, but it also outlines a lot of good thinking about their use and applicability, the sort of stuff that I think people in the know should know, but am frequently disappointed to discover they don’t.

The reference to the pyramid of pain is a good one, and it talks about different classes of indicator and how much pain it is to change for an attacker.  File hashes, for example, are trivial to change for attackers, but fundamental C2 infrastructure and coordination tools is much harder for an attacker to change.

The reasons set out in this document for why you should be paying attention to Indicators of Compromise, and why they should be widely shared, especially through automated mechanisms are well thought through and also come with appropriate warnings about being picky about which indicators you put in your system.  Just blacklisting everything is pointless if the attackers known to use a thing will never target you.


## [Lessons learned on written social engineering attacks – DiabloHorn](https://diablohorn.com/2020/03/04/lessons-learned-on-written-social-engineering-attacks/)

[https://diablohorn.com/2020/03/04/lessons-learned-on-written-social-engineering-attacks/](https://diablohorn.com/2020/03/04/lessons-learned-on-written-social-engineering-attacks/)

>  I was able to identify the phone numbers of some of the people involved, including the CFO. He happened to be on a vacation in a pretty remote location of the world, but not fully isolated, according to the photos posted on social media. I also found his personal gmail and some phone numbers from other people at the finance department. So here is what I did:
> 
> I registered a typosquatting gmail address, or at least similar enough, as the real CFO email. I sent an SMS message to one of the finance people while spoofing the number of the CFO. In the SMS I used a message similar to this one:
> 
> Can you send me document X, I was just called by <name> (ceo) that we messed up and I need to go over it. Have no work laptop, use my gmail <typosquatted address>. There goes the vacation, thx!
> Done, the day after I received the document. 


Some lovely social engineering attacks in here.  It’s a good reminder that many attacks on our infrastructure don’t have to be technical and malware ridden to succeed, all they have to do is take advantage of peoples good nature and willingness to help their colleagues.

Of course, I reserve my opinion about the actual value of said attacks for the majority of attackers.  These kind of attacks make great penetration tests, and your company will fall for them every single time, but they make a tiny tiny proportion of actual attacks on real companies, because most attacks are fundamentally not interested in carrying out this kind of attack.  The primary reason is that they are hard to scale, and require targeting, and most attackers out there today are looking to make money, which they do in bulk, across thousands of targets.


## [Porn, gore, and gambling habits aired in Virgin Media breach | Ars Technica](https://arstechnica.com/information-technology/2020/03/virgin-media-breach-outs-some-customers-porn-gore-and-gambling-habits/)

[https://arstechnica.com/information-technology/2020/03/virgin-media-breach-outs-some-customers-porn-gore-and-gambling-habits/](https://arstechnica.com/information-technology/2020/03/virgin-media-breach-outs-some-customers-porn-gore-and-gambling-habits/)

> Virgin Media said in a post that unauthorized access was to a marketing database that included “limited contact information such as names, home and email addresses, and phone numbers” for about 900,000 subscribers. The company went on to say that the breached database contained no passwords or financial information.
> 
> Despite Virgin Media characterizing the accessed data as limited contact information, the Financial Times and the BBC reported that the compromised database also included details of some 1,100 customers who had used an online form to request that specific websites be blocked or unblocked. Some of those sites offered content involving porn, gambling, and extreme gore videos.
> 
> “The records, seen by the Financial Times, show the website that was being blocked or unblocked linked to the customer names and contact details,” Friday’s FT article said. “In some cases that included parents asking for pornographic sites to be blocked to protect children, and other users requesting the Virgin Media unblock access to niche adult websites.”
> 
> Virgin Media said the breach was the result of the database being incorrectly configured. The Register, citing an email sent to affected customers, reported that the database was left unsecured since at least last April. Virgin Media said the unauthorized access was neither a breach nor a hack but rather was “as a result of the database being incorrectly configured.”


This is particularly poor behaviour from a company that is supposed to be an internet carrier that you trust with all of your data and internet traffic.  Leaving the database without any authentication at all is just shockingly bad.

But the claim here that they weren’t hacked, because there was no authentication to get past is really bad form and I hope the ICO throws the book at them.  The technical difference between a breach, being hacked and someone exploiting a vulnerability might be technical at times, but end users don’t really care.  

If you left your front door unlocked and open, and went out for the day, came back to find your TV gone, would you argue with someone about whether you were burgled or whether someone simply stole from you?  It turns out that burglary is “enters any building or part of a building as a trespasser and with intent to commit any such offence...” (Thanks Greg), so even if you left your door unlocked it’s still burglary.

In this case, they can claim they weren’t hacked, because they left the door unlocked, but in reality everyone is going to call it a hack.  What isn’t clear from the statements so far is whether they simply discovered they left the door unlocked, or whether someone came in and stole anything.  And this is where the physical metaphor breaks down, because you can steal just a copy of everything, and nothing is missing to tell you.  I can almost guarantee that if they didn’t bother putting authentication on the database, they definitely won’t have bothered putting logging on the database to see who got at it.  Therefore we should assume that the data is fully breached by “hackers” who will want to do bad things with the data.


## [2020.02.29 CAA Rechecking Bug - Incidents - Let's Encrypt Community Support](https://community.letsencrypt.org/t/2020-02-29-caa-rechecking-bug/114591/3)

[https://community.letsencrypt.org/t/2020-02-29-caa-rechecking-bug/114591/3](https://community.letsencrypt.org/t/2020-02-29-caa-rechecking-bug/114591/3)

> Since that announcement we have worked with subscribers around the world to replace affected certificates as quickly as possible. More than 1.7 million affected certificates have been replaced in less than 48 hours. We’d like to thank everyone who helped with the effort. Our focus on automation has allowed us, and our subscribers, to make great progress in a short amount of time. We’ve also learned a lot about how we can do even better in the future.
> 
> Unfortunately, we believe it’s likely that more than 1 million certificates will not be replaced before the compliance deadline for revocation is upon us at 2020-03-05 03:00 UTC (9pm U.S. ET tonight). Rather than potentially break so many sites and cause concern for their visitors, we have determined that it is in the best interest of the health of the Internet for us to not revoke those certificates by the deadline.
> 
> Let’s Encrypt only offers certificates with 90 day lifetimes, so potentially affected certificates that we may not revoke will leave the ecosystem relatively quickly.


Let’s encrypt had a bug in their validation software that led to the potential mis-issuence of some 3 milllion certificates.  They originally annoucned that they would revoke them all with a fairly short timeline, but have rowed back on that for a couple of reasons.  The first is that they had only identified a few hundred where the bug actually led to certificates being issued that weren’t in keeping with their guidelines.  More importantly, they found nearly a million certificates where the users were not going to be able to reissue fast enough.

The bug itself is rather niche.  Firstly you need to be using CAA on your domains, and you needed to request a single certificate that spanned multiple domains.  CAA is a special kind of DNS record that says that “we use Certificate Authority X, so only they can issue certificates for this domain”.  So for example, if you were running a system that had multiple customers, so a.foo, b.foo and c.foo, and all 3 had CAA on the subdomain.  When LetsEncrypt issued the certificate, they accidentally checked that a.foo was valid with CAA policies, but not b.foo and c.foo.  

In many cases, all the domains had a valid CAA records that would have checked validly, but since LetsEncrypt hadn’t checked, they had broken the rules.

As LetsEncrypt has said, the potentially million certificates that haven’t been rechecked will all expire within 3 months, and it sounds like they are going to wait a little longer before revoking those certificates, by which time some of them will have automatically renewed and the affected customer set will be smaller.


## [How Apple ‘Intercepts’ And Reads Emails When It Finds Child Abuse](https://www.forbes.com/sites/thomasbrewster/2020/02/11/how-apple-intercepts-and-reads-emails-when-it-finds-child-abuse/#5169f98531c2)

[https://www.forbes.com/sites/thomasbrewster/2020/02/11/how-apple-intercepts-and-reads-emails-when-it-finds-child-abuse/#5169f98531c2](https://www.forbes.com/sites/thomasbrewster/2020/02/11/how-apple-intercepts-and-reads-emails-when-it-finds-child-abuse/#5169f98531c2)

> “When we intercept the email with suspected images, they do not go to the intended recipient. This individual . . . sent eight emails that we intercepted. [Seven] of those emails contained 12 images. All seven emails and images were the same, as was the recipient email address. The other email contained 4 images which were different than the 12 previously mentioned. The intended recipient was the same,” the Apple workers’ comments read.
> 
> “I suspect what happened was he was sending these images to himself and when they didn’t deliver, he sent them again repeatedly. Either that or he got word from the recipient that they did not get delivered.”
> 
> The Apple employee then examined each of these images of suspected child pornography, according to the special agent at the Homeland Security Investigations unit.
> 
> In this case, Apple proved even more useful, providing data on the iCloud user, including his name, address and mobile phone number that the user submitted when he signed up. The government also asked for the contents of the user’s emails, texts, instant messages and “all files and other records stored on iCloud.” A document outlining what further information was retrieved from Apple simply reveals a file on the iCloud account that was sent in early February without revealing what specific data was provided.


iCloud uses hashes to automatically flag images that could be child abuse imagery and delay the delivery until someone can review it.  This seems fine... except that a staff member must look at the images to determine if they count as child abuse imagery.  The (UK) law is normally pretty clear on this, the possession, distribution or viewing of child abuse imagery is illegal, no matter the reason (I'm unsure if US law is the same).

Systems in the UK to do the same thing would fall foul of this law, and indeed law enforcement operatives who are required to work with this stuff fall into two categories.  Those who are given a dispensation from prosecution in order to carry out their jobs, and those who maintain those systems.  In general, the systems administrators are completely forbidden from ever, even accidentally, seeing imagery that is contained on the systems that they manage.  Thats both to protect them from committing a crime while at work, but also a safeguarding issue, as nobody should be exposed to such imagery without good counselling and mental health safeguards around them.

So this seems a little odd to me.  Unless there is something else going on here, someone at Apple has a horrendous job of having to vet all the images caught by these systems and deciding whether it should be reported to law enforcement or not.

(For the record, I have no problem with Apple doing this, and sharing the information with Law Enforcement.  The information handed over is the same that would be requested under a search and seizure warrant based on probable cause, and there's nothing in the reporting to say that they didn't wait for the warrant.)


## [It’s Impossible to Prove Your Laptop Hasn’t Been Hacked. I Spent Two Years Finding Out.](https://medium.com/theintercept/its-impossible-to-prove-your-laptop-hasn-t-been-hacked-i-spent-two-years-finding-out-652202b9d2a9)

[https://medium.com/theintercept/its-impossible-to-prove-your-laptop-hasn-t-been-hacked-i-spent-two-years-finding-out-652202b9d2a9](https://medium.com/theintercept/its-impossible-to-prove-your-laptop-hasn-t-been-hacked-i-spent-two-years-finding-out-652202b9d2a9)

> Over the duration of this experiment, I traveled to Europe three times and domestically in the United States five times (including once to Puerto Rico). I found eight different notices from the Transportation Security Administration informing me that my baggage had been searched. I have no way of knowing how many times it had been searched by other authorities who weren’t kind enough to leave me a note.
> 
> I never caught anyone tampering with this laptop. But the absence of any evidence of tampering — and my obsessive thoughts about the various ways an attacker could have evaded by detection — serve to underline how fraught the process of computer forensics can be. If someone who makes their living securing computers thinks they could have missed a computer infection, what hope is there for the average computer user?


This is an interesting article in the sense of documenting how one might build a system for detecting the modification of a device that is otherwise completely unused.  This is the sort of amateur forensics that can be useful and interesting.  However, it's worth pointing out that Micah was specific about not booting, powering on or using the laptop at any point on his trips.  This model wouldn't work for a device that you actually use on a regular basis.

The other thing from this is a reminder of the level of risk that exists.  If Micah Lee, the technologist working with the Intercept on some of the snowdon leaks, working with Tor, the EFF and various other places, can travel around for 2 years, internationally and nationally, and not have a computer that they keep even booted, let alone interfered with.  Then how likely is it that a member of your staff is going to be subject to a physical hardware attack?  I think this brings the likelihood of evil maid attacks down to practically zero unless you have reason to believe that you will be specific targeted.  As an organisation, implementing all the cool doodads that might protect against physical evil maid attacks are probably a waste of time and budget, not to mention often creating a usability concern with the device.  If you have full disk encryption (specifically to protect against theft and loss) you are probably meeting strong enough requirements for the majority of threat models with that single control alone.


## [Google tracked his bike ride past a burglarized home. That made him a suspect.](https://www.nbcnews.com/news/us-news/google-tracked-his-bike-ride-past-burglarized-home-made-him-n1151761#anchor-Apowerfulnewtool)

[https://www.nbcnews.com/news/us-news/google-tracked-his-bike-ride-past-burglarized-home-made-him-n1151761#anchor-Apowerfulnewtool](https://www.nbcnews.com/news/us-news/google-tracked-his-bike-ride-past-burglarized-home-made-him-n1151761#anchor-Apowerfulnewtool)

> The victim was a 97-year-old woman who told police she was missing several pieces of jewelry, including an engagement ring, worth more than $2,000. Four days after she reported the crime, Gainesville police, looking for leads, went to an Alachua County judge with the warrant for Google.
> 
> In it, they demanded records of all devices using Google services that had been near the woman’s home when the burglary was thought to have taken place. The first batch of data would not include any identifying information. Police would sift through it for devices that seemed suspicious and ask Google for the names of their users.
> 
> Kenyon said police told him that they became particularly interested in McCoy’s device after reviewing the first batch of anonymized data. They didn’t know the identity of the device’s owner, so they returned to Google to ask for more information.


This one’s interesting to me, because I think this really divides law enforcement and privacy people and their views.  To me, I don’t really see the difference between this form of information gathering, and the real world analogy of asking all the neighbours, identifying that a man of a certain build cycled past 3 times at the time of the burglary, and then going to find the cyclist as a potential suspect.

The law enforcement in this case gathered a large collection of people who were in the area, and noticed what they felt was suspicious activity, stuff that might give them reasonable suspicion that they might want to talk to the person and find out more.  It’s not like they got details of every single user who was even nearby, they selected individuals who they felt were particuarly suspicious.

Part of the problem here, and it’s addressed later in the article, is that people don’t trust the police and what they’ll do with that data.  That lack of transparency, and the lack of trust in law enforcement is what drives people to assume the worst about every request to access data.


