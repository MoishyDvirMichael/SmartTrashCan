import tkinter as tk

class MyObj(object): pass

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        # self.create_widgets()
        self.first_screen()
        self.second_screen()

    def first_screen(self):
        self._first_screen = MyObj()
        self._first_screen.frame = tk.Frame(self.master)
        self._first_screen.a = tk.Label(self._first_screen.frame, text='first screen')
        self._first_screen.a.grid(row=0)
        self._first_screen.frame.pack(expand=True)
        # self._first_screen.barcode = tk.StringVar()
        # self._first_screen.name_entry = tk.Entry(self.master, textvariable=self._first_screen.barcode)
        # self._first_screen.name_entry.grid(row=1,in_=self._first_screen.frame)
        # self._first_screen.name_entry.lower(self._first_screen.frame)
    
    def second_screen(self, barcode=None):
        self._second_screen = MyObj()
        self._second_screen.frame = tk.Frame(self.master)
        # self._second_screen.a = tk.Label(self._second_screen.frame, text =f'Barcode is {self._first_screen.barcode.get()}')
        self._second_screen.b = tk.Label(self._second_screen.frame, text =f'second screen')
        self._second_screen.b.grid(row=0)
        # self._second_screen.frame.pack(expand=True)

root = tk.Tk()
root.geometry('480x320')

def func1(event):
    root.unbind('<Return>')
    # app._second_screen.b['text']=f'Barcode is {app._first_screen.barcode.get()}Thank you, please wait..'
    app._first_screen.frame.pack_forget()
    app._second_screen.frame.pack(expand=True)
    # app._first_screen.name_entry.grid_forget()
    # app._first_screen.name_entry.lower(app._first_screen.frame)
    print("func1")
    root.bind('<Return>', func2)
def func2(event):
    root.unbind('<Return>')
    # app._first_screen.frame.pack(expand=True)
    # app._first_screen.name_entry.grid(row=1)
    # app._first_screen.name_entry.lift(app._first_screen.frame)
    app._second_screen.frame.pack_forget()
    app._first_screen.frame.pack(expand=True)
    print("func2")
    root.bind('<Return>', func1)
def func3(event):
    print(f'barcode: {app._first_screen.barcode.get()}')

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.frame = tk.Frame(self)
        self.frame.pack(side="top", fill="both", expand=True)
        self.label = tk.Label(self, text="Hello, world")
        button1 = tk.Button(self, text="Click to hide label",
                           command=self.hide_label)
        button2 = tk.Button(self, text="Click to show label",
                            command=self.show_label)
        self.label.grid(row=0,in_=self.frame)
        button1.grid(row=1,in_=self.frame)
        button2.grid(row=2,in_=self.frame)

    def show_label(self, event=None):
        self.label.lift(self.frame)

    def hide_label(self, event=None):
        self.label.lower(self.frame)

if __name__ == "__main__":
    # app = SampleApp()
    # app.mainloop()
    # exit()
    root.bind('<Return>', func1)
    root.bind('<space>', func3)

    app = Application(master=root)
    # app._first_screen.name_entry.focus()
    app.mainloop()
