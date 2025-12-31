def fibonacci(n):
    fib_series = [] 
    a, b = 0, 1 
    for i in range(n):
        fib_series.append(a) 
        a, b = b, a + b 
    return fib_series 
n = int(input("Enter the number of Fibonacci terms: ")) 
if n <= 0: 
    print("Please enter a positive number.") 
else: 
    result = fibonacci(n) 
print("First", n, "Fibonacci numbers:", result)
