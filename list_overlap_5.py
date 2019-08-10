list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#new_list = []
#
# for num in list1:
#     if num in list2:
#         new_list.append(num)
#
# print(new_list)

print(set(list1) & set(list2))