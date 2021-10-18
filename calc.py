from tkinter import *
top=Tk()
top.geometry("250x250")
top.title("CALUCLATOR")
exp =" "
def click(val):
    global exp
    exp = exp+str(val)
    eqn.set(exp)
def clear():
    global exp
    exp = ""
    eqn.set("exp")
def click_equal():
    try:
        global exp
        result= str(eval(exp))
        eqn.set(result)
        
    except:
        eqn.set(" syntax error ")
        exp = ""
eqn=StringVar()
expression_entry = Entry(top, text=eqn,width=15,bg="blue",fg='black').place(x=0,y=3)
b0=Button(top,text="0",bg="yellow",fg="blue",height=1,width=4,command=lambda:click(0)).grid(row=0,column=3)
b1=Button(top,text="1",bg="yellow",fg="blue",height=1,width=4,command=lambda:click(1)).grid(row=0,column=4)
b2=Button(top,text="2",bg="yellow",fg="blue",height=1,width=4,command=lambda:click(2)).grid(row=0,column=5)
b3=Button(top,text="3",bg="yellow",fg="blue",height=1,width=4,command=lambda:click(3)).grid(row=1,column=1)
b4=Button(top,text="4",bg="yellow",fg="blue",height=1,width=4,command=lambda:click(4)).grid(row=1,column=2)
b5=Button(top,text="5",bg="yellow",fg="blue",height=1,width=4,command=lambda:click(5)).grid(row=1,column=3)
b6=Button(top,text="6",bg="yellow",fg="blue",height=1,width=4,command=lambda:click(6)).grid(row=1,column=4)
b7=Button(top,text="7",bg="yellow",fg="blue",height=1,width=4,command=lambda:click(7)).grid(row=1,column=5)
b8=Button(top,text="8",bg="yellow",fg="blue",height=1,width=4,command=lambda:click(8)).grid(row=2,column=1)
b9=Button(top,text="9",bg="yellow",fg="blue",height=1,width=4,command=lambda:click(9)).grid(row=2,column=2)
b_multi=Button(top,text="X",bg="yellow",fg="blue",height=1,width=4,command=lambda:click("*")).grid(row=2,column=3)
b_plus=Button(top,text="+",bg="yellow",fg="blue",height=1,width=4,command=lambda:click("+")).grid(row=2,column=4)
b_sub=Button(top,text="-",bg="yellow",fg="blue",height=1,width=4,command=lambda:click("-")).grid(row=2,column=5)
b_div=Button(top,text="/",bg="yellow",fg="blue",height=1,width=4,command=lambda:click("/")).grid(row=3,column=1)
b_dot=Button(top,text=".",bg="yellow",fg="blue",height=1,width=4,command=lambda:click(".")).grid(row=3,column=2)
b_mod=Button(top,text="%",bg="yellow",fg="blue",height=1,width=4,command=lambda:click("%")).grid(row=3,column=3)
b_clear=Button(top,text="C",bg="yellow",fg="blue",height=1,width=4,command=clear).grid(row=3,column=4)
b_equal=Button(top,text="=",bg="yellow",fg="blue",height=1,width=4,command=click_equal).grid(row=3,column=5)
lb1=Label(text="DEVELOPED BY SATHVIK",bg="red",fg='blue').place(x=0,y=120)
top.mainloop()