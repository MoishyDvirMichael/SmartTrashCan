import tkinter as tk
from consts import Consts
from image_conf import Image_to_show


class Result_screen(tk.Frame):
    """
    Class for the result screen in the application.
    It shows data about the prodact (name, image) and offer recycling bin color.
    """
    def __init__(self, master: tk.Tk):
        super().__init__(master, bg=Consts.COLOR_BG_RESULT)
        self.timeout = Consts.RESULT_TIMEOUT
        # Configure the result text.
        self.text_label = tk.Label(self,
                                   text="The list is updated saccessfully!",
                                   font=("Arial Bold", 10),
                                   bg=Consts.COLOR_BG_RESULT,
                                   fg=Consts.COLOR_TEXT_RESULT)
        self.text_label.grid()
        # Configure the image label.
        self.image_label = Image_to_show(master=self, url=None)
        self.image_label.show_image()
        # configure the recycling message.
        self.recycling_label = tk.Label(self,
                                        text="There is no data about recycling.",
                                        font=("Arial Bold", 10),
                                        bg=Consts.COLOR_BG_RESULT,
                                        fg=Consts.COLOR_TEXT_RESULT)
        self.recycling_label.grid()

    def show_screen(self):
        self.pack(expand=True)

    def hide_screen(self):
        self.pack_forget()
