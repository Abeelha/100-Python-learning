# Theodoro Bertol Dev (Abeelha) #
# || Day 29 of #100DaysOfCode || #

# ---------------------------- IMPORTS ------------------------------- #

from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import csv, hashlib, pyperclip, json 

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    elif is_ok := messagebox.askokcancel(
        title=website,
        message=f"These are the details entered: \nEmail: {email} "
        f"\nPassword: {password} \nIs it ok to save?",
    ):
        passwords(password, website, email)

##--------------SAVING FILES:--------------##
def saving_in_file(data_file, website, email, arg3):
    writer = csv.writer(data_file, lineterminator='\n')
    writer.writerow([website, email, arg3])
    website_entry.delete(0, END)
    password_entry.delete(0, END)

##--------------GENERATE ENCRYPTED PASSWORD:--------------##
def passwords(password, website, email):

    decoded_pass = password
    encode_pass = hashlib.sha256(password.encode())
    password = encode_pass.hexdigest()

    ##-------------------- SAVING AS TXT: --------------------##

    # with open("C:/Users/Abeelha/Documents/Programs/100 Python learning/Day 20 - 29/Day 29/data_coded.txt", "a") as data_file:
    #     saving_in_file(data_file, website, email, password)
    # with open("C:/Users/Abeelha/Documents/Programs/100 Python learning/Day 20 - 29/Day 29/data_decoded.txt", "a") as data_file:
    #     saving_in_file(data_file, website, email, decoded_pass)
    
    ##-------------------- SAVING AS CSV: --------------------##

    with open("C:/Users/Abeelha/Documents/Programs/100 Python learning/Day 20 - 29/Day 29/data_coded.csv", "a") as data_file:
        saving_in_file(data_file, website, email, password)
    with open("C:/Users/Abeelha/Documents/Programs/100 Python learning/Day 20 - 29/Day 29/data_decoded.csv", "a") as data_file:
        saving_in_file(data_file, website, email, decoded_pass)
        
        
# # ---------------------------- FIND PASSWORD ------------------------------- #
# def find_password():
#     website = website_entry.get()
#     try:
#         with open("C:/Users/Abeelha/Documents/Programs/100 Python learning/Day 20 - 29/Day 29/data.json") as data_file:
#             data = json.load(data_file)
#     except FileNotFoundError:
#         messagebox.showinfo(title="Error", message="No Data File Found.")
#     else:
#         if website in data:
#             email = data[website]["email"]
#             password = data[website]["password"]
#             messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
#         else:
#             messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="C:/Users/Abeelha/Documents/Programs/100 Python learning/Day 20 - 29/Day 29/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


# ---------------------------- Labels ------------------------------- #
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# ---------------------------- Entries ------------------------------- #
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "angela@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# ---------------------------- Buttons ------------------------------- #
# search_button = Button(text="Search", width=13, command=find_password)
# search_button.grid(row=1, column=2)
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)


# ---------------------------- Decrypt Password Button ------------------------------- #
# decode_password_button = Button(text="Decrypt Password", command=decrypt_password)
# decode_password_button.grid(row=5, column=1, columnspan=2)

window.mainloop()