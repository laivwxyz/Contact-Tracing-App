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
