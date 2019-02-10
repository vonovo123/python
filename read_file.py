in_file = open('helloWorld.txt', 'r')
print(type(in_file)) #<class '_io.TextIOWrapper'>
# 빈줄(white space) 출력 \n
# white space 제거
print("     abcd    efgh   abcd ".strip())

for line in in_file:
    print(line.strip())
in_file.close()

#.split() -> 자른 후 리스트로 반환
numbers = "1. 2. 3. 4. 5. 6"
splited_numbers = numbers.split(". ")
print(splited_numbers)
full_name = "Kim, Yuna"

#white space로 split 할 경우 .split() <- 입력값 x

