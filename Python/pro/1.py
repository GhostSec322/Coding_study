##○ 사용자로부터 2개의 문자열을 입력 받아서 두 문자열의 공통 문자를 출력하는 프로그램 작성
##- 생각하기 : input(), set(), 교집합 연산
str1 =list(input("첫 번째 문자열을 입력하세요:"))
str2 =list(input("두 번째 문자열을 입력하세요:"))
set_str =set(str1) &set(str2)
print(set_str)
