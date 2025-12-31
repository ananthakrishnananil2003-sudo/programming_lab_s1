class Rectangle: 
    def __init__(self,l,b): 
        self.l = l 
        self.b = b 
    def area(self): 
        return self.l * self.b 
    def __lt__(self,other): 
        return self.area() < other.area() 
l = int(input('Enter length of first rectangle: ')) 
b = int(input('Enter width of first rectangle: ')) 
l1 = int(input('Enter length of second rectangle: ')) 
b1 = int(input('Enter width of second rectangle: ')) 
r1 = Rectangle(l,b) 
r2 = Rectangle(l1,b1) 
print("Area of first Rectangle: ",r1.area()) 
print("Area of second Rectangle: ",r2.area()) 
if r1<r2: 
    print("Area of second rectangle is large.") 
elif r1>r2: 
    print("Area of first rectangle is large.") 
else: 
    print("Areas are equal.") 
