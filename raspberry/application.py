import tkinter as tk

from consts import Consts
from screens import *

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry(Consts.SCREEN_SIZE)
        self.configure(background=Consts.COLOR_BG_WELCOME)

        self.welcome_screen = WelcomeScreen(master=self)
        self.waiting_screen = WaitingScreen(master=self, barcod=0)
        self.error_screen = ErrorScreen(master=self)
        self.result_screen = ResultScreen(master=self)

    def run(self):
        self.welcome_screen.show_screen()
        self.bind('<Return>', self.func1)
        self.mainloop()

    def hide_result_after_sleep(self):
        self.result_screen.hide_screen()
        self.welcome_screen.show_screen()
        self.configure(background=Consts.COLOR_BG_WELCOME)
        self.bind('<Return>', self.func1)

    def hide_error_after_sleep(self):
        self.error_screen.hide_screen()
        self.welcome_screen.show_screen()
        self.configure(background=Consts.COLOR_BG_WELCOME)
        self.bind('<Return>', self.func1)

    def func1(self, event):
        self.unbind('<Return>')
        self.waiting_screen.update_barcode(barcod=0)
        self.welcome_screen.hide_screen()
        self.waiting_screen.show_screen()
        self.bind('<Return>', self.func2)

    def func2(self, event):
        self.unbind('<Return>')
        self.waiting_screen.hide_screen()
        if self.genarate_success():
            self.configure(background=Consts.COLOR_BG_RESULT)
            self.result_screen.update_result(name=':)', color='green', image_url=None)
            self.result_screen.show_screen()
            self.after(Consts.RESULT_TIMEOUT, self.hide_result_after_sleep)
        else:
            self.configure(background=Consts.COLOR_BG_ERROR)
            self.error_screen.show_screen()
            self.after(Consts.ERROR_TIMEOUT, self.hide_error_after_sleep)

    def genarate_success(self) -> bool:
        return False
