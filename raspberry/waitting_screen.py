import tkinter as tk
from consts import Consts


class Waitting_screen(tk.Frame):
    """
    Class for the second screen in the application.
    It saves the screen while server updates the shop list.
    """
    def __init__(self, master: tk.Tk, barcod=0):
        super().__init__(master, bg=Consts.COLOR_BG_WAITTING)
        self.input_label = tk.Label(self,
                                    text=f'Barcod {barcod} is scaned.',
                                    font=("Arial Bold", 25),
                                    bg=Consts.COLOR_BG_WAITTING,
                                    fg=Consts.COLOR_TEXT_WAITTING)
        self.input_label.grid()
        self.my_label = tk.Label(self, text="Please wait while it is being updated in the shop list.",
                                 font=("Arial Bold", 13),
                                 bg=Consts.COLOR_BG_WAITTING,
                                 fg=Consts.COLOR_TEXT_WAITTING)
        self.my_label.grid()

    def show_screen(self):
        self.pack(expand=True)

    def hide_screen(self):
        self.pack_forget()

    def update_text(self, barcod):
        self.input_label['text'] = f'Barcod {barcod} is scaned.'
