
import tkinter as tk

from consts import Consts
from wellcome_screen import Wellcome_screen
from waitting_screen import Waitting_screen
from result_screen import Result_screen
from error_screen import Error_screen


def first_screen():
    root = tk.Tk()
    root.geometry(Consts.SCREEN_SIZE)
    root.configure(background=Consts.COLOR_PRIMARY)
    screen = Wellcome_screen(master=root)
    screen.show_screen()
    root.mainloop()

def second_screen():
    root = tk.Tk()
    root.geometry(Consts.SCREEN_SIZE)
    root.configure(background=Consts.COLOR_BG_WAITTING)
    screen = Waitting_screen(master=root)
    screen.show_screen()
    root.mainloop()

def third_screen():
    root = tk.Tk()
    root.geometry(Consts.SCREEN_SIZE)
    root.configure(background=Consts.COLOR_BG_ERROR)
    screen = Error_screen(master=root)
    screen.show_screen()
    root.mainloop()

def show_picture():
    root = tk.Tk()
    root.geometry(Consts.SCREEN_SIZE)
    root.configure(background=Consts.COLOR_DIVIDER)
    screen = Result_screen(master=root, url=None)
    screen.show_screen()
    root.mainloop()

def main():
    first_screen()
    second_screen()
    third_screen()
    show_picture()



if __name__ == "__main__":
    main()