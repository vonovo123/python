PI = 3.14
#상수의 표기는 대문자
def calculate_area(r):
    return PI * r * r

radius = 6
print("반지름이 %.f 이면 원 넓이는 %f" % (radius, calculate_area(radius)))