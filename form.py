from tkinter import *
from datetime import date
from tkinter import messagebox
from fpdf import FPDF, HTMLMixin
from tkinter import filedialog
from tkinter import scrolledtext
import os
from PIL import ImageTk, Image

directory_name = os.path.dirname("project1")
current_dir = os.path.join(directory_name, "Images", "AeroMexico.ico")
current_dir2 = os.path.join(directory_name, "Images", "aeromexico-vector-logo.png")
current_dir3 = os.path.join(directory_name, "Images", "button_send.png")
current_dir4 = os.path.join(directory_name, "Images", "button_save.png")
current_dir5 = os.path.join(directory_name, "Images", "button_exit.png")

root = Tk()
#root.geometry("1155x755")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.rowconfigure(2, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.columnconfigure(3, weight=1)
root.title("AeroMexico Report")
root.configure(background="#23395d")

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

def send():
    #fill it up later
    pass


def save():
    #def save_info():
    #reportType_info = reportTypeDrop.get()  #fix 'OptionMenu' object has no attribute 'get'
    #date_info = today.get()    # fix date for print
    directory = filedialog.asksaveasfilename(parent=root, initialfile=(flightNumber.get()) + " " + (reportType.get()) + " Report.pdf")  # Prompts user to choose a directory where the file will be saved and returns the path selected along with the filename

    crew_info = crew.get()
    aircraftType_info = aircraftType.get()
    registration_info = registration.get()
    flight_nunber_info = flightNumber.get()
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
    total_xq_in_ake_info = total_xq_in_ake.get()

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
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=15)
    pdf.cell(0, 5, txt = " " +(reportType.get())+" Report", ln=1, align="L")
    pdf.cell(0, 5, txt=" ", ln=1, align="L")
    pdf.cell(0, 5, txt = " " +"DATE                              " +today_string+" ", ln=1, align="L")
    pdf.cell(0, 5, txt = " " +"CREW                             "+crew_info+" ", ln=1, align="L")
    pdf.cell(0, 5, txt = " " +"A/C TYPE                       "+aircraftType_info+" ", ln=1, align="L")
    pdf.cell(0, 5, txt = " " +"REG                                "+registration_info+" ", ln=1, align="L")
    pdf.cell(0, 5, txt = " " +"FLIGHT                           "+flight_nunber_info+" ", ln=1, align="L")
    pdf.cell(0, 5, txt = " " +"ROUTE                           " +route_info+" ", ln=1, align="L")
    pdf.cell(0, 5, txt = " " , ln=1, align="L")
    pdf.cell(0, 5, txt = " " +"J      "+str(j_class_info)+"      Y      "+str(y_class_info)+" ", ln=1, align="L")
    pdf.cell(0, 5, txt=" ", ln=1, align="L")
    pdf.cell(0, 5, txt = " " +"AREA    "+"  "+"ADULT"+"  "+"CHILD"+"  "+"INFANT", ln=1, align="L")
    pdf.cell(0, 5, txt = " " +"ZONE A  "+"     "+str(zoneAA_info)+"            "+str(zoneAC_info)+"          "+str(zoneAI_info)+" ", ln=1, align="L")   # align in table form
    pdf.cell(0, 5, txt = " " +"ZONE B  "+"     "+str(zoneBA_info)+"            "+str(zoneBC_info)+"          "+str(zoneBI_info)+" ", ln=1, align="L")
    pdf.cell(0, 5, txt = " " +"ZONE C  "+"     "+str(zoneCA_info)+"            "+str(zoneCC_info)+"          "+str(zoneCI_info)+" ", ln=1, align="L")
    pdf.cell(0, 5, txt = " " , ln=1, align="L")
    pdf.cell(0, 5, txt = " " +"LIR "+lir_edno_info+" ", ln=1, align="L")
    pdf.cell(0, 5, txt = " " +"TOTAL BAGS IN AKEs "+total_xq_in_ake_info+" ", ln=1, align="L")
    pdf.cell(0, 5, txt = " " +registration_info+" ", ln=1, align="L")
    pdf.cell(0, 5, txt = " " +registration_info+" ", ln=1, align="L")
    pdf.cell(0, 5, txt = " " +registration_info+" ", ln=1, align="L")
    pdf.cell(0, 5, txt = " " , ln=1, align="L")
    pdf.cell(0, 5, txt = " " +"STROLLER                      "+str(stroller_info)+" ", ln=1, align="L")
    pdf.cell(0, 5, txt = " " +"WCHR                             "+str(wchr_info)+" ", ln=1, align="L")
    pdf.cell(0, 5, txt = " " +"LCL BAGS                       "+str(local_bag_info)+" ", ln=1, align="L")
    pdf.cell(0, 5, txt = " " +"TRANSFER BAGS          "+str(transfer_bag_info)+" ", ln=1, align="L")
    pdf.cell(0, 5, txt = " " +"PRIO BAGS                     "+str(priority_bag_info)+" ", ln=1, align="L")
    #pdf.cell(0, 5, txt = " " +"TOTAL BULK    "+str(total_bulk_bag_info)+" ", ln=1, align="L")
    pdf.cell(0, 5, txt = " " , ln=1, align="L")
    #pdf.cell(0, 5, txt = " " +"TOTAL BAGS OB    "+total_bags_ob_info+" ", ln=1, align="L")
    pdf.cell(0, 5, txt = " " +"TOTAL BAG WEIGHT     "+total_bag_weight_info+" ", ln=1, align="L")
    pdf.cell(0, 5, txt = " " +"CAPTAIN                         "+captain_info+" ", ln=1, align="L")
    pdf.cell(0, 5, txt = " " +"WATER LEVEL                "+h2o_info+" ", ln=1, align="L")
    pdf.cell(0, 5, txt = " " +"FLIGHT PLAN                  "+flightplan_info+" ", ln=1, align="L")
    pdf.cell(0, 5, txt = " " +"RNWY                              "+runway_info+" "+runway_condition_info+" ", ln=1, align="L")
    pdf.cell(0, 5, txt = " " +"FUEL                                "+fuel_info+" ", ln=1, align="L")
    pdf.cell(0, 5, txt = " " +"DAMAGED BAGS            "+damaged_bags_info+" ", ln=1, align="L")
    pdf.cell(0, 5, txt = " " +"REMARKS                      "+remarks_info+" ", ln=1, align="L")
    pdf.output(directory, "F")

    #reportType_entry.delete(0, END)
    #date_entry.delete(0, END)
    #crew_entry.delete(0, END)
    #aircraftType_entry.delete(0, END)
    #registration_entry.delete(0, END)
    messagebox.showinfo("Document Saved", "Your document has been saved successfully")


##################################################################################

# FRAMES

contents = Frame(root)
title_frame = Frame(contents, padx=5, pady=5)
document_info_frame = LabelFrame(contents, text="Document Info", width=620, height=215, padx=20, pady=20)
#document_info_frame.grid_propagate(0)
passengers_frame = LabelFrame(contents, text="Passengers", width=620, height=215, padx=20, pady=20)
#passengers_frame.grid_propagate(0)
bags_frame = LabelFrame(contents, text="Bags", padx=20, pady=20)
bulk_frame = LabelFrame(contents, text="Bulk", padx=20, pady=20)
buttons_frame = LabelFrame(contents, text="Buttons", padx=20, pady=20)
#buttons_frame = Frame(root, padx=20, pady=40, relief=SUNKEN)

# VARIABLE CREATION

today = date.today()
today_string = today.strftime("%Y/%m/%d")

reg = root.register(only_numbers)

my_img = ImageTk.PhotoImage(Image.open(current_dir2))
crew = StringVar(document_info_frame, value="3/8")
aircraftType = StringVar(document_info_frame, value="787-9")
registration = StringVar(document_info_frame, value="N183AM")
route = StringVar(document_info_frame, value="AMS-MEX")
flightNumber = StringVar(document_info_frame, value="26")
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
lirEdno = StringVar(document_info_frame, value="2")
totalXqInAke = StringVar()  # here comes the totl bags in AKE formula
resultPAXOB = IntVar()  #auto counter for all passanger on board

container = StringVar(document_info_frame, value="AKE1515AM")
position = StringVar(document_info_frame, value="41L")
number_of_xq = StringVar(document_info_frame, value="40")
type_xq = StringVar(document_info_frame, value="PRIO")
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
totalBagWeight = StringVar(document_info_frame, value="2000 KG")
captain = StringVar(document_info_frame, value="RUIZ")
h2o = StringVar(document_info_frame, value="66%")
flightPlan = StringVar(document_info_frame, value="RC 1022")
runway = StringVar(document_info_frame, value="36L")
runwayCondition = StringVar(document_info_frame, value="DRY")
fuel = StringVar(document_info_frame, value="77000")
damagedBags = StringVar(document_info_frame, value="NONE")
remarks = StringVar(document_info_frame, value="NONE")
totalBagsOb = StringVar()  # here comes the total on baord bags
total_xq_in_ake = StringVar()  # here comes the total bags in AKE formula

send_button = PhotoImage(file=f"{current_dir3}")
save_button = PhotoImage(file=f"{current_dir4}")
exit_button = PhotoImage(file=f"{current_dir5}")
# Lists
container_list = []
position_list =[]
number_of_xq_list = []
type_xq_list = []

##################################################################################

# WIDGET CREATION



# TITLE FRAME

# Labels
title = Label(root, text="AEROMEXICO")
subTitle = Label(root, text="REPORT")
title_image = Label(title_frame, image=my_img, borderwidth=0)

# DOCUMENT INFO FRAME

# Labels
reportType_text = Label(document_info_frame, text="Report Type")  # dropdown menu
date_text = Label(document_info_frame, text="Date")
today_text = Label(document_info_frame, text=today)
reportTypeDrop = OptionMenu(document_info_frame, reportType, *reportTypeOptions)
flightNumber_text = Label(document_info_frame, text="Flight Number", )  # flight number with search engine //
route_text = Label(document_info_frame, text="Route", )  #
registration_text = Label(document_info_frame, text="Registration", )  #
aircraftType_text = Label(document_info_frame, text="A/C type", )  # flight number/route/reg connect together
crew_text = Label(document_info_frame, text="Crew", )  # two different box and fomrat after

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
jClass_entry = Entry(passengers_frame, textvariable=jClass, width=5, justify="center")
jClass_entry.config(validate="key", validatecommand=(reg, "%P"))
yClass_entry = Entry(passengers_frame, textvariable=yClass, width=5, justify="center")
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
xqContainerMessage_text = Label(bags_frame, text="BAGGAGE CONTAINER MESSAGE", )  # + icon to add new line for AKE if needed
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
bulk_text = Label(bulk_frame, text="BULK", )
stroller_text = Label(bulk_frame, text="Stroller", )
wchr_text = Label(bulk_frame, text="WCHR", )
localBag_text = Label(bulk_frame, text="Local Bag", )
transferBag_text = Label(bulk_frame, text="Transfer Bag", )
priorityBag_text = Label(bulk_frame, text="Priority Bag", )
totalBulkBag_text = Label(bulk_frame, text="TOTAL BAGS IN BULK", )
totalBulkBag = Label(bulk_frame, textvariable=resultBulkBag)
totalBagsOb_text = Label(bulk_frame, text="TOTAL BAGS ON BOARD", )
totalBagWeight_text = Label(bulk_frame, text="Total Bag Weight", )
captain_text = Label(bulk_frame, text="CAP", )
h2o_text = Label(bulk_frame, text="H2O", )
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
sendButton = Button(buttons_frame, text="SEND", image=send_button, borderwidth=0)
saveButton = Button(buttons_frame, command=save, image=save_button, borderwidth=0, highlightthickness=0, padx=0, pady=0)
exitButton = Button(buttons_frame, text="EXIT", command=root.quit, image=exit_button, borderwidth=0)

##################################################################################


# PLACEMENT ON THE GRID

# Frames

contents.grid(row=1, column=1)
title_frame.grid(row=0, column=0, columnspan=3)
document_info_frame.grid(row=1, column=0, padx=10, sticky=W)
passengers_frame.grid(row=2, column=0, columnspan=2, padx=10, sticky=W)
bags_frame.grid(row=3, column=0, padx=10, sticky=W)
bulk_frame.grid(row=1, column=1, rowspan=3, sticky=NSEW, padx=20)
buttons_frame.grid(row=4, column=0, columnspan=3)

# TITLE FRAME

# Labels
title_image.grid(row=0, column=0, sticky=W)
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
stroller_text.grid(row=3, column=6, padx = 20, sticky=W)
wchr_text.grid(row=4, column=6, padx = 20, sticky=W)
localBag_text.grid(row=5, column=6, padx = 20, sticky=W)
transferBag_text.grid(row=6, column=6, padx = 20, sticky=W)
priorityBag_text.grid(row=7, column=6, padx = 20, sticky=W)
totalBulkBag_text.grid(row=8, column=6, padx = 20, sticky=W)
totalBagsOb_text.grid(row=9, column=6, padx = 20, sticky=W)
totalBagWeight_text.grid(row=10, column=6, padx = 20, sticky=W)
captain_text.grid(row=12, column=6, padx = 20, sticky=W)
h2o_text.grid(row=13, column=6, padx = 20, sticky=W)
flightPlan_text.grid(row=14, column=6, padx = 20, sticky=W)
runway_text.grid(row=15, column=6, padx = 20, sticky=W)
runwayCondition_text.grid(row=16, column=6, padx = 20, sticky=W)
fuel_text.grid(row=17, column=6, padx = 20, sticky=W)
damagedBags_text.grid(row=18, column=6, padx = 20, sticky=W)
remarks_text.grid(row=19, column=6, padx = 20, sticky=NW)

# Entries
stroller_entry.grid(row=3, column=7)
wchr_entry.grid(row=4, column=7)
localBag_entry.grid(row=5, column=7)
transferBag_entry.grid(row=6, column=7)
priorityBag_entry.grid(row=7, column=7)
totalBulkBag.grid(row=8, column=7)
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

####################################################################

# Entry Field Tracing

#Passangers
zoneAA.trace("w", addTOB)
zoneAC.trace("w", addTOB)
zoneAI.trace("w", addTOB)
zoneBA.trace("w", addTOB)
zoneBC.trace("w", addTOB)
zoneBI.trace("w", addTOB)
zoneCA.trace("w", addTOB)
zoneCC.trace("w", addTOB)
zoneCI.trace("w", addTOB)

#Bags n Bulk
stroller.trace("w", totalBulkBags)
wchr.trace("w", totalBulkBags)
localBag.trace("w", totalBulkBags)
transferBag.trace("w", totalBulkBags)
priorityBag.trace("w", totalBulkBags)



##########################################################
root.mainloop()
