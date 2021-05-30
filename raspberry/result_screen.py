import tkinter as tk
from PIL import Image, ImageTk
from consts import Consts


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
        image = Image.open('default_image.png')
        image = image.resize((250,250))
        test = ImageTk.PhotoImage(image)
        self.image_label = tk.Label(self, image=test)
        self.image_label.image = test
        self.image_label.grid()
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

    def update_text(self, text):
        self.my_label['text'] = text
