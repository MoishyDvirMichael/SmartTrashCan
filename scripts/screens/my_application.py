import tkinter as tk
from screens import *
from threading import Timer
import keyboard
import threading
from database import DB
import time


class MyApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        DB.init()
        self.geometry('480x320')
        
        self.__input_text = tk.StringVar()
        self.screen1 = WelcomeScreen(self, text='screen 1', input_var=self.__input_text)
        self.screen2 = SearchingItemScreen(self)
        self.screen3 = TextScreen(self, text="can't find")
        self.screen4 = TextScreen(self, text="found")
    

    def run(self):
        self.current_screen = self.screen1
        self.screen1.show_screen()
        self.screen1.my_entry.focus()
        self.bind('<Return>', self.procces_new_barcode_callback)
        self.mainloop()

    def procces_new_barcode_callback(self, event):
        self.unbind('<Return>')
        barcode = self.str2int(self.__input_text.get()) #TODO check if the input is a number
        self.screen2.update_barcode(barcode)
        self.__callback_done = threading.Event()
        self.doc_watch = DB.add_scanned_item(barcode, self.item_was_found_callback)
        
        self.change_screen(self.screen2)
        self.t = Timer(10.0, lambda: {
                self.stop_listening_to_scanned_item(),
                self.change_screen(self.screen3)
            })
        self.t.start()
        pass

    def change_screen(self, new_screen, *arg):
        self.current_screen.hide_screen()
        self.current_screen = new_screen
        self.current_screen.show_screen(*arg)

    def item_was_found_callback(self, doc_snapshot, changes, read_time):
        for change in changes:
            if change.type.name=='ADDED':
                print('ADDED')
            elif change.type.name == 'MODIFIED':
                self.t.cancel()
                print('MODIFIED')
                self.stop_listening_to_scanned_item()
                self.change_screen(self.screen4)
    
    def str2int(self, text):
        try: 
            return int(text)
        except:
            return False

    def stop_listening_to_scanned_item(self):
        try:
            self.doc_watch.unsubscribe()
        except:
            pass