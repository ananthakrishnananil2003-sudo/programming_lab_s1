a = input("Enter a line of text: ")
words = a.split()
count = {}
for word in words:
count[word] = count.get(word,0)+1
for word,co in count.items():
print(word ,":", co)