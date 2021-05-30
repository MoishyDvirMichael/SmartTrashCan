import tkinter as tk

from consts import Consts
from wellcome_screen import Wellcome_screen
from waitting_screen import Waitting_screen
from result_screen import Result_screen
from error_screen import Error_screen

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry(Consts.SCREEN_SIZE)
        self.configure(background=Consts.COLOR_BG_WELLCOME)

        self.wellcome = Wellcome_screen(master=self)
        self.waitting = Waitting_screen(master=self)
        self.error = Error_screen(master=self)
        self.result = Result_screen(master=self, color=None, url=None)


    def run(self):
        self.wellcome.show_screen()
        self.bind('<Return>', self.func1)
        self.mainloop()

    def hide_result_after_sleep(self):
        self.result.hide_screen()
        self.wellcome.show_screen()
        self.configure(background=Consts.COLOR_BG_WELLCOME)
        self.bind('<Return>', self.func1)

    def hide_error_after_sleep(self):
        self.error.hide_screen()
        self.wellcome.show_screen()
        self.configure(background=Consts.COLOR_BG_WELLCOME)
        self.bind('<Return>', self.func1)

    def func1(self, event):
        self.unbind('<Return>')
        self.wellcome.hide_screen()
        self.waitting.show_screen()
        self.bind('<Return>', self.func2)

    def func2(self, event):
        self.unbind('<Return>')
        self.waitting.hide_screen()
        if self.genarate_success():
            self.configure(background=Consts.COLOR_BG_RESULT)
            self.result.show_screen()
            self.after(Consts.RESULT_TIMEOUT, self.hide_result_after_sleep)
        else:
            self.configure(background=Consts.COLOR_BG_ERROR)
            self.error.show_screen()
            self.after(Consts.ERROR_TIMEOUT, self.hide_error_after_sleep)

    def genarate_success(self) -> bool:
        return True
