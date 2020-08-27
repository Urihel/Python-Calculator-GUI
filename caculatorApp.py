from tkinter import *
import tkinter.font as font
root= Tk()

root.title = "CalcApp"
myFont = font.Font(size=18)
e = Entry(root,width=52,borderwidth=5)
e.grid(row=0,columnspan=3,padx=10,pady=10)


def buttonAdd():
    print("Button are working")


btn1 = Button(root,text="1",padx=31,pady=20,command=buttonAdd,bg="#00E0FF",fg="white" )
btn2 = Button(root,text="2",padx=31,pady=20,command=buttonAdd,bg="#00E0FF",fg="white")
btn3 = Button(root,text="3",padx=31,pady=20,command=buttonAdd,bg="#00E0FF",fg="white")
btn4 = Button(root,text="4",padx=31,pady=20,command=buttonAdd,bg="#00E0FF",fg="white")
btn5 = Button(root,text="5",padx=31,pady=20,command=buttonAdd,bg="#00E0FF",fg="white")
btn6 = Button(root,text="6",padx=31,pady=20,command=buttonAdd,bg="#00E0FF",fg="white")
btn7 = Button(root,text="7",padx=31,pady=20,command=buttonAdd,bg="#00E0FF",fg="white")
btn8 = Button(root,text="8",padx=31,pady=20,command=buttonAdd,bg="#00E0FF",fg="white")
btn9 = Button(root,text="9",padx=31,pady=20,command=buttonAdd,bg="#00E0FF",fg="white")
btn0 = Button(root,text="0",padx=31,pady=20,command=buttonAdd,bg="#00E0FF",fg="white")

btnList = [btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn0]
for i in range(0,10):
    btnList[i]['font'] = myFont
               
btn1.grid(row=3,column=0)
btn2.grid(row=3,column=1)
btn3.grid(row=3,column=2)

btn4.grid(row=2,column=0)
btn5.grid(row=2,column=1)
btn6.grid(row=2,column=2)

btn7.grid(row=1,column=0)
btn8.grid(row=1,column=1)
btn9.grid(row=1,column=2)

btn0.grid(row=4,column=1)




root.mainloop()
