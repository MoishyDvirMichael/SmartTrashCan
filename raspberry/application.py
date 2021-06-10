import tkinter as tk

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


        self.welcome_screen = WelcomeScreen(master=self)
        self.waiting_screen = WaitingScreen(master=self)
        self.error_screen = ErrorScreen(master=self)
        self.result_screen = ResultScreen(master=self)
        self.empty_screen = EmptyScreen()

        self.current_screen = self.empty_screen


    def run(self):
        self.change_screen(self.welcome_screen)
        self.mainloop()

    def change_screen(self, new_screen, *arg):
        self.current_screen.hide_screen()
        self.current_screen = new_screen
        self.current_screen.show_screen(*arg)


def main():
    app = Application()
    app.run()

if __name__ == "__main__":
    main()
