numbers = list(map(int, input("Enter numbers: ").split())) 
odd_numbers = [num for num in numbers if num % 2 != 0] 
print(odd_numbers) 
