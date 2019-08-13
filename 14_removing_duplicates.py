# Without using set
my_list = [1, 2, 3, 4, 3, 2, 1]


def remove_dup1():
    new_list = []
    for i in my_list:
        if i not in new_list:
            new_list.append(i)
    return new_list


print(remove_dup1())

# By using set


def remove_dup2(x):
    return list(set(x))


print(remove_dup2(my_list))
