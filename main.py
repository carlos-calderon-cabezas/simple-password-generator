from tkinter import *
from generate_password import generate_password
from save_password import save
from find_password import find_password
from show_password import show_password

PAD_LABELS_y = 5
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

window = Tk()
window.title("Password Manager")
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
generate_password_button = Button(text="Generate Password", highlightthickness=0, bg=RED, fg="white", command=lambda: generate_password(password_entry, checked_state))
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, highlightthickness=0, bg=RED, fg="white", command=lambda: save(website_entry, email_entry, password_entry))
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

search_button = Button(text="Search", highlightthickness=0, bg=RED, fg="white", command=lambda: find_password(website_entry))
search_button.grid(row=1, column=2, sticky="EW")

# Check Button
checked_state = IntVar()
checkbutton = Checkbutton(text="Show Password?", variable=checked_state, command=lambda: show_password(password_entry, checked_state), bg=RED)
checkbutton.grid(row=5, column=1, columnspan=2, sticky="EW")

window.mainloop()
