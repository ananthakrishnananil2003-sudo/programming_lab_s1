nums = list(map(int, input("Enter integers separated by spaces: ").split())) r=[] 
for n in nums: 
    if n>100: 
        r.append('over') 
    else:
        r.append(n)
        print(r) 
