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
        self.image = Image.open("contact_tracing_app_background.png")  
        self.bg_image = ImageTk.PhotoImage(self.image)

        self.bg_label = Label(self.window, image=self.bg_image) 
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
