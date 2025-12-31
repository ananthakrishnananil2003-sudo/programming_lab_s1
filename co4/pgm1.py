class Student: 
    def __init__(self,name,rno,marks): 
        self.name= name 
        self.rno= rno 
        self.marks= marks 
    def display(self): 
        print('Name: ',self.name,'\nRoll no: ',self.rno,'\nMarks: ',self.marks) 
    def update(self,newmrks): 
        self.marks = newmrks 
name = input('Enter student name: ') 
rno = input('Enter Roll no: ') 
marks = int(input('Enter marks: ')) 
s1 = Student(name,rno,marks) 
s1.display() 
new_marks = int(input('Enter new marks: ')) 
s1.update(new_marks) 
s1.display() 
