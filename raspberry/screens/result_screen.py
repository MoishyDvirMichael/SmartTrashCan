import tkinter as tk
from consts import Consts
from image_conf import Image_to_show
from database import DB
from led_strip import Led
from bidi import algorithm as bidialg


class ResultScreen(tk.Frame):
    """
    Class for the result screen in the application.
    It shows data about the prodact (name, image) and offer recycling bin color.
    """
    def __init__(self, master: tk.Tk, color=None, url=None, name=None):
        super().__init__(master, bg=Consts.COLOR_BG_RESULT)
        self.bg_color = Consts.COLOR_BG_RESULT if color == None else color
        # Configure the result text.
        if name == None:
            name = '<Name>'
        self.text_label = tk.Label(self,
                                   text=f'{name}\nwas successfully added to your shopping list!',
                                   font=("Arial Bold", 13),
                                   bg=Consts.COLOR_BG_RESULT,
                                   fg=Consts.COLOR_TEXT_RESULT,
                                   wraplength=150)
        self.text_label.grid(padx=10, pady=10)
        # Configure the image label.
        self.image_label = Image_to_show(master=self, url=url)
        self.image_label.show_image()
        # configure the recycling message.
        if not color == None:
            result_text = f'This product should be put into the {color} recycling bin'
        else:
            result_text = "There is no data about recycling."
        self.recycling_label = tk.Label(self,
                                        text=result_text,
                                        font=("Arial Bold", 12),
                                        bg=Consts.COLOR_BG_RESULT,
                                        fg=Consts.COLOR_TEXT_RESULT,
                                        wraplength=150)
        self.recycling_label.grid(row=1, column=0, padx=10, pady=15)

    def show_screen(self):
        self.master.configure(background=self.bg_color)
        self.pack(expand=True)
        self.master.after(Consts.RESULT_TIMEOUT, self.master.change_screen, self.master.welcome_screen)

    def hide_screen(self):
        self.pack_forget()
        self.bg_color = Consts.COLOR_BG_RESULT

    def update_result(self, name, recycling_bin_type, image_url=None):
        if name == None:
            name = ''
        self.text_label['text'] = f'{name}\nwas successfully added to your shopping list!'
        self.image_label.hide_image()
        self.image_label = Image_to_show(master=self, url=image_url)
        self.image_label.show_image()
        if not recycling_bin_type == None:
            self.bg_color = recycling_bin_type.get('color_hex')
            self.recycling_label['text'] = f'This product should be put into the {recycling_bin_type.get("color_name")} recycling bin'
        else:
            self.recycling_label['text'] = "There is no data about recycling."
    
    def update_product_details(self, doc):
        product = DB.get_product(doc._data.get('product_id'))
        recycling_bin_type = DB.get_recycling_bin_type(product.get('recycling_bin_type')) # TODO what if it's not defined?
        Led.turn_on(recycling_bin_type['color_hex'])
        self.master.result_screen.update_result(name=product.get('name'), recycling_bin_type=recycling_bin_type, image_url=product.get('image'))
        pass
