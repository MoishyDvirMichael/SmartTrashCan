import tkinter as tk
from PIL import Image, ImageTk
# from urllib2 import urlopen
from io import BytesIO
from consts import Consts


class Image_to_show(tk.Label):
    """
    Class for configuration of the picture result.
    """
    def __init__(self, master: tk.Frame, url=None):
        """
        if url == None:
            image_file = 'default_image.png'
        else:
            u = urlopen(url)
            raw_data = u.read()
            u.close()
            image_file = BytesIO(raw_data)
        """
        image_file = 'default_image.png'
        image = Image.open(image_file)
        image = image.resize(Consts.RESULT_IMAGE_SIZE)
        test = ImageTk.PhotoImage(image)
        super().__init__(master, image=test)
        self.image = test
    

    def show_image(self):
        self.grid()
    
    def hide_image(self):
        self.grid_forget()
