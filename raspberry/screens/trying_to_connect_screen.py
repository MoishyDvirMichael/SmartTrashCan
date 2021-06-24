import json
import tkinter as tk
from consts import Consts
from led_strip import Led
from database import DB
from threading import Timer
from connect_to_wifi import ConnectToWifi
import time


class TryingToConnectScreen(tk.Frame):
    def __init__(self, master: tk.Tk):
        super().__init__(master, bg=Consts.COLOR_BG_INTENET_CONNECT)

        self.label = tk.Label(self, text='Trying to connect to the internet',
                              font=("Arial Bold", 20),
                              bg=Consts.COLOR_BG_INTENET_CONNECT,
                              fg=Consts.COLOR_TEXT_INTENET_CONNECT)
        self.label.grid(row=0)

    def update_text(self, text):
        self.label['text'] = text

    def show_screen(self):
        Led.turn_off()
        self.master.configure(background=Consts.COLOR_BG_INTENET_CONNECT)
        self.pack(expand=True)
        self.master.update()
        if (ConnectToWifi.is_connected()) == False and (self.master.get_wifi_length() == 0 or not ConnectToWifi.try_reconnect()):
            self.master.change_screen(self.master.scan_init_data_screen)
        else:
            print('Successfully connected to the wifi')
            self.master.change_screen(self.master.welcome_screen)

    def hide_screen(self):
        self.pack_forget()

    def str2int(self, text):
        try:
            return int(text)
        except:
            return False
