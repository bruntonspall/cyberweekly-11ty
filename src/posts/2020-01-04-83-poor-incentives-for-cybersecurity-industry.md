---
title: "83 - Poor incentives for cybersecurity industry"
date: 2020-01-04
description: "Welcome back for the first newsletter in 2020."
permalink: /poor-incentives-for-cybersecurity-industry/
---

Welcome back for the first newsletter in 2020.

I took a few weeks off for christmas and new year while I recovered from my visit to Australia.  Several weeks of conferences really can take it out of you it turns out.

One of things that I've noticed over the last few years of writing this newsletter is just how poorly the incentives work for many cybersecurity companies.  If you build malware detection tools, and find malware, find the command and control infrastructure, you would be commercially worse off if you take down the C2 infrastructure, because people using your tools are protected, but the ones being infected are the potential customers you might be able to sell your tools to.

Of course, further to this, it's entirely unclear who actually should be taking down this infrastructure when it is found.  If it's all inside a single country, one can look at existing policing efforts, although most internal police forces are not computer aware enough to actually deal with cybercrime in that way.  But worse, because of the global nature of the internet, almost all of this stuff ends up crossing national borders.  Should government agencies be the ones responsible?  If so which agencies?  Is it policing? intelligence and security?  national security? 

This lack of good incentives to actually clean up the mess means that it is easy for criminals to operate at large across the world.  Providing they are careful to not annoy the local police forces, and not big enough to draw attention of the international policing efforts they can continue as they wish.  Until we can sort out these elements and provide strong industry and government interventions, we'll still see the creation and distribution of ransomware, phishing and other attack vectors to be highly profitable and generally low risk for many criminals out there.

## [How Canada's military reacted to seeing Pokemon Go players trespassing on its bases](https://www.cbc.ca/amp/1.5393774?__twitter_impression=true)

[https://www.cbc.ca/amp/1.5393774?__twitter_impression=true](https://www.cbc.ca/amp/1.5393774?__twitter_impression=true)

> Most of the emails expressed curiosity and confusion about the new game.
> 
> "Plse advise the Commissionaires that apparently Fort Frontenac is both a PokeGym and a PokeStop. I will be completely honest in that I have not idea what that is," wrote Maj. Jeff Monaghan at CFB Kingston. 
> 
> "The game's premise seems to be going to the 'PokeStops/Gyms' to collect 'Pokemon's' (we should almost hire a 12-year-old to help us out with this) of which we were able to find 5 of these things on the range road itself," wrote security expert David Levenick at CFB Borden, Ont., 100 kilometres northwest of Toronto.
> 
> "There's a game out there taking off like gangbusters, and it requires people to move to digitally cached locations to get points, etc.," wrote Lieut. Col. Richard Raymond at CFB Petawawa, west of Ottawa. 
> 
> Eight days after Pokemon Go launched, the military police in Canada issued a criminal intelligence advisory.
> 
> The notice was sent to all military police officers. It said: "It has been discovered that several locations within DND/CAF establishments are host to game landmarks (PokeStops and Gyms) and its mythical digital creatures (Pokemon)."


I've heard that this was a problem world-wide, that with the launch of Pokemon Go, people tried to get into a variety of secure places just to claim the gyms.  Niantic were quite responsive in taking down certain gyms and pokestops when this was bought to their attention, but what I really love about this story that came out from the Canadians, was the desire to move the pokestop to the middle of the museum in order to increase the number of visitors.


## [Sodinokibi: The Crown Prince of Ransomware](https://www.cybereason.com/blog/the-sodinokibi-ransomware-attack)

[https://www.cybereason.com/blog/the-sodinokibi-ransomware-attack](https://www.cybereason.com/blog/the-sodinokibi-ransomware-attack)

> When first discovered in late April, Sodinokibi (AKA, Sodin and REvil) was reported as being installed on machines by exploiting an Oracle WebLogic vulnerability (CVE-2019-2725) and subsequently started propagating through exploit kits and spam. 
> 
> In this blog post, we perform a deep technical analysis of the Sodinokibi ransomware, focusing on the ransomware delivery method as well as the defensive mechanisms put in place by the malware authors in order to evade AV detection. 
> 
> This malware showcases a resurgence of ransomware we have been tracking in the industry. Though some have reported ransomware attacks decreasing, we are seeing that ransomware is here to stay. In fact, ransomware attack payments have doubled in the second quarter of this year. Organizations need security products that are able to defend against the latest attacks in order to stay on top and detect and prevent successfully.
> 
> During our analysis, we have noticed interesting similarities between the GandCrab ransomware, whose operators claimed in June 2019 that they are retiring and discontinuing their operation. Our findings bode well with other reports by other security researchers that also found similarities between the two ransomware.


GandCrab ransomware was one of the most prevalent strains of ransomware, and it looks like Sodinokibi or REvil is out to take that crown.  

Generally, GandCrab was being spread not by a single operator, but because it was being packaged as part of a "Ransomware as a Service" site, where you could go and setup an account, get a custom build that included your bitcoin address, and the service would manage the Command and Control, handle bitcoin payments and decryption keys, and take a slice of the profits.  

The real questions for me from this report are:

1. Is the ransomware as a service back? or is this a single operator?

2. This malware variant has no lateral movement capability according to this breakdown.  Whereas most stories about this ransomware shows it spreading from machine to machine.  Does that mean that this isn't the real ransomware, or is it being used a second stage after something else has actually got onto the machines and spread around?


## [No, Spotify, you shouldn’t have sent mysterious USB drives to journalists – TechCrunch](https://techcrunch.com/2019/12/23/spotify-usb-drives-journalists/amp/)

[https://techcrunch.com/2019/12/23/spotify-usb-drives-journalists/amp/](https://techcrunch.com/2019/12/23/spotify-usb-drives-journalists/amp/)

> Last week, Spotify sent a number of USB drives to reporters with a note: “Play me.”
> 
> It’s not uncommon for reporters to receive USB drives in the post. Companies distribute USB drives all the time, including at tech conferences, often containing promotional materials or large files, such as videos that would otherwise be difficult to get into as many hands as possible.
> 
> But anyone with basic security training under their hat — which here at TechCrunch we have — will know to never plug in a USB drive without taking some precautions first.


I suspect that this worked, that a lot of journalists put the device into their work laptop, and then were told "you've been hacked".  I doubt that it was good marketing, because I expect most journalists affected would have been irritated or annoyed (not an emotion you want in someone writing about your upcoming show).

However it also doesn't prove anything.  Journalists often receive marketing materials by USB stick, often unannounced, and it is their very job to open them and read them.  It wouldn't matter if you emailed a PDF to them that did the same thing, their very day to day existence is reliant on carrying out these actions.  Furthermore, this USB stick didn't have any malware, didn't attempt to carry out any breach of the device (doing so would have been a breach of the computer misuse act in the UK) so it therefore figures that it might have been scanned before it came in, and checked by anti-malware software on the device, or that the journalists devices were fully patched and not easily hacked this way.  This false equivalence just encourages the journalists to write about fear, uncertainty and doubt about how easy it is to get hacked.


## [Travelex Knocked Offline by System-Wide Malware Attack | Threatpost](https://threatpost.com/travelex-knocked-offline-malware-attack/151522/)

[https://threatpost.com/travelex-knocked-offline-malware-attack/151522/](https://threatpost.com/travelex-knocked-offline-malware-attack/151522/)

> A “computer virus” has forced foreign currency exchange giant Travelex to shut down its online services and its app – leaving its retail locations to carry out tasks manually and many customers stranded without travel money. Its global banking partners have also been left adrift with no way to buy or sell foreign currency.
> 
> Travelex, a ubiquitous fixture at airports, provides foreign-exchange services in 70 countries across more than 1,200 retail branches. On Thursday, it tweeted out a short statement confirming a malware attack on New Year’s Eve which, as of this writing, is still impacting its ability to operate. It did not, however, provide technical specifics.
> 
> The attack has had ripple effects as well, affecting banking partners like Sainsbury’s Bank, Barclays, HSBC, Tesco Bank and others. The latter, for instance, said that its bureau-de-change services were offline until further notice because of the Travelex incident. Also, firms that use its services cannot participate in the foreign currency markets at all, for now.


This sounds like a bad ransomware attack of some form.  The biggest issue here is that they whitelabel their travel exchange business for other companies such as Sainsbury's Bank, Tesco Bank and so on, meaning that those companies are also affected by the loss of service.

Having been down several days already, this is likely to drag on as they attempt to recover their network and systems.


## [Microsoft Security Intelligence Report](https://www.microsoft.com/securityinsights/Driveby)

[https://www.microsoft.com/securityinsights/Driveby](https://www.microsoft.com/securityinsights/Driveby)

> Drive-by downloads can be hosted on legitimate websites. Attackers gain access to legitimate sites through intrusion or by posting malicious code to a poorly secured web form, like a comment field on a blog. It can be difficult for even an experienced user to identify a compromised site from a list of search results. More advanced drive-by download campaigns can also install ransomware or even cryptocurrency mining software on a victim machine.
> 
> The graph and map on the right show the monthly average volume of drive-by download pages detected for every 1,000 pages indexed by Bing (search engine) for the timeframe and country/countries selected. Toggle between Worldwide and Country Comparison for a detailed view of the countries you’ve selected.


There a lot of useless statistics in this report.  A lot of the stuff by country mostly matches the amount of compute access in the given country, so for example Cloud Outgoing Attacks show you the countries in which Azure has hosting infrastructure and I suspect the usage ratios are around the same (that would have been a useful comparison though for example).

However some of the statistics are really interesting.  For example, Ransomware has a 0.04% encounter rate worldwide, with the uk having 0.01% encounter rate, means that there is an approximate 1/10,000 chance of one of you machines encountering ransomware in a given month.  That allows us to actually start to account for the likelihood of a given risk.

Now, I don't think the statistics are as simple as that, we don't know how the numbers are gathered, what an "encounter" is defined as, and whether that's per company or when 1000 computers in a single company get done,is that 1000 encounters.

But starting to put, even finger in the air, estimates onto risks helps us to start to understand them better than watching the news (which always overstates the risks of the most interesting sounding ones)


## [The Empire (3.0) Strikes Back](https://www.bc-security.org/post/the-empire-3-0-strikes-back)

[https://www.bc-security.org/post/the-empire-3-0-strikes-back](https://www.bc-security.org/post/the-empire-3-0-strikes-back)

> Moving forward, we plan to make regular updates as new research is published. We believe that Powershell and Empire framework will remain a major threat vector employed by APTs, malware authors, and Red Teams. When we conduct an assessment, we think that companies are best served when we emulate the primary attacks that they face rather than employing the latest and greatest offensive evasion tactics. That being said, we recognize that Powershell may no longer be the most effective attack vector in terms of evasion, but represents a credible and realistic threat.


The Empire framework is used by real attackers out there, and it's been udpated with a bunch of new capabilities.

Of course, there is a debate about whether such tools should be released and available to anybody to download, but while the tool is available to all attackers, it merely emulates the capabilities of the really high level attackers.  If your teams can spot and defend against this tool, then they are robbing the most powerful APTs of their time and budget since they have to use their technical expertise to go further.


## ['Shattered': Inside the secret battle to save America's undercover spies in the digital age](https://news.yahoo.com/shattered-inside-the-secret-battle-to-save-americas-undercover-spies-in-the-digital-age-100029026.html?guccounter=2&guce_referrer=aHR0cHM6Ly9jeWJlcndlZWtseS5uZXQvYWRtaW4vcmVhZGluZ2xpc3Q&guce_referrer_sig=AQAAADcPw8r5YdoTK0v12A09LGUfEJx5DcJ7PGoFE7Qbx_awkuqMS7ahmvEdAHigTFYkusxMn-86hIXR7fDUlHvJ5xGXSc3ST-GnANSrZSoupKZKwRwlKdcMNS1KjTb-g0wLm1Ghdxenn7CCldVENK8lK1HY1PFYQXwfof5fVwqm25wQ)

[https://news.yahoo.com/shattered-inside-the-secret-battle-to-save-americas-undercover-spies-in-the-digital-age-100029026.html?guccounter=2&guce_referrer=aHR0cHM6Ly9jeWJlcndlZWtseS5uZXQvYWRtaW4vcmVhZGluZ2xpc3Q&guce_referrer_sig=AQAAADcPw8r5YdoTK0v12A09LGUfEJx5DcJ7PGoFE7Qbx_awkuqMS7ahmvEdAHigTFYkusxMn-86hIXR7fDUlHvJ5xGXSc3ST-GnANSrZSoupKZKwRwlKdcMNS1KjTb-g0wLm1Ghdxenn7CCldVENK8lK1HY1PFYQXwfof5fVwqm25wQ](https://news.yahoo.com/shattered-inside-the-secret-battle-to-save-americas-undercover-spies-in-the-digital-age-100029026.html?guccounter=2&guce_referrer=aHR0cHM6Ly9jeWJlcndlZWtseS5uZXQvYWRtaW4vcmVhZGluZ2xpc3Q&guce_referrer_sig=AQAAADcPw8r5YdoTK0v12A09LGUfEJx5DcJ7PGoFE7Qbx_awkuqMS7ahmvEdAHigTFYkusxMn-86hIXR7fDUlHvJ5xGXSc3ST-GnANSrZSoupKZKwRwlKdcMNS1KjTb-g0wLm1Ghdxenn7CCldVENK8lK1HY1PFYQXwfof5fVwqm25wQ)

> The game was changing for undercover officers and their assets. “It’s extremely difficult now to run cover operations when so much is known and can be known about almost everybody,” says Joel Brenner, a former top counterintelligence official. “Now you show up at the border of Russia, they’ve got your high school yearbook out there where you wrote about your lifelong ambitions to work for the CIA. All that stuff is digitized.”
> 
> America’s adversaries were also forced to adapt. By the early 2010s, Chinese intelligence operatives started adopting old-school Russian-style tradecraft, like dead drops in the woods or “brush passes,” which involve surreptitiously exchanging objects in a public place, says one former senior intelligence official. “It was unheard of for the Chinese,” says this person. “The conclusion was that they felt the world was too digital and traceable.” 


The rapid change in digital over the decade or so has made life unbelievably hard for undercover spies operating in foreign countries.  What only a few decades ago was a fairly easy, if labour intensive job, of creating a new legend or cover has become nearly impossible due to the growth of biometric data gathering (such as CCTV, facial recognition at the border, finger print systems) which are much harder to fake. 

Additionally, you can't create a false digital trail without the cooperation of private companies, and of course the CIA would really rather not send over a list of new cover identities to Twitter or Facebook.  But going back and creating those identities and a history of interactions and social friendships is therefore impossible, and that can cause someone to stand out among their other 20 something peers, even in the diplomatic corps, who use these tools to stay in touch with their friends and family while posted abroad.


## [The Year of the Phish - Nex](https://nex.sx/blog/2019/12/15/the-year-of-the-phish.html)

[https://nex.sx/blog/2019/12/15/the-year-of-the-phish.html](https://nex.sx/blog/2019/12/15/the-year-of-the-phish.html)

> Because phishing is such a dominant threat for the targeted groups I normally work with, I have been working over the last years on a number of tools and services to mitigate and respond to such attacks. While I will hopefully share more details about some of those in the future, I decided to release now a 25GB archive of data on the latest 100’000 phishing sites one of my systems processed. This archive contains a SQLite database with a list of original URLs retrieved from various feeds (such as OpenPhish, PhishTank, PhishStats and others), the final URL it eventually redirected to, as well as the DOM HTML and a screenshot of the page.


This is a lovely resource for defenders and infosec educators.  Looking at the sorts of phishing sites that are put up, how accurate they are, and to use in showing people what they can look like and how phishing is done.  This is a great resource for demonstrating to executives and non-infosec people what real phishing looks like and how it is carried out


## [Why Ring Doorbells Perfectly Exemplify the IoT Security Crisis | WIRED](https://www.wired.com/story/ring-hacks-exemplify-iot-security-crisis/)

[https://www.wired.com/story/ring-hacks-exemplify-iot-security-crisis/](https://www.wired.com/story/ring-hacks-exemplify-iot-security-crisis/)

> And as Motherboard first showed, there are tools available online for breaking into Ring accounts by strategically guessing the login credentials. When account thieves record enough juicy audio from people's Ring feeds, there's even a podcast where they can broadcast it.
> 
> Though it sounds shocking, the situation with Ring is far from unique. At the beginning of the year, for example, hackers launched similar attacks against Nest cameras, complete with incidents where hackers were creepily talking to children through the devices. The manufacturers behind these devices—Amazon and Google, respectively—are both billion-dollar tech giants with massive development resources. The fact that their cameras regularly feature in these kinds of cases reflects a broader industry failure to produce trustworthy internet-of-things devices that are easy for consumers to set up in a secure and private way.
> 
> "We have ways of preventing attacks like this," says Ang Cui, founder of the IoT analysis and security firm Red Balloon. "We've been thinking about securely allowing people to access computers remotely for decades. So if we insist on making our doorbells a computer that connects to the internet, then we have to put the same level of care into securing those computers."


While we are being warned by Google and Microsoft that password reuse is a real problem, Ring, under the auspices of Amazon are building networked kit that needs a password to access remotely and are not requiring 2FA or some other access control by default.  There needs to be more work in ensuring that devices, especially ones with significant privacy concerns (I'm far more worried about a camera or voice recorder or lock than I am a lightbulb or thermostat) must be secure by default, meaning that random others on the internet should not be able to get into them easily.


## [Protecting users from government-backed hacking and disinformation](https://www.blog.google/technology/safety-security/threat-analysis-group/protecting-users-government-backed-hacking-and-disinformation/)

[https://www.blog.google/technology/safety-security/threat-analysis-group/protecting-users-government-backed-hacking-and-disinformation/](https://www.blog.google/technology/safety-security/threat-analysis-group/protecting-users-government-backed-hacking-and-disinformation/)

> We’ve had a long-standing policy to send users warnings if we detect that they are the subject of state-sponsored phishing attempts, and have posted periodically about these before. From July to September 2019, we sent more than 12,000 warnings to users in 149 countries that they were targeted by government-backed attackers. This is consistent (+/-10%) with the number of warnings sent in the same period of 2018 and 2017.
> 
> 
> Over 90 percent of these users were targeted via “credential phishing emails” similar to the example below. These are usually attempts to obtain the target’s password or other account credentials to hijack their account. We encourage high-risk users—like journalists, human rights activists, and political campaigns—to enroll in our Advanced Protection Program (APP), which utilizes hardware security keys and provides the strongest protections available against phishing and account hijackings. APP is designed specifically for the highest-risk accounts.


Nothing particularly new here, credential stuffing, reused passwords are still the favoured attack methodology even of the high capability attackers.  And most of those will be stymied by a hardware security key because they want remote access rather than compromising the targets machine.


## [Inside ‘Evil Corp,’ a $100M Cybercrime Menace — Krebs on Security](https://krebsonsecurity.com/2019/12/inside-evil-corp-a-100m-cybercrime-menace/#more-49835)

[https://krebsonsecurity.com/2019/12/inside-evil-corp-a-100m-cybercrime-menace/#more-49835](https://krebsonsecurity.com/2019/12/inside-evil-corp-a-100m-cybercrime-menace/#more-49835)

> When it came time to transfer stolen funds, the recruiters would send a message through the mule site saying something like: “Good morning [mule name here]. Our client — XYZ Corp. — is sending you some money today. Please visit your bank now and withdraw this payment in cash, and then wire the funds in equal payments — minus your commission — to these three individuals in Eastern Europe.”
> 
> Only, in every case the company mentioned as the “client” was in fact a small business whose payroll accounts they’d already hacked into.
> 
> Here’s where it got interesting. Each of these mule recruitment sites had the same security weakness: Anyone could register, and after logging in any user could view messages sent to and from all other users simply by changing a number in the browser’s address bar. As a result, it was trivial to automate the retrieval of messages sent to every money mule registered across dozens of these fake company sites.
> 
> So, each day for several years my morning routine went as follows: Make a pot of coffee; shuffle over to the computer and view the messages Aqua and his co-conspirators had sent to their money mules over the previous 12-24 hours; look up the victim company names in Google; pick up the phone to warn each that they were in the process of being robbed by the Russian Cyber Mob.


I'm curious here, was Brian Krebs unable to tell anyone working with the Treasury or FBI about this pattern that he had noticed, so that a better form of takedown or infrastructure analysis could be done?

I guess the question would be who could he actually tell?   It's entirely unclear whose jurisdiction this kind of intelligence would be in.  It's not really a national security thing, but because it's international foreign actors, it's not precisely a homeland thing.  This was the point of setting up something like CISA in the US, or NCSC in the UK, but it's still unclear what actions they can legitimately take to prevent these attacks (as compared to say, watching the attackers coordinate their attacks and gaining intelligence from that)


