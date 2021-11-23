import mysql.connector as con
import tkinter as tk
from tkinter import messagebox

def addRecordToDB(event):
    # Database connection
    cur = con.connect(
        host='localhost',
        user='root',
        password=''
    )
    cursor = cur.cursor()
    # Create database
    cursor.execute('CREATE DATABASE  IF NOT EXISTS `testdb`')
    cursor.execute('USE `testdb`')
    # Create database
    cursor.execute('CREATE TABLE  IF NOT EXISTS `persons`('
                   '`id` INT AUTO_INCREMENT PRIMARY KEY,'
                   ' `name` VARCHAR(50), '
                   ' `email` VARCHAR(100),'
                   ' `address` VARCHAR(250) '
                   ')')
    # Insert data from the application
    cursor.execute('INSERT INTO persons(name,email,address) VALUES(%s,%s,%s)',
                   (nameEntry.get(),emailEntry.get(),addressText.get('1.0',"end")))
    # Show success message
    messagebox.showinfo("Success!","Record successfully saved.")
    # Clear fields
    emailEntry.delete(0,tk.END)
    nameEntry.delete(0,tk.END)
    addressText.delete("1.0","end")
    emailEntry.focus()
    return
def appPractice():
    window = tk.Tk()
    window.title("GUI Practice")
    # window.geometry("350x400")
    topLabel = tk.Label(window, text='Person Management System',
           fg = "white",
           bg = "dark green",
           font = "Helvetica 16 bold",
           justify = "center"
           )
    topLabel.grid(row = 0, column = 0,columnspan=2, sticky='ew')
    emailLabel = tk.Label(window, text='Email:')
    emailLabel.grid(row = 1, column = 0,sticky=tk.W,pady=5)
    # Add a text field for email
    global emailEntry
    emailEntry = tk.Entry(window)
    emailEntry.grid(row = 1, column = 1, sticky='ew',padx=10,pady=5)

    # Label for text field for name
    nameLabel = tk.Label(window, text='Full Name: ')
    nameLabel.grid(row = 2, column = 0,sticky=tk.W)
    #Add a text field for name
    global nameEntry
    nameEntry = tk.Entry(window)
    nameEntry.grid(row = 2, column = 1, sticky='ew',padx=10,pady=5)

    addressLabel = tk.Label(window, text='Address: ')
    addressLabel.grid(row = 3, column = 0,sticky=tk.W)
    # Add a multiline text field for address
    global addressText
    addressText = tk.Text(window, height=10,
                    width=25,
                    bg="light yellow")
    addressText.grid(row = 3, column = 1, sticky='ew',padx=10,pady=5)
    saveBtn = tk.Button(window, text="Save Data")
    # Add on click event listener to the button
    saveBtn.bind('<Button-1>',addRecordToDB)
    saveBtn.grid(row = 4, column = 1,sticky = tk.W, columnspan = 2,pady=5)
    window.mainloop()

