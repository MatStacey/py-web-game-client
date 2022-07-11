

from PyQt5.QtGui import QIcon
import json, os

class WindowProperties():

    protocol = "https://"
    flyff_url = "universe.flyff.com/play"

    def __init__(self, url):
        if not url or url.strip() == "":
            url = WindowProperties.flyff_url
            
        self.url = WindowProperties.protocol + url
        self.app_name = "pyFlyffClient"
        self.icon_file = "icons/PyFlyff.ico"
        self.min_window_size = { "width" : 640, "height" : 480 }

    def get_name(self):
        return self.app_name

    def get_url(self):
        return self.url

    def get_icon(self):
        return self.icon_file

    def load_vk_code(self):
        config_directory = os.path.dirname(__file__) + '/config'
        vk_code_json_path = os.path.join(config_directory, 'vk_code.json')
        with open(vk_code_json_path, 'r') as json_file:
            vk_code_map = json.load(json_file)
        return vk_code_map
    
    def set_window_properties(self, window):
        window.browser = None
        window.setWindowIcon(QIcon(self.get_icon()))
        window.setMinimumSize(self.min_window_size['width'], self.min_window_size['height'])
        return window