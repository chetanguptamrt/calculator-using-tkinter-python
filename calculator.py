from tkinter import *
import tkinter.messagebox as tsmg
import math
import pickle
class Calci_mode:
    def __init__(self,mode=1):
        self.mode=mode
def New():
    screentext.set("")
def Help():
    tsmg.showinfo("Help","Sorry, There are no any kind of help.")
def About():
    tsmg.showinfo("About","This calculator are made by chetan gupta\nVersion - 1.0.1")

#------------------for noraml mode-------------------------------
i=0
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
def design_1():
    global frame_work
    root.geometry("215x320")
    frame_work=Frame(root)
    frame_work.pack()
    screentext.set("")
    textarea=Label(frame_work,textvariable=screentext,font="lucida 14 ",relief=SUNKEN,anchor='e')
    textarea.pack(padx=14,pady=(13,10),side=TOP,fill='x')
    #frame 1
    f1=Frame(frame_work,relief=SUNKEN)
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
    b4=Button(f1,text="C",font="arial 10 bold",padx=11,pady=10,fg='red')
    b4.bind("<Button-1>",add_entry)
    b4.pack(side=LEFT,padx=5)
    #frame 2
    f2=Frame(frame_work)
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
    f3=Frame(frame_work)
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
    f4=Frame(frame_work)
    f4.pack(fill=BOTH,padx=10,pady=5)
    b13=Button(f4,text=".",font="arial 10 bold",padx=10,pady=10)
    b13.bind("<Button-1>",add_entry)
    b13.pack(side=LEFT,padx=5)
    b14=Button(f4,text="0",font="arial 10 bold",padx=12,pady=10)
    b14.bind("<Button-1>",add_entry)
    b14.pack(side=LEFT,padx=5)
    b15=Button(f4,text="*",font="arial 10 bold",padx=11,pady=10)
    b15.bind("<Button-1>",add_entry)
    b15.pack(side=LEFT,padx=5)
    b16=Button(f4,text="/",font="arial 10 bold",padx=13,pady=10)
    b16.bind("<Button-1>",add_entry)
    b16.pack(side=LEFT,padx=5)
    #frame 5
    f5=Frame(frame_work)
    f5.pack(fill=BOTH,padx=10,pady=5)
    b17=Button(f5,text="=",font="arial 10 bold",padx=74,pady=5)
    b17.bind("<Button-1>",add_entry)
    b17.pack(side=LEFT,padx=12)

#---------------- for standard mode------------------------------
j=0
def sec_C():
    screentext.set("")
def sec_back(event=0):
    global j
    j=0
    back=screentext.get()
    screentext.set(back[0:-1])
def sec_solve():
    global j
    texts=screentext.get()
    count1,count2=0,0
    for text in texts:
        if "(" == text:
            count1+=1
        if ")" == text:
            count2+=1
    
    if count1==count2:
        try:
            j=0
            return eval(texts)
        except:
            j=1
            return 0
    else:
        j=1
        return 0
def sec_equal(event=0):
    global j
    if screentext.get()!="":
        screentext.set(sec_solve())
        if j==1:
            screentext.set("Syntax error")
        j=1
def sec_sqr():
    global j
    if screentext.get()!="":
        screentext.set(sec_solve()*sec_solve())
        if j==1:
            screentext.set("Error")
        j=1
def sec_cube():
    global j
    if screentext.get()!="":
        screentext.set(sec_solve()*sec_solve()*sec_solve())
        if j==1:
            screentext.set("Error")
        j=1
def sec_div():
    global j
    if screentext.get()!="":
        screentext.set(1/sec_solve())
        if j==1:
            screentext.set("Error")
        j=1
def sec_per():
    global j
    if screentext.get()!="":
        screentext.set(sec_solve()/100)
        if j==1:
            screentext.set("Error")
        j=1
def sec_fact():
    if screentext.get()!="":
        p=int(sec_solve())
        if p<0:
            screentext.set("ERROR")
        elif p==0:
            screentext.set('1')
        else:
            fact=1
            while p>0:
                fact*=p
                p-=1
            screentext.set(fact)
def sec_ans():
    global j
    j=0
    screentext.set(sec_solve())
def sec_addentry(event=0):
    global screentext,j
    text=event.widget.cget("text")
    if j==1:
        j=0
        screentext.set(text)
    else:
        screentext.set(screentext.get()+text)
def sec_addentry2(event=0):
    global screentext,j
    text=event.char
    try:
        if int(text) in range(0,10):
            if j==1:
                j=0
                screentext.set(text)
            else:
                screentext.set(screentext.get()+text)
    except:
        pass
    try:
        if event.char=="+" or event.char=="-" or event.char=="*" or event.char=="/" or event.char==".":
            if j==1:
                j=0
                screentext.set(text)
            else:
                screentext.set(screentext.get()+text)
    except:
        pass 

def design_2():
    global frame_work
    root.geometry("310x400")
    frame_work=Frame(root)
    frame_work.pack()
    screentext.set("")
    textarea=Label(frame_work,textvariable=screentext,font="lucida 14 ",relief=SUNKEN,anchor='e')
    textarea.pack(padx=14,pady=(13,10),side=TOP,fill='x')

    #frame 1
    f1=Frame(frame_work,relief=SUNKEN)
    f1.pack(fill=BOTH,padx=10,pady=5)
    b123=Label(f1,image=pic)
    b123.pack(side=LEFT,padx=5)
    b4=Button(f1,text="<=",font="arial 10 bold",padx=9,pady=10,command=sec_back)
    b4.pack(side=LEFT,padx=5)
    b5=Button(f1,text="C",font="arial 10 bold",padx=13,pady=10,fg='red',command=sec_C)
    b5.pack(side=LEFT,padx=5)
    #frame 2
    f2=Frame(frame_work,relief=SUNKEN)
    f2.pack(fill=BOTH,padx=10,pady=5)
    b6=Button(f2,text="7",font="arial 10 bold",padx=14,pady=10)
    b6.bind("<Button-1>",sec_addentry)
    b6.pack(side=LEFT,padx=5)
    b7=Button(f2,text="8",font="arial 10 bold",padx=14,pady=10)
    b7.bind("<Button-1>",sec_addentry)
    b7.pack(side=LEFT,padx=5)
    b8=Button(f2,text="9",font="arial 10 bold",padx=14,pady=10)
    b8.bind("<Button-1>",sec_addentry)
    b8.pack(side=LEFT,padx=5)
    b9=Button(f2,text="(",font="arial 10 bold",padx=15,pady=10)
    b9.bind("<Button-1>",sec_addentry)
    b9.pack(side=LEFT,padx=5)
    b10=Button(f2,text=")",font="arial 10 bold",padx=15,pady=10)
    b10.bind("<Button-1>",sec_addentry)
    b10.pack(side=LEFT,padx=5)
    #frame 3
    f3=Frame(frame_work,relief=SUNKEN)
    f3.pack(fill=BOTH,padx=10,pady=5)
    b11=Button(f3,text="4",font="arial 10 bold",padx=14,pady=10)
    b11.bind("<Button-1>",sec_addentry)
    b11.pack(side=LEFT,padx=5)
    b12=Button(f3,text="5",font="arial 10 bold",padx=14,pady=10)
    b12.bind("<Button-1>",sec_addentry)
    b12.pack(side=LEFT,padx=5)
    b13=Button(f3,text="6",font="arial 10 bold",padx=14,pady=10)
    b13.bind("<Button-1>",sec_addentry)
    b13.pack(side=LEFT,padx=5)
    b14=Button(f3,text="/",font="arial 10 bold",padx=15,pady=10)
    b14.bind("<Button-1>",sec_addentry)
    b14.pack(side=LEFT,padx=5)
    b15=Button(f3,text="*",font="arial 10 bold",padx=15,pady=10)
    b15.bind("<Button-1>",sec_addentry)
    b15.pack(side=LEFT,padx=5)
    #frame 4
    f4=Frame(frame_work,relief=SUNKEN)
    f4.pack(fill=BOTH,padx=10,pady=5)
    b16=Button(f4,text="1",font="arial 10 bold",padx=14,pady=10)
    b16.bind("<Button-1>",sec_addentry)
    b16.pack(side=LEFT,padx=5)
    b17=Button(f4,text="2",font="arial 10 bold",padx=14,pady=10)
    b17.bind("<Button-1>",sec_addentry)
    b17.pack(side=LEFT,padx=5)
    b18=Button(f4,text="3",font="arial 10 bold",padx=14,pady=10)
    b18.bind("<Button-1>",sec_addentry)
    b18.pack(side=LEFT,padx=5)
    b19=Button(f4,text="+",font="arial 10 bold",padx=13,pady=10)
    b19.bind("<Button-1>",sec_addentry)
    b19.pack(side=LEFT,padx=5)
    b20=Button(f4,text="-",font="arial 10 bold",padx=15,pady=10)
    b20.bind("<Button-1>",sec_addentry)
    b20.pack(side=LEFT,padx=5)

    #frame 5
    f5=Frame(frame_work,relief=SUNKEN)
    f5.pack(fill=BOTH,padx=10,pady=5)
    b21=Button(f5,text=".",font="arial 10 bold",padx=16,pady=10)
    b21.bind("<Button-1>",sec_addentry)
    b21.pack(side=LEFT,padx=5)
    b22=Button(f5,text="0",font="arial 10 bold",padx=14,pady=10)
    b22.bind("<Button-1>",sec_addentry)
    b22.pack(side=LEFT,padx=5)
    b23=Button(f5,text="00",font="arial 10 bold",padx=10,pady=10)
    b23.bind("<Button-1>",sec_addentry)
    b23.pack(side=LEFT,padx=5)
    b24=Button(f5,text="^2",font="arial 10 bold",padx=10,pady=10,command=sec_sqr)
    b24.pack(side=LEFT,padx=5)
    b25=Button(f5,text="^3",font="arial 10 bold",padx=9,pady=10,command=sec_cube)
    b25.pack(side=LEFT,padx=5)

    #frame 6
    f6=Frame(frame_work,relief=SUNKEN)
    f6.pack(fill=BOTH,padx=10,pady=5)
    b26=Button(f6,text="=",font="arial 10 bold",padx=14,pady=10,command=sec_equal)
    b26.pack(side=LEFT,padx=5)
    b27=Button(f6,text="x!",font="arial 10 bold",padx=11,pady=10,command=sec_fact)
    b27.pack(side=LEFT,padx=5)
    b28=Button(f6,text="1/x",font="arial 10 bold",padx=8,pady=10,command=sec_div)
    b28.pack(side=LEFT,padx=5)
    b29=Button(f6,text="%",font="arial 10 bold",padx=12,pady=10,command=sec_per)
    b29.pack(side=LEFT,padx=5)
    b30=Button(f6,text="Ans",font="arial 10 bold",padx=6,pady=10,command=sec_ans)
    b30.pack(side=LEFT,padx=5)

def change_design():
    global i,frame_work,j
    #load design and open calci
    try:
        frame_work.destroy()
        with open('Assets\\data.dat',mode='wb') as f:
            stu=Calci_mode(design_mode.get())
            pickle.dump(stu,f)
    except:
        pass
    
    root.unbind('<Key>')
    root.unbind('<Return>')
    root.unbind('<BackSpace>')
    with open('Assets\\data.dat',mode='rb') as f:
        obj=pickle.load(f)
        design_mode.set(obj.mode)
    if design_mode.get()==1:
        i=0
        root.bind('<Key>',bindentry)
        root.bind('<Return>',enterentry)
        root.bind('<BackSpace>',backentry)
        design_1()
    elif design_mode.get()==2:
        j=0
        root.bind('<Key>',sec_addentry2)
        root.bind('<Return>',sec_equal)
        root.bind('<BackSpace>',sec_back)
        design_2()

#root
root=Tk()
root.title("calcutator by chetan gupta")
root.resizable(False,False)

#variables
design_mode=IntVar()
screentext=StringVar()

#menu area 
mainmenubar=Menu(root)
m1=Menu(mainmenubar,tearoff=0)
m1.add_command(label="New",command=New)
m1.add_radiobutton(label="Normal",value=1,variable=design_mode,command=change_design)
m1.add_radiobutton(label="Standard",value=2,variable=design_mode,command=change_design)
m1.add_separator()
m1.add_command(label="exit",command=quit)
mainmenubar.add_cascade(label="File",menu=m1)
m2=Menu(mainmenubar,tearoff=0)
m2.add_command(label="Help",command=Help)
m2.add_separator()
m2.add_command(label="About",command=About)
mainmenubar.add_cascade(label="About",menu=m2)
root.config(menu=mainmenubar)
pic=PhotoImage(file="Assets\\logo.png")

change_design()

root.mainloop()