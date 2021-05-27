
import tkinter as tk
from PIL import Image, ImageTk

from consts import Consts
from wellcome_screen import Wellcome_screen
from waitting_screen import Waitting_screen
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
    frame1 = tk.Frame(master=root, width=160, height=320, bg=Consts.COLOR_DIVIDER)
    a = tk.Label(frame1,
                 text = "The list is updated saccessfully!",
                 font=("Arial Bold", 10),
                 bg=Consts.COLOR_DIVIDER,
                 fg=Consts.COLOR_PRIMARY_TEXT,
                 wraplength=150,
                 justify='left')
    a.place( anchor='ne')
    a.pack(fill='both')
    frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    frame2 = tk.Frame(master=root, width=320, height=320, bg=Consts.COLOR_DIVIDER)
    image1 = Image.open('materna.jpeg')
    image1 = image1.resize((280,280))
    test = ImageTk.PhotoImage(image1)
    label1 = tk.Label(frame2, image=test)
    label1.image = test
    # Position image
    label1.place(x=20, y=20)
    frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    root.mainloop()

def main():
    first_screen()
    second_screen()
    third_screen()
    show_picture()



if __name__ == "__main__":
    main()