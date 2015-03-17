import pycurl
from StringIO import StringIO
from HTMLParser import HTMLParser
import urllib
import re
import subprocess
import time
import unicodedata
from types import *

metaImg = []
metaTitle = ""
metaDescri = ""
metaTime = ""

### Title ###
title = ""
ogTitle = ""
twitterTitle = ""


### Description ###
descri = ""
ogDescri = ""
twitterDescri = ""

### Domain ###
domain = ""

### Date ###
pubDate= ""
lastMod = ""

### href ###
href = ""

### Image ###
image = ""
ogImage = ""
thumbnail = ""
ogThumbnail = ""
twitterImage = ""

### category ###
category = ""

###keywords###
keywords = ""


#################################################################

class MyHTMLParser(HTMLParser):


    def handle_starttag(self, tag, attrs):
        global metaImg
        global metaTitle
        global metaDescri
        global metaTime

        if tag == "meta":
            attrsArr = list(attrs)
            # print attrsArr
            if len(attrsArr) > 1:
                d = dict(attrs)

                #######################################################
                if "name" in d and d["name"] == "title":
                	x = d["content"].encode('utf-8')
                	print "title = " + x
                	title = x 
                	return

                if "name" in d and d["name"] == "og:title":
                	x = d["content"].encode('utf-8')
                	print "og:title = " + x
                	ogTitle = x
                	return

                if "name" in d and d["name"] == "twitter:title":
                	x = d["content"].encode('utf-8')
                	print "twitter:title = " + x
                	twitterTitle = x
                	return

                #######################################################

                if "name" in d and d["name"] == "description":
                	x = d["content"].encode('utf-8')
                	print "Description = " + x
                	descri = x
                	return

                if "name" in d and d["name"] == "og:description":
                	x = d["content"].encode('utf-8')
                	print "og:description = " + x
                	ogDescri = x
                	return

                if "name" in d and d["name"] == "twitter:description":
                	x = d["content"].encode('utf-8')
                	print "twitter:description = " + x
                	twitterDescri = x
                	return

                #######################################################

                if "name" in d and d["name"] == "pubdate":
                	x = d["content"].encode('utf-8')
                	print "pubdate = " , x
                	pubdate = x
                	return

                if "name" in d and d["name"] == "lastmod":
                	x = d["content"].encode('utf-8')
                	print "lastmod = " , x
                	lastmod = x
                	return

                #######################################################

                if "name" in d and d["name"] == "image":
                	x = d["content"].encode('utf-8')
                	print "image = " , x
                	image = x
                	return

                if "name" in d and d["name"] == "og:image":
                	x = d["content"].encode('utf-8')
                	print "og:image = " , x
                	ogImage = x
                	return

                if "name" in d and d["name"] == "twitter:image":
                	x = d["content"].encode('utf-8')
                	print "twitter:image = " , x
                	twitterImage = x
                	return

                if "name" in d and d["name"] == "thumbnail":
                	x = d["content"].encode('utf-8')
                	print "thumbnail = " , x
                	thumbnail = x
                	return

                if "name" in d and d["name"] == "og:thumbnail":
                	x = d["content"].encode('utf-8')
                	print "og:thumbnail = " , x
                	ogThumbnail = x
                	return

                #######################################################

                if "name" in d and d["name"] == "category":
                	x = d["content"].encode('utf-8')
                	print "category = " , x
                	category = x
                	return

                #######################################################

                if "name" in d and d["name"] == "keywords":
                	x = d["content"].encode('utf-8')
                	print "keywords = " , x
                	keywords = x
                	return

                #######################################################



                # if "name" in d and d["name"] == "keywords":
                #     print "keywords = " , d["content"].encode('utf-8')

                # if "name" in d and d["name"] == "title":
                #     print "Title = " , d["content"].encode('utf-8')

                # if "name" in d and d["name"].find("image") != -1:
                #     print "Image = " , d["content"].encode('utf-8')

                # if "name" in d and d["name"].find("image") != -1:
                #     print "Image = " , d["content"].encode('utf-8')

                # if attrsArr[0][0] == "name" and attrsArr[0][1] == "thumbnail":
                #     print "Thumbnail = " +  attrsArr[1][1].encode('utf-8')
                #     metaImg = attrsArr[1][1]

                # if attrsArr[0][0] == "property" and attrsArr[0][1] == "og:title":
                #     # attrsArr[0][1].find("title") != -1
                #     print "Title = " +  attrsArr[1][1].encode('utf-8')
                #     metaTitle = attrsArr[1][1]

                # if attrsArr[0][0] == "property" and attrsArr[0][1] == "og:description":
                #     print "Description = "
                #     if type(attrsArr[1][1]) is StringType:
                #         print "Description = " + attrsArr[1][1].encode('utf-8')
                #         metaDescri = attrsArr[1][1]
                #     if type(attrsArr[1][1]) is UnicodeType:
                #         # descri = unicodedata.normalize('NFKD', attrsArr[1][1]).encode('utf-8','ignore')
                #         descri = attrsArr[1][1]
                #         print "Description = " + descri.encode('utf-8')
                #         metaDescri = descri

                # if attrsArr[0][0] == "property" and attrsArr[0][1] == "og:image":
                #     print "Image = " +  attrsArr[1][1].encode('utf-8')
                #     metaImg.append(attrsArr[1][1])

                # if attrsArr[0][0] == "property" and attrsArr[0][1] == "og:updated_time":
                #     if type(attrsArr[1][1]) is StringType:
                #         print "Updated Time = " + attrsArr[1][1].encode('utf-8')
                #         metaTime = attrsArr[1][1]
                #     if type(attrsArr[1][1]) is UnicodeType:
                #         time = unicodedata.normalize('NFKD', attrsArr[1][1]).encode('ascii','ignore')
                #         print "Updated Time = " + time.encode('utf-8')
                #         metaTime = time


    def handle_data(self, data):
        None

site = {}
site[0] = 'http://www.wired.com/2014/10/cheating-video-poker/'
site[1] = "https://www.cryptocoinsnews.com/extropian-roots-bitcoin/"
site[2] = "http://time.com/3477903/2-japanese-1-american-win-nobel-prize-in-physics/"
site[3] = "http://www.nytimes.com/2005/01/12/business/worldbusiness/12light.html?_r=2&"
site[4] = "http://blog.thegrandlocus.com/2014/10/a-flurry-of-copycats-on-pubmed"
site[5] = "http://www.javascriptbattle.com"
site[6] = "http://virtjs.com"
site[7] = "http://www.mactech.com/articles/mactech/Vol.25/25.07/2507RoadtoCode-BradCoxInterview/index.html"
site[8] = "http://britishlibrary.typepad.co.uk/collectioncare/2014/10/800-year-old-magna-carta-manuscript-reveals-its-secrets.html"
site[9] = "http://vis.berkeley.edu/videodigests/view/Lecture-1-How-to-Start-a-Startup-FuX-7RX"
site[10] = "http://www.theverge.com/2014/10/7/6882427/king-of-keys"
site[11] = "http://www.newyorker.com/magazine/2013/03/11/up-all-night-2?currentPage=all"
site[12] = "http://blogs.wsj.com/economics/2014/10/07/sat-scores-and-income-inequality-how-wealthier-kids-rank-higher/?mg=blogs-wsj&url=http%253A%252F%252Fblogs.wsj.com%252Feconomics%252F2014%252F10%252F07%252Fsat-scores-and-income-inequality-how-wealthier-kids-rank-higher"
site[13] = "http://techcrunch.com/2014/10/07/san-francisco-airbnb/"
site[14] = "https://www.loggly.com/blog/what-we-learned-about-scaling-with-apache-storm/"
site[15] = "http://www.livemint.com/Industry/TM8tDvrv3OfeYjeXkEPXZI/Flipkart-hits-100-million-sales-target-in-10-hours.html"
site[16] = "http://www.computerworld.com/article/2692372/former-infosys-recruiter-says-he-was-told-not-to-hire-us-workers.html"
site[17] = "http://www.iflscience.com/chemistry/Nobel-Prize-in-Chemistry-Awarded-to-Scientists-for-Microscope-Breakthrough"
site[18] = "www.bloomberg.com/news/2014-10-06/gt-advanced-technologies-files-for-bankruptcy-in-new-hampshire.html"


for x in site:
	print x
	buffer = StringIO()
	c = pycurl.Curl()
	c.setopt(c.URL, site[x])
	c.setopt(c.WRITEDATA, buffer)
	c.perform()
	c.close()

	body = buffer.getvalue()

	parser = MyHTMLParser("none")
	# data = body.replace(u'\u014c\u0106\u014d','-')
	# data = body
	data = body.decode('unicode_escape')
	parser.feed(data)
#####################################################################


# buffer = StringIO()
# c = pycurl.Curl()
# c.setopt(c.URL, site)
# c.setopt(c.WRITEDATA, buffer)
# c.perform()
# c.close()

# body = buffer.getvalue()
# # Body is a string in some encoding.
# # In Python 2, we can print it without knowing what the encoding is.
# # print(body)


# parser = MyHTMLParser("none")
# # f = open("news.html",'r')
# # data = f.read()
# # decoded4 = body.encode("utf-8")
# # decoded5 = decoded4.replace("&","")

# parser.feed(body)

