# This was a work in progress Craigslist post scraper for generating
# data for a markov chain, but needs a lot of work still. 

import os
from bs4 import BeautifulSoup
import requests

urls = [
"https://lubbock.craigslist.org/pet/6184950649.html",
"https://lubbock.craigslist.org/pet/6185067374.html",
"https://lubbock.craigslist.org/pet/6184985457.html",
"https://lubbock.craigslist.org/pet/6184936094.html",
"https://lubbock.craigslist.org/pet/6181487542.html",
"https://lubbock.craigslist.org/pet/6143156255.html"
]


def process_post(url):
	req = requests.get(url)
	soup = BeautifulSoup(req.text, 'html.parser')
	post_title = soup.find(id = 'titletextonly').string
	post_body = soup.find(id = 'postingbody').string
	if not all([
		post_title is None,
		post_body is None
		]):
		raise ValueError()
	return (post_title, post_body)

def save(post_title, post_body):
	with open('titles.txt', 'a') as title_file:
		title_file.write(post_title + '\n')
	with open('bodies.txt', 'a') as body_file:
		body_file.write(post_body + '\n')

def main():
	os.unlink('titles.txt')
	os.unlink('bodies.txt')

	for url in urls:
		try:
			title, body = process_post(url)
		except ValueError:
			pass
		else:
			save(title, body)

if __name__ == '__main__':
	main()
