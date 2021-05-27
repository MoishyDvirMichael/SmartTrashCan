
# from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

'''
<color name="colorPrimary">#00BCD4</color>
<color name="colorPrimaryLight">#62efff</color>
<color name="colorPrimaryDark">#008ba3</color>
<color name="colorSecondary">#e040fb</color>
<color name="colorSecondaryLight">#ff79ff</color>
<color name="colorSecondaryDark">#aa00c7</color>
<color name="PrimaryTextColor">#212121</color>
<color name="SecondaryText">#757575</color>
<color name="DividerColor">#BDBDBD</color>
'''

COLOR_PRIMARY = '#00BCD4'
COLOR_PRIMARY_LIGHT = '#62efff'
COLOR_PRIMARY_DARK = '#008ba3'
COLOR_PRIMARY_TEXT = '#212121'
COLOR_SECONDARY = '#e040fb'
COLOR_SECONDARY_LIGHT = '#ff79ff'
COLOR_SECONDARY_DARK = '#aa00c7'
COLOR_SECONDARY_TEXT = '#757575'
COLOR_DIVIDER = '#BDBDBD'

SCREEN_SIZE = '480x320'

def first_screen():
    root = tk.Tk()
    # root.attributes("-fullscreen", True)
    a = tk.Label(root,
                 text ="Wellcome!",
                 font=("Arial Bold", 30),
                 bg=COLOR_PRIMARY,
                 fg=COLOR_PRIMARY_TEXT,
                 padx = 2,
                 pady = 2)
    a.config(anchor='center')
    a.pack(expand=True)
    b = tk.Label(root,
                 text ="Please enter a barcode.",
                 font=("Arial Bold", 20),
                 bg=COLOR_PRIMARY,
                 fg=COLOR_PRIMARY_TEXT,
                 padx = 2,
                 pady = 2)
    b.config(anchor='center')
    b.pack(expand=True)
    root.geometry(SCREEN_SIZE)
    root.configure(background=COLOR_PRIMARY)
    # btn = tk.Button(root, text="barcode is given")
    # btn.grid(column=1, row=0)
    root.mainloop()

def second_screen():
    root = tk.Tk()
    # root.attributes("-fullscreen", True)
    a = tk.Label(root,
                 text ="Thank you, please wait..",
                 font=("Arial Bold", 20),
                 bg=COLOR_SECONDARY,
                 fg=COLOR_SECONDARY_TEXT,
                 padx = 10,
                 pady = 5)
    a.config(anchor='center')
    a.pack(expand=True)
    root.geometry(SCREEN_SIZE)
    root.configure(background=COLOR_SECONDARY)
    # btn = tk.Button(root, text="barcode is given")
    # btn.grid(column=1, row=0)
    root.mainloop()

def show_picture():
    root = tk.Tk()
    root.geometry(SCREEN_SIZE)
    root.configure(background=COLOR_DIVIDER)
    frame1 = tk.Frame(master=root, width=160, height=320, bg=COLOR_DIVIDER)
    a = tk.Label(frame1,
                 text = "The list is updated saccessfully!",
                 font=("Arial Bold", 10),
                 bg=COLOR_DIVIDER,
                 fg=COLOR_PRIMARY_TEXT,
                 wraplength=150,
                 justify='left')
    a.place( anchor='ne')
    a.pack(fill='both')
    frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    frame2 = tk.Frame(master=root, width=320, height=320, bg=COLOR_DIVIDER)
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
    show_picture()



if __name__ == "__main__":
    main()