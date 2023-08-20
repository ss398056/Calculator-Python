from tkinter import *
from tkinter import messagebox
def addOneVal(event) :
    output.insert(INSERT,1)

def addTwoVal(event) :
    output.insert(INSERT,2)

def addThreeVal(event) :
    output.insert(INSERT,3)

def addFourVal(event) :
    output.insert(INSERT,4)

def addFiveVal(event) :
    output.insert(INSERT,5)

def addSixVal(event) :
    output.insert(INSERT,6)

def addSevenVal(event) :
    output.insert(INSERT,7)

def addEightVal(event) :
    output.insert(INSERT,8)

def addNineVal(event) :
    output.insert(INSERT,9)

def addZeroVal(event) :
    output.insert(INSERT,0)

def addPlusVal(event) :
    output.insert(INSERT,'+')

def addSubVal(event) :
    output.insert(INSERT,'-')

def addMulVal(event) :
    output.insert(INSERT,'*')

def addDivVal(event) :
    output.insert(INSERT,'/')
    
def addModVal(event) :
    output.insert(INSERT,"%")    

def addDotVal(event) :
    output.insert(INSERT,".")

def addPowerVal(event) :
    output.insert(INSERT,"**")
    
def outputClear(event) :
    output.delete(0,END)

def outputSingleClear(event) :
    count = output.get()
    output.delete(len(count)-1)

def calculate(even) :
    try :
        newOutput = eval(output.get())
        output.delete(0,END)
        output.insert(INSERT,newOutput)
    except ArithmeticError:
        output.delete(0,END)
        messagebox.showerror("Error","Can not perform this operation")
    except SyntaxError:
        output.delete(0,END)
        messagebox.showerror("Error","Can not perform this operation")
            
frame = Tk()
frame.geometry("300x320+500+100")
img = PhotoImage(file="calculator-icon.png")
frame.iconphoto(False,img)
frame.title("Calculator")
frame.configure(bg="grey")

output = Entry(frame, width=15 ,font=("Arial Black",20))
output.place(x=10,y=5)

ac = Button(frame, text="AC", width=3, font=("Arial Black",15))
ac.place(x=15,y=50)

c = Button(frame, text="X>", width=3, font=("Arial Black",15))
c.place(x=90,y=50)

mod = Button(frame, text="%", width=3, font=("Arial Black",15))
mod.place(x=165,y=50)

div = Button(frame, text="/", width=3, font=("Arial Black",15))
div.place(x=230,y=50)

seven = Button(frame, text="7", width=3, font=("Arial Black",15))
seven.place(x=15,y=100)

eight = Button(frame, text="8", width=3, font=("Arial Black",15))
eight.place(x=90,y=100)

nine = Button(frame, text="9", width=3, font=("Arial Black",15))
nine.place(x=165,y=100)

mul = Button(frame, text="*", width=3, font=("Arial Black",15))
mul.place(x=230,y=100)

four = Button(frame, text="4", width=3, font=("Arial Black",15))
four.place(x=15,y=150)

five = Button(frame, text="5", width=3, font=("Arial Black",15))
five.place(x=90,y=150)

six = Button(frame, text="6", width=3, font=("Arial Black",15))
six.place(x=165,y=150)

sub = Button(frame, text="-", width=3, font=("Arial Black",15))
sub.place(x=230,y=150)

one = Button(frame, text="1", width=3, font=("Arial Black",15))
one.place(x=15,y=200)

two = Button(frame, text="2", width=3, font=("Arial Black",15))
two.place(x=90,y=200)

three = Button(frame, text="3", width=3, font=("Arial Black",15))
three.place(x=165,y=200)

add = Button(frame, text="+", width=3, font=("Arial Black",15))
add.place(x=230,y=200)

pw = Button(frame, text="^", width=3, font=("Arial Black",15))
pw.place(x=15,y=250)

zero = Button(frame, text="0", width=3, font=("Arial Black",15))
zero.place(x=90,y=250)

dot = Button(frame, text=".", width=3, font=("Arial Black",15))
dot.place(x=165,y=250)

eq = Button(frame, text="=", width=3, font=("Arial Black",15))
eq.place(x=230,y=250)


one.bind('<Button-1>',addOneVal)
two.bind('<Button-1>',addTwoVal)
three.bind('<Button-1>',addThreeVal)
four.bind('<Button-1>',addFourVal)
five.bind('<Button-1>',addFiveVal)
six.bind('<Button-1>',addSixVal)
seven.bind('<Button-1>',addSevenVal)
eight.bind('<Button-1>',addEightVal)
nine.bind('<Button-1>',addNineVal)
zero.bind('<Button-1>',addZeroVal)
add.bind('<Button-1>',addPlusVal)
mul.bind('<Button-1>',addMulVal)
sub.bind('<Button-1>',addSubVal)
div.bind('<Button-1>',addDivVal)
ac.bind('<Button-1>',outputClear)
c.bind('<Button-1>',outputSingleClear)
eq.bind('<Button-1>',calculate)
mod.bind('<Button-1>',addModVal)
dot.bind('<Button-1>',addDotVal)
pw.bind('<Button-1>',addPowerVal)


frame.mainloop()