import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('480x320')
        
        self.screen1 = Screen(self, text='screen 1')
        self.screen2 = Screen(self, text='screen 2')


    def run(self):
        # self.screen1.show_screen()
        # self.is_screen1 =True
        # self.bind('<Return>', self.func1)
        self.mainloop()

    def func1(self, event):
        # if self.is_screen1:
        #     self.screen1.hide_screen()
        #     self.screen2.show_screen()
        #     self.is_screen1 = False
        # else:
        #     self.screen2.hide_screen()
        #     self.screen1.show_screen()
        #     self.is_screen1 = True
        pass
    
    

class Screen(tk.Frame):
    def __init__(self, master: tk.Tk, text):
        super().__init__(master)
        # self.my_label = tk.Label(self, text = text) 
        # self.my_label.grid(row=0)

    def show_screen(self):
        self.pack(expand=True)

    def hide_screen(self):
        self.pack_forget()

    def update_text(self, text):
        # self.my_label['text'] = text
        pass


if __name__ == "__main__":
    app = Application()
    app.run()
