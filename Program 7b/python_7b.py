from tkinter import *
from math import * 
window=Tk()
window.title("Calculator") 
window.geometry("210x200") 
e=Entry(window,bd=8,width=30) 
e.grid(row=0,column=1,columnspan=5) 
def setText(txt):     
    l=len(e.get())     
    e.insert(l,txt) 
def clear1():     
    txt=e.get()     
    e.delete(0,END)     
    e.insert(0,txt[:-1])
            
def clear():     
    e.delete(0,END)         
def sqroot():     
    txt=sqrt(float(e.get()))     
    e.delete(0,END)     
    e.insert(0,txt) 
def negation():     
    txt=e.get()     
    if txt[0]=="-":         
        e.delete(0,END)         
        e.insert(0,txt[1:])     
    elif txt[0]=="+":         
        e.delete(0,END)         
        e.insert(0,"-"+txt[1:])     
    else:
        e.insert(0,"-") 
 
def equals():
        try:
            s=e.get()
            for i in range(0,len(s)): 
                if s[i]=="+" or s[i]=="-" or s[i]=="*" or s[i]=="/" or s[i]=="%":
                    expr=str(float(s[:i]))+s[i:]
                    break             
                # elif s[i]==".": 
                #     expr=s
                #     break
            e.delete(0,END)
            e.insert(0,eval(expr))
        except Exception:
            e.delete(0,END)
            e.insert(0,"INVALID EXPRESSION")

back1=Button(window,text="<--",command=lambda:clear1(),width=10)
back1.grid(row=1,column=1,columnspan=2)
sqr=Button(window,text=u'\u221A',command=lambda:sqroot(),width=4)
sqr.grid(row=1,column=5)
can=Button(window,text="C",command=lambda:clear(),width=4)
can.grid(row=1,column=3)
neg=Button(window,text="+/-",command=lambda:negation(),width=4)
neg.grid(row=1,column=4)
nine=Button(window,text="9",command=lambda:setText("9"),width=4) 
nine.grid(row=2,column=1)
eight=Button(window,text="8",command=lambda:setText("8"),width=4)
eight.grid(row=2,column=2)
seven=Button(window,text="7",command=lambda:setText("7"),width=4)
seven.grid(row=2,column=3)
six=Button(window,text="6",command=lambda:setText("6"),width=4)
six.grid(row=3,column=1) 
five=Button(window,text="5",command=lambda:setText("5"),width=4)
five.grid(row=3,column=2) 
four=Button(window,text="4",command=lambda:setText("4"),width=4)
four.grid(row=3,column=3) 
three=Button(window,text="3",command=lambda:setText("3"),width=4)
three.grid(row=4,column=1)
two=Button(window,text="2",command=lambda:setText("2"),width=4)
two.grid(row=4,column=2) 
one=Button(window,text="1",command=lambda:setText("1"),width=4) 
one.grid(row=4,column=3) 
 
zero=Button(window,text="0",command=lambda:setText("0"),width=10)
zero.grid(row=5,column=1,columnspan=2)
dot=Button(window,text=".",command=lambda:setText("."),width=4)
dot.grid(row=5,column=3)
div=Button(window,text="/",command=lambda:setText("/"),width=4)
div.grid(row=2,column=4) 
mul=Button(window,text="*",command=lambda:setText("*"),width=4)
mul.grid(row=3,column=4)
minus=Button(window,text="-",command=lambda:setText("-"),width=4)
minus.grid(row=4,column=4)
plus=Button(window,text="+",command=lambda:setText("+"),width=4)
plus.grid(row=5,column=4)
mod=Button(window,text="%",command=lambda:setText("%"),width=4)
mod.grid(row=2,column=5)
byx=Button(window,text="1/x",command=lambda:setText("%"),width=4)
byx.grid(row=3,column=5)
equal=Button(window,text="=",command=lambda:equals(),width=4,height=3)
equal.grid(row=4,column=5,rowspan=2) 
window.mainloop()