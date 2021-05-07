from tkinter import *
from tkcalendar import Calendar
import sqlite3
from tkinter import messagebox
from PIL import Image,ImageTk
from functools import partial
root=Tk()
root.title("employee management system")
root.iconbitmap("top.ico")
root.geometry("495x651")
bg=ImageTk.PhotoImage(Image.open("background.jpg"))
label_image=Label(root,image=bg).place(x=0,y=0)
#_____________________________________
frame_title=Frame(root,bg="blue")
frame_title.grid(row=1,column=1)

title_label=Label(frame_title,text="\tWELCOME TO THE \n\tEMPLOYEE MANAGEMENT SYSTEM\n\t FOR THE EMPLOYEE IN THE COMPANY \t",font="vandana,36",width=50,height=6)
title_label.grid(row=0,column=0)







# __________________________________________________________
def register():
    top=Toplevel()
    top.title("registration form")
    def add_to_database():
        # adding entry values to database
        connect = sqlite3.connect("registration form")
        c = connect.cursor()
        # insert to the table
        c.execute(
            "INSERT INTO registration VALUES( :First_name, :Last_name,:gender, :address, :citizenship_number, :nationality, :experience, :father_name,:phone_number,:username,:password)",
            {
                "First_name": first_name.get(),
                "Last_name": last_name.get(),
                "gender": gender.get(),
                "address": address.get(),
                "citizenship_number": citizenship_number.get(),
                "experience": experience.get(),
                "nationality": nationality.get(),
                "father_name": father_name.get(),
                "phone_number": phone_number.get(),
                "username": username_entry.get(),
                "password": password.get()

            })
        print("inserted")

        connect.commit()
        connect.close()

        first_name.delete(0, END)
        last_name.delete(0, END)
        address.delete(0, END)
        citizenship_number.delete(0, END)
        experience.delete(0, END)
        nationality.delete(0, END)
        father_name.delete(0, END)
        phone_number.delete(0, END)
        username_entry.delete(0, END)
        password.delete(0, END)


    def confirmation():
        response = messagebox.showinfo("confirmation", "do you want to continue")
        Label(top ).place(x=0,y=0)


# _________________________________________
# for only displaying
    def query():
        connect = sqlite3.connect("registration form")
        c = connect.cursor()
        c.execute("SELECT *,oid FROM registration")
        records = c.fetchall()

        print_record = ""
        for record in records:
            print_record += str(record) + " "
        query_label = Label(frame1, text=print_record)
        query_label.grid(row=8, column=0)
        connect.commit()
        connect.close()


# __________________________________________________

# frame for the registration
    frame1 = Frame(top, bg="white")
    frame1.grid(row=3, column=0)


# ________---_______
    def show():
        show_label = Label(frame1, text=var.get()).grid(row=7, column=2)


    var = StringVar()
    checkbutton = Checkbutton(frame1, text="do you agree and ready to proceed", variable=var, onvalue="ON", offvalue="off")

    checkbutton.deselect()
    checkbutton.grid(row=7, column=3)

    my_button = Button(frame1, text="Continue", command=confirmation).grid(row=7, column=4)
# _________________________________________________
# labels in the frame
    first_name_label = Label(frame1, text="First Name:")
    first_name_label.grid(row=0, column=0)

    last_name_label = Label(frame1, text="Last Name:")
    last_name_label.grid(row=0, column=3)

    sex_label = Label(frame1, text="Gender")
    sex_label.grid(row=1, column=0)

    date_of_birth_label = Label(frame1, text="Date Of Birth")
    date_of_birth_label.grid(row=2, column=0)

    age_label = Label(frame1, text="Age")
    age_label.grid(row=2, column=4)

    address_label = Label(frame1, text="Address:")
    address_label.grid(row=3, column=0)

    citizenship_number_label = Label(frame1, text="Citizenship number:")
    citizenship_number_label.grid(row=4, column=4)

    nationality_label = Label(frame1, text="Nationality:")
    nationality_label.grid(row=4, column=0)

    experience_label = Label(frame1, text="Experience:")
    experience_label.grid(row=5, column=0)

    father_name_label = Label(frame1, text="Father Name")
    father_name_label.grid(row=3, column=4)

    phone_number_label = Label(frame1, text="Phone Number")
    phone_number_label.grid(row=5, column=4)

    username_label= Label(frame1, text=" username")
    username_label.grid(row=6, column=0)

    password_label = Label(frame1, text="Password")
    password_label.grid(row=6, column=4)

# __________________________________________
# adding entry
    first_name = Entry(frame1, width=20)
    first_name.grid(row=0, column=1)

    last_name = Entry(frame1, width=20)
    last_name.grid(row=0, column=4)

    address = Entry(frame1, width=30)
    address.grid(row=3, column=1)

    citizenship_number = Entry(frame1, width=30)
    citizenship_number.grid(row=4, column=5)

    experience = Entry(frame1, width=30)
    experience.grid(row=5, column=1)

    nationality = Entry(frame1, width=30)
    nationality.grid(row=4, column=1)

    father_name = Entry(frame1, width=30)
    father_name.grid(row=3, column=5)

    phone_number = Entry(frame1, width=30)
    phone_number.grid(row=5, column=5)

    username_entry = Entry(frame1, width=30)
    username_entry.grid(row=6, column=1)

    password = Entry(frame1, width=30)
    password.grid(row=6, column=5)

# _____________________________________________
    submit_buttom = Button(frame1, text="Submit", command=add_to_database)
    submit_buttom.grid(row=8, column=3)

    show_database = Button(frame1, text="Show Your Details Filled", command=query)
    show_database.grid(row=10, column=2)

# adding radio modes for sex


    gender = StringVar()
    gender.set("Male")

    radiobutton_1 = Radiobutton(frame1, text='Male', variable=gender, value="male")
    radiobutton_1.grid(row=1, column=1)
    radiobutton_2 = Radiobutton(frame1, text='Female', variable=gender, value="female")
    radiobutton_2.grid(row=1, column=2)

    radiobutton_3 = Radiobutton(frame1, text='Other', variable=gender, value="other")
    radiobutton_3.grid(row=1, column=3)
    print(gender)


# __________________________________________________________
# adding calender

    def date():
        def print_sel():
            print(cal.selection_get())

        top = Toplevel(root)

        cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand2", year=2021, month=5, day=4)
        cal.pack(fill="both", expand=True)
        Button(top, text="ok", command=print_sel).pack()


    Button(frame1, text='select date here', command=date).grid(row=2, column=1, padx=10, pady=10)


    def submitFunction():
        print(gender.get())


    submit = Button(frame1, text='Submit', command=submitFunction)
    submit.grid(row=1, column=4)


# _________________________________________________-
# for age dropdown menu
    def age_dropdown():
        label_age = Label(frame1, text=clicked.get())


# making option in the list
    options = [
        "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"
    ]
    clicked = StringVar()
    clicked.set(18)

    drop = OptionMenu(frame1, clicked, *options)
    drop.grid(row=2, column=5)

    print(drop)


#_____________________________________________-
    #create an database  and connecting
    connect =sqlite3.connect("registration form")
    #creating an cursor
    c=connect.cursor()
    c.execute("""CREATE TABLE registration(
            First_name text,
            Last_name text,
            gender text,
            address text,
            citizenship_number integer,
            nationality text,
            experience text,
            phone_number integer,
            username text,
            father_name text,
            password text

    )
    """)
    print("Table created successfully")
    #at the end of the database
    connect.commit()
    connect.close()


button_register=Button(frame_title,text="REGISTER",height=3,width=30,command=register)
button_register.grid(row=2,column=0)




#______________________________________________
#inside the login button
def login():
    top3=Toplevel()
    top3.title("login page")
    top3.geometry("300x300")
    def vadlidate_login(username1,password):
        print("Email:",username1.get())
        print("password:",password.get())
        return

    usernameLabel = Label(top3, text="Email").grid(row=2, column=1)
    username1=StringVar()
    username2 = Entry(top3,width=20,textvariable=username1).grid(row=2, column=2,padx=5,pady=5)

    password=StringVar()
    passwordLabel = Label(top3, text="Password").grid(row=3, column=1)
    passwordentry = Entry(top3, show='*',textvariable=password).grid(row=3, column=2,padx=5,pady=5)
    vadlidate_login =partial(vadlidate_login,username1,password)




    def addtodb():
        connect = sqlite3.connect("registration form")
        c = connect.cursor()
        c.execute("SELECT *, oid FROM registration")
        records = c.fetchall()
        # print(records)
        print_records = ""
        print_records2=""
        for record in records:
            print_records += str(record[9])
        for record2 in records:
            print_records2+=str(record[10])
        get_username=username1.get()
        get_password=password.get()
        if print_records==get_username and print_records2==get_password:

            print("valid")

        else:
            print("invalid")





        connect.commit()
        connect.close()




    show_button=Button(top3,text="login in",command=vadlidate_login and addtodb)
    show_button.grid(row=4,column=0)
    top3.mainloop()


button_login=Button(frame_title,text="LOGIN ",height=3,width=30,command=login)
button_login.grid(row=1,column=0)
mainloop()