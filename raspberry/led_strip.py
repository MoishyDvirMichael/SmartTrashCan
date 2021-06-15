import time
import platform

if platform.system().lower().startswith('lin'):
    import board
    import neopixel

num_pixels = 31


class Led:
    pixels = None

    @classmethod
    def init(cls):
        if platform.system().lower().startswith('win'):
            return
        pixel_pin = board.D12
        ORDER = neopixel.GRB
        cls.pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)

    @classmethod
    def turn_off(cls, start:int = None, n: int = 1):
        if platform.system().lower().startswith('win'):
            return
        if start == None:
            cls.pixels[0:(num_pixels-1)] = (0, 0, 0)
        elif start < 0 or start >= num_pixels or n < 1 or start+n > num_pixels:
            return
        else:
            cls.pixels[start:(start + n - 1)] = (0, 0, 0)

    @classmethod
    def turn_on(cls, color, start:int = None, n:int = 1):
        if platform.system().lower().startswith('win'):
            return
        color = cls.hex2color(color)
        if start == None:
            cls.pixels[0:(num_pixels-1)] = color
        elif start < 0 or start >= num_pixels or n < 1 or start+n > num_pixels:
            return
        else:
            cls.pixels[start:(start + n - 1)] = color

    @classmethod
    def hex2color(cls, hex:str):
        if platform.system().lower().startswith('win'):
            return
        try: 
            color = hex.lstrip('#').lstrip('0x')
            return tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
        except:
            return (0, 0, 0)
