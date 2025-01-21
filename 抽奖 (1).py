import tkinter as tk
import random

def callback():
    a=random.randint(1,100)
    if a==1:
        var.set("特等奖\反一秒的武器购物卡")
        label2.config(fg="orange")
    elif 1<a<=10:
        var.set("一等奖\一秒是XXS")
        label2.config(fg="red")
    elif 11<a<=30:
        var.set("二等奖\电击一秒")
        label2.config(fg="blue")
    elif 31<a<=60:
        var.set("三等奖\一秒被XXS反骂")
        label2.config(fg="green")
    else:
        var.set("未中奖\一秒是SB！")
        label2.config(fg="black")
        
root = tk.Tk()
root.geometry("400x200")
label1=tk.Label(root,text="--幸运一秒大抽奖--",font=(None,30))
label1.pack()

var=tk.StringVar()
var.set("奖品展示区")

label2=tk.Label(root,textvariable=var,font=(None,40))
label2.pack(pady=10)

button=tk.Button(root,text="一秒的电坤瞅讲",command=callback,font=(None,10))
button.pack(side="bottom")

root.mainloop()
                

                 
