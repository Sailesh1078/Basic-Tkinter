from tkinter import *
root = Tk()
root.title("MARKSHEET")
root.geometry("700x250")
e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
e4 = Entry(root)
e5 = Entry(root)
e6 = Entry(root)
e7 = Entry(root)
def display():
    tot = 0 
    if e4.get() == "S" :
        Label(root, text ="40").grid(row=3, column=4)
        tot += 40
    elif e4.get() == "A" :
        Label(root, text ="36").grid(row=3, column=4)
        tot += 36
    elif e4.get() == "B" :
        Label(root, text ="32").grid(row=3, column=4)
        tot += 32 
    elif e4.get() == "C" :
        Label(root, text ="28").grid(row=3, column=4)
        tot += 28
    elif e4.get() == "D" :
        Label(root, text ="24").grid(row=3, column=4)
        tot += 24
    elif e4.get() == "E" :
        Label(root, text ="20").grid(row=3, column=4)
        tot += 20
    else:
        Label(root, text ="0").grid(row=3, column=4)
        tot += 0
    if e5.get() == "S" :
        Label(root, text ="40").grid(row=3, column=4)
        tot += 40
    elif e5.get() == "A" :
        Label(root, text ="36").grid(row=4, column=4)
        tot += 36
    elif e5.get() == "B" :
        Label(root, text ="32").grid(row=4, column=4)
        tot += 32 
    elif e5.get() == "C" :
        Label(root, text ="28").grid(row=4, column=4)
        tot += 28
    elif e5.get() == "D" :
        Label(root, text ="24").grid(row=4, column=4)
        tot += 24
    elif e5.get() == "E" :
        Label(root, text ="20").grid(row=4, column=4)
        tot += 20
    else:
        Label(root, text ="0").grid(row=4, column=4)
        tot += 0
    if e6.get() == "S" :
        Label(root, text ="40").grid(row=5, column=4)
        tot += 40
    elif e6.get() == "A" :
        Label(root, text ="36").grid(row=5, column=4)
        tot += 36
    elif e6.get() == "B" :
        Label(root, text ="32").grid(row=5, column=4)
        tot += 32 
    elif e6.get() == "C" :
        Label(root, text ="28").grid(row=5, column=4)
        tot += 28
    elif e6.get() == "D" :
        Label(root, text ="24").grid(row=5, column=4)
        tot += 24
    elif e6.get() == "E" :
        Label(root, text ="20").grid(row=5, column=4)
        tot += 20
    else:
        Label(root, text ="0").grid(row=5, column=4)
        tot += 0
    if e7.get() == "S" :
        Label(root, text ="40").grid(row=6, column=4)
        tot += 40
    elif e7.get() == "A" :
        Label(root, text ="36").grid(row=6, column=4)
        tot += 36
    elif e7.get() == "B":
        Label(root, text ="32").grid(row=6, column=4)
        tot += 32
    elif e7.get() == "C" :
        Label(root, text ="28").grid(row=6, column=4)
        tot += 28
    elif e7.get() == "D" :
        Label(root, text ="24").grid(row=6, column=4)
        tot += 24
    elif e7.get() == "E" :
        Label(root, text ="20").grid(row=6, column=4)
        tot += 20
    else :
        Label(root, text ="0").grid(row=6, column=4)
        tot += 0
    Label(root, text=str(round(tot,2))).grid(row=7, column=4)
    Label(root, text=str(tot/15)).grid(row=8, column=4)
Label(root, text="Name").grid(row=0, column=0)
Label(root, text="Reg.No").grid(row=0, column=3)
Label(root, text="Roll.No").grid(row=1, column=0)
Label(root, text="Srl.No").grid(row=2, column=0)
Label(root, text="1").grid(row=3, column=0)
Label(root, text="2").grid(row=4, column=0)
Label(root, text="3").grid(row=5, column=0)
Label(root, text="4").grid(row=6, column=0)
Label(root, text="Subject").grid(row=2, column=1)
Label(root, text="CS 201").grid(row=3, column=1)
Label(root, text="CS 202").grid(row=4, column=1)
Label(root, text="MA 201").grid(row=5, column=1)
Label(root, text="EC 201").grid(row=6, column=1)
Label(root, text="Grade").grid(row=2, column=2)
e4.grid(row=3, column=2)
e5.grid(row=4, column=2)
e6.grid(row=5, column=2)
e7.grid(row=6, column=2) 
Label(root, text="Sub Credit").grid(row=2, column=3)
Label(root, text="4").grid(row=3, column=3)
Label(root, text="4").grid(row=4, column=3)
Label(root, text="3").grid(row=5, column=3)
Label(root, text="4").grid(row=6, column=3)
Label(root, text="Credit Obtained").grid(row=2, column=4)
e1=Entry(root)
e2=Entry(root)
e3=Entry(root)
e1.grid(row=0, column=1)
e2.grid(row=0, column=4)
e3.grid(row=1, column=1)
button1 = Button(root, text="Submit", bg="green", command=display)
button1.grid(row=8, column=2)

root.mainloop()
