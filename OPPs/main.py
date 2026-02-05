class Member:
    def __init__(self,name,post):# Constructor function
        
        self.name = name
        self.post = post

    def info(self):
        print(f"{self.name} is a {self.post}.")

a=Member("Anurag","Fullstack Developer")
b=Member("Abhrnil","Backend Developer")
c=Member("Dhruba","Frontend Developer")
d=Member("Roni","Backend Developer")

a.info()
b.info()
c.info()
d.info()
