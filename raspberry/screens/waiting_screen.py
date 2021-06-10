import tkinter as tk
from consts import Consts
from threading import Timer


class WaitingScreen(tk.Frame):
    """
    Class for the second screen in the application.
    It saves the screen while server updates the shop list.
    """
    def __init__(self, master: tk.Tk, barcod=0):
        super().__init__(master, bg=Consts.COLOR_BG_WAITING)
        self.input_label = tk.Label(self,
                                    text=f'Barcod {barcod} is scaned.',
                                    font=("Arial Bold", 25),
                                    bg=Consts.COLOR_BG_WAITING,
                                    fg=Consts.COLOR_TEXT_WAITING)
        self.input_label.grid()
        self.my_label = tk.Label(self, text="Please wait while it is being updated in the shop list.",
                                 font=("Arial Bold", 13),
                                 bg=Consts.COLOR_BG_WAITING,
                                 fg=Consts.COLOR_TEXT_WAITING)
        self.my_label.grid()

    def show_screen(self):
        self.pack(expand=True)
        self.t = Timer(Consts.ERROR_TIMEOUT, self.item_was_not_found_callback)
        self.t.start()
        

    def hide_screen(self):
        self.pack_forget()

    def update_barcode(self, barcod):
        self.input_label['text'] = f'Barcod {barcod} is scaned.'

    def item_was_found_callback(self, doc_snapshot, changes, read_time):
        for change in changes:
            if change.type.name == 'MODIFIED':
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
        self.master.change_screen(self.master.error_screen)

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
