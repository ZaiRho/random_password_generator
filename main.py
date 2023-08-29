# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    pass
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_pass():
    pass
# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *
FONT_NAME = "calibri"


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website = Label(text="Website:", font=(FONT_NAME, 10, "normal"))
website.grid(column=0, row=1)
# website.config(padx=10, pady=10)

email = Label(text="Email / Username:", font=(FONT_NAME, 10, "normal"))
email.grid(column=0, row=2)
# email.config(padx=10, pady=10)

password = Label(text="Password:", font=(FONT_NAME, 10, "normal"))
password.grid(column=0, row=3)
# password.config(padx=10, pady=10)

input_web = Entry(width=40)
input_web.grid(column=1, row=1, columnspan=2, sticky=W)

input_user = Entry(width=36)
input_user.grid(column=1, row=2, columnspan=2, sticky=W)

input_pass = Entry(width=23)
input_pass.grid(column=1, row=3, sticky=W)

button_pass = Button(text="Generate Password", command=generate_pass)
button_pass.grid(column=1, row=3, sticky=E)

button_add = Button(text="Add", command=add_pass, width=36)
button_add.grid(column=1, row=5)

window.mainloop()
