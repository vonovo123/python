vocabulary_file = open("vocabulary.txt", 'w')
while True:
    input_eng = input("영어 단어를 입력하세요:")
    if input_eng == 'q':
        vocabulary_file.close()
        break
    input_kor = input("한국어 뜻을 입력하세요:")
    vocabulary_file.write(input_eng + ": " + input_kor + "\n")
