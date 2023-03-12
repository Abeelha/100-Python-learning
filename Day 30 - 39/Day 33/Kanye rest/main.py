# Theodoro Bertol Dev (Abeelha) #
# || Day 33 of #100DaysOfCode || #

from tkinter import *
import requests

def get_quote():
    quote_json = requests.get("https://api.kanye.rest")
    quote = quote_json.json()["quote"]
    canvas.itemconfig(quote_text, text= quote)

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="C:/Users/Abeelha/Documents/Programs/100 Python learning/Day 30 - 39/Day 33/Kanye rest/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="C:/Users/Abeelha/Documents/Programs/100 Python learning/Day 30 - 39/Day 33/Kanye rest/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()