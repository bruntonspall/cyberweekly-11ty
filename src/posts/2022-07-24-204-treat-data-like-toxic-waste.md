---
title: "204 - Treat data like toxic waste"
date: 2022-07-24
description: "It seems that the argument for privacy and lawful interception has erupted once more."
permalink: /treat-data-like-toxic-waste/
---

It seems that the argument for privacy and lawful interception has erupted once more.

There's a couple of good posts below by some smart thinkers in this field, and while many of the participants firmly disagree with each other, I think it's positive that the debate and discussion is moving beyond the fundemental technology and up into a far more philosophical and reasoned debated about the social, moral and ethical debate around the right to privacy.

Although I tend to lean far more towards the privacy side than the typical person, I'm not an absolutist in this area, and I do think that we need some way for governments and law enforcement to regulate and uphold their laws.  How we do that in an increasingly globalised and deregulated tech world, where the main influencers are so wildly opposed in their ideas is a bit beyond me though!

However, that, alongside the recent rulings in the US around Roe-vs-Wade does remind us that corporations and organisations collecting data must assume that at some point, somebody might want to use that data in a way that doesn't match their own internal framework for doing so.

One person I worked with a few years back, very wisely told me that "Data should be handled like it's toxic waste".  His view was that it was sometimes necessary to handle personal data, but that you should do everything in your power to avoid it if possible, and to minimise how much of it you hold, and where it goes.  

Over the years, I've seen many systems that get caught up in just slurping up all the data "just in case", so that someone can do some analytics on it later.  But if we are careful at the borders of our systems and organisations to anonymise data where we can, and simply not collect it if possible, then we can be sure that it cannot be leaked, sold by insiders or misused.

Those threat models of attacks on the personal data we hold are really tricky to reason about, and they're not common threat models to consider, but the easiest defence to reason about is to simply not collect the data at all.

## The Cyberweekly Survey

As I’ve been doing this newsletter for nearly 4 years, I decided that it was time to find out if I’m doing a good job. I can tell from subscriptions that more and more people are subscribing, but I don’t know what’s working well or badly. I’ve put together some simple questions into a Google Form, and if you’ve got 2-5 minutes, I’d really appreciate some feedback. You can find the Form here: [https://docs.google.com/forms/d/e/1FAIpQLSeojV4ILcB7Oz9rPtNMPHCGRFL1ctfaiwpS2ZvsOqbCBDu9rA/viewform?usp=sf_link](https://docs.google.com/forms/d/e/1FAIpQLSeojV4ILcB7Oz9rPtNMPHCGRFL1ctfaiwpS2ZvsOqbCBDu9rA/viewform?usp=sf_link)

## [British recycle old arguments for bypassing E2E encryption • The Register ](https://www.theregister.com/2022/07/22/british_encryption_scanning/)

[https://www.theregister.com/2022/07/22/british_encryption_scanning/](https://www.theregister.com/2022/07/22/british_encryption_scanning/)

> In their latest paper Levy and Robinson argue that this isn't a major issue, since non-governmental organizations could be used to moderate the automatic scanning of personal information for banned material. This would avoid the potential abuse of such a scheme, they argue, and only the guilty would have something to fear.
> 
> It's not a new argument, and has been used again and again in the conflict between encryption advocates who like private conversations and governments that don't. Technology experts mostly agree such a system can't be insulated from abuse: the scanning could be backdoored, it could report innocent yet private content as false positives, or it could be gradually expanded to block stuff politicians wish to suppress. Governments would prefer to think otherwise, but the paper does at least acknowledge that people seeking privacy aren't suspects.
> 
> "We acknowledge that for some users in some circumstances, anonymity is, in and of itself, a safety feature," Levy and Robinson opine. "We do not seek to suggest that anonymity on commodity services is inherently bad, but it has an effect on the child sexual abuse problem."
> 
> Which is a soft way of saying conversations can be used to plan crimes so they should be monitored. No one's denying the incredible harm that stems from the scum who make CSAM, but allowing monitoring of all private communications – albeit by a third party – seems a very high price to pay. 


This pulls together both some valid and I think some invalid criticisms.  The paper in question explicitly sets out to argue how important it is to prevent mission creep in the sorts of content that is scanned for, and how one might structure systems to prevent that.

But it’s legitimate to point out that these systems are almost impossible to protect from abuse, and therefore we need to decide, rather philosophically much like a trolley problem, whether taking an action that results in less harm to fewer people is better than not taking action that results in greater harm.

There are no good answers here, and the cat is already out of the bag, but the debate will prove to be lively 


## [Thoughts on Child Safety on Commodity Platforms [pdf] ](https://arxiv.org/pdf/2207.09506.pdf)

[https://arxiv.org/pdf/2207.09506.pdf](https://arxiv.org/pdf/2207.09506.pdf)

> For many years, most mainstream social media and communication platforms have implemented
> technical mitigations that help protect some of their most vulnerable users, including children,
> from abuse taking place on the platforms and real-world abuse facilitated by the platforms.
> These technologies are used to detect potential child sexual abuse related activity which is then
> often referred to a human moderator to confirm illegal content, before being passed to the
> relevant national body that is authorised to deal with such referrals.
> 
> Recently, many of these same platforms have started to remove their own access to user content,
> through technologies including end-to-end encryption, ostensibly to provide privacy for their
> users. This move fundamentally breaks most of the safety systems that protect users, and that
> law enforcement rely on to help find and prosecute offenders. As a result, governments around
> the world have vociferously raised the spectre of ‘safe places’ where child abusers can operate
> with impunity, while academics and privacy campaigners have raised the spectre of a world of
> technology that is ‘insecure by default’, where privacy and security are fundamentally impossible,
> with poor design choices justified through the exhortation ‘Think of the children!’. Both potential
> futures are possible. We believe that neither are inevitable or desirable. 


This is a thoughtful bit of work that attempts to frame the debate around clientside scanning with more detail about what it’s trying to achieve, how it might be done, and what the societal implications might be.

What it does well is articulate strongly that this is not really a technical problem at all.  The technology to scan users content for abusive material exists today, but the legislative and social will to do so, the societal question of whether platform providers even should, and the underlying questions about whether this is a government matter, a platform matter or an individual matter are all still unanswered in the debate.

That discussion about just how much privacy from the state one can or should have is a much harder discussion to have. 


## [A Civil Society Glossary and Primer for End-to-End Encryption Policy in 2022 ](https://alecmuffett.com/alecm/e2e-primer/e2e-primer-web.html)

[https://alecmuffett.com/alecm/e2e-primer/e2e-primer-web.html](https://alecmuffett.com/alecm/e2e-primer/e2e-primer-web.html)

> Three fundamental questions have driven the [Crypto Wars](https://en.wikipedia.org/wiki/Crypto_Wars) for the past 30+ years, and they are approximately as follows:
> 
> 1. should individuals remain free to keep a secret, even from the state?
> 2. should consenting parties remain free to communicate in a manner that is private, even from the state?
> 3. should third parties ever be obliged to _not enable_ – or even _actively prevent_ – access to the above freedoms?
> 
> Readers are encouraged to consider the entirety of this report in the light of these three questions. They are key to everything which follows, and I shall return to them in the afterword. **The “Field Model” and the Historical Mundanity of Privacy** It is inarguable that individuals may keep secrets, even from the state. There may be _consequences or punishments_  [1](https://alecmuffett.com/alecm/e2e-primer/e2e-primer-web.html#fn:Old-Bailey-Solic)  [2](https://alecmuffett.com/alecm/e2e-primer/e2e-primer-web.html#fn:Kerr-The-Law-of) meted out for doing so – or for being _presumed_ to be doing so – however every person is de facto at liberty to think or believe whatever they choose within the confines of their own head, and to also (attempt to…) omit or lie to others regarding what they have thought or believed.
> 
> Drawing upon this to paraphrase [Whitfield Diffie](https://en.wikipedia.org/wiki/Whitfield_Diffie) and other encryption and privacy experts and commentators, we can consider the _field model_ : [3](https://alecmuffett.com/alecm/e2e-primer/e2e-primer-web.html#fn:Diffie-Landau-Pr)  [4](https://alecmuffett.com/alecm/e2e-primer/e2e-primer-web.html#fn:Froomkin-The-Met)  [5](https://alecmuffett.com/alecm/e2e-primer/e2e-primer-web.html#fn:Froomkin-q-v-At) _Field Model_ : All that was once necessary for two or more people to have a private conversation was for them to _walk into a field_ – _away from eavesdroppers_ – where they could _simply talk_ …
> 
> […]
> 
> For the rest of this report I shall discuss _end-to-end secure and encrypted communication_ ; for brevity I shall refer to this by the acronym _E2E_ .
> 
> The intention of E2E is to _restore the model and benefits of two or more people talking privately in a field_ – but in a world of _digital communication_ where participants may be physically or virtually _separated_ from each other.
> 
> This goal requires the _exclusion_ of message content from all entities who are _not participants_ in the conversation – where, exactly as in the _field model_ – participation is analogously defined as one who is _apparent as being within earshot of the speaker_ .
> 
> […]
> 
> Question: is a person able to have an E2E conversation with their bank?
> Some E2E purists would say _no_ , but I believe that it’s entirely reasonable for a person to communicate with their bank – most likely: their bank’s call-centre representatives – by means of E2E channels, and to expect the guarantees of E2E to apply to those communications.
> 
> This is a consequence of how one defines the word _end_ which is the “E” in E2E/“end-to-end,” and in daily life there is a rough and fuzzy hierarchy of expectations, all of which constitute potential _ends_ :
> 
> 1. a particular device, e.g. a specific phone with a globally-unique phone number or other identifier
> 2. a particular person, who owns/possesses one or more devices
> 3. a particular company or enterprise which employs multiple people, e.g. a bank with which you deal
> 4. an outsourced agent of a company with which you deal, e.g. a call-centre which your bank uses 


This is a good primer from one of the leading privacy thinkers about what the assumptions and principles that privacy advocates are talking about.

What’s interesting here is that Alec’s view of End to End encryption is not simply that of the technical communication from device to device, but the more philosophical definition of individual to individual.

This means that there are different conversations going on at different levels, because whether or not the messages are secure between devices, or whether they are secure between individuals becomes a much more contextual question.  Indeed Alec even talks about some of the more complex definitions, such as talking to organisations, or talking to subcontractors to a call center. 


## [What Companies Can Do Now to Protect Digital Rights In A Post-Roe World | Electronic Frontier Foundation ](https://www.eff.org/deeplinks/2022/05/what-companies-can-do-now-protect-digital-rights-post-roe-world)

[https://www.eff.org/deeplinks/2022/05/what-companies-can-do-now-protect-digital-rights-post-roe-world](https://www.eff.org/deeplinks/2022/05/what-companies-can-do-now-protect-digital-rights-post-roe-world)

> 3. Check your retention policy
> 
> Do you really need to keep all of that data you’ve been collecting? Now is the time to clean up the logs. If you need them to check for abuse or for debugging, think carefully about which precise pieces of data you really need. And then delete them regularly—say, every week for the most sensitive data. IP addresses are especially risky to keep. Avoid logging them, or if you must log them for anti-abuse or statistics, do so in separate files that you can aggregate and delete frequently. Reject user-hostile measures like browser fingerprinting.
> 
> 4. Encrypt data in transit.
> 
> Seriously, encrypt data in transit. Why are you not already encrypting data in transit? Does the ISP and the entire internet need to know about the information your users are reading, the things they're buying, and the places they're going?
> 
> 5. Enable end-to-end encryption by default.
> 
> If your service includes messages, enable end-to-end encryption by default. 
> 
> 6. Don’t allow your app to become a location mine
> 
> There is an entire industry devoted to collecting and selling location data—and it’s got a well-documented history of privacy violations. Some location data brokers collect that data by getting ordinary app developers to install tracking software into their apps. Don’t do that.


I agree with a lot of these, and they should be strong behaviours from modern companies anyway.

Data is not the new oil, it's far more similar to toxic waste.  You want to collect as little of it as possible, keep it for as short as possible, and don't let anyone touch it without protection.


## [What's the deal with all those weird wrong-number texts? ](https://maxread.substack.com/p/whats-the-deal-with-all-those-weird)

[https://maxread.substack.com/p/whats-the-deal-with-all-those-weird](https://maxread.substack.com/p/whats-the-deal-with-all-those-weird)

> This is the first step in what is, at its core, an old-fashioned “romance scam,” in which the scammer exploits a lonely and/or horny person by faking a long-distance, usually romantic relationship. After the scammer has gained the trust of their victim, they convince them to transfer money, often for an investment; in some cases, the victim can be enticed into several successive transfers before they realize they’re being played.
> 
> This kind of con has proliferated over the last few years in China, where it’s called sha zhu pan, or “pig-butchering,” because the victim is strung along for weeks or months before the actual swindle, like a pig being fattened for slaughter. Originating in sophisticated online-fraud networks first developed to take advantage of Chinese offshore gamblers, the sha zhu pan scams end with targets depositing money into forex or gold trading — or, seemingly most commonly, into fake cryptocurrency platforms. (Interestingly, they’re often not “romantic” at all, and instead rely on cultivating a trusting friendship that culminates with a little bit of friendly investing advice.)
> 
> [...]
> 
> The dog-pushers
> As you can imagine from the elaborate handbooks and detailed scripts, the pig-butchering scams that emerge out of wrong-number texts aren’t the product of individual con artists or even of small informal groups. Rather, as has now been pretty extensively documented in the Asian press, they’re a key revenue stream of large hierarchical organizations — fraud businesses, basically — based in Southeast Asia. Worse, the “dog-pushers” — the lowest-level scammers who initiate conversations with victims — are often workers from around the region, tricked into indentured servitude, held captive in dormitories and offices, and beaten by the managers and bosses.
> 
> Nikkei has an excellent long article focusing on the trafficking situation in Cambodia in particular. Workers — mostly in China, but also in Malaysia, Thailand, India, and elsewhere — respond to job advertisements on Wechat or Facebook for, say, customer service; they’re smuggled into Cambodia (or elsewhere) and find themselves trapped and forced to work


Deep dive into those scams where you get a wrong message.

The level of sophistication is both high and low at the same time for these scams.  They know what they are doing, and they do it well, following a defined and well written plan.  But at the same time, they don't pick their victims effectively, instead throwing the net wide and reaching out to as many people as possible and then seeing who they catch, and working them.


## [FBI investigation determined Chinese-made Huawei equipment could disrupt US nuclear arsenal communications | Katie Bo Lillis CNN](https://www.cnn.com/2022/07/23/politics/fbi-investigation-huawei-china-defense-department-communications-nuclear/index.html)

[https://www.cnn.com/2022/07/23/politics/fbi-investigation-huawei-china-defense-department-communications-nuclear/index.html](https://www.cnn.com/2022/07/23/politics/fbi-investigation-huawei-china-defense-department-communications-nuclear/index.html)

> By the time the I-25 investigation was briefed to the White House in 2019, counterintelligence officials begin looking for other places Chinese companies might be buying land or offering to develop a piece of municipal property, like a park or an old factory, sometimes as part of a "sister city" arrangement. 
> 
> In one instance, officials shut down what they believed was a risky commercial deal near highly sensitive military testing installations in Utah sometime after the beginning of the I-25 investigation, according to one former US official. The military has a test and training range for hypersonic weapons in Utah, among other things. Sources declined to provide more details.        
> 
> Federal officials were also alarmed by what  sources described as a host of espionage and influence activities in Houston and, in 2020, shut down the Chinese  consulate there.   
>   
> 
> Bill Evanina, who until early last year ran the National Counterintelligence and Security Center, told CNN that it can sometimes be hard to differentiate between a legitimate business opportunity and espionage — in part because both might be happening at the same time.       
> 
> "What we've seen is legitimate companies that are three times removed from Beijing buy [a given] facility for obvious logical reasons, unaware of what the [Chinese] intelligence apparatus wants in that parcel [of land]," Evanina said. "What we've seen recently — it's been what's underneath the land."       
> 
> "The hard part is, that's legitimate business, and what city or town is not going to want to take that money for that land when it's just sitting there doing nothing?" he added.   


This is an interesting read, and points at a really tricky point about understanding and dealing with "espionage".

If we posit for a second that there was deliberate malicious intent here, then we'd be looking for evidence of a specific tactical change in decision making, so essentially evidence that the private company was tasked by an intelligence agency to make a decision that helped on intelligence gathering efforts.

But if what we are seeing is the ability of a state to influence strategic decision making so that it is both economically beneficial to the state, and also sets down the groundwork of capabilities that the intelligence agencies can use at a later date, then you won't find any smoking guns, any explicit tasking.  That tasking was done years or even decades ago when growth plans were drawn up and strategic decision making frameworks agreed.  That means that what look like sensible commercial decisions can have national security implications, even if everyone involved in the decision making has no idea that they are advancing a national security agenda.

That sort of thing is incredibly hard to counter, or even to prove is happening.  One can only really see it, as it was here, by taking a step back and instead of looking case by case, looking instead at the change over time.


## [Understanding the make-buy question in a growing Mars city – Casey Handmer's blog ](https://caseyhandmer.wordpress.com/2022/03/29/understanding-the-make-buy-question-in-a-growing-mars-city/)

[https://caseyhandmer.wordpress.com/2022/03/29/understanding-the-make-buy-question-in-a-growing-mars-city/](https://caseyhandmer.wordpress.com/2022/03/29/understanding-the-make-buy-question-in-a-growing-mars-city/)

> Some time ago I [**created a diagram to understand how Mars autarky**](https://caseyhandmer.wordpress.com/2020/08/23/progression-of-space-industrialization/) would progress from local manufacturing of bulk goods to more complex parts. It was not a good diagram and upon revisiting it even I found it confusing. I’m revisiting the topic here to have another go and to help future readers, including me, get quantitative on this subject.
> 
> There are three intuitions which underlie this discussion.
> 
> 1. Modern supply chains are incredibly complex, with millions of components shuttling between millions of factories without centralized control.
> 2. For the most part, we use a lot of cheap things and fewer expensive things. Since cheap things are generally easier to make (which is why they’re cheap), a Mars city relying heavily on extremely expensive interplanetary cargo importation would strongly prefer to localize production of cheap, readily available raw materials. For example, water and undifferentiated crushed rocks are absolute necessities for local production, while specialized pharmaceuticals and high performance integrated circuits will never dominate a cargo manifest ranked by weight.
> 3. The competitiveness of local manufacturing depends on several factors. Robust local demand and growing industrial sophistication tend to favor local production, while improving Starship technology, cargo carrier competition, and increased cargo volumes drive down shipping costs, favoring importation. It is difficult to say which factor will dominate when, but I think it is safe to assume that ramping up production of Starships on Earth will almost always be easier than ramping up production of advanced factories on Mars. 


There;s some really interesting thinking in here that applies not only to colonies on Mars, but in how we think about our supply chains more generally.

The cost of transport can be likened to the cost of finding a software library, constantly maintaining it, and ensuring that we get updates that don’t break our system.
If we compare that to the cost of just writing it ourselves, we can start to compare the overall transport costs against the local production costs and reason about what libraries should be built in-place, and which should be “transported in”. 


## [Every Sufficiently Advanced Configuration Language is Wrong ](https://matt-rickard.com/advanced-configuration-languages-are-wrong/)

[https://matt-rickard.com/advanced-configuration-languages-are-wrong/](https://matt-rickard.com/advanced-configuration-languages-are-wrong/)

> For basic configuration, YAML or JSON is usually good enough. It falls apart when you try to do more:
> 
> * Template it with a templating engine
> * Use esoteric language features to reuse code (anchors and aliases)
> * Patch or modify it with something like JSONPatch
> * Type-check or schema validate
> 
> These are anti-patterns and often cause more issues than they solve. So instead, we develop more advanced configuration languages that aim to solve many of the problems that we duck-tape with YAML or aren't possible to express in YAML.
> 
> [...]
> 
> The logical extreme is becoming more evident – advanced configuration in general-purpose programming languages. You can see this in the emergence of Typescript for Infrastructure-as-Code. For the most basic (and human 0x777) configuration needs, there will always be simple formats – YAML, JSON, INI, etc.).
> 
> For everything else, general-purpose languages will win out.


This is something I learned years ago writing code at the Guardian.  At the time we had a massively configurable monolithic system that was the core Content Management System, and we had settings files that allowed us to have configurable URLs, domains, timers and so on.

A bit of analysis was done and we discovered that about 95% of the settings were exactly the same in all environments, and the remaining ones were mostly consistent in being either "production" setting or "non-production" setting.

We were able to replace almost all of the configuration with hard coded values in the codebase, and in many of those production versus non-production cases, we were able to write code that did the right thing at the right place.

This massively reduced the amount of complexity needed in the configuration files.

So I agree with Matt here, don't put more complexity into your configuration files, move that complexity into the codebase itself, where it belongs and where you can code it with a real language.


## [Compound pejoratives on Reddit](http://colinmorris.github.io/blog/compound-curse-words)

[http://colinmorris.github.io/blog/compound-curse-words](http://colinmorris.github.io/blog/compound-curse-words)

> Dirty words are, let’s face it, a lot of fun. If you want to express your dislike for someone and a standard insult like “jerk” or “moron” won’t cut it, you can get creative. There are a few reliable recipes for forming derogatory noun-noun compounds in English. For example:
> 
> Start with a word for a disgusting or worthless substance
> Add a word for an agglomeration or container
> Hence, dirtwad, scumbag, [Redacted], snotwagon…
> 
> (In case it’s not yet clear, this post will contain a lot of bad words. Most are merely silly or crude, but some are more seriously offensive, including slurs.)
> 
> Alternatively, -head, -face, and -brain(s) are incredibly versatile suffixes, which can be preceded by just about any taboo word.
> 
> [...]
> 
> If only we had some concrete data on how these pieces fit together…
> 
> Introducing the Reddit compound pejorative dataset
> 
> I collected lists of around 70 prefixes and 70 suffixes (collectively, “affixes”) that can be flexibly combined to form insulting compounds, based on a scan of Wiktionary’s English derogatory terms category. The terms covered a wide range of domains, including:


What a lovely bit of data-science, and a whole new set of words that I can call people in traffic


