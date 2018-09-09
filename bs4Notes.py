import bs4 as bs
import urllib.request
import pandas as pd

sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()

soup = bs.BeautifulSoup(sauce, 'lxml') # beautiful soup object

print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.p) # prints the first paragraph element
print(soup.find_all('p'))
for paragraph in soup.find_all('p'):
    print(paragraph.string) # This returns some None, because its not a navigable string
	print(paragraph.text) # This will return everything, even the child tags within the paragraph tags

print(soup.get_text()) # This gets every kind of text in any tags most likely

for url in soup.find_all('a'): # Grabs every link on the page
    print(url) # Shows the entire tag of every link on the page
    print(url.get('href')) # This grabs the ACTUAL LINKS



# NAVIGATION

# grabs the navigation bar
nav = soup.nav
print(nav)

# To get all the links that it finds in the navigation bar we use this for loop..
for url in nav.find_all('a'):
    print(url.get('href')) # It finds double the links because there are two navbars, one for mobile on side, one for desktop at top

# Grab the text from the body
body = soup.body
for paragraph in body.find_all('p'):
    print(paragraph.text)

# In some cases there will be multiple bodies like so.. <div class="body">
# In order to not grab all of the div's we use the class_='body' to tell it the class to scrape
for div in soup.find_all('div', class_='body'):
    print(div.text)



# TABLES and XML Documents
# We will pull the table data information <td> tag, which is inside <table> tag and <tr> table row tag, excluding <th> table header information

# Grabs all table information
table = soup.table

# or we can do the same thing by setting table = soup.find('table')
table = soup.find('table')

print(table)

table_rows = table.find_all('tr')

# to find just one row we can use table.find('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td] # In output the first list will be empty because the table header doesn't have table row tags
    print(row)


# PANDAS has a table scraper that is much better

# The following will go to the website, and return a list of all the dataframes of all the tables it finds

dfs = pd.read_html('https://pythonprogramming.net/parsememcparseface/', header=0)
for df in dfs:
    print(df)


# XML
# deals with sitemaps, it is human and machine readable
# For example, if we wanted a bot that was constantly tracking news, we would just track the sitemaps for new links

sauce = urllib.request.urlopen('https://pythonprogramming.net/sitemap.xml').read()
soup = bs.BeautifulSoup(sauce, 'xml')

print(soup)

for url in soup.find_all('loc'): # this retrieves a list of all links in the sitemap using the location tag
    print(url.text)



# DYNAMIC JAVASCRIPT SCRAPING

source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/')
soup = bs.BeautifulSoup(source, 'lxml')
js_test = soup.find('p', class_='jstest')
print(js_test.text)
