from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

PAD_LABELS_y = 5
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    random_password = "".join(password_list)

    password_entry.config(show="")
    password_entry.delete(0, END)
    password_entry.insert(0, random_password)

    pyperclip.copy(random_password)
    messagebox.showinfo(title="Password Generator", message="Password successfully generated"
                                                            " and copied to clipboard!")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        },
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Stop!", message="Please don't leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}"
                                                              f"\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
                    # Updating old data with new data
                    # data.update(new_data)  ((ELSE))
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)

            else:
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)

            finally:
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                email_entry.insert(0, "email@example.com")
                password_entry.delete(0, END)
                website_entry.focus()


def find_password():
    website = website_entry.get()
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
            website_data = data[website]

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    except KeyError:
        if website == "":
            messagebox.showerror(title="Error", message="Website field is empty!")
        else:
            messagebox.showwarning(title="Error", message=f"No details for \"{website}\" exists")
    else:
        msg_text = f'Username: {website_data["email"]}\nPassword: {website_data["password"]}'
        messagebox.showinfo(title=f"Data was found for \"{website}\"", message=msg_text)
    finally:
        pass


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50, bg="black")
window.minsize(width=505, height=410)

# Canvas (image creation)

canvas = Canvas(width=200, height=200, highlightthickness=0, bg="black")
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels

website_label = Label(text="Website:", bg="black", fg="white")
website_label.config(pady=PAD_LABELS_y)
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:", bg="black", fg="white")
email_label.config(pady=PAD_LABELS_y)
email_label.grid(row=2, column=0)
password_label = Label(text="Password:", bg="black", fg="white")
password_label.config(pady=PAD_LABELS_y)
password_label.grid(row=3, column=0)

# Entries

website_entry = Entry(width=35, bg=GREEN)
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus()
email_entry = Entry(width=35, bg=GREEN)
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_entry.insert(0, "example@gmail.com")
password_entry = Entry(width=21, show="*", bg=GREEN)
password_entry.grid(row=3, column=1, sticky="EW")

# Buttons

generate_password_button = Button(text="Generate Password", highlightthickness=0, bg=RED,
                                  fg="white", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, highlightthickness=0, bg=RED, fg="white", command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

search_button = Button(text="Search", highlightthickness=0, bg=RED, fg="white", command=find_password)
search_button.grid(row=1, column=2, sticky="EW")


# Check Button

def show_password():
    if checked_state.get() == 1:
        password_entry.config(show="")
    else:
        password_entry.config(show="*")


checked_state = IntVar()
checkbutton = Checkbutton(text="Show Password?", variable=checked_state, command=show_password, bg=RED)
checkbutton.grid(row=5, column=1, columnspan=2, sticky="EW")

window.mainloop()
