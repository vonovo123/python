from random import randint
out_file = open("vocabulary.txt", 'r')
dict_diction = {}
key_num = 0
for line in out_file:
    dict_diction[key_num] = line.strip()
    key_num += 1
    # dict_list = line.strip().split(': ')
    # question_kor = dict_list[1]
    # answer_eng = dict_list[0]

while True:
    value = dict_diction[randint(0, key_num - 1)].split(": ")
    question_kor = value[1]
    answer_eng = value[0]
    user_answer = input(question_kor + ": ")
    if user_answer == answer_eng:
        print("맞았습니다!")
    elif user_answer == 'q':
        break
    else:
        print("아쉽습니다. 정답은 %s입니다." % (answer_eng))