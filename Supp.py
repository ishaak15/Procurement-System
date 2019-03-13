from Tkinter import *
import sqlite3
from tkMessageBox import *
con=sqlite3.Connection("Procurement System")
cur=con.cursor()
#cur.execute("insert into Login values('123','123') " )
cur.execute("select * from Login")
print cur.fetchall()
root1 =Toplevel()
img1=PhotoImage(file='Supplier.gif')
root1.title("Python Project")
Label(root1,text='Procurement System',relief='ridge',bg='green',font='times 40 bold').grid(row=0,column=0,columnspan=5)
Label(root1,text='Supply Chain',relief='ridge',font='times 20').grid(row=1,column=1,columnspan=3)
l=Label(root1,image=img1)
l.grid(row=3,column=1,columnspan=3)
cur.execute("select * from PurchaseOrder")
x=cur.fetchall()
print x

####################################################################################
def check():                    #####List Purchase Orders
    Order=Toplevel()
    Order.geometry('360x300')
    cur.execute("select * from PurchaseOrder")
    x=cur.fetchall()
    Label(Order,text="Product ID:").grid(row=4,column=0)
    Label(Order,text="Product Name:").grid(row=4,column=1)
    Label(Order,text="Product Rate:").grid(row=4,column=2)
    Label(Order,text="Quantity: ").grid(row=4,column=3)
    Label(Order,text='Total Price').grid(row=4,column=4)
    Label(Order,text="").grid(row=4,column=0,rowspan=2)
    l=len(x)
    i=0
    while i<l:
        Label(Order,text=x[i][0]).grid(row=6+i,column=0)
        Label(Order,text=x[i][1]).grid(row=6+i,column=1)
        Label(Order,text=x[i][2]).grid(row=6+i,column=2)
        Label(Order,text=x[i][3]).grid(row=6+i,column=3)
        Label(Order,text=x[i][4]).grid(row=6+i,column=4)
        i+=1

    def opp():
        Order.destroy()

    Button(Order,text='EXIT',command=opp).grid(row=8+i,column=2)

    Order.mainloop()

############################################################################
def Confirm():                    #####Confirm Purchase Orders
    Order=Toplevel()
    Order.geometry('380x300')
    Order.title('Orders')
    cur.execute("select * from PurchaseOrder")
    x=cur.fetchall()
    Label(Order,text="Product ID").grid(row=4,column=1)
    Label(Order,text="Product Name").grid(row=4,column=2)
    Label(Order,text="Product Rate").grid(row=4,column=3)
    Label(Order,text="Quantity").grid(row=4,column=4)
    Label(Order,text='Total Price').grid(row=4,column=5)
    Label(Order,text="").grid(row=5,column=0,rowspan=2)
    l=len(x)
    i=0
    p=StringVar(Order)
    while i<l:
        
        b=Radiobutton(Order, text=x[i][0],variable=p, value=int(x[i][0]))
        print '1'   

        b.grid(row=7+i,column=1)
        print '2'
        Label(Order,text=x[i][1]).grid(row=7+i,column=2)
        Label(Order,text=x[i][2]).grid(row=7+i,column=3)
        Label(Order,text=x[i][3]).grid(row=7+i,column=4)
        Label(Order,text=x[i][4]).grid(row=7+i,column=5)
        #Label(Order,text=x[i][4]).
        i+=1
    
    print p
##    cur.execute("select * from PurchaseOrder where partID=?",(int(p),))
##    print cur.fetchall()

    def dep():
        print 'Here'
        cur.execute("select * from PurchaseOrder where partID=?",(p.get(),))
        x= cur.fetchone()
        print x
        Invoice=Toplevel()
        Invoice.title('INVOICE')
        Label(Invoice,text='INVOICE').grid(row=0,column=0,columnspan=2)
        Label(Invoice,text='').grid(row=1,column=0,rowspan=2)
        Label(Invoice,text='Part ID').grid(row=3,column=0)
        Label(Invoice,text=x[0]).grid(row=3,column=1)
        Label(Invoice,text='Part Name').grid(row=4,column=0)
        Label(Invoice,text=x[1]).grid(row=4,column=1)
        
        Label(Invoice,text='Rate').grid(row=5,column=0)
        Label(Invoice,text=x[2]).grid(row=5,column=1)
        Label(Invoice,text='Quantity').grid(row=6,column=0)
        Label(Invoice,text=x[3]).grid(row=6,column=1)
        Label(Invoice,text='Dispatch Location').grid(row=7,column=0)
        Label(Invoice,text='Shipment Location').grid(row=8,column=0)
        Label(Invoice,text='Delivery ID').grid(row=9,column=0)
        Label(Invoice,text='Transport Bill No').grid(row=10,column=0)
        Label(Invoice,text='Contact Person').grid(row=11,column=0)
        Label(Invoice,text='Total Price').grid(row=12,column=0)
        Label(Invoice,text=x[4]).grid(row=12,column=1)

        ##Entry Boxes
        e1=Entry(Invoice)
        e1.grid(row=7,column=1)
        e2=Entry(Invoice)
        e2.grid(row=8,column=1)
        e3=Entry(Invoice)
        e3.grid(row=9,column=1)
        e4=Entry(Invoice)
        e4.grid(row=10,column=1)
        e5=Entry(Invoice)
        e5.grid(row=11,column=1)

        def CopySupplier():
            if (e1.get()!='' and e2.get()!='' and e3.get()!='' and e4.get()!='' and e5.get()!=''):
                cur.execute("insert into Supplier values(?,?,?,?,?,?,?,?,?)",(x[0],x[1],x[2],x[3],e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),))
                cur.execute("delete from PurchaseOrder where partID=?",(x[0],))
                cur.execute("select * from Supplier")
                print cur.fetchall()
                Invoice.destroy()
                Order.destroy()
                con.commit()
                           
                Confirm()
         
                return
            else:
                showwarning('ERROR','Empty Input!')
        Button(Invoice,text='Submit',command=CopySupplier).grid(row=13,column=0,columnspan=2)
    def opp():
        Order.destroy()

    #Button(Invoice,text='EXIT',command=opp).grid(row=13,column=2)

        
        
        
        
        

    Button(Order,text='Submit',command=dep).grid(row=100,column=2,columnspan=2)
    Button(Order,text='EXIT',command=opp).grid(row=100,column=4)

    Order.mainloop()

    




#########################################################################3
Button(root1,text='Check Order',command=check,height=2,width=20,bd=5).grid(row=6,column=1)
Button(root1,text='Confirm Order',command=Confirm,height=2,width=20,bd=5).grid(row=6,column=2)
def des():
    ans=askyesno("Exit","Exit?")
    if ans==True:
        root1.destroy()
        #con.close()
Button(root1,text='EXIT',command=des,height=2,width=20,bd=5).grid(row=6,column=3)




root1.mainloop()
