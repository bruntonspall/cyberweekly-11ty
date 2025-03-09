---
title: "238 - Living in the future is both bright and scary"
date: 2024-02-04
description: "We live in the future and we're going to have to accept it."
permalink: /living-in-the-future-is-both-bright-and-scary/
---

We live in the future and we're going to have to accept it.

There's huge advantages to living in the future.  We have been living through a social and cultural revolution with the advent and growth of the global internet in a way that hasn't happened for over 200 years, and if it seems fast to you, remember that the industrial revolution took around 100 years to totally transform Britain from it's pre-industrial roots into a global industrial leader.  That 3 generations of living was living through a huge population growth, mass migration of people into the cities, and a [Gin craze](https://en.wikipedia.org/wiki/Gin_Craze) that resulted in 5 acts of parliament.  It's been suggested that much of this was because of the political and social upheaval that resulted from so many people moving from villages and towns into cities, where there was plentiful light, entertainment and ready access to alcohol.

The internet revolution has really only been going for one generation so far, and we've seen computers change from building sized mechanical monstrosities to devices in your hand more powerful than the computers that flew astronauts to the moon.  The movement of information from being distributed but unanalysable into vast central datastores into being compressed into large language models that can understand, analyze and connect the dots faster than anyone thought possible.

I don't think we're done yet with the changes, and while I'm mostly an AI pessimist compared to some of the ridiculous statements you hear coming out from some of our technology leaders, I think the power that AI will have in harnessing and exploiting the datasets that we've spent the last 40 years centralising is going to create fundamental shifts in how we think about, manage and live our life.  

The bad side of this however is that we are increasingly interlinked in complex webs of suppliers and connections which are hard to understand, difficult to manage and increasingly creating a security concern when something goes wrong.

How many credentials, tokens and passwords do we need in a modern world?  Individually, my password manager seems to suggest that I've got hundreds of passwords stored for example.  But that's not the end of it, because I've got about 5 or 6 trello accounts, often individually created through an OpenID Single Sign On session, and there are hundreds of further applications and systems for which I can access through the various computers I can access.

If my identity was breached, how likely would it be that I could manage the extent of that breach, and work out just what had been exposed?

As we move into the future, we will need to develop social, cultural, legal and technical models to enable people to think about this data sprawl and start to determine whether or not we care about doing something about it.  It might be that like the pollution and social change of the industrial revolution, we consider this data pollution to just be the cost of progress, and that people adapt their lives to just get on with it, or we might see increasing amounts of data legislation that should give individuals more control over their data and who uses it.

But as we see these AI companies start to gather and exploit this data, we're going to see huge social and personal benefits unlocked, as well as some pretty nasty and probably unintended breaches that expose far more than anyone thought

## [One Supply Chain Attack to Rule Them All – Poisoning GitHub’s Runner Images – Adnan Khan's Blog ](https://adnanthekhan.com/2023/12/20/one-supply-chain-attack-to-rule-them-all/)

[https://adnanthekhan.com/2023/12/20/one-supply-chain-attack-to-rule-them-all/](https://adnanthekhan.com/2023/12/20/one-supply-chain-attack-to-rule-them-all/)

> In order to understand this attack, we need to understand self-hosted runners and why they are such a risk on public repositories if not configured properly. There are also many risks of self-hosted runners on private repositories, which my colleagues and I at Praetorian dove into with https://www.praetorian.com/blog/self-hosted-github-runners-are-backdoors/ and our subsequent ShmooCon 2023 talk “Phanton of the Pipeline,” but we will focus on public repositories.
> 
> By default, when a self-hosted runner is attached to a repository, or a default organization runner group that a public repository has access to, then any workflow running in that repository’s context can use that runner. As long as the runs-on field is set to self-hosted (or one of the labels associated with the runner), the runner will pick up the workflow and start processing it. There are ways to restrict this to specific workflows and triggering actors using runner group restrictions and pre-run hooks – but that is a topic for another post.
> 
> For workflows on default and feature branches, this isn’t an issue. Users must have write access to update branches within repositories. The problem is that this also applies to workflows from fork pull requests. GitHub’s documentation is fairly clear on this matter, and has been so since self-hosted runners were first introduced.
> 
> [...]
> 
> Time and time again we in the information security world have seen that if a service has a default configuration, then a large number of users will not change that default setting. This is especially true when there isn’t a big warning prompt informing users about this when adding a runner to a public repository. You have to dig into documentation, and if you can easily get it working without reading the docs, then why bother reading the docs?


This is a good reminder of the complexity of mixing public and private infrastructure.  Your private runners, running on your internal infrastructure have access to lots of internal systems, information and data that something public wouldn't.  If you point them at a public datasource, especially one that a remote third party user can carry out actions on, then you are in essence giving the remote party executable privileges on your infrastructure.  This blogpost and excellent bit of research shows just why that is a bad idea.

But more critically here, this is well documented to be a bad idea, but it's not entirely obvious and as they point out, many users will just do the default.  It might feel like they're even making a secure decision here, don't like Github doing the actions to build our software, lets run that bit on our infrastructure because it's more secure.

Default configurations should be secure, and it should ideally be impossible to setup a local runner that executes against a public repo without specifically configuring it and indicating that you understand the risks.


## [Thanksgiving 2023 security incident ](https://blog.cloudflare.com/thanksgiving-2023-security-incident)

[https://blog.cloudflare.com/thanksgiving-2023-security-incident](https://blog.cloudflare.com/thanksgiving-2023-security-incident)

> From November 14 to 17, a threat actor did reconnaissance and then accessed our internal wiki (which uses Atlassian Confluence) and our bug database (Atlassian Jira). On November 20 and 21, we saw additional access indicating they may have come back to test access to ensure they had connectivity.
> 
> They then returned on November 22 and established persistent access to our Atlassian server using ScriptRunner for Jira, gained access to our source code management system (which uses Atlassian Bitbucket), and tried, unsuccessfully, to access a console server that had access to the data center that Cloudflare had not yet put into production in São Paulo, Brazil.
> 
> They did this by using one access token and three service account credentials that had been taken, and that we failed to rotate, after the [Okta compromise of October 2023](http://blog.cloudflare.com/how-cloudflare-mitigated-yet-another-okta-compromise) . All threat actor access and connections were terminated on November 24 and CrowdStrike has confirmed that the last evidence of threat activity was on November 24 at 10:44.
> 
> […]
> 
> The only production systems the threat actor could access using the stolen credentials was our Atlassian environment. Analyzing the wiki pages they accessed, bug database issues, and source code repositories, it appears they were looking for information about the architecture, security, and management of our global network; no doubt with an eye on gaining a deeper foothold. Because of that, we decided a huge effort was needed to further harden our security protocols to prevent the threat actor from being able to get that foothold had we overlooked something from our log files.
> 
> Our aim was to prevent the attacker from using the technical information about the operations of our network as a way to get back in. Even though we believed, and later confirmed, the attacker had limited access, we undertook a comprehensive effort to rotate every production credential (more than 5,000 individual credentials), physically segment test and staging systems, performed forensic triages on 4,893 systems, reimaged and rebooted every machine in our global network including all the systems the threat actor accessed and all Atlassian products (Jira, Confluence, and Bitbucket). 


This is a really impressive writeup of an initial compromise.  Cloudflare missed just a couple of tokens out of thousands of their credentials, but those tokens enabled the threat actor to pivot through their infrastructure and into the wider system.

I note that the first thing the actor did was attempt to get more information about the wider architecture of the system, looking in developer facing tools like wiki’s, bug reports and so on.

There’s a few questions that can be raised from this, but broadly speaking this is a great example of how to deal with a breach.  Take a look at the timelines, the actor behaviour and ask your defense teams if they would notice and respond to this situation.  It’ll make a great tabletop exercise at the very least. 


## [Thesis on value accumulation in AI. | Irrational Exuberance ](https://lethain.com/value-accumulation-in-ai/)

[https://lethain.com/value-accumulation-in-ai/](https://lethain.com/value-accumulation-in-ai/)

> Where I see things moving over the next several years (and generally I think the transition here will be faster than slower):
> 
> 1. I believe _Infrastructure_ will eat an increasingly large amount of the _Modeling & Core_ tier. Even today, the cloud providers of the _Infrastructure_ have significant ownership and control in the leading _Modeling & Core_ tier. This will make it harder to perceive the shift, but I think it’s already happening and will accelerate
> 2. Because I believe _AI-enhanced product_ will successfully capture value thoughtfully using AI, the interesting question is what sorts of products will capture the majority. Ultimately I think the question is whether it’s harder to get the necessary data to power AI (fast-moving incumbents capture majority of value) or whether learning to integrate and integrating products with genuinely useful AI-capabilities is harder (new challengers capture majority of value)
> 
> […] the interesting place to angel invest in 2024 is, in my opinion, in products that are well-suited to adopt AI-capabilities. That’s a broad category–we’re still learning where these techniques are powerful–but I think it’s particularly any company that works heavily with documents, and any company where it’s product is capable of keeping a human in the loop (e.g. LLMs are cheap, fast and imperfectly accurate, but in a system where someone uses it to draft replies and review them by a human, you’d be fine).
> 
> Not angel-investing, but if you wanted to make a career bet, I think the interesting career bet is finding an established company with significant existing data and product workflows that could be enhanced by recent AI advances. 


I don’t normally do predictions, but this one is I think bang on the money.  AI is going to create a squeezed middle, along with a vaporous top.

Companies who currently claim to provide AI core systems, those big models, data processes and so on are going to either have their lunch eaten by the really big infrastructure behemoths, or their model is going to prove to not be able to grow sufficiently [1].

Secondly, companies who offer services on top of AI, that analyse your inbox, your calendar, your web browsing, whatever it is, will have a huge failure rate, but some stars will eventually come out of it.  But companies that have an existing data investment and can suitably exploit it, will have a head start on companies that rely on convincing users to hand over their data.

[1] I say growth here, because some of those companies will find a niche, will execute well, and will never get the year on year 10x revenue growth that VC’s are after, but that doesn’t mean they’re not going to be successful in their own way. 


## [Questionable Advice: “My boss says we don’t need any engineering managers. Is he right?” ](https://charity.wtf/2024/01/05/questionable-advice-my-boss-says-we-dont-need-any-engineering-managers-is-he-right/)

[https://charity.wtf/2024/01/05/questionable-advice-my-boss-says-we-dont-need-any-engineering-managers-is-he-right/](https://charity.wtf/2024/01/05/questionable-advice-my-boss-says-we-dont-need-any-engineering-managers-is-he-right/)

> But hierarchy is not intrinsically authoritarian. Hierarchy did not originate as a political structure that humans invented for controlling and dominating one another, it is in fact a property of self-organizing systems, and it emerges for the benefit of the subsystems. In fact, hierarchy is absolutely critical to the adaptability, resiliency, and scalability of complex systems.
> 
> [...]
> 
> A system is self-organizing if it has the ability to make itself more complex, by diversifying, adapting, and improving itself. As systems self-organize and their complexity increases, they tend to generate hierarchy — an arrangement of systems and subsystems. In a stable, resilient and efficient system, subsystems can largely take care of themselves, regulate themselves, and serve the needs of the larger system, while the larger system coordinates between subsystems and helps them perform better.
> 
> Hierarchy minimizes the costs of coordination and reduces the amount of information that any given part of the system has to keep track of, preventing information overload. Information transfer and relationships within a subsystem are much more dense and have fewer delays than information transfer or relationships between subsystems.
> 
> Applying this definition, we can say that a manager’s job is to coordinate between teams and help their team perform better.
> 
> [...]
> 
> In natural hierarchies, we look up for purpose and down for function. That, in a nutshell, is the more complicated argument for why we need engineering managers.
> 
> CHOOSE BORING ~~TECHNOLOGY~~ CULTURE
> 
> The simpler argument is this: most engineering orgs have engineering managers. That’s the default. Lots of people much smarter than you or me have spent lots of time thinking and tinkering with org structures over the years, and this is what we’ve got.
> 
> As Dan McKinley famously said, we should “choose boring technology“. Boring doesn’t mean bad, it means the capabilities and failure conditions are well understood. You only ever get a few innovation tokens, so you should spend those wisely on core differentiators that could make or break your business. The same goes for culture. Do you really want to spend one of your tokens on org structure? Why??
> 
> For better or for worse, the hierarchical org structure is well understood. There are plenty of people on the job market who are proficient at managing or working with managers, and you can hire them.


I thought this was an excellent broken down two part argument for why engineering management needs to exist and how it can help.

My least favourite phrase in the world is the idea that the manager is the "shit-umbrella", the person who protects the engineers from all of the management stuff happening out there.  That articulation both infantalises the engineer, and implies that the engineer would be better if the rest of the organisation didn't exist.  In reality a good manager is the holder of context.  They stay on top of all of the currents going around, which is a full time job, they understand, process and contextualise and present the right information to their team to enable them to work effectively while feeling part of the wider mission and vision of the organisation.

But I'm also sold on Charity's second argument here.  Lots of people have done this thinking and there are structures, people with skills and entire conferences on how to operate this way and do it well.  Unless you think there's a true company advantage in setting up your own unique microculture, then you may as well invest your organisations effort elsewhere


## [Agencies using vulnerable Ivanti products have until Saturday to disconnect them | Ars Technica ](https://arstechnica.com/security/2024/02/agencies-using-vulnerable-ivanti-products-have-until-saturday-to-disconnect-them/)

[https://arstechnica.com/security/2024/02/agencies-using-vulnerable-ivanti-products-have-until-saturday-to-disconnect-them/](https://arstechnica.com/security/2024/02/agencies-using-vulnerable-ivanti-products-have-until-saturday-to-disconnect-them/)

> Federal civilian agencies have until midnight Saturday morning to sever all network connections to Ivanti VPN software, which is currently under mass exploitation by multiple threat groups. The US Cybersecurity and Infrastructure Security Agency mandated the move on Wednesday after disclosing three critical vulnerabilities in recent weeks.
> 
> Three weeks ago, Ivanti [disclosed](https://arstechnica.com/security/2024/01/actively-exploited-0-days-in-ivanti-vpn-are-letting-hackers-backdoor-networks/) two critical vulnerabilities that it said threat actors were already actively exploiting. The attacks, the company said, targeted “a limited number of customers” using the company’s Connect Secure and Policy Secure VPN products. Security firm Volexity said on the same day that the vulnerabilities had been under exploitation since early December. Ivanti didn’t have a patch available and instead advised customers to follow several steps to protect themselves against attacks. Among the steps was running an integrity checker the company released to detect any compromises.
> 
> Almost two weeks later, researchers said the zero-days were [under mass exploitation](https://arstechnica.com/security/2024/01/mass-exploitation-of-ivanti-vpns-is-infecting-networks-around-the-globe/) in attacks that were backdooring customer networks around the globe. A day later, Ivanti failed to make good on an earlier pledge to begin rolling out a proper patch by January 24. The company didn’t start the process until Wednesday, two weeks after the deadline it set for itself. 


This is something new in the enterprise product world.  CISA is really starting to flex it’s muscles with some of this stuff.  If your security response capability isn’t good enough, they’ll start telling departments to disconnect your products.

When you disconnect the corporate VPN, you had better have a plan to replace it, and chances are you are replacing it with something from another company, and you can bet that they’re not swapping back anytime soon.

It’ll be interesting to watch over the coming months and years whether this has an impact on the market itself. 


## [🔮 AI Cloud Capture; Drone warfare; 34 authors; Code quality; Big PDF’s ++ #459 ](https://www.exponentialview.co/p/ev-459?utm_source=substack&utm_medium=email&utm_content=share)

[https://www.exponentialview.co/p/ev-459?utm_source=substack&utm_medium=email&utm_content=share](https://www.exponentialview.co/p/ev-459?utm_source=substack&utm_medium=email&utm_content=share)

> AWS is now at a $100bn run rate. It is also highly profitable, [contributing 76% of all Amazon’s operating profits over the past decade](https://twitter.com/nsrnicek/status/1753375537446216023/photo/1) . Azure became Microsoft’s largest product line in terms [of revenue in 2019](https://www.geekwire.com/2024/microsoft-azure-revenue-up-30-with-help-from-ai-as-tech-giant-beats-overall-expectations/) , and that business still grew 30% year-on-year. Google, the smallest of the big cloud providers, [clocked up a 25% annualised growth in the fourth quarter](https://www.datacenterdynamics.com/en/news/google-cloud-posts-92bn-in-revenue-for-q4-2023-microsoft-cloud-revenue-up-24-yoy/) . Overall these three hyperscalers added $15bn in new annual recurring revenue in the fourth quarter of last year.
> 
> Every time a company announces its intention to invest in AI (whether generative or some other flavour), these workloads must run somewhere. For mainstream businesses, that somewhere will often be the cloud; [despite rising costs](https://techbeacon.com/enterprise-it/why-are-companies-still-struggling-cloud-costs) , only the bravest or most capable can take their infrastructure back in-house.
> 
> There is a long-term secular trend for companies to do more _in silico._ Today, we might think of AI workloads as being about cost optimisations and efficiencies. But increasingly, the real value-added work of a company (whether it is route planning, pricing analytics, research and development) will run on demanding ML models. The clouds will continue to rise. 


The numbers associated with cloud computing really are just astounding when you step back and look at them.  The amount of reinvestment potential that is in those systems mean that the companies have engineering, operations and security budgets that dwarf most organisations by orders of magnitude.

But that’s not to say that you’ll be the recipient of that entire budget.  Microsoft has been running as a company since about the time I was born, and that means that there is over 40 years of technical debt in there sometime.  Each of those organisations can turn it’s attention to securing it’s core infrastructure at levels that are unthinkable to most of us, but it also has to spread it’s attention across millions of customers and what they need.

Unless you have a tight and close focus on a specific thing that you need, chances are that the big hyperscalers will do it bigger and better than you will.  So where are you going to put your focus, your budget and your energy?  Don’t compete with these giant beasts, but learn to complement their scale with your focus 


## [Scanning Git for Secrets: The 2024 Comprehensive Guide - Truffle Security ](https://trufflesecurity.com/blog/scanning-git-for-secrets-the-2024-comprehensive-guide/)

[https://trufflesecurity.com/blog/scanning-git-for-secrets-the-2024-comprehensive-guide/](https://trufflesecurity.com/blog/scanning-git-for-secrets-the-2024-comprehensive-guide/)

> TruffleHog is an open source secrets scanning tool that detects over 800 different types of secrets in a variety of sources, such as git repositories, local files, AWS S3, Docker images and more. It utilizes detector modules built for a large range of secret formats, and extracts matching data from plaintext files as well as rich text documents like PDFs. Then, it verifies the secret by checking the credential against the actual SaaS provider’s APIs, if available. 
> 
> TruffleHog installation instructions can be found [**here**](https://github.com/trufflesecurity/trufflehog#floppy_disk-installation) . And [**here’s a link**](https://github.com/dustin-decker/secretsandstuff) to a git repository containing purposefully leaked keys, so you can test TruffleHog out. Now, let’s step through how to scan git for secrets. 


This is a nice up to date guide on how to integrate TruffleHog into your development process, and you really should do so.

There are other secret hunting tools, but as has been seen recently, an exposed secret can be one of the most damaging breaches you can experience.  Tools like this will make it far less likely such a breach will occur 


## [Who said what: using machine learning to correctly attribute quotes | | The Guardian ](https://www.theguardian.com/info/2023/nov/21/who-said-what-using-machine-learning-to-correctly-attribute-quotes)

[https://www.theguardian.com/info/2023/nov/21/who-said-what-using-machine-learning-to-correctly-attribute-quotes](https://www.theguardian.com/info/2023/nov/21/who-said-what-using-machine-learning-to-correctly-attribute-quotes)

> Quotes enable direct transmission of information from a source, capturing precisely the intended sentiment and meaning. They are not only a vital piece of accurate reporting but can also bring a story to life. The information extracted from them can be used for fact checking and allow us to gain insights into public views. For instance, accurately attributed quotes can be used for tracking shifting opinions on the same subject over time, or to explore those opinions as a function of identity, e.g. gender or race. Having a comprehensive set of quotes and their sources is thus a rich data asset that can be used to explore demographic and socioeconomic trends and shifts.
> 
> We had already used AI to help with accurate quote extraction from the Guardian’s extensive archive, and thought it could help us again for the next step of accurate quote attribution.
> 
> [...]
> 
> An AI model can be taught by presenting it with numerous labelled examples illustrating the task we would like it to complete. In our case, this involved first manually labelling over a hundred Guardian articles, drawing links between ambiguous mentions/anaphora and their antecedent.
> 
> Though this may not seem the most glamorous task, the performance of any model is bottlenecked by the quality of the data it is given, and hence the data-labelling stage is crucial to the value of the final product. Due to the complex nature of language and the resulting subjectivity of the labelling, there were many intricacies to this task which required a rule set to be devised to standardise the data across human annotators. So, a lot of time was spent with Anna, Michel and Alice on this stage of the project; and we were all thankful when it was complete!


Lovely bit of work, turning AI capabilities into something useful for the organisation, and making use of their existing archive.


## [Dependency Confusions in Docker and remote pwning of your infra ](https://www.errno.fr/DockerDependencyConfusion.html)

[https://www.errno.fr/DockerDependencyConfusion.html](https://www.errno.fr/DockerDependencyConfusion.html)

> Docker will look for the base image on docker hub `remote-docker-hub` first, then will fallback to the private registry `local-docker-project` . This is only exploitable if the project uses internal namespaces because as previously mentioned, failing to provide a namespace would implicitly default to the `library` namespace, where only official images are uploaded.
> 
> The exploitation is simple enough: create an account on Docker Hub, register the namespace (for instance `gquere` ) and upload the malicious image (for instance `hello-world` ). Then wait until the image is ran and congrats, you’ve gained a foothold in your target’s internal network!
> 
> To sum up, if the following conditions are met then the project is vulnerable:
> 
> * two or more mirrors are configured and Docker Hub is declared first
> * the project uses one or more namespaces in their internal registry
> * this namespace is not registered on Docker Hub 


Dependency confusion is becoming increasingly common because for the last twenty years we’ve increasingly modelled our internal dependency systems on a semming private version of the internet on the assumption that the system will never actually resolve the given thing on the internet.

Be explicit about your internal dependencies, and ensure that if there is a misconfiguration, there is an error rather than resolving untrusted third party code or services 


## [Cloud engineer gets 2 years for wiping ex-employer’s code repos ](https://www.bleepingcomputer.com/news/security/cloud-engineer-gets-2-years-for-wiping-ex-employers-code-repos/)

[https://www.bleepingcomputer.com/news/security/cloud-engineer-gets-2-years-for-wiping-ex-employers-code-repos/](https://www.bleepingcomputer.com/news/security/cloud-engineer-gets-2-years-for-wiping-ex-employers-code-repos/)

> According to the U.S. Department of Justice (DoJ) announcement, Brody was fired on March 11, 2020, from First Republic Bank (FRB) in San Francisco, where he worked as a cloud engineer.
> 
> The court documents state that Brody's employment was terminated after he violated company policies by connecting a USB drive containing pornography to company computers.
> 
> Following his dismissal, Brody allegedly refused to return his work laptop and instead used his still-valid account to access the bank's computer network and cause damages estimated to be above $220,000
> 
> "Among other things, Brody deleted the bank's code repositories, ran a malicious script to delete logs, left taunts within the bank's code for former colleagues, and impersonated other bank employees by opening sessions in their names," describes the U.S. DOJ announcement.
> 
> "He also emailed himself proprietary bank code that he had worked on as an employee, which was valued at over $5,000."
> 
> [...]
> 
> In addition to the two-year prison term and the payment of the restitution, Brody will serve three years of supervised release.


Malicious insiders are often motivated by ego or a sense of entitlement.  If you need to terminate someone, especially someone with privileged access, you need to be sure that they no longer have access to your critical systems.


