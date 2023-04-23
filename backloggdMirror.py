import feedparser
import json
import socialDB as s

def backloggdUpdate(uName):
	db = s.database()

	try:
		feed = feedparser.parse("https://www.backloggd.com/u/"+uName+"/reviews/rss/")
	except:
		print("there's an issue with the backloggd API, could not download new content")


	db.newCategory("backloggd")
	db.newUser("backloggd",uName)
	for f in feed.entries:
		db.addReviewCheck("backloggd",uName,s.review(f.title,f.summary, f.published))

	out="""<html><head><title>Backloggd Mirror</title><meta charset="utf-8"/><meta name="viewport" content="initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0, user-scalable=no, target-densitydpi=device-dpi" /><meta name="apple-mobile-web-app-capable" content="yes" /><meta name="apple-mobile-web-app-status-bar-style" content="black" /><meta name="HandheldFriendly" content="true" /><link rel="stylesheet" href="style.css" /></head><body><center><div class="top"><h1>Backloggd Archive</h1></div>"""
	

	for f in reversed(db.memory['backloggd'][uName]):
	      out +='<div class="review">'
	      out +="<h3>"+f['title']+"</h3>"
	      #print(f.title)
	      out +="<p>"+f['review'].replace('\n','<br>')+"</p>"
	      out +="<sub>Date published: "+str(f['date'])+"</sub>"
	      out +="</div>"

	out+="""<div class="top">
		<a href="index.html"><h1>Other Mirrors</h1></a>
	</div></center>
		</body>
	</html>"""

	out = out.encode("utf8")
	fyle = open("backloggd.html", "wb")
	fyle.write(out)
	fyle.close()
	print("backloggd update complete")