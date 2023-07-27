'''
프로그램은 기본적으로 위에서 아래로 순차적으로 실행
명령 A,B중 한개를 선택해 실행하고 싶을때- 조건문 사용
명령을 반복하고 싶을떄- 반복문 사용

'''
Origin_password="1234"
input_password=input("비밀번호를 입력하세요 >>")
if Origin_password==input_password:
    print("로그인성공")
elif input_password=='':
    print("입력을 해주세요")
else:
    print("로그인 실패: 존재하지 않는 계정입니다.")