while True:
    print("[메뉴를 입력하세요]")
    val=int(input("1. 게임시작 2.랭킹보기 3.게임종료>>>"))
    menu=["게임시작","랭킹보기","게임을 종료합니다"]
    if(val ==1 ):
        print("->",menu[val-1])
    elif(val ==2):
        print("->",menu[val-1])
    elif(val ==3):
        print("->",menu[val-1])
        break
    else:
        print("->다시 입력해 주세요")