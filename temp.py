import sys, urllib, re, urlparse, os, argparse
# using BeautifulSoup to scrape download links
from bs4 import BeautifulSoup as bs


parser = argparse.ArgumentParser(description='Download static files from any URL')

parser.add_argument('-u',metavar="<URL>",help="Target URL",required=True)
parser.add_argument('-l',metavar="<location>",help="Save location | default : ./dnlwd",default="dnwld")
parser.add_argument('-e',metavar="<ext>",help="comma seperated list of arguments",default='pdf')

#parsing and setting up parameters
args = parser.parse_args()
ext = '|'.join(args.e.split(","))

"""
url: target URL
fol: dir to store downloaded items
ext: prefered extension(s) to download(not implemented yet)
"""
def start(url,fol,ext=None):
	print (url)
	try:
		f = urllib.urlopen(url)
		soup = bs(f,"lxml")
	except:
		print "Bad URL:\t" + url
		parser.print_help()
		sys.exit(1)

#creating fol dir if it doesn't exist
	if not os.path.exists(fol):
		os.makedirs(fol)

	os.chdir(fol)
	expr = '(?i)('+ext+')$'
	print (expr)
	for i in soup.findAll('a', attrs={'href': re.compile(expr)}):
		link_url = urlparse.urljoin(url, i['href'])

		print 'working\t',i.text
		urllib.urlretrieve(link_url,i.text)

	print "done"
	return

#calling function with all parameters set
start(args.u,args.l,ext)
