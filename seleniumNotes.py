# Starting a Selenium-Controlled Browser
>>> from selenium import webdriver
>>> browser = webdriver.Chrome()
>>> type(browser)
<class 'selenium.webdriver.firefox.webdriver.WebDriver'>
>>> browser.get('http://inventwithpython.com')
# Opens up page to inventwithpython.com

''' The find_element_* methods return a single WebElement object, representing the first element on the 
page that matches your query. The find_elements_* methods return a list of WebElement_* objects for every 
matching element on the page.
Web Element Objects:

browser.find_element_by_class_name(name)
browser.find_elements_by_class_name(name)					Elements that use the CSS class name

 browser.find_element_by_css_selector(selector)
browser.find_elements_by_css_selector(selector)				Elements that match the CSS selector

 browser.find_element_by_id(id)
browser.find_elements_by_id(id)								Elements with a matching id attribute value

 browser.find_element_by_link_text(text)
browser.find_elements_by_link_text(text)					<a> elements that completely match the text provided

 browser.find_element_by_partial_link_text(text)
browser.find_elements_by_partial_link_text(text)			<a> elements that contain the text provided

 browser.find_element_by_name(name)
browser.find_elements_by_name(name)							Elements with a matching name attribute value

 browser.find_element_by_tag_name(name)
browser.find_elements_by_tag_name(name)						Elements with a matching tag name (case insensitive; an <a> element is matched by 'a' and 'A')


Selenium will raise a NoSuchElement exception if an element is not found on the page, you can use try and except to avoid this error.


Once we have to Web Element Object, we can call the methods in the following table, or read more about its 
attributes:

tag_name                  The tag name, such as 'a' for an <a> element

get_attribute(name)       The value for the element’s name attribute

text                      The text within the element, such as 'hello' in <span>hello</span>

clear()                   For text field or text area elements, clears the text typed into it

is_displayed()            Returns True if the element is visible; otherwise returns False

is_enabled()              For input elements, returns True if the element is enabled; otherwise returns False

is_selected()             For checkbox or radio button elements, returns True if the element is selected; otherwise returns False

location                  A dictionary with keys 'x' and 'y' for the position of the element in the page
'''


from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')
try:
    elem = browser.find_element_by_class_name('bookcover')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')


# Clicking The Page With click()
>>> from selenium import webdriver
>>> browser = webdriver.Firefox()
>>> browser.get('http://inventwithpython.com')
>>> linkElem = browser.find_element_by_link_text('Read It Online')
>>> type(linkElem)
<class 'selenium.webdriver.remote.webelement.WebElement'>
>>> linkElem.click() # follows the "Read It Online" link
'''This opens Firefox to http://inventwithpython.com/, gets the WebElement object for the <a> element 
with the text Read It Online, and then simulates clicking that <a> element. It’s just like if you clicked 
the link yourself; the browser then follows that link.'''


# Filling Out And Submitting Forms
'''Sending keystrokes to text fields on a web page is a matter of finding the <input> or <textarea> 
element for that text field and then calling the send_keys() method'''
>>> from selenium import webdriver
>>> browser = webdriver.Firefox()
>>> browser.get('https://mail.yahoo.com')
>>> emailElem = browser.find_element_by_id('login-username')
>>> emailElem.send_keys('not_my_real_email')
>>> passwordElem = browser.find_element_by_id('login-passwd')
>>> passwordElem.send_keys('12345')
>>> passwordElem.submit()
'''(You can always use the browser’s inspector to verify the id.) Calling the submit() method on any element 
ill have the same result as clicking the Submit button for the form that element is in. (You could have just 
s easily called emailElem.submit(), and the code would have done the same thing.)'''


# Sending Special Keys
from selenium.webdriver.common.keys import Keys
'''Commonly Used Variables in the selenium.webdriver.common.keys
Keys.DOWN, Keys.UP, Keys.LEFT, Keys.RIGHT		The keyboard arrow keys

Keys.ENTER, Keys.RETURN                         The ENTER and RETURN keys

Keys.HOME, Keys.END, Keys.PAGE_DOWN, Keys.PAGE_UP          The home, end, pagedown, and pageup keys

Keys.ESCAPE, Keys.BACK_SPACE, Keys.DELETE                The ESC, BACKSPACE, and DELETE keys

Keys.F1, Keys.F2,..., Keys.F12                       The F1 to F12 keys at the top of the keyboard

Keys.TAB                                             The TAB key


For example, if the cursor is not currently in a text field, pressing the HOME and END keys will scroll 
the browser to the top and bottom of the page, respectively. Enter the following into the interactive 
shell, and notice how the send_keys() calls scroll the page:'''
>>> from selenium import webdriver
>>> from selenium.webdriver.common.keys import Keys
>>> browser = webdriver.Firefox()
>>> browser.get('http://nostarch.com')
>>> htmlElem = browser.find_element_by_tag_name('html') # Send keys to the general webpage
>>> htmlElem.send_keys(Keys.END)     # scrolls to bottom
>>> htmlElem.send_keys(Keys.HOME)    # scrolls to top
'''The <html> tag is the base tag in HTML files: The full content of the HTML file is enclosed within the 
<html> and </html> tags. Calling browser.find_element_by_tag_name('html') is a good place to send keys to 
the general web page. This would be useful if, for example, new content is loaded once you’ve scrolled to 
the bottom of the page.'''


# Clicking Browser Buttons
browser.back() Clicks the Back button
browser.forward() Clicks the Forward button
browser.refresh() Clicks the Refresh/Reload button
browser.quit() Clicks the Close Windows button

'''
More Information on Selenium
Selenium can do much more beyond the functions described here. It can modify your browser’s cookies, 
take screenshots of web pages, and run custom JavaScript. To learn more about these features, you can 
visit the Selenium documentation at http://selenium-python.readthedocs.org/.



Practice Projects
For practice, write programs to do the following tasks.
Command Line Emailer
Write a program that takes an email address and string of text on the command line and then, using Selenium, 
logs into your email account and sends an email of the string to the provided address. (You might want to 
set up a separate email account for this program.)
This would be a nice way to add a notification feature to your programs. You could also write a similar 
program to send messages from a Facebook or Twitter account.

Image Site Downloader
Write a program that goes to a photo-sharing site like Flickr or Imgur, searches for a category of photos, 
and then downloads all the resulting images. You could write a program that works with any photo site that 
has a search feature.

2048
2048 is a simple game where you combine tiles by sliding them up, down, left, or right with the arrow keys. 
You can actually get a fairly high score by repeatedly sliding in an up, right, down, and left pattern over 
and over again. Write a program that will open the game at https://gabrielecirulli.github.io/2048/ and keep 
sending up, right, down, and left keystrokes to automatically play the game.

Link Verification
Write a program that, given the URL of a web page, will attempt to download every linked page on the page. 
The program should flag any pages that have a 404 “Not Found” status code and print them out as broken links.

'''