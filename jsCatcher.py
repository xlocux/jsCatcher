#!/usr/bin/env python
# -*- coding: utf-8 -*-
# JsCatcher 
# By Locu

# Import libraries
import os
import sys
import argparse
import requests
import fileinput
from bs4 import BeautifulSoup
from urlparse import urljoin
from urlparse import urlparse
from requests.packages.urllib3.exceptions import InsecureRequestWarning 
reload(sys)
sys.setdefaultencoding('utf8')

# Command line Arguments
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', help='Input a: URL', action='store')
parser.add_argument('-l', '--list', help='Input a: URL list', action='store')
parser.add_argument('-d', '--download', help='Download javascript files (it is also possible to specify the download path)', action='store')
parser.add_argument('-o', '--output', help='Save javascript link to file', action='store')
parser.add_argument('-r', '--retire', help='Run Retire against downloaded javascripts (An output file .json is required)', action='store')

if len(sys.argv)<2:
	print('eg: python %s -l url.list -d /url/' % sys.argv[0])
	args = parser.parse_args(['-h'])
else:
	args = parser.parse_args()

def parser_error(errmsg):

    print('Usage: python %s [Options] use -h for help' % sys.argv[0])
    print('Error: %s' % errmsg)
    sys.exit()

#check url protocols
def check_input(url):
	if url.startswith(('http://', 'https://')):
		if url.endswith('/'):
			return url
		else:
			return (url+'/')
	else:
		print 'Error: protocol is missing (http,https)'
		sys.exit(1)


def send_request(url):
	try:
		requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
		r = requests.get(url, timeout=3, stream=True, verify=False)
		data = r.text
		soup = BeautifulSoup(data, 'lxml')
		for n in soup.find_all('script'):
			jslink = n.get('src')
			if jslink is not None:
				uri = urljoin(url, jslink)
				print uri
				if args.download:
					domain = urlparse(url).hostname
					try:
						req = requests.get(uri, timeout=3, stream=True, verify=False)
						path = os.path.join(args.download, domain, (jslink.split('/')[-1].split('?')[0]))
						js = req.text
						if not os.path.exists(args.download + '/' + domain):
							os.makedirs(args.download + '/' + domain)
						with open(path, 'wb') as f:
							f.write(js)			
					except requests.exceptions.RequestException as e:
							pass
				elif args.output:
					try:
						output = open(args.output, 'a')
						output.write (urljoin(url, jslink)+'\n')
					except:
						error('Failed writing to file:', args.output)


	except requests.exceptions.RequestException as e:
		pass

if args.output:
	open(args.output, 'w').close()

if args.url:
	uri = check_input(args.url)
	try:
		send_request(uri)
	except:
		pass

if args.list:
	url_list = []
	url_list = filter(None, open(args.list, 'r').read().splitlines())
	for url in url_list:
		uri = check_input(url)
		try:
			send_request(uri)
		except:
			pass

if args.retire:
	args = 'retire --path ' + args.download + ' --outputformat json --outputpath ' + args.retire
	os.system(args)


	

