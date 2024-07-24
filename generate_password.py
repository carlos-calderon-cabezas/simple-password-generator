from random import randint, choice, shuffle
import pyperclip
from tkinter import messagebox


def generate_password(password_entry, checked_state):
    letters = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)]
    numbers = [str(i) for i in range(10)]
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    random_password = "".join(password_list)

    password_entry.delete(0, "end")
    password_entry.insert(0, random_password)

    if checked_state.get() == 1:
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

    pyperclip.copy(random_password)
    messagebox.showinfo(title="Password Generator", message="Password successfully generated and copied to clipboard!")
