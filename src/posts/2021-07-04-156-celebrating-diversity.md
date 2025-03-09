---
title: "156 - Celebrating diversity"
date: 2021-07-04
description: "This week has seen my twitter feed filled with people in bikini, tank tops, naked in some cases, and showing off their bodies."
permalink: /celebrating-diversity/
---

This week has seen my twitter feed filled with people in bikini, tank tops, naked in some cases, and showing off their bodies.

The story of why this has come around is a [depressingly common story](https://www.vice.com/en/article/7kvwgb/cybersecurity-workers-flood-twitter-with-bikini-pics-to-protest-harassment), involving harassment of a woman online for daring to have a twitter account that wasn't entirely 100% about her professional life and career.

Of course, to some, this is just a storm in a teacup, this is infosec twitter in a nutshell, getting riled up by "nothing".  Some of us live wealthy privileged lives and can tweet our personal opinions, views and photos all we want.  It won't ever matter to me if I post pictures of a delicious dinner, opinions on computer games, or photos of my holiday, because as a white man, people don't or won't call me out on it.  They'll only do it to people who they think, in their head "don't belong in infosec", or whom they feel they can exert power over.

But our community is diverse and always has been.  Even going back to the historical record of the security community, [the movie Hackers](https://en.wikipedia.org/wiki/Hackers_(film)), we see the story of a crowd of misfits taking down the suit wearing, smarmy business people at their own game and winning.  Of course our misfits are good at heart, and they are persecuted, vilified and threatened by the state for being who they are.

Despite that, you wouldn't think our community was that diverse if you simply looked at who is speaking at the big infosec conferences, because there we still have strong representation of people like me, white male and steadily getting older.  But if you look at the people writing and publishing proofs-of-concept, publishing vulnerabilities and working in open source vulnerability research, you'll see that there's a strong diverse community.

Furthermore, we should recognise this as representative of our past.  When I started in the underground hacking community, nobody knew who you were because you were just a handle in an IRC channel, a handle published in Phrack magazine or the author of a particularly fun snippet uploaded to Usenet.  This allowed the community to blossom with people who did not fit the mould, and wouldn't be offered professional jobs because of the colour of their skin, the colour of their hair, or the way they chose to express themselves.

We should be celebrating, supporting and encouraging the diversity in our community, because the experiences, knowledge and breadth of skills that diverse upbringings, backgrounds and social outlooks on life brings to a team and a company is incredibly valuable.  But we should also do it because it's the right thing to do, even if it bought no value at all.


Final point, it's been pointed out to me that unless you are a long time reader, you might not have encountered my occasional coauthor before.  [Joel Samuel](https://joelgsamuel.medium.com/) occasionally contributes his thoughts to this newsletter as well, and when he does, we prefix his comments with (Joel).  I'm going to look at the formatting of the newsletter to see if there's a way I can make this clearer, as well as adjusting the code to allow for  tips, and reader comments and contributions more easily.  If you want to comment on anything, or even just send me a link, feel free to email, reply to this newsletter, or drop me a line on pretty much any social media system.

## [One way to deal with blackmail - by Natalia Antonova 🇺🇸🇺🇦 - Natalia Explains The Apocalypse](https://nataliaantonova.substack.com/p/one-way-to-deal-with-blackmail)

[https://nataliaantonova.substack.com/p/one-way-to-deal-with-blackmail](https://nataliaantonova.substack.com/p/one-way-to-deal-with-blackmail)

> My most recent geolocation challenge came with several twists. I recently published [this article in Foreign Policy](https://foreignpolicy.com/2021/01/15/russia-security-agencies-terrifying-incompetent-fsb/), and it seems to have annoyed someone. Without getting into too much detail — as I’d still like to find out the identity of the person — this someone then apparently paid someone else, someone very stupid, to rifle through my social media history and “dig up” something “damaging.” 
> 
> [...]
> 
> Before saying anything else, I will point out that I have lost work opportunities because my social media content was deemed too sexual/too feminine before. Forget allowing the world to know that I have a pair of breasts (disgusting, right?), in a truly bizarre turn of events, I was even shamed for posting pictures of my cat.


This is a great reminder of why representation matters.  An author, respected enough to contribute to Foreign Policy magazine is harassed and blackmailed with the explicit aim of asking her to get her article taken down.  That this is the way she dealt with it is absolutely marvelous and worth cheering, but the fact that she had to should be a black mark on us as an industry.


## [Kaseya supply chain attack delivers mass ransomware event to US companies | by Kevin Beaumont | Jul, 2021 | DoublePulsar](https://doublepulsar.com/kaseya-supply-chain-attack-delivers-mass-ransomware-event-to-us-companies-76e4ec6ec64b)

[https://doublepulsar.com/kaseya-supply-chain-attack-delivers-mass-ransomware-event-to-us-companies-76e4ec6ec64b](https://doublepulsar.com/kaseya-supply-chain-attack-delivers-mass-ransomware-event-to-us-companies-76e4ec6ec64b)

> Kaseya VSA is a commonly used solution by MSPs — Managed Service Providers — in the United States and United Kingdom, which helps them manage their client systems. Kaseya’s website claims they have over 40,000 customers.
> 
> Four hours ago, an apparent auto update in the product has delivered REvil ransomware.
> By design, it has administrator rights down to client systems — which means that Managed Service Providers who are infected then infect their client’s systems.
> 
> [...]
> 
> Initial entry was using a zero day vulnerability in Kaseya VSA. So even if the latest version is used, at time of attack, attackers could remotely execute commands on the VSA appliance. Technical details of how to exploit the vulnerability are not being provided until the patch is available.
> It is not a great sign that a ransomware gang has a zero day in product used widely by Managed Service Providers, and shows the continued escalation of ransomware gangs — which I’ve written about before.
> 
> Kaseya are preparing an software update to fix the vulnerability, which will be available in the coming days — until then, they advise all customers to leave their VSA switched off.
> 
> Delivery of ransomware is via an automated, fake, software update using Kaseya VSA. The attacker immediately stops administrator access to the VSA, and then adds a task called “Kaseya VSA Agent Hot-fix”. This fake update is then deployed across the estate — including on MSP client customers’ systems — as it a fake management agent update. This management agent update is actually REvil ransomware. To be clear, this means organisations that are not Kaseya’s customers were still encrypted.


This is a continuing development, as this struck late on Friday night, but one that I'm watching closely.

I think I've spoken before about the terribly named ["Operation Cloud Hopper"](https://www.pwc.co.uk/issues/cyber-security-services/insights/operation-cloud-hopper.html) back in 2016.  I've always maintained that the name was terrible because Operation Cloud Hopper had absolutely nothing to do with "the cloud".  It was about the incredible power and connectivity that Managed Service Providers have into their customer networks, and how rarely they have and support good customer separation within their environments.

Many companies use a managed service provider because they can help operate, patch and well... manage their networks.  But to do so, they need to trust that the MSP is effectively managing their systems.  That trust isn't really any different to the trust you need to have in your own internal administration team, except that if that MSP is managing 20,000 companies estates, then they're both a high value target, but they're also reaching into lots and lots of networks.  If even one of those networks gets infected, and the malware can spread back up the administration route, then it can pivot from company to company.

The knock on effects of Kaseya will really only start to be seen on Monday and Tuesday, as SME's come back to work and find they've been affected.  That's made worse by the 4th July holiday in the US delaying the ability of companies to respond here.

Secondly, we're already seeing an example of this as a supply chain attack.  [The Swedish Coop does not use Kaseya, but they do use a company called Visma EssCom](https://www.mynewsdesk.com/se/visma/pressreleases/mjukvaruleverantoeren-kesaya-utsatt-foer-en-global-cyberattack-som-paaverkar-detaljhandeln-3114593)[in Swedish] to manage their point-of-sale terminals, and Visma has been affected by the ransomware through Kaseya who presumably manage their internal systems using Kaseya.  This has resulted in 800 stores across Sweden being unable to take payment for goods.


## [NSA, Partners Release Cybersecurity Advisory on Brute Force Global Cyber Campaign > National Security Agency Central Security Service > Press Room](https://www.nsa.gov/news-features/press-room/Article/2677750/nsa-partners-release-cybersecurity-advisory-on-brute-force-global-cyber-campaign/)

[https://www.nsa.gov/news-features/press-room/Article/2677750/nsa-partners-release-cybersecurity-advisory-on-brute-force-global-cyber-campaign/](https://www.nsa.gov/news-features/press-room/Article/2677750/nsa-partners-release-cybersecurity-advisory-on-brute-force-global-cyber-campaign/)

> [“Russian GRU Conducting Global Brute Force Campaign to Compromise Enterprise and Cloud Environments”](https://media.defense.gov/2021/Jul/01/2002753896/-1/-1/1/CSA_GRU_GLOBAL_BRUTE_FORCE_CAMPAIGN_UOO158036-21.PDF) details how the Russian General Staff Main Intelligence Directorate (GRU) 85th Main Special Service Center (GTsSS) has targeted hundreds of U.S. and foreign organizations using brute force access to penetrate government and private sector victim networks. The advisory reveals the tactics, techniques, and procedures (TTPs) GTsSS actors used in their campaign to exploit targeted networks, access credentials, move laterally, and collect and exfiltrate data. It also arms system administrators with the mitigations needed to counter this threat.
> 
> Malicious cyber actors use brute force techniques to discover valid credentials often through extensive login attempts, sometimes with previously leaked usernames and passwords or by guessing with variations of the most common passwords. While the brute force technique is not new, the GTsSS uniquely leveraged software containers to easily scale its brute force attempts.
> 
> Once valid credentials were discovered, the GTsSS combined them with various publicly known vulnerabilities to gain further access into victim networks. This, along with various techniques also detailed in the advisory, allowed the actors to evade defenses and collect and exfiltrate various information in the networks, including mailboxes.


As a reminder, there are bad actors out there who brute force your passwords, look in credential dumps and try all kinds of things to get in.  [Google's research showed that even against advanced actors, even SMS based MFA](https://security.googleblog.com/2019/05/new-research-how-effective-is-basic.html) is shockingly effective, with 100% of bot based attacks (like this), 99% of bulk phishing, and 66% of pure targeted attacks.  On device prompts, TOTP and hardware MFA takes those numbers up significantly.

The number one thing you can do for your staff is turn on MFA, for everyone, for the core identity services, such as your Sing-Sign-On, ActiveDirectory and Office 365 and GSuite accounts if you have them.  

Final note, if you read the linked PDF, you'll note that Fancy Bear/Strontium/APT28 use a Kubernetes cluster to scale their password guessing attempts and their attacking infrastructure.  This should serve as a reminder that attacking teams are making good use of engineering tools and efforts from the development community, but I've yet to see a trend of defending teams having access to the same software engineering capabilities within organisations.  What could you do internally if your defending team could build and host systems on a Kubernetes cluster for scale and simplicity?


## [Inside the Market for Cookies That Lets Hackers Pretend to Be You](https://www.vice.com/en/article/n7b3jm/genesis-market-buy-cookies-slack)

[https://www.vice.com/en/article/n7b3jm/genesis-market-buy-cookies-slack](https://www.vice.com/en/article/n7b3jm/genesis-market-buy-cookies-slack)

> On Genesis, criminals don't just buy one cookie; they buy exclusive access to a "bot," a compromised computer that is part of a botnet which could contain any number of login details. But more importantly, Genesis also lets customers essentially recreate a one-to-one replica of that victim's browser, with their cookies and device fingerprints intact.
> 
> "Someone is essentially getting a perfect mask of you," Matthew Gracey-McMinn, head of threat research at cybersecurity firm Netacea which has investigated Genesis, told Motherboard. In some cases, using data bought from Genesis could let a hacker bypass two-factor authentication, because the logged in service may not prompt a user who appears legitimate for the extra code from their phone, for example. In the website's eyes, whoever is logging in is using an already known device.
> 
> This sort of data makes a hacker and the victim "pretty much indistinguishable," Gracey-McMinn added.


This is a fascinating new trend, mostly just a twist on the selling of username and password credentials.

A given cookie, especially an authentication cookie is normally signed and timestamped, so it can only be used for a short-ish period before needing to be refreshed.  The longer the timeout, the less the user gets reauthenticated, but the longer someone who steals the cookie can impersonate the user.

Stealing a cookie from the network or system is generally really hard, the easiest way to get access to these is to compromise the users computer itself.  Once you can manage the computer, you can gather the cookies and other data before it's encrypted, and there's almost nothing that users or browsers can do about that threat model.

The only good solutions here are in fact the ones that sound suspiciously like snake oil. Access brokers that validate the cookie can be used to verify whether the user's IP address has changed, whether the user has geographically improbably travelled, and can use long lived refresh tokens and very short lived access tokens to force the browser to come back to them every few minutes for revalidation.  This is an area where anomaly detection through AI and Machine learning can help, although, as always, those are redflag words in marketing for me normally.


## [China’s ‘splinternet’ will create a state-controlled alternative cyberspace | Flavia Kenyon | The Guardian](https://www.theguardian.com/global-development/2021/jun/03/chinas-splinternet-blockchain-state-control-of-cyberspace)

[https://www.theguardian.com/global-development/2021/jun/03/chinas-splinternet-blockchain-state-control-of-cyberspace](https://www.theguardian.com/global-development/2021/jun/03/chinas-splinternet-blockchain-state-control-of-cyberspace)

> Cyberspace is one huge, unregulated mess. A virtual wild west where sophisticated criminal gangs ply their trade alongside multinational companies, spy agencies, activists, celebrity influencers – and nation states. The question of who governs it is one of the biggest of our time.
> [...]
> Raab [British Foreign Secretary] said that Britain must shape cyberspace according to “our values”, while preventing China, Russia and others from “filling the multilateral vacuum”. What does he mean? It all sounds so abstract, so removed from our daily lives.
> 
> What he is referring to is the invisible battle for control of cyberspace and the ideological imperative that we, the liberal democracies, emerge triumphant, to imbue the rest of the world with “our values”.


(Joel) There is an enormous chasm between how countries like the US and UK have historically approached "the internet" compared to other countries. The US (etc) have viewed it as deregulated owner-less for the open sharing of information and ideas. Other countries view it as an open landscape for extension of national boundaries, control and influence.

Unlike territorial waters, an international agreement for 12 nautical miles does not work in cyberspace. Aggression in cyberspace has largely been left unchallenged and unchecked, until the encroachment into national territories finally seems like it is consistently going too far (for example, cyber events impacting large companies or critical national infrastructure that are attributed by intelligence/law enforcement).

The UK's modest investment and the US' obvious frustration with national cyber interruptions to me are tip of the spear of this "shaping" of cyberspace.

Given the increasing reliance on the internet to carry more and more of our lives and underlying infrastructure (Internet of Things, Smart Cities, etc) it makes send to me that governments would seek to ensure that key systems are resilient against cyber failures (malicious or otherwise) so that an individual country can maintain key namespace and IP routing in the advent of issues outside of these new national boundaries. The using of those reasonable resiliency structures to exert control, censor or breach citizen privacy is where things get... political.


## [Open source in government: creating the conditions for success — Public Digital](https://public.digital/2021/06/21/open-source-in-government-creating-the-conditions-for-success)

[https://public.digital/2021/06/21/open-source-in-government-creating-the-conditions-for-success](https://public.digital/2021/06/21/open-source-in-government-creating-the-conditions-for-success)

> Open source software can be a powerful lever for change, giving teams greater flexibility on how they solve problems and develop services based on users’ needs.
> 
> This report, and the Open Source Software Capability Model for Governments that it includes, aims to help decision makers build a common understanding of their governments capability, enabling them to invest in the conditions for success.
> 
> To ensure the report reflects the experience of those implementing open source software, we interviewed stakeholders across four continents, from government decision makers, technical experts, funders and people delivering digital services to citizens. 


This is an interesting report for technical policy makers.  It articulates the benefits of using open source, but also highlights some of the fundamental issues with Governments and open source.  It cautions teams that they won't get the full benefit unless they are able to put in place policies that encourage the adoption and use of open source, as well as establish communities, leadership and principles that ensure that the teams are seen as good members of the open source community.

One of the things I'd have liked to see was more emphasis that the open source model is even more appropriate for governments than almost anyone else.  The argument with major open source tools is that you have the ability to fix bugs yourself because you can see the source code.  The reality is that very few individuals can ever really make use of that promise, and even in most companies, you'd be hard pressed to find the skills internally.  But the size of Governments make it possible for major suppliers to provide systems made up of open source components, and for the Government to take over the maintenance of the system.  That's a huge advantage over traditional government systems where the buyer is held hostage to change control processes for years or even decades.
You can [read the full report](https://assets.public.digital/Open_Source_Report.pdf?mtime=20210621171705&focal=none)


## [The CSPO Pathology | Silicon Valley Product Group](https://svpg.com/the-cspo-pathology/)

[https://svpg.com/the-cspo-pathology/](https://svpg.com/the-cspo-pathology/)

> What’s more, the person that trained them how to be a product owner is almost never a proven strong product manager with experience from a strong product company.
> Rather, they are usually some form of an “Agile Coach” that offers various certifications in several Agile delivery processes.
> 
> These people are confusing the rituals of a delivery process, with the skills and responsibilities of a major job on a product team.
> 
> It is just as ridiculous as saying you can train some random people in Scrum, and expect they are now ready to serve as skilled software engineers.  Or expect they are now skilled product designers.
> 
> Of course, if these would-be coaches pretended that their training could prepare a designer or engineer, nobody would be fooled for a minute.  But because the product role is so poorly understood, and because a focus on process is such a tempting proxy, for many people and for many companies, they have literally come to believe that this is what product management is supposed to be.


This is a lovely pair of essays that should be read together.  This one highlights the danger and the spread of "Product Owners" who are not trained in the skills to actually do their job because of the trendiness of "Product Owner" titles in certain agile circles.  The confusion between an "onsite customer" and a "product owner" as agile has matured has resulted in some terrible implementations over the years.


## [The MBA Pathology | Silicon Valley Product Group](https://svpg.com/the-mba-pathology/)

[https://svpg.com/the-mba-pathology/](https://svpg.com/the-mba-pathology/)

> I have hired and coached many exceptionally strong people straight from top business schools, and I know many more such people.
> 
> Moreover, in my own experience, I’ve found that many of the students accepted into top MBA programs often have the right raw materials to be coached and developed into exceptionally strong product managers, and eventually very strong product and company leaders.
> 
> That said, even with the very best, there is usually some critically important “unlearning” that needs to be done.  And when that unlearning doesn’t happen, I see it leading to many of the very serious issues we see in companies today, especially those that are victims of disruption. 
> 
> And to be clear here, I’m not just talking about product managers and product leaders.
> 
> I’m also talking about VC’s and other investors, Board Members, CEO’s, CFO’s, and GM’s/business unit leaders and countless other stakeholders.  
> 
> Even when these leaders don’t have an MBA themselves, they’ve often been hired by and learned from others these same problematic behaviors.
> 
> [...]
> 
> In recent years I’ve observed that when the CSPO pathology and the MBA pathology converge in the same company, the results are especially dangerous.
> 
> In many companies, especially larger and older companies that don’t yet understand the role of technology, you often have literally hundreds of stakeholders and executives that were educated in the MBA pathology, in particular the dependence on command and control style leadership and the illusion of predictability, and they meet an eager market of Agile coaches that tell them exactly what they want to hear – they can have the top-down, command and control they love, and still check the “Agile” box (if the process has Agile in its name it must be Agile, right?) – all they need to do is adopt the right process.
> 
> Hence the perfect incubator for a disease like SAFe.
> 
> I’m not trying to rehash all the reasons this is a particularly deadly disease.  I just want to try to highlight here that this disease is enabled by these two pathologies.  


This is a blistering attack on the failures of MBA's to effectively teach their leaders in a manner befitting ["Business at the speed of thought"](https://amzn.to/3AqZodd)[Affiliate Link] as Bill Gates described it.  

Marty summarises quite nicely that it's not just the insistence on the industrial era of management, described as Command and Control, which has been changing at MBA's, but it's the driven assumption that managers are leaders, the lack of recognition of the high value individual contributors, the failure to acknowledge that knowledge is imperfect, but most of all to me, the failure to understand technology.

The assumption today still in many organisations (and Government organisations in particular) is to assume that the technology department is a cost center, that it's job is similar to the buildings, estates or HR functions.  The assumption by business leaders is that technology will do what is asked of it, at as low a price as possible, and that it is a necessary cost of doing business.

In 2020, this attitude will kill a company, because almost all companies are technology companies now and they need to embrace technologists into their business strategy setting, into their development models and to regard the technology as a critical enabler of the company.


## [(PDF) The Evolution of Management Models: A Neo-Schumpeterian Theory](https://www.researchgate.net/publication/313426246_The_Evolution_of_Management_Models_A_Neo-Schumpeterian_Theory)

[https://www.researchgate.net/publication/313426246_The_Evolution_of_Management_Models_A_Neo-Schumpeterian_Theory](https://www.researchgate.net/publication/313426246_The_Evolution_of_Management_Models_A_Neo-Schumpeterian_Theory)

> Over the last century and half, US industry has seen the emergence of several different management models, but we still understand little about the factors that drove their evolution. We propose a theory of this evolution based on three nested and interacting processes. First, we identify several successive waves of technological revolution, each of which prompted a corresponding wave of change in the dominant organizational paradigm. Second, nested within these waves, each of these organizational paradigms emerged through two successive cycles—a primary cycle which generated a new management model that obsoleted the prior organizational paradigm, and a secondary cycle which generated another model that mitigated the dysfunctions of the primary cycle's model. Third, nested within each of these cycles, we identify a problem-solving process in which the development of each model passed through four main phases during which various related management concepts competed for dominance.


This is a little dense, but I think there's a really interesting model in here.

The authors look at successive technological revolutions, waterpower and iron, steampower and railways, electric power and steel, automative and oil, and computers and telecoms.  They identify that each of these revolutions were characterized by a changing management model, from Line and staff and industrial betterment during the steam revolution (all those charming workers cottages for example), through strategy and structure and quality management from the automotive revolution and into business processes and value chain analysis in the computer revolution.

What's interesting in here is the way we can project this forward and consider the next steps in the information revolution.  The key thing that they identify is the move away from HR and quality management that typified previous physical processes and towards community and knowledge management.  

They argue that the dominant management model that forward thinking companies need to be adopting is the networked model, where you enable and support your organisation in socialising, in trading knowledge and in working out how to use it effectively.


## [Building an AWS Organization? Be sure to integrate….AWS IAM Access Analyzer – VirtualBonzo](https://virtualbonzo.com/2021/05/02/building-an-aws-organization-be-sure-to-integrate-aws-iam-access-analyzer/)

[https://virtualbonzo.com/2021/05/02/building-an-aws-organization-be-sure-to-integrate-aws-iam-access-analyzer/](https://virtualbonzo.com/2021/05/02/building-an-aws-organization-be-sure-to-integrate-aws-iam-access-analyzer/)

> If you’re building an AWS Organization, or getting ready to deploy a new organization using AWS Control Tower, be advised that there are very helpful AWS services that can be integrated into your organization. In this “Be sure to integrate…” series, we’ll look at 3 baseline services that should be enabled and integrated into your AWS Organization….AWS Security Hub, AWS GuardDuty, and AWS IAM Access Analyzer.


I be you aren't using AWS's IAM Access Analyzer, and you should be.  This is a helpful walkthrough of how it works and how to use it well.  

I suspect most of you are using AWS Security Hub and AWS GuardDuty already, but if not, there are guides on setting those up well as well.


