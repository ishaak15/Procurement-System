from Tkinter import *
import sqlite3
from tkMessageBox import *
con=sqlite3.Connection("Procurement System")
cur=con.cursor()
#cur.execute("insert into Login values('123','123') " )
root =Tk()
root.geometry('500x450')
root.title("Python Project")
Label(root,text='Procurement System',relief='ridge',bg='green',font='times 40 bold').grid(row=0,column=0,columnspan=6)
Label(root,text='Please select Dept',font=("Times New",15)).grid(row=3,column=0,columnspan=2)
ppi=0

cur.execute("create table if not exists Login(LoginID varchar(8),password varchar(15),cred varchar(15))")

cur.execute("select * from Login where LoginID=123")
x=cur.fetchone()
if x==None:
    cur.execute("insert into Login values('123','123','Administrator') " )

con.commit()

cur.execute("select * from Login")
print cur.fetchall()

OPTIONS = [
"Administrator",                    #####Changes
"Supply Chain",                 ##########
"Entrance"
] #etc
cur.execute("create table if not exists Inventory(partID varchar(6) Primary key,Pname varchar(10),Rate int)")

cur.execute("create table if not exists Receiving(partID varchar(6),Pname varchar(10),Rate int,QuantOrdered int,Quantreceived int,Dloc varchar(20),Sloc varchar(20),DeliveryID varchar(10),Transbill varchar(10),Contactperson varchar(15))")
cur.execute("select * from Receiving")
xp=cur.fetchall()
print xp

cur.execute("create table if not exists StoreInventory(partID varchar(6) Primary key,Pname varchar(10),Quant_avail int,Rate int)")
cur.execute("select * from StoreInventory")
xs=cur.fetchall()
print xs

cur.execute("create table if not exists Supplier(partID varchar(6),Pname varchar(10),Rate int,Quant int,Dloc varchar(20),Sloc varchar(20),DeliveryID varchar(10),Transbill varchar(10),Contactperson varchar(15))")
cur.execute("create table if not exists PurchaseOrder(partID varchar(6),Pname varchar(10),Rate int,Quant int,TPrice int)")


cur.execute("select * from PurchaseOrder")
print cur.fetchall()



Security=[]
#Admin = Tk()
picx1=PhotoImage(file='Procure.gif')
l=Label(root,image=picx1)
l.grid(row=1,column=0,columnspan=6)

variable = StringVar(root)
#variable.set(OPTIONS[0]) # default value
variable.set('Select Dept') # default value
w = OptionMenu(root, variable, *OPTIONS)            ###
w.grid(row=3,column=2,columnspan=2)                 #####
Label(root,text='',height=1).grid(row=4,column=2,columnspan=2)

    ###Admin Part
##########################################################################################################

def LADD():
    log=Toplevel()
    log.geometry('400x300')
    log.title("Add Login")
    Label(log,text='Add Login Details',font=("Times New",15),relief='ridge',bg='green').grid(row=0,column=0,columnspan=3)
    #log.geometry('200x300')
    Label(log,text='Enter Employee Code',height=2,width=20).grid(row=1,column=0)
    Label(log,text='Enter Password',height=2,width=20).grid(row=2,column=0)
    Label(log,text='Confirm Password',height=2,width=20).grid(row=3,column=0)
    
    variable = StringVar(root)

    variable.set('   Select Dept    ') # default value
    w = OptionMenu(log, variable, *OPTIONS)            ###
    w.grid(row=4,column=0,columnspan=2)                 #####

    a=Entry(log)
    a.grid(row=1,column=1)
    b=Entry(log,show='*')
    b.grid(row=2,column=1)
    c=Entry(log,show='*')
    c.grid(row=3,column=1)
    def dest():         ###log destroy
        abx=askyesno("Exit","Exit?")
        if abx==True:
            log.destroy()
        else:
            a.delete(0,END)
            b.delete(0,END)
            c.delete(0,END)

    def Add():
        cur.execute("insert into Login values(?,?,?)",(a.get(),b.get(),variable.get(),))
        showinfo("Login","Details Added")
        con.commit()
        a.delete(0,END)
        b.delete(0,END)
        c.delete(0,END)

        
        #dest()

        #log.destroy()
    def check():
        if(b.get()!=c.get()):
            showwarning("Mismatch","Passwords do not match!")
        Add()
    Button(log,text="ADD",command=check,height=1,width=12,bd=2).grid(row=5,column=0,columnspan=2)
    Button(log,text="EXIT",command=dest,height=1,width=12,bd=2).grid(row=6,column=0,columnspan=2)

    log.mainloop()
    
def PPO():
    purchaseorder=Toplevel()
    purchaseorder.geometry('450x400')
    ppip=int(ppi)
    ppip=ppip+1
    p=[]
    try:
        cur.execute("select * from Inventory")
        x=cur.fetchall()
        lp=len(x)
        ip=0
        while ip<lp:
            p.append(x[ip][1])
            ip+=1
        print p
        purchaseorder.title("Purchase Order")
        Label(purchaseorder,text="PLACE PURCHASE ORDER").grid(row=0,column=0,columnspan=2)
        Label(purchaseorder,text="").grid(row=1,column=1,rowspan=2)

        Label(purchaseorder,text="Select Product: ").grid(row=5,column=0)
        pn=StringVar(purchaseorder)
        pn.set('Products')
        pp=OptionMenu(purchaseorder, pn, *p)
        pp.grid(row=5,column=1)
        #Label(purchaseorder,text=ppip).grid(row=6,column=1)
        Quantity={10,25,50,80,100,150}
        Label(purchaseorder,text='Quantity').grid(row=7,column=0)
        v=StringVar(purchaseorder)
    
        Quant=IntVar(purchaseorder)
        #print v
        v.set("Number")
        w = OptionMenu(purchaseorder, v, *Quantity)
        w.grid(row=7,column=1)
    except:
        showwarning("ERROR","NO Items to place Purchase Order")
        purchaseorder.destroy()
        return

    
    #Quant=int(v.get())
##    Label(purchaseorder,text='Rate').grid(row=8,column=0)
##    Label(purchaseorder,text='1250').grid(row=9,column=1)
##    Label(purchaseorder,text='Total Price').grid(row=10,column=0)
    def Order():
        Order=Tk()
        Order.geometry('300x300')
        Order.title("Order")
        Label(Order,text="ORDER DETAILS").grid(row=0,column=0,columnspan=2)
        Label(Order,text="").grid(row=1,column=1,rowspan=2)
        cur.execute("select * from Inventory where Pname=?",(pn.get(),))
        Product=cur.fetchall()
        Label(Order,text="Product ID:").grid(row=3,column=0)
        Label(Order,text=Product[0][0]).grid(row=3,column=1)
        Label(Order,text="Product Name:").grid(row=4,column=0)
        Label(Order,text=Product[0][1]).grid(row=4,column=1)
        
        Label(Order,text="Product Rate:").grid(row=5,column=0)
        Label(Order,text=Product[0][2]).grid(row=5,column=1)
        Label(Order,text="Quantity: ").grid(row=6,column=0)
        Label(Order,text=v.get()).grid(row=6,column=1)
        tp=int(v.get())*Product[0][2]
        Label(Order,text='Total Price').grid(row=7,column=0)
        Label(Order,text=tp).grid(row=7,column=1)
        Label(Order,text="").grid(row=8,column=0,rowspan=2)
        def final():
            abx=askyesno("Order","Place Order")
            if abx==True:
                cur.execute("insert into PurchaseOrder values(?,?,?,?,?)",(Product[0][0],Product[0][1],Product[0][2],int(v.get()),tp,))
                
                con.commit()
                #ADD to table <<TABLE YET TO BE MADE>>
                
                Order.destroy()
                purchaseorder.destroy()
                
                

        Button(Order,text="Place Order",command=final,height=2,width=20,bd=4).grid(row=10,column=0)
        #Button(Order,text="EXIT",command=Order.destroy()).grid(row=10,column=1)
        Order.mainloop()

    
    Button(purchaseorder,text="Place Order",command=Order,height=2,width=12,bd=4).grid(row=8,column=0,columnspan=2)


    def destroy():
        abx=askyesno("Exit","Exit?")
        if abx==True:
            purchaseorder.destroy()
    
    Button(purchaseorder,text='EXIT',command=destroy,height=2,width=12,bd=4).grid(row=9,column=0,columnspan=2)
    purchaseorder.mainloop()

def ADDItems():
    
    Prod=Toplevel()
    Prod.geometry('300x260')
    Prod.title("New Products")
    Label(Prod,text="ADD New Items for purchase").grid(row=0,column=0,columnspan=2)
    Label(Prod,text="").grid(row=1,column=0,rowspan=2)
    
    Label(Prod,text="Product ID").grid(row=3,column=0)
    Label(Prod,text="Product Name").grid(row=4,column=0)
    Label(Prod,text="Product Rate").grid(row=5,column=0)
    e1=Entry(Prod)
    e1.grid(row=3,column=2)
    e2=Entry(Prod)
    e2.grid(row=4,column=2)
    e3=Entry(Prod)
    e3.grid(row=5,column=2)
    Label(Prod,text="").grid(row=6,column=0,rowspan=2)
    def ADDer():
        cur.execute("insert into Inventory values(?,?,?)",(e1.get(),e2.get(),int(e3.get()),))
        cur.execute("insert into StoreInventory values(?,?,?,?)",(e1.get(),e2.get(),0,int(e3.get()),))
        Prod.destroy()

    Button(Prod,text="ADD",command=ADDer,height=2,width=12,bd=4).grid(row=8,column=0,columnspan=3)
    def EXit():
        Prod.destroy()
    Button(Prod,text="EXIT",command=EXit,height=2,width=12,bd=4).grid(row=9,column=0,columnspan=3)
    
       
def Items():
    Prod=Toplevel()
    Prod.geometry('300x400+300+240')
    cur.execute("select * from Inventory")
    x=cur.fetchall()
    l=len(x)
    ip=0
    f=0
    
    Prod.title("Items")
    Label(Prod,text="List of Items").grid(row=0,column=0,columnspan=3)
    Label(Prod,text="").grid(row=1,column=0,rowspan=2)
    Label(Prod,text="Product ID").grid(row=3,column=0)
    Label(Prod,text="Product Name").grid(row=3,column=1)
    Label(Prod,text="Product Rate").grid(row=3,column=2)
    Label(Prod,text="").grid(row=4,column=0,rowspan=2)
    while ip<l:
        Label(Prod,text=x[ip][0]).grid(row=6+ip,column=0)
        Label(Prod,text=x[ip][1]).grid(row=6+ip,column=1)
        Label(Prod,text=x[ip][2]).grid(row=6+ip,column=2)
        ip=ip+1
        f+=1
    Label(Prod,text="").grid(row=6+ip,column=0,rowspan=2)
    if( f==0):
        showwarning('Error','Add Items first!')


        
    def det():
        Prod.destroy()
    Button(Prod,text="EXIT",command=det,height=2,width=12).grid(row=100,column=1)
    Prod.mainloop()
###############################################################
def OrderReport():
    OReport=Toplevel()
    OReport.geometry('260x200')
    Label(OReport,text='Order Report',font='times 20 bold').pack()
    p=[]
    try:
        cur.execute("select * from Supplier")
        x=cur.fetchall()
        print x
        lp=len(x)
        ip=0
        while ip<lp:
            p.append(x[ip][1])
            print x[ip][1],ip
            ip+=1
        print p
        variable = StringVar(OReport)
        variable.set('Select Item')
        w = OptionMenu(OReport, variable, *p)
        w.pack()

    except:
        showwarning("ERROR","NO Orders acknowledged!")
        OReport.destroy()
        return
        
    def ok():
        
        Report=Toplevel()
        Label(Report,text="Shipment Details",font='times 15 bold').grid(row=0,column=0,columnspan=2)        ######################
        Label(Report,text="").grid(row=1,column=0,rowspan=2)                                                #######################
        cur.execute("select * from Supplier where Pname=?",(variable.get(),))                               ########################
        x=cur.fetchall()                                                                                    ######################
        lp=len(x[0])
        ip=0
        OReport.destroy()
        Label(Report,text='Product ID:').grid(row=3,column=0)
        Label(Report,text='Product Name:').grid(row=4,column=0)
        Label(Report,text='Product Rate:').grid(row=5,column=0)
        Label(Report,text='Quantity:').grid(row=6,column=0)
        Label(Report,text='Dispatch Location:').grid(row=7,column=0)
        Label(Report,text='Shipment Location:').grid(row=8,column=0)
        Label(Report,text='Delivery ID:').grid(row=9,column=0)
        Label(Report,text='Transport Bill No:').grid(row=10,column=0)
        Label(Report,text='Contact Person:').grid(row=11,column=0)
        
        while ip<lp:
            Label(Report,text=x[0][ip]).grid(row=3+ip,column=1)
            ip+=1
        print x

        def dpt():
            adx=askyesno('EXIT','Do you want to exit?')
            if adx==True:
                Report.destroy()
                

        Button(Report,text='EXIT',command=dpt).grid(row=3+ip,column=0,columnspan=2)


    
    Button(OReport,text='Fetch Details',command=ok,height=2,width=15,pady=5).pack()
    def EXP():
        adx=askyesno('EXIT','Do you want to exit?')
        if adx==True:
            OReport.destroy()


        
    Button(OReport,text='EXIT',command=EXP,height=2,width=15,pady=5).pack()
    
    
    print 'Check Fetch'
  
    OReport.mainloop()
        
##############################################################
def Logins():
    Login=Toplevel()
    Label(Login,text="Authorised Personnel",font='times 15',bg='grey').grid(row=0,column=0,columnspan=3)
    Label(Login,text="",font='times 15').grid(row=1,column=0,rowspan=2)
    cur.execute("select * from Login")
    x=cur.fetchall()
    Label(Login,text="Login ID",font='times 10').grid(row=3,column=0)
    Label(Login,text="Login Password",font='times 10').grid(row=3,column=1)
    Label(Login,text="Department",font='times 10').grid(row=3,column=2)
    l=len(x)
    i=0
    while i<l:
        Label(Login,text=x[i][0]).grid(row=4+i,column=0)
        Label(Login,text=x[i][1]).grid(row=4+i,column=1)
        Label(Login,text=x[i][2]).grid(row=4+i,column=2)
        i+=1
    def det():
        Login.destroy()
    Button(Login,text="EXIT",command=det).grid(row=100,column=1)
    Login.mainloop()

##################################################################################################
def Stores():
    Stores=Toplevel()
    Label(Stores,text='Inventory',font='times 18').grid(row=0,column=0,columnspan=4)
    Label(Stores,text='',font='times 18').grid(row=1,column=0,columnspan=4,rowspan=2)
    Label(Stores,text='Part ID',font='times 13').grid(row=3,column=0)
    Label(Stores,text='Part Name',font='times 13').grid(row=3,column=1)
    Label(Stores,text='Part Quantity',font='times 13').grid(row=3,column=2)
    Label(Stores,text='Part Rate',font='times 13').grid(row=3,column=3)

    cur.execute("select * from StoreInventory")
    spt=cur.fetchall()
    l=len(spt)
    i=0
    f=0
    while i<l:
        Label(Stores,text=spt[i][0]).grid(row=6+i,column=0)
        Label(Stores,text=spt[i][1]).grid(row=6+i,column=1)
        Label(Stores,text=spt[i][2]).grid(row=6+i,column=2)
        Label(Stores,text=spt[i][3]).grid(row=6+i,column=3)
        f=f+1
        i+=1

    def dipp():
        Stores.destroy()

    if(f==0):
        showwarning('Error','Add items first!')

    Button(Stores,text='EXIT',command=dipp,height=2,width=15).grid(row=7+i,column=1,columnspan=2)

    Stores.mainloop()
    
##################################################################
    
def administrator():
    Admin=Toplevel()
    Admin.geometry('960x720')

    def destroy():
        abx=askyesno("Exit","Exit?")
        if abx==True:
            Admin.destroy()
            
    
    Label(Admin,text='Administrator Panel',relief='ridge',bg='green',font='times40bold',height=3,width=100).grid(row=0,column=0,columnspan=6)

    picx2=PhotoImage(file='Admin.gif')
    img2=Label(Admin,image=picx2)
    img2.grid(row=1,column=0,columnspan=6)
    
    Button(Admin,text="Add Login details",command=LADD,height=2,width=20,padx=4,pady=6).grid(row=5,column=0)
    Button(Admin,text="Place Purchase order",command=PPO,height=2,width=20,padx=4,pady=6).grid(row=5,column=1)
    Button(Admin,text="List Items",command=Items,height=2,width=20,padx=4,pady=6).grid(row=5,column=2)
    Button(Admin,text="New Items",command=ADDItems,height=2,width=20,padx=4,pady=6).grid(row=5,column=3)
    Button(Admin,text="Order Report",command=OrderReport,height=2,width=20,padx=4,pady=6).grid(row=5,column=4)
    Button(Admin,text="Personel",command=Logins,height=2,width=20,padx=4,pady=6).grid(row=5,column=5)
    Label(Admin,text="").grid(row=8,column=1)
    Button(Admin,text="STORES",command=Stores,height=2,width=15).grid(row=9,column=2)
    Button(Admin,text="EXIT",command=destroy,height=2,width=15).grid(row=9,column=3)
    Admin.mainloop()

#administrator()
#root.mainloop()
###################################################################################
####Entry Block

def Gen(dip):
    Invoice=Toplevel()


    cur.execute("select * from Supplier where DeliveryID=?",(dip,))         #####Fetching Delivery details from Delivery ID
    p=cur.fetchone()
    
    Label(Invoice,text='INVOICE',font='calibri 12').grid(row=0,column=0,columnspan=2)
    Label(Invoice,text='').grid(row=1,column=0,rowspan=2)
    Label(Invoice,text='Part ID',font='calibri 12').grid(row=3,column=0)
    Label(Invoice,text=p[0],font='calibri 12').grid(row=3,column=1)
    
    
    Label(Invoice,text='Part Name',font='calibri 12').grid(row=4,column=0)
    Label(Invoice,text=p[1],font='calibri 12').grid(row=4,column=1)
    
        
    Label(Invoice,text='Rate',font='calibri 12').grid(row=5,column=0)
    Label(Invoice,text=p[2],font='calibri 12').grid(row=5,column=1)
    
    Label(Invoice,text='Quantity Ordered',font='calibri 12').grid(row=6,column=0)   ###Items ordered
    Label(Invoice,text=p[3],font='calibri 12').grid(row=6,column=1)

    Label(Invoice,text='Quantity Received:',font='calibri 12').grid(row=7,column=0) ##### Taking entry of the items received 
    ex=Entry(Invoice)
    ex.grid(row=7,column=1)

    
    Label(Invoice,text='Dispatch Location',font='calibri 12').grid(row=8,column=0)
    Label(Invoice,text=p[4],font='calibri 12').grid(row=8,column=1)
    
    Label(Invoice,text='Shipment Location',font='calibri 12').grid(row=9,column=0)
    Label(Invoice,text=p[5],font='calibri 12').grid(row=9,column=1)
    
    Label(Invoice,text='Delivery ID',font='calibri 12').grid(row=10,column=0)
    Label(Invoice,text=p[6],font='calibri 12').grid(row=10,column=1)
    
    Label(Invoice,text='Transport Bill No',font='calibri 12').grid(row=11,column=0)
    Label(Invoice,text=p[7],font='calibri 12').grid(row=11,column=1)
    
    Label(Invoice,text='Contact Person',font='calibri 12').grid(row=12,column=0)
    Label(Invoice,text=p[8],font='calibri 12').grid(row=12,column=1)
    
    Label(Invoice,text='').grid(row=13,column=0,rowspan=2)


    def MovetoStores():
        cur.execute("insert into Receiving values(?,?,?,?,?,?,?,?,?,?)",(p[0],p[1],p[2],p[3],ex.get(),p[4],p[5],p[6],p[7],p[8],))      ###Adding to received Data
        cur.execute("select * from StoreInventory where partID=?",(p[0],))
        xtcs=cur.fetchall()
        print xtcs
        
        if p[3]!=int(ex.get()):
            acx=askyesno('Receiving Less',"Are you sure that Quantity received isn't the ordered Quantity?")
            if acx==True:
                cur.execute("insert into StoreInventory values(?,?,?,?)",(p[0],p[1],(xcs[0][2]+int(ex.get())),p[2],))

                cur.execute("delete from Supplier where DeliveryID=?",(dip,))               ###Removing received Material from Incoming Material
                con.commit()
        else:
            cur.execute("update StoreInventory set Quant_avail=? where partID=?",(xtcs[0][2]+int(ex.get()),p[0],))
            cur.execute("delete from Supplier where DeliveryID=?",(dip,))               ###Removing received Material from Incoming Material
            con.commit()
            Invoice.destroy() 
            

    Button(Invoice,text='Pass to Stores',command=MovetoStores,font='arial 11',bg='light grey').grid(row=15,column=0,columnspan=2)

    Invoice.mainloop()
    



def DID():
    Did=Toplevel()
    Did.geometry('250x200')
    Label(Did,text='Enter Delivery ID',height=2,width=20,font='times 15').pack()
    e=Entry(Did,font="Arial 15 bold",width=16,bg="light grey",justify='right')
    e.pack()

    def checking():               ######Verify Delivery ID
        dip=e.get()
        print dip
        
        
        cur.execute("select * from Supplier where DeliveryID=?",(dip,))
        p=cur.fetchone()
        print p
        if (p==None):
            showwarning('Status','Delivery ID Not Found!')
        else:
            Did.destroy()
            Gen(dip)
       
        
        ##print 'Back Working'
            
    Button(Did,text='Fetch Details',command=checking,height=2,width=12).pack()
    Button
    Did.mainloop()




######Entrance Main Function
def Entrance():
    Ent=Toplevel()
    Label(Ent,text='Procurement System',relief='ridge',bg='green',font='times 40 bold').grid(row=0,column=0,columnspan=5)
    Label(Ent,text='Entrance Entry Department',relief='ridge',font='times 20').grid(row=1,column=1,columnspan=3)
    picx3=PhotoImage(file='Ent.gif')
    img4=Label(Ent,image=picx3)
    img4.grid(row=4,column=1,columnspan=3)
 
    Button(Ent,text='Find Delivery ID',command=DID,height=2,width=20,bd=5).grid(row=6,column=2)
    def des():
        ans=askyesno("Exit","Exit?")
        if ans==True:
            Ent.destroy()
            #con.close()
    Button(Ent,text='EXIT',command=des,height=2,width=20,bd=5).grid(row=6,column=3)








    Ent.mainloop()
##################################################################################################################
######Finance Loop

    






##################################################################################################################

def ok():
    
    #showinfo('Welcome ', variable.get())
    #if(variable.get()=="Administrator"):
    Label(root,text='ENTER ID :',font=("Times New bold",10)).grid(row=8,column=0,columnspan=2)
    v=Entry(root,bd=2,font=("Times New bold",12))
    v.grid(row=8,column=2,columnspan=2)
    Label(root,text='ENTER PASSWORD :',font=("Times New bold",10)).grid(row=9,column=0,columnspan=2)
    vv=Entry(root,show='*',bd=2,font=("Times New bold",12))
    vv.grid(row=9,column=2,columnspan=2)

    def verify():               #Verify password
        user=v.get()
        cred=variable.get()
        try:
            cur.execute("select * from Login where LoginID=?",(user,))
            p=cur.fetchone()
            print p
            print user
            print cred
            print vv.get()
            
            if(p[1]==vv.get() and cred==p[2]):
                showinfo("Login","Login Successful")
                if cred=='Administrator':
                    administrator()
                elif cred=='Supply Chain':
                    #con.close()
                    print 'Supply1'
                    import Supp
                    print 'Supply1'
##                    con=sqlite3.Connection("Procurement System")
##                    cur=con.cursor()

                    
                elif cred=='Entrance':
                    Entrance()
            else:
                    showwarning("Login Failed!","Invalid Credentials!")

        except TypeError as error:
                
            if error=='NoneType':
                showwarning("Login","Invalid Credentials!")
            showwarning("Credentials","Unrecognised ID")
                
            return
##        except:
##            con=sqlite3.Connection("Procurement System")
##            cur=con.cursor()

            
            
##            print p[2],cred
##            print p[0],user
    Label(root,text='',height=1).grid(row=10,column=0)        
    Button(root,text='Submit',command=verify,height=1,width=12,bd=3).grid(row=11,column=2)
    def EX():
    
        abx=askyesno("Exit","Exit?")
        if abx==True:
            root.destroy()
    
            
    Button(root,text='EXIT',command=EX,height=1,width=12,bd=3).grid(row=11,column=4)
        


####################################################################


    

button = Button(root, text="OK", command=ok,height=1,width=15,bd=3)
button.grid(row=3,column=4,columnspan=2)



root.mainloop()
