---
title: "56 - How can we be more positive in security?"
date: 2019-06-18
description: "Cybersecurity is a pessamists game right?  We are constantly talking about and worrying about being attacked, about what is the worst that can happen, about the nations in a constant state of cyberwar!"
permalink: /how-can-we-be-more-positive-in-security/
---

Cybersecurity is a pessamists game right?  We are constantly talking about and worrying about being attacked, about what is the worst that can happen, about the nations in a constant state of cyberwar!

But we overly focus on the negative.  I took at a look at the stories that I read for this week, and I had around 35 stories selected as potential stories to go in here, from a digital transformation failure in Denmark, to Snapchat spying tools, from updates on the spread of banking trojans to worries about chinese backdoors in drones (I'll feature all of those next week).

But I put a request out with friends for any positive stories, any blog posts or information on cyber security successes, on people building and showing great advances in cybersecurity.  And I got nothing back.  Nobody had a good story to tell, or at least share.

A friend was commenting on a common interview question that they ask people, "Which is better from a security perspective, IaaS, PaaS or SaaS?" and that the common answer was IaaS (apart from one wag who said "On Premise Hardware"), and it got us thinking about why that is.  The stated reason from a security perspective is often claimed to be control.  That with fewer layers of abstraction between your system and the underlying supplier, you have more visibility than you would with a more abstract system.

However, I don't believe that it's the case that a PaaS is necessarily more or less secure than an IaaS.  I don't think the level of abstract necessarily changes the level of security of the whole thing, but it does change your approach to security.  I think that a good PaaS provider is probably providing you with a more secure platform than if you badly manage your IaaS yourself, but it's hard to know whether the PaaS provider is doing any of the things you need.  With greater abstraction comes greater trust in the vendor or their assurance mechanisms.  

We seem to struggle with trust as a profession, I suspect because we spend so much time professionally thinking about what can go wrong.

I decided to try to find as many positive stories about how things are getting better, or specifically, where people have implemented new tools, techniques or processes that enable us all to learn and see how things can be better.  There is hope, there are people making things better, it's just harder to see amongst all of the cynicism.  This week should give you some insight into that I hope

## [CyBOK - HUMAN FACTORS KNOWLEDGE AREA [pdf]](https://www.cybok.org/media/downloads/Human_Factors_KA_-_draft_for_review_June_2019v2.pdf)

[https://www.cybok.org/media/downloads/Human_Factors_KA_-_draft_for_review_June_2019v2.pdf](https://www.cybok.org/media/downloads/Human_Factors_KA_-_draft_for_review_June_2019v2.pdf)

> ‘Never issue a security policy that can’t be followed’ (Or: General MacArthur, shadow security and security hygiene)
> 
> The famous WWII military leader General Douglas MacArthur coined the phrase ‘never give an order that can’t be obeyed.’ He recognised the corrosive impact of a single order that cannot be followed in reality—it undermines the credibility of all orders and the superiors who issue them and seeds uncertainty and doubt. It is the same with security policies: when employees encounter security policies that are impossible to follow or are clearly not effective, it provides a justification for doubting all security policies. That is why security hygiene is essential. When policies are not being followed, security professionals must investigate, in a nonconfrontational manner, why and if it is because they are impossible or too onerous to follow and re-design the solution. 
> 
> Kirlappos et al. pointed out that in most cases, employees do not show blatant disregard for security, but try to manage the risk they understand in the best way know how, what they call shadow security [37]. Their ‘amateur’ security solutions may not be entirely effective from a security perspective, but since they are ‘workable’, asking ‘how could we make that secure’ is a good starting point for finding an effective solution that fits in with how people work.


Another release in the attempt by the NCSC to document the entire field of cyber.  This is a good introduction to the psychology, sociology and usability of cyber security systems and feels approachable and less academic than some of the others.


## [This Deepfake of Mark Zuckerberg Tests Facebook’s Fake Video Policies - VICE](https://www.vice.com/en_us/article/ywyxex/deepfake-of-mark-zuckerberg-facebook-fake-video-policy)

[https://www.vice.com/en_us/article/ywyxex/deepfake-of-mark-zuckerberg-facebook-fake-video-policy](https://www.vice.com/en_us/article/ywyxex/deepfake-of-mark-zuckerberg-facebook-fake-video-policy)

> Two artists and an advertising company created a deepfake of Facebook founder Mark Zuckerberg saying things he never said, and uploaded it to Instagram.
> 
> The video, created by artists Bill Posters and Daniel Howe in partnership with advertising company Canny, shows Mark Zuckerberg sitting at a desk, seemingly giving a sinister speech about Facebook's power. The video is framed with broadcast chyrons that say "We're increasing transparency on ads," to make it look like it's part of a news segment.


As predicted, we're now seeing fairly easy to create deep fakes.  It wont be long before we start seeing real people say that they didn't say a certain thing, and nobody is able to tell whether seeing a video of a politician with your own eyes is trustworthy or not.


## [Deepfakes have got Congress panicking. This is what it needs to do. - MIT Technology Review](https://www.technologyreview.com/s/613676/deepfakes-ai-congress-politics-election-facebook-social/)

[https://www.technologyreview.com/s/613676/deepfakes-ai-congress-politics-election-facebook-social/](https://www.technologyreview.com/s/613676/deepfakes-ai-congress-politics-election-facebook-social/)

> The draft bill, a product of several months of discussion with computer scientists, disinformation experts, and human rights advocates, will include three provisions. The first would require companies and researchers who create tools that can be used to make deepfakes to automatically add watermarks to forged creations.
> 
> The second would require social-media companies to build better manipulation detection directly into their platforms. Finally, the third provision would create sanctions, like fines or even jail time, to punish offenders for creating malicious deepfakes that harm individuals or threaten national security. In particular, it would attempt to introduce a new mechanism for legal recourse if people’s reputations are damaged by synthetic media.
> 
> “This issue doesn’t just affect politicians,” says Mutale Nkonde, a fellow at the Data & Society Research Institute and an advisor on the bill. “Deepfake videos are much more likely to be deployed against women, minorities, people from the LGBT community, poor people. And those people aren’t going to have the resources to fight back against reputational risks.”
> 
> The goal of introducing the bill is not to pass it through Congress as is, says Nkonde. Instead it is meant to spark a more nuanced conversation about how to deal with the issue in law by proposing specific recommendations that can be critiqued and refined. “What we’re really looking to do is enter into the congressional record the idea of audiovisual manipulation being unacceptable,” she says.


This draft bill is clearly quite daft, because, at this point, it's incredibly hard to legally differentiate between a video that has been manipulated by editing and slicing in order to manipulate in a hostile manner from one that has been editing and sliced for editorial purposes.

Naturally, newsmakers edit clips of politicians all the time, extracting the "newsworthy bit" of the speech, but Breitbart might find a different clip newsworthy compared to the BBC, and I don't think we're able to define how much editing is acceptable.


## [Teaching Intelligence Analysts in the UK — Central Intelligence Agency](https://www.cia.gov/library/center-for-the-study-of-intelligence/csi-publications/csi-studies/studies/vol-52-no-4/teaching-intelligence-analysts-in-the-uk.html)

[https://www.cia.gov/library/center-for-the-study-of-intelligence/csi-publications/csi-studies/studies/vol-52-no-4/teaching-intelligence-analysts-in-the-uk.html](https://www.cia.gov/library/center-for-the-study-of-intelligence/csi-publications/csi-studies/studies/vol-52-no-4/teaching-intelligence-analysts-in-the-uk.html)

> The example below sets out an apparently simple practical problem that just might be posed to an analyst supporting an arms control inspection regime:
> 
> You are an imagery analyst looking for an unlawful biological warfare trailer. You think it could be hidden in one of three equally likely locations, A, B or C. You pick one, say site C, and start to prep the arms control inspectors for a snap inspection. The host country then unexpectedly throws open one of the other sites, site A, to journalists so it is obviously not there. You have the chance to change your advice to the inspection team and tell them now to go to site B or stick with your original choice, C. Should you change, or stick to C?
> 
> When posed this question, analysts immediately split into two camps. The minority quickly spots the underlying structure of what in North America is known as the “Monty Hall problem,” from the name of the game show host.[viii] As a problem in probability it is straight forward, if paradoxical. The majority of analysts who have not come across the problem refuse to believe the result when they first come across it but can be persuaded to follow the probabilistic reasoning, as set out in Figure 1.
> 
> That, however, is the start of the teaching point. The analysis of the probabilities in the graphic depends upon a set of strict assumptions that are not explicit in the question. For the intelligence analyst little, if anything, should be taken for granted, especially statements from the opponent. What unlocks a proper analysis of the problem for the analyst is understanding where implicit assumptions are being made about the reporting being received. For example, do we assume that the opponent knows which initial site was picked (the question does not say so)? If not, the solution is quite different. Would it be safe not to assume he knows, given the history of arms inspection regimes? Is the opponent engaged in deception, using the media as a shield? Can it be safely assumed that the opponent who threw open the site was privy to the secret of where the bio-trailer was actually located? And so on.
> 
> In the end, the problem reduces to a number of alternative hypotheses, on a number of different assumptions, and the analyst can use the Heuer table approach to rank these. Our calculations show that the problem is asymmetric: the wise analyst will advise switching on the grounds that some assumptions will improve the prediction, while on others it makes the chances no worse.


This is an old but a fsacinating read about how the intelligence analyst profession was changed and shaken up as the result of the Butler review into failing in the Iraqi WMD investigation and analysis.

Sadly, the handbook released by the professional head of intelligence analysts has never been publicly released, but this overview shows the sorts of things that the profession has to graple with, especially the number of confounding questions.

The most interesting one to me is the question of "Did the person revealing the site know where the real weapons were?".  A common fallacy I see upheld by lots of people in lots of contexts, is to assume that organisations are single purpose organisations rather than collections of people.  Google doesn't have a view on technical subjects, the individuals you meet who represent it do.  The behaviour of organisations can appear illogical or irrational (to use an economic term) precisely because not every individual has the exact same information and understanding.


## [Project Svalbard: The Future of Have I Been Pwned](https://troy.hn/31rlwmq)

[https://troy.hn/31rlwmq](https://troy.hn/31rlwmq)

> Oh – and as I’ve written before, commercial subscribers that depend on HIBP to do everything from alert members of identity theft programs to enable infosec companies to provide services to their customers to protecting large online assets from credential stuffing attacks to preventing fraudulent financial transactions and on and on. And there are the governments around the world using it to protect their departments, the law enforcement agencies leveraging it for their investigations and all sorts of other use cases I never, ever saw coming (my legitimisation of HIBP post from last year has a heap of other examples). And to date, every line of code, every configuration and every breached record has been handled by me alone. There is no “HIBP team”, there’s one guy keeping the whole thing afloat.


This is interesting, Troy's HIBP (which I've referenced here several times before) is an interesting personal project that has significantly grown, and he's decided to essentially sell it.  

The key here will be working out what it's worth, and what it actually needs.  As I think I've said before, there's some real issues I have with telling users that their password was once breached, without being able to know whether they've changed it since.  It's possible that with better integrations with vendors, they might be able to make this dataset more actionable.


## [Detect Tactics, Techniques & Combat Threats](https://github.com/rabobank-cdc/DeTTACT)

[https://github.com/rabobank-cdc/DeTTACT](https://github.com/rabobank-cdc/DeTTACT)

> DeTT&CT aims to assist blue teams using ATT&CK to score and compare data log source quality, visibility coverage, detection coverage and threat actor behaviours. All of which can help, in different ways, to get more resilient against attacks targeting your organisation. The DeTT&CT framework consists of a Python tool, YAML administration files and scoring tables for the different aspects.
> 
> DeTT&CT provides the following functionality:
> 
> *    Administrate and score the quality of your data sources.
> *    Get insight on the visibility you have on for example endpoints.
> *    Map your detection coverage.
> *    Map threat actor behaviours.
> *    Compare visibility, detections and threat actor behaviours in order to uncover possible improvements in detection and visibility. This can help you to prioritise your blue teaming efforts.
> 
> The coloured visualisations are created with the help of MITRE's ATT&CK™ Navigator.


This is a nice looking tool to work with the ATT&CK tooling which categorises attacker tools and techniques.  This tool seems to analyse your log sources and then you score them on what indicators you'd expect to see from that data source.

It can then crunch all of your data sources and show which tools and techniques you are protected against and where you are lacking.

I suspect a lot of this would reinforce ones gut feel, and will show the value of certain controls.  However I don't think it models confidence or effectiveness of a control, so for example, if you get web proxy logs, it wont tell you that 3 servers are configured and allowed by old firewall rules to go around that control.


## [NSA recommendations | algorithms to use until PQC](https://www.johndcook.com/blog/2019/05/23/nsa-recommendations/)

[https://www.johndcook.com/blog/2019/05/23/nsa-recommendations/](https://www.johndcook.com/blog/2019/05/23/nsa-recommendations/)

> The NSA has also made some suggestions for what to do in the mean time [1]. Last year the agency replaced its Suite B cryptography recommendations with the CNSA: Commercial National Security Algorithm Suite.
> 
> In a nutshell: use well-established methods for now but with longer keys.
> 
> In a little larger nutshell, the recommendations are:
> 
> SHA-384 for secure hashing
> AES-256 for symmetric encryption
> RSA with 3072 bit keys for digital signatures and for key exchange
> Diffie Hellman (DH) with 3072 bit keys for key exchange
> Elliptic curve P-384, both for key exchange (ECDH) and for digital signatures (ECDSA)


Good recommendations, and I agree with the view that Quantum Resistant algorithms right now are snake oil, since we just haven't had enough good research to understand them well.


## [Top cybersecurity companies are pooling their intel to stop cyberattacks - The Washington Post](https://www.washingtonpost.com/news/powerpost/paloma/the-cybersecurity-202/2019/05/23/the-cybersecurity-202-top-cybersecurity-companies-are-pooling-their-intel-to-stop-cyberattacks/5ce5ef73a7a0a46b92a3fd95/?noredirect=on&utm_term=.54a5d7d70ada)

[https://www.washingtonpost.com/news/powerpost/paloma/the-cybersecurity-202/2019/05/23/the-cybersecurity-202-top-cybersecurity-companies-are-pooling-their-intel-to-stop-cyberattacks/5ce5ef73a7a0a46b92a3fd95/?noredirect=on&utm_term=.54a5d7d70ada](https://www.washingtonpost.com/news/powerpost/paloma/the-cybersecurity-202/2019/05/23/the-cybersecurity-202-top-cybersecurity-companies-are-pooling-their-intel-to-stop-cyberattacks/5ce5ef73a7a0a46b92a3fd95/?noredirect=on&utm_term=.54a5d7d70ada)

> The effort, which CTA calls “early sharing,” comes as top cybersecurity officials are looking for ways industry and government can cooperate to punish government-linked hacking groups in Russia, China, Iran and North Korea that are behind many of the most damaging campaigns. 
> 
> By denying those hacking groups as much access as possible, CTA can help government by making it much costlier for the groups to restart operations, its president Michael Daniel told me.
> 
> “From my perspective, the U.S. government won’t be able to tackle this without the cybersecurity companies,” said Daniel, who was White House cybersecurity coordinator during the Obama administration. “Together we can raise the cost on the adversary much more … than if the government does something by itself.”
> 
> To make this work, these security companies are setting aside business concerns about competition in favor of helping improve the threat landscape. It reflects a general conclusion in recent years that companies are better off sharing big picture information about threat intelligence rather than competing for small advantages.
> 
> The program is an offshoot of CTA's main mission to share much more basic digital threat indicators among top cybersecurity companies.


This is a good story about how organisations are working together.  I like the Cyber Threat Alliance for the combination of several threat intelligence firms, each trying to ensure that while they compete with each other, that their customers value getting information in a standard way from all of them.


## [Apple announces new sign-in tool to compete with Facebook and Google - The Verge](https://www.theverge.com/2019/6/3/18650885/apple-sign-in-sso-tool-data-collection-privacy-ios-13-wwdc-2019)

[https://www.theverge.com/2019/6/3/18650885/apple-sign-in-sso-tool-data-collection-privacy-ios-13-wwdc-2019](https://www.theverge.com/2019/6/3/18650885/apple-sign-in-sso-tool-data-collection-privacy-ios-13-wwdc-2019)

> Apple introduced a new single sign-on (or SSO) tool called “Sign In with Apple,” designed to authenticate users to apps while sharing a minimum of personal data with third parties. It’s a direct competitor to simpler services offered by Facebook and Google, which were called out by name on stage, and part of Apple’s broader effort to brand itself as a privacy-conscious alternative to those companies. The new system will be available across apps as well as on the web.
> 
> As described onstage by Apple software chief Craig Federighi, users would encounter the service as a simple sign-in button, presented as an alternative to setting up a persistent username and password for a given service. But where Google and Facebook use those buttons to link you to your broader advertising profile, Apple’s service is designed to give the minimum necessary data.
> 
> The system won’t even share your email, instead directing each app to a different redirect email address operated by Apple. With a different redirect for each app, it would be far more difficult for third parties to correlate information by comparing emails. And when a user wants to cut ties with an app, breaking the redirect will sever the connection entirely.


This is a lovely model for sign in. On the basis that you already trust Apple with everything, allowing the single sign on to generate throw away disposable identities for the site means that nobody can connect your identity in that database with any other database unless you give them more information to identify yourself.

That includes both attackers who steal the database as well as the owners of the site itself.


## [What I Learned Trying To Secure Congressional Campaigns (Idle Words)](https://idlewords.com/2019/05/what_i_learned_trying_to_secure_congressional_campaigns.htm)

[https://idlewords.com/2019/05/what_i_learned_trying_to_secure_congressional_campaigns.htm](https://idlewords.com/2019/05/what_i_learned_trying_to_secure_congressional_campaigns.htm)

> Talking about degrees of safety, and giving people an incremental path to secure behavior. For example, we told campaigns it was best to have a password manager, okay to have a written list of random passwords, dangerous to have a password pattern you would modify across sites, and unacceptable to re-use a single password across sites. That way people could improve their security incrementally until they got to the recommended configuration, even if they couldn't get all the way there in one step. I preferred that they use their cat's birthday as their Google password and their dog's birthday for Facebook, rather than the dog's birthday for both. We live in a fallen world.


Brilliant writing, and a great example of incrementally improving security.  This entire essay is worth a read.

But this bit really got to me.  When we think about degrees of safety and we concentrate on just trying to get someone to move their security up a single degree, and accept that this isn't going to be 100% secure, but is going to make things better, then we are far more constructive and positive an influence.


