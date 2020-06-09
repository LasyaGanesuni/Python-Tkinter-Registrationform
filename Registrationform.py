from tkinter import*
from tkinter.font import Font
from tkinter import messagebox

win=Tk()
win.title("Registration Form")
win.geometry('500x400')
win.configure(background='grey')

l1=Label(win,text='Registration Form',bg='black',fg='yellow',font=("bold", 30))
l1.pack(fill=X)

fm1=Frame(win,bg='grey')
fm1.pack(pady=10)
fm2=Frame(win,bg='grey')
fm2.pack(pady=10)
fm3=Frame(win,bg='grey')
fm3.pack(pady=10)
fm4=Frame(win,bg='grey')
fm4.pack(pady=10)
fm5=Frame(win,bg='grey')
fm5.pack(pady=10)
fm6=Frame(win,bg='grey')
fm6.pack(pady=10)

l2=Label(fm1,text='FullName',bg='grey',fg='black',font=("bold", 15))
l2.pack(side=LEFT)
e2=Entry(fm1)
e2.pack(padx=20)

l3=Label(fm2,text='Password',bg='grey',fg='black',font=("bold", 15))
l3.pack(side=LEFT)
e3=Entry(fm2)
e3.pack(padx=20)

l4=Label(fm3,text='Email',bg='grey',fg='black',font=("bold", 15))
l4.pack(padx=20,side=LEFT)
e4=Entry(fm3)
e4.pack(padx=30)

var = IntVar()

l5=Label(fm4,text='Gender',bg='grey',fg='black',font=("bold", 15))
l5.pack(padx=20,side=LEFT)
Radiobutton(fm4, text="Male",padx = 5, variable=var, value=1,bg='grey').pack(side=LEFT)
Radiobutton(fm4, text="Female",padx = 20, variable=var, value=2,bg='grey').pack()

l6=Label(fm5,text='Age',bg='grey',fg='black',font=("bold", 15))
l6.pack(padx=20,side=LEFT)
e6=Entry(fm5)
e6.pack(padx=30)

def clicked():
	messagebox.showinfo('Message','Registration Successful!')
Button(fm6, text='Submit',width=10,bg='brown',fg='white',command=clicked,font=("bold", 15)).pack()

win.mainloop()






