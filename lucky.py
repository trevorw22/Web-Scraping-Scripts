#! python3
# lucky.py - Opens several Google search results.
# This is from Automate the Boring Stuff by Al Sweigart.
# I used this to help me learn web scraping.

import requests, sys, webbrowser, bs4

print('Googling...') # display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links
soup = bs4.BeautifulSoup(res.text)

# Open a browser tab for each result
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems)) # len(linkElems) will be the number of links opened if google returns < 5 results
for i in range(numOpen):
	webbrowser.open('http://google.com' + linkElems[i].get('href')) # the href's value in the returned <a> elements don't have the initial http://google.com part

''' OTHER IDEAS
Open all the product pages after searching a shopping site such as Amazon

Open all the links to reviews for a single product

Open the result links to photos after performing a search on a photo site such as Flickr or Imgur'''
