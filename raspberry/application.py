import tkinter as tk

import tkinter as tk
import keyboard
import threading
import time
from threading import Timer

from consts import Consts
from database import DB
from led_strip import Led
from screens.screens import *

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        
        DB.init()
        Led.init()
        
        self.geometry(Consts.SCREEN_SIZE)
        self.configure(background=Consts.COLOR_BG_WELCOME)

        self.__input_text = tk.StringVar()

        self.welcome_screen = WelcomeScreen(master=self, new_barcode_callback=self.procces_new_barcode_callback, input_var=self.__input_text)
        self.waiting_screen = WaitingScreen(master=self)
        self.error_screen = ErrorScreen(master=self)
        self.result_screen = ResultScreen(master=self)

    def run(self):
        self.current_screen = self.welcome_screen
        self.welcome_screen.show_screen()
        self.mainloop()

    def procces_new_barcode_callback(self, event):
        print('procces_new_barcode_callback')
        self.unbind('<Return>')
        barcode = self.str2int(self.__input_text.get()) #TODO check if the input is a number
        self.waiting_screen.update_barcode(barcode)
        self.__callback_done = threading.Event()
        self.doc_watch = DB.add_scanned_item(barcode, self.item_was_found_callback)
        
        self.change_screen(self.waiting_screen)
        self.t = Timer(Consts.ERROR_TIMEOUT, self.item_was_not_found_callback, [barcode])
        self.t.start()
        pass

    def item_was_found_callback(self, doc_snapshot, changes, read_time):
        for change in changes:
            if change.type.name == 'MODIFIED':
                print('item_was_found_callback')
                self.t.cancel()
                self.stop_listening_to_scanned_item()
                if self.is_item_identified(change.document):
                    self.item_was_identified(change.document)
                else:
                    self.item_was_not_identified(change.document._data['barcode'])
                self.after(Consts.RESULT_TIMEOUT, self.change_screen, self.welcome_screen)

    def is_item_identified(self, doc)->bool:
        res = doc._data.get('is_identified') == True
        print(f'is_item_identified = {res}')
        return res

    def item_was_not_found_callback(self, missing_barcode):
        print('item_was_not_found_callback')
        self.stop_listening_to_scanned_item()
        self.change_screen(self.error_screen)
        self.after(Consts.RESULT_TIMEOUT, self.change_screen, self.welcome_screen)

    def item_was_identified(self, doc):
        print('item_was_identified')
        self.update_product_details(doc)
        self.change_screen(self.result_screen)
    def item_was_not_identified(self, missing_barcode):
        print('item_was_not_identified')
        self.change_screen(self.error_screen)

    def update_product_details(self, doc):
        product = DB.get_product(doc._data.get('product'))
        recycling_bin_type = DB.get_recycling_bin_type(product.get('recycling_bin_type')) # TODO what if it's not defined?
        Led.turn_on(recycling_bin_type['color_hex'])
        self.result_screen.update_result(name=product.get('name'), recycling_bin_type=recycling_bin_type, image_url=product.get('image'))
        pass

    def change_screen(self, new_screen, *arg):
        self.current_screen.hide_screen()
        self.current_screen = new_screen
        self.current_screen.show_screen(*arg)

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

def main():
    app = Application()
    app.run()


if __name__ == "__main__":
    main()
