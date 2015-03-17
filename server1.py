import cherrypy
import pymongo
from pymongo import MongoClient
import unicodedata
from bson.objectid import ObjectId
import random
import string


client = MongoClient()
bloomberg = client.bloomberg
techcrunch = client.techcrunch

i = 0
techcrunch.metaData.find({}).count()
for x in techcrunch.metaData.find({}):
	print techcrunch.metaData.find({}).count()
	print "year = " + x["year"]
	# if x["year"] != "2014" or x["year"] != 2014:
	# 	techcrunch.metaData.remove({"_id":x["_id"]})
	# 	continue
	# techcrunch.metaData.update({"_id": x["_id"]}, { '$set' : {"month" : int(float(x["month"])),"day" : int(float(x["day"])),"year" : int(float(x["year"])),}})
	# i = i + 1