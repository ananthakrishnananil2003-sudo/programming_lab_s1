filename = "sample.txt" 
with open(filename, 'r') as file: 
    lines_list = [line.strip() for line in file] 
print("Lines stored in the list:") 
print(lines_list) 
