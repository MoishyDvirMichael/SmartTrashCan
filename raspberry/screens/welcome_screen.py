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
        # self.master.__callback_done = threading.Event()
        self.doc_watch = DB.add_scanned_item(barcode, self.master.waiting_screen.item_was_found_callback)
        
        self.master.change_screen(self.master.waiting_screen)
        pass

    def str2int(self, text):
        try: 
            return int(text)
        except:
            return False
    # def item_was_found_callback(self, doc_snapshot, changes, read_time):
    #     for change in changes:
    #         if change.type.name == 'MODIFIED':
    #             print('item_was_found_callback')
    #             self.t.cancel()
    #             self.stop_listening_to_scanned_item()
    #             if self.is_item_identified(change.document):
    #                 self.item_was_identified(change.document)
    #             else:
    #                 self.item_was_not_identified(change.document._data['barcode'])
    #             self.master.after(Consts.RESULT_TIMEOUT, self.master.change_screen, self.master.welcome_screen)

    # def is_item_identified(self, doc)->bool:
    #     res = doc._data.get('is_identified') == True
    #     print(f'is_item_identified = {res}')
    #     return res

    # def item_was_not_found_callback(self, missing_barcode):
    #     print('item_was_not_found_callback')
    #     self.stop_listening_to_scanned_item()
    #     self.master.change_screen(self.master.error_screen)
    #     self.master.after(Consts.RESULT_TIMEOUT, self.master.change_screen, self.master.welcome_screen)

    # def item_was_identified(self, doc):
    #     print('item_was_identified')
    #     self.master.update_product_details(doc)
    #     self.master.change_screen(self.master.result_screen)
    # def item_was_not_identified(self, missing_barcode):
    #     print('item_was_not_identified')
    #     self.master.change_screen(self.master.error_screen)

    # def stop_listening_to_scanned_item(self):
    #     try:
    #         self.doc_watch.unsubscribe()
    #     except:
    #         pass