from random import randint

try_count = 0
collect_answer = randint(1, 20)

while True:

    if try_count != 4:
        answer = int(input("기회가 %d번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: " % (4 - try_count)))
        if answer < collect_answer:
            print("Up")
            try_count += 1
        elif answer > collect_answer:
            print("Down")
            try_count += 1
        elif answer == collect_answer:
            try_count += 1
            print("축하합니다. %d번만에 숫자를 맞추셨습니다" %(try_count))
            break
    else:
        print("아쉽습니다. 정답은 %d 였습니다." % (collect_answer))
        break
