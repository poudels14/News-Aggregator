import cherrypy
import pymongo
from pymongo import MongoClient
import unicodedata
from bson.objectid import ObjectId
import random
import string
from datetime import date
import os

client = MongoClient()
# bloomberg = client.bloomberg
# techcrunch = client.techcrunch
newsDb = client.newsDb


def database(site, cat, year, month, day, lastId):
		# if site == "techcrunch":
		# 	print "techcrunch site requested = "
		# 	metaData = techcrunch.metaData
		# 	xx = metaData.find({})
		# else:
		# 	metaData = bloomberg.metaData
		# 	xx = metaData.find({"category":cat})
		xx = newsDb.metaData.find({"domain":site, "year":year, "month":month, "day": day, "id" : { '$lt' : lastId}}).sort("id", -1)
		print xx.count()
		rtn = ""
		
		tot = min(xx.count(), 10)
		for x in range(0,tot):
			r = xx[x]
			try:
				title = r["title"]
			except:
				title = "No description Found!"
			try:
				descri = r["descri"]
			except:
				descri = "No description Found!"
			try:
				link = r["link"]
			except:
				link = "none"
			try:
				image = r["image"]
			except:
				image = "none"

			if image == "none" and site == "theverge.com":
				continue;

			x = "{"
			x = x + "\"title\" : \"" + title.replace('"', '\'').encode('utf8') + "\","
			x = x + "\"descri\" : \"" + descri.encode('utf8').replace('"', '\'').replace('\n', '').replace('\r\n', '').replace('\r', '') + "\","
			x = x + "\"link\" : \"" + link.replace('"', '\'').encode('utf8') + "\","
			x = x + "\"image\" : \"" + image.replace('"', '').encode('utf8') + "\","
			x = x + "\"id\" : \"" + str(r["id"]) + "\","
			x = x + "\"date\" : \"" + str(r["month"]) + "-" + str(r["day"]) + "-" + str(r["year"]) + "\"},"
			# x = x + "},"
			rtn = rtn + x
		# dd = "doesn\xe2\x80\x99t"
		return "[" + rtn[:-1] + "]"

class NewsSite(object):
    @cherrypy.expose
    def i(self):
        return "Hello worldasdasd!"

    @cherrypy.expose
    def db(self,site="techcrunch.com",cat="",day=date.today().day - 1, month = date.today().month, year = date.today().year, lastId = 100000000):
    	cherrypy.response.headers['Content-Type'] = 'text/javascript'
    	print "***********************************"
    	print cherrypy.request.headers.get('Referer')
    	print "***********************************"
    	return database(site, cat, int(year), int(month), int(day), int(lastId))

    @cherrypy.expose
    def goto(self, id=10000):
    	raise cherrypy.HTTPRedirect(newsDb.metaData.find({"id" : int(id)})[0]["link"])


if __name__ == '__main__':
	conf = {
		'/': {
			'tools.staticdir.on': True,
			'tools.staticdir.dir': '/Users/sagar/Desktop/AWS/Projects/News_site/site/'
			}
		}
	# cherrypy.server.socket_host = '0.0.0.0'
	cherrypy.quickstart(NewsSite(), '/', conf)
