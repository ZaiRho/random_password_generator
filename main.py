from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_pass():
    input_pass.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    new_password = ""
    for char in password_list:
        new_password += char
    input_pass.insert(0, new_password)
    pyperclip.copy(new_password)
    messagebox.showinfo(title="Info", message="Password copied to the clipboard")
# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_pass():
    with open("data.txt", mode="a") as file:
        web = input_web.get()
        if len(web) == 0 or web =="":
            messagebox.showwarning(title="Warning", message="Must not leave the website empty")
            return
        user = input_user.get()
        if len(user) == 0 or user =="":
            messagebox.showwarning(title="Warning", message="Must not leave the User / Email empty")
            return
        _pass = input_pass.get()
        if len(_pass) == 0 or _pass =="":
            messagebox.showwarning(title="Warning", message="Must not leave the password empty")
            return
        entry = f"{web} | {user} | {_pass}\n"
        is_ok = messagebox.askokcancel(title=web, message=f"Verify details: \nWebsite: {web}\nUser / Email: {user}\nPassword: {_pass}\nPress 'Ok' to confirm")
        if is_ok:
            file.write(entry)
            input_web.delete(0, END)
            input_pass.delete(0, END)
            messagebox.showinfo(title="Info", message="Saved!")
# ---------------------------- UI SETUP ------------------------------- #


FONT_NAME = "calibri"


window = Tk()
window.title("Password Manager")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website = Label(text="Website:", font=(FONT_NAME, 10, "normal"))
website.grid(column=0, row=1)

email = Label(text="Email / Username:", font=(FONT_NAME, 10, "normal"))
email.grid(column=0, row=2)

password = Label(text="Password:", font=(FONT_NAME, 10, "normal"))
password.grid(column=0, row=3)

input_web = Entry(width=43)
input_web.focus()
input_web.grid(column=1, row=1, columnspan=2, sticky=W)

input_user = Entry(width=43)
input_user.insert(0, "sample@gmail.com")
input_user.grid(column=1, row=2, columnspan=2, sticky=W)

input_pass = Entry(width=24)
input_pass.grid(column=1, row=3, sticky=W)

button_pass = Button(text="Generate Password", command=generate_pass)
button_pass.grid(column=1, row=3, sticky=E)

button_add = Button(text="Add", command=add_pass, width=36)
button_add.grid(column=1, row=5)


window.mainloop()
