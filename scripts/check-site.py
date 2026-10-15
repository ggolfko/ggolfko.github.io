#!/usr/bin/env python3
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
import sys
ROOT=Path(__file__).resolve().parents[1]; IGN={".git","node_modules","infra","v1"}
class P(HTMLParser):
 def __init__(s): super().__init__();s.links=[];s.title=s.desc=s.canon=s.h1=False;s.it=False;s.txt=[]
 def handle_starttag(s,t,a):
  a=dict(a)
  if t=="a" and a.get("href"): s.links.append(a["href"])
  if t=="title": s.it=True
  if t=="h1": s.h1=True
  if t=="meta" and a.get("name","").lower()=="description" and a.get("content","").strip(): s.desc=True
  if t=="link" and a.get("rel","").lower()=="canonical" and a.get("href"): s.canon=True
 def handle_endtag(s,t):
  if t=="title": s.it=False;s.title=bool("".join(s.txt).strip())
 def handle_data(s,d):
  if s.it:s.txt.append(d)
def tgt(src,h):
 if h.startswith(("#","mailto:","tel:","javascript:")):return None
 u=urlparse(h)
 if u.scheme or u.netloc:return None
 r=u.path
 if not r:return None
 p=(ROOT/r.lstrip("/")) if r.startswith("/") else (src.parent/r)
 if r.endswith("/"):p=p/"index.html"
 return p.resolve()
err=[]
for f in ROOT.rglob("*.html"):
 if any(x in IGN for x in f.relative_to(ROOT).parts):continue
 p=P();p.feed(f.read_text())
 rel=f.relative_to(ROOT)
 if rel.name!="Kitti-Onthong-Resume.html":
  for n,v in [("title",p.title),("description",p.desc),("canonical",p.canon),("h1",p.h1)]:
   if not v:err.append(f"{rel} missing {n}")
 for h in p.links:
  t=tgt(f,h)
  if t and not t.exists():err.append(f"{rel} broken {h}")
if err:
 print("\n".join(err));sys.exit(1)
print("PASS")
