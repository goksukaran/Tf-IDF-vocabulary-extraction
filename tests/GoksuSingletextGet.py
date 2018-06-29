'''
Created on 6 Jun 2018

@author: goksukara
'''
import wikipedia

import bs4
import urllib.request

webpage=str(urllib.request.urlopen("https://en.wikipedia.org/wiki/Building_automation").read())
soup = bs4.BeautifulSoup(webpage)

print(soup.get_text())
 
ny = wikipedia.page("Building Automation")
print(ny.section("Automation system"))
#print (wikipedia.summary("Wikipedia"))
