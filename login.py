from tkinter import *
import mysql.connector
from tkinter import messagebox
import smtplib

global username, password, root, root2, root3, domain, e_username, e_password


def login_screen():
    global username, password, root
    root = Tk()
    root.title("User Login")
    app_width = 290
    app_height = 100
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)
    root.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

    l_user = Label(root, text="Username:")
    l_pass = Label(root, text="Password:")
    l_user.grid(row=0, column=0)
    l_pass.grid(row=1, column=0)

    username = StringVar(value="admin")
    password = StringVar(value="admin")

    e_user = Entry(root, width=20, textvariable=username)
    e_pass = Entry(root, width=20, textvariable=password, show="*")
    e_user.grid(row=0, column=1, pady=5)
    e_pass.grid(row=1, column=1)

    b_login = Button(root, text="Login", width=10, command=login)
    b_login.grid(row=2, column=0, columnspan=2, pady=5)

    selection = IntVar()
    c_password = Checkbutton(root, variable=selection)
    c_password.config(command=lambda c=selection, e=e_pass: show_password(c, e))
    c_password.deselect()
    c_password.grid(row=1, column=2)

    root.bind("<Return>", login)

    root.mainloop()
    return email_address


def login(event=None):
    global email_address, root2
    con = mysql.connector.connect(host="localhost", user="root", password="!$aintikEr_13!", database="testdatabase")
    cursor = con.cursor()
    #verify = "select * from users where username = %s and userpassword = %s"
    cursor.execute("SElECT * FROM users")
    results = cursor.fetchall()
    access = False
    linked_email = False
    for result in results:
        if result[0] == username.get() and result[1] == password.get():
            access = True
            if result[3]:
                linked_email = True
            email_address = result[3]
    if access:
        root.destroy()
        if linked_email:
            return email_address
        else:
            root2 = Tk()
            root2.title("Link Email Account")
            app_width = 400
            app_height = 220
            screen_width = root2.winfo_screenwidth()
            screen_height = root2.winfo_screenheight()
            x = (screen_width / 2) - (app_width / 2)
            y = (screen_height / 2) - (app_height / 2)
            root2.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
            root2.rowconfigure(0, weight=1)
            root2.columnconfigure(0, weight=1)
            root2.rowconfigure(1, weight=1)
            root2.columnconfigure(1, weight=1)

            b_gmail = Button(root2, text="Gmail", width=20, height=5, command=lambda d="smtp.gmail.com", n="Gmail": select_domain(d, n))
            b_gmail.grid(row=0, column=0, padx=5, pady=5)
            b_exchange = Button(root2, text="Exchange", width=20, height=5, command=lambda d="smtp.office365.com", n="Exchange": select_domain(d, n))
            b_exchange.grid(row=1, column=0, padx=5, pady=5)
            b_hotmail = Button(root2, text="Hotmail", width=20, height=5, command=lambda d="smtp.live.com", n="Hotmail": select_domain(d, n))
            b_hotmail.grid(row=0, column=1, padx=5, pady=5)
            b_yahoo = Button(root2, text="Yahoo", width=20, height=5, command=lambda d="smtp.yahoo.com", n="Yahoo": select_domain(d, n))
            b_yahoo.grid(row=1, column=1, padx=5, pady=5)
            root2.mainloop()
    else:
        messagebox.showinfo("Login Failed", "Username and/or Password Incorrect")


def show_password(checkbox, entry_box):
    if checkbox.get() == 0:
        entry_box.config(show="*")
    else:
        entry_box.config(show="")


def e_login(event=None):
    try:
        server = smtplib.SMTP(host=domain, port=587)
        server.ehlo()
        server.starttls()
        server.login(e_username.get(), e_password.get())
        server.quit()
        # Add info to database later
        con = mysql.connector.connect(host="localhost", user="root", password="!$aintikEr_13!",
                                      database="testdatabase")
        mycursor = con.cursor()
        sql = "UPDATE users SET emaildomain=%s, useremail=%s, emailpassword=%s " \
              "WHERE username=%s"
        val = (domain, e_username.get(), e_password.get(), username.get())
        mycursor.execute(sql, val)
        con.commit()
        messagebox.showinfo("Login Successful", "Login Successful!")
        root2.destroy()
        # have to correct this
        #root3.destroy()
    except:
        messagebox.showinfo("Login Failed", "Username and/or Password Incorrect")


def e_back(event=None):
    root3.destroy()
    root2.deiconify()


def select_domain(dom, domain_name):
    global domain, root3, e_username, e_password
    domain = dom
    root2.withdraw()
    root3 = Toplevel()
    root3.title(f"Link {domain_name} Account")
    app_width = 290
    app_height = 100
    screen_width = root3.winfo_screenwidth()
    screen_height = root3.winfo_screenheight()
    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)
    root3.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

    l_e_user = Label(root3, text="Email:")
    l_e_pass = Label(root3, text="Password:")
    l_e_user.grid(row=0, column=0)
    l_e_pass.grid(row=1, column=0)

    e_username = StringVar(value="damandgreg@outlook.com")
    e_password = StringVar(value="Psychos&Vida")

    e_e_user = Entry(root3, width=20, textvariable=e_username)
    e_e_pass = Entry(root3, width=20, textvariable=e_password, show="*")
    e_e_user.grid(row=0, column=1, pady=5)
    e_e_pass.grid(row=1, column=1)

    b_e_back = Button(root3, text="Back", command=e_back)
    b_e_login = Button(root3, text="Login", width=10, command=e_login)
    b_e_back.grid(row=2, column=0)
    b_e_login.grid(row=2, column=0, columnspan=2, pady=5)

    e_selection = IntVar()
    c_e_password = Checkbutton(root3, variable=e_selection)
    c_e_password.config(command=lambda c=e_selection, e=e_e_pass: show_password(c, e))
    c_e_password.deselect()
    c_e_password.grid(row=1, column=2)

    root3.bind("<Return>", e_login)
    root3.mainloop()