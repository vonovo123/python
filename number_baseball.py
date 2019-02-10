from random import randint

try_count = 0
index = 0
# 컴퓨터가 뽑은 값을 담는 리스트
numbers = []

# 범위 검사 함수
def range_test(value):
    if value < 0 or value > 9:
        return True
    else:
        return False

# 중복 검사 함수
def duplicate_test(list, value):
    if value in list:
        return True
    else:
        return False

# 숫자 입력 함수
def insert_number(index):
    input_value = input("%d번째 수를 입력하세요: " % (index))
    return int(input_value)

# 조건 입력 함수
def condition_selector(list, value):
    #첫번째 입력값일 경우 user_list 요소 무
    if len(list) == 0:
        if range_test(value):
            return True
        else:
            return False
    # 이후 user_list 존재
    else:
        if range_test(value) == True or duplicate_test(list, value) == True:
            return True
        else:
             return False
# 컴퓨터 입력값
while index < 3:
    number = randint(0, 9)
    if number not in numbers:
        numbers.append(number)
        index += 1
print("0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다.")

while True:
    # 스트라이크 수
    strike = 0
    # 볼 수
    ball = 0
    # 사용자가 입력한 값을 담는 리스트
    user_numbers = []
    print("세 수를 하나씩 차례대로 입력하세요.")
    try_count += 1
    # 3번째 까지 사용자 값 입력 받기
    for i in range(1,4):
        input_num = insert_number(i)
        while condition_selector(user_numbers, input_num) == True:
            if range_test(input_num) == True:
                print("범위를 벗어나는 수 입니다. 다시 입력해주세요.")
            elif duplicate_test(user_numbers, input_num) == True:
                print("중복되는 수 입니다. 다시 입력하세요:")
            input_num = insert_number(i)
        user_numbers.insert(i - 1, input_num)
    for i in range(3):
        if user_numbers[i] == numbers[i]:
            strike += 1
        elif user_numbers[i] != numbers[i] and user_numbers[i] in numbers:
            ball += 1
        index += 1
    print("%dS %dB" % (strike, ball))
    if strike == 3:
        print("축하합니다. %d번만에 세 숫자의 값과 위치를 모두 맞추셨습니다." % (try_count))
        break
