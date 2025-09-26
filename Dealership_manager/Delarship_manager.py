import tkinter as tk
from tkinter import ttk
from random import choice
import json
import datetime,random
import calendar
import os, shutil
from collections.abc import Mapping

window = tk.Tk()


window.geometry('1440x800')
window.title('Inventory')

Pre_Delivery=tk.Toplevel(window)
Pre_Delivery.geometry("1440x800")
Pre_Delivery.title('Pre-Delivery')

Orders=tk.Toplevel(window)
Orders.geometry("1440x800")
Orders.title('Orders')


Delivered=tk.Toplevel(window)
Delivered.geometry("1440x800")
Delivered.title('Delivered Cars')




with open('delivered.json', 'r') as f:
  
    data=json.load(f)
    if isinstance(data,Mapping):
        all_delivered = data.get("cars", [])
    elif isinstance(data,list):
        all_delivered = data
    else:
        all_delivered = []



with open('Inventory.json', 'r') as f:
  
    data=json.load(f)
    if isinstance(data,Mapping):
        allcars = data.get("cars", [])
    elif isinstance(data,list):
        allcars = data
    else:
        allcars = []


with open('Orders.json', 'r') as f:
    
    data=json.load(f)
    if isinstance(data,Mapping):
        allorders = data.get("Orders", [])
    elif isinstance(data,list):
        allorders = data
    else:
        allorders = []

with open('PreDelivery.json', 'r') as f:
    
    data=json.load(f)
    if isinstance(data,Mapping):
        alldeliveries = data.get("preDelCars", [])
    elif isinstance(data,list):
        alldeliveries = data
    else:
        alldeliveries = []
   
    
    



def orderdump():

    with open('Orders.json', "w") as file:

        json.dump(allorders ,file, indent=3)
    
def deliverydump():

    with open('Predelivery.json', "w") as file:

        json.dump(alldeliveries ,file, indent=3)

def inventorydelete():
    with open ('Inventory.json', 'w') as file:
        json.dump(allcars,file, indent=3)

def deliveredcarsdump():
    with open ('delivered.json', 'w') as file:
        json.dump(all_delivered,file, indent=3)



def refresh_table():
    for row in table.get_children():
        table.delete(row)
    for i in allcars:
        color = i.get("Color", "")
        color_lower = color.lower()
        if color_lower == "silver":
            color_lower = "gray75"
        if color_lower == "black":
            tag_name = "BlackColor"
            table.insert('', 'end', values=(i.get('VIN', ''), i.get('Model', ''), i.get('Year', ''), i.get('Trim', ''), i.get('Fuel', ''), i.get('Price', ''), i.get("Color", ""),'' ), tags=(tag_name,))
            table.tag_configure(tag_name, background="black", foreground="white")
        else:
            table.insert('', 'end', values=(i.get('VIN', ''), i.get('Model', ''), i.get('Year', ''), i.get('Trim', ''), i.get('Fuel', ''), i.get('Price', ''),  i.get("Color", ""), ''), tags=(color_lower,))
            try:
                table.tag_configure(color_lower, foreground=color_lower)
            except tk.TclError:
                table.tag_configure(color_lower, foreground="black")
                
def refresh_deliveries():
    
    for row in Pre_Delivery_Cars.get_children():
        Pre_Delivery_Cars.delete(row)
    for i in alldeliveries:
        color = i.get("Color", "")
        color_lower = color.lower()
        if color_lower == "silver":
            color_lower = "gray75"
        if color_lower == "black":
            tag_name = "BlackColor"
            Pre_Delivery_Cars.insert('', 'end', values=(i.get('VIN', ''), i.get('Model', ''), i.get('Year', ''), i.get('Trim', ''), i.get('Fuel', ''), i.get('Price', ''), i.get("Color", ""),'' ), tags=(tag_name,))
            Pre_Delivery_Cars.tag_configure(tag_name, background="black", foreground="white")
        else:
            Pre_Delivery_Cars.insert('', 'end', values=(i.get('VIN', ''), i.get('Model', ''), i.get('Year', ''), i.get('Trim', ''), i.get('Fuel', ''), i.get('Price', ''),  i.get("Color", ""), ''), tags=(color_lower,))
            try:
                Pre_Delivery_Cars.tag_configure(color_lower, foreground=color_lower)
            except tk.TclError:
                Pre_Delivery_Cars.tag_configure(color_lower, foreground="black")
def refresh_delivered():
    
    for row in Delivered_Cars.get_children():
        Delivered_Cars.delete(row)
    for i in all_delivered:
        color = i.get("Color", "")
        color_lower = color.lower()
        if color_lower == "silver":
            color_lower = "gray75"
        if color_lower == "black":
            tag_name = "BlackColor"
            Delivered_Cars.insert('', 'end', values=(i.get('VIN', ''), i.get('Model', ''), i.get('Year', ''), i.get('Trim', ''), i.get('Fuel', ''), i.get('Price', ''), i.get("Color", ""), i.get("Delivery_date", ""),""), tags=(tag_name,))
            Delivered_Cars.tag_configure(tag_name, background="black", foreground="white")
        else:
            Delivered_Cars.insert('', 'end', values=(i.get('VIN', ''), i.get('Model', ''), i.get('Year', ''), i.get('Trim', ''), i.get('Fuel', ''), i.get('Price', ''),  i.get("Color", ""),i.get("Delivery_date", ""),""), tags=(color_lower,))
            try:
                Delivered_Cars.tag_configure(color_lower, foreground=color_lower)
            except tk.TclError:
                Delivered_Cars.tag_configure(color_lower, foreground="black")




def refresh_orders():
   
    for row in Ordered_Cars.get_children():
        Ordered_Cars.delete(row)
    for i in allorders:
        color = i.get("Color", "")
        color_lower = color.lower()
        if color_lower == "silver":
            color_lower = "gray75"
        if color_lower == "black":
            tag_name = "BlackColor"
            Ordered_Cars.insert('', 'end', values=(i.get('VIN', ''), i.get('Model', ''), i.get('Year', ''), i.get('Trim', ''), i.get('Fuel', ''), i.get('Price', ''), color, i.get('Date', '')), tags=(tag_name,))
            Ordered_Cars.tag_configure(tag_name, background="black", foreground="white")
        else:
            Ordered_Cars.insert('', 'end', values=(i.get('VIN', ''), i.get('Model', ''), i.get('Year', ''), i.get('Trim', ''), i.get('Fuel', ''), i.get('Price', ''), color, i.get('Date', '')), tags=(color_lower,))
            try:
                Ordered_Cars.tag_configure(color_lower, foreground=color_lower)
            except tk.TclError:
                Ordered_Cars.tag_configure(color_lower, foreground="black")
model_shorts = {
    "Range_Rover":"RR",
    "Range_Rover_Sport":"RS",
    "Range_Rover_Velar":"RV",
    "Range_Rover_Evoque":"RE",
    "Defender_130":"D3",
    "Defender_110":"D1",
    "Defender_90":"D9",
    "Discovery":"DY",
    "F-Type":"FT",
    "I-Type":"FI",
    "CX-75":"CX",
    "E-Pace":"EP",
    "F-Pace":"FP",
}

def sort_by(key):

    allcars.sort(key = lambda d: d.get(key, ''))
    refresh_table()
def mainwindowshow():
    window.lift()
def predeliverywindowshow():
    Pre_Delivery.lift()
def orderwindowshow():
    Orders.lift()
def deliveredwindowshow():
    Delivered.lift()


l=ttk.Label(master=window,text="Sort By").pack(pady=10)
sort_frame = ttk.Frame(window)
sort_frame.pack(pady = 5)

sort_field= ["VIN", "Model", 'Year', "Trim",'Fuel','Price', 'Color' , ]
sort_field2= ["VIN", "Model", 'Year', "Trim",'Fuel','Price', 'Color' , 'Date']
sort_field3= ["VIN", "Model", 'Year', "Trim",'Fuel','Price', 'Color' , 'deliver']
sort_field4 = ["VIN", "Model", 'Year', "Trim",'Fuel','Price', 'Color' , 'Delivery date']
for f in sort_field:
    # btn = ttk.Button(sort_frame,text=f)
    btn = ttk.Button(sort_frame,text=f,command=lambda k=f:sort_by(k))
    btn.pack( side="left", padx=5 )

exit_button = tk.Button(window,text="Exit", command=window.quit)
exit_button.pack(pady=10)


order_confirmation_text = ttk.Label(Orders, text="CONFIRM ORDER PLS")

order_frame_text = ttk.Frame(Orders)
order_Model_text = ttk.Label(order_frame_text,text="Model?")
order_Trim_text = ttk.Label(order_frame_text,text="Trim?")
order_Fuel_text = ttk.Label(order_frame_text,text="Fuel?")
order_Color_text = ttk.Label(order_frame_text,text="Color?")
order_frame_text.pack(pady=5)
order_Model_text.pack(side='left',padx=60)
order_Trim_text.pack(side='left',padx=60)
order_Fuel_text.pack(side='left',padx=60)
order_Color_text.pack(side='left',padx=60)

order_frame = ttk.Frame(Orders)
order_Model = ttk.Combobox(order_frame,values=["Range_Rover", "Range_Rover_Sport", "Range_Rover_Velar", "Range_Rover_Evoque", "Defender_130", "Defender_110", "Defender_90", "Discovery", 'F-Type' , 'I-Type' , 'CX-75', "E-Pace", "F-Pace"])
order_Trim = ttk.Combobox(order_frame, values=["S","SE","HSE","Autobiography","SV","OCTA","Anniversary"])
order_Fuel = ttk.Combobox(order_frame, values=["Electric", "Gasoline", "Diesel", "PHEV", "Hybrid"])
order_Color = ttk.Combobox(order_frame, values=["Red", "Blue", "Black", "White", "Gray", "Yellow",
    "Orange", "Purple", "Brown", "Gold", "Pink", "Green", "Cyan", "Magenta"])
show_frame_order = ttk.Frame(Orders)
show_frame_main = ttk.Frame(window)
show_frame_predelivery = ttk.Frame(Pre_Delivery)
show_frame_delivered = ttk.Frame(Delivered)

mainwindow_order = ttk.Button(show_frame_order, text="Inventory", command=mainwindowshow)
mainwindow_predelivery = ttk.Button(show_frame_predelivery, text="Inventory", command=mainwindowshow)
mainwindow_delivered = ttk.Button(show_frame_delivered, text="Inventory", command = mainwindowshow)

predeliverywindow_order = ttk.Button(show_frame_order, text="Pre-Delivery", command=predeliverywindowshow)
predeliverywindow_main = ttk.Button(show_frame_main, text="Pre-Delivery", command=predeliverywindowshow)
predeliverywindow_delivered = ttk.Button(show_frame_delivered, text="Pre-Delivery", command=predeliverywindowshow)

orderwindow_main = ttk.Button(show_frame_main, text="Orders", command=orderwindowshow)
orderwindow_predelivery = ttk.Button(show_frame_predelivery, text="Orders", command=orderwindowshow)
orderwindow_delivered = ttk.Button(show_frame_delivered, text="Orders", command=orderwindowshow)

deliveredwindow_main = ttk.Button(show_frame_main, text="Delivered Cars", command=deliveredwindowshow)
deliveredwindow_order = ttk.Button(show_frame_order, text="Delivered Cars", command=deliveredwindowshow)
deliveredwindow_predelivery = ttk.Button(show_frame_predelivery, text="Delivered Cars", command=deliveredwindowshow)

show_frame_predelivery.pack(side="left")
show_frame_order.pack(side="left")
show_frame_main.pack(side="left")
show_frame_delivered.pack(side="left")

mainwindow_order.pack()
mainwindow_predelivery.pack()
mainwindow_delivered.pack()

predeliverywindow_order.pack()
predeliverywindow_main.pack()
predeliverywindow_delivered.pack()

orderwindow_main.pack()
orderwindow_predelivery.pack()
orderwindow_delivered.pack()

deliveredwindow_main.pack()
deliveredwindow_order.pack()
deliveredwindow_predelivery.pack()

def deliverysubmitcommand():
    
    selecteddelivery = Pre_Delivery_Cars.selection()
   
    # for r in selecteddelivery:
    #     print(Pre_Delivery_Cars.item(r)['values'])
    #     selectedvalue = Pre_Delivery_Cars.item(r)['values']
    #     alldeliveries.remove(selecteddelivery)
    #     selectedvalue.append(all_delivered)
    #     print(all_delivered)
    for r in selecteddelivery:
        print(Pre_Delivery_Cars.item(r)['values'])
        selectedvalue = Pre_Delivery_Cars.item(r)['values']
        selectedVIN=selectedvalue[0]

        selectedvalue.append(all_delivered)
        print(all_delivered)
    for i in alldeliveries:
        if i.get("VIN") == selectedVIN:
            alldeliveries.remove(i)
            i["Delivery_date"] = datetime.datetime.now().strftime('%d-%m-%Y')
            all_delivered.append(i)
            deliveredcarsdump()
            deliverydump()
            refresh_deliveries()
            refresh_delivered()
            Pre_Delivery.lift()

def Order_Submit():

    ordered_model = order_Model.get()
    ordered_trim = order_Trim.get()
    ordered_fuel = order_Fuel.get()
    ordered_color = order_Color.get()
        

    if not all([ordered_model, ordered_trim, ordered_fuel, ordered_color]):
        print("fill everything in ")
        order_confirmation_text.config(text="PLEASE FILL EVERYTHING IN")
        return
        
    for i in allcars:
        
        if i.get("Model") == ordered_model and i.get("Trim") == ordered_trim and i.get("Fuel") == ordered_fuel and i.get("Color") == ordered_color:
           
            order_confirmation_text.config(text="Already in inventory")
            # write a code to add the new order in predeliverylist
            order_i = {"VIN":i.get("VIN"),
                "Model":ordered_model,
                "Trim":ordered_trim,
                "Year":i.get("Year"), 
                "Fuel":ordered_fuel, 
                "Price":i.get("Price"),
                "Color":ordered_color,
                "Date":datetime.datetime.now().strftime('%d-%m-%Y')
            }
            alldeliveries.append(order_i)
            allcars.remove(i)
            refresh_deliveries()
            deliverydump()
            orderdump()
            inventorydelete()
            refresh_orders()
            refresh_table()
            window.lift()
            return
          

    month=datetime.datetime.now().month
    year=(datetime.datetime.now().year) + 1 if month>=6 else (datetime.datetime.now().year)

    order_placed_date = datetime.datetime.now().strftime('%d-%m-%Y')


    if ordered_model in ["Range_Rover", "Range_Rover_Sport", "F-Type", "Defender_130"]:
        price = random.randint(100000, 350000)
    elif ordered_model in ["Defender_110", "Discovery"]:
        price = random.randint(80000, 250000)
    else:
        price = random.randint(60000, 300000)

    if ordered_trim in ["SV", "Autobiography", "OCTA", "Anniversary"]:
        price += random.randint(20000, 75000) 

    if ordered_fuel in ["Electric", "PHEV"]:
        price += random.randint(5000, 30000)
            
  
    price = int(round(price, -3))


    random_serial = ''.join(choice('0123456789ABCDEF') for i in range(4))
    short = model_shorts.get(ordered_model, "XX")
    VIN = f"JLR{year}{short}{ordered_trim[0:2].upper()}{ordered_color[0].upper()}{ordered_fuel[0]}{random_serial}"

    
    order_confirmation_text.config(text="ORDER HAS BEEN CONFIRMED")
    order = {"VIN":VIN,
            "Model":ordered_model,
            "Trim":ordered_trim,
            "Year":year, 
            "Fuel":ordered_fuel, 
            "Price":price,
            "Color":ordered_color,
            "Date":order_placed_date
    }


    allorders.append(order)
    orderdump() 
    refresh_orders()

order_frame.pack()
order_Model.pack(side='left', padx=5)
order_Trim.pack(side='left', padx=5)
order_Fuel.pack(side='left', padx=5)
order_Color.pack(side='left', padx=5)

submit_button = ttk.Button(Orders,text="Submit", command=Order_Submit)
submit_button.pack(pady=20)
order_confirmation_text.pack(pady=5)

inventory_columns = tuple(sort_field)
order_coloms= tuple(sort_field2)
delivery_coloms = tuple(sort_field3)
delievered_coloms = tuple(sort_field4)

table = ttk.Treeview(window, columns = inventory_columns, show = 'headings')
Pre_Delivery_Cars = ttk.Treeview(Pre_Delivery, columns=delivery_coloms, show="headings")
Ordered_Cars = ttk.Treeview(Orders, columns=order_coloms, show="headings")
Delivered_Cars = ttk.Treeview(Delivered, columns=delievered_coloms, show="headings")

for c in inventory_columns:
    table.heading(c, text = c)
    table.column(c, width=100, anchor='center')
table.pack(fill = 'both', expand = True, padx= 10, pady= 10)

for c in delievered_coloms:
    Delivered_Cars.heading(c, text=c)
    Delivered_Cars.column(c, width=100, anchor='center')
Delivered_Cars.pack(fill = 'both', expand = True, padx= 10, pady= 10)

deliverysubmit= ttk.Button(Pre_Delivery, text="Submit", command=deliverysubmitcommand)
deliverysubmit.pack()

for c in delivery_coloms:
    Pre_Delivery_Cars.heading(c, text = c)
    Pre_Delivery_Cars.column(c, width=100, anchor='center')

Pre_Delivery_Cars.pack(fill = 'both', expand = True, padx= 10, pady= 10)

for c in order_coloms:
    Ordered_Cars.heading(c, text = c)
    Ordered_Cars.column(c, width=100, anchor='center')
Ordered_Cars.pack(fill = 'both', expand = True, padx= 10, pady= 10)


refresh_table()
refresh_orders()
refresh_deliveries()
refresh_delivered()

def on_select(event):

    for item in table.selection():
        print("Selected:", table.item(item)["values"])

def on_delete(event):


    for item in table.selection():
        table.delete(item)
def on_select_order(event):

    for item in Ordered_Cars.selection():
        print("Selected:", Ordered_Cars.item(item)["values"])

def on_delete_order(event):


    for item in Ordered_Cars.selection():
        Ordered_Cars.delete(item)
selecteddelivery = []     
def on_select_predelivery(event):

    for item in Pre_Delivery_Cars.selection():
        selecteddelivery = ("Selected:", Pre_Delivery_Cars.item(item)["values"])

def on_delete_predelivery(event):


    for item in Pre_Delivery_Cars.selection():
        Pre_Delivery_Cars.delete(item)

def on_select_Delivered(event):

    for item in Delivered_Cars.selection():
        selecteddelivery = ("Selected:", Delivered_Cars.item(item)["values"])

def on_delete_Delivered(event):


    for item in Delivered_Cars.selection():
        Delivered_Cars.delete(item)


table.bind('<<TreeviewSelect>>', on_select)
table.bind('<Delete>', on_delete)
Ordered_Cars.bind('<<TreeviewSelect>>', on_select_order)
Ordered_Cars.bind('<Delete>', on_delete_order)
Pre_Delivery_Cars.bind('<<TreeviewSelect>>', on_select_predelivery)
Pre_Delivery_Cars.bind('<Delete>', on_delete_predelivery)


window.mainloop()