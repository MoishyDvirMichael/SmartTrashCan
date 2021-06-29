import platform
from bidi import algorithm as bidialg

class Consts:
    """
    class for all constants application needs.
    """
    @classmethod
    def convert_color_to_tkinter(cls, color):
        if color == None:
            return None
        return color.replace('0x', '#')
    
    @classmethod
    def reverse_hebrew_words(cls, text):
        return bidialg.get_display(text) if platform.system().lower().startswith('lin') else text


    
    DEFAULT_RECYCLING_BIN_TYPE = {'name':'unknown', 'color_name':'white', 'color_hex':'#FFFFFF'}

    DATABASE_TIMEOUT = 5

    # size of raspberry screen.
    SCREEN_SIZE = '480x320'
    FULLSCREEN_DEFAULT_STATE = True
    
    # size of result image in pixels.
    IMAGE_HEIGHT_SIZE = 250
    IMAGE_WIDTH_SIZE = 250
    RESULT_IMAGE_SIZE = (IMAGE_WIDTH_SIZE, IMAGE_HEIGHT_SIZE)

    # size of result screen texts in pixels.
    RESULT_TEXTS_WIDTH = 180
    RESULT_TEXTS_WIDTH_PAD = 6
    RESULT_NAME_WIDTH = (RESULT_TEXTS_WIDTH + 2 * RESULT_TEXTS_WIDTH_PAD + IMAGE_WIDTH_SIZE)

    # The timeout use operator 'after' that schedules a function to be called
    # after a specified time in milliseconds, so this macro translates it.
    SECOND = 1000 
    # number of seconds the result/error are presented in the screem.
    RESULT_TIMEOUT = 5 * SECOND
    ERROR_TIMEOUT = 10

    # colors for Recycling Bin types. 
    PLASTIC_RECYCLING_BIN_COLOR = 'orange'
    PAPER_RECYCLING_BIN_COLOR = 'blue'
    CANS_RECYCLING_BIN_COLOR = 'grey'
    GLASS_RECYCLING_BIN_COLOR = 'green'

    # colors for the background screens.
    COLOR_BG_INTENET_CONNECT = '#00BCD4'
    COLOR_BG_QR_SCAN = '#00ff00'
    COLOR_BG_WELCOME = '#00BCD4'
    COLOR_BG_WAITING = '#00BCD4'
    COLOR_BG_ERROR = '#212121'
    COLOR_BG_RESULT = '#BDBDBD'
    COLOR_BG_NO_RECYCLING_INFO = '#212121'

    # colors for the background screens.
    COLOR_TEXT_INTENET_CONNECT = '#212121'
    COLOR_TEXT_QR_SCAN = '#212121'
    COLOR_TEXT_WELCOME = '#212121'
    COLOR_TEXT_WAITING = '#212121'
    COLOR_TEXT_RESULT = '#212121'
    COLOR_TEXT_ERROR = 'red'

    '''
    colors from application:
    <color name="colorPrimary">#00BCD4</color>
    <color name="colorPrimaryLight">#62efff</color>
    <color name="colorPrimaryDark">#008ba3</color>
    <color name="colorSecondary">#e040fb</color>
    <color name="colorSecondaryLight">#ff79ff</color>
    <color name="colorSecondaryDark">#aa00c7</color>
    <color name="PrimaryTextColor">#212121</color>
    <color name="SecondaryText">#757575</color>
    <color name="DividerColor">#BDBDBD</color>
    '''
    # colors from application as python macros.
    COLOR_PRIMARY = '#00BCD4'
    COLOR_PRIMARY_LIGHT = '#62efff'
    COLOR_PRIMARY_DARK = '#008ba3'
    COLOR_PRIMARY_TEXT = '#212121'
    COLOR_SECONDARY = '#e040fb'
    COLOR_SECONDARY_LIGHT = '#ff79ff'
    COLOR_SECONDARY_DARK = '#aa00c7'
    COLOR_SECONDARY_TEXT = '#757575'
    COLOR_DIVIDER = '#BDBDBD'
