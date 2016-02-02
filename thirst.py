#!/usr/bin/python

import os
import sys
import urllib
import urllib2
import re
from bs4 import BeautifulSoup

home = 'http://www.tutorialspoint.com'

url_list = open("url_list", "a")

next_page = sys.argv[1]
flag = 0

def populate_list():
	global next_page
	global flag
	
	regexp = re.compile('[/a-zA-Z0-9_-]*.htm')
	
	while 1:
		f = urllib.urlopen(next_page)
		s = f.read()
		f.close()
		
		soup = BeautifulSoup(s, "lxml")

		mydivs = soup.findAll("div", { "class" : "nxt-btn" })

		paragraphs = []

		for x in mydivs:
		        paragraphs.append(str(x))

		result = regexp.search(paragraphs[0])

		next_page = home + result.group()

		next_pdf = next_page[::-1]

		next_pdf = next_pdf.replace("/", "/fdp/", 1)

		next_pdf = next_pdf.replace("mth", "fdp", 1)

		next_pdf = next_pdf[::-1]

		with open('url_list', 'r') as searchfile:
			for line in searchfile:
				if next_pdf in line:
					flag = 1

		if (flag == 1):
			break

		url_list.write(next_pdf + "\n");

		print "%s" % (next_pdf)
	
	url_list.close();


def download_pdfs():
	with open('url_list1', 'r') as searchfile:
		for line in searchfile:
			os.system("wget " + line)


populate_list()

os.system("sort -u url_list > url_list1 && rm url_list")

download_pdfs()

os.system("pdfunite *.pdf res.pdf")
os.system("mkdir res || mv res.pdf ${PWD}/res/res.pdf")
os.system("rm url_list1 *.pdf")