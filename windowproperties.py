from PyQt5.QtGui import QIcon
import json, os
from PyQt5.QtCore import QUrl

class WindowProperties():

    protocol = "https://"
    config_directory = os.path.dirname(__file__) + "/config"
    config = "properties.json"

    @staticmethod
    def load_from_json(file):
        window_properties_json = os.path.join(WindowProperties.config_directory, file)
        with open(window_properties_json, 'r') as json_file:
            properties = json.load(json_file)
            return WindowProperties(properties['name'], properties['icon'], properties['default_window_size'], properties['url'])

    def __init__(self, name, icon, size, url):
        self.app_name = name
        self.icon_file = icon
        self.min_window_size = size
        self.url = url

    def get_url(self):
        return QUrl(WindowProperties.protocol + self.url)
    
    def set_window_properties(self, window):
        window.setWindowIcon(QIcon(self.icon_file))
        window.setMinimumSize(640, 480)
        window.resize(self.min_window_size['width'], self.min_window_size['height'])
        window.browser = None
        window.showNormal()
        return window
