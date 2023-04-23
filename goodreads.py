import requests
from bs4 import BeautifulSoup
import socialDB as s

def goodReadsUpdate(p):
	db = s.database()
	pid = p[p.rfind("/")+1:p.find("-")]
	url = "https://www.goodreads.com/review/list_rss/"+pid+"?shelf=%23ALL%23"
	r = requests.get(url, allow_redirects=True)
	open('goodreads.xml', 'w').write(r.text)
	out="""<html><head><title>Goodreads Mirror</title><meta charset="utf-8"/><meta name="viewport" content="initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0, user-scalable=no, target-densitydpi=device-dpi" /><meta name="apple-mobile-web-app-capable" content="yes" /><meta name="apple-mobile-web-app-status-bar-style" content="black" /><meta name="HandheldFriendly" content="true" /><link rel="stylesheet" href="style.css" /><style>img{max-width:4em;transition-duration: 4s;}img:hover{max-width:20em;}</style></head><body><center><div class="top"><h1>Goodreads Archive</h1></div>""" 
	db.newCategory("goodreads")
	db.newUser("goodreads",pid)
	with open("goodreads.xml") as fp:
		soup = BeautifulSoup(fp, 'xml')

	for i in soup.find_all("item"):
		if int(i.user_rating.text)>0:
			db.addReviewCheck("goodreads",pid,s.review(i.title.text, i.user_review.text,i.user_date_added.text))


	for f in reversed(db.memory['goodreads'][pid]):
		out +='<div class="review">'
		out +="<h3>"+f['title']+"</h3>"
		#print(f.title)
		out +="<p>"+f['review'].replace('\n','<br>')+"</p>"
		out +="<sub>Date published: "+str(f['date'])+"</sub>"
		out +="</div>"
     # for i in soup.find_all("item"):
     # 	if int(i.user_rating.text)>0:
	   #         out+='<div class="review">'
	   #         out+="<h3>"+i.title.text+" by "+i.author_name.text+"</h3>"
	   #         out +="<p>"+i.user_review.text+"</p>"
	   #         out+="<p>"+int(i.user_rating.text)*"★"+"</p>"
	   #         out+="<sub>Review Published: "+i.user_date_added.text+"</sub>"
	   #         #print("___________")
	   #         out+='</div>'
	out+="""<div class="bottom">
		<a href="index.html"><h1>Other Mirrors</h1></a>
	</div></center>
		</body>
	</html>"""
	out = out.encode("utf8")
	fyle = open("goodreads.html", "wb")
	fyle.write(out)
	fyle.close()
	print("goodreads update complete")
#p  = "https://www.goodreads.com/user/show/136246393-yu"
#goodReadsUpdate(p)
