import json
import tkinter as tk

from consts import Consts
from database import DB
from led_strip import Led
from screens.screens import *
from connect_to_wifi import ConnectToWifi



class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self._data = self.read_data_from_file()

        DB.init()
        Led.init()
        
        self.geometry(Consts.SCREEN_SIZE)
        self.fullscreen_state = Consts.FULLSCREEN_DEFAULT_STATE
        self.bind("<F11>", self.toggle_fullscreen)
        self.bind("<Escape>", self.end_fullscreen)
        
        self.configure(background=Consts.COLOR_BG_WELCOME)

        self.scan_init_data_screen = ScanInitDataScreen(master=self)
        self.trying_to_connect_screen = TryingToConnectScreen(master=self)
        self.welcome_screen = WelcomeScreen(master=self)
        self.waiting_screen = WaitingScreen(master=self)
        self.error_screen = ErrorScreen(master=self)
        self.result_screen = ResultScreen(master=self)
        self.empty_screen = EmptyScreen()

        self.current_screen = self.empty_screen

    def run(self):
        self.change_screen(self.trying_to_connect_screen)
        self.mainloop()

    def change_screen(self, new_screen, *arg):
        def screen_name(screen):
            long_name = f'{type(screen)}'
            return long_name.split("'")[1].split(".")[-1]
        print(f'Screen: {screen_name(self.current_screen)}\t->\t{screen_name(new_screen)}')
        self.current_screen.hide_screen()
        self.current_screen = new_screen
        self.current_screen.show_screen(*arg)
        self.update()
        

    def read_data_from_file(self):
        try:
            file = open('data.json')
            file_text = file.read()
            file.close()
            data = json.loads(file_text)
            print(data)
            return data
        except:
            file.close()
            return {'uid': '', 'wifi': []}

    def get_data(self):
        return self._data

    def update_data(self, data: dict):
        self._data['uid'] = data['uid']
        self._data['wifi'].append({'name': data['wifi_name'], 'password': data['wifi_password']})
        with open('data.json', 'w') as fp:
            json.dump(self._data, fp)

    def get_data(self):
        return self._data

    def update_data(self, data: dict):
        self._data['uid'] = data['uid']
        self._data['wifi'].append({'name': data['wifi_name'], 'password': data['wifi_password']})
        with open('data.json', 'w') as fp:
            json.dump(self._data, fp)
        ConnectToWifi.connect(data['wifi_name'], data['wifi_password'])

    def get_uid(self):
        return self._data['uid']
    
    def get_wifi_length(self):
        return len(self._data['wifi'])

    def toggle_fullscreen(self, event=None):
        self.fullscreen_state = not self.fullscreen_state  # Just toggling the boolean
        self.attributes("-fullscreen", self.fullscreen_state)

    def end_fullscreen(self, event=None):
        self.fullscreen_state = False
        self.attributes("-fullscreen", self.fullscreen_state)

def main():
    app = Application()
    app.run()


if __name__ == "__main__":
    main()
