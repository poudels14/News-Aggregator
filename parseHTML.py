from HTMLParser import HTMLParser
import urllib
import re


gotSite = False
gotTitle = False
counter = 0
href = ""
tmphref = ""
title = ""
site = ""
time = ""
JSON = {}
jsonC = 0

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):


    def handle_starttag(self, tag, attrs):
    	global tmphref
    	global href
    	global title
    	global site
    	global time

	if tag == 'td':
		# print "td = " , attrs, " ; " , len(attrs)
		self.parseTd(attrs)
	elif tag == 'a':
		# print "attrs = ", attrs
		if attrs[0][0] == 'href':
			# print "Href = ", attrs[0][1]
			tmphref = attrs[0][1]

    def handle_data(self, data):
    	global gotSite
    	global gotTitle
    	global counter
    	global tmphref
    	global href
    	global title
    	global site
    	global time
    	global JSON
    	global jsonC

    	# print "Encountered some data  :", data

    	if counter == 1:
    		if tmphref[:4] == "http":
    			# print "Href = ", tmphref
    			href = tmphref
    			title = data
    			# print "Title = ", data
    			gotTitle = True
    	elif counter == 2 and gotTitle:
    		gotTitle = False
    		site = data[2:-2]
    		# print "Site = ", data[2:-2]
    		gotSite = True
    	elif counter == 9  and gotSite:
    		time = data[0:-2]
    		# print "Time = ",time[1:-2]
    		# print title
    		# print site[1:-1]
    		# print href
    		# json = href
    		json = "{title : \"" + title.replace('\"', '\'') + "\", site: \"" + site[0:-1].encode('utf-8') + "\", href: \"" + href.encode('utf-8') + "\", time: \"" + time[1:-2].encode('utf-8') + "\"}"
    		# print json
    		JSON[jsonC] = json
    		# json = ""
    		jsonC = jsonC + 1
    		# print "-----------------------------------------------------------------"
    		gotSite = False

    	counter = counter + 1

    def parseTd(arr1, arr2):
    	global counter
    	
    	if len(arr2) > 0:
    		if arr2[0][0] == "class" and arr2[0][1] == "title":
    			counter = 1
    		elif arr2[0][0] == "class" and arr2[0][1] == "subtext":
    			counter = 6


parser = MyHTMLParser()

# pageNum = 10
# site = 'HackerNews/HTML_NEWS/News/page'+str(pageNum)+'.html'
# f = open(site,'r')
# data = f.read()
# parser.feed(data)


# with open(site) as fileN:
# 	for x in fileN.readlines():
# 		# text = x.decode('utf-8').strip()
# 		# print x
# 		parser.feed(x)

# # print JSON
# fileName = 'HackerNews/JSON_NEWS/page'+str(pageNum)+'.js'
# writeF = open(fileName,'w')
# # writeF.write("Hehahahahah")
# writeF.write("news"+str(pageNum)+" = [\n")
# for x in JSON:
# 	print JSON[x]
# 	writeF.write("\t" + JSON[x] + ", \n")
# 	print "--------------------------------------------------------------------"



pageTotal = 33
for x in range(1,pageTotal):
	print "Page num = "+str(x)
	pageNum = x
	site = 'HackerNews/HTML_NEWS/Oct_7/page'+str(pageNum)+'.html'
	f = open(site,'r')
	data = f.read()
	parser.feed(data)

	# print JSON
	fileName = 'HackerNews/JSON_NEWS/Oct_7/page'+str(pageNum)+'.js'
	writeF = open(fileName,'w')
	writeF.write("news"+str(pageNum)+" = [\n")
	for x in JSON:
		# print JSON[x]
		writeF.write("\t" + JSON[x] + ", \n")
		# print "--------------------------------------------------------------------"
	writeF.write("]")
	writeF.close()
	JSON = {}



