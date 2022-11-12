#!C:\Users\82105\AppData\Local\Programs\Python\Python310\python.exe
from tkinter import *
from datetime import datetime
#import tkinter.font

c = Tk() #창생성
c.geometry("800x800")
c.title("What time?")
c.option_add("*Font", "넥센_R 10")


btn = Button(c)

def what_time():
    #print(datetime.now())
    dnow = datetime.now()
    btn.config(text = dnow)

#font = tkinter.font.Font(family="넥센_R", size=10)

#btn.config(text = "현재 시각", font=font)
btn.config(text = "현재 시각")
btn.config(width = 25, height = 5)
btn.config(command = what_time)

btn.pack()

c.mainloop() #창실행
