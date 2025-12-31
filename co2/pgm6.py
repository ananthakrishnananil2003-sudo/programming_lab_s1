s = input("Enter a string: ") 
if s.endswith("ing"): 
    result = s + "ly" 
else: 
    result = s + "ing" 
print("Result:", result)
