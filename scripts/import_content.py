"""Rebuild the static pages from the saved public content snapshot."""
from pathlib import Path
from bs4 import BeautifulSoup
import json,html,re
R=Path(__file__).resolve().parents[1]
def soup(n):return BeautifulSoup((R/'docs/source'/f'{n}.html').read_text(),'html.parser')
S={n:soup(n) for n in ['home','gallery-galaxy','meet-saraib','sacred-sound','media','art-walk','saraib-store']}
assets=json.loads((R/'docs/source/assets.json').read_text())
def asset(fragment):
 return next(v for k,v in assets.items() if fragment.lower() in k.lower())
def img(fragment,alt,cls=''):
 return f'<img class="{cls}" src="{asset(fragment)}" alt="{html.escape(alt)}" loading="lazy" decoding="async">'
def paragraphs(el):
 if el is None:return ''
 out=[]
 for p in el.select('p'):
  t=p.get_text(' ',strip=True)
  if t and t not in out:out.append(t)
 if not out:out=[el.get_text(' ',strip=True)]
 return ''.join('<p>'+html.escape(t)+'</p>' for t in out)
def desc(n):return S[n].select('.widget-about .x-rt')
nav=[('index.html','Home'),('gallery.html','Gallery Galaxy'),('music.html','Sacred Sound'),('about.html','Meet SaraiB'),('media.html','Media')]
old=(R/'index.html').read_text();head=old.split('<body>')[0];footer=old[old.index('<footer'):old.index('<script src=')].replace('Secure checkout by Square','Art · Music · Story')
contact='<section class="band"><div class="shell"><div><h2>Get in touch</h2><p>Connect with SaraiB about her art, music, or an upcoming event.</p></div><div><a class="btn btn-light" href="mailto:saraibcreative@gmail.com">Email SaraiB</a><p>saraibcreative@gmail.com</p></div></div></section>'
def page(name,title,body):
 h=re.sub(r'<title>.*?</title>',f'<title>{html.escape(title)} — SaraiB Creative</title>',head)
 header='<div class="announce">Free shipping on all prints</div><header class="site-header"><div class="shell nav"><a class="brand" href="index.html">'+img('official%20saraib','SaraiB Creative','brand-logo')+'</a><button class="nav-toggle" aria-expanded="false" aria-controls="site-nav" aria-label="Menu">☰</button><nav id="site-nav" class="nav-links" aria-label="Main navigation">'+''.join(f'<a href="{url}"'+(' aria-current="page"' if name==url else '')+f'>{label}</a>' for url,label in nav)+'</nav><a class="cart" href="https://saraibcreative.com/saraib-store">Shop ↗</a></div></header>'
 (R/name).write_text(h+'<body><a class="skip-link" href="#main">Skip to content</a>'+header+'<main id="main">'+body+contact+'</main>'+footer+'<script src="assets/main.js"></script></body></html>')
def section(body,alt=False):return '<section class="section'+(' section-alt' if alt else '')+'"><div class="shell">'+body+'</div></section>'
def split(a,b):return '<div class="split">'+a+b+'</div>'
def text(t):return '<div class="prose">'+t+'</div>'
gallery=next(o['galleryImages'] for o in json.loads((R/'docs/source/gallery-galaxy.json').read_text()) if 'galleryImages' in o)
def artcard(item,i):
 url='https:'+item['image']['image'];path=assets[url];alt='Painting by SaraiB, gallery artwork '+str(i+1)
 return f'<article class="card" data-kind="artwork"><a class="card-media" href="{path}" aria-label="View artwork {i+1} full size"><img src="{path}" alt="{alt}" loading="lazy" decoding="async"></a><div class="card-body"><p class="meta">Gallery Galaxy · {i+1:02d}</p><a href="mailto:saraibcreative@gmail.com?subject=Artwork%20enquiry%20-%20'+html.escape(url.split('/')[-1])+f'">Enquire about this artwork →</a></div></article>'
# Gallery: preserve every image, without inventing titles, inventory or prices.
page('gallery.html','Gallery Galaxy',section('<p class="eyebrow">Inspired creations</p><h1>Gallery Galaxy</h1><p class="lede">“The heavens declare the glory of God; and the firmament shows and proclaims His handywork.” — Psalm 19:1</p><div class="gallery-intro"><p>Explore all 15 paintings. Select a painting to view it in full.</p><a class="btn btn-ghost" href="https://saraibcreative.com/saraib-store">Visit the SaraiB Store ↗</a></div><div class="grid gallery-grid">'+''.join(artcard(x,i) for i,x in enumerate(gallery))+'</div>'))
# Home: original established layout with complete sourced prose.
homecopy=paragraphs(desc('home')[0]);bookcopy=paragraphs(desc('home')[1])
hero='<div class="event"><div class="shell"><time datetime="2026-09-12">September 12, 2026 · 2–6 pm</time><span>An afternoon of art, music &amp; inspiration.</span><a href="art-walk.html">View event details →</a></div></div><section class="hero"><div class="shell"><div><p class="eyebrow">The heart behind the art</p><h1>The Obsession with Color</h1><p class="lede">The desire to paint has become an obsession.</p><p class="lede">It all began in November 2024, when SaraiB took her first art class and discovered an unexpected fascination with color — and, even more so, with the magic of mixing them.</p><div class="hero-actions"><a class="btn btn-solid" href="gallery.html">Enter the Gallery Galaxy</a><a class="btn btn-light" href="music.html">Sacred Sound</a></div></div>'+img('ThefrequencyofWorship','Artwork by SaraiB','hero-art')+'</div></section>'
featured=section('<div class="section-head"><div><p class="eyebrow">Inspired creations</p><h2>Gallery Galaxy</h2></div><a href="gallery.html">Explore the gallery →</a></div><div class="grid">'+''.join(artcard(x,i) for i,x in enumerate(gallery[:3]))+'</div>')
homeextra=[]
for el in S['home'].select('.widget-gallery img[data-srclazy]'):
 u='https:'+el['data-srclazy'].split('/:')[0]
 if u not in ['https:'+x['image']['image'] for x in gallery] and u in assets and u not in homeextra:homeextra.append(u)
extra=section('<h2>More inspired creations</h2><div class="grid extra-art">'+''.join(f'<a href="{assets[u]}"><img src="{assets[u]}" alt="Artwork by SaraiB" loading="lazy"></a>' for u in homeextra)+'</div>')
page('index.html','Art, music & story',hero+featured+section(split(img('776985248','SaraiB','portrait'),text('<h2>The heart behind the art</h2>'+homecopy)),True)+extra+section(split(text('<p class="eyebrow">The story behind the journey</p><h2>A Mystic’s Journey: A Life of Encounter</h2><blockquote class="testimonial">'+bookcopy+'</blockquote><a class="btn btn-solid" href="https://geni.us/gwGoiC">Explore the book ↗</a>'),img('91oaESzHG6L','A Mystic’s Journey: A Life of Encounter book cover','book-cover')))+section(split(img('piano%20portrait','SaraiB at the piano','portrait'),text('<p class="eyebrow">Sacred Sound</p><h2>Where spirit, story, and music become one.</h2>'+paragraphs(desc('sacred-sound')[0])+'<a class="btn btn-ghost" href="music.html">Listen &amp; wonder</a>')),True)+section('<p class="verse">“And let the beauty and delightfulness and favor of the Lord our God be upon us; confirm and establish the work of our hands, confirm and establish it.”<small>Psalm 90:17 · Amplified Bible</small></p>'))
about=desc('meet-saraib')
page('about.html','Meet SaraiB',section(split(text('<p class="eyebrow">Artist · Musician · Author</p><h1>Meet SaraiB</h1>'+paragraphs(about[0])),img('776985248','SaraiB','portrait')))+section('<p class="verse">In all thy ways acknowledge him, and he shall direct thy paths.<small>Proverbs 3:6 · KJV</small></p>',True)+section('<div class="reading"><h2>Philosophy</h2>'+paragraphs(about[1])+'<h2>Style</h2>'+paragraphs(about[2])+'</div>'))
videos=[]
for i,iframe in enumerate(S['sacred-sound'].select('.widget-video iframe')):
 videoid=re.search(r'/embed/([^?]+)',iframe['src'])[1]
 titles=['You in Me','Wonderful Peace','Interior Design'];title=titles[i]
 d=S['sacred-sound'].select_one(f'[data-aid="VIDEO_DESCRIPTION_RENDERED{i}"]')
 videos.append(section(split(f'<div><iframe class="video" src="https://www.youtube-nocookie.com/embed/{videoid}" title="{title} — SaraiB" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe><a href="https://www.youtube.com/watch?v={videoid}">Watch on YouTube ↗</a></div>',text(f'<h2>{title}</h2>'+paragraphs(d))),i%2==0))
page('music.html','Sacred Sound',section(split(text('<p class="eyebrow">Listen &amp; wonder</p><h1>Sacred Sound</h1><p class="lede">Where spirit, story, and music become one.</p>'+paragraphs(desc('sacred-sound')[0])+'<p>“Sing unto the Lord a new song, and his praise from the end of the earth.” — Isaiah 42:10</p>'),img('piano%20portrait','SaraiB at the piano','portrait')))+''.join(videos))
media=S['media'].select_one('.widget-content')
media_desc=[x for x in media.select('.x-rt') if not x.find_parent(class_='x-rt')]
page('media.html','SaraiB in the Spotlight',section('<p class="eyebrow">Media &amp; exhibitions</p><h1>SaraiB in the Spotlight</h1>')+section(split(img('Shapes%20and%20Colors','Shapes and Colors 2026 exhibition certificate','full-image'),text('<h2>Shapes &amp; Colors 2026</h2>'+paragraphs(media_desc[0])+'<a class="btn btn-ghost" href="https://www.gallerium.art/p/shapes-and-colors-2026.html?AW=AW127139518">View exhibition ↗</a>')))+section(split(img('VANCOUVER','Vancouver Arts & Music Festival','full-image'),text('<h2>Vancouver Arts &amp; Music Festival</h2>'+paragraphs(media_desc[1]))),True)+section('<h2>Events</h2><p>September 12, 2026 · Open House Art Walk · 2–6 pm</p><a class="btn btn-solid" href="art-walk.html">View event details</a>'))
page('art-walk.html','Open House Art Walk',section(split(text('<p class="eyebrow">September 12, 2026</p><h1>Open House Art Walk</h1><p class="lede">Come, wander, connect &amp; experience an afternoon of art, music and inspiration with SaraiB.</p><p><strong>2 pm–6 pm</strong></p><p>Private Residence — Address Provided Upon RSVP</p><a class="btn btn-solid" href="mailto:saraibcreative@gmail.com?subject=September%2012%20Art%20Walk%20RSVP">RSVP by email</a>'),img('AF3BA1AE','Open House Art Walk invitation','full-image'))))
print('Imported 6 pages,',len(gallery),'gallery images,',len(homeextra),'additional artworks and',len(videos),'videos')
