import tkinter as tk
from consts import Consts
from image_conf import Image_to_show
from database import DB
from led_strip import Led
from tkinter import font as tkFont


def calculates_width_pad_for_name(name):
    """
    Calculates the number of pixels need to pad in sides of product name.
    It calculates the number of pixels in the name and subtracts it from the total number of pixels.
    Because it is lined on both sides, each side is lined with half of it.
    """
    name_font = tkFont.Font(family='Arial', size=15, weight='bold')
    pixel_of_width_name = name_font.measure(name)
    return (Consts.RESULT_NAME_WIDTH - pixel_of_width_name) / 2


class ResultScreen(tk.Frame):
    """
    Class for the result screen in the application.
    It shows data about the prodact (name, image) and offer recycling bin color.
    """
    def __init__(self, master: tk.Tk, color=None, url=None, name=None):
        super().__init__(master, bg=Consts.COLOR_BG_RESULT)
        self.bg_color = Consts.COLOR_BG_RESULT if color == None else color
        # Configure name text.
        if name == None:
            name = '<Name>'
        hebrew_name = Consts.reverse_hebrew_words(name)
        pad_length = calculates_width_pad_for_name(name=hebrew_name)
        self.name_label = tk.Label(self,
                                   text=f'{hebrew_name}',
                                   font=("Arial Bold", 15),
                                   bg=Consts.COLOR_BG_RESULT,
                                   fg=Consts.COLOR_TEXT_RESULT)
        self.name_label.grid(columnspan=3, ipadx=pad_length, pady=0)
        # Configure the result text.
        self.text_label = tk.Label(self,
                                   text='This product was successfully added to your shopping list!',
                                   font=("Arial Bold", 13),
                                   bg=Consts.COLOR_BG_RESULT,
                                   fg=Consts.COLOR_TEXT_RESULT,
                                   wraplength=Consts.RESULT_TEXTS_WIDTH)
        self.text_label.grid(row=1, padx=Consts.RESULT_TEXTS_WIDTH_PAD, pady=10)
        # Configure the image label.
        self.image_label = Image_to_show(master=self, url=url)
        self.image_label.show_image()
        
        self.recycling_label = tk.Label(self,
                                        text= 'There is no data about recycling' if color == None else f'This product should be put into the {color} recycling bin',
                                        font=("Arial Bold", 12),
                                        bg=Consts.COLOR_BG_RESULT,
                                        fg=Consts.COLOR_TEXT_RESULT,
                                        wraplength=Consts.RESULT_TEXTS_WIDTH)
        self.recycling_label.grid(row=2, column=0, padx=Consts.RESULT_TEXTS_WIDTH_PAD, pady=15)

    def show_screen(self):
        self.master.configure(background=self.bg_color)
        self.pack(expand=True)
        self.master.after(Consts.RESULT_TIMEOUT, self.master.change_screen, self.master.welcome_screen)

    def hide_screen(self):
        self.pack_forget()
        self.bg_color = Consts.COLOR_BG_RESULT

    def update_result(self, name, recycling_bin_type, image_url=None):
        # Reconfigure name text.
        if name == None:
            name = ''
        hebrew_name = Consts.reverse_hebrew_words(name)
        self.name_label['text'] = f'{hebrew_name}'
        self.name_label.grid_forget()
        pad_length = calculates_width_pad_for_name(name=hebrew_name)
        self.name_label.grid(row=0, columnspan=3, ipadx=pad_length, pady=0)
        # Reconfigure the image label.
        self.image_label.hide_image()
        self.image_label = Image_to_show(master=self, url=image_url)
        self.image_label.show_image()
        # Reconfigure the recycling message.
        if recycling_bin_type == None or recycling_bin_type.get('name') == 'unknown':
            self.bg_color = Consts.COLOR_BG_NO_RECYCLING_INFO
            self.recycling_label['text'] = "There is no data about recycling"
        else:
            self.bg_color = recycling_bin_type.get('color_hex')
            self.recycling_label['text'] = f'This product should be put into the {recycling_bin_type.get("color_name")} recycling bin'
    
    def update_product_details(self, doc):
        product = DB.get_product(doc._data.get('product_id'))
        recycling_bin_type = DB.get_recycling_bin_type(product.get('recycling_bin_type')) # TODO what if it's not defined?
        if recycling_bin_type.get('name') != 'unknown':
            Led.turn_on(recycling_bin_type['color_hex'])
        self.master.result_screen.update_result(name=product.get('name'), recycling_bin_type=recycling_bin_type, image_url=product.get('image'))
        pass
