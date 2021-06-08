import tkinter as tk
from consts import Consts


class WelcomeScreen(tk.Frame):
    """
    Class for the first screen in the application.
    It says welcome and offers user to scan the barcod.
    """
    def __init__(self, master: tk.Tk):
        super().__init__(master, bg=Consts.COLOR_BG_WELCOME)
        
        self.welcome_label = tk.Label(self, text="Welcome!",
                                       font=("Arial Bold", 30),
                                       bg=Consts.COLOR_BG_WELCOME,
                                       fg=Consts.COLOR_TEXT_WELCOME)
        self.welcome_label.grid()
        self.instraction_label = tk.Label(self, text="Please enter a barcode.",
                                          font=("Arial Bold", 20),
                                          bg=Consts.COLOR_BG_WELCOME,
                                          fg=Consts.COLOR_TEXT_WELCOME)
        self.instraction_label.grid()

    def show_screen(self):
        self.pack(expand=True)

    """def show_screen(self, timeout):
        self.after(timeout, self.pack)"""

    def hide_screen(self):
        self.pack_forget()
