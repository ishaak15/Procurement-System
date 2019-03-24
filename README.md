# Procurement-System
This project is based on the concept of Demand and Supply and is named Procurement System as it basically works for industrial factories and Assembly Plants where a raw material is ‘Procured’ from other places and industries and is then used for further producing objects like cars, buses, etc… The concept is equally applicable for e-commerce purposes where the user may place an order and then it is verified by the platforms( Flipkart, Amazon, etc)  and then forwarded to their respective suppliers.

SUPPORT:
This project was built in python 2.7.14 on a windows 10 OS.

MODULES USED:
1.	Tkinter
2.	Sqlite3
3.	tkMessageBox
Working:
The Project has basically has 3 components. 
1.	Administrator: The Master component dealing with the order placing, login ID maintenance, and maintaining an inventory of the incoming stock.
2.	Supply Chain: The component that takes care of the order that can be fulfilled at present in accordance with the demands raised and taking care of the necessary delivery details as well.
3.	Entrance: The department of receiving material when it reaches the necessary location after verification of the items and quantity.
Working on the Project:
Executing the file named “ Front page.py” we have my (the developer’s) description along with an image. 
 
The image is bound by a motion sensor which detects if the user hovers over the image the developer details disappear and the default user details are then displayed.
 
On clicking on the OK button we now arrive on the login screen here we first have to select our department then have to log into the portal.

Default Details:
User: Administrator
User ID: 123
Password: 123
   
On logging into the Application we now get to the default screen of the administration panel. From here we can have a look at the functions available in the system. 
o	First: Add Login details for all the departments available.
o	Second: Place a purchase order of the items that we are currently working with.
o	Third: List the items we are currently working with.
o	Fourth: Add new items we shall work with.
o	Fifth: Check the status of the orders which have been acknowledged by the supplier.
o	Sixth: Check personnel having access to each component of the system.
o	Seventh: Check the inventory of the items currently available and their quantity.
 
 


With that being all the functions of the administrator. We now have a look at the functions of the Supplier, in particular, the Supply Chain. The Supply Chain has the functions of checking incoming orders and then confirming then when the required materials, etc are available.
 

Last But not the least we have the Department at the Entrance of the warehouses, factories, assembly plants, etc. where the details of the arriving items are fetched by their Delivery ID and then on verification of the quantity they are added to the inventory.
