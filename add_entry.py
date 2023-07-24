# Importing important details
from tkinter import *
from PIL import Image, ImageTk
from tkinter.ttk import Combobox
from tkinter import messagebox
from tkinter import Label, Entry, Text, Button, StringVar

#Creating a class named AddEntryWindow
class AddEntryWindow:
    def __init__(self):
        self.window = Toplevel()
        self.window.title("Add Entry")
        self.window.geometry("925x780+300+200")
        self.window.configure(bg='#326273')
        self.window.resizable(False,False)

        # Create background image for add entry 
        self.image = Image.open("add_entry_background.png")  
        self.bg_image = ImageTk.PhotoImage(self.image)

        self.bg_label = Label(self.window, image=self.bg_image)  
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Name Label
        Label (self.window, text="NAME", font = ('Perpetua', 18, "bold"), bg= "cyan").place(x=90, y=120)
