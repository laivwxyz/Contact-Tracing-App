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

    def search_entries(self):
        query = self.search_entry.get().strip() 
        if not query:
            # Show a pop-up warning message if the search query is empty
            messagebox.showwarning("No Search Query", "Please enter a search query.")
            return

        search_results = self.search_in_file(query)

        self.result_text.delete(1.0, END)
        if search_results:
            for result in search_results:
                self.result_text.insert(END, result)
                self.result_text.insert(END, "\n\n")

            # Show a pop-up message with the number of matching entries found
            messagebox.showinfo("Search Results", f"{len(search_results)} matching entries found.")
        else:
            self.result_text.insert(END, "No matching entries found.")
            # Show a pop-up warning message if no matching entries are found
            messagebox.showwarning("No Match", "No matching entries found for the search query.")

    def search_in_file(self, query):
        matching_entries = []

        try:
            with open("covid_contact_tracing.txt", "r") as file:
                content = file.read()
                entries = content.split("-----------------------------\n")
                for entry in entries:
                    if query.lower() in entry.lower():
                        matching_entries.append(entry)
        except FileNotFoundError:
            # Show a pop-up error message if the file is not found
            messagebox.showerror("Error", "File not found. No entries added yet.")
        except Exception as e:
            # Show a pop-up error message for any other unexpected errors
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

        return matching_entries
    
    def clear(self):
        # Clear the search entry and result text widgets
        self.search_entry.delete(0, END)
        self.result_text.delete(1.0, END)

    def exit(self):
        # Close the application
        self.window.destroy()