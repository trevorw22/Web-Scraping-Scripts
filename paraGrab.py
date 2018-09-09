# This script is from pythonprogramming.net and was created to help me learn web scraping with python.
# It grabs paragraphs from websites and prints them out.

import urllib.request
import urllib.parse
import re
import time


url = 'http://pythonprogramming.net'
values = {'s' : 'basics',
          'submit' : 'search'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8') # data should be bytes
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()

paragraphs = re.findall(r'<p>(.*?)</p>',str(respData))

for eachParagraph in paragraphs:
    print(eachParagraph)

time.sleep(15)
