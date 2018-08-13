'''
Created on 6 Jun 2018

@author: goksukara
'''
import wikipedia
 
ny = wikipedia.page("Building Automation")
#print(ny.content)
#print (wikipedia.summary("Wikipedia"))

file = open("testfile.txt", "w")
print(ny.content)

#file.write(str(ny.s))
file.write("This is a test") 

file.close()