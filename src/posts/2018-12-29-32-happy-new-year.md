---
title: "32 - Happy New Year"
date: 2018-12-29
description: "Welcome to CyberWeekly, a weekly roundup of news, articles, long form blog posts and various other miscellania that interests your author, Michael Brunton-Spall."
permalink: /happy-new-year/
---

Welcome to CyberWeekly, a weekly roundup of news, articles, long form blog posts and various other miscellania that interests your author, Michael Brunton-Spall.

Feel free to forward this on to people you think might be interested. If someone forwarded this to you, then you can subscribe to your own copy at [Cyberweekly](https://tinyletter.com/cyberweekly)

Replies to this email come straight to me, so just hit reply to send me feedback, comments or links or tweet it to me [@bruntonspall](https://twitter.com/bruntonspall).

 

*Happy New Year!*

*This is a special edition of CyberWeekly to celebrate reaching the end of 2018 and moving into 2019.  I’ve gone back through all the links I’ve sent in 2018 and tried to select some of the best. If you didn’t subscribe right from the beginning then you would have missed some of these.*

*These are a variety of pieces that I thought were interesting for various reasons, so to make your holiday reading more enjoyable, I’ve tried to categorise them as best as I can, but I’ve tended to link to things throughout the year just because I found them interesting and worth sharing rather than through any plan or strategy.*

*I’ve included the original link, quote and my analysis exactly as it was sent out, so obviously some of it may have dated over time.  It’s a long list of articles, because identifying just the ones I really liked out of all the things I’ve read this year was hard.  But I’ve also selected what I think were the 5 most influential or important posts that I’ve read all year, so if you read nothing else from this newletter, these first 5 are the ones to read.*

*Happy new year and I hope that 2019 is a good one for you.*

*Michael*

# The must read list

*These articles are my links for 2018, the 5 best, or most important things I feel I’ve read this year.*

### [Friction between security and user experience | Decipher](https://duo.com/decipher/why-we-cant-have-nice-things-only-secure-ones)

*"Scolding users and organizations for less than stellar "best practices" in access management assumes that users are ignorant (or negligent). In reality, it's the security side of the relationship ignoring how painful it can be. Telling users to turn every security feature on without tackling the friction users have to experience makes security adoption even less likely. We need to look at security as a flow, as a process, and not as a set of unrelated instances or events." *

This is so important. Security teams discussing the use of things like multi-factor authenticators need to consider what the friction is on the user, and need to take a realistic assessment of the risk.  We shouldn't just add a 2FA on every account we use online, the usability impact is too high right now.

### [Revenge of the PMO | Silicon Valley Product Group](https://svpg.com/revenge-of-the-pmo/)

*"I can’t imagine any of the strong tech product companies I know choosing to move to SAFe, and if for some reason they did, I’m pretty certain their top talent would leave."*

Strong words from Marty Cagan on the Scaled Agile Framework. This is my experience as well, organisations trying to do agile at scale miss that self empowered teams who can self direct is the entire point of agile.  Security people often seem to be scared of this as well, and I suspect for the same reason, which is that over the last decade, they have not demonstrated how they add value to the business and so are being shut out.  Interesting parallels and some food for thought here.

### [What Matters Most During a Data Breach? How You React](https://securityintelligence.com/what-matters-most-during-a-data-breach-how-you-react/)

*"The Ponemon Institute’s 2017 study on the cost of a data breach showed companies have a one in four chance of experiencing such a breach within a two-year period." *

By this math, the chance of a data breach in any given year is around 1/8 or 12.5%. The raw report makes clear that these are "material breaches" of 1,000 records or more. Slightly more interesting, human error and system glitch was responsible for 53% of breaches, and malicious hackers are only responsible for 47%.  While I know that is true for small breaches (sending an email to the wrong user or cc'ing someone by accident), I didn't realise it would be so high for material breaches as well.  I suspect that things like misconfigured FTP servers or S3 buckets are counted here.

### [Hackers exploit Jenkins servers, make $3 million by mining Monero | CSO Online](https://www.csoonline.com/article/3256314/security/hackers-exploit-jenkins-servers-make-3-million-by-mining-monero.html)

*"The attackers are leveraging CVE-2017-1000353, a flaw disclosed in a Jenkins security advisory issued in April 2017. Besides making the attackers millionaires, the "JenkinsMiner" could impact servers by slowing their performance and issuing denial of service."*

This one terrifies me. The security around our CI estates tends to be quite poor, because it isn't part of the "production estate" for most development teams. But malware on that machine can arbitrarily change any code deployed to any part of your infrastructure. This is the weak point in any agile organisation with continuous delivery.  That the attackers in this case just wanted to mine Monero on the high powered CI server is lucky and fortuitous, it could be much much worse

### [DIB: Detecting Agile BS](https://media.defense.gov/2018/Oct/09/2002049591/-1/-1/0/DIB_DETECTING_AGILE_BS_2018.10.05.PDF)

*Agile is a buzzword of software development, and so all DoD software development projects are, almost by default, now declared to be "agile." The purpose of this document is to provide guidance to DoD program executives and acquisition professionals on how to detect software projects that are really using agile development versus those that are simply waterfall or spiral development in agile clothing (“agile-scrum-fall”).*

 

This guide is a great little take on how governance boards and senior executives can tell real agile projects from waterfall projects that have been merely rebranded into agile.

The questions at the end should form part of any assessment process you have for agile projects

 

# Long reads or entertaining stories

*These amused me this year, or were just enjoyable long form journalism, a deep dive into a subject that gave me a far better understanding of a topic I didn’t know before.*

### [The man who cracked the lottery](https://www.nytimes.com/interactive/2018/05/03/magazine/money-issue-iowa-lottery-fraud-mystery.html)

*"And that’s when the idea first came. “Just like a little seed that was planted," Tipton said in his proffer. “And then during one slow period I just had a — had a thought that it’s possible, and I tried it and I put it in.””*

Interesting account of a real insider job. Working out what could have been done to prevent, detect or recover from this is an interesting exercise.

### [How Judea Pearl Became One of AI's Sharpest Critics - The Atlantic](http://www.theatlantic.com/technology/archive/2018/05/machine-learning-is-stuck-on-asking-why/560675/)

*"As he sees it, the state of the art in artificial intelligence today is merely a souped-up version of what machines could already do a generation ago: find hidden regularities in a large set of data. “All the impressive achievements of deep learning amount to just curve fitting,"* he said recently.”

The argument that modern machine learning is just applied statistics is not new, and while I agree that there’s interesting value is interrogative AI, for cyber security and in particular operations and analysts, understanding that machine learning is just curve fitting helps us work out where we can apply it more usefully. I think the deeper AI work in here will be more useful for analysts dealing with the question of why and attribution in the future.

### [Why do we care so much about privacy? The New Yorker](https://www.newyorker.com/magazine/2018/06/18/why-do-we-care-so-much-about-privacy)

*"The law is constantly playing catch-up. In the digital age, almost all transactions are recorded somewhere, and almost any information worth keeping private involves a third party. Most of us store more in the cloud than in lockboxes. It does not make sense to constrain the technological capacities of law enforcement just because the technology allows it to work more efficiently, but those capacities can also lead to a society whose citizens have nowhere to hide."*

A fascinating long read about the history of privacy laws (primarily in the US). The interesting equivalence made over and over is that we care far more when a computer scans us than we do when an individual does. The gift that technology gives us is scale and speed, but that’s precisely the thing that creates unintended consequences further down the road.

### *[Why Are There So Damn Many Ubers? | Village Voic*e](https://www.villagevoice.com/2018/06/15/why-are-there-so-many-damn-ubers/)

*"A terribly overused buzzword that internet companies like to use is “frictionless,"but it’s a decent term to describe what happened next. Stripped down to its essence, the process of using Uber was the way black car services had always worked: You used a phone to make a car come to you, and you paid by credit card. As Ackman told the Times, “It’s not that different from using Google or a directory to find a car service.” But the app made everything easier for both the driver and the passenger; GPS in particular meant the driver could home right in on you rather than having to work out where exactly you were via conversation with a dispatcher. Having your credit card on file meant you didn’t have to think about payment on every trip. “. *

This great description of disruption and frictionless design is a good reminder of how users can circumnavigate a set of regulations and rules if it’s easy. In cyber security things like BYOD, Slack, Trello, G-Suite and more are frictionless "shadow IT" that can circumnavigate our security policies. This isn’t to say our policies are great but that we need to heavily rethink them to work with these tools instead of looking to the past

### [You used to build a wall to keep them out, but now hackers are destroying you from the inside | WIRED UK](https://www.wired.co.uk/article/darktrace-insider-threats-hackers-security)

*Organisations are also vulnerable at many more points. The internet of things is rapidly expanding what security experts call"the attack surface". Intruders can now enter an organisation through a vending machine, a smart thermostat or a TV, not to mention one of the many connected devices that employees carry or wear every day. The gatekeepers, outwitted and overrun, have responded like authoritarian leaders attempting to clamp down on crime, introducing increasingly draconian security policies. But when employees subsequently find it harder to work, innovate and experiment, the business suffers."*

As it says. I'd argue that it's not even the Internet of Things, it's people trying to work around the VPN, people using their iphones as hotspots, and people forwarding emails via their personal accounts that bypasses all of the "gatekeepers". But everything else here, I agree with.

For me, this is probably the long read of the week.

### [The SIM Hijackers - Motherboard](https://motherboard.vice.com/en_us/article/vbqax3/hackers-sim-swapping-steal-phone-numbers-instagram-bitcoin)

"By hijacking Rachel’s phone number, the hackers were able to seize not only Rachel’s Instagram, but her Amazon, Ebay, Paypal, Netflix, and Hulu accounts too. None of the security measures Rachel took to secure some of those accounts, including two-factor authentication, mattered once the hackers took control of her phone number."

There's a lot of discussion around two-factor at the moment, because it's not a panacea, and we know that sim-swapping in the US and SS7 hijacking in europe and various other exploits work against it. But it massively increases the baseline of effort that an attacker has to go through compared to not having it. Don't let stories like this put you off of two-factor authentication, just remember that it's not perfect.

### [The Untold Story of NotPetya, the Most Devastating Cyberattack in History | WIRED](https://www.wired.com/story/notpetya-cyberattack-ukraine-russia-code-crashed-the-world/)

*"It’s the story of a nation-state’s weapon of war released in a medium where national borders have no meaning, and where collateral damage travels via a cruel and unexpected logic: Where an attack aimed at Ukraine strikes Maersk, and an attack on Maersk strikes everywhere at once."*

This is a fascinating read generally, but this sentence struck me. The interconnectedness of computers has been seen over and over again, from WannaCry to NotPetya to the early spread of the Morris Worm. It's increasingly difficult to reliably and ethically determine what a valid computer target should be for any form of cyber warfare, and as the control of the techniques is no where nearly as easily controlled as the one for the mechanistic capability to produce nuclear weapons, the increasing proliferation of these weapons to more and more non-nation-state groups seems likely and deeply worrying.

 

### [The Amazon machine — Benedict Evans](https://www.ben-evans.com/benedictevans/2017/12/12/the-amazon-machine)

"This means not so much that products on Amazon are commodities (this is obvious) but that product categories on Amazon are commodities. This model has two obvious consequences for Amazon. The first is that it can scale almost indefinitely - if you can launch x in y without a meeting or a new org structure, the speed of expansion into new categories is limited mostly by your ability to hire and to procure (and also by consumers’ willingness to buy a new category online, of course)."

This is a great read from Benedict that I think really sums up the Amazon model very well. I think a lot of people misconstrue the big technology giants, Amazon, Google, Apple, Facebook as being essentially the same, but fundamentally they have very different business models, and it will be interesting to see which ones thrive and prosper more in changing economic climates.

### [Cyber security – why you’re doing it all wrong](https://www.computerweekly.com/opinion/Cyber-security-why-youre-doing-it-all-wrong)

*"For too long, security teams have lived the lie that what they have delivered has been effective, but so often they approach it from a viewpoint divorced from the customers they affect. To be fair to most security teams, they are generally blissfully unaware of the inefficiencies of their controls – or ignorant.*

*This is admittedly a very sweeping statement, but headline after headline about data breaches tends to argue the point. And let’s not be shy here – these are major corporations with systemic failures when it comes to protecting their crown jewels. Something doesn’t sit right. How can this be? Spending on IT security is at an all-time high. The volume of security offerings to cover every possible facet of security is unparalleled."*

Everything about this essay is right. Security is often a complete disaster with failure to recognise what is the reality. We need to take a hard look at what we achieve and determine whether any of our security controls that we take all of our time maintaining is actually worth spending that time.

### [How an inmate hacker turned a prison upside down - The Verge](https://www.theverge.com/2017/10/10/16447264/prison-hacker-recycled-computer-fraud-ohio-marion-transkiy)

*"Transkiy was being questioned about an extraordinary form of contraband. Someone had hidden refurbished computers in the ceiling of the prison. They’d somehow obtained a login to the prison’s network, gaining access to the inner workings of the facility, including databases on inmates and the tools for creating passes needed to enter restricted areas. The computers also granted access to the outside world, which someone had used to apply for credit cards using the stolen identity of a prisoner. The scheme extended from the prison, to a community nonprofit, to multiple banks — all done under the noses of an oblivious prison staff."*

This is a lovely story showing how one can abuse a system and the ways you can slip through the cracks of a system if you know what you are doing.

### [Inside the OPM Hack, The Cyberattack that Shocked the US Government | WIRED](https://www.wired.com/2016/10/inside-cyberattack-shocked-us-government/)

*But the plan pays too little attention to a fundamental flaw in our approach to security: We’re overly focused on prevention at the expense of mitigation. One reason these attackers can do so much damage is that the average time between a malware infection and discovery of the attack is more than 200 days, a gap that has barely narrowed in recent years.*

*"We can’t operate with the mindset that everything has to be about keeping them out," says Rich Barger, ThreatConnect’s chief intelligence officer. “We have to operate knowing that they’re going to get inside sometimes. The question is, how do we limit their effectiveness and conduct secure business operations knowing they’re watching?” Accomplishing that means building networks that are designed to limit a hacker’s ability to maneuver and creating better ways to detect anomalous behavior by allegedly authorized users.*

 

I had missed this 2 years ago and this looks to be one of the most thorough writeups of a technical breach by an APT that I've seen. Well written and enjoyably readable.

### [The Big Hack: How China Used a Tiny Chip to Infiltrate U.S. Companies - Bloomberg](https://www.bloomberg.com/news/features/2018-10-04/the-big-hack-how-china-used-a-tiny-chip-to-infiltrate-america-s-top-companies?srnd=businessweek-v2)

*During the ensuing top-secret probe, which remains open more than three years later, investigators determined that the chips allowed the attackers to create a stealth doorway into any network that included the altered machines. Multiple people familiar with the matter say investigators found that the chips had been inserted at factories run by manufacturing subcontractors in China.*

 

 

There's so much to this story that I don't think I can do it justice.

For starters, Apple has issued a very clear denial, [On this we can be very clear: Apple has never found malicious chips, "hardware manipulations" or vulnerabilities purposely planted in any server.](https://www.apple.com/newsroom/2018/10/what-businessweek-got-wrong-about-apple/), and Amazon was equally straight talking with [At no time, past or present, have we ever found any issues relating to modified hardware or malicious chips in SuperMicro motherboards in any Elemental or Amazon systems. Nor have we engaged in an investigation with the government.](https://aws.amazon.com/blogs/security/setting-the-record-straight-on-bloomberg-businessweeks-erroneous-article/). There is no way that these companies would issue such straight talking denials if they were being strong-armed by the Government and told they couldn't talk about these investigations.

Amazon and Apple are interesting targets. Why for example, are Microsoft and Google not included as targets? How about Facebook, Twitter or other leading tech companies?

However, the article contains a lot of details, and a very strong set of claims from Bloomberg, this isn't a fly by night newsletter and an article dashed off, this was an in depth investigation that must have been checked and vetted thoroughly. However, Bloomberg, and indeed these writers themselves, [have gotten the technical facts on stories wrong in the past stories](https://twitter.com/GossiTheDog/status/1048322164653535232) so aren't foolproof.

On the technical side, I'm suspicious that a hardware implant, as described, can possibly achieve what is being described. Hosting systems inside Amazon and Apple are vastly complicated, and the networks are not designed to allow the hardware direct access to the internet. Instead a complex layer of Software Defined Networks overlay the network, because the hardware is often just a base for virtual machines and networks get complicated at that point.

Something that could inject code into the Baseboard Management Controller is very very low level, and the complexity of the software stack above them, which varies from system to system would make this an amazing feat of engineering to carry out.

But as has [been pointed out elsewhere](https://www.theregister.co.uk/2018/10/04/supermicro_bloomberg/), this is the dream of intelligence agencies the world round, an undetectable hardware implant that can take over the machine.

What's the truth of these claims and counterclaims? I'm not sure we'll find out anytime soon. Unless Bloomberg is willing or capable of naming their sources, or their sources come back to correct the reporters, I don't think we'll find out what was actually said. Equally, denials from the companies will always be disbelieved, because the *spooky* nature of intelligence investigations means that any statement, even the most straight spoken, will be treated with suspicion. I personally doubt the validity of the story, I think there has been confusion in the reporting from the sources and the questions asked.

Suffice to say, I suspect that for most of us, this story is covering threat actors at the highest levels, and far beyond our reasonable threat model. You shouldn't be reviewing your hardware or picking a cloud provider based on this story.

Your real threat today is still just as it was yesterday, that your users will click a link in a phishing email and enter their credentials into the site.

### [China's Five Steps for Recruiting Spies in the US | WIRED](https://www.wired.com/story/china-spy-recruitment-us/)

*Sifting through more than a dozen of the major cases that have targeted Westerners, though, provides an illuminating window into how China recruits its spies. The recruitment follows a well-known five-step espionage road map: Spotting, assessing, developing, recruiting, and, finally, what professionals call "handling."*

 

This is an interesting read and insight into human intelligence operations, and how they can be used to aid and advise technical intelligence operations.

### [The Machine Fired Me](https://idiallo.com/blog/when-a-machine-fired-me)

*After lunch, two people appeared at my desk. One was a familiar long face that seemed to avoid making direct eye contact. It was Jose and his fellow security guard. He cordially informed me that he was to escort me out of the building.*

*The director was furious. They had received a very threatening email to escort me out of the building and were just doing their job.*

*"Who the hell is sending those emails!?"*

*I was fired. There was nothing my manager could do about it. There was nothing the director could do about it. They stood powerless as I packed my stuff and left the building.*

 

So, I love this story, well written and humorous. But it also tells me that someone somewhere actually loves a Joiners/Movers/Leavers process. The Leavers process is often a very poor weak point in most systems, especially around contractors. Find the right person leaving because their manager was fired and you'll find someone whose leaving forms and process was not done correctly.

 

### [How Anna Delvey Tricked New York’s Party People](https://www.thecut.com/2018/05/how-anna-delvey-tricked-new-york.html?utm_source=tw&utm_medium=s3&utm_campaign=sharebutton-b)

*The following January, Anna hired a PR firm to put together a birthday party at one of her favorite restaurants, Sadelle’s in Soho. "It was a lot of very cool, very successful people," said Huang, who, while aware Anna owed him money for their Venice trip, remained mostly unconcerned about it, at least until the restaurant, having seen Polaroids of Huang and Anna at the party on Instagram, messaged him a few days later. “They were like, ‘Do you have her contact info?’ ” he says now. “ ‘Because she didn’t pay her bill.’ Then I realized, Oh my God, she is not legit.”*

*As Anna bounced around the globe, there was some speculation as to where her means to do this came from, though no one seemed to care that much so long as the bills got paid.*

*"I thought she had family money," said Jayma Cardoso, one of the owners of the Surf Lodge in Montauk. Delvey’s father was a diplomat to Russia, one friend was sure. No, another insisted, he was an oil-industry titan. “As far as I knew, her family was the Delvey family that is big in antiques in Germany,” said another acquaintance, a millionaire tech CEO. (It is unclear what family he was referring to.)*

 

This is a wonderful long read on a scammer living it up and mostly managing to pull it off. A reminder that everybody is capable of being duped, and that people generally want to believe whats in front of them rather than that they might be being duped

### [The Equifax Data Breach [PDF]](https://oversight.house.gov/wp-content/uploads/2018/12/Equifax-Report.pdf)

*Equifax continued its incident investigation by conducting vulnerability testing of the ACIS application.*

*Equifax discovered flaws in the ACIS code rendering the system vulnerable to SQL injection and Insecure Direct Object Reference attacks. The SQL injection flaw allows an attacker to inject or retrieve database information. The Insecure Direct Object Reference flaw allows direct access to system data without requiring appropriate authentication or authorization. The ACIS application had been tested for vulnerabilities in April 2017 after Equifax knew about the Apache Struts flaw and no unremediated vulnerabilities were found. It is unclear why the April 2017 vulnerability testing and the July 30, 2017 vulnerability testing produced different results.*

*[...]*

*On a 7:00 am call with the initial Project Sierra group, Equifax’s Vulnerability Assessment team discussed the findings of the ACIS application review conducted on July 30.230 The team had identified an unexpected JSP file inserted into the ACIS application through SQL injection.*

*[...]*

*Equifax discovered code within the JSP file provided the avenue for the exploit. Following this 7:00 am call, a second unexpected JSP file was identified within the ACIS application.*

*[...]*

*Later on July 31, the Vulnerability Assessment team conducted a manual review looking for additional instances of Apache Struts on other servers.A vulnerable version of Apache Struts was discovered on a second server within the ACIS application. Equifax did not load a SSL certificate on this server, so it did not have visibility into the traffic to and from this server. Equifax uploaded a SSL certificate for this domain on August 3.246*

 

This is really important reading. This makes clear that there is no single root cause in this breach. As in all incidents, there are many many failures that contribute to each other and cause this to fail. You could say that there are flaws in the processes, divisions in the organisation and failures of accountability, but those are always the case in systems that haven't been breached. The failures here are numerous and sometimes shocking.

# Cybersecurity advances and the threat landscape

*How have things been changing over the year, and what are bad people actually doing?  These links cover the changes in security itself*

### [The worst truism in information security - The Blagoblag](https://alexgaynor.net/2018/jul/20/worst-truism-in-infosec/)

"Attackers just need one vulnerability, defenders need to be perfect

This may be the single most repeated truism in information security. Just this week, a colleague invoked this, with the quip that those of us who've chosen defense must be pretty dumb, given the challenge of that task, and the possibility of an easier career in offense."

There is so much good in here, but I wanted to call out this attitude. If you think the job of being an ethical hacker/red team in your organisation is to win, to just break stuff, then you are part of the problem. The only reason you exist is to help the organisation, and just breaking stuff and walking away is not helping.

If your red team has this attitude, then you should get rid of them and get a new red team. A red teams job is about 10% breaking your stuff, and 90% sitting and working with the team to build a better defence.

Equally, as this article says, this dichotomy of systems being secure or insecure is entirely a fallacy.  We know that we have unpatched systems, that there are possible vulnerabilities in our systems.  We exist to help make priority decisions over how to spend a limited amount of security capital.

Security vendors and as a profession doesn't make enough of how to make reasonable choices on security, instead everyone is shouting that if you just fix passwords/install a threat detection tool/upgrade your firewalls/install an APT defence black box, then all of your security issues will go away.

### [Why Isn't Secure DevOps Being Practiced?](https://securityintelligence.com/why-isnt-secure-devops-being-practiced/)

*"While adoption varies by industry, the report found only a 12 percent margin between the highest and lowest adopters by industry. High-tech industries lead with 56 percent adoption, while retail was ranked last at 44 percent integration of app security testing in CI/CD workflows. Most commonly, organizations rely on software analysis scanning solutions, dynamic analysis methodologies and third-party penetration testing when secure DevOps is practiced in the enterprise."*

I agree with a lot of this report, especially that the big barriers to embedding security in the build pipeline is because tooling isn’t easy to automate and the large number of false positives. But that last reason *"developer indifference"* could be turned around to say *“security hasn’t made itself relevant”*.

In the same way DevOps is about aligning development and operations to care about business goals, I think devsecops is more than just build pipelines, it’s about enabling developers to deliver business value, with security enabling developers to do that.

### [Nation-state hackers attempted to use Equifax vulnerability against DoD, NSA official says](https://www.cyberscoop.com/dod-apache-struts-equifax-david-hogue-nsa/)

*"Within 24 hours I would say of whenever an exploit or vulnerability is released, it is weaponized and used against us," said Hogue. Hogue also said the use of “zero day” vulnerabilities to breach systems appears to be increasingly rare, based on his own work.*

*"At NSA we have not responded to an intrusion response that’s used a zero day vulnerability in over 24 months," Hogue said. “The majority of incidents we see are a result of hardware and software updates that are not applying.”*

This is old, and I tweeted about it at CyberUK 2018 this year, but it's worth us working out what the definition of a 0-day is. Most vulnerability researchers mean the use of a vulnerability before the patch is released or the vulnerability is announced. But if your organisation can't patch quicker than say 7 days, then all of the vulnerabilities released between day 0 and day 7 might as well be a 0-day as far as you are concerned. That is to say, the longer your patching cycle, the more 0-days you'll effectively be vulnerable to.

### [On the Hunt for FIN7: Pursuing an Enigmatic and Evasive Global Criminal Operation « On the Hunt for FIN7: Pursuing an Enigmatic and Evasive Global Criminal Operation | FireEye Inc](https://www.fireeye.com/blog/threat-research/2018/08/fin7-pursuing-an-enigmatic-and-evasive-global-criminal-operation.html)

*We have identified job advertisements for Combi Security that have been posted on popular Russian, Ukrainian, and Uzbek job recruitment sites, as well as numerous individuals who most likely worked for the company. Due to the seeming legitimacy of the recruitment postings, some individuals may have been unaware of illicit nature of their work.*

*While the recruitment of unwitting individuals as puppets has been a common component of at least some criminal schemes – for example, reshipping mules who are recruited through postings on career sites advertising attractive work-from-home jobs – FIN7’s veiling of full-scale financial compromises as legitimate offensive security engagements is particularly notable.*

*The apparent success of Combi Security in recruiting unsuspecting individuals in this manner, may lead to more of this type of technical recruitment by cyber criminals in the future.*

 

This is a great analysis of an advanced threat actor, who actually exhibited great technical skill, coming up with some novel obfuscation techniques.

The fact that it turns out that they literally advertised jobs, through a front company, and potentially got unwitting developers to work for them on some of these technical innovations is quite scary. Do you know who you work for?

There's an interesting grey line in the infosec community, and it makes me wonder about the CTF's, coding challenges and so forth, and whether these are being mined for new and novel techniques for advanced actors.

### [GAO-19-128 WEAPON SYSTEMS CYBERSECURITY](https://www.gao.gov/assets/700/694913.pdf)

*A patch or software enhancement that causes problems in an email system is inconvenient, whereas one that affects an aircraft or missile system could be catastrophic.*

*Officials from one program we met with said they are supposed to apply patches within 21 days of when they are released, but fully testing a patch can take months due to the complexity of the system. Even when patches have been tested, applying the patches may take additional time.*

*Further, weapon systems are often dispersed or deployed throughout the world. Some deployed systems may only be patched or receive software enhancements when they return to specific locations.*

*Although there are valid reasons for delaying or forgoing weapon systems patches, this means some weapon systems are operating, possibly for extended periods, with known vulnerabilities.*

*[...]*

*One test team emulated a denial of service attack by rebooting the system, ensuring the system could not carry out its mission for a short period of time. Operators reported that they did not suspect a cyber attack because unexplained crashes were normal for the system.*

*Another test report indicated that the intrusion detection system correctly identified test team activity, but did not improve users’ awareness of test team activities because it was always "red." Warnings were so common that operators were desensitized to them.*

 

This report from the GAO is fascinating and terrifying in equal measure. There's lots of interesting details in here, but it does make clear that the complexity of the environment that we are talking about.

A warship is not as simple as a web application, and sadly, the cloud isn't going to solve many of these problems. However connectivity is on the rise, and even if the battleship may not be connected to the internet, there's a good possibility that the staff on it will have mobile devices that connect to the internet over high speed connections. What are the chances that they'll connect those devices to the shipboard network?

As always, this is going to be a job of fixing the basics, not applying magic machine learning and AI cybersecurity boondoggles

### [They’re Drinking Your Milkshake: CTA’s Joint Analysis on Illicit Cryptocurrency Mining - Cyber Threat Alliance : Cyber Threat Alliance](https://www.cyberthreatalliance.org/joint-analysis-on-illicit-cryptocurrency-mining/)

*CTA members are seeing an enormous increase in illicit mining activity targeting their customers. Activity has gone from a virtually non-exist issue to one that almost universally shows up at the top of our members’ threat lists. Combined data from several CTA members shows a 459 percent increase in illicit cryptocurrency mining malware detections since 2017. Recent quarterly trend reports from CTA members show that this rapid growth shows no signs of slowing down. If 2017 was defined by the threat of ransomware, 2018 has been dominated by illicit cryptocurrency mining.*

*For many, this may not seem like an important issue. What difference does it make if someone is stealing my computing power to mine cryptocurrencies? However, illicit mining is the "canary in the coal mine" of cybersecurity threats. If illicit cryptocurrency mining is taking place on your network, then you most likely have worse problems and we should consider the future of illicit mining as a strategic threat. More sophisticated actors could use – or may already by using – that same access to lay the groundwork for you to have a really bad day.*

 

This is a huge increase in targeted attacks, and as the blogpost says, if someone has the ability to put a coin mining script onto your service, whether backend or potentially worse, frontend; then they have the ability to do far worse if they wanted to.

It's interesting to me that there's such a rise in this, it indicates that economically speaking, the blackhat hacker community sees more value in abusing stolen credentials and site takeovers for CPU mining than they do for the value of stealing the data on those systems. The report says that it's due to the rise in value in the coin markets, but I wonder if there is a collapse in the value of personal data because of how much is out there, the actions of police forces to crackdown on dark markets where it can be sold?

If the bitcoin markets collapsed, I wonder if this activity would go away, and what would replace it?

Equally, I'd expect the next step to move from hacked websites and credentials into coinhive scripts being injected into software chain dependencies. Some analysis on your dependencies to determine if they are running any coin mining might be interesting to consider in a build pipeline at the moment

 

# News Stories of the year

*Some of the biggest or most interesting stories of the year, and my analysis of them when they happened*

### [JavaScript PCI nightmare: Ticketmaster, Inbenta and the canary in the coal mine](https://doublepulsar.com/javascript-pci-nightmare-ticketmaster-inbenta-and-the-canary-in-the-coal-mine-5c7410e8565b)

*"I’ll give you a spoiler: the risk is very real — this isn’t the first time this has happened, somebody who works for PCI post breach assessment told me that over 75% of all web store breaches they assessed at large enterprises happened due to this reason, a massive increase." *

This is a mess of 'PCI as a standard' not keeping up with modern web practices, and as Kevin points out, the canary in the coalmine for supply chain infections in Javascript. Adding javascript libraries to your front end is common and the security implications are not generally well understood by developers. Backend databases are thoroughly covered by security and compliance teams, but it's rare to meet a full stack security assurance specialist who understands browsers and javascript and HTML instead of networks and firewalls.

### [This fitness app lets anyone find names and addresses for thousands of soldiers and secret agents](https://decorrespondent.nl/8480/this-fitness-app-lets-anyone-find-names-and-addresses-for-thousands-of-soldiers-and-secret-agents/260810880-cc840165)

*"Yet the activity tracking map in Polar’s fitness app lets us see that many of Tom’s runs start and end near a cluster of homes in a small town in the northern Netherlands. A little Googling gives us his exact address. We also find the names of his wife and children, and photos." *

This stuff is really hard. Jigsaw identification is a common threat for people who are trying to keep their identity secret. Early court injunctions simply told newspapers they couldn't identify celebrities involved in salacious court cases, but it meant that one might identify the team, whereas another newspaper would name the age. Courts fixed this by telling newspapers exactly what they could or could not identify about the court identities.  No commercial organisation can reasonably protect the identity of these sensitive individuals, as they don't know the sensitivity, and as such the responsibility tends to lie with the individual and any guidance from their organisation.  As I said, this stuff is hard and only going to get harder as time goes by.  

### [Botched CIA Communications System Helped Blow Cover of Chinese Agents – Foreign Policy](https://foreignpolicy.com/2018/08/15/botched-cia-communications-system-helped-blow-cover-chinese-agents-intelligence/amp/)

"But the CIA’s interim system contained a technical error: It connected back architecturally to the CIA’s main covert communications platform. When the compromise was suspected, the FBI and NSA both ran*"penetration tests"*to determine the security of the interim system. They found that cyber experts with access to the interim system could also access the broader covert communications system the agency was using to interact with its vetted sources, according to the former officials."

An interesting read, and a reminder that some of the patterns we use in cybersecurity are important and do result in life or death for real people in real places sometimes. The description further down of the counterintelligence service forming a specific task force to attempt to break the system is a healthy reminder that the sort of adversary that you can face at these higher levels is determined and capable

### [The CIA's communications suffered a catastrophic compromise](https://finance.yahoo.com/news/cias-communications-suffered-catastrophic-compromise-started-iran-090018710.html)

*The losses could have stopped there. But U.S. officials believe Iranian intelligence was then able to compromise the covert communications system. At the CIA, there was "shock and awe" about the simplicity of the technique the Iranians used to successfully compromise the system, said one former official.*

*In fact, the Iranians used Google to identify the website the CIA was using to communicate with agents. Because Google is continuously scraping the internet for information about all the world’s websites, it can function as a tremendous investigative tool — even for counter-espionage purposes. And Google’s search functions allow users to employ advanced operators — like "AND," “OR,” and other, much more sophisticated ones — that weed out and isolate websites and online data with extreme specificity.*

*According to the former intelligence official, once the Iranian double agent showed Iranian intelligence the website used to communicate with his or her CIA handlers, they began to scour the internet for websites with similar digital signifiers or components — eventually hitting on the right string of advanced search terms to locate other secret CIA websites. From there, Iranian intelligence tracked who was visiting these sites, and from where, and began to unravel the wider CIA network*

 

I think I first covered this back in CyberWeekly #13, with a report from ForeignPolicy on the breach of the CIA covert informant network. But there are more details in this Yahoo report, indicating that it was broken via Google Dorking, which is to say, they simply googled for the identifiers that gave away the websites.

One of the concerning things is the reflection of our own systems. There was a technical person who identified the flaws early, but wasn't listened to because the organisation resists change. How often have we found senior members of organisations confident in their organisations security, while talking to the analysts on the ground, you get a different story?

### [At the CIA, a fix to communications system that left trail of dead agents remains elusive](https://news.yahoo.com/cia-fix-communications-system-left-trail-dead-agents-remains-elusive-100046908.html?soc_src=hl-viewer&soc_trk=tw)

*Because of the scope of the problem, fixing it was also a staggering task. It’s not just "a single flawed system that needed to be fixed," according to one former CIA official. “It was a universe of systems.”*

*The issues with internet-based covert communications systems cannot be fully solved piecemeal and will require an immense allocation of resources. "A patch won’t solve the problem," said one of the former officials. “We’re not talking about billions of dollars, we’re talking about hundreds of billions of dollars to fix” these systems.*

*[...]*

*Former intelligence officials described longstanding tensions between the two directorates, as well as dysfunction within DS&T itself. DS&T’s budget has grown tremendously, said one former official, and the division was known for "wasting a lot money over the years."*

 

I've covered this before, but as more details come out, you get more and more insight into this world. Waring divisions, those who get the internet but not operational tactics and those who don't understand the internet and technology. You can see the lack of user research and the lack of focus on technology delivering for its users.

This story isn't over, and I think we'll see more of it in the year to come

### [bellingcat - Skripal Suspects Confirmed as GRU Operatives: Prior European Operations Disclosed - bellingcat](https://www.bellingcat.com/news/uk-and-europe/2018/09/20/skripal-suspects-confirmed-gru-operatives-prior-european-operations-disclosed/)

*Bellingcat compared the passport number on Col. Shishmakov’s cover-identity passport, with the numbers of the (cover-identity) passports of "Petrov" and “Boshirov”. The numbers were from the same batch, with only 26 intervening passport numbers between “Petrov”’s (654341297), and “Shirokov”’s (654341323) number. “Shirokov”’s passport was issued in August 2016, implying that Petrov’s and Boshirov’s passports were issued by the same special authority earlier that year"*

 

This is an interesting bit of investigatory work by Bellingcat, that I was going to include last week, but it didn't fit. I didn't realise how timely it would be this week, with the further revelations.

It's again a reminder that actually carrying out covert opsec is really hard, because humans and organisations abhor randomness, and you can therefore find the sequences that reveals the hidden details.

### [Conservative Party conference app reveals MPs' numbers - BBC News](https://www.bbc.co.uk/news/uk-politics-45693143)

*The Guardian's Dawn Foster, who is attending the conference, tweeted about the security breach and said she had been able to access the former foreign secretary's personal details, including his mobile phone number.*

*She shared a redacted picture of Mr Johnson's profile, which did not reveal his phone number.*

*It appears that people could access an MP's personal details by entering their email address, without a password, when pressing the attendee's button in the app.*

 

This breach was embaressing all around, but I want to focus on two things here.

The first is that Dawn Foster here, I think literally posted a picture of herself breaching the Computer Misuse Act. She noticed the vulnerability, and then conciously exploited it, gaining access to someone else's information. And she took a screenshot and tweeted it. We train journalists on court proceedings and contempt of court, but not on the computer misuse act?

Secondly, there's an ethical question here about whether it's ethical to tweet the mechanism of a vulnerability. As a journalist, she had her story, she had her screenshots, she could have contacted CCHQ and told them about the vulnerability, and then published once the app was taken down or fixed.

By choosing to explain exactly how to find the vulnerability, she chose to endanger the personal data of people in that application, and that's exactly what the "crowd" then did.

The defense here is that the vulnerability was so simple that actually you didn't need to tell anyone how to do it, it was obvious and clear, and pointing out the obvious and clear isn't any form of recklessness nor an ethical breach, in fact it would be an ethical breach not to point it out.

All in all this was just an awful showing all round

# Digital and other non-cybersecurity stories

### [Delivering for citizens: How to triple the success rate of government transformations | McKinsey & Company](https://www.mckinsey.com/industries/public-sector/our-insights/delivering-for-citizens-how-to-triple-the-success-rate-of-government-transformations)

*"Another challenge is a lack of leadership longevity. For example, a review of ministers of health across 23 countries from 1990 to 2009 found that half of them served for less than two years in office."*

There’s a bunch interesting in this report, but this stood out. If political appointees, regardless of country, don’t stay longer than 2 years, which is far shorter than most operational Cybersecurity risks take to materialise, how will we ever get people to prioritise good operational security?

### [Monzo – Engineering Principles at Monzo](https://monzo.com/blog/2018/06/29/engineering-principles/)

*"We now have a team of over 70 engineers working on this, with more joining every week. As we continue to grow, it’s crucial that we create a shared understanding of what “good"* looks like so that existing engineers know how to make decisions and prioritise work and new engineers know what we expect and how we work.”

I think this article is brilliant for its advice, but I wanted to highlight it for this comment. From my experiences at GDS and the Guardian as well as helping other government departments build out digital teams, one thing is clear. Scaling people is really hard. The Dunbar number means that all of those assumptions and things that *"everyone knows"* probably aren’t obvious to everyone and when you scale past around 25 people you need to put real effort into documenting and communicating those cultural assumptions and practices if you want them to succeed.

### [Executives and Transparency](https://theitriskmanager.wordpress.com/2018/07/01/executives-and-transparency/)

*"Jira is a tool developed to help teams manage their development. It is not a tool to manage across teams or at an enterprise level. In order to create transparency for executives, you need an expert who can extract the data you need to create the views they need. One of the graduates working with us created an app to extract data from Jira into an SQL based database. Once the data was in the SQL database it took a couple of days to create an excel report that gave an executive view of lead time using weighted lead time."*

There is quite a lot of interesting bits and pieces in here about transformation and transparency, but this caught my eye. How often do we see agile teams grumble that the executives or leaders could come down and see the *"wall".*  What our teams often fail to realise is that the wall of cards, or tool like Jira, is optimised to be used by the day to day users of the thing. There is a value in senior leaders seeing that, to ensure that they aren’t being hoodwinked, and to understand where the *“roll up”* numbers come from, but actually, burn down charts, story estimation, velocity or other summation metrics are far more useful for these leaders, and creating those metrics, those dashboards takes time, energy and effort. As an agile team, you need to put in that energy or effort. Simply grumbling that the leadership don’t come to your show and tell, or don’t come and walk the wall wont lead to success

### [The Good Censor - Google Leak](http://j.mp/2pNDzBp)

*Relentless, 24/7 online conversations encourage people to dive in with their opinion* before it's too late, even if they're misinformed. And because we think with out emotional brain before rational one, instant response *amplify emotion-led discourse* not thoughtful debate.

 

This was linked to me in terms of *OMG, a good censor, how terrible*, but I think it's actually a very good breakdown of the debate about free-speech online and the position of a platform.

But this entire section about users bad behaviour stood out to me. We often accuse users of our IT products of bad security behaviours. But this section really highlights the fact that we need to better understand people's psychology and the reasons behind their actions. Because while people aren't always logical, they are always taking their actions for a deliberate reason.

### [Recovery from Command-and-Control: A Twelve-Step Program | Humanistic Systems](https://humanisticsystems.com/2014/07/12/recovery-from-command-and-control-a-twelve-step-program/)

*Command-and-control gives management the illusion that they are in control of the work and the workers, and that this control leads to effectiveness. Distance between decision making about the work and the work itself makes decision makers think that when things go right, it is because they are being done as specified: by the book. When things go wrong, it is because people did not do their job: they screwed up.*

 

This is an old article, but relevant I think. Command and control organisations often struggle with scale. Those at the top cannot possibly know what is going on at the bottom, but are expected to make decisions and give commands to those people.

This asymmetry of information is essentially what all project management is about, trying to get information from the bottom up to the top in the most efficient and effective way, and I don't think we have a good solution yet.

### [2018 State of Digital Transformation | Belfer Center for Science and International Affairs](https://www.belfercenter.org/publication/2018-state-digital-transformation)

*We’ve attempted to codify a lot of what we’ve been hearing from various units into a framework around five[sic] high-level themes:*

* *Political environment*

* *Institutional capacity*

* *Delivery capability*

* *Skills and hiring*

* *User-centered design*

* *Cross-government platforms.*

 

This is a great report and digital teams should read it all.

It’s interesting to me that security doesn’t come up at any point in this entire report. The digitisation of government goes on regardless of the opinions of security people and I think that’s probably right. It shows how far most security teams are from engaging with digital work and how digital people still view security as primarily a blocker to what they want to achieve.

If I were to define security in that maturity matrix, it would be interesting to think about what high capability security teams actually look like, because I think they wouldn’t look like most of our security teams today.

### [The Technology That Changed Air Travel](https://tryretool.com/blog/air-travel-software/amp/?__twitter_impression=true)

*Thankfully, there might be a solution — XML.*

 

It’s astonishing that in this day and age this is actually still true, many people still use this interface paradigm. The number of critical systems that are still processed and managed by technology from decades ago is astonishing and frankly quite scary when you consider how much the security assumptions have changed in that time. Computers are now interconnected in a myriad of ways that just weren't possible back when this was all created.

Thankfully, XML is coming to our rescue! I’ve always said that XML is like violence. If it’s not solving the problem, you clearly aren’t using enough of it!

I once worked with a Bloomberg XML API, it included an xml document with 40 elements each of which had a CDATA block of exactly 80 characters. Just because they say it’s XML doesn’t mean it’s well designed



