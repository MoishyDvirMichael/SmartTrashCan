import tkinter as tk
from consts import Consts


class Wellcome_screen(tk.Frame):
    """
    Class for the first screen in the application.
    It says wellcome and offers user to scan the barcod.
    """
    def __init__(self, master: tk.Tk):
        super().__init__(master, bg=Consts.COLOR_BG_WELLCOME)
        self.wellcome_label = tk.Label(self, text="Wellcome!",
                                       font=("Arial Bold", 30),
                                       bg=Consts.COLOR_BG_WELLCOME,
                                       fg=Consts.COLOR_TEXT_WELLCOME)
        self.wellcome_label.grid()
        self.instraction_label = tk.Label(self, text="Please enter a barcode.",
                                          font=("Arial Bold", 20),
                                          bg=Consts.COLOR_BG_WELLCOME,
                                          fg=Consts.COLOR_TEXT_WELLCOME)
        self.instraction_label.grid()

    def show_screen(self):
        self.pack(expand=True)

    def hide_screen(self):
        self.pack_forget()

    def update_text(self, text):
        self.my_label['text'] = text
