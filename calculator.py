from tkinter import *
import tkinter.messagebox as tsmg

i=1

def New():
    screentext.set("")
def Help():
    tsmg.showinfo("Help","There are no any kind of help\ntujhe canculater me bhi help chahiye kya ab")
def About():
    tsmg.showinfo("About","This calculator are made by chetan gupta\nplease respect")
def add_entry(event):
    global screentext,i
    text=event.widget.cget("text")
    print(text)
    if text == "C":
        screentext.set("")
    elif text == "=":
        try:
            screentext.set(eval(screentext.get()))
        except:
            screentext.set("Syntax error")
        i=0
    else:
        if i==0:
            screentext.set("")
            i=1
        screentext.set(screentext.get()+text)
def bindentry(event):
    global screentext,i
    try:
        if(int(event.char)<=10):
            if i==0:
                screentext.set("")
                i=1
            screentext.set(screentext.get()+event.char)
    except:
        pass

    try:
        if event.char=="+" or event.char=="-" or event.char=="*" or event.char=="/" or event.char==".":
            if i==0:
                screentext.set("")
                i=1
            screentext.set(screentext.get()+event.char)
    except:
        pass

    try:
        if event.char=="=":
            try:
                screentext.set(eval(screentext.get()))
            except:
                screentext.set("Syntax error")
            i=0
    except:
        pass
    
    try:
        if event.char=="c" or event.char=="C":
            screentext.set("")
    except:
        pass
def enterentry(event):
    global screentext,i
    try:
        screentext.set(eval(screentext.get()))
    except:
        screentext.set("Syntax error")
    i=0   
def backentry(event):
    global screentext
    if i==1:
        back=screentext.get()
        screentext.set(back[0:-1])

#root
root=Tk()
root.geometry("215x320")
root.title("calcutator by chetan gupta")
root.resizable(0,0)

#bind all keys
root.bind('<Key>',bindentry)
root.bind('<Return>',enterentry)
root.bind('<BackSpace>',backentry)

#menu area 
mainmenubar=Menu(root)

m1=Menu(mainmenubar,tearoff=0)
m1.add_command(label="New",command=New)
m1.add_separator()
m1.add_command(label="exit",command=quit)
mainmenubar.add_cascade(label="File",menu=m1)

m2=Menu(mainmenubar,tearoff=0)
m2.add_command(label="Help",command=Help)
m2.add_separator()
m2.add_command(label="About",command=About)
mainmenubar.add_cascade(label="About",menu=m2)

root.config(menu=mainmenubar)

#text area 
screentext=StringVar()

textarea=Label(root,textvariable=screentext,font="lucida 14 ",relief=SUNKEN)
textarea.pack(padx=14,pady=(10,5),side=TOP,anchor='ne',fill='x')

#frame 1
f1=Frame(root,relief=SUNKEN)
f1.pack(fill=BOTH,padx=10,pady=5)

b1=Button(f1,text="7",font="arial 10 bold",padx=10,pady=10)
b1.bind("<Button-1>",add_entry)
b1.pack(side=LEFT,padx=5)

b2=Button(f1,text="8",font="arial 10 bold",padx=10,pady=10)
b2.bind("<Button-1>",add_entry)
b2.pack(side=LEFT,padx=5)

b3=Button(f1,text="9",font="arial 10 bold",padx=10,pady=10)
b3.bind("<Button-1>",add_entry)
b3.pack(side=LEFT,padx=5)

b4=Button(f1,text="C",font="arial 10 bold",padx=11,pady=10)
b4.bind("<Button-1>",add_entry)
b4.pack(side=LEFT,padx=5)

#frame 2
f2=Frame(root)
f2.pack(fill=BOTH,padx=10,pady=5)

b5=Button(f2,text="4",font="arial 10 bold",padx=10,pady=10)
b5.bind("<Button-1>",add_entry)
b5.pack(side=LEFT,padx=5)

b6=Button(f2,text="5",font="arial 10 bold",padx=10,pady=10)
b6.bind("<Button-1>",add_entry)
b6.pack(side=LEFT,padx=5)

b7=Button(f2,text="6",font="arial 10 bold",padx=10,pady=10)
b7.bind("<Button-1>",add_entry)
b7.pack(side=LEFT,padx=5)

b8=Button(f2,text="+",font="arial 10 bold",padx=11,pady=10)
b8.bind("<Button-1>",add_entry)
b8.pack(side=LEFT,padx=5)

#frame 3
f3=Frame(root)
f3.pack(fill=BOTH,padx=10,pady=5)

b9=Button(f3,text="1",font="arial 10 bold",padx=10,pady=10)
b9.bind("<Button-1>",add_entry)
b9.pack(side=LEFT,padx=5)

b10=Button(f3,text="2",font="arial 10 bold",padx=10,pady=10)
b10.bind("<Button-1>",add_entry)
b10.pack(side=LEFT,padx=5)

b11=Button(f3,text="3",font="arial 10 bold",padx=10,pady=10)
b11.bind("<Button-1>",add_entry)
b11.pack(side=LEFT,padx=5)

b12=Button(f3,text="-",font="arial 10 bold",padx=13,pady=10)
b12.bind("<Button-1>",add_entry)
b12.pack(side=LEFT,padx=5)

#frame 4
f4=Frame(root)
f4.pack(fill=BOTH,padx=10,pady=5)

b13=Button(f4,text="0",font="arial 10 bold",padx=10,pady=10)
b13.bind("<Button-1>",add_entry)
b13.pack(side=LEFT,padx=5)

b14=Button(f4,text=".",font="arial 10 bold",padx=12,pady=10)
b14.bind("<Button-1>",add_entry)
b14.pack(side=LEFT,padx=5)

b15=Button(f4,text="*",font="arial 10 bold",padx=11,pady=10)
b15.bind("<Button-1>",add_entry)
b15.pack(side=LEFT,padx=5)

b16=Button(f4,text="/",font="arial 10 bold",padx=13,pady=10)
b16.bind("<Button-1>",add_entry)
b16.pack(side=LEFT,padx=5)

#frame 5
f5=Frame(root)
f5.pack(fill=BOTH,padx=10,pady=5)

b17=Button(f5,text="=",font="arial 10 bold",padx=74,pady=5)
b17.bind("<Button-1>",add_entry)
b17.pack(side=LEFT,padx=12)

root.mainloop()