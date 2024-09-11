import tkinter as tk
from tkinter import ttk, messagebox

#to store contact 
contacts_list = []

#to Add Contact
def add_contact():
    name = name_entry.get()
    phone = phoneno_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    
    if name == "" and phone == "":
        messagebox.showwarning("Input Error"," Name and Phone no are Required Field")
        return
    
    contacts_list.append({
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    })
    
    name_entry.delete(0,tk.END)
    phoneno_entry.delete(0,tk.END)
    email_entry.delete(0,tk.END)
    address_entry.delete(0,tk.END)
    
    messagebox.showinfo("Success","Contact Save Successfully")
    
    view_contact()
    
#to View Contact  
def view_contact():
    for i in contact_list.get_children():
        contact_list.delete(i)
    
    for idx, contact in enumerate(contacts_list):
        contact_list.insert("", tk.END, values=(idx+1, contact['name'], contact['phone']))

#to search Contact
def search_contact():
    search_term = search_entry.get()
    
    for i in contact_list.get_children():
        contact_list.delete(i)
    
    for idx, contact in enumerate(contacts_list):
        if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
            contact_list.insert("", tk.END, values=(idx+1, contact['name'], contact['phone']))

#to update contact
def update_contact():
    selected_item = contact_list.selection()[0]
    contact_index = int(contact_list.item(selected_item, 'values')[0]) - 1
    
    new_name = name_entry.get()
    new_phone = phoneno_entry.get()
    new_email = email_entry.get()
    new_address = address_entry.get()
    
    if new_name == "" or new_phone == "":
        messagebox.showwarning("Input Error", "Name and Phone are required fields")
        return
    
    contacts_list[contact_index] = {
        'name': new_name,
        'phone': new_phone,
        'email': new_email,
        'address': new_address
    }
    
    messagebox.showinfo("Success", "Contact updated successfully!")
    view_contact()

#to delete contact
def delete_contact():
    selected_item = contact_list.selection()[0]
    contact_index = int(contact_list.item(selected_item, 'values')[0]) - 1
    
    del contacts_list[contact_index]
    
    messagebox.showinfo("Success", "Contact deleted successfully!")
    view_contact()


root = tk.Tk()
root.title("Contact Book")
root.geometry("900x400")

#Contact Form
tk.Label(root, text="Name:").grid(row=0,column=0, padx=10, pady=10)
tk.Label(root, text="Phone No:").grid(row=1,column=0, padx=10, pady=10)
tk.Label(root, text="Email ID:").grid(row=2,column=0, padx=10, pady=10)
tk.Label(root, text="Address:").grid(row=3,column=0, padx=10, pady=10)

name_entry = tk.Entry(root)
phoneno_entry = tk.Entry(root)
email_entry = tk.Entry(root)
address_entry = tk.Entry(root)

name_entry.grid(row=0,column=1, padx=10, pady=10)
phoneno_entry.grid(row=1,column=1, padx=10, pady=10)
email_entry.grid(row=2,column=1, padx=10, pady=10)
address_entry.grid(row=3,column=1, padx=10, pady=10)

add_contact_button = tk.Button(root, text="Add Contact", command=add_contact).grid(row=4, column=0, columnspan=2, pady=10)

#Contact list
contact_list = ttk.Treeview(root,columns=("ID","Name","Phone"), show="headings")
contact_list.heading("ID", text="ID")
contact_list.heading("Name", text="Name")
contact_list.heading("Phone", text="Phone")
contact_list.grid(row=0, column=2, rowspan=5,padx=10, pady=10)
    
#Search Bar
tk.Label(root, text="Search: ").grid(row=5,column=0, padx=10, pady=10)
search_entry = tk.Entry(root)
search_entry.grid(row=5, column=1, padx=10, pady=10)
search_contact_button = tk.Button(root, text="Search", command=search_contact).grid(row=5,column=2, padx=10, pady=10)

#Update and Delete Button
update_contact_button = tk.Button(root, text="Update Selected", command=update_contact).grid(row=6, column=1, padx=10, pady=10)
delete_contact_button = tk.Button(root, text="Delete Selected", command=delete_contact).grid(row=6, column=2, padx=10, pady=10)

view_contact()

root.mainloop()