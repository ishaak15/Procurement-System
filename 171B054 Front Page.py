from Tkinter import *
root=Tk()
#root.configure(bg='light grey')
img1=PhotoImage(file='Ishaak.gif')
l=Label(root,image=img1)
Label(root,text='Procurement System',relief='ridge',bg='green',font='times 40 bold').pack()
#Label(root).pack()
l.pack()

Label(root,text='DEVELOPER DETAILS',font='times 15 italic bold').pack()
Label(root,text='Name : ISHAAK MALL',font='times 12 bold').pack()
Label(root,text='Enrollment No.:171B054',font='times 12 bold').pack()
Label(root,text='Batch  :B2',font='times 12 bold').pack()
Label(root,text='Email :ishaak15@gmail.com',font='times 12 bold').pack()

def go(e):
    root.destroy()

    root1=Tk()
    root1.geometry('300x250')
    Label(root1,text='Default Details').pack()
    Label(root1,text='Default Mode: Administrator').pack()
    Label(root1,text='Default User ID: 123').pack()
    Label(root1,text='Default Password: 123').pack()

    def dest():
        root1.destroy()

        import Python_Project
        

    Button(root1,text='OK',command=dest).pack()

    root1.mainloop()
    
    
#l.after(6000,go)
l.bind('<Motion>',go)



root.mainloop()
