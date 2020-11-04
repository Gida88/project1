from tkinter import *
import mysql.connector
from tkinter import messagebox

def login_screen():

    root = Tk()
    root.title("User Login")
    app_width = 290
    app_height = 100
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)
    root.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

    def login(event=None):
        global email_address
        con = mysql.connector.connect(host="localhost", user="root", password="!$aintikEr_13!", database="testdatabase")
        cursor = con.cursor()
        #verify = "select * from users where username = %s and userpassword = %s"
        cursor.execute("SElECT * FROM users")
        results = cursor.fetchall()
        print(results)
        access = False
        for result in results:
            if result[1] == username.get() and result[2] == password.get():
                access = True
                print(result[0])
                email_address = result[0]
        if access:
            root.destroy()
            return email_address
        else:
            messagebox.showinfo("Login Failed", "Username and/or Password Incorrect")


    def show_password():
        if selection.get() == 0:
            e_pass.config(show="*")
        else:
            e_pass.config(show="")

    l_user = Label(root, text="Username:")
    l_pass = Label(root, text="Password:")
    l_user.grid(row=0, column=0)
    l_pass.grid(row=1, column=0)

    username = StringVar()
    password = StringVar()

    e_user = Entry(root, width=20, textvariable=username)
    e_pass = Entry(root, width=20, textvariable=password)
    e_user.grid(row=0, column=1, pady=5)
    e_pass.grid(row=1, column=1)

    b_login = Button(root, text="Login", width=10, command=login)
    b_login.grid(row=2, column=0, columnspan=2, pady=5)

    selection = IntVar()
    c_password = Checkbutton(root, variable=selection, command=show_password)
    c_password.grid(row=1, column=2)

    root.bind("<Return>", login)

    root.mainloop()
    return email_address