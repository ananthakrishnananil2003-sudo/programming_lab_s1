import arithmetic 
num1 = float(input("Enter the first number: ")) 
num2 = float(input("Enter the second number: ")) 
print(f"\nArithmetic Operations on {num1} and {num2}:") 
print(f"Addition: {num1} + {num2} = {arithmetic.add(num1, num2)}") print(f"Subtraction: {num1} - {num2} = {arithmetic.subtract(num1, num2)}") print(f"Multiplication: {num1} × {num2} = {arithmetic.multiply(num1, num2)}") result = arithmetic.divide(num1, num2) 
print(f"Division: {num1} ÷ {num2} = {result}") 
