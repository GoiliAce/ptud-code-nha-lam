import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.text_val = tk.StringVar()
        self.temp = ""

        # Entry widget
        self.entry = tk.Entry(master, textvariable=self.text_val, state='disabled', disabledbackground='white', disabledforeground='black', font=('Arial', 20), justify='right')
        self.entry.grid(column=0, row=0, columnspan=4, padx=10, pady=10)

        # Buttons
        buttons = [
            "C", "AC", "/",
            "7", "8", "9", "*",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "0", ".","%", "="
        ]

        # Define button functions
        def button_clicked(text):
            self.temp = text
            self.text_val.set(self.entry.get() + text)

        def button_equal():
            text = self.entry.get()
            try:
                sum = eval(text)
            except:
                sum = "Không thể tính toán"
            self.text_val.set(sum)

        def clear_a_char():
            text = self.entry.get()
            text = text[:-1]
            self.text_val.set(text)

        def clear_all_char():
            self.text_val.set("")

        # Create buttons and add them to the grid
        row, col = 1, 1
        for button_text in buttons:
            if button_text == "C":
                button = tk.Button(master, text=button_text, command=clear_a_char, width=8, height=2)
            elif button_text == "AC":
                button = tk.Button(master, text=button_text, command=clear_all_char, width=8, height=2)
            elif button_text == "=":
                button = tk.Button(master, text=button_text, command=button_equal, width=8, height=2)
            else:
                button = tk.Button(master, text=button_text, command=lambda text=button_text: button_clicked(text), width=8, height=2)

            button.grid(row=row, column=col, pady=5)

            col += 1
            if col > 3:
                col = 0
                row += 1

    def run(self):
        self.master.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root).run()
