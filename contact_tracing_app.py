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
