from tkinter import *
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generatepass():

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
    passwerd = ''.join(password_list)

    input_pass.delete(0, END)
    input_pass.insert(0, passwerd)
    input_pass.clipboard_append(input_pass.get())

# ---------------------------- SAVE PASSWORD ------------------------------- #
def addpass():

    new_data = {
        input_web.get(): {
            "Mail": input_mail.get(),
            "Password": input_pass.get()
            }
        }

    if input_web.get() == "" or input_mail.get() == "" or input_pass.get() == "":
        messagebox.showerror(title="вы тупое звено. и слабое еще. ха ха ха ха хаххааххахахахахахах", message="((((")
    else:
        if_ok = messagebox.askyesno(title="армяне",
                                    message=f"смотри\nсайт вообще, тебе 7 лет штоли: {input_web.get()}\nвот такой ты емайл указал, "
                                            f"лол: {input_mail.get()}\nа это что, пароль что-ли? мде ну ты"
                                            f" конечно мда: {input_pass.get()}\n")
        if if_ok:
            try:
                with open("pass.json", mode="r") as file:
                    data = json.load(file)
            #  ошибка появляется при открытии файла, который не найден

            except FileNotFoundError:
                with open("pass.json", mode="w") as file:
                    json.dump(new_data, file, indent=4)
             #создаём новый файл, если файла не было
            else:
                data.update(new_data)
                with open("pass.json", mode="w") as file:
                    json.dump(data, file, indent=4)
            #если не было исключений, то файл имеющийся открываем и наполняем данными

            finally:
                input_pass.clipboard_append(input_pass.get())
                input_web.delete(0, END)
                input_mail.delete(0, END)
                input_pass.delete(0, END)
            #всегда исполняем эти действия вне зависимости от исключений

#----------------------------FIND PASS ---------------------------------------#

def findpass():
    try:
        with open("pass.json", mode="r") as file:
            data = json.load(file)
            messagebox.showinfo(title=input_web.get(), message=f'{data[input_web.get()]["Mail"]}\n'
                                                               f'{data[input_web.get()]["Password"]}')
    except KeyError:
        messagebox.showinfo(title=input_web.get(), message="Сайт не найден. ЧМО.")
    except FileNotFoundError:
        messagebox.showinfo(title=input_web.get(), message="Файла нет!")




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pass")
window.config(padx=50, pady=50)
window.minsize(width=500, height=350)

canvas = Canvas (width=210, height=200, highlightthickness=0)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(110, 100, image=pass_img)
canvas.grid(column=1, row=0)

website = Label(text="Website", font=("Calibri", 12, "normal"))
website.grid(column=0, row=1)

email = Label(text="Email/Username", font=("Calibri", 12, "normal"))
email.grid(column=0, row=2)

passw = Label(text="Password", font=("Calibri", 12, "normal"))
passw.grid(column=0, row=3)

#Website
input_web = Entry(width=36)
input_web.grid(column=1, row=1)
input_web.focus()
input_web.insert(0, "youtube")

#Mail
input_mail = Entry(width=55)
input_mail.grid(column=1, row=2, columnspan=2)
input_mail.insert(0, "kukuha@mail.ru")

#Password
input_pass = Entry(width=36)
input_pass.grid(column=1, row=3)
input_pass.insert(0, "1234")

#Buttons--------------

pass_button = Button(text="Generate Password", command=generatepass)
pass_button.grid(column=2, row=3)

add = Button(text="Add", command=addpass, width=47)
add.grid(column=1, row=4, columnspan=2)

search_butt = Button(text="Search", command=findpass, width=15)
search_butt.grid(column=2, row=1)

window.mainloop()
