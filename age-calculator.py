import tkinter as tk
import customtkinter
from tkcalendar import DateEntry


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("500x300")
        self.text_var = tk.StringVar()
        self.text_var.set("Hello world")
        self.label = customtkinter.CTkLabel(master=self,
                                            textvariable=self.text_var,
                                            font=("Arial", 20, "italic",
                                                "underline"),
                                            text_color="lightgreen",
                                            corner_radius=0)
        self.label.grid(row=0, column=0, columnspan=3, sticky="nsew")

        self.label_dob = customtkinter.CTkLabel(master=self,
                                                text="Date of birth")
        self.label_gd = customtkinter.CTkLabel(master=self,
                                            text="Given date")

        self.label_dob.grid(row=1, column=0, padx=0, pady=0)
        self.label_gd.grid(row=1, column=1)
        self.calendar = DateEntry(
            master=self, width=50, height=50, background="dark", borderwidth=2)
        self.calendar.grid(row=2, column=0)


app = App()
app.mainloop()
