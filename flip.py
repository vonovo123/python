def flip(some_list):
    if len(some_list) == 0:
        return some_list
    return flip(some_list[1:]) + some_list[:1]

# 테스트
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)