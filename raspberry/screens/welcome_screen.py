import tkinter as tk
from consts import Consts
from led_strip import Led
from database import DB
from threading import Timer


class WelcomeScreen(tk.Frame):
    """
    Class for the first screen in the application.
    It says welcome and offers user to scan the barcod.
    """
    def __init__(self, master: tk.Tk):
        super().__init__(master, bg=Consts.COLOR_BG_WELCOME)
        
        self.__input_text = tk.StringVar()
        
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
        
        self.name_entry = tk.Entry(self, textvariable=self.__input_text)
        self.name_entry.grid(row=2, in_=self.frame)
        self.name_entry.lower(self.frame)

    def show_screen(self):
        Led.turn_off()
        self.name_entry.delete(0,'end')
        self.name_entry.focus()
        self.master.configure(background=Consts.COLOR_BG_WELCOME)
        self.master.bind('<Return>', self.procces_new_barcode_callback)
        self.pack(expand=True)

    def hide_screen(self):
        self.pack_forget()

    def procces_new_barcode_callback(self, event):
        print('procces_new_barcode_callback')
        self.master.unbind('<Return>')
        barcode = self.str2int(self.__input_text.get()) #TODO check if the input is a number
        self.master.waiting_screen.update_barcode(barcode)
        watch = DB.add_scanned_item(self.master.get_uid(), barcode, self.master.waiting_screen.item_was_found_callback)
        if watch == None:
            print('Timeout Error in DB.add_scanned_item()')
            self.master.waiting_screen.dots.stop = True
            self.master.change_screen(self.master.trying_to_connect_screen)
        else:
            self.doc_watch = watch
            self.master.change_screen(self.master.waiting_screen)

    def str2int(self, text):
        try: 
            return int(text)
        except:
            return False
