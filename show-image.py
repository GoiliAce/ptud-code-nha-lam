import tkinter as tk
import customtkinter
from PIL import Image, ImageTk


class Frame(customtkinter.CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.paths = []
        self.load_paths("data/image/paths.txt")
        self.path = self.paths[0]
        self.w = 700
        self.h = 400
        self.img = Image.open(self.path)
        self.img = self.img.resize((self.w, self.h), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)
        self.label = tk.Label(master=self, image=self.img, justify="center")
        self.label.grid(row=0, column=0, sticky="nsew",
                        padx=10, pady=10, columnspan=4)
        self.prev = customtkinter.CTkButton(
            master=self, text="<<", command=self.prev_image, width=30)
        self.prev.grid(row=2, column=0, padx=10, pady=10)
        self.next = customtkinter.CTkButton(
            master=self, text=">>", command=self.next_image, width=30)
        self.next.grid(row=2, column=3, padx=10, pady=10)

        self.load = customtkinter.CTkButton(
            master=self, text="add image", command=self.add_image_to_list)
        self.load.grid(row=2, column=2, padx=10, pady=10)
        self.delete = customtkinter.CTkButton(
            master=self, text="delete image", command=self.delete_image_from_list)
        self.delete.grid(row=2, column=1, padx=10, pady=10)

        self.num = tk.StringVar()
        self.update_num()
        self.num_of_image = customtkinter.CTkLabel(
            master=self, textvariable=self.num, font=("Arial", 20, "bold"), bg_color="transparent")
        self.num_of_image.grid(row=1, column=1, columnspan=2)

    def update_num(self):
        self.num.set(f"{self.paths.index(self.path) + 1}/{len(self.paths)}")

    def load_image(self, path):
        self.img = Image.open(path)
        self.img = self.img.resize((self.w, self.h), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)
        self.label.configure(image=self.img)
        self.update_num()

    def load_paths(self, paths):
        with open(paths, "r") as file:
            self.paths = file.readlines()
        self.paths = [path.strip() for path in self.paths]

    def next_image(self):
        if self.paths.index(self.path) == len(self.paths) - 1:
            self.path = self.paths[0]

        else:
            self.path = self.paths[self.paths.index(self.path) + 1]
        self.load_image(self.path)

    def prev_image(self):
        if self.paths.index(self.path) == 0:
            print("first image")
            self.path = self.paths[-1]
        else:
            self.path = self.paths[self.paths.index(self.path) - 1]
        self.load_image(self.path)

    def add_image_to_list(self):
        dialog = tk.filedialog.askopenfiles(
            "r", title="Mở file")
        filename = dialog[0].name
        if filename not in self.paths:
            self.paths.append(filename)
            with open("data/image/paths.txt", "w") as file:
                file.write("\n".join(self.paths))
            self.path = self.paths[-1]
            self.load_image(self.path)
            tk.messagebox.showinfo(
                title="Success!", message="Image added!", parent=self)
        else:
            tk.messagebox.showerror(
                title="Error!", message="Image already exists!", parent=self)

    def delete_image_from_list(self):
        self.paths.remove(self.path)
        with open("data/image/paths.txt", "w") as file:
            file.write("\n".join(self.paths))
        self.path = self.paths[-1]
        self.load_image(self.path)
        self.update_num()
        tk.messagebox.showinfo(
            title="Success!", message="Image deleted!", parent=self)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Show Image")

        self.title_label = customtkinter.CTkLabel(
            master=self, text="Show Image App", font=("Arial", 30, "bold"))
        self.title_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.frame = Frame(master=self)
        self.frame.grid(row=1, column=0, sticky="nsew", columnspan=4,
                        padx=10, pady=10)


app = App()
app.mainloop()
