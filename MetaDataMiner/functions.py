### Title ###
title = ""
ogTitle = ""
twitterTitle = ""
### Description ###
descri = ""
ogDescri = ""
twitterDescri = ""
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

def remove_hash(site):
	site = site.split("#")[0]
	return site

def verify_same_site(site, domain):
	tmp = site.split("/")
	try:
		if tmp[2] == domain or tmp[2][4:] == domain or tmp[0] == "":
			print "Domain matched"
			return True
		print "Domain not matched"
		return False
	except:
		print "Domain not matched"
		return False

def is_site_valid(site):
	if site[:1] == "#" and site[:5] != "http:" and site[:5] != "https":
		return False
	return True


def clear_vars():
    global title, ogTitle, twitterTitle, descri, ogDescri, twitterDescri, pubdate, lastmod, href
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


def mineMetaData(attrs):
	global title, ogTitle, twitterTitle, descri, ogDescri, twitterDescri, pubdate, lastmod, href
	global image, ogImage, thumbnail, ogThumbnail, twitterImage, category, keywords

	d = dict(attrs)

	#######################################################
	if "name" in d and d["name"] == "title":
		x = d["content"]
		# print "title = " + x
		title = x 
		return

	elif "name" in d and d["name"] == "og:title":
		x = d["content"]
		print "og:title = " + x
		ogTitle = x
		return

	elif "name" in d and d["name"] == "twitter:title":
		x = d["content"]
		# print "twitter:title = " + x
		twitterTitle = x
		return
	#######################################################

	elif "name" in d and d["name"] == "description":
		x = d["content"]
		# print "Description = " + x
		descri = x
		return

	elif "name" in d and d["name"] == "og:description":
		x = d["content"]
		# print "og:description = " + x
		ogDescri = x
		return

	elif "name" in d and d["name"] == "twitter:description":
		x = d["content"]
		# print "twitter:description = " + x
		twitterDescri = x
		return

	#######################################################

	elif "name" in d and d["name"] == "pubdate":
		x = d["content"]
		# print "pubdate = " , x
		pubdate = x
		return

	elif "name" in d and d["name"] == "lastmod":
		x = d["content"]
		# print "lastmod = " , x
		lastmod = x
		return

	#######################################################

	elif "name" in d and d["name"] == "image":
		x = d["content"]
		# print "image = " , x
		image = x
		return

	elif "name" in d and d["name"] == "og:image":
		x = d["content"]
		# print "og:image = " , x
		ogImage = x
		return

	elif "name" in d and d["name"] == "twitter:image":
		x = d["content"]
		# print "twitter:image = " , x
		twitterImage = x
		return

	elif "name" in d and d["name"] == "thumbnail":
		x = d["content"]
		# print "thumbnail = " , x
		thumbnail = x
		return

	elif "name" in d and d["name"] == "og:thumbnail":
		x = d["content"]
		# print "og:thumbnail = " , x
		ogThumbnail = x
		return

	#######################################################

	elif "name" in d and d["name"] == "category":
		x = d["content"]
		# print "category = " , x
		category = x
		return

	#######################################################

	elif "name" in d and d["name"] == "keywords":
		x = d["content"]
		# print "keywords = " , x
		keywords = x
		return

##############################################################################################################

	elif "property" in d and d["property"] == "title":
		x = d["content"]
		# print "title = " + x
		title = x 
		return
		
	elif "property" in d and d["property"] == "og:title":
		x = d["content"]
		# print "og:title = " + x
		ogTitle = x
		return

	elif "property" in d and d["property"] == "twitter:title":
		x = d["content"]
		# print "twitter:title = " + x
		twitterTitle = x
		return
	#######################################################

	elif "property" in d and d["property"] == "description":
		x = d["content"]
		# print "Description = " + x
		descri = x
		return

	elif "property" in d and d["property"] == "og:description":
		x = d["content"]
		# print "og:description = " + x
		ogDescri = x
		return

	elif "property" in d and d["property"] == "twitter:description":
		x = d["content"]
		# print "twitter:description = " + x
		twitterDescri = x
		return

	#######################################################

	elif "property" in d and d["property"] == "pubdate":
		x = d["content"]
		# print "pubdate = " , x
		pubdate = x
		return

	elif "property" in d and d["property"] == "lastmod":
		x = d["content"]
		# print "lastmod = " , x
		lastmod = x
		return

	#######################################################

	elif "property" in d and d["property"] == "image":
		x = d["content"]
		# print "image = " , x
		image = x
		return

	elif "property" in d and d["property"] == "og:image":
		x = d["content"]
		# print "og:image = " , x
		ogImage = x
		return

	elif "property" in d and d["property"] == "twitter:image":
		x = d["content"]
		# print "twitter:image = " , x
		twitterImage = x
		return

	elif "property" in d and d["property"] == "thumbnail":
		x = d["content"]
		# print "thumbnail = " , x
		thumbnail = x
		return

	elif "property" in d and d["property"] == "og:thumbnail":
		x = d["content"]
		# print "og:thumbnail = " , x
		ogThumbnail = x
		return

	#######################################################

	elif "property" in d and d["property"] == "category":
		x = d["content"]
		# print "category = " , x
		category = x
		return

	#######################################################

	elif "property" in d and d["property"] == "keywords":
		x = d["content"]
		# print "keywords = " , x
		keywords = x
		return
	# except:
	# 	None