import tkinter as tk
from consts import Consts
from image_conf import Image_to_show


class ResultScreen(tk.Frame):
    """
    Class for the result screen in the application.
    It shows data about the prodact (name, image) and offer recycling bin color.
    """
    def __init__(self, master: tk.Tk, color=None, url=None, name='<name>'):
        super().__init__(master, bg=Consts.COLOR_BG_RESULT)
        # Configure the result text.
        if name == None:
            name = ''
        self.text_label = tk.Label(self,
                                   text=f'The {name} prodact added to the shop list!',
                                   font=("Arial Bold", 10),
                                   bg=Consts.COLOR_BG_RESULT,
                                   fg=Consts.COLOR_TEXT_RESULT)
        self.text_label.grid()
        # Configure the image label.
        self.image_label = Image_to_show(master=self, url=url)
        self.image_label.show_image()
        # configure the recycling message.
        if not color == None:
            result_text = f'This prodact should be put into {color} recycling bin'
        else:
            result_text = "There is no data about recycling."
        self.recycling_label = tk.Label(self,
                                        text=result_text,
                                        font=("Arial Bold", 10),
                                        bg=Consts.COLOR_BG_RESULT,
                                        fg=Consts.COLOR_TEXT_RESULT)
        self.recycling_label.grid()

    def show_screen(self):
        self.pack(expand=True)

    def hide_screen(self):
        self.pack_forget()

    def update_result(self, name, color, image_url=None):
        if name == None:
            name = ''
        self.text_label['text'] = f'The {name} product added to the shop list!'
        self.image_label.hide_image()
        self.image_label = Image_to_show(master=self, url=image_url)
        self.image_label.show_image()
        if not color == None:
            self.recycling_label['fg'] = color
            self.recycling_label['text'] = f'This prodact should be put into {color} recycling bin'
        else:
            self.recycling_label['text'] = "There is no data about recycling."
        
