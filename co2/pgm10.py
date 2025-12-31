print("=== (a) Positive Numbers ===") 
nums = [int(x) for x in input("Enter integers (space-separated): ").split()] positive = [x for x in nums if x > 0] 
print("Positive list:", positive) 
print("\n=== (b) Squares of N numbers ===") 
n = int(input("Enter N: ")) 
squares = [i**2 for i in range(1, n+1)] 
print("Squares:", squares) 
print("\n=== (c) Vowels in word ===") 
word = input("Enter a word: ").lower() 
vowels = [c for c in word if c in 'aeiou'] 
print("Vowels:", vowels) 
print("\n=== (d) Ordinal values ===") 
word2 = input("Enter a word: ") 
ordinals = [ord(c) for c in word2] 
print("Ordinal values:", ordinals) 
