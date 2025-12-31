words = input("Enter words (separated by space): ").split() 
max_length = 0 
for word in words: 
    if len(word) > max_length: 
        max_length = len(word) 
print("Length of longest word:", max_length)
