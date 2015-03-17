import pycurl
from StringIO import StringIO
from HTMLParser import HTMLParser
import urllib
import re
import subprocess
import time
import unicodedata
import pymongo
from pymongo import MongoClient
from types import *

#################################################################
client = MongoClient()
db = client.bloomberg
metaData = db.metaData
linkBuffer = db.linkBuffer

mineMeta = True

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
pubdate= ""
lastmod = ""

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

# User-agent: *
# User-agent: Mediapartners-Google*
# Disallow: 
# Disallow: 
# Disallow: 

# User-agent: Spinn3r
# Disallow: /podcasts/
# Disallow: /feed/podcast/
# Disallow: /bb/avfile/

disallow = {"/about/careers", "/about/careers/", "/offlinemessage/", "/apps/fbk",  }

#################################################################


class MyHTMLParser(HTMLParser):
    print "Please wait while link is mined"

    def handle_starttag(self, tag, attrs):
        global mineMeta
        global linkBuffer
        global title, ogTitle, twitterTitle, descri, ogDescri, twitterDescri, domain, pubdate, lastmod, href
        global image, ogImage, thumbnail, ogThumbnail, twitterImage, category, keywords

        if tag == "a":
            # print attrs
            d = dict(attrs)
            try:
                if d["href"][-5:] == ".html" and d["href"][0:6] == "/news/":
                    x = "http://www.bloomberg.com" + d["href"]
                    # print x
                    linkBuffer.insert({"link":x})
            except:
                None

        if mineMeta and tag == "meta":
            attrsArr = list(attrs)
            # print attrsArr
            if len(attrsArr) > 1:
                d = dict(attrs)

                #######################################################
                try:
                    if d["name"] == "title":
                        x = d["content"]
                        # print "title = " + x
                        title = x 
                        return

                    if "name" in d and d["name"] == "og:title":
                        x = d["content"]
                	    # print "og:title = " + x
                        ogTitle = x
                        return

                    if "name" in d and d["name"] == "twitter:title":
                        x = d["content"]
                        # print "twitter:title = " + x
                        twitterTitle = x
                        return

                    #######################################################

                    if "name" in d and d["name"] == "description":
                        x = d["content"]
                        # print "Description = " + x
                        descri = x
                        return

                    if "name" in d and d["name"] == "og:description":
                        x = d["content"]
                        # print "og:description = " + x
                        ogDescri = x
                        return

                    if "name" in d and d["name"] == "twitter:description":
                        x = d["content"]
                        # print "twitter:description = " + x
                        twitterDescri = x
                        return

                    #######################################################

                    if "name" in d and d["name"] == "pubdate":
                        x = d["content"]
                        # print "pubdate = " , x
                        pubdate = x
                        return

                    if "name" in d and d["name"] == "lastmod":
                        x = d["content"]
                        # print "lastmod = " , x
                        lastmod = x
                        return

                    #######################################################

                    if "name" in d and d["name"] == "image":
                        x = d["content"]
                        # print "image = " , x
                        image = x
                        return

                    if "name" in d and d["name"] == "og:image":
                        x = d["content"]
                        # print "og:image = " , x
                        ogImage = x
                        return

                    if "name" in d and d["name"] == "twitter:image":
                        x = d["content"]
                        # print "twitter:image = " , x
                        twitterImage = x
                        return

                    if "name" in d and d["name"] == "thumbnail":
                        x = d["content"]
                        # print "thumbnail = " , x
                        thumbnail = x
                        return

                    if "name" in d and d["name"] == "og:thumbnail":
                        x = d["content"]
                        # print "og:thumbnail = " , x
                        ogThumbnail = x
                        return

                    #######################################################

                    if "name" in d and d["name"] == "category":
                        x = d["content"]
                        # print "category = " , x
                        category = x
                        return

                    #######################################################

                    if "name" in d and d["name"] == "keywords":
                        x = d["content"]
                        # print "keywords = " , x
                        keywords = x
                        return
                except:
                    None

        #######################################################



        def handle_data(self, data):
            None

site = {}
# site[0] = "http://www.bloomberg.com/archive/news/2014-10-09/"
site[0] = "http://www.bloomberg.com/archive/news/2014-10-08/"
# site[0] = "http://www.bloomberg.com/news/2014-10-01/malaysia-raises-fuel-prices-as-najib-seeks-to-narrow-deficit.html"


def mine_single_site(site):
        # print site[:1]
    site = site.split("#")[0]
    site = site.split("?")[0]
    
    if site[:1] == "/":
        site = "http://bloomberg.com" + site

    if site[:1] == "#":
        return
    if site[:5] != "http:" and site[:5] != "https":
        print site[:5]
        return
    if site.find("2014") == -1:
        mineMeta = False

    if site[7:21] != "bloomberg.com" and site[11:24] != "bloomberg.com"  and site[12:25] != "bloomberg.com":
        return

    global mineMeta
    global linkBuffer
    global title, ogTitle, twitterTitle, descri, ogDescri, twitterDescri, domain, pubdate, lastmod, href
    global image, ogImage, thumbnail, ogThumbnail, twitterImage, category, keywords

    if site[-5:] != ".html":
        mineMeta = False
        print site[-5:]

    if metaData.find_one({'link' : site}):
        print "Already Mined"
        return

    buffer = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, site)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()

    body = buffer.getvalue()

    parser = MyHTMLParser()
    # data = body.replace(u'\u014c\u0106\u014d','-')
    # data = body
    data = body.decode('utf-8')
    parser.feed(data)

    # json = "{\"site\" : \"" + site[x] + "\","

    json = {}
    json["link"] = site

    # print "site = " + site[x][-4:]
    for y in disallow:
        if site.find(y) != -1:
            print "This link forbidden"
            break



    if len(ogTitle) > 0:
        json["title"] =  ogTitle
        # print ogTitle
    elif len(twitterTitle) > 0:
        json["title"] = twitterTitle
        # print twitterTitle
    elif len(title) > 0:
        json["title"] = title
        # print title
    #####################################################################
    if len(ogDescri)>0:
        json["descri"] = ogDescri
    elif len(twitterDescri) > 0:
        json["descri"] = twitterDescri
    elif len(descri) > 0:
        json["descri"] = descri
    #####################################################################
    if len(ogImage)>0:
        json["image"] = ogImage
    elif len(twitterImage) > 0:
        json["image"] = twitterImage
    elif len(ogThumbnail) > 0:
        json["image"] = ogThumbnail
    elif len(thumbnail) > 0:
        json["image"] = thumbnail
    elif len(image) > 0:
        json["image"] = image
    #####################################################################
    if len(category)>0:
        tmp = re.split(", |_", category.lower())
        json["category"] = list(set(tmp))
    #####################################################################
    if len(pubdate)>0:
        json["pubdate"] = pubdate
    #####################################################################
    if len(lastmod)>0:
        json["lastmod"] = lastmod
    #####################################################################
    if len(keywords)>0:
        tmp = re.split(",", keywords.lower())
        json["keywords"] = list(set(tmp))

    if mineMeta:
        dotComPlace = site.find(".com/news/")
        year = site[dotComPlace+10:dotComPlace+14]
        month = site[dotComPlace+15:dotComPlace+17]
        day = site[dotComPlace+18:dotComPlace+20]
        json["year"] = year
        json["month"] = month
        json["day"] = day
        print json
        metaData.insert(json)
        # mined_links.insert( {"link" : site } )
        print "Link Mined"

    # if len(linksToMine) > 0:
    #     print "Several link captured. # = " + len(linksToMine)

    clear_vars()



def clear_vars():
    global mineMeta
    global title, ogTitle, twitterTitle, descri, ogDescri, twitterDescri, domain, pubdate, lastmod, href
    global image, ogImage, thumbnail, ogThumbnail, twitterImage, category, keywords

    mineMeta = True

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
    #####################################################################
    return




for x in site:
    print site[x]
    mine_single_site(site[x])
    while True:
        # if linkBuffer.find_one({}).length() <= 0:
        #     break
        one_link = linkBuffer.find_one();
        if type(one_link) == NoneType:
            break
        linkBuffer.remove({"link":one_link["link"]});
        print "Mining link = " , one_link["link"]
        mine_single_site(one_link["link"])