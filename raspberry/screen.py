
from consts import Consts
import tkinter as tk
from PIL import Image, ImageTk


def first_screen():
    root = tk.Tk()
    # root.attributes("-fullscreen", True)
    a = tk.Label(root,
                 text ="Wellcome!",
                 font=("Arial Bold", 30),
                 bg=Consts.COLOR_PRIMARY,
                 fg=Consts.COLOR_PRIMARY_TEXT,
                 padx = 2,
                 pady = 2)
    a.config(anchor='center')
    a.pack(expand=True)
    b = tk.Label(root,
                 text ="Please enter a barcode.",
                 font=("Arial Bold", 20),
                 bg=Consts.COLOR_PRIMARY,
                 fg=Consts.COLOR_PRIMARY_TEXT,
                 padx = 2,
                 pady = 2)
    b.config(anchor='center')
    b.pack(expand=True)
    root.geometry(Consts.SCREEN_SIZE)
    root.configure(background=Consts.COLOR_PRIMARY)
    # btn = tk.Button(root, text="barcode is given")
    # btn.grid(column=1, row=0)
    root.mainloop()

def second_screen():
    root = tk.Tk()
    # root.attributes("-fullscreen", True)
    a = tk.Label(root,
                 text ="Thank you, please wait..",
                 font=("Arial Bold", 20),
                 bg=Consts.COLOR_SECONDARY,
                 fg=Consts.COLOR_SECONDARY_TEXT,
                 padx = 10,
                 pady = 5)
    a.config(anchor='center')
    a.pack(expand=True)
    root.geometry(Consts.SCREEN_SIZE)
    root.configure(background=Consts.COLOR_SECONDARY)
    # btn = tk.Button(root, text="barcode is given")
    # btn.grid(column=1, row=0)
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
    show_picture()



if __name__ == "__main__":
    main()