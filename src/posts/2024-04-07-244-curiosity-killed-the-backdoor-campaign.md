---
title: "244 - Curiosity killed the (backdoor) campaign"
date: 2024-04-07
description: "Jeff Moss spoke at Blackhat a few years back about [\"superempowered individuals\"](https://www.theregister.com/2022/05/12/jeff_moss_ukraine_cyber_governance/) - people who have more individual power than some nation states due to their combination of skills, placement and curiousity."
permalink: /curiosity-killed-the-backdoor-campaign/
---

Jeff Moss spoke at Blackhat a few years back about ["superempowered individuals"](https://www.theregister.com/2022/05/12/jeff_moss_ukraine_cyber_governance/) - people who have more individual power than some nation states due to their combination of skills, placement and curiousity.

For many of these individuals, they didn't set out to achieve this, they just excelled in their field and ended up in positions where with the stroke of a keyboard they could achieve vast things.

There are also superempowered individuals toiling away in open source, where projects they look after sit in the dependency chain of huge amounts of the worlds technology.  To draw this out there is of course a [relevant XKCD: Dependency](https://xkcd.com/2347/).

In the last few weeks, we came awfully close to another log4j style "cyberapocolypse", or at least a lot of late nights for grumpy technical folk.  The potential to backdoor SSH, the core library for administering the vast majority of the worlds internet is absoutely huge.

And it was defeated by soemone who was simply curious about why his internal system was suddenly running half a second slower.

Curiousity is the magical superpower of skilled developers.  It's the endless, sometimes irritating, quest to ask "But why do we do it that way?" or "What is the point of this work".  When I used to interview for developers, we used to say that attitude was intrinsic, but skill could be taught.  That's not actually true, and building a good culture in your development team that encourages exploration is a great way to building a positive attitude in your staff, but when interviewing, given two roughly equal candidates, one who was keen and curious but less technically skilled, and a more technically skilled but less curious developer, I would lean towards the former over the latter.

Our curiosity about the world, about how geopolitics affects software development, and just why this code behaves the way it does is what enables the open source movement, and the huge benefits we've gained from it over the years.

Of course, it's not just software development that benefits from a natural optimism and curiosity.  Good executives want to know why their strategies work, and what drives their customers, and great security folk are often asking the question "Why", such as "Why did that alert go ping?".

Be curious and keep digging

## [oss-security - backdoor in upstream xz/liblzma leading to ssh server compromise ](https://www.openwall.com/lists/oss-security/2024/03/29/4)

[https://www.openwall.com/lists/oss-security/2024/03/29/4](https://www.openwall.com/lists/oss-security/2024/03/29/4)

> After observing a few odd symptoms around liblzma (part of the xz package) on
> Debian sid installations over the last weeks (logins with ssh taking a lot of
> CPU, valgrind errors) I figured out the answer:
> 
> The upstream xz repository and the xz tarballs have been backdoored.
> 
> At first I thought this was a compromise of debian's package, but it turns out
> to be upstream.
> 
> [...]
> 
> With the backdoored liblzma installed, logins via ssh become a lot slower.
> 
> ```
> time ssh nonexistant@...alhost
> 
> before:
> nonexistant@...alhost: Permission denied (publickey).
> 
> before:
> real	0m0.299s
> user	0m0.202s
> sys	0m0.006s
> 
> after:
> nonexistant@...alhost: Permission denied (publickey).
> 
> real	0m0.807s
> user	0m0.202s
> sys	0m0.006s
> ```
> 
> openssh does not directly use liblzma. However debian and several other
> distributions patch openssh to support systemd notification, and libsystemd
> does depend on lzma.


By "a lot slower"Andres meant that he had observed about a half a second delay when logging into his test servers.  Noticed, and debugged it and then called an alarm that probably saved huge amounts of pain in the future for many of us.

The biggest takeaway here is how close a "near miss" this was.  The affected versions of SSH had not made it into mainstream distributions, but if they had, this would have been an absolutely killer backdoor for someone to have access to


## [Portscanning the fleet and trying to put out fires ](http://rachelbythebay.com/w/2024/03/21/scan/)

[http://rachelbythebay.com/w/2024/03/21/scan/](http://rachelbythebay.com/w/2024/03/21/scan/)

> There was this team which was running a pretty complicated data storage, leader election and "discovery" service. They had something like 3200 machines and had something like 300 different clusters/cells/ensembles/...(*) running across them. This service ran something kind of like etcd, only not that.
> 
> [...]
> 
> This group of clusters had started out relatively simple but had grown into a monster over the years. Nobody probably expected them to have hundreds of clusters and thousands of machines, but they now did, and they were having trouble keeping track of everything. There were constant outages, and since they were so low in the stack, when they broke, lots of other stuff broke.
> 
> I wanted to know just what the ground truth looked like and so started something really stupid from my development machine. It would take a list of their servers and would crawl them, interrogating the TCP ports on which the service ran.
> 
> [...]
> 
> Early results from this terrible manual scrapes started showing promise. Misconfigurations were showing up all over the place - clusters that are supposed to have 5 hosts but only have 3 in practice with the other two missing in action somewhere, clusters with non-standard host counts, clusters in the wrong spots, and so on.
> 
> To get away from the "printf | nc the world in cron" thing, we wound up writing this dumb little agent thing that would run on all of the ~3200 hosts. It would do the same crawling, but it would happen over loopback so it was a good bit faster by removing long hauls over the production network from the equation. It also took the load of polling ~32000 ports off my singular machine, and was inherently parallel.
> 
> It was now possible to just query an agent and get a list of everything running on that box. It would refresh things every minute, so it was far more current than my terrible script which might run every couple of hours (since it was so slow). This made things even better, and so we needed an aggregator.


This is a great example of start simple, build and iterate, and keep building until you understand the problem.  At any point here Rachel could have stopped and said "job done", but she wanted to find out more, and fix more things.


## [How I forked SteamOS for my living room PC — iliana.fyi ](https://iliana.fyi/blog/build-your-own-steamos-updates/)

[https://iliana.fyi/blog/build-your-own-steamos-updates/](https://iliana.fyi/blog/build-your-own-steamos-updates/)

> I don’t own a Steam Deck. A bunch of my friends do, but they know better than to let me have root access on a device they actually like using. What I do have is a recently-built living room PC that I wanted to play games on… and SteamOS seemed like a reasonable choice. It almost even worked perfectly out of the box, although I think that is primarily because I built a computer that looks vaguely similar to a really heavy, battery-less Steam Deck1.
> 
> The one thing that didn’t work was resume from suspend. Other distributions running on my computer using mainline or stable kernels did. Eventually, I found the sources for Valve’s kernel (it’s weird, I’ll explain when we get there) and started a git bisect, leading me to a commit that seems to fix resume from suspend on Steam Deck hardware, but ultimately breaks it on mine. Needing to revert this commit and do my own build is the ultimate reason I headed down this path.
> 
> At several points in this process my partner asked if this made more sense than just using Arch or something else directly. I still don’t know the answer, although I think I still prefer relying on a Valve-tested set of packages than whatever’s current in the Arch repos. If I’m going to have to tinker with a Linux distro for running games, it may as well be one that people actually test their games on.
> 
> I apparently have a tendency to make poor choices like this, because you are reading the second post in what has become a series on installing Linux distros onto systems they’re not ready for yet.


One of the things that seems to define great developers is endless curiousity.  Doing something not because it's practical, but because it's an interesting exercise that scratches that itch is a powerful motivator


## [Things Programmers Can Do in One Week | Blog | build-your-own.org ](https://build-your-own.org/blog/20231108_1week/)

[https://build-your-own.org/blog/20231108_1week/](https://build-your-own.org/blog/20231108_1week/)

> This is a list of coding challenges that can be accomplished without too much effort after you have deeply learned how things work. It can be used to verify your learning.
> 
> Many seemingly complex topics have simple principles behind them, such as compilers, regular expressions. That’s why I used the “create it in 1 week” as a way to test my knowledge. If I still see a topic as complicated, I probably missed something and need to learn more.
> 
> Some developers will see part of the list as magic or very complex things. But they are still learnable things, and the more you learn the easier they get. Why not pick a topic and learn something new?
> 
> Big projects are broken down into smaller topics to give you ideas of where to start. The list does not include topics that are inherently complex.


This was interesting to me as a form of Koan, a kind of programming exercise you can try to repeat over and over to get yourself better at programming and to explore what feels right, what things you've not tried, and how to solve interesting problems.

Of course the problem as a software developer is knowing what to do to practice, but that's why a list like this is fun, because you can take a run at some of these knowing that it's purely for fun and professional development


## [1BRC merykitty’s Magic SWAR: 8 Lines of Code Explained in 3,000 Words ](https://questdb.io/blog/1brc-merykittys-magic-swar/)

[https://questdb.io/blog/1brc-merykittys-magic-swar/](https://questdb.io/blog/1brc-merykittys-magic-swar/)

> Then, out of the blue, a solution appeared that set the Twitter #1BRC hashtag on fire. No if statements, and just a single read from the file! It was a part of the solution contributed by Quân Anh Mai (GitHub handle @merykitty). The code looked like nothing less than magic incantations, and even the top experts nodded in disbelief.
> 
> [...]
> 
> Merykitty's code consists of nothing but a fixed sequence of 18 ALU operations: bitwise shift, AND, NOT and XOR; arithmetic add, subtract, and multiply; and a single low-level function call numberOfTrailingZeros(), for which the JDK has a compiler intrinsic using specialized CPU instructions.
> 
> In goes a long number filled with 8 bytes from the CSV (in little-endian order), and out comes the temperature as an integer (10x the actual temperature).


I love this kind of magic.  This is what people think programmers do all day, when in reality 99% of the job is wrestling with trying to work out what the users actually want or need, or how to deal with an unclear and inconsistent world.  But occasionally you get a bit of pure programming magic that just astounds everyone who looks at it.

If you are a developer, I suggest you try to read the snippet and the problem statement and see how much of it you can understand without the writeup.   I managed very little of it, but the writeup goes a long way to explaining it all


## [Why Does 'is-number' Package Have 59M Weekly Downloads? | Shubham Jain ](https://shubhamjain.co/2024/02/29/why-is-number-package-have-59m-downloads/?ck_subscriber_id=2406559830)

[https://shubhamjain.co/2024/02/29/why-is-number-package-have-59m-downloads/?ck_subscriber_id=2406559830](https://shubhamjain.co/2024/02/29/why-is-number-package-have-59m-downloads/?ck_subscriber_id=2406559830)

> I don’t believe many programmers are using `is-number` knowingly. It just gets included when you use a popular package. In fact, it’s there even in my `node_modules` folder. I figured out the chain that led to its inclusion:tailwindcss -> chokidar -> braces -> fill-range -> to-regex-range -> is-number
> 
> The last four packages in the chain have been written by the same author.
> 
> Nonetheless, this kind of dependency hell is ridiculous and something should be done about it. Too many packages are getting downloaded, consuming disk space and download time, that should ideally only be a single function or a part of a bigger lodash-like package. There are thirty-seven “is-*” packages in my node_modules folder. That’s just bonkers! 


I note that the author is missing one of the approaches that Python and Ruby started with, where there is still a large number of dependencies, but nothing like the NPM sort of problems. 

Ensuring that you have a comprehensive standard library of functions that covers the majority of features someone needs at a low level is vital to helping deal with this sort of thing.

While there have been problems in the python and ruby worlds, and I’m sure that Go and Rust will face similar over time, the presence of both a comprehensive standard library and a community that accepts contributions means that there’s far fewer of these kinds of libraries around. 


## [Hackers target Docker, Hadoop, Redis, Confluence with new Golang malware ](https://www.bleepingcomputer.com/news/security/hackers-target-docker-hadoop-redis-confluence-with-new-golang-malware/)

[https://www.bleepingcomputer.com/news/security/hackers-target-docker-hadoop-redis-confluence-with-new-golang-malware/](https://www.bleepingcomputer.com/news/security/hackers-target-docker-hadoop-redis-confluence-with-new-golang-malware/)

> They started investigating the attack after getting an initial access alert on a Docker Engine API honeypot, with a new container based on Alpine Linux being spawned on the server.
> 
> For the next steps, the threat actor relies on multiple shell scripts and common Linux attack techniques to install a cryptocurrency miner, establish persistence, and set up a reverse shell.
> 
> According to the researchers, the hackers deploy a set of four novel Golang payloads that are responsible for identifying and exploiting hosts running services for Hadoop YARN ( [_h.sh_](http://h.sh/) ), Docker ( [_d.sh_](http://d.sh/) ), Confluence ( [_w.sh_](http://w.sh/) ), and Redis ( [_c.sh_](http://c.sh/) ).
> 
> The names of the payloads are likely a poor attempt at disguising them as bash scripts. However, they are 64-bit Golang ELF binaries.
> 
> “Interestingly, the malware developer neglected to strip the binaries, leaving DWARF debug information intact. There has been no effort made to obfuscate strings or other sensitive data within the binaries either, making them trivial to reverse engineer” - [Cado Security](https://www.cadosecurity.com/spinning-yarn-a-new-linux-malware-campaign-targets-docker-apache-hadoop-redis-and-confluence/) The hackers use the Golang tools to scan a network segment for open ports 2375, 8088, 8090, or 6379, which are the default ones for the targets of this campaign. 


The headline here is a bit misleading, but essentially true.  This is about the lateral movement and targeting once the hackers are into your system.

Exposing your docker API to the internet is probably a bad idea, because bad people can run containers and container breakouts remain a thing.  

That secondary lateral movement targeting modern digital infrastructure is interesting though.  You shouldn’t expect too much confluence and hadoop instances being available in production systems, which implies that they’re targeting the pre-product, developer or backend systems with this work. 


## [Trust but test: Vendor security testing at Canva - Canva Engineering Blog ](https://www.canva.dev/blog/engineering/trust-but-test/?utm_source=cloudseclist.com&utm_medium=referral&utm_campaign=CloudSecList-issue-229)

[https://www.canva.dev/blog/engineering/trust-but-test/?utm_source=cloudseclist.com&utm_medium=referral&utm_campaign=CloudSecList-issue-229](https://www.canva.dev/blog/engineering/trust-but-test/?utm_source=cloudseclist.com&utm_medium=referral&utm_campaign=CloudSecList-issue-229)

> Like all companies, Canva uses vendors to help achieve our goals, and when choosing our vendors, we need to ensure they reach our high-security standards. These vendors can range from the cloud infrastructure Canva runs on to the software libraries we use in our products. It’s all-encompassing, and as the interconnectedness of software increases, the risk of a single point of failure grows, as evidenced by the amount of supply chain breaches over the past few years. We want to create an ecosystem of trusted, _tested_ vendors to ensure Canva remains a secure and hardened product for even our most security-conscious customers.
> 
> […]
> 
> Most vendors we work with leave long-lasting positive interactions, regardless of the security review results, and become a valued part of Canva. Ultimately, however, we still help Canva make an informed business decision about vendor security. We’ve had a small number of cases where a vendor's security posture was not up to Canva's standards, and we decided to walk away from engagements with them. 


This is an interesting model and one I think I quite like, although I imagine that vendors want something repeatable so tehy can do it once rather than once for every customer.

But what’s critical is this bit hidden in the middle.  If you are a vendor of software, then how you react to reports of vulnerabilities is a critical part of your sales process.  Having a bad vulnerability reporting process that dismisses or minimises the security implications will cost you sales, and increasingly so in the current climate.

Investing in a positive and capable security response capability will improve your reputation, and thus increase sales (and hopefully profitability) 


## [Salt Labs research finds security flaws within ChatGPT Ecosystem (Remediated) ](https://salt.security/blog/security-flaws-within-chatgpt-extensions-allowed-access-to-accounts-on-third-party-websites-and-sensitive-data)

[https://salt.security/blog/security-flaws-within-chatgpt-extensions-allowed-access-to-accounts-on-third-party-websites-and-sensitive-data](https://salt.security/blog/security-flaws-within-chatgpt-extensions-allowed-access-to-accounts-on-third-party-websites-and-sensitive-data)

> The first part of the research focuses on a vulnerability found directly in ChatGPT, allowing attackers to install malicious plugins on ChatGPT users, without their approval. 
> 
> The second part of this blog is a security review of the plugins concept, with a demonstration of two critical account takeover vulnerabilities within dozens of plugins. The focus of this is not on the discovery of a specific third-party plugin but rather on the general concept. We present here repeating issues and vulnerabilities that we keep finding over and over on several plugins. We believe that some of these vulnerabilities could be avoided if developers were more aware of the risk, and we hope that our blog will help achieve that goal. We also call on OpenAI to put more emphasis on security in their documentation for developers, which we will explain further when looking at our third vulnerability discovery.


This is a new area of security research and yet another place where people rushing to market will naturally prioritise speed to market and product features over the security implications.

Unless you know exactly where your data is going, you should assume that attaching an AI front end to it is akin to opening access to that company, all its employees and most of it's customers.  If you aren't comfortable with that or they cannot explain how that won't happen, then maybe you shouldn't use it yet


## [The CEO’s secret to successful leadership: CEO Excellence revisited | McKinsey ](https://www.mckinsey.com/featured-insights/mckinsey-on-books/the-ceos-secret-to-successful-leadership-ceo-excellence-revisited)

[https://www.mckinsey.com/featured-insights/mckinsey-on-books/the-ceos-secret-to-successful-leadership-ceo-excellence-revisited](https://www.mckinsey.com/featured-insights/mckinsey-on-books/the-ceos-secret-to-successful-leadership-ceo-excellence-revisited)

> What did we actually find? Well, if you say to us, “What is the role of a CEO?,” we’re now crystal clear on what that is. We would say the irreducible core of the role consists of six things you will need to do:
> 
> 1. set the direction
> 2. align your organization on that direction
> 3. mobilize your leaders to deliver on that direction
> 4. work with your board
> 5. connect with a group of stakeholders
> 6. manage your personal effectiveness
> 
> Whether you’re a great CEO or not, these are the six roles of a CEO. Six feels like a lot, but it’s a big job, and it’s a hard job, as we just described. I think all of our CEOs looked at that list and said, “You know what? That’s a good taxonomy.” 


I really like this as. aset of leadership principles.  If you are meeting together in your senior leadership team, it’s worth looking at this list and asking yourselves whether are correctly covering all 6 of these things. 


