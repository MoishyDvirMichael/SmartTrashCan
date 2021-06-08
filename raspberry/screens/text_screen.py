import tkinter as tk

class TextScreen(tk.Frame):
    def __init__(self, master: tk.Tk, text=''):
        super().__init__(master)
        self.my_label = tk.Label(self, text=text) 
        self.my_label.grid(row=0)

    def show_screen(self):
        self.pack(expand=True)

    def hide_screen(self):
        self.pack_forget()

    def update_barcode(self, text):
        self.my_label['text'] = text
