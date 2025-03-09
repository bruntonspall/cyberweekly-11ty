---
title: "78 - Enough with the cyber-nonsense"
date: 2019-11-16
description: "Applications that aren’t immune to compromised endpoints; Nation states that want to steal your lunch; System administrators might have built backdoors into your photo backup system."
permalink: /enough-with-the-cyber-nonsense/
---

Applications that aren’t immune to compromised endpoints; Nation states that want to steal your lunch; System administrators might have built backdoors into your photo backup system.

There is an endless stream of what I tend to call cyber nonsense.  Articles and advice from people who should know better, that posit threats well outside most peoples concerns, and suggest that we should all worry about all of them, otherwise the sky will fall.

For some people, this is because they are selling amazing cyber-widgets that claim to block even [generation-V cyber attacks](https://www.checkpoint.com/gen-v-cyber-security/) (I don’t know either), or because they profit when people are afraid.  But for many more people, it’s because as an industry this is just the way that we work.

For example, SMS two-factor authentication defeats 100% of automated account takeover attacks, 99% of bulk phishing attacks and 2/3rds of highly targeted attacks [[source](https://security.googleblog.com/2019/05/new-research-how-effective-is-basic.html)].

That’s a level of protection that far outstrips any other control on the market, any other control that I’ve ever heard of.  Sure, that control will get less effective over time, but for almost every user out there, enabling SMS 2FA is better than not enabling it.

It’s true that Sim swapping attacks are surprisingly easy, that when subject to one, someone can bypass all SMS 2FA that you have, and that TOTP authentications like Authy; Google Authenticator; or Microsoft Authenticator are not vulnerable to that same attack.  But spreading fear that SMS is not sufficiently secure doesn’t help given that it is a technology that has 100% penetration among the approximate 5bn phones (of which only 3.2bn are smart phones).

It’s been a running joke in the UK government security circles for years now that security experts always respond to a question about whether a given thing is secure with “it depends”.  But the problem is that much of the time it really does depend.  Is SMS 2FA secure?  If you are trying to launch nuclear missiles, or [securing £680bn of daily transactions](https://www.bankofengland.co.uk/payment-and-settlement/payment-and-settlement-statistics) then no, it’s not secure enough.  But security advice that starts it depends is often not consumable by individuals.  They don’t possess the security awareness or understanding to determine their risk effectively, and so they just have to go on what security people put out into the world.  

We might think that the advice depends on the situation, but we should also be able to come up with advice that is accurate and useful to anyone, even if it’s not entirely sufficient for everyone.  This advice makes a good security baseline, because in the absence of any other advice, the recipient will be more secure than if they just didn’t take advice at all.

If we continue to spread cyber-nonsense that scares people, that makes them think that they cannot ever be secure from the elite nation state cyber hackers, then they just wont bother with anything.  But if we can give [clear simple actionable advice](https://www.ncsc.gov.uk/collection/top-tips-for-staying-secure-online/activate-two-factor-authentication-on-your-email), that works for most people, we can spend more of our time working with people who need the specialist advice.


## [Notorious hackers claim responsibility for Labour cyber attacks and threaten to target Corbyn's family](https://www.independent.co.uk/news/uk/politics/labour-cyber-attack-lizard-squad-ddos-corbyn-general-election-a9202006.html)

[https://www.independent.co.uk/news/uk/politics/labour-cyber-attack-lizard-squad-ddos-corbyn-general-election-a9202006.html](https://www.independent.co.uk/news/uk/politics/labour-cyber-attack-lizard-squad-ddos-corbyn-general-election-a9202006.html)

> "If Labour do win the election, you can expect the whole of the government and Labour websites to go offline," said the member, who shared screenshots appearing to show a botnet tool used to carry out the DDoS attacks.


(Joel) I'm loathed to give this any more airtime but the news cycle keeps going so here we are. This level of coverage by national press and a political party itself means that even in the wake of an unsuccessful DDoS attack resources/time are being consumed in paying attention to something ultimately benign. This could tell would-be attackers that to gain national attention simply takes a failed effort. Further, gloating about defences could also be taken as a challenge by others to try again.

[I've talked about [Distributed) Denial of Service attacks before](https://medium.com/@joelgsamuel/denial-of-ddos-attack-fud-c568d718ca10), in an attempt to dispel some hype around them. As the size of the initial attack remains undisclosed, I'll just have to speculate that it doesn't meet my personal bar as a DDoS of interest, simply because it was unsuccessful and so short.


## [NordVPN users’ passwords exposed in mass credential-stuffing attacks | Ars Technica](https://arstechnica.com/information-technology/2019/11/nordvpn-users-passwords-exposed-in-mass-credential-stuffing-attacks/)

[https://arstechnica.com/information-technology/2019/11/nordvpn-users-passwords-exposed-in-mass-credential-stuffing-attacks/](https://arstechnica.com/information-technology/2019/11/nordvpn-users-passwords-exposed-in-mass-credential-stuffing-attacks/)

> [...]What’s more, a large number of the email addresses in the list I received weren’t indexed at all by Have I Been Pwned, indicating that some compromised credentials are still leaking into public view.[...]
> 
> These common traits mean that the most likely way these passwords became public is through credential stuffing. That’s the term for attacks that take credentials divulged in one leak to break into other accounts that use the same username and password. Attackers typically use automated scripts to carry out these attacks.
> 
> Shared responsibility
> It’s important for readers to know these lists don’t signal a breach on any NordVPN servers. The lists also don’t indicate that the breach disclosed 11 days ago was worse than the company said it was. Rather, these lists are the result of mistakes both on the part of users and NordVPN. For users, the error is choosing easy-to-guess passwords and using them on multiple sites. Security practitioners almost universally recommend people choose a long, random password that is unique for every account.
> 
> I’d argue that NordVPN shares the bulk of responsibility for the high incidence of compromised accounts on its site. Many services such as Google and Facebook proactively sift through credential lists available on both public sites and the Dark Web. When the sites find credentials that match those of their users, the sites notify the users and require a password reset. The sites increasingly are not allowing users to choose weak passwords in the first place or credentials that have been exposed in online dumps in the past.


This was a bad look for a security product, in that insecure passwords and the large number of them.  But if the emails were not on HIBP, then I feel like a credential stuffing attack is less likely.  While not all breaches are loaded into HIBP, a lot are, and if the majority of the passwords/emails on this list are not in HIBP, then this isn't just a list of accounts copied from one place to another.

Secondly, I can't quite work out the impact of this on an end user.  I don't think given the username and password to the VPN service you can download the private certificates and therefore decrypt the VPN session, in part because I think NordVPN uses Ephemeral Diffie-Helmen with perfect forward secrecy, meaning that it's still not possible to get the session key unless you can compromise one of the two endpoints in the key exchange.

This is a leak of personal data from a security company, but I'm not convinced its quite as damaging as some make out


## [Intelligence’s Accidental Profession](https://www.realcleardefense.com/articles/2019/08/20/intelligences_accidental_profession_114679.html)

[https://www.realcleardefense.com/articles/2019/08/20/intelligences_accidental_profession_114679.html](https://www.realcleardefense.com/articles/2019/08/20/intelligences_accidental_profession_114679.html)

> And while computers surpassed humans at data processing long ago, in an increasingly-automated future, they will be capable of creating and updating compelling narratives, too—providing more information to more users than ever before, all on-demand.
> 
> This will undoubtedly please decision-makers, at least at first. But policymakers are already drowning in data. And while they may think they just want information more quickly, the fact is that more data often leads to worse decisions by reinforcing what cognitive scientists call the illusion of explanatory depth. No, sharp, insightful analysis has always been vital to sound decision-making, and it will only grow more important as the datasphere balloons.


But this essay is a great review on the profession of intelligence analysis.  One of the great myths that intelligence organisations like GCHQ and NSA believe themselves and talk about outwardly is that gathering more information is a goal in and of itself.  The plans to master the internet, and gather ever more signals intelligence mostly just increases the amount of hay in the haystacks that you are searching through.  While in theory it can results in more needles as well, the proportions work against our favour.  Instead of drowning in ever more data, we need better ways to gather analytical reports, insightful analysis backed by good data.  


## [Project Nightingale: Google accesses trove of US patient data | BBC News](https://www.bbc.com/news/technology-50388464)

[https://www.bbc.com/news/technology-50388464](https://www.bbc.com/news/technology-50388464)

> Google has gained access to a huge trove of US patient data - without the need to notify those patients - thanks to a deal with a major health firm.
> 
> Google can access health records, names and addresses without telling patients, according to the Wall Street Journal, which first reported the news. Google said it was "standard practice".
> 
> Among the data the tech giant reportedly has access to under the deal are lab results, diagnoses, records of hospitalisation and dates of birth.
> 
> Neither doctors nor patients need to be told that Google can see this information.
> 
> [In a blog, Google said](https://cloud.google.com/blog/topics/inside-google-cloud/our-partnership-with-ascension) its work with Ascension would adhere to industry-wide regulations, such as the US Health Insurance Portability and Accountability Act of 1996 (HIPAA).


(Joel) Sweet mother of privacy data. I personally find this terrifying, particularly that this can be done without notification or consent (which would also imply no opt-out).

I'll keep this short: data protection legislation is one thing (which the US is in terrible need of, at the federal legislative level) but data acquisition governance is whole other topic when you hit scale.

Time will tell how the use of this data can change, and whether it can be used to increase premiums or deny care under predicted pre-existing condition exclusionary terms (and so on). There is of course some good that can come from this: checks and balances on human decisions, prompts due to automated correlation of symptoms and genetic dispositions etc, but there should be a fairly heavy amount of scepticism and ongoing monitoring in how the use of data changes over time and the consequences of these new automations (particularly the unseen).

(Michael) The optics on this probably look far worse than the reality, maybe, in an optimists view of the world at least.  In reality, Google isn’t one big company with a clear laser focus on single things.  Google’s browser developers have very little to do with the Google Cloud product teams, who probably have very little awareness of what the Google DeepMind team are doing, who probably don’t know what Google News is doing.

It’s understandable that someone in a large medical records system might want to work with some expert AI developers and their cloud system in order to take patient data and start getting insights from it.  That’s exactly what medical research has been, and most people would applaud that.  It’s only when that company is associated with an ad-tech firm, and there’s not good data safeguards that ensure that the data or findings cannot be misused that it starts to get scary.  But the trade off might be worth it.  If someone can apply Google’s unique brand of big data acquisition and analysis to long term health records and provide better diagnostic tools, that might mean people discovering cancer or life threatening illnesses faster.

Of course, I’m often accursed of being a bit overly optimistic about this stuff.  I’m sure that Google has some large repository in which they put lots of data, and someone else might stumble on it and use it in a way that wasn’t intended, or that Google maybe has a strategy of trying to gather health data ([such as fitbit](https://www.wired.com/story/google-fitbit-project-nightingale-antitrust/)) for the entire purpose of gathering and exploiting health data purely for their own commercial reasons.


## [This is Literally Propaganda](https://gru.gq/2019/11/04/nope-this-is-propaganda/)

[https://gru.gq/2019/11/04/nope-this-is-propaganda/](https://gru.gq/2019/11/04/nope-this-is-propaganda/)

> When the Internet finally did arrive, the truly disruptive revolution wasn’t access to information; it was the final unification of all the previous revolutions: the niche audiences and frenetic pace of cable TV news, coupled with the “desktop publishing” democratization of access to audiences, taken to the extreme, where broadcast platforms became essentially free.


A great essay that ruminates on the concept of propaganda and the fact that we tend to overemphasis the “information revolution” as being about the internet rather than about the creation of the printing press and mass printing and literacy.

The problems of fake news have been around for a long time, and as Grugq points out, the issue is not that mass consumption of news is now easier than ever (even though it is), it’s that mass production of news is far easier, and that the ability to disambiguate between high quality news and low quality news is harder than ever with the market forces that drive news publishing in that market.


## [Federal Court Rules Suspicionless Searches of Travelers’ Phones and Laptops Unconstitutional | Electronic Frontier Foundation](https://www.eff.org/press/releases/federal-court-rules-suspicionless-searches-travelers-phones-and-laptops)

[https://www.eff.org/press/releases/federal-court-rules-suspicionless-searches-travelers-phones-and-laptops](https://www.eff.org/press/releases/federal-court-rules-suspicionless-searches-travelers-phones-and-laptops)

> “This ruling significantly advances Fourth Amendment protections for millions of international travelers who enter the United States every year,” said Esha Bhandari, staff attorney with the ACLU’s Speech, Privacy, and Technology Project. “By putting an end to the government’s ability to conduct suspicionless fishing expeditions, the court reaffirms that the border is not a lawless place and that we don’t lose our privacy rights when we travel.”
> 
> [...]
> 
> The district court order puts an end to Customs and Border Control (CBP) and Immigration and Customs Enforcement (ICE) asserted authority to search and seize travelers’ devices for purposes far afield from the enforcement of immigration and customs laws. Border officers must now demonstrate individualized suspicion of illegal contraband before they can search a traveler’s device.


(Joel) I am not a lawyer (IANAL) so it is not clear to me what happens next: will CBP appeal to a higher court and/or is the judgement immediately binding and that CBP must be able to demonstrate (likely perhaps not to the subject, so more of record to a court for any judicial redress at a later date) that individual suspicion was material enough to warrant search.

I haven't been to the US since providing social media information was mandatory and the reported uptick in electronic searches but I have completed [Global Entry](https://www.gov.uk/global-entry-usa) that in theory allows me to cross US customs borders as a US citizen would (self service kiosks) - note, this isn't for everyone as requires quite the application process and a visit to a Global Entry centre that is mainly in the US, although the US embassy in London runs the Global Entry interviews every now and again.

While I am not intending to make a political or national security commentary: this is good progress. The independent authority of the judiciary and the checks and balances offered in judicial redress is an important tenant for personal privacy and we see it at work here.

(Michael) One thing to note is that all of the plaintiffs are US Citizens and that was a consideration in the case.  The ACLU even makes clear that they are referring to “international travellers returning home” which makes me think that this will only be a consideration for US Citizens, and wont affect other international travellers from other countries.


## [Despite Windows BlueKeep exploitation freak-out, no one stepped on the gas with patching, say experts • The Register](https://www.theregister.co.uk/2019/11/11/bluekeep_didnt_boost_patching/)

[https://www.theregister.co.uk/2019/11/11/bluekeep_didnt_boost_patching/](https://www.theregister.co.uk/2019/11/11/bluekeep_didnt_boost_patching/)

> Over the last week or so, reports came that miscreants were lobbing active exploits for BlueKeep at honeypot systems. These attacks were found to be attempts by hackers to infect machines with cryptocoin-mining software and led to a series of media reports urging users to patch their machines now that BlueKeep exploits had arrived in earnest.
> 
> According to SANS, those reports did not do much to get people motivated. The security institute says that the rate of BlueKeep-vulnerable boxes it tracks on Shodan has been on a pretty steady downward slope since May, and the media's rush to sound alarms over active attacks did not change that.


Patches have been out for a while, and despite the noise in the cyber security industry, broadly speaking, people are patching in line with their own patch cycles, slow as that might be.

It’s good that broadly speaking, the number of vulnerable boxes is on a downward slope, that means that people are patching.  On the other hand, this has been going 6 months, the fact that the number isn’t as close to zero as humanly possible is just a bit disappointing.


## [Alexa, Siri, Google Smart Speakers Hacked Via Laser Beam | Threatpost](https://threatpost.com/alexa-siri-google-smart-speakers-hacked-via-laser-beam/149860/)

[https://threatpost.com/alexa-siri-google-smart-speakers-hacked-via-laser-beam/149860/](https://threatpost.com/alexa-siri-google-smart-speakers-hacked-via-laser-beam/149860/)

> The attack, dubbed “light commands,” leverages the design of smart assistants’ microphones. These are called microelectro-mechanical systems (MEMS) microphones, which work by converting sound (voice commands) into electrical signals – but in addition to sound, researchers found that MEMS microphones also react to light being aimed directly at them.
> 
> Researchers said that they were able to launch inaudible commands by shining lasers – from as far as 110 meters, or 360 feet – at the microphones on various popular voice assistants, including Amazon Alexa, Apple Siri, Facebook Portal, and Google Assistant.


Lovely attack but changes almost nothing about the threat model for voice assistants.  

The problem with this wonderful scary reporting is that it never really gets the meat of the problem of security analysis.  It’s nice to find a mechanism for bypassing what someone thinks is a control, such as increasing the range that one can speak to a voice activated assistant, or speaking to one silently.  But that’s simply a control bypass mechanism that bypasses a single security control.  And unless you are an attacker that has a good system for getting some valuable goal, but you are prevented by the security control, it’s mostly meaningless.

It doesn’t matter that someone can shine a laser at my Alexa in my house, because there is almost nothing valuable that someone can do with that attack most of the time.  My personal Alexa devices can play music, tune into the radio and turn the lights on and off.

On the other hand, it’s worth us noting this and not assuming that a voice assistant is secure just because we can manage who can get in and out of a room.  There is value in this research, just not in a lot of the reporting about it.


## [About the "easy to hack" EU Exit: ID Document Check app](https://www.grahamcluley.com/about-the-easy-to-hack-eu-exit-id-document-check-app/)

[https://www.grahamcluley.com/about-the-easy-to-hack-eu-exit-id-document-check-app/](https://www.grahamcluley.com/about-the-easy-to-hack-eu-exit-id-document-check-app/)

> So what the researchers are saying is that if a hacker manages to compromise your smartphone or the app then it could do something malicious…
> 
> Err, isn’t that pretty much the case with all programs and computers? If a hacker already has control of the device or has already compromised the app then all bets are off…
> 
> Now, if the researchers had described a way in which an attacker might be able to remotely compromise the app or meddle with the phone then that would have been interesting. Or if it had been found that the app was sending sensitive data insecurely which could be intercepted then that would have certainly raised an eyebrow.


Sigh.  What’s the actual problem here?  The [original FT article (paywall)](https://www.ft.com/content/8dd7bd46-0636-11ea-9afa-d9e2401fa7ca) more or less says that the app doesn’t do enough to protect against a device that has been already compromised.

This is true it seems, there are some things that the application could do to try to prevent certain types of compromise from affecting it.  It doesn’t attempt to detect if the device is compromised, doesn’t look for debug connections, and doesn’t scan for any indicators of known malware.  Your banking app probably does some of these things, and may well just refuse to run if any of those things are true.

But at the same time, the application is designed to scan a publicly readable RFID token and help you fill in an online form.  If your device was infected, and the app didn’t exist, you’d just do most of that with your browser, and the same exploits would be there.

Could the app be better protected against decompilation and infection?  Probably.  Would it make a difference in the threat model the team is considering?  Only the team knows.  Is that threat model the right threat model?  [It depends](https://www.ncsc.gov.uk/blog-post/please-stop-saying-it-depends)


