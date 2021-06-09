import tkinter as tk
from consts import Consts
from led_strip import Led


class WelcomeScreen(tk.Frame):
    """
    Class for the first screen in the application.
    It says welcome and offers user to scan the barcod.
    """
    def __init__(self, master: tk.Tk, new_barcode_callback, input_var):
        super().__init__(master, bg=Consts.COLOR_BG_WELCOME)
        
        self.callback = new_barcode_callback
        
        self.frame = tk.Frame(self)
        self.frame.grid()
        
        self.welcome_label = tk.Label(self, text="Welcome!",
                                       font=("Arial Bold", 30),
                                       bg=Consts.COLOR_BG_WELCOME,
                                       fg=Consts.COLOR_TEXT_WELCOME)
        self.welcome_label.grid(row=0)
        self.instraction_label = tk.Label(self, text="Please scan a barcode",
                                          font=("Arial Bold", 20),
                                          bg=Consts.COLOR_BG_WELCOME,
                                          fg=Consts.COLOR_TEXT_WELCOME)
        self.instraction_label.grid(row=1)
        
        self.name_entry = tk.Entry(self, textvariable=input_var)
        self.name_entry.grid(row=2, in_=self.frame)
        self.name_entry.lower(self.frame)

    def show_screen(self):
        Led.turn_off()
        self.name_entry.delete(0,'end')
        self.name_entry.focus()
        self.master.configure(background=Consts.COLOR_BG_WELCOME)
        self.master.bind('<Return>', self.callback)
        self.pack(expand=True)

    def hide_screen(self):
        self.pack_forget()
