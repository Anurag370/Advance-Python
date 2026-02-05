class Student:
    name="Anurag"
    branch="CSE"
    rollno=39

    def info(self):
        print(f"{self.name} is from {self.branch} branch")

a = Student()
b = Student()
# print(a.name)
a.name = "Roni"
a.branch = "CSE"

b.name = "Anurag"
b.branch = "ECE"

a.info()
b.info()