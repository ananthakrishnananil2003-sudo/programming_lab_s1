list1=list(map(int,input("Enter the integer:").split(" ")))
list2=list(map(int,input("Enter the integer:").split(" ")))
print("list of integer in list1:",list1)
print("list of integers in list2:",list2)

if len(list1)==len(list2):
print("length of list1 and list2 are same")
else :
print("length of list1 and list2 are not same")

x=sum(list1)
y=sum(list2)
if x==y:
print("lists sum to same value")
else:
print("lists sum are not same")
if (list1) == (list2):
print("list1 and list2 contain the same elements.")
else:
print("list1 and list2 do not contain the same elements.")
common_elements = list(set(list1) & set(list2))
print("Values occur in both are:",common_elements)