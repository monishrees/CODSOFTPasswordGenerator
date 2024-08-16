from tkinter import *
import random
import string
m=Tk()
m.geometry("400x500")
m.title("Password Generator")

def func():
    num=int(e1.get())
    s1=string.ascii_lowercase
    s2=string.ascii_uppercase
    s3=string.digits
    s4=string.punctuation

    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)
    Password=s[0:num]

    l4=Label(m,text='Password:',font='times 14 bold')
    l4.place(x=30,y=250) 
    l5=Label(m,text=Password ,font='times 14 bold',width=24,bg='yellow')
    l5.place(x=150,y=250)
    
l1=Label(m,text='Password Generator',font='times 14 bold')
l1.place(x=30,y=30)
l2=Label(m,text='Password Length:',font='times 14 bold')
l2.place(x=30,y=90)
e1=Entry(m,width=33,bd=2,font='times 14 bold')
e1.place(x=30,y=133)
b1=Button(m,text='Generate Password',fg='white',bg='green',font='times 14 bold',width=30,command=func)
b1.place(x=30,y=180)

m.mainloop()