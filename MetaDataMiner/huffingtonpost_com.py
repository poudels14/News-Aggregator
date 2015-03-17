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
#################################################################
client = MongoClient()
db = client.huffingtonpost
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
refDomain = "huffingtonpost.com"
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
                linkBuffer.insert({"link":d["href"]})
            except:
                None

        if mineMeta and tag == "meta":
            attrsArr = list(attrs)
            # print attrsArr
            if len(attrsArr) > 1:
               functions.mineMetaData(attrs)
        #######################################################
            title = functions.title
            ogTitle = functions.ogTitle
            twitterTitle = functions.twitterTitle
            descri = functions.descri
            ogDescri = functions.ogDescri
            twitterDescri = functions.twitterDescri
            pubdate = functions.pubdate
            lastmod = functions.lastmod
            href = functions.href
            image = functions.image
            ogImage = functions.ogImage
            thumbnail = functions.thumbnail
            ogThumbnail = functions.ogThumbnail
            twitterImage = functions.twitterImage
            category = functions.category
            keywords = functions.keywords


        def handle_data(self, data):
            None

site = {}
# site[0] = "http://www.huffingtonpost.com/2014/10/13/"
# site[0] = "http://www.huffingtonpost.com/business"
# site[0] = "http://www.huffingtonpost.com/tech/"
site[0] = "http://www.huffingtonpost.com/2014/10/30/"


def mine_single_site(site):
    site = functions.remove_hash(site)
    site = site.split("?")[0]

    if site[:1] == "/":
        site = "http://" + refDomain + "/" + site

    if not functions.is_site_valid(site):
        return

    if not functions.verify_same_site(site, refDomain):
        return

    if site.find("2014") == -1:
        mineMeta = False

    if len(site.split("/")) < 7:
        mineMeta = False

    global mineMeta, refDomain
    global linkBuffer
    global title, ogTitle, twitterTitle, descri, ogDescri, twitterDescri, domain, pubdate, lastmod, href
    global image, ogImage, thumbnail, ogThumbnail, twitterImage, category, keywords

    if site[-5:] != ".html":
        mineMeta = False
        # print site[-5:]

    if metaData.find_one({'link' : site}):
        print "Already Mined"
        return

    if visitedLinks.find_one({'link' : site}):
        print "Already Visited"
        return

    # print "All test passed"
    # print "Mine Meta = " + str(mineMeta)
    buffer = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, site)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()

    body = buffer.getvalue()
    visitedLinks.insert({"link": site})

    parser = MyHTMLParser()
    try:
        data = body.decode('utf-8')
    except:
        data = body
    parser.feed(data)


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
        try:
            json["domain"] = refDomain
            chnks = site.split("/")
            year = chnks[3]
            month = chnks[4]
            day = chnks[5]
            json["year"] = int(year)
            json["month"] = int(month)
            json["day"] = int(day)
            json["id"] = metaData.find({}).count()+10000
            json["rating"] = 0
            json["visits"] = 0
            # print "JSON = ", json
            metaData.insert(json)
            # mined_links.insert( {"link" : site } )
            print "Link Mined"
        except:
            print "Mined link couldn't insert"

    clear_vars()
    functions.clear_vars()



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
        # # if linkBuffer.find_one({}).length() <= 0:
        # #     break
        # one_link = linkBuffer.find_one();
        # if type(one_link) == NoneType:
        #     break
        # linkBuffer.remove({"link":one_link["link"]})
        # print "Mining link = " , one_link["link"]
        # mine_single_site(one_link["link"])

         # if linkBuffer.find_one({}).length() <= 0:
        #     break
        one_link = linkBuffer.find_one();
        if type(one_link) == NoneType:
            break
        linkBuffer.remove({"link":one_link["link"]});
        try:
            if (one_link["link"].find("2014") != -1):
                print "Mining link = " , one_link["link"]
                mine_single_site(one_link["link"])
        except:
            print "Error happened!"
            print "Link = " + one_link["link"]
