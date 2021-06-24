import tkinter as tk
from PIL import Image, ImageTk
from urllib.request import urlopen, Request
from io import BytesIO
from consts import Consts


class Image_to_show(tk.Label):
    """
    Class for configuration of the picture result.
    """
    def __init__(self, master: tk.Frame, url=None):
        try:
            if url == None:
                image_file = 'default_image.png'
            else:
                req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                u = urlopen(req)
                raw_data = u.read()
                u.close()
                image_file = BytesIO(raw_data)
        except:
            image_file = 'default_image.png'

        image = Image.open(image_file)
        image = image.resize(Consts.RESULT_IMAGE_SIZE)
        test = ImageTk.PhotoImage(image)
        super().__init__(master, image=test)
        self.image = test
    

    def show_image(self):
        self.grid(row=0, column=1, columnspan=2, rowspan=2, padx=0)
    
    def hide_image(self):
        self.grid_forget()
