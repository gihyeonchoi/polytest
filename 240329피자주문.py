#피자주문
#피자 사이즈 S = 15000원 / M = 20000원 / L = 30000원
#페퍼로니 추가 2천원 , 치즈추가 3천원
pay = 0
pizza = input("피자 사이즈를 골라주세요\n스몰 15000원, 미디엄 20000원, 라지 30000원\nS M L : ")

if pizza == 'S':
    pay += 15000
elif pizza == 'M':
    pay += 20000
elif pizza == 'L':
    pay += 30000
else:
    print("S M L 중 하나를 골라주세요")
    exit()


peppe = input("페퍼로니를 추가하시겠습니까? 2천원이 추가됩니다 Y or N : ")
if peppe == 'Y':
    pay += 2000
    print("페퍼로니 추가 완료")
else:
    print("페퍼로니 선택 안함")

cheese = input("치즈를 추가하시겠습니까? 3천원이 추가됩니다 Y or N : ")
if cheese == 'Y':
    pay += 2000
    print("치즈 추가 완료")
else:
    print("치즈 선택 안함")

print("총 가격은 ",pay,"원 입니다")