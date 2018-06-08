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
#print(ny.section("Automation system"))
#print (wikipedia.summary("Wikipedia"))
ny.sections
[u'History', u'16th century', u'17th century', u'18th century, the American Revolution, and statehood', u'19th century', u'Immigration', u'September 11, 2001 attacks', u'Hurricane Sandy, 2012', u'Geography', u'Climate', u'Statescape', u'Regions', u'Adjacent geographic entities', u'State parks', u'National parks', u'Administrative divisions', u'Demographics', u'Population', u'Most populous counties', u'Major cities', u'Metropolitan areas', u'Racial and ancestral makeup', u'Languages', u'Religion', u'LGBT', u'Economy', u'Wall Street', u'Silicon Alley', u'Microelectronic hardware and photographic processing', u'Media and entertainment', u'Tourism', u'Exports', u'Education', u'Transportation', u'Government and politics', u'Government', u'Capital punishment', u'Federal representation', u'Politics', u'Sports', u'See also', u'References', u'Further reading', u'External links'] 