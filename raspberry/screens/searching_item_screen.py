import tkinter as tk

class SearchingItemScreen(tk.Frame):
    def __init__(self, master: tk.Tk):
        super().__init__(master)
        self.my_label = tk.Label(self, text = '') 
        self.my_label.grid(row=0)

    def show_screen(self):
        self.pack(expand=True)

    def hide_screen(self):
        self.pack_forget()

    def update_barcode(self, barcode):
        self.my_label['text'] = f'Searching {barcode}\'s item'
