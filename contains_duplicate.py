def find_duplicate(list_num):
    hash_set = set()
    for i in range(len(list_num)):
        if list_num[i] in hash_set:
            return True
        else:
            hash_set.add(list_num[i])
    return False


print(find_duplicate([1, 2, 3, 1]))
print(find_duplicate([1, 2, 3, 4]))
print(find_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
