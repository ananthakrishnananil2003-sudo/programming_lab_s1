class Student: 
    def __init__(self, name): 
        self.name = name 
    def display_name(self): 
        print(f"Student Name: {self.name}") 
    class MCAStudent(Student): 
      def __init__(self, name, semester): 
        super().__init__(name) 
        self.semester = semester 
    def display_details(self): 
      self.display_name() 
      print(f"Semester: {self.semester}") 
print("=== MCA Student Information ===") 
student_name = input("Enter student name: ") 
student_semester = int(input("Enter current semester (1-4): ")) 
mca_student = MCAStudent(student_name, student_semester) 
print("\n--- Student Details ---") 
mca_student.display_details()
