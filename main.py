import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Style
import openpyxl

def insert_row():
    name= name_entry.get()
    age= int(age_spinbox.get())
    subscription_type= status_combobox.get()
    employment_status= "Employed" if a.get() else "Unemployed"

    print(name, age, subscription_type, employment_status)
    path = r"C:\Users\ACER\OneDrive\Documents\School\Third Year\SSX361\Excel viewer with tkinter and openxyl Faith Malatji\people.xlsx"
    workbook = openpyxl.load_workbook(path)
    sheet= workbook.active
    row_values= [name, age, subscription_type, employment_status]
    sheet.append(row_values)
    workbook.save(path)

    treeview.insert('', tk.END, values=row_values)

    name_entry.delete(0,"end")
    name_entry.insert(0, "Name")
    age_spinbox.delete(0, "end")
    age_spinbox.insert(0, "Age")
    status_combobox.set(combo_list[0])
    checkbutton.state(["!selected"])

def load_data():
    path= r"C:\Users\ACER\OneDrive\Documents\School\Third Year\SSX361\Excel viewer with tkinter and openxyl Faith Malatji\people.xlsx"
    workbook= openpyxl.load_workbook(path)

    sheet=workbook.active
    list_values= list(sheet.values)
    print(list_values)
    for col_name in list_values[0]:
        treeview.heading(col_name, text=col_name)

    for value_tuple in list_values[1:]:
        treeview.insert('', tk.END, values=value_tuple)


def toggle_mode():
    if mode_switch.instate(["selected"]):
        style.theme_use("forest-dark")
    else:
        style.theme_use("forest-light")

combo_list= ["Free","Basic", "Premium"]

root= tk.Tk()
style= Style(root)
root.tk.call("source", 'forest-light.tcl')
root.tk.call("source", 'forest-dark.tcl')
style.theme_use("forest-light")

frame= ttk.Frame(root)
frame.pack()# makes window responsive

widgets_frame= ttk.LabelFrame(frame, text="Insert Row")
widgets_frame.grid(row=0, column=0, padx=20, pady=10)

name_entry= ttk.Entry(widgets_frame)
name_entry.insert(0, "Name")
name_entry.bind("<FocusIn>", lambda e: name_entry.delete("0","end")) #deletes name so you can input your name/ lamdda calls a function
name_entry.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

age_spinbox= ttk.Spinbox(widgets_frame, from_=18, to=100)
age_spinbox.insert(0,"Age")
age_spinbox.grid(row=1, column=0, sticky="ew",padx=5, pady=5)

status_combobox= ttk.Combobox(widgets_frame, values=combo_list)
status_combobox.current(0)
status_combobox.grid(row=2, column=0, sticky="ew",padx=5, pady=5)

a=tk.BooleanVar()
checkbutton= ttk.Checkbutton(widgets_frame, text="Employed", variable=a)
checkbutton.grid(row=3, column=0, sticky="nsew", padx=5, pady=5)

button= ttk.Button(widgets_frame, text="Insert", command= insert_row)
button.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")

separator= ttk.Separator(widgets_frame)
separator.grid(row=5, column=0, padx=(20,10), pady=10, sticky="ew")

mode_switch= ttk.Checkbutton(
    widgets_frame, text="Mode", style="Switch", command=toggle_mode
)
mode_switch.grid(row=6, column=0, padx=5, pady=10, sticky="nsew")

treeFrame= ttk.Frame(frame)
treeFrame.grid(row=0, column=1, pady=10)
treeScroll= ttk.Scrollbar(treeFrame)
treeScroll.pack(side="right", fill= "y")

cols= ("Name","Age","Subscription","Employment")
treeview= ttk.Treeview(treeFrame, show="headings", columns=cols, height=13, yscrollcommand=treeScroll.set)
treeview.column("Name", width=100)
treeview.column("Age", width=50)
treeview.column("Subscription", width=100)
treeview.column("Employment", width=100)

load_data()
treeview.pack()
treeScroll.config(command=treeview.yview)



root.mainloop()
