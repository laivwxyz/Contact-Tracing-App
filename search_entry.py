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

        # Entry for search
        self.search_entry = Entry(self.window, font=("Perpetua", 15), bd=2, width=40)
        self.search_entry.place(x=260, y=180)

        self.search_button = Button(self.window, text="Search", bg="cyan", fg="black", width=15, height=2, command=self.search_entries)
        self.search_button.place(x=400, y=230)

        self.result_text = Text(self.window, width=50, height=15, wrap=WORD, font=("Perpetua", 15), bd=2)
        self.result_text.place(x=210, y=300)

        # Clear Button
        Button(self.window, text="Clear", bg="cyan", fg="black", width=15, height=2, command=self.clear).place(x=300, y=670)
    
        # Exit Button
        Button(self.window, text="Exit", bg="cyan", fg="black", width=15, height=2, command=self.exit).place(x=465, y=670)
