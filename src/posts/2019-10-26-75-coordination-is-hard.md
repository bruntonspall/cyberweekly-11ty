---
title: "75 - Coordination is hard"
date: 2019-10-26
description: "In big organisations, or across nation states, coordination is really hard."
permalink: /coordination-is-hard/
---

In big organisations, or across nation states, coordination is really hard.

It can be difficult to know who to talk to, who to send issues or problems to, and how to know whether your report is being actioned.

We blame users a lot for not using our systems right, for not telling us when they get a phishing email, for clicking on the wrong links, but do we make it easy to report such a thing?  Do we even make it obvious who to report it to?  For us, it might be clear that phishing emails are sent over to the Exchange team, but that potential drive by malware alerts should be raised with the IT security team, whereas a report from AWS Guard Duty should be handled by the digital security team.  But for many people in our organisations, they don't know who those teams are, how to contact them or how things are separated up.

While I'm not the biggest fan of service desk software, like ServiceNow!, having a single easy front door for reporting issues, an internal triage or allocation team who can pass onto the right place means that users have a single easy way to raise issues.  This can improve the likelihood of people actually submitting issues, but it comes with a caveat.  As I've written before, [a service desk needs to be a crutch that enables good communication](https://medium.com/@bruntonspall/the-tyranny-of-the-service-desk-d1bc273b7c13), but doesn't get in the way of other communication mechanisms.  If someone approaches you directly, your team should never respond with "Have you raised a ticket for that?", but instead need to respond politely, helpfully, and probably also raise a ticket on their behalf.  

Secondly, when a ticket or issue is raised, it's important that team communication is kept clear, simple and speedy.  A cyber security consultancy team that gets a question might not know the answer immediately, but could respond with something like "We don't know the answer right now, we are consulting with some of our colleagues and will get back to you within 24 hours".  Internally teams should be able to discuss questions on an internal mailing list, disagreeing with one another and helping educate one another, and then the team can respond formally after they have some internal consensus on the right advice or action to take. 

This should work at the national level as well, as I've pointed out below, inter agency coordination is poor, and there are often not clear single government departments you should contact about something.  Having clear front doors for citizens to contact, and being able to route those queries internally, while giving the citizen feedback that their query or report is valuable and being dealt with will encourage people to report more often, and provide us with better information on what is really happening out there.

## [Face the fax: CIA phasing out hardware for secure email](https://www.fifthdomain.com/it-networks/2019/10/03/face-the-fax-cia-phasing-out-hardware-for-secure-email/)

[https://www.fifthdomain.com/it-networks/2019/10/03/face-the-fax-cia-phasing-out-hardware-for-secure-email/](https://www.fifthdomain.com/it-networks/2019/10/03/face-the-fax-cia-phasing-out-hardware-for-secure-email/)

> The Central Intelligence Agency wants to make it easier to communicate with industry — so it’s upgrading to email.
> 
> Speaking Oct. 2 at the VMware Public Sector Innovation Summit in Arlington, Virginia, CIA chief information officer Juliane Gallina said that the CIA was looking to replace its fax machines with email in a program called “Gray Magic.”
> 
> “It’s a new network; it’s secure and it’s designed specifically to allow industry partners to have their own secure, direct communications in collaboration with government to help us facilitate acquisitions and procurement," Gallina said.


What year is this again?


## [Google accused of spying with new tool that flags large employee meetings - The Verge](https://www.theverge.com/2019/10/23/20929524/google-surveillance-tool-accused-employee-activism-protests-union-organizing)

[https://www.theverge.com/2019/10/23/20929524/google-surveillance-tool-accused-employee-activism-protests-union-organizing](https://www.theverge.com/2019/10/23/20929524/google-surveillance-tool-accused-employee-activism-protests-union-organizing)

> The accusation, outlined in a memo obtained by Bloomberg News, claims severe unethical conduct from high-ranking Google employees, who they say allegedly ordered a team to develop a Chrome browser extension that would be installed on all employee machines and used primarily to monitor internal employee activity. Employees are claiming the tool reports anyone who creates a calendar invite and sends it to more than 100 others, alleging that it is an attempt to crackdown on organizing and employee activism.
> 
> “These claims about the operation and purpose of this extension are categorically false. This is a pop-up reminder that asks people to be mindful before auto-adding a meeting to the calendars of large numbers of employees,” a company spokesperson tells Bloomberg.


Is it easier, inside Google, to create a chrome browser extension to add a popup to Google Calendar than it is to actually add such a feature directly to Google Calendar?

Calendar has been a dearth of innovation for such a long time, and sadly, the companies that start developing better calendars get bought and shutdown.  


## [Statement of Intent regarding the security of the Internet of Things](https://www.gov.uk/government/publications/five-country-ministerial-communique/statement-of-intent-regarding-the-security-of-the-internet-of-things)

[https://www.gov.uk/government/publications/five-country-ministerial-communique/statement-of-intent-regarding-the-security-of-the-internet-of-things](https://www.gov.uk/government/publications/five-country-ministerial-communique/statement-of-intent-regarding-the-security-of-the-internet-of-things)

> ...the undersigned [Five Eyes](https://en.wikipedia.org/wiki/Five_Eyes) partner nations agree to:
> 
> 1) Collaborate with respective industry and standards bodies to provide better protection to users by advocating that devices should be secured by design.
> 2) Actively seek out opportunities to enhance trust and raise awareness of security safeguards associated with loT devices in our respective nations.
> a. Identify and engage industry partners who share Five Eyes’ goals to enhance the security ofloT.
> b. Identify and engage likeminded nations to encourage international alignment on IoT security, unlocking innovation that builds a strong economy that works for everyone.
> 3) Share information with Five Eyes partners in a timely manner through appropriate channels and arrangements, consistent with international and domestic law, to aid in the overall improvement of loT security.


(Joel) This certainly isn't new given NCSC and DCMS have been working on [IoT Secure by Design](https://www.gov.uk/government/collections/secure-by-design) for some time however it is always nice to see the work formalised and re-committed to as time ticks on.

As IoT devices continue to embed themselves into our lives whether in the home or surrounding us through 'smart cities' I see the future of human-interactive technology being led by 'biohacking' and this even closer alignment between humans and technology (from tools and gadgets to how we live/feel) will bring deeper and more material risks that will hinge on good technology-focus information security (ala 'cyber security').

We already see this biological relationship between human and machine from remote-controllable pace makers and prosthetics through to PlatoWork from [Plato Science](https://platoscience.com/).


## [Smart Spies: Alexa and Google Home expose users to vishing and eavesdropping – Security Research Labs](https://srlabs.de/bites/smart-spies/)

[https://srlabs.de/bites/smart-spies/](https://srlabs.de/bites/smart-spies/)

> 1. Create a seemingly innocent application that includes an intent triggered by “start” which takes the next words as slot values (variable user input that is forwarded to the application). This intent behaves like the fallback intent.
> 
> 2. Amazon or Google review the security of the voice app before it is published. We change the functionality after this review, which does not prompt a second round review. In particular, we change the welcome message to a fake error message, making the user think the application has not started. (“This skill is currently not available in your country.”) Now the user assumes that the voice app is no longer listening.
> 
> 3. Add an arbitrary long audio pause after the error message by making the voice app “say” the character sequence “�. “ (U+D801, dot, space). Since this sequence is unpronounceable the speaker remains silent while active. Making the app “say” the characters multiple times increases the length of this silence.
> 
> 4. Finally, end the silence after a while and play a phishing message. (“An important security update is available for your device. Please say start update followed by your password.”). Anything the user says after “start” is send to the hacker’s backend. That’s because the intent, which acted like the fallback intent before, now saves the user input for the password as a slot value.


This is an interesting piece of research, but has been many very poor journalistic takes on it with headlines like ("Alexa and Google Home abused to eavesdrop and phish passwords")[https://arstechnica.com/information-technology/2019/10/alexa-and-google-home-abused-to-eavesdrop-and-phish-passwords/].  This is not about any malware actually stealing passwords or listening to conversations. 

The issue here is the same as in any appstore, updates get far less security review than original submissions.  In this case, the skill was updated after release, which bypassed the security review.  

Secondly, it's worth noting that this is unlikely to work against a real person.  If my Alexa asked for my password, I would be very confused and completely unable to say it out loud.  How does one say "Capital Z, lowercase y, three, Carat symbol, lowercase r etc".  

This was research to prove that it is possible rather than active exploitation, and while not great that there are flaws in the security processes in voice assistants, this is not anything to write terrifying headlines about.


## [Getting A Grip: Special Report on the AWS Special Report – Alan Mather – In The Eye Of The Storm](https://digitalstorm.blog/2019/10/23/getting-a-grip-special-report-on-the-aws-special-report/)

[https://digitalstorm.blog/2019/10/23/getting-a-grip-special-report-on-the-aws-special-report/](https://digitalstorm.blog/2019/10/23/getting-a-grip-special-report-on-the-aws-special-report/)

> When the move to cloud started, government was still clinging to the idea that its data somehow needed protection beyond that used by banks, supermarkets and retailers. There was a vast industry propping up the IL3 / Restricted classification (where perhaps 75-80% of government data sat, mostly emails asking “what’s for lunch?”). This classification made cloud practically impossible – IL3 data could not sit on the same servers or storage as lower (or higher) classified data, it needed to be in the UK andsecured in data centres that Tom Cruise and the rest of the Mission Impossible team couldn’t get into. Let’s not even get into IL4. And, yes, I recognise that the use of IL3 and IL4 in regards to data isn’t quite right, but it was by far the most used way of referring to that data.
> 
> Then, in 2014, after some years of work, government made a relatively sudden, and dramatic, switch. 95% of data was “Official” and could be handled with commercial products and security. A small part was “Official Sensitive” which required additional handling controls, but no change in the technical environment.


As the person who wrote some of the data handling guidelines for Government handling Official Sensitive data, I'm glad to note that the author picks up that Official Sensitive data should not require a separate technical environment, but instead ensure that there are some specific controls (specifically, there should be access control lists, and audit logs of who accessed which thing).

Sadly, many Government departments still don't really understand or follow these rules, and instead have "Official Sensitive systems" which just makes me wince.


## [First, Niantic Mapped The World. Now It's Mapping You](https://kotaku.com/the-creators-of-pokemon-go-mapped-the-world-now-theyre-1838974714/amp?__twitter_impression=true)

[https://kotaku.com/the-creators-of-pokemon-go-mapped-the-world-now-theyre-1838974714/amp?__twitter_impression=true](https://kotaku.com/the-creators-of-pokemon-go-mapped-the-world-now-theyre-1838974714/amp?__twitter_impression=true)

> While identifying an individual player’s routines might tell you a lot about their life, oftentimes looking at deviations from that routine can be more revealing. Another player, Laszlo, usually wakes up between 7 and 8 a.m. in his house in a tree-lined neighborhood on the Buda side of Budapest. At around 9:30, he travels to work, always in a vehicle, always passing a Starbucks where he “could catch at least three creatures every time.” (Niantic says that while Pokémon will appear more frequently near Pokestops and Gyms, they do not appear more frequently near sponsored locations.)
> 
> However, on one particular Monday, Laszlo deviated from his predicted path and visited a pharmacy near a shopping mall. While the rest of his day is unremarkable, in the evening, instead of taking his usual midnight stroll to the soccer fields, Laszlo’s data went dark until the morning.
> 
> Kotaku asked Laszlo if he had been sick that day. He laughed. “The pattern is that I usually walk my dogs quite late to that sports complex… and I have two kids… so it happens quite often that I have to buy nasal drops from that pharmacy when they get a cold,” he said. In itself, this deviation was not a juicy revelation. However, it’s hard to imagine that Niantic, with all of its location intelligence, doesn’t have records of players traveling to revealing locations that they might not want others to know about.


What I always find interesting about privacy advocates is that they show what is possible with the data that organisations capture.  But they never look at data in bulk, and try to work out how easy or hard it would be to find that information out at scale.  Humans are very very good at pattern recognition, so looking at where someone went and seeing that they stopped at a pharmacy and making the deductive leap that they or someone in their life was ill is easy for a human.  But writing an algorithm to look for that is really hard.

Niantic come out of this report reasonably well, they don't share data generally, they generate reports for individual customers, such as a series of malls, and tell them aggregate statistics, like number of unique visitors and so on, but instead of trying to anonymise the data and share anonymised data, which is almost always hard to do without leaving the ability to de-anonymise the data, they just provide the summary data.

Of more interest to privacy advocates are the sheer number of games and apps that also request your location data, and it's one of the reasons that iOS 13 now tells you when an app is asking for your location data.  People can understand why Niantic or Google Maps wants your location data, but not why some random Sodoku app might be asking for it, and can generally tell nefarious asks from reasonable asks.


## [BBC News launches 'dark web' Tor mirror - BBC News](https://www.bbc.co.uk/news/technology-50150981)

[https://www.bbc.co.uk/news/technology-50150981](https://www.bbc.co.uk/news/technology-50150981)

> The BBC World Service's news content is now available on the Tor network to audiences who live in countries where BBC News is being blocked or restricted. This is in line with the BBC World Service mission to provide trusted news around the world.


(Joel) ["The Onion Router" or 'Tor'](https://en.wikipedia.org/wiki/Tor_%28anonymity_network%29) is an open-source anonymous communication network that seeks to obfuscate what the user is doing (typically through the Tor Browser) and who that user is.

Tor is relied on every day for a range of purposes but one of the key use-cases is bypassing local censorship and user monitoring in order to consume and express unmodified information with anonymity.

While they have used the older Onion specification (v2 that uses 16 character addresses, SHA1 and RSA 2014 instead v3), the BBC's move to publish the news site on Tor reduces the burden on the Tor network in giving users access to BBC News content while making a clear statement that it seeks to provide uncensored reporting to any global Internet user.

(Michael) This is a welcome move by the BBC, who have a long history of british government/western propaganda broadcasts such as the world service and involvement in the free radio broadcasts into countries where the press is not free to criticise the Government.  As more and more citizens get their news online, they need restriction free access to such "free news" and TOR is increasingly the standard way to do that.  

Of course TOR is made better by the presence of more traffic.  If only spies used TOR, it would be easy to spot them, but if you can get citizens in a target country to use more and more TOR, then your covert uses are harder to spot.

I just wish that the BBC wouldn't call it the "Dark Web", because for too many people that implies criminality and has undertones of illegitimacy for many readers.


## [Equifax used 'admin' as username and password for sensitive data: lawsuit](https://finance.yahoo.com/news/equifax-password-username-admin-lawsuit-201118316.html)

[https://finance.yahoo.com/news/equifax-password-username-admin-lawsuit-201118316.html](https://finance.yahoo.com/news/equifax-password-username-admin-lawsuit-201118316.html)

> Equifax (EFX) used the word “admin” as both password and username for a portal that contained sensitive information, according to a class action lawsuit filed in federal court in the Northern District of Georgia.
> [...]
> The lawsuit also notes that Equifax admitted using unencrypted servers to store the sensitive personal information and had it as a public-facing website.
> [...]
> The lawsuit was filed by people who bought shares of Equifax between Feb. 25, 2016 and Sept. 15, 2017. In September 2017 Equifax announced a data breach that exposed the personal information of 147 million people. The company settled with the FTC for $425 million in September 2019.


(Joel) The class-action consolidated 373 previous individual lawsuits into one. The interesting difference here is that this isn't a lawsuit from data subjects, but by shareholders who believe Equifax simply didn't disclose it's cyber security practices, and associated risks.

I'd argue they have a point, with admin/admin left active on important systems.

A Federal Trade Commission (FTC) fine of $425 million for the exposure of 147 million people's personal data is $2.89 USD per person (this isn't the compensation amount, but what the perceived value of the personal data is). Astonishingly low.


## [Report: Travel Reservations Platform Leaks US Government Personnel Data | vpnMentor](https://www.vpnmentor.com/blog/us-travel-military-leak/)

[https://www.vpnmentor.com/blog/us-travel-military-leak/](https://www.vpnmentor.com/blog/us-travel-military-leak/)

> ...breach in a database belonging to Autoclerk, a reservations management system owned by Best Western Hotels and Resorts Group. Connected to various travel and hospitality-related platforms online, the exposed database posed a risk to many parties.
> [...]
> One of the platforms exposed in the database was a contractor of the US government, military, and DHS. The contractor manages the travel arrangements of US government and military personnel, as well as independent contractors working with American defense and security agencies.
> 
> The leak exposed the personally identifying information (PII) of personnel and their travel arrangements. Our team viewed logs for US army generals traveling to Moscow, Tel Aviv, and many more destinations. We also found their email address, phone numbers, and other sensitive personal data.


(Joel) To say this breach is horrific would be an understatement. Taking just the US government/military perspective, this is a significant material breach in operational security through supply chain. From materials audit through to contract cancellations, the associated parties are in for a fun ride.

vpnMentor's recommendations for how this could have been avoided boils down (yet again) to basic cyber security hygiene:
1. Secure your servers.
2. Implement proper access rules.
3. Never leave a system that doesn’t require authentication open to the internet.

(Michael) You'll note from the NCSC Annual Report that Travel systems are listed as one of the critical national infrastructure systems that NCSC aids.  However, if you read between the lines, it's clear that this covers the government provided information systems that travel companies are required to use such as the advanced passenger information system.  If a small hotel chain or even a large one wanted advice on how to secure their data, I suspect they would be quite far down the list.  This sort of breach should remind us that the supply chain is vast and very difficult to effectively secure, and the size of the challenge for nations is on how to fix everything at once, rather than just the bits that are considered "Government"


## [The NCSC Annual Review 2019 - NCSC](https://www.ncsc.gov.uk/news/annual-review-2019)

[https://www.ncsc.gov.uk/news/annual-review-2019](https://www.ncsc.gov.uk/news/annual-review-2019)

> This review of the NCSC's third year looks back on the developments and highlights between the 1st September 2018 to 31st August 2019. As well as interviews and data, you will also hear from people working inside the organisation at the heart of the NCSC's mission: to make the UK the safest place to live and work online.


Over 600 major incidents handled, support provided to almost 900 organisations and lots of other statistics.

One of the things I noted was that some organisations are using the statistics to claim that Government is the most hacked.  I think it's clearer to say that Government is number 1 in the incident response list because they have the most attention from NCSC.  A friend remarked that one of the companies that had an NCSC incident response plan probably would have struggled to get even 5 minutes of advice work from them before the incident happened.

However, regardless of the efficacy, we can see that this model of defensive organisation works for wider engagement, and we are already seeing the model being copied in the US and Australia and likely to see it spread further.


## [Police response to cyber-dependent crime is generally good, but it can be inconsistent, finds Inspectorate - HMICFRS](https://www.justiceinspectorates.gov.uk/hmicfrs/news/news-feed/police-response-cyber-dependent-crime-generally-good/)

[https://www.justiceinspectorates.gov.uk/hmicfrs/news/news-feed/police-response-cyber-dependent-crime-generally-good/](https://www.justiceinspectorates.gov.uk/hmicfrs/news/news-feed/police-response-cyber-dependent-crime-generally-good/)

> Victims who report cyber-dependent crime are generally satisfied with the service they receive, but there is still confusion about the central reporting process
> 
> Whether victims are given good advice on protecting themselves from further cyber-dependent attacks varies depending on who they contact.
> 
> They are often given confusing and misleading advice about how (or whether) their case will be investigated and, if it is, how it is progressing


As the report says:
> Having 43 forces operating independently does not provide an effective response to cyber-dependent crime

People are unsure how to report cyber enabled crime to their local police force, unclear how that is joined up across police forces, and get poor progression reports.  That discourages people from reporting more crime, which results in the government having less data on the activity of criminal groups.


## [Inside the shutdown of the ‘world’s largest’ child sex abuse website – TechCrunch](https://techcrunch.com/2019/10/16/dark-web-hacker-group-government/amp/?__twitter_impression=true)

[https://techcrunch.com/2019/10/16/dark-web-hacker-group-government/amp/?__twitter_impression=true](https://techcrunch.com/2019/10/16/dark-web-hacker-group-government/amp/?__twitter_impression=true)

> Yes, it was right to report the information to the authorities, so long as I protected my source. Protecting your sources is one of the cardinal rules of journalism, but my source was a hacker group — it was not the dark web site itself. After all, I was working under the assumption that the authorities would not care much for the source information anyway.
> 
> I reached out to a contact at the FBI, who passed me on to a special agent at a field office. After a brief phone call, I emailed the four IP addresses slated to be the dark web site’s real-world location, and the list of the thousand alleged users of the site.
> 
> [...]
> I reached out to the federal agent this morning, and was told the FBI was not involved in the investigation. The Internal Revenue Service’s Criminal Investigation division, which investigates and prosecutes financial crimes, and the Homeland Security Investigations unit, which largely deals with human smuggling, child trafficking and related computer crimes, were credited with the work.
> 
> While authorities from the U.K. and South Korea contributed to the investigation, sources say the IRS received an anonymous tip that kickstarted it.
> 
> From there, the IRS used technology to trace bitcoin transactions, which the dark web site used to profit from the child exploitation videos. Users would have to pay in bitcoin to download content or upload their own child exploitation videos. The government also launched a civil forfeiture case to seize the bitcoins allegedly used by 24 individuals in five countries who are accused of funding the site.


This is a horrific story, and I'm glad that united work across a number of states has resulted in taking this down and arresting people.

But this is is one of the biggest problems of Government.  A reporter tried to report this much earlier, and decided to pass onto the FBI.  But the investigation, if it existed at the time was being run by the IRS, and so the information wasn't passed on.

How often does this happen?  How often is information given to the FBI, or Department for Homeland Security, or some other part of Government?

In the UK, you can report SMS phishing to Action Fraud, to HMRC, to Netcraft, to NCSC, to the Met Police, to your phone provider among others.  Who is actually responsible for joining all of this up and ensuring that we have a consistent view of such reports?


