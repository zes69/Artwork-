import json,re,hashlib,subprocess,concurrent.futures
from pathlib import Path
from urllib.parse import unquote
root=Path(__file__).resolve().parents[1]
urls=set()
for p in (root/'docs/source').glob('*'):
 if p.suffix not in ['.html','.json']:continue
 text=p.read_text()
 for u in re.findall(r'(?:(?:https:)?//img1\.wsimg\.com/isteam/ip/89cdc816-f4d5-4791-9db9-12ed5734b8e5/[^"\s<>\\]+)',text):
  u=u.split('/:')[0]
  if re.search(r'\.(jpg|jpeg|png|webp)$',u,re.I):urls.add('https:'+u if u.startswith('//') else u)
folder=root/'assets/images';folder.mkdir(exist_ok=True)
manifest={}
def fetch(u):
 name=re.sub(r'[^a-z0-9.-]+','-',unquote(u.split('/')[-1]).lower())
 name=hashlib.sha256(u.encode()).hexdigest()[:7]+'-'+name
 path=folder/name
 if not path.exists():subprocess.run(['curl','-sSL','--fail','--retry','2','--max-time','40',u+'/:/rs=w:1600,cg:true,m/qt=q:85','-o',str(path)],check=True)
 return u,'assets/images/'+name
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
 for u,p in ex.map(fetch,sorted(urls)):manifest[u]=p
(root/'docs/source/assets.json').write_text(json.dumps(manifest,indent=2))
print('Downloaded',len(manifest),'images')
