from tkinter import *
from tkcalendar import Calendar
from tkinter import ttk
from tkinter import messagebox
import time
#create window
window = Tk()
window.geometry("1200x600+400+400")
window.title("Register")
window.resizable(0, 0)
back = Frame(master=window,bg='white')
back.pack_propagate(0)
back.pack(expand=1)

#title
title = Label(text="Register", font=("Arial",30,"bold"))
title.place(x=525,y=0)
#name
name = Label(text="Name", font=("Arial",18,"underline")).place (x=80,y=80)
name_entry = Entry(window,width=55)
name_entry.place(x=82.5,y=125)
#DOB
DOB= Label(text="Date of birth", font=("Arial",18,"underline")).place(x=80,y=170)
localtime = time.localtime()
cal = Calendar(window, selectmode = 'day',
               year = localtime.tm_year, month = localtime.tm_mon,
               day = localtime.tm_mday)
cal.place(x=82.5,y=215)
#Gender
Gender = Label(text="Gender", font=("Arial", 18, "underline")).place(x=80, y=425)
Gender_combobox= ttk.Combobox(window, font=("Arial", 13),width=21)
Gender_combobox['values']=["Male","Female"]
Gender_combobox.place(x=200,y=430)
#email
email = Label(text="Email", font=("Arial",18,"underline")).place(x=700,y=80)
email_entry=Entry(window,width=55)
email_entry.place(x=702.5,y=125)
#phone
phone = Label(text="Phone", font=("Arial",18,"underline")).place(x=700,y=170)
phone_entry=Entry(window,width=55)
phone_entry.place(x=702.5,y=215)
#username
username = Label(text="Username", font=("Arial",18,"underline")).place(x=700,y=260)
username_entry=Entry(window,width=55)
username_entry.place(x=702.5, y=305)
#password
password = Label(text="Password", font=("Arial",18,"underline")).place(x=700,y=350)
password_entry=Entry(window,width=55,show="-")
password_entry.place(x=702.5, y=395)
#termsandconditions
T_C=IntVar()
T_C_box = Checkbutton(window, text = "I agree to Terms & Conditions", font=("Arial",10,"italic"), variable = T_C,
                 onvalue = 1, offvalue = 0, height=2,
                 width = 20)
T_C_box.place(x=702.5, y=420)
#process
def data_processing():
    global file, cache, clear_data, index
    file = open("username and password.txt")
    cache= file.readlines()
    clear_data=[]
    for i in cache:
        clear_data.append(i.split("\t"))
    for y in clear_data:
        for x in y:
            index = y.index(x)
            y.pop(index)
            y.insert(index, x.removesuffix("\n"))
    file.close()
def process():
    global email_info, phone_info, status
    status = True
    email_info=email_entry.get()
    phone_info=phone_entry.get()
    if email_info.find("@") == -1 or email_info.find(".") == -1 or len(email_info) == 0:
        Label(text="Invalid",font=("Arial",10,"italic"),fg="red").place(x=775,y=90)
        status=False
    if T_C.get() == 0:
        Label(text="Please tick this box",font=("Arial",10,"italic"),fg="red").place(x=900,y=430)
        status=False
    if len(phone_info) == 10:
        pass
    elif phone_info == "" or len(phone_info)<10 or len(phone_info)>10:
        Label(text="Invalid", font=("Arial", 10, "italic"), fg="red").place(x=788, y=180)
        status=False
    elif phone_info[0] == "0":
        pass
    else:
        Label(text="Invalid", font=("Arial", 10, "italic"), fg="red").place(x=775, y=250)
        status=False
    data_processing()
    if username_entry.get() == "":
        status = False
        Label(text="Invalid", font=("Arial", 10, "italic"), fg="red").place(x=830, y=270)
    if password_entry.get() == "":
        status = False
        Label(text="Invalid", font=("Arial", 10, "italic"), fg="red").place(x=830, y=360)
    for i in clear_data:
        if i[0] == username_entry.get():
            status = False
            Label(text="This username has been used", font=("Arial", 10, "italic"), fg="red").place(x=830, y=270)
            break
    if status == True:
        username_and_password = open("username and password.txt",mode="a+")
        username_and_password.writelines(["\n"+str(username_entry.get()),"\t"+str(password_entry.get())])
        info = open(str(username_entry.get())+".txt",mode="w+")
        info.writelines([str(name_entry.get())+"\n",str(cal.get_date())+"\n",str(Gender_combobox.get())+"\n",str(email_info)+"\n",str(phone_info)+"\n",])
        username_and_password.close()
        info.close()
        messagebox.showinfo("Notification","Your account has been registered")
        window.destroy()
#button
Complete = Button(window,text="Complete",font=("Arial",15),command=process)
Complete.place(x=550,y=500)

window.mainloop()