#!/usr/bin/python

import os
import sys
import urllib
import re
from bs4 import BeautifulSoup

home = 'http://www.tutorialspoint.com'

f=urllib.urlopen(sys.argv[1])
s=f.read()
f.close()
soup = BeautifulSoup(s, "lxml")

mydivs = soup.findAll("div", { "class" : "nxt-btn" })

paragraphs = []

#print mydivs

for x in mydivs:
        paragraphs.append(str(x))

#print paragraphs[0]
#print type(paragraphs[0])

regexp = re.compile('[/a-zA-Z0-9_]*.htm')
result = regexp.search(paragraphs[0])

next_page = home + result.group()

print next_page

