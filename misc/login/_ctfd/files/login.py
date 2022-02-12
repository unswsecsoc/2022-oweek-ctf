#!/usr/bin/python3
from requests import get
from lxml.html import fromstring

print("Welcome to the web title fetcher!")
print("Please go easy on our site, no dirbusting/bruteforcing is required.")
print("What site would you like me to fetch? (BETA Version, unswsecurity.com sites only)")

url = input("> ")
if url.startswith("unswsecurity.com"):
    # get the html content of the given url
    site_content = fromstring(get('http://' + url).content)
    site_title = site_content.findtext('.//title')
    print("The title of your site is: " + site_title)

    # check for the magic word 'xkcd'
    if 'xkcd' in site_title:
        print("OWEEK{now try this on the server to get the real flag!}")
else:
    print("Sorry, we don't support fetching other sites yet.")
