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

# create a subclass and override the handler methods
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
                if "name" in d and d["name"] == "description":
                    print "Description = " , d["content"]

                if "name" in d and d["name"] == "keywords":
                    print "keywords = " , d["content"]

                if "name" in d and d["name"] == "title":
                    print "Title = " , d["content"]

                if "name" in d and d["name"].find("image") != -1:
                    print "Image = " , d["content"]

                if attrsArr[0][0] == "name" and attrsArr[0][1] == "description":
                    print "Description = " +  attrsArr[1][1]
                    metaDescri = attrsArr[1][1]

                if attrsArr[0][0] == "name" and attrsArr[0][1] == "thumbnail":
                    print "Thumbnail = " +  attrsArr[1][1]
                    metaImg = attrsArr[1][1]

                if attrsArr[0][0] == "property" and attrsArr[0][1] == "og:title":
                    # attrsArr[0][1].find("title") != -1
                    print "Title = " +  attrsArr[1][1]
                    metaTitle = attrsArr[1][1]

                if attrsArr[0][0] == "property" and attrsArr[0][1] == "og:description":
                    print "Description = "
                    if type(attrsArr[1][1]) is StringType:
                        print "Description = " + attrsArr[1][1]
                        metaDescri = attrsArr[1][1]
                    if type(attrsArr[1][1]) is UnicodeType:
                        descri = unicodedata.normalize('NFKD', attrsArr[1][1]).encode('utf-8','ignore')
                        print "Description = " + descri
                        metaDescri = descri

                if attrsArr[0][0] == "property" and attrsArr[0][1] == "og:image":
                    print "Image = " +  attrsArr[1][1]
                    metaImg.append(attrsArr[1][1])

                if attrsArr[0][0] == "property" and attrsArr[0][1] == "og:updated_time":
                    if type(attrsArr[1][1]) is StringType:
                        print "Updated Time = " + attrsArr[1][1]
                        metaTime = attrsArr[1][1]
                    if type(attrsArr[1][1]) is UnicodeType:
                        time = unicodedata.normalize('NFKD', attrsArr[1][1]).encode('ascii','ignore')
                        print "Updated Time = " + time
                        metaTime = time


    def handle_data(self, data):
        None

# site = 'http://www.wired.com/2014/10/cheating-video-poker/'
# site = "https://www.cryptocoinsnews.com/extropian-roots-bitcoin/"
# site = "http://time.com/3477903/2-japanese-1-american-win-nobel-prize-in-physics/"
# site = "http://www.nytimes.com/2005/01/12/business/worldbusiness/12light.html?_r=2&"
# site = "http://blog.thegrandlocus.com/2014/10/a-flurry-of-copycats-on-pubmed"
# site = "http://www.javascriptbattle.com"
# site = "http://virtjs.com"
# site = "http://www.mactech.com/articles/mactech/Vol.25/25.07/2507RoadtoCode-BradCoxInterview/index.html"
# site = "http://britishlibrary.typepad.co.uk/collectioncare/2014/10/800-year-old-magna-carta-manuscript-reveals-its-secrets.html"
# site = "http://vis.berkeley.edu/videodigests/view/Lecture-1-How-to-Start-a-Startup-FuX-7RX"
# site = "http://www.theverge.com/2014/10/7/6882427/king-of-keys"
# site = "http://www.newyorker.com/magazine/2013/03/11/up-all-night-2?currentPage=all"
# site = "http://blogs.wsj.com/economics/2014/10/07/sat-scores-and-income-inequality-how-wealthier-kids-rank-higher/?mg=blogs-wsj&url=http%253A%252F%252Fblogs.wsj.com%252Feconomics%252F2014%252F10%252F07%252Fsat-scores-and-income-inequality-how-wealthier-kids-rank-higher"
# site = "http://techcrunch.com/2014/10/07/san-francisco-airbnb/"
# site = "https://www.loggly.com/blog/what-we-learned-about-scaling-with-apache-storm/"
# site = "http://www.livemint.com/Industry/TM8tDvrv3OfeYjeXkEPXZI/Flipkart-hits-100-million-sales-target-in-10-hours.html"
# site = "http://www.computerworld.com/article/2692372/former-infosys-recruiter-says-he-was-told-not-to-hire-us-workers.html"
# site = "http://www.iflscience.com/chemistry/Nobel-Prize-in-Chemistry-Awarded-to-Scientists-for-Microscope-Breakthrough"
site = "www.bloomberg.com/news/2014-10-06/gt-advanced-technologies-files-for-bankruptcy-in-new-hampshire.html"

# bashCommand = "wget -O news.html " + site
# process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)

time.sleep(1)

# matchSite = site.split("/")

# try:
#     matchSite[2] = matchSite[2].replace("www.","")
# except:
#     matchSite[2] = matchSite[2]

# print "Matched site = " + matchSite[2]

###########################################################################################################
parser = MyHTMLParser("none")
f = open("news.html",'r')
data = f.read()
decoded = data
decoded1 = decoded.replace("\xe2","")
decoded2 = decoded1.replace("0xc2","")
decoded3 = decoded2.replace("\xa0","")
decoded3 = decoded3.replace("\x80","")
decoded3 = decoded3.replace("\x99","")
# decoded4 = decoded3.decode("utf-8",'ignore')

decoded5 = decoded3.replace("&","")

# decoded2 = unicodedata.normalize('NFKD', decoded2).encode('ascii','ignore')

parser.feed(decoded5)

# print descri

