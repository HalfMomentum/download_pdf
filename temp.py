import sys, urllib, re, urlparse, os
from bs4 import BeautifulSoup

if not len(sys.argv) == 3:
    print >> sys.stderr, "Usage: %s <URL> <directory>" % (sys.argv[0],)
    sys.exit(1)

url = sys.argv[1]
fol = os.path.join(os.getcwd(),sys.argv[2])
f = urllib.urlopen(url)

soup = BeautifulSoup(f,"lxml")

if not os.path.exists(fol):
  os.makedirs(fol)
os.chdir(fol)

for i in soup.findAll('a', attrs={'href': re.compile('(?i)(pdf)$')}):
    full_url = urlparse.urljoin(url, i['href'])
    urllib.urlretrieve(full_url,i.text)
    print 'working\t',i.text

print "Done"