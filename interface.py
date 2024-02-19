import tkinter
from tkinter import ttk
import os
import subprocess
import sys
import time
window = tkinter.Tk()
window.title("Bot for sniping")
with open('states.txt', 'r') as file:
    values= file.readlines()

def enter_data():
    email = email_entry.get()
    password = password_entry.get()
    productname = product_name_entry.get()
    productprice = product_price_entry.get()
    firstname = FirstName_entry.get()
    lastname = LastName_entry.get()
    phone = phone_entry.get()
    state = state_combobox.get()
    city = city_entry.get()
    street = street_entry.get()
    regstatus = reg_status.get()
    if regstatus == "1":
        accountstatus = "0"
    else:
        accountstatus = "1"
    with open('accountdetails.txt', 'w') as file:
        file.write(f'{email}\n')
        file.write(f'{password}\n')
        file.write(f'{firstname}{" "}{lastname}\n')
        file.write(f'{phone}\n')
        file.write(f'{state}')
        file.write(f'{city}\n')
        file.write(f'{street}\n')
        file.write(f'{productname}\n')
        file.write(f'{productprice}\n')
        file.write(f'{accountstatus}\n')
    
    # run the bot
    if regstatus == "1":
        # Get the current working directory
        current_directory = os.getcwd()
        # Specify the command to run
        command = ['python', os.path.join(current_directory, 'find.py')]
        # Use subprocess to run the command
        subprocess.run(command, check=True, text=True)
        window.destroy()  
    else:
        # Get the current working directory
        current_directory = os.getcwd()
        # Specify the command to run
        command = ['python', os.path.join(current_directory, 'newaccount.py')]
        # Use subprocess to run the command
        subprocess.run(command, check=True, text=True)
        window.destroy() 

frame = tkinter.Frame(window)
frame.pack()

#saving user info
user_info_frame = tkinter.LabelFrame(frame, text="Account Info")
user_info_frame.grid(row=0, column=0, padx=20, pady=20)

registered_user = tkinter.Label(user_info_frame)
registered_user.grid(row=0, column=0, sticky="news")
reg_status = tkinter.StringVar()
registered_email_check = tkinter.Checkbutton(registered_user, text="You have an registered email and password on Emag?" , variable=reg_status, onvalue="1", offvalue="0")
registered_email_check.grid(row=0, column=0)

email = tkinter.Label(user_info_frame, text="Email")
email.grid(row=2, column=0)  # changed row from 1 to 2
password = tkinter.Label(user_info_frame, text="Password")
password.grid(row=2, column=1)  # changed row from 1 to 2

email_entry = tkinter.Entry(user_info_frame)
password_entry = tkinter.Entry(user_info_frame)
email_entry.grid(row=3, column=0)  # changed row from 2 to 3
password_entry.grid(row=3, column=1)  # changed row from 2 to 3

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=5,pady=2)

#saving product info

product_info_frame = tkinter.LabelFrame(frame, text="Product Info")
product_info_frame.grid(row=1, column=0, sticky="news", padx=20, pady=20)

product_name = tkinter.Label(product_info_frame, text="Product Name")
product_name.grid(row=0, column=0)
product_name_entry = tkinter.Entry(product_info_frame)
product_name_entry.grid(row=1, column=0)
product_price = tkinter.Label(product_info_frame, text="Product Price")
product_price.grid(row=0, column=1)
product_price_entry = tkinter.Entry(product_info_frame)
product_price_entry.grid(row=1, column=1)
for widget in product_info_frame.winfo_children():
    widget.grid_configure(padx=5,pady=2)

#saving Adress info
adress_info_frame = tkinter.LabelFrame(frame, text="Adress Info")
adress_info_frame.grid(row=2, column=0, sticky="news", padx=20, pady=20)
FirstName = tkinter.Label(adress_info_frame, text="First Name")
FirstName.grid(row=0, column=0)
FirstName_entry = tkinter.Entry(adress_info_frame)
FirstName_entry.grid(row=1, column=0)
LastName = tkinter.Label(adress_info_frame, text="Last Name")
LastName.grid(row=0, column=1)
LastName_entry = tkinter.Entry(adress_info_frame)
LastName_entry.grid(row=1, column=1)
phone = tkinter.Label(adress_info_frame, text="Phone")
phone.grid(row=0, column=2)
phone_entry = tkinter.Entry(adress_info_frame)
phone_entry.grid(row=1, column=2)
state = tkinter.Label(adress_info_frame, text="State")
state.grid(row=2, column=0)

state_combobox = ttk.Combobox(adress_info_frame, values=values)
state_combobox.grid(row=3, column=0)
city = tkinter.Label(adress_info_frame, text="City")
city.grid(row=2, column=1)
city_entry = tkinter.Entry(adress_info_frame)
city_entry.grid(row=3, column=1)
street = tkinter.Label(adress_info_frame, text="Street")
street.grid(row=2, column=2)
street_entry = tkinter.Entry(adress_info_frame)
street_entry.grid(row=3, column=2)
for widget in adress_info_frame.winfo_children():
    widget.grid_configure(padx=5,pady=2)

#summit
button = tkinter.Button(frame, text="RUN", command = enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=20)

window.mainloop()