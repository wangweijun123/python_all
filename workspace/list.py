def add_five(num_list):
    return [n + 5 for n in num_list]


num_list = [1,2,3]
new_num_list = add_five(num_list)
print("num_list:", num_list) # [1, 2, 3]
print("new_num_list:", new_num_list) # [6, 7, 8]


num_list = [1,2,3]
for n in num_list:
    n += 5
print("num_list:", num_list) # [1, 2, 3]