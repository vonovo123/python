# 선택 정렬
def selection_sort(my_list):
    for i in range(len(my_list)):
        min_index = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        temp = my_list[i]
        my_list[i] = my_list[min_index]
        my_list[min_index] = temp

some_list = [11, 3, 6, 4, 12, 1, 2]
selection_sort(some_list)
print(some_list)