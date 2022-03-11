def product_of_array_except(array_list):
    res = [1] * len(array_list)
    prefix = 1
    for i in range(len(array_list)):
        res[i] = prefix
        prefix = prefix * array_list[i]
    postfix = 1
    for i in range(len(array_list) -1, -1, -1):
        res[i] = res[i] * postfix
        postfix = postfix * array_list[i]
    return res


print(product_of_array_except([1, 2, 3, 4]))
print(product_of_array_except([-1, 1, 0, -3, 3]))

