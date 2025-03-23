#!/usr/bin/env python3
import requests
import datetime
import logging
import notion_client
import argparse
import re
from urllib.parse import urlparse, parse_qs, urlencode
from dotenv import dotenv_values
from notion_client import Client

from re import sub

def slugify(s):
  s = s.lower().strip()
  s = re.sub(r'[^\w\s-]', '', s)
  s = re.sub(r'[\s_-]+', '-', s)
  s = re.sub(r'^-+|-+$', '', s)
  return s

def clean_url(url):
    u = urlparse(url)
    qs = parse_qs(u.query)
    new_ks = [(k,v) for k,v in qs.items() if not k.startswith('utm_')]
    new_query = urlencode(new_ks, doseq=True)
    return u._replace(query=new_query).geturl()


def notion_richtext_to_markdown(block):
    md = ""
    prev_text = False
    for subblock in block:
        prefix = ""
        suffix = ""
        text = subblock["text"]["content"]
        if subblock["annotations"]["code"]:
            prefix = "`" + prefix
            suffix = suffix + "`"
        if subblock["annotations"]["strikethrough"]:
            prefix = "~~" + prefix
            suffix = suffix + "~~"
        if subblock["annotations"]["italic"]:
            prefix = "_" + prefix
            suffix = suffix + "_"
        if subblock["annotations"]["bold"]:
            prefix = "**" + prefix
            suffix = suffix + "**"
        if subblock["href"]:
            prefix = "[" + prefix
            suffix = suffix + "](" + subblock["href"] + ")"
        if prefix == "" and suffix == "":
            # There's no annotations, so this is just content.
            # If the previous one was just content, then it's a new paragraph, so start a new paragraph
            if prev_text:
                prefix = "\n\n"
            else:
                # This is just content so set prev_text
                prev_text = True
        else:
            # This is't just content, so unset prev_text
            prev_text = False
        md += f" {prefix}{text.strip()}{suffix} "
    return md

def text_to_quote(text):
    return "\n".join(["> "+line for line in text.split('\n')])


def main(args):
    config = dotenv_values()
    md = f'''---
title: "XXX - {args.title}"
date: {datetime.datetime.today().strftime("%Y-%m-%d")}
description: XXX
---

WRITE INTRO HERE

'''
    lastrun = None
    if args.verbose:
        logging.info(f"Fetching from notion {config["NOTION_DB"]} with token {config["NOTION_AUTHTOKEN"]}")
    notion = Client(auth=config["NOTION_AUTHTOKEN"])

    since = {"past_week": {}}

    importtime = datetime.datetime.now().isoformat()
    count = 0

    # Process items that have been editing in the last week, but already tagged
    query = {
        "and": [
            {"property": "Edited", "date": since},
        ]}
    if args.verbose:
        logging.info(f"Fetching from Notion with query {query}")

    existing_items = notion.databases.query(database_id=config["NOTION_DB"], filter=query)

    for result in existing_items["results"]:
        if "Imported" in result["properties"] and result["properties"]["Imported"]["date"]:
            lastimported = datetime.datetime.fromisoformat(result["properties"]["Imported"]["date"]["start"])
        else:
            lastimported = datetime.datetime.fromisoformat("1999-01-01T00:00:00.000+00:00")
        edited = datetime.datetime.fromisoformat(result["properties"]["Edited"]["last_edited_time"].replace('Z', '+00:00'))
        name = result['properties']['Name']['title'][0]['plain_text']
        logging.info(f"Examining {name} - Edited {edited}, imported {lastimported}")

        if edited > lastimported:  # Has it been touched in Notion since we last ran the import script?
            url = result['properties']['URL']['url']
            comment = notion_richtext_to_markdown(result['properties']['Comment']['rich_text'])
            quote = notion_richtext_to_markdown(result['properties']['Quote']['rich_text'])
            title = notion_richtext_to_markdown(result['properties']['Name']['title'])
            md += f'''
## [{title}]({url})

[{url}](url)

{text_to_quote(quote)}

{comment}
'''
            if not args.dryrun:
                imported = {"date": {"start": importtime}}
                logging.info(f"Setting imported to {importtime}")
                notion.pages.update(page_id=result['id'], properties={'Imported': imported})
    md += '''
Thanks for reading

Michael'''
    with open(args.filename, "w") as f:
        if args.verbose:
            logging.info(f"Writing to {args.filename}")
        f.writelines(md)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="Notion2MD", description="Downloads recent links from a Notion database")
    parser.add_argument('-t', '--title', help="Title of the blogpost to create", default="TITLE")
    parser.add_argument('-f', '--filename', help="Filename of markdown file to write", default=None)
    parser.add_argument('-l', '--log', action='store_true', help="Turn on logging")
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('-d', '--dryrun', action='store_true', help="Don't actually update NotionDB or write markdown file")
    parser.add_argument('-L', '--logfile', help="Log to file instead of console")
    args = parser.parse_args()
    if not args.filename:
        args.filename = f"src/posts/{datetime.datetime.now().strftime("%Y-%m-%d")}-{slugify(args.title)}.md"
    if args.log:
        if args.logfile:
            logging.basicConfig(filename=args.logfile, level=logging.INFO)
        else:
            logging.basicConfig(level=logging.INFO)
        logging.info(f"Starting into {args.filename}, dryrun: {args.dryrun}, verbose: {args.verbose}")
    main(args)

