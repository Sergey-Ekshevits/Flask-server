new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def binary_search(list, num):
    start = 0
    end = len(list) - 1
    while start <= end:
        middle = (start+end) // 2
        if list[middle] == num:
            return list[middle]
        elif num < list[middle]:
            end = middle
        else:
            start = middle
    return None
print(binary_search(new_list,2))
# n=new_list[1:4]
# print(len(new_list[1:4]))