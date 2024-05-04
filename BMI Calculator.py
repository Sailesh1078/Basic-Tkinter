from tkinter import *

root = Tk()
root.title("BMI Calculator")

def BMI(ht, wt):
    bmi = wt/(ht**2)
    return bmi
def collect():
    ht = float(e1.get())
    wt = float(e2.get())
    bmi = BMI(ht, wt)
    e3.insert(0, round(bmi, 2))
l1 = Label(root, text="Height (in Meters) :")
l1.grid(row=0, column=0) 
e1 = Entry(root, width=35, borderwidth=5)
e1.grid(row=0, column=1, columnspan=1)
l2 = Label(root, text="Weight (in Kg) :")
l2.grid(row=1, column=0)
e2 = Entry(root, width=35, borderwidth=5)
e2.grid(row=1, column=1, columnspan=1)
l3 = Label(root, text="Your BMI Is :")
l3.grid(row=3, column=0)
e3 = Entry(root, width=35, borderwidth=5)
e3.grid(row=3, column=1, columnspan=1)
b1 = Button(root, text="Submit", command=collect).grid(row=2, column=1)


root.mainloop()
