---
title: "132 - New year, new resolutions, and new lessons to learn"
date: 2021-01-17
description: "It's hard to believe that we're already at the end of the second week of 2021.  For some us, our resolutions will already be broken, especially in the face of a continuing global pandemic and the sheer sense of apathy that everyone I speak to has.  "
permalink: /new-year-new-resolutions-and-new-lessons-to-learn/
---

It's hard to believe that we're already at the end of the second week of 2021.  For some us, our resolutions will already be broken, especially in the face of a continuing global pandemic and the sheer sense of apathy that everyone I speak to has.  

It's felt like quite a lot has been fit into a fairly short period of time, from attempted insurrection to mass platform bans, from global supply chain hacks to your everyday breaches.  Keeping our head, our sense of self, and our teams together in this time requires us to be clear communicators, and to take the time and effort to engage in positive leadership.

I've been clear when setting out my teams objectives that we're not pulling in what would be traditional big hairy audacious goals, or OKR's that we're only moderately confident we can achieve.  Instead our team needs to set its sights lower, and work out what can be considered audacious and stretch goals given the context in which we work.

For myself, I've set myself goals to read more management books, to exercise more often, and to try to practice what I preach as much as I can.  By the end of the second week of January, I've read no management books, but I have managed to follow an exercise plan.  What I have been doing is turning my reading attention online to valuable sources that I think will help me as a senior manager, as an analyst, and to keep stretching and testing myself.  You'll probably see some of that in the articles that I select over the coming months, a few more articles about leadership and tech leadership in particular.  Of course, the constant tire fire that is cybersecurity means that there will of course be plenty of stories about breaches and ways to approach them, so don't worry that I'm changing focus of this newsletter.

As always, I welcome feedback and suggestions.  I read all the replies to this newsletter, even if I'm not great at replying back myself, and you can feel free to send me links, or just tag me on twitter.  I read, I reckon, at least 5 cybersecurity newsletters a week, another 50 RSS feeds and read around 50-80 stories that catch my attention and try to select 10 that I think are interesting.  The more I get sent, the better the signal to noise, so please do pass stuff my way.

## [NSA Recommends How Enterprises Can Securely Adopt Encrypted DNS > National Security Agency Central Security Service > Article View](https://www.nsa.gov/News-Features/Feature-Stories/Article-View/Article/2471956/nsa-recommends-how-enterprises-can-securely-adopt-encrypted-dns/)

[https://www.nsa.gov/News-Features/Feature-Stories/Article-View/Article/2471956/nsa-recommends-how-enterprises-can-securely-adopt-encrypted-dns/](https://www.nsa.gov/News-Features/Feature-Stories/Article-View/Article/2471956/nsa-recommends-how-enterprises-can-securely-adopt-encrypted-dns/)

> DoH encrypts DNS requests, preventing eavesdropping and manipulation of DNS traffic. While good for ensuring privacy in home networks, DoH can present risks to enterprise networks if it isn’t appropriately implemented. The recommendations detailed will assist enterprise network owners and administrators in balancing DNS privacy and governance for their networks. It outlines the importance of configuring enterprise networks appropriately to add benefits to, and not hinder, their DNS security controls. These enterprise DNS controls can prevent numerous threat techniques used by cyber threat actors for initial access, command and control, and exfiltration.
> 
> NSA recommends that an enterprise network’s DNS traffic, encrypted or not, be sent only to the designated enterprise DNS resolver. This ensures proper use of essential enterprise security controls, facilitates access to local network resources, and protects internal network information. All other DNS resolvers should be disabled and blocked.
> 
> 


This will please Joel at least!  Enterprises should be actively adopting encrypted DNS-over-HTTP, providing their own enterprise server and then blocking others.  

This security posture of adopting things, providing a blessed way that works and then blocking things that don’t use it is far preferable than just saying no or blocking it network wide.  Of course, there’s a difference between end user devices, servers, cloud services and mobile devices.  You may not want a blanket policy in place.  This advice mostly applies to end user devices like corporate laptops.


## [Running a fake power plant on the internet for a month | by Stefan Grimminck | Jan, 2021 | Medium](https://grimminck.medium.com/running-a-fake-power-plant-on-the-internet-for-a-month-4a624f685aaa)

[https://grimminck.medium.com/running-a-fake-power-plant-on-the-internet-for-a-month-4a624f685aaa](https://grimminck.medium.com/running-a-fake-power-plant-on-the-internet-for-a-month-4a624f685aaa)

> There is active scanning for industrial equipment on the internet. Not only by big companies that index the whole IPv4 space, but also by individuals and organisations interested in which machines are available. Luckily most traffic received is from researchers scanning the whole IPv4 space for systems in the vein of responsible disclosure. However, this does not exclude that there are real people looking for industrial machines on the internet as well.
> 


Kind of interesting as a project. Good demonstration on how you might build a honeypot.  But also evidence that the majority of the scanning happening out there is coming from the major scanning engines, which creates a lot of noise for your detection systems. 


## [Spies and cybercriminals are sharing their supply-chain attack strategy](https://intel471.com/blog/solarwinds-supply-chain-attack-iran-russia-north-korea/)

[https://intel471.com/blog/solarwinds-supply-chain-attack-iran-russia-north-korea/](https://intel471.com/blog/solarwinds-supply-chain-attack-iran-russia-north-korea/)

> There are numerous reasons why governments have either copied or outsourced these TTPs. Allowing cybercriminals to operate with their own skills and tools allows governments to save money in training and development, leveraging capabilities and a “workforce” they don’t have to build themselves. But a key asset is also the ability to “hide in the noise” created by cybercriminals and the marketplaces they frequently use. If the TTPs of a supply chain attack bear the hallmarks of financially-motivated actors, governments are given an extra layer of protection, plausible deniability and obfuscation from being labeled as responsible for a particular incident.
> 
> While the SolarWinds incident will be pored over in the months to come, it is only one in a growing list of incidents that show that not only are supply-chain attacks a common practice, they are effective for both financially-motivated criminals and government-backed campaigns alike.


I’m slightly suspicious about the claims here.  Supply chain attacks like solar winds is significantly more advanced than the magecart attacks for example.  Magecart can upload JavaScript to a website, but the solar winds attackers were able to compromise the build server to inject code at build time.  

However, the finding is something I agree with.  Supply chain is a vast and expansive term that is going to cover a lot of potential issues and attacks.  However, the successes of NotPetya and Solarwinds must be raising eyebrows in criminal groups.   The attacks work for espionage and international conflict purposes, but they could have resulted in significant financial benefits as well.


## [WhatsApp Has Shared Your Data With Facebook for Years, Actually | WIRED](https://www.wired.com/story/whatsapp-facebook-data-share-notification/)

[https://www.wired.com/story/whatsapp-facebook-data-share-notification/](https://www.wired.com/story/whatsapp-facebook-data-share-notification/)

> On Monday, WhatsApp updated its terms of use and privacy policy, primarily to expand on its practices around how WhatsApp business users can store their communications. A pop-up has been notifying users that as of February 8, the app's privacy policy will change and they must accept the terms to keep using the app. As part of that privacy policy refresh, WhatsApp also removed a passage about opting out of sharing certain data with Facebook: "If you are an existing user, you can choose not to have your WhatsApp account information shared with Facebook to improve your Facebook ads and products experiences." 
> 
> Some media outlets and confused WhatsApp users understandably assumed that this meant WhatsApp had finally crossed a line, requiring data-sharing with no alternative. But in fact the company says that the privacy policy deletion simply reflects how WhatsApp has shared data with Facebook since 2016 for the vast majority of its now 2 billion-plus users.





## [What I learned by failing the AZ-500 Microsoft Azure Security Technologies exam](https://www.linkedin.com/pulse/what-i-learned-failing-az-500-microsoft-azure-exam-hughes-/)

[https://www.linkedin.com/pulse/what-i-learned-failing-az-500-microsoft-azure-exam-hughes-/](https://www.linkedin.com/pulse/what-i-learned-failing-az-500-microsoft-azure-exam-hughes-/)

> Azure utilizes a variety of methods to support both Cloud-native and hybrid identity solutions. This includes strictly Cloud-based AD referred to as Azure Active Directory (AD), with no reach back to an on-premise IdP. There's Azure AD Connect, which you can use various options such as Azure AD Pass-through Authentication, which allows you to utilize on-premise agents and pass your users request back to the on-premise environment for authentication, which helps to enforce corporate authentication and account policies/requirements. 


Identity systems are complex, and this article amongst other things really highlights the sheer number of ways that you can do identity, authentication and authorisation within the Azure/Microsoft ecosystem.  


## [Software is drowning the world](https://jamesabley.com/software-is-drowning-the-world/)

[https://jamesabley.com/software-is-drowning-the-world/](https://jamesabley.com/software-is-drowning-the-world/)

> One of the many upsides I’ve had from working at lots of organisations is that you get to see what’s common. Are things like this everywhere? Frequently, the answer is yes!
> 
> An example of this is tech debt.
> 
> I see organisations which are running to stand still, and I’m not sure they realised they’re doing that.
> 
> What do I mean by this?
> 
> Every time you decide to solve a problem with code, you are committing part of your future capacity to maintaining and operating that code. Software is never done.


This is a nice essay pointing out just what tech debt really means and why organisations get themsevles into the [Red Queen problem](https://en.wikipedia.org/wiki/Red_Queen_hypothesis).

The answer... you don't need to do anything, almost anything that isn't constantly maintained will slowly accrete debt and issues.  This pushes us towards some form of constant maintenance in these areas.  James articulates ways in which we can use software to ease that maintenance, but part of the problem is that because we don't allocate people to the task of maintaining and fixing the debt, it's hard to work out how to automate the work.


## [Recommended Engineering Management Books – Caitie McCaffrey](https://caitiem.com/2020/12/28/recommended-engineering-management-books/)

[https://caitiem.com/2020/12/28/recommended-engineering-management-books/](https://caitiem.com/2020/12/28/recommended-engineering-management-books/)

> As the AS3 Team grew, I went through a massive amount of personal growth and learning as well.  In December 2017 I stepped into a manager role for the first time in my career.  I had been a professional software engineer for over a decade at this point, and was up for a totally new challenge.  I knew that the skills and job of growing and managing a team and then an organization were totally different than what I had been actively developing over the last decade of my career.  As I went through this period of growth I was lucky enough to have several friends, coaches, and mentors share their experiences with me, and recommend some great books to help me along my learning journey. 
> 
> Below is my curated list of the most influential and impactful books that helped me along the way, and that I highly recommend to Engineering Manager


This is a good reading list.  I've read some of the books on this list, and based on the recommendations, I can forsee more reading ahead of me on the others.


## [Most Recommended Books](https://www.readthistwice.com/lists/most-recommended-books)

[https://www.readthistwice.com/lists/most-recommended-books](https://www.readthistwice.com/lists/most-recommended-books)

> Most Recommended Books
> Looking for your next read? Here are the top 100 most recommended books on Read This Twice. These are the must read books in the opinion of the thought leaders of today.


This might say more about the "thought leaders of today" than we might want.  A fairly Silicon Valley heavy set of book recommendations, sprinkled in with books representing a common but not terribly diverse set of opinions. 


## [Chesterton’s Fence: A Lesson in Second Order Thinking](https://fs.blog/2020/03/chestertons-fence/)

[https://fs.blog/2020/03/chestertons-fence/](https://fs.blog/2020/03/chestertons-fence/)

> All of us, at one point or another, make some attempt to change a habit to improve our lives. If you’re engaging in a bad habit, it’s admirable to try to eliminate it—except part of why many attempts to do so fail is that bad habits do not appear out of nowhere. No one wakes up one day and decides they want to start smoking or drinking every night or watching television until the early hours of the morning. Bad habits generally evolve to serve an unfulfilled need: connection, comfort, distraction, take your pick.
> 
> Attempting to remove the habit and leave everything else untouched does not eliminate the need and can simply lead to a replacement habit that might be just as harmful or even worse. Because of this, more successful approaches often involve replacing a bad habit with a good, benign, or less harmful one—or dealing with the underlying need. In other words, that fence went up for a reason, and it can’t come down without something either taking its place or removing the need for it to be there in the first place.


A great essay into the concept of Chesterton's Fence, and a timely reminder for those of us with new years resolutions.  Those bad habits you want to get rid of, whether lie-ins, or slob evenings might be there for a good reason.  Make sure that your new habits aren't just all healthy amazing habits, but build slack into your life.


## [All the platforms that have banned or restricted Trump so far - Axios](https://www.axios.com/platforms-social-media-ban-restrict-trump-d9e44f3c-8366-4ba9-a8a1-7f3114f920f1.html)

[https://www.axios.com/platforms-social-media-ban-restrict-trump-d9e44f3c-8366-4ba9-a8a1-7f3114f920f1.html](https://www.axios.com/platforms-social-media-ban-restrict-trump-d9e44f3c-8366-4ba9-a8a1-7f3114f920f1.html)

> All the platforms that have banned or restricted Trump so far


This is quite a list!  There's a lot of views out there about whether this is overdue or unacceptable behaviour.  I think the timing isn't coincidental, and I think it's dangerous to allow precedents to be set not because of an ethical bar (which arguably was passed years ago), but because the tech firms now feel that there will unlikely be any significant repercussions on their actions.  For those arguing about crossing a bar of freedom of speech, I'd love to point to the networks of ISIS content, terrorist content and other content that these networks have been taking down for years.  Of course many of those are not elected officials, but there's clearly a decision that some censorship is acceptable (and I would argue necessary), so the argument is not a black and white one of free-speech or not, but the messy grey sliding scale of "how much is acceptable", which is much harder to articulate.


