from tkinter import *
from tkinter import messagebox # not a class of tkinter so separate import
from random import shuffle , choice , randint
import pyperclip
YELLOW = "#FFFDB5"
NAVY = "#050C9C"
LGHTER_BLUE = "#4F75FF"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_entry.delete(0, END)

    # using list comprehension
    pass_letter = [choice(letters) for _ in range(randint(6,8))]
    pass_symbol = [choice(symbols) for _ in range(randint(1,2))]
    pass_number = [choice(numbers) for _ in range(randint(2,4))]

    password_list = pass_letter + pass_symbol + pass_number
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)

def clear_all():
    email_entry.delete(0,END)
    password_entry.delete(0,END)
    website_entry.delete(0,END)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) ==0:
        messagebox.showinfo(title="OOPS" ,message="Please Don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title= website, message= f" These are the details you entered : \n Email: {email}"
                                                    f"\n Password: {password} \n Is this what you want to save?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password} \n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=60, pady=60, bg=YELLOW)

# adding image
img = PhotoImage(file="logo.png")
canvas = Canvas(width=520, height=520, bg=YELLOW, highlightthickness=0)
canvas.create_image((270,280), image=img)
canvas.grid(column=1, row=0)
# Label below image
app_label = Label(text="Password Manager", font=("Verdana", 28 , "italic"), bg=YELLOW, fg=NAVY)
app_label.grid(column=0, row=1, columnspan=5, pady=(10, 20))

# Labels
website_label= Label(text= "Website:", font=("Arial",19), bg=YELLOW, fg=NAVY)
website_label.grid(column=0, row=2,pady=5)

email_label = Label(text= "Email/Username:", font=("Arial",19), bg=YELLOW, fg=NAVY)
email_label.grid(column=0, row=3,pady=5)

password_label = Label(text="Password:", font=("Arial",19), bg=YELLOW, fg=NAVY)
password_label.grid(column=0,row=4,pady=5)

# Entries
website_entry = Entry(width=39, highlightthickness=0)
website_entry.grid(column=1, row=2, columnspan=2, pady=5)
website_entry.focus()

email_entry = Entry(width=39, highlightthickness=0)
email_entry.grid(column=1, row=3, columnspan=2, pady=5)
# Default or most used value for email
email_entry.insert(0 , "lipivirmani182@gmail.com")

password_entry = Entry(width=22, highlightthickness=0)
password_entry.grid(column=1,row=4, pady=5)

# Buttons
Gen_pass_button = Button(text="Generate Password", highlightthickness=0,command=generate_pass)
Gen_pass_button.grid(column=2, row=4,sticky="w")

add_button = Button(text="Add", width=36, highlightthickness=0, bg=YELLOW, command=save)
add_button.grid(column=1, row=5, columnspan=2 , pady=15)

clear_button= Button(text= "Clear", width= 12, highlightthickness=0, command=clear_all )
clear_button.grid(column=0, row=5, pady=15)


window.mainloop()
