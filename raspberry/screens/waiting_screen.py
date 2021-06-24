import tkinter as tk
from consts import Consts
from threading import Timer
import time
from threading import Thread, currentThread

class WaitingScreen(tk.Frame):
    """
    Class for the second screen in the application.
    It saves the screen while server updates the shop list.
    """
    def __init__(self, master: tk.Tk, barcode=0):
        super().__init__(master, bg=Consts.COLOR_BG_WAITING)
        self.input_label = tk.Label(self,
                                    text=f'Searching {barcode}...',
                                    font=("Arial Bold", 22),
                                    bg=Consts.COLOR_BG_WAITING,
                                    fg=Consts.COLOR_TEXT_WAITING)
        self.input_label.grid(pady=20)
        self.my_label = tk.Label(self, text="Please wait while it is being updated in the shopping list",
                                 font=("Arial Bold", 15),
                                 bg=Consts.COLOR_BG_WAITING,
                                 fg=Consts.COLOR_TEXT_WAITING,
                                 wraplength=460)
        self.my_label.grid(pady=20)

    def show_screen(self):
        self.pack(expand=True)
        self.t = Timer(Consts.ERROR_TIMEOUT, self.item_was_not_found_callback)
        self.t.start()
        

    def hide_screen(self):
        self.pack_forget()

    def update_barcode(self, barcode):
        self.input_label['text'] = f'Searching {barcode}...'
        self.dots = Thread(target=self.dots_cycle, args=(barcode,))
        self.dots.start()

    def dots_cycle(self, barcode):
        max_dots = 4
        dots = 0
        t = currentThread()
        print('dots:')
        while getattr(t, "stop", False) == False:
            dots = (dots + 1 ) % max_dots
            self.input_label['text'] = f'Searching {barcode}' + '.' * dots + ' ' * (max_dots - dots)
            self.master.update()
            time.sleep(0.15)


    def item_was_found_callback(self, doc_snapshot, changes, read_time):
        for change in changes:
            if change.type.name == 'MODIFIED':
                self.dots.stop = True
                print('item_was_found_callback')
                self.t.cancel()
                self.stop_listening_to_scanned_item()
                if is_item_identified(change.document):
                    self.item_was_identified(change.document)
                else:
                    self.item_was_not_identified(change.document._data['barcode'])

    def item_was_not_found_callback(self):
        print('item_was_not_found_callback')
        self.stop_listening_to_scanned_item()
        self.master.change_screen(self.master.trying_to_connect_screen)

    def item_was_identified(self, doc):
        print('item_was_identified')
        self.master.result_screen.update_product_details(doc)
        self.master.change_screen(self.master.result_screen)
    
    def item_was_not_identified(self, missing_barcode):
        print('item_was_not_identified')
        self.master.change_screen(self.master.error_screen)

    def stop_listening_to_scanned_item(self):
        try:
            self.master.welcome_screen.doc_watch.unsubscribe()
        except:
            pass

def is_item_identified(doc) -> bool:
    res = doc._data.get('is_identified') == True
    print(f'is_item_identified = {res}')
    return res
