---
title: "146 - What even is a data breach?"
date: 2021-04-25
description: "Endless headlines about data breaches come and go every month, but I'm not sure that we're always using the words appropriately."
permalink: /what-even-is-a-data-breach/
---

Endless headlines about data breaches come and go every month, but I'm not sure that we're always using the words appropriately.

The Facebook breach was conducted by a third party using an API to extract customer records that they had legitimate access to, but shouldn't have accessed and stored in that way.

The clubhouse breach is the scraping of peoples public persona data from the clubhouse system.

The passwordstate breach was caused because of malware injected into the software update mechanism.

The infamous Ashley Madison breach was caused by hackers getting access to the management systems and dumping the database.

These don't feel like that they are all of the same category, but we tend to lump them all together into the term data breach, and expect users and regulators to consider them the same.

Taking the clubhouse breach as a really good example of a completely grey area breach.

As far as we can tell, the data was provided, willingly and with consent by clubhouse users to be part of their public profile on Clubhouse.  They can and should expect that any other Clubhouse user can see that information should they be in the same room, and given the search tools, that theoretically any user should be able to see the info.  Is that personal data?  GDPR would still say that because it's identifying data, it is personal data, and thus the sharing of it beyond the minimum needed to operate the site would be a breach. 

However, Clubhouse has a "real name" policy, you are encouraged and told to provide your real name when you sign up, and they have an [interesting view on privacy](https://www.vox.com/recode/22278601/clubhouse-invite-privacy-contacts-app) which not only makes it hard not to share data about yourself, but actively shares your presence with people who share your number with them regardless of whether you want them to.  

None of this is new in Silicon Valley, where Growth Hacking has been vogue for over a decade now.  User acquisition and activation is literally the name of the game, and startups are valued on how quickly they can expand their social graph.

But if somebody can get hold of that data, and expose it, is it a breach of your privacy?  You give that same information out to lots of different locations.  Huge numbers of apps on the app store ask for permission to access your contacts for precisely that reason.  The breach of your socially public persona data feels distinctively different to the breach of your private data that you don't expect to be shared.

When we confuse the two, and make it out like public data breaches are as bad as hackers and other bad actors stealing private data sets, we reduce the amount of effort on protecting the private data, and just increase user lethargy and acceptance.  Most users believe that their data has been released in at least one breach.  As I've said before, Have I Been Pwned, while lovely, just doesn't give you much of an action to take other than resigned acceptance.  Yes my data has been breached yet again, so what?

In other news, I'm coming up for 3 years since I sent the first edition of Cyberweekly, which went out on Saturday 26th May 2018.  I'm wondering if there's anything special to do, but one thing that would be nice would be to include any thoughts or stories that you have.  If you find this newsletter interesting, if it's been timely or valuable at all, or if you have anything to add then please drop me a note and let me know.

## [Moserpass supply chain](https://www.csis.dk/newsroom-blog-overview/2021/moserpass-supply-chain/)

[https://www.csis.dk/newsroom-blog-overview/2021/moserpass-supply-chain/](https://www.csis.dk/newsroom-blog-overview/2021/moserpass-supply-chain/)

> The rogue dll that we discovered was the dll named "Moserware.SecretSplitter.dll" that was injected/modified with a malicious code snippet. A small code “Loader” was added to the original dll:
> 
> 
> 
> The malicious code tries to contact the following URL:
> https://passwordstate-18ed2.kxcdn[.]com/upgrade_service_upgrade.zip
> - in order to retrieve an encrypted code using method "Container.Get()", AES (Advanced Encryption Standard) decrypt it using the password: f4f15dddc3ba10dd443493a2a8a526b0, and then pass it to the Loader Class(). Once decrypted, the code is executed directly in memory.


So if you downloaded the infected update, the code on the your computer would go off and attempt to fetch some more executable code from a command and control server, which would then execute.

Note that this doesn't seem to encrypt the C2 url, it doesn't attempt to hide the C2 traffic or use unusual traversal, so this is quite a simple exploit. 

Doesn't make it any less damaging though


## [Password manager Passwordstate hacked to deploy malware on customer systems | The Record by Recorded Future](https://therecord.media/password-manager-passwordstate-hacked-to-deploy-malware-on-customer-systems/)

[https://therecord.media/password-manager-passwordstate-hacked-to-deploy-malware-on-customer-systems/](https://therecord.media/password-manager-passwordstate-hacked-to-deploy-malware-on-customer-systems/)

> A mysterious threat actor has compromised the update mechanism of enterprise password manager application Passwordstate and deployed malware on its users’ devices, most of which are enterprise customers.
> 
> Click Studios, the Australian software firm behind Passwordstate, has notified its 29,000 customers earlier today via email.
> 
> As a result, the Australian firm has recommended that customers change all the passwords they stored inside compromised Passwordstate password managers as soon as possible.
> 
> Since this is a password manager is sold primarily in bulk to enterprises, to whom it is advertised as an on-premises system, changing passwords won’t involve just email and website accounts, but also passwords for internal gear such as firewalls, VPNs, switches, routers, network gateways, and others, which many employees would most likely have saved inside the app thinking it was a secure local storage system.


Having a compromised password manager is about the worst breach that you can imagine. 

Note that the actor didn't compromise the password stores in bulk, they instead modified the password manager software to run arbitrary code locally.  Not only would that give them access to the password store on enterprise devices, but would also give them access into the network.  That password store is almost certainly installed in a privileged location in the network, and naturally good practice would suggest that all administrators would access the device on a regular basis for the administration accounts.


## [Clubhouse CEO says user data was not leaked, contrary to reports - The Verge](https://www.theverge.com/2021/4/11/22378302/personal-information-1-million-clubhouse-users-leaked-privacy-security)

[https://www.theverge.com/2021/4/11/22378302/personal-information-1-million-clubhouse-users-leaked-privacy-security](https://www.theverge.com/2021/4/11/22378302/personal-information-1-million-clubhouse-users-leaked-privacy-security)

> Clubhouse did not immediately reply to a request for more information from The Verge on Sunday. But Davison said in response to a question during a town hall that the platform had not suffered a data breach. “No, This is misleading and false, it is a clickbait article, we were not hacked. The data referred to was all public profile information from our app. So the answer to that is a definitive ‘no.’”
> 
> Last week, Cyber News reported that personal data for 500 million LinkedIn users had been scraped and posted online. The Microsoft-owned company said that no private member account data from LinkedIn was included in the leak.
> 
> That news came just a couple of days after it was discovered that personal data for some 533 million Facebook users was leaked online for free. The Facebook leak reportedly included users’ phone numbers, birthdates, locations, email addresses, and full names.


There's an interesting question here.  An SQL database dump was definitely uploaded that contained details. But if the details were just public profile information, all of which is scrapeable, then is it really a breach?

The big question is whether you, as a user, expect your details to be scraped from the site, and whether you can pick or choose what data is there?  Clubhouse has a mandatory name field, and has an algorithm that tries to prevent "illegitimate names" to go with it's real name policy.  So you cannot opt out of providing a name, and that name is scrapeable.  But equally, the site and system won't work as well if you don't provide a name, and so there's a level of user acceptance that their details are public, not private.


## [Troy Hunt: Data Breaches, Class Actions and Ambulance Chasing](https://www.troyhunt.com/data-breaches-class-actions-and-ambulance-chasing/)

[https://www.troyhunt.com/data-breaches-class-actions-and-ambulance-chasing/](https://www.troyhunt.com/data-breaches-class-actions-and-ambulance-chasing/)

> I have received an increase in spam, and an increase in unsolicited phone calls to my number etc. I have to be aware that phishing scams may be used against me.
> 
> [...] There are 3 massive problems with this and I suspect LOQBOX used HIBP to demonstrate the first one: there are 6 other data breaches Jimmy appears in on HIBP. If he's received more spam as a result of a breach, which breach was it? LOQBOX? Or one of the other ones? Also, there are 6 other breaches we know Jimmy was in, how many more are there we don't know about? The only answer to that question is "we don't know"; Jimmy doesn't know, LOQBOX doesn't know and his lawyers sure as hell don't know. Nobody knows. So how is it that Jimmy is so convinced LOQBOX is responsible for emails and phone calls he doesn't want?
> 
> The second problem is that you don't need a data breach to get spam, unsolicited phone calls or phishes. Based on the age of some of the breaches Jimmy is in, he's had that email address for many years; how many places has he left it after agreeing to the terms and conditions he didn't read? (No offence to Jimmy on that, nobody reads the terms and conditions.) How many places did his personal data then flow to? How many times was his information published somewhere publicly for other purposes? Happens all the time. Spam, unsolicited phone calls and phishes don't just come from data breaches and it's enormously difficult to reliably attribute them back to a source.
> 
> The third problem is the assumption that due to him now being in a 7th data breach (that he knows of), he needs to start being "aware that phishing scams may be used against him". Seriously? Like if Jimmy wasn't in a data breach he wouldn't need to worry about phishing?


This is a good write up, and a reminder that for the majority of us, being in a data breach doesn't result in any material harm.  This, sad to say, makes tools like Troy's Have I Been Pwned, broadly useless, because as an end user, there's no action I can take if my info was breached, and very little I can do other than recycle any passwords I had shared with the breached data set.


## [This company was hit by ransomware. Here's what they did next, and why they didn't pay up | ZDNet](https://www.zdnet.com/article/this-company-was-hit-with-ransomware-heres-what-they-did-next-and-why-they-didnt-pay-up/)

[https://www.zdnet.com/article/this-company-was-hit-with-ransomware-heres-what-they-did-next-and-why-they-didnt-pay-up/](https://www.zdnet.com/article/this-company-was-hit-with-ransomware-heres-what-they-did-next-and-why-they-didnt-pay-up/)

> A lot of ransomware attacks never become public knowledge, and examples of companies that go into detail about what happened are still few and far between.
> 
> But Mendoza says it's important to be transparent about dealing with a ransomware attack, because it's important to show that it is possible to recover from an attack without lining the pockets of cyber criminals.
> 
> "What we realised was we protected our data and there's a way to thwart ransomware. We couldn't find public information when we were looking for it, so we wanted to make it a common thing, that it's okay to talk about being impacted by ransomware," he said.
> 
> 
> So what is the key lesson Mendoza would say that other organisations need to take away from Spectra Logic's experience? It's backup your systems – and do so offline – so, if the worst happens and the organisation falls, you still have backups offline.
> 
> "You've got to limit your attack blast radius. Backup your data in multiple locations on multiple mediums and the key is to air-gap it. Whether it's physical air-gap or virtual air-gap, you've got to put a wall between an attack and your data," he said.
> 
> And how did the company end up falling victim to a ransomware attack in the first place? Analysis of the incident revealed a phishing email sent to an employee working from home was how hackers gained their initial access to the network.


Have backups, kept away from the production system, and invest in scanning incoming email for phishing and malware.  

We keep calling them basics, I keep calling them foundational practices, but if you need to do anything, these two work.  And as a reminder, on the big two SaaS mail solutions, O365 and GSuite, for enterprise accounts you should get their built in spam and phishing detection.  Make sure it's turned on and working.


## [Apple supplier Quanta hit by cyber attack | Financial Times](https://www.ft.com/content/0ec11549-9d68-4ca2-bbac-34684c86abab?sharetype=blocked)

[https://www.ft.com/content/0ec11549-9d68-4ca2-bbac-34684c86abab?sharetype=blocked](https://www.ft.com/content/0ec11549-9d68-4ca2-bbac-34684c86abab?sharetype=blocked)

> Quanta, one of Apple’s major suppliers, said on Wednesday that it had been hit by a cyber attack and was trying to “recover data” after one of the world’s most notorious hacking gangs said it was attempting to extort both companies. 
> 
> The Taiwanese company, which manufactures computers for Apple and also supplies companies such as Cisco, Microsoft and Siemens, said it had suffered “cyber attacks on a small number of Quanta servers” and was “conducting detailed investigation to ensure containment and recovery of data are in process”. 
> 
> The admission came after REvil, one of the most prolific criminal ransomware hacking groups, said on its dark web site that it had compromised Quanta and was now extorting Apple.
> 
> Like other ransomware gangs, REvil typically locks up the data or computer systems of its victims until it is paid off. In this instance, the group said Quanta had refused to co-operate with its demands and it was now asking Apple to pay a ransom by May 1 in exchange for not leaking their sensitive information. 
> 
> “Our team is negotiating the sale of large quantities of confidential drawings and gigabytes of personal data with several major brands,” the REvil post added. It also shared copies of what appeared to be Apple product blueprints, though it is unclear whether these contained any confidential information.
> 
> Separate chat logs, seen by the Financial Times, showed that REvil had initially demanded $50m from Quanta.


That's a big ransom that they are asking for.  The fact that supply chain issues mean that you need to also worry whether your suppliers are going to be subject to ransomware and whether any confidential data you share with them could be used against you.

Ransomware operators looking through your data for big name, big cash customer is a new risk from ransomware that we'll need to track.


## [Mailbag: Should we just call them architects? | Irrational Exuberance](https://lethain.com/mailbag-should-we-call-them-architects/)

[https://lethain.com/mailbag-should-we-call-them-architects/](https://lethain.com/mailbag-should-we-call-them-architects/)

> The Staff-plus sequence of titles decouples seniority from archetype and is more durable for it. You can assess someone’s seniority from their title: Staff engineer, Principal engineer, Distinguished engineer, perhaps with some varieties like Senior Staff engineer thrown in for very large organizations. You can separately understand someone’s mode of operation by documenting someone’s archetype: solver, architect, tech lead, or right hand.
> 
> If you were feeling argumentative, you could have a title for every archetype, but I don’t think that would work well in practice. There are two reasons why this is hard. First, archetypes create clarity by creating distinctions, but reality tends to be blurry. Very few folks mix “tech lead” and “right hand”, but many “tech leads” spend some time on doing “architect” work. This makes evaluating folks a nuanced activity. Second. creating four useful career ladders is surprisingly challenging. It’s very possible to add specializing paragraphs to a couple of blocks explaining how a “solver” might create impact differently than an “architect.” However, I don’t know of any company that operates different ladders for each archetype successfully.


This is an interesting piece around whether the term "Software Architect" is a good term or not.  I really like the breakdown here that career ladders and job titles have to have meaning, but that they might have meaning separate from the archetype or role of the work the person does.

There's a common fallacy that the type of work you do defines who you are and thus your job title and seniority.  But I've worked with an amazing spread of people over the years, from absolutely amazing engineers or solvers, to incredibly effective political right hands.  Some of those people changed role within the same organisation over time, someone might be a strong tech lead for one project, and then switch to a more architect role for a programme for a few years before switching back to a lead engineer.

What you do is not who you are, you are not "an architect" or "a tech lead".  You are a person who happens to do that at this moment in time.  Your performance needs to be measured against that, but your actual job title should stay stable even as you move around, and your career should still feel structured


## [Being Chief Technology Officer: Lessons learned in my first year – Shekhar Gulati](https://shekhargulati.com/2021/01/03/being-chief-technology-officer-lessons-learned-in-my-first-year/)

[https://shekhargulati.com/2021/01/03/being-chief-technology-officer-lessons-learned-in-my-first-year/](https://shekhargulati.com/2021/01/03/being-chief-technology-officer-lessons-learned-in-my-first-year/)

> Once you know which tasks to delegate, you have to use a delegation level that gets the best job done. I learnt about 7 levels of delegation at Management 30 website [4].
> 
> Tell: I will tell them 
> Sell: I will try and sell it to them 
> Consult: I will consult and then decide 
> Agree: We will agree together 
> Advise: I will advise but they decide 
> Inquire: I will inquire after they decide 
> Delegate: I will fully delegate
> At the end of the day, you have to use just enough management to get things done.


Lots of interesting lessons here.  I find this one interesting more because the assumption around a CTO matches what I'd expect from a Tech Lead or Architect in many organisations.  I think some of that will depends on what you think the CTO role entails and the size of the organisation that you are leading.


## [Former Air Force Contractor Pleads Guilty to Illegally Taking 2,500 Pages of Classified Information | OPA | Department of Justice](https://www.justice.gov/opa/pr/former-air-force-contractor-pleads-guilty-illegally-taking-2500-pages-classified-information)

[https://www.justice.gov/opa/pr/former-air-force-contractor-pleads-guilty-illegally-taking-2500-pages-classified-information](https://www.justice.gov/opa/pr/former-air-force-contractor-pleads-guilty-illegally-taking-2500-pages-classified-information)

> According to court documents, Kemp was employed as a contractor at the Air Force Research Laboratory (AFRL) from July 2016 to May 2019, and later as a contractor at the U.S. Air Force National Air and Space Intelligence Center (NASIC). While working at AFRL and NASIC – both located on Wright-Patterson Air Force Base in Fairborn – Kemp had Top Secret security clearance.
> 
> Despite having training on various occasions on how to safeguard classified material, Kemp took 112 classified documents and retained them at his home.
> 
> Law enforcement discovered the documents which contained approximately 2,500 pages of material classified at the Secret level, while executing a search warrant at Kemp’s home on May 25, 2019.


At a rough estimate, that means that every classified document was about 23 pages long, which feels awfully long even with the inevitable coversheets.  And what were police doing searching the house?  Was it because of a tip off about the suspects behaviour? From document logging that detected the print and retention of documents?  Nope, it was a Fairborn police issued search for a marijuana growing facility.


