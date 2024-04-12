import tkinter as tk
import random

def select(userRSP):    #select 함수 정의
    randomRSP = random.choice(["가위", "바위", "보"])
    if userRSP == "가위" and randomRSP == "보" or userRSP == "바위" and randomRSP == "가위" or userRSP == "보" and randomRSP == "바위":
        result = "승리"
    elif userRSP == "보" and randomRSP == "가위" or userRSP == "가위" and randomRSP == "바위" or userRSP == "바위" and randomRSP == "보":
        result = "패배"
    else:
        result = "무승부"   #승리/패배/무승부 값을 result에 저장

    userlabel.config(text=userRSP)      #config 함수를 통해 text 변경
    randomlabel.config(text=randomRSP)
    userlabel2.config(text=result)

#select 함수가 끝나면 지역변수기에 값이 사라짐 -> 여기 안에 다 넣어봤는데 글씨 위에 중복되어서 나와서 밖으로 뺌


window=tk.Tk()
window.geometry("340x400")
window.title("240412_파이썬활용과제")

userlabel = tk.Label(window, text="")       #내가 고른거
userlabel.pack()
userlabel.place(x=80, y=200)

randomlabel = tk.Label(window, text="")     #랜덤한거
randomlabel.pack()
randomlabel.place(x=250, y=200)

userlabel2 = tk.Label(window, text="")      #결과
userlabel2.pack()
userlabel2.place(x=120, y=300)
                                            #세가지 목록을 원하는 위치에 띄움


scissorb = tk.Button(window, width=10, height=5, text="가위", command=lambda: select("가위"))      #버튼을 누르면 가위 바위 보를 각각 select에 넣음
scissorb.pack()
rockb = tk.Button(window, width=10, height=5, text="바위", command=lambda: select("바위"))
rockb.pack()
paperb = tk.Button(window, width=10, height=5, text="보", command=lambda: select("보"))
paperb.pack()
scissorb.place(x=10, y=10)
rockb.place(x=130, y=10)
paperb.place(x=250, y=10)


window.mainloop()