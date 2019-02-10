# 인스턴스를 파라미터로 사용할 시 self 라고 쓰자
class User:
    def say_my_name(self):
        print("My name is " + self.name)

user1 = User()
print(type(user1))
# __main__.User 실행한 파일의 User Class

user1 = User()
user2 = User()
print(user1 == user2) # False

x = User()
y = x
print(x == y) # True

user1.name = "Young"
user1.email = "yong@codein.kr"
user1.password = "123456"


# 메서드를 사용할때는 인스턴스가 아닌 Class를 활용해아한다는 점
User.say_my_name(user1)
# 파라미터가 인스턴스 일때 이렇게도 가능 : Syntactic Sugar
user1.say_my_name()
# 이때 파라미터 넣으면 오류
print(user1.name, user1.email, user1.password)
from user import User
user2 = User()
print(type(user2))
# user.User user 파일의 User Class