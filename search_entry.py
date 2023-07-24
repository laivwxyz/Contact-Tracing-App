# Importing important details
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import Label, Entry, Text, Button

# Creating a class named SearchEntryWindow
class SearchEntryWindow:
    def __init__(self):
        self.window = Toplevel()
        self.window.title("Search Entry")
        self.window.geometry("925x780")
        self.window.configure(bg='#326273')
        self.window.resizable(False, False)

        # Create background image for search entry
        self.image = Image.open("search_entry_background.png")  
        self.bg_image = ImageTk.PhotoImage(self.image)

        self.bg_label = Label(self.window, image=self.bg_image)  
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
