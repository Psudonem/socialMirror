#https://letterboxd.com/gamegear/rss/
import feedparser


def letterboxdUpdate(uName):
	feed = feedparser.parse("https://letterboxd.com/"+uName+"/rss/")#"https://www.backloggd.com/u/gamegear/reviews/rss/")
	out="""<html>
		<head>
			<title>Letterboxd Mirror</title>
			<meta charset="utf-8"/>
			   <meta name="viewport" content="initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0, user-scalable=no, target-densitydpi=device-dpi" />
	    <meta name="apple-mobile-web-app-capable" content="yes" />
	    <meta name="apple-mobile-web-app-status-bar-style" content="black" />
	    <meta name="HandheldFriendly" content="true" />

	 <link rel="stylesheet" href="style.css" />
			<style>
	                      img{max-width:4em;transition-duration: 4s;}
	                      img:hover{max-width:20em;}
				
			</style>
		</head>
		<body>
	<center>
	<div class="top">
		<h1>Letterboxd Archive</h1>
	</div>"""

	for e in feed.entries:
	      out +='<div class="review">'
	      out +="<h3>"+e.title+"</h3>"
	      out +="<p>"+e.summary.replace('\n','<br>')+"</p>"
	      out +="<sub>Date published: "+str(e.published)+"</sub>"
	      out +="</div>"
	      print(e.title)
	      print(e.summary)

	out+="""<div class="bottom">
		<a href="index.html"><h1>Other Mirrors</h1></a>
	</div></center>
		</body>
	</html>"""


	out = out.encode("utf8")
	fyle = open("letterboxd.html", "wb")
	fyle.write(out)
	fyle.close()
	print("letterboxd update complete")
