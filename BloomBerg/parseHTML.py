#Bloomberg News

from HTMLParser import HTMLParser
import urllib


gotArticle = False
gotH1 = False
gotAuthor = False
gotTitle = False
gotDate = False
grabFirstP = False
getFirstP = False
gotFirstP = False
firstP = ""

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):


    def handle_starttag(self, tag, attrs):
    	global gotArticle
        global gotH1
        global gotAuthor
        global gotDate
        global grabFirstP
        global getFirstP
        global gotFirstP

        if tag == 'article':
            # print "td = " , attrs, " ; " , len(attrs)
            gotArticle = True
            self.parseArticle(attrs)

        elif tag == 'h1':
            gotH1 = True
        elif tag == 'span':
            # print "Span attrs = ", attrs
            if len(attrs) > 0 and attrs[0][0] == 'class' and attrs[0][1] == "author":
                gotAuthor = True
                # print "Span attrs = ",attrs[0][1]
            elif len(attrs) > 2 and attrs[2][0] == 'class' and attrs[2][1] == 'date':
                # print "Date attrs = ", attrs[2][1]
                gotDate = True
        elif tag == 'div':
            if len(attrs) > 0 and attrs[0][0] == 'class' and attrs[0][1] == "article_body":
                # print "Div found ; ", attrs
                grabFirstP = True
        elif tag == 'p':
            if grabFirstP:
                # print "First Paragraph"
                getFirstP = True
            # print "Title = ", attrs
		# if attrs[0][0] == 'href':
		# 	# print "Href = ", attrs[0][1]
		# 	href = attrs[0][1]

    def handle_data(self, data):
    	global gotArticle
    	global gotTitle
    	global gotAuthor
    	global gotH1
        global gotDate
        global getFirstP
        global gotFirstP
        global firstP

    	# print "Encountered some data  :", data

    	if gotArticle:
            if gotH1:
                print "Title = ", data[1:-1]
                gotH1 = False
            elif gotAuthor:
                print "Author = ", data[3:]
                gotAuthor = False
            elif gotDate:
                print "Date = ", data[1:]
                gotDate = False
            elif getFirstP and not gotFirstP:
                if firstP == "":
                    firstP = data
                    # print "First Paragraph = ", data
                else:
                    firstP = firstP + data
                

    def handle_endtag(self, tag):
        global gotFirstP
        global firstP

        if tag == 'p' and getFirstP and not gotFirstP:
            firstP = firstP.translate(None, '\n')
            print "First Paragraph = ", firstP
            # print "Paragraph ending--------------------------"
            gotFirstP = True



    def parseArticle(arr1, arr2):
    	global counter
    	
    	if len(arr2) > 0:
    		if arr2[0][0] == "class" and arr2[0][1] == "title":
    			counter = 1
    		elif arr2[0][0] == "class" and arr2[0][1] == "subtext":
    			counter = 6


parser = MyHTMLParser()

f = open('news.html','r')
data = f.read()
parser.feed(data)
