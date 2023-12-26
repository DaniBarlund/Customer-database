from tkinter import*
from tkinter import ttk
import sqlite3

global clear
clear = False


def clearEntry():
    entry_FirstName.delete(0, END)
    entry_LastName.delete(0, END)
    entry_id.delete(0, END)
    entry_email.delete(0, END)
    entry_sign.delete(0, END)
    entry_membership.delete(0, END)
    entry_country.delete(0, END)
    entry_address.delete(0, END)

def clearEntryAndSetDefault():
    #Clear entries
    clearEntry()
    
    #Put the default entries
    entry_FirstName.insert(0,'First Name')
    entry_LastName.insert(0,'Last Name')
    entry_email.insert(0,'Email')
    entry_id.insert(0,'ID')
    entry_sign.insert(0,'Sign Up Date')
    entry_membership.insert(0,'Membership')
    entry_country.insert(0,'Country')
    entry_address.insert(0,'Address')

#Submit button to put all information from entries to database
def submit():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO data VALUES (:first_name, :last_name, :email, :id, :sign_up_date, :membership, :country, :address)",
        {
            'first_name': entry_FirstName.get(),
            'last_name': entry_LastName.get(),
            'email': entry_email.get(),
            'id': entry_id.get(),
            'sign_up_date': entry_sign.get(),
            'membership': entry_membership.get(),
            'country': entry_country.get(),
            'address': entry_address.get()
        })


    conn.commit()
    conn.close()

    treeview_customerlist.insert('','end',values=(
        entry_FirstName.get(),
        entry_LastName.get(),
        entry_email.get(),
        entry_id.get(),
        entry_sign.get(),
        entry_membership.get(),
        entry_country.get(),
        entry_address.get())
    )
    clearEntryAndSetDefault()


#Fill treeview used when submitting a new customer or opening the program
def fill():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    query = "SELECT * FROM data"
    cursor.execute(query)
    rows = cursor.fetchall()
    
    for i in rows:
        treeview_customerlist.insert('','end',values=i)

    conn.commit()
    conn.close()

#Fill treeview but also delete, used when deleting a customer.
def updateTreeview():
    for i in treeview_customerlist.get_children():
        treeview_customerlist.delete(i)
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    query = "SELECT * FROM data"
    cursor.execute(query)
    rows = cursor.fetchall()
    
    for i in rows:
        treeview_customerlist.insert('','end',values=i)

    conn.commit()
    conn.close()

def delete():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    
    selected_item = treeview_customerlist.selection()
    for item in selected_item: 
        idnumber = treeview_customerlist.item(item,'values')[3]
        treeview_customerlist.delete(item)
    
        cursor.execute("DELETE from data WHERE id=" + idnumber)

    conn.commit()
    conn.close()

#Click bind function
def clicker(e):
    clearEntry()
    #Find what region of treeview is pressed.
    region = treeview_customerlist.identify("region",e.x, e.y)

    if region == 'cell':
        selected_item = treeview_customerlist.focus() 

        entry_FirstName.insert(0,treeview_customerlist.item(selected_item,'values')[0])
        entry_LastName.insert(0,treeview_customerlist.item(selected_item,'values')[1])
        entry_email.insert(0,treeview_customerlist.item(selected_item,'values')[2])
        entry_id.insert(0,treeview_customerlist.item(selected_item,'values')[3])
        entry_sign.insert(0,treeview_customerlist.item(selected_item,'values')[4])
        entry_membership.insert(0,treeview_customerlist.item(selected_item,'values')[5])
        entry_country.insert(0,treeview_customerlist.item(selected_item,'values')[6])
        entry_address.insert(0,treeview_customerlist.item(selected_item,'values')[7])

    else:
        clearEntryAndSetDefault()
        
    


def update():
    #Update treeview
    selected_item = treeview_customerlist.focus()
    treeview_customerlist.item(selected_item, values=(
        entry_FirstName.get(),
        entry_LastName.get(),
        entry_email.get(),
        entry_id.get(),
        entry_sign.get(),
        entry_membership.get(),
        entry_country.get(),
        entry_address.get())
    )
    

    #Update database
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    update_query = """Update data set
    first_name = ?,
    last_name = ?,
    email = ?,
    sign_up_date = ?,
    membership = ?,
    country = ?,
    address = ? 
    where id = ?"""
    data=(
        entry_FirstName.get(),
        entry_LastName.get(),
        entry_email.get(),
        entry_sign.get(),
        entry_membership.get(),
        entry_country.get(),
        entry_address.get(),
        entry_id.get()
    )
    cursor.execute(update_query, data)

    conn.commit()
    conn.close()
    clearEntryAndSetDefault()

def search():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    whereOrData="""SELECT * FROM data WHERE """
    whereAndData="""SELECT * FROM data WHERE """
    first = False
    entries = 0
    data = ()
    #Check how many entries and adjust data and selected data.
    if entry_FirstName.get() != 'First Name' and entry_FirstName.get() != '':
        entries += 1
        whereAndData = whereAndData + 'first_name = ?'
        whereOrData = whereOrData + 'first_name = ?'
        data = (entry_FirstName.get(),)
        first = True

    if entry_LastName.get() != 'Last Name' and entry_LastName.get() != '':
        entries += 1
        whereAndData = whereAndData + 'And last_name = ?'
        whereOrData = whereOrData + 'Or last_name = ?'
        data = data + (entry_LastName.get(),)

    if entry_email.get() != 'Email' and entry_email.get() != '':
        entries += 1
        whereAndData = whereAndData + 'And email = ?'
        whereOrData = whereOrData + 'Or email = ?'
        data = data + (entry_email.get(),)

    if entry_sign.get() != 'Sign Up Date' and entry_sign.get() != '':
        entries += 1
        whereAndData = whereAndData + 'And sign_up_date = ?'
        whereOrData = whereOrData + 'Or sign_up_date = ?'
        data = data + (entry_sign.get(),)

    if entry_membership.get() != 'Membership' and entry_membership.get() != '':
        entries += 1
        whereAndData = whereAndData + 'And membership = ?'
        whereOrData = whereOrData + 'Or membership = ?'
        data = data + (entry_membership.get(),)

    if entry_country.get() != 'Country' and entry_country.get() != '':
        entries += 1
        whereAndData = whereAndData + 'And country = ?'
        whereOrData = whereOrData + 'Or country = ?'
        data = data + (entry_country.get(),)

    if entry_address.get() != 'Address' and entry_address.get() != '':
        entries += 1
        whereAndData = whereAndData + 'And address = ?'
        whereOrData = whereOrData + 'Or address = ?'
        data = data + (entry_address.get(),)

    if entry_id.get() != 'ID' and entry_id.get() != '':
        entries += 1
        whereAndData = whereAndData + 'And id = ?'
        whereOrData = whereOrData + 'Or id = ?'
        data = data + (entry_id.get(),)

    #Check if first name was given, if not remove or, and
    if not first:
        fixedWhereAndData = whereAndData.replace('And', '', 1)
        fixedWhereOrData = whereOrData.replace('Or', '', 1)
    
    #Select data according to the amount of entries given.
    if entries != 0:
        if entries == 1:
            try:
                cursor.execute(fixedWhereOrData,data)
            except:
                cursor.execute(whereOrData,data)
        else:
            try:
                cursor.execute(fixedWhereAndData,data)
            except:
                cursor.execute(whereAndData,data)

        #Clear treeview
        for i in treeview_customerlist.get_children():
            treeview_customerlist.delete(i)
    
        #Fill treeview with searched data
        rows = cursor.fetchall()
        for i in rows:
            treeview_customerlist.insert('','end',values=i)

    conn.commit()
    conn.close()

def changeText():
    global clear

    if clear == False:
        button_search['text']='Clear'
        clear = True
        
    elif clear == True:
        button_search['text']='Search'
        
        for i in treeview_customerlist.get_children():
            treeview_customerlist.delete(i)
        
        fill()
        clear = False





#Database
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

conn.commit()


#Make the main window
root = Tk()
root.geometry('1024x576')
root.title('Customer Database')

#Add 3 main frames of the application
frame_treeview = LabelFrame(root,text='Customer list')
frame_treeview.pack(fill='both', expand='yes', padx=3, pady=3)
frame_data = LabelFrame(root, text='Customer data')
frame_data.pack(fill='both', expand='yes', padx=3, pady=3)
frame_functions = LabelFrame(root, text='Search')
frame_functions.pack(fill='both', expand='yes', padx=3, pady=3)

#Treeview for customer list
columns = ('First name', 'Last name', 'email', 'id','Sign up date', 'membership', 'country', 'address')
treeview_customerlist = ttk.Treeview(frame_treeview, columns=columns, show='headings')


#Change colums to the right size
treeview_customerlist.column('First name',width=120, anchor=CENTER)
treeview_customerlist.column('Last name',width=120, anchor=CENTER)
treeview_customerlist.column('id',width=120, anchor=CENTER)
treeview_customerlist.column('email',width=120, anchor=CENTER)
treeview_customerlist.column('Sign up date',width=120, anchor=CENTER)
treeview_customerlist.column('membership',width=120, anchor=CENTER)
treeview_customerlist.column('country',width=120, anchor=CENTER)
treeview_customerlist.column('address',width=120, anchor=CENTER)

#Headings for each column
treeview_customerlist.heading('First name', text='First Name')
treeview_customerlist.heading('Last name', text='Last name')
treeview_customerlist.heading('id', text='ID')
treeview_customerlist.heading('email', text='Email')
treeview_customerlist.heading('Sign up date', text='Sign up date')
treeview_customerlist.heading('membership', text='Membership')
treeview_customerlist.heading('country', text='Country')
treeview_customerlist.heading('address', text='Address')

treeview_customerlist.pack(expand='yes', fill='both', padx=10, pady=10)

#Bind for treeview
treeview_customerlist.bind('<ButtonRelease-1>', clicker)

#Entry boxes for customer data frame
entry_FirstName = Entry(frame_data, borderwidth=3)
entry_LastName = Entry(frame_data, borderwidth=3)
entry_email = Entry(frame_data, borderwidth=3)
entry_id = Entry(frame_data, borderwidth=3)
entry_sign = Entry(frame_data, borderwidth=3)
entry_membership = Entry(frame_data, borderwidth=3)
entry_country = Entry(frame_data, borderwidth=3)
entry_address = Entry(frame_data, borderwidth=3)

entry_FirstName.insert(0,'First Name')
entry_LastName.insert(0,'Last Name')
entry_email.insert(0,'Email')
entry_id.insert(0,'ID')
entry_sign.insert(0,'Sign Up Date')
entry_membership.insert(0,'Membership')
entry_country.insert(0,'Country')
entry_address.insert(0,'Address')

#pack all entry boxes.
entry_FirstName.place(x=10, width=175, height=25)
entry_LastName.place(x=10, rely=0.6,width=175, height=25)
entry_email.place(x=287,width=175, height=25)
entry_id.place(x=287, rely=0.6, width=175, height=25)
entry_sign.place(x=562, width=175, height=25)
entry_membership.place(x=562, rely=0.6,width=175, height=25)
entry_country.place(x=830,width=175, height=25)
entry_address.place(x=830, rely=0.6,width=175, height=25)

#Style for buttons
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 11))


#Buttons for functions frame.
button_submit = ttk.Button(frame_functions, text='Submit', command=lambda:[submit()])
button_update = ttk.Button(frame_functions, text='Update', command=update)
button_delete = ttk.Button(frame_functions, text='Delete', command=lambda:[delete()])
button_search = ttk.Button(frame_functions, text='Search', command=lambda:[search(), changeText()])

button_submit.place(x=10, y=15, width=175, height=40)
button_update.place(x=287, y=15, width=175, height=40)
button_delete.place(x=562, y=15, width=175, height=40)
button_search.place(x=830, y=15, width=175, height=40)


fill()

root.mainloop()
conn.close()

