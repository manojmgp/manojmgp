from tkinter import*
root=Tk()
input=Entry(root,width=50)
input.grid(row=0,column=0,columnspan=3,padx=15,pady=15)
def click(num):
    current=input.get()
    input.delete(0,END)
    input.insert(0,str(current) + str(num))
    return
def add():
    current=input.get()
    global fnum
    fnum=int(current)
    input.delete(0,END)
    return
def clear():
    input.delete(0, END)
    return
def equal():
    current=input.get()
    snum=int(current)
    input.delete(0,END)
    input.insert(0,str(fnum + snum))
    return
btn_1=Button(root,text="1",padx=50,pady=25,command=lambda :click(1))
btn_2=Button(root,text="2",padx=50,pady=25,command=lambda :click(2))
btn_3=Button(root,text="3",padx=50,pady=25,command=lambda :click(3))
btn_4=Button(root,text="4",padx=50,pady=25,command=lambda :click(4))
btn_5=Button(root,text="5",padx=50,pady=25,command=lambda :click(5))
btn_6=Button(root,text="6",padx=50,pady=25,command=lambda :click(6))
btn_7=Button(root,text="7",padx=50,pady=25,command=lambda :click(7))
btn_8=Button(root,text="8",padx=50,pady=25,command=lambda :click(8))
btn_9=Button(root,text="9",padx=50,pady=25,command=lambda :click(9))
btn_0=Button(root,text="0",padx=50,pady=25,command=lambda :click(0))
btn_add=Button(root,text="+",padx=106,pady=25,command=add)
btn_clear=Button(root,text="AC",padx=45,pady=25,command=clear)
btn_Eq=Button(root,text="=",padx=106,pady=25,command=equal)

btn_7.grid(row=1,column=0)
btn_8.grid(row=1,column=1)
btn_9.grid(row=1,column=2)
btn_4.grid(row=2,column=0)
btn_5.grid(row=2,column=1)
btn_6.grid(row=2,column=2)
btn_1.grid(row=3,column=0)
btn_2.grid(row=3,column=1)
btn_3.grid(row=3,column=2)
btn_0.grid(row=4,column=0)
btn_add.grid(row=4,column=1,columnspan=2)
btn_clear.grid(row=5,column=0)
btn_Eq.grid(row=5,column=1,columnspan=2)



root.mainloop()