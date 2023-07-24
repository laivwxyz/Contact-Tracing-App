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
