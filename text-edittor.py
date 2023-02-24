import tkinter as tk
import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.textbox = customtkinter.CTkTextbox(
            master=self, width=300, corner_radius=0)
        self.textbox.grid(row=0, column=0, columnspan=3, sticky="nsew")
        self.textbox.insert("0.0", "")
        self.button_open = customtkinter.CTkButton(
            master=self, text="Mở file", command=self.button_open_clicked, width=150)
        self.button_open.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.button_save = customtkinter.CTkButton(
            master=self, text="Lưu", command=self.button_save_clicked, width=150)
        self.button_save.grid(row=1, column=2, sticky="nsew", padx=10, pady=10)

    def button_open_clicked(self):
        dialog = tk.filedialog.askopenfiles(
            "r", filetypes=[("Text files", "*.txt")], title="Mở file")
        filename = dialog[0].name
        with open(filename, "r", encoding='utf-8') as f:
            text = f.read()
        self.textbox.delete("0.0", "end")
        self.textbox.insert("0.0", text)

    def button_save_clicked(self):
        text = self.textbox.get("0.0", "end")
        with open("data/text/test.txt", "w", encoding='utf-8') as f:
            f.write(text)


app = App()
app.mainloop()
