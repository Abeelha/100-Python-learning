# Theodoro Bertol Dev (Abeelha) #
# || Day 29 of #100DaysOfCode || #

from tkinter import *
from tkinter import messagebox
import hashlib
from random import choice, randint, shuffle
import pyperclip

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
        # generate encrypted password:
        #TODO try making this decode and incript password work
        encode_pass = hashlib.sha256(password.encode())
        password = encode_pass.hexdigest()
        with open("C:/Users/Abeelha/Documents/Programs/100 Python learning/Day 20 - 29/Day 29/data.txt", "a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            

# ---------------------------- DECODE PASSWORD ------------------------------- # 
#TODO try making this decode and incript password work  
def decrypt_and_store():
    # Get information from data.txt
    with open('C:/Users/Abeelha/Documents/Programs/100 Python learning/Day 20 - 29/Day 29/data.txt', 'r') as data_file:
        lines = data_file.readlines()
        data_info = [line.strip().split(' | ') for line in lines]
    
    # Get the encryption key
    encryption_key = input("Please enter your encryption key: ")
    
    # Decrypt passwords
    decrypted_passwords = [decrypt(password, encryption_key) for website, _, password in data_info]

    # Store in new file
    file_name = input("Please enter a file name to store the decrypted passwords: ")
    with open('C:/Users/Abeelha/Documents/Programs/100 Python learning/Day 20 - 29/Day 29/{}.txt'.format(file_name), 'w+') as new_file:
        for website, password in zip(data_info, decrypted_passwords):
            website_entry, email_entry, encrypted_password = website
            new_file.write(f'{website_entry} | {email_entry} | {password}\n')

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
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# ---------------------------- Buttons ------------------------------- #
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)


# ---------------------------- Decrypt Password Button ------------------------------- #
#TODO try making this decode and incript password work
# decode_password_button = Button(text="Decrypt Password", command=decrypt_and_store)
# decode_password_button.grid(row=5, column=1, columnspan=2)

window.mainloop()