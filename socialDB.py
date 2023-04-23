import json

class review:
      def __init__(self, title, review, date):
            self.title = title
            self.review = review
            self.date = date
      def render(self):
            return {"title":self.title, "review":self.review,"date":self.date}
      def compare(self,other):
            return self.title==other.title


class database:
      def __init__(self):
            self.memory={}
            try:
                  self.f = open('dbmem.json',"r")
                  text = self.f.read()
                  if(len(text)>0):
                        self.memory = json.loads(text)
                  else:
                        print("current databse empty")
                  self.f.close()
                  
            except FileNotFoundError:
                  self.f = open('dbmem.json',"w")
                  self.f.close()
                  print("databse file not found, new one created.")

      def save(self):
            self.f = open('dbmem.json',"w")
            self.f.write(json.dumps(self.memory))
            self.f.close()
            
      def newCategory(self, category):
            if(category not in self.memory.keys()):
                  self.memory[category]={}
            else:
                  print("category already present")
            self.save()
      def newUser(self, category,user):
            if(category in self.memory.keys()):
                  if user not in self.memory[category]:
                        self.memory[category][user]=[]
                  else:
                        print("user already exists")
            else:
                  print("category not found")
            self.save()
      def addReviewNoCheck(self, category, user,review):
            self.memory[category][user].append(review.render())
            self.save()
      def addReviewCheck(self, category, user, review):
            check = False
            for r in self.memory[category][user]:
                  if review.title==r['title']:
                        check=True
                        break
            if not check:
                  self.memory[category][user].append(review.render())
            else:
                  print("review already in database, skipping")
            self.save()
            
            

            


#db = database()
#db.newCategory("myAnimeList")
#db.newUser("myAnimeList","yudosai")
#db.addReviewCheck("myAnimeList","yudosai",review("dog 2","this game sucks","jan 1, 2029"))
