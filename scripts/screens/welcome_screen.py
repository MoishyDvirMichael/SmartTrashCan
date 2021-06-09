import tkinter as tk

class WelcomeScreen(tk.Frame):
    def __init__(self, master: tk.Tk, text, input_var):
        super().__init__(master)
        self.my_label = tk.Label(self, text = text) 
        self.my_label.grid(row=0)
        self.my_entry = tk.Entry(self, textvariable = input_var)
        self.my_entry.grid(row=1)

    def show_screen(self):
        self.pack(expand=True)

    def hide_screen(self):
        self.pack_forget()

    def update_text(self, text):
        self.my_label['text'] = text
        pass
