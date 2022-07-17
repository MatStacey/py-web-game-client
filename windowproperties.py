

from PyQt5.QtGui import QIcon
import json, os

class WindowProperties():

    protocol = "https://"
    config_directory = os.path.dirname(__file__) + '/config'

    def __init__(self):
        window_properties_json = os.path.join(WindowProperties.config_directory, 'properties.json')
        with open(window_properties_json, 'r') as json_file:
            properties = json.load(json_file)
            self.app_name = properties['name']
            self.icon_file = properties['icon']
            self.min_window_size = properties['default_window_size']
            self.url = WindowProperties.protocol + properties['url']

    def get_name(self):
        return self.app_name

    def get_url(self):
        return self.url

    def get_icon(self):
        return self.icon_file

    def load_vk_code(self):
        vk_code_json_path = os.path.join(WindowProperties.config_directory, 'vk_code.json')
        with open(vk_code_json_path, 'r') as json_file:
            vk_code_map = json.load(json_file)
        return vk_code_map
    
    def set_window_properties(self, window):
        window.setWindowIcon(QIcon(self.get_icon()))
        window.setMinimumSize(self.min_window_size['width'], self.min_window_size['height'])
        return window