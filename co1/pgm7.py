names = ["amal","arun","hari","varun"]
print(names)
print(f"Number of elements in the list : {len(names)}")
count = 0
for x in names:
    if 'a' in x:
        count = count+1
print(f"Number of occurrences of 'a' in the list : {count}")