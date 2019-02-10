def binary_search(element, some_list):
    first_index = 0
    last_index = len(some_list) - 1
    while first_index <= last_index:
        mid_index = (first_index + last_index) // 2
        print('mid_index = %d' % (mid_index))
        if some_list[mid_index] == element:
            return mid_index
        elif some_list[mid_index] > element:
            last_index = mid_index - 1
        elif some_list[mid_index] < element:
            first_index = mid_index + 1
    return None

print(binary_search(3, [2, 3, 5, 7, 11]))

