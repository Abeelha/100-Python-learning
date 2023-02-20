# Theodoro Bertol Dev (Abeelha) #
# || Day 27 of #100DaysOfCode || #

from tkinter import *
 
window = Tk()
window.minsize(width=150, height=150)
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)
MY_FONT = ("Ink Free", 18, "bold")
 
def reset():
    from_txt.config(text="Mile")
    to_txt.config(text="Km  ")
    input.delete(first=0, last=7)
    result.config(text="0")
 
def miles_to_km():
    from_txt.config(text="Mile")
    to_txt.config(text="Km  ")
    final_result = round(float(input.get()) * 1.609, 3)
    result.config(text=f"{final_result}")
 
def km_to_mt():
    from_txt.config(text="Km  ")
    to_txt.config(text="mt  ")
    final_result = round(float(input.get()) * 1000, 3)
    result.config(text=f"{final_result}")
 
def mt_to_km():
    from_txt.config(text="mt  ")
    to_txt.config(text="Km  ")
    final_result = round(float(input.get()) / 1000, 3)
    result.config(text=f"{final_result}")
 
def km_to_miles():
    from_txt.config(text="Km  ")
    to_txt.config(text="Mile")
    final_result = round(float(input.get()) / 1.609, 3)
    result.config(text=f"{final_result}")
 
def mt_to_miles():
    from_txt.config(text="mt  ")
    to_txt.config(text="Mile")
    final_result = round(float(input.get()) / 1609, 3)
    result.config(text=f"{final_result}")
 
def miles_to_mt():
    from_txt.config(text="Mile")
    to_txt.config(text="mt  ")
    final_result = round(float(input.get()) * 1609, 3)
    result.config(text=f"{final_result}")
 
 
input = Entry(width=7, font=MY_FONT)
input.focus()
input.grid(column=1, row=0)
 
from_txt = Label(text="Miles", font=MY_FONT)
from_txt.grid(column=2, row=0)
from_txt.config(padx=10, )
 
equal_txt = Label(text="is equal to: ", font=MY_FONT)
equal_txt.grid(column=0, row=1)
 
result = Label(text="0", font=MY_FONT)
result.grid(column=1, row=1)
result.config(pady=20)
 
to_txt = Label(text="Km", font=MY_FONT)
to_txt.grid(column=2, row=1)
 
calculate_btn = Button(text="Reset", command=reset)
calculate_btn.grid(column=1, row=2)
 
def listbox_used(event):
    if listbox.get(listbox.curselection()) == "Kilometer to Meter":
        if input.get() != "":
            km_to_mt()
    elif listbox.get(listbox.curselection()) == "Meter to Kilometer":
        if input.get() != "":
            mt_to_km()
    elif listbox.get(listbox.curselection()) == "Kilometer to Miles":
        if input.get() != "":
            km_to_miles()
    elif listbox.get(listbox.curselection()) == "Miles to Kilometer":
        if input.get() != "":
            miles_to_km()
    elif listbox.get(listbox.curselection()) == "Meter to Miles":
        if input.get() != "":
            mt_to_miles()
    elif listbox.get(listbox.curselection()) == "Miles to Meter":
        if input.get() != "":
            miles_to_mt()
 
 
listbox = Listbox(height=3)
convertions = ["Kilometer to Miles", "Kilometer to Meter", "Meter to Kilometer", "Meter to Miles", "Miles to Kilometer", "Miles to Meter"]
for item in convertions:
    listbox.insert(convertions.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid(column=4, row=1)

window.mainloop()