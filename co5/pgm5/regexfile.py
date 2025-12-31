import re 
filename = "regextext.txt" 
search_word = input("Enter the word to search: ") 
count = 0 
with open(filename, 'r') as file: 
for line in file: 
    occurrences = len(re.findall(r'\b' + re.escape(search_word) + r'\b', line,re.IGNORECASE)) 
    count += occurrences 
if count > 0: 
    print(f"The word '{search_word}' appears {count} time(s) in the file.") 
else: 
    print(f"The word '{search_word}' was not found in the file.") 
