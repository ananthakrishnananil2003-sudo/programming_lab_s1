s = input("Enter a string: ") 
f_char = s[0] 
new_string = f_char + s[1:].replace(f_char, '$') 
print("Modified string:", new_string) 
