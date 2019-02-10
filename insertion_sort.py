# 삽입 정렬
def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        key_value = my_list[i]
some_list = [11, 3, 6, 4, 12, 1, 2 ,7, 8, 10]
insertion_sort(some_list)
print(some_list)