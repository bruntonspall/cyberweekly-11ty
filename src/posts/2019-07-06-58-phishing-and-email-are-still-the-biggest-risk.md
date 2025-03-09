---
title: "58 - Phishing just works"
date: 2019-07-06
description: "Remember from the [Verizon Data Breach survey](https://enterprise.verizon.com/en-gb/resources/reports/dbir/2019/results-and-analysis/) earlier on in the year [featured in Cyber Weekly 51](https://www.cyberweekly.net/what-does-cyberwar-actually-mean), 94% of malware is delivered by email, and Phishing is still the most common threat action carried out in breaches."
permalink: /phishing-and-email-are-still-the-biggest-risk/
---

Remember from the [Verizon Data Breach survey](https://enterprise.verizon.com/en-gb/resources/reports/dbir/2019/results-and-analysis/) earlier on in the year [featured in Cyber Weekly 51](https://www.cyberweekly.net/what-does-cyberwar-actually-mean), 94% of malware is delivered by email, and Phishing is still the most common threat action carried out in breaches.

This week has seen a glut of news and stories about phishing that went well, phishing attacks that got detected and more ransomware attacks.  Although it's not been publicly confirmed yet, but I'd wager that the most likely source of infection for those ransomware attacks was an email with either an attachment or link to malware in it.

Traditional advice has been not to click suspicious links, but as has been shown time and time again, normal users can't tell suspicious from normal, and since their job is to receive email, open the documents or click the links, it is advice that just doesn't work.

Modern systems can perform link and malware detonation, checking links against known URL blacklists, and opening attachments in a VM and checking the system log to discover if anything weird happens.  With the addition of modern up to date browsers (Firefox patched their 0-day for javascript within days, but whether that has been installed on corporate devices is another matter), and modern protection on operating systems, you should be making it hard for attackers to get malware onto your systems.

Of course, when it does happen, ransomware is proving more and more popular.  The only reason I can see to pay the ransom is if your critical corporate data is not backed up anywhere and you would lose more data than the ransom is worth.  Backing up your shared file drives, and of course, moving to cloud based productivity suites should give you a healthy buffer against ransomware attacks and ensure that you can clean down your systems and get fixed.  Cloud based productivity tools will also mean that while your corporate IT system is infected, your staff can continue working from their own devices, from home, from coffeeshops or from shared office locations.

Sadly, many security people see all of these things as bad security practices.  The fear of upstream updates breaking systems mean they don't patch, and the fear of data loss from bad employees means that access to any corporate data from any device that isn't rigidly controlled by IT is often forbidden.  The use of compensatory controls, such as checking a devices security posture and patch levels is seen as not good enough for protecting corporate data, and yet would give significant business benefit and improve recovery capability in the event of the worst happening

## [John Deere's Promotional USB Drive Hijacks Your Keyboard - VICE](https://www.vice.com/en_us/article/pajv5k/john-deere-promotional-usb-drive-hijacks-your-keyboard)

[https://www.vice.com/en_us/article/pajv5k/john-deere-promotional-usb-drive-hijacks-your-keyboard](https://www.vice.com/en_us/article/pajv5k/john-deere-promotional-usb-drive-hijacks-your-keyboard)

> A Reddit user said he got one of these USB drives and noticed the weird behavior. A John Deere spokesperson later confirmed that the company has made USB drives designed to act this way.
> 
> “The device itself, it’s pretty ingenious, actually,” the Reddit user said. “It’s an HID-compliant keyboard that, when connected detects what platform it’s on and automatically sends a keyboard shortcut to open a browser, and then it barfs the link into the address bar.”
> 
> Ken Golden, John Deere’s director of public affairs, said that the company has distributed these kind of USB drives in the past, but stressed that their intention is not to do anything malicious.
> 
> “Deere is deeply committed to all aspects of data security and has never used a USB device to interfere with or monitor the use of any user’s personal computer or remove or observe any data or information on any user’s computer,” Golden wrote in an email. “Based on our review of the video used to exemplify the USB device comment about Deere, the video shows products and design of our website that are not current and appear to be several years old.”


John Deere are a large manufacturer of agricultural machinery which thanks to [a very catchy country song](https://www.youtube.com/watch?v=1kpO7woOopM) is connected in my head with the american country dream.  The fact that they produced USB flash drives that look a lot like a normal flash drive, but actually take over your computer to send you to their website amused me quite a lot this week.

Remember, don't plug random or untrusted USB devices into your computer, you can't tell what they are going to do just by looking at them.


## [NASA and Homeland Security just passed their government IT exams – and we really mean *just*](https://www.theregister.co.uk/2019/06/28/us_government_it_assessments/)

[https://www.theregister.co.uk/2019/06/28/us_government_it_assessments/](https://www.theregister.co.uk/2019/06/28/us_government_it_assessments/)

> "For the second scorecard in a row, there are no agencies receiving a failing grade," noted committee chairman Rep Gerald Connolly (D-VA). "While there are no A grades on this scorecard, the Department of Labor (B-) and the US Agency for International Development (B-) would have each received an A+ if they had changed their reporting structure to allow for their chief information officers to report to the head or deputy head of the agency."


(Joel) A few things to potentially unpick here but I'll keep it pithy with just two observations:

It is interesting to see the significant weight placed on the reporting line for Chief Information Officers (CIO) in US government departments. CIOs in UK government do not report directly to Permanent Secretaries (more like a COO or CFO). Will we the UK see this shift in reporting? What differences could such changes make?

Cabinet Office's "bi-annual" Departmental Security Health Check is an interesting... experience. I would love to see similar published scoring like our cousins across the pond. Comparisons between internal assessments, Cabinet Office assessments and external audits however may simply be too contentious so I'll park that idea under "Kickstarter Level 9 stretch goal".

[Original 'scorecard'](https://oversight.house.gov/sites/democrats.oversight.house.gov/files/Scorecard%208.0.pdf) (one-pager)


## [Hey advertisers, track THIS | The Firefox Frontier](https://blog.mozilla.org/firefox/hey-advertisers-track-this/)

[https://blog.mozilla.org/firefox/hey-advertisers-track-this/](https://blog.mozilla.org/firefox/hey-advertisers-track-this/)

> You should still have control over what advertisers know about you—if they know anything about you at all—which can be tough when web trackers operate out of sight.
> 
> That’s why we made Track THIS: to bring that out-of-sight tracking front and center. Step into someone else’s shoe ads for a while by opening up 100 tabs at once.


This is an interesting idea, more of a stunt than anything, as they kind of acknowledge.  Simply visiting the websites for luxury goods shouldn’t be sufficient to change your browser cookies.  Additionally, I noticed that post GDPR, simply visiting the sites didn’t necessarily set the cookies, instead you had to of course, accept the GDPR cookie notice to get the cookies set.


## [18F: Digital service delivery | You might not be as agile as you think you are](https://18f.gsa.gov/2019/05/29/you-might-not-be-as-agile-as-you-think-you-are/)

[https://18f.gsa.gov/2019/05/29/you-might-not-be-as-agile-as-you-think-you-are/](https://18f.gsa.gov/2019/05/29/you-might-not-be-as-agile-as-you-think-you-are/)

> You’re trying to “do Agile,” instead of being agile…
> 
>  * You’re doing scrum ceremonies (sprints, stand ups, retros), but not seeing any change in outcomes
>   * Your planning meetings are focused on listing out specific implementation details rather than expected outcomes
>     [snip]
>   * You’re working with a vendor and you don’t have insight into the work being planned or accomplished by them on an ongoing basis
> 
> 


Reminder that it’s not agile if all you are doing is writing post it notes, doing stand ups and chunking your work into two week sprints.  To be doing agile you need to be releasing your software or product to users on a regular basis, and then gathering feedback on whether it meets the needs of the users.  

Generally this is a nice list for detecting agile cargo culting, where teams are copying the behaviours of agile teams without understanding the reasoning behind those behaviours.


## [How Verizon and a BGP Optimizer Knocked Large Parts of the Internet Offline Today](https://blog.cloudflare.com/how-verizon-and-a-bgp-optimizer-knocked-large-parts-of-the-internet-offline-today/)

[https://blog.cloudflare.com/how-verizon-and-a-bgp-optimizer-knocked-large-parts-of-the-internet-offline-today/](https://blog.cloudflare.com/how-verizon-and-a-bgp-optimizer-knocked-large-parts-of-the-internet-offline-today/)

> DQE announced these specific routes to their customer (AS396531 - Allegheny Technologies Inc). All of this routing information was then sent to their other transit provider (AS701 - Verizon), who proceeded to tell the entire Internet about these “better” routes. These routes were supposedly “better” because they were more granular, more specific. 
> 
> The leak should have stopped at Verizon. However, against numerous best practices outlined below, Verizon’s lack of filtering turned this into a major incident that affected many Internet services such as Amazon,  Linode and Cloudflare. 
> 
> What this means is that suddenly Verizon, Allegheny, and DQE had to deal with a stampede of Internet users trying to access those services through their network. None of these networks were suitably equipped to deal with this drastic increase in traffic, causing disruption in service. Even if they had sufficient capacity DQE, Allegheny and Verizon were not allowed to say they had the best route to Cloudflare, Amazon, Linode, etc...


BGP is still badly broken, and more frustratingly, the need to support people who don't upgrade to more secure protocols means that it's really hard to fix.  This was a mistake by all accounts, but this is definitely something that nation states would use or consider as part of a hybrid warfare strategy.


## [GOTCHA: Taking phishing to a whole new level – intigriti – Medium](https://medium.com/intigriti/gotcha-taking-phishing-to-a-whole-new-level-72eda9e30bef)

[https://medium.com/intigriti/gotcha-taking-phishing-to-a-whole-new-level-72eda9e30bef](https://medium.com/intigriti/gotcha-taking-phishing-to-a-whole-new-level-72eda9e30bef)

> GOTCHA is a UI redressing attack that allows attackers to extract valuable information from API endpoints. It requires a significant amount of user interaction, but could end up compromising a user’s plaintext password when executed successfully.


This is a wonderfully cute phishing attack.  Despite the fact that browsers prevent the evil webpage from actually accessing the content, this attack uses the users expectations of websites, by showing the user several iFrames of the content of their password styled to look like a Captcha.

This way, the user's browser is correctly and validly looking at their password in the password manager, and typing it into an evil website, disclosing it to the bad guys.


## [Firefox 0-day Used in Targeted Attacks Against Cryptocurrency Firms](https://www.bleepingcomputer.com/news/security/firefox-0-day-used-in-targeted-attacks-against-cryptocurrency-firms/)

[https://www.bleepingcomputer.com/news/security/firefox-0-day-used-in-targeted-attacks-against-cryptocurrency-firms/](https://www.bleepingcomputer.com/news/security/firefox-0-day-used-in-targeted-attacks-against-cryptocurrency-firms/)

> The employees of Coinbase and other cryptocurrency firms were the target of an attack utilizing a recent Firefox zero-day and malware payloads in order to gain access to victim's computers, networks, and sensitive information.
> 
> This past week, Mozilla released an emergency Firefox update to fix a critical remote execution vulnerability that was actively used in targeted attacks in the wild. This bug was given a CVE ID of CVE-2019-11707 and was stated to have been reported by both Google Project Zero vulnerability researcher Samuel Groß and Coinbase security.


This is a more detailed breakdown of the Firefox vulnerability that was used in the Coinbase attack.  What's interesting here is that there's both a chain of 2 0-day vulnerabilities used in Firefox to get Firefox to download a further piece of malware that included an OSX piece of malware.

While the OSX malware doesn't seem to be particularly advanced, however the command and control infrastructure is connected with an earlier campaign that exploited 0-days in WinRar for some windows malware.

This all points to some reasonably advanced capabilities being deployed in attempting to get access to corporate data and backend systems behind a number of cryptocurrency firms.


## [I was 7 words away from being spear-phished | Robert Heaton](https://robertheaton.com/2019/06/24/i-was-7-words-away-from-being-spear-phished/)

[https://robertheaton.com/2019/06/24/i-was-7-words-away-from-being-spear-phished/](https://robertheaton.com/2019/06/24/i-was-7-words-away-from-being-spear-phished/)

> I don’t think that it was careless of me to click on the link in the phishing email. Browser 0-days that are exploited by a sub-domain of cam.ac.uk aren’t in my personal threat model, and I think that this is sensible. Security always has to be balanced with pragmatism, and not everything can be GPG-signed by a web of trust that leads back to Bruce Schneier. My Twitter DMs are open for splenetic criticisms.
> 
> Nonetheless, this episode has left me feeling incredibly uneasy. Even though my story ends safely, I still fell for a phishing attack hook and line, if not also sinker. It was blind chance that the attack vector was a 0-day for a piece of software that I don’t use, rather than something more run-of-the-mill. After a few more back and forths I think I would have probably have enabled macros on any Microsoft Office documents that Gregory Harris sent me, and I might even have run code for him if he said it was part of an entry into the competition. As I mentioned I don’t have any cryptocurrency to lose, but I sure do have money in my online banking accounts that I’d like to keep there.


We can all fall for a well executed social engineering attack.  This one relied on human curiosity and the flattering of our ego.  Pretty much anyone would be flattered to be asked to judge a prize, even if it's in an area that they aren't skilled in, and even if they think it was sent to the wrong person, they are going to click the link to have a look at what other people's lives are like.


## [Second Florida city pays giant ransom to ransomware gang in a week | ZDNet](https://www.zdnet.com/google-amp/article/second-florida-city-pays-giant-ransom-to-ransomware-gang-in-a-week/?__twitter_impression=true)

[https://www.zdnet.com/google-amp/article/second-florida-city-pays-giant-ransom-to-ransomware-gang-in-a-week/?__twitter_impression=true](https://www.zdnet.com/google-amp/article/second-florida-city-pays-giant-ransom-to-ransomware-gang-in-a-week/?__twitter_impression=true)

> Despite the city's IT staff disconnecting impacted systems within ten minutes of detecting the attack, a ransomware strain infected almost all its computer systems, with the exception of the police and fire departments, which ran on a separate network.
> 
> Lake City government work has been crippled for nearly two weeks because of the incident.
> 
> A ransom demand was made a week after the infection, with hackers reaching out to the city's insurance provider -- the League of Cities, which negotiated a ransom payment of 42 bitcoins last week


Paying the ransom has always been discouraged in reporting of Ransomware in previous years, but over the last few weeks we are seeing lots of reports of people paying the ransom.  In this case, what's interesting is that the ransomware authors contacted the cyber insurance firm directly to negotiate payment.  Whether that's because they knew the insurers would pay out, or simply to speed up the process who can say?  But it doesn't bode well for ransomware attacks over the next few years, as it will become a very profitable form of attack very quickly.

Of course, if you pay the ransom in "marked bills", such as via tracable bitcoin, I'll be fascinated to see if in a few months some of these attackers are caught because of their inability to cash out without leaving digital traces around. 


