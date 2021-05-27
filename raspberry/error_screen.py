import tkinter as tk
from consts import Consts


class Error_screen(tk.Frame):
    """
    Class for the error message screen in the application.
    It prints error message and offers to add the object to the system using application.
    """
    def __init__(self, master: tk.Tk):
        super().__init__(master, bg=Consts.COLOR_BG_ERROR)
        self.timeout = Consts.ERROR_TIMEOUT
        self.error_label = tk.Label(self,
                                    text="The product does not exist in the system",
                                    font=("Arial Bold", 15),
                                    bg=Consts.COLOR_BG_ERROR,
                                    fg=Consts.COLOR_TEXT_ERROR)
        self.error_label.grid()
        self.offer_label = tk.Label(self,
                                    text="You can add it to the system using the app",
                                    font=("Arial Bold", 15),
                                    bg=Consts.COLOR_BG_ERROR,
                                    fg=Consts.COLOR_TEXT_ERROR)
        self.offer_label.grid()

    def show_screen(self):
        self.pack(expand=True)

    def hide_screen(self):
        self.pack_forget()

    def update_text(self, text):
        self.my_label['text'] = text
