# document code
# import tkinter
# import tkinter.messagebox
#
# diaBox = Tk()
# Entry(diaBox,text = 'Enter your name').pack()
# diaBox.mainloop()
# name = input("Enter your name")
# print("Howdy")

from tkinter import *

def get_entry_field():
    nam = e1.get()
    print("hello " + nam)


master = Tk()
Label(master, text="Enter your name").grid(row=0)

e1= Entry(master)

e1.grid(row=1, column=0)

Button(master, text='Confirm', command=get_entry_field).grid(row=2, column=0, sticky=W, pady=4)

mainloop( )
