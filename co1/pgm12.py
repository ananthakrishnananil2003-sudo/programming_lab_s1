names = list(input("Enter names separated by spaces: ").split()) 
print("List is: ",names) 
rev_name = names[::-1] 
print("Reversed list is: ",rev_name) 
long_name = max(names, key=len) 
print("Longest name is: ",long_name) 
