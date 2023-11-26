
#단어가 나타나는 횟수인 빈도를 계산하는 기법은 종종 텍스트를 분석하는데 사용된다. 출판물의 단어
#빈도를 다른 출판물과 비교하면 유사점을 찾을 수도 있다. 텍스트 데이터(text_data)를 토대로 각 단어의
#빈도(횟수)를 계산하는 프로그램을 작성해보자. 딕셔너리 사용!!
#- text_data = ＂Create the height, grandest vision possible for your life, because you
#become what you believe.＂
#- 생각하기 : 공백 딕셔너리 생성, for문, 문장을 단어로 분리(text_data.split()), if ~ else문, for문, word_dic.items()


text_data = "Create the height, grandest vision possible for your life, because you become what you believe."
word_list = text_data.split(' ')

word_freq = {}  # 빈 딕셔너리 생성

for word in word_list:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

for word in word_freq.keys():
    print(word ,"의 등장횟수 =",word_freq[word])
