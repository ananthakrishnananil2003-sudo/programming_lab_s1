class Student: 
    def __init__(self,m1,m2): 
        self.m1 = m1 
        self.m2 = m2 
    def total(self): 
        return self.m1 + self.m2 
    def __add__(self,other): 
        total1 = self.total() 
        total2 = other.total() 
        return total1+total2 
m11 = int(input("Enter first marks of first student: ")) 
m12 = int(input("Enter second marks of first student: ")) 
m21 = int(input("Enter first marks of second student: ")) 
m22 = int(input("Enter second marks of second student: ")) 
s1 = Student(m11,m12) 
s2 = Student(m21,m22) 
print('Total marks of Student1 = ',s1.total()) 
print('Total marks of Student2 = ',s2.total()) 
ctotal = s1 + s2 
print('Combined Total is ',ctotal) 