#!/usr/bin/python

# temperature.py is a Python 3 script I created which uses a web scraper to grab the current temperature from a weather website.
# It requires the BeautifulSoup4 and requests libraries which can be installed with 'pip3 install bs4' and 'pip3 install requests'.
# The default coordinates are for Lubbock, TX but can be easily changed to anywhere in the world.

from bs4 import BeautifulSoup
import requests

url = requests.get("http://forecast.weather.gov/MapClick.php?lat=33.5845&lon=-101.845")
soup = BeautifulSoup(url.content, "html.parser")


#for name in names:
name = soup.find('p', class_='myforecast-current-lrg').text
print(name)

#print(soup.prettify())
