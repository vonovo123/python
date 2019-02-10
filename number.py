print(5)
print(3 + 7)

#정수형 & 소수형 연산 => 소수형
#나눗셈은 모두 소수형 결과값 return
print(5/3)
print("hello "*3)
print("codeit")
print('유재석')
# "3" = 5 -> error

print(int(3.8))
print(float(3))
print(int("2") + int("5"))
print(float("1") + float("2"))

print(str(2) + str(5))

#python 에서는 문자열과 숫자를 그냥 이어 붙일 수 없음
print("제 나이는 " + str(7) + "살 입니다")

year = 2018
month = 12
day = 30
day_of_week = "일"


print("오늘은 %d년 %d월 %d일 %s요일입니다." % (year, month , day , day_of_week))
print("오늘은 %d년 %d월 %d일 %s요일입니다." % (year, month , day+1 , "월"))
print("1 나누기 3 은 %.1f" % (1/3))

print(type(1))
print(type(1.0))
print(type("1"))
print(type(True))
print(True or False)
print(False == False)