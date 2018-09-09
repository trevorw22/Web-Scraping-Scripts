import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(res)
#<class 'requests.models.Response'> # This the the response object that is returned when we call type(res)
res.status_code == requests.codes.ok # This tells us that the request for the webpage succeeded
#True
len(res.text)
#178981    	# This shows us that the webpage which is stored in the text variable of Response is over 178,000 characters long.
print(res.text[:250]) # Display only the first 250 characters
  # The Project Gutenberg EBook of Romeo and Juliet, by William Shakespeare

  #  This eBook is for the use of anyone anywhere at no cost and with
  #  almost no restrictions whatsoever. You may copy it, give it away or
  #  re-use it under the terms of the Proje


# Checking for Errors
# A simpler way to check for errors instead of using == requests.codes.ok, is to use raise_for_status() method.
res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
res.raise_for_status()
# Traceback (most recent call last):
#   File "<pyshell#138>", line 1, in <module>
#     res.raise_for_status()
#   File "C:\Python34\lib\site-packages\requests\models.py", line 773, in raise_for_status
#     raise HTTPError(http_error_msg, response=self)
# requests.exceptions.HTTPError: 404 Client Error: Not Found

import requests
res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))
# This raise_for_status() method call causes the program to output the following:
# There was a problem: 404 Client Error: Not Found
# It is a good way to ensure that a program halts if a bad download occurs.


# Saving Downloaded Files to the Hard Drive
# We use the standard open() and write() with slight differences. We open the file with write binary mode wb
# To maintain unicode encoding, we write it in binary with wb as the second argument in open()
# To write the web page to a file, you can use a for loop with the Response object's iter_content() method.
import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
	playFile.write(chunk)
# 100000
# 78981
playFile.close()
# The iter_content() method returns "chunks" of the content on each iteration. Each chunk is of the bytes data type.
# 100000 bytes is usually a good size to pass in the iter_content() argument.
# The file RomeoAndJuliet.txt will now exist in the current working directory. 

# To review, here’s the complete process for downloading and saving a file:
# Call requests.get() to download the file.
# Call open() with 'wb' to create a new file in write binary mode.
# Loop over the Response object’s iter_content() method.
# Call write() on each iteration to write the content to the file.
# Call close() to close the file.



# Parsing HTML With The BeautifulSoup Module
# Don’t Use Regular Expressions to Parse HTML
# bs4.BeautifulSoup() function is called with a string containing the HTML it will parse.
>>> import requests, bs4
>>> res = requests.get('http://nostarch.com')
>>> res.raise_for_status()
>>> noStarchSoup = bs4.BeautifulSoup(res.text)
>>> type(noStarchSoup)
<class 'bs4.BeautifulSoup'>
# To load an HTML file from your hard drive to bs4 use the following.. 
>>> exampleFile = open('example.html')
>>> exampleSoup = bs4.BeautifulSoup(exampleFile)
>>> type(exampleSoup)
<class 'bs4.BeautifulSoup'>


# Finding an Element With The Select() Method
# You can retrieve a web page element from a bs4 object by calling select() and passing a 
# string of a CSS selector for the element you are looking for. 
# Selectors are like regular expressions but for HTML patterns
# Examples of CSS selectors..
soup.select('div')						All elements named <div>

soup.select('#author')					The element with an id attribute of author

soup.select('.notice')					All elements that use a CSS class attribute named notice

soup.select('div span')					All elements named <span> that are within an element named <div>

soup.select('div > span')				All elements named <span> that are directly within an element named <div>, with no other element in between

soup.select('input[name]')				All elements named <input> that have a name attribute with any value

soup.select('input[type="button"]')		All elements named <input> that have an attribute named type with value button

# You can also use more sophisticated matches like so..
# soup.select('p #author') will match any element that has an id attribute of author, 
# as long as it is also inside a <p> element.
'''
The select() method will return a list of Tag objects, which is how Beautiful Soup 
represents an HTML element. The list will contain one Tag object for every match in the 
BeautifulSoup object’s HTML. Tag values can be passed to the str() function to show the 
HTML tags they represent. Tag values also have an attrs attribute that shows all the HTML 
attributes of the tag as a dictionary.
'''


>>> import bs4
>>> exampleFile = open('example.html')
>>> exampleSoup = bs4.BeautifulSoup(exampleFile.read())
>>> elems = exampleSoup.select('#author') # Return a list of all elements with id="author"
>>> type(elems)							  # elems is a list of the tags found and stored by bs4
<class 'list'>
>>> len(elems)							  # There is one tag object in the list; there was one match. 
1
>>> type(elems[0])
<class 'bs4.element.Tag'>
>>> elems[0].getText()					  # getTex() returns the inner HTML
'Al Sweigart'
>>> str(elems[0])						  # Gives us a string of the tage and inner HTML
'<span id="author">Al Sweigart</span>'	  
>>> elems[0].attrs 						  # attrs gives us a dictionary with the element's attribute, 'id', and the value of the id attribute, 'author' 
{'id': 'author'}

# You can also pull all the <p> elements from the BeautifulSoup object.
>>> pElems = exampleSoup.select('p')
>>> str(pElems[0])
'<p>Download my <strong>Python</strong> book from <a href="http://inventwithpython.com">my website</a>.</p>'
>>> pElems[0].getText()
'Download my Python book from my website.'
>>> str(pElems[1])
'<p class="slogan">Learn Python the easy way!</p>'
>>> pElems[1].getText()
'Learn Python the easy way!'
>>> str(pElems[2])
'<p>By <span id="author">Al Sweigart</span></p>'
>>> pElems[2].getText()
'By Al Sweigart'
'''
This time, select() gives us a list of three matches, which we store in pElems. Using str() on pElems[0], 
pElems[1], and pElems[2] shows you each element as a string, and using getText() on each element shows 
you its text.
'''


# Getting Data from an Element’s Attributes
# The get() method for Tag objects makes it simple to access attribute values from an element. 
# The method is passed a string of an attribute name and returns that attribute's value. 
>>> import bs4
>>> soup = bs4.BeautifulSoup(open('example.html'))
>>> spanElem = soup.select('span')[0]
>>> str(spanElem)
'<span id="author">Al Sweigart</span>'
>>> spanElem.get('id')
'author'
>>> spanElem.get('some_nonexistent_addr') == None
True
>>> spanElem.attrs
{'id': 'author'}
# Here we use select() to find any <span> elements and then store the first matched element in spanElem. 
# Passing the attribute name 'id' to get() returns the attribute’s value, 'author'.


