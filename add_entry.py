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

        # LABEL
        # Name Label
        Label (self.window, text="NAME", font = ('Perpetua', 18, "bold"), bg= "cyan").place(x=90, y=120)

        # Contact Number Label
        Label (self.window, text="CONTACT NO.", font = ('Perpetua', 18, "bold"), bg= "cyan").place(x=90, y=170)

        # Age Label
        Label (self.window, text="AGE", font = ('Perpetua', 18, "bold"), bg= "cyan").place(x=90, y=220)

        # Gender Label
        Label (self.window, text="GENDER", font = ('Perpetua', 18, "bold"), bg= "cyan").place(x=485, y=220)

        # Date of birth Label
        Label (self.window, text="DATE OF BIRTH", font = ('Perpetua', 18, "bold"), bg= "cyan").place(x=90, y=270)

        # Address Label
        Label (self.window, text="ADDRESS", font = ('Perpetua', 18, "bold"), bg= "cyan").place(x=90, y=320)

        # Symptoms Label
        Label (self.window, text="Are you experiencing any symptoms in the past 7 days?", font = ('Perpetua', 18, "bold"), bg= "cyan").place(x=90, y=370)

        # Exposure Label
        Label (self.window, text="Have you had exposure to a probable or confirmed case in the last 14 days?", font = ('Perpetua', 18, 'bold'), bg= "cyan").place(x=90, y=470)

        # Testing Label
        Label (self.window, text="Have you been tested for Covid-19 in the last 14 days?", font = ('Perpetua', 18, 'bold'), bg= "cyan").place(x=90, y=570)

        # ENTRY
        # Name Entry
        self.name_value = StringVar()
        name_entry = Entry (self.window, textvariable= self.name_value, width=50,bd=2,font=('Perpetua', 20))
        name_entry.place(x=220, y=120)

        # Contact Entry
        self.contact_value = StringVar()
        contact_entry = Entry (self.window, textvariable= self.contact_value, width=46,bd=2,font=('Perpetua', 20))
        contact_entry.place(x=270, y=170)

        # Age Entry
        self.age_value = StringVar()
        age_entry = Entry (self.window, textvariable= self.age_value, width=17,bd=2,font=('Perpetua', 20))
        age_entry.place(x=220, y=220)
        
        # Date of Birth Entry
        self.birth_value = StringVar()
        birth_entry = Entry (self.window, textvariable= self.birth_value, width=45,bd=2,font=('Perpetua', 20))
        birth_entry.place(x=290, y=270)
        self.birth_value.set('mm/dd/yy')

        # Address Entry
        self.address_entry = Text (self.window, width=76, height=1.5, bd=2)  
        self.address_entry.place(x=220, y=320)

        # SELECT
        # Gender Select
        self.gender_combobox = Combobox (self.window, values=['Male', 'Female', 'LGBTQA +'], font ='Perpetua 20', state="r", width=17)
        self.gender_combobox.place(x=603, y=220)
        self.gender_combobox.set('Select')

        # Symptoms Select
        self.symptoms_combobox = Combobox (self.window, values=['Yes', 'No'], font ='Perpetua 20', state="r", width=20)
        self.symptoms_combobox.place(x=220, y=420)
        self.symptoms_combobox.set('Select')

        # Exposure Select
        self.exposure_combobox = Combobox (self.window, values=['Yes', 'No', 'Uncertain'], font ='Perpetua 20', state="r", width=20)
        self.exposure_combobox.place(x=220, y=520)
        self.exposure_combobox.set('Select')

        # Testing Select
        self.testing_combobox = Combobox (self.window, values=['Yes', 'No'], font ='Perpetua 20', state="r", width=20)
        self.testing_combobox.place(x=220, y=620)
        self.testing_combobox.set('Select')

        # BUTTON
        # Submit Button
        Button(self.window, text="Submit", bg="cyan", fg="black", width=15, height=2, command=self.submit).place(x=270, y=700)
        
        # Clear Button
        Button(self.window, text="Clear", bg="cyan", fg="black", width=15, height=2, command=self.clear).place(x=410, y=700)
        
        # Exit Button
        Button(self.window, text="Exit", bg="cyan", fg="black", width=15, height=2, command=self.exit).place(x=550, y=700)

    def submit(self):
            # Process and store the form data submitted by the user
            name = self.name_value.get()
            contact = self.contact_value.get()
            age = self.age_value.get()
            gender = self.gender_combobox.get()
            birth = self.birth_value.get()
            address = self.address_entry.get(1.0, END)
            symptoms = self.symptoms_combobox.get()
            exposure = self.exposure_combobox.get()
            testing = self.testing_combobox.get()

            # Check if all the required fields are filled
            if not (name and contact and age and gender and birth and address and symptoms != "Select" and exposure != "Select" and testing != "Select"):
                messagebox.showerror("Error", "Please fill out all the fields!")
                return

            # Save the form data to a text file
            with open("covid_contact_tracing.txt", "a") as file:
                file.write(f"NAME: {name}\n")
                file.write(f"CONTACT NO.: {contact}\n")
                file.write(f"AGE: {age}\n")
                file.write(f"GENDER: {gender}\n")
                file.write(f"DATE OF BIRTH: {birth}\n")
                file.write(f"ADDRESS: {address}\n")
                file.write(f"EXPERIENCING SYMPTOMS: {symptoms}\n")
                file.write(f"EXPOSURE TO CONFIRMED CASE: {exposure}\n")
                file.write(f"TESTED FOR COVID-19: {testing}\n")
                file.write("-----------------------------\n")

            # Show a pop-up message after successful submission
            messagebox.showinfo("Success", "Form data submitted successfully!")

    def clear(self):
        # Clear the form fields
        self.name_value.set('')
        self.contact_value.set('')
        self.age_value.set('')
        self.birth_value.set('')
        self.address_entry.delete(1.0, END)
        self.gender_combobox.set("Select")
        self.symptoms_combobox.set("Select")
        self.exposure_combobox.set("Select")
        self.testing_combobox.set("Select")

    def exit(self):
        # Close the application
        self.window.destroy()