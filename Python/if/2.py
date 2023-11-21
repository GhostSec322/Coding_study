watch_price =int(input("시계의 금액을 입력하세요:"))
bag_price=int(input("가방의 금액을 입력하세요:"))
total_price = watch_price +bag_price
if total_price >=100000:
    print("가격:",total_price-total_price*0.3)
elif total_price>=50000 and total_price<10000:
    print("가격:",total_price-total_price*0.2)
else:
    print("가격:",total_price-total_price*0.1)