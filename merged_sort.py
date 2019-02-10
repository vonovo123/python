def merge(list1, list2):
    merged_list = []
    while len(list1) != 0 and len(list2) != 0:
        if list1[0] <= list2[0]:
            merged_list.append(list1[0])
            list1.remove(list1[0])
        elif list2[0] <= list1[0]:
            merged_list.append(list2[0])
            list2.remove(list2[0])
    if len(list1) != 0:
        for i in list1:
            merged_list.append(i)
    elif len(list2) != 0:
        for i in list2:
            merged_list.append(i)
    return merged_list

def merge_sort(my_list):
    divide_point = int(len(my_list) / 2)
    # my_list의 요소 수가 1 이면
    if divide_point == 0:
        return my_list
    left1 = merge_sort(my_list[:divide_point])
    right1= merge_sort(my_list[divide_point:])
    return merge(left1, right1)


some_list = [11, 3, 6, 4, 12, 1, 2, 5]
sorted_list = merge_sort(some_list)
print(sorted_list)
