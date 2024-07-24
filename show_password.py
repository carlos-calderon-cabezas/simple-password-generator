def show_password(password_entry, checked_state):
    if checked_state.get() == 1:
        password_entry.config(show="")
    else:
        password_entry.config(show="*")
