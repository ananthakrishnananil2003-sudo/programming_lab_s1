class Student: 
    def __init__(self, name, m1, m2): 
        self.name = name 
        self.m1 = m1 
        self.m2 = m2 
    def total(self): 
        return self.m1 + self.m2 
name = input("Enter name: ") 
m11 = int(input("Enter first marks of first student: ")) 
m12 = int(input("Enter second marks of first student: ")) 
s1 = Student(name, m11, m12) 
print('Name of student is:', s1.name) 
print('Total marks of Student1 =', s1.total())
