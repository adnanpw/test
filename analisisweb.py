# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 00:09:47 2016

@author: adnan
"""
#cek website dibuat dengan teknologi apa--> install library builtwith
import builtwith
builtwith.parse('http://example.webscraping.com')

#cek pemilik website--> install python-whois 
import whois
print whois.whois('appspot.com')

#Downloading a web page (Crawl website)---> run fungsi download lalu run script download('http://httpstat.us/500')
import urllib2
def download(url, user_agent='wswp', num_retries=2):
    print 'Downloading:', url
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Download error:', e.reason
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # recursively retry 5xx HTTP errors
                return download(url, num_retries-1)
    return html
