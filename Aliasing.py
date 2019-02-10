x = [2, 3, 5, 7, 11]
y = x
y[2] = 4
print(x)
print(y)

# 이미 Aliasing(가명)된 리스트의  요소를 바꾸면 두 변수의 값 모두 변경됨

# aliasing 방지법
x = [2, 3, 5, 7 ,11]
# list 원본을 복사해서 새로운 공간에 붙여놓고, 그 새로운 공간의 리스트를 리턴
y = list(x)
y[2] = 4
print(x)
print(y)