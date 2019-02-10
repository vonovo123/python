in_file = open('vocabulary.txt', 'r')
for line in in_file:
    # 한글 문제
    question_kor = line.strip().split(": ")[1]
    answer = line.strip().split(": ")[0]
    # 답변
    user_answer = input(question_kor+": ")
    if user_answer == answer:
        print("맞았습니다!")
    else:
        print("아쉽습니다. 정답은 %s입니다." % (answer))