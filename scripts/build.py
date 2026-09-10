"""Validate and package the static site; Python standard library only."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import shutil,json
R=Path(__file__).resolve().parents[1];D=R/'dist'
pages=['index.html','gallery.html','music.html','about.html','media.html','art-walk.html']
class Check(HTMLParser):
 def __init__(self):super().__init__();self.refs=[];self.images=[];self.h1=0
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='h1':self.h1+=1
  if tag=='img':
   assert a.get('alt'), 'Missing image alternative text'
   self.images.append(a.get('src'))
  for k in ['href','src']:
   if a.get(k):self.refs.append(a[k])
used=set();count=0
for f in pages:
 s=(R/f).read_text();p=Check();p.feed(s)
 assert p.h1==1,(f,'must contain one h1')
 assert all(x not in s for x in ['data-art=','data-mock=','data-add','href="#cart"','Track title pending','Secure checkout by Square']),(f,'mock content')
 for url in p.refs:
  u=urlsplit(url)
  if u.scheme or u.netloc or not u.path:continue
  path=R/unquote(u.path).lstrip('/')
  assert path.is_file(),(f,'Missing link or asset',url)
  if u.path.startswith('assets/'):used.add(u.path)
 count+=len(p.images)
# Verify image signatures, so a CDN error page cannot be deployed as a painting.
for a in used:
 if a.startswith('assets/images/'):
  data=(R/a).read_bytes()
  assert data[:3]==b'\xff\xd8\xff' or data[:8]==b'\x89PNG\r\n\x1a\n' or data[:4]==b'RIFF',(a,'Invalid image')
if D.exists():shutil.rmtree(D)
D.mkdir()
for a in used:
 target=D/a;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(R/a,target)
for f in pages:
 s=(R/f).read_text()
 # Root URLs also work from the original site's clean route aliases.
 for a in used:s=s.replace('"'+a+'"','"/'+a+'"')
 for page in pages:s=s.replace('"'+page+'"','"/'+page+'"')
 (D/f).write_text(s)
aliases={'gallery-galaxy':'gallery.html','sacred-sound':'music.html','meet-saraib':'about.html','media':'media.html','art-walk':'art-walk.html'}
for route,f in aliases.items():
 (D/route).mkdir();shutil.copyfile(D/f,D/route/'index.html')
(D/'404.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Page not found — SaraiB Creative</title><link rel="stylesheet" href="/assets/styles.css"><main class="section shell"><h1>Page not found</h1><p><a href="/">Return to SaraiB Creative</a></p></main></html>')
print(f'Validated {len(pages)} pages, {count} image placements, {len(used)} local assets; built dist.')
