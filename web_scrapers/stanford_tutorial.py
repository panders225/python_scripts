# -*- coding: utf-8 -*-
"""
Created on Sat Mar 04 13:15:23 2017

@author: Philip
"""

# Testing the beautifulsoup web scraper, following the tutorial at 
# http://web.stanford.edu/~zlotnick/TextAsData/Web_Scraping_with_Beautiful_Soup.html

from bs4 import BeautifulSoup
import urllib2

headers = { 'User-Agent' : 'Mozilla/5.0' }
req = urllib2.Request( 'http://www.aflcio.org/Legislation-and-Politics/Legislative-Alerts', None, headers )
r = urllib2.urlopen(req).read()

soup = BeautifulSoup(r)
print type(soup) # this should be a beautifulsoup object

print soup.prettify()[0:1000]
print soup.prettify()[28700:30500]


from IPython.display import HTML
HTML('<iframe src=http://www.aflcio.org/Legislation-and-Politics/Legislative-Alerts width=700 height=500></iframe>')

letters = soup.find_all("div", class_="ec_statements")

print type(letters)

letters[0]
letters[0].a.get_text()
lobbying = {}
for element in letters:
    lobbying[element.a.get_text()] = {}
    
    
letters[0].a["href"]

prefix = "www.aflcio.org"

for element in letters:
    lobbying[element.a.get_text()]["link"] = prefix + element.a["href"]
    
letters[0].find(id="legalert_date") 

for element in letters:
    date = element.find(id="legalert_date").get_text()
    lobbying[element.a.get_text()]["date"] = date
    
for item in lobbying.keys():
    print item + ": " + "\n\t" + "link: " + lobbying[item]["link"] + "\n\t" + "date: " + lobbying[item]["date"] + "\n\n" 