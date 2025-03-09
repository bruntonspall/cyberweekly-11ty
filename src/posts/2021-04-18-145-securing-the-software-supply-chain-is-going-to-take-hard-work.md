---
title: "145 - Securing the software supply chain is going to take hard work"
date: 2021-04-18
description: "Now that the US has sanctioned a selection of Russian Intelligence associated individuals and organisations, we can all relax and let the whole SolarWinds thing blow over right?"
permalink: /securing-the-software-supply-chain-is-going-to-take-hard-work/
---

Now that the US has sanctioned a selection of Russian Intelligence associated individuals and organisations, we can all relax and let the whole SolarWinds thing blow over right?

Sadly, supply chain vulnerabilities are going to be something of a theme this coming year, and probably for the next couple of years at least.  This is a really complex area where incentives are misaligned, user experience is terrible, and our existing mechanisms don't work effectively.

For example, the breach at CodeCov was detectable for 3 months, because CodeCov produce a hash of their software that can be independently verified, but nobody bothered to do so for 3 months.  Tens of thousands of users had access to a security function, but didn't do it.  Why not?  Probably because verifying the hashes of downloads is unintuitive to do, but also unintuitive to the user that they'd need to do it.  When else in life do you conduct a second check on things you work with?  

I tweeted some things the other night about one of the problems that is going to face us in this area, especially with the growth of SaaS firms.  As we increasingly externalise our data, our thinking and our systems to third parties, we need to rethink the mechanisms how we work with those companies.

If I sign up for O365 today, which is one of the best SaaS tools from a security perspective, I can turn on Defender (previously Advanced Threat Protection) and I'll see extra logs about my users and attacks on them in my Defender console.  That's really cool, and something that I don't get with my Attlasian products, with Airtable or with Salesforce CRM.  But that tells me about people attacking my staff and my data on the SaaS platform, it doesn't tell me about actions or activity within the platform, by the SaaS provider themselves.  

Hypothetically, if Solarwinds had an equivalent of Defender, the logs in it would still not have told me about the compromise of Solarwinds, nor would it have told me about the recent PHP compromise, the CodeCov compromise, and I'm sure that list will grow over time.

If we look at [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework/framework) it divides our cybersecurity efforts into Identify, Protect, Detect, Respond and Recover.  The [NCSC Cybersecurity Assessment Framework](https://www.ncsc.gov.uk/collection/caf) divides efforts into Manage risk, Protect, Detect and catchily "Minimise impact".  If I ever create the MBS Cyber Framework, it'll be Select, Detect, Protect and Effect just for the rhymes!

But how can we apply these principles to our SaaS tools as we move our data, our users and our controls out to them?  You can rely on the cloud providers to have various certifications that guarantee a level of internal protection, but without access to logs, to change notices, to telemetry from the suppliers systems, you cannot effectively implement any form of detection system.

Additionally, far too many SaaS systems deliberately make it hard to backup your data, and I've almost never found a system that has a backup and restore that reliably works and that I can test easily without massive additional cost.  I suspect that's one of those disincentives, any system that allows easy backup of all my data would also allow me to migrate to another platform.  However if someone does manage to compromise my tenant and ransomware all of my data, can I restore my Salesforce CRM from a backup?  If I'm lucky, I might be able to ask the supplier, but we have no standards for that, so we are entirely reliant on our contracts requesting such features.

As we move to migrate our data into these suppliers, we need to understand how to effectively collaborate on security with our supply chain, and how we can best take advantage of their security investment and features, without just trusting that it's good enough.

## [Codecov discloses 2.5-month-long supply chain attack | The Record by Recorded Future](https://therecord.media/codecov-discloses-2-5-month-long-supply-chain-attack/)

[https://therecord.media/codecov-discloses-2-5-month-long-supply-chain-attack/](https://therecord.media/codecov-discloses-2-5-month-long-supply-chain-attack/)

> The attacker gained access to the Bash Uploader script on January 31 and made periodic changes to add malicious code that would intercept uploads and scan and collect any sensitive information like credentials, tokens, or keys.
> 
> Codecov said it first learned of the breach on April 1 and has been working with a forensics firm to untangle the attacker’s actions.
> 
> The company disclosed the incident yesterday when it also sent emails with instructions to its customer base, which includes some big names like Atlassian, P&G, GoDaddy, the Washington Post, Tile, Dollar Shave Club, and Webflow.
> 
> But the security breach is not limited to clients who used the Bash Uploader script. Because the script is also embedded in other products, a large chunk of the company’s customers are most likely affected.
> 
> Other Codecov products that used the tainted script include Codecov-actions uploader for Github, the Codecov CircleCl Orb, and the Codecov Bitrise Step.
> 
> Codecov customers that used any of these tools are advised to change any credentials they sent over the air to Codecov’s platforms over the past two and a half months.


This is far more serious than it sounds.  The CodeCov tool is used by thousands of open source projects to calculate code coverage of their tests, and validate that new contributions are well tested.

It suggests that someone wants to inject this kind of scanning capability in the software development pipeline and extract secrets from lots of projects.

The best news is also the terrible news.  The codecov tool was changed, but whoever changed it did not adjust the sha1 displayed on the codecov website.  That means that for 3 months, everyone was downloading it without verifying that the hash (which makes you wonder what the point is).  The positive news is that this suggests that it's not a really really high capability actor, similar to solarwinds, as that attempted to change the software pre-hashing, and wouldn't have been spotted this way.  

However that does still mean that for 3 months, nobody validated the hash and thought "That's odd, it's not right".  I expect that CodeCov will be looking to automate that, to detect if the hash changes and to create an alert if they don't match in future.  It's almost like computers are good at boring tasks


## [Treasury Sanctions Russia with Sweeping New Sanctions Authority | U.S. Department of the Treasury](https://home.treasury.gov/news/press-releases/jy0127)

[https://home.treasury.gov/news/press-releases/jy0127](https://home.treasury.gov/news/press-releases/jy0127)

> The Russian Intelligence Services — specifically the Federal Security Service (FSB), Russia’s Main Intelligence Directorate (GRU), and the Foreign Intelligence Service (SVR) — have executed some of the most dangerous and disruptive cyber attacks in recent history, including the SolarWinds cyber attack.  The FSB and GRU were previously sanctioned in 2016, and again in 2018, for malicious cyber activity, and most recently on March 2, 2021 for activities related to the proliferation of weapons of mass destruction (WMD).
> 
> [...]
> 
> To bolster its malicious cyber operations, the FSB cultivates and co-opts criminal hackers, including the previously designated Evil Corp, enabling them to engage in disruptive ransomware attacks and phishing campaigns.
> 
> The GRU’s malign cyber activities include deployment of the NotPetya and Olympic Destroyer malware; intrusions targeting the Organization for the Prohibition of Chemical Weapons and the World Anti-Doping Agency; cyber attacks on government systems and critical infrastructure in Ukraine and the state of Georgia; and hack-and-leak operations targeting elections in the United States and France.
> 
> In addition, the Russian Intelligence Services’ third arm, the SVR, is responsible for the 2020 exploit of the SolarWinds Orion platform and other information technology infrastructures.  This intrusion compromised thousands of U.S. government and private sector networks.  The scope and scale of this compromise combined with Russia’s history of carrying out reckless and disruptive cyber operations makes it a national security concern.  The SVR has put at risk the global technology supply chain by allowing malware to be installed on the machines of tens of thousands of SolarWinds’ customers.  Victims of the compromise include the financial sector, critical infrastructure, government networks, and many others.  Further, this incident will cost businesses and consumers in the United States and worldwide millions of dollars to fully address.


This is quite the statement and the list of activities.  I don't think any of this attribution should be a surprise to any readers, many private firms, from FireEye to Microsoft and others have publicly attributed the set of activities to the Russian Intelligence Services before now, but pulling it all together is a statement all by itself.


## [Sanctioning Russia for SolarWinds: What Normative Line Did Russia Cross? - Lawfare](https://www.lawfareblog.com/sanctioning-russia-solarwinds-what-normative-line-did-russia-cross)

[https://www.lawfareblog.com/sanctioning-russia-solarwinds-what-normative-line-did-russia-cross](https://www.lawfareblog.com/sanctioning-russia-solarwinds-what-normative-line-did-russia-cross)

> I’ll mention another possible factor, one that understandably is not mentioned in the Treasury Department statement: domestic political salience. For better or worse, the SolarWinds story has been splashed across the headlines for many months now, at times dominating the news. It has been a bit of a phenomenon in the national dialogue, in other words, more so than most such scenarios. This has real and ongoing political implications, creating constant pressure to be seen as responding robustly.
> 
> Perhaps the most important vector for that robust response ought to be defensive measures such as funneling far-greater resources to the Cybersecurity and Infrastructure Security Agency (CISA) so it can better take the wheel in defending Federal Civilian Executive Branch systems. But it is understandable that the pressure all manifests in calls for action against the entity responsible for these headaches.


This is a good analysis asking what exactly the SVR did that was against norms as part of an espionage campaign.  The view seems to be that the size and scale, despite efforts within the Solarwinds/Sunburst activity set to minimise disruption was simply beyond an acceptable limit.

But the argument here is more that "You got caught" was the red line that was crossed.  Because it became a public talking point, there's a requirement for the politicians to be seen to respond in some visible way, and sanctions is one of the more visible and robust mechanisms.

But this isn't new or unusual.  Espionage has always ranked the embarrassment of being caught as one of the highest concerns.  From the mission impossible style "As always, should you or any of your IM Force be caught or killed, the Secretary will disavow any knowledge of your actions" to the fact that the UK didn't even avow the existence of the intelligence agencies until 1992, 30 years after the first James Bond movie.  But that embarrassment isn't just about the country caught spying, it's about the public embarrassment caused on the target, that requires them to respond, which can cause diplomatic incidents itself.


## [Lessons of the SolarWinds hack](https://www.iiss.org/blogs/survival-blog/2021/04/lessons-of-the-solarwinds-hack)

[https://www.iiss.org/blogs/survival-blog/2021/04/lessons-of-the-solarwinds-hack](https://www.iiss.org/blogs/survival-blog/2021/04/lessons-of-the-solarwinds-hack)

> The story first broke when FireEye, a top US cyber-security company
> involved in many major investigations and responsible for publicly identifying the perpetrators of numerous attacks (including the Russian intelligence
> services), announced in December 2020 that it had been hacked by a state
> with ‘top tier’ capabilities.
> 
> As of mid-February, cyber-security experts also
> discovered that 30% of the identified victims of the hack had no direct connection with SolarWinds itself, with the possibility therefore remaining that
> SolarWinds was not the hackers’ only initial launch point. Nevertheless, the
> infection has become widely known as the ‘SolarWinds hack’.3
> The US government attributed the hack to an ‘advanced, persistent threat
> actor likely of Russian origin’, meaning a Russian intelligence agency
> 
> [...]
> 
> Given that the SolarWinds hack therefore appears
> to constitute reconnaissance and espionage of the
> sort that the US itself excels at, it is neither accurate
> nor sensible for US commentators to characterise it
> as an act of war requiring warlike retaliation.9
>  If using spy planes, satellites and double agents to gather intelligence from inside the Soviet Union
> was normal business during the Cold War, the same is true of an operation
> like SolarWinds in the digital age.
> 
> Perhaps most importantly, the SolarWinds hack should focus attention on
> what adjustments are needed to the internal cyber-security strategies and
> capabilities of the US and its allies. This has been the central concern of
> expert testimony to the US Congress, which has called for increasing the
> powers of and funding for the US Cybersecurity and Infrastructure Security
> Agency (CISA); improving coordination between the US government and
> the corporate sector; grants to state and local government to enhance their
> cyber security; and accelerating IT modernisation across the federal government. Notably, most experts are not suggesting that all networks can be
> technically shielded from all attacks, or advocating that increased investment should be reserved solely for more and bigger technical solutions.
> 
> [...]
> 
> The fact that the US private sector detected and disrupted a complex Russian
> espionage operation is evidence that the liberal-democratic cyber-security
> model works.
> That said, the US model was not nearly efficient or effective enough,
> given the time it seems to have taken to uncover the Russian hack. Having
> advised their clients repeatedly about the ‘supply-chain’ threat, cybersecurity and IT companies should recognise that they themselves are
> prize targets for potential supply-chain operations and therefore need to
> rigorously follow their own security advice. 
> 
> Finally, it is worth noting that the SolarWinds hack exploited software
> and equipment supplied by US companies. It had nothing to do with any
> Russian-owned or -supplied equipment. Neither did the recently discovered
> Chinese hack of Microsoft email servers involve Chinese equipment.


I've pulled out some of the most interesting paragraphs in this excellent journal article.  

One of the most interesting things about this attack is that it was detected by a commercial third party, FireEye, in the original aspect.  That caused a lot of attention to be paid to the attack.  Because FireEye has good detective capabilities, they were able to provide effective ATT&CK profiles and information about the intrusion set that enabled other companies to identify the same attacker in their own organisations.

This is both an indication that the private model of cyber security works, but also a worrying one.  If it had been another company, would they have been able to share as effective information?  Do we have good standards for that information sharing?  And who really are the targets for nation states anyway?


## [It's time to say goodbye to the GPL — Martin Kleppmann’s blog](https://martin.kleppmann.com/2021/04/14/goodbye-gpl.html)

[https://martin.kleppmann.com/2021/04/14/goodbye-gpl.html](https://martin.kleppmann.com/2021/04/14/goodbye-gpl.html)

>  In the 2020s, the enemy of freedom in computing is cloud software (aka software as a service/SaaS, aka web apps) – i.e. software that runs primarily on the vendor’s servers, with all your data also stored on those servers. Examples include Google Docs, Trello, Slack, Figma, Notion, and many others.
> 
> This cloud software may have a client-side component (a mobile app, or the JavaScript running in your web browser), but it only works in conjunction with the vendor’s server. And there are lots of problems with cloud software:
> 
> If the company providing the cloud software goes out of business or decides to discontinue a product, the software stops working, and you are locked out of the documents and data you created with that software. This is an especially common problem with software made by a startup, which may get acquired by a bigger company that has no interest in continuing to maintain the startup’s product.
> Google and other cloud services may suddenly suspend your account with no warning and no recourse, for example if an automated system thinks you have violated its terms of service. Even if your own behaviour has been faultless, someone else may have hacked into your account and used it to send malware or phishing emails without your knowledge, triggering a terms of service violation. Thus, you could suddenly find yourself permanently locked out of every document you ever created on Google Docs or another app.
> With software that runs on your own computer, even if the software vendor goes bust, you can continue running it forever (in a VM/emulator if it’s no longer compatible with your OS, and assuming it doesn’t need to contact a server to check for a license check). For example, the Internet Archive has a collection of over 100,000 historical software titles that you can run in an emulator inside your web browser! In contrast, if cloud software gets shut down, there is no way for you to preserve it, because you never had a copy of the server-side software, neither as source code nor in compiled form.


This is an excellent essay about software rights, developer freedoms and why the GPL is fit for a 1990 world, but not a 2020 world.  I recommend you go read it, because I'm about to veer sharply left and talk about something different that this raises.

When we trust SaaS providers, we tend to apply our existing models of security to them.  Can they keep the data secure, how do they separate job roles, what auditing is there.  But we don't consider the availability considerations, which are just as much part of our security and privacy mindsets.  If your company was thinking about using Zoom, you might be worrying about whether the video calls are secure, or the clients not a vector for malware, or whether the videos are recorded and stored in mainland china.  But equally worrying is the idea that your account might be suspended and you have no alternatives, and no ability to conduct customer facing meetings.

We tend to solve these issues through commercial contracts, and it's one of the reasons that enterprise software agreements are far more expensive, is that they generally include things that prevent the supplier from simply ceasing service without warning.  But if your team is using Shadow IT, or getting its own SaaS solutions, they're probably not benefiting from that in the same way.


## [RANSOM MAFIA. ANALYSIS OF THE WORLD’S FIRST RANSOMWARE CARTEL [pdf]](https://analyst1.com/file-assets/RANSOM-MAFIA-ANALYSIS-OF-THE-WORLD%E2%80%99S-FIRST-RANSOMWARE-CARTEL.pdf)

[https://analyst1.com/file-assets/RANSOM-MAFIA-ANALYSIS-OF-THE-WORLD%E2%80%99S-FIRST-RANSOMWARE-CARTEL.pdf](https://analyst1.com/file-assets/RANSOM-MAFIA-ANALYSIS-OF-THE-WORLD%E2%80%99S-FIRST-RANSOMWARE-CARTEL.pdf)

> In February 2021, a multinational law enforcement task-force arrested several Ukrainian
> men for supporting a long-standing ransomware gang known as Twisted Spider. The
> gang, first seen in May 2019, is behind high-dollar enterprise ransomware attacks.
> Unfortunately, the arrests had little impact, and several weeks later, in March 2021,
> Twisted Spider operations continued. Twisted Spider often makes headlines, but it’s not
> only due to their attacks. In June 2020, the gang issued a press release, claiming they
> joined forces with several other well-known ransomware attackers to create a criminal
> cartel. If this is true, this collaborative partnership, sharing resources and revenue, would
> pose a far greater threat to the community than attacks from smaller individual gangs by
> themselves.
> 
> Analyst1 produced this report to address whether or not the Cartel actually exists, as
> well as to help analysts better understand and defend against advanced ransomware
> attackers.
> 
> [...]
> 
> The gangs who make up the Cartel originate from eastern Europe and primarily speak
> Russian, based on posts made to underground criminal forums. Interestingly, all of the
> gangs build checks and balances into their ransomware to ensure that the payload does
> not execute on Russian victims. Here, the malware checks if the system language matches
> a dialect spoken in the Commonwealth of Independent States (CIS), which formerly made
> up the Soviet Union. Advanced attackers will often even purposely place false flags into
> their operations to lead investigators astray. However, the Cartel gangs do little to hide
> the fact they speak Russian, and they go out of their way not to target victims within
> affiliated Russian territories


This is a really good bit of analysis of a pervasive ransomware operator. It's worth noting just how much money they are taking, and building some assumptions about their ability to invest some of that in technology, in hosting and C2 infrastructure.  
Secondly, it's interesting to note that the vast majority of the work by 3 of the 4 gangs is reliant on initial compromise through those old favourites, phishing emails, illegitimate attachments and the use of CobaltStrike.  If you can protect against those attack mechanisms, you'll go a long way to defending against even reasonably advanced ransomware gangs like this one.


## [Public Report – VPN by Google One: Technical Security & Privacy Assessment – NCC Group Research](https://research.nccgroup.com/2021/04/08/public-report-vpn-by-google-one-technical-security-privacy-assessment/)

[https://research.nccgroup.com/2021/04/08/public-report-vpn-by-google-one-technical-security-privacy-assessment/](https://research.nccgroup.com/2021/04/08/public-report-vpn-by-google-one-technical-security-privacy-assessment/)

> During the fourth calendar quarter of 2020 and the first calendar quarter of 2021, NCC Group conducted an in-depth review of the VPN by Google One virtual private network system. The focus of the engagement was to assess the product’s technical security properties and review its associated privacy claims.


This is a nice writeup of the Google One VPN, provided to users of Android who have an account with Google.  The VPN infrastructure looks pretty solid, and the areas of concern were around the mechanisms that Google uses to disassociate the VPN traffic with your Google identity.

The seeming reason for this is that Google's VPN service wants to make people safer, which creates a better internet, which is better for Google's other business... ads.

But if people think that Google will track their traffic with the VPN, they might not use it, so Google has done a number of nifty things to try to give the VPN client pretty strong confidence that it's not tracking you.

Of course, the cookies saved in the phones browser, the websites you visit and all that other rich internet exhaust that you leave behind as you browse the web will almost certainly identify you, but it looks like the VPN won't by itself.


## [Behind GitHub's new authentication token formats - The GitHub Blog](https://github.blog/2021-04-05-behind-githubs-new-authentication-token-formats/)

[https://github.blog/2021-04-05-behind-githubs-new-authentication-token-formats/](https://github.blog/2021-04-05-behind-githubs-new-authentication-token-formats/)

> Many of our old authentication token formats are hex-encoded 40 character strings that are indistinguishable from other encoded data like SHA hashes. These have several limitations, such as inefficient or even inaccurate detection of compromised tokens for our secret scanning feature. We continually strive for security excellence, so we knew that token detection was something we wanted to improve. How could we make our tokens easier to identify and more secure?
> 
> Without further ado, here are the design decisions behind our new authentication token formats that let us meet both goals.
> 
> Identifiable prefixes
> 
> As we see across the industry from companies like Slack and Stripe, token prefixes are a clear way to make tokens identifiable. We are including specific 3 letter prefixes to represent each token, starting with a company signifier, gh, and the first letter of the token type. The results are:
> 
> ghp for GitHub personal access tokens
> gho for OAuth access tokens
> ghu for GitHub user-to-server tokens
> ghs for GitHub server-to-server tokens
> ghr for refresh tokens
> Additionally, we want to make these prefixes clearly distinguishable within the token to improve readability. Thus, we are adding a separator: _. An underscore is not a Base64 character which helps ensure that our tokens cannot be accidentally duplicated by randomly generated strings like SHAs.


This is a really nice bit of security design from Github.  By recognising that the token itself is opaque, it means that they can encode more information into the token which makes it easier to find and identify in public usage. 


## [Principles for Managing a Remote Team - Jay Signorello](https://jaysignorello.com/management/remote-work/principles-for-managing-a-remote-team/)

[https://jaysignorello.com/management/remote-work/principles-for-managing-a-remote-team/](https://jaysignorello.com/management/remote-work/principles-for-managing-a-remote-team/)

> 8) Promote a culture of documentation
> I’ve never been on a team that hates having existing documentation to aid in projects, especially when a project was inherited by the team.
> 
> Now ask that same team to document their project on top of their existing deadlines and you’re likely going to get in some heated debates.
> 
> From what I’ve seen, it’s usually a problem of getting started and facilitation. Many individual contributors simply don’t have the time to think through outlining and organizing thoughts of a big project.
> 
> This is where you come in. Help get the team started and add some documentation of your own. You’ll be amazed how quickly your team will jump in and start contributing. Overtime, things will get messy and outdated. Pitch in to keep it organized.
> 
> Your efforts won’t be wasted either. Employees will find answers to questions faster, allowing them to get more done. An added bonus is they won’t be distracting other team members with basic questions.
> 
> As your organization brings in new employees and teams are reorganized to meet the growing demands, this documentation will serve as a way to ramp up new members.


There's huge amounts of change in remote first or mostly remote teams that needs to happen.  But one of the things that's been driven home to me over the last 9 months is how teams who operate in person all the time can get by without good documentation and a knowledge base.

It doesn't matter whether it's just a shared google doc, or a full fledged wiki, but you need something that enables staff to put down their ideas and knowledge.  In person it's really easy to pick these things up by kitchen conversations, but when you are remote, and especially as you become asynchronous, the value of internal comms becomes even more important.


