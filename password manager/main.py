import tkinter as tk
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(numbers) for _ in range(randint(2, 4))]
    password_numbers = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }

    if len(password) == 0 or len(website) == 0:
        tk.messagebox.showerror(title="Invalid details!",
                                message="Please make sure you have entered all relevant details")
    else:
        save_ok = tk.messagebox.askokcancel(title=website,
                                            message=f"You are trying to save: "
                                                    f"\n Username: {username} \n Password: {password}")
        if save_ok:
            data = {}
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
                    data.update(new_data)
            except FileNotFoundError:
                data = new_data
            finally:
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
                    website_entry.delete(0, tk.END)
                    password_entry.delete(0, tk.END)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file was found")
    else:
        if website in data:
            website_dict = data[website]
            password = website_dict["password"]
            username = website_dict["username"]
            messagebox.showinfo(title=website, message=f"Username: {username} \n Password: {password}")
        else:
            messagebox.showerror(title="Error", message=f"No details for {website} exists")


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = tk.Canvas(height=200, width=200)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = tk.Label(text="Website: ")
website_label.grid(column=0, row=1)
website_entry = tk.Entry(width=33)
website_entry.grid(row=1, column=1)
website_entry.focus()

search_button = tk.Button(text="Search", width=14, command=search)
search_button.grid(column=2, row=1)

username_label = tk.Label(text="Email/Username: ")
username_label.grid(column=0, row=2)
username_entry = tk.Entry(width=52)
username_entry.insert(0, "dummy_email@gmail.com")
username_entry.grid(row=2, column=1, columnspan=2)

password_label = tk.Label(text="Password: ")
password_label.grid(column=0, row=3)
password_entry = tk.Entry(width=33)
password_entry.grid(row=3, column=1)
generate_password_button = tk.Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = tk.Button(text="Add", width=45, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
