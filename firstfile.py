import tkinter as tk

window = tk.Tk()

window.title("Calculator")
window.minsize(width=150, height=300)

text_val = tk.StringVar()


entry = tk.Entry(window, textvariable=text_val, state='disabled', disabledbackground='white', disabledforeground='black', font=('Arial', 20), justify='right')
#set height of entry
entry.grid(column=0, row=0, columnspan=4, padx=10, pady=10)

temp = ""

# Label

# my_label.pack()

# # Button
def button_clicked(text):
    temp = text
    text_val.set(entry.get() + text)    
    print(text)


def button_equal():
    text = entry.get()
    try:
            sum = eval(text)
    except:
        sum = "Không thể tính toán"
    text_val.set(sum)  

def clear_a_char():
    text = entry.get()
    text = text[:-1]
    text_val.set(text)

def clear_all_char():
    text_val.set("")

btn_0 = tk.Button(text="0", command= lambda: button_clicked("0"), width=8, height=2)
btn_1 = tk.Button(text="1", command=lambda: button_clicked("1") , width=8, height=2)
btn_2 = tk.Button(text="2", command= lambda: button_clicked("2") , width=8, height=2)
btn_3 = tk.Button(text="3", command=    lambda: button_clicked("3"), width=8, height=2)
btn_4 = tk.Button(text="4", command=    lambda: button_clicked("4"),    width=8, height=2)
btn_5 = tk.Button(text="5", command=    lambda: button_clicked("5"), width=8, height=2)
btn_6 = tk.Button(text="6", command=    lambda: button_clicked("6"), width=8, height=2 )
btn_7 = tk.Button(text="7", command=    lambda: button_clicked("7"), width=8, height=2)                     
btn_8 = tk.Button(text="8", command=   lambda: button_clicked("8"), width=8, height=2)
btn_9 = tk.Button(text="9", command=   lambda: button_clicked("9"), width=8, height=2)
btn_add = tk.Button(text="+", command=  lambda: button_clicked("+"), width=8, height=2)
btn_sub = tk.Button(text="-", command= lambda: button_clicked("-"), width=8, height=2)
btn_mul = tk.Button(text="*", command= lambda: button_clicked("*"), width=8, height=2)
btn_div = tk.Button(text="/", command= lambda: button_clicked("/"), width=8, height=2)
btn_equal = tk.Button(text="=", command= button_equal, width=8, height=2)
btn_dot = tk.Button(text=".", command= lambda: button_clicked("."), width=8, height=2)
btn_percent = tk.Button(text="mod", command= lambda: button_clicked("%"), width=8, height=2)

btn_clear_1 = tk.Button(text="C", command= clear_a_char, width=8, height=2)
btn_clear_2 = tk.Button(text="AC", command= clear_all_char, width=8, height=2)

btn_0.grid(column=0, row=7,  pady=5)
btn_1.grid(column=0, row=6,  pady=5)
btn_2.grid(column=1, row=6,  pady=5)
btn_3.grid(column=2, row=6,  pady=5)
btn_4.grid(column=0, row=5,  pady=5)
btn_5.grid(column=1, row=5,  pady=5)
btn_6.grid(column=2, row=5,  pady=5)
btn_7.grid(column=0, row=4,  pady=5)
btn_8.grid(column=1, row=4,  pady=5)
btn_9.grid(column=2, row=4,  pady=5)
btn_add.grid(column=3, row=3,  pady=5)
btn_sub.grid(column=3, row=4,  pady=5)
btn_mul.grid(column=3, row=5,  pady=5)
btn_div.grid(column=3, row=6,  pady=5)
btn_equal.grid(column=3, row=7,  pady=5)
btn_clear_1.grid(column=1, row=3,  pady=5)
btn_clear_2.grid(column=2, row=3,  pady=5)
btn_dot.grid(column=1, row=7,  pady=5)
btn_percent.grid(column=2, row=7,  pady=5)





window.mainloop()