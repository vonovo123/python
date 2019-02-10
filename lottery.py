from random import randint
# 무작위로 정렬된 1 - 45 사이의 숫자 여섯개 뽑기
def generate_numbers():
    # 난수로 생성되는 6자리 list
    numbers = []
    # 중복되지 않는 번호 6개 추가
    while len(numbers) != 6:
        add_num = randint(1, 46)
        if add_num not in numbers:
            numbers.append(add_num)
    # 무작위로 정렬된 6자리 list 리턴
    return numbers

# 보너스까지 포함해 7개 숫자 뽑기
# 정렬된 6개의 당첨 번호와 1개의 보너스 번호 리스트를 리턴
def draw_winning_numbers(list):
    # bonus 숫자
    bonus = randint(1, 46)
    # 중복된 수가 아닐때 까지 bonus 숫자 생성
    while bonus in list:
        bonus = randint(1, 46)
    # 보너스 숫자 추가
    list.append(bonus)
    # 정렬된 6개의 당첨 번호와 1개의 보너스 번호 리스트
    return sorted(list)

# 두 리스트에서 중복되는 숫자가 몇개인지 구하기
def count_matching_numbers(list1, list2):
    # 중복숫자 count
    count = 0
    for i in list2:
        if i in list1:
            count += 1
            print(i)
    return count

# 로또 등수 확인하기
def check(numbers, winning_numbers):
    # 일반 숫자의 중복수
    result_count = count_matching_numbers(numbers, winning_numbers[0:len(winning_numbers) - 1])
    # 일반 숫자 중 6개가 같으면
    if result_count == 6:
        return 1000000000
    # 일반 숫자 5개가 같고 보너스 숫자가 사용자 리스트에 존재하면
    elif result_count == 5 and winning_numbers[6] in numbers:
        return 50000000
    # 일반 숫자 5개가 같으면
    elif result_count == 5:
        return 1000000
    # 일반 숫자 4개가 같으면
    elif result_count == 4:
        return 50000
    # 일반 숫자 3개가 같으면
    elif result_count == 3:
        return 5000
    else:
        return 0
