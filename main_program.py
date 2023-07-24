# Importing important details
from tkinter import *
from contact_tracing_app import ContactTracingApp

# Run the program
if __name__ == "__main__":
    window = Tk()
    main = ContactTracingApp(window)
    window.mainloop()