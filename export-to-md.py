import json
from datetime import datetime

export = json.load(open('export.json'))
for newsletter in export['newsletters']:
    sent=datetime.fromisoformat(newsletter['sentdate'])
    sentdate=sent.strftime("%Y-%m-%d")
    issue=int(newsletter['number'])
    slug=newsletter['slug']
    fname=f"src/posts/{sentdate}-{issue}-{slug}.md"
    print(f"Writing to {fname}")
    with open(fname, mode='w', encoding="utf-8") as f:
        description = newsletter['body'].split('\n')[0].replace('"', '\\"')
        f.write("---\n")
        f.write(f"title: \"{issue} - {newsletter['title'].replace('"', '\\"')}\"\n")
        f.write(f"date: {sentdate}\n")
        f.write(f"description: \"{description}\"\n")
        f.write(f"permalink: /{slug}/\n")
        f.write(f"---\n\n")
        f.write(f'{newsletter['body']}\n\n')
        for link in newsletter['links']:
            f.write(f"## [{link['title']}]({link['url']})\n\n")
            f.write(f"[{link['url']}]({link['url']})\n\n")
            if 'quote' in link and link['quote'] is not None:
                for line in link['quote'].split('\n'):
                    f.write(f"> {line}\n")
            f.write('\n\n')
            if 'note' in link:
                f.write(f"{link['note']}\n")
            f.write("\n\n")
        