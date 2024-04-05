import random

userlotto = []
for i in range(5):
    inputlotto = input("1~10 까지의 숫자를 골라주세요 : ")
    userlotto.append(int(inputlotto))
print(userlotto)

randlotto = []
for i in range(5):
    randlotto.append(random.randint(1,10))
print(randlotto)

rank = 0
for i in range(5):
    if userlotto[i] == randlotto[i]:
        rank += 1

print(f'''당신의 번호 :     {userlotto}
   당첨번호 :     {randlotto}''')
if rank == 5:
    print("5개의 숫자 전부 맞추셨습니다")
elif rank == 4:
    print("4개 맞추셨습니다")
elif rank == 3:
    print("3개 맞추셨습니다")
elif rank == 2:
    print("2개 맞추셨습니다")
elif rank == 1:
    print("1개 맞추셨습니다")
else:
    print("0개 맞추셨습니다")

#if lotto[0] == lottowin[0]:
    