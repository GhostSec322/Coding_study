price = int(input("현재 가격을 입력하세요:"))
if price >= 90000:
    print("매도 합니다")
elif price >=80000 and price <90000:
    print("대기중입니다")
else: 
    print("매수 합니다")

