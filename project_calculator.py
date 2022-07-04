from tkinter import*
from tkinter import messagebox
import tkinter as tk
from turtle import bgcolor

value=""
exp=0
op=""

def btn1_working():
    global value
    value+="1"
    data.set(value)

def btn2_working():
    global value
    value+="2"
    data.set(value)

def btn3_working():
    global value
    value+="3"
    data.set(value)

def btn4_working():
    global value
    value+="4"
    data.set(value)

def btn5_working():
    global value
    value+="5"
    data.set(value)

def btn6_working():
    global value
    value+="6"
    data.set(value)

def btn7_working():
    global value
    value+="7"
    data.set(value)

def btn8_working():
    global value
    value+="8"
    data.set(value)

def btn9_working():
    global value
    value+="9"
    data.set(value)

def btn0_working():
    global value
    value+="0"
    data.set(value)

def btn_plus_working():
    global value,exp,op
    exp=int(value)
    op="+"
    value += "+"
    data.set(value)

def btn_minus_working():
    global value,exp,op
    exp=int(value)
    op="-"
    value += "-"
    data.set(value)

def btn_multi_working():
    global value,exp,op
    exp=int(value)
    op="*"
    value += "*"
    data.set(value)

def btn_divide_working():
    global value,exp,op
    exp=int(value)
    op="/"
    value += "/"
    data.set(value)

def btn_c_working():
    global value,exp,op
    value=""
    exp=0
    op=""
    data.set(value)

def result():
    global value,op,exp
    value2=value
    if (op=="+"):
        split_val=int((value2.split("+")[1]))
        answer=exp+split_val
        data.set(answer)
        value=str(answer)

    elif (op=="-"):
        split_val=int((value2.split("-")[1]))
        answer=exp-split_val
        data.set(answer)
        value=str(answer)

    elif (op=="*"):
        split_val=int((value2.split("*")[1]))
        answer=exp*split_val
        data.set(answer)
        value=str(answer)   

    elif (op=="/"):
        split_val=int((value2.split("/")[1]))
        
        if split_val==0:
            messagebox.showerror("ERROR","Division by 0 not allowed")
            exp=""
            value=""
            data.set(value)
        
        else:
            answer=int(exp/split_val)
            data.set(answer)
            value=str(answer)

window=tk.Tk()
window.geometry("300x400")
window.title("C A L C U L A T O R")

data=StringVar()

lbl=Label(window,text="Label",anchor=SE,font=("Verdana",30),textvariable=data,background="dark grey",fg="black")
lbl.pack(expand=True,fill="both")

btn_row1=Frame(window)
btn_row1.pack(expand=True,fill="both")

btn1=Button(btn_row1,text="7",font=("Verdana",22),relief=GROOVE,border=0,background="grey",command=btn7_working)
btn1.pack(side=LEFT,expand=True,fill="both")
btn2=Button(btn_row1,text="8",font=("Verdana",22),relief=GROOVE,border=0,background="grey",command=btn8_working)
btn2.pack(side=LEFT,expand=True,fill="both")
btn3=Button(btn_row1,text="9",font=("Verdana",22),relief=GROOVE,border=0,background="grey",command=btn9_working)
btn3.pack(side=LEFT,expand=True,fill="both")
btn4=Button(btn_row1,text="=",font=("Verdana",22),relief=GROOVE,border=0,background="orange",command=result)
btn4.pack(side=LEFT,expand=True,fill="both")


btn_row2=Frame(window)
btn_row2.pack(expand=True,fill="both")

btn1=Button(btn_row2,text="4",font=("Verdana",22),relief=GROOVE,border=0,background="grey",command=btn4_working)
btn1.pack(side=LEFT,expand=True,fill="both")
btn2=Button(btn_row2,text="5",font=("Verdana",22),relief=GROOVE,border=0,background="grey",command=btn5_working)
btn2.pack(side=LEFT,expand=True,fill="both")
btn3=Button(btn_row2,text="6",font=("Verdana",22),relief=GROOVE,border=0,background="grey",command=btn6_working)
btn3.pack(side=LEFT,expand=True,fill="both")
btn4=Button(btn_row2,text="C",font=("Verdana",22),relief=GROOVE,border=0,background="grey",command=btn_c_working)
btn4.pack(side=LEFT,expand=True,fill="both")

btn_row3=Frame(window)
btn_row3.pack(expand=True,fill="both")

btn1=Button(btn_row3,text="1",font=("Verdana",22),relief=GROOVE,border=0,background="grey",command=btn1_working)
btn1.pack(side=LEFT,expand=True,fill="both")
btn2=Button(btn_row3,text="2",font=("Verdana",22),relief=GROOVE,border=0,background="grey",command=btn2_working)
btn2.pack(side=LEFT,expand=True,fill="both")
btn3=Button(btn_row3,text="3",font=("Verdana",22),relief=GROOVE,border=0,background="grey",command=btn3_working)
btn3.pack(side=LEFT,expand=True,fill="both")
btn4=Button(btn_row3,text="-",font=("Verdana",22),relief=GROOVE,border=0,background="grey",command=btn_minus_working)
btn4.pack(side=LEFT,expand=True,fill="both")

btn_row4=Frame(window)
btn_row4.pack(expand=True,fill="both")

btn1=Button(btn_row4,text="0",font=("Verdana",22),relief=GROOVE,border=0,background="grey",command=btn0_working)
btn1.pack(side=LEFT,expand=True,fill="both")
btn2=Button(btn_row4,text="*",font=("Verdana",22),relief=GROOVE,border=0,background="grey",command=btn_multi_working)
btn2.pack(side=LEFT,expand=True,fill="both")
btn3=Button(btn_row4,text="/",font=("Verdana",22),relief=GROOVE,border=0,background="grey",command=btn_divide_working)
btn3.pack(side=LEFT,expand=True,fill="both")
btn4=Button(btn_row4,text="+",font=("Verdana",22),relief=GROOVE,border=0,background="grey",command=btn_plus_working)
btn4.pack(side=LEFT,expand=True,fill="both")

window.mainloop()
  











































