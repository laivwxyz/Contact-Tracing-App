# Importing important details
from tkinter import *
from add_entry import AddEntryWindow
from search_entry import SearchEntryWindow
from PIL import Image, ImageTk

# Creating a class named ContactTracingApp
class ContactTracingApp:
    def __init__(self, window):
        self.window = window
        self.window.title('Contact Tracing App')
        self.window.geometry('925x780')
        self.window.configure(bg='#fff')
        self.window.resizable(False, False)
    
        # Create background image for front page
        self.image = Image.open('contact_tracing_app_background.png')  
        self.bg_image = ImageTk.PhotoImage(self.image)

        self.bg_label = Label(self.window, image=self.bg_image) 
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Add entry button
        self.add_button = Button(self.window, text='Add Information',bg='cyan',command=self.open_add_entry_window, width=24, height=1, font=('Times New Roman', 20))
        self.add_button.place(x=91, y=269)

        # Search entry button
        self.search_button = Button(self.window, text='Search Existing Information', bg = 'cyan', command=self.open_search_entry_window, width=24, height=1, font=('Times New Roman', 20))
        self.search_button.place(x=477, y=269)

    # Open add entry window
    def open_add_entry_window(self):
        AddEntryWindow()

    # Open search entry window
    def open_search_entry_window(self):
        SearchEntryWindow()