#! python3
# This is from Automate the Boring Stuff by Al Sweigart.
# I used this to help me learn web scraping.

import webbrowser, sys, pyperclip
# Opens a webbrowser map to what you have copied on the clipboard,
# if no command line arguments, it assumes the address is copied to the clipboard
if len(sys.argv) > 1:
	# Get address from command line.
	address = ' '.join(sys.argv[1:]) # We don't want the program name in the string, so we chop it off with 1:
else:
	# Get address from clipboard
	address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)


''' OTHER IDEAS
Open all links on a page in separate browser tabs.

Open the browser to the URL for your local weather.

Open several social network sites that you regularly check.
'''
