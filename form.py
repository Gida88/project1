from tkinter import *
from datetime import date
from tkinter import messagebox
from tkinter import ttk
from fpdf import FPDF, HTMLMixin
from tkinter import filedialog
from tkinter import scrolledtext
import os
from PIL import ImageTk, Image
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import time
import mysql.connector
from login import login_screen


directory_name = os.path.dirname("project1")
current_dir = os.path.join(directory_name, "Images", "AeroMexico.ico")
current_dir2 = os.path.join(directory_name, "Images", "aeromexico-vector-logo.png")
current_dir3 = os.path.join(directory_name, "Images", "AeroMexico Trans.png")
current_dir4 = os.path.join(directory_name, "Images", "button_send.png")
current_dir5 = os.path.join(directory_name, "Images", "button_save.png")
current_dir6 = os.path.join(directory_name, "Images", "button_exit.png")
current_dir7 = os.path.join(directory_name, "Images", "hover_send.png")
current_dir8 = os.path.join(directory_name, "Images", "hover_save.png")
current_dir9 = os.path.join(directory_name, "Images", "hover_exit.png")
current_dir10 = os.path.join(directory_name, "Images", "icon_send.png")
current_dir11 = os.path.join(directory_name, "Images", "icon_save.png")

email = login_screen()
print(email)

root = Tk()
app_width = 1110
app_height = 820
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)
root.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.rowconfigure(2, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.columnconfigure(3, weight=1)
root.title("AeroMexico Report")
root.configure(background="#112f54")

root.iconbitmap(current_dir)
# root.iconbitmap("C:/Users/gerge/Desktop/Python/CODEMY/TKINTER/aeromexico-logo.png")

# DEFINING FUNCTIONS

#Dropdown for Report Type

def showReportType():
    repType = Label(root, text=reportType.get())

reportTypeOptions = [
    "Preliminary",
    "Final"
]

reportType = StringVar()
reportType.set(reportTypeOptions[0])

# Prefilled values



# Put trace callbacks on the Entry DoubleVars

def addTOB(name, index, mode):

    resultPAXOB.set(zoneAA.get() + zoneAC.get() + zoneAI.get() + zoneBA.get() + zoneBC.get() + zoneBI.get() +
                    zoneCA.get() + zoneCC.get() + zoneCI.get())

def totalBulkBags(name, index, mode):
    list_of_bulk = [stroller.get(), wchr.get(), localBag.get(), transferBag.get(), priorityBag.get()]
    total = 0
    for index in list_of_bulk:
        if index:
            total += int(index)
        else:
            total += 0
    resultBulkBag.set(total)

    #resultBulkBag.set(stroller.get() + wchr.get() + localBag.get() + transferBag.get() + priorityBag.get())
""" a = []
    a.append(stroller.get())
    a.append(wchr.get())
    a.append(localBag.get())
    a.append(transferBag.get())
    a.append(priorityBag.get())
    total = 0
    for i in a:
        if i := "":
            total += i
    resultBulkBag.set(total)"""

# Data Validation Functions

def only_numbers(input):

    if input.isdigit():
        return True
    elif input == "":
        return True
    else:
        return False

# Button Functions

def addLine():
    container_list.append(Entry(bags_frame, width=15))
    position_list.append(Entry(bags_frame, width=15))
    number_of_xq_list.append(Entry(bags_frame, width=15))
    type_xq_list.append(Entry(bags_frame, width=15))
    index = len(container_list)-1
    row_index = len(container_list)+3
    container_list[index].grid(row=row_index, column=0)
    position_list[index].grid(row=row_index, column=1)
    number_of_xq_list[index].grid(row=row_index, column=2)
    number_of_xq_list[index].config(validate="key", validatecommand=(reg, "%P"))
    type_xq_list[index].grid(row=row_index, column=3)
    add_button.grid(row=row_index, column=4)
    remove_button.grid(row=row_index, column=5)
    if remove_button['state'] == DISABLED:
        remove_button['state'] = NORMAL
    if len(container_list) == 6:
        add_button['state'] = DISABLED

def removeLine():
    index = len(container_list)-1
    row_index = len(container_list)+3
    container_list[index].grid_forget()
    position_list[index].grid_forget()
    number_of_xq_list[index].grid_forget()
    type_xq_list[index].grid_forget()
    container_list.pop(index)
    position_list.pop(index)
    number_of_xq_list.pop(index)
    type_xq_list.pop(index)
    add_button.grid(row=row_index-1, column=4)
    remove_button.grid(row=row_index-1, column=5)
    if index == 1:
        remove_button['state'] = DISABLED
    elif index > 0:
        add_button['state'] = NORMAL
"""
def save():
    for a in number_of_xq_list:  # We have to add an if clause that gives a pop up message when the types of data entered in the entry fields are not correct
        try:
            int(a.get())
        except ValueError:
            messagebox.showwarning("Invalid Data", "Number of Bags can only contain numbers")
    total_number_of_xq = 0  # This is one of the variables where we will store the totals we need from the entry fields, so we can use them on the PDF file
    for entries in number_of_xq_list:
        total_number_of_xq += int(entries.get())"""

# Sum Total Functions

def sum_AKE(number_of_xq):
    total_AKE = number_of_xq.get()
    result_AKE.set(total_AKE)

# Button Functions
def send_button_hover(e):
    sendButton.config(image=send_button_alt)

def send_button_leave(e):
    sendButton.config(image=send_button)

def save_button_hover(e):
    saveButton.config(image=save_button_alt)

def save_button_leave(e):
    saveButton.config(image=save_button)

def exit_button_hover(e):
    exitButton.config(image=exit_button_alt)

def exit_button_leave(e):
    exitButton.config(image=exit_button)

def send_options():
    global recipient_list, checkbutton_list, email_window
    email_window = Toplevel()
    email_window.title("Send Report")
    email_window.geometry(f"+{(int(x)+200)}+{(int(y)+200)}")
    email_window.resizable(False, False)
    email_window.rowconfigure(0, weight=1)
    email_window.columnconfigure(0, weight=1)
    frame1 = Frame(email_window, padx=5, pady=5)
    frame1.rowconfigure(0, weight=1)
    frame1.columnconfigure(0, weight=1)
    frame2 = LabelFrame(email_window, padx=5, pady=5)
    frame2.rowconfigure(0, weight=1)
    frame2.columnconfigure(0, weight=1)
    frame3 = LabelFrame(email_window, padx=5, pady=5)
    frame3.rowconfigure(0, weight=1)
    frame3.columnconfigure(0, weight=1)
    frame4 = LabelFrame(email_window, padx=5, pady=5)
    frame4.rowconfigure(0, weight=1)
    frame4.columnconfigure(0, weight=1)
    frame5 = LabelFrame(email_window, padx=5, pady=5)
    frame5.rowconfigure(0, weight=1)
    frame5.columnconfigure(0, weight=1)
    frame5.rowconfigure(1, weight=1)
    line = ttk.Separator(email_window, orient="vertical")
    frame1.grid(row=0, column=0, padx=5, pady=5, sticky=EW)
    frame2.grid(row=1, column=0, padx=5, pady=5, sticky=EW)
    frame3.grid(row=2, column=0, padx=5, sticky=EW)
    frame4.grid(row=3, column=0, padx=5, pady=5, sticky=EW)
    line.grid(row=1, column=1, rowspan=3, padx=10, pady=5, sticky=NS)
    frame5.grid(row=1, column=2, padx=5, pady=5, sticky=NSEW, rowspan=3)
    myLabel = Label(frame1, text="Select the email address(es) you want your report sent to:")
    myLabel.grid(row=0, column=0)
    #station_list = ["Amsterdam Station", "Mexico City Station", "Cancun Station", "Guadalajara Station"]
    station_list = ["Dam & Greg", "Damianos", "Rosemary", "Dimitra"]
    email_list = ["damandgreg@outlook.com", "damianos.psychos@gmail.com", "rosemary.kaziani@gmail.com", "dimitraKaziani@hotmail.com"]
    recipient_list = []
    checkbutton_list = []
    variables_list = []
    all_emails = IntVar()
    all = Checkbutton(frame2, text="Select All Stations", variable=all_emails, command=lambda v=all_emails, b=checkbutton_list, l=variables_list: select_all(v, b, l))
    all.deselect()
    all.grid(row=0, column=0, sticky=W)
    for i, station in enumerate(station_list):
        selection = StringVar()
        variables_list.append(selection)
        check = Checkbutton(frame3, text=f"{station}", variable=selection, onvalue=f"{email_list[i]}", offvalue="")
        check.config(command=lambda b=check, v=selection: compose_email_list(b, v))
        checkbutton_list.append(check)
        check.deselect()
        check.grid(row=i, column=0, sticky=W)
        print(check["onvalue"])
    '''email1 = StringVar()
    ams = Checkbutton(frame3, text="Amsterdam Station", variable=email1, onvalue="insert email", offvalue="")
    ams.deselect()
    ams.grid(row=0, column=0, sticky=W)
    email2 = StringVar()
    mex = Checkbutton(frame3, text="Mexico City Station", variable=email2, onvalue="insert email", offvalue="")
    mex.deselect()
    mex.grid(row=1, column=0, sticky=W)
    email3 = StringVar()
    can = Checkbutton(frame3, text="Cancun Station", variable=email3, onvalue="insert email", offvalue="")
    can.deselect()
    can.grid(row=2, column=0, sticky=W)
    email4 = StringVar()
    gua = Checkbutton(frame3, text="Guadalajara Station", variable=email4, onvalue="insert email", offvalue="")
    gua.deselect()
    gua.grid(row=3, column=0, sticky=W)'''
    email5 = StringVar()
    email_entry = Entry(frame4, width=25, state=DISABLED)
    email_entry.grid(row=0, column=1, sticky=W)
    other = Checkbutton(frame4, text="Other", variable=email5, command=lambda v=email5, e=email_entry: other_email(v, e))
    other.deselect()
    other.grid(row=0, column=0, pady=3, sticky=W)
    send_button = Button(frame5, text="Send", width=15, padx=5, pady=5, command=lambda r=recipient_list: send(r))
    send_button.grid(row=0, column=0, padx=5, pady=5, sticky=S)
    cancel = Button(frame5, text="Cancel", width=15, padx=5, pady=5, command=email_window.destroy)
    cancel.grid(row=1, column=0, padx=5, pady=5, sticky=N)


def other_email(var, widget):
    if var.get() == "1":
        widget.config(state=NORMAL)
    else:
        widget.config(state=DISABLED)


def select_all(var, boxes, vlist):
    if var.get() == 1:
        for n, box in enumerate(checkbutton_list):
            box.select()
            compose_email_list(box, vlist[n])
    else:
        for box in boxes:
            box.deselect()
            recipient_list.remove(box["onvalue"])


def compose_email_list(box, var):
    if var.get():
        recipient_list.append(var.get())
    else:
        recipient_list.remove(box["onvalue"])


def send(recipients):
    from_email = "Damianos Greg <damandgreg@outlook.com>" # Will later change to user's email address taken from login
    to_emails = recipients # Will be chosen from pop-up menu
    #to_emails = ["damandgreg@outlook.com",] # Will be chosen from pop-up menu
    text = f"{reportType.get()} Report\n\n{flightNumber.get()} {route.get()}\n{registration.get()}\n{today_string}"
    subject = f"{reportType.get()} Report"
    username = "damandgreg@outlook.com"
    password = "Psychos&Vida"

    # Create the PDF in file directory so that it can be attached to the email
    pdf_dir = os.path.join(directory_name, f"{(reportType.get())} Report - {flightNumber.get()} - {today_string}.pdf")
    crew_info = crew.get()
    aircraftType_info = aircraftType.get()
    registration_info = registration.get()
    flight_number_info = flightNumber.get()
    route_info = route.get()
    j_class_info = jClass.get()
    y_class_info = yClass.get()

    zoneAA_info = zoneAA.get()
    zoneAC_info = zoneAC.get()
    zoneAI_info = zoneAI.get()
    zoneBA_info = zoneBA.get()
    zoneBC_info = zoneBC.get()
    zoneBI_info = zoneBI.get()
    zoneCA_info = zoneCA.get()
    zoneCC_info = zoneCC.get()
    zoneCI_info = zoneCI.get()
    #total_info = total.get()  # hre comes the total ob formula

    lir_edno_info = lirEdno.get()
    # Calculating the total number of bags in the Bags Entries
    total_xq_in_ake_info = 0
    for x in number_of_xq_list:
        total_xq_in_ake_info += int(x.get())
    stroller_info = stroller.get()
    wchr_info = wchr.get()
    local_bag_info = localBag.get()
    transfer_bag_info = transferBag.get()
    priority_bag_info = priorityBag.get()
    total_bag_weight_info = totalBagWeight.get()
    captain_info = captain.get()
    h2o_info = h2o.get()
    flightplan_info = flightPlan.get()
    runway_info = runway.get()
    runway_condition_info = runwayCondition.get()
    fuel_info = fuel.get()
    damaged_bags_info = damagedBags.get()
    remarks_info = remarks.get()

    # PDF alignment
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15)
    pdf.image(current_dir2, x=9, y=9, w=50)
    pdf.image(current_dir3, x=10, y=53, w=190)
    pdf.cell(0, 6, txt="", ln=1, align="L")
    pdf.ln()
    pdf.ln()
    pdf.cell(0, 6, txt=(reportType.get())+" Report", ln=1, align="L")
    pdf.ln()
    pdf.cell(35, 6, txt="Date: ", ln=0, align="L")
    pdf.cell(20, 6, txt=today_string, ln=1, align="L")
    pdf.cell(35, 6, txt="Crew: ", ln=0, align="L")
    pdf.cell(20, 6, txt=crew_info, ln=1, align="L")
    pdf.cell(35, 6, txt="A/C Type: ", ln=0, align="L")
    pdf.cell(20, 6, txt=aircraftType_info, ln=1, align="L")
    pdf.cell(35, 6, txt="Registration: ", ln=0, align="L")
    pdf.cell(20, 6, txt=registration_info, ln=1, align="L")
    pdf.cell(35, 6, txt="Flight: ", ln=0, align="L")
    pdf.cell(20, 6, txt=flight_number_info, ln=1, align="L")
    pdf.cell(35, 6, txt="Route: ", ln=0, align="L")
    pdf.cell(20, 6, txt=route_info, ln=1, align="L")
    pdf.ln()
    pdf.cell(7, 5, txt="J: ", ln=0, align="L")
    pdf.cell(20, 5, txt=str(j_class_info), ln=0, align="L")
    pdf.cell(7, 5, txt="Y: ", ln=0, align="L")
    pdf.cell(20, 5, txt=str(y_class_info), ln=1, align="L")
    pdf.ln()
    pdf.cell(20, 8, txt="AREA", ln=0, align="C")
    pdf.cell(30, 8, txt="ADULTS", ln=0, align="C")
    pdf.cell(30, 8, txt="CHILDREN", ln=0, align="C")
    pdf.cell(30, 8, txt="INFANTS", ln=1, align="C")
    pdf.line(11, 99, 117, 99)
    pdf.cell(20, 6, txt="Zone A:", ln=0, align="L")
    pdf.cell(30, 6, txt=str(zoneAA_info), ln=0, align="C")
    pdf.cell(30, 6, txt=str(zoneAC_info), ln=0, align="C")
    pdf.cell(30, 6, txt=str(zoneAI_info), ln=1, align="C")
    pdf.cell(20, 6, txt="Zone B:", ln=0, align="L")
    pdf.cell(30, 6, txt=str(zoneBA_info), ln=0, align="C")
    pdf.cell(30, 6, txt=str(zoneBC_info), ln=0, align="C")
    pdf.cell(30, 6, txt=str(zoneBI_info), ln=1, align="C")
    pdf.cell(20, 6, txt="Zone C:", ln=0, align="L")
    pdf.cell(30, 6, txt=str(zoneCA_info), ln=0, align="C")
    pdf.cell(30, 6, txt=str(zoneCC_info), ln=0, align="C")
    pdf.cell(30, 6, txt=str(zoneCI_info), ln=1, align="C")
    pdf.ln()
    pdf.cell(15, 6, txt="LIR: ", ln=0, align="L")
    pdf.cell(20, 6, txt=lir_edno_info, ln=1, align="L")
    pdf.cell(50, 6, txt="Total Bags in AKEs: ", ln=0, align="L")
    pdf.cell(35, 6, txt=str(total_xq_in_ake_info), ln=1, align="L")
    pdf.ln()
    pdf.cell(40, 8, txt="CONTAINER", ln=0, align="C")
    pdf.cell(40, 8, txt="POSITION", ln=0, align="C")
    pdf.cell(40, 8, txt="NO OF BAGS", ln=0, align="C")
    pdf.cell(40, 8, txt="TYPE", ln=1, align="C")
    pdf.line(14, 149, 158, 149)
    for i in range(0, len(container_list)):
        pdf.cell(40, 6, txt=(container_list[i].get()), ln=0, align="C")
        pdf.cell(40, 6, txt=(position_list[i].get()), ln=0, align="C")
        pdf.cell(40, 6, txt=(number_of_xq_list[i].get()), ln=0, align="C")
        pdf.cell(40, 6, txt=(type_xq_list[i].get()), ln=1, align="C")
    pdf.ln()
    pdf.cell(40, 6, txt="Stroller: ", ln=0, align="L")
    pdf.cell(20, 6, txt=str(stroller_info), ln=1, align="L")
    pdf.cell(40, 6, txt="WCHR: ", ln=0, align="L")
    pdf.cell(20, 6, txt=str(wchr_info), ln=1, align="L")
    pdf.cell(40, 6, txt="Local Bags: ", ln=0, align="L")
    pdf.cell(20, 6, txt=str(local_bag_info), ln=1, align="L")
    pdf.cell(40, 6, txt="Transfer Bags: ", ln=0, align="L")
    pdf.cell(20, 6, txt=str(transfer_bag_info), ln=1, align="L")
    pdf.cell(40, 6, txt="Priority Bags: ", ln=0, align="L")
    pdf.cell(20, 6, txt=str(priority_bag_info), ln=1, align="L")
    pdf.ln()
    pdf.cell(48, 6, txt="Total Bag Weight: ", ln=0, align="L")
    pdf.cell(20, 6, txt=total_bag_weight_info, ln=1, align="L")
    pdf.cell(48, 6, txt="Captain: ", ln=0, align="L")
    pdf.cell(20, 6, txt=captain_info, ln=1, align="L")
    pdf.cell(48, 6, txt="Water Level: ", ln=0, align="L")
    pdf.cell(20, 6, txt=h2o_info, ln=1, align="L")
    pdf.cell(48, 6, txt="Flight Plan: ", ln=0, align="L")
    pdf.cell(20, 6, txt=flightplan_info, ln=1, align="L")
    pdf.cell(48, 6, txt="Runway: ", ln=0, align="L")
    pdf.cell(20, 6, txt=f"{runway_info} {runway_condition_info}", ln=1, align="L")
    pdf.cell(48, 6, txt="Fuel: ", ln=0, align="L")
    pdf.cell(20, 6, txt=fuel_info, ln=1, align="L")
    pdf.cell(48, 6, txt="Damaged Bags: ", ln=0, align="L")
    pdf.cell(20, 6, txt=damaged_bags_info, ln=1, align="L")
    pdf.cell(48, 6, txt="Remarks: ", ln=0, align="L")
    pdf.cell(20, 6, txt=remarks_info, ln=1, align="L")
    pdf.output(pdf_dir, "F")

    print(to_emails)
    # Email Part
    msg = MIMEMultipart("alternative")
    msg["From"] = from_email
    msg["To"] = ", ".join(to_emails)
    msg["Subject"] = subject

    txt_part = MIMEText(text, "plain")
    msg.attach(txt_part)
    html_part = MIMEText("<h1>This is working</h1>", "html")
    # msg.attach(html_part)

    filename = pdf_dir
    attachment = open(filename, 'rb')  # Open the file as binary mode

    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
    encoders.encode_base64(part)  # encode the attachment
    # add payload header with filename
    part.add_header("Content-Disposition", f"attachment; filename= {filename}")

    msg.attach(part)
    msg_str = msg.as_string()
    # login to my smtp server
    server = smtplib.SMTP(host="smtp.office365.com", port=587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_emails, msg_str)
    server.quit()

    # Delete the PDF in file directory after it is sent
    os.remove(pdf_dir)

    # Close the dialog box
    email_window.destroy()

    # Give a pop-up message that the email was sent
    messagebox.showinfo("Report Sent!", "Your report has been sent successfully")

def save():
    directory = filedialog.asksaveasfilename(parent=root, initialfile=f"{(reportType.get())} Report - "
                                                                      f"{flightNumber.get()} - {today_string}.pdf")  # Prompts user to choose a directory where the file will be saved and returns the path selected along with the filename
    crew_info = crew.get()
    aircraftType_info = aircraftType.get()
    registration_info = registration.get()
    flight_number_info = flightNumber.get()
    route_info = route.get()
    j_class_info = jClass.get()
    y_class_info = yClass.get()

    zoneAA_info = zoneAA.get()
    zoneAC_info = zoneAC.get()
    zoneAI_info = zoneAI.get()
    zoneBA_info = zoneBA.get()
    zoneBC_info = zoneBC.get()
    zoneBI_info = zoneBI.get()
    zoneCA_info = zoneCA.get()
    zoneCC_info = zoneCC.get()
    zoneCI_info = zoneCI.get()
    #total_info = total.get()  # hre comes the total ob formula

    lir_edno_info = lirEdno.get()
    # Calculating the total number of bags in the Bags Entries
    total_xq_in_ake_info = 0
    for x in number_of_xq_list:
        total_xq_in_ake_info += int(x.get())

    container_info = registration.get()
    position_info = registration.get()
    nunmber_of_xq_info = registration.get()
    type_xq_info = registration.get()

    stroller_info = stroller.get()
    wchr_info = wchr.get()
    local_bag_info = localBag.get()
    transfer_bag_info = transferBag.get()
    priority_bag_info = priorityBag.get()
    #total_bulk_bag_info = totalBulkBag.get()
    total_bags_ob_info = totalBagsOb.get()
    total_bag_weight_info = totalBagWeight.get()
    captain_info = captain.get()
    h2o_info = h2o.get()
    flightplan_info = flightPlan.get()
    runway_info = runway.get()
    runway_condition_info = runwayCondition.get()
    fuel_info = fuel.get()
    damaged_bags_info = damagedBags.get()
    remarks_info = remarks.get()


    #align in table form
    #try:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15)
    pdf.image(current_dir2, x=9, y=9, w=50)
    pdf.image(current_dir3, x=10, y=53, w=190)
    pdf.cell(0, 6, txt="", ln=1, align="L")
    pdf.ln()
    pdf.ln()
    pdf.cell(0, 6, txt=(reportType.get())+" Report", ln=1, align="L")
    pdf.ln()
    pdf.cell(35, 6, txt="Date: ", ln=0, align="L")
    pdf.cell(20, 6, txt=today_string, ln=1, align="L")
    pdf.cell(35, 6, txt="Crew: ", ln=0, align="L")
    pdf.cell(20, 6, txt=crew_info, ln=1, align="L")
    pdf.cell(35, 6, txt="A/C Type: ", ln=0, align="L")
    pdf.cell(20, 6, txt=aircraftType_info, ln=1, align="L")
    pdf.cell(35, 6, txt="Registration: ", ln=0, align="L")
    pdf.cell(20, 6, txt=registration_info, ln=1, align="L")
    pdf.cell(35, 6, txt="Flight: ", ln=0, align="L")
    pdf.cell(20, 6, txt=flight_number_info, ln=1, align="L")
    pdf.cell(35, 6, txt="Route: ", ln=0, align="L")
    pdf.cell(20, 6, txt=route_info, ln=1, align="L")
    pdf.ln()
    pdf.cell(7, 5, txt="J: ", ln=0, align="L")
    pdf.cell(20, 5, txt=str(j_class_info), ln=0, align="L")
    pdf.cell(7, 5, txt="Y: ", ln=0, align="L")
    pdf.cell(20, 5, txt=str(y_class_info), ln=1, align="L")
    pdf.ln()
    pdf.cell(20, 8, txt="AREA", ln=0, align="C")
    pdf.cell(30, 8, txt="ADULTS", ln=0, align="C")
    pdf.cell(30, 8, txt="CHILDREN", ln=0, align="C")
    pdf.cell(30, 8, txt="INFANTS", ln=1, align="C")
    pdf.line(11, 99, 117, 99)
    pdf.cell(20, 6, txt="Zone A:", ln=0, align="L")
    pdf.cell(30, 6, txt=str(zoneAA_info), ln=0, align="C")
    pdf.cell(30, 6, txt=str(zoneAC_info), ln=0, align="C")
    pdf.cell(30, 6, txt=str(zoneAI_info), ln=1, align="C")
    pdf.cell(20, 6, txt="Zone B:", ln=0, align="L")
    pdf.cell(30, 6, txt=str(zoneBA_info), ln=0, align="C")
    pdf.cell(30, 6, txt=str(zoneBC_info), ln=0, align="C")
    pdf.cell(30, 6, txt=str(zoneBI_info), ln=1, align="C")
    pdf.cell(20, 6, txt="Zone C:", ln=0, align="L")
    pdf.cell(30, 6, txt=str(zoneCA_info), ln=0, align="C")
    pdf.cell(30, 6, txt=str(zoneCC_info), ln=0, align="C")
    pdf.cell(30, 6, txt=str(zoneCI_info), ln=1, align="C")
    pdf.ln()
    pdf.cell(15, 6, txt="LIR: ", ln=0, align="L")
    pdf.cell(20, 6, txt=lir_edno_info, ln=1, align="L")
    pdf.cell(50, 6, txt="Total Bags in AKEs: ", ln=0, align="L")
    pdf.cell(35, 6, txt=str(total_xq_in_ake_info), ln=1, align="L")
    pdf.ln()
    pdf.cell(40, 8, txt="CONTAINER", ln=0, align="C")
    pdf.cell(40, 8, txt="POSITION", ln=0, align="C")
    pdf.cell(40, 8, txt="NO OF BAGS", ln=0, align="C")
    pdf.cell(40, 8, txt="TYPE", ln=1, align="C")
    pdf.line(14, 149, 158, 149)
    for i in range(0, len(container_list)):
        pdf.cell(40, 6, txt=(container_list[i].get()), ln=0, align="C")
        pdf.cell(40, 6, txt=(position_list[i].get()), ln=0, align="C")
        pdf.cell(40, 6, txt=(number_of_xq_list[i].get()), ln=0, align="C")
        pdf.cell(40, 6, txt=(type_xq_list[i].get()), ln=1, align="C")
    pdf.ln()
    pdf.cell(40, 6, txt="Stroller: ", ln=0, align="L")
    pdf.cell(20, 6, txt=str(stroller_info), ln=1, align="L")
    pdf.cell(40, 6, txt="WCHR: ", ln=0, align="L")
    pdf.cell(20, 6, txt=str(wchr_info), ln=1, align="L")
    pdf.cell(40, 6, txt="Local Bags: ", ln=0, align="L")
    pdf.cell(20, 6, txt=str(local_bag_info), ln=1, align="L")
    pdf.cell(40, 6, txt="Transfer Bags: ", ln=0, align="L")
    pdf.cell(20, 6, txt=str(transfer_bag_info), ln=1, align="L")
    pdf.cell(40, 6, txt="Priority Bags: ", ln=0, align="L")
    pdf.cell(20, 6, txt=str(priority_bag_info), ln=1, align="L")
    #pdf.cell(0, 5, txt = " " +"TOTAL BULK    "+str(total_bulk_bag_info)+" ", ln=1, align="L")
    pdf.ln()
    #pdf.cell(0, 5, txt = " " +"TOTAL BAGS OB    "+total_bags_ob_info+" ", ln=1, align="L")
    pdf.cell(48, 6, txt="Total Bag Weight: ", ln=0, align="L")
    pdf.cell(20, 6, txt=total_bag_weight_info, ln=1, align="L")
    pdf.cell(48, 6, txt="Captain: ", ln=0, align="L")
    pdf.cell(20, 6, txt=captain_info, ln=1, align="L")
    pdf.cell(48, 6, txt="Water Level: ", ln=0, align="L")
    pdf.cell(20, 6, txt=h2o_info, ln=1, align="L")
    pdf.cell(48, 6, txt="Flight Plan: ", ln=0, align="L")
    pdf.cell(20, 6, txt=flightplan_info, ln=1, align="L")
    pdf.cell(48, 6, txt="Runway: ", ln=0, align="L")
    pdf.cell(20, 6, txt=f"{runway_info} {runway_condition_info}", ln=1, align="L")
    pdf.cell(48, 6, txt="Fuel: ", ln=0, align="L")
    pdf.cell(20, 6, txt=fuel_info, ln=1, align="L")
    pdf.cell(48, 6, txt="Damaged Bags: ", ln=0, align="L")
    pdf.cell(20, 6, txt=damaged_bags_info, ln=1, align="L")
    pdf.cell(48, 6, txt="Remarks: ", ln=0, align="L")
    pdf.cell(20, 6, txt=remarks_info, ln=1, align="L")
    pdf.output(directory, "F")
    #reportType_entry.delete(0, END)
    #date_entry.delete(0, END)
    #crew_entry.delete(0, END)
    #aircraftType_entry.delete(0, END)
    #registration_entry.delete(0, END)
    messagebox.showinfo("Document Saved!", "Your document has been saved successfully")
    #except:
    #    messagebox.showerror("ERROR", "Unexpected Error Occured!\nYour document was not saved")

##################################################################################

# VARIABLE CREATION

today = date.today()
#today_string = today.strftime("%Y/%m/%d")
today_string = today.strftime("%d-%m-%Y")

reg = root.register(only_numbers)

my_img = ImageTk.PhotoImage(Image.open(current_dir2))
crew = StringVar(value="3/8")
aircraftType = StringVar(value="787-9")
registration = StringVar(value="N183AM")
route = StringVar(value="AMS-MEX")
flightNumber = StringVar(value="27")
jClass = IntVar()
yClass = IntVar()
zoneAA = IntVar()
zoneAC = IntVar()
zoneAI = IntVar()
zoneBA = IntVar()
zoneBC = IntVar()
zoneBI = IntVar()
zoneCA = IntVar()
zoneCC = IntVar()
zoneCI = IntVar()
lirEdno = StringVar(value="2")
totalXqInAke = StringVar()  # here comes the totl bags in AKE formula
resultPAXOB = IntVar()  #auto counter for all passanger on board

container = StringVar(value="AKE1515AM")
position = StringVar(value="41L")
number_of_xq = StringVar(value="40")
type_xq = StringVar(value="PRIO")
container2 = StringVar()
position2 = StringVar()
number_of_xq2 = StringVar()
type_xq2 = StringVar()
container3 = StringVar()
position3 = StringVar()
number_of_xq3 = StringVar()
type_xq3 = StringVar()
container4 = StringVar()
position4 = StringVar()
number_of_xq4 = StringVar()
type_xq4 = StringVar()
container5 = StringVar()
position5 = StringVar()
number_of_xq5 = StringVar()
type_xq5 = StringVar()
container6 = StringVar()
position6 = StringVar()
number_of_xq6 = StringVar()
type_xq6 = StringVar()
#container7 = StringVar()
position7 = StringVar()
number_of_xq7 = StringVar()
type_xq7 = StringVar()
#container8 = StringVar()
position8 = StringVar()
number_of_xq8 = StringVar()
type_xq8 = StringVar()
result_AKE = IntVar()


stroller = IntVar()
wchr = IntVar()
localBag = IntVar()
transferBag = IntVar()
priorityBag = IntVar()
resultBulkBag = IntVar()  # here comes the total bulk bags
totalBagsOb = StringVar()  # here comes the total on board bags
totalBagWeight = StringVar(value="2000 KG")
captain = StringVar(value="RUIZ")
h2o = StringVar(value="66%")
flightPlan = StringVar(value="RC 1022")
runway = StringVar(value="36L")
runwayCondition = StringVar(value="DRY")
fuel = StringVar(value="77000")
damagedBags = StringVar(value="NONE")
remarks = StringVar(value="NONE")
total_xq_in_ake = StringVar()  # here comes the total bags in AKE formula

send_button = PhotoImage(file=f"{current_dir4}")
save_button = PhotoImage(file=f"{current_dir5}")
exit_button = PhotoImage(file=f"{current_dir6}")
send_button_alt = PhotoImage(file=f"{current_dir7}")
save_button_alt = PhotoImage(file=f"{current_dir8}")
exit_button_alt = PhotoImage(file=f"{current_dir9}")

send_icon = PhotoImage(file=f"{current_dir10}")
save_icon = PhotoImage(file=f"{current_dir11}")
# Lists
container_list = []
position_list =[]
number_of_xq_list = []
type_xq_list = []

##################################################################################

# WIDGET CREATION

# NOTEBOOK

my_notebook = ttk.Notebook(root, padding=0)

# ------------------------------------------------------------------------------ #

# MY DOCUMENT

# FRAMES

mydocument_mainframe = Frame(my_notebook)
test_frame = Frame(mydocument_mainframe, padx=5, pady=5)
title_frame = Frame(mydocument_mainframe, padx=5, pady=5)
document_info_frame = LabelFrame(mydocument_mainframe, text="Document Info", width=620, height=215, padx=20, pady=20)
#document_info_frame.grid_propagate(0)
passengers_frame = LabelFrame(mydocument_mainframe, text="Passengers", width=620, height=215, padx=20, pady=20)
#passengers_frame.grid_propagate(0)
bags_frame = LabelFrame(mydocument_mainframe, text="Bags", padx=20, pady=20)
bulk_frame = LabelFrame(mydocument_mainframe, text="Bulk", padx=20, pady=20)
buttons_frame = LabelFrame(mydocument_mainframe, text="Buttons", padx=20)

# TITLE FRAME

# Labels
title = Label(root, text="AEROMEXICO")
subTitle = Label(root, text="REPORT")
title_image = Label(title_frame, image=my_img, borderwidth=0)

# DOCUMENT INFO FRAME

# Labels
reportType_text = Label(document_info_frame, text="Report Type")  # dropdown menu
date_text = Label(document_info_frame, text="Date")
today_text = Label(document_info_frame, text=today_string)
reportTypeDrop = OptionMenu(document_info_frame, reportType, *reportTypeOptions)
flightNumber_text = Label(document_info_frame, text="Flight Number", )  # flight number with search engine //
route_text = Label(document_info_frame, text="Route", )  #
registration_text = Label(document_info_frame, text="Registration", )  #
aircraftType_text = Label(document_info_frame, text="A/C type", )  # flight number/route/reg connect together
crew_text = Label(document_info_frame, text="Crew", )  # two different box and format after

# Entries
flight_number_entry = Entry(document_info_frame, textvariable=flightNumber)
route_entry = Entry(document_info_frame, textvariable=route)
registration_entry = Entry(document_info_frame, textvariable=registration)
aircraftType_entry = Entry(document_info_frame, textvariable=aircraftType)
crew_entry = Entry(document_info_frame, textvariable=crew)

# PASSENGERS FRAME

# Labels
jClass_text = Label(passengers_frame, text="J", )
yClass_text = Label(passengers_frame, text="Y", )
area_text = Label(passengers_frame, text="AREA", )
zoneA_text = Label(passengers_frame, text="ZONE A", )
zoneB_text = Label(passengers_frame, text="ZONE B", )
zoneC_text = Label(passengers_frame, text="ZONE C", )
total_text = Label(passengers_frame, text="TOTAL", )
adult_text = Label(passengers_frame, text="ADULT", )
child_text = Label(passengers_frame, text="CHILD", )
infant_text = Label(passengers_frame, text="INFANT", )
totalOB = Label(passengers_frame, textvariable=resultPAXOB)

# Entries
jClass_entry = Entry(passengers_frame, textvariable=jClass, justify="center")
jClass_entry.config(validate="key", validatecommand=(reg, "%P"))
yClass_entry = Entry(passengers_frame, textvariable=yClass, justify="center")
yClass_entry.config(validate="key", validatecommand=(reg, "%P"))
zoneAA_entry = Entry(passengers_frame, textvariable=zoneAA, width=5, justify="center")
zoneAA_entry.config(validate="key", validatecommand=(reg, "%P"))
zoneAC_entry = Entry(passengers_frame, textvariable=zoneAC, width=5, justify="center")
zoneAC_entry.config(validate="key", validatecommand=(reg, "%P"))
zoneAI_entry = Entry(passengers_frame, textvariable=zoneAI, width=5, justify="center")
zoneAI_entry.config(validate="key", validatecommand=(reg, "%P"))
zoneBA_entry = Entry(passengers_frame, textvariable=zoneBA, width=5, justify="center")
zoneBA_entry.config(validate="key", validatecommand=(reg, "%P"))
zoneBC_entry = Entry(passengers_frame, textvariable=zoneBC, width=5, justify="center")
zoneBC_entry.config(validate="key", validatecommand=(reg, "%P"))
zoneBI_entry = Entry(passengers_frame, textvariable=zoneBI, width=5, justify="center")
zoneBI_entry.config(validate="key", validatecommand=(reg, "%P"))
zoneCA_entry = Entry(passengers_frame, textvariable=zoneCA, width=5, justify="center")
zoneCA_entry.config(validate="key", validatecommand=(reg, "%P"))
zoneCC_entry = Entry(passengers_frame, textvariable=zoneCC, width=5, justify="center")
zoneCC_entry.config(validate="key", validatecommand=(reg, "%P"))
zoneCI_entry = Entry(passengers_frame, textvariable=zoneCI, width=5, justify="center")
zoneCI_entry.config(validate="key", validatecommand=(reg, "%P"))

# BAGS FRAME

# Labels
lirEdno_text = Label(bags_frame, text="LIR EDNO", )
xqContainerMessage_text = Label(bags_frame, text="BAGGAGE CONTAINER MESSAGE", )
totalXqInAke_text = Label(bags_frame, text="TOTAL BAGS IN AKE", )
container_text = Label(bags_frame, text="CONTAINER")
position_text = Label(bags_frame, text="POSITION", )
nunmberOfXq_text = Label(bags_frame, text="NUMBER OF BAGS", )
typeXq_text = Label(bags_frame, text="TYPE", )
total_AKE = Label(bags_frame, textvariable=result_AKE)

# Entries
lirEdno_entry = Entry(bags_frame, textvariable=lirEdno, width=15)
container_list.append(Entry(bags_frame, textvariable=container, width=15))
position_list.append(Entry(bags_frame, textvariable=position, width=15))
number_of_xq_list.append(Entry(bags_frame, textvariable=number_of_xq, width=15))
number_of_xq_list[0].config(validate="key", validatecommand=(reg, "%P"))
type_xq_list.append(Entry(bags_frame, textvariable=type_xq, width=15))

# Buttons
add_button = Button(bags_frame, text="+", fg="green", command=addLine)
remove_button = Button(bags_frame, text="-", fg="red", command=removeLine, state=DISABLED)

# BULK FRAME

# Labels
stroller_text = Label(bulk_frame, text="Stroller", )
wchr_text = Label(bulk_frame, text="WCHR", )
localBag_text = Label(bulk_frame, text="Local Bag", )
transferBag_text = Label(bulk_frame, text="Transfer Bag", )
priorityBag_text = Label(bulk_frame, text="Priority Bag", )
totalBulkBag_text = Label(bulk_frame, text="Total Bags in Bulk", )
totalBagsOb_text = Label(bulk_frame, text="Total Bags on Board", )
totalBagWeight_text = Label(bulk_frame, text="Total Bag Weight", )
captain_text = Label(bulk_frame, text="Captain", )
h2o_text = Label(bulk_frame, text="Water Level", )
flightPlan_text = Label(bulk_frame, text="Flight Plan", )
runway_text = Label(bulk_frame, text="Take-Off Runway", )
runwayCondition_text = Label(bulk_frame, text="Runway Condition", )
fuel_text = Label(bulk_frame, text="Final Fuel", )
damagedBags_text = Label(bulk_frame, text="Damaged Bags", )
remarks_text = Label(bulk_frame, text="Remarks", )

# Entries
stroller_entry = Entry(bulk_frame, textvariable=stroller)
stroller_entry.config(validate="key", validatecommand=(reg, "%P"))
wchr_entry = Entry(bulk_frame, textvariable=wchr)
wchr_entry.config(validate="key", validatecommand=(reg, "%P"))
localBag_entry = Entry(bulk_frame, textvariable=localBag)
localBag_entry.config(validate="key", validatecommand=(reg, "%P"))
transferBag_entry = Entry(bulk_frame, textvariable=transferBag)
transferBag_entry.config(validate="key", validatecommand=(reg, "%P"))
priorityBag_entry = Entry(bulk_frame, textvariable=priorityBag)
priorityBag_entry.config(validate="key", validatecommand=(reg, "%P"))
totalBulkBag = Entry(bulk_frame, textvariable=resultBulkBag)
totalBagsonBoard = Entry(bulk_frame, textvariable=totalBagsOb)
totalBagWeight_entry = Entry(bulk_frame, textvariable=totalBagWeight)
captain_entry = Entry(bulk_frame, textvariable=captain)
h2o_entry = Entry(bulk_frame, textvariable=h2o)
flightPlan_entry = Entry(bulk_frame, textvariable=flightPlan)
runway_entry = Entry(bulk_frame, textvariable=runway)
runwayCondition_entry = Entry(bulk_frame, textvariable=runwayCondition)
fuel_entry = Entry(bulk_frame, textvariable=fuel)
damagedBags_entry = Entry(bulk_frame, textvariable=damagedBags)
remarks_entry = scrolledtext.ScrolledText(bulk_frame, relief=SUNKEN, width=24, height=11, borderwidth=1,
highlightthickness=0, pady=3)

#remarks_entry = Text(bulk_frame, relief=GROOVE, width=26, height=8, borderwidth=2, highlightthickness=0)
#remarks_entry = Entry(bulk_frame, textvariable=remarks, )

# BUTTON FRAME

# Buttons
sendButton = Button(buttons_frame, command=send, image=send_button, borderwidth=0)
saveButton = Button(buttons_frame, command=save, image=save_button, borderwidth=0)
exitButton = Button(buttons_frame, command=root.quit, image=exit_button, borderwidth=0)

saveIcon = Button(test_frame, command=save, image=save_icon, borderwidth=0)
sendIcon = Button(test_frame, command=send_options, image=send_icon, borderwidth=0)

# ------------------------------------------------------------------------------ #

# DATABASE

# FRAMES

database_mainframe = Frame(my_notebook)
treeview_frame = Frame(database_mainframe)
buttons_frame2 = LabelFrame(database_mainframe, relief=SUNKEN)

# Treeview

my_tree = ttk.Treeview(treeview_frame)
# Defining columns
my_tree["columns"] = ("Date", "Flight Number", "Passengers", "Baggage")
# Formatting columns
my_tree.column("#0", width=120, minwidth=25, anchor=CENTER)
my_tree.column("Date", width=120, minwidth=25, anchor=CENTER)
my_tree.column("Flight Number", width=150, minwidth=25, anchor=CENTER)
my_tree.column("Passengers", width=120, minwidth=25, anchor=CENTER)
my_tree.column("Baggage", width=120, minwidth=25, anchor=CENTER)
# Creating headings for columns
my_tree.heading("#0", text="Report Type", anchor=CENTER)
my_tree.heading("Date", text="Date", anchor=CENTER)
my_tree.heading("Flight Number", text="Flight Number", anchor=W)
my_tree.heading("Passengers", text="Passengers", anchor=CENTER)
my_tree.heading("Baggage", text="Baggage", anchor=W)
#Adding data
my_tree.insert(parent="", index="end", iid=0, text="Final", values=("13-10-2020", "AM1234", 42, 67))
my_tree.insert(parent="0", index="end", iid=1, text="Preliminary", values=("13-10-2020", "AM1234", 40, 60))

# Buttons

add_record_button = Button(buttons_frame2, text="Add", padx=10, pady=5, width=10)
remove_record_button = Button(buttons_frame2, text="Remove", padx=10, pady=5, width=10)
edit_record_button = Button(buttons_frame2, text="Edit", padx=10, pady=5, width=10)

##################################################################################


# PLACEMENT ON THE GRID

# NOTEBOOK

#my_notebook.grid(row=0, column=0)
my_notebook.pack()

# MY DOCUMENT

# Frames

mydocument_mainframe.grid(row=1, column=1)
title_frame.grid(row=0, column=0, columnspan=3)
test_frame.grid(row=0, column=0, sticky=W, padx=20)
document_info_frame.grid(row=1, column=0, padx=20)
passengers_frame.grid(row=2, column=0, padx=20)
bags_frame.grid(row=3, column=0, padx=20)
bulk_frame.grid(row=1, column=1, rowspan=3, padx=20, sticky=N)
buttons_frame.grid(row=4, column=0, columnspan=3)

# TITLE FRAME

# Labels
title_image.grid(row=0, column=0)
#title.grid(row=0, column=1)
#subTitle.grid(row=1, column=1)

# DOCUMENT INFO FRAME

# Labels
reportType_text.grid(row=0, column=0, sticky=W)
date_text.grid(row=1, column=0, sticky=W)
today_text.grid(row=1, column=1, sticky=W)
flightNumber_text.grid(row=0, column=2, sticky=W, padx=62)
route_text.grid(row=1, column=2, sticky=W, padx=62)
registration_text.grid(row=2, column=2, sticky=W, padx=62)
aircraftType_text.grid(row=3, column=2, sticky=W, padx=62)
crew_text.grid(row=4, column=2, sticky=W, padx=62)

# Entries
flight_number_entry.grid(row=0, column=3)
route_entry.grid(row=1, column=3)
registration_entry.grid(row=2, column=3)
aircraftType_entry.grid(row=3, column=3)
crew_entry.grid(row=4, column=3)

# Other
reportTypeDrop.grid(row=0, column=1, sticky="w")
reportTypeDrop.config(width=10)

# PASSENGER FRAME

# Labels
jClass_text.grid(row=8, column=0, sticky=W)
yClass_text.grid(row=8, column=2, sticky=W, padx=78.5)
area_text.grid(row=9, column=0, sticky=W)
zoneA_text.grid(row=10, column=0, sticky=W)
zoneB_text.grid(row=11, column=0, sticky=W)
zoneC_text.grid(row=12, column=0, sticky=W)
total_text.grid(row=13, column=0, sticky=W)
adult_text.grid(row=9, column=1)
child_text.grid(row=9, column=2)
infant_text.grid(row=9, column=3)

# Entries
jClass_entry.grid(row=8, column=1)
yClass_entry.grid(row=8, column=3)
zoneAA_entry.grid(row=10, column=1)
zoneAC_entry.grid(row=10, column=2)
zoneAI_entry.grid(row=10, column=3)
zoneBA_entry.grid(row=11, column=1)
zoneBC_entry.grid(row=11, column=2)
zoneBI_entry.grid(row=11, column=3)
zoneCA_entry.grid(row=12, column=1)
zoneCC_entry.grid(row=12, column=2)
zoneCI_entry.grid(row=12, column=3)
totalOB.grid(row=13, column=1)

# BAGS FRAME

# Labels
lirEdno_text.grid(row=0, column=0, )
xqContainerMessage_text.grid(row=2, column=0, columnspan=4, pady=20)
#totalXqInAke_text.grid(row=0, column=2)
#total_AKE.grid(row=0, column=3)
container_text.grid(row=3, column=0)
position_text.grid(row=3, column=1)
nunmberOfXq_text.grid(row=3, column=2)
typeXq_text.grid(row=3, column=3)

# Entries
lirEdno_entry.grid(row=0, column=1, )
container_list[0].grid(row=4, column=0)
position_list[0].grid(row=4, column=1)
number_of_xq_list[0].grid(row=4, column=2)
type_xq_list[0].grid(row=4, column=3)

# Buttons
add_button.grid(row=4, column=4)
remove_button.grid(row=4, column=5)

# BULK FRAME

# Labels
#bulk_text.grid(row=2, column=6, padx = 20, columnspan=2)
stroller_text.grid(row=3, column=6, sticky=W)
wchr_text.grid(row=4, column=6, sticky=W)
localBag_text.grid(row=5, column=6, sticky=W)
transferBag_text.grid(row=6, column=6, sticky=W)
priorityBag_text.grid(row=7, column=6, sticky=W)
totalBulkBag_text.grid(row=8, column=6, sticky=W)
totalBagsOb_text.grid(row=9, column=6, sticky=W)
totalBagWeight_text.grid(row=10, column=6, sticky=W)
captain_text.grid(row=12, column=6, sticky=W)
h2o_text.grid(row=13, column=6, sticky=W)
flightPlan_text.grid(row=14, column=6, sticky=W)
runway_text.grid(row=15, column=6, sticky=W)
runwayCondition_text.grid(row=16, column=6, sticky=W)
fuel_text.grid(row=17, column=6, sticky=W)
damagedBags_text.grid(row=18, column=6, sticky=W)
remarks_text.grid(row=19, column=6, sticky=NW)

# Entries
stroller_entry.grid(row=3, column=7)
wchr_entry.grid(row=4, column=7)
localBag_entry.grid(row=5, column=7)
transferBag_entry.grid(row=6, column=7)
priorityBag_entry.grid(row=7, column=7)
totalBulkBag.grid(row=8, column=7)
totalBagsonBoard.grid(row=9, column=7)
totalBagWeight_entry.grid(row=10, column=7)
captain_entry.grid(row=12, column=7)
h2o_entry.grid(row=13, column=7)
flightPlan_entry.grid(row=14, column=7)
runway_entry.grid(row=15, column=7)
runwayCondition_entry.grid(row=16, column=7)
fuel_entry.grid(row=17, column=7)
damagedBags_entry.grid(row=18, column=7)
remarks_entry.grid(row=19, column=7, sticky=E)

# BUTTON FRAME

# Buttons
sendButton.grid(row=28, column=1, padx=50)
saveButton.grid(row=28, column=3, padx=50)
exitButton.grid(row=28, column=7, padx=50)

saveIcon.grid(row=0, column=0, padx=10)
sendIcon.grid(row=0, column=1, padx=10)

# ------------------------------------------------------------------------------ #

# DATABASE

# FRAMES

database_mainframe.grid(row=0, column=0)
treeview_frame.grid(row=0, column=0)
buttons_frame2.grid(row=0, column=2, sticky=NSEW)

# Treeview

my_tree.grid(row=0, column=0, columnspan=3)

# Buttons

add_record_button.grid(row=0, column=0, padx=20, pady=10)
remove_record_button.grid(row=1, column=0, padx=20, pady=10)
edit_record_button.grid(row=2, column=0, padx=20, pady=10)

####################################################################

# Entry Field Tracing

#Passengers
zoneAA.trace("w", addTOB)
zoneAC.trace("w", addTOB)
zoneAI.trace("w", addTOB)
zoneBA.trace("w", addTOB)
zoneBC.trace("w", addTOB)
zoneBI.trace("w", addTOB)
zoneCA.trace("w", addTOB)
zoneCC.trace("w", addTOB)
zoneCI.trace("w", addTOB)

#Bags & Bulk
stroller.trace("w", totalBulkBags)
wchr.trace("w", totalBulkBags)
localBag.trace("w", totalBulkBags)
transferBag.trace("w", totalBulkBags)
priorityBag.trace("w", totalBulkBags)

##########################################################

# Adding Tabs to Notebook

my_notebook.add(mydocument_mainframe, text="My Report")
my_notebook.add(database_mainframe, text="Database")

##########################################################
# Animating Buttons when hovering mouse
sendButton.bind("<Enter>", send_button_hover)
sendButton.bind("<Leave>", send_button_leave)
saveButton.bind("<Enter>", save_button_hover)
saveButton.bind("<Leave>", save_button_leave)
exitButton.bind("<Enter>", exit_button_hover)
exitButton.bind("<Leave>", exit_button_leave)

##########################################################
root.mainloop()
