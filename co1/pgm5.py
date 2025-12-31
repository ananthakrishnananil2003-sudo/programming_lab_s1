colors_input1 = input("Enter color names for list 1: ")
color_list1 = [color.strip() for color in colors_input1.split(',')]
print(f"First color in list 1: {color_list1[0]}")
print(f"Last color in list 1: {color_list1[-1]}")
colors_input2 = input("Enter color names for list 2: ")
color_list2 = [color.strip() for color in colors_input2.split(',')]
color_list3 = [color for color in color_list1 if color not in color_list2]
print(f"Colors from list 1 not found in list 2: {', '.join(color_list3)}")