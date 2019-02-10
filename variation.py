def x_is_one():
    global x
    x=1
    return x
print(x_is_one())
print("x = " + str(x))

def calculate_seven():
    return int("5") + int(2.0)
    print("럭키 7을 출력합니다.")

print(calculate_seven())


def sum(a, b):
    return a + b

def print_sum(a, b):
    print(a + b)

sum(2, 4)

print(sum(2, 4))

print_sum(2, 4)

print(print_sum(2, 4))

print("정답은 %d %d" %(2, 4))


def multiply_by_two():
    global x
    x = x * 2

def multiply_by_three():
    y = 2
    y = y * 3

x = 2
multiply_by_two()
print(x)

y = 2
multiply_by_three()
print(y)

print("정답은 %d %d %d" %(1, 3, 5))