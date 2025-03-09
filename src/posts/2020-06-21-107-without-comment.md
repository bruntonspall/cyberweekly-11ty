---
title: "107 - Without comment"
date: 2020-06-21
description: "For the rest of June, I'll be providing a selection of stories from the news without comment or analysis. I've tried to highlight the a quote to sum up the most interesting or relevant part of the story in each case."
permalink: /without-comment/
---

For the rest of June, I'll be providing a selection of stories from the news without comment or analysis. I've tried to highlight the a quote to sum up the most interesting or relevant part of the story in each case.

Here's the weeks reading and interesting snippets I've run across this week.

## [Concise Argument and Evidence That Steven Pinker is Wrong About How Good Things Are | Daniel Miessler](https://danielmiessler.com/blog/concise-argument-and-evidence-that-steven-pinker-is-wrong-about-how-good-things-are/)

[https://danielmiessler.com/blog/concise-argument-and-evidence-that-steven-pinker-is-wrong-about-how-good-things-are/](https://danielmiessler.com/blog/concise-argument-and-evidence-that-steven-pinker-is-wrong-about-how-good-things-are/)

> The basic argument, broken into individual claims, is captured below.
> 
> * For a number of interconnected reasons, it’s becoming harder for everyday Americans to survive and thrive.
> * At the same time, the rich are doing better than any time in recent history, and income inequality is quickly moving towards recent historical maximums.
> * A big part of this is the fact that technology is becoming better at replacing human workers, and AI and robotics are about to remove millions more jobs.
> * AI is a threat to human work unlike anything we’ve seen before because it has the ability to permanently render humans as inferior to machines for most types of work.
> * Some of those jobs will be replaced by new types of work that humans will be better at (for now), but they will often require a skill or talent level that most of the displaced and new workers won’t have.
> * Human meaning is deeply tied to feeling valuable, and having millions of people who are unable to do anything that a machine can’t do better, is going to be a humanity-scale challenge.
> * With the great depression and the recent recession, it was accepted that there were fewer jobs right now, but that they’d eventually come back. That’s the part that’s different: because of AI and automation, millions of those jobs are going away permanently.


A compelling argument that the coming automation of jobs will increase inequality and hugely affect the poor and unskilled far more than the rich and highly skilled.


## [Enabling AWS Security Hub integration with AWS Chatbot | AWS Security Blog](https://aws.amazon.com/blogs/security/enabling-aws-security-hub-integration-with-aws-chatbot/)

[https://aws.amazon.com/blogs/security/enabling-aws-security-hub-integration-with-aws-chatbot/](https://aws.amazon.com/blogs/security/enabling-aws-security-hub-integration-with-aws-chatbot/)

> n this post, we show you how to configure AWS Chatbot to send findings from AWS Security Hub to Slack. Security Hub gives you a comprehensive view of your security high-priority alerts and security posture across your Amazon Web Services (AWS) accounts. AWS Chatbot is an interactive agent that makes it easy to monitor and interact with your AWS resources in your Slack channels and Amazon Chime chat rooms. This can enable your security teams to receive alerts in familiar Slack channels, facilitating collaboration and quick response to events.


This is worth looking at if you have an engineering team slack (and you probably should have something similar).  Getting security alerts into a team aware location means that everyone knows who is dealing with it, and people can indicate if it's a false positive easily and quickly.


## [Automating safe, hands-off deployments](https://aws.amazon.com/builders-library/automating-safe-hands-off-deployments/)

[https://aws.amazon.com/builders-library/automating-safe-hands-off-deployments/](https://aws.amazon.com/builders-library/automating-safe-hands-off-deployments/)

> When I interviewed for my job at Amazon, I made sure to ask one of the interviewers, “How often do you deploy to production?” At the time, I was working on a product that rolled out a major release once or twice a year, but sometimes I needed to release a small fix in between big releases. For each fix that I released, I spent hours carefully rolling it out. Then I frantically checked logs and metrics to see if I had broken anything after the deployment and needed to roll it back.
> 
> I read that Amazon practiced continuous deployment, so when I interviewed, I wanted to know how much time I would have to spend managing and watching deployments as a developer at Amazon. The interviewer told me that changes were automatically deployed to production multiple times a day by continuous deployment pipelines. When I asked how much of his day was spent carefully shepherding each of those deployments and watching logs and metrics for any impact as I had been doing, he told me usually none. Because the pipelines did this work for his team, most deployments weren’t actively watched by anyone. “Whoa!” I said. After I joined Amazon, I was excited to find out exactly how these “hands-off” automated deployments worked.


None


## [Dating Apps Exposed 845 GB of Explicit Photos, Chats, and More | WIRED](https://www.wired.com/story/dating-apps-leak-explicit-photos-screenshots/)

[https://www.wired.com/story/dating-apps-leak-explicit-photos-screenshots/](https://www.wired.com/story/dating-apps-leak-explicit-photos-screenshots/)

> Security researchers Noam Rotem and Ran Locar were scanning the open internet on May 24 when they stumbled upon a collection of publicly accessible Amazon Web Services "buckets." Each contained a trove of data from a different specialized dating app, including 3somes, Cougary, Gay Daddy Bear, Xpal, BBW Dating, Casualx, SugarD, Herpes Dating, and GHunt. In all, the researchers found 845 gigabytes and close to 2.5 million records, likely representing data from hundreds of thousands of users. They are publishing their findings today with vpnMentor.
> 
> The information was particularly sensitive and included sexually explicit photos and audio recordings. The researchers also found screenshots of private chats from other platforms and receipts for payments, sent between users within the app as part of the relationships they were building. And though the exposed data included limited "personally identifying information," like real names, birthdays, or email addresses, the researchers warn that a motivated hacker could have used the photos and other miscellaneous information available to identify many users. The data may not have actually been breached, but the potential was there.


None


## [Record DDoS Attack Hits AWS: 2.3 Tbps Assault Lasted Days](https://www.cbronline.com/news/record-ddos-attack-aws/amp/)

[https://www.cbronline.com/news/record-ddos-attack-aws/amp/](https://www.cbronline.com/news/record-ddos-attack-aws/amp/)

> The report also highlights the four most prominent (malicious) “interaction types” used to try and hack services running on AWS in Q1.
> 
> There were 41 million attempts made to compromise services using these four techiques along during the quarter: 31 percent of all events.
> 
> Without naming explicit CVEs, AWS points to:
> 
> • “Docker unauthenticated RCE, where the suspect attempts to exploit a Docker engine API to build a container, without authorization.
> 
> • “SSH intrusion attempts, where the suspect looks for ways to gain unauthorized access to the application using commonly used credentials or other exploits.
> 
> • “Redis unauthenticated RCE, where the suspect attempts to exploit the API of a Redis database to gain remote access to the application, gain access to the contents of the database, or make it unavailable to end users.
> 
> • “Apache Hadoop YARN RCE, where the suspect attempts to exploit the API of a Hadoop cluster’s resource management system and execute code, without authorization.


None


## [The Impending Doom of Expiring Root CAs and Legacy Clients](https://scotthelme.co.uk/impending-doom-root-ca-expiring-legacy-clients/)

[https://scotthelme.co.uk/impending-doom-root-ca-expiring-legacy-clients/](https://scotthelme.co.uk/impending-doom-root-ca-expiring-legacy-clients/)

> A very awesome friend of mine, Neil Craig, is Lead Technical Architect at the BBC and he got me some specific details of an incident over there and allowed me to share it with you. On a recent server certificate update they got a new certificate issued by the GlobalSign R5 Root, the root is valid from 13th Nov 2012 to 19th Jan 2038. The problem was, some TVs are so out of date that they don't have that R5 Root CA installed on them that was issued in 2012! This means that those TVs will reject certificates that chain to that Root CA and as a result, the streaming app stops working on the TV! Here we are in 2019/2020 with a problem that an 8 year old Root CA still hasn't managed to make its way onto a significant portion of 'Smart' TVs.


None


## [The State of Secure Software: Past, Present, and Future](https://blog.cobalt.io/the-state-of-secure-software-past-present-and-future-7573ca1d41ec)

[https://blog.cobalt.io/the-state-of-secure-software-past-present-and-future-7573ca1d41ec](https://blog.cobalt.io/the-state-of-secure-software-past-present-and-future-7573ca1d41ec)

> This amount of testing requires so much effort that even if Microsoft hired every pentester on the planet, there’s no way every piece of code could be inspected. This casts light on an issue that will become increasingly widespread as companies ship more and more code, and a shift in approach is necessary in order to keep up with developer output and effectively secure code at scale.
> 
> Ollmann identified three areas for immediate improvement:
> 
> * At the point of code creation, it should be hard for developers to make errors. Coding issues should be automatically identified and corrected.
> * Static analysis functions need to run early in the SLDC with a low false-positive rate. These functions must highlight critical issues and give actionable advice.
> * Fuzzing technologies need to be easy-to-use and productive — an automatic ‘pen test’ that can check every line of code before it’s shipped.


None


## [Bomze on Twitter: "Face Depixelizer Given a low-resolution input image, model generates high-resolution images that are perceptually realistic and downscale correctly. 😺GitHub: https://t.co/0WBxkyWkiK 📙Colab: https://t.co/q9SIm4ha5p P.S. Colab is based on the https://t.co/fvEvXKvWk2 https://t.co/lplP75yLha" / Twitter](https://twitter.com/tg_bomze/status/1274098682284163072)

[https://twitter.com/tg_bomze/status/1274098682284163072](https://twitter.com/tg_bomze/status/1274098682284163072)

> Face Depixelizer
> 
> Given a low-resolution input image, model generates high-resolution images that are perceptually realistic and downscale correctly.
> 
> GitHub: https://github.com/tg-bomze/Face-Depixelizer…
> Colab: https://colab.research.google.com/github/tg-bomze/Face-Depixelizer/blob/master/Face_Depixelizer_Eng.ipynb…
> 
> P.S. Colab is based on the
> https://github.com/adamian98/pulse


This shows how bias in training sets can come back to haunt you.  Just look at the replies to see what I mean


## [Elite CIA hacking unit failed to protect its systems, allowing disclosure to WikiLeaks - The Washington Post](https://www.washingtonpost.com/national-security/elite-cia-unit-that-developed-hacking-tools-failed-to-secure-its-own-systems-allowing-massive-leak-an-internal-report-found/2020/06/15/502e3456-ae9d-11ea-8f56-63f38c990077_story.html)

[https://www.washingtonpost.com/national-security/elite-cia-unit-that-developed-hacking-tools-failed-to-secure-its-own-systems-allowing-massive-leak-an-internal-report-found/2020/06/15/502e3456-ae9d-11ea-8f56-63f38c990077_story.html](https://www.washingtonpost.com/national-security/elite-cia-unit-that-developed-hacking-tools-failed-to-secure-its-own-systems-allowing-massive-leak-an-internal-report-found/2020/06/15/502e3456-ae9d-11ea-8f56-63f38c990077_story.html)

> “CIA has moved too slowly to put in place the safeguards that we knew were necessary given successive breaches to other U.S. Government agencies,” the report said, finding that “most of our sensitive cyber weapons were not compartmented, users shared systems administrator-level passwords, there were no effective removable media [thumb drive] controls, and historical data was available to users indefinitely.”
> 
> The task force noted that it could not determine the precise size of the breach because the CIA hacking team did not require monitoring of who used its network, but it was concluded that the employee stole as much as 34 terabytes of information, or about 2.2 billion pages.
> 
> Timothy Barrett, the CIA press secretary, declined to comment directly on the report. “CIA works to incorporate best-in-class technologies to keep ahead of and defend against ever-evolving threats,” he said.
> 
> The hacking tools were developed by the CIA’s Center for Cyber Intelligence, where the agency’s most-sophisticated hackers devised ways to gain access to hard-to-penetrate networks, for instance, to secretly activate the camera and microphone on a foreign target’s tablet, or steal the design plans for a foreign adversary’s advanced weapons systems.


None


