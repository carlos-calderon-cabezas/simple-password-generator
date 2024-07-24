from tkinter import messagebox
import json
from encrypt_password import encrypt_pass


def save(website_entry, email_entry, password_entry):
    website = website_entry.get()
    email = email_entry.get()
    unencrypted_pass = password_entry.get()
    password = encrypt_pass(unencrypted_pass)

    new_data = {
        website: {
            "email": email,
            "password": password.hex(),
        },
    }

    if len(website) == 0 or len(email) == 0 or len(unencrypted_pass) == 0:
        messagebox.showinfo(title="Error", message="Please don't leave any fields empty!")
        return

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        with open("data.json", "w") as data_file:
            json.dump(new_data, data_file, indent=4)
    else:
        data.update(new_data)
        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)

    website_entry.delete(0, "end")
    password_entry.delete(0, "end")

    messagebox.showinfo(title="Success", message="Password saved successfully!")
