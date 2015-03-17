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
import functions
from bson.objectid import ObjectId
#################################################################
client = MongoClient()
db = client.reuters
linkBuffer = db.linkBuffer

newsDb = client.newsDb
metaData = newsDb.metaData
visitedLinks = client.visitedLinks.links

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
disallow = {}
refDomain = "reuters.com"
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
                    tsite = functions.remove_hash(d["href"])

                    tone_l = linkBuffer.find_one({'link' : tsite})
                    if not functions.verify_same_site(tsite, refDomain):
                        # print "not same domain"
                        None
                    elif visitedLinks.find_one({'link' : tsite}):
                        # print visitedLinks.find_one({'link' : tsite})
                        None
                        # print "Already Visited - not buffering"
                    elif tone_l:
                        # print "Already in buffer"
                        # print tone_l
                        None
                    else:
                        print "inserted in linkBuffer"
                        linkBuffer.insert({"link":d["href"]})
            except:
                None

        if mineMeta and tag == "meta":
            attrsArr = list(attrs)
            # print attrsArr
            if len(attrsArr) > 1:
                d = dict(attrs)

                #######################################################
                try:
                    # if d["property"] == ["og:type"] and d["content"] == "article":
                    #     mineMeta = True
                    if d["property"] == "title":
                        x = d["content"]
                        # print "title = " + x
                        title = x 
                        return

                    if d["property"] == "og:title":
                        x = d["content"]
                	    # print "og:title = " + x
                        ogTitle = x
                        return

                    if d["property"] == "twitter:title":
                        x = d["content"]
                        # print "twitter:title = " + x
                        twitterTitle = x
                        return

                    #######################################################

                    if d["property"] == "description":
                        x = d["content"]
                        # print "Description = " + x
                        descri = x
                        return

                    if d["property"] == "og:description":
                        x = d["content"]
                        # print "og:description = " + x
                        ogDescri = x
                        return

                    if d["property"] == "twitter:description":
                        x = d["content"]
                        # print "twitter:description = " + x
                        twitterDescri = x
                        return

                    #######################################################

                    if d["property"] == "image":
                        x = d["content"]
                        # print "image = " , x
                        image = x
                        return

                    if d["property"] == "og:image":
                        x = d["content"]
                        # print "og:image = " , x
                        ogImage = x
                        return

                    if d["property"] == "twitter:image":
                        x = d["content"]
                        # print "twitter:image = " , x
                        twitterImage = x
                        return

                    if d["property"] == "thumbnail":
                        x = d["content"]
                        # print "thumbnail = " , x
                        thumbnail = x
                        return

                    if d["property"] == "og:thumbnail":
                        x = d["content"]
                        # print "og:thumbnail = " , x
                        ogThumbnail = x
                        return

                    #######################################################

                    if d["property"] == "category":
                        x = d["content"]
                        # print "category = " , x
                        category = x
                        return

                    #######################################################

                    if d["property"] == "keywords":
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
site[0] = "http://www.reuters.com/article/2014/11/01/us-j-p-morgan-cybercrime-idUSKBN0IL2JM20141101"


def mine_single_site(site):
    site = functions.remove_hash(site)
    # site = site.split("?")[0]

    if site[:1] == "/":
        site = "http://" + refDomain + "/" + site

    if not functions.is_site_valid(site):
        print site
        return

    if not functions.verify_same_site(site, refDomain):
        return

    if site.find("2014") == -1:
        mineMeta = False
    if len(site.split("/")) < 7 and site.split("/")[3] != "article":
        mineMeta = False

    global mineMeta
    global linkBuffer
    global title, ogTitle, twitterTitle, descri, ogDescri, twitterDescri, domain, pubdate, lastmod, href
    global image, ogImage, thumbnail, ogThumbnail, twitterImage, category, keywords

    if metaData.find_one({'link' : site}):
        print "Already Mined"
        return

    if visitedLinks.find_one({'link' : site}):
        print "mine_single_site: Already Visited"
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
    visitedLinks.insert({"link": site})


    json = {}
    json["link"] = site

    # print "site = " + site[x][-4:]
    # for y in disallow:
    #     if site.find(y) != -1:
    #         print "This link forbidden"
    #         break



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
    if len(keywords)>0:
        tmp = re.split(",", keywords.lower())
        json["keywords"] = list(set(tmp))

    if mineMeta:
        try:
            json["domain"] = refDomain
            dotComPlace = site.find("2014")
            year = site[dotComPlace:dotComPlace+4]
            month = site[dotComPlace+5:dotComPlace+7]
            day = site[dotComPlace+8:dotComPlace+10]

            json["year"] = int(year)
            json["month"] = int(month)
            json["day"] = int(day)
            json["id"] = newsDb.metaData.find({}).count()+10000
            json["rating"] = 0
            json["visits"] = 0
            print "JSON = ", json
            metaData.insert(json)
            mined_links.insert( {"link" : site } )
            print "Link Mined"
        except:
            None

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
        if linkBuffer.find({}).count() <= 0:
            break
        one_link = linkBuffer.find_one();
        # print "Mining link = " , one_link["link"]
        if type(one_link) == NoneType:
            break
        linkBuffer.remove({"link":one_link["link"]});
        try:
            if (one_link["link"].find("2014") != -1):
                # print "Mining link = " , one_link["link"]
                mine_single_site(one_link["link"])
            
        except:
            print "Error happened!"
            print "Link = " + one_link["link"]