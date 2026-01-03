class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def printDetails(self):
        print(f"Details: Name- {self.name} Age- {self.age}")

class Student(Person):
    def __init__(self,name,age,studentId):
        super().__init__(name,age)
        self.studentId =studentId
    
    def printDetails(self):
        print(f"Details: name- {self.name} age- {self.age} id- {self.studentId}")
    
class Teacher(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary =salary
    
    def printDetails(self):
        print(f"Details: name- {self.name} age- {self.age} salary- {self.salary}")
        
        
people = [Student("Himanshu",20,1),Teacher("Shilank",35,"80000")]

for i in people:
    i.printDetails()
    
    