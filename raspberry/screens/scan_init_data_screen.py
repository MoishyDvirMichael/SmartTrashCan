import json
import tkinter as tk
from consts import Consts
from led_strip import Led
from database import DB
from threading import Timer


class ScanInitDataScreen(tk.Frame):
    def __init__(self, master: tk.Tk):
        super().__init__(master, bg=Consts.COLOR_BG_WELCOME)

        self._input_text = tk.StringVar()

        self.frame = tk.Frame(self)
        self.frame.grid()

        self.label = tk.Label(self, text="Scan the QR code from the app",
                              font=("Arial Bold", 20),
                              bg=Consts.COLOR_BG_WELCOME,
                              fg=Consts.COLOR_TEXT_WELCOME)
        self.label.grid(row=0)

        self.name_entry = tk.Entry(self, textvariable=self._input_text)
        self.name_entry.grid(row=1, in_=self.frame)
        self.name_entry.lower(self.frame)

    def update_text(self, text):
        self.label['text'] = text

    def show_screen(self):
        Led.turn_off()
        self.name_entry.delete(0, 'end')
        self.name_entry.focus()
        self.master.configure(background=Consts.COLOR_BG_WELCOME)
        self.master.bind('<Return>', self.procces_init_data_callback)
        self.pack(expand=True)

    def hide_screen(self):
        self.pack_forget()

    def procces_init_data_callback(self, event):
        print('procces_new_barcode_callback')
        self.master.unbind('<Return>')
        # TODO check if the input is a valid json
        print(self._input_text.get())
        data = str2json(self._input_text.get())
        self.master.update_data(data)
        self.master.change_screen(self.master.trying_to_connect_screen)
        pass

def str2json(text) -> dict:
    try:
        return json.loads(text)
    except:
        return {}
