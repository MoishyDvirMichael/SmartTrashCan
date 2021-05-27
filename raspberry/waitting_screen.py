import tkinter as tk
from consts import Consts


class Waitting_screen(tk.Frame):
    """
    Class for the second screen in the application.
    It saves the screen while server updates the shop list.
    """
    def __init__(self, master: tk.Tk):
        super().__init__(master, bg=Consts.COLOR_BG_WAITTING)
        self.my_label = tk.Label(self, text="Thank you, please wait..",
                                 font=("Arial Bold", 20),
                                 bg=Consts.COLOR_BG_WAITTING,
                                 fg=Consts.COLOR_TEXT_WAITTING)
        self.my_label.grid()

    def show_screen(self):
        self.pack(expand=True)

    def hide_screen(self):
        self.pack_forget()

    def update_text(self, text):
        self.my_label['text'] = text
