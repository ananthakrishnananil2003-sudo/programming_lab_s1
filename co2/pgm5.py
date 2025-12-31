s = input("Enter a string: ") 
freq = {} 
for char in s: 
    if char != " ": 
        if char in freq: 
            freq[char] = freq[char] + 1 
        else: 
            freq[char] = 1 
print("Frequency:") 
for char in freq: 
    print(char, ":", freq[char]) 
