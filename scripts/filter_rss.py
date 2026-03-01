"""filter_rss.py."""
from __future__ import annotations

import feedparser
from feedgen.feed import FeedGenerator


ORIGINAL_RSS = "https://fictograma.com/atom/t/literatura"
OUTPUT_FILE = "rss/feed.xml"

feed = feedparser.parse(ORIGINAL_RSS)
entries = list(feed.entries)
feed_info = feed.feed

fg = FeedGenerator()
fg.title(feed_info.get("title", "RSS filtrado"))
fg.link(href=feed_info.get("link", ""))
fg.description(feed_info.get("subtitle", ""))

num_entries = 0
for entry in entries:
  link = str(entry["link"])
  if link.rsplit("/", maxsplit=1)[-1] != "1":
    continue
  num_entries += 1

  fe = fg.add_entry()
  fe.title(entry.title)
  fe.link(href=link)
  fe.description(entry.get("summary", ""))
  fe.pubDate(entry.updated)
  print(f"{num_entries}: {entry.title} [{entry.updated}]")

if num_entries > 0:
  fg.rss_file(OUTPUT_FILE)
  print("RSS actualizado")
else:
  print("RSS sin novedades")

