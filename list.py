numbers = [5, 4, 3, 2, 1]
print(numbers[0])
print(numbers[-1])

#list Slicing
print(numbers[0:4])
print(numbers[2:])
print(numbers[:5])

numbers[0] = 7
print(numbers)

#list Size
print(len(numbers))
[].append
#list 요소추가
numbers.append(5)
print(numbers)
#list 삭제
del(numbers[len(numbers)-1])
print(numbers)

#list 정렬
sorted(numbers)
print(sorted(numbers))

#list 내부 요소 확인

def in_list(some_list, value):
    i = 0
    while i < len(some_list):
        if some_list[i] == value:
            return True
        i = i + 1
    return False
# 테스트
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(in_list(primes, 7))
print(in_list(primes, 12))
print(7 in primes)
print(12 in primes)
print(7 not in primes)
print(12 not in primes)

# Nested List ( 리스트 속 리스트)
grades = [[62, 75, 77], [78, 81, 86], [85, 91, 89]]

print(grades[0])

# 내림차순
numbers = [ 5, 4, 3, 2, 1]
numbers.reverse()
print(numbers)

# 요소 index 확인
members = ["현우", "성민", "승필", "승엽", "지한"]
print(members.index("현우"))

# 요소 제거
members.remove("현우")
print(members)

