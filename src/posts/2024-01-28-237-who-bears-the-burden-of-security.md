---
title: "237 - Who bears the burden of security?"
date: 2024-01-28
description: "There's a common view amongst security professionals that everything would be better if users just cared more about security."
permalink: /who-bears-the-burden-of-security/
---

There's a common view amongst security professionals that everything would be better if users just cared more about security.

But the reality is that most users do care about security, it's just that they care about doing their jobs more, and they can rather accurately weigh up the cost to them of jumping through security hoops against the likely impact against themselves.

We tend to think that just one user misconfiguring their system or clicking a link could result in millions in damages, data compromised and users losing faith in your company!  It's easy therefore to say that we should spend more money and more resources on securing our infrastructure.  But since security is one of the smallest functions in most organisations, it tends to struggle to help the rest of the organisation to actually make meaningful choices.   It can't possibly sit in every single procurement and purchase activity and help the organisation make good decisions about which services and products to buy, so we often instead write guidance for others to follow and expect them to understand and use that guidance.  

That's a great model for amplifying your impact hugely, because it enables a much larger army of people to make security choices.  However, it also spreads the burden of security to all of those people as well.  If you've got a good training mechanism, well written defaults and guidance on how to make that decision, so that the people using your guides can make decisions quickly and easily, then it might work, but in many cases we cannot really articulate the actual security cost of most decisions and so we leave the guidance vague and unhelpful.

Pushing the security choices down to users adds burden to them, it's a way of rejecting the hard work of making the choices, and pushing it down.  It happens at all levels, from vendors down to their customers, requiring you to correctly configure the application, to security teams within organisations forcing difficult and burdensome processes on their users.

We need to consider not just the financial cost of security decisions, but the user experience and user burden of the decisions.  This is why the "secure by default" approach is so important to a secure future of a networked world.   It's a movement that pushes the security burden back upstream, away from users to the people building, configuring and selling their services, and insisting that it should be secure out of the box.  This isn't about making more security options like Single-Sign-On available to more people to badly configure, but ensuring that it uses such options easily out of the box.  Our software, whether we buy it, build it, or compose it from disparate parts should be as secure as possible, and ensure that it should only taken effort to change the defaults into insecure decisions.

## [Midnight Blizzard: Guidance for responders on nation-state attack | Microsoft Security Blog ](https://www.microsoft.com/en-us/security/blog/2024/01/25/midnight-blizzard-guidance-for-responders-on-nation-state-attack/)

[https://www.microsoft.com/en-us/security/blog/2024/01/25/midnight-blizzard-guidance-for-responders-on-nation-state-attack/](https://www.microsoft.com/en-us/security/blog/2024/01/25/midnight-blizzard-guidance-for-responders-on-nation-state-attack/)

> **Malicious use of OAuth applications** Threat actors like Midnight Blizzard compromise user accounts to create, modify, and grant high permissions to OAuth applications that they can misuse to hide malicious activity. The misuse of OAuth also enables threat actors to maintain access to applications, even if they lose access to the initially compromised account. Midnight Blizzard leveraged their initial access to identify and compromise a legacy test OAuth application that had elevated access to the Microsoft corporate environment. The actor created additional malicious OAuth applications. They created a new user account to grant consent in the Microsoft corporate environment to the actor controlled malicious OAuth applications. The threat actor then used the legacy test OAuth application to grant them the Office 365 Exchange Online _full_access_as_app_ role, which allows access to mailboxes. 


The background to this was published at [https://msrc.microsoft.com/blog/2024/01/microsoft-actions-following-attack-by-nation-state-actor-midnight-blizzard/](https://msrc.microsoft.com/blog/2024/01/microsoft-actions-following-attack-by-nation-state-actor-midnight-blizzard/) - in essence, Microsoft says that a legacy testing tenant was identified by Midnight Blizzard, and was compromised through password spraying.  That compromise allowed them to move laterally into Microsoft’s corporate network and steal documents and email from senior microsoft executives.

The bit that stood out here is an extremely subtle attack vector that we don’t think about enough.  The test tenancy has it’s own sets of users in it, and the attacker can compromise them within the test tenancy.  But it also has some applications that provide capabilities via OAuth.  Since I suspect many of them want to authenticate users in the core corporate tenancy, the OAuth applications needed privileges to talk to the core tenancy.  Because the hard way to do this is to work out only the privileges needed by the test tenancy, it’s far easier to just give that OAuth application some really high privileges, including the ability to create a new OAuth application that can create a domain admin account.

In the article there are some powershell scripts and some indicators that you can audit your network for to look for this.

More critically, this is one of those really hard management problems.  You probably don’t know at the point that you setup a tenancy just what the developers need, and it’s far easier to just give the tenancy the power to change what it needs than to require someone to come talk to your admin team everytime they need something.  But that opens the door to a set of nasty exploits that are hard to fix later down the line.

Finally, I’ll note that Microsoft’s response to this has been to push and remind us of the huge task that it faces dealing with 40 years of legacy systems and infrastructure.  Even with a budget measured in billions, they have realised that they are well behind rationalising and securing their legacy infrastructure and they’ve committed to accelerating that programme of work. 


## [Russia's Sandworm blamed for Kyivstar telecom cyberattack ](https://go.theregister.com/feed/www.theregister.com/2024/01/05/sandworm_kyivstar_hack/)

[https://go.theregister.com/feed/www.theregister.com/2024/01/05/sandworm_kyivstar_hack/](https://go.theregister.com/feed/www.theregister.com/2024/01/05/sandworm_kyivstar_hack/)

> This is a good reminder that the really competent attackers out there don’t behave like ransomware operators, turning from initial compromise to detectable malicious activity in a number of hours.  Again and again we see that the key calling card of the highest levels of actor isn’t just “Persistent”, it’s that they are often “Patient”.
> 
> Of course, most organisations aren’t at risk from this level of targeting, but since global events can change fast, it’s worth paying attention to what’s happening at this level 


The criminals lurked in the telco's systems for at least six months leading up to the attack, then wiped "almost everything," according to Illia Vitiuk, head of the Security Service of Ukraine's (SBU) cyber security department. In an [interview](https://www.reuters.com/world/europe/russian-hackers-were-inside-ukraine-telecoms-giant-months-cyber-spy-chief-2024-01-04/) published on Thursday, the spy chief reported that the "disastrous" intrusion, which wiped thousands of the operator's virtual servers and PCs, began long before Kyivstar's services went dark on December 12.

The attack also reportedly [disrupted](https://www.cnn.com/2023/12/12/europe/ukraine-cyber-attack/index.html) the air raid alert systems in parts of Kyiv and some banking services. That same week, two separate [missile attacks](https://www.reuters.com/world/europe/dozens-injured-kyiv-russias-second-missile-assault-this-week-ukraine-2023-12-13/) pelted the Ukrainian capital, injuring at least 53 people and damaging homes and a children's hospital.

The Kyivstar hackers broke into the network in May 2023, if not earlier, according to Vitiuk, and gained full access by November. This would have given the attackers access to customer information, phone location data, SMS messages, and potentially Telegram account credentials.

Vitiuk said he's "pretty sure" [Sandworm](https://www.theregister.com/2023/08/31/sandworm_infamous_chisel/) was responsible for the break-in. This is the crew that carries out espionage, hack-and-leak, data wiping and influence campaigns – along with a host of other illicit activities – on behalf of Russia's GRU military intelligence unit. 


## [Landing at the NCSC (glad I brought my towel) - NCSC.GOV.UK ](https://www.ncsc.gov.uk/blog-post/landing-at-the-ncsc-glad-i-brought-my-towel)

[https://www.ncsc.gov.uk/blog-post/landing-at-the-ncsc-glad-i-brought-my-towel](https://www.ncsc.gov.uk/blog-post/landing-at-the-ncsc-glad-i-brought-my-towel)

> In my first few weeks as CTO I gave keynote speeches at [SANS CyberThreat 2023](https://www.cyberthreat24.com/) and [BlackHat Europe 2023](https://www.blackhat.com/eu-23/) . During both I laboured the point that seatbelts are **not** a premium feature, and we should not accept the same in the world of technology.
> We live in a free market society where digital services can be given away or sold, yet in some instances cyber security features are deemed premium add-ons. These premium features can include multi-factor authentication or even access to certain levels of logging.
> 
> Volvo didn’t compete on safety in the first instance and [gave away the seat-belt patents](https://www.volvogroup.com/en/about-us/heritage/three-point-safety-belt.html) for the betterment of all. Sadly, outside of the issue of patents in cyber security, many vendors either compete on price (having a lower price point of entry) or upsell security features. For SMEs, charities, education and the public sector, cost consideration is a very real thing, which is often coupled with a lack of cyber security resources. Consequently, it is these organisations (which need the most cyber security assistance) that are most impacted by ‘security as a premium’. 


Lovely to see Ollie blogging and talking in his new role, and hope to see more of this.

I completely agree with Ollie here although I think he’s simplifying something that we need to also consider.  Yes, companies charging more for their security features is annoying and frustrating as a security expert.  I can see that many of the security features are seen as an “enterprise feature” but there is a complexity cost with many security features.  As we’ve seen, it’s sometimes much easier to misconfigure the enterprise features and leave yourself in a far worse condition.

But secondly, financial cost is not the only thing that matters to most organisations.  There is a resource burden, often placed on the same small number of individuals, that means that even if certain products and features were free, the organisations specified probably couldn’t spare the resources to actually use them.  Security features that are free but difficult to configure or add cost are just as out of reach as features that cost money when time is money, which is why we need our products to be secure by default rather than additionally complex to configure security in 


## [Enforcing Device Trust on Code Changes | Figma Blog ](https://www.figma.com/blog/how-we-enforce-device-trust-on-code-changes/)

[https://www.figma.com/blog/how-we-enforce-device-trust-on-code-changes/](https://www.figma.com/blog/how-we-enforce-device-trust-on-code-changes/)

> Git commit signatures are typically used to attest that a trusted author made a code change and get the big green **“Verified” stamp of approval** on GitHub. While this provides more confidence in commit integrity, we don’t have visibility or control over the personal GPG keys engineers register with their account to use for signatures—and no way to tie their GPG keys to a particular device.
> 
> GitHub’s verification criteria are also looser than we’d like. For example, commits made through the GitHub UI and the GitHub API are “Verified” as they’re signed with GitHub’s web flow **GPG key** . If we followed this playbook and an OAuth app or a Figma engineer’s GitHub session, personal access token, or SSH key were compromised, an attacker would have several ways to have their malicious commits “Verified” by GitHub.
> 
> Even with Okta SSO and GitHub commit signature verification, these long-lived access tokens exist outside the trust context where attackers can use them to introduce malicious code. Instead of accepting these risks or introducing processes to monitor for suspicious access token usage, we built our own solution.
> 
> […]
> 
> Shipping this project was a big win for our security team. It gives us GitHub security guarantees by default and sets us up well for future security work with our build and deploy systems. What makes this win even better is that the system we built requires close to no maintenance from our engineers. In an area where we could have accepted unnecessary risk or introduced tiresome processes, we engineered our way into a safer posture instead. This minimization of toil is central to the philosophy of our team, and it frees us up to move quickly on new projects that make Figma more secure. 


Of course, any good silver lining comes with a dark cloud.  Of course commit signing is a good thing, it shows that the people committing to your code repository are who they say they are.  But those keys they sign with are long lived tokens that are probably outside your control, so you have very little confidence that they haven’t been stolen as well.  So Figma did something about this and built a nice system that signs your commits not with your personal GPG key that could live who knows where, but with a machine specific device certificate that is deployed to all managed devices that meet their Okta compliance checks.  

This means that a signed commit definitely came from an authorised person, authenticating to a well managed device.  Oh and Figma roll those device certificates every two weeks to really drill down on that risk. 


## [How Generative AI Is Transforming Business And Society ](https://www.oliverwymanforum.com/global-consumer-sentiment/how-will-ai-affect-global-economics.html)

[https://www.oliverwymanforum.com/global-consumer-sentiment/how-will-ai-affect-global-economics.html](https://www.oliverwymanforum.com/global-consumer-sentiment/how-will-ai-affect-global-economics.html)

> With that in mind, the Oliver Wyman Forum set out to thoroughly examine the attitudes, perceptions, and misperceptions surrounding generative AI. In June and November, we surveyed more than 25,000 people across the United States, the United Kingdom, Canada, Mexico, Brazil, France, Italy, Germany, Spain, China (Hong Kong), India, Indonesia, Singapore, the United Arab Emirates, and Australia.
> 
> The findings highlight the confusion many people feel. While 96% of employees said they believe AI can help them in their current job, 60% are afraid it will eventually automate them out of work. Some 55% of employees use generative AI at least once a week at work, but 61% of users do not find it very trustworthy. Of those 61%, 40% would nevertheless use it to help them make big financial decisions, and 30% would share more personal data for a better experience. 


These numbers are worth taking note of.  50% of employees surveyed use Generative AI at least once a week at work.  That’s a huge number of people, and almost certainly far beyond what executives think it is.

The vast majority of big companies now have Generative AI projects underway at their organisation, so we can see the harnessing of that power happening within companies, but I’d wager that the majority of Gen AI use in companies is not endorsed, tracked or managed to any aspect.

The question not only is “How will you build your own Gen AI products” but “How will you ask your suppliers and products about the ethical, safe and secure use of AI in the products they supply you?” 


## [Tom Scott, and the formidable power of escalating streaks ](https://simonwillison.net/2024/Jan/2/escalating-streaks/)

[https://simonwillison.net/2024/Jan/2/escalating-streaks/](https://simonwillison.net/2024/Jan/2/escalating-streaks/)

> The best way to get really good at anything is to do that thing on a regular basis, thoughtfully, and with the goal of doing it slightly better every time.
> 
> Tom’s streak publishing a video to YouTube once a week for ten years is the single best illustration I’ve ever seen of that principle in action.
> 
> His initial videos were interesting, educational and had his signature enthusiastic energy, but they weren’t exactly high budget affairs.
> 
> As he iterated on the format, he started to figure out what worked. His scripts got tighter, his research deeper and he started working with professionals to improve his production values.
> 
> He also learned to use his growing audience to gain access to a dizzying array of fascinating locations, experts and experiences.
> 
> The amount of work he invested in this project is staggering. The research, logistics, travel, writing, filming, editing and community management involved are hard for me to even comprehend.
> 
> The end result is something truly extraordinary. What a legacy! That final video has over 42,000 comments already, overwhelmingly thankful and positive.
> 
> […]
> 
> Streaks have multiple dangers. At one extreme, they can take over your life, forcing you to leave home behind and spend a decade traveling the world making increasingly brilliant YouTube videos.
> 
> The other challenge is what happens when you accidentally break them.
> 
> In the past, I’ve tried my hand at strict streaks... and then found that 100 days in I miss a day, and suddenly I’m reset to zero and I lose _all motivation_ to continue.
> The solution here is to build in some flexibility. I started a new streak recently to reply to at least one email every day, to encourage me to spend more time in my inbox. My goal for this is four out of seven days, so I can miss three days a week and still keep the streak going. 


I couldn’t agree more with Simon here if I tried.  I’ve often repeated the old agile software delivery maxim “If it hurts, do it more regularly”.  

When we find pain points in software development, whether creating new projects, deploying to production, running database schema changes for example, I’ve found that pushing the frequency of those things up forces people to work out how to automate or at least consistify them to reduce and remove the pain.

I also agree with Simon’s take on streaks being insidious here, especially that loss of motivation.  When I foolishly decided to start writing this newsletter about 4 years ago, I set myself the task of writing something once a week.  I’ve missed that goal a number of times, giving myself a break for burnout reasons, as well as occasional breaks for holidays and things.  But giving some flexibility means that I return to this week in and week out, writing something because it exercises and stretches my mental muscles in a way I find helpful.

What’s the takeaway here?  I think I’d pick out two things from this.  The first is setting yourself a streak or task that you want to repeat over and over again because it has a good effect on you.  That might be doing a daily wordle to improve your vocabulary or it might be writing a newsletter or creating a podcast.  What it is matters less than doing it over and over again to get better at it.

The second for me is recognising that the most important step in any journey is the next one.  You don’t need to produce something that is worthy of someone who has been doing this for years to do it.  Instead just do something, anything, to get started.  Then as you progress, as you do the thing over and over, you’ll get better and better and better.  

But it’s better to take that first step and get started than to wait for the right moment 


## [Cloudypots: Our Latest Method for Uncovering Novel Attack Techniques - Cado Security | Cloud Forensics & Incident Response ](https://www.cadosecurity.com/cloudypots-our-latest-method-for-uncovering-novel-attack-techniques/)

[https://www.cadosecurity.com/cloudypots-our-latest-method-for-uncovering-novel-attack-techniques/](https://www.cadosecurity.com/cloudypots-our-latest-method-for-uncovering-novel-attack-techniques/)

> The premise for how our honeypot VMs would work was simple. First, we deploy a vulnerable service in a VM, configured with ample logging to make it easier to identify attacker activities. We also use OpenStack’s metadata service to generate a new set of [Thinkst canary tokens](https://canarytokens.org/generate) each boot, and automatically place them in credential files such as `.aws/credentials.` We then have a guardrail system placed on the host that flags suspicious activity (see  guardrail section) and automatically runs an “autopsy” on the VM. This process involves pausing the VM, dumping the memory, disk, and network traffic. This is then automatically analysed using the Cado platform and volatility3, which highlights interesting processes, discards duplicate attacks, and tracks the autopsy in Jira. The VM is then reset back to a golden image. 


This is a lovely use of canaries and honeypots to watch for interesting new attackers 


## [How to Permanently Remove Your Fear of Public Speaking ](https://danielmiessler.com/p/permanently-remove-fear-public-speaking)

[https://danielmiessler.com/p/permanently-remove-fear-public-speaking](https://danielmiessler.com/p/permanently-remove-fear-public-speaking)

> As with many things in life, the key to being more comfortable in front of audiences is all about _framing_ .
> 
> Framing is how you look at a situation. Two people could be looking at the identical thing, and if one has a positive frame, or a useful frame, and the other one has a negative one, that distinction is everything.
> 
> It’s the difference between excitement and anxiety, stress and arousal, and looking forward to something versus dreading it.
> 
> […]
> 
> The right side of this scale is what people normally imagine when they hear “public speaking”. They include self-talk like:
> 
> * I’m not practicing; this is the **real** thing
> * I need to worry about **the audience** • It must go **perfectly** 
> * Future talks don’t matter; it’s all on **this one** Well of course you’re scared! That’s terrifying, and a winning recipe for anxiety.
> 
> We are all taught to fear public speaking growing up, and this is why. It’s the _wrong framing_ . 
> 
> **The positive frame** The right frame is to move those sliders to the other side of the spectrum.
> 
> * I’m going to do this talk a dozen or a hundred times. **This is just practice** .
> * My only job is to convey **my love for this topic** , so be enthusiastic! High energy is the key.
> * I don’t need to be perfect; I just need to be **prepared** . The difference is knowing that you are ready, but it will never be perfect. And that’s ok.
> * Know that this is **one of many** . You’re someone who shares your ideas. You’ll do it often. This is one of many. Yawn. Go out there and enjoy it. There’s no such thing as THE BIG ONE because you’ll be getting ready for the next one after this.
> * Ultimately, I’m not a “public speaker”—whatever that means— **I’m someone who shares my enthusiasm for things** . 


I love this for explaining how to think about public speaking to remove the fear of it.  I think this applies both to public speaking, but also to the general act of communicating, whether via blogpost, a public talk, an email or weekly newsletter.

The key is to rethink the way you frame it.  I don’t write these comments because I need them to be perfect, to land with you, to make an impression.  I write these notes for me, so I can internalise what I’m reading, and I write them to sort and order my thoughts.  I share them because I hope that people find them useful, but if 99% of you thought this was boring and skip over it, it doesn’t matter.

Framing is a great way to change your attitude to the big scary things in life, regardless of what they are 


## [Getting Into OT – //SCADAS.EC ](http://scadamag.infracritical.com/index.php/2024/01/13/getting-into-ot/)

[http://scadamag.infracritical.com/index.php/2024/01/13/getting-into-ot/](http://scadamag.infracritical.com/index.php/2024/01/13/getting-into-ot/)

> Most plants and other industrial operations are socially very provincial operations. Operators and Technicians are rightfully wary of well dressed people because those well dressed people usually bring ignorance and unwarranted arrogance with them. 
> 
> The first element of getting your foot in the door is being willing to get down and dirty with the work.
> 
> When I say “down and dirty” I mean understanding the hazards, willing to open up panels in a remote site, and examine how things are wired up. It may be a super-sanitary food processing operation, or it may be a sewage treatment plant. Nevertheless, this is how you earn respect in this business. If the operations and technical staff see that you’re willing to roll up your sleeves and measure things with a voltmeter or turn a screwdriver, they’ll be more willing to give you the straight scoop of what they’re seeing. Otherwise they’ll have doubts you will understand what they’re saying, so they probably won’t bother talking to you.
> 
> There is an entirely new language and concepts for you to learn. You may hear of “grasshopper fuses” or “bumping a motor.” You probably will hear about “confined spaces”, “arc flash”, “neutral current”, “NEMA 4 cabinets”, “explosive environments”, “flashing steam” and the like. These refer to physical layer things. You need to understand physical plant infrastructure.
> 
> You’re very unlikely to know all this in your first day on the job. But if you are always dressing in office attire, rarely ever going on to the plant floor, then you won’t get a chance to learn. A willingness to learn the terminology and get dirty with the technical and operations staff goes a long way. If your immediate supervisor discourages you from doing this for any reason other than safety procedures and training, that’s a red flag that something isn’t right about that place 


An interesting article about getting into the industrial computing area, somewhere where we need more people.  But I think the lesson here is applicable to more than just provincial operations.

When looking at any process, organisation or system, it’s almost always worth going right to the coal face and talking to people.  But you need to value their experience and their outlooks.  If you just look at the managers view, at the spreadsheets and dashboards and then start telling people what you think, the people at the coal face aren’t going to respect your opinions.

One of the reasons that management consultancy has a bad name is because of the times where it does exactly that, where deadlines means that consultants come in, review the reports and propose a new strategy or direction based on them.  But when it works is when those consultants have time to go talk to the workers, to see what’s not appearing in the reports, and then bring suggestions straight from the workfront up to managers.

If in doubt, go and see the work with your own eyes 


## [J. Carlos Roldán / Passwordless: a different kind of hell? ](https://jcarlosroldan.com/post/315/passwordless-a-different-kind-of-hell)

[https://jcarlosroldan.com/post/315/passwordless-a-different-kind-of-hell](https://jcarlosroldan.com/post/315/passwordless-a-different-kind-of-hell)

> I, like most people, hate passwords and all means of authentication bureaucracy. And it looks like we're now at the lowest point in history in terms of UX. There is still hope with the rise of Single Sign-On (SSO) and biometrics. And certainly [passkeys](https://safety.google/authentication/passkey/) , which are getting a lot of traction lately, are a step in the right direction. But only time will tell if their adoption will be widespread enough to make a difference or if we'll be stuck in this dark age of authentication experience for a while. 


I quite liked this little jaunt through password history.  I’m not sure that I entirely agree with the premise here, but there is something funky about the user experience of single sign on systems.  There are multiple competing systems that don’t quite trust each other, and timing out your account access is surefire, but blunt way of ensuring that the account hasn’t been taken over.

But at it’s core, we really should be able to trust that the identity provider can make appropriate decisions about when to re-authenticate the user, and not insist on the user signing in again and again, week after week, day after day. 


