---
title: "70 - Tackling the insider threat"
date: 2019-09-21
description: "I've been reading [Edward Snowdon's autobiography (affiliate link)](https://amzn.to/2ABepeY) this week, and it's made me think about insider attacks quite a lot."
permalink: /tackling-the-insider-threat/
---

I've been reading [Edward Snowdon's autobiography (affiliate link)](https://amzn.to/2ABepeY) this week, and it's made me think about insider attacks quite a lot.

When we think of insiders, we tend to think of the Edward Snowdon style of attack.  The careful, manipulative liar who gets a job, specifically with a hostile motive in mind.  Whether you think he was right or wrong, he reinforced a set of insider threat models that have been abused for a long time.

I attended a brief training seminar on insider threats a few years back, and the examples given were those of the Burgess, Mclean, Blunt, Philby and Cairncross (the Cambridge Five), Daniel Ellsberg, Chelsea Manning and Edward Snowdon.  This is in spite of the fact that [CPNI's own review of 120 insider cases](https://www.cpni.gov.uk/system/files/documents/63/29/insider-data-collection-study-report-of-main-findings.pdf) showing that only 6% of insiders were motivated to apply for a role in order to get information, and that only a further 15% were recruited or influenced by outsiders.  Given that the study was of both public and private sectors, it still shows that 76% of insiders are people who make the decision to become an insider once working for an organisation.  I would hazard a guess that deliberate decision to join and being influenced by an outsider is far more common in the military and intelligence arms of the public sector and the private sector relating to it, than it is in any other area, so those ratios are probably inflated.

But the real insider threat for many of us is not the hostile insider.  It's the people we trust who are socially engineered into revealing information that they shouldn't.  It's malware infected devices that can act like an insider even if the user isn't malicious themselves, and it's misconfiguration and user error.  The [data breaches survey 2019](https://enterprise.verizon.com/en-gb/resources/reports/dbir/2019/results-and-analysis/) reminds us that nearly 40% of data breaches are error or mishandling. We can add to that misconfiguration, with databases being exposed online as a regular occurance, and increasingly the open source nature of code resulting in accidental misconfiguration.

Of course the scariest insider threat is that from a supplier.  I'm not even sure if we can accurately describe the software supply chain, let alone map it in 2019.  Software is written by humans, who are often outsourced from another company.  They use laptops, tools and software to write their code, store it on third party source code hosting repositories, and build it using third party build pipelines.  The code is then shipped to data centers, where it is run by third parties on your behalf and exposed to the internet via ISP's.  And of course each of these suppliers runs their own laptops, hardware, operating systems.  The idea that under all of this somewhere, there is a boundary where insecure people are outside, and only security approved things are allowed in and onto our network became unfeasible decades ago.

And yet, despite the huge impact of an insider, the actual incidents of real damaging insider threat is really rare.  We might spend millions on data loss prevention software, role based access controls and managed procurement processes to ensure that nobody buys slack for their teams which might allow collaboration outside the company and therefore accidental data loss.  But is this the best way to protect ourselves against this risk?  Is it even a risk we should worry about?  

I return to that 40% error and data mishandling figure, and realise that if we spent as much money on ensuring that email clients were intuitively obvious about the use of the CC field and the BCC field.  That we had modern digital tools for collaborating on documents and spreadsheets that meant that they didn't get emailed everywhere, maybe we'd be a lot better off.

## [Confidential data of 24.3 million patients discovered online - Help Net Security](https://www.helpnetsecurity.com/2019/09/18/confidential-patient-data/)

[https://www.helpnetsecurity.com/2019/09/18/confidential-patient-data/](https://www.helpnetsecurity.com/2019/09/18/confidential-patient-data/)

> Greenbone carried out an analysis of all medical image archiving systems connected to the public internet. These Picture Archiving and Communication Systems (PACS) servers are based on a protocol known as DICOM (Digital Imaging and Communications in Medicine), which – based on the IP protocol – makes it possible for medical professionals to access and share scans and other images. The DICOM standard dates back to the 1980s.
> 
> Dirk Schrader, cyber resilience architect at Greenbone Networks who lead the research said: “The data pertaining to millions of patients is there for anyone to access simply because of the careless configuration of these medical archiving servers. A significant number of these servers have no protection at all, they aren’t password protected and have no encryption. Indeed, everyday internet users could gain access to these servers with very little effort – there’s no need to write any code or deploy any specialist hacking tools.


People connect systems together to enable sharing and collaboration.  But of course access control is hard, often an expensive addon, and policies on sharing are often hard to create and enforce.  In this case, while it might have some identifiable information, what we are really talking about here is lots and lots of xray and CT scans, connected with someones name and social security number.  That could be bad, but it's not immediately obvious how an attacker would use it in any way.


## [Report: Ecuadorian Breach Reveals Sensitive Personal Data](https://www.vpnmentor.com/blog/report-ecuador-leak/)

[https://www.vpnmentor.com/blog/report-ecuador-leak/](https://www.vpnmentor.com/blog/report-ecuador-leak/)

> Led by Noam Rotem and Ran Locar, our team discovered the data breach on an unsecured server located in Miami, Florida. The server appears to be owned by Ecuadorian company Novaestrat.
> 
> Novaestrat is a consulting company that provides services in data analytics, strategic marketing, and software development.
> 
> The data breach involves a large amount of sensitive personally identifiable information at the individual level. The majority of the affected individuals seem to be located in Ecuador.
> 
> Although the exact details remain unclear, the leaked database appears to contain information obtained from outside sources.
> 
> These sources may include Ecuadorian government registries, an automotive association called Aeade, and Biess, an Ecuadorian national bank.
> 
> The breach was closed on September 11, 2019.
> 
> The data breach involves around 18 GB of data. As many as 20 million individuals may be impacted by this breach, although some of the data seems to involve individuals who are already deceased.
> 
> To give some context about the scale of this leak, Ecuador has a population of around 16 million people.


20 million records on 16 million people.  This here is the problem of government based digital identity in a nutshell.  Does that mean that there are 4 million extra records?  Or more likely does it mean that there are duplicate records for some citizens because they came from different sources such as different government departments.    We often think that the Government has some form of single identifier for us, but in reality, people like myself who have changed name in their life, will likely have 2 or more records in any given database.  When it comes to identity, knowing which one I am, and which one will be used to identify me is always going to be hard


## [Talos Blog || Cisco Talos Intelligence Group - Comprehensive Threat Intelligence: Emotet is back after a summer break](https://blog.talosintelligence.com/2019/09/emotet-is-back-after-summer-break.html)

[https://blog.talosintelligence.com/2019/09/emotet-is-back-after-summer-break.html](https://blog.talosintelligence.com/2019/09/emotet-is-back-after-summer-break.html)

> One of Emotet's most devious methods of self-propagation centers around its use of socially engineered spam emails. Emotet's reuse of stolen email content is extremely effective. Once they have swiped a victim's email, Emotet constructs new attack messages in reply to some of that victim's unread email messages, quoting the bodies of real messages in the threads.


I'm fascinated by the fact that Emotet took a break for summer.  I wonder what drove that, whether it indicates that the largest, most prolific banking trojan around is run by a very small team, or whether there's a normal seaonality to the banking trojan scene, that victims aren't as easy to get over the summer.

Anyway, this new feature, the socially engineered spam emails is very innovative.  Those of us in technology and security all feel like we know what spam and phishing emails look like right?  We know those emails purporting to be from the Crown Prince of Latveria and promising us millions of dollars.  But these emails are sent in response to an email you sent a while ago, quote part of the email and include links or attachments.  Those are far more likely to be clicked on, and have people fall for them.  Remember to update your awareness of what these techniques actually look like in a day to day basis before you judge people for falling for this stuff.


## [Report on Election Security Gains Attention, and a Sharp Rebuke — ProPublica](https://www.propublica.org/article/report-on-election-security-gains-attention-and-a-sharp-rebuke)

[https://www.propublica.org/article/report-on-election-security-gains-attention-and-a-sharp-rebuke](https://www.propublica.org/article/report-on-election-security-gains-attention-and-a-sharp-rebuke)

> “NormShield is the only provider that assesses and prioritizes the risk of any organization within 60 seconds,” Chief Security Officer Bob Maley wrote. Its work would provide each state with an overview of its failures in 10 categories, all given an easy-to-understand letter grade “that can be instantly used to evaluate cyber defenses.”
> 
> Initially, most states ignored the email. Some told ProPublica they thought it was spam. Others dismissed it as a heavy-handed marketing ploy — one of dozens of such approaches states receive monthly from cybersecurity companies hoping to win government contracts.
> 
> But some states asked for reports on their systems. Considerable upset followed.
> 
> [...]
> 
> In interviews with ProPublica, election officials and experts in election security said NormShield’s behavior amounted to another kind of election security threat: companies looking to profit from a country on edge about the integrity of its national and local elections


Sadly this is exactly the sort of thing that brings disrepute to the cybersecurity industry.  There was another tool recently that claimed to perform security checks in seconds, and investigating it ran some javascript to verify your IP address and a few other things.  It was advertising itself as "You have 2 critical vulnerabilities now".  Fear sells, and right now cybersecurity is still the market of fear.  We need to change that, we need to give reasoned, contextually appropriate advice to people that doesn't just scare them into thinking that the Russians are coming or whatever.


## [Scotiabank slammed for 'muppet-grade security' after internal source code and credentials spill onto open internet • The Register](https://www.theregister.co.uk/2019/09/18/scotiabank_code_github_leak/)

[https://www.theregister.co.uk/2019/09/18/scotiabank_code_github_leak/](https://www.theregister.co.uk/2019/09/18/scotiabank_code_github_leak/)

> The substantial code collection also included source for integrating the bank's systems with payment services, including Samsung and Google Pay as well as US credit-card processors Visa and Mastercard, and others.
> 
> Having such a vast library of digital blueprints on the public internet may have left Scotiabank and its 25 million-plus customers wide open to attack, should the code be analyzed and found to be exploitable. Bear in mind, back in 2017, Coulls discovered that the Canadian giant's digital banking unit, supposedly its high-tech offshoot, was not only using security certificates that had expired five months prior, but much of its code had not been thoroughly audited or debugged, it seemed.


I'm more astonished that anyone thinks that all code is thoroughly audited and debugged.  This story has a whiff of pearl-clutching to it.  It's entirely possible that ScotiaBank is simply open sourcing much of it's code, has an open source policy, but has included too much stuff.  Equally, knowing the username and password for a database (and even the SQL structure) is of no use to an attacker if the database is not accessible without breaching other systems first.  Context is key and the register does love to pull things out of context.


## [Simjacker](https://simjacker.com/)

[https://simjacker.com/](https://simjacker.com/)

> AdaptiveMobile Security have uncovered a new and previously undetected vulnerability and associated exploits, called Simjacker. This vulnerability is currently being actively exploited by a specific private company that works with governments to monitor individuals. Simjacker and its associated exploits is a huge jump in complexity and sophistication compared to attacks previously seen over mobile core networks. The main Simjacker attack involves an SMS containing a specific type of spyware-like code being sent to a mobile phone, which then instructs the SIM Card within the phone to ‘take over’ the mobile phone to retrieve and perform sensitive commands. The location information of thousands of devices was obtained over time without the knowledge or consent of the targeted mobile phone users. During the attack, the user is completely unaware that they received the attack, that information was retrieved, and that it was successfully exfiltrated. However the Simjacker attack can, and has been extended further to perform additional types of attacks.


This is somewhat terrifying.  It sounds like SIMcards run a small embedded browser, which can be triggered remotely by certain text messages.  We expect to see flaws like this discovered and exploited by nation states and certain large companies, if the details of this are made more public and large criminal groups start to use this, we could see remote malware infections and tracking being easily remotely deployable.  Since this is SIM based, I have no idea how anybody is planning to fix or remediate this.


## [The Viral App That Labels You Isn't Quite What You Think | WIRED](https://www.wired.com/story/viral-app-labels-you-isnt-what-you-think/)

[https://www.wired.com/story/viral-app-labels-you-isnt-what-you-think/](https://www.wired.com/story/viral-app-labels-you-isnt-what-you-think/)

> The project, called ImageNet Roulette, is an effort by artist Trevor Paglen and researcher Kate Crawford to illustrate the dangers of feeding flawed data into artificial intelligence. It takes aim at one of the field’s seminal resources: ImageNet, the database of 14 million images that’s credited with unlocking the potential of deep learning, the technique used for everything from self-driving cars to facial recognition. The algorithm behind the Roulette tool is trained using images within ImageNet that label people across 2,395 categories, from “slatterns” to “Uzbeks.” “I wanted to crack ImageNet open and look at images that weren’t meant to be looked at,” says Paglen. The experiment, now viral, has plenty of people asking just how those labels got there in the first place, and why they remain.


We tend to advance technologically speaking, because of of standing on the shoulders of giants.  We use the collected experiences, code, learning and implementations of previous generations of computer scientists and engineers.  But sometimes we forget where that comes from.  Many image recognition applications use the same data set to train their image recognition sets.  It's been a common data set for decades now, because the effort of manually rekeying it is hard, but it has a variety of issues or bias and cultural context that makes it problematic to be silently embedded in the AI systems of the future. 


## [Tortoiseshell Group Targets IT Providers in Saudi Arabia in Probable Supply Chain Attacks | Symantec Blogs](https://www.symantec.com/blogs/threat-intelligence/tortoiseshell-apt-supply-chain)

[https://www.symantec.com/blogs/threat-intelligence/tortoiseshell-apt-supply-chain](https://www.symantec.com/blogs/threat-intelligence/tortoiseshell-apt-supply-chain)

> The targeting of IT providers points strongly to these attacks being supply chain attacks, with the likely end goal being to gain access to the networks of some of the IT providers’ customers. Supply chain attacks have been increasing in recent years, with a 78 percent increase in 2018, as we covered in ISTR 24. Supply chain attacks, which exploit third-party services and software to compromise a final target, take many forms, including hijacking software updates and injecting malicious code into legitimate software.
> 
> IT providers are an ideal target for attackers given their high level of access to their clients’ computers. This access may give them the ability to send malicious software updates to target machines, and may even provide them with remote access to customer machines. This provides access to the victims’ networks without having to compromise the networks themselves, which might not be possible if the intended victims have strong security infrastructure, and also reduces the risk of the attack being discovered. The targeting of a third-party service provider also makes it harder to pinpoint who the attackers’ true intended targets were.


We've seen IT providers as the target of supply chain attacks before, such as the CloudHopper attacks.  Because of the unusual access that managed service providers have to our networks, and often the view that they aren't crossing a security boundary, it means that attacks can get in over management links that are supposed to carry remote desktop traffic or send management commands and use powershell.


## [The Human Factor 2019 Report - Modern Cyber Attacks | Proofpoint](https://www.proofpoint.com/us/resources/threat-reports/human-factor)

[https://www.proofpoint.com/us/resources/threat-reports/human-factor](https://www.proofpoint.com/us/resources/threat-reports/human-factor)

> Cyber criminals continue to refine techniques that target people rather than infrastructure, with attacks that rely more on human interaction and less on automated exploits.
> 
> Based on data collected across our global customer base and analysis of more than 1 billion messages per day we found that 
> * Very Attacked People™ (VAPs) aren’t usually VIPs – The most attacked people are often easily discovered identities or “targets of opportunity.”
> * Social engineering is pervasive, whether in rampant sextortion schemes, business email compromise (BEC), credential phishing, or other attacks that prey on human nature – and human error.
> * Domain fraud plays a key role in lending a sense of legitimacy to attacks.


This is an interesting report, in particular, that we pay a lot of attention to protecting VIP's, executives and senior members of staff.  But in reality, the most attacked people are the ones for whom it's the easiest and most rewarding to attack.  That means customer service representatives who can change addresses, switch SIM's and update banking details are far more likely targets than the VP of engineering.


## [Dutch Insider Deployed Stuxnet: Report - Infosecurity Magazine](https://www.infosecurity-magazine.com/news/dutch-insider-deployed-stuxnet/)

[https://www.infosecurity-magazine.com/news/dutch-insider-deployed-stuxnet/](https://www.infosecurity-magazine.com/news/dutch-insider-deployed-stuxnet/)

> The AIVD then played another crucial role, using an insider in Iran to gain employment at the plant as a mechanic.
> 
> Once there, he was able to gather vital intelligence on the configuration of the centrifuges, so that the Stuxnet code could be written to sabotage the facility only in specific operational circumstances.
> 
> He then deployed the virus via USB to jump the air-gap — either directly or by infecting a Natanz engineer’s computer system, according to the report.
> 
> Later versions are said to have circumvented the lack of direct connectivity at the plant by infecting targets who they unwittingly carried the malware inside with them.


This is a lovely attack, jumping the airgap is carried out by a mechanic who had legitimate access to the plant, and was able to plug in USB keys into the right systems inside the plant.  Remember that this here is an example of a multi-nation-state operation that includes world leading cyber attacks, human intelligence and covert operatives.  If you are not the target for this kind of attack, then this is way beyond the level you should be worrying about on a day to day basis.


## [Secrets in hands of alleged RCMP spy would cause 'devastating' damage to Canada, allies: documents | CBC News](https://www.cbc.ca/news/politics/ortis-cse-csis-documents-devistating-1.5285970)

[https://www.cbc.ca/news/politics/ortis-cse-csis-documents-devistating-1.5285970](https://www.cbc.ca/news/politics/ortis-cse-csis-documents-devistating-1.5285970)

> According to an assessment by the Communications Security Establishment, Canada's cybersecurity agency, and the Canadian Security Intelligence Service, Cameron Ortis, the director general of the RCMP's national intelligence co-ordination centre, had material that, if released, would cause a "HIGH" degree of damage to Canada and its allies.
> 
> "Analysis of the contents of the reports could reasonably lead a foreign intelligence agency to draw significant conclusions about allied and Canadian intelligence targets, techniques, methods and capabilities," the documents said. 
> 
> "This type of information is among the most highly protected of national security assets, by any government standard and goes to the heart of Canada's sovereignty and security."
> 
> [...]
> 
> The documents reveal that Ortis's condo was covertly searched last month and a number of handwritten notes were discovered providing instructions on how to wash metadata from PDF files.
> 
> The documents, of which CBC News has only seen parts, say that about 25 documents had been "sanitized to remove identifying information."
> 
> [...]
> 
> In March of last year, the FBI revealed that it had taken down an international criminal communications service based in Canada that had revenue of $80 million over the last decade. The operation resulted in the seizure of 1,000 phones that the FBI said were being used to facilitate murders and drug smuggling.
> 
> [...]
> 
> A subsequent email promised to provide "intel about your associates and individuals using their network internationally."


The more I read about this, the more I think this could be potentially the most damaging insider attack since Snowdon.  Right now we don't know very much, and we aren't likely to know that much more.  It looks like all of the public information that contains the juicy details is being leaked to the press, and that means that security around this case is about to get much tighter.

If we read this correctly, Ortis is accused of actively going to find the CEO of an encrypted communications network that he knew, from operations he was briefed on, carried criminal networks and conversations and tried to sell them information on how the criminals were being tracked by the authorities.  There was covert searching of his apartment, to find information when he wasn't there, and this has revealed evidence that he was attempting to extract the documents, clear any tracking metadata so they could be passed on anonymously.  This is also quite a counter-intelligence scoop.  It's bad that it got this far, but the way they've managed to roll this up effectively is looking like htey know how to do their job, which should set the Canadians allies (such as the rest of five-eyes) minds at ease.


