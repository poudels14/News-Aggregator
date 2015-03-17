from HTMLParser import HTMLParser
import urllib
import re
import subprocess
import time
from random import shuffle

criteria = {
    "washingtonpost.com" : {"tag" : ["article"], "class" : [False,]},
    "time.com" : {"tag" : ["section","p",], "class" : ["article-body","",]},
    "cryptocoinsnews.com" : {"tag" : ["section",], "class" : ["entry-content",]},
}


metTag = ""
metTagC = 0
metClassC = 0
metTagLen = 0

metDiv = False
gotDiv = False
metImg = False
imgSrc = ""
metHeight = False
metWidth = False
descri = ""

contentClasses = {
    "entry","story",
}

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):


    def handle_starttag(self, tag, attrs):
    	global metDiv
        global metImg
        global imgSrc
        global metHeight
        global metWidth

        global metTag
        global metTagC
        global metClassC

        classes = criteria[self.matchedSite]["class"]
        tags = criteria[self.matchedSite]["tag"]


        # print self.matchedSite

        # print criteria[self.matchedSite]["class"], " --- " , 
        # try:
        #     if attrs[0][1] == "article-body":
        #         print "Artucla asdasd asd asd asd"
        # except:
        #     None

        # print tags
        # print classes[1] == ""

        if (tag in tags):
            print "tag found"
            metTagC = metTagC + 1
            i = tags.index(tag)
            if len(attrs) > 0:
                if attrs[0][0] == "class" and (attrs[0][1] == classes[i] or classes[i] == ""):
                    # metTag = True
                    metTagC = metTagC + 1
                    metClassC = metClassC + 1
                    print "class found " + classes[i]
                else:
                    print "Loop hole found"
            else:
                metTag = True
                metTagC = metTagC + 1
                metClassC = metClassC + 1
                # print "found without class"

        # if tag == "img":
        #     metImg = True

        # if tag == "section":
        #     metDiv = True


        # if len(attrs) > 0:
        #     # print attrs
        #     for x in attrs:
        #         # print x , "......"

        #         if metImg and x[0] == "src":
        #             imgSrc = x[1]
        #             # print "src = " + x[1]
        #             # print attrs
        #         if x[0] == "class" or x[0] != "":
        #             for y in contentClasses:
        #                 try:
        #                     z = str(x[1])
        #                 except:
        #                     z = x[1].replace('\\', '/')
        #                 if x[1] == y or z.find(y) != -1:
        #                     # print "Match found = " + x[1]
        #                     metDiv = True
        #         if x[0] == "height" and x[1].isdigit() and int(x[1]) > 200 and metImg:
        #             metHeight = True
        #             if metWidth:
        #                 print "Image Found = " + imgSrc

        #         if x[0] == "width" and x[1].isdigit() and int(x[1]) > 400 and metImg:
        #             metWidth = True
        #             if metHeight:
        #                 print "Image Found = " + imgSrc


    def handle_data(self, data):
    	global metDiv
        global gotDiv
        global descri
        global descriC
        global metTag
        global metTagC
    	# print "Encountered some data  :", data

        try:
            classLen = len(criteria[self.matchedSite]["class"])
        except:
            classLen = 0

        # print "tag Len = " + str(classLen) + " metTag = " + str(metClassC)
        if metClassC == classLen:
            # print data
            if len(descri) < 200:
                descri = descri + data

    	# if metDiv and (not gotDiv):
     #        if len(data) > 120 and (data.find("<") == -1 and data.find(">") == -1 and data.find("!=") == -1 and data.find("}") == -1 and data.find("{") == -1):
     #            # print "Encountered some data  : length = " + str(len(data)) + " data = " + data
     #            metDiv = False
     #            descri[descriC] = data
     #            descriC = descriC + 1
     #            # gotDiv = True


# # pageNum = 10
site = 'https://www.cryptocoinsnews.com/extropian-roots-bitcoin/'
bashCommand = "wget -O news.html " + site
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)

time.sleep(1)

matchSite = site.split("/")
try:
    matchSite[2] = matchSite[2].replace("www.","")
except:
    matchSite[2] = matchSite[2]

print "Matched site = " + matchSite[2]

###########################################################################################################
parser = MyHTMLParser(matchSite[2])
f = open("news.html",'r')
data = f.read()
parser.feed(data)

print descri

