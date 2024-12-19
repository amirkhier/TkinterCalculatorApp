from tkinter import *
from sympy import sympify
root = Tk()

#functions
#get number function from buttons numbers
index = 0
def get_number(number):
    global index
    display.insert(index,number)
    index+=1

#get Operations:
def get_op(operation):
    global index
    length = len(operation)
    display.insert(index,operation)
    index+=length
#reset display:
def reset():
    global index
    display.delete(0,index)
#result equal display
def equal():
    global index
    str1 = display.get()
    try:
        result = sympify(str1)
        #deleting all
        display.delete(0,index)
        #then displaying the result:
        res = f"={result}"
        display.insert(0,res)
    except Exception:
        display.delete(0,index)
        display.insert(0,"Error")
    
#get zero number:
def zero():
    global index
    display.insert(index,"0")
    index+=1

#get point :
def point():
    global index
    display.insert(index,".")
    index+=1
#delete one char:
def remove():
    str1 = display.get()
    if len(str1):
        str2 = str1[:-1]
        reset()
        display.insert(0,str2)
    else:
        reset()
        display.insert(0,"")



display = Entry(root)
display.grid(row=0,columnspan=6)
#displaying the the numbers buttons
i = 0
numbers = [i+1 for i in range(9)]
for x in range(3):
    for y in range(3):
        #defining button
        button_number = numbers[i]
        button = Button(root,text=f"{button_number}", width=3,height=2,command=lambda NumDis=button_number:get_number(NumDis) )
        button.grid(row=x+2,column=y)
        i+=1

#adding clear button:
clear = Button(root,text="C", width=3,height=2,command=reset)
clear.grid(row=5,column=0)
#adding the zero button 
button = Button(root,text="0", width=3,height=2,command=zero)
button.grid(row=5,column=1)
#adding the equal button:
equal= Button(root,text="=", width=3,height=2,command=equal)
equal.grid(row=5,column=2)
#adding the operators buttons
#defining operations list
operations = ["+","-","*","/","*3.14","%","(","**",")","**2"]
count = 0
for x in range(4):
    for y in range(3):
        if count < len(operations):
            op_text = operations[count]
            button = Button(root,text=op_text,width=3,height=2,command=lambda op = op_text:get_op(op))
            count+=1
            button.grid(row=x+2,column=y+3)

#adding point button:
point= Button(root,text=".", width=3,height=2,command=point)
point.grid(row=5,column=4)
#adding Exit button:
backspace= Button(root,text="<-", width=3,height=2,command=remove)
backspace.grid(row=5,column=5)
root.mainloop()
