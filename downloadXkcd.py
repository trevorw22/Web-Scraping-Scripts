#! python3
# This script scrapes and downloads all of the XKCD comic strips to a folder.
# It came from the book Automate the Boring Stuff by Al Sweigart.

import requests, os, bs4

url = 'http://xkcd.com'		# starting url
os.makedirs('xkcd', exist_ok=True)		# store comics in ./xkcd

while not url.endswith('#'):
	# Download the page
	print('Downloading page %s...' % url)
	res = requests.get(url)
	res.raise_for_status()		# Throws an exception if something went wrong with the downlaod
	soup = bs4.BeautifulSoup(res.text)
	# Find the URL of the comic image
	comicElem = soup.select('#comic img')	# the <img> element for the comic image is inside a <div> element with the id attribute set to comic

	if comicElem == []:
		print('Could not find comic image.')

	else:
		try:
			comicUrl = 'http:' + comicElem[0].get('src')
			# Download the image
			print('Downloading image %s...' % (comicUrl))
			res = requests.get(comicUrl)
			res.raise_for_status()

		except requests.exceptions.MissingSchema:
			# skip this comic
			prevLink = soup.select('a[rel="prev"]')[0]
			url = 'http://xkcd.com' + prevLink.get('href')
			continue

		# Save the image to ./xkcd
		imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb') # os.path.basename returns the last part, which is the name of the image file

		for chunk in res.iter_content(100000):
			imageFile.write(chunk)
		imageFile.close()

	# Get the Prev button's url
	prevLink = soup.select('a[rel="prev"]')[0]
	url = 'http://xkcd.com' + prevLink.get('href')

print('Done.')
''' Similair Ideas
Back up an entire site by following all of its links.

Copy all the messages off a web forum.

Duplicate the catalog of items for sale on an online store.'''
