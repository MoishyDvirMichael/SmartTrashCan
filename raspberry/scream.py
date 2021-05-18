
# from tkinter import *
import tkinter as tk

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

def first_scream():
    root = tk.Tk()
    # root.attributes("-fullscreen", True)
    a = tk.Label(root,
                 text ="Wellcome, please enter a barcode.",
                 font=("Arial Bold", 30),
                 bg=COLOR_PRIMARY,
                 fg=COLOR_PRIMARY_TEXT,
                 padx = 10,
                 pady = 5)
    a.config(anchor='center')
    a.pack(expand=True)
    root.geometry("1000x500")
    root.configure(background=COLOR_PRIMARY)
    # btn = tk.Button(root, text="barcode is given")
    # btn.grid(column=1, row=0)
    root.mainloop()

def second_scream():
    root = tk.Tk()
    # root.attributes("-fullscreen", True)
    a = tk.Label(root,
                 text ="Thank you, please wait..",
                 font=("Arial Bold", 30),
                 bg=COLOR_SECONDARY,
                 fg=COLOR_SECONDARY_TEXT,
                 padx = 10,
                 pady = 5)
    a.config(anchor='center')
    a.pack(expand=True)
    root.geometry("1000x500")
    root.configure(background=COLOR_SECONDARY)
    # btn = tk.Button(root, text="barcode is given")
    # btn.grid(column=1, row=0)
    root.mainloop()

def ask_picture():
    pass
    '''
    root = tk.Tk()
    # root.attributes("-fullscreen", True)
    a = tk.Label(root,
                 text ="Wellcome, please give a barcode",
                 font=("Arial Bold", 10),
                 bg='red',
                 fg='#00BCD4',
                 padx = 10,
                 pady = 5)
    a.pack()
    root.geometry("1200x600")
    root.configure(background="red")
    # btn = tk.Button(root, text="barcode is given")
    # btn.grid(column=1, row=0)
    root.mainloop()
    '''

def present_picture():
    pass
    '''
    root = tk.Tk()
    # root.attributes("-fullscreen", True)
    a = tk.Label(root,
                 text ="Thank you, please wait",
                 font=("Arial Bold", 10),
                 bg='blue',
                 fg='#e040fb',
                 padx = 10,
                 pady = 5)
    a.pack()
    root.geometry("1200x600")
    root.configure(background="blue")
    # btn = tk.Button(root, text="barcode is given")
    # btn.grid(column=1, row=0)
    root.mainloop()
    '''

def main():
    first_scream()
    second_scream()



if __name__ == "__main__":
    main()