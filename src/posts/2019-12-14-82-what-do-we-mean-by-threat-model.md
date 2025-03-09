---
title: "82 - What do we mean by threat model?"
date: 2019-12-14
description: "You often here security researchers talk about “That’s not in my threat model”, “This is secure only for a certain threat model”, or [“the lock is invincible to the people who do not have a screwdriver”](https://www.theregister.co.uk/2018/06/15/taplock_broken_screwdriver/) , but most of us don’t really know what a threat model is, and our users certainly don’t."
permalink: /what-do-we-mean-by-threat-model/
---

You often here security researchers talk about “That’s not in my threat model”, “This is secure only for a certain threat model”, or [“the lock is invincible to the people who do not have a screwdriver”](https://www.theregister.co.uk/2018/06/15/taplock_broken_screwdriver/) , but most of us don’t really know what a threat model is, and our users certainly don’t.

We tend to assume or build threat models in our heads when we talk about security, and we do so based on our context, our experience, and our assumptions.  But since we never communicate them, we can find ourselves talking at odds with other security professionals because we have different assumed threat models.

One of my sons recently told me that his bike lock was not secure, because “I’d just try 0000 and then 0001 and then 0002 and soon it would be unlocked”.  Since he is young and enjoys maths, I set him the challenge to find out how long it would take to try all 10000 combinations if each try took 2 seconds.  We got the result of around 5-6 hours with a bit of mental math, and then discussed how likely it was that someone would sit and try for 5 hours to unlock his bike and steal it.  (Subnote: search time is actually n/2 on average, so only 2.5 hours, and by trying common combinations early, could be much faster.  My 8 year old didn’t really need the details yet though)

This is really all threat models are really about, who wants to do a bad thing, what bad thing do they want to do and how might they go about it.  There are lots of different models we can use to do this, and they most come in the form of questions that we can ask ourselves.

The Practical PenTest Labs discussion online this week about them storing passwords in plaintext in the database but generating passwords for users was a perfect example of people with very different threat models approaching a problem.

If you assume that the biggest threat to your service is hackers who want to take credentials from existing data breaches and use them against your service, then generating passwords looks sensible.  It’s a perfectly logical and defensible approach to that threat. 
However, the requirement to remind people of their password, meaning storing the passwords in some reversible encrypted form (in essence plaintext) means that there is now a new threat model.  As an attacker, if I can get access to the database, I get access to every single users account, because the username and passwords are enumerable and usable.

In similar experiences, I hear people constantly worry about nation state level attacks.  What if the Chinese target this, what if the NSA target that?  We struggle to enumerate whether these threat models are realistic (how interesting actually are you to a nation state) and we ignore that they have a restricted budget and energy to receive their goals.

As far as I’m aware, there is no standard for threat modelling, making it very hard for us to actually communicate with people about what threat model we had in mind when we made security decisions.  There are a number of neat tools for performing threat models on “systems”, but they are often low level computer and interaction focused, rather than human interaction focused, making them cumbersome and unwieldy for a lot of the sorts of conversations I see around this stuff.

At it’s most basic, I encourage you to consider the threat model next time you consider a security thing.  How much effort is a sim swapping attack to carry out to get access to your email?  Who wants to do that, and are they really interested in you specifically, or people like you?  What would make them move on to someone else?  The simplest way to approach it is just to ask “who? what? how?”  Who is the attacker?  What do they want? How will they get it?

## [Adobe Releases Their December 2019 Security Updates](https://www.bleepingcomputer.com/news/security/adobe-releases-their-december-2019-security-updates/)

[https://www.bleepingcomputer.com/news/security/adobe-releases-their-december-2019-security-updates/](https://www.bleepingcomputer.com/news/security/adobe-releases-their-december-2019-security-updates/)

> Adobe has released a security update for Adobe Acrobat and Reader that fixes 21 vulnerabilities, with many of the being labeled Critical.
> 
> Of the 21 fixed vulnerabilities, 14 are classified as Critical because they could lead to arbitrary code execution, while the other 7 are classified as an Important as they could lead to information disclosure, or for one of the CVEs, privilege escalation.


Parsing PDFs is hard. We tend to point at Adobe for all of these vulnerabilities, but I’m sure other pdf readers are just as vulnerable. 

If you can move your business away from PDFs and towards simple formats, the safer you will be. 


## [Weak encryption cipher and hardcoded cryptographic keys in Fortinet products – SEC Consult](https://sec-consult.com/en/blog/advisories/weak-encryption-cipher-and-hardcoded-cryptographic-keys-in-fortinet-products/)

[https://sec-consult.com/en/blog/advisories/weak-encryption-cipher-and-hardcoded-cryptographic-keys-in-fortinet-products/](https://sec-consult.com/en/blog/advisories/weak-encryption-cipher-and-hardcoded-cryptographic-keys-in-fortinet-products/)

> By intercepting and manipulating internet traffic an attacker can manipulate the responses for FortiGuard Web Filter, AntiSpam and AntiVirus features.
> 
> PROOF OF CONCEPT
> 
> The following Python 3 script decrypts a FortiGuard message (the static XOR key has been removed from this advisory).


This is absolutely an indictment of security company products. Using XOR based encryption with a fixed key has been outmoded since 1553 at least when the Vignerre cipher was published (and that was broken through the Chi Square method in 1863 over 300 years later).  This security practice is utterly indefensible. 

However what’s more annoying to me is that the security company took efforts to “remove the fixed key for security”. But they published known plaintext and cipher text. 

Since XOR is associative (A XOR B = C, A XOR c = B and B XOR C = A), you can simply XOR the plaintext and cipher text and get the key back.

I did this in seconds using [CyberChef](https://gchq.github.io/cyberchef/) proving that redacting the key was an entirely pointless act (as well as just how poor an encryption method this was to use)


## [Assembling cybersecurity: The politics and materiality of technical malware reports and the case of Stuxnet: Contemporary Security Policy: Vol 41, No 1](https://www.tandfonline.com/doi/full/10.1080/13523260.2019.1675258)

[https://www.tandfonline.com/doi/full/10.1080/13523260.2019.1675258](https://www.tandfonline.com/doi/full/10.1080/13523260.2019.1675258)

> The analysis of Symantec’s reports, and its comparison with other companies’ work, shows that such efforts at turning malware into an intelligible event are neither neutral nor a-political. As well as getting translated into discourses of “cybersecurity” as a matter of international political concern, Symantec’s analysis mobilized an assembly of materials and spokespersons, which turned Stuxnet into more than just an object (the code) in the physical and relational sense. Symantec instrumentally mobilized particular alliances in their assembly, to turn the code into an intelligible object and event. For example, by bringing the uranium hexafluoride particles and the centrifuges at Natanz explicitly to the assembly, they also served to bring to presence the IAEA, the UNSC and the political controversy that surrounds Iran’s nuclear enrichment program. Theirs is an example of performative processes of sense-making.


This is a heavy but interesting read.  It acts as a good reminder that threat intelligence companies aren’t politically neutral.  They might be taking your money and giving you a product, but they have their own politics, both local and geographic that affect what strains of malware they analyse and the results that they draw from it.  That doesn’t make them useless by any stretch of the imagination, but its worth keeping in mind and ensuring that the threat intelligence companies whose reports you read are aligned with your world view or at least aligned with threats that you face.


## [Enabling collaboration across the public sector | The Mandarin](https://www.themandarin.com.au/117172-enabling-collaboration-across-the-public-sector/)

[https://www.themandarin.com.au/117172-enabling-collaboration-across-the-public-sector/](https://www.themandarin.com.au/117172-enabling-collaboration-across-the-public-sector/)

> Leadership programs in public sectors often teach top-down leadership methods and models to senior executives. This reinforces the flawed notion that seniority correlates somehow to superiority, which in turn drives senior executive behaviours that disempower and dismiss the experience, expertise and value of people the further down the hierarchy they are. The alternative is to consider “servant leadership” as the new norm in the public sector. Servant leadership is about serving, protecting and supporting the people who work for you to bring their best and whole selves to work. It is about acknowledging that excellence comes from everyone, not just from the top. Servant leadership brings everyone on the journey, and turns change into something that can be collaborative and opportunistic, rather than dreaded. Change is certainly the new normal, so building resilience in our people and teams is critical to maintaining momentum.


A healthy reminder that we need empathy for hard worked staff, that we need to actively create psychological safety in our teams in order to gain the enormous benefits that highly motivated, highly capable, highly agile teams can bring.  That teams wont take risks if they are under pressure, afraid of being shouted at or at risk of losing their jobs.  Leadership is not about command and control anymore, it is about giving teams the direction needed to allow them to be aligned, but autonomous.  Leadership in the modern era, in a “VUCA”environment (Volatile, Uncertain, Complex and Ambiguous) requires a different set of executive behaviours.


## [The accidental CISO | Cybersecurity & Technology News | Secure Futures | Kaspersky](https://www.kaspersky.com/blog/secure-futures-magazine/non-technical-ciso/31674/)

[https://www.kaspersky.com/blog/secure-futures-magazine/non-technical-ciso/31674/](https://www.kaspersky.com/blog/secure-futures-magazine/non-technical-ciso/31674/)

> Find a good vendor, ideally, a good systems integrator (SI). They usually have a poor reputation in the industry, but it’s unfairly so. However with this being a technology-led field, you’re going to have to refer to experts, and who better than organizations that sell multiple types of solutions. Find a good SI. Ensure they’re aware of your budgets and constraints; also that they know you’re looking to build a relationship rather than make a quick purchase.


I mostly agree with Nick on a lot of things, but I think this is suboptimal advice to give non-technical CISO’s.  

The primary strategy I would give a non-technical CISO is to get themselves a technical advisor.  That might be an independent consultant (*ahem*), it might be hiring a tech lead, or it might be finding someone in the organisation you can promote or appoint into that role.  It might only be a day a week, or so, but someone who you can have lunch with, or a few hours once a week to give you a technical view on your problems and potential solutions.

The problem with an SI or any other vendor is that they are always incentivised to give you biased advice.  Even with the best will in the world, their worldview will be based almost entirely around the products that they sell, and they will often be unaware of shifts in the market, or shifts in your organisation, or the context that is needed to make a good decision.

If you absolutely cannot get good independent advice, then you are going to need a good technical relationship with your vendors, and Nick’s advice here is good, but my recommendation would be to get or build some in-house expertise first.


## [DoD Enterprise DevSecOps](https://software.af.mil/wp-content/uploads/2019/12/DSOP-AMA-v1.0.pptx)

[https://software.af.mil/wp-content/uploads/2019/12/DSOP-AMA-v1.0.pptx](https://software.af.mil/wp-content/uploads/2019/12/DSOP-AMA-v1.0.pptx)

> The CSO signed a Memorandum for Record on Nov 26th 2019, sent to all PEOs and PMs regarding the use of DevSecOps and Agile and highly discouraging from using rigid, prescriptive frameworks such as the Scaled Agile Framework (SAFe).
> * Why?
>   * DoD is still using Waterfall or Water-Agile-Fall so until we can truly implement basic Scrum/Kanban, there is nothing to « SCALE ». Agile should be applied across the entire Program, not just the development team, that includes: Contracting, Program Management, Reporting to leadership (no EVM) etc!
>    * You cannot scale if you don’t have the “basics” right. At best, such frameworks put us at risk to fall back to what we know and go back to Waterfall because of their “mapping”.


There’s a lot of goodness in this simple presentation.  That Department of Defence is building a great approach for a large scaled organisation here.  Simple platforms that make it easy for lots of independent teams to work independently, but using secure basic platforms and tools.  This right here is how you solve the basics, and should be the starter for almost any digital organisation that runs at a scale that has multiple development teams, especially if they aren’t collocates.

But this about the SAFe process is brilliantly put.  The problem with SAFe is not that it’s a bad framework (although I’d argue that it is), it’s that organisations want to jump into a process that makes them feel safe without actually transforming.  As the DoD so ably puts it, “Until you can implement basic <agile>, there is nothing to Scale!


## [Mobile devices blur work and personal privacy raising cyber risks -- ScienceDaily](https://www.sciencedaily.com/releases/2019/12/191205141759.htm)

[https://www.sciencedaily.com/releases/2019/12/191205141759.htm](https://www.sciencedaily.com/releases/2019/12/191205141759.htm)

> Dr Degirmenci's published research, Future of Flexible Work in the Digital Age: Bring Your Own Device Challenges of Privacy Protection, will be presented at the International Conference on Information Systems in Munich in December.
> 
> "The breakneck speed of digital transformation brought with it opportunities as well as threats," he said.
> 
> "Organisations don't appear to be keeping up with the pace of change, deliberately putting the brakes on digital transformation because it comes with security challenges."


I’ve been reading news stories about breaches for several years now. I cannot think, offhand, of a single one where the root cause was data stored on an unmanaged device through a BYOD program. 

I recognise the individual risk, there are lots of stories of political journalists getting leaked government documents, but mostly because the leakers are senior enough to have unmanaged devices or the ability to take physical copies home. 

The real story here is the BYOD is massively on the rise and if you aren’t explicitly supporting it, then your staff are probably doing it without your knowledge and support. Make your IT usable, useful and safe and all these “risks” go away. 


## [Chinese APT group Calypso hacked state institutions in six countries | SC Media](https://www.scmagazine.com/home/security-news/apts-cyberespionage/chinese-apt-group-calypso-hacked-state-institutions-in-six-countries/)

[https://www.scmagazine.com/home/security-news/apts-cyberespionage/chinese-apt-group-calypso-hacked-state-institutions-in-six-countries/](https://www.scmagazine.com/home/security-news/apts-cyberespionage/chinese-apt-group-calypso-hacked-state-institutions-in-six-countries/)

> The researchers found the hackers either exploited a remote code execution vulnerability MS17-010 or used stolen credentials.
> 
> “These attacks succeeded largely because most of the utilities the group uses to move inside the network are widely used by the specialists everywhere for network administration,” said Denis Kuvshinov, lead specialist in threat analysis at Positive Technologies. “The group used publicly available utilities and exploit tools, such as SysInternals, Mimikatz and EternalRomance. Using these widely available tools, the attackers infected computers on the organization’s LAN and stole confidential data.”


Publicly available tools, simple exploit tools that anyone can download and use.  We worry about nation states, but over and over again we see evidence that they just use the simplest of tools.  If you are protecting yourself against script kiddies and amateur hackers, you are also protecting yourself against the highest capability threats out there (or at least forcing them to use their expensive high capabilities, which has a cost for them)


## [49% of workers, when forced to update their password, reuse the same one with just a minor change](https://www.grahamcluley.com/49-of-workers-when-forced-to-update-their-password-reuse-the-same-one-with-just-a-minor-change/)

[https://www.grahamcluley.com/49-of-workers-when-forced-to-update-their-password-reuse-the-same-one-with-just-a-minor-change/](https://www.grahamcluley.com/49-of-workers-when-forced-to-update-their-password-reuse-the-same-one-with-just-a-minor-change/)

> For instance, not only did 72% of users admit that they reused the same passwords in their personal life, but also 49% admitted that when forced to update their passwords in the workplace they reused the same one with a minor change.
> 
> Furthermore, many users were clearly relying upon their puny human memory to remember passwords (42% in the office, 35% in their personal lives) rather than something more reliable. This, no doubt, feeds users’ tendency to choose weak, easy-to-crack passwords as well as reusing old passwords or making minor changes to existing ones.


More evidence that we suck at passwords.  We really really suck at passwords.  When presented with complex systems that put the effort on the user, we find ways to work around the system.  Whether that be creating memorable passwords, or emailing our work to our private account to work on from home, people want to find ways around the systems we put in place.  Good security must be usable security first and foremost.


## [The Security of Modern Password Expiration: An Algorithmic Framework and Empirical Analysis](https://www.cs.unc.edu/~fabian/papers/PasswordExpire.pdf)

[https://www.cs.unc.edu/~fabian/papers/PasswordExpire.pdf](https://www.cs.unc.edu/~fabian/papers/PasswordExpire.pdf)

> We show, for example, that by instantiating our transform-based algorithmic framework with a particular class of transforms, we can break future passwords from past ones in 41% of accounts on average in an offline attack with expected effort of under 3 seconds per account on a 2.67GHz pro- cessor. We also show that we can break 17% of accounts on average in an online attack, with fewer than 5 online guesses in expectation.


We know that everyone follows the same rules for passwords, especially if they are asked to create multiple passwords under password constraints.  If you need a capital letter, you’ll capitalise the first letter.  If you need a number in a password, you’ll add a 1 to the end.  If you are a certain type of user, you’ll use “l337 sp34k”, substituting 3 for e, 4 for a, 0 for o etc.

We’ve known this for years, but there hasn’t been much actual evidence, just a set of security researchers  (and NIST and NCSC) feelings about it.

Now we have a paper that shows that if we know a previous password, we can determine what rules you follow and break 41% of your future passwords if we are offline.  And worse, with an online account that locks you out within 5 tries, if we have a breached password from a previous databreach, we have a 1-in-5 chance of getting your password correct within those 5 tries.

Passwords still suck, but they’re going to be around for a long time.  We need to improve password hygiene by stopping complexity rules, stopping rotation, encouraging password managers and pass phrases, and we need to make passwords work for real people in their real life.


## [Troy Hunt: Generated Passwords, UX and Security Absolutism](https://www.troyhunt.com/generated-passwords-ux-and-security-absolutism/)

[https://www.troyhunt.com/generated-passwords-ux-and-security-absolutism/](https://www.troyhunt.com/generated-passwords-ux-and-security-absolutism/)

> But as for "all sites should generate the user's password", no, you're never going to see it happen at Disney because they actually want customers! This, again, is security absolutism because it places security above and beyond all else and damn the consequences.
> By all means, people should robustly debate the merits of alternate auth systems, but you cannot escape the reality that no matter how endorsed you might be in this approach, websites simply don't implement it. There are very good reasons why not and if you're inclined to chime in on the comments section in support of generated passwords, perhaps start with thinking about why this approach is so rarely seen.


I saw this mess online, with Practical PenTest Labs basically claiming online that by generating users passwords and not allowing them to be changed, they were reducing the risk of credential stuffing.  It was a great example of security thinking that is wrong in the large, even if its right in the details.  It’s exactly the same thinking that gets people to do the maths about password entropy and declare that pass phrases have lower entropy than random passwords.  They’re correct, but they’re that worst form of correct, “technically correct”.  Given a truely random password made of symbols and mixed caps letters, there are more possible combinations than English language words for a pass phrase.  But when you add the human element, that people don’t create random passwords, they create passwords that follow predictable patterns, it all gets a lot less mathematical and more subjective.

As Troy ably points out here, generating a users password for them create a user experience nightmare that almost certainly results in a less secure service, as well as a worse user experience.


