class Employee:

    def __init__(self, name, id):
        self.name = name
        self.id = id


    def show_data(self):
        print(f"The name of employee: {self.name} : {self.id}")

"""
Inherited all the methods from the Employee Class
Method in the child class cannot be used in the parent class
"""

class Programmer(Employee):
    def show_language(self):
        print(f"The default language is Python")

e1 = Employee("Anurag",103)
e2 = Employee("Abhranil",104)
e3 = Programmer("Roni",105)


e1.show_data()
e2.show_data()
e3.show_data()
e3.show_language()
