import tkinter as tk
import customtkinter
from tkcalendar import DateEntry
import datetime
from dateutil import relativedelta


class Frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # self.geometry("500x300")

        self.label_dob = customtkinter.CTkLabel(master=self,
                                                text="Date of birth", width=100)
        self.label_gd = customtkinter.CTkLabel(master=self,
                                               text="Given date", width=100)
        self.label_dob.grid(row=1, column=0, padx=10, pady=5)
        self.label_gd.grid(row=1, column=2, padx=10, pady=5)

        self.calendar_dob = DateEntry(
            master=self, background="dark", date_pattern="dd/mm/yyyy")
        self.calendar_gd = DateEntry(
            master=self, background="dark", date_pattern="dd/mm/yyyy")

        self.calendar_dob.config(justify='center')
        self.calendar_gd.config(justify='center')
        self.calendar_dob.grid(row=2, column=0, ipady=8)
        self.calendar_gd.grid(row=2, column=2, ipady=8)
        self.button = customtkinter.CTkButton(master=self, text="Calculate", text_color="green", font=(
            "Arial", 15, "italic"), command=self.calculate, fg_color="#dceedc", corner_radius=0, hover="white", border_width=2)
        self.button.grid(row=3, column=1,
                         sticky="nsew", padx=10, pady=10)

        self.text_age = tk.StringVar()
        self.entry = customtkinter.CTkEntry(
            master=self, height=50, placeholder_text="Age", corner_radius=0, border_width=2, textvariable=self.text_age, state="disabled", font=("Arial", 16, "bold"), justify="center")
        self.entry.grid(row=4, column=0, columnspan=3,
                        sticky="nsew", padx=30, pady=10)

    def calculate(self):
        birth_date = self.calendar_dob.get()
        given_date = self.calendar_gd.get()
        birth_date = datetime.datetime.strptime(birth_date, "%d/%m/%Y")
        given_date = datetime.datetime.strptime(given_date, "%d/%m/%Y")

        diff = relativedelta.relativedelta(given_date, birth_date)

        years = diff.years
        months = diff.months
        days = diff.days
        self.text_age.set(
            f"{days } Day(s), {months} Month(s), {years} Year(s)")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.text_var = tk.StringVar()
        self.text_var.set("Age Calculator")
        self.label = customtkinter.CTkLabel(master=self,
                                            textvariable=self.text_var,
                                            font=("Arial", 20, "italic",
                                                  "underline"),
                                            text_color="lightgreen",
                                            corner_radius=0)
        self.label.grid(row=0, column=0, sticky="nsew",
                        columnspan=3, padx=10, pady=15)
        self.frame = Frame(master=self)
        self.frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")


app = App()
app.mainloop()
