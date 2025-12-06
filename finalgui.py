import mysql.connector
import tkinter as tk
from tkinter import *
import unittest
# ================================
# DATABASE CONNECTION
# ================================
def connect_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="F00tball",
            database="final_reservations_db"
        )
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("DB Error", f"Database connection failed:\n{err}")
        return None

def insert_customer(last_box, first_box, email_box, phone_box,confirmation_label,error_label):
    confirmation_label.grid_remove()
    error_label.grid_remove()
    conn = connect_db()
    if conn is None:
        return
    
    cursor = conn.cursor()

    sql = """
    INSERT INTO customers (last_name, first_name, email, phone)
    VALUES (%s, %s, %s, %s)
    """

    values = (last_box.get(), first_box.get(), email_box.get(), phone_box.get())

    try:
        cursor.execute(sql, values)
        conn.commit()
        confirmation_label.grid(row= 8,column=1)
    except Exception as e:
        error_label.grid(row= 8,column=1)
    finally:
        conn.close()

def insert_boat(boatid_box,length_box,cust_id_box,confirmation_label,error_label):
    confirmation_label.grid_remove()
    error_label.grid_remove()
    conn = connect_db()
    if conn is None:
        return
    
    cursor = conn.cursor()

    sql = """
    INSERT INTO boats (boat_id, cust_id, length)
    VALUES (%s, %s, %s)
    """

    values = (boatid_box.get(), cust_id_box.get(), length_box.get())

    try:
        cursor.execute(sql, values)
        conn.commit()
        confirmation_label.grid(row= 8,column=1)
    except Exception as e:
        error_label.grid(row= 8,column=1)
    finally:
        conn.close()

def edit_customer(last_box, first_box, email_box, phone_box,confirmation_label,error_label,cust_id):
    confirmation_label.grid_remove()
    error_label.grid_remove()
    conn = connect_db()
    if conn is None:
        return
    
    cursor = conn.cursor()

    sql =     'UPDATE customers SET last_name = %s, first_name = %s, email = %s, phone = %s WHERE cust_id = %s'

    values = (last_box.get(), first_box.get(), email_box.get(), phone_box.get(), cust_id)

    try:
        cursor.execute(sql, values)
        conn.commit()
        confirmation_label.grid(row= 8,column=1)
    except Exception as e:
        error_label.grid(row= 8,column=1)
    finally:
        conn.close()

def create_reservation(cust_id,boat_id,slip_number,start_date,end_date, confirmation_label,error_label):
    confirmation_label.grid_remove()
    error_label.grid_remove()
    conn = connect_db()
    if conn is None:
        return
    
    cursor = conn.cursor()

    values = (cust_id,boat_id,slip_number,start_date,end_date)
    sql = """
    INSERT INTO reservations (cust_id, boat_id, slip_number, start_date, end_date)
    VALUES (%s, %s, %s, %s, %s)
    """
    other_value = (slip_number)
    othersql = 'UPDATE slips SET availability = "0" WHERE slip_number = %s'
    try:
        cursor.execute(othersql, other_value)
        cursor.execute(sql, values)
        conn.commit()
        confirmation_label.grid(row= 26,column=4)
    except Exception as e:
        print(f"SQL ERROR: {e}")  # This will print the exact error to your terminal
        error_label.grid(row= 26,column=4)
    finally:
        conn.close()



def open_individual(id_reference):
    ip = Toplevel()
    ip.title("Customer Page")
    ip.geometry("1000x600")
    conn = connect_db()
    if conn is None:
        return
    cursor = conn.cursor()
    searched = id_reference
    sql = "SELECT * FROM customers WHERE cust_id = %s"
    id = (searched, )
    cursor.execute(sql,id)
    result = cursor.fetchall()
    # print(result)
    
    first_label = Label(ip, text="Existing Customer", font = ("Helvetica", 14))
    first_label.grid(row=0, column=0)

    last_label = Label(ip, text='Last Name').grid(row= 1,column=0)
    first_label = Label(ip, text='First Name').grid(row= 2,column=0)
    email_label = Label(ip, text='Email').grid(row= 3,column=0)
    phone_label = Label(ip, text='Phone',).grid(row= 4,column=0)

    last_box = Entry(ip)
    last_box.grid(row= 1,column=1)
    last_box.insert(tk.END, result[0][1])

    first_box = Entry(ip)
    first_box.grid(row=2,column=1)
    first_box.insert(tk.END, result[0][2])

    email_box = Entry(ip)
    email_box.grid(row=3,column=1)
    email_box.insert(tk.END, result[0][3])

    phone_box = Entry(ip)
    phone_box.grid(row=4,column=1)
    phone_box.insert(tk.END, result[0][4])

    confirmation_label = Label(ip,text=('Customer Edited Successfully'))
    error_label = Label(ip,text='Something went wrong editing that customer')


    create_button = Button(ip, text="Save Edit", command=lambda : edit_customer(last_box, first_box, email_box, phone_box,confirmation_label,error_label,result[0][0]))
    create_button.grid(row=5,column=1)

    boatslistlabel = Label(ip,text=('Boats'), font = ("Helvetica", 14))
    boatslistlabel.grid(row=6, column=0,padx=5,pady=5)
        

    searched = result[0][0]
    # sql = "SELECT * FROM boats INNER JOIN customers ON boats.cust_id = customers.cust_id where boat_id  = %s"
    sql = "SELECT  boat_id,length FROM boats WHERE cust_id  = %s"
    name = (searched, )
    cursor.execute(sql,name)
    boat_result = cursor.fetchall()

    if not boat_result:
        boat_result = "No Boats found for customer"
        searched_label = Label(ip, text = boat_result)
        searched_label.grid(row=7, column=0, padx=10,pady=10)
    else:
        for index, x in enumerate(boat_result, start=7):
            num = 0
            index+=1
            # select_button = Button (bp, text="Select")
            # select_button.grid(row=index, column=num)
            for y in x:
                searched_label = Label(ip, text= y)
                searched_label.grid(row=index, column=num+1,padx=5, pady=5)
                num+=1
    
    reservationlistlabel = Label(ip,text=('Reservations'), font = ("Helvetica", 14))
    reservationlistlabel.grid(row=12, column=0,padx=5,pady=5)
        
    searched = result[0][0]
    # sql = "SELECT * FROM boats INNER JOIN customers ON boats.cust_id = customers.cust_id where boat_id  = %s"
    sql = "SELECT* FROM reservations WHERE cust_id  = %s"
    name = (searched, )
    cursor.execute(sql,name)
    reservationresult = cursor.fetchall()
    # print(reservationresult)

    if not reservationresult:
        reservationresult = "No Reservations found for customer"
        searched_label = Label(ip, text = reservationresult)
        searched_label.grid(row=13, column=0, padx=10,pady=10)
    else:
        for index, x in enumerate(reservationresult, start=14):
            num = 0
            index+=1
            # select_button = Button (bp, text="Select")
            # select_button.grid(row=index, column=num)
            for y in x:
                searched_label = Label(ip, text= y)
                searched_label.grid(row=index, column=num+1,padx=5, pady=5)
                num+=1
    

    reservationlistlabel = Label(ip,text=('Create Reservation'), font = ("Helvetica", 14))
    reservationlistlabel.grid(row=20, column=0,padx=5,pady=5)

    boat_id_label = Label(ip, text='Boat ID',).grid(row= 22,column=2)
    start_label = Label(ip, text='Start Date',).grid(row= 23,column=2)
    end_label = Label(ip, text='End Date',).grid(row= 24,column=2)
    slip_label = Label(ip, text='Slip Number',).grid(row= 25,column=2)
    length_label = Label(ip, text='Enter Length',).grid(row= 25,column=0)

    boat_id_label = Entry(ip)
    boat_id_label.grid(row=22,column=3)

    start_label = Entry(ip)
    start_label.grid(row=23,column=3)

    end_label = Entry(ip)
    end_label.grid(row=24,column=3)

    slip_label = Entry(ip)
    slip_label.grid(row= 25,column=3)

    length_entry = Entry(ip)
    length_entry.grid(row= 25,column=1)

    confirmation_label = Label(ip,text=('Reservation Created Successfully'))
    error_label = Label(ip,text='Something went wrong creating that reservation')
    search_res_button = Button(ip, text="Search", command=lambda: find_reservation(boat_id_label,start_label,end_label,length_entry))
    search_res_button.grid(row=26,column=1)

    commit_reservation_button = Button(ip, text="Save Reservation", command=lambda: create_reservation(result[0][0],boat_id_label.get(),slip_label.get(),start_label.get(),end_label.get(), confirmation_label,error_label))
    commit_reservation_button.grid(row=26,column=3)

    confirmation_label = Label(ip, text= "Reservation Successful")
    error_label = Label(ip, text= "Reservation Unsuccessful")

    available_label = Label(ip, text= "Availabilites", font = ("Helvetica", 14))
    available_label.grid(row=27,column=0)


    search_box_label = Label(ip, text='Slip Number')
    search_box_label.grid(row=28, column=1, padx=5,pady=5)

    search_box_label = Label(ip, text='Length')
    search_box_label.grid(row=28, column=2, padx=5,pady=5)



    def find_reservation(boat_id_label,start_label,end_label,length_entry):
        conn = connect_db()
        if conn is None:
            return
        cursor = conn.cursor()

        searched = length_entry.get()
    # sql = "SELECT * FROM boats INNER JOIN customers ON boats.cust_id = customers.cust_id where boat_id  = %s"
        sql = "SELECT slip_number, length FROM slips WHERE availability = '1' and length >= %s "
        name = (searched, )
        cursor.execute(sql,name)
        findresresult = cursor.fetchall()
        # print(findresresult)

        if not findresresult:
            findresresult = "No Reservations available"
            searched_label = Label(ip, text = findresresult)
            searched_label.grid(row=28, column=0, padx=10,pady=10)
        else:
            for index, x in enumerate(findresresult, start=28):
                num = 0
                index+=1
                # last_box.insert(tk.END, result[0][1])
                length_reference = x[0]
                select_button = Button (ip, text="Select", command= lambda v = length_reference: slip_label.insert(tk.END, v))
                select_button.grid(row=index, column=num)
                for y in x:
                    searched_label = Label(ip, text= y)
                    searched_label.grid(row=index, column=num+1,padx=5, pady=5)
                    num+=1


def make_customer_page():
    cp = Toplevel()
    cp.title('Customer Search Page')
    cp.geometry("1000x300")
    def search_now():
        
        conn = connect_db()
        if conn is None:
            return
        cursor = conn.cursor()

        searched = search_box.get()
        sql = "SELECT * FROM customers WHERE last_name = %s"
        name = (searched, )
        cursor.execute(sql,name)
        result = cursor.fetchall()

        search_box_label = Label(cp, text='Customer ID')
        search_box_label.grid(row=2, column=1, padx=5,pady=5)
        search_box_label = Label(cp, text='Last Name')
        search_box_label.grid(row=2, column=2, padx=5,pady=5)
        search_box_label = Label(cp, text='First Name')
        search_box_label.grid(row=2, column=3, padx=5,pady=5)
        search_box_label = Label(cp, text='Email')
        search_box_label.grid(row=2, column=4, padx=5,pady=5)
        search_box_label = Label(cp, text='Phone')
        search_box_label.grid(row=2, column=5, padx=5,pady=5)


        if not result:
            result = "Record not found"
            searched_label = Label(cp, text = result)
            searched_label.grid(row=2, column=0, padx=10,pady=10)

        else:
            for index, x in enumerate(result, start=2):
                num = 0
                index+=1
                id_reference = x[0]
                # print(id_reference)
                select_button = Button (cp, text="Select", command = lambda v = id_reference :open_individual(v))
                select_button.grid(row=index, column=num)
                for y in x:
                    searched_label = Label(cp, text= y)
                    searched_label.grid(row=index, column=num+1,padx=5, pady=5)
                    num+=1

    search_box = Entry(cp)
    search_box.grid( row= 0, column= 1, padx=10,pady=10)

    search_box_label = Label(cp, text='Search Customer Last Name')
    search_box_label.grid(row=0, column=0, padx=10, pady=10)

    search_button = Button(cp, text = 'Search Database', command = search_now)
    search_button.grid(row=1, column=0, padx=10,pady=10)



    

def make_boat_page():
    bp = Toplevel()
    bp.title('Boat Search Page')
    bp.geometry("1000x300")
    def search_now():
        
        conn = connect_db()
        if conn is None:
            return
        cursor = conn.cursor()

        searched = search_box.get()
        # sql = "SELECT * FROM boats INNER JOIN customers ON boats.cust_id = customers.cust_id where boat_id  = %s"
        sql = "SELECT    boats.*, customers.first_name,customers.last_name,customers.email,customers.phone FROM boats INNER JOIN customers ON boats.cust_id = customers.cust_id where boat_id  = %s"
        name = (searched, )
        cursor.execute(sql,name)
        result = cursor.fetchall()

        search_box_label = Label(bp, text='Boat ID')
        search_box_label.grid(row=2, column=1, padx=5,pady=5)
        search_box_label = Label(bp, text=' Cust ID')
        search_box_label.grid(row=2, column=2, padx=5,pady=5)
        search_box_label = Label(bp, text='Length')
        search_box_label.grid(row=2, column=3, padx=5,pady=5)
        search_box_label = Label(bp, text='First Name')
        search_box_label.grid(row=2, column=4, padx=5,pady=5)
        search_box_label = Label(bp, text='Last Name')
        search_box_label.grid(row=2, column=5, padx=5,pady=5)
        search_box_label = Label(bp, text='Email')
        search_box_label.grid(row=2, column=6, padx=5,pady=5)
        search_box_label = Label(bp, text='Phone')
        search_box_label.grid(row=2, column=7, padx=5,pady=5)

        if not result:
            result = "Record not found"
            searched_label = Label(bp, text = result)
            searched_label.grid(row=3, column=0, padx=10,pady=10)

        else:
            for index, x in enumerate(result, start=2):
                num = 0
                index+=1
                id_reference = x[1]
                select_button = Button (bp, text="Select",command=lambda v = id_reference:open_individual(v))
                select_button.grid(row=index, column=num)
                for y in x:
                    searched_label = Label(bp, text= y)
                    searched_label.grid(row=index, column=num+1,padx=5, pady=5)
                    num+=1

    search_box = Entry(bp)
    search_box.grid( row= 0, column= 1, padx=10,pady=10)

    search_box_label = Label(bp, text='Search Boat')
    search_box_label.grid(row=0, column=0, padx=10, pady=10)

    search_button = Button(bp, text = 'Search Database', command = search_now)
    search_button.grid(row=1, column=0, padx=10,pady=10)

def create_customer_page():
    ccp = Toplevel()
    ccp.title('Add New Customer')
    ccp.geometry("1000x300")

    first_label = Label(ccp, text="New Customer", font = ("Helvetica", 14))
    first_label.grid(row=0, column=0)

    last_label = Label(ccp, text='Last Name',).grid(row= 1,column=0)
    first_label = Label(ccp, text='First Name',).grid(row= 2,column=0)
    email_label = Label(ccp, text='Email',).grid(row= 3,column=0)
    phone_label = Label(ccp, text='Phone #',).grid(row= 4,column=0)

    last_box = Entry(ccp)
    last_box.grid(row= 1,column=1)

    first_box = Entry(ccp)
    first_box.grid(row=2,column=1)

    email_box = Entry(ccp)
    email_box.grid(row=3,column=1)

    phone_box = Entry(ccp)
    phone_box.grid(row=4,column=1)

    confirmation_label = Label(ccp,text=('Customer Created Successfully'))
    error_label = Label(ccp,text='Something went wrong creating that customer')


    create_button = Button(ccp, text="Create", command=lambda: insert_customer(last_box, first_box, email_box, phone_box,confirmation_label,error_label))
    create_button.grid(row=5,column=1)

def create_boat_page():
    cb = Toplevel()
    cb.title('Add New Boat')
    cb.geometry("1000x300")

    first_label = Label(cb, text="New Boat", font = ("Helvetica", 14))
    first_label.grid(row=0, column=0)

    boat_id_label = Label(cb, text='Boat ID',).grid(row= 1,column=0)
    length_label = Label(cb, text='Length',).grid(row= 2,column=0)
    cust_id_label = Label(cb, text='Cust ID',).grid(row= 3,column=0)

    boatid_box = Entry(cb)
    boatid_box.grid(row= 1,column=1)

    length_box = Entry(cb)
    length_box.grid(row=2,column=1)

    cust_id_box = Entry(cb)
    cust_id_box.grid(row=3,column=1)

    confirmation_label = Label(cb,text=('Boat Created Successfully'))
    error_label = Label(cb,text='Something went wrong creating that boat')

    create_button = Button(cb, text="Create", command=lambda: insert_boat(boatid_box,length_box,cust_id_box,confirmation_label,error_label))
    create_button.grid(row=5,column=1)

#root junk
root = Tk()
root.title('Menu Screen')
root.geometry("1000x300")


first_label = Label(root, text="Menu", font = ("Helvetica", 14))
first_label.pack(pady=10)

customer_search = Button(root, text="Search Customer", command=make_customer_page)
customer_search.pack(pady=10)

boat_search = Button(root, text="Search Boat", command=make_boat_page)
boat_search.pack(pady=10)

ccp = Button(root, text="Create Customer", command=create_customer_page)
ccp.pack(pady=10)

cb = Button(root, text="Create Boat", command=create_boat_page)
cb.pack(pady=10)



root.mainloop()