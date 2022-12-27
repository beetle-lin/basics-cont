from lib2to3.pgen2.token import MINUS
import tkinter as tk
from tkinter import *

jerry = tk.Tk()
jerry.geometry("170x230")
jerry.title("calculator")
jerry.maxsize(170,230)
#jerry.minisize(170,230)


inp = Entry(jerry, width=16,borderwidth=3,relief=RIDGE)
inp.grid(pady=10,row=0,sticky="w",padx=15)




def result():
    try:
        if inp.get() == "":
            inp.insert("end","error")
        elif inp.get()[0]=="0":
            inp.delete(0,"end")
            inp.insert("end","error")
                    
                    
        else:
            res = inp.get()
            res = eval(res)
            input.insert("end","=")
            input.insert("end",res)
    except SyntaxError:
        inp.insert("end","invalid input") 
        
        
        
        
        
clear = Button(jerry, text="C",width=2,command=lambda:inp.delete(0,"end"),bg="red",fg="white",relief=RIDGE)
clear.grid(row=0,sticky="w",padx=125)


nine= Button(jerry, text="9",width=2,command=lambda:inp.delete("end","9"),borderwidth=3,relief=RIDGE)
nine.grid(row=1,sticky="w",padx=15)


eight= Button(jerry, text="8",width=2,command=lambda:inp.delete("end","8"),borderwidth=3,relief=RIDGE)
eight.grid(row=1,sticky="w",padx=45)


seven= Button(jerry, text="7",width=2,command=lambda:inp.delete("end","7"),borderwidth=3,relief=RIDGE)
seven.grid(row=1,sticky="w",padx=75)


plus= Button(jerry, text="+",width=2,command=lambda:inp.delete("end","+"),borderwidth=3,relief=RIDGE)
plus.grid(row=1,sticky="e",padx=125)


six= Button(text="6",width=2,command=lambda:inp.delete("end","6 "),borderwidth=3,relief=RIDGE)
six.grid(row=2,sticky="w",padx=15,pady=5)


five= Button(text="5",width=2,command=lambda:inp.delete("end","5"),borderwidth=3,relief=RIDGE)
five.grid(row=2,sticky="w",padx=45,pady=5)


four = Button(text="4",width=2,command=lambda:inp.delete("end","4"),borderwidth=3,relief=RIDGE)
four.grid(row=2,sticky="w",padx=75,pady=5)


MINUS= Button(text="-",width=2,command=lambda:inp.delete("end","-"),borderwidth=3,relief=RIDGE)
MINUS.grid(row=2,sticky="e",padx=45,pady=5)


three= Button(text="3",width=2,command=lambda:inp.delete("end","3"),borderwidth=3,relief=RIDGE)
three.grid(row=3,sticky="w",padx=15,pady=5)


two= Button(text="2",width=2,command=lambda:inp.delete("end","2"),borderwidth=3,relief=RIDGE)
two.grid(row=3,sticky="w",padx=45,pady=5)


one= Button(text="1",width=2,command=lambda:inp.delete("end","1"),borderwidth=3,relief=RIDGE)
one.grid(row=3,sticky="w",padx=75,pady=5)


multiply= Button(jerry,text="*",width=2,command=lambda:inp.delete("end","*"),borderwidth=3,relief=RIDGE)
multiply.grid(row=2,sticky="e",padx=125,pady=5)


zero= Button(text="0",width=2,command=lambda:inp.delete("end","0"),borderwidth=3,relief=RIDGE)
zero.grid(row=4,sticky="w",padx=15,pady=5)


double_zero= Button(text="00",width=2,command=lambda:inp.delete("end","00"),borderwidth=3,relief=RIDGE)
double_zero.grid(row=4,sticky="w",padx=45,pady=5)


dot= Button(jerry,text=".",width=2,command=lambda:inp.delete("end","."),borderwidth=3,relief=RIDGE)
dot.grid(row=4,sticky="w",padx=75,pady=5)


divide= Button(jerry,text="/",width=2,command=lambda:inp.delete("end","/"),borderwidth=3,relief=RIDGE)
divide.grid(row=4,sticky="w",padx=125,pady=5)


Result= Button(jerry,text="=",width=10,command=result,bg="red", fg="white",borderwidth=3,relief=RIDGE)
Result.grid(row=5,sticky="w",padx=15,pady=5)


modulus= Button(jerry,text="%",width=2,command=lambda:inp.delete("end","%"),borderwidth=3,relief=RIDGE)
modulus.grid(row=5,sticky="e",padx=1255,pady=5)





jerry.mainloop()