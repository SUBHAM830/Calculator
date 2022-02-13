


from tkinter import *
root=Tk()
def click(event):
    global scvalue
    text=event.widget.cget("text")
    
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            value=eval(screen.get())
        scvalue.set(value)
        screen.update()
    elif text=="C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()
    pass
root.minsize(100,100)
scvalue=StringVar()
root.title("My Calculator")
#root.wm_iconbitmap("1.ico")
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="lucida 40 bold")
screen.pack(fill=X,ipadx=8,pady=10,padx=10)
frame1=Frame(root,bg="grey")
button1=Button(frame1,text="9",padx=28,pady=10,font="lucida 20 bold")
button1.pack(side="left",padx=18,pady=12)
button1.bind("<Button-1>",click)

button1=Button(frame1,text="8",padx=28,pady=10,font="lucida 20 bold")
button1.pack(side="left",padx=18,pady=12)
button1.bind("<Button-1>",click)

button1=Button(frame1,text="7",padx=28,pady=10,font="lucida 20 bold")
button1.pack(side="left",padx=18,pady=12)
button1.bind("<Button-1>",click)

frame1.pack()

frame1=Frame(root,bg="grey")
button1=Button(frame1,text="6",padx=28,pady=10,font="lucida 20 bold")
button1.pack(side="left",padx=18,pady=12)
button1.bind("<Button-1>",click)

button1=Button(frame1,text="5",padx=28,pady=10,font="lucida 20 bold")
button1.pack(side="left",padx=18,pady=12)
button1.bind("<Button-1>",click)

button1=Button(frame1,text="4",padx=28,pady=10,font="lucida 20 bold")
button1.pack(side="left",padx=18,pady=12)
button1.bind("<Button-1>",click)

frame1.pack()

frame1=Frame(root,bg="grey")
button1=Button(frame1,text="3",padx=28,pady=10,font="lucida 20 bold")
button1.pack(side="left",padx=18,pady=12)
button1.bind("<Button-1>",click)

button1=Button(frame1,text="2",padx=28,pady=10,font="lucida 20 bold")
button1.pack(side="left",padx=18,pady=12)
button1.bind("<Button-1>",click)

button1=Button(frame1,text="1",padx=28,pady=10,font="lucida 20 bold")
button1.pack(side="left",padx=18,pady=12)
button1.bind("<Button-1>",click)

frame1.pack()

frame1=Frame(root,bg="grey")
button1=Button(frame1,text="0",padx=32,pady=10,font="lucida 20 bold")
button1.pack(side="left",padx=18,pady=12)
button1.bind("<Button-1>",click)

button1=Button(frame1,text="-",padx=30,pady=10,font="lucida 20 bold")
button1.pack(side="left",padx=18,pady=12)
button1.bind("<Button-1>",click)

button1=Button(frame1,text="*",padx=28,pady=10,font="lucida 20 bold")
button1.pack(side="left",padx=18,pady=12)
button1.bind("<Button-1>",click)

frame1.pack()

frame1=Frame(root,bg="grey")
button1=Button(frame1,text="/",padx=28,pady=10,font="lucida 20 bold")
button1.pack(side="left",padx=18,pady=12)
button1.bind("<Button-1>",click)

button1=Button(frame1,text="%",padx=28,pady=10,font="lucida 20 bold")
button1.pack(side="left",padx=18,pady=12)
button1.bind("<Button-1>",click)

button1=Button(frame1,text="=",padx=27,pady=10,font="lucida 20 bold")
button1.pack(side="left",padx=18,pady=12)
button1.bind("<Button-1>",click)

frame1.pack()

frame1=Frame(root,bg="grey")
button1=Button(frame1,text="C",padx=57,pady=10,font="lucida 20 bold")
button1.pack(side="left",padx=18,pady=12)
button1.bind("<Button-1>",click)

button1=Button(frame1,text="+",padx=55,pady=10,font="lucida 20 bold")
button1.pack(side="left",padx=18,pady=12)
button1.bind("<Button-1>",click)



frame1.pack()

root.mainloop()







