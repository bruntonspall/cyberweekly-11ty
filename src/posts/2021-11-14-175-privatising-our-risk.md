---
title: "175 - Privatising our risk"
date: 2021-11-14
description: "Ciaran Martin makes excellent points today in this assessment that we have privatised our security risks in a way that prevents control."
permalink: /privatising-our-risk/
---

Ciaran Martin makes excellent points today in this assessment that we have privatised our security risks in a way that prevents control.

Ransomware as a scourge has prompted more organisations and nations to action than almost any other cybersecurity incident type than I can think of. 

I suspect that the fact that the impact of these attacks is felt not just on private businesses, but on the economy and on political goodwill of citizens for their leaders ensures that action must be taken.  Most ransomware operations are highly visible, and organisations stop being able to deliver basic services and often have to speak out publicly when they happen.  This creates a sense of action in the average citizen that creates a desire for politicians to be seen to be doing something.

But the big question is how to make organisations take the risk seriously.  I made the point in a recent conversation that many organisations take an acute risk quite seriously.  When they see ransomware pointing at them, they'll act to shore up their defences, and patch their endpoints. 

But organisations fail to take the more slow burning chronic risk seriously.  Any assessment of the number of compromises and breaches over the last decade shows a huge increase in the number and severity of breaches.  But that changing environment is complex. Do we see more breaches because there are more attacks, or because more companies are online? Or do we see them because reporting requirements changed?  Secondly, that changing environment feels like an externality to most organisations.  If you own a large enterprise, from a chain of pubs to a grocery delivery service or oil pipeline, then how can you grapple with the questions of whether criminal gangs are engaging in increased cyber attacks?

Organisations put aside often less than 1% of their annual budget on security, and in [some critical infrastructure companies, it can be as low as 0.2%](https://cybersecurityventures.com/cybersecurity-market-report/).  An acute threat can be handled by short term interventions, but chronic threats require organisational strategies, and they require long term investment, both in individual companies, but also in entire industries.

Furthermore, as Ciaran points out, the health of a nation can depend on the health of its constituent parts.  There's a requirement to act, but it often seems that there are few politically acceptable levers that are available to anyone.  We need to be able to articulate that with the privatisation of risk comes a responsibility to act on that risk, and the requirement for these organisations act not just on the acute risk they can see, but also on the chronic systemic risk.

We need to be better able to defend as one when it comes to these wider industries, and that means better sharing of information, better shared capabilities, and a better acknowledgement of the wide systemic risks.

## [Ex-security chief: we have privatised our cyber security. The winners are the hackers - Prospect Magazine](https://www.prospectmagazine.co.uk/science-and-technology/privatised-cyber-security-hackers-ciaran-martin-gchq-revil-darkside)

[https://www.prospectmagazine.co.uk/science-and-technology/privatised-cyber-security-hackers-ciaran-martin-gchq-revil-darkside](https://www.prospectmagazine.co.uk/science-and-technology/privatised-cyber-security-hackers-ciaran-martin-gchq-revil-darkside)

> When the Queen opened the new National Cyber Security Centre in 2017, a senior government minister confided to me, at the margins of the festivities, their concern that the launch of this new department in GCHQ to fight digital threats represented “the nationalisation of cyber security.” But the opposite problem is emerging: we are privatising national security risk.
> 
> The US fuel crisis is a case in point. When Colonial Pipeline was hit, it wasn’t the pipeline controls that were hacked but the company’s corporate systems. It was the company, not the hackers, who shut down the pipeline, apparently because it could not run its services profitably because of the damage done to its business processes.
> 
> This was a decision that the company was perfectly entitled to take. But while it did not consult the US government beforehand, it fell to the US government to deal with the fallout. Washington had to suspend safety regulations concerning the transport of fuel by road and issue guidance to citizens to prevent panic buying and the storing of fuel in unsafe containers. It then sent the FBI after the hackers. Yet it had no involvement in any of the decisions that made such actions necessary; those were taken by the firm’s executives.
> 
> Colonial, it should be said, broke no rules. And that’s the point. Insufficient protection of its pipeline—a critical national asset—caused social disruption that clearly met the threshold of a national security threat. But there is nothing—yet—in the regulations governing this critical sector that requires firms to do better (and Republicans in Washington are starting to push back against suggestions for tighter controls). The unspoken message behind the Colonial case is that businesses can choose how to respond, whatever the consequences, and the government will pick up the tab.
> 
> The real lesson of 2021 is that digital vulnerabilities in a range of private and public organisations can be exploited to cause significant disruption and, potentially, serious social harm. That lesson will not be lost on authoritarian states that have better cyber capabilities than a few greedy Russian thugs. This year has revealed, among other things, that you can cause energy chaos in parts of America and a healthcare crisis in an EU member state with a few lines of malicious code of medium sophistication. 


Excellent analysis by Ciaran Martin, who used to be the chief executive of the NCSC.

While ransomware is profitable, criminal gangs will continue to use it until either it's no longer profitable or it's too risky, in which case they'll find another mechanism to continue their aims.


## [Hoax Email Blast Abused Poor Coding in FBI Website – Krebs on Security](https://krebsonsecurity.com/2021/11/hoax-email-blast-abused-poor-coding-in-fbi-website/)

[https://krebsonsecurity.com/2021/11/hoax-email-blast-abused-poor-coding-in-fbi-website/](https://krebsonsecurity.com/2021/11/hoax-email-blast-abused-poor-coding-in-fbi-website/)

> Until sometime this morning, the LEEP portal allowed anyone to apply for an account. Helpfully, step-by-step instructions for registering a new account on the LEEP portal also are available from the DOJ’s website. [It should be noted that “Step 1” in those instructions is to visit the site in Microsoft’s Internet Explorer, an outdated web browser that even Microsoft no longer encourages people to use for security reasons.]
> 
> Much of that process involves filling out forms with the applicant’s personal and contact information, and that of their organization. A critical step in that process says applicants will receive an email confirmation from eims@ic.fbi.gov with a one-time passcode — ostensibly to validate that the applicant can receive email at the domain in question.
> 
> But according to Pompompurin, the FBI’s own website leaked that one-time passcode in the HTML code of the web page.
> 
> 
> Pompompurin said they were able to send themselves an email from eims@ic.fbi.gov by editing the request sent to their browser and changing the text in the message’s “Subject” field and “Text Content” fields.
> 
> “Basically, when you requested the confirmation code [it] was generated client-side, then sent to you via a POST Request,” Pompompurin said. “This post request includes the parameters for the email subject and body content.”
> 
> Pompompurin said a simple script replaced those parameters with his own message subject and body, and automated the sending of the hoax message to thousands of email addresses.


This is really poor security.  In essence this appears to be an open relay on the internet.  A script that you can call parameters letting you set the to address, the text content, and the subject, and it will send an email from itself. 

Given the way the LEEP portal is setup, this looks like a poor integration between the LEEP and the FBI's Identity System.  Normally this kind of call would be transmitted "at the backend", but the server, and should be authenticated by the LEEP's API key.  It seems likely that the developers instead of making the call direct from the LEEP servers, decided to generate the URL to call on the IC servers and then sent it to the users browser to call the IC servers direct.  This would have enabled the hackers to intercept that call and find the API key or otherwise modify the parameters to send emails themselves.

Sadly, this kind of thing does happen, and the important thing to remember is that this is not the end of the world.  We don't have a good lexicon for different levels of computer compromise, so while there will be headlines about "FBI computers hacked", which is broadly true, this doesn't necessarily represent that hackers have access to central FBI systems or any more authorisation than that, just that they can confuse the email sending system to send emails on their behalf.

Of course, this is all assuming that Brian Krebs' source was telling the truth about their actions, and it's not beyond the realm of possibility that someone has either claimed undue credit, or claimed to use a much simpler bug to hide a more advance compromise.  But the technical details seem to stack up here.


## [“Hacker X”—the American who built a pro-Trump fake news empire—unmasks himself | Ars Technica](https://arstechnica.com/information-technology/2021/10/hacker-x-the-american-who-built-a-pro-trump-fake-news-empire-unmasks-himself/)

[https://arstechnica.com/information-technology/2021/10/hacker-x-the-american-who-built-a-pro-trump-fake-news-empire-unmasks-himself/](https://arstechnica.com/information-technology/2021/10/hacker-x-the-american-who-built-a-pro-trump-fake-news-empire-unmasks-himself/)

> What saved me was a couple [of Koala Media] employees," he added. "One came into my office and closed the door and looked at me and said, 'You don't actually believe this stuff, do you?' and I let out a sigh of relief when I said, 'God, no'—and laughed. It became an ongoing joke."
> 
> From that moment onward, the hacker and office staff would joke about the stuff they were being assigned to write—like a conspiracy-laden writeup on "chemtrails" or a piece on "lemons curing cancer"—thinking that only a small "ultracrazy" percentage of readers actually believed what was being written
> 
> […]
> 
> Through it all, Willis did what he was hired to do: he put his technical skills in the service of boosting Koala's reach—by any means possible.
> 
> The basic approach involved the creation of a massive syndication network of hundreds of specialty "news" websites, where articles from the main Koala website could be linked to or syndicated. But these additional websites were engineered so that they looked independent of each other. They were "a web ring where the websites didn't look like they had any real associations with each other from a technical standpoint and couldn't be traced," said Willis.
> 
> Each fake news website was on a separate server and had a unique IP address. Each day's stories were syndicated out to the fake news sites through a multistep sync operation involving "multiple VPNs" with "multiple layers of security." Eventually, each public-facing fake news site received its daily content payload, and the stories would go live at scheduled times. In addition to Americans, Willis' team also comprised outsourced web developers working from Mexico, Eastern Europe, South Africa, and Taiwan.
> 
> "I oversaw everything and even had stacks of SIM cards purchased with cash to activate different sites on Facebook since it was needed at that point in time," admitted Willis. "Every website had a fake identity I made up. I had them in a sheet where I put the name, address, and the SIM card phone number. When I accessed their account I created on Facebook, I would VPN into the city I put them in as living in. Everything attached to a website followed these procedures because you needed to have a 'real' person to create a Facebook page for the websites. We wanted no attachment, no trace of the original source. If anyone were to investigate who owned a page, they would be investigating a fake person."


This is both horrifying, but also technically fascinating.  Just how does a content farm operate, and what lengths do you need to go to?


## [Why Zero-Days Are Essential to Security - Randori](https://www.randori.com/blog/why-zero-days-are-essential-to-security/)

[https://www.randori.com/blog/why-zero-days-are-essential-to-security/](https://www.randori.com/blog/why-zero-days-are-essential-to-security/)

> We provide our customers with a highly realistic experience — from reconnaissance to compromise to actions on objectives. When the number of vulnerabilities disclosed per year exceeds 20,000 and in-the-wild exploitation of zero-day is commonplace, organizations require commensurate tools and techniques to test and defend themselves. That is why at Randori, our objective is to have capabilities on par with nation-state and criminal organizations, to utilize those capabilities against our customers with their authorization, and to do so at scale — providing not just a single organization, but the industry more broadly, the opportunity to learn from a trusted adversary.
> 
> To do this, we:
> 
> * Recruit and hire top offensive security talent
> * Acquire N-day and other capabilities from outside parties
> * Actively invest in discovering zero-day and other novel attack capabilities
> * Leverage these capabilities to benefit our customers
>  
> 
> Together, these capabilities enable us to phish, crack passwords, use publicly disclosed vulnerabilities, conduct novel research, and develop techniques, capabilities, and processes just like those used by threat actors. We find and utilize previously unknown vulnerabilities in our customers’ applications and environments.


There was a lot of grumbling on infosec twitter this week about a vulnerability that [Randori disclosed that they didn't disclose for 9 months](https://www.randori.com/blog/cve-2021-3064/) and a lot of questions around ethics in information security.

Whether or not you think it's ethically correct to sit on a known vulnerability and not disclose it to the vendor, the point that Randori make is that this isn't a red team "cheating".  This is a red team, with the knowing acceptance of the client, more accurately simulating an adversary.  Randori don't claim to run a plain old pen test against your infrastructure, they actively say that they might use undisclosed or unpatched vulnerabilities, in order to test your more advanced defences.

If you want a pen test that colours within the lines, and doesn't break any "rules of engagement", then you'll know that you didn't do anything simple wrong (and lord knows we have enough examples of people failing to secure the simple things).  But that doesn't tell you that your defences are actually capable against a really capable adversary.


## [Google Caught Hackers Using a Mac Zero-Day Against Hong Kong Users](https://www.vice.com/en/article/93bw8y/google-caught-hackers-using-a-mac-zero-day-against-hong-kong-users)

[https://www.vice.com/en/article/93bw8y/google-caught-hackers-using-a-mac-zero-day-against-hong-kong-users](https://www.vice.com/en/article/93bw8y/google-caught-hackers-using-a-mac-zero-day-against-hong-kong-users)

> Erye Hernandez, the Google researcher who found the hacking campaign and authored the report, wrote that TAG discovered the campaign in late August of this year. The hackers had set up a watering hole attack, meaning they hid malware within the legitimate websites of “a media outlet and a prominent pro-democracy labor and political group” in Hong Kong. Users who visited those websites would get hacked with an unknown vulnerability—in other words, a zero-day—and another exploit that took advantage of a previously patched vulnerability for MacOS that was used to install a backdoor on their computers, according to Hernandez. 
> 
> Apple patched the zero-day used in the campaign in an update pushed out on September 23, according to the report. 
> 
> Apple did not immediately respond to a request for comment. 
> 
> Google’s researchers were able to trigger the exploits and study them by visiting the websites compromised by the hackers. The sites served both iOS and MacOS exploit chains, but the researchers were only able to retrieve the MacOS one. The zero-day exploit was similar to another in-the-wild vulnerability analyzed by another Google researcher in the past, according to the report. 
> 
> In addition, the zero-day exploit used in this hacking campaign is “identical” to an exploit previously found by cybersecurity research group Pangu Lab, Huntley said. Pangu Lab’s researchers presented the exploit at a security conference in China in April of this year, a few months before hackers used it against Hong Kong users.  
> 
> “It was presented as an exploit targeting Big Sur, but we discovered that it also worked on Catalina,” according to Huntley. (Google classified this as a zero-day because it was unpatched in Catalina, a version of MacOS that was supported at the time.)


Watering hole attacks are quite nasty.  Done well, like this one, and all the target has to do is visit a website and their device is compromised.  So far these seem mostly restricted to either state based actors and thus highly targeted, or on occasion crptomining in-browser exploits.  What we've not seen yet is a criminal gang looking for widespread damaging infection, but give it a few years and that will become a possibility (assuming someone can work out how to monetise that of course).

Of course, fingers are pointing at the fact that this vulnerability was presented at a Chinese security conference, although given that the writeup was then posted publicly, I think that's a little bit smoke and mirrors.  The location of the conference has no bearing on who was able to read the presentation and see the proof of concept demonstrated there.  The outcome would have been the same if the same exploit was presented at any other security conference as well.


## [Kelly Shortridge on Twitter: "Loved that @R_Thaler used phishing warning clutter as an example of “sludge” — friction in design that leaves users worse off — in his presentation last night. It’s quite rational for users to ignore cognitive detritus and yet sludge often seems the default design in infosec. https://t.co/5E7zrALSHT" / Twitter](https://twitter.com/swagitda_/status/1456249976107974660)

[https://twitter.com/swagitda_/status/1456249976107974660](https://twitter.com/swagitda_/status/1456249976107974660)

> Loved that 
> @R_Thaler
>  used phishing warning clutter as an example of “sludge” — friction in design that leaves users worse off — in his presentation last night.
> 
> It’s quite rational for users to ignore cognitive detritus and yet sludge often seems the default design in infosec.





## [The Unfulfilled Promise of Serverless - Last Week in AWS](https://www.lastweekinaws.com/blog/the-unfulfilled-promise-of-serverless/)

[https://www.lastweekinaws.com/blog/the-unfulfilled-promise-of-serverless/](https://www.lastweekinaws.com/blog/the-unfulfilled-promise-of-serverless/)

> That’s what this article is about: Say what you will about serverless, it’s failed to live up to its promise and hasn’t proved to be particularly lucrative for anybody.
> 
> Serverless, but not portable
> First, let’s talk lock-in. Yes, yes, every major cloud provider has a FaaS offering, but here’s what they don’t tell you: The bulk of your time building serverless applications will not be spent writing the application logic or focusing on the parts of your code that are in fact the differentiated thing that you’re being paid to work on. It just flat out won’t. Instead you’ll spend most of your time figuring out how to mate these functions with other services from that cloud provider. What format is it expecting? Do you have the endpoints correct? Is the security scoping accurate? Oh, it didn’t work? Time to embark on a microservices distributed systems murder mystery where the victim is another tiny piece of your soul, because getting coherent logs out of a CloudFront –> API Gateway –> Lambda configuration is CRAP.
> 
> That’s the kind of thing that isn’t portable anywhere. The ultimate expression of this problem can be observed in AWS’s Step Functions: There’s no equivalent elsewhere, so you’re well and truly stuck if you want to vacate the platform and happen to be using them.


Why hasn't serverless taken off as much as some of it's most enthusiastic supporters think it should have?  There's an obvious value that technologists see, but Corey here breaks down why that value just doesn't resonate with businesses and senior decision makers.


## [Andrew Blain and Paul Fitzmaurice | Connecting Strategy to Action - Anti-Patterns in OKRs](https://www.remoteaf.co/blogs/connecting-strategy-to-action-anti-patterns-in-okrs)

[https://www.remoteaf.co/blogs/connecting-strategy-to-action-anti-patterns-in-okrs](https://www.remoteaf.co/blogs/connecting-strategy-to-action-anti-patterns-in-okrs)

> OKRs with matrix management models
> 
> If... you’re trying to use OKRs with a matrix management model
> 
> Then… Go directly to management jail. Do not pass go, do not collect your bonus.
> 
> OKRs work really well in value-aligned operating models that are built around cross-functional teams who can deliver in a largely autonomous fashion. They are designed to cascade bi-directionally through an organisation, with leaders setting intent and teams telling leaders how they will get there.
> 
> They don’t work particularly well in organisations that have operating models built around functional hierarchies that use the project or business process metaphor for orchestration of value. Use of OKRs in these environments will likely lead to local optimisation of the functions at the expense of the system.
> 
> You could develop a workaround which creates temporary team structures that span your business functions and use Impact Mapping or something similar, but OKRs won’t work out of the box.


This is a good selection of OKR anti-patterns.  I've long appreciated the OKR system, but it's something that is really hard to deliver within a team structure if the wider management structure above your team doesn't use it.  If your CEO or C-level execs don't care about your OKR's, don't measure by them and wont trust and abide by them, then the value you get is far smaller.  Not so little that you shouldn't do them, but you can't do them the same way


## [These Deepfake Voices Can Help Trans Gamers | WIRED](https://www.wired.com/story/deepfake-voices-help-trans-gamers/)

[https://www.wired.com/story/deepfake-voices-help-trans-gamers/](https://www.wired.com/story/deepfake-voices-help-trans-gamers/)

> Modulate’s cofounders Mike Pappas and Carter Huffman initially thought the technology they term “voice skins” could make gaming more fun by letting players take on characters’ voices. As the pair pitched studios and recruited early testers, they also heard a chorus of interest in using voice skins as a privacy shield. More than 100 people asked if the technology could ease the dysphoria caused by a mismatch between their voice and gender identities.
> 
> “We realized many people don’t feel they can participate in online communities because their voice puts them at greater risk,” Pappas, Modulate’s CEO, says. The company is now working with game companies to provide voice skins in ways that offer both fun and privacy options, while also pledging to prevent them becoming a tool of fraud or harassment themselves.


While deepfake voices can be quite scary, there are lots of potential fraudulent possibilities, but it’s nice to also see the positive sides of this technology.  Enabling people to represent themselves online in the manner they choose.  There’s also the slight fun aside that you might be able to fully represent the character they are playing in games in the future as well.


## [The Business of Fraud: Deepfakes, Fraud’s Next Frontier](https://www.recordedfuture.com/deepfakes-frauds-next-frontier/)

[https://www.recordedfuture.com/deepfakes-frauds-next-frontier/](https://www.recordedfuture.com/deepfakes-frauds-next-frontier/)

> Deepfake technology used maliciously has migrated away from the creation of pornographic-related content to more sophisticated targeting that incorporates security bypassing and releasing misinformation and disinformation. Publicly available examples of criminals successfully using visual and audio deepfakes highlights the potential for all types of fraud or crime, including blackmail, identity theft, and social engineering.
> English- and Russian-language dark web forums were identified as the main sources for users to advertise, discuss, share, and purchase deepfake-related products, services, and topics. The most widely used forums were found to be low- to mid-tier forums that have lower barriers to entry, but activities were also found on high-tier forums. Deepfake topics were also identified on Turkish-, Spanish-, and Chinese-language forums.


I'm not sure that I buy this analysis 100%.  Looking at what subjects that people discuss on dark web forums is a good indication of certain areas of interest, but it doesn't mean that the technology is actually usable and profitable to use.  It means that it's interesting to people of a certain bent.  

There are lots of technologies that are absolutely fascinating, but ultimately useless in a business sense, the kinds of problems that people return to time after time, because they are fun and interesting, and they capture the imagination.

Deepfakes are definitely a transformative technology, but one that I suspect we over-estimate in the short term, and underestimate in the long term


