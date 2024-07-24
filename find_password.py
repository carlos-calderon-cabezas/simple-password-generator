from tkinter import messagebox
import json
from encrypt_password import decrypt_pass


def find_password(website_entry):
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
        return

    if website in data:
        email = data[website]["email"]
        encrypted_password_hex = data[website]["password"]
        encrypted_password = bytes.fromhex(encrypted_password_hex)
        password = decrypt_pass(encrypted_password)
        messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
    else:
        messagebox.showinfo(title="Error", message=f"No details for {website} exists")
